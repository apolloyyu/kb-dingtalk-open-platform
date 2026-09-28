---
title: "视频会议自动化：从业务系统到钉钉会议无缝集成"
source_url: "https://open.dingtalk.com/document/development/create-and-close-video-meetings"
namespace: "development"
slug: "create-and-close-video-meetings"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 视频会议自动化：从业务系统到钉钉会议无缝集成"
doc_id: "7kwwdRgOPM"
updated_at: "2026-09-23 12:04:42"
---

> Source: https://open.dingtalk.com/document/development/create-and-close-video-meetings
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 视频会议自动化：从业务系统到钉钉会议无缝集成
> Updated: 2026-09-23 12:04:42

# 视频会议自动化：从业务系统到钉钉会议无缝集成

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现视频会议的自动创建、关闭、云录制及信息查询，支持将业务系统中的会议需求自动转换为钉钉视频会议，实现统一会议管理。

## 概述

本方案提供一套完整的钉钉视频会议管理解决方案，通过调用钉钉开放平台的会议相关API，实现在业务系统中直接创建视频会议、批量查询会议信息、开启/停止云录制、关闭会议等功能，并支持查询会议录制的视频和文本信息。

### 方案背景

企业在日常运营中常面临以下痛点：

- **会议手动创建耗时**：业务系统中已安排的会议计划，仍需人工在钉钉中重新创建会议并邀请参会人，重复操作效率极低。
- **会议状态难追踪**：会议是否已开始、参会人员是否到场、会议时长等信息无法实时同步至业务系统。
- **录制管理复杂**：重要会议需要录制存档，但手动开启录制容易遗漏，录制文件分散存储难以查找。
- **会议数据孤岛**：会议相关信息（参会人列表、录制内容、会议纪要）未与业务系统打通，难以进行后续分析。

### 核心价值

本方案提供一套完整的钉钉视频会议管理解决方案，通过调用钉钉开放平台的会议相关API，实现在业务系统中直接创建视频会议、批量查询会议信息、开启/停止云录制、关闭会议等功能。

- **会议自动创建**：业务系统确定会议计划后一键同步至钉钉视频会议，无需人工重新创建，大幅提升会议组织效率。
- **会议信息实时查询**：支持根据conferenceId批量查询会议信息及参会人员列表，实时掌握会议状态。
- **云录制智能管理**：支持自动开启/停止会议云录制，并查询录制详情、视频下载链接及文本转录内容。
- **会议全生命周期管理**：从创建、进行、录制到关闭，实现会议全流程自动化管理。

### 适用场景

本方案适用于以下典型业务场景：

- **CRM系统客户会议自动创建**：销售人员在CRM系统中安排客户拜访会议后自动创建钉钉视频会议，并邀请相关人员参加。
- **项目管理系统站会自动化**：每日站会时间到达时自动创建钉钉视频会议，团队成员一键入会。
- **培训系统课程录制归档**：在线培训课程自动开启云录制，课后自动查询录制文件并归档至知识库。
- **会议纪要自动生成**：会议结束后自动查询录制文本信息，结合AI生成会议纪要并同步至业务系统。

## 典型业务场景

### 场景一：CRM系统客户会议自动创建并邀请参会人

#### 痛点分析

销售团队在CRM系统中安排客户拜访会议，但仍需在钉钉中手动创建视频会议：

- CRM系统中的会议数据无法自动带入钉钉会议，需人工重新填写会议主题、时间、参会人
- 参会人员需手动逐个添加，大型会议动辄数十人，操作繁琐且易遗漏
- 会议开始后无法实时掌握参会情况，销售人员难以确认客户是否准时入会
- 会议结束后缺乏统一的录制归档机制，重要沟通内容难以回溯

#### 价值验证

- **自动化流程**

  ![CRM客户会议自动创建流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2826310971/p1103556.png)
- **关键优势**

  - **会议自动创建**：CRM系统提交会议计划后1秒内自动创建钉钉视频会议，无需人工重新填写。
  - **参会人批量邀请**：支持根据CRM中的客户联系人和内部销售团队自动添加参会人，减少80%的手动操作。
  - **会议状态实时同步**：支持查询会议信息及参会人员列表，实时掌握客户是否入会。

### 场景二：培训系统课程自动录制与内容归档

#### 痛点分析

企业在线培训课程在钉钉中进行，但录制管理依赖人工操作：

