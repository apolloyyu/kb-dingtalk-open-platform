---
title: "创建、更新、查询及更新会议室分组"
source_url: "https://open.dingtalk.com/document/development/meeting-room-grouping-operation-process"
namespace: "development"
slug: "meeting-room-grouping-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 创建、更新、查询及更新会议室分组"
doc_id: "UPf5bLxcdW"
updated_at: "2026-07-10 10:11:11"
---

> Source: https://open.dingtalk.com/document/development/meeting-room-grouping-operation-process
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 创建、更新、查询及更新会议室分组
> Updated: 2026-07-10 10:11:11

# 创建、更新、查询及更新会议室分组

本文档展示了，创建一个企业内部应用，使用智能会议室提供的API，实现创建、更新、查询及更新会议室分组相关流程。

## **预期效果**

会议室分组效果，如下所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4017088771/p524073.png)

## **流程简介**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请智能会议室相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用会议室相关API：

1. 调用服务端API-[创建会议室分组](0444-create-meeting-room-groups.md)接口，获取会议室分组返回结果`result`字段**，**即会议室分组ID**。**
2. 根据会议室分组ID，调用服务端API-[更新会议室分组信息](0447-update-meeting-room-groups.md)接口，实现会议室分组信息更新操作。
3. 调用服务端API-[查询会议室分组列表](0448-query-meeting-rooms-groups.md)接口，实现获取会议室分组列表内容。
4. 根据会议室分组ID，调用服务端API-[查询会议室分组信息](0449-query-meeting-room-groups.md)接口，实现获取单个会议室分组具体内容信息。
5. 根据会议室分组ID，调用服务端API-[删除会议室分组](0445-delete-a-conference-room-group.md)接口，实现删除会议室分组操作。

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

## **步骤四：**调用会议室分组相关API

1. 调用服务端API-[创建会议室分组](0444-create-meeting-room-groups.md)接口，获取会议室分组返回结果`result`字段**，**即会议室分组ID**。**

   ```
   public void createRoomsGroups() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupHeaders createMeetingRoomGroupHeaders = new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupHeaders();
           createMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupRequest createMeetingRoomGroupRequest = new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE")
                   .setGroupName("第一分组")
                   .setParentGroupId(0L);
           try {
               CreateMeetingRoomGroupResponse meetingRoomGroupWithOptions = client.createMeetingRoomGroupWithOptions(createMeetingRoomGroupRequest, createMeetingRoomGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(meetingRoomGroupWithOptions.getBody()));
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
2. 根据会议室分组ID，调用服务端API-[更新会议室分组信息](0447-update-meeting-room-groups.md)接口，实现会议室分组信息更新操作。

   ```
    public void updateRoomsGroups() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupHeaders updateMeetingRoomGroupHeaders = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupHeaders();
           updateMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupRequest updateMeetingRoomGroupRequest = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE")
                   .setGroupName("我的第一分组")
                   .setGroupId(39L);
           try {
               UpdateMeetingRoomGroupResponse updateMeetingRoomGroupResponse = client.updateMeetingRoomGroupWithOptions(updateMeetingRoomGroupRequest, updateMeetingRoomGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateMeetingRoomGroupResponse.getBody()));
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
3. 调用服务端API-[查询会议室分组列表](0448-query-meeting-rooms-groups.md)接口，实现获取会议室分组列表内容。

   ```
    public void RoomsGroupsList() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListHeaders queryMeetingRoomGroupListHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListHeaders();
           queryMeetingRoomGroupListHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListRequest queryMeetingRoomGroupListRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE");
           try {
               QueryMeetingRoomGroupListResponse queryMeetingRoomGroupListResponse = client.queryMeetingRoomGroupListWithOptions(queryMeetingRoomGroupListRequest, queryMeetingRoomGroupListHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryMeetingRoomGroupListResponse.getBody()));
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
4. 根据会议室分组ID，调用服务端API-[查询会议室分组信息](0449-query-meeting-room-groups.md)接口，实现获取单个会议室分组具体内容信息。

   ```
   public void RoomsGroupsInfo() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupHeaders queryMeetingRoomGroupHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupHeaders();
           queryMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupRequest queryMeetingRoomGroupRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE");
           try {
               QueryMeetingRoomGroupResponse queryMeetingRoomGroupResponse = client.queryMeetingRoomGroupWithOptions("39", queryMeetingRoomGroupRequest, queryMeetingRoomGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryMeetingRoomGroupResponse.getBody()));
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
5. 根据会议室分组ID，调用服务端API-[删除会议室分组](0445-delete-a-conference-room-group.md)接口，实现删除会议室分组操作。

   > **[!NOTE]**
   >
   > 若会议室分组下存在会议室，则该会议室分组无法删除。

   ```
    public void  deleteRoomsGroups() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);
           com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupHeaders deleteMeetingRoomGroupHeaders = new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupHeaders();
           deleteMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupRequest deleteMeetingRoomGroupRequest = new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupRequest()
                   .setUnionId("E9CS6X*******eN7QiEiE");
           try {
               DeleteMeetingRoomGroupResponse deleteMeetingRoomGroupResponse = client.deleteMeetingRoomGroupWithOptions("40", deleteMeetingRoomGroupRequest, deleteMeetingRoomGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(deleteMeetingRoomGroupResponse.getBody()));
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
