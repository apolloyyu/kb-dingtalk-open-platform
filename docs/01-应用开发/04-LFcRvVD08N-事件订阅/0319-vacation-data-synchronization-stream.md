---
title: "假期数据同步"
source_url: "https://open.dingtalk.com/document/development/vacation-data-synchronization-stream"
namespace: "development"
slug: "vacation-data-synchronization-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 考勤事件 > 假期数据同步"
doc_id: "HBIoWmAkWi"
updated_at: "2025-10-16 14:32:33"
---

> Source: https://open.dingtalk.com/document/development/vacation-data-synchronization-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 考勤事件 > 假期数据同步
> Updated: 2025-10-16 14:32:33

# 假期数据同步

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 假期数据同步 |
| 英文名称 | overtime\_to\_vacation\_data |

## 功能描述

eventType为overtime\_to\_vacation\_data，表示企业发生假期相关的数据变更时，钉钉推送的假期数据同步事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `workHoursPerDay`（integer）：一天的工作时长（单位：小时）。
- `overtimeDayType`（string）：加班类型：  
  - workDay：工作日加班转调休  
  - restDay：休息日加班转调休  
  - holiday：节假日加班转调休
- `workDate`（string）：对应的工作日，格式yyyyMMdd，如：20210312。
- `overtimeDay`（float）：加班转调休时长（以天为单位），例如：0.262。
- `corpId`（string）：企业的corpid。
- `delayEndTime`（long）：假期的延迟失效时间（unix时间戳）。 startTime < endTime <= delayEndTime。
- `leaveCode`（string）：转成的调休假，对应的假期code。
- `overtimeHour`（float）：加班转调休时长（以小时为单位），例如：2.1。 与overtimeDay的换算关系：overtimeDay=overtimeHour/workHoursPerDay。
- `vacationRate`（integer）：加班转调休的比例，即实际工作时长\*vacationRate=调休时长。
- `startTime`（long）：该假期的开始生效时间（unix时间戳）。
- `endTime`（long）：该假期的结束生效时间（unix时间戳）。
- `userId`（string）：对应的员工id。

### **事件体数据示例如下:**

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
    "overtimeDay": "0.262",
    "corpId": "ding33f33xxxx",
    "delayEndTime": 1640966399000,
    "leaveCode": "c1f772d2-xxxx-407e-816a-55be5c245569",
    "overtimeHour": "2.1",
    "vacationRate": 2,
    "startTime": 1615392000000,
    "endTime": 1640966399000,
    "userId": "3350xxxx555"
  }
}
```
