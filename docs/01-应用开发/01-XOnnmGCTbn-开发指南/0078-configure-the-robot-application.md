---
title: "配置企业机器人"
source_url: "https://open.dingtalk.com/document/dingstart/configure-the-robot-application"
namespace: "dingstart"
slug: "configure-the-robot-application"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 企业机器人 > 企业机器人 > 配置企业机器人"
doc_id: "23Rqnd2S4X"
updated_at: "2026-06-30 09:01:10"
---

> Source: https://open.dingtalk.com/document/dingstart/configure-the-robot-application
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 企业机器人 > 企业机器人 > 配置企业机器人
> Updated: 2026-06-30 09:01:10

# 配置企业机器人

如果你需要配置一个企业机器人应用，你可以参考本文档操作步骤。

## **前提条件**

需要完成[应用创建与配置](0007-create-application.md)流程。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**应用能力** > **机器人，**开启机器人配置**。**
3. **配置机器人信息：**

   | **配置项** | **必填** | **描述** |
   | --- | --- | --- |
   | 机器人名称 | 是 | 请使用意图正确、文明的词汇，避免歧义、错别字及不合规词汇。 |
   | 机器人图标 | 是 | 建议大小为240像素\*240像素，请使用清晰的图片，图片核心内容居中。尽量避免尺寸过小、过大或者内容不合规图片。 |
   | 机器人简介 | 是 | 请简要描述机器人信息，最多10个字符，该描述将在群内添加机器人时向用户进行展示。 |
   | 机器人描述 | 是 | 请描述机器人功能，最多200字符，该描述将在机器人名片信息和群内添加机器人时向用户进行展示。 |
   | 机器人消息预览图 | 是 | 图片格式必须为：png、jpeg、jpg，不超过2M，可修改。 |
   | 消息接收模式 | 否 | 用于接收钉钉推送的POST消息：  - HTTP 模式 - Stream 模式 详情参考[机器人接收消息](0080-robot-receive-message.md)。 |
   | 消息接收地址  **[!NOTE]**  仅**HTTP模式**下需要填写 | 否 | 填写一个公网可访问的本企业HTTPS服务地址，用于接收钉钉推送的POST消息。 |
4. 单击发布（保存）机器人。
5. （可选）发布后，你可以单击**点击调试**按钮**，**此时会生成一个测试群**，**你可以在群内测试@机器人的功能。

## **后续步骤**

机器人发布后，必须要发布应用，详情参考[发布应用](0019-publish-dingtalk-application.md)。
