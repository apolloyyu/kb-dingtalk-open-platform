---
title: "假期消费记录变更"
source_url: "https://open.dingtalk.com/document/development/holiday-consumption-record-change"
namespace: "development"
slug: "holiday-consumption-record-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 假期消费记录变更"
doc_id: "oW5jioMFep"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/holiday-consumption-record-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 假期消费记录变更
> Updated: 2022-01-19 19:29:22

# 假期消费记录变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 假期消费记录变更 |
| 英文名称 | leave\_record\_change |

## 功能描述

数据为假期消费记录(请假数据)变更。该数据为在授权微应用的企业中，发生假期消费记录(请假数据)增加、修改的时刻推送。

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
  "eventType": "leave_record_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "leaveViewUnit": "hour",
    "processIdList": [
      "xxxx-xxx-xxx"
    ],
    "corpid": "dingxxx",
    "recordNumPerHour": 100,
    "syncAction": "leave_record_change",
    "userid": "user01",
    "recordId": "59b71a21-xxx",
    "leaveRecordType": "leave",
    "sourceType": "vacation",
    "leaveReason": "管理员导入",
    "param0434": 100.0,
    "leaveCode": "148d5315-xxx",
    "startTime": 1636646400000,
    "endTime": 1636819199000,
    "leaveStatus": "success"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=154)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 154,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "processIdList": [
      "xxxx-xxx-xxx"
    ],
    "corpid": "dingxxx",
    "leave_view_unit": "hour",
    "syncAction": "leave_record_change",
    "leave_status": "success",
    "end_time": 1636819199000,
    "record_num_per_hour": 100,
    "userid": "user01",
    "record_id": "59b71a21-xxx",
    "start_time": 1636646400000,
    "sourceType": "vacation",
    "param0434": 100.0,
    "leave_record_type": "leave",
    "leave_code": "148d5315-xxx",
    "leave_reason": "管理员导入"
  }
}
```
