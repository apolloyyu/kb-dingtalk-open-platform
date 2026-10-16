---
title: "OA审批流接入：附件审批的下载与预览"
source_url: "https://open.dingtalk.com/document/development/new-version-of-attachment-approval-process"
namespace: "development"
slug: "new-version-of-attachment-approval-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 标准版 > OA审批流接入：附件审批的下载与预览"
doc_id: "gCYVw2ivlo"
updated_at: "2026-10-16 09:22:54"
---

> Source: https://open.dingtalk.com/document/development/new-version-of-attachment-approval-process
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 标准版 > OA审批流接入：附件审批的下载与预览
> Updated: 2026-10-16 09:22:54

# OA审批流接入：附件审批的下载与预览

## **概述**

在企业日常运营中，审批流程往往需要附带各类文件材料，如合同扫描件、发票原件、设计图纸、资质证明等。传统审批系统要求用户手动上传附件至审批表单，再跨系统传递文件给审批人，导致审批周期长、文件版本混乱、追溯困难。

### 方案背景

企业OA审批流程中常涉及合同、发票、资质证明等附件材料，审批人需在钉钉端内直接预览或下载附件以完成审核判断。通过OA审批流附件接口对接，可实现审批附件在钉钉端的在线预览、安全下载和版本管理，避免审批人频繁跳转原系统查看附件，提升审批效率和体验一致性。

企业在日常运营中常面临以下痛点：

- **附件查看路径长**： 审批详情页仅显示附件名称和大小，点击后需跳转至业务系统才能预览内容，每次审批平均额外耗时2分钟，日均浪费30分钟以上。
- **移动端无法预览**： 多数业务系统的附件预览功能未适配移动端，审批人出差或通勤时无法在手机端查看合同条款、发票明细等关键附件，被迫延迟审批决策。
- **附件下载无管控**： 敏感附件（如薪资单、商业合同）可被任意下载转发，缺乏水印、禁止复制、有效期限制等安全措施，存在数据泄露风险。
- **多版本附件难区分**： 同一审批单上传多个版本的附件时，钉钉端无法识别版本号和时间戳，审批人容易误阅旧版文件导致审批结论错误。

### **核心价值**

- **附件全链路自动化：** 从钉盘空间获取、文件上传、审批实例创建到附件授权下载/预览，全流程API驱动，消除人工干预环节。
- **审批体验一体化：** 审批人在钉钉端内即可查看附件详情、完成操作，无需跳转外部系统或下载本地文件。
- **数据安全可控：** 基于审批钉盘空间的权限隔离机制，附件仅在授权范围内可访问，支持临时授权下载和预览链接，保障敏感文件安全。

### **适用场景**

本方案适用于需要在自有业务系统中发起带附件审批、并在审批过程中对附件进行下载或预览操作的场景，典型包括：

- **合同审批：** 附合同扫描件、履约保函等法律文件。
- **采购审批：** 附报价单、供应商资质证明、历史维修记录等附件。
- **报销审批：** 附发票影像、费用明细表等财务凭证。
- **工程验收：** 附验收报告、现场照片、检测报告等材料。

## 典型业务场景

### **场景一：建设工程合同审批（建筑行业）**

#### **痛点分析**

某大型建筑集团使用自研项目管理系统管理工程合同审批流程，项目经理提交合同审批时需附上合同扫描件、对方营业执照、履约保函等多份附件。原有流程存在以下问题：

- **附件传递低效：** 纸质合同需扫描后通过邮件发送给各级审批人，平均耗时2-3个工作日，紧急合同无法及时推进。
- **版本管理混乱：** 多轮修改后的合同版本分散在不同人员邮箱中，审批人难以确认当前最新版本，易签署错误版本。
- **合规审查困难：** 法务和财务审批人无法在审批界面直接查看附件内容，需打印纸质材料逐一核对，效率低下且易遗漏关键条款。
- **审计追溯缺失：** 手工传递的附件缺乏操作日志，事后审计无法还原审批过程中的文件流转路径和责任人。

#### **价值验证**

- **自动化流程**

  ![建设工程合同审批场景图_20261010_165718](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6849971971/p1105045.png)
- **关键优势**

  - **附件信息一键审批：** 审批人在钉钉端内直接查看合同详情并完成操作，无需跨系统切换。
  - **审批流程实时可视：** 钉钉端内展示完整的合同数据（含附件列表、对方资质、历史签约记录），审批进度一目了然，支持评论和催办。
  - **数据同步全链路：** 审批结果实时回写项目管理系统，驳回时自动通知申请人补充材料，确保两端数据一致且可追溯，合同审批周期缩短60%以上。

### **场景二：高校科研经费报销审批（教育行业）**

#### **痛点分析**

