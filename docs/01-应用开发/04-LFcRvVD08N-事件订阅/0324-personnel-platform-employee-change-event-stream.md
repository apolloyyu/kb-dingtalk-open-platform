---
title: "人事平台员工异动事件v2"
source_url: "https://open.dingtalk.com/document/development/personnel-platform-employee-change-event-stream"
namespace: "development"
slug: "personnel-platform-employee-change-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 智能人事事件 > 人事平台员工异动事件v2"
doc_id: "jrfu4pdKi5"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/personnel-platform-employee-change-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 智能人事事件 > 人事平台员工异动事件v2
> Updated: 2022-01-19 19:29:22

# 人事平台员工异动事件v2

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事平台员工异动事件v2 |
| 英文名称 | hrm\_mdm\_user\_change |
| 事件BizType | 137 |

## 功能描述

当biz\_type=137时，数据为人事平台员工异动V2相关数据。该数据为人事平台员工异动V2相关的数据变更时推送。

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
  "eventType": "hrm_mdm_user_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "changeType": 4,
    "staffId": "01301xxxx140"
  }
}
```
