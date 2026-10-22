"""Expand manually curated references from official snapshot text, without stored answers.

Each Markdown note has a JSON `match_all:` list and {{quote: slug | literal}}
markers. Complete matching raw blocks and their source identity are emitted. Missing or
ambiguous documents/quotes warn and never silently become evidence.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import evidence_sections

MARKER = re.compile(r"\{\{quote:\s*([^|{}]+)\|([^{}]+)\}\}")


def expand(root, query, docs, validate=False):
    root = pathlib.Path(root)
    output, errors, seen = [], [], set()
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
        rows = []
        for slug, literal in MARKER.findall(text):
            candidates = by_slug.get(slug.strip(), [])
            if len(candidates) != 1:
                errors.append(f"{note.name}: document missing or ambiguous: {slug.strip()}")
                continue
            doc = candidates[0]
            try:
                with (root / doc["local_path"]).open(encoding="utf-8", newline="") as handle:
                    source_text = handle.read()
                lines = source_text.splitlines()
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
            block = evidence_sections.literal_block(source_text, i + 1)
            scope = " / ".join(doc.get("breadcrumb") or [])
            context = (f"[{doc['title']} · {scope} · "
                       + " / ".join(x.lstrip('# ') for x in block['scope'][-2:]) + "]\n"
                       + f"source_url: {doc['source_url']} · updated_at: {doc.get('updated_at', '')}\n")
            unit = evidence_sections.source_unit(context + block['body'], [doc['source_url']],
                version=doc.get('updated_at', ''), scope=block['scope'])
            if selected and unit not in seen:
                seen.add(unit)
                rows.append(unit)
        if selected and rows:
            output.extend(rows)
    if not output and not errors:
        return "", errors
    header = "== 定位字段的原文摘录 ==\ncoverage: literal source blocks with document and heading scope; excerpt only"
    warnings = ["⚠补充依据待复核，不得据此下结论：" + x for x in errors]
    return header + "\n" + "\n".join(output + warnings), errors


if __name__ == "__main__":
    import sys
    root = pathlib.Path(sys.argv[1])
    docs = [json.loads(line) for line in (root / "meta/documents.jsonl").read_text().splitlines()]
    _, errors = expand(root, "", docs, validate=True)
    print(json.dumps({"invalid_refs": errors}, ensure_ascii=False))
    sys.exit(bool(errors))
