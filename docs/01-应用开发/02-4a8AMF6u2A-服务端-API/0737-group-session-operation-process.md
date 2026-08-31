---
title: "创建、查询、修改及管理群会话"
source_url: "https://open.dingtalk.com/document/development/group-session-operation-process"
namespace: "development"
slug: "group-session-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 使用教程 > 创建、查询、修改及管理群会话"
doc_id: "2JVIs4IAgf"
updated_at: "2026-07-14 09:22:01"
---

> Source: https://open.dingtalk.com/document/development/group-session-operation-process
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 使用教程 > 创建、查询、修改及管理群会话
> Updated: 2026-07-14 09:22:01

# 创建、查询、修改及管理群会话

本文档介绍了如何调用群会话相关接口实现群会话操作的相关流程。首先创建一个企业内部应用，再使用群会话提供的API，实现创建群会话、获取群会话信息、群会话管理操作、修改群会话流程。

## 流程简介

步骤一：获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“场景群”和“群管理”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤四：调用服务端群会话相关API。

1. 调用服务端API-[创建群会话](0738-create-common-group-new-version-v2.md)接口，进行创建群会话，获取群会话`chatId`。
2. 根据群会话`chatId`，调用服务端API-[查询群信息](0740-obtain-a-group-session.md)接口，获取群会话的信息。
3. 根据群会话chatId进行群会话管理操作。

   - 根据群会话`chatId`，调用新版服务端API-[获取群会话的OpenConversationId](0745-obtain-group-openconversationid.md)接口，获取群会话`openConversationId`。
   - 根据群会话`chatId`，调用服务端API-[批量设置企业群管理员](0742-batch-setup-group-administrator.md)接口，进行群会话管理员的设置。
   - 根据群会话`chatId`，调用服务端API-[设置禁止群成员私聊](0743-set-private-chat.md)接口，设置群会话群成员间是否可以私聊。
   - 根据群会话`chatId`，调用服务端API-[更新群成员的群昵称](0741-set-a-group-nickname.md)接口，进行设置群会话成员的昵称。
   - 根据群会话`chatId`，调用服务端API-[获取入群二维码链接](0744-obtain-a-qr-code-link.md)接口，其他的企业成员点击链接即可申请加入群聊。
4. 根据群会话`chatId`，调用服务端API-[更新群会话](0739-api-updategroup.md)接口，进行群会话信息的修改。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

单击**开发配置**>**权限管理**，在权限搜索框中分别输入`qyapi_chat_manage`、`qyapi_chat_read`和`qyapi_chat_base_read`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用新服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

```
 public void getAccessToken() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("din*********hgn")
                .setAppSecret("9G_O************mBkhgGIO");
        GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
        System.out.println(JSON.toJSONString(accessToken.getBody()));
    }
```

## 步骤四：调用服务端群会话相关API

1. 调用服务端API-[创建群会话](0738-create-common-group-new-version-v2.md)接口，进行创建群会话，获取群会话chatId。

   ```
   package com.aliyun.sample;

   import com.aliyun.tea.*;

   public class Sample {

     /**
        * <b>description</b> :
        * <p>使用 Token 初始化账号Client</p>
        * @return Client
        * 
        * @throws Exception
        */
     public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       return new com.aliyun.dingtalkim_1_0.Client(config);
     }

     public static void main(String[] args_) throws Exception {
           
       com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
       com.aliyun.dingtalkim_1_0.models.CreateGroupHeaders createGroupHeaders = new com.aliyun.dingtalkim_1_0.models.CreateGroupHeaders();
       createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
       com.aliyun.dingtalkim_1_0.models.CreateGroupRequest.CreateGroupRequestManagementOptions managementOptions = new com.aliyun.dingtalkim_1_0.models.CreateGroupRequest.CreateGroupRequestManagementOptions()
         .setMentionAllAuthority(0)
         .setShowHistoryType(0)
         .setValidationType(0)
         .setSearchable(0)
         .setChatBannedType(0)
         .setManagementType(0);
       com.aliyun.dingtalkim_1_0.models.CreateGroupRequest createGroupRequest = new com.aliyun.dingtalkim_1_0.models.CreateGroupRequest()
         .setName("测试群")
         .setOwner("manager4220")
         .setOwnerType("emp")
         .setUseridlist(java.util.Arrays.asList(
           "userId"
         ))
         .setConversationTag(2L)
         .setExtidlist(java.util.Arrays.asList(
           "unionId"
         ))
         .setIcon("@mediaId")
         .setManagementOptions(managementOptions);
       try {
         client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       } catch (TeaException err) {
         if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       } catch (Exception _err) {
         TeaException err = new TeaException(_err.getMessage(), _err);
         if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       }        
     }
   }
   ```
2. 根据群会话chatId，调用服务端API-[查询群信息](0740-obtain-a-group-session.md)接口，获取群会话的信息。

   ```
   public void getChatInfo() {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/get");
           OapiChatGetRequest req = new OapiChatGetRequest();
           req.setChatid("chate39f540dxxxx");
           req.setHttpMethod("GET");
           OapiChatGetResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getChatInfo());
       }
   ```
