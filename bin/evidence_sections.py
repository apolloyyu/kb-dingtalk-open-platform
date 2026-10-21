"""Select complete Markdown evidence units. Pure stdlib, no I/O or model calls.

The identical module is shipped by both KB adapters. Its content hash is checked
by the cross-repository acceptance script; product facts belong to the sources.
"""
import math
import re

FACETS = (
    ('有效期', '时效', '过期', '失效'),
    ('上限', '最多', '限额', '配额', '限制'),
    ('权限', '授权', '可见', '访问控制'),
)


def previous_questions(text):
    """Role-labelled history: answers are not new user subject declarations.

    Unlabelled legacy input is preserved byte-for-byte. Full source history is
    retained by the caller; this projection is used only for retrieval subjects.
    """
    labels = list(re.finditer(r'(?m)^(用户|助理|User|Assistant)[:：]\s*', text))
    if len(labels) < 2 or labels[0].start() != 0:
        return text
    users = []
    for i, match in enumerate(labels):
        end = labels[i + 1].start() if i + 1 < len(labels) else len(text)
        if match[1] in ('用户', 'User'):
            users.append(text[match.end():end].strip())
    return '\n\n'.join(users)


def facets(query):
    return [group for group in FACETS if any(term in query.lower() for term in group)]


def relevance(text, query):
    low = text.lower().replace('\\_', '_')
    return (sum(20 for group in facets(query) if any(term in low for term in group))
            + sum(min(len(w), 8) for w in query_terms(query) if w in low))


def units(text):
    """Heading-aware units with ancestor scope; headings inside fences are data."""
    lines = text.splitlines(keepends=True)
    start = 0
    if lines and lines[0].strip() == '---':
        end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == '---'), None)
        if end is not None:
            start = end + 1
    result, ancestors, block, fence = [], [], [], None
    begin = start + 1

    def flush():
        if ''.join(block).strip():
            result.append({'line': begin, 'scope': [x[1] for x in ancestors],
                           'body': ''.join(block).strip()})

    for index in range(start, len(lines)):
        line = lines[index]
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            block.append(line)
            continue
        heading = re.match(r'^(#{1,6})\s+(.+)', line) if fence is None else None
        if heading:
            flush()
            depth = len(heading[1])
            ancestors = [x for x in ancestors if x[0] < depth] + [(depth, line.strip())]
            block = []
            begin = index + 2
        else:
            block.append(line)
    flush()
    return result


def query_terms(query, symbols=()):
    low = query.lower()
    words = set(re.findall(r'[a-z][a-z0-9_.+/-]{1,}', low))
    for part in re.findall(r'[一-鿿]+', low):
        for size in (2, 3, 4):
            words.update(part[i:i + size] for i in range(len(part) - size + 1))
    words.difference_update({'什么', '怎么', '如何', '可以', '是否', '这个', '那个', '钉钉', '请问'})
    words.update(term for group in facets(query) for term in group)
    return words | {s.lower() for s in symbols if s}


