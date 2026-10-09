---
title: "自有OA审批：三方流程与页面对接"
source_url: "https://open.dingtalk.com/document/development/use-three-party-process-and-page-docking"
namespace: "development"
slug: "use-three-party-process-and-page-docking"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 标准版 > 自有OA审批：三方流程与页面对接"
doc_id: "jRJBkTCOOK"
updated_at: "2026-10-09 14:27:07"
---

> Source: https://open.dingtalk.com/document/development/use-three-party-process-and-page-docking
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 标准版 > 自有OA审批：三方流程与页面对接
> Updated: 2026-10-09 14:27:07

# 自有OA审批：三方流程与页面对接

## 概述

本文档展示了如何创建一个企业内部应用，使用钉钉OA审批流程中心提供的API，将自有业务系统的审批流程和页面集成到钉钉端内。通过创建/更新/删除三方审批模板、创建/更新审批实例、同步审批待办任务等API，实现在钉钉端内打开业务系统详情页进行审批的场景。

### 方案背景

企业自研或采购的第三方OA系统通常拥有独立的审批流程和页面，员工需要在多个系统间切换处理审批，导致操作割裂、效率低下。通过将自有审批流程对接到钉钉OA审批中心，用户可在钉钉端内打开业务系统页面审批，享受一站式体验。

企业在日常运营中常面临以下痛点：

- **审批入口分散：** 员工需要在多个系统中分别处理审批，钉钉内的待办提醒无法覆盖自有系统的审批任务，容易遗漏。
- **审批体验不一致：** 自有系统的审批页面与钉钉风格不统一，用户操作习惯割裂，学习成本高。
- **待办消息触达率低：** 自有系统的审批通知依赖邮件或短信，时效性差，无法利用钉钉的消息推送和待办中心能力。
- **审批数据孤岛：** 审批状态、处理记录等数据分散在各系统中，管理层难以在钉钉内统一查看审批进展。

### 核心价值

本方案提供三方审批系统与钉钉端内页面对接解决方案，通过调用钉钉开放平台的审批流程中心API，实现审批数据的双向同步。

- **审批模板同步：** 将自有系统的审批表单模板同步至钉钉，用户在钉钉OA审批管理后台即可查看和管理三方审批模板。
- **审批实例联动：** 在自有系统发起审批后，自动在钉钉中创建对应的审批实例，用户可在钉钉审批中心的四大列表（待处理、已处理、已发起、我收到的）中查看和操作。
- **待办任务推送：** 审批节点信息同步至钉钉后，自动生成钉钉待办任务，复用钉钉统一的待办提醒和消息推送能力。
- **审批状态回传：** 在钉钉中完成审批操作后，可将审批结果（同意、拒绝等）回传至自有系统，保持两端数据一致。

### 适用场景

本方案适用于以下典型业务场景：

- **ERP系统采购审批对接：** 企业在ERP系统中发起采购申请后，自动同步至钉钉端内，审批人在钉钉内完成审批，结果回传至ERP系统更新采购单状态。
- **HR系统请假审批联动：** HR系统中的请假申请同步至钉钉，员工在钉钉待办中心收到提醒并处理，审批结果自动更新至HR考勤模块。
- **项目管理平台费用报销对接：** 项目管理系统中的费用报销流程接入钉钉审批中心，项目经理在钉钉内审批，报销数据同步回项目预算模块。
- **CRM系统合同审批协同：** CRM系统中的合同审批流程同步至钉钉，销售团队在钉钉内完成多级审批，合同状态实时更新回CRM系统。

## 典型业务场景

### 场景一：中集瑞江多业务系统审批统一接入钉钉

#### 痛点分析

中集瑞江作为中集集团信息化自研试点中心，内部自研了MES、IOT、SRM等十几个独立运作的业务系统，各系统独立承载特定职能数据和工作流程。这种高度专业化分工的模式在提升单点业务效率的同时，也导致了企业内部信息流的碎片化与断裂问题：

- 员工需要在十几个系统中分别处理审批任务，操作繁琐且容易遗漏紧急审批。
- 各系统的审批页面风格不统一，用户操作习惯割裂，学习成本高。
- 审批通知依赖各系统内部消息，无法利用钉钉的统一待办提醒和消息推送能力。
- 管理层无法在钉钉内统一查看所有审批进展，需要分别登录多个系统查询。

