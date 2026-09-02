---
title: "阿里云Codeup机器人"
source_url: "https://open.dingtalk.com/document/dingstart/alibaba-cloud-codeup-robot"
namespace: "dingstart"
slug: "alibaba-cloud-codeup-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > 阿里云Codeup机器人"
doc_id: "QsZ5Zcovix"
updated_at: "2026-07-21 15:55:24"
---

> Source: https://open.dingtalk.com/document/dingstart/alibaba-cloud-codeup-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > 阿里云Codeup机器人
> Updated: 2026-07-21 15:55:24

# 阿里云Codeup机器人

本文介绍如何在钉钉群添加一个阿里云Codeup机器人进行消息推送。

## 步骤一：获取阿里云Codeup机器人Webhook

1. 以PC端为例，打开PC端钉钉，进入**机器人管理**页面。

   1. 选择需要添加机器人的群聊，然后依次单击右上角**群设置** > **智能群助手**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7915439661/p524289.png)
   2. 在**机器人管理**页面，单击**添加机器人**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7915439661/p524296.png)
2. 在**机器人管理**页面，选择**阿里云Codeup**机器人，然后单击**添加**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6915439661/p524297.png)
3. 单击**添加。**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6915439661/p524299.png)
4. 输入机器人名字后，单击**完成**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7915439661/p524305.png)
5. 复制出机器人的Webhook地址，可用于向这个群发送消息，格式如下。

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX
   ```

   > **[!IMPORTANT]**
   >
   > 请保管好此Webhook 地址，不要公布在外部网站上，泄露后有安全风险。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7915439661/p524308.png)

## 步骤二：在阿里云Codeup中设置项目的Webhook

1. 登录[阿里云Codeup](https://codeup.aliyun.com/)，进入你的项目。![iShot2022-11-23 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5250264871/p523365.png)
2. 单击左下角**设置**。![iShot2022-11-23 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5250264871/p523369.png)
3. 然后单击**Webhooks**，单击**新建Webhook**，填写第一步获取的Webhook地址，并勾选需要订阅的事件，单击**确定**即可。![iShot2022-11-23 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5250264871/p523371.png)
