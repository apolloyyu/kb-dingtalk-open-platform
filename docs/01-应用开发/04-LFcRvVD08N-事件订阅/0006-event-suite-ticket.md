---
title: "套件票据"
source_url: "https://open.dingtalk.com/document/development/event-suite-ticket"
namespace: "development"
slug: "event-suite-ticket"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "身份与免登 > 套件票据"
doc_id: "RUtDfsITHa"
updated_at: "2025-09-16 22:25:11"
---

> Source: https://open.dingtalk.com/document/development/event-suite-ticket
> Path: 应用开发 / 事件订阅 / 身份与免登 > 套件票据
> Updated: 2025-09-16 22:25:11

# 套件票据

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 套件票据 |
| 英文名称 | suite\_ticket |

## 功能描述

数据为第三方企业应用票据最新suiteTicket，定时每5个小时推送一次。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
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
- `data.suiteTicket`（string）：suiteTicket值。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "suite_ticket",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "suiteTicket": "QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
  }
}
```

SyncHTTP/RDS推送

高优先级事件，为RDS推送方式时，数据插入表open\_sync\_biz\_data中。SyncHTTP推送方式时EventType为SYNC\_HTTP\_PUSH\_HIGH。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.suiteTicket`（string）：suiteTicket值。

### **biz\_data数据示例(biz\_type=2)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 2,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "suite_ticket",
    "suiteTicket": "QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
  }
}
```
