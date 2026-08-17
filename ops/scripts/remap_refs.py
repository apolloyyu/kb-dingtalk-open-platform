#!/usr/bin/env python3
"""按 slug 重映射认知层引用(index/TOPICS.md 链接与 evals/questions.jsonl 的 ref_docs)。

上游快照有插入时,同目录后续文档的 NNNN- 序号整体顺移,认知层引用的带序号路径随之
失效(2026-08-17 流水线首跑即断 5 条)。序号只是排序展示前缀,slug(去序号文件名)
才是稳定身份——本脚本把失效引用按 slug 找回现路径做机械替换;slug 消失(真删除)或
一 slug 对多文件(歧义)时不动,留给 lint 报错走人工。幂等,可重复执行。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def build_maps():
    by_slug, fnames = {}, set()
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, "docs")):
        for f in files:
            if not f.endswith(".md"):
                continue
            fnames.add(f)
            slug = re.sub(r"^\d{4}-", "", f)
            rel = os.path.relpath(os.path.join(dirpath, f), ROOT).replace(os.sep, "/")
            by_slug.setdefault(slug, []).append(rel)
    return by_slug, fnames


def fix_topics(by_slug):
    p = os.path.join(ROOT, "index", "TOPICS.md")
    text = open(p, encoding="utf-8").read()
    fixed = []

    def repl(match):
        target = match.group(1)  # ../docs/....md
        if os.path.exists(os.path.normpath(os.path.join(ROOT, "index", target))):
            return match.group(0)
        slug = re.sub(r"^\d{4}-", "", os.path.basename(target))
        cand = by_slug.get(slug) or []
        if len(cand) != 1:
            return match.group(0)  # 歧义或已删除:不动,留给 lint
        fixed.append((target, cand[0]))
        return "(../" + cand[0] + ")"

    new = re.sub(r"\((\.\./docs/[^)]+?\.md)\)", repl, text)
    if fixed:
        open(p, "w", encoding="utf-8").write(new)
    return fixed


def fix_evals(by_slug, fnames):
    p = os.path.join(ROOT, "evals", "questions.jsonl")
    if not os.path.exists(p):
        return []
    fixed, out = [], []
    for line in open(p, encoding="utf-8"):
        s = line.rstrip("\n")
        try:
            o = json.loads(s)
        except ValueError:
            out.append(s)
            continue
        refs = o.get("ref_docs")
        if isinstance(refs, list):
            nr = []
            for r in refs:
                base = os.path.basename(str(r))
                if base not in fnames:
                    slug = re.sub(r"^\d{4}-", "", base)
                    cand = by_slug.get(slug) or []
                    if len(cand) == 1:
                        nb = os.path.basename(cand[0])
                        fixed.append((base, nb))
                        r = str(r).replace(base, nb)
                nr.append(r)
            o["ref_docs"] = nr
            s = json.dumps(o, ensure_ascii=False)
        out.append(s)
    if fixed:
        open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return fixed


def main():
    by_slug, fnames = build_maps()
    t = fix_topics(by_slug)
    e = fix_evals(by_slug, fnames)
    for old, new in t:
        print(f"TOPICS: {os.path.basename(old)} -> {os.path.basename(new)}")
    for old, new in e:
        print(f"evals:  {old} -> {new}")
    print(f"重映射完成:TOPICS {len(t)} 条,evals {len(e)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
