---
title: "OA审批流接入：查询用户可见表单与待审批数量"
source_url: "https://open.dingtalk.com/document/development/user-form-and-approval-form-query"
namespace: "development"
slug: "user-form-and-approval-form-query"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 标准版 > OA审批流接入：查询用户可见表单与待审批数量"
doc_id: "OIBT32AHaY"
updated_at: "2026-10-16 09:22:56"
---

> Source: https://open.dingtalk.com/document/development/user-form-and-approval-form-query
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 标准版 > OA审批流接入：查询用户可见表单与待审批数量
> Updated: 2026-10-16 09:22:56

# OA审批流接入：查询用户可见表单与待审批数量

## **概述**

本方案通过调用钉钉OA审批新版服务端API，实现业务系统与钉钉审批能力的深度集成。开发者可在自有系统中动态查询企业可管理表单、用户可见表单及待审批数量，无需硬编码表单配置，支持审批入口的动态渲染和个性化待办提醒，适用于统一工作台、智能推荐、消息推送等多种业务场景。

### 方案背景

员工登录钉钉后需快速了解自己有哪些审批权限、可查看哪些表单以及当前有多少待处理审批，但现有OA审批体系缺乏统一的个人审批工作台视图。通过查询用户可见表单与待审批数量接口，可在钉钉端构建个性化审批仪表盘，帮助员工高效规划审批工作优先级。

企业在日常运营中常面临以下痛点：

- **审批权限不透明**： 员工不清楚自己有权查看或审批哪些表单类型，遇到新业务场景时需反复询问管理员确认权限范围，沟通成本高且响应慢。
- **待办数量不可见**： 钉钉待办中心仅展示任务列表，无法按表单类型汇总待审批数量，员工无法直观感知工作量分布，难以合理安排处理顺序。
- **跨系统审批难聚合**： 来自OA、费控、HR等不同系统的审批分散在各自入口，员工需逐一登录查看待办数量，每日重复操作耗时15分钟以上。
- **审批负载不均**： 管理者无法实时查看团队成员的待审批数量和积压情况，工作分配依赖主观判断，部分员工长期过载而另一些人闲置。

### **核心价值**

本方案的核心价值体现在以下三个方面：

- **表单列表动态获取：** 通过API实时拉取企业内所有可管理或指定用户可见的审批表单，避免在业务系统中维护静态表单配置表。
- **待办数量精准统计：** 基于用户userId精确查询其待处理审批数量，支持在业务系统首页或消息中心展示个性化待办提醒。
- **权限隔离可控：** 获取表单列表时自动遵循钉钉OA审批的权限体系，仅返回调用者有权访问的表单，保障数据安全。

### **适用场景**

本方案适用于需要在自有业务系统中动态展示审批表单入口、实时显示用户待办数量的场景，典型包括：

- **统一审批工作台：** 在业务系统首页聚合展示用户可见的所有审批表单入口及待办数量，实现一站式审批入口。
- **智能表单推荐：** 根据用户角色和部门动态过滤可见表单列表，仅展示与其职责相关的审批类型。
- **待办消息推送：** 定时轮询用户待审批数量变化，触发站内信或移动端推送通知。

## 典型业务场景

### 场景一：制造企业统一审批工作台（制造业）

#### **痛点分析**

某大型制造企业使用自研ERP系统管理生产、采购、人事等多条业务线，各业务线的审批表单分散在不同子系统中。原有流程存在以下问题：

- **表单入口分散：** 员工需在ERP、MES、HR等多个系统中分别查找对应审批表单，无法在一个页面集中发起各类审批。
- **待办感知滞后：** 审批人无法在ERP首页看到自己的待审批数量，需逐个进入各子系统查看，容易遗漏紧急审批。
- **表单配置僵化：** 新增审批类型时需手动在各子系统中添加入口链接，运维成本高且易遗漏。

#### **价值验证**

- **自动化流程**

  ![制造企业统一审批工作台场景图_20261012_102626](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8849971971/p1105101.png)
- **关键优势**

  - **表单入口一键聚合：** 员工在ERP首页即可看到所有可用审批表单，点击直接跳转钉钉端内发起审批，无需切换系统。
  - **待办数量实时刷新：** 首页顶部展示用户待审批数量徽章，每5分钟自动轮询更新，确保审批人不遗漏任何待办。
  - **权限自动适配：** 不同角色的员工看到的表单列表自动过滤，普通员工仅见请假/报销类表单，管理层额外可见采购/合同类表单，审批周期缩短40%以上。

### **场景二：高校教职工移动办公门户（教育行业）**

#### **痛点分析**

某重点大学使用自研教职工移动办公APP处理日常事务，教师需提交调课申请、科研经费报销、设备采购等多种审批。原有流程存在以下问题：

- **表单查找困难：** APP内审批入口采用固定菜单结构，新上线的审批类型需发版更新才能添加入口，响应速度慢。
- **跨校区待办遗漏：** 主校区和分校区教师的待审批通知依赖邮件推送，移动端无实时提醒，偏远校区教师平均延迟2天处理审批。
- **个性化体验差：** 所有教师看到相同的审批表单列表，行政人员频繁看到教学类表单，教授频繁看到财务类表单，干扰核心操作。

