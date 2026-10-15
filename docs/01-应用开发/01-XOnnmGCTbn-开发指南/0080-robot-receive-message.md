---
title: "机器人接收消息"
source_url: "https://open.dingtalk.com/document/dingstart/robot-receive-message"
namespace: "dingstart"
slug: "robot-receive-message"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 企业机器人 > 企业机器人 > 机器人接收消息"
doc_id: "hJQd2sPi7J"
updated_at: "2026-06-30 09:01:09"
---

> Source: https://open.dingtalk.com/document/dingstart/robot-receive-message
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 企业机器人 > 企业机器人 > 机器人接收消息
> Updated: 2026-06-30 09:01:09

# 机器人接收消息

如果你需要开发机器人接收消息，你可以依据本文档操作步骤完成机器人接收消息服务端的开发。

## **背景信息**

机器人接收消息的模式可以分为 Stream模式 和 HTTP 模式。下面将针对两种模式介绍机器人如何接收消息。

## **前提条件**

需要完成[应用创建与配置](0007-create-application.md)流程。

## **操作步骤**

### **Stream 模式（推荐）**

> 更多语言请参考[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)。

1. Java 开发环境准备：

- 运行环境：JDK 1.8 及以上
- 安装 Java SDK：

  添加依赖项到工程的`pom.xml`文件或下载对应的 jar 包，最新的 SDK 版本可以在[这里](https://s01.oss.sonatype.org/?spm=openapi-amp.sdkpublish.0.0.78cefAyIfAyImO#nexus-search;quick~app-stream-client)查看和下载。

  ```
  <dependency>
    <groupId>com.dingtalk.open</groupId>
    <artifactId>app-stream-client</artifactId>
    <version>{sdk-version}</version>
  </dependency>
  ```

2. 服务端接入示例：

   ```
   public class BotExample {
     
     
     public static void main(String[] args) {
       OpenDingTalkClient client = OpenDingTalkStreamClientBuilder
                   .custom()
                   .credential(new AuthClientCredential("${ClientId}", "${ClientSecret}"))
                   .registerCallbackListener("${topic}", new RobotMsgCallbackConsumer())
                   .build();
        client.start();
     }
     
     
     public static class RobotMsgCallbackConsumer implements OpenDingTalkCallbackListener<JSONObject, JSONObject> {
       
       /*
        * @param request
        * @return
        */
       @Override
       public JSONObject execute(JSONObject request) {
           System.out.println(JSON.toJSONString(request));
           try {
               JSONObject text = request.getJSONObject("text");
               if (text != null) {
                   //机器人接收消息内容
                   String msg = text.getString("content").trim();
                   String openConversationId = request.getString("conversationId");
               }
           } catch (Exception e) {
               log.error("receive group message by robot error:" +e.getMessage(), e);
           }
           return new JSONObject();
       }
     } 
   }
   ```

   | **参数名称** | **说明** |
   | --- | --- |
   | ClientId | 企业内部应用的应用凭证ClientId。 |
   | ClientSecret | 企业内部应用的应用凭证ClientSecret。 |
   | topic | 机器人回调名称，固定值：`/v1.0/im/bot/messages/get`。 |
3. 开发完成后，你需要[添加机器人入群](0079-add-robot-to-group.md)，当你@机器人发送“你好”，服务端接收消息格式如下：

   ```
   {
     "conversationId": "cidjMOsz******AhS4Jg==",
     "atUsers": [
       {
         "dingtalkId": "$:LWCP_v1:$v*********f1+2ow21Zzg"
       }
     ],
     "chatbotCorpId": "ding9f50*****6741",
     "chatbotUserId": "$:LWCP_v1:$v*********1+2ow21Zzg",
     "msgId": "msg2*****p+w==",
     "senderNick": "小钉",
     "isAdmin": true,
     "senderStaffId": "452523285939877041",
     "sessionWebhookExpiredTime": 1695204671648,
     "createAt": 1695199269062,
     "senderCorpId": "ding9f50*****6741",
     "conversationType": "2",
     "senderId": "$:LWCP_v1:$C*********pnNGsP0HS+",
     "conversationTitle": "统一应用模型-测试群",
     "isInAtList": true,
     "sessionWebhook": "https://oapi.dingtalk.com/robot/sendBySession?session=c610ee93e4d96899d9236bd4bea185dd",
     "text": {
       "content": " 你好"
     },
     "robotCode": "ding1f*******dabddc",
     "msgtype": "text"
   }
   ```

   | **参数名称** | **说明** |
   | --- | --- |
   | conversationId | 会话 ID。 |
   | atUsers | 被@人的信息：  - **dingtalkId**：加密的发送者 ID。 |
   | chatbotCorpId | 机器人所在的企业 corpId。 |
   | chatbotUserId | 加密的机器人 ID，暂无使用场景，可忽略。 |
   | msgId | 加密的消息 ID，暂无使用场景，可忽略。 |
   | senderNick | 发送者昵称。 |
   | isAdmin | 是否为管理员。 |
   | senderStaffId | 企业内部群中@该机器人的用户 ID。 |
   | sessionWebhookExpiredTime | 当前会话的 Webhook 地址过期时间。 |
   | createAt | 消息的时间戳，单位毫秒。 |
   | senderCorpId | 企业内部群有的发送者当前群的企业 corpId。 |
   | conversationType | 会话类型：  - **1**：单聊 - **2**：群聊 |
   | senderId | 加密的发送者 ID。  **[!NOTE]**  使用 senderStaffId，为发送者 userId 值。 |
   | conversationTitle | 群聊时才有的会话标题。 |
   | isInAtList | 是否在@列表中。 |
   | sessionWebhook | 当前会话的 Webhook 地址。 |
   | text | 文本消息：  - content：文本内容 |
   | robotCode | 机器人编码。 |
   | msgtype | 消息类型，请参考[消息发送与接收类型](../02-4a8AMF6u2A-服务端-API/0699-robot-message-type.md)。 |

### **HTTP 模式**

1. Java 开发环境准备：

   - 运行环境：JDK 1.7 及以上
2. 服务端接入示例：

   ```
   @RestController
   public class RobotsController {
     	// 下方 value = "/robots", 决定下方设置机器人消息接收地址，例如：https://example.com/robots
       @RequestMapping(value = "/robots", method = RequestMethod.POST)
       public String helloRobots(@RequestBody(required = false) JSONObject json) {
           System.out.println(json);
         	//机器人接收消息内容
           String content = json.getJSONObject("text").get("content").toString().replaceAll(" ", "");

           return null;
       }
   }
   ```
3. 开发完成后，你需要[添加机器人入群](0079-add-robot-to-group.md)，当你@机器人发送“你好”，服务端接收消息格式如下：

   ```
   {
     "conversationId": "cidjMOsz******AhS4Jg==",
     "atUsers": [
       {
         "dingtalkId": "$:LWCP_v1:$v*********f1+2ow21Zzg",
         "staffId": "452523285939877041"
       }
     ],
     "chatbotCorpId": "ding9f50*****6741",
     "chatbotUserId": "$:LWCP_v1:$v*********1+2ow21Zzg",
     "msgId": "msg2*****p+w==",
     "senderNick": "小钉",
     "isAdmin": true,
     "senderStaffId": "452523285939877041",
     "sessionWebhookExpiredTime": 1695204671648,
     "createAt": 1695199269062,
     "senderCorpId": "ding9f50*****6741",
     "conversationType": "2",
     "senderId": "$:LWCP_v1:$C*********pnNGsP0HS+",
     "conversationTitle": "统一应用模型-测试群",
     "isInAtList": true,
     "sessionWebhook": "https://oapi.dingtalk.com/robot/sendBySession?session=c610ee93e4d96899d9236bd4bea185dd",
     "content": " 你好"
     "msgtype": "text"
   }
   ```

   | **参数名称** | **说明** |
   | --- | --- |
   | conversationId | 会话 ID。 |
   | atUsers | 被@人的信息：  - **dingtalkId**：加密的发送者 ID。 - **staffId**：当前企业内部群中员工 userId 值。 |
   | chatbotCorpId | 机器人所在的企业 corpId。 |
   | chatbotUserId | 加密的机器人 ID，暂无使用场景，可忽略。 |
   | msgId | 加密的消息 ID，暂无使用场景，可忽略。 |
   | senderNick | 发送者昵称。 |
   | isAdmin | 是否为管理员。 |
   | senderStaffId | 企业内部群中@该机器人的用户 ID。 |
   | sessionWebhookExpiredTime | 当前会话的 Webhook 地址过期时间。 |
   | createAt | 消息的时间戳，单位毫秒。 |
   | senderCorpId | 企业内部群有的发送者当前群的企业 corpId。 |
   | conversationType | 会话类型：  - **1**：单聊 - **2**：群聊 |
   | senderId | 加密的发送者 ID。  **[!NOTE]**  使用 senderStaffId，为发送者 userId 值。 |
   | conversationTitle | 群聊时才有的会话标题。 |
   | isInAtList | 是否在@列表中。 |
   | sessionWebhook | 当前会话的 Webhook 地址。 |
   | content | 消息文本。 |
   | msgtype | 消息类型，请参考[消息发送与接收类型](../02-4a8AMF6u2A-服务端-API/0699-robot-message-type.md)。 |

## **后续步骤**

机器人接收消息开发完成后，你可以针对接收的消息进行回复或发送消息，可继续以下操作：

- [机器人回复/发送消息](0081-robot-reply-and-send-messages.md)