#### 价值验证

- **自动化流程**

  ![中集瑞江多系统审批接入场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7227251971/p1104583.png)
- **关键优势**

  - **多系统审批统一接入：** MES/IOT/SRM等十几个独立系统的审批流程、待办事项及关键工作通知全部汇聚至钉钉端内统一处理。
  - **数据互通高效协同：** 打破系统间信息孤岛，实现跨系统数据共享与流程自动化，增强组织整体响应能力。
  - **审批体验全面升级：** 员工从"登录多个系统逐一处理"变为"打开钉钉一键处理"，操作复杂度大幅降低，审批响应时间显著缩短。

完整案例详情：[中集瑞江数字化转型案例](https://page.dingtalk.com/wow/tianyuan/act/toufang?wh_showError=true&caseId=NTMzNg==)

### 场景二：HR请假审批与钉钉考勤联动

#### 痛点分析

HR系统独立管理请假审批，但考勤打卡数据在钉钉中，两套系统数据不互通，员工请假后仍需手动在钉钉提交补卡申请，HR需跨系统核对请假与考勤记录。

#### 价值验证

- **自动化流程**

  ![制造业生产工单审批场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7227251971/p1104584.png)
- **关键优势**

  - **生产工单审批集成：** MES/ERP/QMS三套系统的工单审批节点统一接入钉钉待办列表，审批人无需跨系统切换。
  - **审批流程实时可视：** 钉钉端内展示聚合了三系统的完整工单数据（含物料清单、质检要求、历史工单数据），审批进度一目了然。
  - **数据同步全链路：** 审批结果实时回写原业务系统，驳回时批量取消下游待办，确保两端数据一致且可追溯。

## 实施指南

### 技术架构

本方案通过以下5个核心技术组件实现企业自有审批系统与钉钉OA审批中心的无缝对接：

- **身份鉴权层：** 基于钉钉开放平台OAuth2.0协议，通过应用凭证获取访问令牌，为所有接口调用提供统一的身份验证凭证，确保接口调用的安全性和合法性。
- **审批模板管理层：** 将自有审批模板同步至钉钉OA审批中心，获取全局唯一的模板编码作为标识，支持模板的创建、更新和删除操作，实现审批表单结构的云端统一管理。
- **审批实例引擎：** 在钉钉端创建审批实例，生成实例唯一标识，承载具体的审批业务数据（如申请人、审批内容、附件等），支撑完整的审批生命周期管理。
- **待办任务同步层：** 将审批任务批量同步至钉钉流程中心，生成任务标识并与钉钉用户绑定，使审批人可在钉钉待办列表中统一查看和处理来自多个业务系统的审批任务。
- **状态双向同步层：** 实现审批状态的双向同步，用户在钉钉端完成审批后，状态实时回写至业务系统；业务系统主动终止或完成审批时，钉钉端任务状态同步更新，确保两端数据一致性。

### 前置条件

- **应用准备**：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Form.Read`（工作流模板读权限）可选
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Workflow.Instance.Read`（工作流实例读权限）
  - `qyapi_aflow`（审批流数据管理权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请审批相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端审批相关API。

1. 调用新版服务端API-[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，获取模板的唯一编码`processCode`。
2. 如果没有保存`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。
3. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
4. 根据模板编码`processCode`，调用新版服务端API-[创建实例](0513-create-a-ticket-approval-instance.md)接口发起审批实例，获取审批实例`processInstanceId`。
5. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
6. 根据审批实例`processInstanceId`和待办事项列表tasks，调用[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。
7. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
8. 根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
9. 根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0514-update-instance-status.md)或 [批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。
10. 最后，若需要对审批模板数据进行清理，可以调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

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

   - `Workflow.Form.Write`（工作流模板写权限）—— 用于创建、更新、删除审批模板。
   - `Workflow.Form.Read`（工作流模板读权限）—— 用户获取模板Code，可选。
   - `Workflow.Instance.Write`（工作流实例写权限）—— 用于创建审批实例、更新实例状态。
   - `Workflow.Instance.Read`（工作流实例读权限）—— 用于查询审批任务和实例信息。
   - `qyapi_aflow`（审批流数据管理权限）—— 用于审批流程数据综合管理。

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

### 步骤四：核心API调用

1. **创建或更新审批模板**：调用新版服务端API-[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > 该场景下无需设置processFeatureConfig流程中心集成相关配置，默认会以打开业务系统详情页方式进行审批。

   ```
   public void  saveProcess() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     SaveProcessHeaders saveProcessHeaders = new SaveProcessHeaders();
     saveProcessHeaders.xAcsDingtalkAccessToken = "accessToken";

     // 1. 单行输入控件
     FormComponentProps formComponentProps1 = new FormComponentProps()
       .setComponentId("TextField-abcd")
       .setPlaceholder("请输入")
       .setLabel("单行输入")
       .setRequired(true);
     FormComponent formComponent1 = new FormComponent()
       .setComponentType("TextField")
       .setProps(formComponentProps1);
     // 2. 多行输入控件
     FormComponentProps formComponentProps2 = new FormComponentProps()
       .setComponentId("TextareaField-abcd")
       .setPlaceholder("请输入")
       .setLabel("多行输入")
       .setRequired(true);
     FormComponent formComponent2 = new FormComponent()
       .setComponentType("TextareaField")
       .setProps(formComponentProps2);
     // 3. 数字输入控件
     FormComponentProps formComponentProps3 = new FormComponentProps()
       .setComponentId("NumberField-abcd")
       .setPlaceholder("请输入")
       .setLabel("数字输入")
       .setUnit("元")
       .setRequired(true);
     FormComponent formComponent3 = new FormComponent()
       .setComponentType("NumberField")
       .setProps(formComponentProps3);
     // 4. 单选控件
     SelectOption option1 = new SelectOption();
     option1.setKey("option1");
     option1.setValue("选项1");
     SelectOption option2 = new SelectOption();
     option2.setKey("option2");
     option2.setValue("选项2");
     FormComponentProps formComponentProps4 = new FormComponentProps()
       .setComponentId("DDSelectField-abcd")
       .setPlaceholder("请选择")
       .setLabel("单选")
       .setBizAlias("staff_type")
       .setOptions(java.util.Arrays.asList(option1, option2))
       .setRequired(true);
     FormComponent formComponent4 = new FormComponent()
       .setComponentType("DDSelectField")
       .setProps(formComponentProps4);

     // 5. 多选控件
     SelectOption option3 = new SelectOption();
     option3.setKey("option1");
     option3.setValue("选项1");
     SelectOption option4 = new SelectOption();
     option4.setKey("option2");
     option4.setValue("选项2");
     FormComponentProps formComponentProps5 = new FormComponentProps()
       .setComponentId("DDMultiSelectField-abcd")
       .setPlaceholder("请选择")
       .setLabel("多选")
       .setOptions(java.util.Arrays.asList(option3, option4))
       .setRequired(true);
           FormComponent formComponent5 = new FormComponent()
                   .setComponentType("DDMultiSelectField")
                   .setProps(formComponentProps5);

           // 6. 日期控件
           FormComponentProps formComponentProps6 = new FormComponentProps()
                   .setComponentId("DDDateField-abcd")
                   .setPlaceholder("请选择")
                   .setLabel("日期")
                   .setUnit("小时")
                   .setFormat("yyyy-MM-dd HH:mm")
                   .setRequired(true);
           FormComponent formComponent6 = new FormComponent()
                   .setComponentType("DDDateField")
                   .setProps(formComponentProps6);

           // 7. 时间区间控件
           FormComponentProps formComponentProps7 = new FormComponentProps()
                   .setComponentId("DDDateRangeField-abcd")
                   .setPlaceholder("请选择")
                   .setLabel("[\"开始时间\",\"结束时间\"]")
                   .setUnit("小时")
                   .setFormat("yyyy-MM-dd HH:mm")
                   .setRequired(true);
           FormComponent formComponent7 = new FormComponent()
                   .setComponentType("DDDateRangeField")
                   .setProps(formComponentProps7);

           // 8. 文字说明控件
           FormComponentProps formComponentProps8 = new FormComponentProps()
                   .setComponentId("TextNote-abcd")
                   .setLabel("说明")
                   .setContent("详细说明内容")
                   .setLink("https://www.dingtalk.com/")
                   .setPrint("0")
                   .setRequired(false);
           FormComponent formComponent8 = new FormComponent()
                   .setComponentType("TextNote")
                   .setProps(formComponentProps8);

           // 10. 图片控件
           FormComponentProps formComponentProps10 = new FormComponentProps()
                   .setComponentId("DDPhotoField-abcd")
                   .setLabel("图片");
           FormComponent formComponent10 = new FormComponent()
                   .setComponentType("DDPhotoField")
                   .setProps(formComponentProps10);

           // 11. 金额控件
           FormComponentProps formComponentProps11 = new FormComponentProps()
                   .setComponentId("MoneyField-abcd")
                   .setUpper("0")
                   .setPlaceholder("请输入金额")
                   .setLabel("奖金（元）");
           FormComponent formComponent11 = new FormComponent()
                   .setComponentType("MoneyField")
                   .setProps(formComponentProps11);

           // 13. 附件控件
           FormComponentProps formComponentProps13 = new FormComponentProps()
                   .setComponentId("DDAttachment-abcd")
                   .setLabel("附件");
           FormComponent formComponent13 = new FormComponent()
                   .setComponentType("DDAttachment")
                   .setProps(formComponentProps13);

           // 14. 联系人控件
           FormComponentProps formComponentProps14 = new FormComponentProps()
                   .setComponentId("InnerContactField-abcd")
                   .setLabel("联系人")
                   .setChoice("1");
           FormComponent formComponent14 = new FormComponent()
                   .setComponentType("InnerContactField")
                   .setProps(formComponentProps14);

           // 15. 部门控件
           FormComponentProps formComponentProps15 = new FormComponentProps()
                   .setComponentId("DepartmentField-abcd")
                   .setLabel("部门")
                   .setMultiple(false);
           FormComponent formComponent15 = new FormComponent()
                   .setComponentType("DepartmentField")
                   .setProps(formComponentProps15);

           // 16. 关联审批单控件
           AvaliableTemplate template = new AvaliableTemplate();
           template.setName("出差申请单");
           template.setProcessCode("出差申请单的ProcessCode");
           FormComponentProps formComponentProps16 = new FormComponentProps()
                   .setComponentId("RelateField-abcd")
                   .setLabel("关联审批单")
                   .setAvailableTemplates(java.util.Arrays.asList(template));
           FormComponent formComponent16 = new FormComponent()
                   .setComponentType("RelateField")
                   .setProps(formComponentProps16);

           // 17. 省市区控件
           FormComponentProps formComponentProps17 = new FormComponentProps()
                   .setComponentId("AddressField-abcd")
                   .setLabel("省市区")
                   .setPlaceholder("请选择")
                   .setAddressModel("city");
           FormComponent formComponent17 = new FormComponent()
                   .setComponentType("AddressField")
                   .setProps(formComponentProps17);

           // 18. 评分控件
           FormComponentProps formComponentProps18 = new FormComponentProps()
                   .setComponentId("StarRatingField-abcd")
                   .setLabel("请输入")
                   .setLimit(5);
           FormComponent formComponent18 = new FormComponent()
                   .setComponentType("StarRatingField")
                   .setProps(formComponentProps18);        
                         
           SaveProcessRequestProcessFeatureConfigFeatures features1 = new SaveProcessRequestProcessFeatureConfigFeatures()
               .setName("TASK_EXECUTE")
               .setRunType("REDIRECT")
               .setPcUrl("https://www.dingtalk.com")
               .setMobileUrl("https://www.dingtalk.com");

         	SaveProcessRequestProcessFeatureConfig processFeatureConfig = new SaveProcessRequestProcessFeatureConfig()
           		.setFeatures(java.util.Arrays.asList(features1));
           
           SaveProcessRequest saveProcessRequest = new SaveProcessRequest()
                   .setName("使用三方流程和页面对接钉钉OA")
                   .setDescription("钉钉OA审批支持将外部系统（企业自研或采购的第三方系统）的审批任务推送到钉钉审批应用，用户在钉钉审批中即可统一查看和处理所有审批、享受一站式的审批体验。")
                   .setFormComponents(java.util.Arrays.asList(
                           formComponent1, formComponent2, formComponent3, formComponent4, formComponent5,
                           formComponent6, formComponent7, formComponent8, formComponent10,
                           formComponent11, formComponent13, formComponent14, formComponent15,
                           formComponent16, formComponent17, formComponentProps18
                   ))
                   .setProcessFeatureConfig(processFeatureConfig);
           try {
               SaveProcessResponse saveProcessResponse = client.saveProcessWithOptions(saveProcessRequest, saveProcessHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(saveProcessResponse.getBody()));
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

   **请求参数****：**

   - `name`：表单模板名称，最大长度200字符。
   - `description`：表单模板描述，最大长度300字符。
   - `formComponents`：表单控件列表，单一表单最大组件数不超过200。
   - `processCode`：更新时指定，未填写表示新建。

   **返回字段：**

   - `processCode`：审批模板的唯一编码，后续所有操作均需使用此编码。
   > **[!NOTE]**
   >
   > 若没有保存接口返回的模板编码`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。
2. **获取模板code（备选）：**如果未保存`processCode`，可调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。

   ```
   public void getProcessCodeByName() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameHeaders getProcessCodeByNameHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameHeaders();
           getProcessCodeByNameHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameRequest getProcessCodeByNameRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameRequest()
                   .setName("名称");
           try {
               GetProcessCodeByNameResponse getProcessCodeByNameResponse = client.getProcessCodeByNameWithOptions(getProcessCodeByNameRequest, getProcessCodeByNameHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(getProcessCodeByNameResponse.getBody()));
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

   - `name`：审批模板名称。

   **返回字段：**

   - `processCode`：审批模板的唯一编码。
3. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。

   ![未标题-1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7193809661/p517459.gif)
4. **同步审批实例数据到钉钉：**根据模板编码`processCode`，调用新版服务端API-[创建实例](0513-create-a-ticket-approval-instance.md)接口发起审批实例，获取审批实例`processInstanceId`。

   ```
   public void saveIntegratedInstance() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           SaveIntegratedInstanceHeaders saveIntegratedInstanceHeaders = new SaveIntegratedInstanceHeaders();
           saveIntegratedInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
     
           //1.单行输入框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues1 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户名称")
                   .setValue("小钉");

           //2.多行输入框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues2 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户描述")
                   .setValue("潜在优质客户");
     
           //3.数字输入框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues3 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("数量")
                   .setValue("100");
     
           //4.单选框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues4 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户类型")
                   .setValue("大客户");
     
           //5.多选框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues5;
           formComponentValues5 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户标签")
                   .setValue("[\"重要\",\"一般\"]")
                   .setComponentType("DDMultiSelectField");

           //6.日期组件，日期时间格式需要与创建OA审批模板中的日期控件格式一致
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues6 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("日期")
                   .setValue("2022-08-14 15:00");
     
           //7.日期区间组件，日期时间格式需要与创建OA审批模板中的时间区间控件格式一致
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues7 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("[\"客户达成意向开始时间\",\"客户达成意向结束时间\"]")
                   .setValue("[\"2022-08-14 15:00\",\"2022-08-15 15:00\"]");

           //8.文字说明组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues8 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("文字说明")
                   .setValue("详细说明内容");
       
           //10.图片组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues10 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("图片")
                   .setValue("[\"http://url1\",\"http://url2\",\"http://url3\"]");
           
     			//11.金额组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues11 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("金额（元）")
                   .setValue("100");

     			/*
           		附件控件的 value 是一个 json 数组转义为字符串形式。数组中的每个 json 对象是一个附件文件，
             	每个文件都必须包含 spaceId、fileName、fileSize、fileType 和 fileId 字段，这些字段
             	都可以通过调用钉盘的上传附件接口获取。
           */
       		//13.附件组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues13 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("附件")
                   .setValue("[{\"spaceId\": \"163xxxx658\", \"fileName\": \"2644.JPG\", \"fileSize\": \"333\", \"fileType\": \"jpg\", \"fileId\": " +
       "\"643xxxx140\"}]");    
     
     
     			//14.联系人组件，注意联系人控件需要指定extValue值，具体格式参考下面示例，其中emplId和itemId为用户userId
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues14 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("联系人")
                   .setValue(JSON.toJSONString(Arrays.asList("联系人名称")))
                   .setExtValue("[{\"name\":\"小钉\",\"emplId\":\"userid123\",\"itemId\":\"userid123\"}]");

           //15.部门组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues15 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("联系人部门")
                   .setValue("部门ID");
                               
           //16.关联审批单组件，注意关联审批单控件需要指定extValue值，具体格式参考下面示例，其中procInstId为需要关联的审批实例id
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues16 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("关联审批单")
                   .setValue(JSON.toJSONString(Arrays.asList("xxx提交的出差报销审批")))
             			.setExtValue("{\"list\":[{\"procInstId\":\"zUUgcEmeSQG-xxx\"}]}");
                               
           //17.省市区组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues17 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户地址")
                   .setValue(JSON.toJSONString(Arrays.asList("北京,北京市,朝阳区,东湖街道,xxxxxxxA座")));
                               
           //18.评分组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues18 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("评分")
                   .setValue("5");

     			//设置抄送人
          SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers notifiers0 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers()
                   .setUserid("manager001")
                   .setPosition("start");
      		
     		SaveIntegratedInstanceRequest saveIntegratedInstanceRequest = new SaveIntegratedInstanceRequest()
                   .setProcessCode("proc")
                   .setOriginatorUserId("manager1234")
                   .setFormComponentValueList(java.util.Arrays.asList(
                      formComponentValues1, formComponentValues2, formComponentValues3, formComponentValues4,
                      formComponentValues5, formComponentValues6, formComponentValues7, formComponentValues8,
                      formComponentValues10, formComponentValues11,
                      formComponentValues13,formComponentValues14,formComponentValues15, formComponentValues16, 
                      formComponentValues17, formComponentValues18
                   ))
                   .setTitle("xxx的审批")
                   .setUrl("https://www.dingtalk.com/")
                   .setNotifiers(java.util.Arrays.asList(
                       notifiers0
                   ));
           try {
               SaveIntegratedInstanceResponse saveIntegratedInstanceResponse = client.saveIntegratedInstanceWithOptions(saveIntegratedInstanceRequest, saveIntegratedInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(saveIntegratedInstanceResponse.getBody()));
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

   - `processCode`：审批模板code，可通过获取模板code接口获取。
   - `originatorUserId`：审批实例发起人的userId。
   - `formComponentValueList`：表单控件列表，最多100个元素。
   - `title`：实例标题，最大长度64字符。
   - `url`：第三方审批系统中审批单详情页地址，最大长度1024字符。

   **返回字段：**

   - `processInstanceId`：审批实例ID。
5. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
6. **创建流程中心待处理任务**：根据审批实例processInstanceId和待办事项列表tasks，调用[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口，将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。

   ```
   public void createIntegratedTask() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     			CreateIntegratedTaskHeaders createIntegratedTaskHeaders = new CreateIntegratedTaskHeaders();
           createIntegratedTaskHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks tasks0 = new CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks()
                   .setUserId("manager001")
                   .setUrl("https://www.dingtalk.com");
           CreateIntegratedTaskRequest createIntegratedTaskRequest = new CreateIntegratedTaskRequest()
                   .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                   .setActivityId("act_xxxxx")
                   .setTasks(java.util.Arrays.asList(
                       tasks0
                   ));
           try {
               CreateIntegratedTaskResponse createIntegratedTaskResponse = client.createIntegratedTaskWithOptions(createIntegratedTaskRequest, createIntegratedTaskHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(createIntegratedTaskResponse.getBody()));
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

   > **[!NOTE]**
   >
   > - 创建待处理任务后，审批单详情页中会出现同意/拒绝操作按钮，同时流程中心会把该审批任务同步生成为钉钉待办任务，复用钉钉统一待办提醒功能。
   > - **该场景下同步的审批任务将会以打开业务系统详情页方式进行审批。**

   **请求参数：**

   - `processInstanceId`：OA审批流程实例ID。
   - `activityId`：自定义审批节点ID，最大长度256字符。
   - `tasks`：任务列表，最多20个元素。
   - `userId`：用户userId。
   - `url`：待办事项跳转URL，最大长度1024字符。

   **返回字段：**

   - `taskId`：OA审批任务ID。
7. **查询OA审批任务**：创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，查询用户运行中的审批任务。

   ```
   public void  queryIntegratedTodoTask() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           QueryIntegratedTodoTaskHeaders queryIntegratedTodoTaskHeaders = new QueryIntegratedTodoTaskHeaders();
           queryIntegratedTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
           QueryIntegratedTodoTaskRequest queryIntegratedTodoTaskRequest = new QueryIntegratedTodoTaskRequest()
                   .setUserId("manager001")
                   .setPageSize(10)
                   .setPageNumber(1)
                   .setCreateBefore(1660036833411L);
           try {
               QueryIntegratedTodoTaskResponse queryIntegratedTodoTaskResponse = client.queryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryIntegratedTodoTaskResponse.getBody()));
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
   - `userId`：用户userId。
   - `status`：任务状态：PENDING、COMPLETED或CANCELED。

   **返回字段：**

   - `list`：任务列表。
8. **更新流程中心任务状态**：根据审批实例`processInstanceId`和审批待办任务taskId，完成待办状态的更新或将审批实例下正在运行中的待办事项设置为CANCELED。

   - 调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

     ```
     public void  updateIntegratedTask() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       			UpdateIntegratedTaskHeaders updateIntegratedTaskHeaders = new UpdateIntegratedTaskHeaders();
             updateIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
             UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks tasks0 = new UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks()
                     .setTaskId(1234567L)
                     .setStatus("COMPLETED")
                     .setResult("AGREE");
             UpdateIntegratedTaskRequest updateIntegratedTaskRequest = new UpdateIntegratedTaskRequest()
                     .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                     .setTasks(java.util.Arrays.asList(
                         tasks0
                     ));
             try {
                 UpdateIntegratedTaskResponse updateIntegratedTaskResponse = client.updateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateIntegratedTaskResponse.getBody()));
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
     - `tasks`：OA审批任务列表，最多20个。
     - `taskId`：OA审批任务ID。
     - `status`：更新为目标任务状态：CANCELED表示撤销，COMPLETED表示完成。
     - `result`：任务结果：AGREE表示同意，REFUSE表示拒绝。
   - 在或签等场景，调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。

     ```
     public void  cancelIntegratedTask() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       			CancelIntegratedTaskHeaders cancelIntegratedTaskHeaders = new CancelIntegratedTaskHeaders();
             cancelIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
             CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new CancelIntegratedTaskRequest()
                     .setProcessInstanceId("tPr_FB_mT_xxxxxxxxx2hQ05201655306463")
                     .setActivityId("act_xxxx")
                     .setActivityIds(java.util.Arrays.asList(
                         "act_xxxx"
                     ));
             CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new UpdateIntegratedTaskRequest()
                     .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                     .setTasks(java.util.Arrays.asList(
                         tasks0
                     ));
             try {
                 CancelIntegratedTaskResponse cancelIntegratedTaskResponse = client.cancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(cancelIntegratedTaskResponse.getBody()));
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
     - `activityIds`：待办组ID列表。
9. **更新实例状态**：根据审批实例`processInstanceId`和实例状态status、实例结果result等，更新实例状态。

   - 调用[更新实例状态](0514-update-instance-status.md)，更新实例状态。

     ```
     public void  updateProcessInstance() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       			com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceHeaders updateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceHeaders();
             updateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
             com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers()
                     .setUserId("001");
             com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest updateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest()
                     .setProcessInstanceId("proc")
                     .setStatus("COMPLETED")
                     .setResult("agree")
                     .setNotifiers(java.util.Arrays.asList(
                         notifiers0
                     ));
             try {
                 UpdateProcessInstanceResponse updateProcessInstanceResponse = client.updateProcessInstanceWithOptions(updateProcessInstanceRequest, updateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateProcessInstanceResponse.getBody()));
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
     - `status`：实例状态：COMPLETED表示结束审批流，TERMINATED表示终止审批流。
     - `result`：实例结果：agree表示同意，refuse表示拒绝。
     - `notifiers`：抄送人userId列表，最多30个。
   - 调用[批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md)接口，批量更新实例状态。

     ```
     public void  batchUpdateProcessInstances() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       			com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceHeaders batchUpdateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceHeaders();
             batchUpdateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
             com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers updateProcessInstanceRequests0Notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers()
                     .setUserId("001");
             com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests updateProcessInstanceRequests0 = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests()
                     .setProcessInstanceId("EF6YJL35")
                     .setStatus("COMPLETED")
                     .setResult("agree")
                     .setNotifiers(java.util.Arrays.asList(
                         updateProcessInstanceRequests0Notifiers0
                     ));
             com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest batchUpdateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest()
                     .setUpdateProcessInstanceRequests(java.util.Arrays.asList(
                         updateProcessInstanceRequests0
                     ));
             try {
                 BatchUpdateProcessInstanceResponse batchUpdateProcessInstanceResponse = client.batchUpdateProcessInstanceWithOptions(batchUpdateProcessInstanceRequest, batchUpdateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
                 System.out.println(JSON.toJSONString(batchUpdateProcessInstanceResponse.getBody()));
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

     - `updateProcessInstanceRequests`：实例列表，最多50个。
     - `processInstanceId`：实例ID。
     - `status`：实例状态：COMPLETED表示结束审批流，TERMINATED表示终止审批流。
     - `result`：实例结果：agree表示同意，refuse表示拒绝。
10. **删除审批模板**：若需要对审批模板数据进行清理，调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

    ```
    public void  deleteProcess() throws Exception {
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
                DeleteProcessResponse deleteProcessResponse = client.deleteProcessWithOptions(deleteProcessRequest, deleteProcessHeaders, new RuntimeOptions());
                System.out.println(JSON.toJSONString(deleteProcessResponse.getBody()));
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

    - `processCode`：审批模板code。

    **返回字段：**

    - `processCode`：模板code。

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ OA审批相关权限申请成功（Workflow.Form.Write、Workflow.Instance.Write、Workflow.Instance.Read、qyapi\_aflow）。
- ✅ accessToken获取成功。
- ✅ 审批模板创建成功，获取processCode。
- ✅ 审批实例创建成功，获取processInstanceId。
- ✅ 待处理任务创建成功，审批单在钉钉中可见。
- ✅ 审批任务查询成功，返回正确的任务列表。
- ✅ 任务状态更新成功，审批结果同步至自有系统。
- ✅ 实例状态更新成功，审批流程正常结束。
- ✅ 模板删除功能验证通过（可选）。

## **常见问题（FAQ）**

- **Q1：创建审批模板时必填哪些参数？**

  A：必填参数包括：

  - `name`：审批模板名称。
  - `formComponents`：表单控件列表，至少包含一个控件。
  - 可选参数包括`description`（模板描述）等。
- **Q2：如何获取processCode？**

  A：有两种方式：

  - 调用创建或更新审批模板接口后，从返回结果中获取`result.processCode`。
  - 如果未保存processCode，可调用获取模板code接口，根据模板名称查询。
- **Q3：创建待处理任务后，钉钉中会有什么变化？**

  A：创建待处理任务后：

  1. 审批单详情页中会出现同意/拒绝操作按钮。
  2. 流程中心会把该审批任务同步生成为钉钉待办任务。
  3. 审批人可在钉钉待办中心看到该审批提醒。
- **Q4：如何同步待办任务数据？**

  A：通过以下步骤同步待办任务：

  1. 调用创建流程中心待处理任务接口，将三方系统的审批节点信息同步至钉钉。
  2. 调用查询OA审批任务接口，确认任务已正确同步。
  3. 当审批状态变更时，调用更新流程中心任务状态接口同步最新状态。
- **Q5：钉钉开放平台需要申请哪些权限？**

  A：对接OA审批流程中心需要申请以下权限：

  | **权限点code** | **权限点名称** | **用途说明** |
  | --- | --- | --- |
  | Workflow.Form.Write | 工作流模板写权限 | 创建、更新、删除审批模板 |
  | Workflow.Instance.Write | 工作流实例写权限 | 创建审批实例、更新实例状态 |
  | Workflow.Instance.Read | 工作流实例读权限 | 查询审批任务和实例信息 |
  | qyapi\_aflow | 审批流数据管理权限 | 审批流程数据综合管理 |

  不同业务场景可能需要不同的权限组合，请根据实际需求申请。
