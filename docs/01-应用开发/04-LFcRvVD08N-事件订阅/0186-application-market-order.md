---
title: "应用市场下单"
source_url: "https://open.dingtalk.com/document/development/application-market-order"
namespace: "development"
slug: "application-market-order"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 应用市场下单"
doc_id: "rjnsKkqJLK"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/application-market-order
> Path: 应用开发 / 事件订阅 / 应用市场 > 应用市场下单
> Updated: 2022-01-19 19:29:22

# 应用市场下单

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 应用市场下单 |
| 英文名称 | market\_order |

## 功能描述

数据为企业在钉钉服务市场购买开通应用产生订单时刻，推送的订单信息事件内容。

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
    "discount": 1.0,
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

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=17)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 17,
  "biz_data": {
    "orderType": "RENEW",
    "distributorCorpName": "测试代理企业",
    "discountFee": 0,
    "solutionPackageName": "中小企业财务解决方案",
    "syncAction": "market_order",
    "orderId": "312139204444444",
    "openId": "2343242412",
    "itemCode": "xxxxxxx",
    "orderLabel": 1,
    "saleModelType": "CYC_UPGRADE",
    "solutionPackageKey": "SOLUTION313-31231",
    "discount": 1.0,
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
    "eventId": "c7c7120f2c07419**ebdba0318c8",
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
