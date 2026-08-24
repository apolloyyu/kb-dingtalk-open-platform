---
title: "医疗通讯录全量同步"
source_url: "https://open.dingtalk.com/document/development/full-synchronization-of-medical-address-book"
namespace: "development"
slug: "full-synchronization-of-medical-address-book"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 医疗 > 医疗通讯录全量同步"
doc_id: "wQejFQjBHx"
updated_at: "2025-08-28 19:47:36"
---

> Source: https://open.dingtalk.com/document/development/full-synchronization-of-medical-address-book
> Path: 应用开发 / 事件订阅 / 行业开放 > 医疗 > 医疗通讯录全量同步
> Updated: 2025-08-28 19:47:36

# 医疗通讯录全量同步

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 医疗通讯录全量同步 |
| 英文名称 | industry\_medical\_full\_sync |

## 功能描述

医疗通讯录发生医疗通讯录全量同步时，推送的医疗通讯录全量同步事件数据说明。

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

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "industry_medical_full_sync",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {}
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。

### **事件体示例**

```
{
  "EventType": "industry_medical_full_sync",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8"
}
```
