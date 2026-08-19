---
title: "三方工作台卡片集成连接器"
source_url: "https://open.dingtalk.com/document/dingstart/three-way-workbench-card-integration-connector"
namespace: "dingstart"
slug: "three-way-workbench-card-integration-connector"
group: "工作台"
tab: "使用教程"
breadcrumb: "合作伙伴教程 > 第三方低码组件 > 三方工作台卡片集成连接器"
doc_id: "KjPBYoNBBL"
updated_at: "2026-08-19 09:12:32"
---

> Source: https://open.dingtalk.com/document/dingstart/three-way-workbench-card-integration-connector
> Path: 工作台 / 使用教程 / 合作伙伴教程 > 第三方低码组件 > 三方工作台卡片集成连接器
> Updated: 2026-08-19 09:12:32

# 三方工作台卡片集成连接器

本文介绍以连接器为动态资源配置工作台卡片的流程。

## **准备工作**

- 企业已入驻为产品方案商，详情请参考[入驻成为产品方案商](../../01-应用开发/07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)。

## **步骤一：创建连接器**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 依次选择**开发能力 > 连接平台 > 连接器。**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532754.png)
3. 单击**创建连接器**，进入创建连接器页面，填写连接器名称和连接器描述，单击**确定**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p1095445.png)
4. > **[!NOTE]**
   >
   > APISecret如何配置，可参考[API Secret鉴权](../../02-连接平台/02-XdgyZifJkr-我的连接/0017-apissecret-authentication.md)介绍。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p1095446.png)

## **步骤二：配置连接器执行动作**

1. 在连接平台首页，选择**连接器**，然后在自建连接器下单击目标连接器。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532773.png)
2. ​在目标连接器基础信息页面，单击**执行动作**，然后单击**创建执行动作**。

   > **[!NOTE]**
   >
   > 执行动作的配置方法，请参考[添加执行动作](../../02-连接平台/02-XdgyZifJkr-我的连接/0012-add-execution-action-1.md)说明。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532780.png)​
3. 完成配置后，点击**发布**。

## **步骤三：创建卡片模板并配置变量**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，单击开放能力，选择卡片平台。

   ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1591017871/p514943.png)
2. 在模板列表页面，单击**新建模板**。

   ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514949.png)
3. 在新建模板页面，依照下列要求填写模板信息后，单击**创建**。

   - **模板名称：**该名称是该卡片在工作台上最终展示的名称。
   - **卡片类型：**选择工作台卡片。
   - **关联应用：**选择需要关联的应用，本文档介绍第三方工作台卡片，选择关联应用选择本企业创建的第三方企业应用（建议关联已上架到应用市场的第三方企业应用）。

     ![iShot2022-11-09 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515297.png)
4. 进入模板编辑页面，本文以**视频卡片**为例。

   - 在左侧数据源内，添加普通变量。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p1095450.png)
   - 在设计器中添加视频组件，右侧设置视频地址时，选择字符串变量。

     ![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514989.png)
   - 填写视频地址的变量字段名称。

     ![iShot2022-12-12 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9706190761/p533779.png)
   - 设置视频的封面。

     ![iShot2022-11-09 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515298.png)
5. 依照上述步骤设置完成后，在右上角依次单击**保存**和**发布**。

## **步骤四：创建动态数据源工作台卡片实例**

1. 单击**卡片实例管理**。

   ![iShot2022-12-08 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9706190761/p532266.png)
2. 单击**创建卡片实例**。

   ![iShot2022-12-08 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9706190761/p532267.png)
3. 在实例创建页面，创建数据源时选择**开放平台连接器数据源**。

   ![iShot2022-12-08 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532268.png)
4. 在新增数据源页面，依照下列要求填写后，单击**新增**。

   - **连接器：**选择连接器。
   - **执行动作：**选择执行动作。
   - **数据拉取策略：**选择数据拉取策略。

   ![iShot2022-12-08 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9706190761/p532270.png)
5. 完成数据配置，每个变量的数据类型都选择动态数据。每个变量的数据选择与其对应的执行动作出参字段。

   ![iShot2022-12-08 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532274.png)
6. 完成工作台场域配置后，单击**创建实例**。

   ![iShot2022-12-08 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9706190761/p532279.png)

## **步骤五：投放卡片实例**

1. 在工作台模板的实例列表页面，选择需要投放的实例，单击**投放**。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1591017871/p516025.png)
2. 在投放页面，依照下列要求，填写投放配置信息，单击**投放**。

   - **插件名称：**自动生成，与卡片模板名称保持一致。
   - **组件名称：**自动生成。
   - **组件图标：**上传卡片在工作台展示时左上角的图标。
   - **预览图：**上传卡片效果的预览图片。

     ![iShot2022-11-24 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1591017871/p524172.png)

## **步骤六：工作台卡片编辑和发布**

卡片实例投放后，点击提醒内的**点击这里**，进入工作台卡片的编辑和发布页面。

1. 在插件管理页面，查看创建的卡片实例，目前为已上架状态。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1591017871/p516029.png)
2. 已上架状态的插件，需要经过产品验收审核后才能正常使用。提交组件验收申请，请参考[组件上架和审核](0024-step-3-component-shelf-and-review.md)。
3. 组件验收申请通过后，卡片实例状态变更为验收通过，单击**版本管理**。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1591017871/p516036.png)
4. 在卡片实例详情页面，需要先设置卡片的灰度企业，然后可以全量发布。

   ![iShot2022-11-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1591017871/p516041.png)
