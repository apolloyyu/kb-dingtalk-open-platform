#!/usr/bin/env python3
"""知识库体检（只读）：结构一致性 + 索引漂移 + 断链。发现问题不顺手改，修复走 ops/INGEST.md。

检查项：
  1. meta/documents.jsonl ↔ docs/ 双向一致（无缺文件、无孤儿文件）
  2. meta/kb_manifest.jsonl 覆盖面 = documents.jsonl
  3. index/ 与元数据无漂移（build_index --check）
  4. graph/links.jsonl、hubs.md 与 docs/ 无漂移（build_links --check）
  5. 根入口文件与 index/TOPICS.md 的相对链接可达
  6. tombstone 过的 doc_id 不应再出现在 documents.jsonl
  7. graph/ 表引用的 doc_path 存在（WARN）
  8. meta/kb_manifest.jsonl 与 graph 五表（api/errcode/event/jsapi/permission）与 docs/meta 无漂移
  9. evals/questions.jsonl 的 ref_docs 全部可达（快照重编号的哨兵）

用法: python3 ops/scripts/lint.py    # 退出码 0=通过（WARN 不算失败）
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RE_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")

fails, warns = [], []


def load_jsonl(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def check_docs_meta():
    docs_meta = load_jsonl("meta/documents.jsonl")
    listed = {d["local_path"] for d in docs_meta}
    missing = [p for p in sorted(listed) if not os.path.exists(os.path.join(ROOT, p))]
    on_disk = set()
    for dirpath, _, files in os.walk(os.path.join(ROOT, "docs")):
        for fn in files:
            if fn.endswith(".md"):
                on_disk.add(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    orphans = sorted(on_disk - listed)
    if missing:
        fails.append(f"[1] documents.jsonl 里 {len(missing)} 篇文件缺失，如 {missing[:3]}")
    if orphans:
        fails.append(f"[1] docs/ 下 {len(orphans)} 个孤儿文件不在 documents.jsonl，如 {orphans[:3]}")
    if not missing and not orphans:
        print(f"  [1] OK  docs/ {len(on_disk)} 篇 ↔ documents.jsonl 双向一致")
    kb = load_jsonl("meta/kb_manifest.jsonl")
    kbset = {r["local_path"] for r in kb}
    if kbset != listed:
        fails.append(f"[2] kb_manifest 覆盖面与 documents 不一致（差 {len(kbset ^ listed)} 篇），重跑 compile_qa_kb.py")
    else:
        print(f"  [2] OK  kb_manifest 覆盖 {len(kbset)} 篇")
    return docs_meta


def check_generated():
    # [8b] 实体表行数地板:漂移检查(空 vs 空也一致)拦不住"一致地错",
    # 2026-08-31 实录:上游 tab 命名加空格致 api/jsapi/permission 连续两周为空,lint 全绿。
    floors = {"api.jsonl": 800, "errcode.jsonl": 1500, "event.jsonl": 100,
              "jsapi.jsonl": 400, "permission.jsonl": 150}
    for fn, floor in floors.items():
        fp = os.path.join(ROOT, "graph", fn)
        n = sum(1 for _ in open(fp, encoding="utf-8")) if os.path.exists(fp) else 0
        if n < floor:
            fails.append(f"[8b] graph/{fn} 仅 {n} 行(地板 {floor}):实体抽取疑似整体失效")
        else:
            print(f"  [8b] OK  graph/{fn} {n} 行(≥{floor})")

    for name, script in (("[3] index", "build_index.py"), ("[4] graph/links", "build_links.py"),
                         ("[8] kb_manifest", "compile_qa_kb.py"), ("[8] graph五表", "build_qa_index.py")):
        r = subprocess.run(["python3", os.path.join(SCRIPTS, script), "--check"],
                           capture_output=True, text=True, cwd=ROOT)
        if r.returncode != 0:
            fails.append(f"{name} 漂移：{r.stdout.strip().splitlines()[-1] if r.stdout else script}")
        else:
            print("  " + name + " OK  " + (r.stdout.strip().splitlines()[-1] if r.stdout else ""))


def check_evals_refs():
    p = os.path.join(ROOT, "evals", "questions.jsonl")
    if not os.path.exists(p):
        return
    missing = []
    for line in open(p, encoding="utf-8"):
        q = json.loads(line)
        for ref in q.get("ref_docs", []):
            if not os.path.exists(os.path.join(ROOT, ref)):
                missing.append(f"{q['id']}:{os.path.basename(ref)}")
    if missing:
        fails.append(f"[9] evals ref_docs 失效 {len(missing)} 条（快照重编号后未按 slug 重映射）：{missing[:5]}")
    else:
        print("  [9] OK  evals ref_docs 全部可达")


def check_entry_links():
    targets = ["README.md", "AGENTS.md", "CLAUDE.md", os.path.join("index", "TOPICS.md"),
               os.path.join("graph", "GRAPH.md"), os.path.join("ops", "INGEST.md")]
    if not os.access(os.path.join(ROOT, "bin", "dkdoc"), os.X_OK):
        warns.append("[5] bin/dkdoc 缺失或不可执行")
    bad = []
    for rel in targets:
        fp = os.path.join(ROOT, rel)
        if not os.path.exists(fp):
            warns.append(f"[5] 入口文件缺失：{rel}")
            continue
        base = os.path.dirname(fp)
        for text, target in RE_LINK.findall(open(fp, encoding="utf-8").read()):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            t = os.path.normpath(os.path.join(base, target.split("#")[0]))
            if not os.path.exists(t):
                bad.append(f"{rel} -> {target}")
    if bad:
        fails.append(f"[5] 入口文件断链 {len(bad)} 条：{bad[:5]}")
    else:
        print("  [5] OK  入口文件（README/AGENTS/CLAUDE/TOPICS/GRAPH/INGEST）链接可达")


def check_tombstones(docs_meta):
    ts = load_jsonl("meta/tombstones.jsonl")
    if ts is None:
        print("  [6] OK  暂无 tombstone")
        return
    alive = {d.get("doc_id") for d in docs_meta}
    back = [t for t in ts if t.get("doc_id") in alive]
    if back:
        warns.append(f"[6] {len(back)} 个 tombstone 文档又出现在 documents.jsonl（复活？确认后清理 tombstone 该行）")
    else:
        print(f"  [6] OK  {len(ts)} 条 tombstone 均已不在现役集合")


def check_graph_tables():
    bad = 0
    for table, field in (("api.jsonl", "doc_path"), ("event.jsonl", "doc_path"), ("jsapi.jsonl", "doc_path")):
        for r in load_jsonl(os.path.join("graph", table)) or []:
            p = r.get(field)
            if p and not os.path.exists(os.path.join(ROOT, p)):
                bad += 1
    for r in load_jsonl(os.path.join("graph", "permission.jsonl")) or []:
        for a in r.get("current_apis", []):
            if a.get("doc_path") and not os.path.exists(os.path.join(ROOT, a["doc_path"])):
                bad += 1
    if bad:
        warns.append(f"[7] graph/ 表引用了 {bad} 个不存在的 doc_path，重跑 build_qa_index.py")
    else:
        print("  [7] OK  graph/ 表引用的文档全部存在")


def main():
    print("open-platform-wiki lint：")
    docs_meta = check_docs_meta()
    check_generated()
    check_entry_links()
    check_tombstones(docs_meta)
    check_graph_tables()
    check_evals_refs()
    print()
    for w in warns:
        print("WARN " + w)
    for f_ in fails:
        print("FAIL " + f_)
    if fails:
        print(f"\n结果：{len(fails)} 项失败，{len(warns)} 项警告。修复走 ops/INGEST.md，不要手改生成物。")
        return 1
    print(f"结果：通过（{len(warns)} 项警告）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
