---
title: "OA审批流接入：发起与撤销审批实例"
source_url: "https://open.dingtalk.com/document/development/new-version-of-initiate-and-cancel-approval-flow"
namespace: "development"
slug: "new-version-of-initiate-and-cancel-approval-flow"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 标准版 > OA审批流接入：发起与撤销审批实例"
doc_id: "s7yjG9gPJc"
updated_at: "2026-10-12 18:04:41"
---

> Source: https://open.dingtalk.com/document/development/new-version-of-initiate-and-cancel-approval-flow
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 标准版 > OA审批流接入：发起与撤销审批实例
> Updated: 2026-10-12 18:04:41

# OA审批流接入：发起与撤销审批实例

## **概述**

本方案提供一套完整的钉钉OA审批流服务端集成解决方案，通过调用钉钉开放平台新版OA审批相关API，实现在业务系统中直接发起审批实例、查询审批详情、转交审批任务及撤销审批实例等功能，支持将自有审批流程无缝接入钉钉统一审批中心。

### **方案背景**

企业自研或采购的业务系统通常拥有独立的审批流程和页面，员工需要在多个系统间切换处理审批，导致操作割裂、效率低下。通过将自有审批流程对接到钉钉OA审批中心，用户可在钉钉统一入口查看和处理所有审批，享受一站式体验。

- **多系统切换繁琐：** 员工需在业务系统和钉钉之间反复切换，操作路径冗长且容易遗漏紧急审批。
- **审批状态不同步：** 业务系统与钉钉端数据不一致，导致审批进度难以实时追踪和管理。
- **审批流程分散：** 管理层无法在钉钉内统一查看所有审批进展，需分别登录多个系统查询。
- **消息通知滞后：** 审批通知依赖邮件或线下沟通，无法利用钉钉的统一待办提醒和消息推送能力。

### **核心价值**

本方案通过复用钉钉官方OA审批的流程引擎和表单组件能力，将业务系统的审批流程无缝集成至钉钉端内，实现审批操作的统一管理和高效协同。

- **统一审批入口：** 用户在钉钉审批列表中即可查看和处理所有自有系统审批，减少系统切换成本。
- **低改造成本：** 只需调用少量API即可完成对接，无需重构原有业务流程和页面逻辑。
- **实时状态同步：** 审批结果实时回写业务系统，确保两端数据一致且可追溯。
- **消息即时触达：** 借助钉钉待办提醒和消息通知能力，审批任务第一时间推送至审批人。

### **适用场景**

以下典型场景适合采用本方案进行审批流程集成：

- 企业自研CRM/ERP/OA等业务系统需要与钉钉审批中心打通。
- 连锁零售门店运营审批（如装修申请、促销活动审批）。
- 制造业生产工单流转审批（如质检报告、物料申请）。
- 人力资源相关审批（如请假、报销、入职离职流程）。

## **典型业务场景**

### **场景一：CRM客户跟进审批**

#### 痛点分析

某科技企业使用自研CRM系统管理客户跟进流程，销售人员录入潜在客户信息后需提交主管审批才能分配公海资源或启动商务谈判。原有流程存在以下问题：

- **商机响应滞后：** 销售线索录入后需等待主管线下签字确认，平均延迟2-3天，导致高意向客户被竞品抢先接触。
- **客户信息不完整：** 审批人仅能看到客户名称和联系方式，无法在钉钉内查看历史沟通记录、需求描述和竞品对比分析，难以做出准确判断。
- **审批责任模糊：** 多人会签时缺乏明确的审批顺序和时限要求，容易出现互相推诿或重复审批，延长决策周期。
- **数据孤岛严重：** CRM中的客户状态与钉钉审批进度不同步，销售无法实时获知审批结果，需反复电话或邮件询问主管。

#### 价值验证

- **自动化流程**

  ![CRM客户跟进审批场景图_20261010_103655](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1849971971/p1104961.png)
- **关键优势**

  - **客户信息一键审批：** CRM系统录入客户后自动创建钉钉审批实例，审批人在钉钉端内直接查看客户详情并完成操作，无需跨系统切换。
  - **审批流程实时可视：** 钉钉端内展示完整的客户数据（含联系方式、需求描述、历史跟进记录），审批进度一目了然，支持评论和催办。
  - **数据同步全链路：** 审批结果实时回写CRM系统，驳回时自动取消下游待办，确保两端数据一致且可追溯。

### **场景二：制造业生产工单审批**

#### 痛点分析

某制造企业自研MES系统管理生产工单流转，涉及多道工序审批（如首件检验、工序交接、成品入库）。原有流程依赖纸质单据和班组长口头确认，存在以下问题：

