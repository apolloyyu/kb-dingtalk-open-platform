#!/usr/bin/env python3
"""从 graph/api.jsonl + 官方文档 Markdown 表格确定性生成 API 答案卡。

只按文档结构解析，不写产品/接口特例：基本信息、请求头/查询/路径/Body、响应体。
结构或关键字段不完整即标 partial，dkdoc 自动回落原文；full 卡才允许快路径。
"""
import argparse
import json
import os
import re
import shutil
import sys

FULL_RATIO_FLOOR = 0.70
CARD_COUNT_FLOOR = 1200
CARD_SIZE_LIMIT = 4500


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(x) for x in f if x.strip()]


def clean(s, limit=220):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    s = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", s)
    s = s.replace("\\_", "_")
    return s[:limit]


def norm(s):
    return re.sub(r"[\s*_`：:]", "", clean(s)).lower()


def split_cells(line):
    s = line.strip().strip("|")
    return [clean(x.replace("\\|", "|"), 1000) for x in re.split(r"(?<!\\)\|", s)]


def is_separator(row):
    return bool(row) and all(re.fullmatch(r":?-{3,}:?", x.replace(" ", "")) for x in row)


def tables(text):
    out, buf = [], []
    for line in text.splitlines() + [""]:
        if line.lstrip().startswith("|"):
            buf.append(line)
        elif buf:
            rows = [split_cells(x) for x in buf]
            if len(rows) >= 2:
                out.append(rows)
            buf = []
    return out


def sections(md):
    ms = list(re.finditer(r"^#{2,4}\s+(.+?)\s*$", md, re.M))
    out = []
    for i, m in enumerate(ms):
        title = norm(m.group(1))
        end = ms[i + 1].start() if i + 1 < len(ms) else len(md)
        out.append((title, md[m.end():end]))
    return out


def frontmatter_value(md, key):
    m = re.search(r"^" + re.escape(key) + r":\s*[\"']?([^\"'\n]+)", md[:1600], re.M)
    return m.group(1).strip() if m else ""


def basic_info(md):
    result = {}
    wanted = {"httpurl": "endpoint", "httpmethod": "method",
              "支持的应用类型": "app_types_raw", "权限要求": "permission_raw"}
    for tab in tables(md):
        for row in tab:
            if len(row) < 2:
                continue
            k = norm(row[0])
            if k in wanted:
                result[wanted[k]] = clean(row[1], 600)
    return result


def field_table(tab):
    if len(tab) < 3 or not is_separator(tab[1]):
        return None
    headers = [norm(x) for x in tab[0]]
    name_i = next((i for i, x in enumerate(headers)
                   if x in ("名称", "参数名称", "字段名称", "字段", "参数")), None)
    if name_i is None:
        return None
    type_i = next((i for i, x in enumerate(headers) if x in ("类型", "数据类型")), None)
    req_i = next((i for i, x in enumerate(headers) if x in ("是否必填", "必填", "是否必须")), None)
    desc_i = next((i for i, x in enumerate(headers) if x in ("描述", "说明", "参数说明")), None)
    ex_i = next((i for i, x in enumerate(headers) if x in ("示例值", "示例", "example")), None)
    fields = []
    for row in tab[2:]:
        if name_i >= len(row) or not clean(row[name_i]):
            continue
        def val(i):
            return clean(row[i], 260) if i is not None and i < len(row) else ""
        req = val(req_i)
        fields.append({"name": val(name_i), "type": val(type_i),
                       "required": norm(req) in ("是", "true", "必填", "yes"),
                       "example": val(ex_i), "desc": val(desc_i)})
    return fields


SECTION_NAMES = {
    "headers": ("请求头", "header参数", "headers"),
    "path": ("路径参数", "path参数"),
    "query": ("查询参数", "query参数"),
    "body": ("请求体", "body参数"),
    "returns": ("响应体", "返回参数", "response参数"),
}


