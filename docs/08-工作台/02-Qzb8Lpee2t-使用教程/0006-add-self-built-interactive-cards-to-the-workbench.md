---
title: "自建 工作台卡片的创建和使用"
source_url: "https://open.dingtalk.com/document/dingstart/add-self-built-interactive-cards-to-the-workbench"
namespace: "dingstart"
slug: "add-self-built-interactive-cards-to-the-workbench"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 低码组件 > 自建工作台卡片的创建和使用"
doc_id: "5p2alsFzF1"
updated_at: "2026-08-18 09:12:06"
---

> Source: https://open.dingtalk.com/document/dingstart/add-self-built-interactive-cards-to-the-workbench
> Path: 工作台 / 使用教程 / 组件教程 > 低码组件 > 自建工作台卡片的创建和使用
> Updated: 2026-08-18 09:12:06

# 自建工作台卡片的创建和使用

本文档介绍企业自建工作台卡片的创建和配置使用流程。

> **[!NOTE]**
>
> 自建工作台卡片，只能由当前组织使用，不能给其他企业使用。

## **什么是工作台卡片**

在钉钉工作台内，工作台卡片是非常重要的帮助应用功能与场域融合的能力。通过工作台卡片，你的应用可以通过一个卡片将部分数据和功能提供给用户，与用户直接产生互动。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0329998661/p521777.png)

## **工作台卡片特性**

### **工作台组件物料丰富**

工作台卡片通过集成低代码搭建器、数据资产平台、连接器等能力，可以以可视化的方式来实现业务场景的快速酷化方案，借助钉钉强大的底层团队的PaaS能力、配置能力、集成能力，极大丰富了工作台组件物料。

**示例1：**通过和数据资产平台的打通可以直接给出业务信息透传、组织经营情况、异常指标等，并在工作台以自定义的形式展现用户关心的核心数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p521782.png)

**示例2**：通过和连接器的打通，可以将用户组织内部的一些数据，通过工作台卡片展示到组织工作台，且展示形式可以由用户自主定义，充分满足用户的各类工作台组件定制化需求。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p521792.png)

### **开发门槛较低且时间短**

在之前的版本中用户需要通过全码开发的方式，将一些组织自定义的组件发布到工作台上。对比全码开发，卡片属于低代码开发，用户可通过卡片设计器简单的拖、拉、拽操作，创建一个能够在工作台使用的组件，开发门槛较低且开发时间短。

### **无需额外适配**

工作台卡片与其他场域卡片无使用形式上的区别，之前创建过卡片的用户可快速将存量卡片发布到工作台使用，不需要做额外的适配。

## **准备工作**

企业拥有自定义工作台的能力，需要申请开通钉钉专业版或者钉钉专属版功能。具体可在[钉钉管理后台](https://oa.dingtalk.com/) **> 自定义工作台**中咨询。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p516474.png)

## **操作步骤**

### **步骤一：创建工作台卡片模板**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，单击**开放能力**，选择**卡片平台**。

   ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514943.png)
2. 在**模板列表**页面，单击**新建模板**。

   ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514949.png)
3. 在新建模板页面，依照下列要求填写模板信息后，单击**创建**。

   - **模板名称：**自建工作台卡片，是该卡片在工作台上最终展示的名称。
   - **卡片类型：**选择工作台卡片。
   - **关联应用：**选择需要关联的应用，本文档介绍企业自建工作台卡片，关联应用选择本企业创建的企业内部应用即可。

     ![iShot2022-11-09 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515297.png)
4. 进入模板编辑页面，本文以**创建静态数据源视频卡片**为例。

   - 在左侧组件库内，将视频组件拖拽至设计器。

     ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514987.png)
   - 在设计器中单击视频组件，右侧设置视频地址时，选择**快捷创建新变量**。

     ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514989.png)
   - 填写视频地址的变量字段名称。

     ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514993.png)
   - 设置视频的封面。

     ![iShot2022-11-09 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515298.png)
   - 依照上述步骤设置完成后，在右上角依次单击**保存**和**发布**。

### **步骤二：创建工作台卡片实例**

1. 工作台卡片模板单击保存和发布后，单击右上角**卡片实例管理**。

   ![iShot2022-11-09 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515301.png)
2. 在实例列表页面，单击**创建卡片实例**。

   ![iShot2022-11-09 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515302.png)
3. 在实例创建页面，依照下列要求完成卡片实例的配置，并单击右下角的**创建实例**。

   - **数据配置：**选择静态数据类型，并填写需要展示的视频链接。
   - **新增场域：**选择工作台。![iShot2022-11-09 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515304.png)

### **步骤三：投放卡片实例**

1. 在工作台模板的实例列表页面，选择需要投放的实例，单击**投放**。

   ![iShot2022-11-09 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515318.png)
2. 在投放页面，依照下列要求，填写投放配置信息，单击**投放**。

   - **插件名称：**自动生成，与卡片模板名称保持一致。
   - **组件名称：**自动生成。
   - **组件图标：**上传卡片在工作台展示时左上角的图标。
   - **预览图：**上传卡片效果的预览图片。

     ![iShot2022-11-24 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p524098.png)

### **步骤四：工作台卡片编辑和发布**

卡片实例投放后，点击提醒内的**点击这里**，进入工作台卡片管理编辑页面。

1. 在插件管理页面，查看创建的卡片实例，单击卡片实例的版本管理。

   ![iShot2022-11-09 13](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515358.png)
2. 在卡片实例详情页面，可以设置插件的灰度企业，灰度设置完成后可以将卡片实例全量发布。

   ![iShot2022-11-09 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515360.png)
3. 卡片实例全量发布后，在工作台管理中，创建自定义工作台。

   ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515366.png)
4. 编辑自定义工作台，使用创建的工作台卡片实例。

   - 单击**查看详情**，查看自定义工作台详情。![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515370.png)
   - 单击配置工作台，进入工作台设计器。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515371.png)
   - 在工作台设计器页面，单击左上角**新建页面**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515372.png)
   - 在左侧组件库的自建组件库中，将卡片实例拖拽至目标位置。

     ![iShot2022-11-11 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p516247.png)
   - 在设计器右上角分别单击**保存**和**更新**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515375.png)
   - 在自定义工作台页面，单击**发布工作台**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515376.png)
   - 在选择发布范围页面，设置工作台可见范围，单击**发布**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515377.png)

### **步骤五：查看效果**

在自定义工作台发布可见范围内的员工，通过钉钉客户端切换当前企业工作台，查看的效果如下图所示。![iShot2022-11-11 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p516266.png)
