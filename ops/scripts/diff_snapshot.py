#!/usr/bin/env python3
"""新快照对账：把重跑爬虫得到的新快照与本库当前快照按稳定 ID 对比，产出变更清单；--apply 一键换层重编。

原则（见 ops/INGEST.md）：
  - 文档身份 = doc_id（钉钉文档树的稳定 ID），不是 URL、不是文件路径
  - 变更判定 = html_sha256 内容指纹，updated_at 仅作展示
  - 删除不是静默消失：写入 meta/tombstones.jsonl 留档（tombstone）
  - 索引/图谱是派生物：apply 后全量重建，不做增量修补，避免漂移

用法:
  python3 ops/scripts/diff_snapshot.py <新快照目录>            # 只出报告
  python3 ops/scripts/diff_snapshot.py <新快照目录> --apply    # 换入新快照 + 重建全部派生层 + lint
新快照目录 = tools/build_dingtalk_open_docs_kb.py 重跑的产物根目录（含 docs/ 与 metadata/documents.jsonl）。
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS = os.path.join(ROOT, "ops", "scripts")


def load_docs(base):
    for rel in ("metadata/documents.jsonl", "meta/documents.jsonl"):
        p = os.path.join(base, rel)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                return [json.loads(line) for line in f], os.path.dirname(p)
    sys.exit(f"找不到 {base} 下的 metadata|meta/documents.jsonl")


def key_of(d):
    return d.get("doc_id") or f'{d["namespace"]}/{d["slug"]}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("snapshot", help="新快照根目录")
    ap.add_argument("--apply", action="store_true", help="应用变更：换 docs/ 与 meta/，写 tombstone，重建派生层")
    args = ap.parse_args()

    old_docs, _ = load_docs(ROOT)
    new_docs, new_meta_dir = load_docs(args.snapshot)
    old = {key_of(d): d for d in old_docs}
    new = {key_of(d): d for d in new_docs}

    added = [new[k] for k in new.keys() - old.keys()]
    deleted = [old[k] for k in old.keys() - new.keys()]
    updated, moved = [], []
    for k in old.keys() & new.keys():
        o, n = old[k], new[k]
        if o.get("html_sha256") != n.get("html_sha256"):
            updated.append((o, n))
        elif o["local_path"] != n["local_path"]:
            moved.append((o, n))

    today = datetime.date.today().isoformat()
    label = os.path.basename(os.path.normpath(args.snapshot))
    lines = [f"# 快照对账 {today}", ""]
    lines.append(f"- 旧：{len(old)} 篇（本库 meta/documents.jsonl）")
    lines.append(f"- 新：{len(new)} 篇（{args.snapshot}）")
    lines.append(f"- 新增 {len(added)} / 更新 {len(updated)} / 移动 {len(moved)} / 删除 {len(deleted)}")
    lines.append("")
    if added:
        lines.append("## 新增")
        for d in sorted(added, key=lambda x: x["local_path"]):
            lines.append(f"- [{d['title']}]({d['local_path']}) · {d['group']}/{d['tab']} · {d['updated_at'][:10]}")
        lines.append("")
    if updated:
        lines.append("## 内容更新")
        for o, n in sorted(updated, key=lambda x: x[1]["local_path"]):
            lines.append(f"- [{n['title']}]({n['local_path']}) · {o['updated_at'][:10]} → {n['updated_at'][:10]}")
        lines.append("")
    if moved:
        lines.append("## 目录位置移动（内容未变）")
        for o, n in sorted(moved, key=lambda x: x[1]["local_path"]):
            lines.append(f"- {o['local_path']} → {n['local_path']}")
        lines.append("")
    if deleted:
        lines.append("## 删除（已写 tombstone，源站已下线或移出目录树）")
        for d in sorted(deleted, key=lambda x: x["local_path"]):
            lines.append(f"- {d['title']} · {d['source_url']} · 最后见于 {d['local_path']}")
        lines.append("")
    lines.append("## 后续动作")
    lines.append("- 结构层（index/ graph/ meta/kb_manifest）：--apply 已全量重建；未 --apply 则本报告仅供预览。")
    lines.append("- 认知层（index/TOPICS.md）：对照上面清单，凡命中 TOPICS 引用的文档（可用 `rg <path> index/TOPICS.md` 与 `graph/links.jsonl` 反查），由 LLM 复核该主题条目是否要改写。")
    report = "\n".join(lines) + "\n"

    os.makedirs(os.path.join(ROOT, "ops", "changes"), exist_ok=True)
    rp = os.path.join(ROOT, "ops", "changes", f"{today}-{label}.md")
    with open(rp, "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    print(f"报告已写入 {os.path.relpath(rp, ROOT)}")

    if not args.apply:
        return 0

    # ---- 应用：原始层整体换成新快照（镜像语义），删除留 tombstone ----
    if deleted:
        tp = os.path.join(ROOT, "meta", "tombstones.jsonl")
        with open(tp, "a", encoding="utf-8") as f:
            for d in deleted:
                f.write(json.dumps({
                    "deleted_at": today, "doc_id": d.get("doc_id"),
                    "title": d["title"], "source_url": d["source_url"],
                    "namespace": d["namespace"], "slug": d["slug"],
                    "last_local_path": d["local_path"], "last_updated_at": d["updated_at"],
                }, ensure_ascii=False) + "\n")
        print(f"tombstone 追加 {len(deleted)} 条 → meta/tombstones.jsonl")

    subprocess.run(["rsync", "-a", "--delete",
                    os.path.join(args.snapshot, "docs") + "/",
                    os.path.join(ROOT, "docs") + "/"], check=True)
    for fn in ("documents.jsonl", "failures.json", "groups.json"):
        src = os.path.join(new_meta_dir, fn)
        if os.path.exists(src):
            subprocess.run(["cp", src, os.path.join(ROOT, "meta", fn)], check=True)
    sm = os.path.join(args.snapshot, "MANIFEST.json")
    if os.path.exists(sm):
        subprocess.run(["cp", sm, os.path.join(ROOT, "meta", "source_manifest.json")], check=True)
    ua = os.path.join(args.snapshot, "UNAVAILABLE.md")
    if os.path.exists(ua):
        subprocess.run(["cp", ua, os.path.join(ROOT, "meta", "UNAVAILABLE.md")], check=True)
    print("原始层已换入新快照")

    # ---- 派生层全量重建 ----
    for cmd in (["python3", os.path.join(SCRIPTS, "compile_qa_kb.py")],
                ["python3", os.path.join(SCRIPTS, "build_qa_index.py")],
                ["python3", os.path.join(SCRIPTS, "build_cards.py")],
                ["python3", os.path.join(SCRIPTS, "build_term_index.py")],
                ["python3", os.path.join(SCRIPTS, "build_index.py")],
                ["python3", os.path.join(SCRIPTS, "build_links.py")],
                ["python3", os.path.join(SCRIPTS, "lint.py")]):
        print("$ " + " ".join(os.path.relpath(c, ROOT) if os.path.sep in c else c for c in cmd))
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode != 0 and "lint" not in cmd[1]:
            sys.exit(f"重建失败：{cmd}")

    # 根 MANIFEST.json 更新快照信息
    mp = os.path.join(ROOT, "MANIFEST.json")
    if os.path.exists(mp):
        m = json.load(open(mp, encoding="utf-8"))
        try:
            sm_data = json.load(open(os.path.join(ROOT, "meta", "source_manifest.json"), encoding="utf-8"))
            m["snapshot"] = {"crawl_time": sm_data.get("crawl_time"), "documents": len(new),
                             "applied_at": today, "diff_report": os.path.relpath(rp, ROOT)}
        except Exception:
            m["snapshot"] = {"applied_at": today, "documents": len(new)}
        json.dump(m, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("完成。别忘了：1) 复核 index/TOPICS.md（见报告『后续动作』）；2) git commit 让 Diff 可追溯。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
