---
title: "深度集成钉钉OA审批：专享OpenAPI与AppLink协议对接"
source_url: "https://open.dingtalk.com/document/development/use-the-exclusive-openapi-capability-to-dingtalk-oa-approval-through"
namespace: "development"
slug: "use-the-exclusive-openapi-capability-to-dingtalk-oa-approval-through"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 高级专享版 > 深度集成钉钉OA审批：专享OpenAPI与AppLink协议对接"
doc_id: "qK67vMgGCX"
updated_at: "2026-10-12 18:04:50"
---

> Source: https://open.dingtalk.com/document/development/use-the-exclusive-openapi-capability-to-dingtalk-oa-approval-through
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 高级专享版 > 深度集成钉钉OA审批：专享OpenAPI与AppLink协议对接
> Updated: 2026-10-12 18:04:50

# 深度集成钉钉OA审批：专享OpenAPI与AppLink协议对接

## 概述

本方案面向企业多套业务系统已接入钉钉OA审批流程中心、但希望进一步实现个性化定制的场景，通过钉钉OA审批高级版专享OpenAPI和前端页面AppLink协议，支持企业自建应用深度集成钉钉官方OA审批。该方案提供审批中心列表查询、批量处理审批任务、流程交接、审批页面跳转等专享能力，帮助企业构建一站式沉浸式审批工作台，实现分来源筛选、批量操作、管理员代转交等个性化业务需求。

### 方案背景

企业在完成自有OA审批或官方OA审批的基础集成后，往往面临更深层的定制化诉求：管理层希望在自建应用中统一查看和处理所有审批任务，而非在钉钉原生界面中操作；管理员需要批量将离职员工的待办任务转交给接替人员；业务系统希望直接跳转到钉钉官方OA审批的特定页面（如发起页、详情页）以复用钉钉原生交互体验。钉钉OA审批高级版提供了专享OpenAPI和AppLink协议，使这些个性化需求得以快速落地。

### 核心价值

本方案的核心价值体现在以下三个方面：

- **深度定制**： 专享OpenAPI开放审批中心列表、批量处理、流程交接等能力，企业可根据自身业务逻辑实现页面和功能逻辑的完全定制。
- **丰富能力**： AppLink协议支持从自建应用直接跳转至钉钉官方OA审批首页、实例发起页、实例详情页等，复用钉钉原生交互体验。
- **个性响应**： 支持企业自建审批中心、流程交接、审批页面集成等多种业务解决方案，响应更个性化的业务需求。

### 适用场景

本方案适用于已完成基础OA审批集成、需要进一步深化定制的企业场景，典型包括：

- **一站式沉浸审批**： 公司管理层日常审批事项繁多，希望把多个三方系统的审批流程和钉钉侧流程集中在企业自建应用内统一批量处理。
- **管理员流程交接**： 员工离职或岗位调整时，管理员需批量将其待处理审批任务转交给组织内其他在职人员。
- **审批页面深度集成**： 企业自建应用内的某些业务功能模块，希望直接跳转打开钉钉官方OA审批首页、实例发起页、实例详情页等。

## 典型业务场景

### 场景一：大型零售连锁门店运营审批聚合（零售行业）

#### 痛点分析

某全国连锁零售品牌拥有500+门店，使用自研POS系统管理门店补货申请、SAP系统管理供应商采购订单、自研HR系统管理店员排班调休，三套系统各有独立审批流程。区域经理和总部运营总监每天需登录三个系统分别查看和处理审批，存在以下问题：

- **多系统切换频繁**： 日均审批量80+笔，分布在三个系统中，每次切换需重新登录、查找待办，耗时约25分钟。
- **批量操作缺失**： 同类审批（如批量补货、批量排班调整）无法一次性处理，需逐条点击同意，重复操作疲劳度高。
- **审批上下文割裂**： 在POS中看不到关联的供应商库存状态，在SAP中看不到门店历史销售数据，决策信息不完整。

#### 价值验证

- **自动化流程**

  ![零售连锁门店运营审批聚合场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0949971971/p1105199.png)
- **关键优势**

  - **多源聚合**： POS补货审批、SAP采购审批、HR排班审批三类待办统一展示，无需切换系统，日均节省25分钟操作时间。
  - **批量提效**： 同类审批勾选后批量同意，单次操作从80次点击降至3次，高频场景处理效率提升90%以上。
  - **上下文完整**： 自建审批中心详情页嵌入各系统数据接口，审批人可在同一页面查看关联库存、历史销量等辅助决策信息。

