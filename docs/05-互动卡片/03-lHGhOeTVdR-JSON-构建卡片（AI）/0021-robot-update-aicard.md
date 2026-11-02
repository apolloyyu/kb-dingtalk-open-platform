---
title: "机器人更新卡片"
source_url: "https://open.dingtalk.com/document/development/robot-update-aicard"
namespace: "development"
slug: "robot-update-aicard"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "发送与互动 > 机器人更新卡片"
doc_id: "nRfSL89U0q"
updated_at: "2026-10-29 11:52:29"
---

> Source: https://open.dingtalk.com/document/development/robot-update-aicard
> Path: 互动卡片 / JSON 构建卡片（AI） / 发送与互动 > 机器人更新卡片
> Updated: 2026-10-29 11:52:29

# 机器人更新卡片

本接口用于更新卡片内容和状态，不提供创建请求中的转发、投递通知及 cardAtUserIds 等配置字段；具体支持字段以官方接口文档为准。

## **说明**

**用企业内部应用的机器人，**通过调用[更新 AI 卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0792-api-updateaicard.md)接口，**更新已经发出的卡片内容和状态**。

卡片要先用[机器人发送卡片](0020-robot-send-aicard.md)创建并投递，更新时用创建时的 `outTrackId` 定位这张卡片。access\_token 的获取方式和所需权限 `AICard.Instance.Write` 与发送相同。

## 更新卡片

只发实际变化的消息，不要重发 `createSurface`。下面把订单标题改为「订单已发货」，并把卡片置为完成：

```
PUT /v1.0/card/ai/instances/update
{
  "outTrackId": "order-001-20261027",
  "outUpdateId": "order-001-20261027-shipped",
  "flowStatus": "FINISH",
  "a2uiMessages": ["{\"version\":\"v1.0\",\"updateDataModel\":{\"surfaceId\":\"order-001\",\"path\":\"/order/title\",\"value\":\"订单已发货\"}}"]
}
```

返回 `{"success": true, "result": {"outTrackId": "...", "outUpdateId": "...", "flowStatus": "FINISH"}}`。

- `a2uiMessages` 只支持 `updateComponents` 和 `updateDataModel`：数据变化用 `updateDataModel`，组件和布局变化用 `updateComponents`。
- `outUpdateId` 是本次更新的幂等标识：每次新的更新换一个新值，同一次更新重试时保持不变，内容也保持不变。
- 不要重放表单的初始数据，否则会覆盖用户已经输入的内容。
- `a2uiAnnotations` 更新时无需重复传，需要新增标注组件时再传。

## 只改状态

`a2uiMessages` 传空数组返回 `400 param.invalid`。如遇此情况，可附带一条将已知字段原值写回的 `updateDataModel`。下面仅适用于标题仍为「订单已发货」的订单示例；

> **[!NOTE]**
>
> 实际使用必须取当前值，避免覆盖新内容。

```
PUT /v1.0/card/ai/instances/update
{
  "outTrackId": "order-001-20261027",
  "outUpdateId": "order-001-20261027-finish",
  "flowStatus": "FINISH",
  "a2uiMessages": ["{\"version\":\"v1.0\",\"updateDataModel\":{\"surfaceId\":\"order-001\",\"path\":\"/order/title\",\"value\":\"订单已发货\"}}"]
}
```

## flowStatus 取值

只传枚举名，不传数字码。

| **取值** | **含义** |
| --- | --- |
| `PROCESSING` | 处理中，代表创建时一般用这个。 |
| `INPUTTING` | 输入中，代表流式内容正在产出。 |
| `EXECUTING` | 执行中，代表正在运行某项任务。 |
| `CONFIRMING` | 待确认，代表等待用户确认。 |
| `CONFIRMED` | 已确认。 |
| `FINISH` | 已完成。 |
| `ERROR` | 失败。 |
| `ABORTED` | 已中止。 |
| `TIMEOUT` | 已超时。 |

## 常见错误

- **提示**`400 param.invalid`

  消息格式或类型不合法，空 `a2uiMessages` 返回该错误。

  - 看返回的 `errorMsg`。
  - 至少带一条更新消息，不要重发 `createSurface`。
- **提示**`400 param.cardNotExist`

  `outTrackId` 对应的卡片不存在**。**确认用的是创建时的 `outTrackId`，且与创建时是同一个应用**。**
- **提示**`400 param.idempotencyConflict`

  同一个 `outUpdateId` 带了不同内容**。**

  - 新的更新换新 `outUpdateId`。
  - 重试时保持内容不变。
- **提示**`500 system.resultUnknown` **/** `system.operationInProgress`

  结果未知或仍在处理**。**先核实卡片状态，再用**同一个** `outUpdateId` 重试**。**
- **群里只显示「暂无可展示的最终产物」**

  卡片上没有任何 `a2uiAnnotations` 标注，或标注的组件文本由函数生成**。**检查 `artifact` 标注及组件文本类型。需要变更标注时按官方接口传参，并验证更新后的摘要。
