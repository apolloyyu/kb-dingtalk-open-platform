---
title: "服务号接收单聊消息"
source_url: "https://open.dingtalk.com/document/development/service-number-receiving-single-chat-message"
namespace: "development"
slug: "service-number-receiving-single-chat-message"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 服务号接收单聊消息"
doc_id: "6NrHBhXxWK"
updated_at: "2025-08-28 19:47:31"
---

> Source: https://open.dingtalk.com/document/development/service-number-receiving-single-chat-message
> Path: 应用开发 / 事件订阅 / 专属开放 > 服务号接收单聊消息
> Updated: 2025-08-28 19:47:31

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.toUser`（string）：接收方账号unionid，即服务号的unionid。
- `data.msgType`（string）：消息类型：  
  - text：文本  
  - image：图片  
  - voice：语音
- `data.fromUser`（string）：发送方帐号unionid。
- `data.createTime`（long）：创建时间，long型时间戳。
- `data.fromUserId`（string）：发送方帐号unionid。
- `data.sessionWebhook`（string）：会话sessionWebhook。
- `data.msgId`（string）：消息id。
- `data.tmpPicUrl`（string）：临时图片下载链接，消息类型为image时，此字段有效。
- `data.senderNick`（string）：发送者昵称。
- `data.sessionWebhookExpiredTime`（long）：sessionWebhook的过期时间。
- `data.content`（string）：文本消息内容，当消息类型为语音时，此处自动识别成文字。

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `toUser`（string）：接收方账号unionid，即服务号的unionid。
- `msgType`（string）：消息类型：  
  - text：文本  
  - image：图片  
  - voice：语音
- `fromUser`（string）：发送方帐号unionid。
- `createTime`（long）：创建时间，long型时间戳。
- `fromUserId`（string）：发送方帐号unionid。
- `sessionWebhook`（string）：会话sessionWebhook。
- `msgId`（string）：消息id。
- `tmpPicUrl`（string）：临时图片下载链接，消息类型为image时，此字段有效。
- `senderNick`（string）：发送者昵称。
- `sessionWebhookExpiredTime`（long）：sessionWebhook的过期时间。
- `content`（string）：文本消息内容，当消息类型为语音时，此处自动识别成文字。

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
