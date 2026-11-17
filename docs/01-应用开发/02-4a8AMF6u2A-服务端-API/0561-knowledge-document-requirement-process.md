---
title: "项目文档管理：知识库文档沉淀与需求流程线上化"
source_url: "https://open.dingtalk.com/document/development/knowledge-document-requirement-process"
namespace: "development"
slug: "knowledge-document-requirement-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 集成方案 > 项目文档管理：知识库文档沉淀与需求流程线上化"
doc_id: "wLUR56Gz0w"
updated_at: "2026-11-11 09:20:20"
---

> Source: https://open.dingtalk.com/document/development/knowledge-document-requirement-process
> Path: 应用开发 / 服务端 API / 文档/文件 > 集成方案 > 项目文档管理：知识库文档沉淀与需求流程线上化
> Updated: 2026-11-11 09:20:20

# 项目文档管理：知识库文档沉淀与需求流程线上化

## 概述

本方案基于钉钉开放平台的知识库和文档API，为企业提供了一套完整的项目文档管理解决方案。通过新建知识库、创建文档、添加权限等核心接口，企业可将项目过程中产生的文档统一归档至知识库中，实现文档的集中存储、多级目录管理和精细化权限管控。同时，结合在线文档的评论、待办等协作能力，贯通项目需求的创建、评审、分配、验收全流程，使项目信息实时同步、协作效率显著提升。

### **方案背景**

在大型项目推进过程中会产生大量文档数据，项目管理员统一归档整理项目成员产出的文档数据具有较大时间成本，且项目信息同步不及时、需求流程无法整体把控，会导致项目进度推迟，直接影响企业的生产活动。

企业在日常运营中常面临以下痛点：

- **项目文档不集中**：项目过程中产生的文档分散在各处，不便统一管理；文档存储在本地，成员需要充当项目信息的搬运工，导致效率低下。
- **需求信息不同步**：项目需求的创建、评审、分配、验收流程无法贯通，导致信息不同步，影响需求的推进速度。
- **文档权限难管理**：针对不同项目成员无法准确给予查看/编辑权限，可能导致文档误修改或误删除。

### **核心价值**

针对项目管理的场景，可使用钉钉文档接口实现一套完整的项目内容沉淀、需求流程管控和权限管理方案。

- **知识库沉淀文档**：知识库提供多级目录存储方式，通过项目和知识库的绑定，统一归档项目过程中产生的文档，项目信息可快速流转，项目组成员能够高效获取项目资料。
- **在线文档贯通需求流程**：需求可直接关联钉钉文档，文档的评论功能支持线上需求评审，文档的待办可管理需求协作人员、监控项目进度，项目验收过程可直接同步信息到文档，通过@人功能提醒关注人，实现一片文档贯穿需求全流程。
- **完善的权限模型**：知识库及文档有可编辑/可查看下载/仅可查看等权限点，可控制用户的编辑、下载、查看等操作，具有灵活的继承和独立权限模型，文档可继承上级权限也可单独设置权限。

### **适用场景**

本方案适用于以下典型业务场景：

- **工程项目文档统一归档**：适用于多部门协作的大型项目，需要将项目文档按目录结构统一归档，并为不同角色成员分配差异化文档权限。
- **项目需求全流程线上追踪**：适用于研发团队，需要将需求从创建到验收的全流程与文档关联，实现需求状态实时同步和进度监控。
- **跨部门协作项目资料集中沉淀**：适用于跨部门协同项目，需要将各部门产出的项目资料集中存储于知识库，便于全员检索和复用。

## **典型业务场景**

### **场景一：****工程项目文档统一归档**

#### **痛点分析**

Teambition钉钉项目是一款集项目、任务管理于一体的数字化协作平台。在大型工程项目中，项目管理员需要将项目成员产出的各类文档统一归档，并为不同角色分配差异化权限，但当前面临以下问题：

- 项目文档散落在各成员的本地设备和聊天记录中，项目管理员需要逐一收集整理，耗时耗力。
- 项目空间和文档存储割裂，成员无法在项目内直接查找关联文档，信息获取效率低。
- 文档权限管理粗放，难以针对不同项目成员角色（如项目经理、开发人员、测试人员）精确分配查看/编辑权限。
- 项目复盘时缺乏完整的文档归档记录，难以追溯历史版本的文档变更。

