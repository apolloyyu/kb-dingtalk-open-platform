---
title: "三方系统快捷审批集成：待办中心与消息卡片一键审批"
source_url: "https://open.dingtalk.com/document/development/custom-quick-approval-supports-quick-approval-of-pending-tasks-from"
namespace: "development"
slug: "custom-quick-approval-supports-quick-approval-of-pending-tasks-from"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 高级专享版 > 三方系统快捷审批集成：待办中心与消息卡片一键审批"
doc_id: "qadJyJX9rv"
updated_at: "2026-10-16 09:23:02"
---

> Source: https://open.dingtalk.com/document/development/custom-quick-approval-supports-quick-approval-of-pending-tasks-from
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 高级专享版 > 三方系统快捷审批集成：待办中心与消息卡片一键审批
> Updated: 2026-10-16 09:23:02

# 三方系统快捷审批集成：待办中心与消息卡片一键审批

## **概述**

本方案面向企业多套业务系统审批任务分散、管理层希望在不离开钉钉界面的前提下快速处理三方审批的场景，通过钉钉OA审批流程中心提供的自定义快捷审批API和回调机制，支持三方业务系统将审批任务同步至钉钉审批中心，并在待办中心列表页、OA审批消息卡片上展示自定义快捷审批按钮。审批人点击按钮后，钉钉回调三方系统更新任务状态并同步回钉钉审批中心，实现一站式沉浸审批体验。

### 方案背景

企业已有大量第三方业务系统（如费控、采购、HR系统）产生审批任务，员工需登录各系统逐一处理，操作路径长、效率低。通过将三方审批接入钉钉待办中心并支持消息卡片一键审批，员工可在钉钉内集中处理所有审批，无需跳转原系统。

企业在日常运营中常面临以下痛点：

- **多系统登录繁琐**： 员工日均需登录5+个业务系统处理审批，每次审批平均耗时3分钟，日均浪费40分钟以上。
- **审批进度不透明**： 提交审批后无法在钉钉内实时查看处理状态，需反复登录原系统刷新确认，催办依赖人工沟通。
- **移动端审批体验差**： 第三方系统多数未适配移动端，员工出差或居家时无法及时处理紧急审批，延误业务进程。
- **审批数据难汇总**： 各部门审批量、平均处理时长等统计指标分散在各系统，管理层无法在钉钉内获取全局视图。

### **核心价值**

本方案的核心价值体现在以下三个方面：

- **一键审批：** 在钉钉待办中心列表页和OA审批消息卡片上直接展示三方系统的快捷审批按钮，审批人无需跳转至业务系统即可完成简单审批操作。
- **闭环同步：** 审批人点击快捷按钮后，钉钉回调三方系统更新任务状态，三方系统将最新状态同步回钉钉审批中心，形成完整数据闭环。
- **灵活定制：** 支持三方系统自定义快捷按钮文案、图标、可见条件，根据业务场景灵活配置不同审批类型的快捷操作入口。

### **适用场景**

本方案适用于审批任务来源多样、简单审批占比高的企业管理场景，典型包括：

- **高管一站式审批：** 公司CEO/CFO等管理层每日需处理来自多个三方系统的审批，其中大量为简单确认类审批，希望在钉钉内一键完成而不跳转系统。
- **高频轻量审批：** 费用报销确认、请假续期、考勤补卡等轻量级审批频次高、操作简单，适合在待办列表直接快捷处理。
- **消息卡片即时审批：** 审批人收到OA审批消息卡片通知后，希望直接在卡片上完成审批操作，无需点击进入详情页。

## **典型业务场景**

### **场景一：连锁酒店集团运营审批快捷处理（酒店文旅行业）**

#### **痛点分析**

某全国连锁酒店集团拥有80+门店，使用自研PMS系统管理客房预订审批、采购系统管理物资申领审批、HR系统管理员工排班调休，三套系统审批任务分散运行。集团运营总监和各店店长每天需处理大量审批，原有流程存在以下问题：

