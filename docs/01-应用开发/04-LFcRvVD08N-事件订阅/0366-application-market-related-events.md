---
title: "应用市场事件"
source_url: "https://open.dingtalk.com/document/development/application-market-related-events"
namespace: "development"
slug: "application-market-related-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 应用市场事件"
doc_id: "HUpGcq7lXu"
updated_at: "2025-10-16 15:06:42"
---

> Source: https://open.dingtalk.com/document/development/application-market-related-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 应用市场事件
> Updated: 2025-10-16 15:06:42

# 应用市场事件

本文介绍了应用市场RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 应用市场数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 17 | xxxxx\_0 | corpxxxx | orderidxx | 17 | 市场订单 |
| 37 | xxxxx\_0 | corpxxxx | orderidxx | 37 | 应用市场商业化服务关闭或服务开通事件 |
| 63 | xxxxx\_0 | corpxxxx | 开通人的unionid | 63 | 应用开通记录回调信息 |
| 212 | xxxxx\_0 | corpxxxx | 无业务意义，幂等。 | 212 | 应用商品订单退款事件 |

## biz\_type=17

当biz\_type=17时，数据为订单信息。

该数据为企业在钉钉服务市场购买开通应用产生订单时刻推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 订单的orderid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "orderId": "312139204444444",
    "suiteId": 123123,
    "suiteKey": "xxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "corpId": "dingxxxxxxxxxxxx",
    "maxOfPeople": 100,
    "minOfPeople": 0,
    "paidtime": 1524897069000,
    "serviceStopTime": 1524897069000,
    "payFee": 1000,
    "orderCreatSource": "xxxx",
    "distributorCorpName": "测试代理企业",
    "distributorCorpId": "dingxxxxxxxxxxxxx",
    "nominalPayFee": 1000,
    "discountFee": 0,
    "discount": 1,
    "subQuantity": 1,
    "serviceStartTime": 168000312000,
    "orderType": "RENEW",
    "unionId": "union1265341625",
    "outTradeNo": "30990011123",
    "mainArticleCode": "DT_GOODS_1233",
    "mainArticleName": "测试商品001",
    "openId": "2343242412",
    "isvOperationCode": "***",
    "articleType": "normal",
    "originalArticleCode": "DT_GOODS_23311",
    "originalItemCode": "DT_GOODS_23311_123",
    "appId": 299011,
    "extendParam": {
        "name": "***"
    },
    "buyUserId": "staff2313",
    "solutionPackageKey": "SOLUTION313-31231",
    "solutionPackageName": "中小企业财务解决方案",
    "mainCorpId": "ding23093214311",
    "saleModelType": "CYC_UPGRADE",
    "orderLabel": 1,
    "presentRelMainOrderId": 209130000311,
    "autoChangeFreeItem": false,
    "leadsFrom": "广场-搜索",
    "purchaseType":1
}
```

字段说明：

| 字段 | 说明 |
| --- | --- |
| orderId | 订单ID。 |
| syncAction | 该订单对应的用户操作。  当syncAction为market\_order时，表示市场订单支付。 |
| suiteId | 用户购买第三方企业应用的suiteId。 |
| suiteKey | 用户购买第三方企业应用的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| maxOfPeople | 规格支持最大使用人数。 |
| minOfPeople | 规格支持最小使用人数。 |
| corpId | 购买企业的corpId。 |
| buyCorpId | 购买企业的corpId。  **[!IMPORTANT]**  使用HTTP推送方式时返回此参数，且此参数即将废弃，**建议使用corpId作为购买企业的唯一标识。** |
| distributorCorpName | 分销商企业名称。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| distributorCorpId | 分销商企业corpId。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| paidtime | 支付时间（单位：毫秒）。 |
| serviceStopTime | 服务结束时间（单位：毫秒）。 |
| orderCreatSource | 订单来源：   - 默认订单来自应用中心。 - 若值为**TIANYUAN**，表示来自天元系统平台。 |
| payFee | 实际支付价格（单位：分）。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| nominalPayFee | 名义票面费用（单位：分），现与payFee值相等。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| discountFee | 折扣减免费用（单位：分），现值为0。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| discount | 折扣，现值为1.00。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| serviceStartTime | 服务开始时间（单位：毫秒）。 |
| orderType | 订单类型，取值：   - **BUY**：新购 - **RENEW**：续费 - **UPGRADE**：升级 - **RENEW\_UPGRADE**：续费升配 - **RENEW\_DEGRADE**：续费降配 |
| unionId | 下单人unionId。 |
| outTradeNo | 外部订单号。 |
| mainGoodsCode | 内购商品关联的主应用商品code。  **[!NOTE]**  当订单为内购商品订单时该字段有值。 |
| mainGoodsName | 内购商品关联的主应用商品名称。  **[!NOTE]**  当订单为内购商品订单时该字段有值。 |
| openId | 用户在当前开放应用内的唯一标识。 |
| purchaseType | 购买类型。   - **1**：组织购买 - **2**：个人购买 |
| isvOperationCode | 开发者后台商品管理生成商品二维码时ISV填入的渠道码。 |
| articleType | 商品类型，取值：   - **normal**：普通商品 - **image**：OXM镜像商品。   **[!NOTE]**  OXM商品：非官方商品纳入钉钉一方售卖的机制，需要确定对接方式，并经过必要的立项和评审环节，可融入付费钉钉或独立售卖，支持进入钉钉甄选市场的商品。 |
| originalArticleCode | 镜像商品对应的原生商品Code。  **[!NOTE]**  非OXM商品可不用关注该字段。 |
| originalItemCode | 镜像商品规格Code对应的原生商品的规格Code。  **[!NOTE]**  非OXM商品可不用关注该字段。 |
| appId | 应用ID。  **[!NOTE]**  内购订单时该字段有值。 |
| extendParam | 订单扩展参数。 |
| buyUserId | 下单人在企业内的工号。 |
| solutionPackageKey | 解决方案KEY值。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| solutionPackageName | 解决方案名称。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| mainCorpId | 个人体验版虚拟组织对应的主组织ID。 |
| autoChangeFreeItem | 自动转免费规格。  **[!NOTE]**  付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。 |
| orderLabel | 订单标记，取值   - **0**: 普通订单 - **1**：满赠订单 |
| presentRelMainOrderId | 满赠订单关联的付费主订单ID。 |
| leadsFrom | 商机来源，取值包含：   - 工作台-底部推荐 - 工作台-分组推荐 - 工作台-分组更多-顶部推荐位 - 工作台-应用图标推荐 - 广场-搜索 - 广场-banner - 广场-专题 - 广场-商品推荐 - 应用中心-新企业管理员推荐 - 应用中心-搜索 - 应用中心-banner - 应用中心-专题 - 应用中心-全部应用（安卓） - 应用中心-解决方案 - 人事专区 - 开发者后台-推广码 - PC应用中心 |
| saleModelType | 售卖模式，取值：   - **CYC\_UPGRADE\_MEMBER**： 按周期 + 数量（人数）售卖 - **CYC\_UPGRADE**： 按周期售卖 - **QUANTITY**： 按数量（人数）售卖 |

## biz\_type=37

当biz\_type=37时，数据为应用市场商业化服务关闭数据或服务开通数据。

该数据在退款导致服务关闭或续费变配生效时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 订单orderId。 |
| biz\_data | 数据为Json格式。 |

#### **服务关闭的biz\_data数据如下（目前仅退款导致服务关闭时推送）：**

```
{
    "eventType": "subscription_close",
    "syncAction": "market_service_close",
    "orderId": "312139204444444",
    "corpId": "dingxxxxxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "suiteId": 123123,
    "suiteKey": "xxxxxxxxx",
    "payFee": 1000,
    "subQuantity": 1,
    "closeType": 3
}
```

**字段说明：**

| 字段 | 说明 |
| --- | --- |
| eventType | 事件类型：   - **subscription\_close**：服务关闭事件 |
| syncAction | 操作类型：   - **market\_service\_close**：服务关闭事件 |
| orderId | 订单id。 |
| corpId | 购买企业的corpId。 |
| suiteId | 用户购买第三方企业应用的suiteId。 |
| suiteKey | 用户购买第三方企业应用的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| payFee | 实际支付价格（单位：分）。 |
| closeType | 服务关闭类型：   - **3**：退款导致的服务关闭 |

#### 服务开通的biz\_data数据如下（目前仅续费变配服务开通时推送）：

```
{
    "eventType": "subscription_open",
    "syncAction": "market_service_open",
    "orderId": "312139204444444",
    "corpId": "dingxxxxxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "suiteId": 123123,
    "suiteKey": "xxxxxxxxx",
    "payFee": 1000,
    "subQuantity": 1,
    "serviceStartTime": 167000031311,
    "serviceStopTime": 168000031311,
    "openType": 3
}
```

**字段说明：**

| 字段 | 说明 |
| --- | --- |
| eventType | 事件类型：   - **subscription\_open**：服务开通事件 |
| syncAction | 操作类型：   - **market\_service\_open**：服务开通事件 |
| orderId | 订单id。 |
| corpId | 购买企业的corpId。 |
| suiteId | 用户购买第三方企业应用的suiteId。 |
| suiteKey | 用户购买第三方企业应用的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| payFee | 实际支付价格（单位：分）。 |
| serviceStartTime | 订购服务开始时间（单位：毫秒）。 |
| serviceStopTime | 订购服务结束时间（单位：毫秒）。 |
| openType | 服务开通类型：   - **3**：续费变配开通 |

## biz\_type=63

应用商品新增个人开通后，增加了应用的触达率，为了方便ISV对客户进行后续跟踪和推广，组织/个人在应用开通后，钉钉后台新增了应用开通记录的回调信息。

目前应用开通的回调信息有两种：

1. 应用开通的订单信息

   侧重于订单信息回调。
2. 应用开通的记录信息

   应用开通记录回调信息中不一定会有订单。

> **[!IMPORTANT]**
>
> 当同组织的两个用户对同一商品的开通时间完全重合，或者同组织下已经开通该商品的有效期完全包含新开通商品有效期的时候，不会产生订单。

当biz\_type=63时，为应用开通记录的回调信息。

当组织或个人应用开通时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 开通人的unionid。 |
| biz\_type | 63，为固定值，标识应用开通记录的回调信息。 |
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
    "itemType":"charge_goods_free_item"
}
```

