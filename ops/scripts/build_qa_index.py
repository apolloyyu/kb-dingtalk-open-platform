#!/usr/bin/env python3
"""从语料抽出「结构化事实索引」，供答疑系统做精确检索与冲突消解。

产出 compiled/index/ 下 4 张表：
  api.jsonl        每个服务端 API 一行：endpoint / method / 权限点 / 应用类型 / 新旧
  permission.jsonl 权限点 -> 涉及的 API（补上官方空壳的「权限点映射文档」）
  errcode.jsonl    全局错误码逐条展开（原文是 2501 行的单篇大表，整篇入库无法命中）
  event.jsonl      事件类型标识 -> 事件文档
用法: python3 tools/build_qa_index.py
"""
import collections
import json
import os
import re
import sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "graph")
HIST = "历史文档（不推荐）"

RE_URL_ROW = re.compile(r"\|\s*HTTP URL\s*\|\s*(\S+?)\s*\|")
RE_METHOD = re.compile(r"\|\s*HTTP Method\s*\|\s*(\w+)")
RE_PERM_ROW = re.compile(r"\|\s*权限要求\s*\|\s*([^|]+)\|")
RE_APPTYPE = re.compile(r"\|\s*支持的应用类型\s*\|\s*([^|]+)\|")
# 历史文档多数只在 SDK 代码块里出现 endpoint
RE_BARE = re.compile(r"https?://(?:oapi|api)\.dingtalk\.com/[A-Za-z0-9_/.{}\-]+")
RE_PERM_CODE = re.compile(r"permission[:\-]([A-Za-z0-9_.]+)")
RE_EVENT = re.compile(r'"?EventType"?\s*[:=]\s*"([a-z0-9_]{4,60})"')
# 客户端 JSAPI 调用名，如 dd.setNavigationBar / dd.biz.util.uploadAttachment
RE_JSAPI = re.compile(r"\bdd(?:\.[A-Za-z_$][A-Za-z0-9_$]*)+")


def unescape_md(s: str) -> str:
    return s.replace("\\_", "_").replace("\\*", "*").replace("\\", "").strip()


def load_docs():
    p = os.path.join(ROOT, "meta", "documents.jsonl")
    return [json.loads(line) for line in open(p, encoding="utf-8")]


