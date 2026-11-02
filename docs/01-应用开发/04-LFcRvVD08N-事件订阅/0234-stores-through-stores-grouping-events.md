---
title: "门店通门店分组事件"
source_url: "https://open.dingtalk.com/document/development/stores-through-stores-grouping-events"
namespace: "development"
slug: "stores-through-stores-grouping-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 行业通用 > 门店通门店分组事件"
doc_id: "8Sgyddort8"
updated_at: "2025-08-28 19:47:45"
---

> Source: https://open.dingtalk.com/document/development/stores-through-stores-grouping-events
> Path: 应用开发 / 事件订阅 / 行业开放 > 行业通用 > 门店通门店分组事件
> Updated: 2025-08-28 19:47:45

# 门店通门店分组事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 门店通门店分组事件 |
| 英文名称 | shop\_group\_event |

## 功能描述

门店通门店分组事件，该事件为门店通门店分组变更的数据推送。

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
- `data.id`（long）：变更人员id。
- `data.type`（string）：变更类型：  
  - create：新增  
  - update：更新  
  - delete：删除  
  - add\_store：添加门店到分组  
  - remove\_store：从分组中移除门店
- `data.bizId`（string）：事件id，幂等。
- `data.storeIdList`（array）：操作的门店列表。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "shop_group_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "bizId": "Idxxxxxx",
    "storeIdList": [
      646890708
    ],
    "id": 12,
    "type": "add_store"
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
- `biz_data.id`（long）：变更人员id。
- `biz_data.type`（string）：变更类型：  
  - create：新增  
  - update：更新  
  - delete：删除  
  - add\_store：添加门店到分组  
  - remove\_store：从分组中移除门店
- `biz_data.bizId`（string）：事件id，幂等。
- `biz_data.storeIdList`（array）：操作的门店列表。

### **biz\_data数据示例(biz\_type=187)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 187,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "shop_group_event",
    "bizId": "Idxxxxxx",
    "storeIdList": [
      646890708
    ],
    "id": 12,
    "type": "add_store"
  }
}
```
