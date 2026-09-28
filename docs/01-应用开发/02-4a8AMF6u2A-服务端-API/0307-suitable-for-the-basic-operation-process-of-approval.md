---
title: "宜搭审批流程：从业务系统到宜搭审批无缝集成"
source_url: "https://open.dingtalk.com/document/development/suitable-for-the-basic-operation-process-of-approval"
namespace: "development"
slug: "suitable-for-the-basic-operation-process-of-approval"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 使用教程 > 宜搭审批流程：从业务系统到宜搭审批无缝集成"
doc_id: "F3JUb2d9be"
updated_at: "2026-09-23 12:04:40"
---

> Source: https://open.dingtalk.com/document/development/suitable-for-the-basic-operation-process-of-approval
> Path: 应用开发 / 服务端 API / 宜搭 > 使用教程 > 宜搭审批流程：从业务系统到宜搭审批无缝集成
> Updated: 2026-09-23 12:04:40

# 宜搭审批流程：从业务系统到宜搭审批无缝集成

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现宜搭审批单的自动发起、任务处理及状态管理，支持将业务系统中的审批请求自动转换为宜搭审批流程，实现统一审批管理。

## 概述

本方案提供一套完整的宜搭审批集成解决方案，通过调用钉钉开放平台的宜搭相关API，实现在业务系统中直接发起宜搭审批单、查询审批详情、同意/拒绝审批任务、撤销或删除审批实例等功能，支持基于低代码平台构建的个性化审批流程自动化。

### 方案背景

企业在日常运营中常面临以下痛点：

- **宜搭审批手动发起耗时**：业务系统中已生成的审批数据，仍需人工在宜搭应用中重新填写表单并提交，重复操作效率极低
- **审批进度难追踪**：宜搭审批单的状态变化（待审批/已通过/已拒绝）无法实时同步至业务系统，需人工反复查看
- **任务节点管理复杂**：宜搭审批流程中的任务节点taskId在转交后会发生变化，难以准确定位当前审批人
- **数据孤岛阻碍协同**：宜搭审批数据未与业务系统打通，审批完成后需人工更新业务数据，容易遗漏

### 核心价值

本方案提供一套完整的宜搭审批集成解决方案，通过调用钉钉开放平台的宜搭相关API，实现在业务系统中直接发起宜搭审批单、查询审批详情、同意/拒绝审批任务、撤销或删除审批实例等功能。

- **审批自动发起**：业务系统确定审批数据后一键同步至宜搭审批，无需人工重新填写表单，大幅提升审批效率
- **审批详情实时查询**：支持根据formInstanceId获取宜搭审批单的完整详情信息，包括表单数据、审批进度等
- **审批任务智能处理**：支持业务系统自动同意/拒绝宜搭审批任务，实现审批流程自动化
- **审批实例灵活管理**：支持撤销或删除宜搭审批实例，满足数据纠错和流程调整需求

### 适用场景

本方案适用于以下典型业务场景：

- **CRM系统客户审批自动流转**：销售人员在CRM系统中提交客户资质审核申请后自动创建宜搭审批单，审批人直接在宜搭端处理
- **ERP系统采购审批集成**：采购申请在ERP系统中提交后自动生成宜搭审批流程，审批通过后自动更新采购单状态
- **HR系统入职审批联动**：新员工入职资料在HR系统录入后自动发起宜搭审批，审批通过后自动开通账号权限
- **财务系统报销审批同步**：员工在财务系统提交报销申请后自动创建宜搭审批单，审批结果回写财务系统触发付款

## 典型业务场景

### 场景一：CRM系统客户资质审核自动发起宜搭审批

#### 痛点分析

销售团队在CRM系统中录入客户信息后，仍需人工在宜搭应用中重新填写客户资质审核表单：

- CRM系统中的客户数据无法自动带入宜搭审批表单，需人工复制粘贴
- 审批人在宜搭中看不到CRM系统的客户审核申请，需频繁切换系统查看
- 审批进度无法实时同步至CRM系统，销售人员难以掌握审核状态
- 审批完成后客户状态无法自动更新，需人工手动修改

#### 价值验证

- **自动化流程**

  ![CRM客户资质审核流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0826310971/p1103534.png)
- **关键优势**

  - **审批自动发起**：CRM系统提交客户审核后1秒内自动创建宜搭审批单，无需人工重复填写表单。
  - **审批详情实时查询**：支持根据formInstanceId随时获取宜搭审批单的完整详情，包括表单数据和审批进度。
  - **状态实时回写**：审批完成后通过API自动更新CRM系统客户状态为"已审核"，确保数据一致性。

### 场景二：ERP系统采购审批与宜搭流程联动

#### 痛点分析