def select(text, query, budget, symbols=()):
    """Keep complete source units; never cut a table, code fence or a URL.

    Oversized sections become explicitly partial projections of complete blocks
    or table rows, with a preserved scope and column header.
    """
    if len(text) <= budget:
        return text, {'coverage': 'full', 'source_chars': len(text), 'selected_chars': len(text),
                      'omitted_units': 0, 'overflow': False}
    parts = units(text)
    if not parts:
        return text, {'coverage': 'full', 'source_chars': len(text), 'selected_chars': len(text),
                      'omitted_units': 0, 'overflow': len(text) > budget}
    words = query_terms(query, symbols)
    hays = [(' '.join(p['scope']) + '\n' + p['body']).lower().replace('\\_', '_') for p in parts]
    weights = {w: math.log(1 + len(parts) / (1 + sum(w in h for h in hays)))
               * (3 if re.search(r'[a-z]', w) else len(w) / 2) for w in words}
    exact = [s.lower() for s in symbols if s]
    scores = []
    for i, (part, hay) in enumerate(zip(parts, hays)):
        head = ' '.join(part['scope']).lower()
        score = sum(v * (2 if w in head else 1) for w, v in weights.items() if w in hay)
        score += sum(100 for s in exact if s in hay)
        scores.append((-score, i))
    scores.sort()
    chosen, used, projected = [], 0, False
    for score, i in scores:
        size = len(parts[i]['body']) + sum(len(s) + 1 for s in parts[i]['scope']) + 40
        if size > budget:
            body = project(parts[i]['body'], query, max(100, budget - 120))
            if not body:
                continue
            parts[i] = {**parts[i], 'body': body}
            projected = True
            size = len(body) + sum(len(s) + 1 for s in parts[i]['scope']) + 40
        if chosen and (-score <= 0 or used + size > budget):
            continue
        chosen.append(i)
        used += size
        if used >= budget:
            break
    chosen.sort()
    rendered = []
    for i in chosen:
        part = parts[i]
        rendered.append('\n'.join(part['scope']) + f"\n[原文起始行 {part['line']}]\n" + part['body'])
    result = '\n\n'.join(rendered)
    return result, {'coverage': 'full' if len(chosen) == len(parts) and not projected else 'excerpt',
                    'source_chars': len(text), 'selected_chars': len(result),
                    'omitted_units': len(parts) - len(chosen), 'overflow': len(result) > budget}


def project(body, query, budget):
    """Oversized sections: whole paragraphs/fences, or a marked table projection.

    No partial row or code fence is emitted. A table projection retains its
    column header; the result explicitly remains an excerpt, never a full schema.
    """
    blocks, current, fence = [], [], None
    for line in body.splitlines(keepends=True):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
        if not line.strip() and fence is None:
            if current:
                blocks.append(''.join(current).strip())
            current = []
        else:
            current.append(line)
    if current:
        blocks.append(''.join(current).strip())
    candidates = []
    for index, block in enumerate(blocks):
        if len(block) > budget and block.lstrip().startswith('|'):
            rows = block.splitlines()
            if len(rows) < 3:
                continue
            head = rows[:2]
            # Flattened nested schemas have no reliable depth information.
            # Isolated rows cannot preserve their object ancestry; defer the
            # table as a whole instead of assembling a misleading schema.
            if any(re.search(r'\|\s*(?:Object|Array|Map(?:&lt;|<)|List(?:&lt;|<))', row, re.I)
                   for row in rows[2:]):
                block = '[表格未展开：含嵌套对象，原始表共 ' + str(len(rows) - 2) + ' 行；完整表见原文]'
                candidates.append((-relevance('\n'.join(rows), query), index, block))
                continue
            scored = sorted(((relevance(row, query), n, row) for n, row in enumerate(rows[2:], 2)),
                            key=lambda x: (-x[0], x[1]))
            picked, size = [], sum(map(len, head))
            for score, n, row in scored:
                if score > 0 and size + len(row) < budget - min(40, budget // 4):
                    picked.append((n, row))
                    size += len(row)
            if picked:
                block = '\n'.join(head + [row for _, row in sorted(picked)]) + f'\n[表格摘录：省略 {len(rows) - 2 - len(picked)} 行]'
        if len(block) <= budget:
            candidates.append((-relevance(block, query), index, block))
    selected, size = [], 0
    for _, index, block in sorted(candidates):
        if size + len(block) <= budget:
            selected.append((index, block))
            size += len(block)
    return '\n\n'.join(block for _, block in sorted(selected))


def referenced_commands(text, paths):
    """Only literal, token-bounded paths from known contracts; no inferred path."""
    found = []
    for path in paths:
        for match in re.finditer(r'(?<![a-z0-9_+.-])' + re.escape(path) + r'(?![a-z0-9_+.-])', text, re.I):
            found.append((match.start(), match.end(), path))
    found.sort(key=lambda item: (item[0], -(item[1] - item[0])))
    result, covered_until = [], -1
    for start, end, path in found:
        if start < covered_until:
            continue
        if path not in result:
            result.append(path)
        covered_until = end
    return result
