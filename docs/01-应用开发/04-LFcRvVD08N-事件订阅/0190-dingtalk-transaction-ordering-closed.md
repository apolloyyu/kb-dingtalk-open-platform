---
title: "钉钉交易订购关闭"
source_url: "https://open.dingtalk.com/document/development/dingtalk-transaction-ordering-closed"
namespace: "development"
slug: "dingtalk-transaction-ordering-closed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 钉钉交易订购关闭"
doc_id: "sjQzeMjfnh"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-transaction-ordering-closed
> Path: 应用开发 / 事件订阅 / 应用市场 > 钉钉交易订购关闭
> Updated: 2022-01-19 19:29:22

# 钉钉交易订购关闭

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉交易订购关闭 |
| 英文名称 | market\_service\_close |

## 功能描述

表示服务关闭事件数据，目前仅退款导致服务关闭时推送。

> 高优先级事件，SyncHTTP推送方式EventType为SYNC\_HTTP\_PUSH\_HIGH，RDS推送方式存放在open\_sync\_biz\_data表中。

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

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data中。

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
    "syncAction": "market_service_close",
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
