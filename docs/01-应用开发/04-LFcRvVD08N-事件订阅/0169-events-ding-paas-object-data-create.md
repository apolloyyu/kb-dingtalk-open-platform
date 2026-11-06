---
title: "主数据实例新增事件"
source_url: "https://open.dingtalk.com/document/development/events-ding-paas-object-data-create"
namespace: "development"
slug: "events-ding-paas-object-data-create"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "客户管理 > 主数据实例新增事件"
doc_id: "XeBmTP4p5v"
updated_at: "2025-08-28 19:47:14"
---

> Source: https://open.dingtalk.com/document/development/events-ding-paas-object-data-create
> Path: 应用开发 / 事件订阅 / 客户管理 > 主数据实例新增事件
> Updated: 2025-08-28 19:47:14

# 主数据实例新增事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 主数据实例新增事件 |
| 英文名称 | ding\_paas\_object\_data\_create |

## 功能描述

主数据实例新增事件数据。

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
- `data.dataId`（string）：变更的数据ID。
- `data.dataType`（string）：数据类型master。
- `data.objectType`（string）：事件类型：  
  \* ding\_paas\_object\_data\_create：创建记录   
  \* ding\_paas\_object\_data\_update：更新记录   
  \* ding\_paas\_object\_data\_delete：删除记录

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ding_paas_object_data_create",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "dataId": "INST-XX",
    "dataType": "master",
    "objectType": "crm_customer"
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
- `ObjectType`（string，必填）：事件类型：  
  \* ding\_paas\_object\_data\_create：创建记录   
  \* ding\_paas\_object\_data\_update：更新记录   
  \* ding\_paas\_object\_data\_delete：删除记录
- `DataId`（string，必填）：变更的数据ID。
- `DataType`（string，必填）：数据类型master。

### **事件体示例**

```
{
  "EventType": "ding_paas_object_data_create",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "ObjectType": "crm_customer",
  "DataId": "INST-XX",
  "DataType": "master"
}
```
