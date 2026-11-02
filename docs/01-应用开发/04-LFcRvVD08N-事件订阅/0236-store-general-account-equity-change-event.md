---
title: "门店通用户权益变更事件"
source_url: "https://open.dingtalk.com/document/development/store-general-account-equity-change-event"
namespace: "development"
slug: "store-general-account-equity-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 行业通用 > 门店通用户权益变更事件"
doc_id: "PQKKWWjoSi"
updated_at: "2025-08-28 19:47:46"
---

> Source: https://open.dingtalk.com/document/development/store-general-account-equity-change-event
> Path: 应用开发 / 事件订阅 / 行业开放 > 行业通用 > 门店通用户权益变更事件
> Updated: 2025-08-28 19:47:46

# 门店通用户权益变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 门店通用户权益变更事件 |
| 英文名称 | shop\_rights\_event |

## 功能描述

该文档为门店通用户权益变更事件的数据推送说明。

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
- `data.quantity`（long）：权益生效门店数量，关闭权益时无该字段。
- `data.packageCode`（string）：权益套餐Code。
- `data.start`（long）：权益开始时间戳，关闭权益时无该字段。
- `data.end`（long）：权益结束时间戳，关闭权益时无该字段。
- `data.type`（string）：变更类型：  
  - create：新增权益  
  - update：更新权益  
  - close：关闭权益
- `data.bizId`（string）：事件id，幂等。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "shop_rights_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "quantity": 100,
    "packageCode": "RIGHTS_MDT_LEVEL_PRO",
    "bizId": "Idxxxxxx",
    "start": 11222222,
    "end": 11222222,
    "type": "create"
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
- `quantity`（long，必填）：权益生效门店数量，关闭权益时无该字段。
- `packageCode`（string，必填）：权益套餐Code。
- `start`（long，必填）：权益开始时间戳，关闭权益时无该字段。
- `end`（long，必填）：权益结束时间戳，关闭权益时无该字段。
- `type`（string，必填）：变更类型：  
  - create：新增权益  
  - update：更新权益  
  - close：关闭权益
- `bizId`（string，必填）：事件id，幂等。

### **事件体示例**

```
{
  "EventType": "shop_rights_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "quantity": 100,
  "packageCode": "RIGHTS_MDT_LEVEL_PRO",
  "bizId": "Idxxxxxx",
  "start": 11222222,
  "end": 11222222,
  "type": "create"
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
- `biz_data.quantity`（long）：权益生效门店数量，关闭权益时无该字段。
- `biz_data.packageCode`（string）：权益套餐Code。
- `biz_data.start`（long）：权益开始时间戳，关闭权益时无该字段。
- `biz_data.end`（long）：权益结束时间戳，关闭权益时无该字段。
- `biz_data.type`（string）：变更类型：  
  - create：新增权益  
  - update：更新权益  
  - close：关闭权益
- `biz_data.bizId`（string）：事件id，幂等。

### **biz\_data数据示例(biz\_type=211)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 211,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "quantity": 100,
    "syncAction": "shop_rights_event",
    "packageCode": "RIGHTS_MDT_LEVEL_PRO",
    "bizId": "Idxxxxxx",
    "start": 11222222,
    "end": 11222222,
    "type": "create"
  }
}
```
