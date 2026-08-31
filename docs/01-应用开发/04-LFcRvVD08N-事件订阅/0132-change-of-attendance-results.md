---
title: "考勤结果变更"
source_url: "https://open.dingtalk.com/document/development/change-of-attendance-results"
namespace: "development"
slug: "change-of-attendance-results"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 考勤结果变更"
doc_id: "wKFqONGaK6"
updated_at: "2025-08-28 19:46:54"
---

> Source: https://open.dingtalk.com/document/development/change-of-attendance-results
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 考勤结果变更
> Updated: 2025-08-28 19:46:54

# 考勤结果变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 考勤结果变更 |
| 英文名称 | attend\_bossCheck\_change |

## 功能描述

当钉钉管理员修改考勤结果变更时，钉钉通过事件订阅的方式将考勤结果变更内容推送给开发者。

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
- `data.planId`（integer）：排班Id。
- `data.userId`（string）：用户userId。
- `data.workDate`（string）：工作日。
- `data.action`（string）：推送类型。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "attend_bossCheck_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "workDate": "2020-11-10 00:00:00",
    "action": "attend_bossCheck_update",
    "planId": 123,
    "userId": "001"
  }
}
```

HTTP推送

### 入参

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `planId`（integer，必填）：排班Id。
- `userId`（string，必填）：用户userId。
- `workDate`（string，必填）：工作日。
- `action`（string，必填）：推送类型。

### **事件体示例**

```
{
  "EventType": "attend_bossCheck_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "workDate": "2020-11-10 00:00:00",
  "action": "attend_bossCheck_update",
  "planId": 123,
  "userId": "001"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 入参

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.planId`（integer）：排班Id。
- `biz_data.userId`（string）：用户userId。
- `biz_data.workDate`（string）：工作日。
- `biz_data.action`（string）：推送类型。

### **biz\_data数据示例(biz\_type=298)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 298,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "workDate": "2020-11-10 00:00:00",
    "syncAction": "attend_bossCheck_change",
    "action": "attend_bossCheck_update",
    "planId": 123,
    "userId": "001"
  }
}
```
