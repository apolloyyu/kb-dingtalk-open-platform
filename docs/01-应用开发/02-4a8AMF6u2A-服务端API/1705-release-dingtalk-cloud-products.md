---
title: "释放钉钉云产品"
source_url: "https://open.dingtalk.com/document/development/release-dingtalk-cloud-products"
namespace: "development"
slug: "release-dingtalk-cloud-products"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 释放钉钉云产品"
doc_id: "tGfLwMt8Rg"
updated_at: "2025-10-16 14:31:26"
---

> Source: https://open.dingtalk.com/document/development/release-dingtalk-cloud-products
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 释放钉钉云产品
> Updated: 2025-10-16 14:31:26

# 释放钉钉云产品

## 钉钉云产品释放资源

不同的钉钉云产品资源，释放资源方法不同。下表列出常见的云产品资源释放方法。

| **付费模式** | **云产品类型** | **释放资源流程** | **产品资源****示例** |
| --- | --- | --- | --- |
| 包年包月 | 所有云产品 | 在开发者后台提交申请，申请通过后在钉钉云（阿里云）中查看工单，按工单指引操作 | 包年包月付费的ECS |
| 按量付费 | RDS | 在开发者后台提交申请，申请通过后自动释放 | RDS |
| 非RDS的其他云产品 | 阿里云产品中进行释放 | 按量付费的ECS |

## 资源释放流程

## 包年包月的云产品资源释放

包年包月的云产品资源释放，需要在开发者后台提交审批单申请，申请通过后根据工单号在钉钉云（阿里云）中查看工单，按工单指引操作进行释放。产品释放后，剩余金额自动进入账户余额。包年包月的云产品的释放流程如下：

第一步，开发者登录[钉钉开发者后台](http://open-dev.dingtalk.com/)，点击应用开发-钉钉云-资源释放。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2775299951/p163374.png "image.png")

第二步，点击申请释放资源，填写相关信息，并提交申请。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2775299951/p163375.png "image.png")

第三步，申请通过后，查看申请详情，获取阿里云工单号

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3775299951/p163376.png "image.png")

第四步，登录钉钉云（阿里云）工单系统，根据工单号中查看工单，按工单指引操作进行释放。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3775299951/p163377.png "image.png")

## 按量付费的产品资源释放

**按量付费产品不同，释放操作路径不同，开发者以实际释放时的操作引导为准。**

### 按量付费的RDS释放

RDS资源释放，需要在开发者后台提交审批单申请，申请通过后自动释放。释放流程如下：

第一步，开发者登录[钉钉开发者后台](http://open-dev.dingtalk.com/)，点击应用开发-钉钉云。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3775299951/p163378.png "image.png")

第二步，点击登录控制台，找到对应RDS资源，将实例名改为WillRelease。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3775299951/p163379.png "image.png")

第三步，登录开发者后台，点击钉钉云-资源释放。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3775299951/p163380.png "image.png")

第四步，点击申请释放资源，填写相关内容，并点击提交。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3775299951/p163381.png "image.png")

第五步，申请通过后，资源可自动释放。

### 非RDS的其他云产品资源释放

按量付费的非RDS的云产品，在阿里云云产品中进行释放。以负载均衡资源释放为例，释放流程如下：

第一步，开发者登录[钉钉开发者后台](http://open-dev.dingtalk.com/)，点击应用开发-钉钉云-登录控制台。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4775299951/p163382.png "image.png")

第二步，在云产品中找到对应的负载均衡，点击“释放设置”。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4775299951/p163383.png "image.png")

第三步，选择释放行为进行释放。

**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4775299951/p163384.png "image.png")** ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4775299951/p163385.png "image.png")