def extract_fields(md):
    found = {k: [] for k in SECTION_NAMES}
    broken = []
    for title, body in sections(md):
        kind = next((k for k, names in SECTION_NAMES.items()
                     if any(title == n or title.endswith(n) for n in names)), None)
        if not kind:
            continue
        tabs = tables(body)
        if not tabs:
            continue
        parsed_any = False
        for tab in tabs:
            parsed = field_table(tab)
            if parsed is not None:
                found[kind].extend(parsed)
                parsed_any = True
        if not parsed_any:
            broken.append(kind)
    for kind, items in found.items():
        uniq = {}
        for x in items:
            uniq.setdefault(x["name"], x)
        found[kind] = list(uniq.values())
    return found, sorted(set(broken))


def limit_lines(md, fields):
    candidates = []
    for xs in fields.values():
        candidates.extend(x.get("desc", "") for x in xs)
    # 正文只取非代码、非表格行；数值结论保留所在完整行。
    in_code = False
    for line in md.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and not line.lstrip().startswith("|"):
            candidates.append(line)
    pat = re.compile(r"最多|最大|上限|有效期|只能|仅限|每次|不超过|[0-9]+\s*(?:秒|分钟|小时|天|次|个|条|人|字节|mb|kb)", re.I)
    out = []
    for s in candidates:
        s = clean(s, 240)
        if s and pat.search(s) and s not in out:
            out.append(s)
        if len(out) >= 8:
            break
    return out


def render_fields(title, rows, compact_optional=False):
    lines = [f"## {title}"]
    if not rows:
        return lines + ["- none"]
    required = [x for x in rows if x["required"]]
    optional = [x for x in rows if not x["required"]]
    for x in required:
        suffix = f": {x['desc']}" if x["desc"] else ""
        lines.append(f"- {x['name']} ({x['type'] or 'unknown'}, required){suffix}")
    if compact_optional and optional:
        lines.append("- optional: " + ", ".join(
            f"{x['name']}({x['type'] or 'unknown'})" for x in optional))
    else:
        for x in optional:
            suffix = f": {x['desc']}" if x["desc"] else ""
            lines.append(f"- {x['name']} ({x['type'] or 'unknown'}, optional){suffix}")
    return lines


def build_card(row, md):
    doc_id = frontmatter_value(md, "doc_id")
    basic = basic_info(md)
    fields, broken = extract_fields(md)
    endpoint = clean(row.get("endpoint") or basic.get("endpoint"), 500)
    method = clean(row.get("method") or basic.get("method"), 20).upper()
    has_request = bool(re.search(r"^##\s+\*{0,2}请求\*{0,2}\s*$", md, re.M))
    has_response = bool(re.search(r"^##\s+\*{0,2}响应\*{0,2}\s*$", md, re.M))
    has_basic = bool(basic.get("endpoint") and basic.get("method"))
    reasons = []
    if not has_basic: reasons.append("missing_basic_table")
    if not endpoint: reasons.append("missing_endpoint")
    if not method: reasons.append("missing_method")
    if not has_request: reasons.append("missing_request_section")
    if not has_response: reasons.append("missing_response_section")
    if broken: reasons.append("unparsed_tables:" + ",".join(broken))

    app_types = row.get("app_types") or []
    permissions = row.get("permission_scopes") or []
    lines = [f"# {clean(row.get('title'), 300)}", "", f"doc_id: {doc_id}",
             "completeness: PENDING", f"archived: {str(bool(row.get('archived'))).lower()}",
             f"method: {method or '—'}", f"endpoint: {endpoint or '—'}",
             f"api_version: {row.get('api_version') or '—'}",
             "app_types: " + (", ".join(app_types) if app_types else "not_stated"),
             "permissions: " + (", ".join(permissions) if permissions else "not_stated")]
    lines += [""] + render_fields("Request headers", fields["headers"], True)
    lines += [""] + render_fields("Path params", fields["path"], True)
    lines += [""] + render_fields("Query params", fields["query"], True)
    lines += [""] + render_fields("Body", fields["body"], True)
    lines += [""] + render_fields("Returns", fields["returns"], True)
    limits = limit_lines(md, fields)
    lines += ["", "## Limits"] + ([f"- {x}" for x in limits] or ["- none stated"])
    lines += ["", f"source_url: {row.get('source_url') or '—'}",
              f"updated_at: {row.get('updated_at') or '—'}"]
    body = "\n".join(lines) + "\n"
    if len(body) > CARD_SIZE_LIMIT:
        reasons.append(f"card_too_large:{len(body)}")
    full = not reasons
    body = body.replace("completeness: PENDING",
                        "completeness: full" if full else "completeness: partial", 1)
    if reasons:
        body = body.replace(f"archived: {str(bool(row.get('archived'))).lower()}",
                            f"partial_reason: {','.join(reasons)}\narchived: {str(bool(row.get('archived'))).lower()}", 1)
    return doc_id, body, "full" if full else "partial", reasons


