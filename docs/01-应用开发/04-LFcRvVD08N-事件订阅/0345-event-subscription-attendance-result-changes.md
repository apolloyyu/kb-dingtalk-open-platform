---
title: "考勤结果变更"
source_url: "https://open.dingtalk.com/document/development/event-subscription-attendance-result-changes"
namespace: "development"
slug: "event-subscription-attendance-result-changes"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 考勤事件 > 考勤结果变更"
doc_id: "O7a8rNmPhv"
updated_at: "2025-12-08 15:00:11"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-attendance-result-changes
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 考勤事件 > 考勤结果变更
> Updated: 2025-12-08 15:00:11

# 考勤结果变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 考勤结果变更 |
| 英文名称 | attend\_bossCheck\_change |
| 事件BizType | 298 |

## 功能描述

当钉钉考勤结果变更时，钉钉通过事件订阅的方式将考勤结果变更内容推送给开发者。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### 企业内部应用

### 入参

- `EventType`（String）：事件英文名称
- `EventTime`（Long）：事件发生的时间
- `CorpId`（String）：企业corpId
- `BizId`（String）：无业务意义，幂等
- `planId`（integer，必填）：排班Id。
- `userId`（string，必填）：用户userId。
- `workDate`（string，必填）：工作日。
- `action`（string，必填）：推送类型。

### **事件体示例**

```
{
  "CorpId": "1663**351222567",
  "workDate": "2020-11-10 00:00:00",
  "EventType": "attend_bossCheck_change",
  "EventTime": 1663143335567,
  "action": "attend_bossCheck_update",
  "planId": 123,
  "BizId": "1663**35567",
  "userId": "001"
}
```

### 第三方企业应用(biz\_type=298)

数据为RDS和SyncHTTP推送的事件体，当为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 入参

- `corp_id`（String）：企业corp\_id
- `biz_id`（String）：biz\_id无业务意义，幂等
- `biz_type`（Integer）：事件bizType
- `biz_data`（object）：事件bizData介绍
- `biz_data.syncAction`（String）：事件英文名
- `biz_data.planId`（integer）：排班Id。
- `biz_data.userId`（string）：用户userId。
- `biz_data.workDate`（string）：工作日。
- `biz_data.action`（string）：推送类型。

### **biz\_data数据示例如下:**

```
{
  "workDate": "2020-11-10 00:00:00",
  "syncAction": "attend_bossCheck_change",
  "action": "attend_bossCheck_update",
  "planId": 123,
  "userId": "001"
}
```
