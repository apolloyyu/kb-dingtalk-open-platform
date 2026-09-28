---
title: "构建会议室资源池：数据上钉实现会议室高效调度"
source_url: "https://open.dingtalk.com/document/development/conference-room-operation-process"
namespace: "development"
slug: "conference-room-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 构建会议室资源池：数据上钉实现会议室高效调度"
doc_id: "HXCX70UL9r"
updated_at: "2026-09-23 12:04:45"
---

> Source: https://open.dingtalk.com/document/development/conference-room-operation-process
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 构建会议室资源池：数据上钉实现会议室高效调度
> Updated: 2026-09-23 12:04:45

# 构建会议室资源池：数据上钉实现会议室高效调度

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现会议室的自动创建、信息更新、列表查询、详情获取及删除操作，支持将业务系统中的会议室资源自动同步至钉钉智能会议室模块，实现统一会议室管理。

## 概述

本方案提供一套完整的钉钉智能会议室管理解决方案，通过调用钉钉开放平台的会议室相关API，实现在业务系统中直接创建会议室、更新会议室信息、查询会议室列表及详情、删除会议室等功能，并支持会议室容量、位置、标签等属性的自动化配置。

### 方案背景

企业在日常运营中常面临以下痛点：

- **会议室手动创建耗时**：行政系统在OA中已登记的会议室信息，仍需人工在钉钉中重新创建并配置参数，重复操作效率极低。
- **会议室状态难追踪**：会议室是否可用、容纳人数、所在位置等信息无法实时同步至业务系统，难以进行资源调度。
- **会议室数据孤岛**：会议室相关信息（名称、容量、位置、标签）未与业务系统打通，难以进行统一的资源管理和统计分析。
- **会议室维护复杂**：会议室信息变更（如搬迁、扩容）需人工逐个修改，缺乏批量更新机制。

### 核心价值

本方案提供一套完整的钉钉智能会议室管理解决方案，通过调用钉钉开放平台的会议室相关API，实现在业务系统中直接创建会议室、更新会议室信息、查询会议室列表及详情、删除会议室等功能。

- **会议室自动创建**：业务系统确定会议室资源后一键同步至钉钉智能会议室，无需人工重新配置，大幅提升会议室录入效率。
- **会议室信息实时更新**：支持根据roomId更新会议室名称、容量、位置、标签等属性，确保双端数据一致。
- **会议室列表精准查询**：支持分页查询会议室列表及单个会议室详情，实时掌握会议室资源分布情况。
- **会议室全生命周期管理**：从创建、更新、查询到删除，实现会议室全流程自动化管理。

### 适用场景

本方案适用于以下典型业务场景：

- **行政系统会议室自动同步**：行政管理系统中新增会议室后自动创建钉钉智能会议室，员工可直接在钉钉端预订。
- **办公空间优化调整**：办公室搬迁或扩容时批量更新会议室位置和容量信息，确保预订系统数据准确。
- **会议室资源统计分析**：定期查询会议室列表并进行数据分析，评估会议室利用率和资源配置合理性。
- **临时会议室快速清理**：活动结束后自动删除临时创建的会议室，保持会议室列表整洁。

## 典型业务场景

### 场景一：行政系统会议室自动同步至钉钉

#### 痛点分析

行政部门在OA系统中登记新会议室，但仍需在钉钉中手动创建：

- OA系统中的会议室数据无法自动带入钉钉会议室，需人工重新填写名称、容量、位置等
- 会议室标签（如"带投影""可视频会议"）需手动逐个添加，大型办公楼动辄数十间会议室，操作繁琐且易遗漏
- 会议室位置信息（楼层、区域）未与钉钉端同步，员工预订时难以快速定位
- 会议室容量变更后无法及时更新，导致预订冲突或资源浪费

#### 价值验证

- **自动化流程**

  ![行政系统会议室自动同步流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5826310971/p1103636.png)
- **关键优势**

  - **会议室自动创建**：OA系统提交会议室信息后1秒内自动创建钉钉智能会议室，无需人工重新配置。
  - **属性完整同步**：支持同步会议室名称、容量、位置、标签、图片等完整信息，减少90%的手动操作。
  - **数据实时一致**：会议室信息变更后自动更新钉钉端，确保双端数据一致性。

