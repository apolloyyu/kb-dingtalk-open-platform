---
title: "机器人消息已读事件"
source_url: "https://open.dingtalk.com/document/development/bot-message-read-event"
namespace: "development"
slug: "bot-message-read-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 机器人 > 机器人消息已读事件"
doc_id: "0dXbHbrfBQ"
updated_at: "2025-08-28 19:46:49"
---

> Source: https://open.dingtalk.com/document/development/bot-message-read-event
> Path: 应用开发 / 事件订阅 / 即时通讯 > 机器人 > 机器人消息已读事件
> Updated: 2025-08-28 19:46:49

# 机器人消息已读事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 机器人消息已读事件 |
| 英文名称 | robot\_msg\_read |

## 功能描述

开发者操作机器人发消息时，机器人消息被读可以通知到开发者。

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
- `data.unionId`（string）：已读消息人的unionId。
- `data.userId`（string）：已读人的userId，如果用户属于corpId对应企业会透出此字段。
- `data.operatTime`（string）：消息已读时间。
- `data.processQueryKey`（string）：消息的processQueryKey。
- `data.robotCode`（string）：机器人编码,当发送消息时指定才会透出此字段。
- `data.openConversationId`（string）：群聊和人与人单聊中机器人发消息，且发消息时指定，才会透出此字段。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "robot_msg_read",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "sdjkqwheda",
    "operatTime": "1654641965416",
    "robotCode": "dingnxkjdhasdw",
    "openConversationId": "cidajsdhqwiocid111",
    "userId": "manager",
    "processQueryKey": "dsadfsafaewsrdefe"
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
- `UnionId`（string）：已读消息人的unionId。
- `UserId`（string）：已读人的userId，如果用户属于corpId对应企业会透出此字段。
- `OperatTime`（string）：消息已读时间。
- `ProcessQueryKey`（string）：消息的processQueryKey。
- `RobotCode`（string）：机器人编码,当发送消息时指定才会透出此字段。
- `OpenConversationId`（string）：群聊和人与人单聊中机器人发消息，且发消息时指定，才会透出此字段。

### **事件体示例**

```
{
  "EventType": "robot_msg_read",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "OpenConversationId": "cidajsdhqwiocid111",
  "UserId": "manager",
  "OperatTime": "1654641965416",
  "UnionId": "sdjkqwheda",
  "ProcessQueryKey": "dsadfsafaewsrdefe",
  "RobotCode": "dingnxkjdhasdw"
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
- `biz_data.UnionId`（string）：已读消息人的unionId。
- `biz_data.UserId`（string）：已读人的userId，如果用户属于corpId对应企业会透出此字段。
- `biz_data.OperatTime`（string）：消息已读时间。
- `biz_data.ProcessQueryKey`（string）：消息的processQueryKey。
- `biz_data.RobotCode`（string）：机器人编码,当发送消息时指定才会透出此字段。
- `biz_data.OpenConversationId`（string）：群聊和人与人单聊中机器人发消息，且发消息时指定，才会透出此字段。

### **biz\_data数据示例(biz\_type=260)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 260,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "OpenConversationId": "cidajsdhqwiocid111",
    "syncAction": "robot_msg_read",
    "UserId": "manager",
    "OperatTime": "1654641965416",
    "UnionId": "sdjkqwheda",
    "ProcessQueryKey": "dsadfsafaewsrdefe",
    "RobotCode": "dingnxkjdhasdw"
  }
}
```
