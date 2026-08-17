---
title: "企业在应用市场购买商品对应的权益服务关闭"
source_url: "https://open.dingtalk.com/document/development/equity-services-close-etc-corresponding-to-goods-purchased-by-the-stream"
namespace: "development"
slug: "equity-services-close-etc-corresponding-to-goods-purchased-by-the-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 应用市场事件 > 企业在应用市场购买商品对应的权益服务关闭"
doc_id: "masTeXGZO2"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/equity-services-close-etc-corresponding-to-goods-purchased-by-the-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 应用市场事件 > 企业在应用市场购买商品对应的权益服务关闭
> Updated: 2022-01-19 19:29:22

# 企业在应用市场购买商品对应的权益服务关闭

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业在应用市场购买商品对应的权益服务关闭 |
| 英文名称 | market\_service\_close |

## 功能描述

eventType为subscription\_close，表示服务关闭事件数据，目前仅退款导致服务关闭时推送。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "market_service_close",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "suiteId": 123123,
    "corpId": "dingxxxxxxxxxxxx",
    "orderId": "312139204444444",
    "itemCode": "xxxxxxx",
    "subQuantity": 3,
    "eventType": "subscription_close",
    "closeType": 3,
    "itemName": "xxxxx",
    "payFee": 1000,
    "serviceStopTime": 168000031311,
    "serviceStartTime": 167000031311,
    "suiteKey": "xxxxx",
    "goodsCode": "xxxxxxx",
    "goodsName": "测试规格"
  }
}
```
