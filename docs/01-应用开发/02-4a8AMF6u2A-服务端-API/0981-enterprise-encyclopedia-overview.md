---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/enterprise-encyclopedia-overview"
namespace: "development"
slug: "enterprise-encyclopedia-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "企业文化 > 企业百科 > 概述"
doc_id: "3Lobj00Phr"
updated_at: "2026-07-20 09:25:28"
---

> Source: https://open.dingtalk.com/document/development/enterprise-encyclopedia-overview
> Path: 应用开发 / 服务端 API / 企业文化 > 企业百科 > 概述
> Updated: 2026-07-20 09:25:28

# 概述

本文介绍了企业百科的功能，如何开通企业百科等内容，以及企业百科接口能力等内容。

## 什么是企业百科

企业百科是一部企业信息高效汇聚和传递的百科全书。更多功能介绍，请参见[钉钉使用手册-企业百科](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmb5raajaqLXLq?dontjump=true%23%23)。

- 将企业内具有特定意义的信息（企业专用名词、行业用语、缩写词等），提炼为“词条”收录到“企业百科”，有效降低知识的获取成本，有利于企业知识高速汇聚。
- 在聊天窗口中提及百科词条，会有下滑实线引导，点击跳转到对应的“词条卡片”，查看并了解相关信息，让知识流转更高效。

  ![企业百科概述-词条示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8270154871/p427490.png)

## **如何开通企业百科**

开发者可以通过钉钉移动端或PC端开通企业百科应用，开通后在工作台打开应用并使用。

以PC端开通企业百科为例：

步骤一：打开钉钉PC端，单击**工作台**。

步骤二：在工作台页面，单击**应用中心**。

步骤三：在应用中心页面，在**搜索框**输入企业百科。

步骤四：单击搜索出的**企业百科**应用。

步骤五：在企业百科产品详情页，单击**免费开通**。

![lALPJxf-wlZKbgPNBOHNB9s_2011_1249](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6395049461/p427803.jpg)

![lALPJwY7SR5p7h_NBLnNB9U_2005_1209](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5395049461/p427804.jpg)

## 开放概览

企业百科API基于钉钉企业百科功能开放了根据词条名称获取词条释义、匹配文本中的词条等能力，开发者能以应用身份调用企业百科 API 操作对应数据。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新增词条](0982-new-entry.md) | 新增企业词条。 | 新版 |
| [审核词条](0983-review-entries.md) | 同意或拒绝新增词条。 | 新版 |
| [根据词条ID查询详情](0985-query-entry.md) | 根据词条ID查询词条的详情信息。 | 新版 |
| [更新词条](0986-update-entry.md) | 更新已审核通过的词条信息。 | 新版 |
| [删除词条](0987-delete-entry.md) | 删除企业词条。 | 新版 |
| [分页获取企业词条信息](0988-entry-search.md) | 分页获取企业词条信息。 | 新版 |
| [匹配文本中的词条](0989-enterprise-encyclopedia-match-entries-in-a-text.md) | 将文本与企业词条进行匹配，获取与词条全称或别名相同的文本内容。 | 新版 |
| [查询词条详情](0984-enterprise-encyclopedia-query-entry-details-by-entry-name.md) | 根据词条名称查询该词条相关详情信息。 | 新版 |

## 名词解释

- **词条名称**：包括词条的名称、全称以及别名。
- **词条释义**：词条的含义阐释。
- **相关应用**：词条相关的应用，可一键跳转。
- **相关文档**：词条相关的说明文档、使用指南等，可一键跳转。
- **相关链接**：词条相关的产品入口、网页链接、参考文献等，可一键跳转。
- **相关联系人**：与当前词条内容有关联的联系人，一键可查看联系人的个人主页。
- **词条编辑者**：词条最近编辑者信息，一键可查看编辑者的个人主页。

词条相关信息如下图所示。

![企业百科-名词解释-词条示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3474049461/p427519.png)