#### **价值验证**

- **自动化流程**

  ![高校教职工移动办公门户场景图_20261012_102729](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8849971971/p1105103.png)
- **关键优势**

  - **表单列表千人千面：** 教师登录后仅看到与其岗位相关的审批表单，行政岗优先显示公文流转，教学岗优先显示调课申请，减少无效浏览时间。
  - **待办提醒即时触达：** APP后台静默轮询待审批数量，超过阈值时推送本地通知，跨校区教师审批响应速度提升60%。
  - **新表单零配置上线：** 管理员在钉钉后台新建审批模板后，APP下次启动自动拉取并展示，无需发版更新。

## 实施指南

### 技术架构

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **表单查询层：** 负责调用获取企业可管理表单、用户可见表单、待审批数量等查询接口，返回结构化表单元数据。
- **权限过滤层：** 基于钉钉OA审批的权限体系，自动过滤调用者无权访问的表单，保障数据安全。
- **缓存加速层：** 对表单列表和待办数量进行短时缓存，降低API调用频率，提升前端渲染性能。

### 前置条件

- **应用准备**： 已完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)流程，获取应用 Client ID 和 Client Secret。
- **权限要求：** 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Form.Read`（工作流模板读权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Workflow.Instance.Read`（工作流实例读权限）
- **开发环境**： 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**： 下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请 OA 审批相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。
2. 创建多个审批表单模板后，可调用新版服务端API-[获取当前企业所有可管理的表单](0494-get-all-manageable-forms-for-the-current-enterprise.md)接口，获取用户在当前企业所有可管理的审批表单列表。调用本接口，userId对应的人员必须拥有该企业OA审批的权限。
3. 创建多个审批表单模板后，可调用新版服务端API-[获取指定用户可见的审批表单列表](0493-obtains-a-list-of-approval-forms-visible-to-the-specified.md)接口，获取该用户可见的审批表单列表。
4. 根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。
5. 发起多个审批实例后，可根据模板编码`processCode`，调用新版服务端API-[获取审批实例ID列表](0500-obtain-an-approval-list-of-instance-ids.md)接口，获取权限范围内的相关部门审批实例ID列表。
6. 发起多个审批实例后，也可根据用户userId，调用新版服务端API-[获取用户待审批数量](0507-queries-the-number-of-requests-to-be-approved-by-users.md)接口，获取该用户待处理的审批数量。

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

   - `Workflow.Form.Write`（工作流模板写权限）：用于创建或更新审批表单模板。
   - `Workflow.Form.Read`（工作流模板读权限）：用于获取企业可管理表单和用户可见表单列表。
   - `Workflow.Instance.Write`（工作流实例写权限）：用于发起审批实例。
   - `Workflow.Instance.Read`（工作流实例读权限）：用于获取用户待审批数量。

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

