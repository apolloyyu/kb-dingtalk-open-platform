---
title: "主数据实例更新事件"
source_url: "https://open.dingtalk.com/document/development/event-ding-paas-object-data-update"
namespace: "development"
slug: "event-ding-paas-object-data-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "客户管理 > 主数据实例更新事件"
doc_id: "3MSC0w0ogd"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-ding-paas-object-data-update
> Path: 应用开发 / 事件订阅 / 客户管理 > 主数据实例更新事件
> Updated: 2022-01-19 19:29:22

# 主数据实例更新事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 主数据实例更新事件 |
| 英文名称 | ding\_paas\_object\_data\_update |

## 功能描述

主数据实例更新事件数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ding_paas_object_data_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "dataId": "INSTXXX",
    "formCode": "PROC-XXX",
    "dataType": "master",
    "objectType": "crm_customer"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "ding_paas_object_data_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "ObjectType": "crm_customer",
  "DataId": "INSTXXX",
  "DataType": "master",
  "FormCode": "PROC-XXX"
}
```
