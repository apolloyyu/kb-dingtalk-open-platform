---
title: "钉钉 CLI 事件订阅 — 给你的 Agent 装上钉钉的\"耳朵\""
source_url: "https://open.dingtalk.com/document/development/dingtalk-cli-event-subscription"
namespace: "development"
slug: "dingtalk-cli-event-subscription"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "进阶实战 > 事件驱动开发 > 钉钉 CLI 事件订阅 — 给你的 Agent 装上钉钉的\"耳朵\""
doc_id: "e6ollBomSO"
updated_at: "2026-08-17 17:38:37"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-cli-event-subscription
> Path: 应用开发 / 钉钉CLI / 进阶实战 > 事件驱动开发 > 钉钉 CLI 事件订阅 — 给你的 Agent 装上钉钉的"耳朵"
> Updated: 2026-08-17 17:38:37

# 钉钉 CLI 事件订阅 — 给你的 Agent 装上钉钉的"耳朵"

## 背景

你的 Agent 已经能发消息、建待办、约会议了，但它有一个明显的短板：无法感知钉钉侧发生的事件。有人 @ 你、收到单聊消息——这些它都无从得知，只能被动等待你下达指令。

传统做法是写脚本定时轮询消息，但轮询存在延迟、消耗 API 配额，还容易漏消息或重复处理。

事件订阅采用另一种思路：钉钉侧一旦发生事件，就主动、实时地推送给你。你的 Agent 可以在事件到达时直接响应，从而具备主动感知钉钉事件的能力。

入口命令是 `dws event`，实时消费统一走一条 `dws event consume` 长连接，无需编写轮询脚本。

