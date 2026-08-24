---
title: "群会话用户主动退群"
source_url: "https://open.dingtalk.com/document/development/group-session-users-actively-withdraw-from-the-group"
namespace: "development"
slug: "group-session-users-actively-withdraw-from-the-group"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 会话管理 > 群会话用户主动退群"
doc_id: "lUqMzdAzxo"
updated_at: "2025-08-28 19:46:44"
---

> Source: https://open.dingtalk.com/document/development/group-session-users-actively-withdraw-from-the-group
> Path: 应用开发 / 事件订阅 / 即时通讯 > 会话管理 > 群会话用户主动退群
> Updated: 2025-08-28 19:46:44

# 群会话用户主动退群

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话用户主动退群 |
| 英文名称 | chat\_quit |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。该文档为群会话删除人员事件推送数据说明。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.timeStamp`（long）：时间戳。
- `data.chatId`（string）：会话的ID。
- `data.corpId`（string）：发生群会话变更的企业。
- `data.operatorUnionId`（string）：主动退群人员的UnionId。
- `data.openConversationId`（string）：群ID。
- `data.operator`（string）：主动退群人员的userId。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "chat_quit",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 1608026903228,
    "chatId": "chat676e50a07xxxx",
    "corpId": "dinge8a56572f80bxxxx",
    "operatorUnionId": "zRboxxxcpAiEiE",
    "openConversationId": "cidmfWxxxx",
    "operator": "user456"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `timeStamp`（long）：时间戳。
- `chatId`（string）：会话的ID。
- `corpId`（string）：发生群会话变更的企业。
- `operatorUnionId`（string）：主动退群人员的UnionId。
- `openConversationId`（string）：群ID。
- `operator`（string）：主动退群人员的userId。

### **事件体示例**

```
{
  "EventType": "chat_quit",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 1608026903228,
  "chatId": "chat676e50a07xxxx",
  "corpId": "dinge8a56572f80bxxxx",
  "operatorUnionId": "zRboxxxcpAiEiE",
  "openConversationId": "cidmfWxxxx",
  "operator": "user456"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.timeStamp`（long）：时间戳。
- `biz_data.chatId`（string）：会话的ID。
- `biz_data.corpId`（string）：发生群会话变更的企业。
- `biz_data.operatorUnionId`（string）：主动退群人员的UnionId。
- `biz_data.openConversationId`（string）：群ID。
- `biz_data.operator`（string）：主动退群人员的userId。

### **biz\_data数据示例(biz\_type=179)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 179,
  "biz_data": {
    "timeStamp": 1608026903228,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "chatId": "chat676e50a07xxxx",
    "corpId": "dinge8a56572f80bxxxx",
    "syncAction": "chat_quit",
    "operatorUnionId": "zRboxxxcpAiEiE",
    "openConversationId": "cidmfWxxxx",
    "operator": "user456"
  }
}
```
