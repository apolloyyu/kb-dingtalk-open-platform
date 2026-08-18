---
title: "步骤四：组件的发布"
source_url: "https://open.dingtalk.com/document/dingstart/step-4-publish-the-component"
namespace: "dingstart"
slug: "step-4-publish-the-component"
group: "工作台"
tab: "使用教程"
breadcrumb: "合作伙伴教程 > 第三方全码组件 > 上架流程 > 步骤四：组件的发布"
doc_id: "d28zaNQSB9"
updated_at: "2025-09-03 15:57:23"
---

> Source: https://open.dingtalk.com/document/dingstart/step-4-publish-the-component
> Path: 工作台 / 使用教程 / 合作伙伴教程 > 第三方全码组件 > 上架流程 > 步骤四：组件的发布
> Updated: 2025-09-03 15:57:23

# 步骤四：组件的发布

本文介绍了第三方企业应用组件开发完成后提交上架审批、产品审核和发布组件的操作步骤。

## 一、提交上架审批

根据以下步骤，提交上架审批：

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/plugin)。
2. 在顶部菜单栏，单击**定制服务**，然后选择**插件管理**，最后单击**创建插件**，如下图所示：

   ![提交上架审批](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875597261/p300331.png)
3. 在版本管理页面，单击**提交上架**发起上架审批。

   > **[!IMPORTANT]**
   >
   > - 保证在提交上架之前，对组件完成了测试。
   > - 上架审批主要进行代码检测，一般在1分钟内完成。审核结束后会将审核结果同步到插件状态面板，并通过钉钉小秘书同步给开发者。

   ![提交上架](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7351987261/p300332.png)

   - **审批失败**

     如审批拒绝，会在版本管理中透出异常原因，请修改后重新上传并提交，如下图所示：

     ![上架审批拒绝](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7351987261/p300333.png)
   - **审批通过**

     如审批通过后，会流转到产品审核阶段，需要发起审批流提交验收申请。

## 二、提交产品审核

根据以下步骤，提交产品审核：

1. 加入开发群。

   - 钉钉搜索群号**23108710**申请加入**钉钉组件和工作台开发互助群**，加群后看群公告。
   - 钉钉扫描下面二维码访问。

     ![钉钉组件和工作台开发互助群](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2202750861/p618360.png)
2. 加入**钉钉ISV沟通组**。

   如果你未加入**钉钉ISV沟通组**，可通过钉钉扫描下方二维码加入：

   ![ISV沟通组](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7351987261/p300340.png)
3. 提交产品验收审批流。

   **钉钉ISV沟通组**组织内提交产品验收的审批流，可以重新提交组件验收或提交组件迭代更新验收。具体内容可查看审批流内说明。

   ![提交产品验收的审批流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4295058261/p300342.png)
4. 产品审核通过后可以在**版本管理界面**中发布该版本。

## 三、提交发布

根据以下步骤，提交发布：

1. 单击**设置灰度**，设置灰度范围。

   > **[!NOTE]**
   >
   > 发布时可以选择灰度发布，按用户百分比或者指定企业CorpId进行灰度发布。**全量发布前必须进行灰度**，如果开发者判断不需要灰度，可以先设置一个灰度值后，单击**全量发布**。

   ![设置灰度](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8351987261/p300344.png)

   - **灰度百分比**：灰度范围可设置为1%~70%，超过70%时请设置全量发布。
   - **灰度组织（可选）**：输入应用新插件的组织的corpId，多个corpId请用（;）分隔。
2. 通过灰度测试后，单击**全量发布**完成组件上线。

   > **[!IMPORTANT]**
   >
   > 全量发布后会直接影响线上用户，请经过灰度测试后再全量发布。
