---
title: "钉钉交易订购开启"
source_url: "https://open.dingtalk.com/document/development/dingtalk-transaction-ordering-on"
namespace: "development"
slug: "dingtalk-transaction-ordering-on"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 钉钉交易订购开启"
doc_id: "WL4bcuTWCB"
updated_at: "2025-08-28 19:47:23"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-transaction-ordering-on
> Path: 应用开发 / 事件订阅 / 应用市场 > 钉钉交易订购开启
> Updated: 2025-08-28 19:47:23

# 钉钉交易订购开启

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉交易订购开启 |
| 英文名称 | market\_service\_open |

## 功能描述

企业在应用市场购买商品对应的权益服务开通事件数据，目前仅续费变配服务开通时推送。

> 高优先级事件，SyncHTTP推送方式EventType为SYNC\_HTTP\_PUSH\_HIGH，RDS推送方式存放在open\_sync\_biz\_data表中。

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
- `data.suiteId`（long）：用户购买第三方企业应用的suiteId。
- `data.corpId`（string）：购买企业的corpId。
- `data.orderId`（string）：订单id。
- `data.itemCode`（string）：规格码。
- `data.subQuantity`（integer）：购买数量。
- `data.eventType`（string）：事件类型：  
  - subscription\_open：服务开通事件
- `data.openType`（integer）：服务开通类型：  
  - 3：续费变配开通
- `data.itemName`（string）：规格名称。
- `data.payFee`（integer）：实际支付价格（单位：分）。
- `data.serviceStopTime`（long）：订购服务结束时间（单位：毫秒）。
- `data.serviceStartTime`（long）：订购服务开始时间（单位：毫秒）。
- `data.suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `data.goodsCode`（string）：商品码。
- `data.goodsName`（string）：商品名称。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "market_service_open",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "suiteId": 123123,
    "corpId": "dingxxxxxxxxxxxx",
    "orderId": "312139204444444",
    "itemCode": "xxxxxxx",
    "subQuantity": 3,
    "eventType": "subscription_close",
    "openType": 3,
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

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.suiteId`（long）：用户购买第三方企业应用的suiteId。
- `biz_data.corpId`（string）：购买企业的corpId。
- `biz_data.orderId`（string）：订单id。
- `biz_data.itemCode`（string）：规格码。
- `biz_data.subQuantity`（integer）：购买数量。
- `biz_data.eventType`（string）：事件类型：  
  - subscription\_open：服务开通事件
- `biz_data.openType`（integer）：服务开通类型：  
  - 3：续费变配开通
- `biz_data.itemName`（string）：规格名称。
- `biz_data.payFee`（integer）：实际支付价格（单位：分）。
- `biz_data.serviceStopTime`（long）：订购服务结束时间（单位：毫秒）。
- `biz_data.serviceStartTime`（long）：订购服务开始时间（单位：毫秒）。
- `biz_data.suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `biz_data.goodsCode`（string）：商品码。
- `biz_data.goodsName`（string）：商品名称。

### **biz\_data数据示例(biz\_type=37)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 37,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "suiteId": 123123,
    "corpId": "dingxxxxxxxxxxxx",
    "syncAction": "market_service_open",
    "orderId": "312139204444444",
    "itemCode": "xxxxxxx",
    "subQuantity": 3,
    "eventType": "subscription_close",
    "openType": 3,
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
