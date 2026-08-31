#!/usr/bin/env python3
"""从 meta/documents.jsonl + meta/kb_manifest.jsonl 全量重建 index/ 三级索引。

产出（全部是生成物，勿手改；手改会被下次重建覆盖，且 lint --check 会报漂移）：
  index/INDEX.md                     L1 总索引：8 大类 26 子类 + 路由提示
  index/<NN-大类>/<NN-子类>.md        L2 子类索引：该 tab 全部文档一行一篇
  index/<NN-大类>/<NN-子类>/          大 tab（>SPLIT 篇）拆为目录：
      _index.md                        L2 功能域列表
      <NN-功能域>.md                   L3 域内文档清单
index/TOPICS.md 是人工/LLM 维护的认知层页面，本脚本永不触碰。

用法:
  python3 ops/scripts/build_index.py           # 重建
  python3 ops/scripts/build_index.py --check   # 只比对不落盘，漂移则退出码 1


【bin 工具数据契约】bin/dkdoc(含 ctx)依赖流水线产物的以下字段,改动前先同步 bin 并跑冒烟:
  meta/documents.jsonl: local_path/slug/title/breadcrumb/headings/snippet/source_url/updated_at
  meta/kb_manifest.jsonl: local_path/tier/deprecated
  graph/{api,errcode,event,jsapi,permission,links}.jsonl: 各表既有列(见 dkdoc 各 cmd_*)
冒烟由 kb_pipeline.sh 在 push 前执行(dkdoc find 免登 + dkdoc ctx 免登)。"""
import argparse
import collections
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IDX = os.path.join(ROOT, "index")
SPLIT = 200          # tab 文档数超过该值则按 breadcrumb[0] 功能域拆 L3
HIST = "历史文档（不推荐）"
PRESERVE = {"TOPICS.md"}  # index/ 下不归本脚本管的文件

GROUP_DESC = {
    "应用开发": "钉钉应用（小程序/H5/机器人/酷应用）开发主线：概念、服务端 API、前端 JSAPI、事件订阅、CLI 与工具。绝大多数开发问题落在这里。",
    "连接平台": "第三方系统与钉钉互通：连接器、触发器/执行器、自动化流。",
    "AI PaaS": "AI 助理（AI Assistant）与大模型开放能力。",
    "硬件开发": "智能硬件（考勤机/门禁等）固件协议接入，独立技术栈。",
    "互动卡片": "IM 互动卡片：模板搭建、创建投放、更新、AI 卡片。",
    "专属版客户端插件": "专属钉钉客户端原生插件（Android/iOS/Win 独立技术栈，一般开发答疑不涉及）。",
    "数据资产": "宜数（智能问数）与数据大屏，后台操作教程为主。",
    "工作台": "企业工作台配置、装修与组件。",
}

TAB_HINTS = {
    ("应用开发", "开发指南"): "平台基础概念、ID/凭证体系、应用类型选型、免登、获取 access_token、快速上手、安全合规",
    ("应用开发", "服务端API"): "REST OpenAPI 全集（新版 api.dingtalk.com 与旧版 oapi.dingtalk.com）：通讯录、消息、文档、审批、考勤、日程等功能域",
    ("应用开发", "客户端JSAPI"): "小程序/H5 前端 JSAPI：jsapi 鉴权（jsapi_ticket）、容器能力、界面、设备、选人、地图支付等",
    ("应用开发", "事件订阅"): "业务事件回调：Stream 模式与 HTTP 回调两种接入方式 + 各业务域事件字段明细",
    ("应用开发", "钉钉CLI"): "dingtalk-cli 脚手架：初始化、本地调试、构建与发布小程序/H5",
    ("应用开发", "开发工具"): "小程序开发者工具、API Explorer、IDE 插件等调试辅助",
    ("应用开发", "平台服务"): "服务商入驻、协议、计费、应用市场运营规则（非开发向）",
    ("连接平台", "平台介绍"): "连接平台定位、能力与开通方式",
    ("连接平台", "开发指南"): "连接器开发全流程：认证配置、数据模型、触发器与执行器",
    ("连接平台", "连接器中心"): "官方连接器目录与逐个配置说明",
    ("连接平台", "连接平台自动化"): "自动化流程（流程编排）搭建与使用",
    ("AI PaaS", "平台介绍"): "AI PaaS 整体架构与接入方式",
    ("AI PaaS", "炼丹炉大模型平台"): "模型训练/部署平台",
    ("AI PaaS", "AI 助理创建平台"): "AI 助理创建、角色设定、能力/工作流/知识配置、AI 卡片发消息、RPA 拟人操作",
    ("AI PaaS", "AI 客服助理"): "AI 客服助理产品说明",
    ("硬件开发", "智能硬件"): "智能硬件接入：固件、协议、设备管理",
    ("互动卡片", "开发指南"): "卡片模板搭建与发布、卡片实例创建/投放、事件回调、动态数据源、卡片更新",
    ("互动卡片", "卡片模板搭建器"): "可视化搭建器：面板、变量绑定与协议（Markdown/图表/表格/表单）、条件/循环渲染、交互组件",
    ("互动卡片", "互动卡片搭建平台"): "旧版卡片搭建平台（存量）",
    ("互动卡片", "卡片规范设计"): "设计规范、链接跳转规范、钉钉表情列表、宽屏卡片",
    ("专属版客户端插件", "功能介绍"): "端侧插件能力总览",
    ("专属版客户端插件", "插件开发"): "Android/iOS/Windows 原生插件开发",
    ("数据资产", "平台介绍"): "数据资产平台与大屏搭建教学",
    ("数据资产", "宜数（智能问数）"): "宜数配置：数据管理、调优、权限",
    ("工作台", "平台介绍"): "工作台开通方式与服务商渠道",
    ("工作台", "使用教程"): "工作台装修、组件配置教程",
}

