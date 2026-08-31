---
title: "创建、查询及关闭视频会议"
source_url: "https://open.dingtalk.com/document/development/create-and-close-video-meetings"
namespace: "development"
slug: "create-and-close-video-meetings"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 创建、查询及关闭视频会议"
doc_id: "7kwwdRgOPM"
updated_at: "2026-07-10 10:11:06"
---

> Source: https://open.dingtalk.com/document/development/create-and-close-video-meetings
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 创建、查询及关闭视频会议
> Updated: 2026-07-10 10:11:06

# 创建、查询及关闭视频会议

本文档介绍了如何调用会议接口创建视频会议等流程。首先创建一个企业内部应用，再使用会议提供的API，实现创建视频会议、关闭视频会议和批量查询视频会议信息流程。

## 流程简介

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请会议相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端会议相关API。

1. 调用服务端API-[创建视频会议](0399-create-a-video-conference.md)接口，进行创建视频会议，获取视频会议conferenceId。
2. 根据视频会议conferenceId，调用服务端API-[批量查询视频会议信息](0403-batch-query-of-video-conference-information.md)接口，获取视频会议信息及参会人员列表。
3. 根据视频会议conferenceId，调用服务端API-[开启视频会议云录制](0424-video-conference-open-cloud-recording.md)接口，开启视频会议云录制。
4. 调用视频会议conferenceId，调用服务端API-[开启视频会议云录制](0424-video-conference-open-cloud-recording.md)接口，关闭视频会议云录制。
5. 根据视频会议conferenceId，调用服务端API-[关闭视频会议](0400-close-audio-video-conference.md)接口，进行关闭视频会议。
6. 查询会议录制信息。

   1. 根据视频会议conferenceId，调用服务单API-[查询会议录制的详情信息](0426-query-recording-information.md)接口，实现查询会议录制的录制人、录制开始时间、录制持续时长等信息。
   2. 根据视频会议conferenceId，调用服务端API-[查询会议录制中的视频信息](0427-queries-the-playback-information-about-a-recorded-cloud-video.md)接口，实现查询视频下载地址、视频文件大小和视频时长等信息。
   3. 根据视频会议conferenceId，调用服务端API-[查询会议录制中的文本信息](0428-queries-the-text-information-about-cloud-recording.md)接口，实现查询会议录制的文本内容、文本记录开始时间、文本记录结束时间等信息。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`VideoConference.Conference.Write`和`VideoConference.Conference.Read`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

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

## 步骤四：调用服务端会议相关API

