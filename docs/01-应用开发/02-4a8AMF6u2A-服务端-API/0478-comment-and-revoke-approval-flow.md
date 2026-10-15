---
title: "OA审批流接入：添加审批评论与终止审批"
source_url: "https://open.dingtalk.com/document/development/comment-and-revoke-approval-flow"
namespace: "development"
slug: "comment-and-revoke-approval-flow"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 标准版 > OA审批流接入：添加审批评论与终止审批"
doc_id: "bgZxXfNCbv"
updated_at: "2026-10-12 18:04:42"
---

> Source: https://open.dingtalk.com/document/development/comment-and-revoke-approval-flow
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 标准版 > OA审批流接入：添加审批评论与终止审批
> Updated: 2026-10-12 18:04:42

# OA审批流接入：添加审批评论与终止审批

## 概述

本方案提供一套完整的钉钉OA审批评论及撤销服务端集成解决方案，通过调用钉钉开放平台新版OA审批相关API，实现在业务系统中直接获取表单Schema、发起审批实例、上传附件至审批钉盘、添加带附件的审批评论及撤销审批实例等功能，支持将自有审批流程无缝接入钉钉统一审批中心。

### **方案背景**

企业自研或采购的业务系统在审批流转过程中，常需对审批实例补充说明材料（如合同扫描件、验收报告等），但缺乏统一的附件上传入口；同时，当审批提交错误或需求变更时，缺少标准化的撤销操作通道。通过将审批评论及撤销能力对接到钉钉OA审批中心，用户可在钉钉端内完成附件补充与审批终止，享受一站式体验。

- **附件补充无入口：** 审批发起人无法在业务系统外补充证明材料，导致审批信息不完整、决策依据缺失。
- **审批撤销不规范：** 错误提交的审批单依赖线下沟通撤回，缺乏系统级撤销记录与状态同步机制。
- **钉盘空间未打通：** 审批附件散落在个人钉盘或本地存储，无法与审批实例关联管理，审计追溯困难。
- **Schema确认缺失：** 发起审批前未校验表单结构，导致控件ID不匹配、数据提交失败等运行时错误。

### **核心价值**

本方案通过复用钉钉官方OA审批的钉盘空间管理与评论引擎能力，将审批附件上传、评论添加及撤销操作无缝集成至业务系统，实现审批全生命周期的闭环管理。

- **附件集中管理：** 所有审批附件统一上传至审批专属钉盘空间，与实例绑定，支持一键下载与审计追溯。
- **评论可追溯：** 带附件的审批评论永久留存，形成完整的审批沟通链路，避免信息丢失。
- **撤销标准化：** 通过API触发撤销操作，自动更新审批状态为"已终止"，并同步回调通知业务系统。
- **Schema预校验：** 发起审批前获取表单Schema，确保控件配置与模板一致，降低集成调试成本。

### **适用场景**

以下典型场景适合采用本方案进行审批评论及撤销功能集成：

- 律师事务所案件审批流程中需补充证据材料附件并添加律师评审意见。
- 教育培训机构课程变更审批，发现排课冲突后需撤销已提交的审批单重新发起。
- 医疗机构药品采购审批，需在审批过程中追加供应商资质证明文件作为评论附件。
- 建筑工程项目验收审批，发现检测数据有误后需终止当前流程并修正后重新提交。

## 典型业务场景

### **场景一：律师事务所案件审批补充证据材料**

#### **痛点分析**

某律师事务所使用自研案件管理系统处理案件审批流程，律师在提交案件立案审批后常需补充新的证据材料或法律意见书。原有流程存在以下问题：

- **证据补充无通道：** 案件立案审批发起后，律师无法通过系统向审批单追加新收集的证据文件，只能线下发送 email 给合伙人，导致审批材料不完整。
- **沟通记录分散：** 律师对案件的补充说明散落在微信、邮件等多个渠道，审批人无法在审批单内集中查看所有沟通内容，影响决策效率。
- **附件管理混乱：** 证据文件存储在个人电脑或共享网盘中，未与审批实例关联，后续审计追溯时需人工逐一查找对应关系。
- **错误审批难纠正：** 立案信息填写错误后缺乏系统化撤销机制，只能通知审批人口头驳回，缺少正式的终止记录和状态同步。

