---
title: "（可选）应用市场开放能力接入"
source_url: "https://open.dingtalk.com/document/services/application-market-open-capability-access"
namespace: "services"
slug: "application-market-open-capability-access"
group: "应用开发"
tab: "平台服务"
breadcrumb: "合作指南 > 产品方案商 > 应用市场的合作指引 > （可选）应用市场开放能力接入"
doc_id: "ep1RKGpQiN"
updated_at: "2026-08-25 09:45:09"
---

> Source: https://open.dingtalk.com/document/services/application-market-open-capability-access
> Path: 应用开发 / 平台服务 / 合作指南 > 产品方案商 > 应用市场的合作指引 > （可选）应用市场开放能力接入
> Updated: 2026-08-25 09:45:09

# （可选）应用市场开放能力接入

本文主要讲述的是钉钉平台除直接提供应用市场相关功能之外还提供了一系列开放API接口供广大开发者接入使用。

## 1、应用内购功能接入

针对有应用内购买接入需求的服务商请参考以下**接入步骤**完成应用内购买功能的开发及上线。

> **[!IMPORTANT]**
>
> 应用内购当前不支持优惠券、满赠等优惠能力。

1. [应用内购概述](../02-4a8AMF6u2A-服务端-API/0876-application-market-overview.md)
2. [内购商品购买与核销](../02-4a8AMF6u2A-服务端-API/0878-lg1nb7.md)
3. [创建内购商品](../02-4a8AMF6u2A-服务端-API/0877-byb8fg.md)
4. [获取内购商品SKU页面地址](../02-4a8AMF6u2A-服务端-API/0883-obtain-the-address-of-the-product-sku-details-page.md)
5. [内购商品订单处理完成](../02-4a8AMF6u2A-服务端-API/0884-internal-purchase-order-processing-completed.md)
6. [获取内购订单信息](../02-4a8AMF6u2A-服务端-API/0885-obtain-information-about-internal-purchase-orders.md)
7. [应用内购商品核销](../02-4a8AMF6u2A-服务端-API/0886-application-of-in-house-purchase-verification.md)
8. [获取未处理的已支付订单](../02-4a8AMF6u2A-服务端-API/0887-obtaining-isv-unfinished-processing-order.md)

## 2、交易信息推送接入

应用商品上架后如果有用户成功发起订单请求，在订单**支付完成**、**订单关闭**、**订单退款**、订**购服务开通**、**订购服务到期**等场景下钉钉侧会**推送相关的交易数据给到ISV**，由各ISV按照接入文档完成推送消息的接入。

推送消息接入分为**HTTP接入和RDS接入**，具体接入形式请在开发者后台进行配置，配置样例如下。

- 推送类型为**使用HTTP推送**时，不需要做额外的订阅。

  ![使用HTTP推送](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6400112261/p265815.png)
- 推送类型为**使用SyncHTTP推送**或**使用钉钉云推送**时，需要勾选下图标识出来的2个订阅事件。

  ![钉钉云推送](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6400112261/p265822.png)

针对**试用规格的开通**，钉钉平台会推送1条试用订单开通的订单数据给到ISV，ISV接收到推送消息后用来给购买客户开通应用服务等操作。

- [试用订单（商品操作）推送](../04-LFcRvVD08N-事件订阅/0190-commodity-operation.md)

  针对付费规格购买，在订单支付、订单关闭、订单退款场景下钉钉平台会推送1笔订单。
- [付费订单（应用市场下单）推送](../04-LFcRvVD08N-事件订阅/0191-application-market-order.md)
- 订购信息推送：

  - [钉钉交易订购开启](../04-LFcRvVD08N-事件订阅/0195-dingtalk-transaction-ordering-on.md)
  - [钉钉交易订购关闭](../04-LFcRvVD08N-事件订阅/0196-dingtalk-transaction-ordering-closed.md)

## 3、续费变配接入

客户提前续费时，可选择低规格版本或者高规格版本，当前在用的规格使用到期之后新的周期将按照用户选择的低规格版本或者高规格版本生效。

### 名词解释

按照客户提前续费时选择的不同版本，可以将续费定义为以下三种形式：

- **续费**：续费规格版本**等于**当前在用版本
- **续费升配**：续费规格版本**大于**当前在用版本
- **续费降配**：续费规格版本**小于**当前在用版本

### 使用场景说明：

当用户因组织架构调整或其它原因，在当前规格周期到期后，想选择更高版本或更低版本的规格来满足业务需要。**如果不选择接入续费变配能力，则客户在续期操作时将只能继续选择同规格的版本。**

续费变配接入流程，请参考[续费变配接入](../02-4a8AMF6u2A-服务端-API/0881-renewal-and-configuration-change-access.md)。

## 4、应用内授权开通接入

应用内开通接入流程，请参考[移动端应用内授权](../02-4a8AMF6u2A-服务端-API/0879-in-app-authorization-to-open-access.md#3b0cf6efb5pp9)。

## 5、个人版&免费规格接入

应用内授权&个人版&免费规格接入流程，请参考[成员授权接入](../02-4a8AMF6u2A-服务端-API/0880-document-on-authorization-of-application-market-members.md)。
