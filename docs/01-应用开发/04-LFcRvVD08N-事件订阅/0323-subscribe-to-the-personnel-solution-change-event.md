---
title: "人事解决方案变更事件"
source_url: "https://open.dingtalk.com/document/development/subscribe-to-the-personnel-solution-change-event"
namespace: "development"
slug: "subscribe-to-the-personnel-solution-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 智能人事事件 > 人事解决方案变更事件"
doc_id: "TfLyyuV2zg"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/subscribe-to-the-personnel-solution-change-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 智能人事事件 > 人事解决方案变更事件
> Updated: 2022-01-19 19:29:22

# 人事解决方案变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事解决方案变更事件 |
| 英文名称 | hrm\_solution\_manage |
| 事件BizType | 175 |

## 功能描述

当biz\_type=175时，数据为人事解决方案变更事件的相关数据。该数据为人事解决方案变更事件相关的数据推送。

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
  "eventType": "hrm_solution_manage",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "ding57935b18bfd13e9735cxxxxxxxxxx",
    "solutionType": "onboarding",
    "staffId2SolutionInstanceIdMap": "{\"16846746xxxx5028\":\"875f797531ef49xxxx296feaa\"}",
    "solutionStatus": "start"
  }
}
```
