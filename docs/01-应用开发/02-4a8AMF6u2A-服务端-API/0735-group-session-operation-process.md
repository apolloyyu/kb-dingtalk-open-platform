---
title: "群会话全生命周期管理：建群、查群、管群全链路实践"
source_url: "https://open.dingtalk.com/document/development/group-session-operation-process"
namespace: "development"
slug: "group-session-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 集成方案 > 群会话全生命周期管理：建群、查群、管群全链路实践"
doc_id: "2JVIs4IAgf"
updated_at: "2026-10-14 09:16:59"
---

> Source: https://open.dingtalk.com/document/development/group-session-operation-process
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 集成方案 > 群会话全生命周期管理：建群、查群、管群全链路实践
> Updated: 2026-10-14 09:16:59

# 群会话全生命周期管理：建群、查群、管群全链路实践

## **概述**

本方案基于钉钉即时通信IM群会话API，介绍如何通过服务端接口实现群会话的创建、查询、管理及修改全流程。企业通过创建内部应用并调用群会话相关API，可将群管理操作集成到自有业务系统中，实现从业务事件触发建群、群信息查询、群权限管控到群信息维护的端到端自动化闭环。

### **方案背景**

企业在日常团队协作中，往往面临更深层的个性化诉求：业务系统需要自动创建项目群、客户群或应急群，但依赖人工手动建群效率低且易出错；群创建后缺乏统一的信息查询和管理机制，群成员变动、群信息更新等操作分散在不同入口，难以实现自动化运维；跨部门协作时群权限管控缺失，成员间私聊干扰工作沟通，群昵称不规范导致身份识别困难。钉钉即时通信IM提供了群会话创建、查询、管理等完整API链路，使这些需求得以快速落地。

### **核心价值**

- **群会话自动化创建：** 业务系统触发建群事件时自动调用API创建群会话并获取chatId，无需人工干预，建群效率提升90%以上。
- **群信息实时查询与管理：** 通过chatId一键查询群详情、批量设置管理员、更新群昵称、获取入群二维码，实现群会话全生命周期的程序化管控。
- **群权限精细化管控：** 支持设置禁止群成员私聊、批量配置群管理员角色，保障企业信息安全与沟通秩序，满足合规要求。
- **跨系统集成无缝衔接：** 群会话API与企业内部系统深度对接，实现从业务事件到群管理的端到端自动化闭环，消除信息孤岛。

### **适用场景**

- **智能制造产线异常协同：** 生产线设备告警触发时，MES系统自动创建故障应急群并拉入相关工程师，同步推送设备参数与维修记录，缩短故障响应时间至5分钟内。
- **律师事务所案件协作管理：** 案件立案后OA系统自动创建案件专属群，按角色设置群昵称（主办律师/协办律师/实习律师），禁止非授权成员私聊，确保案件信息安全合规。
- **零售连锁门店运营协同：** 新店开业筹备期自动创建门店筹备群，批量设置区域经理为群管理员，生成入群二维码供供应商扫码加入，实现多方高效协同。
- **金融机构客户服务响应：** 高净值客户咨询触发时CRM系统自动创建专属服务群，实时更新群成员昵称标注客户经理职级，保障服务专业性与响应时效。

## **典型业务场景**

### **场景一：智能制造产线异常协同群自动创建（智能制造行业）**

#### **痛点分析**

某大型装备制造企业拥有12条自动化产线，日均产生300+设备告警事件。过去依赖值班工程师手动建群协调维修，原有流程存在以下问题：

- **建群响应迟缓：** 设备告警触发后，值班工程师需手动创建应急群并逐一添加相关人员，平均建群耗时15分钟，故障响应总时长达45分钟，产线停机损失持续扩大。
- **成员遗漏频发：** 手动拉人依赖个人记忆，关键技术人员（如电气工程师、机械工程师）常被遗漏，曾发生5起因缺少专业人员导致故障误判的事件。
- **角色辨识困难：** 群内成员昵称未统一标注，多人同时发言时难以快速识别谁是主控负责人、谁负责具体模块，沟通效率低下。

#### **价值验证**

