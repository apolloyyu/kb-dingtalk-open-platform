---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/honorary-product-introduction"
namespace: "development"
slug: "honorary-product-introduction"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 荣誉 > 概述"
doc_id: "lws0PHA96h"
updated_at: "2026-07-20 09:25:26"
---

> Source: https://open.dingtalk.com/document/development/honorary-product-introduction
> Path: 应用开发 / 服务端API / 企业文化 > 荣誉 > 概述
> Updated: 2026-07-20 09:25:26

# 概述

本文介绍了什么是荣誉产品、如何开通荣誉和名词解释。

## 荣誉介绍

组织荣誉是钉钉为企业提供的组织文化解决方案，目的是在线公开激励员工。管理员创建并颁发荣誉，同时将荣誉同步到全员群、部门群中，以此鼓励优秀员工，树立标杆榜样。 更多功能介绍，请参见[钉钉使用手册-荣誉](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/AzXEvLlGD39WeAoqjy66W2j4OkP01ZYR)。

![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6270154871/p436531.png)

## 如何开通荣誉

管理员可以通过钉钉移动端或PC端开通荣誉应用，开通后在工作台打开应用并使用。

已PC端开通为例：

**开通路径一：应用中心**

步骤一：打开钉钉PC端，单击**工作台**。

步骤二：在工作台页面，单击**应用中心**。

步骤三：在应用中心页面，在**搜索框**输入荣誉。

步骤四：单击搜索出的**荣誉**应用。

步骤五：在荣誉产品详情页，单击**免费开通**。

![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6270154871/p436542.png)

![7](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6270154871/p436489.png)**开通路径二：全局搜索**

步骤一：打开钉钉PC端，在**搜索框**搜索荣誉。

步骤二：单击搜索出的**荣誉**应用。

步骤三：在荣誉产品详情页，单击**免费开通**。![9](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6270154871/p436495.png)

![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6270154871/p436910.png)

## 开放概览

### **开放接口列表**

荣誉提供了丰富的接口开放能力，开发者通过API接口可以实现荣誉和企业业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询当前企业下可颁发的荣誉列表](0976-query-the-list-of-honors-that-can-be-issued-under.md) | 查询当前企业下可颁发的荣誉列表。 | 新版 |
| [给员工颁发荣誉](0974-award-of-honor.md) | 用于给组织内的员工颁发荣誉。 | 新版 |
| [创建荣誉勋章模板](0977-create-medal-of-honor-template.md) | 创建荣誉模板。 | 新版 |
| [撤销员工获得的荣誉勋章](0978-revoke-an-employee-s-medal-of-honor.md) | 撤销员工的荣誉勋章。 | 新版 |
| [查询员工已获得的组织荣誉](0975-check-the-honors-that-an-employee-has-received.md) | 查询某个员工获得的组织荣誉记录。 | 新版 |

### **回调事件列表**

荣誉支持荣誉授予、荣誉审核结果回调事件。

- [荣誉授予](../04-LFcRvVD08N-事件订阅/0183-honor-confer.md)
- [荣誉审核结果](../04-LFcRvVD08N-事件订阅/0184-honor-review-results.md)

## 名词解释

### 荣誉信息列表（openHonors）

企业下可颁发的荣誉信息列表，定义为openHonors。

![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6270154871/p436544.png)

### 荣誉名字（honorName）

荣誉名字，定义为honorName。
