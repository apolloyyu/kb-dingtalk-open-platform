---
title: "AI助理安装事件"
source_url: "https://open.dingtalk.com/document/development/ai-assistant-installation-event"
namespace: "development"
slug: "ai-assistant-installation-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > AI 助理 > AI助理安装事件"
doc_id: "CwrYe3iGEH"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/ai-assistant-installation-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > AI 助理 > AI助理安装事件
> Updated: 2022-01-19 19:29:22

# AI助理安装事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI助理安装事件 |
| 英文名称 | ai\_assistant\_install |

## 功能描述

当用户组织开通了 AI 助理安装事件后，组织下用户通过分享功能添加（安装）AI 助理时，会触发事件推送。
![安装 AI 助理](https://img.alicdn.com/imgextra/i3/O1CN01VFQmTS1MPc92z9lFQ_!!6000000001427-2-tps-360-588.png)

> 支持[组织内使用的 AI 助理](https://open.dingtalk.com/document/ai-dev/create-a-dingtalk-ai-assistant)和[可跨组织使用的 AI 助理](https://open.dingtalk.com/document/ai-dev/creative-dingtalk-ai-assistant)。

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
  "eventType": "ai_assistant_install",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "eventId": "fa491439984641e7bbf0ea73796xxx",
    "unionId": "RHCAZvgbllRse8xrcn68exxxxx",
    "aiAssistantId": "8d874fc30c93459b80c58xxx08db53cc",
    "name": "AI 助手",
    "description": "我是一个专业的商品推荐专员"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "ai_assistant_install",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "fa491439984641e7bbf0ea73796xxx",
  "unionId": "RHCAZvgbllRse8xrcn68exxxxx",
  "aiAssistantId": "8d874fc30c93459b80c58xxx08db53cc",
  "name": "AI 助手",
  "description": "我是一个专业的商品推荐专员"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=368)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 368,
  "biz_data": {
    "eventId": "fa491439984641e7bbf0ea73796xxx",
    "unionId": "RHCAZvgbllRse8xrcn68exxxxx",
    "syncAction": "ai_assistant_install",
    "aiAssistantId": "8d874fc30c93459b80c58xxx08db53cc",
    "name": "AI 助手",
    "description": "我是一个专业的商品推荐专员"
  }
}
```
