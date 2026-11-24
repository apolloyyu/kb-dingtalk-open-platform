---
title: "企业在应用市场开通应用产生的订单"
source_url: "https://open.dingtalk.com/document/development/orders-generated-by-enterprises-opening-applications-in-the-application-market-stream"
namespace: "development"
slug: "orders-generated-by-enterprises-opening-applications-in-the-application-market-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 应用市场事件 > 企业在应用市场开通应用产生的订单"
doc_id: "RDP3YJiD2Z"
updated_at: "2025-10-16 14:32:41"
---

> Source: https://open.dingtalk.com/document/development/orders-generated-by-enterprises-opening-applications-in-the-application-market-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 应用市场事件 > 企业在应用市场开通应用产生的订单
> Updated: 2025-10-16 14:32:41

# 企业在应用市场开通应用产生的订单

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业在应用市场开通应用产生的订单 |
| 英文名称 | market\_order |

## 功能描述

eventType为market\_order，表示企业在钉钉服务市场购买开通应用产生订单时，钉钉推送的市场订单数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `orderId`（string）：订单ID。
- `suiteId`（long）：用户购买第三方企业应用的suiteId。
- `suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `goodsName`（string）：商品名称。
- `goodsCode`（string）：商品码。
- `itemName`（string）：规格名称。
- `itemCode`（string）：规格码。
- `corpId`（string）：购买企业的corpId。
- `maxOfPeople`（integer）：规格支持最大使用人数。
- `minOfPeople`（integer）：规格支持最小使用人数。
- `paidtime`（long）：支付时间（单位：毫秒）。
- `serviceStopTime`（long）：服务结束时间（单位：毫秒）。
- `payFee`（integer）：实际支付价格（单位：分）。  
  >当商品类型articleType为image时不返回此字段。
- `orderCreatSource`（string）：订单来源：  
  - 默认订单来自应用中心。  
  - 若值为TIANYUAN，表示来自天元系统平台。
- `distributorCorpName`（string）：分销商企业名称。  
  >当商品类型articleType为image时不返回此字段。
- `distributorCorpId`（string）：分销商企业corpId。  
  >当商品类型articleType为image时不返回此字段。
- `nominalPayFee`（integer）：名义票面费用（单位：分），现与payFee值相等。  
  >当商品类型articleType为image时不返回此字段。
- `discountFee`（integer）：折扣减免费用（单位：分），现值为0。  
  >当商品类型articleType为image时不返回此字段。
- `discount`（float）：折扣，现值为1.00。  
  >当商品类型articleType为image时不返回此字段。
- `subQuantity`（integer）：购买数量。
- `serviceStartTime`（long）：服务开始时间（单位：毫秒）。
- `orderType`（string）：订单类型，取值：  
  - BUY：新购  
  - RENEW：续费  
  - UPGRADE：升级  
  - RENEW\_UPGRADE：续费升配  
  - RENEW\_DEGRADE：续费降配
- `unionId`（string）：下单人unionId。
- `outTradeNo`（string）：外部订单号。
- `mainArticleCode`（string）：内购商品关联的主应用商品code。  
  >当订单为内购商品订单时该字段有值。
- `mainArticleName`（string）：内购商品关联的主应用商品名称。  
  >当订单为内购商品订单时该字段有值。
- `openId`（string）：用户在当前开放应用内的唯一标识。
- `orderChannelCode`（string）：订单来源渠道码。
- `isvOperationCode`（string）：开发者后台商品管理生成商品二维码时ISV填入的渠道码。
- `articleType`（string）：商品类型，取值：  
  - normal：普通商品  
  - image：OXM镜像商品  
  >OXM商品：非官方商品纳入钉钉一方售卖的机制，需要确定对接方式，并经过必要的立项和评审环节，可融入付费钉钉或独立售卖，支持进入钉钉甄选市场的商品。
- `originalArticleCode`（string）：镜像商品对应的原生商品Code。  
  >非OXM商品可不用关注该字段。
- `originalItemCode`（string）：镜像商品对应的原生商品Code。
- `appId`（long）：应用ID。  
  >内购订单时该字段有值。
- `extendParam`（object）：订单扩展参数。
- `extendParam.name`（string）：名字
- `buyUserId`（string）：下单人在企业内的工号。
- `solutionPackageKey`（string）：解决方案KEY值。  
  >当订单为解决方案时该字段有值。
- `solutionPackageName`（string）：解决方案名称。  
  >当订单为解决方案时该字段有值。
- `mainCorpId`（string）：个人体验版虚拟组织对应的主组织ID。
- `saleModelType`（string）：售卖模式，取值：  
  - CYC\_UPGRADE\_MEMBER： 按周期 + 数量（人数）售卖  
  - CYC\_UPGRADE： 按周期售卖  
  - QUANTITY： 按数量（人数）售卖
- `orderLabel`（integer）：订单标记，取值：  
  - 0: 普通订单  
  - 1：满赠订单
- `presentRelMainOrderId`（long）：满赠订单关联的付费主订单ID。
- `autoChangeFreeItem`（boolean）：自动转免费规格。>付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。
- `leadsFrom`（string）：商机来源，取值包含：  
  - 工作台-底部推荐  
  - 工作台-分组推荐  
  - 工作台-分组更多-顶部推荐位  
  - 工作台-应用图标推荐  
  - 广场-搜索  
  - 广场-banner  
  - 广场-专题  
  - 广场-商品推荐  
  - 应用中心-新企业管理员推荐  
  - 应用中心-搜索  
  - 应用中心-banner  
  - 应用中心-专题  
  - 应用中心-全部应用（安卓）  
  - 应用中心-解决方案  
  - 人事专区  
  - 开发者后台-推广码  
  - PC应用中心
- `purchaseType`（integer）：购买类型。  
  - 1：组织购买  
  - 2：个人购买

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "market_order",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "orderType": "RENEW",
    "distributorCorpName": "测试代理企业",
    "discountFee": 0,
    "solutionPackageName": "中小企业财务解决方案",
    "orderId": "312139204444444",
    "openId": "2343242412",
    "itemCode": "xxxxxxx",
    "orderLabel": 1,
    "saleModelType": "CYC_UPGRADE",
    "solutionPackageKey": "SOLUTION313-31231",
    "discount": "1",
    "maxOfPeople": 100,
    "autoChangeFreeItem": false,
    "purchaseType": 1,
    "distributorCorpId": "dingxxxxxxxxxxxxx",
    "originalArticleCode": "DT_GOODS_23311",
    "itemName": "测试规格",
    "buyUserId": "staff2313",
    "payFee": 1000,
    "serviceStopTime": 1524897069000,
    "articleType": "normal",
    "serviceStartTime": 168000312000,
    "appId": 299011,
    "outTradeNo": "30990011123",
    "suiteKey": "xxxxxxxxx",
    "orderCreatSource": "xxxx",
    "mainCorpId": "ding23093214311",
    "mainArticleName": "测试商品001",
    "goodsName": "测试商品",
    "minOfPeople": 0,
    "suiteId": 123453,
    "unionId": "union1265341625",
    "corpId": "dingxxxxxxxxxxxx",
    "mainArticleCode": "DT_GOODS_1233",
    "subQuantity": 1,
    "originalItemCode": "DT_GOODS_23311_123",
    "leadsFrom": "广场-搜索",
    "presentRelMainOrderId": 209130000311,
    "extendParam": {
      "name": "xxx"
    },
    "nominalPayFee": 1000,
    "isvOperationCode": "****",
    "goodsCode": "xxxxxxxxxxx",
    "paidtime": 1524897069000,
    "orderChannelCode": "all_star_isv_channel_code"
  }
}
```
