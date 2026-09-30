---
title: "DWS 发送与更新"
source_url: "https://open.dingtalk.com/document/development/json-card-dws-send-and-update"
namespace: "development"
slug: "json-card-dws-send-and-update"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "发送与互动 > DWS 发送与更新"
doc_id: "O4jGWuJILz"
updated_at: "2026-09-30 09:14:01"
---

> Source: https://open.dingtalk.com/document/development/json-card-dws-send-and-update
> Path: 互动卡片 / JSON 构建卡片（AI） / 发送与互动 > DWS 发送与更新
> Updated: 2026-09-30 09:14:01

# DWS 发送与更新

## 消息内容格式

`--content`是 A2UI 消息的**字符串数组**：每条消息先序列化成 JSON 字符串，再组成数组。把它保存为文件，命令中用 `"$(cat content.json)"` 读入，避免在命令行里手写转义。

**content.json**：

```
[
  "{\"version\":\"v1.0\",\"createSurface\":{\"surfaceId\":\"order-001\",\"catalogId\":\"https://dingtalk.com/card/a2ui/catalogs/public/catalog.json\"}}",
  "{\"version\":\"v1.0\",\"updateDataModel\":{\"surfaceId\":\"order-001\",\"path\":\"/\",\"value\":{\"order\":{\"title\":\"订单已创建\",\"detail\":\"订单号 A2024001，预计 3 天内发货\"}}}}",
  "{\"version\":\"v1.0\",\"updateComponents\":{\"surfaceId\":\"order-001\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"detail\"],\"gap\":8},{\"id\":\"title\",\"component\":\"Text\",\"text\":{\"path\":\"/order/title\"}},{\"id\":\"detail\",\"component\":\"Text\",\"variant\":\"caption\",\"text\":{\"path\":\"/order/detail\"}}]}}"
]
```

这是 [完整示例](0001-json-build-card.md) 中的订单卡片。也可以用 `dws aicard lint --emit` 从卡片文件直接生成，详见 [DWS 创建与校验](0014-json-card-dws-create-and-validate.md)。

## 发送卡片命令

发到群聊或单聊，二选一：

- **群聊**

  ```
  dws chat message send-a2ui-card \
  --conversation-id <openConversationId> \
  --content "$(cat content.json)"
  ```
- **单聊**

  ```
  dws chat message send-a2ui-card \
  --open-dingtalk-id <openDingTalkId> \
  --content "$(cat content.json)"
  ```

| **参数** | **是否必填** | **说明** |
| --- | --- | --- |
| --content | 是 | A2UI 消息 JSON **字符串数组**，非空。 |
| --conversation-id | 群聊必填 | 群聊 `openConversationId`，与 `--open-dingtalk-id` 互斥。 |
| --open-dingtalk-id | 单聊必填 | 单聊接收者 `openDingTalkId`，与 `--conversation-id` 互斥。 |
| --support-forward | 否 | 允许转发，默认不允许。 |
| --a2ui-annotations | 否 | 组件注解 JSON 对象数组，支持空数组 []。 |
| --dry-run | 否 | 只预览要发送的内容，不实际发送。 |

> **[!NOTE]**
>
> - 卡片创建时状态为 `PROCESSING`。
> - 发送成功后保存返回的 `bizId`，后续更新靠它定位这张卡片。
> - 没有模板 ID 参数，卡片结构全部由消息携带。

目标 ID 可以用 DWS 查询：

- 群聊用 `dws chat +chat-search --query "群名关键词"` 获取 `openConversationId`。
- 人员用 `dws contact user search --query "姓名"` 获取 `openDingTalkId`。

## 更新卡片命令

只发实际变化的消息（`updateDataModel` / `updateComponents`），不要重发 `createSurface`。

下面把订单标题改为「订单已发货」，并把卡片置为完成：

**update.json**：

```
[
  "{\"version\":\"v1.0\",\"updateDataModel\":{\"surfaceId\":\"order-001\",\"path\":\"/order/title\",\"value\":\"订单已发货\"}}"
]
```

**命令**：

```
dws chat message update-a2ui-card \
--biz-id <bizId> \
--flow-status FINISH \
--content "$(cat update.json)"
```

| **参数** | **是否必填** | **说明** |
| --- | --- | --- |
| --biz-id | 是 | 发送时返回的 bizId。 |
| --content | 是 | A2UI 消息 JSON 字符串数组，非空。 |
| --flow-status | 是 | 更新后的卡片状态，取值见下方卡片状态，也兼容数字 1–9。 |

## 卡片状态

`--flow-status` 使用下面的枚举名。创建时默认为 `PROCESSING`，之后按业务进展推进：

| **取值** | **含义** |
| --- | --- |
| PROCESSING | 处理中，创建时的默认状态。 |
| INPUTTING | 输入中，流式内容正在产出。 |
| EXECUTING | 执行中，正在运行某项任务。 |
| CONFIRMING | 待确认，等待用户确认。 |
| CONFIRMED | 已确认。 |
| FINISH | 已完成。 |
| ERROR | 失败。 |
| ABORTED | 已中止。 |
| TIMEOUT | 已超时。 |
