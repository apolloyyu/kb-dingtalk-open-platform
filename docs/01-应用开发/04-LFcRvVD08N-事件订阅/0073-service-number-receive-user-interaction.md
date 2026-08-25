---
title: "服务号接收用户交互"
source_url: "https://open.dingtalk.com/document/development/service-number-receive-user-interaction"
namespace: "development"
slug: "service-number-receive-user-interaction"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务窗 > 服务号接收用户交互"
doc_id: "x6dXM4Xx0t"
updated_at: "2025-08-28 19:46:40"
---

> Source: https://open.dingtalk.com/document/development/service-number-receive-user-interaction
> Path: 应用开发 / 事件订阅 / 服务窗 > 服务号接收用户交互
> Updated: 2025-08-28 19:46:40

# 服务号接收用户交互

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务号接收用户交互 |
| 英文名称 | isw\_user\_event\_received |

## 功能描述

服务号收到用户的交互事件, 目前只有菜单点击事件。

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
- `data.fromUser`（string）：发送方帐号unionid。
- `data.createTime`（long）：发生时间。
- `data.toUser`（string）：接收方账号unionid，即服务号的unionid。
- `data.actionType`（string）：触发事件的动作类型：  
  \* click：拉取自定义消息  
  \* view：跳转链接
- `data.actionKey`（string）：事件KEY值，与自定义菜单接口中KEY值对应。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "isw_user_event_received",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "toUser": "abab1201",
    "actionType": "click",
    "fromUser": "abab124",
    "createTime": 1442027997327,
    "actionKey": "V001_TODAY_AIR"
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
- `fromUser`（string，必填）：发送方帐号unionid。
- `createTime`（long，必填）：发生时间。
- `toUser`（string，必填）：接收方账号unionid，即服务号的unionid。
- `actionType`（string，必填）：触发事件的动作类型：  
  \* click：拉取自定义消息  
  \* view：跳转链接
- `actionKey`（string，必填）：事件KEY值，与自定义菜单接口中KEY值对应。

### **事件体示例**

```
{
  "EventType": "isw_user_event_received",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "toUser": "abab1201",
  "actionType": "click",
  "fromUser": "abab124",
  "createTime": 1442027997327,
  "actionKey": "V001_TODAY_AIR"
}
```
