---
title: "客户触达提效：服务群消息自动发送与群发任务管理"
source_url: "https://open.dingtalk.com/document/development/enable-the-service-group-to-send-messages"
namespace: "development"
slug: "enable-the-service-group-to-send-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 集成方案 > 客户触达提效：服务群消息自动发送与群发任务管理"
doc_id: "n20TTzaUKI"
updated_at: "2026-10-19 09:11:48"
---

> Source: https://open.dingtalk.com/document/development/enable-the-service-group-to-send-messages
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 服务群 > 集成方案 > 客户触达提效：服务群消息自动发送与群发任务管理
> Updated: 2026-10-19 09:11:48

# 客户触达提效：服务群消息自动发送与群发任务管理

## **概述**

本方案面向需要高频客户触达的企业，通过集成钉钉开放平台服务群API，实现从场景服务群创建、单群消息发送到多群群发任务的全流程自动化管理，帮助企业提升客户服务效率、降低人工运营成本、保障消息触达一致性。

### **方案背景**

企业在客户服务和运营过程中，普遍面临以下挑战：

- **客户建群依赖人工操作**：销售或客服需手动为每个客户创建服务群，耗时耗力且容易遗漏关键信息录入。
- **群发通知缺乏统一管理**：运营活动、数据报告等群发任务分散在不同人员手中，难以追踪发送状态和覆盖范围。
- **服务质量无法量化评估**：群内客户问题和情绪反馈缺少系统化记录机制，难以及时发现并响应潜在风险。
- **活跃用户识别困难**：无法快速定位服务群中的高价值用户，导致资源投入与实际需求错配。

### **核心价值**

本方案通过调用钉钉开放平台的服务群相关API，实现在业务系统中直接创建服务群、消息发送、查询群活跃等功能。

- **服务群自动创建**：通过API批量创建场景服务群，消除人工建群的时间成本和信息误差。
- **消息发送集中管控**：单群发送与多群群发任务统一调度，支持发送状态实时查询与异常告警。
- **活跃用户精准识别**：调用活跃用户接口获取群内互动数据，支撑差异化服务策略制定。

### **适用场景**

本方案适用于以下典型业务场景：

- **线上引流建群**：通过网站/APP链接或线下海报二维码，自动为客户创建专属服务群并推送欢迎消息。
- **运营活动群发**：向多个服务群同步推送促销活动、产品更新、数据分析报告等运营内容。
- **服务质量监控**：定期查询服务群活跃用户列表，结合消息发送记录评估客户服务满意度与响应时效。
- **客户问题预警**：通过分析群内消息频次与关键词，及时发现客户投诉或负面情绪并触发人工介入。

## **典型业务场景**

### **场景一：线上引流自动建群（零售电商）**

#### **痛点分析**

某跨境电商企业日均新增客户咨询量超500次，过去依赖客服手动创建微信/钉钉服务群，存在以下问题：

- **建群效率低下**：每位客服每日最多处理80个客户建群请求，高峰期排队等待时间超过30分钟。
- **信息录入不一致**：不同客服对客户标签、来源渠道、需求分类的记录标准不统一，后续数据分析困难。
- **欢迎消息延迟**：建群后需人工复制粘贴欢迎语，平均延迟2-5分钟，影响客户首次体验。

#### **价值验证**

- **自动化流程**

  ![线上引流自动建群自动化流程场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8032732971/p1106631.jpg)
- **核心优势**

  - **秒级建群响应**：客户扫码或点击链接后，系统自动调用创建场景服务群API，3秒内完成建群并推送个性化欢迎消息。
  - **信息标准化录入**：建群时自动关联客户ID、来源渠道、咨询产品等结构化字段，确保数据一致性。
  - **全链路留痕追溯**：从客户触达到建群完成的每一步操作均有日志记录，支持多维度数据分析与历史回溯。

### **场景二：运营活动多群群发（教育培训）**

#### **痛点分析**

某在线教育平台拥有200+课程服务群，每月需推送课程更新、直播预告、学习报告等内容，原有流程存在以下问题：

