---
title: "市场订单标识"
source_url: "https://open.dingtalk.com/document/development/market-order-identification"
namespace: "development"
slug: "market-order-identification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 市场订单标识"
doc_id: "sZXZ9B3EP2"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/market-order-identification
> Path: 应用开发 / 事件订阅 / 应用市场 > 市场订单标识
> Updated: 2022-01-19 19:29:22

# 市场订单标识

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 市场订单标识 |
| 英文名称 | market\_order\_tag |

## 功能描述

市场订单标识事件。

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
  "eventType": "market_order_tag",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "dingxxxd12445",
    "orgProfile": {
      "isSuggestedAttention": true
    },
    "orderId": "2345ddd"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=253)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 253,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "dingxxxd12445",
    "orgProfile": {
      "isSuggestedAttention": true
    },
    "syncAction": "market_order_tag",
    "orderId": "2345ddd"
  }
}
```