某重点大学使用科研管理系统处理教师科研经费报销审批，课题负责人提交报销申请时需附上发票扫描件、出差审批单、会议邀请函等证明材料。原有流程存在以下问题：

- **票据核验繁琐：** 财务人员需在科研系统和邮件之间反复切换查看发票真伪及金额匹配性，单笔报销审核耗时40分钟以上。
- **材料完整性难把控：** 不同科研项目对附件要求差异大，审批人无法在线快速判断材料是否齐全，退回补件率高达35%。
- **跨校区协作滞后：** 主校区财务处与分校区科研秘书之间依赖线下传递纸质材料，偏远校区报销到账时间比主校区晚5-7天。
- **预算执行监控弱：** 报销审批与课题预算额度脱节，超预算支出只能在事后发现，缺乏事前拦截机制。

#### **价值验证**

- **自动化流程**

  ![高校科研经费报销审批场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6849971971/p1105049.png)
- **关键优势**

  - **票据与预算在线联动：** 审批人在钉钉端内直接查看发票影像、课题剩余额度及历史报销记录，一站式完成合规校验。
  - **材料完整性智能提示：** 系统根据项目类型自动列出所需附件清单，缺失项高亮提醒，减少无效退回次数。
  - **跨校区审批零时差：** 所有附件集中存储于审批钉盘空间，分校区人员无需等待纸质材料流转即可在线审批，报销到账时效提升70%以上。

## 实施指南

### 技术架构

本方案的技术架构包含以下核心组件：

- **身份鉴权层**： 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **钉盘管理层**： 负责审批钉盘空间获取和文件上传，实现附件的安全存储与权限隔离。
- **实例执行层**： 负责审批实例的发起、查询和状态跟踪，驱动审批流程的执行。
- **附件授权层**： 负责审批附件的下载/预览授权，保障敏感文件在授权范围内使用。

### 前置条件