- **群发任务分散执行**：不同运营人员各自负责部分群组，发送时间不统一，客户收到消息的时间差可达数小时。
- **发送状态不可见**：无法实时查看哪些群已成功发送、哪些群因成员变动导致发送失败，事后补发成本高。
- **活跃用户难识别**：无法区分高互动学员与沉默用户，导致营销资源平均分配，转化率偏低。

#### **价值验证**

- **自动化流程**

  ![运营活动多群群发自动化流程场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8032732971/p1106633.jpg)
- **核心优势**

  - **群发任务统一调度**：一次配置即可向所有目标服务群下发消息，系统自动处理发送队列与重试逻辑。
  - **发送状态实时监控**：调用群发任务接口后可查询每条消息的送达状态，失败群自动标记并支持一键补发。
  - **活跃用户精准筛选**：调用查询服务群活跃用户接口获取近7天互动数据，优先向高活跃群推送重点内容。

## **实施指南**

### **技术架构**

- **接口调用层**：通过钉钉开放平台服务群API实现场景服务群创建、消息发送、群发任务管理等能力。
- **应用认证层**：基于OAuth2.0协议完成企业授权，获取`accessToken`用于后续API调用。
- **业务逻辑层**：封装客户建群、消息发送、群发调度、活跃用户查询等核心业务流程，实现自动化触发与状态同步。
- **数据存储层**：企业内部数据库存储客户信息、服务群映射关系、发送记录等数据，钉钉作为消息通道与协同入口。
- **错误处理层**：对API调用失败、权限不足、群成员变更等情况进行捕获与重试，保障系统稳定性。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备：** 已完成钉钉开发者账号注册并完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求：**已在钉钉开发者后台为应用添加以下接口权限：

  - ServiceGroup.Group.ReadWrite （服务群读写权限）
  - ServiceGroup.Message.Send （服务群消息发送权限）
- **开发环境：** 已安装Java开发环境（JDK 8及以上版本）。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请服务群相关接口的权限。

步骤三，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，通过accessToken鉴权调用者身份。

步骤四，调用服务端服务群相关API：

1. 调用服务端API-[创建场景服务群](1119-create-a-scenario-service-group.md)接口，进行创建场景服务群，获取服务群openConversationId。
2. 根据服务群openConversationId，调用服务端API-[添加服务群成员](1120-add-service-group-members.md)接口，新增服务群成员。
3. 根据服务群openConversationId发送消息。

   - 单个群发送消息，根据服务群openConversationId，调用服务端API-[发送服务群消息](1118-service-group-message-sending-interface.md)接口，实现单个群消息的发送
   - 群发消息，根据不同服务群openConversationId，调用服务端API-[群发任务](1117-service-group-sending-task-interface.md)接口，实现不同服务群进行群发消息。
4. 根据服务群openConversationId，调用服务端API-[查询服务群活跃用户](1121-queries-active-service-users.md)接口，查看服务群的活跃用户。

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

   - `ServiceGroup.Group.ReadWrite （服务群读写权限）—— 用于创建场景服务群、添加/移除群成员。`
   - `ServiceGroup.Message.Send （服务群消息发送权限）—— 用于向服务群发送文本、图片、链接等类型消息。`

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

1. 调用服务端API-[创建场景服务群](1119-create-a-scenario-service-group.md)接口，进行创建场景服务群，获取服务群openConversationId。

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

   **参数说明**：

   - `groupBizId`：业务关联ID，自定义参数值。
   - `openTeamId`：开放团队ID。
   - `openGroupSetId`：开放群组ID。
   - `groupName`：群名称。
   - `ownerStaffId`：群主员工userid。
   - `memberStaffIds`：群成员员工ID列表，最大值20。
   - `groupTagNames`：群标签。

   **返回字段**：

   - `openConversationId`：开放群ID，用于后续发送消息、添加成员等操作。
   - `groupUrl`：加群的URL。
2. 根据服务群openConversationId，调用服务端API-[添加服务群成员](1120-add-service-group-members.md)接口，新增服务群成员。

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

   **参数说明**：

   - `openTeamId`：开放团队ID。
   - `openConversationId`：服务群openConversationId，来自创建场景服务群接口的返回值。
   - `userIds`：待添加员工在钉钉组织内的userId列表，最大值100。

   **返回字段**：

   - `success`：添加是否成功，true表示成功。
