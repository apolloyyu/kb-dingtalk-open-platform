---
title: "Travis机器人"
source_url: "https://open.dingtalk.com/document/dingstart/travis-robot"
namespace: "dingstart"
slug: "travis-robot"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > Travis机器人"
doc_id: "UVYY3KiG7Q"
updated_at: "2026-07-22 16:55:28"
---

> Source: https://open.dingtalk.com/document/dingstart/travis-robot
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 第三方机器人工具接入 > Travis机器人
> Updated: 2026-07-22 16:55:28

# Travis机器人

本文介绍如何在钉钉群添加一个Travis机器人进行消息推送。

## 步骤一：获取Travis机器人的Webhook地址

1. 以PC端为例，打开PC端钉钉，进入**机器人管理**页面。

   1. 选择需要添加机器人的群聊，然后依次点击**群设置** > **智能群助手**。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0047597261/p232816.png)
   2. 点击**添加机器人**，进入**机器人管理**页面。

      ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0528597261/p185964.png)
2. 在**机器人管理**页面选择**Travis**机器人，然后点击**添加**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9781076061/p185969.png)
3. 输入机器人名字后，点击**完成**。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9781076061/p185972.png)
4. 复制出机器人的Webhook地址，可用于向这个群发送消息，格式如下：

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX
   ```

   > **[!IMPORTANT]**
   >
   > 请保管好此Webhook 地址，不要公布在外部网站上，泄露后有安全风险。

   ![机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9781076061/p185974.png)

## 步骤二：配置Travis的项目配置文件

将如下内容添加到 .travis.yml 文件中

```
notifications: webhooks: https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx
```
