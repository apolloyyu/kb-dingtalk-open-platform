---
title: "服务号接收单聊消息"
source_url: "https://open.dingtalk.com/document/development/service-number-receiving-single-chat-message"
namespace: "development"
slug: "service-number-receiving-single-chat-message"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 服务号接收单聊消息"
doc_id: "6NrHBhXxWK"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-number-receiving-single-chat-message
> Path: 应用开发 / 事件订阅 / 专属开放 > 服务号接收单聊消息
> Updated: 2022-01-19 19:29:22

# 服务号接收单聊消息

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务号接收单聊消息 |
| 英文名称 | isw\_user\_msg\_received |

## 功能描述

服务号收到用户单聊消息的事件,钉钉服务器给开发者推送的事件内容，开发者根据收到的用户消息，结合发消息的接口，实现个性化的自动回复功能。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "isw_user_msg_received",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "toUser": "U4n9RTxxxxxx4AiEiE",
    "msgType": "image",
    "fromUser": "VsIS5Rxxxxxx8ygiEiE",
    "createTime": 145265545673,
    "fromUserId": "2003xxx19",
    "sessionWebhook": "https://oapi.dingtalk.com/xxx",
    "msgId": "dsa8d87y2c3d6",
    "tmpPicUrl": "https://down-cdn.dingtalk.com/dsa8d87y7c8d8c.jpg",
    "senderNick": "发送者01",
    "sessionWebhookExpiredTime": 1442027997327,
    "content": "test content"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "isw_user_msg_received",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "toUser": "U4n9RTxxxxxx4AiEiE",
  "msgType": "image",
  "fromUser": "VsIS5Rxxxxxx8ygiEiE",
  "createTime": 145265545673,
  "fromUserId": "2003xxx19",
  "sessionWebhook": "https://oapi.dingtalk.com/xxx",
  "msgId": "dsa8d87y2c3d6",
  "tmpPicUrl": "https://down-cdn.dingtalk.com/dsa8d87y7c8d8c.jpg",
  "senderNick": "发送者01",
  "sessionWebhookExpiredTime": 1442027997327,
  "content": "test content"
}
```
