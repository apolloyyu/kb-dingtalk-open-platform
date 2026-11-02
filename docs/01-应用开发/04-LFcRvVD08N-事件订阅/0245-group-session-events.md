---
title: "群会话事件"
source_url: "https://open.dingtalk.com/document/development/group-session-events"
namespace: "development"
slug: "group-session-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 群会话事件"
doc_id: "cYgkyb7RnT"
updated_at: "2025-10-16 14:31:54"
---

> Source: https://open.dingtalk.com/document/development/group-session-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 群会话事件
> Updated: 2025-10-16 14:31:54

# 群会话事件

本文介绍了群会话事件的相关说明。

通过服务端API创建的企业群，当企业群会话发生变化，并且注册回调事件时填写的事件类型“call\_back\_tag”包含群会话事件，比如call\_back\_tag字段为“chat\_add\_member”、“chat\_remove\_member”，那么企业群会话发生了群会话添加人员和群会话删除人员，钉钉服务器会向url推送事件。

## 事件类型

| **事件类型** | **说明** |
| --- | --- |
| chat\_add\_member | 群会话添加人员。 |
| chat\_remove\_member | 群会话删除人员。 |
| chat\_quit | 群会话用户主动退群。 |
| chat\_update\_owner | 群会话更换群主。 |
| chat\_update\_title | 群会话更换群名称。 |
| chat\_disband | 群会话解散群。 |

## 群会话添加人员

**示例：**

```
{
  "Operator": "10203029011219896",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_add_member",
  "UserId": [
    "user456"
  ],
  "TimeStamp": 1608027106990,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数描述**：

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| UserId | 用户发生变更的userid列表。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话删除人员

**示例**：

```
{
  "Operator": "user456",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_remove_member",
  "UserId": [
    "16055180056034334"
  ],
  "TimeStamp": 1608027391148,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| UserId | 用户发生变更的userid列表。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话用户主动退群

**示例**：

```
{
  "Operator": "user456",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_quit",
  "TimeStamp": 1608026903228,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话更换群主

**示例**：

```
{
  "OpenConversationId": "cidmfWxxxx",
  "Owner": "manager4220",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_update_owner",
  "TimeStamp": 1608026611710,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Owner | 已经更新的新的群主的userid。 |
| OpenConversationId | 群ID。 |

## 群会话更换群名称

**示例**：

```
{
  "Operator": "user456",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_update_title",
  "Title": "开放平台",
  "TimeStamp": 1608027247528,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Title | 已经更新的新的群标题。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话解散群

**示例**：

```
{
  "Operator": "10203029011219896",
  "OpenConversationId": "cid1MFt2YA6gA1121KaBGSThA==",
  "CorpId": "dinge8a56572f80b02a8ffe93478753d9884",
  "EventType": "chat_disband",
  "TimeStamp": 1608030111461,
  "ChatId": "chat7795efa07307ead803adfa08b03f0ff5"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |
