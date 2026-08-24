---
title: "CRM客户动态"
source_url: "https://open.dingtalk.com/document/development/crm-customer-dynamics"
namespace: "development"
slug: "crm-customer-dynamics"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "客户管理 > CRM客户动态"
doc_id: "gisJXJVwNW"
updated_at: "2025-08-28 19:47:16"
---

> Source: https://open.dingtalk.com/document/development/crm-customer-dynamics
> Path: 应用开发 / 事件订阅 / 客户管理 > CRM客户动态
> Updated: 2025-08-28 19:47:16

# CRM客户动态

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM客户动态 |
| 英文名称 | crm\_customer\_track |

## 功能描述

CRM客户动态相关信息发生变更时，钉钉通过事件订阅的方式将CRM客户动态相关变更内容推送给开发者。CRM客户动态事件数据推送说明。

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
- `data.tracks`（array）：客户动态相关的数据变更列表。
- `data.tracks[].creator`（string）：动态创建者的userid。
- `data.tracks[].corpId`（string）：客户所在组织的corpId。
- `data.tracks[].customerId`（string）：客户ID。
- `data.tracks[].subType`（integer）：客户动态子类型。
- `data.tracks[].gmtCreate`（long）：动态创建时间。
- `data.tracks[].type`（integer）：客户动态类型。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "crm_customer_track",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "tracks": [
      {
        "creator": "manager1234",
        "corpId": "ding9axxx",
        "customerId": "84c75568-xxx-xxx",
        "subType": 0,
        "type": 107,
        "gmtCreate": 1630474492814
      }
    ]
  }
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
- `biz_data.tracks`（array）：客户动态相关的数据变更列表。
- `biz_data.tracks[].creator`（string）：动态创建者的userid。
- `biz_data.tracks[].corpId`（string）：客户所在组织的corpId。
- `biz_data.tracks[].customerId`（string）：客户ID。
- `biz_data.tracks[].subType`（integer）：客户动态子类型。
- `biz_data.tracks[].gmtCreate`（long）：动态创建时间。
- `biz_data.tracks[].type`（integer）：客户动态类型。

### **biz\_data数据示例(biz\_type=133)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 133,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "crm_customer_track",
    "tracks": [
      {
        "creator": "manager1234",
        "corpId": "ding9axxx",
        "customerId": "84c75568-xxx-xxx",
        "subType": 0,
        "type": 107,
        "gmtCreate": 1630474492814
      }
    ]
  }
}
```
