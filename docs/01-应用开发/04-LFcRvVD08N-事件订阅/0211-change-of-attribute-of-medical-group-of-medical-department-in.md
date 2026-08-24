---
title: "医疗行业科室医疗组属性变动"
source_url: "https://open.dingtalk.com/document/development/change-of-attribute-of-medical-group-of-medical-department-in"
namespace: "development"
slug: "change-of-attribute-of-medical-group-of-medical-department-in"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 医疗 > 医疗行业科室医疗组属性变动"
doc_id: "m7wcdvjQ2X"
updated_at: "2025-08-28 19:47:36"
---

> Source: https://open.dingtalk.com/document/development/change-of-attribute-of-medical-group-of-medical-department-in
> Path: 应用开发 / 事件订阅 / 行业开放 > 医疗 > 医疗行业科室医疗组属性变动
> Updated: 2025-08-28 19:47:36

# 医疗行业科室医疗组属性变动

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 医疗行业科室医疗组属性变动 |
| 英文名称 | industry\_medical\_dept\_prop\_event |

## 功能描述

医疗通讯录发生医疗行业科室医疗组变动时，推送的医疗行业科室医疗组变动事件数据。

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
- `data.deptType`（string）：科室医疗组类型，有以下取值：  
  - 3：科室  
  - 4：医疗组
- `data.type`（string）：变动类型，有以下取值：  
  - add：新增  
  - delete：删除  
  - modify：修改
- `data.deptCode`（string）：科室医疗组code。
- `data.propCode`（string）：属性code，有以下取值：  
  - 1：科室主任  
  - 2：住院总医师  
  - 11：科室副主任  
  - 41：科室病历质控员  
  - 42：科室信息维护员  
  - 43：科室医疗权限管理组长  
  - 45：教学秘书  
  - 46：临床路径管理员

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "industry_medical_dept_prop_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deptType": "3",
    "type": "add",
    "deptCode": "9332",
    "propCode": "1"
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
- `propCode`（string）：属性code，有以下取值：  
  - 1：科室主任  
  - 2：住院总医师  
  - 11：科室副主任  
  - 41：科室病历质控员  
  - 42：科室信息维护员  
  - 43：科室医疗权限管理组长  
  - 45：教学秘书  
  - 46：临床路径管理员

### **事件体示例**

```
{
  "EventType": "industry_medical_dept_prop_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "deptType": "3",
  "type": "add",
  "deptCode": "9332",
  "propCode": "1"
}
```