字段说明：

| **字段** | **说明** |
| --- | --- |
| buyerUnionId | 系统生成，固定值不会改变，可用来识别下单人。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| suiteId | 第三方企业应用的ID。 |
| fromDate | 开始时间。 |
| endDate | 结束时间。 |
| appId | 应用ID。 |
| tryoutType | 开通类型。   - **personal\_tryout**：个人开通 - **enterprise\_tryout**：企业开通（管理员） |
| goodsCode | 商品码。 |
| itemType | 开通的规格类型：   - **charge\_goods\_free\_item**：付费商品的免费规格 - **charge\_item**: 付费规格   **[!NOTE]**  当开通付费商品的免费规格/付费规格时会返回该字段。 |
| EventType | 事件类型。 |

## biz\_type=212

当biz\_type=212时，数据为应用商品订单退款事件。

该数据为应用商品订单退款的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值212，表示应用商品订单退款的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "corpId" : "ding57935b18bfd13e9735cxxxxxxxxxx",
  "syncAction" : "market_order_refund_event",
  "orderId": "208****232",
  "refundFee": 10000.00
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | **事件类型：**   - market\_order\_refund\_event：应用商品订单退款 |
| orderId | String | 退款订单的orderId。 |
| refundFee | Long | 退款金额。 |
| corpId | String | 企业corpId。 |