- **自动化流程**

  ![智能制造产线异常协同群自动创建场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9160491971/p1105513.png)
- **关键优势**

  - **群会话自动化创建：** MES系统检测到设备异常时，自动调用创建群会话API生成应急群并获取chatId，根据告警级别和故障类型自动拉入对应工程师团队，从告警触发到群创建完成仅需3秒，故障响应时间从45分钟缩短至8分钟。
  - **群信息实时查询与管理：** 通过查询群信息接口确认成员到位情况，利用更新群昵称接口为每位成员标注角色标识（主控/电气/机械），沟通时一眼识别负责人，协同效率提升70%，关键人员遗漏率从12%降至零。
  - **群权限精细化管控：** 通过批量设置管理员接口指定技术负责人为群管理者，确保群内沟通秩序可控，故障误判事件归零，月度产线停机损失降低62%。

### **场景二：律师事务所案件协作群合规管理（法律服务行业）**

#### **痛点分析**

某知名律师事务所年处理案件超2000件，涉及大量敏感客户信息与证据材料。此前案件群由助理手动创建和管理，原有流程存在以下问题：

- **合规风险突出：** 群成员添加缺乏审核机制，曾发生3起非授权人员被误拉入案件群导致案情泄露的事件，律所面临客户投诉和执业纪律处分风险。
- **私聊管控缺失：** 群成员间可自由发起单聊，敏感案件信息通过私聊渠道传播难以追溯，合规审计时无法证明信息流转可控。
- **身份标识混乱：** 群内律师昵称格式不统一，实习生与主办律师难以区分，客户在群内咨询时经常找错对接人，影响服务专业形象。

#### **价值验证**

- **自动化流程**

  ![律师事务所案件协作群合规管理场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9160491971/p1105514.png)
- **关键优势**

  - **群会话自动化创建：** 案件管理系统立案时自动调用创建群会话API生成案件专属群，根据案件类型和参与人员自动拉入主办律师、协办律师及实习助理，非授权人员误拉事件归零。
  - **群信息实时查询与管理：** 通过更新群昵称接口统一标注"主办-张律师""协办-李律师""实习-王助理"等角色标识，客户咨询时精准对接对应律师，服务满意度从82%提升至96%；通过获取入群二维码链接接口生成扫码入口供授权人员加入。
  - **群权限精细化管控：** 通过批量设置管理员接口指定主办律师为群管理者，启用禁止群成员私聊功能确保所有沟通在群内公开进行，敏感信息流转全程可追溯，合规审计通过率提升至100%，客户投诉降为零。

## 实施指南

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有服务端调用的身份合法性。
- **群会话创建层：** 根据业务事件自动生成群聊并获取唯一标识，支持按业务规则动态配置群名称、群主及初始成员。
- **群信息查询层：** 实现群详情读取和标识符转换，为后续管理操作提供数据基础。
- **群权限管控层：** 实现群角色分配和沟通规则配置，保障企业信息安全与合规要求。
- **群信息维护层：** 实现群成员身份标注、入群渠道管理和群基础信息动态维护。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 申请以下接口权限：

  - `qyapi_chat_manage`（群会话管理权限）
  - `qyapi_chat_read`（群会话读取权限）
  - `qyapi_chat_base_read`（群会话基础读取权限）
- **开发环境：** 已安装Java开发环境（JDK 8及以上版本）。
- **SDK准备：** 下载钉钉服务端SDK，版本建议最新稳定版。

### **代码实现**

步骤一：获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“场景群”和“群管理”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

步骤四：调用服务端群会话相关API。

1. 调用服务端API-[创建群会话](0736-create-common-group-new-version-v2.md)接口，进行创建群会话，获取群会话`chatId`。
2. 根据群会话`chatId`，调用服务端API-[查询群信息](0738-obtain-a-group-session.md)接口，获取群会话的信息。
3. 根据群会话`chatId`，调用新版服务端API-[获取群会话的OpenConversationId](0743-obtain-group-openconversationid.md)接口，获取群会话`openConversationId`。

步骤五：根据群会话chatId进行群会话管理操作。

