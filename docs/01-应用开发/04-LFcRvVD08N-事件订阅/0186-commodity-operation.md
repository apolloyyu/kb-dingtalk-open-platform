---
title: "商品操作"
source_url: "https://open.dingtalk.com/document/development/commodity-operation"
namespace: "development"
slug: "commodity-operation"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 商品操作"
doc_id: "AD5xmOmX3y"
updated_at: "2025-08-28 19:47:20"
---

> Source: https://open.dingtalk.com/document/development/commodity-operation
> Path: 应用开发 / 事件订阅 / 应用市场 > 商品操作
> Updated: 2025-08-28 19:47:20

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.suiteId`（long）：第三方企业应用的ID。
- `data.itemType`（string）：开通的规格类型：  
  - charge\_goods\_free\_item：付费商品的免费规格  
  - charge\_item: 付费规格  
  >当开通付费商品的免费规格/付费规格时会返回该字段。
- `data.corpId`（string）：开通第三方企业应用的企业corpid。
- `data.endDate`（string）：结束时间。
- `data.userid`（string）：下单人userid。
- `data.fromDate`（string）：开始时间。
- `data.buyerUnionId`（string）：系统生成，固定值不会改变，可用来识别下单人。
- `data.appId`（long）：应用ID。
- `data.tryoutType`（string）：开通类型：  
  - personal\_tryout：个人开通  
  - enterprise\_tryout：企业开通（管理员）
- `data.goodsCode`（string）：商品码。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.suiteId`（long）：第三方企业应用的ID。
- `biz_data.itemType`（string）：开通的规格类型：  
  - charge\_goods\_free\_item：付费商品的免费规格  
  - charge\_item: 付费规格  
  >当开通付费商品的免费规格/付费规格时会返回该字段。
- `biz_data.corpId`（string）：开通第三方企业应用的企业corpid。
- `biz_data.endDate`（string）：结束时间。
- `biz_data.userid`（string）：下单人userid。
- `biz_data.fromDate`（string）：开始时间。
- `biz_data.buyerUnionId`（string）：系统生成，固定值不会改变，可用来识别下单人。
- `biz_data.appId`（long）：应用ID。
- `biz_data.tryoutType`（string）：开通类型：  
  - personal\_tryout：个人开通  
  - enterprise\_tryout：企业开通（管理员）
- `biz_data.goodsCode`（string）：商品码。

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
