---
title: "客户群管理：让每个客户群都纳入统一管控体系"
source_url: "https://open.dingtalk.com/document/development/crm-customer-group-operation-process"
namespace: "development"
slug: "crm-customer-group-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 集成方案 > 客户群管理：让每个客户群都纳入统一管控体系"
doc_id: "eXcenZ0ww1"
updated_at: "2026-10-22 17:12:17"
---

> Source: https://open.dingtalk.com/document/development/crm-customer-group-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 集成方案 > 客户群管理：让每个客户群都纳入统一管控体系
> Updated: 2026-10-22 17:12:17

# 客户群管理：让每个客户群都纳入统一管控体系

## **概述**

本方案基于钉钉CRM客户群组与客户群API，实现企业客户服务群组的创建、更新、查询及客户群的批量管理，支持将客户服务沟通纳入钉钉CRM统一管控体系。

### **方案背景**

企业在客户服务运营过程中，常需围绕客户建立专属服务群组，但传统方式存在以下痛点：

- **群组分散难管理**：服务群散落在个人会话中，缺乏统一的群组资产视图，人员变动后客户资源易流失。
- **群信息不完整**：群组名称、公告、成员配额等关键信息未与CRM客户数据关联，无法支撑精细化运营。
- **批量操作效率低**：逐个创建或查询群组耗时费力，缺少条件筛选和分页拉取能力。
- **权限管控缺失**：群主、管理员、协同人角色未结构化定义，责任边界模糊导致响应滞后。

### **核心价值**

本方案通过调用钉钉CRM客户群组与客户群接口，实现服务群组的标准化管理：

- **群组资产集中沉淀**：所有服务群组归属企业而非个人，人员离职时群组可无缝交接。
- **群信息结构化维护**：支持设置群名称、公告、置顶状态、欢迎语、成员配额等完整属性。
- **高效批量检索**：支持按名称搜索、关系类型筛选、分页游标连续拉取，单次最多返回指定条数记录。
- **角色权限精细定义**：明确群主、管理员、成员三级角色，确保服务响应责任到人。

### **适用场景**

本方案适用于以下典型业务场景：

- **VIP客户服务群运营**：为高价值客户建立专属服务群，配置固定服务人员并设置个性化欢迎语。
- **项目交付协同群管理**：围绕交付项目创建临时协同群，项目结束后归档或解散，过程留痕可追溯。
- **区域销售服务群统筹**：按区域或产品线批量创建服务群，统一管理群公告与成员配额，提升标准化服务水平。

## **典型业务场景**

### **场景一：VIP客户服务群标准化运营**

#### **痛点分析**

某金融企业的客户经理在维护高净值客户时，依赖微信或个人钉钉群进行沟通，存在以下问题：

- 客户经理离职后，客户服务群随之失联，历史沟通记录无法继承。
- 不同经理的服务群命名规则不统一，管理层无法快速识别群组所属客户等级。
- 新入群成员缺乏标准化欢迎流程，客户体验参差不齐。
- 群成员数量无上限控制，部分群组膨胀至数百人，重要消息被淹没。

#### **价值验证**

- **自动化流程**

  ![VIP客户服务群运营场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7330662971/p1107518.png)
- **核心优势**

  - **客户资产企业化沉淀**：服务群归属企业应用而非个人账号，人员变动时群组自动移交继任者。
  - **群信息标准化配置**：通过API统一设置群名称、公告、欢迎语、成员配额，确保服务一致性。
  - **角色权限清晰定义**：群主、管理员、成员三级角色结构化存储，责任边界明确可追溯。

### **场景二：项目交付协同群全周期管理**

#### **痛点分析**

某IT服务企业在项目交付阶段需频繁创建临时协同群，面临以下挑战：

- 项目启动时手动建群、拉人、设公告，重复操作耗时长且易遗漏关键成员。
- 项目结束后群组未及时解散或归档，遗留群组占用管理精力。
- 多个并行项目的群组混杂，无法按项目阶段或负责人快速检索定位。
- 群内沟通记录未与项目台账关联，复盘时难以回溯决策过程。

#### **价值验证**

- **自动化流程**

  ![项目交付协同群管理场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7330662971/p1107519.png)
- **核心优势**

  - **群组创建自动化**：项目立项时自动触发建群API，预设成员列表与公告内容，减少人工干预。
  - **条件检索精准定位**：支持按项目名称、负责人、创建时间等维度组合查询，秒级定位目标群组。
  - **分页游标完整拉取**：支持通过nextToken逐页获取全部历史群组，确保项目档案无遗漏。

## **实施指南**

### **技术架构**

