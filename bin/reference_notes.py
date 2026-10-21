"""Expand manually curated references from official snapshot text, without stored answers.

Each Markdown note has a JSON `match_all:` list and {{quote: slug | literal}}
markers. Only matching raw lines and their source identity are emitted. Missing or
ambiguous documents/quotes warn and never silently become evidence.
"""
import json
import pathlib
import re

MARKER = re.compile(r"\{\{quote:\s*([^|{}]+)\|([^{}]+)\}\}")


def expand(root, query, docs, validate=False):
    root = pathlib.Path(root)
    output, errors = [], []
    by_slug = {}
    for doc in docs:
        by_slug.setdefault(doc.get("slug"), []).append(doc)
    for note in sorted((root / "notes").glob("*.md")):
        text = note.read_text()
        match = re.search(r"(?m)^match_all:\s*(\[.*\])$", text)
        if not match:
            continue
        patterns = json.loads(match[1])
        selected = all(re.search(p, query, re.I) for p in patterns)
        if not selected and not validate:
            continue
        rows, seen, last_context = [], set(), None
        for slug, literal in MARKER.findall(text):
            candidates = by_slug.get(slug.strip(), [])
            if len(candidates) != 1:
                errors.append(f"{note.name}: document missing or ambiguous: {slug.strip()}")
                continue
            doc = candidates[0]
            try:
                lines = (root / doc["local_path"]).read_text().splitlines()
            except OSError:
                errors.append(f"{note.name}: source file missing: {slug.strip()}")
                continue
            hits = [(i, line) for i, line in enumerate(lines) if literal.strip() in line]
            if not hits:
                errors.append(f"{note.name}: quote missing: {slug.strip()} | {literal.strip()}")
                continue
            # Quote strings must identify one official row; duplicates within SDK
            # examples cannot silently select one out of conflicting occurrences.
            if len(hits) != 1:
                errors.append(f"{note.name}: quote ambiguous: {slug.strip()} | {literal.strip()}")
                continue
            i, line = hits[0]
            key = (doc["source_url"], i)
            if key in seen:
                continue
            seen.add(key)
            # Markdown examples may themselves contain headings. Track the real
            # section hierarchy outside fenced code, including level 4+ types.
            headings, fence = [], None
            for previous in lines[:i]:
                opened = re.match(r"\s*(`{3,}|~{3,})", previous)
                if opened:
                    marker = opened[1]
                    if fence is None:
                        fence = marker
                    elif marker[0] == fence[0] and len(marker) >= len(fence):
                        fence = None
                    continue
                heading = re.match(r"^(#{1,6})\s+", previous)
                if heading and fence is None:
                    depth = len(heading[1])
                    headings = [h for h in headings if len(h) - len(h.lstrip('#')) < depth]
                    headings.append(previous)
            scope = " / ".join(doc.get("breadcrumb") or [])
            context = (doc["source_url"], tuple(headings[-2:]))
            if context != last_context:
                rows.append(f"[{doc['title']} · {scope} · {' / '.join(x.lstrip('# ') for x in headings[-2:])}]\n"
                            f"source_url: {doc['source_url']} · updated_at: {doc.get('updated_at', '')}")
                last_context = context
            if line.lstrip().startswith('|'):
                start, end = i, i + 1
                while start and lines[start - 1].lstrip().startswith('|'):
                    start -= 1
                while end < len(lines) and lines[end].lstrip().startswith('|'):
                    end += 1
                table = "\n".join(lines[start:end])
                if any(re.search(r'\|\s*(?:Object|Array|Map|List)', row, re.I) for row in lines[start:end]):
                    if len(table) <= 4200:
                        table_key = (doc['source_url'], start, end)
                        if table_key not in seen:
                            seen.add(table_key)
                            rows.append(table)
                    else:
                        rows.extend(lines[start:start + 2])
                        rows.append('[nested table not expanded; complete source: ' + doc['source_url'] + ']')
                else:
                    rows.extend(lines[start:start + 2])
                    rows.append(line)
            else:
                rows.append(line)
        if selected and rows:
            output.extend(rows)
    if not output and not errors:
        return "", errors
    header = "== 定位字段的原文摘录 ==\ncoverage: literal source rows with document and heading scope; excerpt only"
    warnings = ["⚠补充依据待复核，不得据此下结论：" + x for x in errors]
    return header + "\n" + "\n".join(output + warnings), errors


if __name__ == "__main__":
    import sys
    root = pathlib.Path(sys.argv[1])
    docs = [json.loads(line) for line in (root / "meta/documents.jsonl").read_text().splitlines()]
    _, errors = expand(root, "", docs, validate=True)
    print(json.dumps({"invalid_refs": errors}, ensure_ascii=False))
    sys.exit(bool(errors))
