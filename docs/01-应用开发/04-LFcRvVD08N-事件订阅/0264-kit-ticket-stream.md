---
title: "套件票据"
source_url: "https://open.dingtalk.com/document/development/kit-ticket-stream"
namespace: "development"
slug: "kit-ticket-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 授权事件 > 套件票据"
doc_id: "HOXW4CTPzV"
updated_at: "2025-10-16 14:32:02"
---

> Source: https://open.dingtalk.com/document/development/kit-ticket-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 授权事件 > 套件票据
> Updated: 2025-10-16 14:32:02

# 套件票据

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 套件票据 |
| 英文名称 | suite\_ticket |

## 功能描述

数据为第三方企业应用票据最新suiteTicket。

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

- `suiteTicket`（string）：suiteTicket值。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "suite_ticket",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "suiteTicket": "QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
  }
}
```
