---
title: "门店通节点变更事件"
source_url: "https://open.dingtalk.com/document/development/store-pass-node-change-event"
namespace: "development"
slug: "store-pass-node-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 行业通用 > 门店通节点变更事件"
doc_id: "qG8F4lFrgw"
updated_at: "2025-08-28 19:47:44"
---

> Source: https://open.dingtalk.com/document/development/store-pass-node-change-event
> Path: 应用开发 / 事件订阅 / 行业开放 > 行业通用 > 门店通节点变更事件
> Updated: 2025-08-28 19:47:44

# 门店通节点变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 门店通节点变更事件 |
| 英文名称 | shop\_node\_event |

## 功能描述

门店架构节点变更事件，该事件为门店架构节点变更时的数据推送。

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
- `data.id`（long）：变更节点id。
- `data.code`（string）：门店通通讯录标识。
- `data.type`（string）：变更类型：  
  - create：新增。  
  - update：更新。  
  - delete：删除。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "shop_node_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "code": "alt-contact:ODk4MDAx",
    "id": 652893003,
    "type": "create"
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
- `biz_data.id`（long）：变更节点id。
- `biz_data.code`（string）：门店通通讯录标识。
- `biz_data.type`（string）：变更类型：  
  - create：新增。  
  - update：更新。  
  - delete：删除。

### **biz\_data数据示例(biz\_type=185)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 185,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "code": "alt-contact:ODk4MDAx",
    "syncAction": "shop_node_event",
    "id": 652893003,
    "type": "create"
  }
}
```
