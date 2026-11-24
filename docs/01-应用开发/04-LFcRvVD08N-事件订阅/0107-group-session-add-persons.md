---
title: "群会话添加人员"
source_url: "https://open.dingtalk.com/document/development/group-session-add-persons"
namespace: "development"
slug: "group-session-add-persons"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 会话管理 > 群会话添加人员"
doc_id: "BED6iH4jfK"
updated_at: "2025-08-28 19:46:42"
---

> Source: https://open.dingtalk.com/document/development/group-session-add-persons
> Path: 应用开发 / 事件订阅 / 即时通讯 > 会话管理 > 群会话添加人员
> Updated: 2025-08-28 19:46:42

# 群会话添加人员

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话添加人员 |
| 英文名称 | chat\_add\_member |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。该文档为群会话添加人员事件字段说明。

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
- `data.unionId`（array）：用户发生变更的unionId列表。
- `data.chatId`（string）：会话的ID。
- `data.corpId`（string）：发生群会话变更的企业。
- `data.operatorUnionId`（string）：操作人员的UnionId。
- `data.eventType`（string）：事件类型。
- `data.userId`（array）：用户发生变更的userId列表。
- `data.openConversationId`（string）：群ID。
- `data.operator`（string）：操作人员的userId。
- `data.timeStamp`（long）：时间戳。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "chat_add_member",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 1608027106990,
    "unionId": [
      "3rBUxxxQiEiE"
    ],
    "chatId": "chat28367b03e4b4ca4b5074e1dbfb5d6088",
    "corpId": "dinge8a56572f80bxxxx",
    "operatorUnionId": "iis6fGqqqt87xxxxiEiE",
    "eventType": "chat_add_member",
    "userId": [
      "user456"
    ],
    "openConversationId": "iis6fGqqqt87xxxxiEiE",
    "operator": "10203029011219896"
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
- `unionId`（array）：用户发生变更的unionId列表。
- `chatId`（string）：会话的ID。
- `corpId`（string）：发生群会话变更的企业。
- `operatorUnionId`（string）：操作人员的UnionId。
- `eventType`（string）：事件类型。
- `userId`（array）：用户发生变更的userId列表。
- `openConversationId`（string）：群ID。
- `operator`（string）：操作人员的userId。
- `timeStamp`（long）：时间戳。

### **事件体示例**

```
{
  "EventType": "chat_add_member",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 1608027106990,
  "unionId": [
    "3rBUxxxQiEiE"
  ],
  "chatId": "chat28367b03e4b4ca4b5074e1dbfb5d6088",
  "corpId": "dinge8a56572f80bxxxx",
  "operatorUnionId": "iis6fGqqqt87xxxxiEiE",
  "eventType": "chat_add_member",
  "userId": [
    "user456"
  ],
  "openConversationId": "iis6fGqqqt87xxxxiEiE",
  "operator": "10203029011219896"
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
- `biz_data.unionId`（array）：用户发生变更的unionId列表。
- `biz_data.chatId`（string）：会话的ID。
- `biz_data.corpId`（string）：发生群会话变更的企业。
- `biz_data.operatorUnionId`（string）：操作人员的UnionId。
- `biz_data.eventType`（string）：事件类型。
- `biz_data.userId`（array）：用户发生变更的userId列表。
- `biz_data.openConversationId`（string）：群ID。
- `biz_data.operator`（string）：操作人员的userId。
- `biz_data.timeStamp`（long）：时间戳。

### **biz\_data数据示例(biz\_type=177)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 177,
  "biz_data": {
    "timeStamp": 1608027106990,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionId": [
      "3rBUxxxQiEiE"
    ],
    "chatId": "chat28367b03e4b4ca4b5074e1dbfb5d6088",
    "corpId": "dinge8a56572f80bxxxx",
    "syncAction": "chat_add_member",
    "operatorUnionId": "iis6fGqqqt87xxxxiEiE",
    "eventType": "chat_add_member",
    "userId": [
      "user456"
    ],
    "openConversationId": "iis6fGqqqt87xxxxiEiE",
    "operator": "10203029011219896"
  }
}
```
