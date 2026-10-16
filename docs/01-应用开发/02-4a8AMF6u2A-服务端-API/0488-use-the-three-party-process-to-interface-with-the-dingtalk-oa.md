---
title: "三方流程审批页面托管：官方详情页与自定义操作区对接"
source_url: "https://open.dingtalk.com/document/development/use-the-three-party-process-to-interface-with-the-dingtalk-oa"
namespace: "development"
slug: "use-the-three-party-process-to-interface-with-the-dingtalk-oa"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 高级专享版 > 审批页面托管 > 三方流程审批页面托管：官方详情页与自定义操作区对接"
doc_id: "LCCWJvMCnZ"
updated_at: "2026-10-16 09:23:06"
---

> Source: https://open.dingtalk.com/document/development/use-the-three-party-process-to-interface-with-the-dingtalk-oa
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 高级专享版 > 审批页面托管 > 三方流程审批页面托管：官方详情页与自定义操作区对接
> Updated: 2026-10-16 09:23:06

# 三方流程审批页面托管：官方详情页与自定义操作区对接

## **概述**

本方案面向企业自有流程引擎但缺乏移动端/H5详情页面、希望复用钉钉官方OA审批详情页样式并自定义审批操作区按钮的场景，通过钉钉OA审批流程中心提供的审批页面托管API，支持三方业务系统在创建审批模板/实例时注册操作区自定义按钮渲染回调和执行回调接口，在钉钉端打开官方OA审批详情页处理流程。审批人获得多端一致的审批体验，同时三方业务可灵活配置同意/拒绝/转交等操作按钮及异常报错文案。

### 方案背景

部分复杂审批场景（如合同评审、项目立项）需在钉钉审批详情页内嵌业务系统自定义操作区，同时保留钉钉官方审批头部的标准字段展示。通过页面托管方案，可在同一详情页中融合钉钉标准审批信息与业务系统专属操作面板，兼顾规范性与灵活性。

企业在日常运营中常面临以下痛点：

- **信息展示割裂**： 钉钉标准审批页无法展示业务系统特有的附件预览、关联单据、历史版本等信息，审批人需额外跳转查看。
- **操作按钮缺失**： 审批详情页缺少业务系统专属操作入口（如"查看合同原文""下载附件包"），审批人需记忆原系统URL手动访问。
- **样式冲突频繁**： 业务系统嵌入页面与钉钉官方样式不兼容，出现滚动条重叠、按钮遮挡、字体错位等问题，影响审批体验。
- **权限控制复杂**： 不同角色在审批详情页应看到不同的操作区和数据字段，现有托管方案难以实现细粒度权限隔离。

### **核心价值**

本方案的核心价值体现在以下三个方面：

- **统一体验：** 将不同业务系统的审批单结构、样式统一为钉钉官方OA审批详情页，为用户提供多端（移动端/PC/平板）一致体验。
- **零成本打通：** 托管后可0成本实现与钉钉IM、待办等一方功能打通，拥有多个提升审批效率和体验的功能，实现三方即一方的审批体验。
- **灵活定制：** 详情页中的审批操作区按钮（同意、拒绝、转交等）可支持由三方业务灵活自定义配置，满足不同业务定制化诉求。

### **适用场景**

本方案适用于自有流程引擎但缺乏详情页面、希望复用钉钉官方样式并自定义操作区的企业管理场景，典型包括：

- **无移动端详情页面：** 公司存在审批系统不支持移动端/H5页面，使得员工尤其是管理层无法在钉钉场景下审批，通过审批托管低成本拥有优秀的钉钉多端统一审批体验。
- **一方功能打通诉求：** 审批人希望审批与钉钉一方功能更好的打通，提高审批效率，托管后的一键拉群、分享到聊天、复制链接到聊天/文档、打印、下载等功能可以0成本拥有。
- **流程效率治理：** 管理层提出希望对公司的流程效率进行系统分析治理，托管后的效率诊断和流程挖掘可以系统地发现效率、流程合理性等问题，并基于钉钉的流程治理实践给出优化建议。

