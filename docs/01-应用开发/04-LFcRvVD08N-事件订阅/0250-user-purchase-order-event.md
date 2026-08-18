---
title: "用户购买下单事件"
source_url: "https://open.dingtalk.com/document/development/user-purchase-order-event"
namespace: "development"
slug: "user-purchase-order-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 用户购买下单事件"
doc_id: "03mFSBbkdG"
updated_at: "2025-10-16 14:31:47"
---

> Source: https://open.dingtalk.com/document/development/user-purchase-order-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 用户购买下单事件
> Updated: 2025-10-16 14:31:47

# 用户购买下单事件

本文介绍了用户购买下单事件的相关说明。

此事件的推送会发生在企业在钉钉应用市场下单购买应用后，向ISV应用回调地址POST数据。

> **[!NOTE]**
>
> 用户购买下单事件适用于第三方企业应用。

**POST数据解密后示例：**

```
{
    "SuiteKey": "xxxxxx",
    "EventType": "market_buy",
    "orderId": 308356401,
    "goodsCode": "FW_GOODS-xxxxxxxx",
    "goodsName": "测试上001",
    "buyCorpId": "xxxxxx",
    "corpId": "xxxxxx",
    "itemCode": "1c5f70cf04c437fb9aa1b20xxxxxxxx",
    "itemName": "按照范围收费规格0-300",
    "subQuantity": 1,
    "maxOfPeople": 300,
    "minOfPeople": 0,
    "serviceStopTime": 1477065600000,
    "paidtime": 1474535702000,
    "orderCreateSource": "APP-STORE",
    "buyUserId": "staff2313",
    "articleType": "normal",
    "originalArticleCode": "DT_GOODS_23311",
    "originalItemCode": "DT_GOODS_23311_123",
    "payFee": 147600,
    "nominalPayFee": 147600,
    "discountFee": 600,
    "discount": 0.06,
    "distributorCorpId": "xxxxxx",
    "distributorCorpName": "测试企业",
    "serviceStartTime": 1477065500000,
    "orderType": "BUY",
    "orderChargeType": "FREE",
    "saleModelType": "CYC_UPGRADE",
    "openId": 3412321001,
    "unionId": "gliiW0piiii02zBUjUxxxx",
    "outTradeNo": 209310000312,
    "mainGoodsCode": "DT_GOODS_39001",
    "mainGoodsName": "测试商品002",
    "appId": 299011,
    "extendParam": {
        "name": "***"
    },
    "isvOperationCode": "*****",
    "solutionPackageKey": "SOLUTION313-31231",
    "solutionPackageName": "中小企业财务解决方案",
    "mainCorpId": "ding23093214311",
    "autoChangeFreeItem": false,
    "orderLabel": 1,
    "presentRelMainOrderId": 209130000311,
    "leadsFrom": "广场-搜索",
    "purchaseType": 1
}
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| SuiteKey | 用户购买的应用的SuiteKey。 |
| EventType | 回调事件类型。 |
| corpId | 购买该应用企业的corpid。 |
| buyCorpId | 购买该应用企业的corpid。  **[!IMPORTANT]**  使用HTTP推送方式时返回此参数，且此参数即将废弃，**建议使用corpId作为购买企业的唯一标识。** |
| goodsCode | 购买的商品码。 |
| itemCode | 购买的商品规格码。 |
| itemName | 购买的商品规格名称。 |
| subQuantity | 订购的具体人数。 |
| maxOfPeople | 购买的商品规格能服务的最多企业人数。 |
| minOfPeople | 购买的商品规格能服务的最少企业人数。 |
| orderId | 订单ID。 |
| paidtime | 下单时间。 |
| serviceStopTime | 该订单的服务到期时间。 |
| payFee | 订单支付费用，以分为单位。 |
| orderCreateSource | 订单创建来源，如果来自钉钉分销系统，则值为"TIANYUAN"。 |
| nominalPayFee | 钉钉分销系统提单价，以分为单位。 |
| discountFee | 折扣减免费用。 |
| discount | 订单折扣。 |
| distributorCorpId | 钉钉分销系统提单的代理商的企业corpId。 |
| distributorCorpName | 钉钉分销系统提单的代理商的企业名称。 |
| serviceStartTime | 该订单的服务开始时间。 |
| orderType | 订单类型，取值：   - BUY：新购 - RENEW：续费 - UPGRADE：升级 - RENEW\_UPGRADE：续费升配 - RENEW\_DEGRADE：续费降配 |
| orderChargeType | 订单收费类型，取值   - FREE：免费开通 - TRYOUT：试用开通   **[!NOTE]**  仅针对试用规格。 |
| saleModelType | 售卖模式，取值：   - **CYC\_UPGRADE\_MEMBER**： 按周期 + 数量（人数）售卖 - **CYC\_UPGRADE**： 按周期售卖 - **QUANTITY**： 按数量（人数）售卖 |
| openId | 用户在当前开放应用内的唯一标识。 |
| unionId | 用户在当前钉钉开放平台账号范围内的唯一标识。 |
| outTradeNo | 外部订单号。 |
| mainGoodsCode | 内购商品关联的主应用商品code,当订单为内购商品订单时该字段有值。 |
| mainGoodsName | 内购商品关联的主应用商品名称,当订单为内购商品订单时该字段有值。 |
| appId | 应用ID。  **[!NOTE]**  内购订单时该字段有值。 |
| purchaseType | 购买类型，取值：   - **1**：组织购买 - **2**：个人购买 |
| extendParam | 订单扩展参数。 |
| isvOperationCode | 开发者后台商品管理生成商品二维码时ISV填入的渠道码。 |
| solutionPackageKey | 解决方案KEY值。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| solutionPackageName | 解决方案名称。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| mainCorpId | 个人体验版虚拟组织对应的主组织ID。 |
| autoChangeFreeItem | 自动转免费规格。  **[!NOTE]**  付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。 |
| orderLabel | 订单标记，取值：   - **0**：普通订单 - **1**：满赠订单 |
| presentRelMainOrderId | 满赠订单关联的付费主订单ID。 |
| leadsFrom | 商机来源，取值包含：   - 工作台-底部推荐 - 工作台-分组推荐 - 工作台-分组更多-顶部推荐位 - 工作台-应用图标推荐 - 广场-搜索 - 广场-banner - 广场-专题 - 广场-商品推荐 - 应用中心-新企业管理员推荐 - 应用中心-搜索 - 应用中心-banner - 应用中心-专题 - 应用中心-全部应用(安卓) - 应用中心-解决方案 - 人事专区 - 开发者后台-推广码 - PC应用中心 |

应用在收到此事件推送后务必返回包含经过加密的字符串"success"的JSON数据。只有返回了对应的JSON数据，钉钉才会判断此事件推送成功。

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d15066227608",
  "timestamp":"1783610513",
  "nonce":"123456",
  "encrypt":"1vn9lYTuuHSoaxwCGylH9xRhasdfghjkl" // "success"字段的加密数据
}
```

其中：

- **msg\_signature**：消息体签名。
- **timestamp**：时间戳。
- **nonce**：随机字符串。
- **encrypt**："success"的加密字符串。
