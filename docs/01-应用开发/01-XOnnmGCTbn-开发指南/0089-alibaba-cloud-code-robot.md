---
title: "阿里云Code机器人"
source_url: "https://open.dingtalk.com/document/dingstart/alibaba-cloud-code-robot"
namespace: "dingstart"
slug: "alibaba-cloud-code-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > 阿里云Code机器人"
doc_id: "rHvI8YzqV7"
updated_at: "2026-07-22 16:55:28"
---

> Source: https://open.dingtalk.com/document/dingstart/alibaba-cloud-code-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > 阿里云Code机器人
> Updated: 2026-07-22 16:55:28

# 阿里云Code机器人

本文介绍如何在钉钉群添加一个阿里云Code机器人进行消息推送。

> **[!IMPORTANT]**
>
> - 阿里云Code产品已升级为[阿里云Codeup](https://codeup.aliyun.com/)，支持原阿里云code项目迁移至Codeup。
> - 如果您已将项目迁移至阿里云Codeup，请参考文档阿里云Codeup机器人。

## 步骤一：获取阿里云Code机器人Webhook

1. 以PC端为例，打开PC端钉钉，进入**机器人管理**页面。

   1. 选择需要添加机器人的群聊，然后依次点击**群设置** > **智能群助手**。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0047597261/p232816.png)
   2. 点击**添加机器人**，进入**机器人管理**页面。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0528597261/p185964.png)
2. 在**机器人管理**页面选择**阿里云Code**机器人，然后点击**添加**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6894746061/p185968.png)
3. 输入机器人名字后，点击**完成**。

   ![完成](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7068736061/p185341.png)
4. 复制出机器人的Webhook地址，可用于向这个群发送消息，格式如下：

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX
   ```

   > **[!IMPORTANT]**
   >
   > 请保管好此Webhook 地址，不要公布在外部网站上，泄露后有安全风险。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6894746061/p185981.png)

## 步骤二：在阿里云Code中设置项目的Webhook

> **[!IMPORTANT]**
>
> - 阿里云Code产品已升级为[阿里云Codeup](https://codeup.aliyun.com/)，支持原阿里云code项目迁移至Codeup。
> - 如果您已将项目迁移至阿里云Codeup，请参考文档阿里云Codeup机器人。

### **旧版阿里云Code**

如果目前使用的仍是旧版本阿里云Code，请参考以下配置流程。

1. 进入你的项目，点击左侧**设置**，进入设置页面。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6894746061/p185982.png)
2. 然后点击**WebHooks**，填入**步骤一**生成的Webhook，并勾选感兴趣的事件，然后点击**增加WEBHOOKS**即可完成设置。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6894746061/p185983.png)

### **新版阿里云Codeup**

如果目前使用的是新版本阿里云Codeup，请参考以下配置流程。

1. 进入你的项目。

   ![iShot2022-11-23 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5250264871/p523365.png)
2. 左下角点击**设置**。

   ![iShot2022-11-23 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5250264871/p523369.png)
3. 然后点击**Webhooks**，点击**新建Webhook**，填写第一步获取的Webhook地址，并勾选需要订阅的事件，点击确定。

   ![iShot2022-11-23 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5250264871/p523371.png)
