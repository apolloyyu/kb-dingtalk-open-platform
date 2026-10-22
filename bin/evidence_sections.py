"""Select complete Markdown evidence units. Pure stdlib, no I/O or model calls.

The identical module is shipped by both KB adapters. Its content hash is checked
by the cross-repository acceptance script; product facts belong to the sources.
"""
import hashlib
import json
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


def _declaration_match(body, query, symbols=()):
    """Match real field-definition rows outside fences, without heading hints."""
    names = {'名称', '参数', '参数名', '字段', '字段名', 'name', 'field', 'parameter', 'field name', 'parameter name'}
    types = {'类型', '数据类型', '参数类型', '字段类型', 'type', 'data type'}
    details = {'描述', '说明', '含义', '是否必填', '必填', 'required', 'description'}
    generic = names | types | details | {'请求', '响应', '查询', '创建', '可选', '示例', '使用', '返回'}
    subject = re.sub(r'https?://\S+', '', query, flags=re.I)
    literal_symbols = [symbol for symbol in symbols if symbol.lower() in subject.lower()]
    terms = query_terms(subject, literal_symbols) - generic
    lines, fence, index = body.splitlines(), None, 0
    while index < len(lines):
        line = lines[index]
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            index += 1
            continue
        if fence is not None or not line.lstrip().startswith('|'):
            index += 1
            continue
        end = index + 1
        while end < len(lines) and lines[end].lstrip().startswith('|'):
            end += 1
        rows = lines[index:end]
        index = end
        if len(rows) < 3:
            continue
        cells = lambda row: [cell.strip() for cell in re.split(r'(?<!\\)\|', row.strip().strip('|'))]
        header = [re.sub(r'[*`_]', '', cell).lower() for cell in cells(rows[0])]
        separators = cells(rows[1])
        if (len(separators) != len(header) or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in separators)
                or not (set(header) & names and set(header) & types and set(header) & details)):
            continue
        columns = [n for n, cell in enumerate(header) if cell in names or cell in {'描述', '说明', '含义', 'description'}]
        for row in rows[2:]:
            values = cells(row)
            hay = ' '.join(values[n] for n in columns if n < len(values)).lower().replace('\\_', '_')
            if any((bool(re.search(r'(?<![a-z0-9_])' + re.escape(term) + r'(?![a-z0-9_])', hay))
                    if re.search(r'[a-z]', term) else term in hay) for term in terms):
                return True
    return False


def _captioned_codes(text, query):
    """Literal source captions/fence info, with complete fences and exact lines."""
    lines, headings, result, i = text.splitlines(keepends=True), [], [], 0
    subject = re.sub(r'https?://\S+', '', query.lower())
    while i < len(lines):
        opened = re.match(r'^\s*(`{3,}|~{3,})([^\r\n]*)', lines[i])
        if not opened:
            heading = re.match(r'^(#{1,6})\s+', lines[i])
            if heading:
                depth = len(heading[1])
                headings = [(d, h) for d, h in headings if d < depth]
                headings.append((depth, lines[i].rstrip('\r\n')))
            i += 1
            continue
        end = i + 1
        while end < len(lines):
            close = re.match(r'^\s*(`{3,}|~{3,})\s*$', lines[end])
            if close and close[1][0] == opened[1][0] and len(close[1]) >= len(opened[1]):
                break
            end += 1
        if end == len(lines):
            break
        start, labels = i, opened[2].strip().split()[:1]
        previous = i - 1
        while previous >= 0 and not lines[previous].strip():
            previous -= 1
        if previous >= 0 and re.fullmatch(r'[A-Za-z][A-Za-z0-9.+#_-]{0,30}', lines[previous].strip()):
            start = previous
            labels.append(lines[previous].strip())
        if any(re.fullmatch(r'[A-Za-z][A-Za-z0-9.+#_-]{0,30}', label)
               and re.search(r'(?<![a-z0-9_])' + re.escape(label.lower()) + r'(?![a-z0-9_])', subject)
               for label in labels):
            result.append({'body': ''.join(lines[start:end + 1]), 'line': start + 1,
                           'scope': [h for _, h in headings]})
        i = end + 1
    return result


