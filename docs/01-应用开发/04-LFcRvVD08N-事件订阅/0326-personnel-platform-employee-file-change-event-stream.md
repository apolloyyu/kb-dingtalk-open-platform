---
title: "人事平台员工档案变动事件"
source_url: "https://open.dingtalk.com/document/development/personnel-platform-employee-file-change-event-stream"
namespace: "development"
slug: "personnel-platform-employee-file-change-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 智能人事事件 > 人事平台员工档案变动事件"
doc_id: "V9SBaW4IOq"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/personnel-platform-employee-file-change-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 智能人事事件 > 人事平台员工档案变动事件
> Updated: 2022-01-19 19:29:22

# 人事平台员工档案变动事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事平台员工档案变动事件 |
| 英文名称 | hrm\_mdm\_user\_info\_change |

## 功能描述

eventType为hrm\_mdm\_user\_info\_change，表示人事平台员工档案变动事件数据。

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
  "eventType": "hrm_mdm_user_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "staffId": "xxx6129461xxxxxx"
  }
}
```