- 根据群会话`chatId`，调用服务端API-[批量设置企业群管理员](0740-batch-setup-group-administrator.md)接口，进行群会话管理员的设置。
- 根据群会话`chatId`，调用服务端API-[设置禁止群成员私聊](0741-set-private-chat.md)接口，设置群会话群成员间是否可以私聊。
- 根据群会话`chatId`，调用服务端API-[更新群成员的群昵称](0739-set-a-group-nickname.md)接口，进行设置群会话成员的昵称。
- 根据群会话`chatId`，调用服务端API-[获取入群二维码链接](0742-obtain-a-qr-code-link.md)接口，其他的企业成员点击链接即可申请加入群聊。
- 根据群会话`chatId`，调用服务端API-[更新群会话](0737-api-updategroup.md)接口，进行群会话信息的修改。

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

   - `qyapi_chat_manage`（群会话管理权限）
   - `qyapi_chat_read`（群会话读取权限）
   - `qyapi_chat_base_read`（群会话基础读取权限）

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

### **步骤四：****核心API调用**

1. 调用服务端API-[创建群会话](0736-create-common-group-new-version-v2.md)接口，进行创建群会话，获取群会话chatId。

   ```
   public void createGroup() throws Exception{
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
       CreateGroupHeaders createGroupHeaders = new CreateGroupHeaders();
       createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
       CreateGroupRequest.CreateGroupRequestManagementOptions managementOptions = new CreateGroupRequest.CreateGroupRequestManagementOptions()
         .setMentionAllAuthority(0)
         .setShowHistoryType(0)
         .setValidationType(0)
         .setSearchable(0)
         .setChatBannedType(0)
         .setManagementType(0);
       CreateGroupRequest createGroupRequest = new CreateGroupRequest()
         .setName("测试群")
         .setOwner("manager4220")
         .setOwnerType("emp")
         .setUseridlist(java.util.Arrays.asList(
           "userId"
         ))
         .setConversationTag(2L)
         .setExtidlist(java.util.Arrays.asList(
           "unionId"
         ))
         .setIcon("@mediaId")
         .setManagementOptions(managementOptions);
       try {
         client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       } catch (TeaException err) {
         if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       } catch (Exception _err) {
         TeaException err = new TeaException(_err.getMessage(), _err);
         if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       }        
     }
   ```

   **请求参数：**

   - `name`：群会话名称。
   - `owner`：群主的userId，必须是企业内部有效用户。
   - `useridlist`：初始群成员的userId列表，至少包含群主本人。

   **返回字段：**

   - `conversationTag`：群类型。
   - `openConversationId`：群会话ID。
   - `chatId`：群会话唯一标识，后续所有群管理接口的必传参数。
2. 根据群会话chatId，调用服务端API-[查询群信息](0738-obtain-a-group-session.md)接口，获取群会话的信息。

   ```
   public void getChatInfo() {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/get");
     OapiChatGetRequest req = new OapiChatGetRequest();
     req.setChatid("chate39f540dxxxx");
     req.setHttpMethod("GET");
     OapiChatGetResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getChatInfo());
   }
   ```

   **请求参数：**

   - `chatid`：群会话的ID。

   **返回字段：**

   - `chat_info`：群会话详细信息对象，包含群名称、群主、成员列表等。
