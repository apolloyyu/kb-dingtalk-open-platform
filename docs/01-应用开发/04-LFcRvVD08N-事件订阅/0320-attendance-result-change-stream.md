---
title: "考勤结果变更"
source_url: "https://open.dingtalk.com/document/development/attendance-result-change-stream"
namespace: "development"
slug: "attendance-result-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 考勤事件 > 考勤结果变更"
doc_id: "JyVhlUCJ3r"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/attendance-result-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 考勤事件 > 考勤结果变更
> Updated: 2022-01-19 19:29:22

# 考勤结果变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 考勤结果变更 |
| 英文名称 | attend\_bossCheck\_change |

## 功能描述

当钉钉考勤结果变更，eventType=attend\_bossCheck\_change时，钉钉通过事件订阅的方式将考勤结果变更内容推送给开发者。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

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
