---
title: "企业机器人发送单聊消息"
source_url: "https://open.dingtalk.com/document/development/the-application-robot-in-the-enterprise-sends-a-single-chat"
namespace: "development"
slug: "the-application-robot-in-the-enterprise-sends-a-single-chat"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 使用教程 > 企业机器人发送单聊消息"
doc_id: "00qwY23Yye"
updated_at: "2026-07-14 09:21:54"
---

> Source: https://open.dingtalk.com/document/development/the-application-robot-in-the-enterprise-sends-a-single-chat
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 使用教程 > 企业机器人发送单聊消息
> Updated: 2026-07-14 09:21:54

# 企业机器人发送单聊消息

如果你需要通过企业机器人给你发送单聊消息，可以参考本文档操作步骤。

## **明确需求**

在正式开发之前，你可以提前了解，本文档将帮助你在 Stream 模式下，当你与机器人进行单独聊天时，你可以发送消息给机器人，接着通过调用 [批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口，使机器人回复你的消息。你可以尝试运行“快速体验”提供的示例 demo。这将帮助你对企业机器人的使用有一个直观的体验。

## **前提条件**

1. 完成[配置企业机器人](../01-XOnnmGCTbn-开发指南/0076-configure-the-robot-application.md)流程（消息接收模式选择 Stream 模式）。
2. 完成 OpenAPI 接口的[调用权限申请](0003-add-api-permission.md)，需申请`企业内机器人发送消息权限`。
3. 开发环境准备：

   | **开发环境** | **说明** |
   | --- | --- |
   | Java | - 已安装 JDK 1.8 及以上 - 已安装 Maven 3 |
   | Python | - Python 3 |

## **快速体验**

1. 你可以下载示例 demo：

   | **示例** | **说明** |
   | --- | --- |
   | Java | [stream-robot-private-message-quick-start-java.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250519/llkrhu/stream-robot-private-message-quick-start-java.zip) |
   | Python | [stream-robot-private-message-quick-start-python.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250519/senypi/stream-robot-private-message-quick-start-python.zip) |
2. 启动示例 demo：

   | **类型** | **说明** |
   | --- | --- |
   | Java | 1. 修改 application.properties 配置文件的参数：  - app.appKey：应用的 Client ID，详情参考 [Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 - app.appSecret：应用的 Client Secret，详情参考[Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 - robot.code：机器人的编码，详情参考[机器人ID](0698-development-robot-overview.md)。 2. 启动 Application.java 文件。  3. 在单聊会话中发送消息给机器人，例如：“你好”。  image.png  此时，你可以看到机器人发送的消息内容。​ |
   | Python | 1. 引入依赖：`pip install alibabacloud-dingtalk dingtalk-stream`。  2. 在当前文件目录下输入启动命令：`python3 send_robot_private_message.py --client_id="your app client id" --client_secret="your app client secret" --robot_code="your robot code"`。  注意替换 client\_id、client\_secret 和 robot\_code，参数如何获取请参考 Java 中的说明。  3. 在单聊会话中发送消息给机器人，例如：“你好”。 |

## **操作步骤**

> 下方为 Java 示例，Python 示例请下载上方体验 demo。

1. 添加依赖项到工程的`pom.xml`文件。

   ```
   <dependencies>
     <dependency>
       <groupId>com.dingtalk.open</groupId>
       <artifactId>dingtalk-stream</artifactId>
       <version>1.1.0</version>
     </dependency>
     <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
       <version>2.7.4</version>
     </dependency>

     <dependency>
       <groupId>com.aliyun</groupId>
       <artifactId>dingtalk</artifactId>
       <version>2.0.76</version>
     </dependency>

     <dependency>
       <groupId>org.projectlombok</groupId>
       <artifactId>lombok</artifactId>
       <version>1.18.26</version>
       <optional>true</optional>
     </dependency>

     <dependency>
       <groupId>com.alibaba</groupId>
       <artifactId>fastjson</artifactId>
       <version>1.2.68</version>
     </dependency>
   </dependencies>
   ```
2. 创建 main 方法，并启动。

   ```
   import com.alibaba.fastjson.JSONObject;
   import com.aliyun.dingtalkoauth2_1_0.models.GetAccessTokenRequest;
   import com.aliyun.dingtalkoauth2_1_0.models.GetAccessTokenResponse;
   import com.aliyun.dingtalkrobot_1_0.Client;
   import com.aliyun.dingtalkrobot_1_0.models.BatchSendOTOHeaders;
   import com.aliyun.dingtalkrobot_1_0.models.BatchSendOTORequest;
   import com.aliyun.dingtalkrobot_1_0.models.BatchSendOTOResponse;
   import com.aliyun.tea.TeaException;
   import com.aliyun.teaopenapi.models.Config;
   import com.aliyun.teautil.models.RuntimeOptions;
   import com.dingtalk.open.app.api.OpenDingTalkClient;
   import com.dingtalk.open.app.api.OpenDingTalkStreamClientBuilder;
   import com.dingtalk.open.app.api.callback.OpenDingTalkCallbackListener;
   import com.dingtalk.open.app.api.security.AuthClientCredential;
   import lombok.extern.slf4j.Slf4j;

   import java.util.Objects;

   @Slf4j
     public class sendPrivateMessage {

       public static final String CLIENT_ID = "< your client id>";

       public static final String CLIENT_SECRET = "<your client secret>";

       public static void main(String[] args) throws Exception {
         OpenDingTalkClient client = OpenDingTalkStreamClientBuilder
           .custom()
           .credential(new AuthClientCredential(CLIENT_ID, CLIENT_SECRET))
           .registerCallbackListener("/v1.0/im/bot/messages/get", new sendPrivateMessage.RobotMsgCallbackConsumer())
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
           String userId = request.get("senderStaffId").toString();
           String content = request.getJSONObject("text").getString("content");
           String robotCode = request.get("robotCode").toString();
           log.info("receive bot message from user={}, msg={},robotCode={} ", userId, content,robotCode);

           BatchSendOTOHeaders batchSendOTOHeaders = new BatchSendOTOHeaders();
           batchSendOTOHeaders.setXAcsDingtalkAccessToken(getToken());

           BatchSendOTORequest batchSendOTORequest = new BatchSendOTORequest();
           batchSendOTORequest.setMsgKey("sampleText");
           batchSendOTORequest.setRobotCode(robotCode);
           batchSendOTORequest.setUserIds(java.util.Arrays.asList(userId));

           JSONObject msgParam = new JSONObject();
           msgParam.put("content", "java-getting-start say : " + "hello");
           batchSendOTORequest.setMsgParam(msgParam.toJSONString());
           try {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkrobot_1_0.Client client = new Client(config);
             BatchSendOTOResponse batchSendOTOResponse = client.batchSendOTOWithOptions(batchSendOTORequest, batchSendOTOHeaders, new RuntimeOptions());
                   if (Objects.isNull(batchSendOTOResponse) || Objects.isNull(batchSendOTOResponse.getBody())) {
                       log.error("RobotPrivateMessages_send batchSendOTOResponse return error, response={}",
                               batchSendOTOResponse);
                       return null;
                   }
                   return new JSONObject();
               } catch (TeaException e) {
                   log.error("RobotPrivateMessages_send batchSendOTOResponse throw TeaException, errCode={}, " +
                           "errorMessage={}", e.getCode(), e.getMessage(), e);
                   throw e;
               } catch (Exception e) {
                   log.error("RobotPrivateMessages_send batchSendOTOResponse throw Exception", e);
                   try {
                       throw e;
                   } catch (Exception ex) {
                       throw new RuntimeException(ex);
                   }
               }
           }

           public static String getToken() {
               GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest();
               getAccessTokenRequest.setAppKey(CLIENT_ID);
               getAccessTokenRequest.setAppSecret(CLIENT_SECRET);
               Config config = new Config();
               config.protocol = "https";
               config.regionId = "central";
               try {
                   com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
                   GetAccessTokenResponse accessToken = client.getAccessToken(getAccessTokenRequest);
                   return accessToken.getBody().getAccessToken();
               } catch (Exception e) {
                   throw new RuntimeException(e);
               }
           }
       }
   }
   ```
3. 你可以在单聊会话中发送消息给机器人。​

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7834868071/p768550.png)

   此时，你可以看到机器人发送的消息内容。​

## **相关文档**

- [机器人接收消息](../01-XOnnmGCTbn-开发指南/0078-robot-receive-message.md)
- [消息发送与接收类型](0699-robot-message-type.md)
- [配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)
- [批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md)

> 如果企业机器人发送消息的消息类型无法满足你的需求，你可以参考[互动卡片](0777-overview-card.md)。
