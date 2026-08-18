---
title: "三方 工作台卡片的创建和使用"
source_url: "https://open.dingtalk.com/document/dingstart/creation-and-use-of-tripartite-ecological-cards"
namespace: "dingstart"
slug: "creation-and-use-of-tripartite-ecological-cards"
group: "工作台"
tab: "使用教程"
breadcrumb: "合作伙伴教程 > 第三方低码组件 > 三方工作台卡片的创建和使用"
doc_id: "N8U3QbfS48"
updated_at: "2025-09-03 15:57:17"
---

> Source: https://open.dingtalk.com/document/dingstart/creation-and-use-of-tripartite-ecological-cards
> Path: 工作台 / 使用教程 / 合作伙伴教程 > 第三方低码组件 > 三方工作台卡片的创建和使用
> Updated: 2025-09-03 15:57:17

# 三方工作台卡片的创建和使用

本文档介绍三方工作台卡片的创建并配置使用流程。

> **[!NOTE]**
>
> 授权企业如果开通了三方工作台卡片关联的应用，该授权企业就可以在企业工作台添加该卡片。

## **准备工作**

- 企业已入驻为产品方案商，详情请参考[入驻成为产品方案商](../../01-应用开发/07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)。

## **什么是工作台卡片**

在工作台中，工作台卡片是非常重要的帮助应用功能与场域融合的能力。通过工作台卡片，你的应用可以通过一个卡片将部分数据和功能提供给用户，与用户直接产生互动。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p521777.png)

## **工作台卡片特性**

### **特性1：丰富工作台组件物料**

工作台卡片通过集成低代码搭建器、数据资产平台、连接器等能力，可以以可视化的方式来实现业务场景的快速酷化方案，借助钉钉强大的底层团队的PaaS能力、配置能力、集成能力，极大丰富了工作台组件物料。

**示例1：**通过和数据资产平台的打通可以直接给出业务信息透传、组织经营情况、异常指标等，并在工作台以自定义的形式展现用户关心的核心数据。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p521782.png)

**示例2**：通过和连接器的打通，可以将用户组织内部的一些数据，通过工作台卡片展示到组织工作台，且展示形式可以由用户自主定义，充分满足用户的各类工作台组件定制化需求。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p521792.png)

### **特性2：开发门槛较低且开发时间短**

在之前的版本中用户需要通过全码开发的方式，将一些组织自定义的组件发布到工作台上。对比全码开发，卡片属于低代码开发，用户可通过卡片设计器简单的拖、拉、拽操作，创建一个能够在工作台使用的组件，开发门槛较低且开发时间短。

### **特性3：无需额外适配**

工作台卡片与其他场域卡片无使用形式上的区别，之前创建过卡片的用户可快速将存量卡片发布到工作台使用，不需要做额外的适配。

## **步骤一：创建三方工作台卡片模板**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，单击开放能力，选择卡片平台。

   ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p514943.png)
2. 在模板列表页面，单击**新建模板**。![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p514949.png)
3. 在新建模板页面，依照下列要求填写模板信息后，单击**创建**。

   - **模板名称：**该名称是该卡片在工作台上最终展示的名称。
   - **卡片类型：**选择工作台卡片。
   - **关联应用：**选择需要关联的应用，本文档介绍第三方工作台卡片，选择关联应用选择本企业创建的第三方企业应用（建议关联已上架到应用市场的第三方企业应用）。

     ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516009.png)
4. 进入模板编辑页面，本文以**创建静态数据源视频卡片**为例。

   - 左侧组件库内，将视频组件拖拽至设计器。

     ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516012.png)
   - 设计器中单击视频组件，右侧设置视频地址时，选择**快捷创建新变量**。

     ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516014.png)
   - 填写视频地址的变量字段名称。

     ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516016.png)
   - 可以设置视频的封面。![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516018.png)
   - 依照上述步骤设置完成后，在右上角依次单击**保存**和**发布**。

## **步骤二：创建第三方工作台卡片实例**

1. 工作台卡片模板单击保存和发布后，单击右上角**卡片实例管理**。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516020.png)
2. 在实例列表页面，单击**创建卡片实例**。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516021.png)
3. 在实例创建页面，依照下列要求完成卡片实例的配置，并单击右下角的**创建实例**。

   - **数据配置：**选择静态数据类型，并填写需要展示的视频链接。
   - **新增场域：**选择工作台。![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516024.png)

## **步骤三：投放卡片实例**

1. 在工作台模板的实例列表页面，选择需要投放的实例，单击**投放**。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516025.png)
2. 在投放页面，依照下列要求，填写投放配置信息，单击**投放**。

   - **插件名称：**自动生成，与卡片模板名称保持一致。
   - **组件名称：**自动生成。
   - **组件图标：**上传卡片在工作台展示时左上角的图标。
   - **预览图：**上传卡片效果的预览图片。![iShot2022-11-24 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6062439661/p524172.png)

## **步骤四：工作台卡片编辑和发布**

卡片实例投放后，点击提醒内的**点击这里**，进入工作台卡片的编辑和发布页面。

1. 在插件管理页面，查看创建的卡片实例，目前为已上架状态。![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516029.png)
2. 已上架状态的插件，需要经过产品验收审核后才能正常使用。提交组件验收申请，请参考[组件上架和审核](https://open.dingtalk.com/document/dashboard/component-installation-and-review)。
3. 组件验收申请通过后，卡片实例状态变更为验收通过，单击**版本管理**。![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516036.png)
4. 在卡片实例详情页面，需要先设置卡片的灰度企业，然后可以全量发布。![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516041.png)

## **步骤五：查看效果**

授权开通了该第三方卡片绑定的第三方企业应用的企业，按照以下步骤可添加该第三方卡片组件到工作台。

> **[!NOTE]**
>
> - 工作台卡片设置灰度或者全量发布后，授权企业需要等待五分钟左右在组件中心内才可以查看。
> - 当前第三方工作台卡片默认分类归属于酷应用。

1. 在本企业钉钉工作台最下方，单击添加组件。![iShot2022-11-11 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516394.png)
2. 在组件中心页面，找到该第三方工作台卡片，单击右上角**管理**，单击**添加到工作台**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2804529661/p516514.png)

## **技术支持**

若您在创建工作台卡片中遇到问题，欢迎扫描下方二维码进入答疑群咨询。

![iShot2022-11-11 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p516397.png)