### 场景二：全国物流枢纽园区运营审批集成（物流仓储行业）

#### 痛点分析

某全国物流枢纽园区入驻企业超200家，各企业使用不同ERP/WMS系统管理仓储作业，园区管委会需统一监管安全生产、环保合规、消防巡检等审批事项。原有监管模式存在以下问题：

- **监管碎片化**： 200+企业系统各异，管委会无法统一查看园区安全合规状态，隐患排查依赖企业自主上报，瞒报漏报率高。
- **整改跟踪难**： 发现违规项后需线下发整改通知书、电话催办、现场复核，缺乏数字化跟踪手段，整改完成率仅65%。
- **应急响应滞后**： 突发事件（如危化品泄漏、火灾警报）需多部门协同审批处置，传统电话协调耗时长，错过最佳处置窗口。

#### 价值验证

- **自动化流程**

  ![物流枢纽园区运营审批集成场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0949971971/p1105250.png)
- **关键优势**

  - **风险全景**： 200+企业安全合规状态一屏呈现，隐患自动分级预警，瞒报漏报率从高位降至5%以下。
  - **整改闭环**： 违规项一键发起整改指令，系统自动跟踪进度并提醒逾期未改企业，整改完成率从65%提升至95%。
  - **应急联动**： 突发事件自动触发多部门协同审批，响应时间从2小时缩短至10分钟，抓住最佳处置窗口。

## 实施指南

### 技术架构

本方案的技术架构包含以下核心组件：

- **身份鉴权层**： 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **数据聚合层**： 调用钉钉OA审批高级版专享接口，聚合官方OA审批、自有OA审批等多来源待办数据至统一列表。
- **批量处理层**： 根据审批类型processType区分官方/自有审批任务，分别调用对应批量更新接口完成状态同步。
- **流程交接层**： 支持管理员查询指定员工待处理任务列表，并批量将任务转交给组织内其他在职人员。
- **页面集成层**： 通过AppLink协议从自建应用跳转至钉钉官方OA审批首页、实例发起页、实例详情页等。
- **事件回调层**： 监听审批任务开始、结束、转交及审批实例状态变更等回调事件，保持自建审批中心数据实时性。

### 前置条件

- **应用准备**： 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**： 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限（OA高级版专享））
  - `qyapi_aflow`(审批流数据管理权限)
- **开发环境**： 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**： 下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### 代码实现

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 选择集成方式：

   - **自有OA审批集成：**三方业务系统分别对接钉钉自有OA审批，具体步骤参考[自有OA审批：三方流程与页面对接](0483-use-three-party-process-and-page-docking.md)。
   - **官方OA审批集成：**三方业务系统对接钉钉官方OA审批，具体步骤参考：[官方OA审批：钉钉流程与页面对接](0482-use-the-dingtalk-oa-approval-process-and-page-interface.md)。
   - **用户主动发起：**可直接在钉钉官方OA审批应用内提交审批流程，通过上方两步骤将分散的业务流程集中到钉钉OA审批中心进行管理。
2. **获取审批中心数据：**根据高级版专享相关接口，获取用户在钉钉审批中心的[待处理](0534-api-premiumgettodotasks.md)、[已处理](0535-api-premiumgetdonetasks.md)、[已发起的](0526-api-premiumgetsubmittedinstances.md)、[已收到的](0527-api-premiumgetnoticedinstances.md)审批列表数据。
3. **批量审批任务：**企业自建审批中心应用获取到用户审批中心任务列表数据后，可根据待处理列表接口返回的审批类型`processType`（0：官方OA审批、1：自有OA审批），分别对官方OA审批、自有OA审批的任务进行批量更新。

   - **自有OA审批任务批量更新：**根据审批实例`processInstanceId`和`taskId`，调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0518-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
   - **官方OA审批任务批量更新：**业务系统根据审批实例`processInstanceId`和`taskId`信息，调用新版服务端API-[批量同意或拒绝审批任务](0536-api-premiumbatchexecuteprocessinstances.md)，对一批具有不同审批实例ID、任务节点ID的审批任务，进行批量处理。
