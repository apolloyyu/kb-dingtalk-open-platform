---
title: "审批流程托管：钉钉流程与三方页面对接"
source_url: "https://open.dingtalk.com/document/development/approval-process-hosting-integration-mode-use-the-dingtalk-official-oa"
namespace: "development"
slug: "approval-process-hosting-integration-mode-use-the-dingtalk-official-oa"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 标准版 > 审批流程托管：钉钉流程与三方页面对接"
doc_id: "cIjO2lxlyi"
updated_at: "2026-10-12 18:04:38"
---

> Source: https://open.dingtalk.com/document/development/approval-process-hosting-integration-mode-use-the-dingtalk-official-oa
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 标准版 > 审批流程托管：钉钉流程与三方页面对接
> Updated: 2026-10-12 18:04:38

# 审批流程托管：钉钉流程与三方页面对接

## **概述**

本方案采用审批流程托管集成模式，将钉钉官方OA审批工作流引擎与三方自研业务页面深度对接。业务系统通过调用钉钉OA审批API创建审批流程实例，并在发起时指定第三方审批系统的详情页跳转地址；当审批人在钉钉端打开审批详情时，自动跳转至业务系统自研页面完成审批操作。该方案既复用钉钉官方工作流的能力，又保留复杂业务表单的自定义呈现，实现低成本快速集成。

### **方案背景**

在企业自有业务系统中，部分审批表单控件字段较多、业务逻辑复杂，若将所有表单控件同步至钉钉OA审批管理后台配置，对接成本高且难以延续用户原有操作习惯。钉钉开放平台提供了"审批流程托管"集成模式，支持业务系统调用新版服务端API创建或更新审批表单模板、发起审批实例并指定三方详情页URL，使审批人从钉钉待办/消息卡片等入口可直接跳转至业务系统自研页面处理审批，兼顾工作流标准化与表单灵活性。

### **核心价值**

本方案的核心价值体现在以下三个方面：

- **灵活对接：** 使用钉钉OA审批官方工作流 + 三方业务自研页面集成，直接复用钉钉官方OA审批流程引擎的工作流能力，无缝连接钉钉聊天、待办、通知，高效审批。
- **简化成本：** 审批详情页采用三方业务自研页面，无需把所有表单控件字段同步至钉钉，简化对接成本，延续用户原来使用的流程和页面习惯，低成本快速使用。
- **统一体验：** 支持从业务系统发起流程，调用钉钉官方OA审批接口创建OA审批流程，审批人从钉钉OA审批/待办/消息卡片等入口直接打开业务系统自研页面审批，体验一致。

### **适用场景**

本方案适用于需要复用钉钉官方工作流引擎但表单页面较复杂的业务系统集成场景，典型包括：

- **复杂表单审批：** 业务系统存在大量自定义控件字段的审批表单，不适合在钉钉管理后台逐一配置，需在自研页面中完整呈现。
- **存量系统对接：** 已有成熟的审批页面和交互逻辑，希望最小化改造成本接入钉钉工作流，保持原有用户体验。
- **多系统协同审批：** 审批流程涉及多个业务系统的数据联动，需在自研页面中实时查询和展示跨系统信息。

## **典型业务场景**

### **场景一：大型制造企业生产工单审批集成（制造业）**

#### **痛点分析**

某大型制造企业使用自研MES系统管理生产工单，工单审批涉及设备编号、工艺路线、物料清单、质检标准等数十个字段，且需实时关联ERP库存数据和PLM图纸信息。原有流程存在以下问题：

- **表单配置繁重：** 若将所有工单字段同步至钉钉OA审批管理后台配置，需维护上百个控件映射关系，新增字段时需同步修改钉钉配置和业务系统，运维成本高。
- **数据联动缺失：** 钉钉原生审批表单无法实时查询ERP库存和PLM图纸，审批人需在多个系统间切换查看，效率低下。
- **用户习惯断裂：** 车间班组长长期使用MES自研工单审批页面，熟悉其布局和快捷操作，切换至钉钉原生表单后学习成本高、抵触情绪强。

