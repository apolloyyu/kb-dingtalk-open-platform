---
title: "市场AI助理下单"
source_url: "https://open.dingtalk.com/document/development/events-market-ai-agent-order"
namespace: "development"
slug: "events-market-ai-agent-order"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 市场AI助理下单"
doc_id: "XSXQKAylnp"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-market-ai-agent-order
> Path: 应用开发 / 事件订阅 / 应用市场 > 市场AI助理下单
> Updated: 2022-01-19 19:29:22

# 市场AI助理下单

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 市场AI助理下单 |
| 英文名称 | market\_ai\_agent\_order |

## 功能描述

数据为企业在钉钉市场购买开通AI助理产生订单时刻，推送的订单信息事件内容。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "market_ai_agent_order",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "orderType": "RENEW",
    "discountFee": 0,
    "orderId": "1234567",
    "itemCode": "xxxxxxx",
    "saleModelType": "CYC_UPGRADE",
    "discount": 1.0,
    "subQuantity": 1,
    "paidTime": 1524897069000,
    "maxOfPeople": 100,
    "presentRelMainOrderId": "209130000311",
    "itemName": "测试规格",
    "payFee": 1000,
    "purchaserId": "dingxxxxxxxxxxxxx",
    "buyCorpName": "测试组织",
    "extendParam": {},
    "serviceStopTime": 1524897069000,
    "serviceStartTime": 1524897069000,
    "appId": "79445cef-460d-xxxxxxx-b192-c663af249e82",
    "goodsCode": "DT_GOODS_23311",
    "orderCreatSource": "xxxx",
    "goodsName": "测试商品001",
    "minOfPeople": 1,
    "purchaserType": 1
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "market_ai_agent_order",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "orderType": "RENEW",
  "discountFee": 0,
  "orderId": "1234567",
  "itemCode": "xxxxxxx",
  "saleModelType": "CYC_UPGRADE",
  "discount": 1.0,
  "subQuantity": 1,
  "paidTime": 1524897069000,
  "maxOfPeople": 100,
  "presentRelMainOrderId": "209130000311",
  "itemName": "测试规格",
  "payFee": 1000,
  "purchaserId": "dingxxxxxxxxxxxxx",
  "buyCorpName": "测试组织",
  "extendParam": {},
  "serviceStopTime": 1524897069000,
  "serviceStartTime": 1524897069000,
  "appId": "79445cef-460d-xxxxxxx-b192-c663af249e82",
  "goodsCode": "DT_GOODS_23311",
  "orderCreatSource": "xxxx",
  "goodsName": "测试商品001",
  "minOfPeople": 1,
  "purchaserType": 1
}
```
