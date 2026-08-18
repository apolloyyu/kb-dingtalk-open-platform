---
title: "应用订单退款事件"
source_url: "https://open.dingtalk.com/document/development/apply-order-refund-event"
namespace: "development"
slug: "apply-order-refund-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 应用订单退款事件"
doc_id: "9ZRR32Ixn4"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/apply-order-refund-event
> Path: 应用开发 / 事件订阅 / 应用市场 > 应用订单退款事件
> Updated: 2022-01-19 19:29:22

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
