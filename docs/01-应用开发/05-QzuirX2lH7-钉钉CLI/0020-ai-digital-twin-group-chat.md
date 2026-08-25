---
title: "构建群聊感知 Agent"
source_url: "https://open.dingtalk.com/document/development/ai-digital-twin-group-chat"
namespace: "development"
slug: "ai-digital-twin-group-chat"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "Agent 场景案例库 > 典型 Agent 实现 > 构建群聊感知 Agent"
doc_id: "j7nCVSVfqi"
updated_at: "2026-07-24 09:14:25"
---

> Source: https://open.dingtalk.com/document/development/ai-digital-twin-group-chat
> Path: 应用开发 / 钉钉CLI / Agent 场景案例库 > 典型 Agent 实现 > 构建群聊感知 Agent
> Updated: 2026-07-24 09:14:25

# 构建群聊感知 Agent

## 场景介绍

项目群、客户群和值班群每天都会产生大量消息。真正需要关注的，往往只有已确定的结论、分配给自己的任务、潜在风险和仍未解决的问题。

普通 Agent 可以总结文本，但它通常不知道群里刚刚发生了什么。dws 的事件订阅能力可以补上这只"耳朵"：持续监听指定群的新消息，由一个轻量脚本暂存消息，再按固定周期交给 Agent 总结。

本文实现的链路如下：

```
钉钉群消息 → dws event consume → Python 聚合 → Agent 总结 → 终端输出
```

Python 脚本支持两种触发条件：

- 收到 Y 条消息后立即总结。
- 第一条消息进入缓冲区 X 分钟后总结。

两个条件谁先满足就触发一次总结。这样既不会逐条调用 Agent，也不会因为群消息较少而一直等不到结果。

## 适用场景

同一套"监听群消息 → 聚合 → 总结"的流程，更换 Prompt 即可覆盖不同类型的群：

| 群类型 | Agent 重点关注 |
| --- | --- |
| 项目群进展总结 | 已完成事项、下一步计划、负责人、风险 |
| 客户群信息整理 | 客户反馈、承诺事项、待回复问题 |
| 值班群交接 | 异常、处理进展、遗留问题 |
| 关键词雷达 | 发布、故障、截止时间等重点信息 |

## 钉钉集成能力

| 能力 | 本文用途 |
| --- | --- |
| `dws event consume` | 实时消费当前用户可见的钉钉事件 |
| `user_im_message_receive_group` | 接收指定群的新消息 |
| Python 脚本 | 缓冲消息，并按时间或条数触发总结 |
| Agent CLI | 理解一批消息并生成结构化摘要，本文以 Qoder CLI 为例 |

最小可用版本不需要创建机器人，也不需要公网服务。dws 负责接收消息，Python 负责聚合，Agent 负责总结，结果先输出到终端即可。

## dws CLI 接入

### 步骤 1：登录 dws

确认已安装 dws CLI，并使用自己的钉钉账号登录：

```
dws auth login
```

本文使用 Qoder CLI 作为示例 Agent，也可以替换为其他支持非交互调用的 Agent CLI。

### 步骤 2：确认群名称

`dws event consume` 监听群消息时需要传入 `openConversationId`，但无需让使用者手动查询和复制。本文的脚本允许直接传入群名称，启动时会自动执行以下搜索：

```
dws chat search --query "群名称" --format json
```

脚本只接受标题完全匹配的群。如果存在多个同名群，脚本会停止并列出对应的 `openConversationId`，避免误监听其他群。已知 `openConversationId` 时也可以直接传入，原有用法仍然兼容。

### 步骤 3：验证群消息事件

如果希望在运行脚本前先验证事件链路，可以从步骤 2 的搜索结果中取出 `openConversationId`，单独运行一次事件消费命令：

```
dws event consume user_im_message_receive_group \
  --group <openConversationId> \
  --max-events 3 \
  --format ndjson
```

然后在目标群发送消息。如果终端能够收到事件，说明监听链路已打通。`--max-events 3` 表示收到 3 条事件后自动退出，适合首次验证。

## 核心实现

下面的脚本完成以下五件事：

1. 根据群名称搜索并确认唯一的 `openConversationId`。
2. 启动 `dws event consume` 监听指定群。
3. 从事件的 `payload.body` 中提取消息时间、发送人和正文。
4. 达到时间或条数阈值时，将这批消息交给 Qoder CLI。
5. 将生成的摘要打印到终端。

