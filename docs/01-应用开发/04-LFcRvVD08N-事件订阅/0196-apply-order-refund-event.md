---
title: "应用订单退款事件"
source_url: "https://open.dingtalk.com/document/development/apply-order-refund-event"
namespace: "development"
slug: "apply-order-refund-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 应用订单退款事件"
doc_id: "9ZRR32Ixn4"
updated_at: "2025-08-28 19:47:22"
---

> Source: https://open.dingtalk.com/document/development/apply-order-refund-event
> Path: 应用开发 / 事件订阅 / 应用市场 > 应用订单退款事件
> Updated: 2025-08-28 19:47:22

# 应用订单退款事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 应用订单退款事件 |
| 英文名称 | market\_order\_refund\_event |

## 功能描述

该文档为应用商品订单退款事件字段说明数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.refundFee`（integer）：退款金额。
- `data.corpId`（string）：企业corpId。
- `data.orderId`（long）：退款订单的orderId。
- `data.instanceEndTime`（long）：退款操作时间戳。

### **事件体示例**

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

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.refundFee`（integer）：退款金额。
- `biz_data.corpId`（string）：企业corpId。
- `biz_data.orderId`（long）：退款订单的orderId。
- `biz_data.instanceEndTime`（long）：退款操作时间戳。

### **biz\_data数据示例(biz\_type=212)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 212,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "refundFee": 10000,
    "corpId": "ding57935b18bfd13e9735cxxxxxxxxxx",
    "syncAction": "market_order_refund_event",
    "orderId": 1123445,
    "instanceEndTime": 16844000000
  }
}
```