#### **价值验证**

- **自动化流程**

  ![项目文档管理_场景一_自动化流程_20261110_145606](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0200634971/p1111336.png)
- **关键优势**

  - **项目文档集中归档**：通过新建知识库绑定项目，将项目过程中产生的文档按目录结构统一存储，项目管理员无需手动收集，成员可一键访问项目全部文档。
  - **任务与文档关联追踪**：任务可直接关联文档，成员在处理任务时能快速定位相关文档，文档更新后可追溯变更记录，支持项目复盘。
  - **精细化权限管控**：知识库和文档支持可编辑/可查看下载/仅可查看等多级权限，可针对不同项目成员角色精确分配，防止文档误修改或误删除。

### **场景二：****项目需求全流程线上追踪**

#### **痛点分析**

云效是一站式BizDevOps平台，通过集成钉钉文档完成项目内容归档和任务流程管控。在研发项目中，需求从创建到验收涉及多个环节和角色，当前面临以下问题：

- 需求文档与任务系统割裂，需求变更后文档未同步更新，导致开发人员基于过时需求进行开发。
- 需求评审过程依赖线下会议或聊天记录，评审意见分散，难以形成结构化记录。
- 需求验收结果无法直接反馈到需求文档，缺乏闭环追踪机制。
- 需求协作人员变动时，新成员难以快速了解需求背景和历史讨论。

#### **价值验证**

- **自动化流程**

  ![项目文档管理_场景二_自动化流程_20261110_152114](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0200634971/p1111360.png)
- **关键优势**

  - **需求文档与任务联动**：在工作台引入钉钉文档Tab，任务可直接关联文档，需求变更后文档同步更新，开发人员始终基于最新需求工作。
  - **在线评论驱动需求评审**：文档的评论功能支持线上需求评审，评审意见集中记录在文档中，可追溯、可搜索，替代线下会议和碎片化聊天。
  - **待办组件跟踪需求进度**：文档的待办功能可管理需求协作人员，分配任务并跟踪完成状态，需求验收结果直接同步到文档，形成闭环。

## **实施指南**

### **技术架构**

