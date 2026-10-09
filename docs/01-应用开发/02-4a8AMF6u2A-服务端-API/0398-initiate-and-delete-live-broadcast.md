---
title: "直播全链路：自动创建培训与观看数据实时追踪"
source_url: "https://open.dingtalk.com/document/development/initiate-and-delete-live-broadcast"
namespace: "development"
slug: "initiate-and-delete-live-broadcast"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 直播全链路：自动创建培训与观看数据实时追踪"
doc_id: "Syba6uq8dM"
updated_at: "2026-09-23 12:04:44"
---

> Source: https://open.dingtalk.com/document/development/initiate-and-delete-live-broadcast
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 直播全链路：自动创建培训与观看数据实时追踪
> Updated: 2026-09-23 12:04:44

# 直播全链路：自动创建培训与观看数据实时追踪

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现直播的自动发起、属性修改、信息查询及删除，支持将业务系统中的直播计划自动转换为钉钉直播，实现统一直播管理。

## 概述

本方案提供一套完整的钉钉直播管理解决方案，通过调用钉钉开放平台的直播相关API，实现在业务系统中直接创建直播、修改直播属性、查询直播详细信息、获取观看数据及观看人员信息、删除直播等功能，并支持通过拼接URL直接进入直播显示界面。

### 方案背景

企业在日常运营中常面临以下痛点：

- **直播手动创建耗时**：培训系统、会议系统中已安排的直播计划，仍需人工在钉钉中重新创建直播并配置参数，重复操作效率极低。
- **直播状态难追踪**：直播是否已开始、观看人数、观看时长等数据无法实时同步至业务系统，难以评估直播效果。
- **观看数据分析困难**：缺乏统一的观看数据视图，难以按部门、时间段、人员等多维度进行统计分析。
- **直播管理分散**：直播相关信息（标题、封面、回放链接）未与业务系统打通，直播结束后需人工整理归档。

### 核心价值

本方案提供一套完整的钉钉直播管理解决方案，通过调用钉钉开放平台的直播相关API，实现在业务系统中直接创建直播、修改直播属性、查询直播详细信息、获取观看数据及观看人员信息、删除直播等功能。

- **直播自动发起**：业务系统确定直播计划后一键同步至钉钉直播，无需人工重新创建，大幅提升直播组织效率。
- **直播信息实时查询**：支持根据liveId查询直播详细信息，实时掌握直播状态、观看人数等关键指标。
- **观看数据深度分析**：通过数据资产平台获取直播观看数据，支持多维度统计分析，评估直播效果。
- **直播全生命周期管理**：从创建、修改、查询到删除，实现直播全流程自动化管理。

### 适用场景

本方案适用于以下典型业务场景：

- **培训系统课程直播自动创建**：HR系统在培训系统中安排在线培训课程后自动创建钉钉直播，员工一键入会观看。
- **企业内部大会直播管理**：年会、全员大会等大型活动自动创建直播，管理层实时查看观看数据和互动情况。
- **产品发布会直播归档**：产品发布会直播结束后自动查询观看数据和回放链接，归档至企业知识库。
- **销售培训直播分析**：销售团队培训直播后自动获取观看人员信息，统计参与率和观看时长。

## 典型业务场景

### 场景一：培训系统课程直播自动创建并追踪观看数据

#### 痛点分析

HR部门在培训系统中安排在线培训课程，但仍需在钉钉中手动创建直播：

- 培训系统中的课程数据无法自动带入钉钉直播，需人工重新填写直播标题、时间、封面等
- 直播开始后无法实时掌握观看人数和观看时长，培训组织者难以评估课程吸引力
- 直播结束后缺乏统一的观看数据统计，难以按部门、岗位等维度分析培训效果
- 直播回放链接分散存储，员工难以快速查找历史培训内容

#### 价值验证

- **自动化流程**

  ![培训课程直播自动创建流程图_20260922_113229](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826310971/p1103626.png)
