---
title: "构建会议室分级体系：数据上钉实现会议室批量调度"
source_url: "https://open.dingtalk.com/document/development/meeting-room-grouping-operation-process"
namespace: "development"
slug: "meeting-room-grouping-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 使用教程 > 构建会议室分级体系：数据上钉实现会议室批量调度"
doc_id: "UPf5bLxcdW"
updated_at: "2026-10-09 14:25:50"
---

> Source: https://open.dingtalk.com/document/development/meeting-room-grouping-operation-process
> Path: 应用开发 / 服务端 API / 音视频 > 使用教程 > 构建会议室分级体系：数据上钉实现会议室批量调度
> Updated: 2026-10-09 14:25:50

# 构建会议室分级体系：数据上钉实现会议室批量调度

本文档展示了，创建一个企业内部应用，使用智能会议室提供的API，实现创建、更新、查询及更新会议室分组相关流程。

## 概述

本方案提供一套完整的钉钉智能会议室分组管理解决方案，通过调用钉钉开放平台的会议室分组相关API，实现在业务系统中直接创建会议室分组、更新分组信息、查询分组列表及详情、删除分组等功能，支持建立多层级的会议室分类管理体系。

### 方案背景

企业在会议室管理中常面临以下痛点：

- **会议室数量庞大**：大型企业拥有数十甚至上百个会议室，缺乏有效的分类管理机制。
- **权限管理复杂**：不同部门、楼层的会议室需要不同的访问权限，手动配置效率低下。
- **资源调度困难**：无法按区域、功能对会议室进行分组管理，导致资源利用率低。
- **信息维护成本高**：会议室属性变更时，需要逐个更新，容易遗漏或出错。

### 核心价值

本方案提供一套完整的钉钉智能会议室分组管理解决方案，通过调用钉钉开放平台的会议室分组相关API，实现在业务系统中直接创建会议室分组、更新分组信息、查询分组列表及详情、删除分组等功能。

- **分级结构自动建立**：业务系统提交分组信息后一键同步至钉钉会议室分组，无需人工重新配置，大幅提升分组录入效率。
- **批量权限配置**：基于分组一次性配置整个分组内所有会议室的访问权限，减少80%的手动操作。
- **数据实时同步**：分组信息变更后自动更新钉钉端，确保双端数据一致性。
- **全生命周期管理**：从创建、更新、查询到删除，实现会议室分组全流程自动化管理。

### 适用场景

本方案适用于以下典型业务场景：

- **多楼层/多区域管理**：按物理位置（如A座1层、B座2层）对会议室分组。
- **部门专属会议室**：为各部门创建专属会议室分组，限制其他部门访问。
- **功能分类管理**：按会议室功能（如视频会议室、培训室、洽谈室）分组。
- **项目临时分组**：为特定项目创建临时会议室分组，项目结束后统一清理。

## 典型业务场景

### 场景一：集团总部多楼层会议室分级管理

#### 痛点分析

某集团总部拥有3栋办公楼，每栋楼5层，每层平均8个会议室，总计120个会议室。传统管理方式下：

- 管理员需要在列表中逐个查找目标会议室，效率极低
- 新员工入职时，需要手动为其分配可访问的会议室列表
- 会议室设备升级（如新增视频会议设备）时，无法批量更新同类型会议室

#### 价值验证

- **自动化流程**

  ![meeting_room_group_create_flow](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0517251971/p1103803.png)
- **关键优势**

  - **一键创建**：业务系统提交分组信息后自动创建钉钉会议室分组，无需人工重新配置。
  - **数据完整**：分组结构、成员、权限等核心信息完整同步，避免手动录入遗漏。
  - **实时同步**：分组信息变更后自动更新钉钉端，确保双端数据一致性。
  - **自动归档**：支持分组生命周期管理，项目结束后可统一清理临时分组。

### 场景二：部门专属会议室分组与权限自动化

#### 痛点分析

企业各部门有专属会议室需求,但权限管理复杂：

- HR、财务等敏感部门需要限制其他部门访问其会议室,手动配置权限耗时且易出错
- 新员工入职时需逐个分配可访问的会议室列表,大型公司数百名员工操作繁琐
- 部门调整或重组时,会议室访问权限需重新配置,缺乏批量更新机制
- 跨部门协作时,临时开放会议室权限后忘记收回,存在安全隐患

#### 价值验证

- **自动化流程**

  ![meeting_room_group_permission_flow](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0517251971/p1103804.png)