#### **价值验证**

- **自动化流程**

  ![律师事务所案件审批场景_20261010_114746](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2849971971/p1104975.png)
- **关键优势**

  - **证据附件在线补充：** 律师可通过审批评论接口随时向审批单追加证据文件，审批人在钉钉端内直接查看完整材料并作出决策。
  - **沟通链路完整留存：** 所有补充说明和附件通过评论功能永久关联至审批实例，形成完整的案件审批沟通记录，便于后续审计追溯。
  - **错误审批规范撤销：** 立案信息有误时可通过撤销接口正式终止审批流程，系统自动记录撤销原因并同步状态，避免口头沟通导致的权责不清。

### **场景二：教育培训机构课程变更审批撤销重提**

#### **痛点分析**

某教育培训机构使用自研教务系统管理课程变更审批，教务人员在提交调课申请后发现排课时间冲突或教室资源不足。原有流程存在以下问题：

- **排课冲突发现晚：** 调课审批提交后才被发现与其他课程时间重叠，但审批已进入流转环节，无法通过系统撤回修改。
- **变更信息不完整：** 审批人仅能看到调课申请表，无法在审批单内查看受影响的学员名单、教师日程和教室占用情况，难以评估变更影响。
- **撤销流程不规范：** 错误的调课申请只能通过线下通知审批人拒绝，缺乏系统级撤销记录，导致教务日志与实际状态不一致。
- **重复提交效率低：** 撤销后重新发起审批需手动填写全部表单信息，无法复用原审批单数据，增加教务人员工作负担。

#### **价值验证**

- **自动化流程**

  ![教育培训课程变更审批场景_20261010_114750](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2849971971/p1104976.png)
- **关键优势**

  - **排课冲突即时撤销：** 发现调课申请有误时可通过撤销接口立即终止审批流程，系统自动记录撤销原因，避免错误审批继续流转影响教学安排。
  - **变更影响在线评估：** 教务人员可通过评论功能向审批单补充受影响学员名单和教室调整方案，审批人在钉钉端内一站式查看所有变更信息。
  - **审批状态实时同步：** 撤销结果实时回写教务系统，确保课程表与审批状态一致，重新发起审批时可快速修正数据，减少重复录入工作量。

## 实施指南

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层** ：负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **模板管理层** ：负责审批表单模板的创建和更新，定义审批流程的结构和字段。
- **实例执行层** ：负责审批实例的发起、查询和撤销等操作，驱动审批流程的执行。
- **评论与附件层** ：负责审批钉盘空间管理和评论添加，实现审批沟通链路的闭环。

### **前置条件**