- **关键优势**

  - **直播自动发起**：培训系统提交课程计划后1秒内自动创建钉钉直播，无需人工重新配置。
  - **观看数据实时同步**：支持查询直播观看人员信息和观看数据，实时掌握课程参与度。
  - **培训效果精准评估**：基于观看时长、完成率等数据生成培训效果报告，辅助优化课程内容。

### 场景二：企业内部大会直播管理与数据分析

#### 痛点分析

企业举办年会、全员大会等大型活动时，直播管理依赖人工操作：

- 大型活动直播需提前测试推流地址、配置直播参数，操作复杂且易出错
- 直播过程中无法实时查看观看人数分布，组织者难以判断活动影响力
- 直播结束后需手动下载观看数据报表，耗时且容易遗漏关键指标
- 直播回放视频未与活动资料关联，员工难以快速回顾重要内容

#### 价值验证

- **自动化流程**

  ![企业大会直播管理流程图_20260922_113347](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826310971/p1103627.png)
- **关键优势**

  - **直播一键创建**：业务系统自动调用API创建直播并返回liveId，主播可直接进入直播界面。
  - **观看数据多维分析**：通过数据资产平台获取观看数据，支持按部门、地区、时段等多维度分析。
  - **直播回放自动归档**：直播结束后自动查询回放链接并归档至企业知识库，便于后续查阅。

## 实施指南

### 技术架构

- **接口调用层**：调用直播服务端API实现直播的创建、修改、查询、删除等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **直播管理层**：调用直播相关API创建、修改、查询、删除直播，获取liveId。
- **数据分析层**：通过数据资产平台获取直播观看数据，进行多维度统计分析。
- **URL拼接层**：根据liveId拼接钉钉直播客户端URL，实现直接进入直播显示界面。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Live.Common.Write`（直播通用写权限）
  - `Live.Common.Read`（直播通用读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请直播相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用直播相关API：

1. 调用服务端API-[创建直播](0431-create-live-streaming.md)接口，获取直播ID`liveId`字段**。**
2. 根据直播`liveId`，调用服务端API-[修改直播属性信息](0434-modify-live-streaming.md)接口，实现修改直播基础信息。
3. 根据直播`liveId`，调用服务端API-[查询直播信息](0433-queries-the-live-streaming-information.md)接口，获取直播详细信息。
4. 你可以通过[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)，获取直播观看数据信息。
5. 根据直播`liveId`，调用服务端API-[查询直播观看人员信息](0435-queries-the-viewing-information-of-viewers.md)接口，获取直播观看人员信息。
6. 根据直播`liveId`，调用服务端API-[删除直播](0432-delete-live-streaming.md)接口，实现删除直播操作。

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

   - `Live.Common.Write`（直播通用写权限）—— 用于创建、修改、删除直播。
   - `Live.Common.Read`（直播通用读权限）—— 用于查询直播信息、观看数据。

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

1. 创建直播：调用服务端API-[创建直播](0431-create-live-streaming.md)接口，获取直播ID`liveId`字段**。**

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

   **参数说明**：

   - `title`：**重点参数**，直播标题。
   - `coverUrl`：直播封面图片URL。
   - `preStartTime`：重点参数，直播开始时间（Unix时间戳，单位毫秒）。
   - `preEndTime`：直播结束时间（Unix时间戳，单位毫秒）。

   **返回字段**：

   - `liveId`：重点参数，直播ID，后续所有操作均需使用此ID。

   **URL拼接说明**：

   获取直播ID后，拼接以下链接实现进入显示界面：

   `dingtalk://dingtalkclient/action/start_uniform_live?liveUuid=直播ID`

   > **[!IMPORTANT]**
   >
   > 只有发起直播的主播才能打开本链接。
