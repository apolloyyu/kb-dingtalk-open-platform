---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/jinzhi-crm-interface-call-description"
namespace: "development"
slug: "jinzhi-crm-interface-call-description"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 概述"
doc_id: "SrnbpYnIB0"
updated_at: "2026-07-20 09:25:34"
---

> Source: https://open.dingtalk.com/document/development/jinzhi-crm-interface-call-description
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 概述
> Updated: 2026-07-20 09:25:34

# 概述

本文介绍了金智CRM的核心功能、开通方式、接口能力以及接入方法，帮助开发者和企业用户快速了解并集成金智CRM系统。通过与钉钉开放平台深度集成，金智CRM提供覆盖客户全生命周期的一站式管理解决方案，支持企业实现销售、采购、生产、库存等业务环节的数字化协同。

## 什么是金智CRM

金智CRM客户全生命周期一站式解决方案，从获客接入开始收集销售线索，经过有效跟进将线索转换为客户或商机，通过销售流程规范销售过程，用拜访引导销售行为，最终达成交易并快速收款，完成端到端的智能客户管理。

金智CRM融合了进销存、生产、财务管理、工单以及数据智能分析，协助企业实时掌握经营状态，打造以数据为中心的实时决策企业。

金智CRM深度融合钉钉，贯穿流程管理以提高各个环节的自动化程度来缩短销售周期、降低销售成本 ，扩大销售量，增加收入与盈利，并最终从根本上提升企业的核心竞争力。

![金智CRM概述](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8154162261/p279426.png)

## 如何开通金智CRM

以PC端开通金智CRM为例：

钉钉PC客户端-工作台-右上角应用市场搜索**金智CRM**。![iShot2022-02-07 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9268055461/p397844.png)

## 开放概览

金智CRM提供了丰富的API接口能力，涵盖客户管理、销售机会、合同订单、采购生产等多个业务领域，支持企业实现跨系统数据同步与流程自动化。

金智CRM已通过钉钉开放平台对外开放其核心业务能力，适用于ISV（独立软件开发商）及企业自研开发者进行系统集成。

#### **客户**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [客户资料](1055-add-or-edit-customer-profile.md) | 新增或编辑客户资料。 | 新版 |
| [客户公共池](1056-add-or-edit-customer-public-pools.md) | 新增或编辑客户公共池。 | 新版 |

#### **联系人**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [联系人](1057-add-or-edit-contacts.md) | 新增或编辑联系人。 | 新版 |

#### **合同**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [合同订单](1058-add-or-edit-contract-orders.md) | 新增或编辑合同订单。 | 新版 |
| [发货单](1059-add-or-edit-invoices.md) | 新增或编辑发货单。 | 新版 |
| [销售换货单](1060-add-or-edit-a-sales-order.md) | 新增或编辑销售换货单。 | 新版 |

#### **销售**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [销售机会](1061-add-or-edit-opportunities.md) | 新增或编辑销售机会。 | 新版 |
| [报价记录](1062-add-or-edit-quotation-records.md) | 新增或编辑报价记录。 | 新版 |

#### **采购**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [采购单](1063-edit-purchase-order.md) | 新增或编辑采购单。 | 新版 |

#### **生产**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [生产单](1064-add-or-edit-a-production-order.md) | 新增或编辑生产单。 | 新版 |

#### **产品**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [产品信息](1065-add-or-edit-product-information.md) | 新增或编辑产品信息。 | 新版 |

#### **库存**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [入库单](1066-add-or-edit-a-shipment-record.md) | 新增或编辑入库单。 | 新版 |
| [出库单](1067-add-or-edit-an-issue-ticket.md) | 新增或编辑出库单。 | 新版 |

#### **数据**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取数据列表](1069-obtain-the-data-list.md) | 获取各种单据的列表数据。 | 新版 |
| [获取数据详情](1068-queries-data-details.md) | 获取各种单据的详情数据。 | 新版 |

## 开放教程

钉钉提供了金智CRM接口接入流程示例，请参见[制造业订单交付全过程管理](1054-management-of-order-delivery-in-the-manufacturing-industry.md)。

## 技术支持

如有在接入过程中遇到问题，可通过搜索群号**33973032**，加入**金智CRM接口咨询**群进行咨询。