3. 根据服务群openConversationId发送消息。

   - 单个群发送消息，根据服务群openConversationId，调用服务端API-[发送服务群消息](1118-service-group-message-sending-interface.md)接口，实现单个群消息的发送

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

     **参数说明**：

     - `targetOpenConversationId`：开放群ID，来自创建场景服务群接口的返回值。
     - `title`：发送消息的标题。
     - `content`：发送消息的内容。
     - `atUnionIds`：被@人的unionId列表。
     - `receiverUnionIds`：接收者unionId列表。

     **返回字段**：

     - `processQueryKey`：异步消息处理键，用于后续查询消息发送状态。
   - 群发消息，根据不同服务群openConversationId，调用服务端API-[群发任务](1117-service-group-sending-task-interface.md)接口，实现不同服务群进行群发消息。

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

     **参数说明**：

     - `openTeamId`：团队ID。
     - `taskName`：群发任务名称。
     - `messageContent`：群发内容，包含`atAll`、`atActiveUser`、`messageType`、`title`、`content`、`images`、`btns`等子字段。
     - `queryGroup`：查询条件，用于指定目标服务群的筛选规则。
     - `sendConfig`：发送配置，控制群发任务的执行策略。

     **返回字段**：

     - `openBatchTaskId`：开放群发任务ID，用于后续查询任务执行状态。
4. 根据服务群openConversationId，调用服务端API-[查询服务群活跃用户](1121-queries-active-service-users.md)接口，查看服务群的活跃用户。

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

   **参数说明**：

   - `openTeamId`：开放团队ID。
   - `openConversationId`：群ID。

   **返回字段**：

   - `activeUserInfos`：活跃用户列表数组，每个元素包含以下字段：
   - `unionId`：用户unionId。
   - `nickName`：用户昵称。
   - `actionIndexL7d`：近7天行为指数。
   - `actionIndexL14d`：近14天行为指数。
   - `actionIndexL30d`：近30天行为指数。
   - `activeScore`：活跃度评分。
   - `ranking`：排名。

   **说明**：返回值为最活跃的用户TOP5，信息包含用户活跃度和行为指数。

## **实施完成检查清单**

- ✅ 应用凭证（`AppKey`和`AppSecret`）已安全获取并妥善保管。
- ✅ 接口权限（`ServiceGroup.Group.ReadWrite`、`ServiceGroup.Message.Send`）已成功添加并生效。
- ✅ `accessToken`获取与缓存机制已实现并通过测试。
- ✅ 创建场景服务群API调用成功，返回`openConversationId`格式符合预期。
- ✅ 添加服务群成员API调用成功，支持批量向单个服务群添加最多100名成员。
- ✅ 发送服务群消息API调用成功，消息类型覆盖文本、图片、链接。
- ✅ 群发任务创建API调用成功，支持批量向100个以内服务群下发消息。
- ✅ 查询服务群活跃用户API调用成功，返回数据包含用户ID、消息条数、最后活跃时间。
- ✅ 错误处理机制已部署，异常情况可自动重试并告警。

## **常见问题（FAQ）**

- **Q1：创建服务群时返回"权限不足"错误如何处理？**

  请检查是否已在开发者后台申请`ServiceGroup.Group.ReadWrite`权限，权限添加后需等待1-2分钟生效；若仍报错，重新获取`accessToken`后再试。
- **Q2：群发任务创建成功但部分群未收到消息是什么原因？**

  常见原因包括：目标群已被解散、群成员全部退出、消息内容触发风控拦截。请调用群发任务查询接口获取每个群的详细发送状态，针对失败群单独补发。
- **Q3：accessToken过期后如何处理？**

  当accessToken过期后，立即重新调用获取`accessToken`接口并更新缓存。建议在缓存中设置7000秒过期时间（早于官方7200秒），提前刷新避免业务中断。
- **Q4：如何确保服务群消息不被误判为垃圾信息？**

  避免短时间内向同一群发送超过5条消息；消息内容应包含明确的业务标识（如订单号、课程名称）；首次建群后发送欢迎消息时附带退订指引，降低用户举报风险。
