---
title: "假期消费记录变更"
source_url: "https://open.dingtalk.com/document/development/holiday-consumption-record-change"
namespace: "development"
slug: "holiday-consumption-record-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 假期消费记录变更"
doc_id: "oW5jioMFep"
updated_at: "2025-08-28 19:46:55"
---

> Source: https://open.dingtalk.com/document/development/holiday-consumption-record-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 假期消费记录变更
> Updated: 2025-08-28 19:46:55

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.processIdList`（array）：消费记录相关审批单。
- `data.recordId`（string）：假期消费记录唯一标识。
- `data.corpid`（string）：组织ID。
- `data.leaveViewUnit`（string）：显示单位：  
  - day：天  
  - hour：小时
- `data.leaveStatus`（string）：请假状态：  
  - init：请假申请  
  - success：请假通过  
  - refuse：请假被拒  
  - abort：请假终止  
  - revoke：撤销已同意的请假单
- `data.syncAction`（string）：同步行为。
- `data.endTime`（long）：额度有效期结束时间，毫秒级时间戳。
- `data.recordNumPerHour`（long）：以小时计算的消费额度。
- `data.userid`（string）：员工的userid。
- `data.startTime`（long）：额度有效期开始时间，毫秒级时间戳。
- `data.param0434`（double）：以天计算的消费额度。
- `data.leaveRecordType`（string）：假期记录类型：  
  - leave：请假  
  - update：新配额
- `data.leaveCode`（string）：假期类型唯一标识。
- `data.leaveReason`（string）：原因。
- `data.sourceType`（string）：事件来源。

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

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.processIdList`（array）：消费记录相关审批单。
- `biz_data.record_id`（string）：假期消费记录唯一标识。
- `biz_data.corpid`（string）：组织ID。
- `biz_data.leave_view_unit`（string）：显示单位：  
  - day：天  
  - hour：小时
- `biz_data.leave_status`（string）：请假状态：  
  - init：请假申请  
  - success：请假通过  
  - refuse：请假被拒  
  - abort：请假终止  
  - revoke：撤销已同意的请假单
- `biz_data.syncAction`（string）：同步行为。
- `biz_data.end_time`（long）：额度有效期结束时间，毫秒级时间戳。
- `biz_data.record_num_per_hour`（long）：以小时计算的消费额度。
- `biz_data.userid`（string）：员工的userid。
- `biz_data.start_time`（long）：额度有效期开始时间，毫秒级时间戳。
- `biz_data.param0434`（double）：以天计算的消费额度。
- `biz_data.leave_record_type`（string）：假期记录类型：  
  - leave：请假  
  - update：新配额
- `biz_data.leave_code`（string）：假期类型唯一标识。
- `biz_data.leave_reason`（string）：原因。
- `biz_data.sourceType`（string）：事件来源。

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
