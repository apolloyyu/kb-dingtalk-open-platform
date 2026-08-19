---
title: "制造业订单交付全过程管理"
source_url: "https://open.dingtalk.com/document/development/management-of-order-delivery-in-the-manufacturing-industry"
namespace: "development"
slug: "management-of-order-delivery-in-the-manufacturing-industry"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 使用教程 > 制造业订单交付全过程管理"
doc_id: "tfPnxoWIdU"
updated_at: "2026-07-20 09:21:36"
---

> Source: https://open.dingtalk.com/document/development/management-of-order-delivery-in-the-manufacturing-industry
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 使用教程 > 制造业订单交付全过程管理
> Updated: 2026-07-20 09:21:36

# 制造业订单交付全过程管理

本文档介绍了如何通过调用通讯录管理和金智CRM接口，实现制造业从客户签约到产品交付的全流程数据打通与自动化管理。首先需创建一个企业内部应用，并基于该应用申请相关API权限，获取访问凭证后，依次调用服务端接口完成客户、销售、采购、仓储等环节的数据协同。

## 使用场景

本方案适用于制造业企业在订单履约过程中的跨部门协作与流程数字化管理，典型业务场景包括：

- **销售合同闭环管理**：从客户建档、销售机会跟进、报价审批到合同签订，实现销售全过程留痕与可追溯。
- **产供销协同联动**：合同订单自动触发采购计划，采购结果驱动入库和生产排程，提升供应链响应效率。
- **仓储物流透明化**：出库单与发货单联动生成，支持物流信息实时同步至客户，增强交付体验。
- **集团多组织协同**：适用于拥有多个生产基地或销售公司的集团型企业，通过统一平台实现数据集中管控。

## 流程简介

步骤一，登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二，获取AppKey和AppSecret。

步骤三，申请接口权限。查找“金智CRM”、“通讯录管理”，申请相应的权限。

步骤四，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五，调用服务端通讯录管理和金智CRM相关API。

订单交付流程：

1. 调用服务端API-[获取部门用户基础信息](0066-queries-the-simple-information-of-a-department-user.md)接口，获取用户基础信息。
2. 调用服务端API-[客户资料](1055-add-or-edit-customer-profile.md)接口，进行客户信息的新增和编辑。
3. 调用服务端API-[产品信息](1065-add-or-edit-product-information.md)接口，进行产品信息的新增和编辑。
4. 调用服务端API-[销售机会](1061-add-or-edit-opportunities.md)接口，进行销售机会的新增和编辑。
5. 调用服务端API-[报价记录](1062-add-or-edit-quotation-records.md)接口，进行报价记录的新增和编辑。
6. 调用服务端API-[合同订单](1058-add-or-edit-contract-orders.md)接口，进行合同订单的新增和编辑。
7. 调用服务端API-[采购单](1063-edit-purchase-order.md)接口，进行采购单的新增和编辑。
8. 调用服务端API-[入库单](1066-add-or-edit-a-shipment-record.md)接口，进行入库单的新增和编辑。
9. 调用服务端API-[发货单](1059-add-or-edit-invoices.md)接口，进行发货单的新增和编辑。
10. 调用服务端API-[出库单](1067-add-or-edit-an-issue-ticket.md)接口，进行出库单的新增和编辑。

数据信息管理：

- 调用服务端API-[获取数据详情](1068-queries-data-details.md)接口，可以获取销售机会、报价单、订单、采购、入库、发货和出库一系列环节的数据详细信息。
- 调用服务端API-[获取数据列表](1069-obtain-the-data-list.md)接口，可得到某一单据的数据列表信息。

## 步骤一，创建企业内部应用

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二，获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三，添加接口权限

申请接口权限。查找“金智CRM”、“通讯录管理”，申请相应的权限。

申请`金智CRM数据管理权限`：

![金智CRM](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6940154871/p410465.png)

申请`通讯录部门成员读权限`权限：

![权限申请通讯录](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6940154871/p410464.png)

## 步骤四，获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

## 步骤五，调用服务端通讯录管理和金智CRM相关API

订单交付流程：

> **[!NOTE]**
>
> - 调用的API新增的数据会返回msgid参数。
> - 每个数据表单的dataType为固定值，详情请参考具体API示例。

1. 调用服务端API-[获取部门用户基础信息](0066-queries-the-simple-information-of-a-department-user.md)接口，获取用户基础信息。
2. 调用服务端API-[客户资料](1055-add-or-edit-customer-profile.md)接口，进行客户信息的新增和编辑。
3. 调用服务端API-[产品信息](1065-add-or-edit-product-information.md)接口，进行产品信息的新增和编辑。
4. 调用服务端API-[销售机会](1061-add-or-edit-opportunities.md)接口，进行销售机会的新增和编辑。
5. 调用服务端API-[报价记录](1062-add-or-edit-quotation-records.md)接口，进行报价记录的新增和编辑。
6. 调用服务端API-[合同订单](1058-add-or-edit-contract-orders.md)接口，进行合同订单的新增和编辑。
7. 调用服务端API-[采购单](1063-edit-purchase-order.md)接口，进行采购单的新增和编辑。
8. 调用服务端API-[入库单](1066-add-or-edit-a-shipment-record.md)接口，进行入库单的新增和编辑。
9. 调用服务端API-[发货单](1059-add-or-edit-invoices.md)接口，进行发货单的新增和编辑。
10. 调用服务端API-[出库单](1067-add-or-edit-an-issue-ticket.md)接口，进行出库单的新增和编辑。

数据信息管理：

- 根据订单交付流程中msgId参数和dataType参数，调用服务端API-[获取数据详情](1068-queries-data-details.md)接口，可以获取销售机会、报价单、订单、采购、入库、发货和出库一系列环节的数据详细信息。
- 调用服务端API-[获取数据列表](1069-obtain-the-data-list.md)接口，可得到某一单据的数据列表信息。
