---
title: "一体化应用安装事件"
source_url: "https://open.dingtalk.com/document/development/all-in-one-application-installation-events"
namespace: "development"
slug: "all-in-one-application-installation-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 一体化应用安装事件"
doc_id: "lUPdnfbEXB"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/all-in-one-application-installation-events
> Path: 应用开发 / 事件订阅 / 应用市场 > 一体化应用安装事件
> Updated: 2022-01-19 19:29:22

# 一体化应用安装事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 一体化应用安装事件 |
| 英文名称 | integration\_app\_install\_event |

## 功能描述

一体化应用安装事件，推送时机：一方商品订单支付后，开通关联的三方应用，并广播该事件给三方应用。

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
  "eventType": "integration_app_install_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "orderType": "\"BUY\"",
    "distributorCorpName": "\"测试组织\"",
    "suiteId": "26976002",
    "unionId": "uVp2soqtUsAHlW9cPkdziPwiEiE",
    "discountFee": "39899",
    "corpId": "ding3f3de3722f372cfa35c2f4657eb6378f",
    "orderId": "222997942580853",
    "syncAction": "integration_app_install_event",
    "itemCode": "DT_GOODS_881680840698056_2290002",
    "subQuantity": "1",
    "distributorCorpId": "ding9f50b15bccd16741",
    "itemName": "\"1000次\"",
    "payFee": "1.0",
    "serviceStopTime": "1713542400000",
    "serviceStartTime": "1681889478000",
    "suiteKey": "suitek23ab8wcw7jpzti8",
    "goodsCode": "DT_GOODS_881680840698056",
    "paidtime": "1681889479724",
    "goodsName": "发票流量包"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=206)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 206,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "orderType": "\"BUY\"",
    "distributorCorpName": "\"测试组织\"",
    "suiteId": "26976002",
    "unionId": "uVp2soqtUsAHlW9cPkdziPwiEiE",
    "discountFee": "39899",
    "corpId": "ding3f3de3722f372cfa35c2f4657eb6378f",
    "syncAction": "integration_app_install_event",
    "orderId": "222997942580853",
    "itemCode": "DT_GOODS_881680840698056_2290002",
    "subQuantity": "1",
    "distributorCorpId": "ding9f50b15bccd16741",
    "itemName": "\"1000次\"",
    "payFee": "1.0",
    "serviceStopTime": "1713542400000",
    "serviceStartTime": "1681889478000",
    "suiteKey": "suitek23ab8wcw7jpzti8",
    "goodsCode": "DT_GOODS_881680840698056",
    "paidtime": "1681889479724",
    "goodsName": "发票流量包"
  }
}
```