- **关键优势**

  - **权限批量配置**：将员工加入对应部门分组后，自动获得该分组下所有会议室的访问权限，减少90%的手动操作。
  - **动态权限调整**：部门调整时只需修改分组归属，无需逐个调整会议室权限，提升管理效率。
  - **安全可控**：支持设置分组可见性，确保敏感部门会议室仅对授权人员开放。

## 实施指南

### 技术架构

- **接口调用层**：调用会议室分组服务端API实现分组的创建、更新、查询、删除等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **分组管理层**：调用会议室分组相关API创建、更新、查询、删除分组，获取groupId。
- **数据同步层**：实现业务系统与钉钉会议室分组数据的双向同步，确保数据一致性。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `VideoConference.Conference.Write`（视频会议信息管理写权限）。
  - `VideoConference.Conference.Read`（视频会议信息管理读权限）。
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- SDK**准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请智能会议室相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用会议室相关API：

1. 调用服务端API-[创建会议室分组](0446-create-meeting-room-groups.md)接口，获取会议室分组返回结果`result`字段**，**即会议室分组ID**。**
2. 根据会议室分组ID，调用服务端API-[更新会议室分组信息](0449-update-meeting-room-groups.md)接口，实现会议室分组信息更新操作。
3. 调用服务端API-[查询会议室分组列表](0450-query-meeting-rooms-groups.md)接口，实现获取会议室分组列表内容。
4. 根据会议室分组ID，调用服务端API-[查询会议室分组信息](0451-query-meeting-room-groups.md)接口，实现获取单个会议室分组具体内容信息。
5. 根据会议室分组ID，调用服务端API-[删除会议室分组](0447-delete-a-conference-room-group.md)接口，实现删除会议室分组操作。

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

   - `VideoConference.Conference.Write`（视频会议信息管理写权限）— 用于创建、更新、删除会议室分组。
   - `VideoConference.Conference.Read`（视频会议信息管理读权限）— 用于查询会议室分组列表及详情。

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

