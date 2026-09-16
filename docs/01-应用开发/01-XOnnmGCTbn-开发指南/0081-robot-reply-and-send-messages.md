---
title: "机器人回复/发送消息"
source_url: "https://open.dingtalk.com/document/dingstart/robot-reply-and-send-messages"
namespace: "dingstart"
slug: "robot-reply-and-send-messages"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 企业机器人 > 企业机器人 > 机器人回复/发送消息"
doc_id: "BYdM70cY4t"
updated_at: "2026-06-30 09:01:08"
---

> Source: https://open.dingtalk.com/document/dingstart/robot-reply-and-send-messages
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 企业机器人 > 企业机器人 > 机器人回复/发送消息
> Updated: 2026-06-30 09:01:08

# 机器人回复/发送消息

如果你需要实现机器人回复或机器人发送消息，可依据本文档操作步骤实现机器人回复或机器人发送消息的开发。

## **背景信息**

机器人回复消息本质上就是机器人发送消息的过程。因此本文中，回复消息和发送消息具有相同的含义。

发送消息的方式可以通过服务端 API 和 Webhook 的方式进行发送，下面将针对两种发送消息的方式进行介绍。

## **前提条件**

需要完成[应用创建与配置](0007-create-application.md)流程。

## **通过 Webhook 发送消息**

> **[!NOTE]**
>
> 通过 webhook 方式发送消息，支持 @ 功能，具体请查下下方接入示例。

1. 通过应用机器人 Webhook url 进行发送消息：

   1. 在[机器人接收消息](0080-robot-receive-message.md)中，获取群内应用机器人的 Webhook url 地址。详情参考[获取应用机器人 Webhook](../02-4a8AMF6u2A-服务端-API/0791-faq-robot.md#3d0beea13di8p)。
   2. Java 开发环境准备：

      - 引入 Java SDK ，更多语言 SDK 参考[旧版服务端SDK下载](../02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。

        ```
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>alibaba-dingtalk-service-sdk</artifactId>
            <version>2.0.0</version>
        </dependency>
        ```
   3. 接入代码示例：

      ```
      public void sendMessageWebhook() throws ApiException {
              DingTalkClient client = new DefaultDingTalkClient("{ Webhook url 地址 }");
              OapiRobotSendRequest request = new OapiRobotSendRequest();
              request.setMsgtype("text");
              OapiRobotSendRequest.Text text = new OapiRobotSendRequest.Text();
              text.setContent("测试文本消息");
              request.setText(text);
              OapiRobotSendRequest.At at = new OapiRobotSendRequest.At();
              at.setAtUserIds(Arrays.asList("4525xxxxxxxxx7041"));
              at.setIsAtAll(false);
              request.setAt(at);
              OapiRobotSendResponse response = client.execute(request);
              System.out.println(response.getBody());
      }
      ```

      更多消息类型，请参考[消息发送与接收类型](../02-4a8AMF6u2A-服务端-API/0699-robot-message-type.md)。
2. 通过机器人接收消息中 sessionWebhook 字段，进行消息发送。

   1. 获取[机器人接收消息](0080-robot-receive-message.md)的 JSON 数据中 sessionWebhook 地址。
   2. Java 开发环境准备：

      - 引入 Java SDK ，更多语言 SDK 参考[旧版服务端SDK下载](../02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。

        ```
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>alibaba-dingtalk-service-sdk</artifactId>
            <version>2.0.0</version>
        </dependency>
        ```
   3. 接入代码示例：

      ```
      public void sendMessageWebhook() throws ApiException {
              DingTalkClient client = new DefaultDingTalkClient("{ SessionWebhook url 地址 }");
              OapiRobotSendRequest request = new OapiRobotSendRequest();
              request.setMsgtype("text");
              OapiRobotSendRequest.Text text = new OapiRobotSendRequest.Text();
              text.setContent("测试文本消息");
              request.setText(text);
              OapiRobotSendRequest.At at = new OapiRobotSendRequest.At();
              at.setAtUserIds(Arrays.asList("4525xxxxxxxxx7041"));
              at.setIsAtAll(false);
              request.setAt(at);
              OapiRobotSendResponse response = client.execute(request);
              System.out.println(response.getBody());
      }
      ```

      更多消息类型，请参考[消息发送与接收类型](../02-4a8AMF6u2A-服务端-API/0699-robot-message-type.md)。

## **通过服务端 API 发送消息**

服务端 API 发送消息列表，更多 API 内容参考[机器人服务端 API](../02-4a8AMF6u2A-服务端-API/0698-development-robot-overview.md)。

| **API 名称** | **描述** |
| --- | --- |
| [机器人发送群聊消息](../02-4a8AMF6u2A-服务端-API/0716-the-robot-sends-a-group-message.md) | 群内发送消息。  暂不支持 @ 功能 |
| [批量发送人与机器人会话中机器人消息](../02-4a8AMF6u2A-服务端-API/0714-chatbots-send-one-on-one-chat-messages-in-batches.md) | 人与机器人会话中发送消息。  暂不支持 @ 功能 |
| [人与人会话中机器人发送普通消息](../02-4a8AMF6u2A-服务端-API/0715-the-robot-sends-ordinary-messages-in-a-person-to-person-conversation.md) | 人与人会话中发送消息。  暂不支持 @ 功能  **[!NOTE]**  仅在[单聊酷应用](0062-private-chat-coolapp-overview.md)场景下使用。 |

服务端 API 调用详情参考文档[服务端SDK下载](../02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)。

## **后续步骤**

机器人发送消息开发完成后，需进行[发布应用](0019-publish-dingtalk-application.md)。

> 如果机器人的消息样式无法满足你的需求，可参考[互动卡片](../02-4a8AMF6u2A-服务端-API/0777-overview-card.md)。
