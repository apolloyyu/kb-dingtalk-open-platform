---
title: "监听交互事件"
source_url: "https://open.dingtalk.com/document/development/json-card-listen-to-interaction-events"
namespace: "development"
slug: "json-card-listen-to-interaction-events"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "发送与互动 > 监听交互事件"
doc_id: "fVE3x7boHl"
updated_at: "2026-09-30 09:14:02"
---

> Source: https://open.dingtalk.com/document/development/json-card-listen-to-interaction-events
> Path: 互动卡片 / JSON 构建卡片（AI） / 发送与互动 > 监听交互事件
> Updated: 2026-09-30 09:14:02

# 监听交互事件

## 能力现状

| **能力** | **状态** |
| --- | --- |
| 监听当前登录用户收到的卡片操作事件 | **可用**：`dws event consume user_card_action_triggered`，用法见本文档。 |
| 服务端 HTTP 回调 | **未开放**：不能注册回调地址，也没有验签和回复能力。 |
| 标准 A2UI 响应 | 尚不可用：`Action.event` 当前只保证声明式元数据被保留，**不要把** `RendererToAgent.action`**、**`wantResponse` **或** `responsePath` **当作端到端可用的能力来设计业务架构**。 |

本文档描述的是现有回调链路：端上产生 `actionData.a2uiAction`，经服务端套上 `{version, action}` 结构后回到业务侧。

## 事件回流链路

用户点击卡片上的按钮、提交表单后，交互结果通过 DingTalk Stream 长连接回到你这边。

订阅事件 `user_card_action_triggered` 即可：

```
dws event consume user_card_action_triggered --flatten
```

- 输出为 NDJSON，一行一个事件，便于 `jq` 或管道处理。
- `--flatten` 输出稳定的顶层业务字段，适合脚本直接消费，不加则保留 `type` / `event_type` / `data` / `headers` 的传输信封。
- 结构化上下文位于 `payload.body.actionData.context`，答案、问题、操作者、业务与会话上下文都在 `payload.body` 下。

> **[!NOTE]**
>
> 连上后 stderr 会打印 `[event] ready`，等它出现再读 stdout，否则会漏掉先到的事件。

## 订阅管理

命令默认用当前登录态自动创建或复用个人订阅，并建立个人长连接，非默认组织要加 `--profile`。

```
# 查看事件目录
dws event list

# 查看事件结构
dws event schema user_card_action_triggered

# 查看订阅与本地消费状态
dws event status

# 停止订阅（先预览，确认后再执行）
dws event stop <subscribe_id> --dry-run
dws event stop <subscribe_id> --yes
```

> **[!NOTE]**
>
> - 停机用 `SIGTERM`、关闭 stdin，或用上面的 `event stop`。
> - 不要 kill -9，否则订阅不会被正确清理。

## 完整验证流程

1. **离线校验**：`aicard lint` 确认结构合法。
2. **发给自己**：`aicard preview` 先看一眼渲染效果。
3. **真机发送**：`send-a2ui-card` 发到目标会话。
4. **推进状态**：`update-a2ui-card` 更新数据并切换 flowStatus。
5. **验证回调**：`event consume` 观察交互事件是否按预期回流。
