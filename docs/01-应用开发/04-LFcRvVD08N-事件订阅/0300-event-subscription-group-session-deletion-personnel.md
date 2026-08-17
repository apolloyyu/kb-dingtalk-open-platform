---
title: "群会话删除人员"
source_url: "https://open.dingtalk.com/document/development/event-subscription-group-session-deletion-personnel"
namespace: "development"
slug: "event-subscription-group-session-deletion-personnel"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 群会话变更事件 > 群会话删除人员"
doc_id: "Bnr8vIpTcG"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-group-session-deletion-personnel
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 群会话变更事件 > 群会话删除人员
> Updated: 2022-01-19 19:29:22

# 群会话删除人员

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话删除人员 |
| 英文名称 | chat\_remove\_member |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。eventType为chat\_remove\_member，表示群会话删除人员事件。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "chat_remove_member",
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
    "userId": [
      "user456"
    ],
    "openConversationId": "iis6fGqqqt87xxxxiEiE",
    "operator": "10203029011219896"
  }
}
```