### Python 脚本

将以下内容保存为 `group_digest.py`：

```
#!/usr/bin/env python3
import argparse
import json
import queue
import subprocess
import threading
import time

EVENT_KEY = "user_im_message_receive_group"
AGENT_COMMAND = ["qodercli", "-p", "--permission-mode", "default", "--tools", "", "--"]

SUMMARY_PROMPT = """你是我的群消息数字分身。
请只根据群消息总结：关键结论、待办及负责人、风险与未决问题、明确提到我的事项。
信息不明确时写“待确认”，不要补充消息中没有的事实。
"""

def read_events(stream, events):
  for line in stream:
    events.put(line)

def parse_message(line):
  try:
    event = json.loads(line)
    data = event.get("data", event)
    if isinstance(data, str):
      data = json.loads(data)

    payload = data.get("payload", data)
    body = payload.get("body", payload)
    text = body.get("content")
    if not text:
      return None
    event_time = (
      body.get("createTime")
      or body.get("create_time")
      or payload.get("event_time")
      or data.get("event_time")
      or ""
    )
    sender = body.get("sender") or "未知成员"
    return f"[{event_time}] {sender}: {text}"
  except (json.JSONDecodeError, AttributeError):
    return None

def resolve_group(group):
  group = group.strip()
  if not group:
    raise RuntimeError("群名称不能为空")
  if group.startswith("cid"):
    return group

  result = subprocess.run(
    [
      "dws",
      "chat",
      "search",
      "--query",
      group,
      "--format",
      "json",
    ],
    text=True,
    capture_output=True,
    check=False,
  )
  if result.returncode:
    detail = result.stderr.strip() or result.stdout.strip() or "调用失败"
    raise RuntimeError(f"搜索群失败：{detail}")

  try:
    response = json.loads(result.stdout)
  except json.JSONDecodeError as error:
    raise RuntimeError("搜索群失败：dws 返回的不是有效 JSON") from error

  if response.get("success") is not True:
    detail = response.get("errorMsg") or response.get("errorCode") or "调用失败"
    raise RuntimeError(f"搜索群失败：{detail}")

  search_result = response.get("result")
  groups = search_result.get("groups", []) if isinstance(search_result, dict) else []
  exact_matches = {
    item.get("openConversationId"): item
    for item in groups
    if isinstance(item, dict)
    and item.get("title") == group
    and item.get("openConversationId")
  }
  if len(exact_matches) == 1:
    return next(iter(exact_matches))
  if len(exact_matches) > 1:
    ids = ", ".join(exact_matches)
    raise RuntimeError(f"找到多个同名群“{group}”，请改用 openConversationId：{ids}")

  candidates = [
    item.get("title")
    for item in groups
    if isinstance(item, dict) and item.get("title")
  ]
  if candidates:
    names = "、".join(candidates[:5])
    raise RuntimeError(f"未找到名称完全匹配的群“{group}”；搜索结果：{names}")
  raise RuntimeError(f"未找到群“{group}”")

def summarize(batch):
  prompt = f"{SUMMARY_PROMPT}\n以下是群消息：\n\n" + "\n".join(batch)
    result = subprocess.run(
        [*AGENT_COMMAND, prompt],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        print(f"[Agent 错误] {result.stderr.strip() or '调用失败'}")
        return

    print(f"\n===== 群消息摘要 {time.strftime('%Y-%m-%d %H:%M:%S')} =====")
    print(result.stdout.strip())
    print("=====================================\n")

def main():
    parser = argparse.ArgumentParser(description="DWS 群消息总结助手")
    parser.add_argument(
        "--group",
        required=True,
        help="群名称或 openConversationId",
    )
    parser.add_argument("--minutes", type=int, default=10, help="最长聚合分钟数")
    parser.add_argument("--max-messages", type=int, default=30, help="最大消息条数")
    args = parser.parse_args()

    try:
        group_id = resolve_group(args.group)
    except RuntimeError as error:
        parser.error(str(error))
    if group_id != args.group.strip():
        print(f"已找到群：{args.group.strip()} ({group_id})")

    process = subprocess.Popen(
        [
            "dws",
            "event",
            "consume",
            EVENT_KEY,
            "--group",
            group_id,
            "--format",
            "ndjson",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    events = queue.Queue()
    threading.Thread(
        target=read_events,
        args=(process.stdout, events),
        daemon=True,
    ).start()

    messages = []
    deadline = None

    print(f"正在监听：{args.minutes} 分钟或 {args.max_messages} 条消息触发一次总结")

    try:
        while process.poll() is None or not events.empty():
            timeout = 1 if deadline is None else max(0, deadline - time.monotonic())
            try:
                line = events.get(timeout=timeout)
            except queue.Empty:
                line = None

            if line:
                message = parse_message(line)
                if message:
                    messages.append(message)
                    deadline = deadline or time.monotonic() + args.minutes * 60

            enough = len(messages) >= args.max_messages
            expired = deadline is not None and time.monotonic() >= deadline
            if messages and (enough or expired):
                summarize(messages)
                messages = []
                deadline = None
    except KeyboardInterrupt:
        print("\n正在停止监听……")
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()

if __name__ == "__main__":
    main()
```