- 讲师容易忘记开启云录制，导致重要培训内容丢失
- 录制文件分散存储在钉盘中，难以按课程分类查找
- 录制视频的下载地址、文件大小、时长等信息无法自动获取
- 录制文本转录内容未与课程资料关联，学员难以快速定位关键知识点

#### 价值验证

- **自动化流程**

  ![培训课程自动录制流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2826310971/p1103560.png)
- **关键优势**

  - **录制自动开启**：课程开始时自动调用API开启云录制，确保培训内容完整记录。
  - **录制信息精准查询**：支持查询录制人、录制开始时间、持续时长、视频下载地址等完整信息。
  - **文本转录自动归档**：自动获取录制文本内容，结合AI生成课程摘要并归档至知识库。

## 实施指南

### 技术架构

- **接口调用层**：调用会议服务端API实现会议的创建、查询、录制、关闭等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **会议管理层**：调用会议相关API创建、关闭视频会议，获取conferenceId。
- **录制管理层**：调用云录制相关API开启/停止录制，查询录制详情、视频信息和文本信息。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `VideoConference.Conference.Write`（视频会议信息管理写权限）
  - `VideoConference.Conference.Read`（视频会议信息管理读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请会议相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端会议相关API。

1. 调用服务端API-[创建视频会议](0401-create-a-video-conference.md)接口，进行创建视频会议，获取视频会议conferenceId。
2. 根据视频会议conferenceId，调用服务端API-[批量查询视频会议信息](0405-batch-query-of-video-conference-information.md)接口，获取视频会议信息及参会人员列表。
3. 根据视频会议conferenceId，调用服务端API-[开启视频会议云录制](0426-video-conference-open-cloud-recording.md)接口，开启视频会议云录制。
4. 调用视频会议conferenceId，调用服务端API-[开启视频会议云录制](0426-video-conference-open-cloud-recording.md)接口，关闭视频会议云录制。
5. 根据视频会议conferenceId，调用服务端API-[关闭视频会议](0402-close-audio-video-conference.md)接口，进行关闭视频会议。
6. 查询会议录制信息。

   1. 根据视频会议conferenceId，调用服务单API-[查询会议录制的详情信息](0428-query-recording-information.md)接口，实现查询会议录制的录制人、录制开始时间、录制持续时长等信息。
   2. 根据视频会议conferenceId，调用服务端API-[查询会议录制中的视频信息](0429-queries-the-playback-information-about-a-recorded-cloud-video.md)接口，实现查询视频下载地址、视频文件大小和视频时长等信息。
   3. 根据视频会议conferenceId，调用服务端API-[查询会议录制中的文本信息](0430-queries-the-text-information-about-cloud-recording.md)接口，实现查询会议录制的文本内容、文本记录开始时间、文本记录结束时间等信息。

## 实施步骤

### **步骤一：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤二：添加接口权限**

1. 在应用详情页，单击**权限管理**。
2. 在权限搜索框中输入以下权限标识并申请：

   - `VideoConference.Conference.Write`（视频会议信息管理写权限）—— 用于创建、关闭会议，开启/停止录制。
   - `VideoConference.Conference.Read`（视频会议信息管理读权限）—— 用于查询会议信息、录制信息。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

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

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：核心API调用**

1. **创建视频会议**：调用服务端API-[创建视频会议](0401-create-a-video-conference.md)接口，进行创建视频会议，获取视频会议conferenceId。

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

   **参数说明**：

   - `confTitle`：**重点参数**，会议主题。
   - `inviteUserIds`：参会人userId列表。

   **返回字段**：

   - `conferenceId`：**重点参数**，视频会议ID，后续所有操作均需使用此ID。
2. 批量查询视频会议信息：根据视频会议conferenceId，调用服务端API-[批量查询视频会议信息](0405-batch-query-of-video-conference-information.md)接口，获取视频会议信息及参会人员列表。

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

   **参数说明**：

   - `conferenceIdList`：**重点参数**，视频会议ID。

   **返回字段**：

   - `title`：会议主题。
   - `startTime`：会议开始时间。
   - `status`：会议状态。
   - `userList`：参会人员列表。
3. **开启视频会议云录制**：根据视频会议conferenceId，调用服务端API-[开启视频会议云录制](0426-video-conference-open-cloud-recording.md)接口，开启视频会议云录制。

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

   **参数说明**：

   - `conferenceId`：重点参数，视频会议ID。
