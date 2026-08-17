---
title: "考勤日统计变更事件"
source_url: "https://open.dingtalk.com/document/development/attendance-day-statistics-change-event"
namespace: "development"
slug: "attendance-day-statistics-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 考勤日统计变更事件"
doc_id: "CJiL9GOZeH"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/attendance-day-statistics-change-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 考勤日统计变更事件
> Updated: 2022-01-19 19:29:22

# 考勤日统计变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 考勤日统计变更事件 |
| 英文名称 | attend\_user\_daily\_summary\_refresh |

## 功能描述

考勤日统计数据发生变更时，钉钉通过事件订阅的方式将变更内容推送给开发者。

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
  "eventType": "attend_user_daily_summary_refresh",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "workDate": "2023-12-12",
    "userId": "1234"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "attend_user_daily_summary_refresh",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "workDate": "2023-12-12",
  "userId": "1234"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=354)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 354,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "workDate": "2023-12-12",
    "syncAction": "attend_user_daily_summary_refresh",
    "userId": "1234"
  }
}
```
