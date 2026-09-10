---
title: "上传并发布插件"
source_url: "https://open.dingtalk.com/document/development/upload-and-publish-plug-ins-1"
namespace: "development"
slug: "upload-and-publish-plug-ins-1"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "操作指南 > 上传并发布插件"
doc_id: "5rQV5OqiQf"
updated_at: "2026-09-10 14:38:14"
---

> Source: https://open.dingtalk.com/document/development/upload-and-publish-plug-ins-1
> Path: 专属版客户端插件 / 功能介绍 / 操作指南 > 上传并发布插件
> Updated: 2026-09-10 14:38:14

# 上传并发布插件

客户端插件开发、创建完成后，你需要上传并发布插件，你可以参考文档操作步骤完成操作。

## **前提条件**

1. 完成[创建客户端插件](0002-creating-a-client-plug-in-1.md)流程。

## **操作步骤**

1. 登录[钉钉企业管理后台](https://oa.dingtalk.com/)，单击**钉钉专属版** > **App定制** > **专属插件。**
2. 在专属插件页面，查找你创建完成的客户端插件，并单击卡片进入**插件详情。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8815628171/p803496.png)

   进入详情页后，可以看到平台默认创建了1.0.0版本，该版本处于**测试版本**阶段。此时，我们可以点击1.0.0版本的**详情**，进入对应版本中上传SDK，也可以单击**创建版本**来创建一个新的版本号并上传对应的SDK。
3. 单击指定版本号（比如1.0.0）操作中的**详情**按钮，进入版本详情页，然后单击**上传**插件包：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8815628171/p803499.png)

   - （可选）上传Android插件，单击**上传**，并选择插件包（\*.deb）完成上传。
   - （可选）上传iOS插件，单击**上传**，并选择指定的产物类型完成上传。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8815628171/p803500.png)

     > **[!IMPORTANT]**
     >
     > 这里每一个文件都必须是zip类型，每一个zip代表一个Pod，请将每个Pod文件夹单独右键压缩成zip，逐一上传。如果是Appex文件，则直接将appex文件压缩成zip。在这里输入正确的名称（务必正确，需要与Pod文件夹名称完全一致，或者与Appex的名称完全一致（不需要.appex后缀）），选择正确的产物类型，点击上传。
   - （可选）更新插件，在实际研发中会遇到以下两种场景需要更新插件：

     - **研发过程持续更新：**

       假如插件正在研发中，需要持续更新插件验证已经修复的问题。我们建议不要**正式发布**，仅更新插件文件即可。

       如下图，单击**删除**删掉原有插件包，然后重新上传最新的插件包。

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4948199761/p610379.png)
     - **新需求升级更新：**

       假如插件已经发布了稳定版本，并已经在线上专属App中运行使用，但此时有新需求需要更新插件，我们建议创建新版本号，并基于新版本号发布插件文件。这样在新版本上线遇到问题时可快速回滚到老版本。步骤如下：

       - 创建新版本。

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8815628171/p803506.png)
       - 填入新的插件版本，例如1.0.1。

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8815628171/p803507.png)
4. 单击指定版本号（比如1.0.0）操作中的**正式发布**，可将插件发布到正式环境中。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8815628171/p803514.png)

   > **[!NOTE]**
   >
   > - 测试版本和正式版本有什么区别？
   >
   >   1. 当版本号是**测试版本**状态时，可以不断地删除原有的SDK文件，并重新上传。
   >   2. 当版本号是**正式版本**（正式发布后）状态时，版本不可再修改任何信息，比如不可以重新上传SDK文件。
   > - Android集成可以直接使用**打包测试**功能发起构建，构建时测试版本号是可选的，便于快速验证功能，但测试版本号在正式集成环境中不可见，因此我们建议测试稳定后，再**正式发布**，并到**App定制** - **App打包** - **创建打包**中构建正式版本。

## **后续步骤**

插件上传完成后，你需要[构建集成插件](0004-building-integration-plug-ins-1.md)。
