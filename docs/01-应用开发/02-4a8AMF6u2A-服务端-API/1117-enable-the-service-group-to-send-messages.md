---
title: "实现服务群发送消息"
source_url: "https://open.dingtalk.com/document/development/enable-the-service-group-to-send-messages"
namespace: "development"
slug: "enable-the-service-group-to-send-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 使用教程 > 实现服务群发送消息"
doc_id: "n20TTzaUKI"
updated_at: "2026-07-20 09:21:41"
---

> Source: https://open.dingtalk.com/document/development/enable-the-service-group-to-send-messages
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 服务群 > 使用教程 > 实现服务群发送消息
> Updated: 2026-07-20 09:21:41

# 实现服务群发送消息

本文档介绍了如何调用服务群接口在服务群发送消息等流程。首先创建一个企业内部应用，再使用服务群提供的API，实现创建场景服务群、发送服务群消息和群发任务流程。

## **预期效果**

### **消息发送**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1050154871/p515752.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1050154871/p515754.png)

## 流程简介

步骤一，登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二，获取AppKey和AppSecret。

步骤三，[申请服务群接口权限](0003-add-api-permission.md)。搜索“服务群”，申请相应的权限。

步骤四，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五，调用服务端服务群相关API。

1. 调用服务端API-[创建场景服务群](1120-create-a-scenario-service-group.md)接口，进行创建场景服务群，获取服务群openConversationId。
2. 根据服务群openConversationId，调用服务端API-[添加服务群成员](1121-add-service-group-members.md)接口，新增服务群成员。
3. 根据服务群openConversationId发送消息。

   - 单个群发送消息，根据服务群openConversationId，调用服务端API-[发送服务群消息](1119-service-group-message-sending-interface.md)接口，实现单个群消息的发送
   - 群发消息，根据不同服务群openConversationId，调用服务端API-[群发任务](1118-service-group-sending-task-interface.md)接口，实现不同服务群进行群发消息。
4. 根据服务群openConversationId，调用服务端API-[查询服务群活跃用户](1122-queries-active-service-users.md)接口，查看服务群的活跃用户。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二：获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三：添加接口权限

[申请服务群接口权限](0003-add-api-permission.md)。搜索“服务群”，申请相应的权限。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1050154871/p515760.png)

## 步骤四：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

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

## **步骤五：**调用服务端服务群相关API