采购部门在ERP系统中提交采购申请，但审批流程需在宜搭中独立处理：

- 采购申请数据分散在ERP和宜搭两个系统中，管理层难以统一查看
- 审批人需在宜搭中查找待审批采购单，容易遗漏重要审批
- 宜搭审批流程中的任务节点taskId在转交后会变化，难以准确定位当前审批人
- 审批通过后采购单状态无法自动更新，需人工手动修改

#### 价值验证

- **自动化流程**

  ![ERP采购审批联动流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0826310971/p1103535.png)
- **关键优势**

  - **审批流程标准化**：复用宜搭低代码平台构建的个性化审批流程，满足不同业务的审批需求。
  - **任务节点精准定位**：通过查询流程运行任务接口动态获取最新taskId，即使转交后也能准确处理审批。
  - **审批结果自动同步**：审批通过后ERP系统自动更新采购单状态为"已批准"，触发后续采购流程。

## 实施指南

### 技术架构

- **接口调用层**：调用宜搭服务端API实现审批单的发起、查询、处理等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **实例管理层**：调用宜搭审批实例相关API发起、查询、撤销、删除审批实例，获取formInstanceId。
- **任务处理层**：调用宜搭任务相关API查询流程运行任务获取taskId，同意或拒绝审批任务。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成**企业内部应用**的创建与配置，并[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)为**网页应用**。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Yida.Process.Write`（宜搭流程数据写权限）
  - `Yida.Process.Read`（宜搭流程数据读权限）
  - `Yida.Task.Read`（宜搭任务读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，查找"宜搭"相关权限并申请。

步骤三：调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口，获取应用访问凭证。

步骤四：调用服务端宜搭相关API。

1. 调用服务端API-[发起宜搭审批流程](0313-api-startinstance-v2.md)接口，创建宜搭审批单流程，获取宜搭审批单的流程实例formInstanceId。
2. 根据审批单流程实例formInstanceId，调用服务端API-[根据流程实例ID获取流程实例](0317-api-getinstancebyid-v2.md)接口，获取宜搭审批单的详情信息。
3. 根据审批单流程实例formInstanceId，调用服务端API-[查询流程运行任务（VPC）](0348-query-process-running-tasks-vpc.md)接口，获取宜搭审批单的节点信息taskId。
4. 根据审批单流程实例formInstanceId和任务节点taskId，调用服务端API-[同意或拒绝宜搭审批任务](0347-execute-approval-tasks.md)接口，执行同意或者拒绝宜搭审批单。
5. 根据审批单流程实例formInstanceId，调用服务端API-[终止流程实例](0310-terminate-a-process-instance.md)接口，实现宜搭审批单撤销操作。
6. 如需删除流程实例数据，调用服务端API-[删除流程实例](0311-delete-the-process-instance.md)接口，实现删除宜搭审批单数据信息。

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

1. **发起宜搭审批流程**：调用服务端API-[发起宜搭审批流程](0313-api-startinstance-v2.md)接口，创建宜搭审批单流程，获取宜搭审批单的流程实例formInstanceId。

   ```
   public void processesInstancesStart() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);

       // 设置请求头
       StartInstanceHeaders startInstanceHeaders = new StartInstanceHeaders();
       startInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建表单数据JSON
       String formDataJson = "{" +
               "\"textField_laao2rcb\": \"测试单行输入框\"," +
               "\"textareaField_laao2rcc\": \"测试多行输入框\"," +
               "\"numberField_laao2rcd\": 50," +
               "\"radioField_laao2rce\": \"选项一\"," +
               "\"checkboxField_laao2rcf\": [\"选项一\",\"选项二\"]," +
               "\"cascadeDateField_laao2rcl\": [\"1668063209000\",\"1668066809000\"]," +
               "\"attachmentField_laao2rcm\": [{" +
               "\"downloadUrl\":\"/ossFileHandle?appType=APP_IE*****SY47KISEL8RXQ&fileName=APP_IE*****SY47KISEL8RXQ_bWFuYWdlcjc2NzVfNU85NjZHRDFQQkM1NjI0SjdJTUZQNFUwU0E4STM1SkVYT0FBTFVX.png&instId=&type=download&originalFileName=mylike.png\"," +
               "\"name\":\"mylike.png\"," +
               "\"previewUrl\":\"/ossFileHandle?appType=APP_IE*****SY47KISEL8RXQ&fileName=APP_IE*****SY47KISEL8RXQ_bWFuYWdlcjc2NzVfNU85NjZHRDFQQkM1NjI0SjdJTUZQNFUwU0E4STM1SkVYT0FBTFVX.png&instId=&type=open\"," +
               "\"size\":5909," +
               "\"url\":\"/ossFileHandle?appType=APP_IE*****SY47KISEL8RXQ&fileName=APP_IE*****SY47KISEL8RXQ_bWFuYWdlcjc2NzVfNU85NjZHRDFQQkM1NjI0SjdJTUZQNFUwU0E4STM1SkVYT0FBTFVX.png&instId=&type=download\"" +
               "}]," +
               "\"employeeField_laao2rcn\":[\"manager7675\"]" +
               "}";

       // 构建发起流程实例请求
       StartInstanceRequest startInstanceRequest = new StartInstanceRequest()
               .setAppType("APP_IE*****SY47KISEL8RXQ")
               .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
               .setUserId("manager7675")
               .setLanguage("zh_CN")
               .setFormUuid("FORM-4W8667*******C7UFKA0Q5TH83BZJ2OAALQ")
               .setFormDataJson(formDataJson)
               .setProcessCode("TPROC--4W8667D1*******UFKA0Q5TH83CZJ2OAALR");

       try {
           StartInstanceResponse startInstanceResponse = client.startInstanceWithOptions(
                   startInstanceRequest, startInstanceHeaders, new RuntimeOptions());
           System.out.println(JSON.toJSONString(startInstanceResponse.getBody()));
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

   - `processCode`：**重点参数**，宜搭审批流程编码。
   - `formDataJson`：**重点参数**，表单数据JSON字符串。
   - `userId`：**重点参数**，发起人userId。

   **返回字段**：

   - `formInstanceId`：**重点参数**，宜搭审批单的流程实例ID，后续所有操作均需使用此ID。
2. **根据流程实例ID获取流程实例**：根据审批单流程实例formInstanceId，调用服务端API-[根据流程实例ID获取流程实例](0317-api-getinstancebyid-v2.md)接口，获取宜搭审批单的详情信息。

   ```
   public void instancesInfos() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);

       // 设置请求头
       GetInstanceByIdHeaders getInstanceByIdHeaders = new GetInstanceByIdHeaders();
       getInstanceByIdHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建查询请求参数
       GetInstanceByIdRequest getInstanceByIdRequest = new GetInstanceByIdRequest()
               .setAppType("APP_IE*****SY47KISEL8RXQ")
               .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
               .setUserId("manager7675")
               .setLanguage("zh_CN");

       try {
           // 根据实例ID获取流程实例详情
           GetInstanceByIdResponse instanceByIdWithOptions = client.getInstanceByIdWithOptions(
                   "9a3f8xxxx64a6",
                   getInstanceByIdRequest,
                   getInstanceByIdHeaders,
                   new RuntimeOptions());
           System.out.println(JSON.toJSONString(instanceByIdWithOptions.getBody()));
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
3. **查询流程运行任务（VPC）**：根据审批单流程实例formInstanceId，调用服务端API-[查询流程运行任务（VPC）](0348-query-process-running-tasks-vpc.md)接口，获取宜搭审批单的节点信息taskId。

   ```
   public void RunningTasks() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);

       // 设置请求头
       GetRunningTasksHeaders getRunningTasksHeaders = new GetRunningTasksHeaders();
       getRunningTasksHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建查询运行中任务请求参数
       GetRunningTasksRequest getRunningTasksRequest = new GetRunningTasksRequest()
               .setProcessInstanceId("9a3f8aa3-2bf4-49a9-9789-a4b78aaf64a6")
               .setAppType("APP_IE*****SY47KISEL8RXQ")
               .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
               .setLanguage("zh_CN")
               .setUserId("manager7675");

       try {
           GetRunningTasksResponse runningTasksWithOptions = client.getRunningTasksWithOptions(
                   getRunningTasksRequest, getRunningTasksHeaders, new RuntimeOptions());
           System.out.println(JSON.toJSONString(runningTasksWithOptions.getBody()));
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

   - `processInstanceId`：**重点参数**，宜搭审批单的流程实例ID。

   **返回字段**：

   - `taskId`：**重点参数**，审批任务节点ID，同意或拒绝审批任务时需使用。

     > **[!NOTE]**
     >
     > 如果宜搭审批单调用过[转交任务](0343-transfer-tasks.md)接口，taskId值是会发生变化，调用[同意或拒绝宜搭审批任务](0347-execute-approval-tasks.md)接口时，需要再次调用[查询流程运行任务（VPC）](0348-query-process-running-tasks-vpc.md)接口，获取最新的taskId值。
4. **同意或拒绝宜搭审批任务**：根据审批单流程实例formInstanceId和任务节点taskId，调用服务端API-[同意或拒绝宜搭审批任务](0347-execute-approval-tasks.md)接口，执行同意或者拒绝宜搭审批单。

   ```
   public void tasksExecute() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);

       // 设置请求头
       ExecuteTaskHeaders executeTaskHeaders = new ExecuteTaskHeaders();
       executeTaskHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建执行任务请求参数
       ExecuteTaskRequest executeTaskRequest = new ExecuteTaskRequest()
               .setOutResult("AGREE")
               .setAppType("APP_IE*****SY47KISEL8RXQ")
               .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
               .setLanguage("zh_CN")
               .setRemark("确认同意")
               .setProcessInstanceId("9a3f8axxxx8aaf64a6")
               .setUserId("manager7675")
               .setTaskId(5578876505L);

       try {
           client.executeTaskWithOptions(executeTaskRequest, executeTaskHeaders, new RuntimeOptions());
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

   - `processInstanceId`：**重点参数**，宜搭审批单的流程实例ID。
   - `taskId`：**重点参数**，审批任务节点ID。
   - `outResult`：**重点参数**，审批结果（AGREE表示同意，DISAGREE表示拒绝）。
   - `remark`：审批意见。
5. **终止流程实例（撤销审批）**：根据审批单流程实例formInstanceId，调用服务端API-[终止流程实例](0310-terminate-a-process-instance.md)接口，实现宜搭审批单撤销操作。

   ```
   public void instancesTerminate() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);

       // 设置请求头
       TerminateInstanceHeaders terminateInstanceHeaders = new TerminateInstanceHeaders();
       terminateInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建终止流程实例请求参数
       TerminateInstanceRequest terminateInstanceRequest = new TerminateInstanceRequest()
               .setAppType("APP_IE*****SY47KISEL8RXQ")
               .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
               .setUserId("manager7675")
               .setLanguage("zh_CN")
               .setProcessInstanceId("9a1985xxxx3018b");

       try {
           client.terminateInstanceWithOptions(terminateInstanceRequest, terminateInstanceHeaders, new RuntimeOptions());
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

   - `processInstanceId`：**重点参数**，宜搭审批单的流程实例ID。
6. **删除流程实例**：如需删除流程实例数据，调用服务端API-[删除流程实例](0311-delete-the-process-instance.md)接口，实现删除宜搭审批单数据信息。

   ```
   public void instancesDelete() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);

       // 设置请求头
       DeleteInstanceHeaders deleteInstanceHeaders = new DeleteInstanceHeaders();
       deleteInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 构建删除流程实例请求参数
       DeleteInstanceRequest deleteInstanceRequest = new DeleteInstanceRequest()
               .setAppType("APP_IE*****SY47KISEL8RXQ")
               .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
               .setUserId("manager7675")
               .setLanguage("zh_CN")
               .setProcessInstanceId("9a198xxxx843018b");

       try {
           client.deleteInstanceWithOptions(deleteInstanceRequest, deleteInstanceHeaders, new RuntimeOptions());
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

   - `processInstanceId`：**重点参数**，宜搭审批单的流程实例ID。

**实施完成检查清单**：

- ✅ 企业内部应用创建成功（网页应用）。
- ✅ Client ID 和 Client Secret获取成功。
- ✅ 宜搭接口权限申请成功。
- ✅ accessToken获取成功。
- ✅ 宜搭审批流程发起成功，获取formInstanceId。
- ✅ 审批单详情查询成功，返回正确的表单数据。
- ✅ 流程运行任务查询成功，获取正确的taskId。
- ✅ 审批任务同意/拒绝操作成功。
- ✅ 审批单撤销操作成功。
- ✅ 审批单删除操作成功。

## 常见问题（FAQ）

- **Q1：宜搭审批和OA审批有什么区别？**

  A：宜搭审批是基于钉钉宜搭低代码平台构建的个性化审批流程，适用于企业自定义的业务审批场景；OA审批是钉钉官方提供的标准审批流程引擎。两者使用不同的API接口，不能混用。本文档专门介绍宜搭审批的集成方案。
- **Q2：为什么taskId会发生变化？**

  A：如果宜搭审批单调用过转交任务接口，将审批任务转交给其他人处理，taskId值会发生变化。因此在调用同意或拒绝宜搭审批任务接口时，需要先再次调用查询流程运行任务（VPC）接口，获取最新的taskId值，避免因taskId过期导致操作失败。
- **Q3：如何获取宜搭审批流程的processCode？**

  A：processCode是宜搭审批流程的唯一标识，可在宜搭应用后台查看已创建的审批流程列表获取。也可在创建宜搭应用时由系统自动生成。
- **Q4：终止流程实例和删除流程实例有什么区别？**

  A：

  - 终止流程实例：撤销正在进行的审批流程，审批单状态变为"已撤销"，但数据仍保留在系统中
  - 删除流程实例：彻底删除审批单数据，数据将从系统中移除，不可恢复

  建议优先使用终止流程实例，仅在需要清理测试数据时使用删除流程实例。