def _scalar_prefix_projection(part, query, symbols=()):
    """Project only proven root scalar rows before the first unknown/container.

    Flattened tables do not encode the later parent tree. Never cross that first
    boundary to infer a field's ancestry. Adjacent conditions stay verbatim.
    """
    roots = {'请求体', '查询参数', '路径参数', '请求头', '响应体', 'request body',
             'query parameters', 'path parameters', 'request headers', 'response body'}
    leaf = re.sub(r'^[#\s]+|[*`]', '', part['scope'][-1]).strip().lower() if part['scope'] else ''
    if leaf not in roots or re.search(r'(?m)^\s*(?:`{3,}|~{3,})', part['body']):
        return None
    lines, spans, i = part['body'].splitlines(keepends=True), [], 0
    while i < len(lines):
        if not lines[i].lstrip().startswith('|'):
            i += 1
            continue
        end = i + 1
        while end < len(lines) and lines[end].lstrip().startswith('|'):
            end += 1
        spans.append((i, end))
        i = end
    if len(spans) != 1:
        return None
    start, end = spans[0]
    table = lines[start:end]
    if len(table) < 3 or not _declaration_match(''.join(table), query, symbols):
        return None
    cells = lambda row: [cell.strip() for cell in re.split(r'(?<!\\)\|', row.strip().strip('|'))]
    header = [re.sub(r'[*`_]', '', cell).lower() for cell in cells(table[0])]
    columns = [n for n, cell in enumerate(header)
               if cell in {'类型', '数据类型', '参数类型', '字段类型', 'type', 'data type'}]
    if len(columns) != 1:
        return None
    scalars = {'string', 'number', 'integer', 'int', 'long', 'double', 'float', 'boolean', 'bool'}
    picked = []
    for row in table[2:]:
        values = cells(row)
        if len(values) != len(header) or re.sub(r'[*`]', '', values[columns[0]]).lower() not in scalars:
            break
        if _declaration_match(''.join(table[:2]) + row, query, symbols):
            picked.append(row)
    if not picked:
        return None
    notice = f'\n[表格摘录：仅原表首个未知或容器类型前的已知标量行；省略 {len(table)-2-len(picked)} 行；完整表见原文]\n'
    return {**part, 'body': ''.join(lines[:start] + table[:2] + picked) + notice + ''.join(lines[end:])}


def _declarations_with_code(parts, codes, query, budget, symbols=()):
    """Allocate a matching literal code caption and field evidence together."""
    def render(selected):
        return '\n\n'.join('\n'.join(part['scope']) + f"\n[原文起始行 {part['line']}]\n" + part['body']
                            for _, part in sorted(selected, key=lambda row: (row[0], row[1]['line'])))
    declarations = [(i, part) for i, part in enumerate(parts) if _declaration_match(part['body'], query, symbols)]
    declarations.sort(key=lambda row: (-relevance(row[1]['body'], query), row[0]))
    codes = sorted(codes, key=lambda part: (-relevance(part['body'], query), part['line']))
    chosen = []
    for code in codes:
        code_index = max((i for i, part in enumerate(parts) if part['line'] <= code['line']), default=0)
        for index, table in declarations:
            if index == code_index:
                # A single section can already contain both the table and its
                # example. Keep it once; mixed code/table blocks are not projected.
                if len(render([(index, table)])) <= budget:
                    chosen = [(index, table)]
                    break
                continue
            pair = [(index, table), (code_index, code)]
            if len(render(pair)) <= budget:
                chosen = pair
                break
            projection = _scalar_prefix_projection(table, query, symbols)
            if projection is not None:
                pair = [(index, projection), (code_index, code)]
                if len(render(pair)) <= budget:
                    chosen = pair
                    break
        if chosen:
            break
    if not chosen:
        return None
    covered = {index for index, _ in chosen}
    extra = [(i, part) for i, part in enumerate(parts) if i not in covered
             and not re.search(r'(?m)^\s*(?:`{3,}|~{3,})', part['body'])]
    for index, part in sorted(extra, key=lambda row: (-relevance(row[1]['body'], query), row[0])):
        if relevance(part['body'], query) > 0 and len(render(chosen + [(index, part)])) <= budget:
            chosen.append((index, part))
    return render(chosen), len({index for index, _ in chosen})


