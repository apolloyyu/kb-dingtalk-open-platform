---
title: "AI助理安装事件"
source_url: "https://open.dingtalk.com/document/development/ai-assistant-installation-event"
namespace: "development"
slug: "ai-assistant-installation-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > AI 助理 > AI助理安装事件"
doc_id: "CwrYe3iGEH"
updated_at: "2026-09-02 18:14:43"
---

> Source: https://open.dingtalk.com/document/development/ai-assistant-installation-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > AI 助理 > AI助理安装事件
> Updated: 2026-09-02 18:14:43

# AI助理安装事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI助理安装事件 |
| 英文名称 | ai\_assistant\_install |

## 功能描述

当用户组织开通了 AI 助理安装事件后，组织下用户通过分享功能添加（安装）AI 助理时，会触发事件推送。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4804438871/p1099520.png)

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
- `data.eventId`（string）：事件唯一 id。
- `data.unionId`（string）：操作人 unionId。
- `data.aiAssistantId`（string）：AI 助理 ID。
- `data.name`（string）：AI 助理名称。
- `data.description`（string）：AI 助理描述。

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（string，必填）：事件唯一 id。
- `unionId`（string，必填）：操作人 unionId。
- `aiAssistantId`（string，必填）：AI 助理 ID。
- `name`（string，必填）：AI 助理名称。
- `description`（string，必填）：AI 助理描述。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（string）：事件唯一 id。
- `biz_data.unionId`（string）：操作人 unionId。
- `biz_data.aiAssistantId`（string）：AI 助理 ID。
- `biz_data.name`（string）：AI 助理名称。
- `biz_data.description`（string）：AI 助理描述。

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