LEGEND = "标记：`⚠归档` = 历史文档/不推荐（接口多数仍可调用，但优先用现行版）；`◇边缘` = 商务/运营/端侧等非开发答疑内容。"


def sanitize(name: str) -> str:
    return re.sub(r"[/\\:：]+", "·", re.sub(r"\s+", "", name))


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def parse_dirs(local_path):
    # docs/<NN-大类>/<NN-code-子类>/<NNNN-slug>.md
    parts = local_path.split("/")
    return parts[1], parts[2]  # gdir, tdir


def nn_of(dirname):
    m = re.match(r"^(\d+)-", dirname)
    return m.group(1) if m else "99"


def doc_line(d, kb, from_dir, drop_crumb0=False):
    rel = os.path.relpath(d["local_path"], from_dir)
    crumb = list(d.get("breadcrumb") or [])
    if crumb and crumb[-1] == d["title"]:
        crumb = crumb[:-1]
    if drop_crumb0 and crumb:
        crumb = crumb[1:]
    s = f"- [{d['title']}]({rel})"
    if crumb:
        s += " · " + " › ".join(crumb)
    s += f" · {d['updated_at'][:10]}"
    k = kb.get(d["local_path"])
    if k:
        if k["tier"] == "T2" or k.get("deprecated"):
            s += " ⚠归档"
        elif k["tier"] == "DROP":
            s += " ◇边缘"
    return s


