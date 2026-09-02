---
title: "GitHub机器人"
source_url: "https://open.dingtalk.com/document/dingstart/github-robot"
namespace: "dingstart"
slug: "github-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > GitHub机器人"
doc_id: "iws78Wk0Pu"
updated_at: "2026-07-22 16:55:26"
---

> Source: https://open.dingtalk.com/document/dingstart/github-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > GitHub机器人
> Updated: 2026-07-22 16:55:26

# GitHub机器人

本文介绍如何在钉钉群添加一个GitHub机器人进行消息推送。

## 步骤一：获取GitHub机器人webhook地址

1. 以PC端为例，打开PC端钉钉，进入**机器人管理**页面。

   1. 选择需要添加机器人的群聊，然后依次点击**群设置** > **智能群助手**。

      ![群助手 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0047597261/p232816.png)
   2. 点击**添加机器人**，进入**机器人管理**页面。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0528597261/p185964.png)
2. 在**机器人管理**页面选择**GitHub**机器人，然后点击**添加**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4581076061/p185965.png)
3. 输入机器人名字后，点击**完成**。

   ![GitHub](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6410746061/p185303.png)
4. 复制出机器人的Webhook地址，可用于向这个群发送消息，格式如下：

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX
   ```

   > **[!IMPORTANT]**
   >
   > 请保管好此Webhook 地址，不要公布在外部网站上，泄露后有安全风险。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4581076061/p185977.png)

## 步骤二：在GitHub中设置项目的webhook

1. 进入你的 GitHub 代码库，依次点击**Settings** > **Webhooks & Services** > **Add Webhook**添加 Webhook。

   ![1554965464234-5c82d1d6-9746-40b9-8b2d-f634e5d0601c.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7824199951/p131235.jpeg)
2. 填入对应GitHub机器人的Webhook地址，即可完成配置。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7824199951/p131236.jpeg)
