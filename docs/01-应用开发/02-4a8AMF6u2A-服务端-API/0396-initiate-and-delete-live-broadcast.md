---
title: "发起、更新、查询及删除直播"
source_url: "https://open.dingtalk.com/document/development/initiate-and-delete-live-broadcast"
namespace: "development"
slug: "initiate-and-delete-live-broadcast"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 发起、更新、查询及删除直播"
doc_id: "Syba6uq8dM"
updated_at: "2026-07-10 10:11:08"
---

> Source: https://open.dingtalk.com/document/development/initiate-and-delete-live-broadcast
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 发起、更新、查询及删除直播
> Updated: 2026-07-10 10:11:08

# 发起、更新、查询及删除直播

本文档展示了，创建一个企业内部应用，使用直播提供的API，实现发起及删除直播的相关流程：

## **流程简介**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请直播相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用直播相关API：

1. 调用服务端API-[创建直播](0429-create-live-streaming.md)接口，获取直播ID`liveId`字段**。**
2. 根据直播`liveId`，调用服务端API-[修改直播属性信息](0432-modify-live-streaming.md)接口，实现修改直播基础信息。
3. 根据直播`liveId`，调用服务端API-[查询直播信息](0431-queries-the-live-streaming-information.md)接口，获取直播详细信息。
4. 你可以通过[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)，获取直播观看数据信息。
5. 根据直播`liveId`，调用服务端API-[查询直播观看人员信息](0433-queries-the-viewing-information-of-viewers.md)接口，获取直播观看人员信息。
6. 根据直播`liveId`，调用服务端API-[删除直播](0430-delete-live-streaming.md)接口，实现删除直播操作。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：**添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`Live.Common.Write`和`Live.Common.Read`，并申请权限。

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

## **步骤四：调用直播相关API**

1. 调用服务端API-[创建直播](0429-create-live-streaming.md)接口，获取直播ID`liveId`字段**。**

   > **[!NOTE]**
   >
   > - 获取直播ID后，拼接以下链接：`dingtalk://dingtalkclient/action/start_uniform_live?liveUuid=直播ID`，实现进入显示界面。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8649463871/p524344.png)
   > - 只有发起直播的主播才能打开本链接。

   ```
    public void createLive() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalklive_1_0.Client client = new com.aliyun.dingtalklive_1_0.Client(config);
           CreateLiveHeaders createLiveHeaders = new CreateLiveHeaders();
           createLiveHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateLiveRequest createLiveRequest = new CreateLiveRequest()
                   .setUnionId("E9CS6*******7QiEiE")
                   .setTitle("测试直播")
                   .setIntroduction("测试直播简介")
                   .setCoverUrl("https://example/k/钉钉图片1.png")
                   .setPreStartTime(1669348228000L)
                   .setPreEndTime(1669351828000L);
           try {
               CreateLiveResponse liveWithOptions = client.createLiveWithOptions(createLiveRequest, createLiveHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(liveWithOptions.getBody()));
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
2. 根据直播`liveId`，调用服务端API-[修改直播属性信息](0432-modify-live-streaming.md)接口，实现修改直播基础信息。

   > **[!NOTE]**
   >
   > 已经开启直播的直播属性信息无法修改。

   ```
   public void updateLives() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalklive_1_0.Client client = new com.aliyun.dingtalklive_1_0.Client(config);
           UpdateLiveHeaders updateLiveHeaders = new UpdateLiveHeaders();
           updateLiveHeaders.xAcsDingtalkAccessToken = "accessToken";
           UpdateLiveRequest updateLiveRequest = new UpdateLiveRequest()
                   .setLiveId("d94f0a69-****-****-****-fe85e460fe0d")
                   .setUnionId("E9CS6*******7QiEiE")
                   .setTitle("live_20221125直播")
                   .setIntroduction("测试直播简介")
                   .setCoverUrl("https://example/k/钉钉图片1.png")
                   .setPreStartTime(1669348228000L)
                   .setPreEndTime(1669351828000L);
           try {
               UpdateLiveResponse updateLiveResponse = client.updateLiveWithOptions(updateLiveRequest, updateLiveHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateLiveResponse.getBody()));
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
3. 根据直播`liveId`，调用服务端API-[查询直播信息](0431-queries-the-live-streaming-information.md)接口，获取直播详细信息。

   ```
    public void  LiveInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalklive_1_0.Client client = new com.aliyun.dingtalklive_1_0.Client(config);
           QueryLiveInfoHeaders queryLiveInfoHeaders = new QueryLiveInfoHeaders();
           queryLiveInfoHeaders.xAcsDingtalkAccessToken = "accessToken";
           QueryLiveInfoRequest queryLiveInfoRequest = new QueryLiveInfoRequest()
                   .setLiveId("d94f0a69-****-****-****-fe85e460fe0d")
                   .setUnionId("E9CS6*******7QiEiE");
           try {
               QueryLiveInfoResponse queryLiveInfoResponse = client.queryLiveInfoWithOptions(queryLiveInfoRequest, queryLiveInfoHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryLiveInfoResponse.getBody()));
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
4. 通过[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)，获取直播观看数据信息。
5. 根据直播`liveId`，调用服务端API-[查询直播观看人员信息](0433-queries-the-viewing-information-of-viewers.md)接口，获取直播观看人员信息。

   ```
    public void  queryUserInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalklive_1_0.Client client = new com.aliyun.dingtalklive_1_0.Client(config);
           QueryLiveWatchUserListHeaders queryLiveWatchUserListHeaders = new QueryLiveWatchUserListHeaders();
           queryLiveWatchUserListHeaders.xAcsDingtalkAccessToken = "accessToken";
           QueryLiveWatchUserListRequest queryLiveWatchUserListRequest = new QueryLiveWatchUserListRequest()
                   .setLiveId("d94f0a69-****-****-****-fe85e460fe0d")
                   .setUnionId("E9CS6*******7QiEiE")
                   .setPageNumber(0)
                   .setPageSize(20);
           try {
               QueryLiveWatchUserListResponse queryLiveWatchUserListResponse = client.queryLiveWatchUserListWithOptions(queryLiveWatchUserListRequest, queryLiveWatchUserListHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryLiveWatchUserListResponse.getBody()));
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
6. 根据直播`liveId`，调用服务端API-[删除直播](0430-delete-live-streaming.md)接口，实现删除直播操作。

   ```
   public void deleteLive() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalklive_1_0.Client client = new com.aliyun.dingtalklive_1_0.Client(config);
           DeleteLiveHeaders deleteLiveHeaders = new DeleteLiveHeaders();
           deleteLiveHeaders.xAcsDingtalkAccessToken = "accessToken";
           DeleteLiveRequest deleteLiveRequest = new DeleteLiveRequest()
                   .setLiveId("d94f0a69-****-****-****-fe85e460fe0d")
                   .setUnionId("E9CS6*******7QiEiE");
           try {
               DeleteLiveResponse deleteLiveResponse = client.deleteLiveWithOptions(deleteLiveRequest, deleteLiveHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(deleteLiveResponse.getBody()));
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
