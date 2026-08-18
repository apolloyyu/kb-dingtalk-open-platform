---
title: "商品操作"
source_url: "https://open.dingtalk.com/document/development/commodity-operation"
namespace: "development"
slug: "commodity-operation"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 商品操作"
doc_id: "AD5xmOmX3y"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/commodity-operation
> Path: 应用开发 / 事件订阅 / 应用市场 > 商品操作
> Updated: 2022-01-19 19:29:22

# 商品操作

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 商品操作 |
| 英文名称 | goods\_tryout |

## 功能描述

应用商品新增个人开通后，增加了应用的触达率，为了方便ISV对客户进行后续跟踪和推广，组织/个人在应用开通后，钉钉后台新增了应用开通记录的回调信息。
目前应用开通的回调信息有两种：

1、应用开通的订单信息

侧重于订单信息回调。

2、应用开通的记录信息

应用开通记录回调信息中不一定会有订单。

> 当同组织的两个用户对同一商品的开通时间完全重合，或者同组织下已经开通该商品的有效期完全包含新开通商品有效期的时候，不会产生订单。

该事件表示商品操作事件，组织或个人应用开通时推送的应用开通记录的回调信息。

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
  "eventType": "goods_tryout",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "fromDate": "2020-12-19 10:59:25",
    "suiteId": 698002,
    "itemType": "charge_goods_free_item",
    "buyerUnionId": "mLyKVGiiwEXQ5mT0Nwxxxx",
    "corpId": "dingd678857e4250521135c2f465xxxx",
    "endDate": "2020-12-19 10:59:25",
    "appId": 1948,
    "tryoutType": "enterprise_tryout",
    "goodsCode": "FW_GOODS-100030xxxx",
    "userid": "12344"
  }
}
```

SyncHTTP/RDS推送

高优先级事件，为RDS推送方式时，数据插入表open\_sync\_biz\_data中。SyncHTTP推送方式时EventType为SYNC\_HTTP\_PUSH\_HIGH。

### **biz\_data数据示例(biz\_type=63)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 63,
  "biz_data": {
    "fromDate": "2020-12-19 10:59:25",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "suiteId": 698002,
    "itemType": "charge_goods_free_item",
    "buyerUnionId": "mLyKVGiiwEXQ5mT0Nwxxxx",
    "corpId": "dingd678857e4250521135c2f465xxxx",
    "syncAction": "goods_tryout",
    "endDate": "2020-12-19 10:59:25",
    "appId": 1948,
    "tryoutType": "enterprise_tryout",
    "goodsCode": "FW_GOODS-100030xxxx",
    "userid": "12344"
  }
}
```
