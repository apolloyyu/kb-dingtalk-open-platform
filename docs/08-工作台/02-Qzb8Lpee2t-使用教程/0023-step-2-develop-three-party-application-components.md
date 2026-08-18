---
title: "步骤二：组件的开发和预览"
source_url: "https://open.dingtalk.com/document/dingstart/step-2-develop-three-party-application-components"
namespace: "dingstart"
slug: "step-2-develop-three-party-application-components"
group: "工作台"
tab: "使用教程"
breadcrumb: "合作伙伴教程 > 第三方全码组件 > 上架流程 > 步骤二：组件的开发和预览"
doc_id: "i5lKDtsvmM"
updated_at: "2026-08-18 09:12:08"
---

> Source: https://open.dingtalk.com/document/dingstart/step-2-develop-three-party-application-components
> Path: 工作台 / 使用教程 / 合作伙伴教程 > 第三方全码组件 > 上架流程 > 步骤二：组件的开发和预览
> Updated: 2026-08-18 09:12:08

# 步骤二：组件的开发和预览

本文介绍了如何使用设计器开发第三方企业应用组件并预览。

## 一、创建插件并设置开发者

> **[!NOTE]**
>
> 插件是组件的载体，一个插件里可以包含多个组件，建议一个插件最多不超过10个组件。

参考以下操作，创建插件并设置开发者：

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/plugin)。
2. 在顶部菜单栏，单击**定制服务，**然后选择**插件管理**，最后单击**创建插件**，如下图所示：

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4425597261/p300246.png)
3. 在**创建插件**页面，填写相关信息，然后单击**创建插件** 。

   ![创建插件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2189687261/p300247.png)

   - 插件名称：插件名称将显示在开发人员的小程序IDE的关联应用列表中，用于区分不同的应用。
   - 插件描述：提交申请后，会根据此信息进行插件的审核。
   - 插件功能：提交申请后，会根据此信息进行插件的审核。
   - 视觉稿设计：提交申请后，会根据此信息进行插件的审核。
   - 组件类型： 不同组件类型应用于不同工作台，请选择**通用组件**。

     > **[!NOTE]**
     >
     > - 组件类型提交后不可修改。
     > - 通用组件应用于标准工作台，定制组件应用于自定义工作台。
   - 使用场景：不同的组件类型使用于不同的场景。
4. 提交审核成功后，单击**返回，**查看插件列表。

   > **[!NOTE]**
   >
   > 插件创建成功后的初始状态为**待上传版本**。

   ![创建插件成功返回](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0020948261/p301800.png)
5. 单击**设置开发者**，添加IDE插件的开发人员，如下图所示：

   > **[!NOTE]**
   >
   > 默认插件创建者会自动添加到插件的开发人员列表中。

   ![开发者设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2189687261/p300248.png)
6. 设置了开发人员后，开发人员在小程序IDE的**关联应用列表**中可见到此插件并进行关联，如图所示：

   ![插件管理并创建插件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300303.png)

## 二、开发第三方企业应用组件

在组件开发过程中，请注意以下几点：

- 第三方企业应用组件提交上架审批后，需要等待产品验收通过才能提交灰度，如下所示：

  ![方应用组件提交上架审批](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300304.png)
- 请使用DingTalk Fe CLI安装脚手架开发，在使用`dd init myapp`命令时，会拉取最新脚手架模板，只有最新模板提供了**quicksetting**的预览能力。

  > **[!NOTE]**
  >
  > 脚手架初始化第5步时，模板请选择**application-ecology**。

  建议存量组件，可以将原工程中的plugin添加到新的模板中，在新的模板中修改相关的mock数据和配置文件，方便IDE中调试，详情可参考[开发组件](0011-step-3-develop-components.md#8b8144165eltj)。
- 第三方企业应用组件开发需遵循第三方企业应用组件[设计规范](https://ding.design/?spm=ding_open_doc.document.0.0.18684a707LUUDg#/cate/1/page/824)和[开发规范](0026-development-specification.md)。
- 如果在开发过程中遇到问题，可通过[联系我们](0019-workbench-dashboard-model-overview.md)加入**标准工作台组件/解决方案接入群**，在群内咨询服务小蜜。

## 三、设计器调试预览

### 移动端工作台预览

1. 登录[开发者后台](https://open-dev.dingtalk.com/?spm=ding_open_doc.document.0.0.74622f92F0qToA#/plugin)。
2. 选择**定制服务**，然后单击**插件管理**，进入插件管理界面，如下图所示：

   ![插件管理列表界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300306.png)
3. 选择发布状态为**开发调试中**的插件，最后单击**版本管理**，进入版本管理界面。

   ![版本管理进入详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300308.png)
4. 在版本管理界面，单击**去设计器调试**，进入调试设计器。

   ![去设计器调试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300309.png)
5. 设计器中单击**移动端预览**，可使用手机进行预览。

   > **[!NOTE]**
   >
   > 暗黑模式将跟随系统设置。

   ![移动端预览](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7975597261/p300310.png)

   示例效果如下所示：

   ![示例效果 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9299687261/p300255.png)

### PC端工作台的预览

1. 登录[开发者后台](https://open-dev.dingtalk.com/?spm=ding_open_doc.document.0.0.74622f92F0qToA#/plugin)。
2. 选择**定制服务**，然后单击**插件管理**，进入插件列表界面，如下图所示：

   ![插件管理列表界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300306.png)
3. 选择发布状态为**开发调试中**的插件，然后单击**版本管理**，进入版本管理界面。

   ![版本管理进入详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6051987261/p300308.png)
4. 单击**配置**，确认配置文件自动同组件代码的`config.json`同步。

   ![PC配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7051987261/p300318.png)配置信息如下图所示：

   ![PC端配置信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7051987261/p300319.png)
5. 在版本管理界面，单击**去设计器调试**，进入调试设计器。

   > **[!NOTE]**
   >
   > 确认目标应用对应的版本在应用场景下具有**PC端工作台**。

   ![PC去设计器设计](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7051987261/p300315.png)
6. 设计器中单击**PC端预览**，可在钉钉PC端打开带有组件的页面。

   ![PC端预览按钮](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7051987261/p300320.png)

   示例效果如下所示：

   ![PC端示例效果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7051987261/p300321.png)