#### **价值验证**

- **自动化流程**

  ![制造企业生产工单审批集成场景图_20261012_114835](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8749971971/p1105139.png)
- **关键优势**

  - **表单零迁移：** 无需将MES工单的数十个字段同步至钉钉管理后台，直接在自研页面中完整呈现，新增字段仅需修改MES前端，钉钉侧零改动。
  - **数据实时联动：** 自研页面内嵌ERP和PLM接口调用，审批人可在同一页面查看库存余量、图纸版本、历史工单记录，决策效率提升50%以上。
  - **体验无缝衔接：** 车间班组长继续使用熟悉的MES审批界面和操作习惯，仅底层工作流切换为钉钉引擎，培训成本趋近于零。

### **场景二：金融机构信贷审批系统集成（金融行业）**

#### **痛点分析**

某商业银行使用自研信贷审批系统处理贷款申请，审批表单包含客户征信报告、收入证明、抵押物评估、风险评级模型输出等敏感数据，且需根据审批阶段动态展示不同字段组合。原有流程存在以下问题：

- **数据安全顾虑：** 若将征信报告、收入证明等敏感字段同步至钉钉OA审批管理后台，存在数据泄露风险，合规部门不予批准。
- **动态字段复杂：** 信贷审批分初审、复审、终审三个阶段，各阶段展示的字段和控件不同，钉钉原生表单难以实现条件渲染和动态显隐。
- **审批链路冗长：** 审批人需在信贷系统和钉钉之间反复切换查看完整材料，平均单笔审批耗时增加15分钟。

#### **价值验证**

- **自动化流程**

  ![金融机构信贷审批系统集成场景图_20261012_115312](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8749971971/p1105140.png)
- **关键优势**

  - **敏感数据不出域：** 征信报告、收入证明等敏感字段仅在信贷系统自研页面内展示，不经过钉钉管理后台，满足金融合规要求。
  - **动态表单自适应：** 自研页面根据审批阶段自动切换字段组合和校验规则，初审显示基础信息，复审追加风险评估，终审展示最终结论，逻辑清晰。
  - **审批效率提升：** 审批人在单一页面内完成所有材料查阅和操作，无需跨系统切换，单笔审批耗时缩短12分钟，日均处理量提升30%。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **流程引擎层：** 复用钉钉官方OA审批工作流引擎，处理审批流转、节点路由、任务分配等核心逻辑。
