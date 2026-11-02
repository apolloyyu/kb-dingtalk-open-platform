---
title: "应用市场下单"
source_url: "https://open.dingtalk.com/document/development/application-market-order"
namespace: "development"
slug: "application-market-order"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用市场 > 应用市场下单"
doc_id: "rjnsKkqJLK"
updated_at: "2025-08-28 19:47:20"
---

> Source: https://open.dingtalk.com/document/development/application-market-order
> Path: 应用开发 / 事件订阅 / 应用市场 > 应用市场下单
> Updated: 2025-08-28 19:47:20

# 应用市场下单

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 应用市场下单 |
| 英文名称 | market\_order |

## 功能描述

数据为企业在钉钉服务市场购买开通应用产生订单时刻，推送的订单信息事件内容。

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
- `data.orderId`（string）：订单ID。
- `data.suiteId`（long）：用户购买第三方企业应用的suiteId。
- `data.suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `data.goodsName`（string）：商品名称。
- `data.goodsCode`（string）：商品码。
- `data.itemName`（string）：规格名称。
- `data.itemCode`（string）：规格码。
- `data.corpId`（string）：购买企业的corpId。
- `data.maxOfPeople`（integer）：规格支持最大使用人数。
- `data.minOfPeople`（integer）：规格支持最小使用人数。
- `data.paidtime`（long）：支付时间（单位：毫秒）。
- `data.serviceStopTime`（long）：服务结束时间（单位：毫秒）。
- `data.payFee`（integer）：实际支付价格（单位：分）。  
  >当商品类型articleType为image时不返回此字段。
- `data.orderCreatSource`（string）：订单来源：  
  - 默认订单来自应用中心。  
  - 若值为TIANYUAN，表示来自天元系统平台。
- `data.distributorCorpName`（string）：分销商企业名称。  
  >当商品类型articleType为image时不返回此字段。
- `data.distributorCorpId`（string）：分销商企业corpId。  
  >当商品类型articleType为image时不返回此字段。
- `data.nominalPayFee`（integer）：名义票面费用（单位：分），现与payFee值相等。  
  >当商品类型articleType为image时不返回此字段。
- `data.discountFee`（integer）：折扣减免费用（单位：分），现值为0。  
  >当商品类型articleType为image时不返回此字段。
- `data.discount`（float）：折扣，现值为1.00。  
  >当商品类型articleType为image时不返回此字段。
- `data.subQuantity`（integer）：购买数量。
- `data.serviceStartTime`（long）：服务开始时间（单位：毫秒）。
- `data.orderType`（string）：订单类型，取值：  
  - BUY：新购  
  - RENEW：续费  
  - UPGRADE：升级  
  - RENEW\_UPGRADE：续费升配  
  - RENEW\_DEGRADE：续费降配
- `data.unionId`（string）：下单人unionId。
- `data.outTradeNo`（string）：外部订单号。
- `data.mainArticleCode`（string）：内购商品关联的主应用商品code。  
  >当订单为内购商品订单时该字段有值。
- `data.mainArticleName`（string）：内购商品关联的主应用商品名称。  
  >当订单为内购商品订单时该字段有值。
- `data.openId`（string）：用户在当前开放应用内的唯一标识。
- `data.orderChannelCode`（string）：订单来源渠道码。
- `data.param1798`（string）
- `data.isvOperationCode`（string）：开发者后台商品管理生成商品二维码时ISV填入的渠道码。
- `data.articleType`（string）：商品类型，取值：  
  - normal：普通商品  
  - image：OXM镜像商品  
  >OXM商品：非官方商品纳入钉钉一方售卖的机制，需要确定对接方式，并经过必要的立项和评审环节，可融入付费钉钉或独立售卖，支持进入钉钉甄选市场的商品。
- `data.originalArticleCode`（string）：镜像商品对应的原生商品Code。  
  >非OXM商品可不用关注该字段。
- `data.originalItemCode`（string）：镜像商品对应的原生商品Code。
- `data.appId`（long）：应用ID。  
  >内购订单时该字段有值。
- `data.extendParam`（object）：订单扩展参数。
- `data.extendParam.name`（string）：名字
- `data.buyUserId`（string）：下单人在企业内的工号。
- `data.solutionPackageKey`（string）：解决方案KEY值。  
  >当订单为解决方案时该字段有值。
- `data.solutionPackageName`（string）：解决方案名称。  
  >当订单为解决方案时该字段有值。
- `data.mainCorpId`（string）：个人体验版虚拟组织对应的主组织ID。
- `data.saleModelType`（string）：售卖模式，取值：  
  - CYC\_UPGRADE\_MEMBER： 按周期 + 数量（人数）售卖  
  - CYC\_UPGRADE： 按周期售卖  
  - QUANTITY： 按数量（人数）售卖
- `data.orderLabel`（integer）：订单标记，取值：  
  - 0: 普通订单  
  - 1：满赠订单
- `data.presentRelMainOrderId`（long）：满赠订单关联的付费主订单ID。
- `data.autoChangeFreeItem`（boolean）：自动转免费规格。>付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。
- `data.leadsFrom`（string）：商机来源，取值包含：  
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
- `data.purchaseType`（integer）：购买类型。  
  - 1：组织购买  
  - 2：个人购买

### **事件体示例**

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
    "discount": 1.0,
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

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.orderId`（string）：订单ID。
- `biz_data.suiteId`（long）：用户购买第三方企业应用的suiteId。
- `biz_data.suiteKey`（string）：用户购买第三方企业应用的suiteKey。
- `biz_data.goodsName`（string）：商品名称。
- `biz_data.goodsCode`（string）：商品码。
- `biz_data.itemName`（string）：规格名称。
- `biz_data.itemCode`（string）：规格码。
- `biz_data.corpId`（string）：购买企业的corpId。
- `biz_data.maxOfPeople`（integer）：规格支持最大使用人数。
- `biz_data.minOfPeople`（integer）：规格支持最小使用人数。
- `biz_data.paidtime`（long）：支付时间（单位：毫秒）。
- `biz_data.serviceStopTime`（long）：服务结束时间（单位：毫秒）。
- `biz_data.payFee`（integer）：实际支付价格（单位：分）。  
  >当商品类型articleType为image时不返回此字段。