def endpoint_version(url: str) -> str:
    host = urlparse(url).netloc
    if host == "api.dingtalk.com":
        return "v2-new"      # 新版 OpenAPI
    if host == "oapi.dingtalk.com":
        return "v1-oapi"     # 老域名，部分仍是唯一入口
    return "unknown"


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    docs = load_docs()

    apis, perms, events, jsapis = [], collections.defaultdict(list), [], []
    stats = collections.Counter()

    for d in docs:
        path = os.path.join(ROOT, d["local_path"])
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8", errors="ignore").read()
        # 上游 tab 命名会抖动(2026-08 起「服务端API」→「服务端 API」),比较一律去空格
        tab_n = (d["tab"] or "").replace(" ", "")
        archived = bool(d["breadcrumb"]) and d["breadcrumb"][0] == HIST
        base = {
            "title": d["title"],
            "source_url": d["source_url"],
            "doc_path": d["local_path"],
            "tab": d["tab"],
            "breadcrumb": d["breadcrumb"],
            "archived": archived,
            "updated_at": d["updated_at"],
        }

        # ---- 客户端 JSAPI 调用名 ----
        if tab_n == "客户端JSAPI":
            names = sorted({n for n in RE_JSAPI.findall(text) if "." in n and len(n) <= 80})
            if names:
                jsapis.append({**base, "jsapi_names": names})
                stats["jsapi_with_name"] += 1
            else:
                stats["jsapi_no_name"] += 1

        # ---- 事件类型 ----
        if tab_n == "事件订阅":
            found = sorted(set(RE_EVENT.findall(text)))
            if found:
                events.append({**base, "event_types": found})
                stats["event_with_type"] += 1
            else:
                stats["event_no_type"] += 1

        if tab_n != "服务端API":
            continue

        # ---- endpoint：优先结构化表格，回退到正文裸 URL ----
        m = RE_URL_ROW.search(text)
        if m:
            url, src = unescape_md(m.group(1)), "table"
        else:
            cands = [unescape_md(u) for u in RE_BARE.findall(text)]
            # 去掉取 token 的通用前置调用，它几乎出现在每篇 SDK 示例里
            cands = [c for c in cands if not c.endswith("/gettoken")] or cands
            if not cands:
                stats["api_no_endpoint"] += 1
                continue
            url, src = collections.Counter(cands).most_common(1)[0][0], "code_block"

        method_m = RE_METHOD.search(text)
        perm_raw = unescape_md(RE_PERM_ROW.search(text).group(1)) if RE_PERM_ROW.search(text) else ""
        apptype_raw = unescape_md(RE_APPTYPE.search(text).group(1)) if RE_APPTYPE.search(text) else ""
        perm_codes = RE_PERM_CODE.findall(perm_raw)

        rec = {
            **base,
            "endpoint": url,
            "endpoint_source": src,
            "method": method_m.group(1) if method_m else None,
            "api_version": endpoint_version(url),
            "permission_scopes": perm_codes,
            "permission_raw": perm_raw,
            "app_types": re.findall(r"appType-([^\s]+?)(?=appType-|$)", apptype_raw),
        }
        apis.append(rec)
        stats[f"api_{src}"] += 1
        for pc in perm_codes:
            perms[pc].append({"title": d["title"], "endpoint": url, "archived": archived,
                              "doc_path": d["local_path"]})

    # ---- 错误码大表逐行展开 ----
    errs = []
    for d in docs:
        if not re.search(r"错误码", d["title"]):
            continue
        path = os.path.join(ROOT, d["local_path"])
        if not os.path.exists(path):
            continue
        lines = open(path, encoding="utf-8", errors="ignore").read().splitlines()
        for ln in lines:
            cells = [unescape_md(c) for c in ln.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            if set(cells[0]) <= set("- ") or cells[0] in ("HttpCode", "错误码"):
                continue
            # 形如 | 200/400 | invalidDept | INVALID DEPT | 非法的部门ID |
            if re.fullmatch(r"[\d/]{3,}", cells[0]) and cells[1]:
                errs.append({
                    "http_code": cells[0],
                    "error_code": cells[1],
                    "message": cells[2] if len(cells) > 2 else "",
                    "explanation": cells[3] if len(cells) > 3 else "",
                    "from_doc": d["title"],
                    "source_url": d["source_url"],
                })

    check_mode = "--check" in sys.argv
    drift = []

    def dump(name, rows):
        content = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
        path = os.path.join(OUT, name)
        if check_mode:
            have = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
            if have != content:
                drift.append(name)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        return len(rows)

    n_api = dump("api.jsonl", apis)
    n_err = dump("errcode.jsonl", errs)
    n_evt = dump("event.jsonl", events)
    n_js = dump("jsapi.jsonl", jsapis)
    n_perm = dump("permission.jsonl", [
        {"permission_scope": k, "api_count": len(v),
         "current_apis": [x for x in v if not x["archived"]],
         "archived_apis": [x for x in v if x["archived"]]}
        for k, v in sorted(perms.items(), key=lambda x: -len(x[1]))
    ])

    print(f"api.jsonl        {n_api:5d} 个接口")
    print(f"  ├ 结构化表格抽取 {stats['api_table']:5d}")
    print(f"  ├ 代码块回退抽取 {stats['api_code_block']:5d}")
    print(f"  └ 抽不出 endpoint {stats['api_no_endpoint']:5d}")
    vc = collections.Counter(a["api_version"] for a in apis)
    ac = collections.Counter((a["api_version"], a["archived"]) for a in apis)
    print(f"  版本分布: {dict(vc)}")
    print(f"  版本×归档: {{{', '.join(f'{k}:{v}' for k,v in sorted(ac.items(), key=str))}}}")
    print(f"permission.jsonl {n_perm:5d} 个权限点  (官方原文档为空壳)")
    print(f"errcode.jsonl    {n_err:5d} 条错误码")
    print(f"event.jsonl      {n_evt:5d} 篇事件文档带类型标识"
          f" (另有 {stats['event_no_type']} 篇无标识)")
    print(f"jsapi.jsonl      {n_js:5d} 篇客户端JSAPI文档带调用名"
          f" (另有 {stats['jsapi_no_name']} 篇无 dd.* 标识)")
    if check_mode:
        if drift:
            print(f"[build_qa_index --check] 漂移: {drift}，需重跑 build_qa_index.py")
            return 1
        print("[build_qa_index --check] OK：graph 五表与 docs/meta 一致")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