1. **创建会议室分组**：调用服务端API-[创建会议室分组](0446-create-meeting-room-groups.md)接口，获取会议室分组返回结果`result`字段**，**即会议室分组ID**。**

   ```
   public void createRoomsGroups() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupHeaders createMeetingRoomGroupHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupHeaders();
       createMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建创建会议室分组请求参数
       com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupRequest createMeetingRoomGroupRequest =
               new com.aliyun.dingtalkrooms_1_0.models.CreateMeetingRoomGroupRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE")
                       .setGroupName("第一分组")
                       .setParentGroupId(0L);

       try {
           CreateMeetingRoomGroupResponse meetingRoomGroupWithOptions = client.createMeetingRoomGroupWithOptions(
                   createMeetingRoomGroupRequest, createMeetingRoomGroupHeaders, new RuntimeOptions());
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

   **参数说明**：

   - `unionId`：**重点参数**，操作人的unionId。
   - `groupName`：分组名称。
   - `parentGroupId`：**重点参数**，父分组ID，传0表示根分组。

   **返回字段**：

   - `result`：**重点参数**，创建的会议室分组ID。
2. **更新会议室分组信息**：根据会议室分组ID，调用服务端API-[更新会议室分组信息](0449-update-meeting-room-groups.md)接口，实现会议室分组信息更新操作。

   ```
   public void updateRoomsGroups() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupHeaders updateMeetingRoomGroupHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupHeaders();
       updateMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建更新会议室分组请求参数
       com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupRequest updateMeetingRoomGroupRequest =
               new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomGroupRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE")
                       .setGroupName("我的第一分组")
                       .setGroupId(39L);

       try {
           UpdateMeetingRoomGroupResponse updateMeetingRoomGroupResponse = client.updateMeetingRoomGroupWithOptions(
                   updateMeetingRoomGroupRequest, updateMeetingRoomGroupHeaders, new RuntimeOptions());
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

   **参数说明**：

   - `groupId`：**重点参数**，会议室分组ID（路径参数）。
   - `unionId`：**重点参数**，操作人的unionId。
   - `groupName`：分组名称。
3. **查询会议室分组列表**：调用服务端API-[查询会议室分组列表](0450-query-meeting-rooms-groups.md)接口，实现获取会议室分组列表内容。

   ```
   public void RoomsGroupsList() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListHeaders queryMeetingRoomGroupListHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListHeaders();
       queryMeetingRoomGroupListHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建查询会议室分组列表请求参数
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListRequest queryMeetingRoomGroupListRequest =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupListRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE");

       try {
           QueryMeetingRoomGroupListResponse queryMeetingRoomGroupListResponse = client.queryMeetingRoomGroupListWithOptions(
                   queryMeetingRoomGroupListRequest, queryMeetingRoomGroupListHeaders, new RuntimeOptions());
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

   **参数说明**：

   - `unionId`：**重点参数**，操作人的unionId。

   **返回字段**：

   - `result`：会议室分组列表数组，每个分组包含：

     - `groupId`：分组ID。
     - `groupName`：分组名称。
     - `parentGroupId`：父分组ID。
4. **查询会议室分组详情**：根据会议室分组ID，调用服务端API-[查询会议室分组信息](0451-query-meeting-room-groups.md)接口，实现获取单个会议室分组具体内容信息。

   ```
   public void RoomsGroupsInfo() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupHeaders queryMeetingRoomGroupHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupHeaders();
       queryMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建查询会议室分组详情请求参数
       com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupRequest queryMeetingRoomGroupRequest =
               new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE");

       try {
           QueryMeetingRoomGroupResponse queryMeetingRoomGroupResponse = client.queryMeetingRoomGroupWithOptions(
                   "39",
                   queryMeetingRoomGroupRequest,
                   queryMeetingRoomGroupHeaders,
                   new RuntimeOptions());
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

   **参数说明**：

   - `groupId`：**重点参数**，会议室分组ID（路径参数）。
   - `unionId`：**重点参数**，操作人的unionId。

   **返回字段**：

   - `groupId`：分组ID。
   - `groupName`：分组名称。
   - `parentGroupId`：父分组ID。
5. **删除会议室分组**：根据会议室分组ID，调用服务端API-[删除会议室分组](0447-delete-a-conference-room-group.md)接口，实现删除会议室分组操作。

   > **[!NOTE]**
   >
   > 若会议室分组下存在会议室，则该会议室分组无法删除。删除前需确保分组为空。

   ```
   public void deleteRoomsGroups() throws Exception {
       // 初始化客户端配置
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkrooms_1_0.Client client = new com.aliyun.dingtalkrooms_1_0.Client(config);

       // 设置请求头
       com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupHeaders deleteMeetingRoomGroupHeaders =
               new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupHeaders();
       deleteMeetingRoomGroupHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建删除会议室分组请求参数
       com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupRequest deleteMeetingRoomGroupRequest =
               new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomGroupRequest()
                       .setUnionId("E9CS6X*******eN7QiEiE");

       try {
           DeleteMeetingRoomGroupResponse deleteMeetingRoomGroupResponse = client.deleteMeetingRoomGroupWithOptions(
                   "40",
                   deleteMeetingRoomGroupRequest,
                   deleteMeetingRoomGroupHeaders,
                   new RuntimeOptions());
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

   **参数说明**：

   - `groupId`：**重点参数**，会议室分组ID（路径参数）。
   - `unionId`：**重点参数**，操作人的unionId。

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ 会议室分组读写权限申请成功。
- ✅ accessToken获取成功。
- ✅ 会议室分组创建成功，获取groupId。
- ✅ 会议室分组信息更新成功。
- ✅ 会议室分组列表查询成功，返回分组列表。
- ✅ 会议室分组详情查询成功，返回完整的分组信息。
- ✅ 会议室分组删除成功（确保分组为空）。

## 常见问题（FAQ）

- **Q1：创建会议室分组时必填哪些参数？**

  A：必填参数包括：

  - `unionId`：操作人的unionId
  - `parentGroupId`：父分组ID，传0表示根分组

  可选参数：

  - `groupName`：分组名称
- **Q2：如何获取groupId？**

  A：调用创建会议室分组接口后，接口返回的result字段即为会议室分组ID。此ID是后续所有会议室分组操作（更新、查询、删除）的唯一标识，务必妥善保存。
- **Q3：如何建立多级分组结构？**

  A：创建子分组时，将`parentGroupId`设置为父分组的`groupId`。例如：

  - 创建根分组：`parentGroupId = 0`
  - 创建一级子分组：`parentGroupId = 根分组的groupId`
  - 创建二级子分组：`parentGroupId = 一级子分组的groupId`
- **Q4：为什么删除会议室分组失败？**

  A：可能原因包括：

  - 应用未拥有智能会议室应用管理权限
  - groupId不正确
  - 会议室分组下仍存在会议室，需先清空分组内的会议室
- **Q5：会议室分组与会议室的关系是什么？**

  A：会议室分组是会议室的逻辑容器，用于对会议室进行分类管理。一个分组下可以包含多个会议室，但一个会议室只能属于一个分组。通过分组可以实现批量权限控制和统一管理。