1. 调用服务端API-[创建场景服务群](1120-create-a-scenario-service-group.md)接口，进行创建场景服务群，获取服务群openConversationId。

   ```
    public void groupsCreate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkservice_group_1_0.Client client = new com.aliyun.dingtalkservice_group_1_0.Client(config);
           CreateGroupHeaders createGroupHeaders = new CreateGroupHeaders();
           createGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateGroupRequest createGroupRequest = new CreateGroupRequest()
                   .setGroupBizId("serviceGroup202211101001")
                   .setOpenTeamId("xGDx**ZXlkiE")
                   .setOpenGroupSetId("3DPxe***VkwiE")
                   .setGroupName("场景服务群")
                   .setOwnerStaffId("manager7675")
                   .setMemberStaffIds(java.util.Arrays.asList(
                           "manager7675","01472825524039877041"
                   ))
                   .setGroupTagNames(java.util.Arrays.asList(
                           "tag"
                   ));
           try {
               CreateGroupResponse groupWithOptions = client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(groupWithOptions.getBody()));
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
2. 根据服务群openConversationId，调用服务端API-[添加服务群成员](1121-add-service-group-members.md)接口，新增服务群成员。

   ```
    public void serviceGroupMember() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkservice_group_1_0.Client client = new com.aliyun.dingtalkservice_group_1_0.Client(config);
           com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupHeaders addMemberToServiceGroupHeaders = new com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupHeaders();
           addMemberToServiceGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupRequest addMemberToServiceGroupRequest = new com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupRequest()
                   .setOpenTeamId("xGDx**ZXlkiE")
                   .setOpenConversationId("cidn0Wqg****znMOiEmpcJCpQ==")
                   .setUserIds(java.util.Arrays.asList(
                           "01296106445126923197"
                   ));
           try {
               AddMemberToServiceGroupResponse addMemberToServiceGroupResponse = client.addMemberToServiceGroupWithOptions(addMemberToServiceGroupRequest, addMemberToServiceGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(addMemberToServiceGroupResponse.getBody()));
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
3. 根据服务群openConversationId发送消息。

   - 单个群发送消息，根据服务群openConversationId，调用服务端API-[发送服务群消息](1119-service-group-message-sending-interface.md)接口，实现单个群消息的发送

     ```
     public void messagesSend() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkservice_group_1_0.Client client = new com.aliyun.dingtalkservice_group_1_0.Client(config);
             SendServiceGroupMessageHeaders sendServiceGroupMessageHeaders = new SendServiceGroupMessageHeaders();
             sendServiceGroupMessageHeaders.xAcsDingtalkAccessToken = "accessToken";

             SendServiceGroupMessageRequest sendServiceGroupMessageRequest = new SendServiceGroupMessageRequest()
                     .setTargetOpenConversationId("cidn0Wqg****znMOiEmpcJCpQ==")
                     .setTitle("服务提醒")
                     .setAtUnionIds(Arrays.asList("E9CS6Xu5*****VOO905eN7QiEiE"))
                     .setReceiverUnionIds(Arrays.asList("E9CS6Xu5*****VOO905eN7QiEiE"))
                     .setContent("#### 杭州天气 \n> 9度，西北风1级，空气良89，相对温度73%\n> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### 10点20分发布 [天气](https://www.dingtalk.com) \n")
                     .setMessageType("MARKDOWN");
             try {
                 SendServiceGroupMessageResponse sendServiceGroupMessageResponse = client.sendServiceGroupMessageWithOptions(sendServiceGroupMessageRequest, sendServiceGroupMessageHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(sendServiceGroupMessageResponse.getBody()));
             } catch (TeaException err) {
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题]
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
   - 群发消息，根据不同服务群openConversationId，调用服务端API-[群发任务](1118-service-group-sending-task-interface.md)接口，实现不同服务群进行群发消息。

     ```
     public void tasksSend() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkservice_group_1_0.Client client = new com.aliyun.dingtalkservice_group_1_0.Client(config);
             SendMsgByTaskHeaders sendMsgByTaskHeaders = new SendMsgByTaskHeaders();
             sendMsgByTaskHeaders.xAcsDingtalkAccessToken = "accessToken";

             SendMsgByTaskRequest.SendMsgByTaskRequestMessageContentBtns messageContentBtns0 = new SendMsgByTaskRequest.SendMsgByTaskRequestMessageContentBtns()
                     .setActionURL("https://www.dingtalk.com")
                     .setTitle("标题1");
             SendMsgByTaskRequest.SendMsgByTaskRequestMessageContentBtns messageContentBtns1 = new SendMsgByTaskRequest.SendMsgByTaskRequestMessageContentBtns()
                     .setActionURL("https://www.dingtalk.com")
                     .setTitle("标题2");
             SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent messageContent = new SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent()
                     .setAtAll(false)
                     .setAtActiveUser(false)
                     .setTitle("群发消息测试")
                     .setMessageType("ACTIONCARD")
                     .setContent("群发任务")
                     .setImages(Arrays.asList("https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"))
                     .setBtns(Arrays.asList(messageContentBtns0,messageContentBtns1))
                     .setTop(false)
                     .setRemind(false);

             SendMsgByTaskRequest.SendMsgByTaskRequestQueryGroup queryGroup = new SendMsgByTaskRequest.SendMsgByTaskRequestQueryGroup()
                     .setQueryType("AIMED")
                     .setOpenConversationIds(Arrays.asList("cidn0Wqg****znMOiEmpcJCpQ==","cidBHpU+/eD0****TQnKJLw=="))
                     .setGroupTagNames(Arrays.asList("tag"))
                     .setOpenGroupSetId("xGDx**ZXlkiE");

             SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig sendConfig = new SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig()
                     .setSendType("INSTANT")
                     .setNeedUrlTrack(false);

             SendMsgByTaskRequest sendMsgByTaskRequest = new SendMsgByTaskRequest()
                     .setOpenTeamId("xGDx**ZXlkiE")
                     .setTaskName("群发任务测试")
                     .setMessageContent(messageContent)
                     .setQueryGroup(queryGroup)
                     .setSendConfig(sendConfig);
             try {
                 SendMsgByTaskResponse sendMsgByTaskResponse = client.sendMsgByTaskWithOptions(sendMsgByTaskRequest, sendMsgByTaskHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(sendMsgByTaskResponse.getBody()));
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
4. 根据服务群openConversationId，调用服务端API-[查询服务群活跃用户](1122-queries-active-service-users.md)接口，查看服务群的活跃用户。

   ```
   public void queryActiveUsers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkservice_group_1_0.Client client = new com.aliyun.dingtalkservice_group_1_0.Client(config);
           QueryActiveUsersHeaders queryActiveUsersHeaders = new QueryActiveUsersHeaders();
           queryActiveUsersHeaders.xAcsDingtalkAccessToken = "accessToken";
           QueryActiveUsersRequest queryActiveUsersRequest = new QueryActiveUsersRequest()
                   .setOpenTeamId("xGDx**ZXlkiE")
                   .setOpenConversationId("cidn0Wqg****znMOiEmpcJCpQ==");
           try {
               QueryActiveUsersResponse queryActiveUsersResponse = client.queryActiveUsersWithOptions(queryActiveUsersRequest, queryActiveUsersHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryActiveUsersResponse.getBody()));
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
