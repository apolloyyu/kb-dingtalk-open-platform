---
title: "通知自动发布：从自有系统到钉钉公告的触达闭环"
source_url: "https://open.dingtalk.com/document/development/create-and-delete-announcements"
namespace: "development"
slug: "create-and-delete-announcements"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "公告 > 使用教程 > 通知自动发布：从自有系统到钉钉公告的触达闭环"
doc_id: "DXnHG9nq6w"
updated_at: "2026-09-23 12:04:36"
---

> Source: https://open.dingtalk.com/document/development/create-and-delete-announcements
> Path: 应用开发 / 服务端 API / 公告 > 使用教程 > 通知自动发布：从自有系统到钉钉公告的触达闭环
> Updated: 2026-09-23 12:04:36

# 通知自动发布：从自有系统到钉钉公告的触达闭环

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现公告的创建、查询、更新及删除操作，支持将业务系统中的通知公告自动发布至钉钉公告模块，实现统一通知管理。

## 概述

本方案提供一套完整的企业公告管理解决方案，通过钉钉开放平台的公告API，实现将企业自有系统中的通知公告自动发布至钉钉公告模块，并支持查询公告列表、获取公告详情、更新公告内容及删除公告等完整操作流程。

### 方案背景

企业在日常运营中常面临以下痛点：

- **公告手动发布耗时**：业务系统中已拟定的通知公告，仍需人工逐个在钉钉公告中重新编辑发布，重复操作效率极低。
- **触达范围难控制**：外部系统发布的公告无法精准定向特定部门或人员，容易遗漏关键接收人。
- **状态无法追踪**：公告是否被阅读、哪些人已读未读，缺乏统一的阅读状态视图，发布者难以掌握实际触达效果。
- **数据孤岛阻碍协同**：公告数据未与企业通讯录、审批、待办等模块打通，无法基于组织架构自动匹配相关人员。

### 核心价值

本方案提供一套完整的企业公告管理解决方案，通过钉钉开放平台的公告API，实现将企业自有系统中的通知公告自动发布至钉钉公告模块，并支持查询公告列表、获取公告详情、更新公告内容及删除公告等完整操作流程。

- **公告自动发布**：业务系统确定公告内容后一键同步至钉钉公告，无需人工重新编辑，大幅提升通知发布效率。
- **精准定向推送**：支持按部门、人员精准设置接收范围，确保重要通知触达目标人群。
- **阅读状态实时追踪**：支持查询每位接收人的阅读状态，发布者实时掌握公告触达效果。
- **组织架构联动**：基于钉钉通讯录自动匹配接收人员，支持按部门、角色批量添加，减少手动查找成本。

### 适用场景

本方案适用于以下典型业务场景：

- **企业内部OA系统公告同步**：自研OA系统中的通知公告自动同步至钉钉公告模块，避免人工重复发布。
- **HR系统政策文件发布**：人力资源系统中的制度文件、薪资调整通知等自动发布为钉钉公告并定向推送相关部门。
- **财务系统报表通知同步**：财务报表、预算通知等从财务系统自动同步至钉钉公告并添加相关审批人为接收人。
- **安全生产系统预警公告联动**：安全预警、应急预案等信息自动创建为钉钉公告事件，相关人员一键加入为接收人，自动接收提醒。

## 典型业务场景

### 场景一：内部OA系统公告同步至钉钉公告

#### 痛点分析

企业使用自研OA系统拟定通知公告，但公告仍需人工逐个在钉钉公告中重新编辑发布，导致：

- 大型通知动辄数十个接收部门，手动添加耗时且易遗漏
- 公告变更时需重新逐个操作，效率极低
- 无法实时追踪每位接收人的阅读状态（已读/未读）
- 公告内容调整时，需人工重新通知所有接收人

#### 价值验证

- **自动化流程**

  ![OA系统公告同步流程图_20260921_141203](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6726310971/p1103372.png)
- **关键优势**

  - **公告自动发布**：OA系统创建公告后1秒内自动发布至钉钉公告模块，无需手动重新编辑。
  - **阅读状态实时回写**：支持接收人已读/未读状态实时回写至OA系统，确保双端数据一致。
  - **变更自动通知**：公告内容更新时自动推送更新通知，无需人工干预。

### 场景二：HR系统政策文件定向发布

#### 痛点分析

人力资源系统中的制度文件、薪资调整通知等仅存在于HR系统中，员工容易遗忘：

- 非HR部门员工无法感知重要政策变化，需人工逐个通知
- 缺乏统一的公告阅读状态视图，HR难以掌握实际触达情况
- 到期前无主动提醒，依赖人工跟进确认
- 跨部门协调时，无法快速查看各政策的接收人覆盖情况

#### 价值验证

图:图:HR系统政策文件自动发布为钉钉公告并定向推送相关部门

- **自动化流程**

  ![HR政策文件发布流程图_20260921_141301](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6726310971/p1103373.png)
