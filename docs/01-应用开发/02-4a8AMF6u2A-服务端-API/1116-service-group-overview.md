---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/service-group-overview"
namespace: "development"
slug: "service-group-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 概述"
doc_id: "8kmatELKJA"
updated_at: "2026-07-20 09:25:37"
---

> Source: https://open.dingtalk.com/document/development/service-group-overview
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 服务群 > 概述
> Updated: 2026-07-20 09:25:37

# 概述

本文档介绍什么是服务群，如何开通服务群，服务群开放了哪些接口能力，以及如何接入服务群能力等。

## 什么是服务群

**服务群**是一款面向钉钉企业的**多群运营工具**，主要包含自动建群、群分组等功能。更多功能介绍请参考[服务群产品介绍](https://www.yuque.com/em8gt4/yiaqxm)。

![222](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7370154871/p449297.png)

## 使用场景

钉钉服务群主要适用于以下场景：

- 自动为客户建群建立长期关系的场景。例如，线上网站/APP的链接，线下海报/宣传册等。
- 有群发通知，运营活动，分析数据的场景。
- 需要提升群服务效率以及记录和评估客户服务质量满意度的场景。
- 及时发现群内客户问题和情绪的场景。

## 如何开通服务群

以PC端开通服务群为例：

步骤一：打开钉钉PC端，单击**工作台**。

步骤二：在工作台页面，单击**应用中心**。

步骤三：在应用中心页面，在**搜索框**输入**智能服务群**。

步骤四：单击搜索出的**智能服务群**应用。

步骤五：在**智能服务群**产品详情页，单击**免费开通**。

![PC端1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7370154871/p449326.png)

![PC端2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7370154871/p449327.png)

## 开放概览

### **开放接口列表**

服务群提供了丰富的接口开放能力，开发者通过API接口可以实现服务群和企业业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [群发任务](1118-service-group-sending-task-interface.md) | 新增群发任务。 | 新版 |
| [创建场景服务群](1120-create-a-scenario-service-group.md) | 创建场景服务群。 | 新版 |
| [更换服务群所在的群分组](1123-modify-a-service-group.md) | 更换服务群所在的群分组。 | 新版 |
| [添加服务群成员](1121-add-service-group-members.md) | 将企业下成员添加到智能服务群中。 | 新版 |
| [发送服务群消息](1119-service-group-message-sending-interface.md) | 发送服务群消息。 | 新版 |
| [查询服务群活跃用户](1122-queries-active-service-users.md) | 获取指定服务群内近期活跃的用户。 | 新版 |
| [升级云客服服务群为钉钉智能服务群](1125-upgraded-the-cloud-customer-service-group-to-the-dingtalk-intelligent.md) | 将智能云客服下的服务群，升级为智能服务群中的服务群。 | 新版 |
| [升级普通群为服务群](1124-a-dingtalk-group-is-upgraded-to-one-of-the-intelligent.md) | 将企业内部群、普通群，升级为智能服务群中的服务群。 | 新版 |

### **回调事件列表**

服务群支持群信息变更、联系人关联客户、入群表单保存及服务群工单等多种回调事件，更多事件参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## 使用教程

钉钉提供了服务群接口接入流程示例，请参见[实现服务群发送消息](1117-enable-the-service-group-to-send-messages.md)。

## **服务支持**

服务群产品使用、合作、API 对接等相关事宜，可通过钉钉扫描下方二维码入群咨询：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3097393571/p992137.png)
