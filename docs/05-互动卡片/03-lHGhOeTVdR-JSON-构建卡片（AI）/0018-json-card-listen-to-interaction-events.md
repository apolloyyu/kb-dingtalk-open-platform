---
title: "监听交互事件"
source_url: "https://open.dingtalk.com/document/development/json-card-listen-to-interaction-events"
namespace: "development"
slug: "json-card-listen-to-interaction-events"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "发送与互动 > 监听交互事件"
doc_id: "fVE3x7boHl"
updated_at: "2026-10-29 11:52:26"
---

> Source: https://open.dingtalk.com/document/development/json-card-listen-to-interaction-events
> Path: 互动卡片 / JSON 构建卡片（AI） / 发送与互动 > 监听交互事件
> Updated: 2026-10-29 11:52:26

# 监听交互事件

## 能力状态

本文介绍 [DWS 发送与更新](0019-json-card-dws-send-and-update.md)对应的个人事件订阅。[机器人发送卡片](0020-robot-send-aicard.md)使用另一条回调链路：由 `callbackType` 选择 `STREAM` 或 `HTTP`，HTTP 模式还需 `callbackRouteKey` 和接收端配置。

| **能力** | **状态** |
| --- | --- |
| 监听当前登录用户收到的卡片操作事件 | **可用**：`dws event consume user_card_action_triggered`，用法见本文档。 |
| 标准 A2UI 响应 | 业务事件订阅不等于标准 A2UI 请求／响应闭环。不能仅凭 Action.event 的声明，依赖 RendererToAgent.action、wantResponse 或 responsePath 自动回写；业务更新需通过更新接口实现。 |

> **[!NOTE]**
>
> 本文以 DWS 个人事件的业务上下文为读取入口，机器人 OpenAPI 的路由和事件格式不能由此推断。实际字段以 `dws event schema user_card_action_triggered` 及回流数据为准。

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

## 完整验证流程

1. **离线校验**：`aicard lint` 确认结构合法。
2. **发给自己**：`aicard preview` 先看一眼渲染效果。
3. **真机发送**：`send-a2ui-card` 发到目标会话。
4. **推进状态**：`update-a2ui-card` 更新数据并切换 flowStatus。
5. **验证回调**：`event consume` 观察交互事件是否按预期回流。
