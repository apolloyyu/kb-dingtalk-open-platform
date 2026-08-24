---
title: "日程变更"
source_url: "https://open.dingtalk.com/document/development/event-calendar-event-change"
namespace: "development"
slug: "event-calendar-event-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 日程 > 日程变更"
doc_id: "sDgVZU4Kpa"
updated_at: "2025-08-27 16:11:01"
---

> Source: https://open.dingtalk.com/document/development/event-calendar-event-change
> Path: 应用开发 / 事件订阅 / 协同 > 日程 > 日程变更
> Updated: 2025-08-27 16:11:01

# 日程变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 日程变更 |
| 英文名称 | calendar\_event\_change |

## 功能描述

日程变更事件推送内容说明。

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
- `data.calendarEventId`（string）：发生变更的日程id。
- `data.calendarEventUpdateTime`（long）：日程更新时间戳。
- `data.calendarId`（string）：日历Id。
- `data.unionIdList`（array）：本次日程变更影响的用户unionId列表。
- `data.changeType`（string）：业务类型：  
  \* created：创建  
  \* updated：更新  
  \* cancelled：取消  
  \* deleteView：用户在自己本地删除日程
- `data.operator`（object）：操作类型。
- `data.operator.type`（string）：日程操作者类型。
- `data.legacyCalendarEventId`（string）：遗留日程id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "calendar_event_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "calendarEventId": "eWFOdXI5bjZIxxxx",
    "calendarEventUpdateTime": 168489710004,
    "calendarId": "xxxxxxxxxxx",
    "unionIdList": [
      "AlmxxxxwiEiE"
    ],
    "changeType": "create",
    "operator": {
      "type": "user"
    },
    "legacyCalendarEventId": "xxxxxxxxxxx"
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
- `calendarEventId`（string）：发生变更的日程id。
- `calendarEventUpdateTime`（long）：日程更新时间戳。
- `calendarId`（string）：日历Id。
- `unionIdList`（array）：本次日程变更影响的用户unionId列表。
- `changeType`（string）：业务类型：  
  \* created：创建  
  \* updated：更新  
  \* cancelled：取消  
  \* deleteView：用户在自己本地删除日程
- `operator`（object）：操作类型。
- `operator.type`（string）：日程操作者类型。
- `legacyCalendarEventId`（string）：遗留日程id。

### **事件体示例**

```
{
  "EventType": "calendar_event_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "calendarEventId": "eWFOdXI5bjZIxxxx",
  "calendarEventUpdateTime": 168489710004,
  "calendarId": "xxxxxxxxxxx",
  "unionIdList": [
    "AlmxxxxwiEiE"
  ],
  "changeType": "create",
  "operator": {
    "type": "user"
  },
  "legacyCalendarEventId": "xxxxxxxxxxx"
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
- `biz_data.calendarEventId`（string）：发生变更的日程id。
- `biz_data.calendarEventUpdateTime`（long）：日程更新时间戳。
- `biz_data.calendarId`（string）：日历Id。
- `biz_data.unionIdList`（array）：本次日程变更影响的用户unionId列表。
- `biz_data.changeType`（string）：业务类型：  
  \* created：创建  
  \* updated：更新  
  \* cancelled：取消  
  \* deleteView：用户在自己本地删除日程
- `biz_data.operator`（object）：操作类型。
- `biz_data.operator.type`（string）：日程操作者类型。
- `biz_data.legacyCalendarEventId`（string）：遗留日程id。

### **biz\_data数据示例(biz\_type=100)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 100,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "calendarEventId": "eWFOdXI5bjZIxxxx",
    "calendarEventUpdateTime": 168489710004,
    "calendarId": "xxxxxxxxxxx",
    "unionIdList": [
      "AlmxxxxwiEiE"
    ],
    "syncAction": "calendar_event_change",
    "changeType": "create",
    "operator": {
      "type": "user"
    },
    "legacyCalendarEventId": "xxxxxxxxxxx"
  }
}
```
