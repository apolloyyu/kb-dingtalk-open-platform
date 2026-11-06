---
title: "医疗行业科室医疗组变动"
source_url: "https://open.dingtalk.com/document/development/changes-in-medical-departments-and-medical-groups-in-the-medical"
namespace: "development"
slug: "changes-in-medical-departments-and-medical-groups-in-the-medical"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 医疗 > 医疗行业科室医疗组变动"
doc_id: "d13aykM6eN"
updated_at: "2025-08-28 19:47:35"
---

> Source: https://open.dingtalk.com/document/development/changes-in-medical-departments-and-medical-groups-in-the-medical
> Path: 应用开发 / 事件订阅 / 行业开放 > 医疗 > 医疗行业科室医疗组变动
> Updated: 2025-08-28 19:47:35

# 医疗行业科室医疗组变动

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 医疗行业科室医疗组变动 |
| 英文名称 | industry\_medical\_dept\_event |

## 功能描述

医疗通讯录发生医疗行业科室医疗组变动时，推送的医疗行业科室医疗组变动事件数据。

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
- `data.deptType`（string）：科室医疗组类型，有以下取值：  
  - 3：科室  
  - 4：医疗组
- `data.type`（string）：变动类型，有以下取值：  
  - add：新增  
  - delete：删除  
  - modify：修改
- `data.deptCode`（string）：科室医疗组code。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "industry_medical_dept_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deptType": "3",
    "type": "add",
    "deptCode": "1"
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
- `deptType`（string）：科室医疗组类型，有以下取值：  
  - 3：科室  
  - 4：医疗组
- `type`（string）：变动类型，有以下取值：  
  - add：新增  
  - delete：删除  
  - modify：修改
- `deptCode`（string）：科室医疗组code。

### **事件体示例**

```
{
  "EventType": "industry_medical_dept_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "deptType": "3",
  "type": "add",
  "deptCode": "1"
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
- `biz_data.deptType`（string）：科室医疗组类型，有以下取值：  
  - 3：科室  
  - 4：医疗组
- `biz_data.type`（string）：变动类型，有以下取值：  
  - add：新增  
  - delete：删除  
  - modify：修改
- `biz_data.deptCode`（string）：科室医疗组code。

### **biz\_data数据示例(biz\_type=195)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 195,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "industry_medical_dept_event",
    "deptType": "3",
    "type": "add",
    "deptCode": "1"
  }
}
```
