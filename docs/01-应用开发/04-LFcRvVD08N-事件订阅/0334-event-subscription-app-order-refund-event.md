---
title: "应用订单退款事件"
source_url: "https://open.dingtalk.com/document/development/event-subscription-app-order-refund-event"
namespace: "development"
slug: "event-subscription-app-order-refund-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 应用市场事件 > 应用订单退款事件"
doc_id: "W7lpVcjI3d"
updated_at: "2025-12-08 15:18:15"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-app-order-refund-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 应用市场事件 > 应用订单退款事件
> Updated: 2025-12-08 15:18:15

# 应用订单退款事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 应用订单退款事件 |
| 英文名称 | market\_order\_refund\_event |

## 功能描述

eventType为market\_order\_refund\_event，表示应用商品订单退款事件数据。

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

- `refundFee`（integer）：退款金额。
- `corpId`（string）：企业corpId。
- `orderId`（long）：退款订单的orderId。
- `instanceEndTime`（long）：退款操作时间戳。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "market_order_refund_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "refundFee": 10000,
    "corpId": "ding57935b18bfd13e9735cxxxxxxxxxx",
    "orderId": 1123445,
    "instanceEndTime": 16844000000
  }
}
```