- **审批链路冗长：** 工单需经班组长→质检员→车间主任三级审批，纸质单据传递慢，紧急插单难以快速响应。
- **质检数据分散：** 检验报告以PDF或照片形式存储在本地文件夹，审批人无法在钉钉内直接查看完整质检记录和历史工单对比。
- **产线协同困难：** 上下游工序间缺乏实时状态同步，上道工序未审批通过时，下道工序仍可能误开工，造成返工浪费。
- **追溯成本高昂：** 出现质量问题时，需人工翻阅纸质单据查找责任人和审批节点，耗时且易遗漏关键信息。

#### 价值验证

- **自动化流程**

  ![制造业生产工单审批场景图_20260930_172820](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1849971971/p1104962.png)
- **关键优势**

  - **生产工单审批集成：** MES系统发起工单审批时自动创建钉钉审批实例，审批人在钉钉端内直接查看工单详情并完成操作，无需跨系统切换。
  - **审批流程实时可视：** 钉钉端内展示完整的工单数据（含物料清单、质检要求、历史工单），审批进度一目了然，支持评论和催办。
  - **数据同步全链路：** 审批结果实时回写MES系统，驳回时自动取消下游待办，确保两端数据一致且可追溯，审批时效提升60%以上。

## 实施指南

### 技术架构

本方案的技术架构包含以下核心组件：

- **身份鉴权层**：负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **模板管理层**：负责审批表单模板的创建和更新，定义审批流程的结构和字段。
- **实例执行层**：负责审批实例的发起、查询、转交和撤销等操作，驱动审批流程的执行。
- **事件回调层**：负责接收审批任务和实例的状态变更事件，实现业务系统与钉钉平台的双向同步。

### **前置条件**

- **应用准备**：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Workflow.Instance.Read`（工作流实例读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。
2. 根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。
3. 根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情信息。
4. 根据审批实例详情信息字段参数，调用新版服务端API-[转交OA审批任务](0506-transfer-the-oa-approval-task.md)接口，实现审批实例的转交操作。
5. 查看审批后，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。

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

### 步骤四：核心API调用

1. **创建或更新审批表单模板**：调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。

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
2. **发起审批实例**：根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。

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
3. **获取单个审批实例详情**：根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情。

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
4. **转交OA审批任务**：根据审批实例详情信息字段参数，调用新版服务端API-[转交OA审批任务](0506-transfer-the-oa-approval-task.md)接口，实现审批实例的转交操作。

   > **[!NOTE]**
   >
   > 操作人userId必须是当前审批节点成员的userId信息，否则无法转交成功，

   ```
    public void tasksRedirect() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskHeaders redirectWorkflowTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskHeaders();
           redirectWorkflowTaskHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest redirectWorkflowTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest()
                   .setTaskId(76835372865L)
                   .setToUserId("014728******77041")
                   .setRemark("请帮忙审批")
                   .setOperateUserId("manager***675");
           try {
               RedirectWorkflowTaskResponse redirectWorkflowTaskResponse = client.redirectWorkflowTaskWithOptions(redirectWorkflowTaskRequest, redirectWorkflowTaskHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(redirectWorkflowTaskResponse.getBody()));
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

   - `taskId`：审批任务节点标识。
   - `toUserId`：转交目标用户的ID。
   - `operateUserId`：执行转交操作的用户ID。
   - `remark`：转交原因说明。

   **返回字段：**

   - `result`：操作结果标识。
5. **撤销审批实例**：查看审批后，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。

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

## 实施完成检查清单

- ✅应用Client ID和Client Secret已获取并妥善保管。
- ✅OA审批相关权限（模板读写、实例读写、实例读）已申请并通过。
- ✅accessToken获取接口调用成功，凭证有效期内可正常使用。
- ✅审批模板创建成功，processCode已保存至业务系统配置。
- ✅审批实例发起成功，instanceId可用于后续任务操作。
- ✅钉钉OA审批中心可查看审批实例并执行审批操作。
- ✅审批实例详情查询及任务转交功能验证通过。
- ✅审批实例撤销功能验证通过。

## **常见问题（FAQ）**

- **Q1：创建审批模板时，formComponents中的componentId有什么要求？**

  componentId在表单内必须唯一，无业务语义，用于标识控件。若需要使用业务标识，可使用bizAlias字段替代。
- **Q2：发起审批实例时，approvers中的actionType有哪些取值？**

  actionType支持NONE（单人审批）、OR（或签，任一审批人同意即通过）、AND（会签，所有审批人均需同意）等取值，具体以API文档为准。
- **Q3：如何获取未保存的processCode？**

  若未保存创建审批模板时返回的processCode，可登录钉钉OA审批管理后台查看获取，或调用获取模板code接口查询。
- **Q4：转交审批任务时，operateUserId有什么要求？**

  operateUserId必须是当前审批节点成员的userId信息，否则无法转交成功。
- **Q5：撤销审批实例后，审批状态如何同步？**

  撤销成功后，审批实例状态变更为"已终止"，可通过订阅审批实例变更回调事件实时感知状态变化。