- **接口调用层**：调用CRM服务端API实现客户群组与客户群的创建、更新、查询、删除等操作。
- **应用认证层**：通过`Client ID`和`Client Secret`获取accessToken，鉴权调用者身份。
- **群组管理层**：调用客户群组相关API创建、更新、查询群组，获取`openGroupSetId`等关键标识符。
- **客户群管理层**：调用客户群相关API创建、批量查询、列表检索客户群，获取`openConversationId`等关键标识符。
- **错误处理层**：完善的`TeaException`异常处理机制，便于快速定位和解决问题。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Crm.CustomerGroup.Write` （客户群会话写权限）
  - `Crm.CustomerGroup.Read` （客户群会话读权限）
- **开发环境**：已安装Java开发环境（JDK1.8及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见**服务端SDK下载**，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 `Client ID` 和 `Client Secret`。

步骤二：申请接口权限，申请客户群组与客户群相关接口的权限。

步骤三：调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口，通过accessToken鉴权调用者身份。

步骤四：调用核心API：

1. 调用服务端API-[创建客户群组](1383-crm-create-group.md)接口，进行创建客户群组，获取客户群组`openGroupSetId`。
2. 根据客户群组`openGroupSetId`，调用服务端API-[更新客户群组](1385-crm-update-group.md)接口，进行更新客户群组。
3. 根据客户群组`openGroupSetId`，调用服务端API-[获取单个客户群组详情](1384-queries-the-details-of-a-single-customer-group.md)接口，进行查询单个客户群组详情。
4. 调用服务端API-[查询客户群组列表](1386-query-groups.md)接口，进行查询客户群组列表。
5. 调用服务端API-[创建客户群](1379-create-a-customer-group.md)接口，进行创建客户群。
6. 根据客户群`openConversationId`，调用服务端API-[获取单个客户群详情](1381-obtain-a-single-customer-group.md)接口，进行获取单个客户群详情。
7. 根据客户群`openConversationId`，调用服务端API-[批量查询客户群](1382-query-customer-groups-in-batches.md)接口，进行批量批量查询客户群详情。
8. 调用服务端API-[查询客户群列表](1380-query-the-list-of-customer-groups.md)接口，进行查询客户群列表。

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

   - `Crm.CustomerGroup.Write` （客户群会话写权限）— 用于创建、更新客户群组与客户群。
   - `Crm.CustomerGroup.Read` （客户群会话读权限）— 用于查询客户群组与客户群详情及列表。

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

### **步骤四：调用核心API**

1. **创建客户群组**：调用服务端API-[创建客户群组](1383-crm-create-group.md)接口，进行创建客户群组，获取客户群组`openGroupSetId`。

   ```
   public void createCustomerGroupSet() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     CreateGroupSetHeaders createGroupSetHeaders = new CreateGroupSetHeaders();
     createGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
     CreateGroupSetRequest createGroupSetRequest = new CreateGroupSetRequest()
       .setName("群组名")
       .setOwnerUserId("301227837930")
       .setCreatorUserId("301227837930")
       .setMemberQuota(100)
       .setManagerUserIds("301227837930,301227837935")
       .setNotice("公告")
       .setNoticeToped(1)
       .setRelationType("crm_customer_personal")
       .setWelcome("欢迎加入");
     try {
       CreateGroupSetResponse groupSetWithOptions = client.createGroupSetWithOptions(createGroupSetRequest, createGroupSetHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(groupSetWithOptions.getBody()));
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

   **参数说明**

   - `name`：群组名称。
   - `ownerUserId`：群主用户userId。
   - `creatorUserId`：创建人用户userId。
   - `memberQuota`：成员配额，即群组最大成员数。
   - `managerUserIds`：管理员用户userId列表，多个用英文逗号隔开。
   - `notice`：群公告内容。
   - `noticeToped`：公告是否置顶，1表示置顶，0表示不置顶。
   - `relationType`：关联对象类型，如crm\_customer\_personal。
   - `welcome`：入群欢迎语。

   **返回字段**

   - `openGroupSetId`：客户群组ID，唯一标识一个客户群组。
2. **更新客户群组**：根据客户群组`openGroupSetId`[更新客户群组](1385-crm-update-group.md)，信息，支持修改群名称、成员配额、管理员、公告等属性。

   ```
   public void updateCustomerGroupSet() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     UpdateGroupSetHeaders updateGroupSetHeaders = new UpdateGroupSetHeaders();
     updateGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
     UpdateGroupSetRequest updateGroupSetRequest = new UpdateGroupSetRequest()
       .setOpenGroupSetId("dfgfghfghdsfdsf")
       .setName("营销群")
       .setMemberQuota(200)
       .setOwnerUserId("301227837938")
       .setManagerUserIds("301227837938")
       .setNotice("公告")
       .setNoticeToped(1)
       .setWelcome("欢迎入群");
     try {
       UpdateGroupSetResponse updateGroupSetResponse = client.updateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(updateGroupSetResponse.getBody()));
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

   **参数说明**

   - `openGroupSetId`：客户群组ID。
   - `name`：群组名称。
   - `memberQuota`：成员配额，即群组最大成员数。
   - `ownerUserId`：群主用户userId。
   - `managerUserIds`：管理员用户userId列表，多个用英文逗号隔开。
   - `notice`：群公告内容。
   - `noticeToped`：公告是否置顶，1表示置顶，0表示不置顶。
   - `welcome`：入群欢迎语。

   **返回字段**

   - `openGroupSetId`：客户群组ID。
3. **获取单个客户群组详情**：根据客户群组`openGroupSetId`，调用服务端API-[获取单个客户群组详情](1384-queries-the-details-of-a-single-customer-group.md)接口，查询单个客户群组详情。

   ```
   public void getCustomerGroupSet() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     GetGroupSetHeaders getGroupSetHeaders = new GetGroupSetHeaders();
     getGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
     GetGroupSetRequest getGroupSetRequest = new GetGroupSetRequest()
       .setOpenGroupSetId("OkldZxxxx");
     try {
       GetGroupSetResponse groupSetWithOptions = client.getGroupSetWithOptions(getGroupSetRequest, getGroupSetHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(groupSetWithOptions.getBody()));
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

   **参数说明**

   - `openGroupSetId`：客户群组ID。

   **返回字段**

   - `name`：群组名称。
   - `ownerUserId`：群主用户userId。
   - `memberQuota`：成员配额。
   - `managerUserIds`：管理员用户userId列表。
   - `notice`：群公告内容。
   - `noticeToped`：公告是否置顶。
   - `relationType`：关联对象类型。
   - `welcome`：入群欢迎语。
4. **查询客户群组列表**：调用服务端API-[查询客户群组列表](1386-query-groups.md)接口，进行查询客户群组列表。

   ```
   public void queryCustomerGroupSets() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     ListGroupSetHeaders listGroupSetHeaders = new ListGroupSetHeaders();
     listGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
     ListGroupSetRequest listGroupSetRequest = new ListGroupSetRequest()
       .setNextToken("fasafsafsd")
       .setMaxResults(10)
       .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}")
       .setRelationType("crm_customer_personal");
     try {
       ListGroupSetResponse listGroupSetResponse = client.listGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(listGroupSetResponse.getBody()));
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

   **参数说明**

   - `nextToken`：分页游标，首次查询传空字符串，后续使用返回的nextToken值。
   - `maxResults`：单次返回最大记录数。
   - `queryDsl`：查询条件，JSON格式字符串。
   - `relationType`：关联对象类型，如`crm_customer_personal`。

   **返回字段**

   - `list`：客户群组列表。
5. **创建客户群**：调用服务端API-[创建客户群](1379-create-a-customer-group.md)接口，进行创建客户群。

   ```
   public void createCustomerGroup() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     CreateGroupHeaders createGroupHeaders = new CreateGroupHeaders();
     createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
     CreateGroupRequest createGroupRequest = new CreateGroupRequest()
       .setGroupName("abc")
       .setOwnerUserId("abc123")
       .setMemberUserIds("a,b,c")
       .setRelationType("abc");
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

   **参数说明**

   - `groupName`：客户群名称。
   - `ownerUserId`：群主用户userId。
   - `memberUserIds`：成员用户userId列表，多个用英文逗号隔开。
   - `relationType`：关联对象类型。

   **返回字段**

   - `openConversationId`：客户群会话ID，唯一标识一个客户群。
6. **获取单个客户群详情**：根据客户群openConversationId，调用服务端API-[获取单个客户群详情](1381-obtain-a-single-customer-group.md)接口，进行获取单个客户群详情。

   ```
   public void getCustomerGroup() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     GetCrmGroupChatSingleHeaders getCrmGroupChatSingleHeaders = new GetCrmGroupChatSingleHeaders();
     getCrmGroupChatSingleHeaders.xAcsDingtalkAccessToken = "<your access token>";
     GetCrmGroupChatSingleRequest getCrmGroupChatSingleRequest = new GetCrmGroupChatSingleRequest()
       .setOpenConversationId("afasd1321");
     try {
       GetCrmGroupChatSingleResponse crmGroupChatSingleWithOptions = client.getCrmGroupChatSingleWithOptions(getCrmGroupChatSingleRequest, getCrmGroupChatSingleHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(crmGroupChatSingleWithOptions.getBody()));
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

   **参数说明**

   - `openConversationId`：客户群会话ID。

   **返回字段**

   - `name`：客户群名称。
   - `ownerUserId`：群主用户userId。
   - `memberUserIds`：成员用户userId列表。
   - `relationType`：关联对象类型。
7. **批量查询客户群**：根据客户群`openConversationId`，调用服务端API-[批量查询客户群](1382-query-customer-groups-in-batches.md)接口，进行批量批量查询客户群详情。

   ```
   public void batchGetCustomerGroups() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     GetCrmGroupChatMultiHeaders getCrmGroupChatMultiHeaders = new GetCrmGroupChatMultiHeaders();
     getCrmGroupChatMultiHeaders.xAcsDingtalkAccessToken = "<your access token>";
     GetCrmGroupChatMultiRequest getCrmGroupChatMultiRequest = new GetCrmGroupChatMultiRequest()
       .setOpenConversationIds(java.util.Arrays.asList(
         "cidQJKDN****=="
       ));
     try {
       GetCrmGroupChatMultiResponse crmGroupChatMultiWithOptions = client.getCrmGroupChatMultiWithOptions(getCrmGroupChatMultiRequest, getCrmGroupChatMultiHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(crmGroupChatMultiWithOptions.getBody()));
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

   **参数说明**

   - `openConversationIds`：客户群会话ID列表。

   **返回字段**

   - `list`：客户群详情列表。
8. **查询客户群列表**：调用服务端API-[查询客户群列表](1380-query-the-list-of-customer-groups.md)接口，进行查询客户群列表。

   ```
   public void queryCustomerGroups() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     QueryCrmGroupChatsHeaders queryCrmGroupChatsHeaders = new QueryCrmGroupChatsHeaders();
     queryCrmGroupChatsHeaders.xAcsDingtalkAccessToken = "<your access token>";
     QueryCrmGroupChatsRequest queryCrmGroupChatsRequest = new QueryCrmGroupChatsRequest()
       .setRelationType("crm_customer_personal")
       .setNextToken("fasdfs1")
       .setMaxResults(10)
       .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}");
     try {
       QueryCrmGroupChatsResponse queryCrmGroupChatsResponse = client.queryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(queryCrmGroupChatsResponse.getBody()));
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

   **参数说明**

   - `relationType`：关联对象类型，如crm\_customer\_personal。
   - `nextToken`：分页游标，首次查询传空字符串，后续使用返回的nextToken值。
   - `maxResults`：单次返回最大记录数。
   - `queryDsl`：查询条件，JSON格式字符串，支持多条件组合与排序。

   **返回字段**

   - `list`：客户群列表。

**实施完成检查清单**

- ✅ 企业内部应用已创建并获取 `Client ID` 和 `Client Secret`。
- ✅ 接口权限`Crm.CustomerGroup.Write`和`Crm.CustomerGroup.Read`已申请并通过审批
- ✅ accessToken获取接口调用正常且缓存机制已实现。
- ✅ 创建客户群组接口调用成功并返回`openGroupSetId`。
- ✅ 更新客户群组接口调用成功。
- ✅ 获取单个客户群组详情接口返回正确的群组信息。
- ✅ 查询客户群组列表接口支持分页游标连续拉取。
- ✅ 创建客户群接口调用成功并返回`openConversationId`。
- ✅ 获取单个客户群详情接口返回正确的群信息。
- ✅ 批量查询客户群接口调用成功并返回多条群详情。
- ✅ 查询客户群列表接口支持条件筛选与分页。
- ✅ `TeaException`异常处理逻辑已实现，可正确解析`err.code`和`err.message`。

## **常见问题（FAQ）**

- **Q1：客户群组与客户群有什么区别？**

  客户群组（GroupSet）是CRM层面的逻辑分组概念，用于聚合管理多个客户群，具有独立的`openGroupSetId`；客户群（Group）是实际的钉钉会话，具有`openConversationId`，可直接发送消息。一个客户群组可关联多个客户群。
- **Q2：relationType参数有哪些可选值？**

  `relationType`用于指定群组关联的CRM对象类型，常见值包括`crm_customer_personal`（个人客户）、`crm_customer_enterprise`（企业客户）等，具体可选值需参考钉钉开发者后台CRM配置页面。
- **Q3：分页查询如何判断是否还有下一页？**

  查询列表接口返回结果中包含`hasMore`字段，true表示有下一页，false表示已是最后一页。同时`nextToken`字段提供下一页的游标值，将其作为下一次请求的`nextToken`参数即可继续拉取数据。当`hasMore`为false时停止分页。
- **Q4：创建客户群时memberUserIds参数的格式是什么？**

  `memberUserIds`为英文逗号分隔的用户userId字符串，如"a,b,c"。注意不是数组格式，而是拼接后的字符串。
- **Q5：为什么查询客户群列表时返回结果为空？**

  请检查以下几点：① `relationType`是否与目标客户群关联类型一致；② `queryDsl`中的`fieldId`是否为有效字段（如`name`、`gmtCreate`）；③ 操作人是否具有对应客户群的查看权限；④ `nextToken`是否正确传递，首次查询应传空字符串。