- **页面对接层：** 负责在发起审批时指定三方详情页URL，并在钉钉端打开时执行跳转至业务系统自研页面。
- **事件回调层：** 监听钉钉OA审批实例状态变更和审批任务回调事件，同步更新业务系统审批状态。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求：** 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Workflow.Instance.Read`（工作流实例读权限）
- **开发环境：** 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：** 下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。
2. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看/**编辑**官方OA审批单模板、查看/搜索模板数据、导出/删除模板数据等。
3. 根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。
4. 发起审批实例成功后，进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
5. 若需要添加审批评论附件，需先将文件上传至审批钉盘空间，再调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口。
6. 调用新版服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
7. 调用客户端JSAPI-[uploadAttachmentToDingTalk](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息，本流程示例使用[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10318)实现。
8. 获取审批钉盘空间spaceId后，可根据审批实例`instanceId`，调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口，实现审批单的添加评论操作。
9. 若需要预览/下载附件，可调用服务端API-[授权下载审批钉盘文件](0503-download-the-approval-nail-file.md)、[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口，进行审批钉盘文件的授权操作，再调用服务端API-[下载审批附件](0504-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。具体使用教程参考：[OA审批流接入：附件审批的下载与预览](0480-new-version-of-attachment-approval-process.md)。
10. 业务系统根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情，获取审批任务各个任务节点信息。
11. 根据审批实例`instanceId`和`taskId`信息，调用新版服务端API-[同意或拒绝审批任务](0505-approve-or-reject-the-approval-task.md)接口，实现审批任务的操作。
12. 若发现提交的审批单有误需撤销该审批实例，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。
13. 审批单状态发生变化后，OA审批支持将[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧。

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

   - `Workflow.Form.Write`（工作流模板写权限）：用于创建或更新审批表单模板。
   - `Workflow.Instance.Write`（工作流实例写权限）：用于发起审批实例和提交审批结果。
   - `Workflow.Instance.Read`（工作流实例读权限）：用于获取审批实例详情和审批任务信息。

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

1. **创建或更新审批表单模板**：调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。管理员也可在OA管理后台手动操作创建。

   ```
   {
     "name": "使用官方OA审批流程+三方页面对接",
     "description": "实现业务系统发起，并指定第三方审批系统中审批单详情页跳转地址进行集成的场景案例，用于满足三方业务自研页面 + OA审批官方工作流集成的复杂业务场景诉求。",
     "templateConfig": {
       "disableStopProcessButton": false,
       "disableFormEdit": false,
       "disableHomepage": false,
       "hidden": false
     },
     "formComponents": [
       {
         "componentType": "TextField",
         "props": {
           "label": "单行输入框", // 控件标题
           "placeholder": "请输入", // 输入提示
           "componentId": "TextField_17EZKEGSOCTC0", // 控件id，表单内唯一，无业务语义
           "required": false, // 是否必填，默认非必填
           "bizAlias": "staffId" // 控件的业务标识，表单内唯一，与componentId二选一
         }
       },
       {
         "componentType": "TextareaField",
         "props": {
           "label": "多行输入框",
           "placeholder": "请输入多行文本内容，需要换行时请输入\r\n", // 输入提示
           "componentId": "TextareaField_17EZKEGSOCTC0",
           "required": false
         }
       },
       {
         "componentType": "NumberField",
         "props": {
           "label": "数字输入框",
           "placeholder": "请输入数字",
           "componentId": "NumberField_108PIFZM21F40",
           "required": false,
           "unit": "元", // 数字单位
           "defaultValue": "10" // 默认值
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
           "componentId": "DDSelectField_14T8M4EKXAV40",
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
           "componentId": "DDMultiSelectField_1XJ7NG1GSD6O0",
           "required": false
         }
       },
       {
         "componentType": "DDDateField",
         "props": {
           "unit": "小时", // 日期格式，枚举值（小时、天）
           "format": "yyyy-MM-dd HH:mm", // 日期格式，非必填，小时对应yyyy-MM-dd HH:mm，天对应yyyy-MM-dd HH:mm
           "bizAlias": "",
           "label": "日期",
           "placeholder": "请选择",
           "componentId": "DDDateField_SQL0DF3MS9C0",
           "required": false,
           "defaultValue": "2021-12-21 17:46" // 默认值
         }
       },
       {
         "componentType": "DDDateRangeField",
         "props": {
           "unit": "小时",
           "format": "yyyy-MM-dd HH:mm",
                   "bizAlias": "",
                   "label": "[\"开始时间\",\"结束时间\"]",
                   "placeholder": "请选择",
                   "componentId": "DDDateRangeField_7MPG14N3OOO0",
                   "duration": true, // 是否自动计算时长
                   "required": false
               }
           },
           {
               "componentType": "TextNote",
               "props": {
                   "link": "https://www.dingtalk.com/", // 超链接
                   "notPrint": "0",
                   "bizAlias": "",
                   "componentId": "TextNote_13RP7230RAF40",
                   "content": "说明文字" // 说明文字
               }
           },
           {
               "componentType": "PhoneField",
               "props": {
                   "mode": "phone", // 枚举值：phone_tel：手机和固话、phone：手机、tel：固话
                   "label": "电话",
                   "placeholder": "请输入",
                   "componentId": "PhoneField_Y0XWOX6ZP6O0",
                   "required": false
               }
           },
           {
               "componentType": "DDPhotoField",
               "props": {
                   "label": "图片",
                   "componentId": "DDPhotoField_P50A0HMHB280",
                   "required": false
               }
           },
           {
               "componentType": "MoneyField",
               "props": {
                   "upper": "0", // 金额需要大写(0不大写，1需要大写)，默认需要大写
                   "label": "金额（元）",
                   "placeholder": "请输入金额",
                   "componentId": "MoneyField_L1PP26ZDV400",
                   "required": false
               }
           },
           {
               "componentType": "DDAttachment",
               "props": {
                   "label": "附件",
                   "componentId": "DDAttachment_18U4QTOWLMPS0",
                   "required": false
               }
           },
           {
               "componentType": "InnerContactField",
               "props": {
                   "label": "联系人",
                   "placeholder": "请选择",
                   "componentId": "InnerContactField_162USP4V1BC00",
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
                   "componentId": "DepartmentField_1GY5JSPOCY000",
                   "required": false
               }
           },
           {
               "componentType": "RelateField",
               "props": {
                   "label": "关联审批单",
                   "placeholder": "请选择",
                   "componentId": "RelateField_5X1DL4KMKUW0",
                   "required": false,
                   "bizAlias": "",
                   "availableTemplates": [ // 可被关联的审批模板列表，为空时表示可关联所有审批模板的实例数据
                       {
                           "name": "官方OA审批-POP-0328-日期区间7", // 可关联的审批表单名称
                           "processCode": "PROC-AF45DE4C-7520-4842-9128-EB7BD0A4EA85" // 可关联的审批表单formCode
                       }
                   ]
               }
           },
           {
               "componentType": "AddressField",
               "props": {
                   "addressModel": "district", // 枚举值,city省市,district省市区,street省市区-街道
                   "bizAlias": "",
                   "label": "省市区",
                   "componentId": "AddressField_1P9H21H8R2LC0",
                   "required": false
               }
           },
           {
               "componentType": "StarRatingField",
               "props": {
                   "limit": 5, // 枚举值：5分制、10分制
                   "label": "评分",
                   "placeholder": "请输入",
                   "componentId": "StarRatingField_10E5NHTA2W0G0",
                   "required": false,
                   "bizAlias": ""
               }
           },
           {
               "children": [ // 明细中的子控件列表，子控件列表遵循各控件属性标准
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
                           "payEnable": false,
                           "upper": "0",
                           "bizAlias": "",
                           "label": "金额（元）",
                           "placeholder": "请输入金额",
                           "componentId": "MoneyField_1S85G4YLMM5C0",
                           "required": false
                       }
                   },
                   {
                       "componentType": "NumberField",
                       "props": {
                           "unit": "元",
                           "payEnable": false,
                           "bizAlias": "",
                           "label": "数字输入框",
                           "placeholder": "请输入数字",
                           "componentId": "NumberField_1XP6AWG50SE80",
                           "required": false
                       }
                   }
               ],
               "componentType": "TableField",
               "props": {
                   "tableViewMode": "table", // 明细填写方式，枚举值：list：列表,table：表格
                   "verticalPrint": true, // 明细打印方式，true：纵向 false：横向
                   "statField": [ // 设置对数字、金额类控件进行总数统计
                       {
                           "componentId": "MoneyField_1S85G4YLMM5C0",
                           "label": "金额（元）"
                       },
                       {
                           "componentId": "NumberField_1XP6AWG50SE80",
                           "label": "数字输入框"
                       }
                   ],
                   "bizAlias": "",
                   "label": "表格",
                   "componentId": "TableField_1MLEPEAQSXHC0"
               }
           }
       ]
   }
   ```

   **请求参数：**

   - `name`：审批表单名称。
   - `description`：表单描述信息。

   **返回字段：**

   - `processCode`：审批表单模板唯一编码。
2. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看/**编辑**官方OA审批单模板、查看/搜索模板数据、导出/删除模板数据等。
3. **发起审批实例并指定三方详情页**：根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，**并指定第三方审批系统中审批单详情页跳转地址****进行集成**（若指定了bizDetailPageUrl，在钉钉OA审批、钉钉待办、消息卡片等入口点击跳转时，将会直接跳转对应业务系统详情页地址），获取审批实例`instanceId`。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9949463871/p926998.png)

   ```
   {
     "processCode": "PROC-C512D64A-60F6-4F83-B708-xxx",
     "originatorUserId": "manager98xx",
     "deptId": -1,
     "microappAgentId": 348925476,
     "bizDetailPageUrl":"https://www.dingtalk.com",
     "formComponentValues": [
       {
         "name": "日期",
         "value": "2021-08-17"
       },
       {
         "name": "[\"开始时间\",\"结束时间\"]",
         "value": "[\"2019-02-19\",\"2019-02-25\"]"
       },
       {
         "name": "身份证",
         "value": "xxxx"
       },
       {
         "name": "图片",
         "value": "[\"http://url1\",\"http://url2\",\"http://url3\"]"
       },
       {
         "name": "表格",
         "value": "[[{\"name\":\"单行输入框\",\"value\":\"[百度](https://www.baidu.com/)\"},{\"name\":\"数字输入框\",\"value\":\"100\"}]]"
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
         "name": "省市区",
         "value": "北京,北京市,河东区"
       },
       {
         "name": "评分",
         "value": "5"
       },
       {
         "name": "文本框",
         "value": "文本框示例"
       }
     ],
     "approvers": [
       {
         "actionType": "NONE",
         "userIds": [
           "manager98xx"
         ]
       },
       {
         "actionType": "OR",
         "userIds": [
           "manager98xx"
         ]
       }
     ]
   }
   ```

   **请求参数：**

   - `processCode`：审批表单模板唯一编码。
   - `originatorUserId`：发起人userid。
   - `deptId`：发起人所属部门ID。

   **返回字段：**

   - `instanceId`：审批实例唯一ID。
4. 发起审批实例成功后，用户可进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
5. **添加审批评论附件：**若需要添加审批评论附件，需先将文件上传至审批钉盘空间，再调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口。具体使用教程参考：[OA审批流接入：添加审批评论与终止审批](0478-comment-and-revoke-approval-flow.md)。

   1. 调用新版服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
   2. 调用客户端JSAPI-[uploadAttachmentToDingTalk](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息，本流程示例使用[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10318)实现。
   3. 获取审批钉盘空间spaceId后，可根据审批实例`instanceId`，调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口，实现审批单的添加评论操作。

      ```
      {
        "commentUserId": "manager98xx",
        "processInstanceId": "DQ7-X2EESQunrozGEe_xxx",
        "text": "测试添加审批评论",
        "file": {
          "attachments": [
            {
              "spaceId": "817447xxx",
              "fileSize": "173404",
              "fileId": "6660150xxx",
              "fileName": "评论附件.jpg",
              "fileType": "jpg"
            }
          ],
          "photos": [
            "https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9227796361/p352432.png"
          ]
        }
      }
      ```
6. **预览下载审批附件：**若需要预览/下载附件，可调用服务端API-[授权下载审批钉盘文件](0503-download-the-approval-nail-file.md)、[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口，进行审批钉盘文件的授权操作，再调用服务端API-[下载审批附件](0504-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。具体使用教程参考：[OA审批流接入：附件审批的下载与预览](0480-new-version-of-attachment-approval-process.md)。
7. **同意/拒绝审批任务：**审批人可通过钉钉OA审批中心、钉钉待办中心、OA审批消息卡片手动操作同意/拒绝审批任务；或业务系统根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情，获取审批任务各个任务节点信息`taskId`。
8. 根据审批实例`instanceId`和相应的任务节点`taskId`信息，调用新版服务端API-[同意或拒绝审批任务](0505-approve-or-reject-the-approval-task.md)接口，实现审批任务的操作，所有审批节点同意后，则该审批单通过。

   ```
   {
       "actionerUserId": "manager98xx",
       "processInstanceId": "fsTunaLIRyeRMrddA1YwZQ0964170020xxxx",
       "remark": "同意",
       "taskId": 8333450,
       "result": "agree",
       "file": {
           "attachments": [
               {
                   "space_id": "817447xxxx",
                   "file_size": "173404",
                   "file_id": "6660150xxxx",
                   "file_name": "评论附件.jpg",
                   "file_type": "jpg"
               }
           ],
           "photos": [
               "https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9227796361/p352432.png"
           ]
       }
   }
   ```

   **请求参数：**

   - `processInstanceId`：审批实例唯一ID。
   - `taskId`：当前审批任务ID。
   - `result`：审批结果，`agree`表示同意，`refuse`表示拒绝。
   - `remark`：审批意见。

   **返回字段：**

   - `success`：操作是否成功。
9. 撤销官方OA审批实例：查看审批后，若发现提交的审批单有误需撤销该审批实例，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。

   ```
   {
       "isSystem": true,
       "processInstanceId": "oKPAxjtgSP-AqeVTk-xxxx",
       "operatingUserId": "manager98xx",
       "remark": "撤销审批实例"
   }
   ```
10. 审批单状态发生变化后，OA审批支持将[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧，可以让企业应用能够更深度地与钉钉平台集成，实现信息共享和业务协同。具体使用教程参考：[事件订阅操作指南](0014-event-subscription-overview.md)。

**实施完成检查清单**

- ✅ 应用已完成创建并获取Client ID和Client Secret。
- ✅ 已申请Workflow.Form.Write、Workflow.Instance.Write、Workflow.Instance.Read权限。
- ✅ accessToken获取成功且缓存策略已配置。
- ✅ 创建或更新审批表单模板接口调用成功。
- ✅ 发起审批实例并指定detailUrl接口调用成功。
- ✅ 同意或拒绝审批流程接口调用成功。
- ✅ 审批实例回调事件注册并正常接收。
- ✅ 三方详情页URL可被钉钉端正确跳转访问。
- ✅ 业务系统审批状态与钉钉审批实例状态同步一致。
- ✅ 前端已实现自研审批页面渲染和审批操作提交
- ✅ 权限过滤生效，不同角色用户看到差异化审批任务。

## **常见问题（FAQ）**

- **Q：detailUrl中的{processInstanceId}占位符如何替换？**

  钉钉端在打开审批详情时，会自动将`{processInstanceId}`替换为实际的审批实例ID，无需业务系统手动处理。若需传递额外参数，可在URL中追加自定义query string。
- **Q：三方详情页是否需要做钉钉免登适配？**

  是的。审批人从钉钉端跳转至三方详情页时，钉钉会在URL中附带免登授权码`code`参数，业务系统需实现免登访问。
- **Q：审批实例回调事件的推送地址如何配置？**

  在钉钉开发者后台的应用详情页，并在事件订阅中添加订阅，填写业务系统的HTTPS回调地址。钉钉会以POST方式推送JSON格式的事件数据。
- **Q：若三方详情页加载失败或超时，钉钉端如何处理？**

  钉钉端会显示默认的错误提示页面，不会阻塞审批流程。建议业务系统确保详情页的高可用性，并在页面加载失败时提供友好的错误提示和重试机制。
- **Q：审批人在自研页面提交的审批结果是否会同步至钉钉待办？**

  是的。调用同意或拒绝审批流程接口提交审批结果后，钉钉待办中的对应任务会自动更新状态，审批人会收到相应的通知消息。