3. 根据群会话`chatId`，调用新版服务端API-[获取群会话的OpenConversationId](0743-obtain-group-openconversationid.md)接口，获取群会话`openConversationId`。

   ```
   public void chatIdToOpenConversationId() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
           ChatIdToOpenConversationIdHeaders chatIdToOpenConversationIdHeaders = new ChatIdToOpenConversationIdHeaders();
           chatIdToOpenConversationIdHeaders.xAcsDingtalkAccessToken = "accessToken";
           try {
               ChatIdToOpenConversationIdResponse response = client.chatIdToOpenConversationIdWithOptions("chatId", chatIdToOpenConversationIdHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(response.getBody()));
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

   **请求参数：**

   - `chatId`：群会话唯一标识，作为路径参数传入。

   **返回字段：**

   - `openConversationId`：新版IM API使用的群会话标识符。
4. 根据群会话`openConversationId`，调用新版服务端API-[批量设置企业群管理员](0740-batch-setup-group-administrator.md)接口，批量设置群管理员。

   ```
   public void chatSubAdminUpdate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
           ChatSubAdminUpdateHeaders chatSubAdminUpdateHeaders = new ChatSubAdminUpdateHeaders();
           chatSubAdminUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
           ChatSubAdminUpdateRequest chatSubAdminUpdateRequest = new ChatSubAdminUpdateRequest()
                   .setOpenConversationId("cidVwhxxxxxLjUA==")
                   .setUserIds(java.util.Arrays.asList(
                       "wZ1vjnPOIxxxxxMTGJGy"
                   ))
                   .setRole(2);
           try {
               ChatSubAdminUpdateResponse chatSubAdminUpdateResponse = client.chatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(chatSubAdminUpdateResponse.getBody()));
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

   **请求参数：**

   - `openConversationId`：群会话新版标识符，由获取OpenConversationId接口返回。
   - `userIds`：企业员工userid列表。
   - `role`：角色类型，2表示设置为管理员，1表示取消管理员。

   **返回字段：**

   - `success`：操作是否成功的布尔值。

### **步骤五：群会话管理**

- 根据群会话`chatId`，调用服务端API-[设置禁止群成员私聊](0741-set-private-chat.md)接口，设置群会话群成员间是否可以私聊。

  ```
  public void updateChatMemberFriendswitch() {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/member/friendswitch/update");
    OapiChatMemberFriendswitchUpdateRequest req = new OapiChatMemberFriendswitchUpdateRequest();
    req.setChatid("chatdafe234xxxx");
    req.setIsProhibit(true);
    OapiChatMemberFriendswitchUpdateResponse rsp = client.execute(req, access_token);
    System.out.println(rsp.getBody());
  }
  ```

  **请求参数：**

  - `chatid`：群会话唯一标识。
  - `is_prohibit`：是否开启禁止开关，true为开启禁止开关，false为关闭禁止开关。

  **返回字段：**

  - `success`：错误码，true表示成功。
- 根据群会话`chatId`，调用服务端API-[更新群成员的群昵称](0739-set-a-group-nickname.md)接口，进行设置群会话成员的昵称。

  ```
  public void updateChatMemberNick() {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/updategroupnick");
    OapiChatUpdategroupnickRequest req = new OapiChatUpdategroupnickRequest();
    req.setUserid("user123");
    req.setChatid("chate39f540d572b71cf97a556d95929fxxxx");
    req.setGroupNick("钉钉小二");
    OapiChatUpdategroupnickResponse rsp = client.execute(req, access_token);
    System.out.println(rsp.getBody());
  }
  ```

  **请求参数：**

  - `chatid`：群会话唯一标识。
  - `userid`：待更新昵称的成员userId。
  - `group_nick`：该成员在群中的昵称。

  **返回字段：**

  - `success`：错误码，true表示成功。
- 根据群会话`chatId`，调用服务端API-[获取入群二维码链接](0742-obtain-a-qr-code-link.md)接口，其他的企业成员点击链接即可申请加入群聊。

  ```
  public void getChatURL() {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/qrcode/get");
    OapiChatQrcodeGetRequest req = new OapiChatQrcodeGetRequest();
    req.setChatid("chat32****3a");
    req.setUserid("manager4220");
    OapiChatQrcodeGetResponse rsp = client.execute(req, access_token);
    System.out.println(rsp.getBody());
  }
  ```

  **请求参数：**

  - `chatid`：群会话唯一标识。
  - `userid`：分享二维码用户的userId，需具备群管理权限。

  **返回字段：**

  - `result`：入群二维码链接地址，可直接用于生成二维码图片。
