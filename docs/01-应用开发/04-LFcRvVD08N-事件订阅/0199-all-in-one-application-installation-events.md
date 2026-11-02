---
title: "一体化应用安装事件"
source_url: "https://open.dingtalk.com/document/development/all-in-one-application-installation-events"
namespace: "development"
slug: "all-in-one-application-installation-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 一体化应用安装事件"
doc_id: "lUPdnfbEXB"
updated_at: "2025-08-28 19:47:24"
---

> Source: https://open.dingtalk.com/document/development/all-in-one-application-installation-events
> Path: 应用开发 / 事件订阅 / 应用市场 > 一体化应用安装事件
> Updated: 2025-08-28 19:47:24

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.orderType`（string）：订单类型，取值： BUY：新购 RENEW：续费 UPGRADE：升级 RENEW\_UPGRADE：续费升配 RENEW\_DEGRADE：续费降配
- `data.distributorCorpName`（string）：分销商企业名称。
- `data.suiteId`（number）：用户购买第三方企业应用的suiteId。
- `data.discountFee`（number）：折扣减免费用（单位：分），现值为0。
- `data.unionId`（string）：下单人unionId。
- `data.corpId`（string）：购买企业的corpId。
- `data.orderId`（number）：订单ID。
- `data.syncAction`（string）：该订单对应的用户操作。 当syncAction为market\_order时，表示市场订单支付。
- `data.itemCode`（string）：规格码。
- `data.subQuantity`（number）：购买数量。
- `data.distributorCorpId`（string）：分销商企业corpId。
- `data.itemName`（string）：规格名称。
- `data.payFee`（number）：实际支付价格（单位：分）。
- `data.serviceStopTime`（number）：服务结束时间（单位：毫秒）。
- `data.serviceStartTime`（number）：服务开始时间（单位：毫秒）。
- `data.suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `data.goodsCode`（string）：商品码。
- `data.goodsName`（string）：商品名称。
- `data.paidtime`（number）：支付时间（单位：毫秒）。

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

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.orderType`（string）：订单类型，取值： BUY：新购 RENEW：续费 UPGRADE：升级 RENEW\_UPGRADE：续费升配 RENEW\_DEGRADE：续费降配
- `biz_data.distributorCorpName`（string）：分销商企业名称。
- `biz_data.suiteId`（number）：用户购买第三方企业应用的suiteId。
- `biz_data.discountFee`（number）：折扣减免费用（单位：分），现值为0。
- `biz_data.unionId`（string）：下单人unionId。
- `biz_data.corpId`（string）：购买企业的corpId。
- `biz_data.orderId`（number）：订单ID。
- `biz_data.syncAction`（string）：该订单对应的用户操作。 当syncAction为market\_order时，表示市场订单支付。
- `biz_data.itemCode`（string）：规格码。
- `biz_data.subQuantity`（number）：购买数量。
- `biz_data.distributorCorpId`（string）：分销商企业corpId。
- `biz_data.itemName`（string）：规格名称。
- `biz_data.payFee`（number）：实际支付价格（单位：分）。
- `biz_data.serviceStopTime`（number）：服务结束时间（单位：毫秒）。
- `biz_data.serviceStartTime`（number）：服务开始时间（单位：毫秒）。
- `biz_data.suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `biz_data.goodsCode`（string）：商品码。
- `biz_data.goodsName`（string）：商品名称。
- `biz_data.paidtime`（number）：支付时间（单位：毫秒）。

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
