---
title: "假期数据同步"
source_url: "https://open.dingtalk.com/document/development/holiday-data-synchronization"
namespace: "development"
slug: "holiday-data-synchronization"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 假期数据同步"
doc_id: "QBAFUr6VK5"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/holiday-data-synchronization
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 假期数据同步
> Updated: 2022-01-19 19:29:22

# 假期数据同步

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 假期数据同步 |
| 英文名称 | overtime\_to\_vacation\_data |

## 功能描述

该数据为企业发生假期相关的数据变更时推送。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "overtime_to_vacation_data",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "workHoursPerDay": 8,
    "overtimeDayType": "restDay",
    "workDate": "20230521",
    "overtimeDay": 0.262,
    "corpId": "ding33f33xxxx",
    "delayEndTime": 1640966399000,
    "leaveCode": "c1f772d2-xxxx-407e-816a-55be5c245569",
    "overtimeHour": 2.1,
    "vacationRate": 2,
    "startTime": 1615392000000,
    "endTime": 1640966399000,
    "userId": "3350xxxx555"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=67)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 67,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "overtimeDay": 0.262,
    "corpId": "ding33f33xxxx",
    "syncAction": "overtime_to_vacation_data",
    "delayEndTime": 1640966399000,
    "overtimeHour": 2.1,
    "vacationRate": 2,
    "userId": "3350xxxx555",
    "workHoursPerDay": 8,
    "overtimeDayType": "restDay",
    "workDate": "20230521",
    "leaveCode": "c1f772d2-xxxx-407e-816a-55be5c245569",
    "startTime": 1615392000000,
    "endTime": 1640966399000
  }
}
```
