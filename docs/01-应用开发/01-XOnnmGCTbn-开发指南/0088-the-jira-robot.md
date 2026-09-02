---
title: "JIRA机器人"
source_url: "https://open.dingtalk.com/document/dingstart/the-jira-robot"
namespace: "dingstart"
slug: "the-jira-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > JIRA机器人"
doc_id: "KNMeBuc11T"
updated_at: "2026-07-22 16:55:27"
---

> Source: https://open.dingtalk.com/document/dingstart/the-jira-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > JIRA机器人
> Updated: 2026-07-22 16:55:27

# JIRA机器人

本文介绍如何在钉钉群添加一个JIRA机器人进行消息推送。

## 注意事项

目前JIRA机器人只支持**jira:issue\_created**和**jira:issue\_updated**事件。

## 步骤一：获取JIRA机器人Webhook地址

1. 以PC端为例，打开PC端钉钉，进入**机器人管理**页面。

   1. 选择需要添加机器人的群聊，然后依次点击**群设置** > **智能群助手**。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0047597261/p232816.png)
   2. 点击**添加机器人**，进入**机器人管理**页面。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0528597261/p185964.png)
2. 在**机器人管理**页面选择**JIRA**机器人，然后点击**添加**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4381076061/p185966.png)
3. 输入机器人名字后，点击**完成**。

   ![完成](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3873736061/p185323.png)
4. 复制出机器人的Webhook地址，可用于向这个群发送消息，格式如下：

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX
   ```

   > **[!IMPORTANT]**
   >
   > 请保管好此Webhook 地址，不要公布在外部网站上，泄露后有安全风险。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4381076061/p185980.png)

## 步骤二：在JIRA中设置项目的Webhook

在JIRA系统中，通过**设置** > **System** > **Webhooks**进入Webhook设置页面，为相应的项目设置钉钉群机器人的Webhook，具体操作如下图所示。

1. 点击**System**菜单。

   ![1554966380276-faeb7e28-e32f-4b60-bdaf-ac12b76d75a7.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8824199951/p131237.jpeg)
2. 选择**Webhooks**设置项。

   ![1554966380296-5e7506f8-fa1a-4d4d-b375-8840ea01e64f.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8824199951/p131238.jpeg)
3. 新增项目**WebHook**。

   ![1554966380519-243b4fb3-eba4-49b5-9285-7f1f4a4c7139.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8824199951/p131239.jpeg)
4. 填写钉钉群聊天机器人Webhook。

   ![1554966380296-490be714-2b2a-44c9-bf21-a820dedb9c48.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9824199951/p131240.jpeg)