## **典型业务场景**

### **场景一：连锁健身品牌门店运营审批托管（体育健身行业）**

#### **痛点分析**

某全国连锁健身品牌拥有120+门店，使用自研门店运营系统管理器械采购审批、私教课程排期审批、会员退费审批、场地维护审批，四套审批流程独立运行且均无移动端/H5详情页面。区域经理和各店店长每天需处理大量审批，原有流程存在以下问题：

- **多端体验割裂：** 日均审批量90+笔，审批人需在PC端登录门店运营系统查看审批详情，手机端仅能收到通知但无法查看详情和操作，区域经理出差时紧急采购审批响应延迟影响门店运营。
- **一方功能缺失：** 审批人收到"器械故障需紧急维修"审批后，需手动复制审批链接发送至维修群沟通，无法一键拉群、分享链接到聊天，每次操作额外耗时2分钟。
- **界面风格不一：** 四类审批详情页样式各异，新入职店长适应周期长达3周，审批操作习惯不一致导致误操作率高达8%。

#### **价值验证**

- **自动化流程**

  ![连锁健身品牌门店运营审批托管场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5160491971/p1105429.png)
- **关键优势**

  - **多端统一：** PC/手机/平板三端详情页样式完全一致，区域经理出差途中用手机即可完整查看审批详情并操作，紧急采购响应从2小时缩短至10分钟。
  - **一方打通：** 审批详情页内置一键拉群、分享链接到聊天、打印、下载等功能，无需手动复制链接，单次审批沟通耗时从2分钟降至零。
  - **灵活定制：** 器械采购审批显示"确认采购""驳回重选"按钮，会员退费审批显示"同意退费""要求补充材料"按钮，不同审批类型操作区差异化配置，误操作率从8%降至1%。

### **场景二：宠物医院连锁诊疗审批托管集成（宠物服务行业）**

#### **痛点分析**

某大型宠物医院连锁拥有30+分院，使用自研诊疗管理系统管理药品采购审批、手术方案审批、住院费用减免审批、设备报修审批，四套审批流程独立运行且均无移动端/H5详情页面。院长和各科室主任每天需处理大量审批，原有流程存在以下问题：

- **紧急审批响应慢：** 日均审批量70+笔，其中手术方案审批具有强时效性（动物病情变化快），但审批人需在PC端登录诊疗系统查看方案详情，手机端无法操作，曾发生3起因审批延迟导致手术错过最佳时机的事件。
- **跨科室协同低效：** 一个复杂手术方案涉及外科、麻醉科、影像科三方确认，审批人需在三个系统中分别查看方案细节，协调周期长达1天，动物等待时间过长增加医疗风险。
- **效率数据缺失：** 管理层希望分析各科室审批效率瓶颈，但自有系统无流程统计看板，无法定位审批积压环节，优化决策缺乏数据支撑。

#### **价值验证**

- **自动化流程**

  ![宠物医院连锁诊疗审批托管集成场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5160491971/p1105430.png)
- **关键优势**

  - **移动审批：** 手术方案审批详情页在手机端完整展示，院长查房途中即可查看详情并批准，手术准备时间从4小时缩短至30分钟，错过最佳时机事件降为零。
  - **协同提速：** 多科室确认类审批在统一详情页中展示所有关联信息，协调周期从1天缩短至2小时，动物等待风险显著降低。
  - **效率可视：** 托管后审批流转数据汇集到钉钉官方审批效率看板，管理层可通过OA审批助手推送或移动端—OA审批—统计模块查看流程效率统计报告，精准定位积压环节。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **模板托管层：** 调用创建/更新三方审批模板接口，将三方业务系统的审批模板同步至钉钉审批中心，获取模板唯一编码`processCode`，并在模板中注册审批操作区自定义按钮渲染回调地址。
