---
title: "支付状态同步"
source_url: "https://open.dingtalk.com/document/development/payment-status-synchronization"
namespace: "development"
slug: "payment-status-synchronization"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 支付状态同步"
doc_id: "p2dgE9jpz6"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/payment-status-synchronization
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 支付状态同步
> Updated: 2022-01-19 19:29:22

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