4. 审批单状态发生变化后，OA审批支持将[审批任务状态变化](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例状态变化](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧，可以让企业应用能够更深度地与钉钉平台集成，实现信息共享和业务协同。具体使用教程参考：[事件订阅操作指南](0014-event-subscription-overview.md)。
5. 调用[管理员查询指定员工的待处理任务列表](0537-api-premiumquerytodotasksbymanager.md)，通过管理员(managerUserId) 查询当前审批人UserId的所有待处理的OA审批任务信息。
6. 调用[管理员批量转交指定员工的待处理任务](0538-api-premiumredirecttasksbymanager.md)，由管理员将管理员查询指定员工的待处理任务列表接口返回的任务批量转交给组织内其他在职人员处理。

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

   - `Workflow.Instance.Write`（工作流实例写权限）：用于批量取消流程中心待处理任务。
   - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限（OA高级版专享））：用于获取用户在钉钉审批中心的待处理、已处理、已发起、已收到列表数据。
   - `qyapi_aflow`(审批流数据管理权限)：用于更新流程中心任务状态。

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

1. **选择集成方式**：

   - **自有OA审批集成：**三方业务系统分别对接钉钉自有OA审批，通过钉钉**自有OA审批相关接口**将业务系统的审批任务数据同步至钉钉OA审批流程中心，具体步骤参考[自有OA审批：三方流程与页面对接](0483-use-three-party-process-and-page-docking.md)。
   - **官方OA审批集成：**三方业务系统对接钉钉官方OA审批，通过钉钉**官方OA审批相关接口**直接在业务系统内发起钉钉官方OA审批流程，具体步骤参考：[官方OA审批：钉钉流程与页面对接](0482-use-the-dingtalk-oa-approval-process-and-page-interface.md)。
   - **用户主动发起：**可直接在钉钉官方OA审批应用内提交审批流程，通过上方两步骤将分散的业务流程集中到钉钉OA审批中心进行管理。
2. **获取审批中心数据**：根据[关于新增OA审批高级版专享OpenAPI和解决方案的说明](1439-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md)中高级版专享相关接口，获取用户在钉钉审批中心的[待处理](0534-api-premiumgettodotasks.md)、[已处理](0535-api-premiumgetdonetasks.md)、[已发起的](0526-api-premiumgetsubmittedinstances.md)、[已收到的](0527-api-premiumgetnoticedinstances.md)审批列表数据。

   - **查询审批中心用户待处理任务列表**

     ```
     public void getPremiumGetTodoTasks() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       PremiumGetTodoTasksHeaders premiumGetTodoTasksHeaders = new PremiumGetTodoTasksHeaders();
       premiumGetTodoTasksHeaders.xAcsDingtalkAccessToken = "<your access token>";
       PremiumGetTodoTasksRequest premiumGetTodoTasksRequest = new PremiumGetTodoTasksRequest()
         .setUserId("manager001")
         .setPageSize(20)
         .setPageNumber(1)
         .setCreateBefore("2024-08-04 17:30:47");
       try {
         PremiumGetTodoTasksResponse premiumGetTodoTasksOptions = client.premiumGetTodoTasksWithOptions(premiumGetTodoTasksRequest, premiumGetTodoTasksHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

     - `userId`：OA审批任务执行人的用户userId。
     - `createBefore`：查询的待办任务创建时间要小于该值，为null则取全部。
     - `pageSize`：分页大小，从1开始，最大值20。
     - `pageNumber`：页码，从1开始, 最大限制10。

     **返回字段：**

     - `list`：待处理任务列表，主要包含`taskId`（任务ID）、`processInstanceId`（实例ID）、`status`（流程状态）、`processType`（审批类型）。
   - **查询审批中心用户已处理任务列表**

     ```
     public void getPremiumGetDoneTasksHeaders() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       PremiumGetDoneTasksHeaders premiumGetDoneTasksHeaders = new PremiumGetDoneTasksHeaders();
       premiumGetDoneTasksHeaders.xAcsDingtalkAccessToken = "<your access token>";
       PremiumGetDoneTasksRequest premiumGetDoneTasksRequest = new PremiumGetDoneTasksRequest()
         .setUserId("manager001")
         .setPageSize(20)
         .setPageNumber(1);
       try {
         PremiumGetDoneTasksResponse premiumGetDoneTasksResponse = client.premiumGetDoneTasksWithOptions(premiumGetDoneTasksRequest, premiumGetDoneTasksHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

     - `userId`：OA审批任务执行人的用户userId。
     - `pageSize`：分页大小，从1开始，最大值20。
     - `pageNumber`：页码，从1开始, 最大限制10。

     **返回字段：**

     - `list`：待处理任务列表，主要包含`taskId`（任务ID）、`processInstanceId`（实例ID）、`status`（流程状态）、`processType`（审批类型）。
   - **查询审批中心用户已发起实例列表**

     ```
     public void getPremiumGetDoneTasksHeaders() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       PremiumGetSubmittedInstancesHeaders premiumGetSubmittedInstancesHeaders = new PremiumGetSubmittedInstancesHeaders();
       premiumGetSubmittedInstancesHeaders.xAcsDingtalkAccessToken = "<your access token>";
       PremiumGetSubmittedInstancesRequest premiumGetSubmittedInstancesRequest = new PremiumGetSubmittedInstancesRequest()
         .setUserId("manager001")
         .setPageSize(20)
         .setPageNumber(1);
       try {
         PremiumGetSubmittedInstancesResponse premiumGetSubmittedInstancesWithOptions = client.premiumGetSubmittedInstancesWithOptions(premiumGetSubmittedInstancesRequest, premiumGetSubmittedInstancesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

     - `userId`：OA审批任务执行人的用户userId。
     - `pageSize`：分页大小，从1开始，最大值20。
     - `pageNumber`：页码，从1开始, 最大限制10。

     **返回字段：**

     - `list`：待处理任务列表，主要包含`taskId`（任务ID）、`processInstanceId`（实例ID）、`status`（流程状态）、`processType`（审批类型）。
   - **查询审批中心用户已收到的实例列表**

     ```
     public void getPremiumGetDoneTasksHeaders() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       PremiumGetNoticedInstancesHeaders premiumGetNoticedInstancesHeaders = new PremiumGetNoticedInstancesHeaders();
       premiumGetNoticedInstancesHeaders.xAcsDingtalkAccessToken = "<your access token>";
       PremiumGetNoticedInstancesRequest premiumGetSubmittedInstancesRequest = new PremiumGetNoticedInstancesRequest()
         .setUserId("manager001")
         .setPageSize(20)
         .setPageNumber(1);
       try {
         PremiumGetNoticedInstancesResponse premiumGetNoticedInstancesWithOptions = client.premiumGetNoticedInstancesWithOptions(premiumGetSubmittedInstancesRequest, premiumGetNoticedInstancesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

     - `userId`：OA审批任务执行人的用户userId。
     - `pageSize`：分页大小，从1开始，最大值20。
     - `pageNumber`：页码，从1开始, 最大限制10。

     **返回字段：**

     - `list`：待处理任务列表，主要包含`taskId`（任务ID）、`processInstanceId`（实例ID）、`status`（流程状态）、`processType`（审批类型）。
3. **批量审批任务：**根据待处理列表接口返回的审批类型`processType`（0：官方OA审批、1：自有OA审批），分别对官方OA审批、自有OA审批的任务进行批量更新。

   - **自有OA审批任务批量更新：**根据审批实例`processInstanceId`和`taskId`，调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

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
   - **官方OA审批任务批量更新：**业务系统根据审批实例`processInstanceId`和`taskId`信息，调用新版服务端API-[批量同意或拒绝审批任务](0536-api-premiumbatchexecuteprocessinstances.md)，对一批具有不同审批实例ID、任务节点ID的审批任务，进行批量处理。

     ```
     public void getPremiumBatchExecuteProcessInstances() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       PremiumBatchExecuteProcessInstancesHeaders premiumBatchExecuteProcessInstancesHeaders = new PremiumBatchExecuteProcessInstancesHeaders();
       premiumBatchExecuteProcessInstancesHeaders.xAcsDingtalkAccessToken = "<your access token>";
       PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList taskInfoList0 = new PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList()
         .setTaskId(12345L)
         .setProcessInstanceId("a171de6c-8bxxxx");
       PremiumBatchExecuteProcessInstancesRequest processInstancesRequest = new PremiumBatchExecuteProcessInstancesRequest()
         .setTaskInfoList(java.util.Arrays.asList(
           taskInfoList0
         ))
         .setActionerUserId("67583405630")
         .setResult("agree");
       try {
         PremiumBatchExecuteProcessInstancesResponse processInstancesResponse = client.premiumBatchExecuteProcessInstancesWithOptions(processInstancesRequest, premiumBatchExecuteProcessInstancesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

     - `taskId`：任务ID。
     - `processInstanceId`：审批实例ID。
     - `actionerUserId`：实际执行人用户ID。
     - `result`：审批操作，agree（同意）或refuse（拒绝）。

     **返回字段：**

     - `result`：任务结果。
4. 审批单状态发生变化后，将[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧。可以让企业应用能够更深度地与钉钉平台集成，实现信息共享和业务协同。具体使用教程参考：[事件订阅操作指南](0014-event-subscription-overview.md)。
5. 调用[管理员查询指定员工的待处理任务列表](0537-api-premiumquerytodotasksbymanager.md)，通过管理员(managerUserId) 查询当前审批人UserId的所有待处理的OA审批任务信息。

   ```
   public void getPremiumQueryTodoTasksByManager() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     PremiumQueryTodoTasksByManagerHeaders premiumQueryTodoTasksByManagerHeaders = new PremiumQueryTodoTasksByManagerHeaders();
     premiumQueryTodoTasksByManagerHeaders.xAcsDingtalkAccessToken = "<your access token>";
     PremiumQueryTodoTasksByManagerRequest premiumBatchExecuteProcessInstancesHeaders = new PremiumQueryTodoTasksByManagerRequest()
       .setNextToken(1)
       .setMaxResults(20)
       .setActionerUserId("staffId123")
       .setManagerUserId("manager123");
     try {
       PremiumQueryTodoTasksByManagerResponse premiumQueryTodoTasksByManagerWithOptions = client.premiumQueryTodoTasksByManagerWithOptions(premiumBatchExecuteProcessInstancesHeaders, premiumQueryTodoTasksByManagerHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `actionerUserId`：操作人userId。
   - `managerUserId`：管理员userId。
   - `nextToken`：分页标识，从1开始。
   - `maxResults`：分页大小，最大值20。

   **返回字段：**

   - `list`：结果列表，包含`taskId`（OA审批任务ID）、`processCode`（审批模板唯一编码）、`businessId`（流程实例业务编号ID）、`processInstanceId`（流程实例ID）等。
6. 调用[管理员批量转交指定员工的待处理任务](0538-api-premiumredirecttasksbymanager.md)，由管理员将管理员查询指定员工的待处理任务列表接口返回的任务批量转交给组织内其他在职人员处理。

   ```
   public void getPremiumRedirectTasksByManager() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     PremiumRedirectTasksByManagerHeaders premiumQueryTodoTasksByManagerHeaders = new PremiumRedirectTasksByManagerHeaders();
     premiumQueryTodoTasksByManagerHeaders.xAcsDingtalkAccessToken = "<your access token>";
     PremiumRedirectTasksByManagerRequest premiumRedirectTasksByManagerRequest = new PremiumRedirectTasksByManagerRequest()
       .setTransfereeUserId("staffId-A")
       .setHandoverUserId("staffId-B")
       .setManagerUserId("manager-12")
       .setTaskIds(java.util.Arrays.asList(
         123456L
       ));
     try {
       PremiumRedirectTasksByManagerResponse premiumRedirectTasksByManagerWithOptions = client.premiumRedirectTasksByManagerWithOptions(premiumRedirectTasksByManagerRequest, premiumQueryTodoTasksByManagerHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `transfereeUserId`：原操作人 userId，支持在职人员和已离职人员。
   - `handoverUserId`：新处理人 userId（被转交人，仅支持在职人员）。
   - `managerUserId`：管理员userId。
   - `taskIds`：转交的任务Id，即taskId。

   **返回字段：**

   - `taskId`：待处理任务id。

**实施完成检查清单**

- ✅ 应用已完成创建并获取Client ID和Client Secret。
- ✅ 已申请`Workflow.Instance.Write`、`Premium.Workflow.ReadWrite.All`、`qyapi_aflow`权限。
- ✅ accessToken获取成功且缓存策略已配置。
- ✅ 自有OA审批任务同步接口调用成功。
- ✅ 官方OA审批实例发起接口调用成功。
- ✅ 审批中心列表查询接口调用成功。
- ✅ 批量同意或拒绝审批任务接口调用成功。
- ✅ 审批实例回调事件注册并正常接收。
- ✅ 自建审批中心前端列表展示和批量操作功能已实现。
- ✅ 官方/自有审批任务按processType区分处理逻辑正确。
- ✅ 权限过滤生效，不同角色用户看到差异化审批任务。

## 常见问题（FAQ）

- **Q：批量同意或拒绝审批任务接口支持的最大任务数量是多少？**

  单次批量操作最多支持10个任务。若待处理任务超过10条，建议分批调用，每批不超过10条，避免超时或限流。
- **Q：processType参数如何区分官方OA审批和自有OA审批？**

  查询审批中心列表接口返回的每个任务对象中包含`processType`字段，值为0表示官方OA审批，值为1表示自有OA审批。批量处理时需根据该字段分别调用对应的更新接口。
