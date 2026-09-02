---
title: "关联群模板机器人到群模板"
source_url: "https://open.dingtalk.com/document/dingstart/associate-group-template-robot-to-group-template"
namespace: "dingstart"
slug: "associate-group-template-robot-to-group-template"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 群模板机器人 > 关联群模板机器人到群模板"
doc_id: "aKBOgv2Iaj"
updated_at: "2026-07-22 16:55:33"
---

> Source: https://open.dingtalk.com/document/dingstart/associate-group-template-robot-to-group-template
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 群模板机器人 > 关联群模板机器人到群模板
> Updated: 2026-07-22 16:55:33

# 关联群模板机器人到群模板

如果你的群模板需要关联群模板机器人，可以参考本文档操作步骤。

## 前提条件

完成[创建群模板机器人](0094-creation-and-installation-of-swarm-template-robots.md)流程。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，单击**开放能力** > **场景群。**
2. 在左侧导航栏选择**群模板**，进入**模板列表**页面：

   - 如果已有群模板：

     1. 单击已有群模板，进入模板信息页面。
     2. 单击**编辑** > **下一步，**进入 **② 填写模板信息**步骤
     3. 单击**选择已创建的机器人，**选择已有机器人，并单击**保存编辑**。
     4. 单击左侧导航栏**模板信息**，然后再单击**提交审核**。

        ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3350174871/p768472.png)
     5. 审核成功后，单击发布。
   - 如果无群模板，则需创建群模板：

     1. 单击**创建群模板，**配置 **① 选择模板**：

        | **配置项** | **说明** |
        | --- | --- |
        | 企业类型 | 类型：  - 企业三方，选择第三方企业应用 - 企业内部，选择企业内部应用 |
        | 可选应用 | 选择配置的应用。 |

        配置完成后，单击**下一步**。
     2. 配置 **②** 填写模板信息：

        | **配置项** | **必填** | **说明** |
        | --- | --- | --- |
        | 模板名称 | 是 | 填写模板名称信息。 |
        | 图标 | 是 | 上传模板图标图片，要求：尺寸大小 32\*32 px，图片大小不超过 3 M，支持jpeg、jpg、png格式。 |
        | 描述 | 是 | 填写模板说明信息。 |
        | 模板图文介绍 | 是 | - 文案介绍：填写模板介绍标题 - 模板描述：填写模板详细介绍 - 图片介绍：上传图片介绍，要求：尺寸大小 343\*195 px，图片大小不超过 3 M，支持jpeg、jpg、png格式 |
        | 模板可见范围 | 否 | 选择模板可见的范围。 |
        | 群设置 | 否 | 选择该模板创建群后的基础设置。 |
        | 选择模板 | 否 | 默认为空白模板。 |
        | 选择插件 | 否 | 选择已创建的群插件/新建插件 |
        | 选择机器人 | 否 | 选择前提条件中已审核通过的机器人。 |

        配置完成后，单击**保存编辑**。
     3. 单击左侧导航栏**群模板**，选择上述保存的群模板。并在模板信息页面，单击**提交审核**。
     4. 审核通过后，单击**发布。**

## **后续步骤**

如果你需要使用群模板机器人发送消息，详情参考文档：

- [群模板机器人发送群聊消息](../02-4a8AMF6u2A-服务端-API/0703-group-template-robot-sends-group-chat-message.md)