- **接口调用层**：调用钉钉知识库和存储服务端API实现知识库创建、知识库列表查询、文档创建、文档权限管理等操作。
- **应用认证层**：通过 Client ID 和 Client Secret 获取accessToken，鉴权调用者身份。
- **用户管理层**：调用通讯录相关API获取部门用户信息，获取用户的unionId。
- **文档管理层**：调用知识库相关API创建知识库和文档，为文档添加成员权限。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_base`（调用企业API时需要具备的基本权限）——通过免登码code获取用户信息。
  - `Wiki.Node.Read`（知识库节点读权限）——应用于获取节点列表。
  - `Storage.File.Write`（企业存储文件写权限）——用于添加权限。
  - `Wiki.Workspace.Write`（知识库写权限）——用于新建知识库。
  - `Wiki.Workspace.Read`（知识库读权限）——用于获取知识库列表。
  - `Storage.Permission.Write`（企业存储授权信息写权限）——用于覆写文档（应用授权）。
  - `qyapi_get_department_member`（通讯录部门成员读权限）——用于获取部门用户基础信息。
  - `Document.WorkspaceDocument.Write`（知识库文档写权限）——用于创建知识库文档。
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：完成[添加网页应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)流程，并接入[企业内部网页应用免登](0017-enterprise-internal-application-logon-free.md)。

步骤二：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤三：申请接口权限，申请会议相关接口的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤五：调用服务端文档相关API。

1. 接入免登后，通过accessToken和免登码调用[通过免登码获取用户信息](0023-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取当前登录用户的`userid`、`unionid`和`name`。
2. 通过accessToken，调用[获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md)接口，获取指定部门的用户基础信息。
3. 通过accessToken和操作人`unionid`，调用[新建知识库](0622-new-knowledge-base.md)接口，创建一个新的知识库空间，并`workspaceId`知识库id。
4. 通过accessToken和操作人`unionid`，调用[获取知识库列表](0625-get-knowledge-base-list.md)接口，查询用户有权限的知识库列表。
5. 通过`workspaceId`和操作人`unionid`，在知识库内创建文档或者文件夹，并获取`dentryUuid`（文件Uuid）、`docKey`（文档id）。

   1. 若在根目录创建文档，则调用[创建知识库文档](0632-create-team-space-document.md)接口创建文档。
   2. 若在某节点下创建文档，则先调用[获取节点列表](0636-get-node-list.md)接口获取`DentryModel`参数值，然后调用[创建知识库文档](0632-create-team-space-document.md)接口创建文档。
6. 通过操作人`unionid`和`dentryUuid`，调用[添加权限](0677-add-permissions-file.md)接口，实现权限成员权限的添加。
7. 通过操作人`unionid`和文档id`docKey`，调用[覆写文档（应用授权）](0563-api-doc-updatecontent.md)接口，通过Markdown的格式覆写整篇文档内容。

## 实施步骤

### **步骤一：接入免登**

1. 创建应用，并完成[添加网页应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)流程。
2. 接入[企业内部网页应用免登](0017-enterprise-internal-application-logon-free.md)。

   ```
   import * as dd from 'dingtalk-jsapi';

   dd.requestAuthCode({
     corpId: 'corpid',
     clientId: 'clientid',
     onSuccess: function (result) {
       /*{
           code: 'hYLK98jkf0m' //string authCode
       }*/
     },
     onFail: function (err) {},
   });
   ```

### **步骤二：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤三：添加接口权限**

1. 在应用详情页，单击**权限管理**。
2. 在权限搜索框中输入以下权限标识并申请：

   - `qyapi_base`（调用企业API时需要具备的基本权限）
   - `Wiki.Node.Read`（知识库节点读权限）
   - `Storage.File.Write`（企业存储文件写权限）
   - `Wiki.Workspace.Write`（知识库写权限）
   - `Wiki.Workspace.Read`（知识库读权限）
   - `Storage.Permission.Write`（企业存储授权信息写权限）
   - `qyapi_get_department_member`（通讯录部门成员读权限）
   - `Document.WorkspaceDocument.Write`（知识库文档写权限）

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤四：获取访问凭证（accessToken）

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

### **步骤五：核心API调用**

1. 获取登录用户信息：通过accessToken和免登码调用[通过免登码获取用户信息](0023-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取当前登录用户的`userid`、`unionid`和`name`。

   ```
   public void getOapiV2UserGetuserinfo() throws Exception{
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/getuserinfo");
     OapiV2UserGetuserinfoRequest req = new OapiV2UserGetuserinfoRequest();
     req.setCode("bab02f63c1e030fbbxxxx");
     OapiV2UserGetuserinfoResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**：

   - `access_token`：调用接口凭证。
   - `code`：免登授权码。

   **返回字段**：

   - `userid`：用户userid。
   - `unionid`：用户unionid。
   - `name`：用户姓名。
2. **获取部门用户信息**：通过accessToken，调用[获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md)接口，获取指定部门的用户基础信息。

   ```
   public void getOapiUserListsimple() throws Exception{
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listsimple");
     OapiUserListsimpleRequest req = new OapiUserListsimpleRequest();
     req.setDeptId(10L);
     req.setCursor(0L);
     req.setSize(10L);
     req.setOrderField("modify_desc");
     req.setContainAccessLimit(false);
     req.setLanguage("zh_CN");
     OapiUserListsimpleResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**：

   - `access_token`：调用接口凭证。
   - `dept_id`：部门ID。
   - `cursor`：分页游标，首次传0。
   - `size`：分页大小，最大100。

   **返回字段**：

   - `list`：用户列表，每项包含`userid`和`name`。
3. **新建知识库**：通过accessToken和操作人`unionid`，调用[新建知识库](0622-new-knowledge-base.md)接口，创建一个新的知识库空间，并`workspaceId`知识库id。

   ```
   public void createWorkspace() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkwiki_2_0.Client client = new com.aliyun.dingtalkwiki_2_0.Client(config);
     AddWorkspaceHeaders addWorkspaceHeaders = new AddWorkspaceHeaders();
     addWorkspaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
     AddWorkspaceRequest.AddWorkspaceRequestOption option = new AddWorkspaceRequest.AddWorkspaceRequestOption()
       .setDescription("workspace_description")
       .setTeamId("lHiicjNxxxx8ZwiEiE");
     AddWorkspaceRequest addWorkspaceRequest = new AddWorkspaceRequest()
       .setOperatorId("tXguN3xxxxLURAiEiE")
       .setName("workspace_name")
       .setOption(option);
     try {
       AddWorkspaceResponse addWorkspaceResponse = client.addWorkspaceWithOptions(addWorkspaceRequest, addWorkspaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(JSON.toJSONString(addWorkspaceResponse.getBody()));
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

   - `operatorId`：操作人unionId。
   - `name`：知识库名称。
   - `option.description`：知识库描述。
   - `option.teamId`：知识小组id。

   **返回字段**：

   - `workspaceId`：知识库ID。
   - `rootNodeId`：根节点ID。
   - `name`：知识库名称。
   - `url`：知识库访问URL。
4. **获取知识库列表**：通过accessToken和操作人`unionid`，调用[获取知识库列表](0625-get-knowledge-base-list.md)接口，查询用户有权限的知识库列表。

   ```
   public void getListWorkSpaces() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkwiki_2_0.Client client = new com.aliyun.dingtalkwiki_2_0.Client(config);
     ListWorkspacesHeaders listWorkspacesHeaders = new ListWorkspacesHeaders();
     listWorkspacesHeaders.xAcsDingtalkAccessToken = "<your access token>";
     ListWorkspacesRequest listWorkspacesRequest = new ListWorkspacesRequest()
       .setOperatorId("tXguN3xxxxiEiE");
     try {
       ListWorkspacesResponse listWorkspacesResponse = client.listWorkspacesWithOptions(listWorkspacesRequest, listWorkspacesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(JSON.toJSONString(listWorkspacesResponse.getBody()));
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

   - `operatorId`：操作人unionId。

   **返回字段**：

   - `workspaces`：知识库列表，每项包含`workspaceId`、`name`、`url`。
5. 若在根目录创建文档，调用[创建知识库文档](0632-create-team-space-document.md)接口创建文档，并获取`dentryUuid`（文件Uuid）、`docKey`（文档id）。

   ```
   public void createWorkspaceDoc() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkdoc_1_0.Client client = new com.aliyun.dingtalkdoc_1_0.Client(config);
     CreateWorkspaceDocHeaders createWorkspaceDocHeaders = new CreateWorkspaceDocHeaders();
     createWorkspaceDocHeaders.xAcsDingtalkAccessToken = "<your access token>";
     CreateWorkspaceDocRequest createWorkspaceDocRequest = new CreateWorkspaceDocRequest()
       .setName("文档")
       .setDocType("DOC")
       .setOperatorId("Q2xwPOxxx");
     try {
       CreateWorkspaceDocResponse createWorkspaceDocResponse = client.createWorkspaceDocWithOptions("YRBGvyxxx",createWorkspaceDocRequest, createWorkspaceDocHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(JSON.toJSONString(createWorkspaceDocResponse.getBody()));
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

   - `workspaceId`：知识库ID（路径参数）。
   - `name`：文档名称。
   - `docType`：文档类型，DOC（文字）、WORKBOOK（表格）、MIND（脑图）、FOLDER（文件夹）。
   - `operatorId`：用户的unionId。

   **返回字段**：

   - `workspaceId`：知识库ID。
   - `nodeId`：知识库文档ID。
   - `dentryUuid`：文件Uuid，用于后续权限操作。
   - `docKey`：文档docKey。
   - `url`：文档URL。
6. 若在某节点下创建文档，先调用[获取节点列表](0636-get-node-list.md)接口获取`DentryModel`参数值，然后调用[创建知识库文档](0632-create-team-space-document.md)接口创建文档。

   - **获取节点列表**：

     ```
     public void listNodes() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkwiki_2_0.Client client = new com.aliyun.dingtalkwiki_2_0.Client(config);
       ListNodesHeaders listNodesHeaders = new ListNodesHeaders();
       listNodesHeaders.xAcsDingtalkAccessToken = "<your access token>";
       ListNodesRequest listNodesRequest = new ListNodesRequest()
         .setParentNodeId("MNDoxxxxmrZQ3")
         .setOperatorId("tXguNxxxxURAiEiE");
       try {
         ListNodesResponse listNodesResponse = client.listNodesWithOptions(listNodesRequest, listNodesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
         System.out.println(JSON.toJSONString(listNodesResponse.getBody()));
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

     - `parentNodeId`：父节点id。
     - `operatorId`：用户的unionId。

     **返回字段**：

     - `workspaceId`：知识库ID。
     - `nodeId`：知识库文档ID。
     - `name`：名称。
     - `category`：类别，枚举值。
     - `permissionRole`：当前用户对知识库节点的权限角色，枚举值。
   - **创建知识库文档**

     ```
     public void createWorkspaceDoc() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkdoc_1_0.Client client = new com.aliyun.dingtalkdoc_1_0.Client(config);
       CreateWorkspaceDocHeaders createWorkspaceDocHeaders = new CreateWorkspaceDocHeaders();
       createWorkspaceDocHeaders.xAcsDingtalkAccessToken = "<your access token>";
       CreateWorkspaceDocRequest createWorkspaceDocRequest = new CreateWorkspaceDocRequest()
         .setName("文档")
         .setDocType("DOC")
         .setOperatorId("Q2xwPOxxx")
         .setParentNodeId("YRBGv0Ye")
         .setTemplateId("123243")
         .setTemplateType("team_template");
       try {
         CreateWorkspaceDocResponse createWorkspaceDocResponse = client.createWorkspaceDocWithOptions("YRBGvyxxx",createWorkspaceDocRequest, createWorkspaceDocHeaders, new com.aliyun.teautil.models.RuntimeOptions());
         System.out.println(JSON.toJSONString(createWorkspaceDocResponse.getBody()));
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

     - `workspaceId`：知识库ID（路径参数）。
     - `name`：文档名称。
     - `docType`：文档类型，DOC（文字）、WORKBOOK（表格）、MIND（脑图）、FOLDER（文件夹）。
     - `operatorId`：用户的unionId。
     - `parentNodeId`：父节点Id。
     - `templateId`：文档模板id。
     - `templateType`：文档模板类型。

     **返回字段**：

     - `workspaceId`：知识库ID。
     - `nodeId`：知识库文档ID。
     - `dentryUuid`：文件Uuid，用于后续权限操作。
     - `docKey`：文档docKey。
     - `url`：文档URL。
7. 通过操作人`unionid`和`dentryUuid`，调用[添加权限](0677-add-permissions-file.md)接口，实现权限成员权限的添加。

   ```
   public void addPermission() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkstorage_2_0.Client client = new com.aliyun.dingtalkstorage_2_0.Client(config);
     AddPermissionHeaders addPermissionHeaders = new AddPermissionHeaders();
     addPermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
     AddPermissionRequest.AddPermissionRequestMembers members0 = new AddPermissionRequest.AddPermissionRequestMembers()
       .setType("USER")
       .setId("01472825524039877041");
     AddPermissionRequest addPermissionRequest = new AddPermissionRequest()
       .setUnionId("tXguNxxxxAiEiE")
       .setRoleId("MANAGER")
       .setMembers(java.util.Arrays.asList(
         members0
       ));
     try {
       AddPermissionResponse addPermissionResponse = client.addPermissionWithOptions("EpGBxxxx7R35y",addPermissionRequest, addPermissionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(JSON.toJSONString(addPermissionResponse.getBody()));
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

   - `dentryUuid`：文件uuid（路径参数），通过创建知识库文档接口返回的`dentryUuid`获取。
   - `unionId`：操作人unionId。
   - `roleId`：角色ID，OWNER（拥有者）、MANAGER（管理者）、EDITOR（编辑者）、DOWNLOADER（查看下载者）、READER（仅可查看者）。
   - `members`：权限成员列表，每项包含：

     - `type`：权限成员类型，ORG（企业）、DEPT（部门）、USER（用户）等。
     - `id`：权限成员ID，USER类型时为员工userId。

   **返回字段**：

   - `success`：本次操作是否成功。
8. 通过操作人`unionid`和文档id`docKey`，调用[覆写文档（应用授权）](0563-api-doc-updatecontent.md)接口，通过Markdown的格式覆写整篇文档内容。

   ```
   public void docUpdateContent() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkdoc_1_0.Client client = new com.aliyun.dingtalkdoc_1_0.Client(config);
     DocUpdateContentHeaders docUpdateContentHeaders = new DocUpdateContentHeaders();
     docUpdateContentHeaders.xAcsDingtalkAccessToken = "<your access token>";
     DocUpdateContentRequest docUpdateContentRequest = new DocUpdateContentRequest()
       .setOperatorId("someOperatorId")
       .setDataType("markdown")
       .setContent("# heading");
     try {
       DocUpdateContentResponse docUpdateContentResponse = client.docUpdateContentWithOptions("someDocKey",docUpdateContentRequest, docUpdateContentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(JSON.toJSONString(docUpdateContentResponse.getBody()));
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

   - `docKey`：文档ID（路径参数），通过创建知识库文档接口返回的`docKey`获取。
   - `operatorId`：操作人unionId。
   - `dataType`：覆写内容的数据格式。
   - `content`：需要写入的内容字符串。

   **返回字段**：

   - `success`：本次操作是否成功。
   - `result`：请求结果。

**实施完成检查清单**：

- ✅ 应用已创建并获取 Client ID 和 Client Secret 凭证。
- ✅ 已添加`qyapi_base`、`qyapi_get_department_member`、`Wiki.Workspace.Write`、`Wiki.Workspace.Read`、`Document.WorkspaceDocument.Write`、`Wiki.Node.Read`、`Storage.Permission.Write`、`Storage.File.Write`共8个接口权限。
- ✅ 已通过Client ID 和 Client Secret 成功获取accessToken。
- ✅ 已通过免登码获取用户身份信息（`userid`、`unionid`和`name`）。
- ✅ 已调用获取部门用户基础信息接口，获取项目成员列表。
- ✅ 已调用新建知识库接口，成功创建项目知识库并获取workspaceId。
- ✅ 已调用获取知识库列表接口，查询用户有权限的知识库列表。
- ✅ 已调用创建知识库文档接口，在知识库中创建需求文档并获取nodeId和dentryUuid。
- ✅ 已调用添加文档权限接口，为项目成员分配文档权限。
- ✅ 项目成员可在钉钉端内访问知识库，查看和编辑项目文档。

## **常见问题（FAQ）**

- **Q1：新建知识库和创建知识库文档有什么区别？**

  新建知识库是创建一个顶层知识库空间，返回`workspaceId`；创建知识库文档是在已有知识库内创建具体的文档或文件夹，返回`nodeId`和`dentryUuid`。
- **Q2：如何获取用户的unionId？**

  企业内部应用可通过[查询用户详情](0055-query-user-details.md)接口获取unionid参数值。
- **Q3：添加文档权限时dentryUuid从哪里获取？**

  调用创建知识库文档接口时，返回参数中包含`dentryUuid`字段，将其作为添加权限接口的路径参数传入。
- **Q4：文档的权限角色有哪些？**

  支持五种角色：OWNER（拥有者）、MANAGER（管理者）、EDITOR（编辑者）、DOWNLOADER（查看下载者）、READER（仅可查看者）。
- **Q5：创建文档时支持哪些文档类型？**

  支持DOC（文字）、WORKBOOK（表格）、MIND（脑图）、FOLDER（文件夹）四种类型。
- **Q6：获取知识库列表时如何分页？**

  首次请求不传`nextToken`，响应中若`nextToken`不为空则表示有更多数据，下次请求传入该值继续获取。