2. **修改直播属性信息**：根据直播`liveId`，调用服务端API-[修改直播属性信息](0434-modify-live-streaming.md)接口，实现修改直播基础信息。

   > **[!NOTE]**
   >
   > 已经开启直播的直播属性信息无法修改，请在直播开始前完成所有属性修改。

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

   **参数说明**：

   - `liveId`：**重点参数**，直播ID。
   - `unionId`：主播的unionId。
   - `title`：直播标题。
   - `coverUrl`：直播封面图片URL。
3. **查询直播信息**：根据直播`liveId`，调用服务端API-[查询直播信息](0433-queries-the-live-streaming-information.md)接口，获取直播详细信息。

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

   **参数说明**：

   - `liveId`：重点参数，直播ID。
   - `unionId`：操作者的unionId。

   **返回字段**：

   - `title`：直播标题。
   - `liveStatus`：直播状态（NOT\_STARTED/IN\_PROGRESS/ENDED）。
   - `startTime`：直播开始时间。
   - `uv`：当前观看人数。
4. **获取直播观看数据**：通过[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)，获取直播观看数据信息。
5. **查询直播观看人员信息**：根据直播`liveId`，调用服务端API-[查询直播观看人员信息](0435-queries-the-viewing-information-of-viewers.md)接口，获取直播观看人员信息。

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

   **参数说明**：

   - `liveId`：**重点参数**，直播ID。
   - `unionId`：用户unionId。
   - `pageSize`：分页大小，每页大小不超过200。

   **返回字段**：

   - `orgUsesList`：组织内的观看用户列表，包含userId、姓名、部门、观看时长等信息。
   - `outOrgUserList`：组织外的观看用户列表，包含姓名、观看时长等信息。
6. **删除直播**：根据直播`liveId`，调用服务端API-[删除直播](0432-delete-live-streaming.md)接口，实现删除直播操作。

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

   **参数说明**：

   - `liveId`：**重点参数**，直播ID。
   - `unionId`：用户unionId。

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ 直播读写权限申请成功。
- ✅ accessToken获取成功。
- ✅ 直播创建成功，获取liveId。
- ✅ 直播URL拼接成功，主播可正常进入直播界面。
- ✅ 直播属性修改成功（直播开始前）。
- ✅ 直播信息查询成功，返回正确的直播详情。
- ✅ 观看数据获取成功，返回观看统计指标。
- ✅ 观看人员信息查询成功，返回观看人员列表。
- ✅ 直播删除成功。

## 常见问题（FAQ）

- **Q1：创建直播时必填哪些参数？**

  A：必填参数包括：

  - `title`：**重点参数**，直播标题。
  - `coverUrl`：直播封面图片URL。
  - `preStartTime`：重点参数，直播开始时间（Unix时间戳，单位毫秒）。
  - `preEndTime`：直播结束时间（Unix时间戳，单位毫秒）。

  可选参数包括 `coverUrl`（直播封面）、`endTime`（直播结束时间）。
- **Q2：如何获取liveId？**

  A：调用创建直播接口后，接口返回中会包含liveId。此ID是后续所有直播操作（修改、查询、删除）的唯一标识，务必妥善保存。
- **Q3：为什么无法修改直播属性？**

  A：已经开启直播的直播属性信息无法修改。如需修改，请在直播开始前调用修改接口，或删除当前直播后重新创建。
- **Q4：直播观看数据和观看人员信息有什么区别？**

  A：

  - **观看数据**：聚合统计指标，包括总观看人数、峰值观看人数、平均观看时长等，用于整体效果评估
  - **观看人员信息**：详细的观看人员列表，包含每个观众的userId、姓名、部门、个人观看时长等，用于精细化分析
- **Q5：如何通过URL直接进入直播界面？**

  A：获取liveId后，拼接以下URL格式：`dingtalk://dingtalkclient/action/start_uniform_live?liveUuid={liveId}`

  **注意**：只有发起直播的主播才能打开本链接，普通观众需通过其他入口进入直播间。
