---
title: "机器人消息撤回事件"
source_url: "https://open.dingtalk.com/document/development/bot-message-withdrawal-event"
namespace: "development"
slug: "bot-message-withdrawal-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 机器人 > 机器人消息撤回事件"
doc_id: "Y2JWtjqvSY"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/bot-message-withdrawal-event
> Path: 应用开发 / 事件订阅 / 即时通讯 > 机器人 > 机器人消息撤回事件
> Updated: 2022-01-19 19:29:22

# 机器人消息撤回事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 机器人消息撤回事件 |
| 英文名称 | robot\_msg\_recall |

## 功能描述

开发者操作机器人发消息时，机器人消息被撤回可以通知到开发者。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "robot_msg_recall",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "sdjkqwheda",
    "operatTime": 1654641965416,
    "robotCode": "dingnxkjdhasdw",
    "openConversationId": "cidajsddddashqwio",
    "userId": "manager",
    "processQueryKey": "dsadfsafaewsrdefe"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "robot_msg_recall",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "OpenConversationId": "cidajsddddashqwio",
  "UserId": "manager",
  "OperatTime": 1654641965416,
  "UnionId": "sdjkqwheda",
  "ProcessQueryKey": "dsadfsafaewsrdefe",
  "RobotCode": "dingnxkjdhasdw"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=261)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 261,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "OpenConversationId": "cidajsddddashqwio",
    "syncAction": "robot_msg_recall",
    "UserId": "manager",
    "OperatTime": 1654641965416,
    "UnionId": "sdjkqwheda",
    "ProcessQueryKey": "dsadfsafaewsrdefe",
    "RobotCode": "dingnxkjdhasdw"
  }
}
```
