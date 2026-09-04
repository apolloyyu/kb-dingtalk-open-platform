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

    print("OK: dkdoc ctx fast-path/evidence-contract regression")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"DKDOC CTX TEST FAIL: {type(exc).__name__}: {exc}")
        sys.exit(1)