### 场景二：办公空间优化调整与会议室批量更新

#### 痛点分析

企业进行办公空间优化时，会议室信息需批量调整：

- 办公室搬迁后，会议室位置信息需逐个手动修改，耗时且容易遗漏
- 会议室扩容或合并后，容量信息未及时更新，导致预订系统显示错误
- 会议室标签（如设备配置）变更后未同步至钉钉，员工预订时无法准确判断是否满足需求
- 临时会议室使用后未及时删除，会议室列表冗余信息增多

#### 价值验证

- **自动化流程**

  ![会议室批量更新流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5826310971/p1103637.png)
- **关键优势**

  - **信息批量更新**：支持根据roomId批量更新会议室名称、容量、位置、标签等属性，提升维护效率。
  - **位置精准标注**：支持设置会议室标题和详细描述，员工可快速定位会议室位置。
  - **临时会议室清理**：活动结束后自动删除临时会议室，保持会议室列表整洁有序。

## 实施指南

### 技术架构

- **接口调用层**：调用会议室服务端API实现会议室的创建、更新、查询、删除等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **会议室管理层**：调用会议室相关API创建、更新、查询、删除会议室，获取roomId。
- **数据同步层**：实现业务系统与钉钉会议室数据的双向同步，确保数据一致性。
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

步骤二：申请接口权限，申请智能会议室相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用会议室相关API：

1. 调用服务端API-[创建会议室](0436-create-a-meeting-room.md)接口，获取会议室返回结果`result`字段**，**即会议室ID**。**
2. 根据会议室ID，调用服务端API-[更新会议室信息](0438-update-meeting-room-information.md)接口，实现会议室信息更新操作。
3. 调用服务端API-[查询会议室列表](0439-check-the-meeting-room-list.md)接口，实现获取会议室列表内容。
4. 根据会议室ID，调用服务端API-[查询会议室详情](0440-check-meeting-room-details.md)接口，实现获取单个会议室具体内容信息。
5. 根据会议室ID，调用服务端API-[删除会议室](0437-delete-a-meeting-room.md)接口，实现删除会议室操作。

## **实施步骤**

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

   - `Yida.Process.Write`（宜搭流程数据写权限）— 用于发起、终止、删除和同意或拒绝宜搭审批流程
   - `Yida.Process.Read`（宜搭流程数据读权限）— 用于获取流程实例
   - `Yida.Task.Read`（宜搭任务读权限）— 用于查询流程运行任务（VPC）

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

