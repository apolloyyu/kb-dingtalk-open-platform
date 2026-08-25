---
title: "（已下线）应用试用记录回调信息说明"
source_url: "https://open.dingtalk.com/document/development/application-trial-offline-record-callback-information"
namespace: "development"
slug: "application-trial-offline-record-callback-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > （已下线）应用试用记录回调信息说明"
doc_id: "D4IQmVOvWp"
updated_at: "2025-10-16 14:31:24"
---

> Source: https://open.dingtalk.com/document/development/application-trial-offline-record-callback-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > （已下线）应用试用记录回调信息说明
> Updated: 2025-10-16 14:31:24

# （已下线）应用试用记录回调信息说明

## 回调信息介绍

应用商品新增个人试用后，增加了应用的触达率，为了方便ISV对客户进行后续跟踪和推广，组织/个人在应用试用后，钉钉后台新增了应用试用记录的回调信息。

目前试用的回调信息有两种：

1. 试用开通的订单信息

   试用开通的订单信息，侧重于订单信息回调。
2. 试用开通记录信息

   试用开通记录回调信息中不一定会有试用订单。

> **[!IMPORTANT]**
>
> 当同组织的两个用户对同一商品的试用时间完全重合，或者同组织下已经开通该商品试用的有效期完全包含新开通试用的有效期的时候，不会产生订单。

## 使用开通记录的回调信息

当biz\_type=63时，为应用试用开通记录的回调信息。

当组织或个人应用试用开通时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 63，为固定值，标识应用试用开通记录的回调信息。 |
| biz\_type | 数据为Json格式。 |
| biz\_data | 开通记录数据，JSON格式。 |

示例：

```
{
    "buyerUnionId":"mLyKVGiiwEXQ5mT0Nwxxxx",
    "suiteId":698002,
    "corpId":"dingd678857e4250521135c2f465xxxx",
    "fromDate":"2020-12-04 10:59:25",
    "endDate":"2020-12-19 10:59:25",
    "EventType":"goods_tryout",
    "appId":1948,
    "tryoutType":"enterprise_tryout",
    "goodsCode":"FW_GOODS-100030xxxx",
    "TimeStamp":"1607050765623"
}
```

字段说明：

| **字段** | **说明** |
| --- | --- |
| buyerUnionId | 系统生成，固定值不会改变，可用来识别下单人。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| suiteId | 套件ID。 |
| fromDate | 试用开始时间。 |
| endDate | 试用结束时间。 |
| appId | 应用ID。 |
| tryoutType | 试用类型   - personal\_tryout：个人试用 - enterprise\_tryout：企业试用（管理员） |
| goodsCode | 商品码。 |
| TimeStamp | 时间戳。 |
| EventType | 事件类型。 |