- **简单审批耗时：** 日均审批量60+笔，其中40%为客房超售确认、物资补货确认等简单操作，每次需登录PMS/采购系统、找到对应任务、点击同意，单次操作平均2分钟。
- **移动端体验差：** 店长巡店时用手机处理审批，需在钉钉消息中点击链接跳转至PMS移动端页面，加载慢且操作繁琐，紧急超售确认响应延迟影响客户体验。
- **消息卡片无操作入口：** 收到"客房超售需确认"消息卡片后，只能点击查看詳情，无法直接在卡片上快速确认，错过最佳换房协调窗口。

#### **价值验证**

- **自动化流程**

  ![连锁酒店集团运营审批快捷处理场景图_v3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2949971971/p1105278.png)
- **关键优势**

  - **一键提效：** 简单确认类审批从2分钟降至5秒，日均节省40分钟操作时间，超售确认响应从15分钟缩短至30秒。
  - **移动友好：** 店长手机端在钉钉待办列表直接快捷审批，无需跳转PMS移动端，巡店途中即可实时处理紧急超售。
  - **卡片直操：** OA审批消息卡片嵌入快捷按钮，收到超售通知后直接在卡片上点击确认，避免错过最佳换房协调窗口。

### **场景二：大型建筑项目多方协同审批集成（建筑工程行业）**

#### **痛点分析**

某大型建筑施工企业同时推进15个在建项目，使用自研项目管理系统管理施工进度审批、物资系统管理材料进场验收审批、安全系统管理隐患排查整改审批，三套系统审批流程独立运行。项目经理和安全总监每天需处理大量审批，原有流程存在以下问题：

- **现场审批不便：** 项目经理常驻工地现场，手机信号不稳定时跳转至项目管理系统移动端页面加载缓慢，材料进场验收确认延迟影响施工进度。
- **安全隐患响应慢：** 安全员发现隐患后发起整改审批，安全总监收到消息卡片后需点击进入详情页查看隐患照片和位置信息才能决策，传统流程耗时长，错过最佳整改时机可能引发事故。
- **多方协同低效：** 一个材料验收审批涉及项目部、物资部、监理方三方确认，需在三个系统中分别操作，协调周期长达2天。

#### **价值验证**

- **自动化流程**

  ![大型建筑项目多方协同审批集成场景图_v3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2949971971/p1105279.png)
- **关键优势**

  - **现场高效：** 材料验收确认从3分钟降至5秒，即使工地信号弱也能在钉钉内快速完成，避免施工等待延误。
  - **安全提速：** 隐患整改审批从消息卡片直接快捷操作，响应时间从1小时缩短至5分钟，降低安全事故风险。
  - **协同闭环：** 三方确认类审批通过快捷按钮+回调机制实现状态实时同步，协调周期从2天缩短至4小时。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **模板同步层：** 调用保存流程中心外部集成审批模板接口，将三方业务系统的审批模板同步至钉钉审批中心，获取模板唯一编码`processCode`。
- **任务创建层：** 调用创建/更新审批待办任务接口，将三方系统的审批任务同步至钉钉审批中心，并注册自定义快捷审批按钮及回调地址。
- **回调处理层：** 三方系统提供HTTPS回调接口，接收钉钉快捷审批操作回调，更新本地任务状态并将最新状态同步回钉钉审批中心，形成数据闭环。
- **事件回调层：** 监听审批任务状态变更回调事件，保持三方系统与钉钉审批中心数据一致性。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_aflow`(审批流数据管理权限)
  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Form.Read`（工作流模板读权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限（OA高级版专享））
