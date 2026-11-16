---
title: "企业内部应用发布"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-application-release"
namespace: "development"
slug: "enterprise-self-built-application-release"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 企业内部应用发布"
doc_id: "8BLaWwtlNJ"
updated_at: "2025-08-28 19:47:28"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-application-release
> Path: 应用开发 / 事件订阅 / 应用管理 > 企业内部应用发布
> Updated: 2025-08-28 19:47:28

# 企业内部应用发布

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业内部应用发布 |
| 英文名称 | inner\_app\_release |

## 功能描述

当开发者对企业内部应用进行发布时，推送事件相关数据。

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
- `data.eventId`（string）：事件的唯一 ID。
- `data.operatorUnionId`（string）：操作人 unionId。
- `data.unifiedAppId`（string）：应用唯一标识。
- `data.name`（string）：应用名称。
- `data.desc`（string）：应用描述。
- `data.icon`（string）：应用图标（Media ID）。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "inner_app_release",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "eventId": "4d1***de",
    "icon": "icon",
    "name": "name",
    "operatorUnionId": "RHC***xxx",
    "unifiedAppId": "7f1***7bc",
    "desc": "desc"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（string，必填）：事件的唯一 ID。
- `operatorUnionId`（string，必填）：操作人 unionId。
- `unifiedAppId`（string，必填）：应用唯一标识。
- `name`（string，必填）：应用名称。
- `desc`（string，必填）：应用描述。
- `icon`（string，必填）：应用图标（Media ID）。

### **事件体示例**

```
{
  "EventType": "inner_app_release",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "4d1***de",
  "icon": "icon",
  "name": "name",
  "operatorUnionId": "RHC***xxx",
  "unifiedAppId": "7f1***7bc",
  "desc": "desc"
}
```
