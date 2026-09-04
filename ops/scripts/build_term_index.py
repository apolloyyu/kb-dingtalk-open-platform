#!/usr/bin/env python3
"""从 docs/ 正文确定性生成 ASCII 标识符倒排索引 graph/terms.json。

标题层检索（title/breadcrumb/headings/snippet）永远命中不了只出现在正文里的字段名、
JSAPI 名、错误码、endpoint 片段（实录：`carddata从哪里获取` 命中「获取开发者权限」，
模型被迫二轮检索，简单题 30–58s）。本索引让 dkdoc ctx 对查询里的 ASCII 词一次命中正文。

格式：{"term": [[doc_idx, count], ...]}，doc_idx 为 meta/documents.jsonl 行号，
每词最多 MAX_DOCS 篇按出现次数降序；df > MAX_DF 的泛词不收（无区分度）。
零 LLM、纯文本扫描；--check 只比对不落盘，供 lint 用。
"""
import argparse
import collections
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "graph", "terms.json")
IDENT = re.compile(r"(?<![A-Za-z0-9_])[A-Za-z][A-Za-z0-9_]{3,}(?:\.[A-Za-z][A-Za-z0-9_]*)*")
MIN_LEN = 5
MAX_DF = 200
MAX_DOCS = 10
TERM_FLOOR = 30000
STOP = set("""http https www html json true false null string integer boolean object array number
long list map the and for with from this that your dingtalk open document development
open.dingtalk.com api.dingtalk.com oapi.dingtalk.com github.com https://open.dingtalk.com""".split())


def build():
    docs = [json.loads(l) for l in open(os.path.join(ROOT, "meta", "documents.jsonl"), encoding="utf-8")]
    index = collections.defaultdict(dict)
    for i, d in enumerate(docs):
        try:
            body = open(os.path.join(ROOT, d["local_path"]), encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for term, cnt in collections.Counter(m.group(0).lower() for m in IDENT.finditer(body)).items():
            if len(term) < MIN_LEN or term in STOP:
                continue
            index[term][i] = cnt
    out = {}
    for term, hits in index.items():
        if len(hits) > MAX_DF:
            continue
        out[term] = sorted(hits.items(), key=lambda x: (-x[1], x[0]))[:MAX_DOCS]
    return out, len(docs)


def dumps(out):
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验 graph/terms.json 与当前 docs 无漂移")
    a = ap.parse_args()
    out, ndocs = build()
    if len(out) < TERM_FLOOR:
        print(f"FAIL: 标识符索引仅 {len(out)} 词（地板 {TERM_FLOOR}），疑似正文缺失，未写入")
        return 1
    text = dumps(out)
    if a.check:
        if not os.path.exists(OUT):
            print("FAIL: graph/terms.json 不存在，运行 build_term_index.py")
            return 1
        cur = open(OUT, encoding="utf-8").read()
        if hashlib.sha256(cur.encode()).hexdigest() != hashlib.sha256(text.encode()).hexdigest():
            print("FAIL: graph/terms.json 与 docs/ 漂移，重跑 build_term_index.py")
            return 1
        print(f"OK: terms.json {len(out)} 词 与 {ndocs} 篇正文一致")
        return 0
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, OUT)
    print(f"OK: terms.json {len(out)} 词 · {ndocs} 篇 · {len(text.encode())/1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
