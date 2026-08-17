---
title: "员工加班事件"
source_url: "https://open.dingtalk.com/document/development/employee-overtime-events"
namespace: "development"
slug: "employee-overtime-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 员工加班事件"
doc_id: "ynUDVb2o6t"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/employee-overtime-events
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 员工加班事件
> Updated: 2022-01-19 19:29:22

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
