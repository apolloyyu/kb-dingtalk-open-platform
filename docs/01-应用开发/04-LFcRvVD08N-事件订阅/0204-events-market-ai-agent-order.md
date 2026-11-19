---
title: "市场AI助理下单"
source_url: "https://open.dingtalk.com/document/development/events-market-ai-agent-order"
namespace: "development"
slug: "events-market-ai-agent-order"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 市场AI助理下单"
doc_id: "XSXQKAylnp"
updated_at: "2026-03-02 10:00:27"
---

> Source: https://open.dingtalk.com/document/development/events-market-ai-agent-order
> Path: 应用开发 / 事件订阅 / 应用市场 > 市场AI助理下单
> Updated: 2026-03-02 10:00:27

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.orderType`（string）：订单类型，取值： BUY：新购 RENEW：续费 UPGRADE：升级 RENEW\_UPGRADE：续费升配 RENEW\_DEGRADE：续费降配
- `data.discountFee`（long）：折扣减免费用（单位：分）
- `data.orderId`（string）：订单ID
- `data.itemCode`（string）：商品规格编码
- `data.saleModelType`（string）：销售模式类型
- `data.discount`（double）：折扣
- `data.subQuantity`（long）：购买数量。
- `data.paidTime`（long）：支付时间（单位：毫秒）。
- `data.maxOfPeople`（long）：规格支持最大使用人数。
- `data.presentRelMainOrderId`（string）：赠品关联主订单ID
- `data.itemName`（string）：商品规格名称
- `data.payFee`（long）：实际支付价格（单位：分）。
- `data.buyCorpName`（string）：购买企业的名称
- `data.extendParam`（object）：扩展参数
- `data.serviceStopTime`（long）：服务结束时间（单位：毫秒）
- `data.serviceStartTime`（long）：服务开始时间（单位：毫秒）
- `data.appId`（string）：应用ID
- `data.goodsCode`（string）：商品编码
- `data.orderCreatSource`（string）：订单来源： 默认订单来自应用中心。 若值为TIANYUAN，表示来自天元系统平台。
- `data.activityType`（string）：活动类型
- `data.goodsName`（string）：商品名称
- `data.minOfPeople`（long）：规格支持最小使用人数。
- `data.purchaserType`（integer）：购买者类型(1:企业购买行为, 2:个人购买行为)
- `data.purchaserId`（string）：购买者ID(企业购买值为corpId；个人购买值为unionId)

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `orderType`（string，必填）：订单类型，取值： BUY：新购 RENEW：续费 UPGRADE：升级 RENEW\_UPGRADE：续费升配 RENEW\_DEGRADE：续费降配
- `discountFee`（long）：折扣减免费用（单位：分）
- `orderId`（string，必填）：订单ID
- `itemCode`（string，必填）：商品规格编码
- `saleModelType`（string，必填）：销售模式类型
- `discount`（double）：折扣
- `subQuantity`（long）：购买数量。
- `paidTime`（long，必填）：支付时间（单位：毫秒）。
- `maxOfPeople`（long）：规格支持最大使用人数。
- `presentRelMainOrderId`（string，必填）：赠品关联主订单ID
- `itemName`（string，必填）：商品规格名称
- `payFee`（long，必填）：实际支付价格（单位：分）。
- `buyCorpName`（string，必填）：购买企业的名称
- `extendParam`（object，必填）：扩展参数
- `serviceStopTime`（long，必填）：服务结束时间（单位：毫秒）
- `serviceStartTime`（long，必填）：服务开始时间（单位：毫秒）
- `appId`（string，必填）：应用ID
- `goodsCode`（string，必填）：商品编码
- `orderCreatSource`（string，必填）：订单来源： 默认订单来自应用中心。 若值为TIANYUAN，表示来自天元系统平台。
- `activityType`（string）：活动类型
- `goodsName`（string，必填）：商品名称
- `minOfPeople`（long）：规格支持最小使用人数。
- `purchaserType`（integer，必填）：购买者类型(1:企业购买行为, 2:个人购买行为)
- `purchaserId`（string，必填）：购买者ID(企业购买值为corpId；个人购买值为unionId)

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