- **关键优势**

  - **自动关联相关部门**：政策文件自动将相关部门负责人和员工添加为接收人，无需手动逐个选择。
  - **DING紧急提醒**：支持重要政策提前N天触发钉钉DING紧急提醒，确保关键信息不遗漏。
  - **阅读状态闭环追踪**：公告发布后自动统计接收人阅读状态（已读/未读），形成完整的政策触达闭环。

## 实施指南

### 技术架构

- **接口调用层**：调用公告服务端API实现公告的创建、查询、更新、删除操作。
- **用户标识获取层**：调用通讯录服务端API获取部门用户详情，获取企业员工在钉钉组织架构中的userId值信息。
- **公告数据同步层**：调用公告服务端API将自有系统的公告信息同步到钉钉公告模块。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

**API版本说明**：服务端API存在新版与旧版差异，建议优先使用新版API以获得更好的性能和功能支持。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_blackboard_manage`（钉钉公告管理权限）
  - `qyapi_blackboard_read`（钉钉公告读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请公告相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端公告相关API。

1. 调用服务端API-[创建公告](0281-create-an-enterprise-announcement.md)接口，进行公告创建。
2. 调用服务端API-[获取公告ID列表](0285-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口，获取公告`blackboardId`。
3. 根据公告blackboardId进行公告管理。

   - 根据公告`blackboardId`，调用服务端API-[获取公告详情](0284-obtains-the-details-get-blackboard.md)接口，实现获取公告详情信息。
   - 根据公告`blackboardId`，调用服务端API-[更新公告](0283-modify-the-announcement-according-to-the-announcement-id.md)接口，实现更新公告内容。
   - 根据公告`blackboardId`，调用服务端API-[删除公告](0282-delete-announcements-based-on-the-announcement-id.md)接口，实现删除公告。

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

   - `qyapi_blackboard_manage`（钉钉公告管理权限）— 用于创建、更新、删除公告。
   - `qyapi_blackboard_read`（钉钉公告读权限）— 用于查询公告列表及详情。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

```
public String getAccessToken() {
    com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
    config.protocol = "https";
    config.regionId = "central";
    try {
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("dingeqqpkv3xxxxxx")
                .setAppSecret("GT-lsu-taDAxxxsTsxxxx");
        GetAccessTokenResponse response = client.getAccessToken(getAccessTokenRequest);
        System.out.println(response.getBody());
        return response.getBody().getAccessToken();
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：核心API调用**

1. **创建公告**：调用服务端API-[创建公告](0281-create-an-enterprise-announcement.md)接口，进行公告创建。

   ```
   public void createNotice() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/create");

       OapiBlackboardCreateRequest req = new OapiBlackboardCreateRequest();

       // 公告基本信息
       OapiBlackboardCreateRequest.OapiCreateBlackboardVo boardVoObj = new OapiBlackboardCreateRequest.OapiCreateBlackboardVo();
       boardVoObj.setOperationUserid("ma*******75");
       boardVoObj.setAuthor("小钉");
       boardVoObj.setTitle("入职须知");
       boardVoObj.setContent("欢迎加入我们的大家庭");
       boardVoObj.setCoverpicMediaid("@lADPDeC2ufXOeRzMqM0BLA");
       boardVoObj.setPrivateLevel(0L);
       boardVoObj.setDing(true);
       boardVoObj.setPushTop(true);

       // 接收人配置
       OapiBlackboardCreateRequest.BlackboardReceiverOpenVo receiverOpenVoObj = new OapiBlackboardCreateRequest.BlackboardReceiverOpenVo();
       receiverOpenVoObj.setUseridList(Arrays.asList("0147**********41"));
       boardVoObj.setBlackboardReceiver(receiverOpenVoObj);

       req.setCreateRequest(boardVoObj);

       OapiBlackboardCreateResponse rsp = client.execute(req, "access_token");
       System.out.println(rsp.getBody());
   }
   ```

   **参数说明**：

   - `title`：**重点参数**，公告标题
   - `content`：**重点参数**，公告内容
   - `useridList`：接收人userId列表
2. **获取公告ID列表**：调用服务端API-[获取公告ID列表](0285-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口，获取公告`blackboardId`。

   ```
   public void getListIds() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/listids");

       OapiBlackboardListidsRequest req = new OapiBlackboardListidsRequest();

       // 查询条件配置
       OapiBlackboardListidsRequest.OapiBlackboardQueryVo queryVoObj = new OapiBlackboardListidsRequest.OapiBlackboardQueryVo();
       queryVoObj.setOperationUserid("ma*******75");
       queryVoObj.setPage(1L);
       queryVoObj.setPageSize(10L);
       queryVoObj.setStartTime(StringUtils.parseDateTime("2022-10-08 00:00:00"));
       queryVoObj.setEndTime(StringUtils.parseDateTime("2022-10-09 00:00:00"));

       req.setQueryRequest(queryVoObj);

       OapiBlackboardListidsResponse rsp = client.execute(req, "access_token");
       System.out.println(rsp.getBody());
   }
   ```
3. **获取公告详情**：根据公告`blackboardId`，调用服务端API-[获取公告详情](0284-obtains-the-details-get-blackboard.md)接口，实现获取公告详情信息。

   > **[!NOTE]**
   >
   > 公告的保密级别和查看权限要求如下：
   >
   > - 非保密公告，全公司员工可查看
   > - 保密公告，公告管理员或公告的接收人可查看

   ```
   public GetBlackboardResponseBody getInfo() {
       com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
       config.protocol = "https";
       config.regionId = "central";
       try {
           com.aliyun.dingtalkblackboard_1_0.Client client = new com.aliyun.dingtalkblackboard_1_0.Client(config);
           // 设置请求头
           GetBlackboardHeaders getBlackboardHeaders = new GetBlackboardHeaders();
           getBlackboardHeaders.xAcsDingtalkAccessToken = "<your access token>";
           // 构建请求参数
           GetBlackboardRequest getBlackboardRequest = new GetBlackboardRequest()
                   .setOperationUserId("manager01")
                   .setBlackboardId("ca80xxxx0a04");
           // 调用API
           GetBlackboardResponse response = client.getBlackboardWithOptions(
                   getBlackboardRequest, getBlackboardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
           System.out.println(response.getBody());
           return response.getBody();
       } catch (Exception e) {
           throw new RuntimeException(e);
       }
   }
   ```

   **参数说明**：

   - `blackboardId`：**重点参数**，公告ID，可通过获取公告ID列表接口获取。
4. **更新公告**：根据公告`blackboardId`，调用服务端API-[更新公告](0283-modify-the-announcement-according-to-the-announcement-id.md)接口，实现更新公告内容。

   > **[!NOTE]**
   >
   > 只有以下权限的人员可更新公告：
   >
   > - 主管理员
   > - 公告子管理员并且是待修改公告的创建者

   ```
   public void updateNotice() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/update");

       OapiBlackboardUpdateRequest req = new OapiBlackboardUpdateRequest();

       // 公告更新信息
       OapiBlackboardUpdateRequest.OapiUpdateBlackboardVo boardVoObj = new OapiBlackboardUpdateRequest.OapiUpdateBlackboardVo();
       boardVoObj.setBlackboardId("206**********ae9");
       boardVoObj.setOperationUserid("ma*******5");
       boardVoObj.setAuthor("小钉");
       boardVoObj.setTitle("入职须知2");
       boardVoObj.setContent("欢迎加入我们的大家庭2");
       boardVoObj.setCoverpicMediaid("@lADPDeC2ufXOeRzMqM0BLA");
       boardVoObj.setDing(true);
       boardVoObj.setNotify(true);

       req.setUpdateRequest(boardVoObj);

       OapiBlackboardUpdateResponse rsp = client.execute(req, getAccessToken());
       System.out.println(rsp.getBody());
   }
   ```

   **参数说明**：

   - `blackboardId`：重点参数，公告ID
   - `title`：更新后的公告标题
   - `content`：更新后的公告内容
   - `notify`：重点参数，修改后是否再次通知接收人，`true`表示发送，`false`表示不发送
5. 删除公告：根据公告`blackboardId`，调用服务端API-[删除公告](0282-delete-announcements-based-on-the-announcement-id.md)接口，实现删除公告。

   > **[!NOTE]**
   >
   > 只有以下身份可以删除：
   >
   > - 主管理员
   > - 公告子管理员并且是待删除公告创建者

   ```
   public void deleteNotice() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/delete");

       OapiBlackboardDeleteRequest req = new OapiBlackboardDeleteRequest();
       req.setBlackboardId("206**********ae9");
       req.setOperationUserid("001");

       OapiBlackboardDeleteResponse rsp = client.execute(req, getAccessToken());
       System.out.println(rsp.getBody());
   }
   ```

   **参数说明**：

   - `blackboardId`：重点参数，公告ID
   - `operationUserId`：操作人的userId

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ 公告读写权限申请成功。
- ✅ access\_token获取成功。
- ✅ 创建公告接口调用成功，公告出现在钉钉公告模块。
- ✅ 获取公告列表接口调用成功，返回正确的公告ID列表。
- ✅ 获取公告详情接口调用成功，返回正确的公告详情。
- ✅ 更新公告接口调用成功，公告内容已更新。
- ✅ 删除公告接口调用成功，公告已从公告模块移除。

## 常见问题（FAQ）

- **Q1：创建公告时必填哪些参数？**

  A：必填参数包括：

  - `title`：公告标题
  - `content`：公告内容
- **Q2：更新公告时有哪些权限限制？**

  A：只有以下权限的人员可更新公告：

  - 主管理员
  - 公告子管理员并且是待修改公告的创建者
- **Q3：公告同步失败的常见原因有哪些？**

  A：常见原因包括：

  - userId不正确（必须是钉钉组织架构中存在的员工userId）
  - blackboardId不正确（必须是已创建的公告ID）
  - access\_token无效或已过期
  - 应用未申请公告相关权限
  - 网络请求超时或服务器异常
- **Q4：批量创建公告的最佳实践是什么？**

  A：当前接口支持单次创建一个公告。如需批量创建，建议在业务层循环调用该接口，注意控制调用频率避免触发限流。