- **应用准备** ：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求** ：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Form.Read`（工作流模板读权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Workflow.Instance.Read`（工作流实例读权限）
- **开发环境** ：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备** ：下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请"OA审批"相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。
2. 根据模板编码`processCode`，调用新版服务端API-[获取表单 schema](0491-obtain-the-form-schema.md)接口获取表单模板schema，查看确认对应表单模板的schema详情信息。
3. 根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。
4. 根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情。
5. 若需要添加审批评论附件，需将文件上传至审批钉盘空间。可以获取到接口参数spaceId，fileType，fileName，fileId，fileSize。获取方式如下：

   1. 调用新版服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
   2. 调用客户端JSAPI-[获取审批钉盘空间信息](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息。
6. 获取审批钉盘空间spaceId后，可根据审批实例`instanceId`，调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口，实现审批单的添加评论操作。
7. 查看审批后，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。

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

   - `Workflow.Form.Write`（工作流模板写权限）：用于创建和更新审批表单模板
   - `Workflow.Form.Read`（工作流模板读权限）：用于获取表单schema
   - `Workflow.Instance.Write`（工作流实例写权限）：用于发起、撤销审批实例
   - `Workflow.Instance.Read`（工作流实例读权限）：用于查询审批实例详情

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

1. **创建或更新审批表单模板** ：调用新版服务端API -[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > 若没有保存接口返回的模板编码`processCode`，可通过[processCode](0475-workflow-overview.md#6fada3928c317)说明。

   ```
     public void createProcessTemplate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           FormCreateHeaders formCreateHeaders = new FormCreateHeaders();
           formCreateHeaders.xAcsDingtalkAccessToken = "accessToken";

           // 1. 单行输入控件
           FormComponentProps formComponentProps1 = new FormComponentProps()
                   .setComponentId("TextField-sys1001")
                   .setPlaceholder("请输入")
                   .setLabel("客户名称")
                   .setRequired(false);
           FormComponent formComponent1 = new FormComponent()
                   .setComponentType("TextField")
                   .setProps(formComponentProps1);
           // 2. 多行输入控件
           FormComponentProps formComponentProps2 = new FormComponentProps()
                   .setComponentId("TextareaField-sys1002")
                   .setPlaceholder("请输入")
                   .setLabel("客户描述")
                   .setRequired(false);
           FormComponent formComponent2 = new FormComponent()
                   .setComponentType("TextareaField")
                   .setProps(formComponentProps2);

           //3.多选控件
           SelectOption option3 = new SelectOption();
           option3.setKey("option1");
           option3.setValue("重要");
           SelectOption option4 = new SelectOption();
           option4.setKey("option2");
           option4.setValue("一般");
           FormComponentProps formComponentProps3 = new FormComponentProps()
                   .setComponentId("DDMultiSelectField-sys1003")
                   .setLabel("客户标签")
                   .setOptions(java.util.Arrays.asList(option3, option4));
           FormComponent formComponent3 = new FormComponent()
                   .setComponentType("DDMultiSelectField")
                   .setProps(formComponentProps3);

           //4. 时间区间控件
           FormComponentProps formComponentProps4 = new FormComponentProps()
                   .setComponentId("DDDateRangeField-sys1004")
                   .setLabel("[\"客户达成意向开始时间\",\"客户达成意向结束时间\"]")
                   .setUnit("小时")
                   .setPlaceholder("请选择对应时间")
                   .setFormat("yyyy-MM-dd HH:mm");
           FormComponent formComponent4 = new FormComponent()
                   .setComponentType("DDDateRangeField")
                   .setProps(formComponentProps4);

           //5.明细控件
           //明细子控件统计
           FormComponentProps.FormComponentPropsStatField formComponentPropsStatField2 = new FormComponentProps.FormComponentPropsStatField()
                   .setComponentId("NumberField-sysC1005")
                   .setLabel("数字输入");

           FormComponentProps.FormComponentPropsStatField formComponentPropsStatField1 = new FormComponentProps.FormComponentPropsStatField()
                   .setComponentId("CalculateField-sysC1005")
                   .setLabel("金额（元）");

           //明细子控件
           //5.1明细单行输入框
           FormComponentProps childProp1 = new FormComponentProps()
                   .setComponentId("TextField-sysC1005")
                   .setLabel("名称");
           FormComponent child1 = new FormComponent()
                   .setComponentType("TextField")
                   .setProps(childProp1);

           //5.2明细金额输入框
           FormComponentProps childProp2 = new FormComponentProps()
                   .setComponentId("MoneyField-sysC1005")
                   .setLabel("单价（元）");
           FormComponent child2 = new FormComponent()
                   .setComponentType("MoneyField")
                   .setProps(childProp2);

           //5.3明细数字输入框
           FormComponentProps childProp3 = new FormComponentProps()
                   .setComponentId("NumberField-sysC1005")
                   .setLabel("个数");
           FormComponent child3 = new FormComponent()
                   .setComponentType("NumberField")
                   .setProps(childProp3);
           //5.4计算公式组件
           JSONObject jsonObject1 = new JSONObject();
           jsonObject1.put("id", "NumberField-sysC1005");
           String s = "*";
           JSONObject jsonObject2 = new JSONObject();
           jsonObject2.put("id", "MoneyField-sysC1005");
           Object objects[] = new Object[]{jsonObject1, s, jsonObject2};
           FormComponentProps childProp4 = new FormComponentProps()
                   .setComponentId("CalculateField-sysC1005")
                   .setLabel("总计")
                   .setPlaceholder("自动计算数值")
                   .setRequired(false)
                   .setFormula(JSON.toJSONString(objects));
           FormComponent child4 = new FormComponent()
                   .setComponentType("CalculateField")
                   .setProps(childProp4);

           FormComponentProps formComponentProps5 = new FormComponentProps()
                   .setComponentId("TableField-sys1005")
                   .setTableViewMode("table")
                   .setLabel("明细")
                   .setVerticalPrint(true)
                   .setStatField(Arrays.asList(formComponentPropsStatField1, formComponentPropsStatField2));
           FormComponent formComponent5 = new FormComponent()
                   .setComponentType("TableField")
                   .setChildren(Arrays.asList(child1, child2, child3, child4))
                   .setProps(formComponentProps5);

           // 6. 联系人控件
           FormComponentProps formComponentProps6 = new FormComponentProps()
                   .setComponentId("InnerContactField-sys1006")
                   .setLabel("联系人")
                   .setPlaceholder("请选择联系人")
                   .setChoice("1");
           FormComponent formComponent6 = new FormComponent()
                   .setComponentType("InnerContactField")
                   .setProps(formComponentProps6);

           // 7. 部门控件
           FormComponentProps formComponentProps7 = new FormComponentProps()
                   .setComponentId("DepartmentField-sys1007")
                   .setLabel("联系人部门")
                   .setPlaceholder("请选择部门")
                   .setMultiple(false);
           FormComponent formComponent7 = new FormComponent()
                   .setComponentType("DepartmentField")
                   .setProps(formComponentProps7);

           // 8. 省市区控件
           FormComponentProps formComponentProps8 = new FormComponentProps()
                   .setComponentId("AddressField-sys1008")
                   .setLabel("客户地址")
                   .setPlaceholder("请选择")
                   .setAddressModel("city");
           FormComponent formComponent8 = new FormComponent()
                   .setComponentType("AddressField")
                   .setProps(formComponentProps8);

           //9.单选控件
           SelectOption selectOption1 = new SelectOption();
           selectOption1.setKey("option1");
           selectOption1.setValue("紧急");
           SelectOption selectOption2 = new SelectOption();
           selectOption2.setKey("option2");
           selectOption2.setValue("普通");
           FormComponentProps formComponentProps9 = new FormComponentProps()
                   .setComponentId("DDSelectField-sys1009")
                   .setLabel("审批需求状态")
                   .setOptions(Arrays.asList(selectOption1, selectOption2));
           FormComponent formComponent9 = new FormComponent()
                   .setComponentType("DDSelectField")
                   .setProps(formComponentProps9);

           FormCreateRequest formCreateRequest = new FormCreateRequest()
                   .setName("客户表单")
                   .setDescription("客户表单")
                   //有参数processCode时为更新模板，无参数processCode时，为创建模板，该示例为创建模板
                   //.setProcessCode("PROC-ECED8693-****-****-****-A5EE2F7E9F46")
                   .setFormComponents(java.util.Arrays.asList(
                           formComponent1, formComponent2, formComponent3, formComponent4,
                           formComponent5, formComponent6, formComponent7, formComponent8,
                           formComponent9
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

   - `name`：审批表单模板名称。
   - `description`：审批表单模板描述。
   - `formComponents`：表单控件列表，定义审批表单的结构和字段。

   **返回字段：**

   - `processCode`：审批模板唯一编码。
2. **获取表单schema**：根据模板编码`processCode`，调用新版服务端API-[获取表单 schema](0491-obtain-the-form-schema.md)接口获取表单模板schema，查看确认对应表单模板的schema详情信息。

   ```
   public void processSchemasInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeHeaders querySchemaByProcessCodeHeaders = new com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeHeaders();
           querySchemaByProcessCodeHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeRequest querySchemaByProcessCodeRequest = new com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeRequest()
                   .setProcessCode("PROC-17428B8C-6C60-xxxx-924C-64F1037AE067");
           try {
               QuerySchemaByProcessCodeResponse processSchemaWithOptions = client.querySchemaByProcessCodeWithOptions(querySchemaByProcessCodeRequest, querySchemaByProcessCodeHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(processSchemaWithOptions.getBody()));
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

   - `processCode`：审批模板唯一编码。

   **返回字段：**

   - `schemaContent`：表单模板的完整Schema结构，包含表单类型、引擎类型及状态等信息。
3. **发起审批实例** ：根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。

   ```
   public void ProcessInstances() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           StartProcessInstanceHeaders startProcessInstanceHeaders = new StartProcessInstanceHeaders();
           startProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

           //1.单行输入框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues1 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户名称")
                   .setValue("小钉");

           //2.多行输入框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues2 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户描述")
                   .setValue("潜在优质客户");

           //3.多选框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues3;
           formComponentValues3 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户标签")
                   .setValue("[\"重要\",\"一般\"]")
                   .setComponentType("DDMultiSelectField");

           //4.日期区间组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues4 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("[\"客户达成意向开始时间\",\"客户达成意向结束时间\"]")
                   .setValue("[\"2022-08-14 15:00\",\"2022-08-15 15:00\"]");

           //5.明细表格组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details1 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("名称")
                   .setValue("钉钉F2 智能视频会议一体机");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details2 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("单价（元）")
                   .setValue("29999");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details3 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("个数")
                   .setValue("1");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details4 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("名称")
                   .setValue("钉钉F1 智能视频会议一体机");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details5 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("单价（元）")
                   .setValue("4999");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details6 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("个数")
                   .setValue("5");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues5 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("明细")
                   .setValue(JSON.toJSONString(Arrays.asList(Arrays.asList(formComponentValues0Details1, formComponentValues0Details2, formComponentValues0Details3), Arrays.asList(formComponentValues0Details4, formComponentValues0Details5, formComponentValues0Details6))))
                   .setDetails(Arrays.asList(formComponentValues0Details1, formComponentValues0Details2, formComponentValues0Details3, formComponentValues0Details4, formComponentValues0Details5, formComponentValues0Details6));

           //6.联系人组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues6 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("联系人")
                   .setValue(JSON.toJSONString(Arrays.asList("联系人userId")));

           //7.部门组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues7 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("联系人部门")
                   .setValue("部门ID");
                  
           //8.省市区组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues8 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户地址")
                   .setValue(JSON.toJSONString(Arrays.asList("北京,北京市,朝阳区,东湖街道,xxxxxxxA座")));

           //9.单选框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues9 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("审批需求状态")
                   .setValue("紧急");

           //设置审批人
           //会签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers0 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("AND")
                   .setUserIds(java.util.Arrays.asList(
                           "014******77041", "0852*******284272"
                   ));
           //或签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers1 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("OR")
                   .setUserIds(java.util.Arrays.asList(
                           "014******77041", "0852*******284272"
                   ));
           StartProcessInstanceRequest startProcessInstanceRequest = new StartProcessInstanceRequest()
                   .setOriginatorUserId("发起人userId")
                   .setProcessCode("PROC-ECED8693-****-****-****-A5EE2F7E9F46")
                   .setDeptId(1L)
                   .setMicroappAgentId(118*****5L)
                   .setApprovers(java.util.Arrays.asList(
                           approvers0, approvers1
                   ))
             			//抄送人
                   .setCcList(java.util.Arrays.asList(
                           "抄送人userId"
                   ))
                   .setCcPosition("FINISH")
                   .setFormComponentValues(java.util.Arrays.asList(
                           formComponentValues1, formComponentValues2, formComponentValues3, formComponentValues4,
                           formComponentValues5, formComponentValues6, formComponentValues7, formComponentValues8,
                           formComponentValues9
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

   - `processCode`：审批模板唯一编码。
   - `originatorUserId`：发起人的用户ID。
   - `formComponentValues`：表单控件值列表，对应模板中定义的各字段。
   - `approvers`：审批人列表，指定各节点的审批人和操作方式。

   **返回字段：**

   - `instanceId`：审批实例唯一标识。
4. **获取单个审批实例详情** ：根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情。

   ```
   public void processInstancesInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders getProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders();
           getProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest getProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest()
                   .setProcessInstanceId("zRfPT*********************159");
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

   - `processInstanceId`：审批实例唯一标识。

   **返回字段：**

   - `taskId`：审批任务节点标识。
   - `status`：审批实例当前状态。
5. 若需要添加审批评论附件，需将文件上传至审批钉盘空间。

   1. 先调用新版服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。

      ```
      public void attachmentSpaceInfo() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
              com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders getAttachmentSpaceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders();
              getAttachmentSpaceHeaders.xAcsDingtalkAccessToken = "accessToken";
              com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest getAttachmentSpaceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest()
                      .setUserId("user123")
                      .setAgentId(8345000L);
              try {
                  GetAttachmentSpaceResponse attachmentSpaceWithOptions = client.getAttachmentSpaceWithOptions(getAttachmentSpaceRequest, getAttachmentSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
   2. 然后调用客户端JSAPI-[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息，本流程示例使用[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10318)实现。

      > **[!IMPORTANT]**
      >
      > 调用该方法前，需要调用[获取审批钉盘空间信息](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)进行授权操作。
6. **添加审批评论** ：获取审批钉盘空间`spaceId`后，可根据审批实例`instanceId`，调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口，实现审批单的添加评论操作。

   ```
   public void attachmentSpaceInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders getAttachmentSpaceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders();
           getAttachmentSpaceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest getAttachmentSpaceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest()
                   .setUserId("user123")
                   .setAgentId(8345000L);
           try {
               GetAttachmentSpaceResponse attachmentSpaceWithOptions = client.getAttachmentSpaceWithOptions(getAttachmentSpaceRequest, getAttachmentSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
7. **撤销审批实例**：查看审批后，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。

   ```
   public void processInstancesTerminate() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceHeaders terminateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceHeaders();
           terminateProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceRequest terminateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceRequest()
                   .setProcessInstanceId("zRfPT*********************159")
                   .setIsSystem(false)
                   .setRemark("审批单提交错误，需要撤销")
                   .setOperatingUserId("审批发起人userId");
           try {
               TerminateProcessInstanceResponse terminateProcessInstanceResponse = client.terminateProcessInstanceWithOptions(terminateProcessInstanceRequest, terminateProcessInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(terminateProcessInstanceResponse.getBody()));
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

   - `processInstanceId`：审批实例唯一标识。
   - `operatingUserId`：执行撤销操作的用户ID。
   - `remark`：撤销原因说明。

   **返回字段：**

   - `result`：操作结果标识。

**实施完成检查清单**

- ✅应用Client ID和Client Secret已获取并妥善保管。
- ✅OA审批相关权限（模板读写、实例读写、实例读）已申请并通过。
- ✅accessToken获取接口调用成功，凭证有效期内可正常使用。
- ✅审批模板创建成功，processCode已保存至业务系统配置。
- ✅表单Schema获取成功，控件结构与模板定义一致。
- ✅审批实例发起成功，instanceId可用于后续任务操作。
- ✅审批钉盘空间获取成功，spaceId及上传凭证有效。
- ✅审批评论添加成功，附件正确关联至审批实例。
- ✅审批实例撤销功能验证通过，状态同步正常。

## **常见问题（FAQ）**

- **Q1：获取表单Schema时返回403错误怎么办？**

  检查是否已申请`Workflow.Form.Read`权限，且accessToken未过期。权限申请后需等待1-2分钟生效。
- **Q2：添加审批评论时附件无法显示？**

  确认所需参数均从获取审批钉盘空间接口和客户端JSAPI正确获取，且文件已成功上传至对应钉盘空间。
- **Q3：撤销审批实例后状态未更新？**

  撤销操作异步执行，可通过订阅审批实例变更回调事件监听状态变化，或调用获取单个审批实例详情接口轮询确认。
- **Q4：能否对已撤销的审批实例再次添加评论？**

  不可以。已撤销的审批实例处于终态，不再接受任何评论或附件操作。如需补充说明，应重新发起新审批实例。
