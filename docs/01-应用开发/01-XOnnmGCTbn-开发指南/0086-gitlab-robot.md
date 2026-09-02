---
title: "GitLab机器人"
source_url: "https://open.dingtalk.com/document/dingstart/gitlab-robot"
namespace: "dingstart"
slug: "gitlab-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > GitLab机器人"
doc_id: "iQsk849Jzk"
updated_at: "2026-07-22 16:55:25"
---

> Source: https://open.dingtalk.com/document/dingstart/gitlab-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > GitLab机器人
> Updated: 2026-07-22 16:55:25

# GitLab机器人

本文介绍如何在钉钉群添加一个GitLab机器人进行消息推送。

## 步骤一：获取GitLab机器人Webhook地址

1. 以PC端为例，打开PC端钉钉，进入**机器人管理**页面。

   1. 选择需要添加机器人的群聊，然后依次单击**群设置** > **智能群助手**。

      ![群设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0047597261/p232816.png)
   2. 点击**添加机器人**，进入**机器人管理**页面。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0528597261/p185964.png)
2. 在**机器人管理**页面选择**GitLab**机器人，然后点击**添加**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3253746061/p185954.png)
3. 输入机器人名字后，点击**完成**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3253746061/p185950.png)
4. 复制出机器人的Webhook地址，可用于向这个群发送消息，格式如下：

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX
   ```

   > **[!IMPORTANT]**
   >
   > 请保管好此Webhook 地址，不要公布在外部网站上，泄露后有安全风险。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4253746061/p185951.png)

## 步骤二：在GitLab中设置项目的Webhook

1. 进入你的 GitLab 项目，依次点击右侧**Settings** > **Webhooks**添加Webhook。

   ![1554966017792-a64b5aff-4238-4a04-b04d-89feae24570d.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6824199951/p131233.jpeg)
2. 填入对应GitLab机器人的Webhook地址，即可完成配置。

   ![1554966017778-02b03401-c80c-47b0-b48a-0db02bad0f81.jpeg ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6824199951/p131234.jpeg)
