---
title: "考勤结果变更"
source_url: "https://open.dingtalk.com/document/development/event-subscription-attendance-result-changes"
namespace: "development"
slug: "event-subscription-attendance-result-changes"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 考勤事件 > 考勤结果变更"
doc_id: "O7a8rNmPhv"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-attendance-result-changes
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 考勤事件 > 考勤结果变更
> Updated: 2022-01-19 19:29:22

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