1. 创建或更新审批表单模板：调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > 若没有保存接口返回的模板编码`processCode`，可通过[processCode](0475-workflow-overview.md#6fada3928c317)说明查询。

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

   - `name`：审批表单名称。
   - `description`：表单描述信息。

   **返回字段：**

   - `processCode`：审批表单模板唯一编码。
2. **获取当前企业所有可管理的表单**：创建多个审批表单模板后，可调用新版服务端API-[获取当前企业所有可管理的表单](0494-get-all-manageable-forms-for-the-current-enterprise.md)接口，获取用户在当前企业所有可管理的审批表单列表。

   > **[!NOTE]**
   >
   > 调用本接口，userId对应的人员必须拥有该企业OA审批的权限。

   ```
   public void processManagementTemplates() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdHeaders getManageProcessByStaffIdHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdHeaders();
           getManageProcessByStaffIdHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdRequest getManageProcessByStaffIdRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdRequest()
                   .setUserId("manager7078");
           try {
               GetManageProcessByStaffIdResponse getManageProcessByStaffIdResponse = client.getManageProcessByStaffIdWithOptions(getManageProcessByStaffIdRequest, getManageProcessByStaffIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
               System.out.println(JSON.toJSONString(getManageProcessByStaffIdResponse.getBody()));
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

   - `userId`：查询人员的userid，该人员必须拥有企业OA审批权限。

   **返回字段：**

   - `result`：可管理审批表单列表，含processCode、iconName、iconUrl、flowTitle等字段。
3. **获取指定用户可见的审批表单列表**：调用新版服务端API-[获取指定用户可见的审批表单列表](0493-obtains-a-list-of-approval-forms-visible-to-the-specified.md)接口，获取该用户可见的审批表单列表。

   ```
   public void processUserVisibilitieTemplates() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesHeaders listUserVisibleBpmsProcessesHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesHeaders();
           listUserVisibleBpmsProcessesHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesRequest listUserVisibleBpmsProcessesRequest = new com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesRequest()
                   .setUserId("manager7078")
                   .setMaxResults(10L)
                   .setNextToken(0L);
           try {
               ListUserVisibleBpmsProcessesResponse listUserVisibleBpmsProcessesResponse = client.listUserVisibleBpmsProcessesWithOptions(listUserVisibleBpmsProcessesRequest, listUserVisibleBpmsProcessesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
               System.out.println(JSON.toJSONString(listUserVisibleBpmsProcessesResponse.getBody()));
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

   - `userId`：目标用户的userid。

   **返回字段：**

   - `processList`：用户可见审批表单列表，包含processCode、name、iconUrl等字段。
4. **发起审批实例**：根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。

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

   - `processCode`：审批表单模板唯一编码。
   - `originatorUserId`：发起人userid。
   - `deptId`：发起人所属部门ID。
   - `microappAgentId`：应用标识AgentId。

   **返回字段：**

   - `instanceId`：审批实例唯一ID。
5. **获取审批实例ID列表**：发起多个审批实例后，可根据模板编码`processCode`，调用新版服务端API-[获取审批实例ID列表](0500-obtain-an-approval-list-of-instance-ids.md)接口，获取权限范围内的相关部门审批实例ID列表。

   ```
   public void processInstanceIdsQuery() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsHeaders listProcessInstanceIdsHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsHeaders();
           listProcessInstanceIdsHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsRequest listProcessInstanceIdsRequest = new com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsRequest()
                   .setProcessCode("PROC-FF6Y2xxxx")
                   .setStartTime(1496678400000L)
                   .setEndTime(1496678400000L)
                   .setNextToken(0L)
                   .setMaxResults(10L)
                   .setUserIds(java.util.Arrays.asList(
                       "发起userid"
                   ));
           try {
               ListProcessInstanceIdsResponse listProcessInstanceIdsResponse = client.listProcessInstanceIdsWithOptions(listProcessInstanceIdsRequest, listProcessInstanceIdsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
               System.out.println(JSON.toJSONString(listProcessInstanceIdsResponse.getBody()));
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

   - `processCode`：审批表单模板唯一编码。
   - `startTime`：查询起始时间戳（毫秒）。
   - `endTime`：查询结束时间戳（毫秒）。
   - `userIds`：发起人userId列表，最大列表长度为10。

   **返回字段：**

   - `list`：审批实例ID。
6. **获取用户待审批数量**：发起多个审批实例后，也可根据用户userId，调用新版服务端API-[获取用户待审批数量](0507-queries-the-number-of-requests-to-be-approved-by-users.md)接口，获取该用户待处理的审批数量。

   ```
   public void processTodoTasksNumbers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumHeaders getUserTodoTaskSumHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumHeaders();
           getUserTodoTaskSumHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumRequest getUserTodoTaskSumRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumRequest()
                   .setUserId("manager123");
           try {
               GetUserTodoTaskSumResponse getUserTodoTaskSumResponse = client.getUserTodoTaskSumWithOptions(getUserTodoTaskSumRequest, getUserTodoTaskSumHeaders, new com.aliyun.teautil.models.RuntimeOptions());
               System.out.println(JSON.toJSONString(getUserTodoTaskSumResponse.getBody()));
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

   - `userid`：待查询用户的userid。

   **返回字段：**

   - `result`：该用户待处理的审批数量。

**实施完成检查清单**

- ✅ 应用已完成创建并获取Client ID和Client Secret。
- ✅ 已申请`Workflow.Form.Write`、 `Workflow.Form.Read`、`Workflow.Instance.Write`和`Workflow.Instance.Read`权限。
- ✅ accessToken获取成功且缓存策略已配置。
- ✅ 获取企业可管理表单列表接口调用成功。
- ✅ 获取用户可见表单列表接口调用成功。
- ✅ 获取用户待审批数量接口调用成功。
- ✅ 前端已实现表单列表动态渲染和待办数量徽章展示。
- ✅ 权限过滤生效，不同角色用户看到差异化表单列表。

## 常见问题（FAQ）

- **Q：为什么调用获取表单列表接口返回空结果？**

  请确认传入的userId对应的用户是否拥有该企业OA审批的管理权限。只有具备OA审批权限的用户才能查询到可管理的表单列表。
- **Q：获取用户可见表单列表和获取企业可管理表单列表有什么区别？**

  获取企业可管理表单列表返回的是userId用户有权管理的所有表单（通常是管理员视角）；获取用户可见表单列表返回的是该用户作为申请人可以发起的表单（通常是普通员工视角），两者权限范围不同。
- **Q：待审批数量接口返回的count包含哪些状态的审批？**

  仅包含当前处于"待审批"状态的实例数量，不包括已同意、已拒绝、已撤销或已终止的审批实例。
- **Q：表单列表接口的返回结果是否需要缓存？**

  建议缓存。表单元数据变更频率低，可在业务系统侧缓存5-10分钟，减少API调用次数。但待审批数量接口不建议长时间缓存，建议每1-5分钟轮询一次以保证时效性。
- **Q：如果用户属于多个部门，获取可见表单列表时会重复返回吗？**

  不会。接口返回的是去重后的表单列表，即使同一表单因多部门权限被多次匹配，结果中也只出现一次。
