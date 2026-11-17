---
title: "支付状态同步"
source_url: "https://open.dingtalk.com/document/development/payment-status-synchronization"
namespace: "development"
slug: "payment-status-synchronization"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 支付状态同步"
doc_id: "p2dgE9jpz6"
updated_at: "2025-08-28 19:47:43"
---

> Source: https://open.dingtalk.com/document/development/payment-status-synchronization
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 支付状态同步
> Updated: 2025-08-28 19:47:43

# 支付状态同步

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 支付状态同步 |
| 英文名称 | edu\_trade\_pay\_status\_sync |

## 功能描述

为了方便开发者感知用户状态变化，统一支付平台提供了事件推送能力，当前仅支持支付状态同步事件，即当用户订单的支付状态发生变化时，钉钉会通过事件订阅的方式将用户订单的支付状态的变更内容推送给开发者。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
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
- `data.subject`（string）：订单标题。
- `data.refundTime`（long）：退款时间，时间戳，单位毫秒。说明 仅在退款行为发生后存在。 其他情况为空，不显示该字段。
- `data.eventTime`（long）：事件发生的时间。
- `data.corpId`（string）：企业corpId。
- `data.bizId`（string）：无业务意义，幂等。
- `data.orderNo`（string）：平台订单号
- `data.tradeNo`（string）：交易订单号。
- `data.merchantOrderNo`（string）：商户自有系统的订单号。
- `data.userId`（integer）：用户唯一id。
- `data.payType`（string）：买家支付渠道类型，取值： 1：支付宝
- `data.payLogonId`（integer）：买家支付登陆id。
- `data.orderType`（string）：订单类型，取值： 1：普通订单 2：聚合支付订单
- `data.merchantMergeOrderNo`（string）：商户聚合支付订单号。
- `data.labelAmount`（long）：订单标签金额，单位分。
- `data.actualAmount`（long）：订单实际金额，单位分。
- `data.refundAmount`（long）：订单退款金额，单位分。
- `data.alipayAppId`（string）：支付宝应用id。
- `data.feature`（string）：扩展字段
- `data.merchantId`（integer）：卖家商户ID。
- `data.payStatus`（integer）：支付状态交易： 2：支付成功 4：交易关闭 8：交易结束
- `data.refundStatus`（integer）：订单退款状态。 1：退款成功
- `data.createTime`（long）：订单创建时间。
- `data.payTime`（long）：支付时间，时间戳，单位毫秒。说明 支付订单后存在。 未支付情况为空，不显示该字段。
- `data.closeTime`（long）：关单时间，时间戳，单位毫秒。说明 关单或交易结束后存在。 其他情况为空，不显示该字段。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_trade_pay_status_sync",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "orderType": "1",
    "orderNo": "xx20230314xxxxxxxxxxxx",
    "corpId": "ding48591xx",
    "tradeNo": "2022080311111",
    "merchantMergeOrderNo": "M20000100",
    "payTime": 1675737492000,
    "subject": "教育产品",
    "refundTime": 1675737493000,
    "actualAmount": 100,
    "refundStatus": 1,
    "alipayAppId": "123400",
    "userId": 1000,
    "merchantOrderNo": "1678xxxx000",
    "payType": "1",
    "feature": "{\"key\":\"1234\"}",
    "labelAmount": 100,
    "createTime": 1675737492000,
    "merchantId": 2088107,
    "payLogonId": 138,
    "eventTime": 1675732000,
    "closeTime": 1675737493000,
    "bizId": "bizxxxxx",
    "payStatus": 2,
    "refundAmount": 100
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `eventId`（String）：事件的唯一Id。
- `subject`（string，必填）：订单标题。
- `refundTime`（long，必填）：退款时间，时间戳，单位毫秒。说明 仅在退款行为发生后存在。 其他情况为空，不显示该字段。
- `EventTime`（long，必填）：事件发生的时间。
- `CorpId`（string，必填）：企业corpId。
- `BizId`（string，必填）：无业务意义，幂等。
- `orderNo`（string，必填）：平台订单号
- `tradeNo`（string，必填）：交易订单号。
- `merchantOrderNo`（string，必填）：商户自有系统的订单号。
- `userId`（integer，必填）：用户唯一id。
- `payType`（string，必填）：买家支付渠道类型，取值： 1：支付宝
- `payLogonId`（integer，必填）：买家支付登陆id。
- `orderType`（string，必填）：订单类型，取值： 1：普通订单 2：聚合支付订单
- `merchantMergeOrderNo`（string，必填）：商户聚合支付订单号。
- `labelAmount`（long，必填）：订单标签金额，单位分。
- `actualAmount`（long，必填）：订单实际金额，单位分。
- `refundAmount`（long，必填）：订单退款金额，单位分。
- `alipayAppId`（string，必填）：支付宝应用id。
- `feature`（string，必填）：扩展字段
- `merchantId`（integer，必填）：卖家商户ID。
- `payStatus`（integer，必填）：支付状态交易： 2：支付成功 4：交易关闭 8：交易结束
- `refundStatus`（integer，必填）：订单退款状态。 1：退款成功
- `createTime`（long，必填）：订单创建时间。
- `payTime`（long，必填）：支付时间，时间戳，单位毫秒。说明 支付订单后存在。 未支付情况为空，不显示该字段。
- `closeTime`（long，必填）：关单时间，时间戳，单位毫秒。说明 关单或交易结束后存在。 其他情况为空，不显示该字段。

