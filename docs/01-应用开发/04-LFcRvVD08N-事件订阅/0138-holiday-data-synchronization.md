---
title: "假期数据同步"
source_url: "https://open.dingtalk.com/document/development/holiday-data-synchronization"
namespace: "development"
slug: "holiday-data-synchronization"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 假期数据同步"
doc_id: "QBAFUr6VK5"
updated_at: "2025-08-28 19:46:54"
---

> Source: https://open.dingtalk.com/document/development/holiday-data-synchronization
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 假期数据同步
> Updated: 2025-08-28 19:46:54

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.workHoursPerDay`（integer）：一天的工作时长（单位：小时）。
- `data.overtimeDayType`（string）：加班类型：  
  - workDay：工作日加班转调休  
  - restDay：休息日加班转调休  
  - holiday：节假日加班转调休
- `data.workDate`（string）：对应的工作日，格式yyyyMMdd，如：20210312。
- `data.overtimeDay`（float）：加班转调休时长（以天为单位），例如：0.262。
- `data.corpId`（string）：企业的corpid。
- `data.delayEndTime`（long）：假期的延迟失效时间（unix时间戳）。 startTime < endTime <= delayEndTime。
- `data.leaveCode`（string）：转成的调休假，对应的假期code。
- `data.overtimeHour`（float）：加班转调休时长（以小时为单位），例如：2.1。 与overtimeDay的换算关系：overtimeDay=overtimeHour/workHoursPerDay。
- `data.vacationRate`（integer）：加班转调休的比例，即实际工作时长\*vacationRate=调休时长。
- `data.startTime`（long）：该假期的开始生效时间（unix时间戳）。
- `data.endTime`（long）：该假期的结束生效时间（unix时间戳）。
- `data.userId`（string）：对应的员工id。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.workHoursPerDay`（integer）：一天的工作时长（单位：小时）。
- `biz_data.overtimeDayType`（string）：加班类型：  
  - workDay：工作日加班转调休  
  - restDay：休息日加班转调休  
  - holiday：节假日加班转调休
- `biz_data.workDate`（string）：对应的工作日，格式yyyyMMdd，如：20210312。
- `biz_data.overtimeDay`（float）：加班转调休时长（以天为单位），例如：0.262。
- `biz_data.corpId`（string）：企业的corpid。
- `biz_data.delayEndTime`（long）：假期的延迟失效时间（unix时间戳）。 startTime < endTime <= delayEndTime。
- `biz_data.leaveCode`（string）：转成的调休假，对应的假期code。
- `biz_data.overtimeHour`（float）：加班转调休时长（以小时为单位），例如：2.1。 与overtimeDay的换算关系：overtimeDay=overtimeHour/workHoursPerDay。
- `biz_data.vacationRate`（integer）：加班转调休的比例，即实际工作时长\*vacationRate=调休时长。
- `biz_data.startTime`（long）：该假期的开始生效时间（unix时间戳）。
- `biz_data.endTime`（long）：该假期的结束生效时间（unix时间戳）。
- `biz_data.userId`（string）：对应的员工id。

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
