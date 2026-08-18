---
title: "自建工作台卡片集成连接器"
source_url: "https://open.dingtalk.com/document/dingstart/self-built-workbench-card-integrated-connector"
namespace: "dingstart"
slug: "self-built-workbench-card-integrated-connector"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 低码组件 > 自建工作台卡片集成连接器"
doc_id: "IuMdzCXeUW"
updated_at: "2026-08-18 09:12:07"
---

> Source: https://open.dingtalk.com/document/dingstart/self-built-workbench-card-integrated-connector
> Path: 工作台 / 使用教程 / 组件教程 > 低码组件 > 自建工作台卡片集成连接器
> Updated: 2026-08-18 09:12:07

# 自建工作台卡片集成连接器

本文介绍以连接器为动态资源配置工作台卡片的流程。

## **准备工作**

企业拥有自定义工作台的能力，需要申请开通钉钉专业版或者钉钉专属版功能。具体可在[钉钉管理后台](https://oa.dingtalk.com/) **> 自定义工作台**中咨询。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p516474.png)

## **步骤一：创建连接器**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，依次选择**开放能力 > 连接平台 > 我的连接器。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532754.png)
2. 单击**创建连接器**，进入创建连接器页面，填写连接器名称和连接器描述，单击**确定**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p1095445.png)
3. 在连接器详情页面，选择鉴权设置，并配置鉴权方式，本教程以[API Secret鉴权](../../02-连接平台/02-XdgyZifJkr-我的连接/0017-apissecret-authentication.md)为例。

   > **[!NOTE]**
   >
   > APISecret如何配置，可参考[API Secret鉴权](../../02-连接平台/02-XdgyZifJkr-我的连接/0017-apissecret-authentication.md)介绍。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p1095446.png)

## **步骤二：配置连接器执行动作**

1. 在连接平台首页，选择**我的连接器**，然后在自建连接器下单击目标连接器。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532773.png)
2. ​在目标连接器基础信息页面，单击**执行动作**，然后单击**创建执行动作**。

   > **[!NOTE]**
   >
   > 执行动作的配置方法，请参考[添加执行动作](../../02-连接平台/02-XdgyZifJkr-我的连接/0012-add-execution-action-1.md)说明。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p532780.png)​
3. 完成配置后，点击**发布**。

## **步骤三：创建卡片模板并配置变量**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，单击**开放能力**，选择**卡片平台**。![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514943.png)
2. 在模板列表页面，单击**新建模板**。![iShot2022-11-08 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p514949.png)
3. 在新建模板页面，依照下列要求填写模板信息后，单击**创建**。

   - **模板名称：**自建工作台卡片，是该卡片在工作台上最终展示的名称。
   - **卡片类型：**选择工作台卡片。
   - **关联应用：**选择需要关联的应用，本文档介绍企业自建工作台卡片，关联应用选择本企业创建的企业内部应用即可。

     ![iShot2022-11-09 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515297.png)
4. 进入模板编辑页面，本文以**视频卡片**为例。

   > **[!NOTE]**
   >
   > 根据自身需求，配置工作台卡片的组件绑定动态变量。
   >
   > 例如，可添加基础文本组件，与title变量绑定。也可以将视频组件与videoUrl变量绑定。

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
6. 完成工作台场域配置后，单击**创建实例并投放**。

   ![创建实例并投放.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p714262.png)

## **步骤五：工作台卡片的使用**

卡片实例投放后，点击提醒内的**点击这里**，进入工作台设计器进行配置和使用。

1. 编辑自定义工作台，使用创建的工作台卡片实例。

   - 单击查看详情，查看自定义工作台详情。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p714268.png)
   - 单击配置工作台，进入工作台设计器。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p714270.png)
   - 在工作台设计器页面，单击左上角**新建页面**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515372.png)
   - 在左侧组件库的自建组件库中，将卡片实例拖拽至目标位置。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p714271.png)
   - 在设计器右上角分别单击**保存**和**发布**。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7255107871/p714273.png)
   - 在自定义工作台页面，单击**发布工作台**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515376.png)
   - 在选择发布范围页面，设置工作台可见范围，单击**发布**。

     ![iShot2022-11-09 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6255107871/p515377.png)
