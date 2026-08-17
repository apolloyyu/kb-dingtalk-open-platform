---
title: "考勤报表字段变更事件"
source_url: "https://open.dingtalk.com/document/development/attendance-report-field-change-event"
namespace: "development"
slug: "attendance-report-field-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 考勤报表字段变更事件"
doc_id: "2QdHfVXPR7"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/attendance-report-field-change-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 考勤报表字段变更事件
> Updated: 2022-01-19 19:29:22

# 考勤报表字段变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 考勤报表字段变更事件 |
| 英文名称 | attendance\_report\_column\_change |

## 功能描述

当考勤报表字段发生变更（如新增、删除或修改）时，钉钉推送发生变更的字段的信息。

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
  "eventType": "attendance_report_column_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "ding12345",
    "columnId": "10001",
    "type": "ADD"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "attendance_report_column_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpId": "ding12345",
  "columnId": "10001",
  "type": "ADD"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=345)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 345,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "ding12345",
    "syncAction": "attendance_report_column_change",
    "columnId": "10001",
    "type": "ADD"
  }
}
```