- **实例托管层：** 调用创建/更新审批实例接口，将三方系统的审批实例同步至钉钉审批中心，获取审批实例`processInstanceId`，并在实例中注册审批操作区自定义按钮执行回调地址。
- **回调渲染层：** 三方系统提供HTTPS回调接口，接收钉钉审批操作区按钮渲染请求，返回自定义按钮配置数据，钉钉据此渲染详情页底部操作区。
- **回调执行层：** 三方系统提供HTTPS回调接口，接收钉钉审批操作区按钮执行请求，处理用户审批操作并返回执行结果，钉钉据此更新审批状态。
- **任务同步层：** 调用创建/更新/查询审批待办任务接口，将三方系统的审批待办任务同步至钉钉审批中心，保持数据一致性。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_aflow`（审批流数据管理权限）
  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Form.Read`（工作流模板读权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限）
- **开发环境：** 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：** 下载钉钉服务端SDK，支持Java/Python/Go等多语言。
- **网关准备：** 三方系统回调接口需在钉钉"数据源管理"中注册为网关，详细使用说明参考[数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：核心API调用：

1. 注册自定义快捷审批按钮callback回调接口，网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)。
2. 调用新版服务端API-[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)，获取模板的唯一编码`processCode`。
3. 若未保存`processCode`，可通过调用[获取模板code](0510-obtain-the-template-code.md)接口获取`processCode`。
4. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. 根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0542-api-premiumexternalintegrationprocessinstance.md)接口发起审批实例，获取审批实例`processInstanceId`。
6. 创建成功后，可进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. 根据`processInstanceId`和`tasks`，调用[保存流程中心外部集成审批任务](0543-api-premiumsaveintegratedtask.md)，获取待办事项的`taskId`并生成对应的钉钉待办任务。
8. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0516-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
9. 据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0518-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
10. 根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0513-update-instance-status.md)或 [批量更新实例状态](0514-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。
11. 若需要对审批模板数据进行清理，可以调用[删除模板](0511-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

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

   - `qyapi_aflow`(审批流数据管理权限)：用于查询/更新流程中心任务状态。
   - `Workflow.Form.Write`（工作流模板写权限）：用于获取模板code。
   - `Workflow.Form.Read`（工作流模板读权限）：用于创建/更新审批实、删除模板。
   - `Workflow.Instance.Write`（工作流实例写权限）：用于更新实例状态。
   - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限）：用于保存流程中心外部集成审批模板或审批任务。

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

1. **注册自定义审批操作按钮区callback回调接口：**一个用于回调三方获取操作区按钮数据的定义（按钮渲染），一个用于回调三方接口进行接收和处理用户的审批提交操作（操作审批）。接口协议详细参考：[审批操作区托管接口协议详解](0489-detailed-explanation-of-hosting-interface-agreement-in-approval-operation-area.md)。
2. **同步审批模板数据到钉钉****：**调用新版服务端API-[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > 该场景需对`processFeatureConfig`中的`CUSTOM_ACTION_DEFINITION`（表示获取操作区按钮数据的回调地址，即按钮渲染回调）、`CUSTOM_ACTION_APPLY`（表示进行审批操作时回调的回调地址，即操作审批回调）模块进行自定义配置。

   ```
   {
     "name": "审批页面托管集成模式",
     "description": "流程中心自定义托管模式：自定义审批操作区",
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
       },
       {
         "componentType": "TextareaField",
         "props": {
           "placeholder": "请输入",
           "label": "多行输入框"
         }
       },
       {
         "componentType": "NumberField",
         "props": {
           "placeholder": "请输入数字",
           "label": "数字输入框",
           "id": "NumberField-1"
         }
       },
       {
         "componentType": "DDSelectField",
         "props": {
           "options": [ // 可选选项列表
             {
               "value": "选项1", // 选项显示名称
               "key": "option_0" // 控件内唯一key，非必填，系统会默认生成
             },
             {
               "value": "选项2",
               "key": "option_1"
             },
             {
               "value": "选项3",
               "key": "option_2"
             },
             {
               "key": "other", // 其他项特殊key
               "value": "其它"
             }
           ],
           "label": "单选框",
           "placeholder": "请选择",
           "componentId": "DDSelectField_1",
           "required": false
         }
       },
       {
         "componentType": "DDMultiSelectField",
         "props": {
           "options": [
             {
               "value": "选项1",
               "key": "option_0"
             },
             {
               "value": "选项2",
               "key": "option_1"
             },
             {
               "value": "选项3",
               "key": "option_2"
             },
             {
               "key": "other", // 其他项特殊key
               "value": "其它"
             }
           ],
           "label": "多选框",
           "placeholder": "请选择",
           "componentId": "DDMultiSelectField_1",
           "required": false
         }
       },
       {
         "componentType": "DDDateField",
         "props": {
           "unit": "小时", // 日期格式，枚举值（小时、天）
           "format": "yyyy-MM-dd HH:mm", // 日期格式，非必填，小时对应yyyy-MM-dd HH:mm，天对应yyyy-MM-dd
           "bizAlias": "",
           "label": "日期",
           "placeholder": "请选择",
           "componentId": "DDDateField_1",
           "required": false,
           "defaultValue": "2021-12-21 17:46" // 默认值
         }
       },
       {
         "componentType": "DDDateRangeField",
         "props": {
           "unit": "天",
           "format": "yyyy-MM-dd",
           "bizAlias": "",
           "label": "[\"开始时间\",\"结束时间\"]",
           "placeholder": "请选择",
           "componentId": "DDDateRangeField_1",
           "duration": true, // 是否自动计算时长
           "durationLabel": "时长", // 时长计算显示文本
           "required": false
         }
       },
       {
         "componentType": "TextNote",
         "props": {
           "link": "https://www.dingtalk.com/", // 超链接
           "notPrint": "0",
           "bizAlias": "",
           "componentId": "TextNote_1",
           "content": "这是一个说明文字" // 说明文字
         }
       },
       {
         "componentType": "DDPhotoField",
         "props": {
           "label": "图片",
           "componentId": "DDPhotoField_1",
           "required": false
               }
           },
           {
               "componentType": "MoneyField",
               "props": {
                   "upper": "0", // 金额需要大写(0不大写，1需要大写)，默认需要大写
                   "label": "金额（元）",
                   "placeholder": "请输入金额",
                   "componentId": "MoneyField_1",
                   "required": false
               }
           },
           {
               "children": [
                   {
                       "componentType": "TextField",
                       "props": {
                           "label": "单行输入框",
                           "placeholder": "请输入",
                           "componentId": "TextField_1UE1ZY1A28AO0",
                           "required": false
                       }
                   },
                   {
                       "componentType": "MoneyField",
                       "props": {
                           "upper": "0",
                           "bizAlias": "",
                           "label": "金额（元）",
                           "placeholder": "请输入金额",
                           "componentId": "MoneyField_1S85G0",
                           "required": false
                       }
                   },
                   {
                       "componentType": "NumberField",
                       "props": {
                           "unit": "元",
                           "bizAlias": "",
                           "label": "数字输入框",
                           "placeholder": "请输入数字",
                           "componentId": "NumberField_1XP6A",
                           "required": false
                       }
                   }
               ],
               "componentType": "TableField",
               "props": {
                   "tableViewMode": "table",
                   "verticalPrint": true,
                   "statField": [
                       {
                           "componentId": "MoneyField_1S85G0",
                           "label": "金额（元）"
                       },
                       {
                           "componentId": "NumberField_1XP6A",
                           "label": "数字输入框"
                       }
                   ],
                   "bizAlias": "table",
                   "label": "表格",
                   "componentId": "TableField_1MLEPEA"
               }
           },
           {
               "componentType": "DDAttachment",
               "props": {
                   "label": "附件",
                   "componentId": "DDAttachment_1",
                   "required": false
               }
           },
           {
               "componentType": "InnerContactField",
               "props": {
                   "label": "联系人",
                   "placeholder": "请选择",
                   "componentId": "InnerContactField_1",
                   "choice": "1", //枚举值：1标识支持多选，0标识单选，默认为0
                   "required": false,
                   "bizAlias": ""
               }
           },
           {
               "componentType": "DepartmentField",
               "props": {
                   "multiple": false, // 是否支持多选，true多选，false单选
                   "label": "部门",
                   "placeholder": "请选择",
                   "componentId": "DepartmentField_1",
                   "required": false
               }
           },
           {
               "componentType": "RelateField",
               "props": {
                   "label": "关联审批单",
                   "placeholder": "请选择",
                   "componentId": "RelateField_1",
                   "required": false,
                   "bizAlias": "",
                   "availableTemplates": [ // 可被关联的审批模板列表，为空时表示可关联所有审批模板的实例数据
                   ]
               }
           },
           {
               "componentType": "AddressField",
               "props": {
                   "addressModel": "district", // 枚举值,city省市,district省市区,street省市区-街道
                   "bizAlias": "",
                   "label": "省市区",
                   "componentId": "AddressField_1",
                   "required": false
               }
           },
           {
               "componentType": "StarRatingField",
               "props": {
                   "limit": 5, // 枚举值：5分制、10分制
                   "label": "评分",
                   "placeholder": "请输入",
                   "componentId": "StarRatingField_1",
                   "required": false,
                   "bizAlias": ""
               }
           }
       ],
       "processFeatureConfig": {
           "features": [
               {
                   // 表示获取操作区（按钮）数据的回调地址（按钮渲染）
                   "name": "CUSTOM_ACTION_DEFINITION",
                   "runType": "OUTBIZ_CUSTOM",
                   "callback": {
                       "apiKey": "getIntegratedCustomActionDefinitions",
                       "appUuid": "dingec6f7227666ad00ba39a90f97fcb1e09",
                       "version": "1"
                   }
               },
               {
                   // 表示进行审批操作时回调的回调地址（操作审批）
                   "name": "CUSTOM_ACTION_APPLY",
                   "runType": "OUTBIZ_CUSTOM",
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

   - `name`：审批模板名称。
   - `description`：模板描述信息。
   - `formComponents`：表单组件配置数组。
   - `processFeatureConfig`：流程中心集成配置。

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
5. **同步审批实例数据到钉钉：**根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0542-api-premiumexternalintegrationprocessinstance.md)发起审批实例，获取审批实例`processInstanceId`。

   > **[!NOTE]**
   >
   > 若在创建审批模板时未注册自定义审批操作按钮相关配置，也支持在创建实例维度进行指定，若同时在模板/实例维度进行了配置，优先以实例维度为准。

   ```
   {
     "formComponentValueList": [
       {
         "name": "单行输入框",
         "value": "[钉钉](https://www.dingtalk.com/)"
       },
       {
         "name": "多行输入框",
         "value": "请输入多行文本内容，需要换行时请输入\r\n请输入多行文本内容，需要换行时请输入\r\n"
       },
       {
         "name": "数字输入框",
         "value": "100"
       },
       {
         "name": "单选框",
         "value": "选项1"
       },
       {
         "name": "多选框",
         "value": "[\"选项1\",\"选项2\"]"
       },
       {
         "name": "日期",
         "value": "2021-08-17 11:11"
       },
       {
         "name": "[\"开始时间\",\"结束时间\"]",
         "value": "[\"2019-02-19 11:11\",\"2019-02-25 11:11\"]"
       },
       {
         "name": "图片",
         "value": "[\"https://img.alicdn.com/imgextra/i3/O1CN01TDKbCW28HuskT5vnR_!!6000000007908-2-tps-2724-650.png\",\"https://img.alicdn.com/imgextra/i3/O1CN01TDKbCW28HuskT5vnR_!!6000000007908-2-tps-2724-650.png\",\"http://url3\"]"
       },
       {
         "name": "表格",
         "value": "[[{\"name\":\"单行输入框\",\"value\":\"[钉钉](https://www.dingtalk.com/)\"},{\"name\":\"数字输入框\",\"value\":\"100\"}]]"
       },
       {
         "name": "金额（元）",
         "value": "100"
       },
       {
         "name": "附件",
         "value": "[{\"spaceId\": \"163xxxx658\", \"fileName\": \"2644.JPG\", \"fileSize\": \"333\", \"fileType\": \"jpg\", \"fileId\": \"643xxxx140\"}]"
       },
       {
         "name": "联系人",
         "value": "[\"0135185610551036178639\"]"
       },
       {
         "name": "关联审批单",
         "value": "[\"9XCLWKxNTom6W_u88iKbug09641720074458\", \"9XCLWKxNTom6W_u88iKbug09641720074458\"]"
       },
       {
         "name": "电话",
         "value": "18015586666"
       },
       {
         "name": "省市区",
         "value": "北京,北京市,河东区"
       },
       {
         "name": "评分",
         "value": "5"
       },
       {
         "name": "部门",
         "value": "714738614"
       }
     ],
     "title": "审批页面托管集成模式",
     "processCode": "PROC-A807C4FF-93AF-409A-A0C5-197CC81E8FF9",
     "originatorUserId": "manager9814",
     "url": "http://www.dingtalk.com",
     "notifiers": [
       {
         "userid": "manager9814",
         "position": "start"
       }
     ],
     "featureConfig": {
       "features": [
         {
           // 表示获取操作区（按钮）数据的回调地址（按钮渲染）
           "name": "CUSTOM_ACTION_DEFINITION",
           "runType": "OUTBIZ_CUSTOM",
           "callback": {
             "apiKey": "getIntegratedCustomActionDefinitions",
             "appUuid": "dingec6f7227666ad00ba39a90f97fcb1e09",
             "version": "1"
           }
         },
         {
           // 表示进行审批操作时回调的回调地址（操作审批）
           "name": "CUSTOM_ACTION_APPLY",
           "runType": "OUTBIZ_CUSTOM",
           "callback": {
             "apiKey": "applyIntegratedCustomAction",
             "appUuid": "dingec6f7227666ad00ba39a90f97fcb1e09",
             "version": "1"
           }
         }
       ]
     },
     "bizData": "{\"apiKey\":\"customActionDefinitionApiKey2\",\"appUuid\":\"appUuid2\",\"version\":\"2\"}"
   }
   ```

   **请求参数：**

   - `formComponentValueList`：表单组件值列表。
   - `title`：审批实例标题。
   - `processCode`：审批模板唯一编码。
   - `originatorUserId`：发起人userid。
   - `url`：审批详情页跳转地址。
   - `featureConfig`：实例级集成配置。
   - `bizData`：用户自定义业务参数（json字符串格式）。

   **返回字段：**

   - `processInstanceId`：审批实例唯一ID。
6. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. **同步审批任务数据到钉钉：**根据审批实例`processInstanceId`和待办事项列表tasks，调用[保存流程中心外部集成审批任务](0543-api-premiumsaveintegratedtask.md)，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。

   ```
   {
     "processInstanceId": "snfwBXcRTWuxuAnpBLGsqQ09641722392174",
     "activityId": "001",
     "tasks": [
       {
         "userId": "manager9814",
         "url": "https://www.dingtalk.com"
       },
       {
         "userId": "0135185610551036178639",
         "url": "https://www.dingtalk.com"
       }
     ]
   }
   ```

   **请求参数：**

   - `processInstanceId`：审批实例唯一ID。
   - `activityId`：审批节点活动ID。
   - `tasks`：待办事项列表，包含审批人userid和详情页URL。

   **返回字段：**

   - `taskId`：审批待办任务唯一ID。
8. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0516-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。

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
9. 根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

   > **[!NOTE]**
   >
   > 审批人从钉钉端打开自定义审批页进行审批时，操作同意/拒绝等功能模块，将会回调[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)接口中**CUSTOM\_ACTION\_APPLY**模块中配置的回调接口，三方在执行自身业务逻辑完之后，需主动同步任务状态至钉钉。

   ```
   {
     "processInstanceId": "qZpLKAIuTGWHFq8YLx4llA09641722243810",
     "tasks": [
       {
         "taskId": 88094338042,
         "status": "COMPLETED",
         "result": "AGREE"
       }
     ]
   }
   ```

   **请求参数：**

   - `processInstanceId`：OA审批流程实例ID。
   - `taskId`：OA审批任务ID。
   - `status`：更新为目标任务状态。
   - `result`：示例结果。

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
10. **同步审批实例状态到钉钉：**根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0513-update-instance-status.md)或 [批量更新实例状态](0514-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。

    ```
    public void updateProcessInstance() throws Exception {
      Config config = new Config();
      config.protocol = "https";
      config.regionId = "central";
      com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
      UpdateProcessInstanceHeaders updateProcessInstanceHeaders = new UpdateProcessInstanceHeaders();
      updateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
      UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers notifiers0 = new UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers()
                    .setUserId("001");
      UpdateProcessInstanceRequest updateProcessInstanceRequest = new UpdateProcessInstanceRequest()
                    .setProcessInstanceId("proc")
                    .setStatus("COMPLETED")
                    .setResult("agree")
                    .setNotifiers(java.util.Arrays.asList(
                        notifiers0
                    ));
      try {
        UpdateProcessInstanceResponse updateProcessInstance = client.updateProcessInstanceWithOptions(deleteProcessRequest, updateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
    - `status`：实例状态，包含`COMPLETED`（结束审批流）和`TERMINATED`（终止审批流）。
    - `result`：实例结果。
    - `userId`：抄送人userId。

    **返回字段：**

    - `success`：是否执行成功。
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
- ✅ 三方审批模板创建成功并获取processCode。
- ✅ `processFeatureConfig`中`PAGE_HOST`正确配置`renderCallback`和`executeCallback`。
- ✅ 审批实例创建成功并获取processInstanceId。
- ✅ 审批待办任务创建成功。
- ✅ 按钮渲染回调接口测试通过，返回正确的按钮配置数据。
- ✅ 按钮执行回调接口测试通过，正确处理审批操作并返回结果。
- ✅ 钉钉端打开官方OA审批详情页显示正常。
- ✅ 审批操作区自定义按钮渲染正确。
- ✅ 权限过滤生效，不同角色用户看到差异化审批任务。

## **常见问题（FAQ）**

- **Q：renderCallback和executeCallback的区别是什么？**

  - `renderCallback`用于钉钉向三方系统请求审批操作区按钮的定义数据（按钮文案、颜色、可见性等），钉钉据此渲染详情页底部操作区；
  - `executeCallback`用于钉钉向三方系统提交用户点击按钮后的审批操作请求，三方系统处理后返回执行结果。两者职责分离，不可混用。
- **Q：回调接口超时如何处理？**

  钉钉回调三方系统接口的超时时间为5秒。若三方系统在5秒内未返回HTTP 200，钉钉将进行最多3次重试，间隔分别为1s、2s、4s。建议三方系统回调接口保持轻量，复杂逻辑异步处理。
- **Q：审批操作区按钮是否可以动态控制可见性？**

  可以。在`renderCallback`返回的按钮配置数据中，可通过`visible`字段控制按钮是否显示，支持根据审批人角色、审批状态、业务条件等动态控制按钮可见性。
- **Q：审批页面托管后，流程效率数据如何查看？**

  托管后三方审批流转情况将汇集到钉钉官方审批效率看板中，管理层可通过OA审批助手推送或移动端—OA审批—统计模块查看流程效率统计报告，全方位诊断企业的审批效率和合理性。
