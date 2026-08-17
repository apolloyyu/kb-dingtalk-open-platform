---
title: 会话与消息(chat)
source_refs: internal/helpers/chat.go, internal/shortcut/chat/unified_send.go, internal/shortcut/chat/chat_message.go, internal/shortcut/chat/chat_group.go, internal/shortcut/chat/chat_bot.go, internal/shortcut/chat/lark_alignment.go, internal/shortcut/chat/resource_download.go, internal/shortcut/chatmsg/chatmsg.go, internal/shortcut/builtin/builtin.go, internal/shortcut/adapter.go, internal/shortcut/runner.go, internal/helpers/ding.go, internal/shortcut/ding/ding.go
---

# 会话与消息(chat)

chat 能力分两层组织:原子 MCP 命令层与快捷命令层;DING 消息独立成组。

## 原子 MCP 命令层

`internal/helpers/chat.go`(约 6000 行)定义 `chatCmd`,`Use` 为 `chat`,下含:

- `group`:create / members add / remove / add-bot / rename;
- `message`:list / send / send-by-bot / send-by-webhook / recall / edit / read-status / query-send-status;
- `bot search`、`category`、`file upload`、`emoji` 等。

经 `callMCPTool` / `callMCPToolOnServer("im"|"bot", ...)` 路由到不同 MCP server。

## 快捷命令层

`internal/shortcut/chat/*.go` 为声明式 `shortcut.Shortcut`(`Service` 为 `"chat"`,命令名以 `+xxx` 形式),各文件 `init()` 调用 `shortcut.Register`;由 `internal/shortcut/builtin/builtin.go` 空白导入聚合,`shortcut.Commands()` 生成 cobra 树;`adapter.go` / `runner.go` 负责执行,`RuntimeContext.CallMCP` 落地。

## 关键映射(消息)

`internal/shortcut/chat/` 下的消息映射:

| Shortcut | 映射 |
|---|---|
| `unified_send.go` `+messages-send` | `send_personal_message` |
| `chat_message.go` `+messages-send-by-bot` | `send_robot_group_message` |
| `chat_message.go` `+messages-batch-send-by-bot` | `batch_send_robot_msg_to_users` |
| `chat_message.go` `+messages-send-by-webhook` | `send_message_by_custom_robot` |
| `chat_message.go` `+messages-recall` | 撤回 |
| `chat_message.go` `+messages-list` | 消息列表 |
| `resource_download.go` `+messages-resource-download` | 资源下载 |

## 群管理映射

| Shortcut | 说明 |
|---|---|
| `lark_alignment.go` `+chat-create` | 建群 |
| `chat_group.go` `+chat-search` | 群搜索 |
| `+chat-members-get` | 成员查询 |
| `+chat-transfer-owner` | 群主转让 |
| `+chat-quit` / `+chat-dismiss` | 退群 / 解散 |
| `+chat-set-admin` | 设置管理员 |
| `+chat-mute`(-member) | 禁言 |
| `+chat-role-*` | 角色相关 |
| `+chat-add-bot` | `add_robot_to_group` |
| `+chat-remove-bot` / `+chat-bots` | 移除/列出机器人 |

## 机器人

`chat_bot.go`:`+bot-search` / `+bot-find`。

## 消息结果投影

`internal/shortcut/chatmsg/chatmsg.go` 提供 `ProjectMessageV1`、`MessageResultContract` 只读投影;另有 `card_update.go`、`card_ref.go`、`send_status.go`、`search.go`。

## DING 消息

- 原子命令 `internal/helpers/ding.go`(`ding message` 组):
  - `send` → `send_ding_message`;
  - `recall`;
  - `list` → `list_ding_messages`(im server);
  - `receiver-status`;
  - `send-personal` → `send_personal_ding`;
  - `send-by-message` → `send_ding_by_message`;
  - `recall-personal`。
- 快捷命令 `internal/shortcut/ding/ding.go`:`+list`、`+receiver-status`、`+send-personal`(Product 均为 `"im"`)。
