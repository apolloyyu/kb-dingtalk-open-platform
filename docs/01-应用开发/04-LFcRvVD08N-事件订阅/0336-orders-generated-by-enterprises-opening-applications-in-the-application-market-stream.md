---
title: "企业在应用市场开通应用产生的订单"
source_url: "https://open.dingtalk.com/document/development/orders-generated-by-enterprises-opening-applications-in-the-application-market-stream"
namespace: "development"
slug: "orders-generated-by-enterprises-opening-applications-in-the-application-market-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 应用市场事件 > 企业在应用市场开通应用产生的订单"
doc_id: "RDP3YJiD2Z"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/orders-generated-by-enterprises-opening-applications-in-the-application-market-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 应用市场事件 > 企业在应用市场开通应用产生的订单
> Updated: 2022-01-19 19:29:22

# 企业在应用市场开通应用产生的订单

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业在应用市场开通应用产生的订单 |
| 英文名称 | market\_order |

## 功能描述

eventType为market\_order，表示企业在钉钉服务市场购买开通应用产生订单时，钉钉推送的市场订单数据。

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
  "eventType": "market_order",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "orderType": "RENEW",
    "distributorCorpName": "测试代理企业",
    "discountFee": 0,
    "solutionPackageName": "中小企业财务解决方案",
    "orderId": "312139204444444",
    "openId": "2343242412",
    "itemCode": "xxxxxxx",
    "orderLabel": 1,
    "saleModelType": "CYC_UPGRADE",
    "solutionPackageKey": "SOLUTION313-31231",
    "discount": "1",
    "maxOfPeople": 100,
    "autoChangeFreeItem": false,
    "purchaseType": 1,
    "distributorCorpId": "dingxxxxxxxxxxxxx",
    "originalArticleCode": "DT_GOODS_23311",
    "itemName": "测试规格",
    "buyUserId": "staff2313",
    "payFee": 1000,
    "serviceStopTime": 1524897069000,
    "articleType": "normal",
    "serviceStartTime": 168000312000,
    "appId": 299011,
    "outTradeNo": "30990011123",
    "suiteKey": "xxxxxxxxx",
    "orderCreatSource": "xxxx",
    "mainCorpId": "ding23093214311",
    "mainArticleName": "测试商品001",
    "goodsName": "测试商品",
    "minOfPeople": 0,
    "suiteId": 123453,
    "unionId": "union1265341625",
    "corpId": "dingxxxxxxxxxxxx",
    "mainArticleCode": "DT_GOODS_1233",
    "subQuantity": 1,
    "originalItemCode": "DT_GOODS_23311_123",
    "leadsFrom": "广场-搜索",
    "presentRelMainOrderId": 209130000311,
    "extendParam": {
      "name": "xxx"
    },
    "nominalPayFee": 1000,
    "isvOperationCode": "****",
    "goodsCode": "xxxxxxxxxxx",
    "paidtime": 1524897069000,
    "orderChannelCode": "all_star_isv_channel_code"
  }
}
```