1. **创建会议室**：调用服务端API-[创建会议室](0436-create-a-meeting-room.md)接口，获取会议室返回结果`result`字段**，**即会议室ID**。**

   ```
   public void createMeetingRoom() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomHeaders createMeetingRoomHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomHeaders();
       createMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";

       // 构建会议室位置信息
       com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest.CreateMeetingRoomRequestRoomLocation roomLocation =
               new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest.CreateMeetingRoomRequestRoomLocation()
                       .setTitle("***测试")
                       .setDesc("xx市xx区xx路xx号");

       // 构建创建会议室请求参数
       com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest createMeetingRoomRequest =
               new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE")
                       .setRoomName("测试会议室")
                       .setRoomCapacity(10)
                       .setRoomPicture("https://example/k/钉钉图片1.png")
                       .setRoomStatus(0)
                       .setRoomLocation(roomLocation)
                       .setRoomLabelIds(java.util.Arrays.asList(1L))
                       .setIsvRoomId("dingTalk1001");

       try {
           CreateMeetingRoomResponse meetingRoomWithOptions = client.createMeetingRoomWithOptions(
                   createMeetingRoomRequest, createMeetingRoomHeaders, new RuntimeOptions());
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

   **参数说明**：

   - `unionId`：**重点参数**，操作人的unionId
   - `roomName`：**重点参数**，会议室名称
   - `roomStatus`：**重点参数**，会议室状态：0-全员可用，1-仅管理员可用，2-部分有权限
   - `isvRoomId`：**重点参数**，调用方外部会议室ID
   - `roomCapacity`：会议室可容纳人数
   - `roomPicture`：会议室图片URL
   - `roomLocation`：会议室位置信息对象，包含`title`（位置标题）和`desc`（详细地址）
   - `roomLabelIds`：标签ID数组：1-电视，2-电话，3-投影仪，4-白板，5-视频会议

   **返回字段**：

   - `result`：会议室ID，后续所有操作均需使用此ID
2. **更新会议室信息**：根据会议室ID，调用服务端API-[更新会议室信息](0438-update-meeting-room-information.md)接口，实现会议室信息更新操作。

   ```
   public void updateMeetingRooms() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomHeaders updateMeetingRoomHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomHeaders();
       updateMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";

       // 构建会议室位置信息
       com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation roomLocation =
               new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation()
                       .setTitle("阿里***A座")
                       .setDesc("**市**区");

       // 构建更新会议室请求参数
       com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest updateMeetingRoomRequest =
               new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE")
                       .setRoomId("9d5356997e44f******0ab267c05d6b3a14")
                       .setRoomName("会议室测试")
                       .setRoomCapacity(10)
                       .setRoomPicture("https://example/k/钉钉图片1.png")
                       .setRoomStatus(0)
                       .setRoomLocation(roomLocation)
                       .setRoomLabelIds(java.util.Arrays.asList(1L))
                       .setIsvRoomId("dingTalk1001");
       try {
           UpdateMeetingRoomResponse updateMeetingRoomResponse = client.updateMeetingRoomWithOptions(
                   updateMeetingRoomRequest, updateMeetingRoomHeaders, new RuntimeOptions());
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

   **参数说明**：

   - `roomId`：**重点参数**，会议室ID（路径参数）
   - `unionId`：**重点参数**，操作人的unionId
   - `roomName`：会议室名称
   - `roomCapacity`：会议室可容纳人数
   - `roomPicture`：会议室图片URL
   - `roomStatus`：会议室状态：0-全员可用，1-仅管理员可用，2-部分有权限
   - `roomLocation`：会议室位置信息对象，包含`title`（位置标题）和`desc`（详细地址）
   - `roomLabelIds`：标签ID数组：1-电视，2-电话，3-投影仪，4-白板，5-视频会议
3. **查询会议室列表**：调用服务端API-[查询会议室列表](0439-check-the-meeting-room-list.md)接口，实现获取会议室列表内容。

   ```
   public void meetingRoomsList() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListHeaders queryMeetingRoomListHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListHeaders();
       queryMeetingRoomListHeaders.xAcsDingtalkAccessToken = "acccessToken";

       // 构建查询会议室列表请求参数
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListRequest queryMeetingRoomListRequest =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListRequest()
                       .setMaxResults(20)
                       .setUnionId("E9CS6X*******eN7QiEiE");

       try {
           QueryMeetingRoomListResponse queryMeetingRoomListResponse = client.queryMeetingRoomListWithOptions(
                   queryMeetingRoomListRequest, queryMeetingRoomListHeaders, new RuntimeOptions());
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

   **参数说明**：

   - `unionId`：**重点参数**，操作人的unionId
   - `maxResults`：每页最大返回数量，默认20，最大值100
   - `nextToken`：分页游标，首次调用不传，后续调用传入上次返回的nextToken

   **返回字段**：

   - `hasMore`：是否有更多数据（true/false）
   - `nextToken`：分页游标
   - `result`：会议室列表数组，每个会议室包含：
   - `roomId`：会议室ID
   - `roomName`：会议室名称
   - `roomStatus`：会议室状态（0-全员可见，1-仅管理员可见，2-部分成员可见）
   - `roomCapacity`：会议室可容纳人数
   - `roomLocation`：会议室位置信息对象（title/desc）
   - `roomPicture`：会议室图片URL
   - `roomLabels`：标签数组（labelId/labelName）
   - `isvRoomId`：调用方外部会议室ID
   - `roomGroup`：分组信息（groupId/groupName/parentId）
4. **查询会议室详情**：根据会议室ID，调用服务端API-[查询会议室详情](0440-check-meeting-room-details.md)接口，实现获取单个会议室具体内容信息。

   ```
   public void meetingRoomsInfo() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomHeaders queryMeetingRoomHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomHeaders();
       queryMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";

       // 构建查询会议室详情请求参数
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomRequest queryMeetingRoomRequest =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE");

       try {
           QueryMeetingRoomResponse queryMeetingRoomResponse = client.queryMeetingRoomWithOptions(
                   "9d5356997e44f******0ab267c05d6b3a14",
                   queryMeetingRoomRequest,
                   queryMeetingRoomHeaders,
                   new RuntimeOptions());
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

   **参数说明**：

   - `roomId`：**重点参数**，会议室ID（路径参数）
   - `unionId`：**重点参数**，企业unionId

   **返回字段**：

   - `roomId`：会议室ID
   - `roomName`：会议室名称
   - `roomCapacity`：会议室容量
   - `roomLocation`：会议室位置信息
   - `roomPicture`：会议室封面图片URL
   - `roomStatus`：会议室状态
   - `roomLabelIds`：会议室标签ID列表
5. **删除会议室**：根据会议室ID，调用服务端API-[删除会议室](0437-delete-a-meeting-room.md)接口，实现删除会议室操作。

   > **[!IMPORTANT]**
   >
   > 删除会议室必须拥有智能会议室应用管理权限。

   ```
   public void deleteMeetingRoom() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomHeaders deleteMeetingRoomHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomHeaders();
       deleteMeetingRoomHeaders.xAcsDingtalkAccessToken = "acccessToken";

       // 构建删除会议室请求参数
       com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomRequest deleteMeetingRoomRequest =
               new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE");

       try {
           DeleteMeetingRoomResponse deleteMeetingRoomResponse = client.deleteMeetingRoomWithOptions(
                   "9d5356997e44f******0ab267c05d6b3a14",
                   deleteMeetingRoomRequest,
                   deleteMeetingRoomHeaders,
                   new RuntimeOptions());
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

   **参数说明**：

   - `roomId`：**重点参数**，会议室ID（路径参数）
   - `unionId`：**重点参数**，企业unionId

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ 会议室读写权限申请成功。
- ✅ accessToken获取成功。
- ✅ 会议室创建成功，获取roomId。
- ✅ 会议室信息更新成功，返回正确的更新结果。
- ✅ 会议室列表查询成功，返回会议室列表。
- ✅ 会议室详情查询成功，返回完整的会议室信息。
- ✅ 会议室删除成功。

## **常见问题（FAQ）**

- **Q1：创建会议室时必填哪些参数？**

  - `unionId`：操作人的unionId
  - `roomName`：会议室名称
  - `roomStatus`：会议室状态（0-全员可用，1-仅管理员可用，2-部分有权限）
  - `isvRoomId`：调用方外部会议室ID

  可选参数包括 `roomCapacity`（容量）、`roomLocation`（位置信息）、`roomPicture`（封面图片）、`roomLabelIds`（标签ID列表）、`groupId`（分组ID）等。
- **Q2：如何获取roomId？**

  A：调用创建会议室接口后，接口返回的result字段即为会议室ID。此ID是后续所有会议室操作（更新、查询、删除）的唯一标识，务必妥善保存。
- **Q3：会议室位置信息如何设置？**

  A：会议室位置信息通过 `roomLocation` 对象设置，包含两个字段：

  - `title`：位置标题（如"阿里A座"）
  - `desc`：详细地址描述（如"杭州市余杭区xxxx"）
- **Q4：为什么删除会议室失败？**

  A：可能原因包括：

  - 应用未拥有智能会议室应用管理权限
  - roomId不正确
  - 应用未申请视频会议写权限
  - 会议室正在被使用中，无法删除
- **Q5：会议室标签如何使用？**

  A：会议室标签通过 `roomLabelIds` 参数设置，传入标签ID列表（如 `[1L, 2L]`）。标签需在钉钉后台预先配置，常见标签包括"带投影""可视频会议""带白板"等，用于标识会议室的设备配置和功能特点。
