---
title: "医疗行业科室医疗组变动"
source_url: "https://open.dingtalk.com/document/development/changes-in-medical-departments-and-medical-groups-in-the-medical"
namespace: "development"
slug: "changes-in-medical-departments-and-medical-groups-in-the-medical"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 医疗 > 医疗行业科室医疗组变动"
doc_id: "d13aykM6eN"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/changes-in-medical-departments-and-medical-groups-in-the-medical
> Path: 应用开发 / 事件订阅 / 行业开放 > 医疗 > 医疗行业科室医疗组变动
> Updated: 2022-01-19 19:29:22

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
