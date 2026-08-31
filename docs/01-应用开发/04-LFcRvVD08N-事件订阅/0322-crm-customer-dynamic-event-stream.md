---
title: "CRM客户动态"
source_url: "https://open.dingtalk.com/document/development/crm-customer-dynamic-event-stream"
namespace: "development"
slug: "crm-customer-dynamic-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 客户管理事件 > CRM客户动态"
doc_id: "y1Xkd8lErW"
updated_at: "2025-10-16 14:32:32"
---

> Source: https://open.dingtalk.com/document/development/crm-customer-dynamic-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 客户管理事件 > CRM客户动态
> Updated: 2025-10-16 14:32:32

# CRM客户动态

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM客户动态 |
| 英文名称 | crm\_customer\_track |

## 功能描述

CRM客户动态相关信息发生变更时，钉钉通过事件订阅的方式将CRM客户动态相关变更内容推送给开发者。eventType为crm\_customer\_track，表示CRM客户动态事件数据。

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

- `tracks`（array）：客户动态相关的数据变更列表。
- `tracks[].creator`（string）：动态创建者的userid。
- `tracks[].corpId`（string）：客户所在组织的corpId。
- `tracks[].customerId`（string）：客户ID。
- `tracks[].subType`（integer）：客户动态子类型。
- `tracks[].gmtCreate`（long）：动态创建时间。
- `tracks[].type`（integer）：客户动态类型。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "crm_customer_track",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "tracks": [
      {
        "creator": "manager1234",
        "corpId": "ding9axxx",
        "customerId": "84c75568-xxx-xxx",
        "subType": 0,
        "gmtCreate": 1630474492814,
        "type": 107
      }
    ]
  }
}
```