4. **停止视频会议云录制**：调用视频会议conferenceId，调用服务端API-[停止视频会议云录制](0427-video-conferencing-stops-cloud-recording.md)接口，关闭视频会议云录制。

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

   **参数说明**：

   - `conferenceId`：重点参数，视频会议ID。
5. **关闭视频会议**：根据视频会议conferenceId，调用服务端API-[关闭视频会议](0402-close-audio-video-conference.md)接口，进行关闭视频会议。

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

   **参数说明**：

   - `conferenceId`：重点参数，视频会议ID。
6. **查询会议录制的详情信息**：根据视频会议conferenceId，调用服务单API-[查询会议录制的详情信息](0428-query-recording-information.md)接口，实现查询会议录制的录制人、录制开始时间、录制持续时长等信息。

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

   **参数说明**：

   - `conferenceId`：重点参数，视频会议ID。
   - `unionId`：用户unionId。

   **返回字段**：

   - `recordId`：录制ID。
   - `unionId`：录制人unionId。
   - `startTime`：录制开始时间。
   - `duration`：录制持续时长（单位：秒）。
   - `recordType`：记录类型。
   - `mediaId`：唯一媒体文件ID。
   - `regionId`：媒体文件所在地域ID。
7. **查询会议录制中的视频信息**：根据视频会议conferenceId，调用服务端API-[查询会议录制中的视频信息](0429-queries-the-playback-information-about-a-recorded-cloud-video.md)接口，实现查询视频下载地址、视频文件大小和视频时长等信息。

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

   **参数说明**：

   - `conferenceId`：重点参数，视频会议ID。
   - `unionId`：用户unionId。
   - `mediaId`：媒体文件ID。
   - `regionId`：地域ID。

   **返回字段**：

   - `mp4FileUrl`：重点参数，视频下载地址。
   - `fileSize`：视频文件大小（单位：字节）。
   - `duration`：视频时长（单位：秒）。
   - `playUrl`：录制视频的在线播放链接。
8. **查询会议录制中的文本信息**：根据视频会议conferenceId，调用服务端API-[查询会议录制中的文本信息](0430-queries-the-text-information-about-cloud-recording.md)接口，实现查询会议录制的文本内容、文本记录开始时间、文本记录结束时间等信息。

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

   **参数说明**：

   - `conferenceId`：重点参数，视频会议ID。

**实施完成检查清单**：

- ✅应用凭证获取成功（Client ID / Client Secret）。
- ✅ 视频会议读写权限申请成功。
- ✅ accessToken获取成功。
- ✅ 视频会议创建成功，获取conferenceId。
- ✅ 会议信息查询成功，返回正确的会议详情和参会人列表。
- ✅ 云录制开启成功。
- ✅ 云录制停止成功。
- ✅ 会议关闭成功。
- ✅ 录制详情查询成功，返回录制人、开始时间、持续时长。
- ✅ 录制视频信息查询成功，返回下载地址、文件大小、时长。
- ✅ 录制文本信息查询成功，返回文本内容、起止时间。

## 常见问题（FAQ）

- **Q1：创建会议时必填哪些参数？**

  A：必填参数包括：

  - `confTitle`：会议主题
  - `userId`：会议发起人的unionId

  可选参数包括 `endTime`（会议结束时间）、`userIds`（参会人userId列表）。
- **Q2：如何获取conferenceId？**

  A：调用创建视频会议接口后，接口返回中会包含conferenceId。此ID是后续所有会议操作（查询、录制、关闭）的唯一标识，务必妥善保存。
- **Q3：云录制开启后如何停止？**

  A：调用停止视频会议云录制接口，传入conferenceId即可停止录制。建议在会议结束前主动调用此接口，确保录制文件完整保存。
- **Q4：录制文本信息的作用是什么？**

  A：录制文本信息是会议语音内容的自动转录文本，可用于：

  - 生成会议纪要，提高会议总结效率
  - 快速检索会议中的关键讨论点
  - 为听障人士提供文字辅助
  - 结合AI进行会议内容分析和知识提取
- **Q5：为什么查询不到录制信息？**

  A：可能原因包括：

  - 会议未开启云录制
  - 录制尚未完成，需等待录制处理完成
  - conferenceId不正确
  - 应用未申请视频会议读权限
