---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-travel"
namespace: "development"
slug: "overview-travel"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 概述"
doc_id: "05Zg7FWMdN"
updated_at: "2026-07-20 09:25:32"
---

> Source: https://open.dingtalk.com/document/development/overview-travel
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 概述
> Updated: 2026-07-20 09:25:32

# 概述

本文介绍了什么是阿里商旅，阿里商旅的接入方式，阿里商旅接口能力，以及如何接入阿里商旅接口能力。

## 什么是阿里商旅

阿里商旅深度融合钉钉，为企业提供一站式数智化商旅综合解决方案，助力企业降本增效，合规透明，提升员工出差体验，提升财务行政工作效率。

阿里商旅是基于行业的数智化差旅管理系统，为企业提供机酒车的预订和全流程管控服务。

将传统企业出差前的差旅申请、审批，出差中的预订、退改签、发票，及出差后的报销、账务等全流程，实现数智化升级，轻松实现员工免垫资免报销，统一对公支付，财务人员无需核验海量报销凭证，节省大量人工成本。

同时7\*24\*365的人工客服坐席，供全天候的服务保障，在实现差旅合规的同时，极大的提升了企业差旅体验。![产品图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2885520461/p375296.png)

## 如何开通阿里商旅

你可以使用手机钉钉扫描以下二维码开通阿里商旅。

![接入二维码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2885520461/p375318.png)

## 如何接入

### 对接流程

![对接图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2885520461/p375320.png)

### 对接方式

![对接方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2885520461/p375321.png)

### 使用流程

![对接后使用流程 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2885520461/p375324.png)

## 开放概览

阿里商旅提供了丰富的接口开放能力，开发者通过API接口可以实现阿里商旅和企业业务系统打通。

#### **城市基本数据**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [机票城市搜索](1012-air-ticket-city-search.md) | 搜索火车票城市。 | 旧版 |
| [火车票城市搜索](1013-train-ticket-city-search.md) | 搜索机票城市。 | 旧版 |

#### **维护成本中心和发票抬头**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新建成本中心](1014-new-cost-center.md) | 新建成本中心。 | 旧版 |
| [修改成本中心](1015-modify-basic-cost-center-information.md) | 修改成本中心基本信息。 | 旧版 |
| [删除成本中心](1016-delete-cost-center.md) | 删除成本中心。 | 旧版 |
| [查询成本中心](1017-query-cost-center.md) | 查询成本中心信息。 | 旧版 |
| [设置成本中心人员信息](1018-set-up-cost-center-personnel-information.md) | 设置成本中心人员信息。 | 旧版 |
| [删除成本中心人员信息](1019-delete-the-personnel-information-of-the-cost-center.md) | 删除成本中心人员信息。 | 旧版 |
| [商旅成本中心转换为外部成本中心](1020-business-travel-cost-center-converted-to-external-cost-center.md) | 商旅成本中心转换为外部成本中心。 | 旧版 |

#### **项目管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [添加项目](1021-add-a-project.md) | 添加商旅项目。 | 旧版 |
| [修改项目](1022-project-change.md) | 修改项目信息。 | 旧版 |
| [删除项目](1023-delete-a-project.md) | 删除项目。 | 旧版 |

#### **出差申请**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新建审批单](1024-user-new-approval-form.md) | 新建审批单。 | 旧版 |
| [获取申请单列表](1025-search-enterprise-approval-form-data.md) | 查询企业审批单数据。 | 旧版 |
| [获取申请单详情](1026-obtains-the-detailed-data-of-a-single-request.md) | 获取单个申请单的详细信息。 | 旧版 |
| [修改申请单](1027-user-modify-approval-form.md) | 修改出差申请单。 | 旧版 |
| [更新申请单状态](1028-update-approval-form.md) | 更新审批单状态。 | 旧版 |
| [搜索第三方酒店超标审批单](1029-dingtalk-oapi-alitrip-btrip-exceedapply-hotel-get.md) | 搜索第三方酒店超标审批单。 | 旧版 |
| [搜索第三方火车票超标审批单](1030-dingtalk-oapi-alitrip-btrip-exceedapply-train-get.md) | 搜索第三方火车票超标审批单。 | 旧版 |
| [回传第三方超标审批结果](1031-dingtalk-oapi-alitrip-btrip-exceedapply-sync.md) | 回传第三方超标审批结果。 | 旧版 |
| [搜索第三方机票超标审批单](1032-dingtalk-oapi-alitrip-btrip-exceedapply-flight.md) | 搜索第三方机票的超标审批单。 | 旧版 |

#### **订单管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取企业机票订单数据](1033-obtains-enterprise-ticket-order-data.md) | 获取企业机票订单数据 | 旧版 |
| [获取企业商旅酒店订单数据](1034-enterprises-obtain-order-data-for-business-hotels.md) | 获取商旅酒店订单数据。 | 旧版 |
| [获取企业火车票订单数据](1035-obtains-the-enterprise-train-ticket-order-data.md) | 获取企业火车票订单数据。 | 旧版 |
| [获取用车订单数据](1036-vehicle-order-query-interface.md) | 获取企业用车订单数据。 | 旧版 |
| [关联单号查询相关订单信息列表](1037-related-order-information.md) | 申请单中关联单号获取订单信息。 | 新版 |

#### **阿里商旅跳转链接**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取商旅访问地址](1038-obtain-business-travel-access-addresses.md) | 获取各个场景预订访问地址，以及我的订单地址。 | 旧版 |

#### **发票管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新增发票配置](1039-new-invoice-configuration.md) | 新增发票配置。 | 旧版 |
| [配置发票适用人群](1040-configure-invoice-users.md) | 配置发票适用人群。 | 旧版 |
| [查询可用发票列表](1041-query-available-invoices.md) | 查询可用发票列表。 | 旧版 |
| [修改发票配置](1042-modify-invoice-configuration.md) | 修改发票配置。 | 旧版 |
| [删除发票信息](1043-delete-invoice-information.md) | 删除发票信息。 | 旧版 |

#### **市内用车申请**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [同步市内用车申请单](1044-synchronize-third-party-city-vehicle-approval-form.md) | 同步市内用车申请单。 | 新版 |
| [审批市内用车申请单](1045-approval-of-third-party-city-car-application-form.md) | 审批市内用车申请单。 | 新版 |
| [查询市内用车申请单](1046-query-the-application-form-for-third-party-vehicles-in-the-city.md) | 查询市内用车申请单。 | 新版 |

#### **账单管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询用车结算记账记录](1047-query-interface-for-vehicle-settlement-and-bookkeeping.md) | 查询商旅用车的结算记账数据。 | 新版 |
| [查询商旅火车票结算记账数据](1048-business-travel-train-ticket-settlement-bookkeeping-query-interface.md) | 查询商旅火车票结算记账数据。 | 新版 |
| [查询酒店结算记账数据](1049-hotel-settlement-bookkeeping-query-interface.md) | 查询商旅酒店结算记账数据。 | 新版 |
| [查询机票结算记账数据](1050-ticket-settlement-bookkeeping-query-interface.md) | 查询机票结算记账数据。 | 新版 |
| [获取月对账结算数据](1051-obtain-monthly-reconciliation-settlement-data.md) | 获取月对账结算数据下载地址。 | 旧版 |

#### **预估价**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询预估价](1052-query-estimated-price.md) | 查询预估价。 | 旧版 |

## 技术支持

如果在接入过程中遇到问题，请联系分配给贵司的阿里商旅专属客户经理，我们将提供专业的技术支持协助对接。
