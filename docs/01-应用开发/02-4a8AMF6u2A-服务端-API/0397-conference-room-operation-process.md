---
title: "创建、更新、查询及删除会议室"
source_url: "https://open.dingtalk.com/document/development/conference-room-operation-process"
namespace: "development"
slug: "conference-room-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 创建、更新、查询及删除会议室"
doc_id: "HXCX70UL9r"
updated_at: "2026-07-10 10:11:09"
---

> Source: https://open.dingtalk.com/document/development/conference-room-operation-process
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 创建、更新、查询及删除会议室
> Updated: 2026-07-10 10:11:09

# 创建、更新、查询及删除会议室

本文档展示了，创建一个企业内部应用，使用智能会议室提供的API，实现会议室的创建、更新、查询和删除操作的相关流程。

## **预期效果**

会议室展示效果如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2017088771/p524058.png)

## **流程简介**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请智能会议室相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用会议室相关API：

1. 调用服务端API-[创建会议室](0434-create-a-meeting-room.md)接口，获取会议室返回结果`result`字段**，**即会议室ID**。**
2. 根据会议室ID，调用服务端API-[更新会议室信息](0436-update-meeting-room-information.md)接口，实现会议室信息更新操作。
3. 调用服务端API-[查询会议室列表](0437-check-the-meeting-room-list.md)接口，实现获取会议室列表内容。
4. 根据会议室ID，调用服务端API-[查询会议室详情](0438-check-meeting-room-details.md)接口，实现获取单个会议室具体内容信息。
5. 根据会议室ID，调用服务端API-[删除会议室](0435-delete-a-meeting-room.md)接口，实现删除会议室操作。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：**添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`VideoConference.Conference.Write`和`VideoConference.Conference.Read`，并申请权限。

## **步骤三：**获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

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

## **步骤四：**调用会议室相关API

1. 调用服务端API-[创建会议室](0434-create-a-meeting-room.md)接口，获取会议室返回结果`result`字段**，**即会议室ID**。**

   ```
   public void createMeetingRoom() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomHeaders createMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomHeaders();
           createMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";
           com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest.CreateMeetingRoomRequestRoomLocation roomLocation = new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest.CreateMeetingRoomRequestRoomLocation()
                   .setTitle("***测试")
                   .setDesc("xx市xx区xx路xx号");
           com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest createMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE")
                   .setRoomName("测试会议室")
                   .setRoomCapacity(10)
                   .setRoomPicture("https://example/k/钉钉图片1.png")
                   .setRoomStatus(0)
                   .setRoomLocation(roomLocation)
                   .setRoomLabelIds(java.util.Arrays.asList(
                           1L
                   ))
                   .setIsvRoomId("dingTalk1001");
           try {
               CreateMeetingRoomResponse meetingRoomWithOptions = client.createMeetingRoomWithOptions(createMeetingRoomRequest, createMeetingRoomHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(meetingRoomWithOptions.getBody()));
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
2. 根据会议室ID，调用服务端API-[更新会议室信息](0436-update-meeting-room-information.md)接口，实现会议室信息更新操作。

   ```
   public void  updateMeetingRooms() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomHeaders updateMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomHeaders();
           updateMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";
           com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation roomLocation = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation()
                   .setTitle("阿里***A座")
                   .setDesc("**市**区");
           com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest updateMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE")
                   .setRoomId("9d5356997e44f******0ab267c05d6b3a14")
                   .setRoomName("会议室测试")
                   .setRoomCapacity(10)
                   .setRoomPicture("https://example/k/钉钉图片1.png")
                   .setRoomStatus(0)
                   .setRoomLocation(roomLocation)
                   .setRoomLabelIds(java.util.Arrays.asList(
                           1L
                   ))
                   .setIsvRoomId("dingTalk1001");
           try {
               UpdateMeetingRoomResponse updateMeetingRoomResponse = client.updateMeetingRoomWithOptions(updateMeetingRoomRequest, updateMeetingRoomHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateMeetingRoomResponse.getBody()));
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
3. 调用服务端API-[查询会议室列表](0437-check-the-meeting-room-list.md)接口，实现获取会议室列表内容。

   ```
   public void meetingRoomsList() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListHeaders queryMeetingRoomListHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListHeaders();
           queryMeetingRoomListHeaders.xAcsDingtalkAccessToken = "acccessToken";
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListRequest queryMeetingRoomListRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListRequest()
                   .setMaxResults(20)
                   .setUnionId("E9CS6X*******eN7QiEiE");
           try {
               QueryMeetingRoomListResponse queryMeetingRoomListResponse = client.queryMeetingRoomListWithOptions(queryMeetingRoomListRequest, queryMeetingRoomListHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryMeetingRoomListResponse.getBody()));
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
4. 根据会议室ID，调用服务端API-[查询会议室详情](0438-check-meeting-room-details.md)接口，实现获取单个会议室具体内容信息。

   ```
    public void  meetingRoomsInfo() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomHeaders queryMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomHeaders();
           queryMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomRequest queryMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE");
           try {
               QueryMeetingRoomResponse queryMeetingRoomResponse = client.queryMeetingRoomWithOptions("9d5356997e44f******0ab267c05d6b3a14", queryMeetingRoomRequest, queryMeetingRoomHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryMeetingRoomResponse.getBody()));
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
5. 根据会议室ID，调用服务端API-[删除会议室](0435-delete-a-meeting-room.md)接口，实现删除会议室操作。

   > **[!NOTE]**
   >
   > 删除会议室必须拥有智能会议室应用管理权限。
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0101829661/p524038.png)

   ```
    public void  deleteMeetingRoom() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomHeaders deleteMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomHeaders();
           deleteMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";
           com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomRequest deleteMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE");
           try {
               DeleteMeetingRoomResponse deleteMeetingRoomResponse = client.deleteMeetingRoomWithOptions("9d5356997e44f******0ab267c05d6b3a14", deleteMeetingRoomRequest, deleteMeetingRoomHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(deleteMeetingRoomResponse.getBody()));
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
