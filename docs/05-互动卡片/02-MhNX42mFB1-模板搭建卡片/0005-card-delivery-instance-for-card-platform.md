---
title: "卡片平台投放卡片实例"
source_url: "https://open.dingtalk.com/document/development/card-delivery-instance-for-card-platform"
namespace: "development"
slug: "card-delivery-instance-for-card-platform"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "快速入门 > 卡片投放 > 卡片平台投放卡片实例"
doc_id: "7ZFaTJNJCw"
updated_at: "2026-08-04 09:07:23"
---

> Source: https://open.dingtalk.com/document/development/card-delivery-instance-for-card-platform
> Path: 互动卡片 / 模板搭建卡片 / 快速入门 > 卡片投放 > 卡片平台投放卡片实例
> Updated: 2026-08-04 09:07:23

# 卡片平台投放卡片实例

通过本文你将了解到如何在卡片平台上将卡片实例投放到不同的场域中。

## **核心概念**

卡片投放赋予了卡片在各场域中流通的能力，可以将你创建的卡片和钉钉结合起来。目前卡片平台支持向**工作台**、**IM** 和**吊顶场景**投放卡片。

## **前置准备**

在投放卡片实例之前，确保你已经完成了以下工作：

- 在卡片平台上完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)。
- 在卡片平台上完成[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)。

## **步骤一：进入卡片实例管理**

1. 登录[开发者后台 > 卡片平台](https://open-dev.dingtalk.com/fe/card)。
2. 选择一张已发布的卡片， 点击「查看」进入卡片模板搭建页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p549118.png)
3. 点击右上角「卡片实例管理」按钮，即可进入卡片实例管理页面。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0465085871/p521498.png)

## **步骤二：选择卡片实例**

进入卡片实例管理页面后，在「卡片实例」栏目中可以查看历史创建的卡片实例列表。选择你需要投放的卡片实例并点击如图的「投放」按钮及可进入「卡片投放」界面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p523795.png)

## **步骤三：投放到特定场域**

在**卡片投放**界面中点击「新增投放配置」，并选择需要投放的场域，完成场域配置表单的填写即可将卡片投放到对应的场域中。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p523796.png)

### **工作台场域**

工作台卡片可以被投放到钉钉工作台中。同时，结合数据资产平台、连接器平台等 PaaS 能力可以快速地将企业自身的业务流程、数据与卡片结合， 打造企业自定义的工作台。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p525105.png)

下图所示为实际效果：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p525115.png)

> **[!NOTE]**
>
> 更多详细信息可参考文档 [自建工作台卡片的创建和使用](../../08-工作台/02-Qzb8Lpee2t-使用教程/0006-add-self-built-interactive-cards-to-the-workbench.md)。

### **IM 场域**

对于 IM 场域卡片平台默认会将卡片实例投放到「钉钉卡片助手」会话中。以下图所示卡片实例为例：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p523767.png)

只需在「卡片投放」界面中新增投放配置并选择 IM 场域。卡片平台将自动完成参数的配置，无需额外填写其他参数，之后点击投放按钮即可完成在 IM 场域的投放

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p539884.png)

下图所示为投放的效果：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p549135.png)

### **吊顶场域**

对于吊顶场域卡片平台默认会将卡片实例投放到「钉钉卡片助手」会话中。以下图所示卡片实例为例

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p523806.png)

只需在「卡片投放」界面中新增投放配置并选择吊顶场域。然后完成场域相关的配置，之后点击投放按钮即可完成在吊顶场域的投放

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p543036.png)

> **[!NOTE]**
>
> 吊顶过期时间表示投放的卡片会在所选时间之后自动关闭。

下图所示为投放效果：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8582293761/p549156.png)