- **应用准备**： 已完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)流程，获取应用 Client ID 和 Client Secret。
- **权限要求**： 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Instance.Write`（审批实例写入权限）
  - `Workflow.Instance.Read`（审批实例读取权限）
- **开发环境**： 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**： 下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### 代码实现

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API和客户端JSAPI：

1. 调用服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取审批钉盘空间`spaceId`。
2. 调用客户端JSAPI-[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息。
3. 获取模板的唯一编码`processCode`。

   - 通过[钉钉管理后台](https://oa.dingtalk.com/index.htm#/microApp/microAppListNew)-OA审批-打开对应审批模板获取。
   - 调用服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，创建审批模板获取`processCode`。
4. 调用服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批，获取审批实例`instanceId`。
5. 根据审批实例`instanceId`，调用服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取审批实例详情中的`fileId`。
6. 审批附件操作：

   1. 下载审批附件

      1. 调用服务端API-[授权下载审批钉盘文件](0503-download-the-approval-nail-file.md)接口，进行审批钉盘文件的授权操作。
      2. 调用服务端API-[下载审批附件](0504-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。目前不支持第三方企业应用调用。
   2. 预览审批附件：

      1. 调用服务端API-[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口，实现钉盘文件的预览操作。
      2. 调用客户端JSAPI-[预览钉盘文件](../03-Ogu5SlPY4t-客户端-JSAPI/0331-jsapi-preview-file-in-ding-talk.md)接口，实现预览钉盘文件。

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

   - `Workflow.Form.Write`（工作流模板写权限）：用于创建和更新审批表单模板
   - `Workflow.Instance.Write`（审批实例写入权限）：用于发起和执行审批实例
   - `Workflow.Instance.Read`（审批实例读取权限）：用于查询审批实例详情

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。

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

1. **获取审批钉盘空间信息**：调用服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取审批钉盘空间`spaceId`。

   ```
   public void ProcessSpaceInfo() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders getAttachmentSpaceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders();
           getAttachmentSpaceHeaders.xAcsDingtalkAccessToken ="accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest getAttachmentSpaceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest()
                   .setUserId("manager7675")
                   .setAgentId(11******75L);
           try {
               GetAttachmentSpaceResponse attachmentSpaceWithOptions = client.getAttachmentSpaceWithOptions(getAttachmentSpaceRequest, getAttachmentSpaceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(attachmentSpaceWithOptions.getBody()));
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

   - `userId`：发起人用户ID。
   - `agentId`：应用AgentId。

   **返回字段：**

   - `spaceId`：审批钉盘空间ID。
2. **上传附件到钉盘**：调用客户端JSAPI-[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息，本流程示例使用[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10318)实现。

   > **[!IMPORTANT]**
   >
   > 调用该方法前，需要调用[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)进行授权操作。
3. **获取审批模板编码** `processCode`：有2种方式可以获取模板的唯一编码`processCode`：

   - **方式一**：通过[钉钉管理后台](https://aflow.dingtalk.com/dingtalk/web/query/dashboard?dinghash=aflowSetting#/aflowSetting)-OA审批-打开对应审批模板获取，可参考[processCode](0475-workflow-overview.md#6fada3928c317)说明。
   - **方式二**：调用服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，创建审批模板获取`processCode`。

     ```
      public void createProcessTemplate() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
             FormCreateHeaders formCreateHeaders = new FormCreateHeaders();
             formCreateHeaders.xAcsDingtalkAccessToken = "accessToken"；

             // 1. 单行输入控件
             FormComponentProps formComponentProps = new FormComponentProps()
                     .setComponentId("DDAttachment-sys1001")
                     .setLabel("附件");
             FormComponent formComponent = new FormComponent()
                     .setComponentType("DDAttachment")
                     .setProps(formComponentProps);

             FormCreateRequest formCreateRequest = new FormCreateRequest()
                     .setName("审批附件表单")
                     .setDescription("测试审批附件组件")
                     //有参数processCode时为更新模板，无参数processCode时，为创建模板，该示例为创建模板
                     //.setProcessCode("PROC-42928B7C-****-****-****-B52B4E1702FC")
                     .setFormComponents(java.util.Arrays.asList(
                             formComponent
                     ));
             try {
                 FormCreateResponse formCreateResponse = client.formCreateWithOptions(formCreateRequest, formCreateHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(formCreateResponse.getBody()));
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

     - `name`：审批表单名称。
     - `formComponents`：表单组件列表，包含附件组件类型和属性。

     **返回字段：**

     - `processCode`：审批模板唯一编码。
4. **发起审批实例**：调用服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批，获取审批实例`instanceId`。

   ```
   public void ProcessInstances() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           StartProcessInstanceHeaders startProcessInstanceHeaders = new StartProcessInstanceHeaders();
           startProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

           //1.附件
           JSONObject json  = new JSONObject();
           json.put("spaceId","479****886");
           json.put("fileName","IMG_2895(1).PNG");
           json.put("fileSize","2****4");
           json.put("fileType","png");
           json.put("fileId","68********11");
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("附件")
                   .setValue(JSON.toJSONString(Arrays.asList(json)));

           //设置审批人
           //会签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers0 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("AND")
                   .setUserIds(java.util.Arrays.asList(
                           "014******877041", "085******4272"
                   ));
           //或签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers1 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("OR")
                   .setUserIds(java.util.Arrays.asList(
                           "014******877041", "085******4272"
                   ));
           StartProcessInstanceRequest startProcessInstanceRequest = new StartProcessInstanceRequest()
                   .setOriginatorUserId("审批发起人userId")
                   .setProcessCode("PROC-42928B7C-****-****-****-B52B4E1702FC")
                   .setDeptId(1L)
                   .setMicroappAgentId(11******5L)
                   .setApprovers(java.util.Arrays.asList(
                           approvers0, approvers1
                   ))
                   .setCcList(java.util.Arrays.asList(
                           "抄送人userId"
                   ))
                   .setCcPosition("FINISH")
                   .setFormComponentValues(java.util.Arrays.asList(
                           formComponentValues
                   ));
           try {
               StartProcessInstanceResponse startProcessInstanceResponse = client.startProcessInstanceWithOptions(startProcessInstanceRequest, startProcessInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(startProcessInstanceResponse.getBody()));
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

   - `originatorUserId`：审批发起人用户ID。
   - `processCode`：审批模板编码。
   - `formComponentValues`：表单组件值，包含附件信息（spaceId、fileName、fileSize、fileType、fileId）。
   - `approvers`：审批人列表，支持会签（AND）和或签（OR）模式。

   **返回字段：**

   - `instanceId`：审批实例ID。
5. **获取审批实例详情**：根据审批实例`instanceId`，调用服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取审批实例详情中的`fileId`。

   ```
    public void processInstancesInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders getProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders();
           getProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest getProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest()
                   .setProcessInstanceId("Ay9***************199");
           try {
               GetProcessInstanceResponse processInstanceWithOptions = client.getProcessInstanceWithOptions(getProcessInstanceRequest, getProcessInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(processInstanceWithOptions.getBody()));
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

   - **processInstanceId**：审批实例ID。

   **返回字段：**

   - **fileId**：附件文件ID，用于后续下载或预览操作。
6. **授权下载审批附件**：调用服务端API-[授权下载审批钉盘文件](0503-download-the-approval-nail-file.md)接口，进行审批钉盘文件的授权操作。

   ```
    public void spaceAuthDownload() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthHeaders addApproveDentryAuthHeaders = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthHeaders();
           addApproveDentryAuthHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos fileInfos0 = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos()
                   .setFileId("49*****61")
                   .setSpaceId(47*****86L);
           com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest addApproveDentryAuthRequest = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest()
                   .setUserId("manager7675")
                   .setFileInfos(java.util.Arrays.asList(
                           fileInfos0
                   ));
           try {
               AddApproveDentryAuthResponse addApproveDentryAuthResponse = client.addApproveDentryAuthWithOptions(addApproveDentryAuthRequest, addApproveDentryAuthHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(addApproveDentryAuthResponse.getBody()));
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

   - `userId`：操作用户ID。
   - `fileInfos`：文件信息列表，包含fileId和spaceId。

   **返回字段：**

   - `result`：授权结果标识。
7. **下载审批附件**：调用服务端API-[下载审批附件](0504-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。目前不支持第三方企业应用调用。

   ```
   public void processFileDownload() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileHeaders grantProcessInstanceForDownloadFileHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileHeaders();
           grantProcessInstanceForDownloadFileHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileRequest grantProcessInstanceForDownloadFileRequest = new com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileRequest()
                   .setProcessInstanceId("Ay9***************199")
                   .setFileId("68********11");
           try {
               GrantProcessInstanceForDownloadFileResponse grantProcessInstanceForDownloadFileResponse = client.grantProcessInstanceForDownloadFileWithOptions(grantProcessInstanceForDownloadFileRequest, grantProcessInstanceForDownloadFileHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(grantProcessInstanceForDownloadFileResponse.getBody()));
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

   - `processInstanceId`：审批实例ID。
   - `fileId`：附件文件ID。

   **返回字段：**

   - `downloadUri`：文件下载链接。
8. **授权预览审批附件**：调用服务端API-[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口，实现钉盘文件的预览操作。

   ```
    public void authPreview() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthHeaders getSpaceWithDownloadAuthHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthHeaders();
           getSpaceWithDownloadAuthHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthRequest getSpaceWithDownloadAuthRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthRequest()
                   .setUserId("ma*****75")
                   .setAgentId(118****5L)
                   .setProcessInstanceId("yIYiVlR3R***********4433")
                   .setFileId("495******61");
           try {
               GetSpaceWithDownloadAuthResponse spaceWithDownloadAuthWithOptions = client.getSpaceWithDownloadAuthWithOptions(getSpaceWithDownloadAuthRequest, getSpaceWithDownloadAuthHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(spaceWithDownloadAuthWithOptions.getBody()));
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

   - `userId`：操作用户ID。
   - `agentId`：应用AgentId。
   - `processInstanceId`：审批实例ID。
   - `fileId`：附件文件ID。

   **返回字段：**

   - `spaceId`：钉盘空间ID。
9. 调用客户端JSAPI-[预览钉盘文件](../03-Ogu5SlPY4t-客户端-JSAPI/0331-jsapi-preview-file-in-ding-talk.md)接口，实现预览钉盘文件。可通过访问[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10317)在线调试该接口。

   > **[!NOTE]**
   >
   > 每一次预览审批附件前，都需要调用[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口实现授权操作。

**实施完成检查清单**

- ✅ 应用凭证获取并配置完成。
- ✅ 接口权限 Workflow.Form.Write、Workflow.Instance.Write、Workflow.Instance.Read 已申请。
- ✅ accessToken 获取接口调通。
- ✅ 审批钉盘空间 spaceId 获取成功。
- ✅ 附件上传 JSAPI 调通并获取 fileId。
- ✅ 审批模板 processCode 获取成功。
- ✅ 发起审批实例接口调通并返回 instanceId。
- ✅ 获取审批实例详情接口可提取 fileId。
- ✅ 授权下载/预览接口调通。
- ✅ 下载/预览审批附件功能验证通过。

## 常见问题（FAQ）

- **Q：为什么调用上传附件JSAPI前必须先获取审批钉盘空间信息？**

  获取审批钉盘空间信息接口会为用户授权钉盘空间访问权限，未授权直接上传会导致权限校验失败。
- **Q：第三方企业应用能否调用下载审批附件接口？**

  目前不支持第三方企业应用调用下载审批附件接口，仅企业内部应用可用。第三方应用可通过授权预览接口实现附件查看。
- **Q：审批附件的授权有效期是多久？**

  授权下载/预览链接为临时授权，有效期由接口返回的token控制，建议在有效期内完成操作，过期需重新授权。
- **Q：如何批量上传多个附件到同一个审批实例？**

  在发起审批实例接口的formComponentValues中，将多个附件的JSON对象放入同一个数组即可，每个对象包含spaceId、fileName、fileSize、fileType、fileId字段。
