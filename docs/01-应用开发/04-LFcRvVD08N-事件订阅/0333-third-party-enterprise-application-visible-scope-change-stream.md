---
title: "第三方企业应用可见范围变更"
source_url: "https://open.dingtalk.com/document/development/third-party-enterprise-application-visible-scope-change-stream"
namespace: "development"
slug: "third-party-enterprise-application-visible-scope-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 第三方企业状态 > 第三方企业应用可见范围变更"
doc_id: "phIVNSzFYJ"
updated_at: "2025-10-16 15:06:47"
---

> Source: https://open.dingtalk.com/document/development/third-party-enterprise-application-visible-scope-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 第三方企业状态 > 第三方企业应用可见范围变更
> Updated: 2025-10-16 15:06:47

# 第三方企业应用可见范围变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 第三方企业应用可见范围变更 |
| 英文名称 | org\_micro\_app\_scope\_update |

## 功能描述

数据为第三方企业应用的最新状态，eventType为org\_micro\_app\_scope\_update，表示第三方企业应用可见范围变更。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `agentId`（long）：应用的agentId。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_micro_app_scope_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": 12345677
  }
}
```
