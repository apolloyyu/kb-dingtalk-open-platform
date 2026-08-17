---
title: "员工打卡事件"
source_url: "https://open.dingtalk.com/document/development/employee-clock-in-event"
namespace: "development"
slug: "employee-clock-in-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 员工打卡事件"
doc_id: "TrTp3BgsuN"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/employee-clock-in-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 员工打卡事件
> Updated: 2022-01-19 19:29:22

# 员工打卡事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 员工打卡事件 |
| 英文名称 | attendance\_check\_record |

## 功能描述

当考勤数据发生员工打卡时，钉钉推送的员工打卡事件数据。

> 同一个人一分钟打卡多次只算一次，即同一个人一分钟只能推送一次员工打卡事件。

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
  "eventType": "attendance_check_record",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "dataList": [
      {
        "address": "中国科学院xxx物理研究所(浙江海外高层次人才创新xxx东)",
        "corpId": "dingxxxx",
        "checkTime": 1570791880000,
        "locationResult": "Normal",
        "groupId": "4C63xxxx",
        "latitude": 30.285230848524307,
        "bizId": "FF62xxxx",
        "locationMethod": "MAP",
        "userId": "0126xxxx",
        "deviceSN": "160xxxxx6KN0294",
        "checkByUser": true,
        "longitude": 120.01713514539931
      }
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "attendance_check_record",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "dataList": [
    {
      "address": "中国科学院xxx物理研究所(浙江海外高层次人才创新xxx东)",
      "corpId": "dingxxxx",
      "checkTime": 1570791880000,
      "locationResult": "Normal",
      "groupId": "4C63xxxx",
      "latitude": 30.285230848524307,
      "bizId": "FF62xxxx",
      "locationMethod": "MAP",
      "userId": "0126xxxx",
      "deviceSN": "160xxxxx6KN0294",
      "checkByUser": true,
      "longitude": 120.01713514539931
    }
  ]
}
```