- 根据群会话`chatId`，调用服务端API-[更新群会话](0737-api-updategroup.md)接口，进行群会话信息的修改。

  ```
  public void createGroup() throws Exception{
      Config config = new Config();
      config.protocol = "https";
      config.regionId = "central";
      com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
      UpdateGroupHeaders updateGroupHeaders = new UpdateGroupHeaders();
      updateGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
      UpdateGroupRequest.UpdateGroupRequestManagementOptions managementOptions = new UpdateGroupRequest.UpdateGroupRequestManagementOptions()
        .setMentionAllAuthority(0)
        .setShowHistoryType(0)
        .setValidationType(0)
        .setSearchable(0)
        .setChatBannedType(0)
        .setManagementType(0);
      UpdateGroupRequest updateGroupRequest = new UpdateGroupRequest()
        .setChatid("chatxxxx")
        .setName("全员群。")
        .setOwner("04201724372xxxx")
        .setOwnerType("emp")
        .setAddUseridlist(java.util.Arrays.asList(
          "userid1"
        ))
        .setDelUseridlist(java.util.Arrays.asList(
          "userid1"
        ))
        .setAddExtidlist(java.util.Arrays.asList(
          "unionId"
        ))
        .setDelExtidlist(java.util.Arrays.asList(
          "unionId"
        ))
        .setIcon("@mediaId")
        .setManagementOptions(managementOptions);
      try {
        client.updateGroupWithOptions(updateGroupRequest, updateGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
      } catch (TeaException err) {
        if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
          // err 中含有 code 和 message 属性，可帮助开发定位问题
        }

      } catch (Exception _err) {
        TeaException err = new TeaException(_err.getMessage(), _err);
        if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
          // err 中含有 code 和 message 属性，可帮助开发定位问题
        }
      }        
    }
  ```

  **请求参数：**

  - `chatid`：群会话唯一标识。
  - `name`：新的群名称，可选参数。

  **返回字段：**

  - `success`：错误码，true表示成功。

**实施完成检查清单**

- ✅ 应用Client ID和Client Secret已安全配置，未硬编码在源码中。
- ✅ `qyapi_chat_manage`、`qyapi_chat_read`、`qyapi_chat_base_read`三项权限已申请并通过审批。
- ✅ accessToken获取逻辑已实现缓存与自动刷新机制，避免频繁请求限流。
- ✅ 创建群会话接口调用成功，chatId已持久化存储于业务数据库。
- ✅ 查询群信息接口返回数据与预期一致，群成员列表完整准确。
- ✅ `OpenConversationId`获取成功，新版API接口调用正常。
- ✅ 批量设置管理员接口执行无误，角色分配符合业务需求。
- ✅ 禁止私聊功能已按场景要求正确开启或关闭。
- ✅ 群昵称更新生效，成员角色标识清晰可辨。
- ✅ 入群二维码链接生成成功，扫码测试可正常申请入群。
- ✅ 更新群会话接口验证通过，群信息修改实时生效。
- ✅ 所有API调用异常捕获完善，错误日志记录完整便于排查。

## **常见问题（FAQ）**

- **Q1：chatId和openConversationId有什么区别？何时使用哪个？**

  - `chatId`是旧版API使用的群会话标识符，适用于创建群、查询群信息、禁止私聊、更新昵称、获取二维码、更新群信息等接口。
  - `openConversationId`是新版IM API的统一标识符，目前主要用于批量设置企业群管理员等新版接口。建议业务系统中同时存储两个ID，根据具体接口文档要求选择使用。
- **Q2：创建群会话时提示"userid不在本企业通讯录"如何处理？**

  该错误通常由以下原因导致：

  - 传入的userId不属于当前企业组织架构；
  - 用户已被离职或删除；
  - userId格式错误（应为钉钉内部userId而非手机号或工号）。
  - 请通过通讯录API校验userId有效性后再调用建群接口。
- **Q3：批量设置管理员接口返回权限不足怎么办？**

  - 确认已申请`qyapi_chat_manage`权限且审批通过；
  - 检查调用方是否为群主或已有管理员身份；
  - 验证openConversationId是否正确（注意不是chatId）。
  - 若仍失败，联系钉钉技术支持提供request\_id进行排查。
- **Q4：入群二维码链接是否有有效期？如何续期？**

  入群二维码链接具有有限期，若群被解散链接将自动失效。如需重新生成，调用获取入群二维码链接接口即可获取新链接。