想让事件订阅支持更多领域（不止 IM）？在[钉钉 CLI 许愿墙](https://docs.dingtalk.com/notable/share/form/v01eLbnj1bw1ELb0laN_dv19yqvsgs3oebp3pcjys_1qX0QQ0?source=link)许个愿，或去 [GitHub](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli) 提 issue。

## 快速开始

### **一键安装**

如果只需要事件能力，可用便捷脚本单独安装，也可以把下面这条命令交给你的 AI 工具执行：

```
curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install-event.sh | sh
```

### **订阅事件**

开始订阅@ 我事件：

```
dws auth login  # 登录
dws event list   # 查看事件列表
dws event consume <event_key>  [flags]  -f ndjson  # 开始监听事件
```

建连成功后会打印 `connected bus pid=...`，这时就从 stdout 一行行读事件。

**事件订阅指令清单**

| 目标 | 命令 |
| --- | --- |
| 看事件目录 | `dws event list` |
| 看字段（写解析依据） | `dws event schema <event_key>` |
| 建连消费 | `dws event consume <event_key> [flags]` |
| IM 意图快捷监听【推荐】 | `dws event +listen-im --kind <意图> -f ndjson` |
| 看订阅 / 连接 / 消费状态 | `dws event status` |
| 取消订阅 | `dws event stop <subscribe_id>` / `--all` |

订阅管理：`--subscribe-id` 复用已有订阅、`--ttl 24h`（`0` 不过期）、`--ephemeral`（退出即取消）。有界自测：`--duration 10m` 或 `--max-events N`。输出格式 `-f`：`ndjson`（默认）/ `json` / `raw` / `compact`。

### **IM 意图快捷入口**

普通 IM 监听不必手选 EventKey，`+listen-im` 支持自然姓名/群名唯一解析，把高层意图编译为对应事件：

```
dws event +listen-im --kind at-me -f ndjson                          # 有人 @ 我
dws event +listen-im --kind all-direct -f ndjson                     # 我的所有单聊
dws event +listen-im --kind all-group -f ndjson                      # 我所在的所有群
dws event +listen-im --kind sender --user-query "张三" -f ndjson      # 某人发给我的消息
dws event +listen-im --kind group --chat-query "项目群" -f ndjson     # 指定群
dws event +listen-im --kind sender --user-query "张三" --events read,recall,reaction -f ndjson
```

OA 审批事件仍走 `dws event consume <event_key>` 显式订阅（见下节）。

## 应用场景

### 只关注"有人@我"

只需在被 @ 时收到提醒，无需任何额外参数。

| 目标场景 | 对应命令 |
| --- | --- |
| 有人 @ 我就触发 | `dws event consume user_im_message_receive_at -f ndjson` |

### 关注特定的人或群

关注特定的人或会话，由服务端完成过滤，开销最小。

| 目标场景 | 对应命令 |
| --- | --- |
| 关注与某人的单聊 | `dws event consume user_im_message_receive_o2o --user <userId>` |
| 关注某个群 | `dws event consume user_im_message_receive_group --group <openConversationId>` |
| 关注全部单聊 | `dws event consume user_im_message_receive_o2o_all` |
| 关注全部群聊 | `dws event consume user_im_message_receive_group_all` |

ID 的获取方式：

- 人名 → `dws aisearch person --keyword "<名字>" --dimension name -f json` 取 `userId`；
- 群名 → `dws chat search --query "<群名>" -f json` 取 `openConversationId`

### **IM + 审批双通道场景**

IM 与审批事件共享同一条 Stream 底座，可组合出完整业务闭环，例如「报销申请助手」：

1. `+listen-im --kind all-direct` 监听私聊，命中关键词「报销」；
2. Agent 自动 `dws oa approval create-instance` 发起审批，回执申请人单号；
3. `event consume user_oa_approval_instance_finished` 监听审批走完；
4. 结果自动回传申请人，并 `dws aitable record create` 记入台账。

### 接入自动化流水线

一行一事件，天然适合交给 `jq` 做类型路由、关键词过滤、按类型落盘。

| 目标场景 | 对应命令 |
| --- | --- |
| 按类型路由 / 过滤 / 落盘 | `dws event consume ... -f ndjson`，配 `--query "关键词1,关键词2"`、`--filter-json '<DSL>'`、`--output-dir` / `--route` |

### 消息驱动的 Agent：收到就处理

“来消息就自动处理”是一个常见诉求，现在可以直接落地：建立一条连接，每收到一条消息就交给你的处理逻辑，自动回复。

| 目标场景 | 对应命令 |
| --- | --- |
| 关注与某人的单聊，收到消息即交给你的逻辑自动回复 | `dws event consume user_im_message_receive_o2o --user <userId> -f ndjson`每条消息一行 JSON，`data` 里带 `content`/`sender`/`conversation_id`/`message_id` 等完整字段。 |

### **审批驱动的自动化：OA 审批事件**

v1.0.58 起，审批状态变化不再需要轮询 `oa list-pending`，六个审批事件实时推送：

| 目标场景 | 对应命令 |
| --- | --- |
| 有人发审批给我，即时提醒 | `dws event consume user_oa_approval_task_created -f ndjson` |
| 我发起的审批走完，自动收尾 | `dws event consume user_oa_approval_instance_finished -f ndjson` |
| 审批被转交给我，接盘提醒 | `dws event consume user_oa_approval_task_redirected -f ndjson` |
| 审批任务处理完成（同意/拒绝） | `dws event consume user_oa_approval_task_finished -f ndjson` |

## 事件能力清单

当前支持 **22 个个人事件**，覆盖 **IM 消息**与 **OA 审批**两个领域，订阅主体 = 当前登录用户，后续随版本持续补齐。

### **IM 消息领域**

| **事件名称** | **event\_key** | **事件描述** |
| --- | --- | --- |
| @我的消息 | user\_im\_message\_receive\_at | 监听有人 @ 我的消息 |
| 指定单聊消息 | user\_im\_message\_receive\_o2o | 监听与指定用户的单聊消息 |
| 指定群消息 | user\_im\_message\_receive\_group | 监听指定群里的消息 |
| 指定发送人消息 | user\_im\_message\_receive\_user | 监听指定用户发给我的消息（不限会话） |
| 全部单聊消息 | user\_im\_message\_receive\_o2o\_all | 当前用户收到的所有单聊消息 |
| 全部群消息 | user\_im\_message\_receive\_group\_all | 当前用户收到的所有群聊消息 |
| 指定单聊消息已读 | user\_im\_message\_read\_o2o | 我在指定单聊中发送的消息被对方已读 |
| 指定群消息已读 | user\_im\_message\_read\_group | 我在指定群聊中发送的消息被已读 |
| 指定单聊消息撤回 | user\_im\_message\_recall\_o2o | 指定单聊中的消息被撤回 |
| 指定群消息撤回 | user\_im\_message\_recall\_group | 指定群聊中的消息被撤回 |
| 指定单聊消息表情回应 | user\_im\_message\_reaction\_o2o | 指定单聊中的消息收到表情回应（贴表情） |
| 指定群消息表情回应 | user\_im\_message\_reaction\_group | 指定群聊中的消息收到表情回应（贴表情） |
| 群标题变更 | user\_im\_group\_updated | 指定群聊的标题发生变更 |
| 群成员加入 | user\_im\_group\_member\_added | 指定群聊有成员加入 |
| 群成员退出 | user\_im\_group\_member\_exited | 指定群聊有成员退出 |
| 群解散 | user\_im\_group\_disbanded | 指定群聊被解散 |

### **OA 审批领域**

| **事件名称** | **event\_key** | **事件描述** |
| --- | --- | --- |
| 审批任务创建 | user\_oa\_approval\_task\_created | 审批任务创建，发送给审批人 |
| 审批任务完成 | user\_oa\_approval\_task\_finished | 审批任务已完成 |
| 审批人任务转交 | user\_oa\_approval\_task\_redirected | 审批任务已转交 |
| 发起审批单 | user\_oa\_approval\_instance\_started | 审批实例已发起 |
| 审批单终止 | user\_oa\_approval\_instance\_terminated | 审批实例已终止 |
| 审批单完成 | user\_oa\_approval\_instance\_finished | 审批实例完成，发送给审批单发起人 |

## 常见问题

- `consume` **迟迟没输出，是不是订阅失败了？**

  先看 stderr 是否出现 `connected bus pid=...` 或 `[event] ready`，再用 `dws event status --event <event_key>` 检查 consumer。事件只会在订阅就绪后到达，先触发、后建连不会补发历史事件。
- **订阅群聊消息为什么失败？**

  目前群聊相关的事件订阅与 dws 登录的组织身份关联：群聊归属于组织，如果当前 dws 登录身份所属的组织与群聊不属于同一组织，就会订阅失败。
- **订阅 @ 事件为什么收不到？**

  @ 事件同理，同样受登录的组织身份限制：登录身份与消息所在组织不一致时就收不到。
- **审批事件收不到怎么办？**

  审批事件同样绑定当前登录身份：只有与"你"相关的审批变化才会推送（发给你审批、你发起、转交给你等）。确认 `dws auth` 登录的组织与审批单所在组织一致；多组织场景用 `--profile` 显式指定。
- **自己发的消息/自己处理的审批为什么没有事件？**

  自己发送的消息不作为事件回来（自环过滤）；验证订阅请用另一个账号或机器人触发。
- **怎么安全停止和清理事件？**

  优先使用 `--ephemeral`，进程退出后再执行 `dws event status --event <event_key>`，确认 `subscriptions=[]`。仍有残留时只执行 `dws event stop <subscribe_id>`；不要默认使用 `--all`，否则可能删掉同一身份下其他正在使用的订阅。
- **订阅创建失败后能无限重试吗？**

  不能。错误返回带重试语义：`retryable=true` 最多再试 2 次且须遵守 `retry_after_seconds`；`retryable=false` 立即停止。处于 `in_flight`/`cooldown`/`terminal_hold` 保护状态时不要并行启动相同订阅绕过。