def build(docs, kb):
    """返回 {index/ 相对路径: 内容} 的 dict。"""
    out = {}
    # 按 (大类, 子类) 分桶，保持官方目录树顺序（local_path 内的 NNNN 前缀即树序）
    tabs = collections.OrderedDict()
    for d in sorted(docs, key=lambda x: x["local_path"]):
        gdir, tdir = parse_dirs(d["local_path"])
        tabs.setdefault((gdir, tdir), []).append(d)

    groups = collections.OrderedDict()
    for (gdir, tdir), items in sorted(tabs.items(), key=lambda kv: (nn_of(kv[0][0]), nn_of(kv[0][1]))):
        groups.setdefault(gdir, []).append((tdir, items))

    l1 = ["# 钉钉开放平台文档 · 总索引", ""]
    l1.append(f"> 快照范围：{sum(len(v) for v in tabs.values())} 篇 · {len(groups)} 大类 · {len(tabs)} 子类。")
    l1.append("> 用法：按大类 → 子类打开对应索引文件，按标题/面包屑定位文档；找不到再全文 `rg 关键词 docs/`。")
    l1.append("> 精确实体（API 接口/错误码/事件名/权限点）不要走目录，直接查 `graph/` 四张表（见 graph/GRAPH.md）。")
    l1.append("> 高频问题的权威文档入口见 [TOPICS.md](TOPICS.md)。")
    l1.append(">")
    l1.append(f"> {LEGEND}")
    l1.append("")

    for gdir, tablist in groups.items():
        gname = tablist[0][1][0]["group"]
        gcount = sum(len(items) for _, items in tablist)
        l1.append(f"## {gdir}（{gcount} 篇）")
        l1.append("")
        desc = GROUP_DESC.get(gname)
        if desc:
            l1.append(desc)
            l1.append("")
        for tdir, items in tablist:
            tname = items[0]["tab"]
            nn = nn_of(tdir)
            fname = f"{nn}-{sanitize(tname)}"
            hint = TAB_HINTS.get((gname, tname), "")
            arch = sum(1 for d in items if kb.get(d["local_path"], {}).get("tier") == "T2")
            drop = sum(1 for d in items if kb.get(d["local_path"], {}).get("tier") == "DROP")
            note = f"{len(items)} 篇"
            if arch:
                note += f"，含 {arch} 篇归档"
            if drop == len(items):
                note += "，整类◇边缘"
            if len(items) > SPLIT:
                link = f"{gdir}/{fname}/_index.md"
            else:
                link = f"{gdir}/{fname}.md"
            l1.append(f"- [{tname}]({link})（{note}）— {hint}")

            # ---- L2 / L3 ----
            if len(items) > SPLIT:
                # 按 breadcrumb[0] 功能域拆分，保持首次出现顺序
                domains = collections.OrderedDict()
                for d in items:
                    crumb = d.get("breadcrumb") or []
                    dom = crumb[0] if crumb else "未分类"
                    domains.setdefault(dom, []).append(d)
                tab_dir = f"{gdir}/{fname}"
                sub = [f"# {gname} / {tname} · 功能域索引", ""]
                sub.append(f"> {len(items)} 篇，按官方目录第一级拆为 {len(domains)} 个功能域。{hint}。")
                sub.append(f"> 找具体接口优先用 `graph/`（api/errcode/event/permission 四张表）；全文检索 `rg 关键词 docs/{gdir}/{tdir}/`。")
                sub.append(">")
                sub.append(f"> {LEGEND}")
                sub.append("")
                for i, (dom, dd) in enumerate(domains.items(), 1):
                    dfname = f"{i:02d}-{sanitize(dom)}.md"
                    darch = sum(1 for d in dd if kb.get(d["local_path"], {}).get("tier") == "T2")
                    dnote = f"{len(dd)} 篇"
                    if darch == len(dd):
                        dnote += "，全部⚠归档"
                    sub.append(f"- [{dom}]({dfname})（{dnote}）")
                    dom_from = f"index/{tab_dir}"
                    l3 = [f"# {tname} / {dom}", ""]
                    l3.append(f"> {len(dd)} 篇 · 上级：[{tname} 功能域索引](_index.md)")
                    l3.append("")
                    for d in dd:
                        l3.append(doc_line(d, kb, dom_from, drop_crumb0=True))
                    out[f"{tab_dir}/{dfname}"] = "\n".join(l3) + "\n"
                out[f"{tab_dir}/_index.md"] = "\n".join(sub) + "\n"
            else:
                from_dir = f"index/{gdir}"
                l2 = [f"# {gname} / {tname}", ""]
                l2.append(f"> {len(items)} 篇 · {hint}。上级：[总索引](../INDEX.md)")
                l2.append("")
                for d in items:
                    l2.append(doc_line(d, kb, from_dir))
                out[f"{gdir}/{fname}.md"] = "\n".join(l2) + "\n"
        l1.append("")

    l1.append("---")
    l1.append("本文件及本目录（TOPICS.md 除外）由 `ops/scripts/build_index.py` 生成，勿手改。")
    out["INDEX.md"] = "\n".join(l1) + "\n"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只比对不落盘，漂移退出码 1")
    args = ap.parse_args()

    docs = load_jsonl(os.path.join(ROOT, "meta", "documents.jsonl"))
    kb = {r["local_path"]: r for r in load_jsonl(os.path.join(ROOT, "meta", "kb_manifest.jsonl"))}
    out = build(docs, kb)

    if args.check:
        drift = []
        on_disk = set()
        for dirpath, _, files in os.walk(IDX):
            for fn in files:
                p = os.path.relpath(os.path.join(dirpath, fn), IDX)
                if p in PRESERVE or fn.startswith("."):
                    continue
                on_disk.add(p)
        for p, content in out.items():
            fp = os.path.join(IDX, p)
            if not os.path.exists(fp):
                drift.append(f"缺失: index/{p}")
            elif open(fp, encoding="utf-8").read() != content:
                drift.append(f"内容漂移: index/{p}")
        for p in on_disk - set(out):
            drift.append(f"多余（生成器不认识）: index/{p}")
        if drift:
            print("[build_index --check] 索引与元数据不一致，需重跑 build_index.py：")
            for d in drift[:50]:
                print("  " + d)
            return 1
        print(f"[build_index --check] OK：{len(out)} 个索引文件与元数据一致")
        return 0

    # 重建：清掉旧生成物（保留 PRESERVE），再写入
    if os.path.isdir(IDX):
        for entry in os.listdir(IDX):
            if entry in PRESERVE or entry.startswith("."):
                continue
            p = os.path.join(IDX, entry)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    for p, content in out.items():
        fp = os.path.join(IDX, p)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
    print(f"[build_index] 重建完成：{len(out)} 个索引文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