1. 调用服务端API-[创建视频会议](0399-create-a-video-conference.md)接口，进行创建视频会议，获取视频会议conferenceId。

   ```
   public void videoConferencesCreate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
           CreateVideoConferenceHeaders createVideoConferenceHeaders = new CreateVideoConferenceHeaders();
           createVideoConferenceHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateVideoConferenceRequest createVideoConferenceRequest = new CreateVideoConferenceRequest()
                   .setUserId("E9CS6X*******QiEiE")
                   .setConfTitle("202211071001视频会议")
                   .setInviteCaller(true)
                   .setInviteUserIds(java.util.Arrays.asList(
                           "tXguN3*******URAiEiE"
                   ));
           try {
               CreateVideoConferenceResponse videoConferenceWithOptions = client.createVideoConferenceWithOptions(createVideoConferenceRequest, createVideoConferenceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(videoConferenceWithOptions.getBody()));
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
2. 根据视频会议conferenceId，调用服务端API-[批量查询视频会议信息](0403-batch-query-of-video-conference-information.md)接口，获取视频会议信息及参会人员列表。

   > **[!NOTE]**
   >
   > 目前只支持查询正在进行的视频会议。

   ```
   public void  videoConferencesInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
           QueryConferenceInfoBatchHeaders queryConferenceInfoBatchHeaders = new QueryConferenceInfoBatchHeaders();
           queryConferenceInfoBatchHeaders.xAcsDingtalkAccessToken = "accessToken";
           QueryConferenceInfoBatchRequest queryConferenceInfoBatchRequest = new QueryConferenceInfoBatchRequest()
                   .setConferenceIdList(java.util.Arrays.asList(
                           "6368xxxx720"
                   ));
           try {
               QueryConferenceInfoBatchResponse queryConferenceInfoBatchResponse = client.queryConferenceInfoBatchWithOptions(queryConferenceInfoBatchRequest, queryConferenceInfoBatchHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryConferenceInfoBatchResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }

           }
       }
   ```
3. 根据视频会议conferenceId，调用服务端API-[开启视频会议云录制](0424-video-conference-open-cloud-recording.md)接口，开启视频会议云录制。

   ```
   public void cloudRecordsStart() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
           StartCloudRecordHeaders startCloudRecordHeaders = new StartCloudRecordHeaders();
           startCloudRecordHeaders.xAcsDingtalkAccessToken = "accessToken";
           StartCloudRecordRequest startCloudRecordRequest = new StartCloudRecordRequest()
                   .setUnionId("E9CS6X*******QiEiE")
                   .setSmallWindowPosition("relative_right")
                   .setMode("speech");
           try {
               StartCloudRecordResponse startCloudRecordResponse = client.startCloudRecordWithOptions("636866074147ec014a76e720", startCloudRecordRequest, startCloudRecordHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(startCloudRecordResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }
           }
       }
   ```
4. 调用视频会议conferenceId，调用服务端API-[停止视频会议云录制](0425-video-conferencing-stops-cloud-recording.md)接口，关闭视频会议云录制。

   ```
    public void cloudRecordsStop() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
           StopCloudRecordHeaders stopCloudRecordHeaders = new StopCloudRecordHeaders();
           stopCloudRecordHeaders.xAcsDingtalkAccessToken = "accessToken";
           StopCloudRecordRequest stopCloudRecordRequest = new StopCloudRecordRequest()
                   .setUnionId("E9CS6X*******QiEiE");
           try {
               StopCloudRecordResponse stopCloudRecordResponse = client.stopCloudRecordWithOptions("636866074147ec014a76e720", stopCloudRecordRequest, stopCloudRecordHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(stopCloudRecordResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }
           }
       }
   ```
5. 根据视频会议conferenceId，调用服务端API-[关闭视频会议](0400-close-audio-video-conference.md)接口，进行关闭视频会议。

   ```
   public void  videoConferencesClose() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);        CloseVideoConferenceHeaders closeVideoConferenceHeaders = new CloseVideoConferenceHeaders();
           closeVideoConferenceHeaders.xAcsDingtalkAccessToken = "accessToken";
           CloseVideoConferenceRequest closeVideoConferenceRequest = new CloseVideoConferenceRequest()
                   .setUnionId("E9CS6X*******QiEiE");
           try {
               CloseVideoConferenceResponse closeVideoConferenceResponse = client.closeVideoConferenceWithOptions("636866074147ec014a76e720", closeVideoConferenceRequest, closeVideoConferenceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(closeVideoConferenceResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.message);
                   System.out.println(err.code);
               }
           }
       }
   ```
6. 查询会议录制信息。

   1. 根据视频会议conferenceId，调用服务单API-[查询会议录制的详情信息](0426-query-recording-information.md)接口，实现查询会议录制的录制人、录制开始时间、录制持续时长等信息。

      ```
       public void VideoDetailedInfos() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
              QueryCloudRecordVideoHeaders queryCloudRecordVideoHeaders = new QueryCloudRecordVideoHeaders();
              queryCloudRecordVideoHeaders.xAcsDingtalkAccessToken = "accessToken";
              QueryCloudRecordVideoRequest queryCloudRecordVideoRequest = new QueryCloudRecordVideoRequest()
                      .setUnionId("E9CS6X*******QiEiE");
              try {
                  QueryCloudRecordVideoResponse queryCloudRecordVideoResponse = client.queryCloudRecordVideoWithOptions("636866074147ec014a76e720", queryCloudRecordVideoRequest, queryCloudRecordVideoHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(queryCloudRecordVideoResponse.getBody()));
              } catch (TeaException err) {
                  if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                      // err 中含有 code 和 message 属性，可帮助开发定位问题
                      System.out.println(err.message);
                      System.out.println(err.code);
                  }

              } catch (Exception _err) {
                  TeaException err = new TeaException(_err.getMessage(), _err);
                  if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                      // err 中含有 code 和 message 属性，可帮助开发定位问题
                      System.out.println(err.message);
                      System.out.println(err.code);
                  }
              }
          }
      ```
   2. 根据视频会议conferenceId，调用服务端API-[查询会议录制中的视频信息](0427-queries-the-playback-information-about-a-recorded-cloud-video.md)接口，实现查询视频下载地址、视频文件大小和视频时长等信息。

      ```
       public void  videosPlayInfos() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
              QueryCloudRecordVideoPlayInfoHeaders queryCloudRecordVideoPlayInfoHeaders = new QueryCloudRecordVideoPlayInfoHeaders();
              queryCloudRecordVideoPlayInfoHeaders.xAcsDingtalkAccessToken = "accessToken";
              QueryCloudRecordVideoPlayInfoRequest queryCloudRecordVideoPlayInfoRequest = new QueryCloudRecordVideoPlayInfoRequest()
                      .setUnionId("E9CS6X*******QiEiE")
                      .setMediaId("7665cd17********90991fe43bb")
                      .setRegionId("cn-shanghai");
              try {
                  QueryCloudRecordVideoPlayInfoResponse queryCloudRecordVideoPlayInfoResponse = client.queryCloudRecordVideoPlayInfoWithOptions("636866074147ec014a76e720", queryCloudRecordVideoPlayInfoRequest, queryCloudRecordVideoPlayInfoHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(queryCloudRecordVideoPlayInfoResponse.getBody()));
              } catch (TeaException err) {
                  if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                      // err 中含有 code 和 message 属性，可帮助开发定位问题
                      System.out.println(err.message);
                      System.out.println(err.code);
                  }
              } catch (Exception _err) {
                  TeaException err = new TeaException(_err.getMessage(), _err);
                  if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                      // err 中含有 code 和 message 属性，可帮助开发定位问题
                      System.out.println(err.message);
                      System.out.println(err.code);
                  }
              }
          }
      ```
   3. 根据视频会议conferenceId，调用服务端API-[查询会议录制中的文本信息](0428-queries-the-text-information-about-cloud-recording.md)接口，实现查询会议录制的文本内容、文本记录开始时间、文本记录结束时间等信息。

      ```
       public void  videosTextInfos() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkconference_1_0.Client client = new com.aliyun.dingtalkconference_1_0.Client(config);
              QueryCloudRecordTextHeaders queryCloudRecordTextHeaders = new QueryCloudRecordTextHeaders();
              queryCloudRecordTextHeaders.xAcsDingtalkAccessToken = "accessToken";
              QueryCloudRecordTextRequest queryCloudRecordTextRequest = new QueryCloudRecordTextRequest()
                      .setUnionId("E9CS6X*******QiEiE")
                      .setStartTime(1000L)
                      .setDirection("0")
                      .setMaxResults(200L);
                      //如果是首次查询，该参数可不传
                      //.setNextToken(0L);
              try {
                  QueryCloudRecordTextResponse queryCloudRecordTextResponse = client.queryCloudRecordTextWithOptions("636866074147ec014a76e720", queryCloudRecordTextRequest, queryCloudRecordTextHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(queryCloudRecordTextResponse.getBody()));
              } catch (TeaException err) {
                  if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                      // err 中含有 code 和 message 属性，可帮助开发定位问题
                      System.out.println(err.message);
                      System.out.println(err.code);
                  }
              } catch (Exception _err) {
                  TeaException err = new TeaException(_err.getMessage(), _err);
                  if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                      // err 中含有 code 和 message 属性，可帮助开发定位问题
                      System.out.println(err.message);
                      System.out.println(err.code);
                  }
              }
          }
      ```