def select(text, query, budget, symbols=(), *, prefer_declarations=False):
    """Keep complete source units; never cut a table, code fence or a URL.

    Oversized sections become explicitly partial projections of complete blocks
    or table rows, with a preserved scope and column header.
    Declaration preference is opt-in; it uses displayed table rows, never an
    ancestor heading or a deferred table's omitted content, to earn priority.
    """
    if len(text) <= budget:
        return text, {'coverage': 'full', 'source_chars': len(text), 'selected_chars': len(text),
                      'omitted_units': 0, 'overflow': False}
    parts = units(text)
    if not parts:
        return text, {'coverage': 'full', 'source_chars': len(text), 'selected_chars': len(text),
                      'omitted_units': 0, 'overflow': len(text) > budget}
    if prefer_declarations:
        codes = _captioned_codes(text, query)
        balanced = _declarations_with_code(parts, codes, query, budget, symbols) if codes else None
        if balanced is not None:
            result, selected_units = balanced
            return result, {'coverage': 'excerpt', 'source_chars': len(text), 'selected_chars': len(result),
                            'omitted_units': len(parts) - selected_units, 'overflow': False}
        if codes:
            # If safe declaration/code co-selection failed, retain the original
            # selection behavior; do not revive rejected rows through projection.
            return select(text, query, budget, symbols, prefer_declarations=False)
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
    prepared = {}
    if prefer_declarations:
        ranked = []
        for score, i in scores:
            part = parts[i]
            overhead = sum(len(s) + 1 for s in part['scope']) + 40
            body = part['body']
            if len(body) + overhead > budget:
                body = project(body, query, max(0, budget - overhead), prefer_declarations=True)
            if not body:
                continue
            prepared[i] = body
            deferred = bool(re.fullmatch(r'\[表格未展开：[^\n]*\]', body.strip()))
            # A deferred table has no displayed field declaration. It cannot
            # borrow the omitted table's score or displace a real small table.
            ranked.append((2 if deferred else 0 if _declaration_match(body, query, symbols) else 1,
                           0 if deferred else score, i))
        scores = [(score, i) for _, score, i in sorted(ranked)]
    chosen, used, projected = [], 0, False
    # A short relevant document preface carries the object and applicability
    # context; a long example must not consume its entire budget first.
    if parts and len(parts[0]['scope']) <= 1:
        opening = parts[0]
        size = len(opening['body']) + sum(len(x) + 1 for x in opening['scope']) + 40
        if size <= min(650, budget // 3) and relevance(opening['body'], query) > 0:
            chosen.append(0)
            used = size
    for score, i in scores:
        if i in chosen:
            continue
        if prefer_declarations:
            body = prepared[i]
            if body != parts[i]['body']:
                projected = True
                parts[i] = {**parts[i], 'body': body}
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


def project(body, query, budget, *, prefer_declarations=False):
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
            if prefer_declarations:
                cells = lambda row: [cell.strip() for cell in re.split(r'(?<!\\)\|', row.strip().strip('|'))]
                header = [re.sub(r'[*`_]', '', cell).lower() for cell in cells(rows[0])]
                columns = [n for n, cell in enumerate(header)
                           if cell in {'类型', '数据类型', '参数类型', '字段类型', 'type', 'data type'}]
                values = [cells(row) for row in rows[2:]]
                scalars = {'string', 'number', 'integer', 'int', 'long', 'double', 'float', 'boolean', 'bool'}
                if len(columns) != 1 or any(len(row) != len(header)
                        or re.sub(r'[*`]', '', row[columns[0]]).lower() not in scalars for row in values):
                    block = '[表格未展开：字段层级无法确认，原始表共 ' + str(len(rows) - 2) + ' 行；完整表见原文]'
                    candidates.append((0, index, block))
                    continue
            # Flattened nested schemas have no reliable depth information.
            # Isolated rows cannot preserve their object ancestry; defer the
            # table as a whole instead of assembling a misleading schema.
            if not prefer_declarations and any(re.search(r'\|\s*(?:Object|Array|Map(?:&lt;|<)|List(?:&lt;|<))', row, re.I)
                   for row in rows[2:]):
                block = '[表格未展开：含嵌套对象，原始表共 ' + str(len(rows) - 2) + ' 行；完整表见原文]'
                candidates.append((0 if prefer_declarations else -relevance('\n'.join(rows), query), index, block))
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
    ranked = sorted(candidates, key=lambda row: (
        0 if _declaration_match(row[2], query) else 2 if row[2].startswith('[表格未展开：') else 1,
        row[0], row[1])) if prefer_declarations else sorted(candidates)
    for _, index, block in ranked:
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


def time_fields(question, history=''):
    """Literal date fields with provenance; no host date or expiry conclusion."""
    records = []
    decoder = json.JSONDecoder()
    projected = previous_questions(history)
    role_filtered = bool(re.match(r'^(?:用户|User)[:：]', history)) and projected != history
    sources = [('current_question', question),
               ('prior_user_questions' if role_filtered else 'unclassified_history', projected)]
    def visit(value, path, origin):
        if isinstance(value, dict):
            for key, child in value.items():
                name = path + '.' + key
                if isinstance(child, str) and re.match(r'^\d{4}-\d{2}-\d{2}[Tt ]', child):
                    records.append({'origin': origin, 'path': name, 'value': child,
                        'kind': 'expiry' if re.search(r'expir|过期', key, re.I) else 'unclassified_timestamp'})
                else:
                    visit(child, name, origin)
        elif isinstance(value, list):
            for n, child in enumerate(value):
                visit(child, path + '[' + str(n) + ']', origin)
    for origin, text in sources:
        offset, number = 0, 0
        while offset < len(text):
            match = re.search(r'[\[{]', text[offset:])
            if not match:
                break
            start = offset + match.start()
            try:
                value, end = decoder.raw_decode(text[start:])
                visit(value, '$[' + str(number) + ']', origin)
                number += 1
                offset = start + end
            except ValueError:
                offset = start + 1
    if not any(record['kind'] == 'expiry' for record in records):
        return ''
    pattern = (r'(?:执行|运行|请求|发生)(?:的)?(?:时间|时刻|日期)(?:是|为|[:：])?\s*'
               r'(\d{4}-\d{2}-\d{2}(?:[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:[Zz]|[+-]\d{2}:?\d{2})?)?)')
    literal = [{'origin': origin, 'value': value}
               for origin, text in sources for value in re.findall(pattern, text)]
    times = [row for row in literal if re.search(r'[Tt ]\d{2}:\d{2}', row['value'])]
    current = [row['value'] for row in times if row['origin'] == 'current_question']
    return '== 输入时间字段 ==\n' + json.dumps({
        'origin': 'user_supplied_text', 'extractor_uses_host_clock': False,
        'execution_time': {'status': 'explicit_text_extracted' if times else 'not_extracted',
                           'candidates_from_current_question': current,
                           'literal_candidates_with_origin': literal},
        'timestamp_fields': records}, ensure_ascii=False)


def literal_block(text, line_number):
    """Return the complete paragraph, list item, table or fence for a line.

    The body is an exact slice, including whitespace and line endings. Scope is
    copied from actual ancestor headings, never inferred from a query.
    """
    lines = text.splitlines(keepends=True)
    target = line_number - 1
    if not 0 <= target < len(lines):
        raise ValueError('source line is outside the document')
    headings, scopes, fences, opened = [], [], [], None
    for i, line in enumerate(lines):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if opened is None:
                opened = (i, marker[1])
            elif marker[1][0] == opened[1][0] and len(marker[1]) >= len(opened[1]):
                fences.append((opened[0], i + 1))
                opened = None
        elif opened is None:
            heading = re.match(r'^(#{1,6})\s+', line)
            if heading:
                depth = len(heading[1])
                headings = [(d, h) for d, h in headings if d < depth]
                headings.append((depth, line.rstrip('\r\n')))
        scopes.append([h for _, h in headings])
    if opened is not None:
        fences.append((opened[0], len(lines)))
    span = next(((start, end) for start, end in fences if start <= target < end), None)
    if span is None:
        item_pattern = re.compile(r'^([ \t]*)(?:[-+*]|\d+[.)])\s+')
        i = 0
        while i <= target:
            item = item_pattern.match(lines[i])
            if not item:
                i += 1
                continue
            indent = len(item[1].expandtabs(4))
            end, blank = i + 1, False
            while end < len(lines):
                line = lines[end]
                if not line.strip():
                    blank = True
                    end += 1
                    continue
                child = item_pattern.match(line)
                leading = len(line[:len(line) - len(line.lstrip(' \t'))].expandtabs(4))
                if child and len(child[1].expandtabs(4)) <= indent:
                    break
                if leading <= indent and (blank or re.match(r'^(?:#{1,6}\s|\s*`{3,}|\s*~{3,}|\s*\|)', line)):
                    break
                blank = False
                end += 1
            while end > i + 1 and not lines[end - 1].strip():
                end -= 1
            if i <= target < end:
                span = i, end
                break
            i = max(i + 1, end)
    if span is None:
        start, end = target, target + 1
        table = lines[target].lstrip().startswith('|')
        def same_block(index):
            line = lines[index]
            if table:
                return line.lstrip().startswith('|')
            return (bool(line.strip()) and not line.lstrip().startswith('|')
                    and not re.match(r'^(?:#{1,6}\s|\s*`{3,}|\s*~{3,})', line))
        if not re.match(r'^#{1,6}\s', lines[target]):
            while start and same_block(start - 1):
                start -= 1
        while end < len(lines) and same_block(end):
            end += 1
        span = start, end
    start, end = span
    return {'body': ''.join(lines[start:end]), 'line': start + 1,
            'end_line': end, 'scope': scopes[target]}


def source_unit(body, source_refs, *, version='', kind='source', scope=()):
    """Wrap an explicitly supplied source or summary without altering its body.

    Identity binds literal references, recorded version, heading scope and exact
    UTF-8 body bytes. Hash equality is byte identity, not semantic validation.
    Callers classify content; this function never promotes a summary to source.
    """
    if kind not in ('source', 'derived_summary'):
        raise ValueError('unknown evidence unit kind')
    refs = sorted(set([source_refs] if isinstance(source_refs, str) else source_refs))
    if not refs or not all(isinstance(ref, str) and ref for ref in refs):
        raise ValueError('evidence units require literal source references')
    metadata = {'kind': kind, 'source_refs': refs, 'version': version,
                'scope': list(scope), 'body_chars': len(body),
                'body_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest()}
    identity = {k: v for k, v in metadata.items() if k != 'body_chars'}
    unit_id = hashlib.sha256(json.dumps(identity, ensure_ascii=False,
        sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()[:24]
    title = '来源证据单元' if kind == 'source' else '派生说明单元'
    return (f"== {title} {unit_id} ==\nevidence_unit: "
            + json.dumps(metadata, ensure_ascii=False, separators=(',', ':')) + '\n' + body)


def _source_spans(text):
    """Read only valid explicit envelopes; raw headings/fences are opaque."""
    pattern = re.compile(r'(?m)^== (?:来源证据单元|派生说明单元) [0-9a-f]{24} ==\nevidence_unit: ([^\n]+)\n')
    offset, fence = 0, None
    while offset < len(text):
        match = pattern.match(text, offset) if fence is None else None
        if match:
            try:
                meta = json.loads(match[1])
                end = match.end() + meta['body_chars']
                if end <= len(text) and meta['body_chars'] >= 0:
                    body = text[match.end():end]
                    rendered = source_unit(body, meta['source_refs'], version=meta['version'],
                                           kind=meta['kind'], scope=meta['scope'])
                    if rendered == text[match.start():end]:
                        offset = end
                        yield match.start(), end, meta
                        continue
            except (KeyError, TypeError, ValueError):
                pass
        newline = text.find('\n', offset)
        end = newline + 1 if newline >= 0 else len(text)
        line = text[offset:end]
        marker = re.match(r'^\s*(`{3,}|~{3,})(.*)', line)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        offset = end


def _groups(entries):
    groups = []
    for entry in entries:
        if entry.lstrip().startswith(('==', '--- notes/')) or not groups:
            groups.append([entry])
        else:
            groups[-1].append(entry)
    return ['\n'.join(group) for group in groups]


def annotate_groups(entries):
    """Deduplicate explicit source units and place them before derived notes.

    Unmarked groups are retained, never guessed to be raw evidence. Each source
    keeps its own envelope/scope; note headers and unresolved references remain
    attached to the remaining note. Applying this function twice is harmless.
    """
    sources, remainder, seen, first_source, first_summary = [], [], set(), None, None
    for group in _groups(entries):
        pieces, cursor = [], 0
        summary = (group.lstrip().startswith('--- notes/')
                   or group.lstrip().startswith('== 行为语义'))
        for start, end, meta in _source_spans(group):
            if meta['kind'] == 'derived_summary':
                summary = True
                continue
            if first_source is None:
                first_source = len(remainder)
            pieces.append(group[cursor:start])
            unit = group[start:end]
            # The validated envelope includes full provenance and full hash.
            if unit not in seen:
                seen.add(unit)
                sources.append(unit)
            cursor = end
        pieces.append(group[cursor:])
        rest = ''.join(pieces)
        if rest.strip():
            if summary and first_summary is None:
                first_summary = len(remainder)
            remainder.append(rest)
    if not sources:
        return remainder
    position = min(x for x in (first_source, first_summary) if x is not None)
    return remainder[:position] + sources + remainder[position:]


def navigation_text(text):
    """Return labelled derived summaries for navigation, not source evidence.

    Without a validated summary envelope, preserve legacy input unchanged.
    This does not change the evidence body or declare a summary authoritative.
    """
    summaries = [text[end - meta['body_chars']:end]
                 for _, end, meta in _source_spans(text)
                 if meta['kind'] == 'derived_summary']
    return '\n\n'.join(summaries) if summaries else text


def pack_groups(entries, cap):
    """Budget complete evidence groups, preserving explicit deferred coverage."""
    fallback = '== 证据覆盖 ==\ncoverage: deferred'
    if cap < len(fallback):
        raise ValueError('evidence budget must be at least ' + str(len(fallback)) + ' characters')
    if len('\n'.join(entries)) <= cap:
        return '\n'.join(entries)
    bodies = _groups(entries)
    def priority(i):
        title = bodies[i].lstrip().splitlines()[0]
        if any(key in title for key in ('证据契约', '输入时间字段', '检索审计', '== 继续')):
            return 0
        if any(meta['kind'] == 'derived_summary' for _, _, meta in _source_spans(bodies[i])):
            return 3
        if any(key in title for key in ('命令契约:', 'API参数卡', '答案卡', '篇目[', '正文[')):
            return 1
        if title.startswith('== 来源证据单元') or any(key in title for key in
                ('CHANGELOG', '定位字段', '产品原文', '原文直取')):
            return 2
        if title.startswith('--- notes/') or '行为语义' in title:
            return 3
        return 4
    notices = []
    for body in bodies:
        title = body.lstrip().splitlines()[0]
        command = re.search(r'命令契约: dws (.+?) ==', title)
        continuation = 'dwsdoc contract ' + json.dumps(command[1]) if command else ''
        doc = re.search(r'篇目\[.*?\] (\S+)', title)
        api_doc = re.search(r'正文\[.*?\].*?\((docs/[^)]+)\)', title)
        note = re.search(r'^--- (notes/\S+)', title)
        if doc or note:
            continuation = 'dwsdoc cat ' + (doc or note)[1]
        if api_doc:
            continuation = 'dkdoc cat ' + api_doc[1]
        if 'CHANGELOG' in title:
            continuation = 'dwsdoc cat docs/CHANGELOG.md'
        source = next((meta for _, _, meta in _source_spans(body) if meta['kind'] == 'source'), None)
        if source:
            continuation = ' | '.join(source['source_refs'])
            title = 'source ' + title.split()[-2]
        # A command continuation already contains the complete selected path;
        # repeating that path in its title consumes budget without new coverage.
        notices.append(continuation if command else title + (' | ' + continuation if continuation else ''))
    coverage_header = '\n== 证据覆盖 ==\ncoverage: excerpt; 未展开完整单元:\n'
    def render(chosen):
        included = '\n'.join(body for i, body in enumerate(bodies) if i in chosen)
        deferred = '\n'.join(notice for i, notice in enumerate(notices) if i not in chosen)
        return included + coverage_header + deferred
    def category(i):
        title = bodies[i].lstrip().splitlines()[0]
        content = bodies[i].lstrip().partition('\n')[2].strip()
        kinds = {meta['kind'] for _, _, meta in _source_spans(bodies[i])}
        if 'derived_summary' in kinds:
            return 'summary'
        if 'source' in kinds:
            return 'source'
        if '命令契约:' in title:
            return 'contract'
        if 'API参数卡' in title or '答案卡' in title:
            return 'card'
        if '篇目[' in title or '正文[' in title:
            return 'primary_document'
        if 'CHANGELOG' in title:
            return 'changelog'
        if any(key in title for key in ('定位字段', '产品原文', '原文直取')):
            return 'source' if content else None
        if title.startswith('--- notes/') or '行为语义' in title:
            return 'summary' if content else None
        return None
    chosen = set()
    ordered = sorted(range(len(bodies)), key=lambda n: (priority(n), n))
    controls = [i for i in ordered if priority(i) == 0]
    categories = []
    for i in ordered:
        kind = category(i)
        if i not in controls and kind is not None and kind not in categories:
            categories.append(kind)
    # Cover the selected evidence categories before another unit from one
    # category consumes the remaining budget. All selection remains whole-unit.
    def include(i):
        candidate = chosen | {i}
        if len(render(candidate)) > cap:
            return False
        chosen.add(i)
        return True
    for i in controls:
        include(i)
    for kind in categories:
        for i in ordered:
            if category(i) == kind and include(i):
                break
    # With every selected evidence category represented, expand original
    # evidence before additional command/navigation candidates.
    for i in sorted(ordered, key=lambda i: (0 if category(i) == 'source' else 1, priority(i), i)):
        if i not in chosen:
            include(i)
    result = render(chosen)
    if len(result) > cap:
        return fallback
    return result