3. 根据群会话`chatId`，调用新版服务端API-[获取群会话的OpenConversationId](0745-obtain-group-openconversationid.md)接口，获取群会话`openConversationId`。

   ```
   public void ConversationId() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
           ChatIdToOpenConversationIdHeaders chatIdToOpenConversationIdHeaders = new ChatIdToOpenConversationIdHeaders();
           chatIdToOpenConversationIdHeaders.xAcsDingtalkAccessToken = "accessToken";
           try {
               ChatIdToOpenConversationIdResponse response = client.chatIdToOpenConversationIdWithOptions("chatId", chatIdToOpenConversationIdHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(response.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
4. 根据群会话`openConversationId`，调用新版服务端API-[批量设置企业群管理员](0742-batch-setup-group-administrator.md)接口，批量设置群管理员。

   ```
   public void subAdministrators() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
           ChatSubAdminUpdateHeaders chatSubAdminUpdateHeaders = new ChatSubAdminUpdateHeaders();
           chatSubAdminUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
           ChatSubAdminUpdateRequest chatSubAdminUpdateRequest = new ChatSubAdminUpdateRequest()
                   .setOpenConversationId("cidVwhxxxxxLjUA==")
                   .setUserIds(java.util.Arrays.asList(
                       "wZ1vjnPOIxxxxxMTGJGy"
                   ))
                   .setRole(2);
           try {
               ChatSubAdminUpdateResponse chatSubAdminUpdateResponse = client.chatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(chatSubAdminUpdateResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   - 根据群会话`chatId`，调用服务端API-[设置禁止群成员私聊](0743-set-private-chat.md)接口，设置群会话群成员间是否可以私聊。

     ```
     public void updateChatMemberFriendswitch() {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update");
             OapiChatMemberFriendswitchUpdateRequest req = new OapiChatMemberFriendswitchUpdateRequest();
             req.setChatid("chatdafe234xxxx");
             req.setIsProhibit(true);
             OapiChatMemberFriendswitchUpdateResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
         }
     ```
   - 根据群会话`chatId`，调用服务端API-[更新群成员的群昵称](0741-set-a-group-nickname.md)接口，进行设置群会话成员的昵称。

     ```
     public void updateChatMemberNick() {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/updategroupnick");
             OapiChatUpdategroupnickRequest req = new OapiChatUpdategroupnickRequest();
             req.setUserid("user123");
             req.setChatid("chate39f540d572b71cf97a556d95929fxxxx");
             req.setGroupNick("钉钉小二");
             OapiChatUpdategroupnickResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
         }
     ```
   - 根据群会话`chatId`，调用服务端API-[获取入群二维码链接](0744-obtain-a-qr-code-link.md)接口，其他的企业成员点击链接即可申请加入群聊。

     ```
     public void getChatURL() {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/qrcode/get");
             OapiChatQrcodeGetRequest req = new OapiChatQrcodeGetRequest();
             req.setChatid("chat32****3a");
             req.setUserid("manager4220");
             OapiChatQrcodeGetResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
         }
     ```
5. 根据群会话`chatId`，调用服务端API-[更新群会话](0739-api-updategroup.md)接口，进行群会话信息的修改。

   ```
   package com.aliyun.sample;

   import com.aliyun.tea.*;

   public class Sample {

     /**
        * <b>description</b> :
        * <p>使用 Token 初始化账号Client</p>
        * @return Client
        * 
        * @throws Exception
        */
     public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       return new com.aliyun.dingtalkim_1_0.Client(config);
     }

     public static void main(String[] args_) throws Exception {
           
       com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
       com.aliyun.dingtalkim_1_0.models.UpdateGroupHeaders updateGroupHeaders = new com.aliyun.dingtalkim_1_0.models.UpdateGroupHeaders();
       updateGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
       com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest.UpdateGroupRequestManagementOptions managementOptions = new com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest.UpdateGroupRequestManagementOptions()
         .setMentionAllAuthority(0)
         .setShowHistoryType(0)
         .setValidationType(0)
         .setSearchable(0)
         .setChatBannedType(0)
         .setManagementType(0);
       com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest updateGroupRequest = new com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest()
         .setChatid("chatxxxx")
         .setName("全员群。")
         .setOwner("04201724372xxxx")
         .setOwnerType("emp")
         .setAddUseridlist(java.util.Arrays.asList(
           "userid1"
         ))
         .setDelUseridlist(java.util.Arrays.asList(
           "userid1"
         ))
         .setAddExtidlist(java.util.Arrays.asList(
           "unionId"
         ))
         .setDelExtidlist(java.util.Arrays.asList(
           "unionId"
         ))
         .setIcon("@mediaId")
         .setManagementOptions(managementOptions);
       try {
         client.updateGroupWithOptions(updateGroupRequest, updateGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       } catch (TeaException err) {
         if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       } catch (Exception _err) {
         TeaException err = new TeaException(_err.getMessage(), _err);
         if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       }        
     }
   }
   ```