- `biz_data.orderCreatSource`（string）：订单来源：  
  - 默认订单来自应用中心。  
  - 若值为TIANYUAN，表示来自天元系统平台。
- `biz_data.distributorCorpName`（string）：分销商企业名称。  
  >当商品类型articleType为image时不返回此字段。
- `biz_data.distributorCorpId`（string）：分销商企业corpId。  
  >当商品类型articleType为image时不返回此字段。
- `biz_data.nominalPayFee`（integer）：名义票面费用（单位：分），现与payFee值相等。  
  >当商品类型articleType为image时不返回此字段。
- `biz_data.discountFee`（integer）：折扣减免费用（单位：分），现值为0。  
  >当商品类型articleType为image时不返回此字段。
- `biz_data.discount`（float）：折扣，现值为1.00。  
  >当商品类型articleType为image时不返回此字段。
- `biz_data.subQuantity`（integer）：购买数量。
- `biz_data.serviceStartTime`（long）：服务开始时间（单位：毫秒）。
- `biz_data.orderType`（string）：订单类型，取值：  
  - BUY：新购  
  - RENEW：续费  
  - UPGRADE：升级  
  - RENEW\_UPGRADE：续费升配  
  - RENEW\_DEGRADE：续费降配
- `biz_data.unionId`（string）：下单人unionId。
- `biz_data.outTradeNo`（string）：外部订单号。
- `biz_data.mainArticleCode`（string）：内购商品关联的主应用商品code。  
  >当订单为内购商品订单时该字段有值。
- `biz_data.mainArticleName`（string）：内购商品关联的主应用商品名称。  
  >当订单为内购商品订单时该字段有值。
- `biz_data.openId`（string）：用户在当前开放应用内的唯一标识。
- `biz_data.orderChannelCode`（string）：订单来源渠道码。
- `biz_data.param1798`（string）
- `biz_data.isvOperationCode`（string）：开发者后台商品管理生成商品二维码时ISV填入的渠道码。
- `biz_data.articleType`（string）：商品类型，取值：  
  - normal：普通商品  
  - image：OXM镜像商品  
  >OXM商品：非官方商品纳入钉钉一方售卖的机制，需要确定对接方式，并经过必要的立项和评审环节，可融入付费钉钉或独立售卖，支持进入钉钉甄选市场的商品。
- `biz_data.originalArticleCode`（string）：镜像商品对应的原生商品Code。  
  >非OXM商品可不用关注该字段。
- `biz_data.originalItemCode`（string）：镜像商品对应的原生商品Code。
- `biz_data.appId`（long）：应用ID。  
  >内购订单时该字段有值。
- `biz_data.extendParam`（object）：订单扩展参数。
- `biz_data.extendParam.name`（string）：名字
- `biz_data.buyUserId`（string）：下单人在企业内的工号。
- `biz_data.solutionPackageKey`（string）：解决方案KEY值。  
  >当订单为解决方案时该字段有值。
- `biz_data.solutionPackageName`（string）：解决方案名称。  
  >当订单为解决方案时该字段有值。
- `biz_data.mainCorpId`（string）：个人体验版虚拟组织对应的主组织ID。
- `biz_data.saleModelType`（string）：售卖模式，取值：  
  - CYC\_UPGRADE\_MEMBER： 按周期 + 数量（人数）售卖  
  - CYC\_UPGRADE： 按周期售卖  
  - QUANTITY： 按数量（人数）售卖
- `biz_data.orderLabel`（integer）：订单标记，取值：  
  - 0: 普通订单  
  - 1：满赠订单
- `biz_data.presentRelMainOrderId`（long）：满赠订单关联的付费主订单ID。
- `biz_data.autoChangeFreeItem`（boolean）：自动转免费规格。>付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。
- `biz_data.leadsFrom`（string）：商机来源，取值包含：  
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
- `biz_data.purchaseType`（integer）：购买类型。  
  - 1：组织购买  
  - 2：个人购买

### **biz\_data数据示例(biz\_type=17)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 17,
  "biz_data": {
    "orderType": "RENEW",
    "distributorCorpName": "测试代理企业",
    "discountFee": 0,
    "solutionPackageName": "中小企业财务解决方案",
    "syncAction": "market_order",
    "orderId": "312139204444444",
    "openId": "2343242412",
    "itemCode": "xxxxxxx",
    "orderLabel": 1,
    "saleModelType": "CYC_UPGRADE",
    "solutionPackageKey": "SOLUTION313-31231",
    "discount": 1.0,
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
    "eventId": "c7c7120f2c07419**ebdba0318c8",
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
