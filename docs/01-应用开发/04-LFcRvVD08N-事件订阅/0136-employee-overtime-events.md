---
title: "员工加班事件"
source_url: "https://open.dingtalk.com/document/development/employee-overtime-events"
namespace: "development"
slug: "employee-overtime-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 员工加班事件"
doc_id: "ynUDVb2o6t"
updated_at: "2025-08-28 19:46:53"
---

> Source: https://open.dingtalk.com/document/development/employee-overtime-events
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 员工加班事件
> Updated: 2025-08-28 19:46:53

# 员工加班事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 员工加班事件 |
| 英文名称 | attendance\_overtime\_duration |

## 功能描述

自建应用通过考勤开放接口写入加班，触发加班转调休时，推送的员工加班事件数据。

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
- `data.dataList`（array）：数据列表。
- `data.dataList[].workHoursPerDay`（integer）：当天工作时长。
- `data.dataList[].overtimeDayType`（string）：当天日期类型（工作日/休息日/节假日。
- `data.dataList[].overtimeDay`（integer）：加班时长，单位天。
- `data.dataList[].workDate`（long）：加班日期。
- `data.dataList[].corpId`（string）：企业的corpId。
- `data.dataList[].action`（string）：表示用户当次加班转调休动作:  
  - add：表示新增转调休。  
  - modify：表示修改当天转调休时长。
- `data.dataList[].overtimeHour`（float）：加班时长，单位小时。
- `data.dataList[].vacationRate`（float）：表示加班转调休的转换比例，1小时加班 \* vacationRate = x小时的调休。
- `data.dataList[].workMinutesPerDay`（integer）：当天工作时长分钟。
- `data.dataList[].userid`（string）：员工的userid。
- `data.dataList[].key`（string）：key是按企业-用户-日期确定的唯一key，加班统计是按日统计的。
- `data.dataList[].timestamp`（long）：时间戳。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "attendance_overtime_duration",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "dataList": [
      {
        "workHoursPerDay": 8,
        "overtimeDayType": "workDay",
        "workDate": 1684944000000,
        "overtimeDay": 0,
        "corpId": "ding9f50b1xxx741",
        "action": "modify",
        "overtimeHour": 0.0,
        "vacationRate": 1.0,
        "workMinutesPerDay": 480,
        "userid": "26524xxx0",
        "key": "ding78d7bd4dc132dbc324f2fxxxbecb85;26524946xxx420;20xx525",
        "timestamp": 1684980455459
      }
    ]
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
- `dataList`（array）：数据列表。
- `dataList[].workHoursPerDay`（integer）：当天工作时长。
- `dataList[].overtimeDayType`（string）：当天日期类型（工作日/休息日/节假日。
- `dataList[].overtimeDay`（integer）：加班时长，单位天。
- `dataList[].workDate`（long）：加班日期。
- `dataList[].corpId`（string）：企业的corpId。
- `dataList[].action`（string）：表示用户当次加班转调休动作:  
  - add：表示新增转调休。  
  - modify：表示修改当天转调休时长。
- `dataList[].overtimeHour`（float）：加班时长，单位小时。
- `dataList[].vacationRate`（float）：表示加班转调休的转换比例，1小时加班 \* vacationRate = x小时的调休。
- `dataList[].workMinutesPerDay`（integer）：当天工作时长分钟。
- `dataList[].userid`（string）：员工的userid。
- `dataList[].key`（string）：key是按企业-用户-日期确定的唯一key，加班统计是按日统计的。
- `dataList[].timestamp`（long）：时间戳。

### **事件体示例**

```
{
  "EventType": "attendance_overtime_duration",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "dataList": [
    {
      "workHoursPerDay": 8,
      "overtimeDayType": "workDay",
      "workDate": 1684944000000,
      "overtimeDay": 0,
      "corpId": "ding9f50b1xxx741",
      "action": "modify",
      "overtimeHour": 0.0,
      "vacationRate": 1.0,
      "workMinutesPerDay": 480,
      "userid": "26524xxx0",
      "key": "ding78d7bd4dc132dbc324f2fxxxbecb85;26524946xxx420;20xx525",
      "timestamp": 1684980455459
    }
  ]
}
```
