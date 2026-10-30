#!/usr/bin/env python3
"""dkdoc ctx 快路径与证据边界回归测试（不访问网络，不修改生成物）。"""
import io
import os
import runpy
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DKDOC = os.path.join(ROOT, "bin", "dkdoc")
MOD = runpy.run_path(DKDOC, run_name="dkdoc_test_module")


def check(ok, message):
    if not ok:
        raise AssertionError(message)


def intent(query):
    return MOD["_intent"]([query])


def run(*args, env=None):
    child_env = os.environ.copy()
    child_env.update(env or {})
    result = subprocess.run(["python3", DKDOC, *args], cwd=ROOT, env=child_env,
                            capture_output=True, text=True, timeout=30)
    check(result.returncode == 0, f"命令失败 {args}: {result.stderr or result.stdout}")
    return result.stdout


def first_body_heading(output):
    return next((line for line in output.splitlines() if line.startswith("== 正文[1/")), "")


def main():
    simple = intent("通过免登码获取用户信息的接口地址和必填参数是什么")
    check(not any(simple.values()), f"简单 API 契约题被误拦截: {simple}")
    check(not intent("获取 access_token 接口")["truncated"],
          "包含字段名的正常检索短语被误判为截断输入")

    cases = {
        "why": "为什么这个接口会返回参数错误",
        "error": "调用接口报错 PARAM_ERROR 怎么排查",
        "support": "这个接口能不能支持批量查询",
        "ui": "priority 为什么会进入客户端优先处理分栏",
        "stage": "鉴权请求中的 $.Body.access_token 能否在执行动作入参映射里读取",
        "id_format": "这个 processInstanceId 看起来不像 UUID，是不是无效 ID",
        "lifecycle": "Page 生命周期函数的触发顺序是什么",
        "enumeration": "列出 Page 支持的全部事件",
        "truncated": "{\"userid_list\":\"538079528\",\"msg\":{\"oa\":",
    }
    for flag, query in cases.items():
        got = intent(query)
        check(got.get(flag), f"未识别 {flag}: {query} -> {got}")

    out = run("ctx", "通过免登码获取用户信息的接口地址和必填参数是什么")
    check("card=1(fast=1)" in out, "简单强锚点 API 题未走 full card 快路径")
    check("== 证据契约 ==" in out and "mode: card-only" in out,
          "快路径未输出 card-only 证据契约")
    check("字段存在不等于它决定产品行为" in out, "证据契约缺少产品行为边界")

    out = run("ctx", "为什么通过免登码获取用户信息会报错")
    check("card=1(fast=0)" in out, "因果/报错题未退出 card-only 快路径")
    check("mode: full-context-required" in out, "回退题未声明全文上下文模式")
    check("card_blocked=" in out and "why" in out and "error" in out,
          "检索审计未记录快路径阻断原因")

    q13 = """https://open.dingtalk.com/document/development/asynchronous-sending-of-enterprise-session-messages?debug=true
{
    \"agent_id\": 3940723895,
    \"userid_list\": \"538079528\",
    \"msg\": {\"oa\":"""
    out = run("ctx", q13)
    check("发送工作通知" in first_body_heading(out),
          "source_url + 截断 JSON 未锚定发送工作通知正文")
    check("card=1(fast=0)" in out and "card_blocked=truncated" in out,
          "截断报文没有稳定阻断 card-only")
    check("api=1" in out and "api=1364" not in out,
          "URL/标点/布尔值仍污染 API 实体检索")

    q75 = "设置鉴权请求参数怎么在执行动作获取相关参数，我需要在配置映射规则编写代码获取"
    out = run("ctx", q75)
    check("执行动作入参设置" in first_body_heading(out),
          "跨阶段指南题未优先执行动作入参正文")
    check("== 正文[2/3] Token鉴权" in out,
          "跨阶段指南题未同时展开 Token 鉴权正文")
    check("批量获取加班规则设置" not in first_body_heading(out),
          "通用请求/参数词仍让加班 API 抢占首篇")
    check("api=0" in out and "card=0(fast=0)" in out
          and "card_blocked=semantic,stage" in out,
          "跨阶段指南题仍被 API 卡或快路径劫持")

    out = run("ctx", "如何在钉钉管理后台免登？")
    expected_flow = (
        "== 正文[1/3] 应用管理后台免登",
        "== 正文[2/3] 获取微应用后台免登的accessToken",
        "== 正文[3/3] 获取应用管理后台免登的用户信息",
    )
    check(all(marker in out for marker in expected_flow),
          "管理后台免登流程未完整展开教程、accessToken 和用户信息三篇正文")
    check("card=1(fast=0)" in out and "card_blocked=semantic" in out,
          "多步骤免登流程没有稳定阻断 card-only")

    out = run("ctx", "--full", "通过免登码获取用户信息的接口地址和必填参数是什么")
    check("card=0(fast=0)" in out and "mode: full-context-required" in out,
          "ctx --full 没有稳定跳过答案卡")
    check("card_blocked=forced_full" in out, "--full 审计未标 forced_full 原因")
    out = run("ctx", "通过免登码获取用户信息的接口地址和必填参数是什么",
              env={"KB_NO_CARDS": "1"})
    check("card=0(fast=0)" in out and "mode: full-context-required" in out,
          "KB_NO_CARDS=1 没有稳定跳过答案卡")
    check("card_blocked=cards_disabled" in out, "KB_NO_CARDS=1 审计未标 cards_disabled 原因")

    out = run("ctx", "创建筛选视图 filterType 参数可选值是什么")
    check("fast=0" in out and "enumeration" in out,
          "「参数可选值」枚举问法未阻断 card-only 快路径")

    out = run("ctx", "如何使用 https://open.dingtalk.com/document/development/"
                     "obtain-the-userid-of-a-user-by-using-the-log-free")
    check("fast=0" in out and "semantic" in out and "== 正文[" in out,
          "URL 锚点 + 用法问句绕过了全文路由（须展开正文示例）")

    out = run("ctx", "Document.Document.Read 这个权限要怎么开通")
    check("添加接口调用权限" in out,
          "权限开通类问题未带入通用「添加接口调用权限」指南篇")

    out = run("ctx", "为什么如何在钉钉管理后台免登？")
    check(out.count("== 正文[") >= 2,
          "流程题总量超限后正文退化到少于 2 篇（丢配置阶段）")

    out = run("ctx", "钉钉小程序的page有哪些事件")
    check("fast=0" in out and "enumeration" in out, "Page 事件枚举题未阻断快路径")
    check("== 正文[1/" in out and "页面配置" in out.split("== 正文[1/", 1)[1][:120],
          "域限定词只在归档区命中时未提升归档篇（小程序 Page 被跨域文档顶掉）")
    check("onLoad" in out and "onShow" in out,
          "Page 事件枚举证据（onLoad/onShow）未进入正文")

    out = run("ctx", "carddata从哪里获取")
    check("cardParamMap" in out and out.count("== 正文[") <= 2 and len(out) < 12000,
          "正文标识符索引未让 cardData 一次命中含 cardParamMap 的正文（或上下文未按实体题收紧）")
    out = run("ctx", "钉钉小程序的路由层级有限制吗")
    check("navigateTo" in out, "IDF 权重后小程序路由题仍未命中 navigateTo 正文")
    out = run("ctx", "通过免登码获取用户信息的接口地址和必填参数是什么")
    check("card=1(fast=1)" in out, "IDF/标识符索引改动后简单强锚点 API 题失去快路径")

    out = run("ctx", "如何获取钉钉群消息的聊天图片")
    check("messageFiles/download" in out or "downloadCode" in out,
          "概念别名(聊天图片→downloadCode)未把机器人接收消息/文件下载文档带入上下文")
    out = run("ctx", "钉钉知识库正文是否有接口")
    check("否定前必读" in out and "块元素" in out.split("== 证据契约 ==", 1)[0],
          "支持性题未前置存在性清单或未命中查询块元素")
    out = run("ctx", "钉钉小程序 离开页面二次确认")
    check("archived_only" in out and "离开二次确认配置" in out,
          "归档独有主题未提示「归档页即依据」")
    out = run("ctx", "机器人发送单聊消息给用户的文档,参数有哪些")
    check("API参数卡" in out and "msgParam" in out,
          "参数枚举题未附教程正链 API 参数卡(msgParam 缺失)")
    out = run("ctx", "https://open.dingtalk.com/document/development/user-information-update?debug=true\n这个接口的 \"dept_position_list\": [\n739566083,\n\"资深产品经理\"\n]")
    check("card=1(fast=0)" in out and "payload" in out,
          "用户贴出闭合 JSON 报文仍走 card-only")

    out = run("ctx", "钉钉服务端 API 的 QPS 和每月调用量限制是多少")
    check("整条逐字照抄，禁止解码成 url= 内嵌地址" in out and "禁止只留文字不给链接" in out, "证据契约缺少链接原样引用纪律")
    out = run("cat", "how-to-process-api-throttling-on-the-dingtalk-server")
    check("dingtalk://dingtalkclient/page/link?url=" in out and "${corpId}" in out and "钉钉专业版" in out,
          "正文中的 dingtalk:// 深链须逐字原样保留(实录:解码成内嵌 html 地址后 ${corpId} 失效)")

    out = run("cat", "use-containers-to-build-a-data-board-card")
    check(out.count("![") == 8 and "[图略:" not in out, "默认不裁图:8 张图应原样保留")
    out = run("cat", "use-containers-to-build-a-data-board-card", env={"KB_IMG_KEEP": "3"})
    check(out.count("![") == 3 and out.count("[图略:") == 5,
          "KB_IMG_KEEP=3 未把 8 张图裁到 3 张(首/中/尾)并留下 [图略] 标记")
    out = run("ctx", "使用容器搭建数据看板卡片的具体操作步骤是什么")
    check("images: 正文配图只配必要的" in out, "契约缺 images 行(只配必要的图)")

    out = run("card", "H2mylS6eke")
    check("completeness: full" in out and "== 证据契约 ==" in out,
          "card 子命令未保留完整性并追加证据契约")
    check("mode: card-only" in out, "精确唯一命中的 full 卡应保持 card-only")
    out = run("card", "用户", "-n", "3")
    check("mode: card-only" not in out,
          "模糊多命中的 card 输出不得声明 card-only 直答")

    cmd_globals = MOD["cmd_card"].__globals__
    original_index = cmd_globals["api_card_index"]
    try:
        with tempfile.TemporaryDirectory() as tmp:
            card_path = os.path.join(tmp, "marker-test.md")
            row = {
                "doc_id": "marker-test",
                "title": "marker-test",
                "endpoint": "https://api.example.test/marker",
                "doc_path": "docs/marker-test.md",
                "path": card_path,
                "archived": False,
                "completeness": "full",
            }
            cmd_globals["api_card_index"] = lambda: [row]
            with open(card_path, "w", encoding="utf-8") as f:
                f.write("# marker-test\ncompleteness: partial\n")
            captured = io.StringIO()
            with redirect_stdout(captured):
                check(MOD["cmd_card"](["marker-test"], 1) == 0,
                      "marker 测试卡未被 cmd_card 读取")
            check("mode: full-context-required" in captured.getvalue(),
                  "index=full 但卡片正文缺 full marker 时错误声明 card-only")

            with open(card_path, "w", encoding="utf-8") as f:
                f.write("# marker-test\ncompleteness: full\n")
            captured = io.StringIO()
            with redirect_stdout(captured):
                check(MOD["cmd_card"](["marker-test"], 1) == 0,
                      "full marker 测试卡未被 cmd_card 读取")
            check("mode: card-only" in captured.getvalue(),
                  "index 与卡片正文均为 full 时未声明 card-only")
    finally:
        cmd_globals["api_card_index"] = original_index

    for query in ("DEAP创建的智能体就是你所谓的数字员工吗", "数字员工到底在哪儿创建的", "dingtalk-tag 提示 DIGITAL_EMPLOYEE_NOT_ENABLED 怎么开通"):
        out = run("ctx", query)
        check("cross_kb: 本题涉及数字员工" in out, f"数字员工题缺跨库提示: {query}")
        check("不得写任何 dws 命令的参数" in out, f"跨库提示缺参数禁令: {query}")
        check("DEAP 1.0 的 AI 助理" in out, f"跨库提示缺「DEAP 平台界面=DEAP 1.0 助理」: {query}")
    out = run("ctx", "通过免登码获取用户信息的接口地址和必填参数是什么")
    check("cross_kb:" not in out, "非数字员工题不应出现跨库提示")

    # 实录 10-13 社区群：问 sheet 最大行数只展开「创建工作表」，模型编出 usedRange 参数。
    for query in ("钉钉文档的信息里 文件数据中的 各个表格sheet的 最大行数怎么获取 似乎你会给我塞空行",
                  "GetRange 会跳过空行吗 usedRange"):
        out = run("ctx", query)
        check("获取工作表" in first_body_heading(out), f"sheet 行数题首篇不是获取工作表: {query}")
        check("== 原文直取" in out and "| lastNonEmptyRow |" in out,
              f"sheet 行数题缺 lastNonEmptyRow 原文: {query}")
        check("Range范围内的所有行" in out, f"sheet 行数题缺 GetRange 返回所有行的原文: {query}")
    for query in ("机器人markdown消息怎么空行", "AI表格最后一行记录怎么取"):
        out = run("ctx", query)
        check("== 原文直取" not in out and "lastNonEmptyRow" not in out,
              f"非电子表格题被行数别名污染: {query}")

    # 实录 10-14 dws 群：把 OpenAPI 的 QPS/月配额/90018 套到 dws 产品命令上（产品命令走 MCP 网关）。
    for query in ("dws发送消息限流规则是什么", "dws使用的 也是 钉钉 OpenAPI 吗"):
        out = run("ctx", query)
        check("cross_kb_ratelimit:" in out and "MCP 网关" in out, f"dws 限流题缺跨库提示: {query}")
    # 零命中路径以 rc=1 表示「没找到」，提示仍须给出
    zero = subprocess.run(["python3", DKDOC, "ctx", "RATE_LIMIT_ERROR 是什么意思"], cwd=ROOT,
                          capture_output=True, text=True, timeout=30)
    check("cross_kb_ratelimit:" in zero.stdout, "零命中的 RATE_LIMIT_ERROR 题缺 dws 限流提示")
    for query in ("钉钉服务端 API 的 QPS 限制是多少", "通过免登码获取用户信息的接口地址和必填参数是什么"):
        out = run("ctx", query)
        check("cross_kb_ratelimit:" not in out, f"非 dws 题不应出现 dws 限流提示: {query}")

    # 实录 10-15 正式群：更新日志正文被上限切在申请表链接中间(…/notable/s)，模型补全出 404 的 alidocs 链接。
    form = ("[钉钉数字员工创建灰度申请（DWS 内&&界面功能）]"
            "(https://alidocs.dingtalk.com/notable/share/form/v013BMqYy5D4dLEmqwZ_MPojg9m_23zNs0R?source=link)")
    # 断言用固定串只为发现原文变更;dws 库 note 不再写死链接(引用本库原文的外部镜像),无需人工同步
    log = open(os.path.join(ROOT, next(
        d["local_path"] for d in MOD["load_jsonl"]("meta/documents.jsonl") if d.get("slug") == "dws-cli-log")),
        encoding="utf-8").read()
    check(form in log, "更新日志原文的灰度申请表链接已变化：更新本测试的 form 常量即可")
    for query in ("数字员工灰度怎么申请", "DIGITAL_EMPLOYEE_NOT_ENABLED 怎么开通", "数字员工怎么开通"):
        out = run("ctx", query)
        check("cross_kb_form:" in out and form in out, f"数字员工开通题缺逐字申请表链接: {query}")
    out = run("ctx", "通过免登码获取用户信息的接口地址和必填参数是什么")
    check("cross_kb_form:" not in out, "非数字员工题不应出现申请表")
    check("不得按格式自行构造" in out and "不得补全" in out, "证据契约缺少截断链接/构造链接禁令")
    # 截断点不得落在链接内部：全库长文 × 各档正文上限
    cut, span = MOD["_cut"], MOD["_LINK_SPAN_RE"]
    check(cut("ab [x](http://e.test/aaaa) cd", 12) == "ab [x](http://e.test/aaaa)", "短链未延到链接结尾")
    check(cut("ab [x](http://e.test/" + "a" * 500 + ")", 12) == "ab ", "长链未退到链接之前")
    bad = []
    for d in MOD["load_jsonl"]("meta/documents.jsonl"):
        fp = os.path.join(ROOT, d["local_path"])
        body = open(fp, encoding="utf-8", errors="ignore").read() if os.path.exists(fp) else ""
        for cap in (3000, 3500, 5000, 6000):
            if len(body) <= cap:
                continue
            k = len(cut(body, cap))
            if any(m.start() < k < m.end() for m in span.finditer(body, max(0, k - 2500))):
                bad.append(f"{d['local_path']}@{cap}")
    check(not bad, f"截断仍切在链接中间 {len(bad)} 处: {bad[:3]}")

    # R10.5 回退:带接口标识符的自然问句 jsapi 恒 0 命中(Q81/Q82);追问须带上一问(Q80);高级版接口须提示(Q107)
    out = run("ctx", "为什么UpdateManager.onUpdateReady方法文档里写小程序不支持啊？")
    check("[jsapi] UpdateManager.onUpdateReady" in out, "标识符问句未召回 jsapi 页")
    out = run("ctx", "--prev", "H5 通过JSAPI调用dd.biz.util.uploadAttachment接口", "不进行预览行不行")
    check("dd.biz.util.uploadAttachment" in out and "jsapi=1" in out, "--prev 未把上一问实体并入")
    out = run("ctx", "审批实例的url只能填一个，多个审批人的情况下怎么让审批人在OA审批应用中看到自己的审批单详情")
    check("[提示] 以下命中同时含标准版与 premium" in out, "标准版/premium 并存未提示")

    # 回退后必须恢复原先已展开的字段约束，而不是只保留文档标题或候选计数。
    out = run("ctx", "自有OA审批创建实例的url只能填一个，多个审批人的情况下怎么让审批人在OA审批应用中看到自己的审批单详情")
    check("| url | String | 是 | 第三方审批系统中审批单详情页地址，最大长度1024字符。 |" in out,
          "自有OA请求体url必填/长度约束未展开")
    check("== 产品原文" not in out, "开平题被同名DWS产品资料插入")
    out = run("ctx", "--full", "https://open.dingtalk.com/document/development/send-group-helper-message outTrackId 需要保存吗")
    check("需保存`outTrackId`，否则无法进行关闭互动卡片吊顶" in out,
          "outTrackId保存约束未展开")
    check("需要重新生成全新的 outTrackId，否则更改不会生效" in out,
          "更改cardTemplateId/cardData的outTrackId约束未展开")
    out = run("cat", "api-premiumgrantprocessinstancefordownloadfile")
    check("评论中上传的附件fileId也支持获取下载链接" in out,
          "高级版审批评论附件支持说明丢失")

    # grep 命中必须给真实source_url，不能按slug猜命名空间。
    out = run("grep", "MCP 服务接入 > 概述")
    check("source_url: https://open.dingtalk.com/document/development/mcp-square-introduction" in out,
          "grep命中未附frontmatter source_url")
    files = {l.split(":", 1)[0] for l in out.splitlines() if l.startswith("docs/")}
    heads = {l[3:].split(" · source_url: ", 1)[0] for l in out.splitlines() if l.startswith("== docs/")}
    check(files and files <= heads, f"有命中文件缺source_url行: {sorted(files - heads)[:3]}")

    # 多个词放进一个引号：find/api/event/jsapi 拆词查，不能整串子串匹配落空(10-28 线上 46 次多词 find 41 次无命中)。
    one, many = run("find", "考勤 变更 事件"), run("find", "考勤", "变更", "事件")
    check("0137-attendance-day-statistics-change-event.md" in one and one == many,
          "find 引号多词未与多参数等价")
    check("attend_user_daily_summary_refresh" in run("event", "考勤 日统计"), "event 引号多词未拆词")
    partial = run("event", "考勤 不存在的词xyz")
    check(partial.splitlines()[0].startswith("考勤"), f"event 多词全中为空时未按命中词数给部分命中: {partial[:80]}")
    check("0137-attendance-day-statistics-change-event.md" not in run("event", "考勤组"),
          "单词 event 查询行为被改变(不应出现部分命中)")
    # grep：原短语能逐字命中时照旧；逐字无命中才按同一行/同一篇含全部词；正则照旧。
    check("（多词" not in run("grep", "MCP 服务接入 > 概述"), "原短语能逐字命中时 grep 未照旧按短语返回")
    out = run("grep", "考勤 变更 事件")
    check("同一行含全部 3 个词" in out and "0164-attendance-overview.md" in out, "grep 多词同行模式失效")
    out = run("grep", "运营答疑群 自有渠道推广")
    check("同一篇内含全部词" in out and "0027-isv-cooperation-guide.md" in out, "grep 多词同篇模式失效")
    check("无命中" in subprocess.run(["python3", DKDOC, "grep", "考勤 不存在的词xyz"], cwd=ROOT,
                                    capture_output=True, text=True, timeout=30).stdout, "grep 多词无命中未说明")
    out = run("grep", "帮助中心\\|运营答疑群")
    check("同一行含全部" not in out and "0027-isv-cooperation-guide.md" in out, "grep 正则被误当多词")
    # 连词/指代虚词不当检索词(或者/相关/具体曾让《部署方式介绍》压过《技术支持》)。
    out = run("ctx", "钉钉帮助中心或相关技术有具体的人名或者群名吗")
    audit = next(l for l in out.splitlines() if l.startswith("已检索"))
    check("0044-ngliko.md" in first_body_heading(out), f"技术支持未成为首篇: {first_body_heading(out)}")

    print("OK: dkdoc ctx fast-path/evidence-contract/rollback/source_url regression")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"DKDOC CTX TEST FAIL: {type(exc).__name__}: {exc}")
        sys.exit(1)
