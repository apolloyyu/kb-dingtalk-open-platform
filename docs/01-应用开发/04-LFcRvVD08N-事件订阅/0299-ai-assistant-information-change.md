---
title: "AI助理信息变更"
source_url: "https://open.dingtalk.com/document/development/ai-assistant-information-change"
namespace: "development"
slug: "ai-assistant-information-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > AI 助理 > AI助理信息变更"
doc_id: "HVqAvN6FEK"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/ai-assistant-information-change
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > AI 助理 > AI助理信息变更
> Updated: 2022-01-19 19:29:22

# AI助理信息变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI助理信息变更 |
| 英文名称 | ai\_assistant\_change |

## 功能描述

AI 助理的信息变更，包括AI助理的创建、修改、删除事件。
温馨提醒：
点击助理创建之后，没有任何信息填写后，就会创建一个初始版本的 AI 助理，用于调试和预览。之后填写后会通过修改事件同步相关变更。

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
  "eventType": "ai_assistant_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "assistantId": "83f***612",
    "unionId": "Q2B***EiE",
    "icon": "$iw***QwA",
    "name": "AI 助理",
    "action": "create"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "ai_assistant_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "assistantId": "83f***612",
  "unionId": "Q2B***EiE",
  "icon": "$iw***QwA",
  "name": "AI 助理",
  "action": "create"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=381)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 381,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "assistantId": "83f***612",
    "unionId": "Q2B***EiE",
    "syncAction": "ai_assistant_change",
    "icon": "$iw***QwA",
    "name": "AI 助理",
    "action": "create"
  }
}
```