### **事件体示例**

```
{
  "EventType": "edu_trade_pay_status_sync",
  "EventTime": 1675732000,
  "CorpId": "ding48591xx",
  "BizId": "bizxxxxx",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "orderType": "1",
  "orderNo": "xx20230314xxxxxxxxxxxx",
  "tradeNo": "2022080311111",
  "merchantMergeOrderNo": "M20000100",
  "payTime": 1675737492000,
  "subject": "教育产品",
  "refundTime": 1675737493000,
  "actualAmount": 100,
  "refundStatus": 1,
  "alipayAppId": "123400",
  "userId": 1000,
  "merchantOrderNo": "1678xxxx000",
  "payType": "1",
  "feature": "{\"key\":\"1234\"}",
  "labelAmount": 100,
  "createTime": 1675737492000,
  "merchantId": 2088107,
  "payLogonId": 138,
  "closeTime": 1675737493000,
  "payStatus": 2,
  "refundAmount": 100
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.subject`（string）：订单标题。
- `biz_data.refundTime`（long）：退款时间，时间戳，单位毫秒。说明 仅在退款行为发生后存在。 其他情况为空，不显示该字段。
- `biz_data.EventTime`（long）：事件发生的时间。
- `biz_data.CorpId`（string）：企业corpId。
- `biz_data.BizId`（string）：无业务意义，幂等。
- `biz_data.orderNo`（string）：平台订单号
- `biz_data.tradeNo`（string）：交易订单号。
- `biz_data.merchantOrderNo`（string）：商户自有系统的订单号。
- `biz_data.userId`（integer）：用户唯一id。
- `biz_data.payType`（string）：买家支付渠道类型，取值： 1：支付宝
- `biz_data.payLogonId`（integer）：买家支付登陆id。
- `biz_data.orderType`（string）：订单类型，取值： 1：普通订单 2：聚合支付订单
- `biz_data.merchantMergeOrderNo`（string）：商户聚合支付订单号。
- `biz_data.labelAmount`（long）：订单标签金额，单位分。
- `biz_data.actualAmount`（long）：订单实际金额，单位分。
- `biz_data.refundAmount`（long）：订单退款金额，单位分。
- `biz_data.alipayAppId`（string）：支付宝应用id。
- `biz_data.feature`（string）：扩展字段
- `biz_data.merchantId`（integer）：卖家商户ID。
- `biz_data.payStatus`（integer）：支付状态交易： 2：支付成功 4：交易关闭 8：交易结束
- `biz_data.refundStatus`（integer）：订单退款状态。 1：退款成功
- `biz_data.createTime`（long）：订单创建时间。
- `biz_data.payTime`（long）：支付时间，时间戳，单位毫秒。说明 支付订单后存在。 未支付情况为空，不显示该字段。
- `biz_data.closeTime`（long）：关单时间，时间戳，单位毫秒。说明 关单或交易结束后存在。 其他情况为空，不显示该字段。

### **biz\_data数据示例(biz\_type=251)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 251,
  "biz_data": {
    "orderType": "1",
    "syncAction": "edu_trade_pay_status_sync",
    "payTime": 1675737492000,
    "subject": "教育产品",
    "refundStatus": 1,
    "alipayAppId": "123400",
    "payType": "1",
    "feature": "{\"key\":\"1234\"}",
    "merchantId": 2088107,
    "closeTime": 1675737493000,
    "refundAmount": 100,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "CorpId": "ding48591xx",
    "orderNo": "xx20230314xxxxxxxxxxxx",
    "tradeNo": "2022080311111",
    "merchantMergeOrderNo": "M20000100",
    "refundTime": 1675737493000,
    "actualAmount": 100,
    "userId": 1000,
    "merchantOrderNo": "1678xxxx000",
    "labelAmount": 100,
    "createTime": 1675737492000,
    "EventTime": 1675732000,
    "payLogonId": 138,
    "BizId": "bizxxxxx",
    "payStatus": 2
  }
}
```