- **开发环境：** 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：** 下载钉钉服务端SDK，支持Java/Python/Go等多语言。
- **网关准备：** 三方系统回调接口需在钉钉"数据源管理"中注册为网关，详细使用说明参考[数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：核心API调用：

1. 注册自定义快捷审批按钮callback回调接口，网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)。
2. 调用新版服务端API-[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)接口，获取模板的唯一编码`processCode`。
3. 如果没有保存`processCode`，可以通过调用[获取模板code](0510-obtain-the-template-code.md)接口获取`processCode`。
4. 创建审批模板成功后，在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. 根据模板编码`processCode`，调用[保存流程中心外部集成审批实例](0542-api-premiumexternalintegrationprocessinstance.md)接口发起审批实例，获取审批实例`processInstanceId`。
6. 创建审批实例成功后，可进入钉钉OA审批中心，查看审批列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. 根据审批实例`processInstanceId`和待办事项列表tasks，调用[保存流程中心外部集成审批任务](0543-api-premiumsaveintegratedtask.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。
8. 调用[查询通过流程中心集成的OA审批任务](0516-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
9. 根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

   > **[!NOTE]**
   >
   > 在或签等场景，可以调用[批量取消流程中心待处理任务](0518-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
10. 根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)或 [审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)事件，更新实例状态。
11. 若需要对审批模板数据进行清理，可以调用[删除模板](0511-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

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

   - `qyapi_aflow`(审批流数据管理权限)：用于更新流程中心任务状态。
   - `Workflow.Form.Write`（工作流模板写权限）：用于获取模板code。
   - `Workflow.Form.Read`（工作流模板读权限）：用于创建/更新审批实例。
   - `Workflow.Instance.Write`（工作流实例写权限）：用于批量取消流程中心待处理任务。
   - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限（OA高级版专享））：用于获取用户在钉钉审批中心的待处理、已处理、已发起、已收到列表数据。

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

### 步骤四：核心API调用

1. **注册自定义快捷审批按钮callback回调接口：**用于审批人在钉钉待办中心、OA审批消息卡片上直接进行审批操作时，钉钉会回调三方系统，三方系统收到回调后更新任务信息，并将新的任务信息同步回钉钉审批中心，形成闭环。

   > **[!NOTE]**
   >
   > 网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)。
2. **同步审批模板数据到钉钉：**调用新版服务端API-[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)接口，获取模板的唯一编码`processCode`。**该场景下无需进行processFeatureConfig流程中心集成配置。**

   ```
   {
     "name": "快捷审批",
     "description": "保存流程中心外部集成审批模板 (高级版专享接口)",
     "formComponents": [
       {
         "componentType": "TextField",
         "props": {
           "componentId": "TextField-1",
           "label": "单行输入框",
           "required": true,
           "bizAlias": "TextField-bizAlias",
           "disabled": false
         }
       }
     ],
     "templateConfig": {
       "disableSendCard": false
     }
   }
   ```

   **请求参数：**

   - `name`：审批模板名称。
   - `description`：模板描述信息。
   - `formComponents`：表单组件配置数组。
   - `templateConfig`：模板配置，`disableSendCard`表示是否禁用发送消息卡片。

   **返回字段：**

   - `processCode`：审批表单模板唯一编码。
3. 若未保存`processCode`，可以通过调用[获取模板code](0510-obtain-the-template-code.md)接口获取`processCode`。

   ```
   public void getProcessCodeByName() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);

       GetProcessCodeByNameHeaders getProcessCodeByNameHeaders = new GetProcessCodeByNameHeaders();
       getProcessCodeByNameHeaders.xAcsDingtalkAccessToken = "accessToken";

       GetProcessCodeByNameRequest request = new GetProcessCodeByNameRequest()
               .setName("名称");

       try {
           GetProcessCodeByNameResponse getProcessCodeByNameResponse = client.getProcessCodeByNameWithOptions(
                   getProcessCodeByNameRequest,
                   getProcessCodeByNameHeaders,
                   new com.aliyun.teautil.models.RuntimeOptions()
           );
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

   - `name`：模板名称。

   **返回字段：**

   - `processCode`：审批表单模板唯一编码。
4. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. **同步审批实例数据到钉钉：**根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0542-api-premiumexternalintegrationprocessinstance.md)接口发起审批实例，获取审批实例`processInstanceId`。该场景下无需进行`featureConfig`流程中心集成配置。

   ```
   {
     "formComponentValueList": [
       {
         "name": "单行输入框",
         "value": "[钉钉](https://www.dingtalk.com/)"
       }
     ],
     "title": "快捷审批",
     "processCode": "PROC-C818F3C2-BDAB-4055-847A-CAF1EB56E1A8",
     "originatorUserId": "1451694214729725262",
     "url": "http://www.dingtalk.com",
     "notifiers": [
       {
         "userid": "1451694214729725262",
         "position": "start"
       }
     ]
   }
   ```

   **请求参数：**

   - `formComponentValueList`：表单组件值列表。
   - `title`：审批实例标题。
   - `processCode`：审批模板唯一编码。
   - `originatorUserId`：发起人userid。
   - `url`：审批详情页跳转地址。
   - `notifiers`：通知人列表。

   **返回字段：**

   - `processInstanceId`：审批实例唯一ID。
6. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. **同步审批任务数据到钉钉**：根据审批实例`processInstanceId`和待办事项列表tasks，调用[保存流程中心外部集成审批任务](0543-api-premiumsaveintegratedtask.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。

   > **[!NOTE]**
   >
   > - **三方系统可以通过****featureConfig****配置审批任务的回调接口，审批人就可以在钉钉待办中心、OA审批消息卡片直接进行审批操作****。**
   > - **callback中的apiKey是在步骤1中提前注册好的数据源。**

   ```
   {
     "processInstanceId": "OW3kMrjfT9Crje23kP-C3g06701727322896",
     "activityId": "xxx-1",
     "tasks": [
       {
         "userId": "1451694214729725262",
         "url": "https://www.dingtalk.com"
       }
     ],
     "featureConfig": {
       "features": [
         {
           "name": "CUSTOM_SHORTCUT",
           "runType": "REDIRECT",
           "callback": {
             "apiKey": "applyIntegratedCustomAction",
             "appUuid": "dingec6f7227666ad00ba39a90f97fcb1e09",
             "version": "1"
           }
         }
       ]
     }
   }
   ```

   **请求参数：**

   - `processInstanceId`：审批实例唯一ID。
   - `activityId`：审批节点活动ID。
   - `tasks`：待办事项列表，包含审批人userid和详情页URL。
   - `featureConfig`：特性配置列表，`CUSTOM_SHORTCUT`表示自定义快捷审批按钮，`callback.apiKey`为注册的数据源标识。

   **返回字段：**

   - `taskId`：审批待办任务唯一ID。
8. 调用[查询通过流程中心集成的OA审批任务](0516-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。创建待处理任务成功后实现效果如下：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1094471471/p925582.png)

   ```
       public void getPremiumRedirectTasksByManager() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           QueryIntegratedTodoTaskHeaders queryIntegratedTodoTaskHeaders = new QueryIntegratedTodoTaskHeaders();
           queryIntegratedTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
           QueryIntegratedTodoTaskRequest queryIntegratedTodoTaskRequest = new QueryIntegratedTodoTaskRequest()
                   .setUserId("manager001")
                   .setPageSize(1)
                   .setPageNumber(1)
                   .setCreateBefore(1660036833411L);
           try {
               QueryIntegratedTodoTaskResponse queryIntegratedTodoTaskWithOptions = client.queryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `userId`：任务执行人的用户userId。
   - `pageSize`：分页大小，从1开始，最大值40。
   - `pageNumber`：页码，从1开始。
   - `createBefore`：查询的时间起点。

   **返回字段：**

   - `list`：任务列表，包含taskId（OA审批任务ID）、activityId（待办组ID）、processInstanceId（流程实例ID）等。
9. **同步审批任务状态到钉钉：**根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

   ```
   public void getPremiumGetDoneTasks() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     UpdateIntegratedTaskHeaders updateIntegratedTaskHeaders = new UpdateIntegratedTaskHeaders();
     updateIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
     UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks tasks0 = new UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks();
     tasks0.setTaskId(1234567L);
     tasks0.setStatus("COMPLETED");
     UpdateIntegratedTaskRequest updateIntegratedTaskRequest = new UpdateIntegratedTaskRequest()
       .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
       .setTasks(java.util.Arrays.asList(
         tasks0
       ));
     try {
       UpdateIntegratedTaskResponse updateIntegratedTaskWithOptions = client.updateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `processInstanceId`：OA审批流程实例ID。
   - `taskId`：OA审批任务ID。
   - `status`：更新为目标任务状态。

   **返回字段：**

   - `success`：更新结果。

   在或签等场景，可以调用[批量取消流程中心待处理任务](0518-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。

   ```
   public void getCancelIntegratedTask() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     CancelIntegratedTaskHeaders cancelIntegratedTaskHeaders = new CancelIntegratedTaskHeaders();
     cancelIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
     CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new CancelIntegratedTaskRequest()
       .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
       .setActivityId("act_xxxx");
     try {
       CancelIntegratedTaskResponse cancelIntegratedTaskWithOptions = client.cancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `processInstanceId`：OA审批流程实例ID。
   - `activityId`：待办组ID。

   **返回字段：**

   - `success`：操作是否成功。
10. **同步审批实例状态到钉钉：**根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)或 [审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)事件，更新实例状态。
11. 若需要对审批模板数据进行清理，可以调用[删除模板](0511-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

    ```
    public void deleteProcessHeaders() throws Exception {
      Config config = new Config();
      config.protocol = "https";
      config.regionId = "central";
      com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
      DeleteProcessHeaders deleteProcessHeaders = new DeleteProcessHeaders();
      deleteProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
      DeleteProcessRequest deleteProcessRequest = new DeleteProcessRequest()
        .setProcessCode("proc-abc")
        .setCleanRunningTask(false);
      try {
        DeleteProcessResponse deleteProcessResponse = client.deleteProcessWithOptions(deleteProcessRequest, deleteProcessHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

    - `processCode`：模板code。
    - `cleanRunningTask`：是否清理正在运行的任务。

    **返回字段：**

    - `processCode`：模板code。

**实施完成检查清单**

- ✅ 应用已完成创建并获取Client ID和Client Secret。
- ✅ 已申请`qyapi_aflow`、`Workflow.Form.Write`、`Workflow.Form.Read`、`Workflow.Instance.Write`、`Premium.Workflow.ReadWrite.All`权限。
- ✅ accessToken获取成功且缓存策略已配置。
- ✅ 流程中心外部集成审批模板保存成功。
- ✅ 审批待办任务创建成功且快捷审批按钮配置正确。
- ✅ 回调接口已在数据源管理中注册为网关。
- ✅ 快捷审批回调处理逻辑测试通过。
- ✅ 任务状态同步回钉钉审批中心验证通过。
- ✅ 审批实例回调事件注册并正常接收。
- ✅ 钉钉待办中心列表页快捷按钮显示正常。
- ✅ OA审批消息卡片快捷按钮显示正常。

## **常见问题（FAQ）**

- **Q：回调接口超时如何处理？**

  钉钉回调三方系统接口的超时时间为5秒。若三方系统在5秒内未返回HTTP 200，钉钉将进行最多3次重试，间隔分别为1s、2s、4s。建议三方系统回调接口保持轻量，复杂逻辑异步处理。
- **Q：审批人点击快捷按钮后，是否需要再次确认？**

  默认不需要二次确认，点击即执行。若业务场景需要二次确认，可在三方系统回调接口中返回特定状态码，钉钉将弹出确认对话框后再执行操作。