`dws event consume --format ndjson` 输出的外层事件中，`data` 可能是一段 JSON 字符串。解码后，群消息正文位于 `payload.body.content`，发送人和创建时间分别位于 `payload.body.sender` 和 `payload.body.createTime`。`parse_message()` 同时兼容旧的扁平结构，避免输出格式变化时丢弃消息。

`resolve_group()` 负责将群名称转换为 `openConversationId`。它不会根据模糊搜索结果自动猜测目标群，只有名称完全匹配且结果唯一时才继续启动事件监听。

脚本为 dws 子进程保留了标准输入，并用独立线程持续读取事件。这样即使 Agent 正在生成摘要，事件流也不会因主线程等待而停止读取。

Qoder CLI 在此处使用打印模式，并禁用了内置工具。总结任务只需读取传入的聊天记录，不需要让 Agent 执行命令或修改文件。

### 运行脚本

例如，每 10 分钟或每 30 条消息总结一次：

```
python3 group_digest.py \
  --group "群名称/群ID，这里两种都行，可选一种即可" \
  --minutes 10 \
  --max-messages 30
```

传入群名称时，脚本会先打印解析到的 `openConversationId`，再进入监听状态。运行后需保持终端开启。达到任一阈值时，脚本会调用 Agent 并在终端输出摘要。停止时按 `Ctrl+C`，不要使用 `kill -9` 强制结束 dws 事件进程。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0299724871/p1088174.png)

## 如何复用这套模板

脚本中与"群消息总结"绑定的部分主要有四处：

| 要修改的部分 | 作用 |
| --- | --- |
| `EVENT_KEY` 和对应筛选参数 | 决定监听哪一种钉钉事件 |
| `resolve_group()` | 将用户输入的群名称转换为事件命令需要的会话 ID |
| `parse_message()` | 决定如何从事件中提取业务字段 |
| `SUMMARY_PROMPT` | 决定 Agent 如何理解和处理这一批事件 |

更换事件前，可以先查看事件的字段结构：

```
dws event schema <event_key> --format json
```

例如，后续需要处理单聊消息、日程变化或其他事件时，聚合队列、时间阈值、条数阈值和 Agent 调用逻辑都可以继续复用。

## 验证与测试

建议先使用较小阈值验证完整链路：

```
python3 group_digest.py \
  --group "群名称/群ID，这里两种都行，可选一种即可" \
  --minutes 1 \
  --max-messages 2
```

依次检查：

1. 启动后，dws 是否打印事件连接就绪信息。
2. 在目标群发送两条消息后，是否立即生成一次摘要。
3. 只发送一条消息并等待一分钟后，是否按时间触发摘要。
4. 按 `Ctrl+C` 后，事件消费进程是否正常退出。

如果 dws 已连接但脚本收不到消息，可以先检查当前状态：

```
dws event status --format json
```

重点确认监听的群 ID 是否正确、当前登录用户是否在群内，以及事件连接是否处于正常状态。

至此，一个可以直接按群名称启动的最小可用群消息数字分身就完成了。后续如需将摘要发回钉钉，只需在 `summarize()` 中增加消息发送逻辑，无需改动群名称解析、事件监听和聚合部分。
