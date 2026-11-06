---
title: "AI助理信息变更"
source_url: "https://open.dingtalk.com/document/development/ai-assistant-information-change"
namespace: "development"
slug: "ai-assistant-information-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > AI 助理 > AI助理信息变更"
doc_id: "HVqAvN6FEK"
updated_at: "2025-08-28 19:46:20"
---

> Source: https://open.dingtalk.com/document/development/ai-assistant-information-change
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > AI 助理 > AI助理信息变更
> Updated: 2025-08-28 19:46:20

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.assistantId`（string）：助理的 ID，唯一标识一个 AI 助理
- `data.unionId`（string）：助理创建人的用户 ID
- `data.icon`（string）：助理的头像（图标），采用钉钉多媒体文件的 Media ID 标识
- `data.name`（string）：助理的名称
- `data.action`（string）：助理信息变更的动作，create/update/delete分别对应创建、修改、删除
- `data.description`（string）：助理的描述

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `assistantId`（string，必填）：助理的 ID，唯一标识一个 AI 助理
- `unionId`（string，必填）：助理创建人的用户 ID
- `icon`（string，必填）：助理的头像（图标），采用钉钉多媒体文件的 Media ID 标识
- `name`（string，必填）：助理的名称
- `action`（string，必填）：助理信息变更的动作，create/update/delete分别对应创建、修改、删除
- `description`（string，必填）：助理的描述

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.assistantId`（string）：助理的 ID，唯一标识一个 AI 助理
- `biz_data.unionId`（string）：助理创建人的用户 ID
- `biz_data.icon`（string）：助理的头像（图标），采用钉钉多媒体文件的 Media ID 标识
- `biz_data.name`（string）：助理的名称
- `biz_data.action`（string）：助理信息变更的动作，create/update/delete分别对应创建、修改、删除
- `biz_data.description`（string）：助理的描述

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
