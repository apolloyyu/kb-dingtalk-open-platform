---
title: "群模板机器人发送群聊消息"
source_url: "https://open.dingtalk.com/document/development/group-template-robot-sends-group-chat-message"
namespace: "development"
slug: "group-template-robot-sends-group-chat-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 使用教程 > 群模板机器人发送群聊消息"
doc_id: "lrp4ohBZhD"
updated_at: "2026-05-15 13:07:49"
---

> Source: https://open.dingtalk.com/document/development/group-template-robot-sends-group-chat-message
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 使用教程 > 群模板机器人发送群聊消息
> Updated: 2026-05-15 13:07:49

# 群模板机器人发送群聊消息

如果你需要通过群模板机器人发送群聊消息，可以参考本文档操作步骤。

## **明确需求**

在正式开发之前，你可以提前了解，本文档将帮助你使用群模板机器人通过[发送群助手消息](0763-group-template-robot-message.md)接口发送群聊消息。为了帮助你快速上手，你可以尝试运行“快速体验”提供的示例 demo。这将帮助你对群模板机器人的使用有一个直观的体验。

## **前提条件**

1. 完成[创建群模板机器人](../01-XOnnmGCTbn-开发指南/0092-creation-and-installation-of-swarm-template-robots.md)流程。
2. 完成 OpenAPI 接口的[调用权限申请](0003-add-api-permission.md)，需申请`钉钉群消息管理权限`。
3. 开发环境准备：

   - Java：已安装 JDK 1.8 及以上
   - Java：已安装 Maven 3

## **快速体验**

1. 你可以下载 [group-template-robot-group-message-quick-start](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240221/oqqnlh/group-template-robot-group-message-quick-start.zip) 示例 demo。
2. 替换 groupTemplateRobotGroupMessage 的 main 方法参数：

   | 配置项 | 说明 |
   | --- | --- |
   | GROUP\_TEMPLATE\_ID | 登录开发者后台，单击**开放能力** > **场景群** > **群模板，**复制 ID。  image.png |
   | ROBOT\_CODE | 登录开发者后台，单击**开放能力** > **场景群** > **群模板** > **目标群模板**。复制机器人 ID。  image.png  如果群模板没有关联机器人，参考[关联群模板机器人到群模板](../01-XOnnmGCTbn-开发指南/0097-associate-group-template-robot-to-group-template.md)。 |
   | OWNER\_USER\_ID | 用户的 userId 信息，详情参考[用户 UserId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-aa9-zk1-os6)。 |
   | CLIENT\_ID | 应用的 Client ID，详情参考[Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 |
   | CLIENT\_SECRET | 应用的 Client Secret，详情参考[Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 |
3. 启动 main 方法，就可以在群内收到机器人发送的消息了。

## **操作步骤**

1. 添加依赖项到工程的`pom.xml`文件。

   ```
   <dependencies>
           <dependency>
               <groupId>com.aliyun</groupId>
               <artifactId>alibaba-dingtalk-service-sdk</artifactId>
               <version>2.0.0</version>
           </dependency>

           <dependency>
               <groupId>com.aliyun</groupId>
               <artifactId>dingtalk</artifactId>
               <version>2.0.76</version>
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
   import com.alibaba.fastjson.JSON;
   import com.alibaba.fastjson.JSONObject;
   import com.aliyun.dingtalkoauth2_1_0.Client;
   import com.aliyun.dingtalkoauth2_1_0.models.GetAccessTokenRequest;
   import com.aliyun.dingtalkoauth2_1_0.models.GetAccessTokenResponse;
   import com.aliyun.teaopenapi.models.Config;
   import com.dingtalk.api.DefaultDingTalkClient;
   import com.dingtalk.api.DingTalkClient;
   import com.dingtalk.api.request.OapiImChatScencegroupMessageSendV2Request;
   import com.dingtalk.api.request.OapiImChatScenegroupCreateRequest;
   import com.dingtalk.api.response.OapiImChatScencegroupMessageSendV2Response;
   import com.dingtalk.api.response.OapiImChatScenegroupCreateResponse;
   import com.taobao.api.ApiException;

   public class groupTemplateRobotGroupMessage {

       //群模板 id
       public static final String GROUP_TEMPLATE_ID = "<your group template id >";

       //群模板机器人 id
       public static final String ROBOT_CODE = "<your group robot id>";

       //群主userId
       public static final String OWNER_USER_ID= "<owner userId>";

       //应用 client id
       public static final String CLIENT_ID= "<your app client id>";

       //应用 client secret
       public static final String CLIENT_SECRET= "< your app client secret>";

       /**
        * 发送群模板机器人消息
        * @param args
        */
       public static void main(String[] args) {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2");
           OapiImChatScencegroupMessageSendV2Request req = new OapiImChatScencegroupMessageSendV2Request();
           req.setTargetOpenConversationId(CreateGroup());
           req.setMsgTemplateId("inner_app_template_markdown");
           JSONObject jsonObject = new JSONObject().fluentPut("title","测试").fluentPut("markdown_content", "# 测试内容 \n > 测试");
           req.setMsgParamMap(JSON.toJSONString(jsonObject));
           req.setRobotCode(ROBOT_CODE);
           OapiImChatScencegroupMessageSendV2Response rsp = null;
           try {
               rsp = client.execute(req, accessToken());
               System.out.println(rsp.getBody());
           } catch (ApiException e) {
               throw new RuntimeException(e);
           }
       }

       /**
        * 获取群 OpenConversationId
        * @return
        */
       public static String CreateGroup() {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/create");
           OapiImChatScenegroupCreateRequest req = new OapiImChatScenegroupCreateRequest();
           req.setTitle("群模板机器人测试群");
           req.setTemplateId(GROUP_TEMPLATE_ID);
           req.setOwnerUserId(OWNER_USER_ID);
           OapiImChatScenegroupCreateResponse rsp = null;
           try {
               rsp = client.execute(req, accessToken());
               return rsp.getResult().getOpenConversationId();
           } catch (ApiException e) {
               throw new RuntimeException(e);
           }

       }

       public static String accessToken(){
           GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest();
           getAccessTokenRequest.setAppKey(CLIENT_ID);
           getAccessTokenRequest.setAppSecret(CLIENT_SECRET);
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           try {
               Client client = new Client(config);
               GetAccessTokenResponse accessToken = client.getAccessToken(getAccessTokenRequest);
               return accessToken.getBody().getAccessToken();
           } catch (Exception e) {
               throw new RuntimeException(e);
           }
       }
   }
   ```

   此时，将自动创建一个群聊会话，并且你可以在群内看到群模板机器人发送的消息了。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9834868071/p768611.png)

## **相关文档**

- [发送群助手消息](0763-group-template-robot-message.md)