def build(repo, check=False):
    rows = load_jsonl(os.path.join(repo, "graph", "api.jsonl"))
    if not rows:
        raise RuntimeError("graph/api.jsonl 为空")
    root = os.path.join(repo, "cards")
    target, tmp = os.path.join(root, "api"), os.path.join(root, ".api-building")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp, exist_ok=True)
    index, full_n = [], 0
    ids = set()
    for row in sorted(rows, key=lambda x: x["doc_path"]):
        path = os.path.join(repo, row["doc_path"])
        if not os.path.exists(path):
            raise RuntimeError(f"doc_path 不存在: {row['doc_path']}")
        md = open(path, encoding="utf-8", errors="replace").read()
        doc_id, body, completeness, reasons = build_card(row, md)
        if not doc_id or doc_id in ids:
            raise RuntimeError(f"doc_id 缺失/重复: {doc_id} ({row['doc_path']})")
        ids.add(doc_id)
        rel = f"cards/api/{doc_id}.md"
        with open(os.path.join(tmp, doc_id + ".md"), "w", encoding="utf-8") as f:
            f.write(body)
        full_n += completeness == "full"
        index.append({"doc_id": doc_id, "title": row.get("title") or "",
                      "endpoint": row.get("endpoint") or "", "doc_path": row["doc_path"],
                      "path": rel, "completeness": completeness,
                      "archived": bool(row.get("archived")), "reasons": reasons})
    ratio = full_n / len(index)
    files = [x for x in os.listdir(tmp) if x.endswith(".md")]
    error = ""
    if len(files) != len(index): error = f"卡片数不符 {len(files)} != {len(index)}"
    elif len(index) < CARD_COUNT_FLOOR: error = f"卡片地板未达标 {len(index)} < {CARD_COUNT_FLOOR}"
    elif ratio < FULL_RATIO_FLOOR: error = f"full 完整率未达标 {ratio:.1%} < {FULL_RATIO_FLOOR:.0%}"
    if error:
        shutil.rmtree(tmp, ignore_errors=True)
        raise RuntimeError(error)
    os.makedirs(root, exist_ok=True)
    index_tmp = os.path.join(root, ".api-index-building.jsonl")
    with open(index_tmp, "w", encoding="utf-8") as f:
        for x in sorted(index, key=lambda x: x["doc_id"]):
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    if check:
        existing_index = os.path.join(root, "api-index.jsonl")
        old_files = set(os.listdir(target)) if os.path.isdir(target) else set()
        new_files = set(os.listdir(tmp))
        drift = old_files != new_files or not os.path.exists(existing_index)
        if not drift:
            drift = any(open(os.path.join(target, fn), "rb").read()
                        != open(os.path.join(tmp, fn), "rb").read() for fn in new_files)
        if not drift:
            drift = open(existing_index, "rb").read() != open(index_tmp, "rb").read()
        shutil.rmtree(tmp, ignore_errors=True)
        os.remove(index_tmp)
        if drift:
            raise RuntimeError("cards/api 或 api-index.jsonl 与 docs/graph 漂移,重跑 build_cards.py")
    else:
        shutil.rmtree(target, ignore_errors=True)
        os.replace(tmp, target)
        os.replace(index_tmp, os.path.join(root, "api-index.jsonl"))
    return len(index), full_n, ratio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    try:
        total, full, ratio = build(os.path.abspath(args.repo), check=args.check)
    except Exception as e:
        print(f"API CARD BUILD FAIL: {type(e).__name__}: {e}")
        return 1
    print(f"OK: API cards {total} · full {full}({ratio:.1%}) · partial {total-full}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
