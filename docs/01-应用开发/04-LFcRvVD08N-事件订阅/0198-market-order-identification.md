---
title: "市场订单标识"
source_url: "https://open.dingtalk.com/document/development/market-order-identification"
namespace: "development"
slug: "market-order-identification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 市场订单标识"
doc_id: "sZXZ9B3EP2"
updated_at: "2025-08-28 19:47:21"
---

> Source: https://open.dingtalk.com/document/development/market-order-identification
> Path: 应用开发 / 事件订阅 / 应用市场 > 市场订单标识
> Updated: 2025-08-28 19:47:21

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.orgProfile`（object）：组织profile信息。
- `data.orgProfile.isSuggestedAttention`（boolean，必填）：组织是否建议重点关注（算法标识）。
- `data.orderId`（string）：订单id。
- `data.corpId`（string）：下单组织corpId。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.orgProfile`（object）：组织profile信息。
- `biz_data.orgProfile.isSuggestedAttention`（boolean，必填）：组织是否建议重点关注（算法标识）。
- `biz_data.orderId`（string）：订单id。
- `biz_data.corpId`（string）：下单组织corpId。

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
