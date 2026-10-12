---
title: "官方OA审批：钉钉流程与页面对接"
source_url: "https://open.dingtalk.com/document/development/use-the-dingtalk-oa-approval-process-and-page-interface"
namespace: "development"
slug: "use-the-dingtalk-oa-approval-process-and-page-interface"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 标准版 > 官方OA审批：钉钉流程与页面对接"
doc_id: "Dv4RnLILxO"
updated_at: "2026-10-12 18:04:36"
---

> Source: https://open.dingtalk.com/document/development/use-the-dingtalk-oa-approval-process-and-page-interface
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 标准版 > 官方OA审批：钉钉流程与页面对接
> Updated: 2026-10-12 18:04:36

# 官方OA审批：钉钉流程与页面对接

## 概述

本文档展示了如何创建一个企业内部应用，使用钉钉官方OA审批相关API，将业务系统的审批流程集成到钉钉端内。通过创建/更新审批模板、发起/撤销审批实例、处理审批任务、管理审批附件等API，以及审批实例和任务的回调事件，实现在钉钉端内打开官方OA审批详情页进行审批的场景。

### 方案背景

企业自研或采购的业务系统通常拥有独立的审批流程和页面，员工需要在多个系统间切换处理审批，导致操作割裂、效率低下。通过将业务系统审批对接到钉钉官方OA审批中心，用户可在钉钉统一入口查看和处理所有审批，享受标准化的一站式体验：

- **多系统切换效率低**：员工需在业务系统和钉钉之间反复切换处理审批，操作繁琐且容易遗漏紧急事项。
- **审批状态不同步**：业务系统与钉钉端数据不一致，审批进度无法实时可视，导致决策延误。
- **通知渠道分散**：审批通知依赖各系统内部消息或邮件，无法利用钉钉的统一待办提醒和消息推送能力。
- **管理层查询困难**：管理者需分别登录多个系统查看审批进展，无法在钉钉内统一掌握全局审批状态。

### 核心价值

本方案通过复用钉钉官方OA审批的流程引擎和表单组件能力，为企业提供标准化的审批体验：

- **更标准**：使用钉钉OA流程和页面能力，无缝连接钉钉聊天、待办、通知，实现高效审批。
- **一站式体验**：复用钉钉官方审批引擎和表单组件，为用户提供多端统一的OA审批产品体验。
- **深度集成**：支持与钉钉消息、待办、钉盘等核心能力无缝连接，审批结果通过回调事件实时同步至业务系统。
- **降低开发成本**：无需自建审批引擎和表单设计器，直接复用钉钉成熟能力，快速完成审批流程上线。

### 适用场景

以下典型场景适合采用本方案进行审批流程集成：

- **制造业生产工单审批**：MES系统发起工单审批时自动创建钉钉审批实例，审批人在钉钉端内直接查看工单详情并完成操作。
- **连锁零售门店运营审批**：各门店店长在业务系统中提交申请后，审批流程自动汇聚至钉钉OA审批中心统一管理。
- **集团化企业跨部门协作**：总部与分支机构通过钉钉统一审批入口处理各类业务申请，提升协同效率。
- **已有成熟审批系统的企业**：希望复用钉钉原生审批引擎和表单组件，同时保留业务系统发起和管理能力的场景。

## 典型业务场景

### 场景一：制造业生产工单审批集成

#### 痛点分析

某制造企业自研MES系统管理生产工单流转，原有审批流程依赖线下签字和邮件确认，效率低且难以追溯。员工需要在MES系统和钉钉之间反复切换，审批状态无法实时同步，导致生产进度延误：

- 员工需在MES系统和钉钉之间反复切换处理审批，操作繁琐且容易遗漏紧急工单。
- 审批状态依赖人工同步，MES系统与钉钉端数据不一致，导致生产进度延误。
- 管理层无法在钉钉内统一查看工单审批进展，需分别登录多个系统查询。
- 审批通知依赖邮件或线下沟通，无法利用钉钉的统一待办提醒和消息推送能力。

#### 价值验证

- **自动化流程**

  ![制造业生产工单审批集成场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6749971971/p1104839.png)
- **关键优势**

  - **生产工单审批集成：** MES系统发起工单审批时自动创建钉钉审批实例，审批人在钉钉端内直接查看工单详情并完成操作，无需跨系统切换。
  - **审批流程实时可视：** 钉钉端内展示完整的工单数据（含物料清单、质检要求、历史工单），审批进度一目了然，支持评论和催办。
  - **数据同步全链路：** 审批结果实时回写MES系统，驳回时自动取消下游待办，确保两端数据一致且可追溯，审批时效提升60%以上。

### 场景二：连锁零售门店运营审批

#### 痛点分析

某连锁零售企业在全国拥有数百家门店，门店装修、促销活动、人员调动等审批事项频繁。各门店店长提交申请后，审批流程分散在多个系统中，区域经理和总部负责人难以统一处理，审批响应时间长：

- 各门店店长需在多个业务系统中分别提交申请，操作繁琐且容易遗漏关键信息。
- 审批流程分散在不同系统，区域经理和总部负责人需登录多个平台逐一处理，效率低下。
- 审批通知依赖各系统内部消息，无法利用钉钉的统一待办提醒和消息推送能力。
- 管理层无法在钉钉内统一查看所有门店审批进展，需分别登录多个系统查询统计。

#### 价值验证

- **自动化流程**

  ![连锁零售门店运营审批场景图_20261009_165105](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6749971971/p1104840.png)
- **关键优势**

  - **门店审批统一入口：** 各门店店长在业务系统中提交申请后，审批流程自动汇聚至钉钉OA审批中心，区域经理和总部负责人在钉钉端内统一处理所有审批事项。
  - **待办消息实时触达：** 借助钉钉待办提醒和消息通知能力，审批任务第一时间推送至审批人，避免遗漏紧急审批事项。
  - **审批响应提速80%：** 审批响应时间从平均2天缩短至4小时内，大幅提升了门店运营决策效率，支撑数百家门店的高效管理。

## 实施指南

### 技术架构

本方案的技术架构包含以下核心组件：

- **身份鉴权层**：负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **审批模板管理层**：负责审批表单模板的创建、更新和查询，将业务系统的审批表单结构同步至钉钉OA审批中心。
- **审批实例引擎**：负责审批实例的发起、撤销和状态管理，承载审批流程的生命周期控制。
- **审批任务处理层**：负责任务节点的查询、同意、拒绝和转交操作，驱动审批流程在各节点间流转。
- **附件与评论服务**：负责审批钉盘空间的授权、文件上传下载以及审批评论的管理，支持富媒体审批交互。
- **事件回调通道**：负责将审批任务和实例的状态变更事件推送至业务系统，实现审批数据的实时双向同步。

### 前置条件

- **应用准备**：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Instance.Write`（工作流实例写权限）
  - `Workflow.Instance.Read`（工作流实例读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### 代码实现

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请"OA审批"相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端OA审批相关API。

1. 调用服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，创建官方OA审批模板并获取模板唯一编码processCode。
2. 调用服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口，根据模板编码发起审批实例并获取实例标识instanceId。
3. 调用服务端API-[获取审批钉盘空间信息](0501-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间上传权限和spaceId。
4. 调用客户端JSAPI-[uploadAttachmentToDingTalk](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)接口，将审批附件上传至钉盘空间。
5. 调用服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口，为审批实例添加评论和附件。
6. 调用服务端API-[授权下载审批钉盘文件](0503-download-the-approval-nail-file.md)接口，获取审批钉盘文件的下载授权。
7. 调用服务端API-[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口，获取审批附件的预览授权。
8. 调用服务端API-[下载审批附件](0504-download-an-approval-attachment.md)接口，获取附件下载链接downloadUri。
9. 调用服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情和各任务节点taskId。
10. 调用服务端API-[同意或拒绝审批任务](0505-approve-or-reject-the-approval-task.md)接口，对指定任务节点执行同意或拒绝操作。
11. 调用服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)接口，撤销已发起的审批实例。
12. 订阅[审批任务变更回调事件](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)，接收审批任务开始、结束、转交等状态变更通知。
13. 订阅[审批实例变更回调事件](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)，接收审批实例开始、结束、终止、删除等状态变更通知。

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

1. **创建或更新审批表单模板：**管理员可在OA管理后台手动操作创建，或调用新版服务端API-[创建或更新审批表单模板](0490-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > - 业务系统若没有保存接口返回的模板编码`processCode`，可登录钉钉管理后台查看获取。
   > - 创建模板成功后，可在钉钉OA审批管理后台，**查看/编辑**官方OA审批单模板、查看/搜索模板数据、导出/删除模板数据等。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7949463871/p838408.png)

   ```
   {
     "name": "使用钉钉OA审批流程和页面对接",
     "description": "可在业务系统发起流程，调用钉钉官方OA审批相关接口创建钉钉OA审批流程，在钉钉端打开钉钉审批详情页处理流程。",
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

   - `name`：审批表单模板名称。
   - `description`：审批表单模板描述。
   - `formComponents`：表单控件列表，定义审批表单的结构和字段。
   - `templateConfig`：模板配置项，控制审批单的显示和行为。

   **返回字段：**

   - `processCode`：审批模板唯一编码。
2. **发起审批实例**：通过OA审批官方应用手动发起审批，或根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0496-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。

   > **[!NOTE]**
   >
   > 发起审批实例成功后，可在钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。

   ```
   {
       "processCode": "PROC-C512D64A-60F6-4F83-B708-xxx",
       "originatorUserId": "manager98xx",
       "deptId": -1,
       "microappAgentId": 348925476,
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

   - `processCode`：审批模板唯一编码。
   - `originatorUserId`：发起人的用户ID。
   - `formComponentValues`：表单控件值列表，对应模板中定义的各字段。
   - `approvers`：审批人列表，指定各节点的审批人和操作方式。

   **返回字段：**

   - `instanceId`：审批实例唯一标识。
3. **添加审批评论附件**：若需要添加审批评论附件，需先将文件上传至审批钉盘空间，再调用新版服务端API-[添加审批评论](0499-official-approval-adds-approval-comments.md)接口。具体使用教程参考：[OA审批流接入：添加审批评论与终止审批](0478-comment-and-revoke-approval-flow.md)。

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

      **请求参数：**

      - `processInstanceId`：审批实例唯一标识。
      - `commentUserId`：添加评论的用户ID。
      - `text`：评论文本内容。
      - `file`：评论附件信息，包含钉盘文件和图片列表。

      **返回字段：**

      - `result`：操作结果标识。
4. **预览下载审批附件**：若需要预览/下载附件，可调用服务端API-[授权下载审批钉盘文件](0503-download-the-approval-nail-file.md)接口、[授权预览审批附件](0502-official-authorized-preview-approval-attachment.md)接口，进行审批钉盘文件的授权操作，再调用服务端API-[下载审批附件](0504-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。具体使用教程参考：[OA审批流接入：附件审批的下载与预览](0480-new-version-of-attachment-approval-process.md)。
5. **获取单个审批实例详情****：**审批人可通过钉钉OA审批中心、钉钉待办中心手动操作同意/拒绝审批任务；或业务系统根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0497-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情，获取审批任务各个任务节点信息`taskId`。
6. **同意或拒绝审批任务**：根据审批实例`instanceId`和相应的任务节点`taskId`信息，调用新版服务端API-[同意或拒绝审批任务](0505-approve-or-reject-the-approval-task.md)接口，实现审批任务的操作，所有审批节点同意后，则该审批单通过。

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

   - `processInstanceId`：审批实例唯一标识。
   - `taskId`：审批任务节点标识。
   - `actionerUserId`：执行审批操作的用户ID。
   - `result`：审批结果，agree表示同意，refuse表示拒绝。

   **返回字段：**

   - `result`：操作结果标识。
7. **撤销审批实例**：查看审批后，若发现提交的审批单有误需撤销该审批实例，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0498-revoke-an-approval-instance.md)，实现审批单的撤销操作。

   ```
   {
       "isSystem": true,
       "processInstanceId": "oKPAxjtgSP-AqeVTk-xxxx",
       "operatingUserId": "manager98xx",
       "remark": "撤销审批实例"
   }
   ```
8. **审批回调事件订阅**：审批单状态发生变化后，OA审批支持将[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧，可以让企业应用能够更深度地与钉钉平台集成，实现信息共享和业务协同。具体使用教程参考：[事件订阅操作指南](0014-event-subscription-overview.md)。

**实施完成检查清单**

- ✅应用Client ID和Client Secret已获取并妥善保管。
- ✅ OA审批相关权限（模板读写、实例读写、任务读写）已申请并通过。
- ✅ accessToken获取接口调用成功，凭证有效期内可正常使用。
- ✅ 审批模板创建成功，processCode已保存至业务系统配置。
- ✅ 审批实例发起成功，instanceId可用于后续任务操作。
- ✅ 钉钉OA审批中心可查看审批实例并执行审批操作。
- ✅ 审批评论附件上传及下载功能验证通过。
- ✅ 审批任务和实例回调事件订阅配置完成，状态变更可实时推送。

## 常见问题（FAQ）

- **Q1：创建审批模板时，formComponents中的componentId有什么要求？**

  componentId在表单内必须唯一，无业务语义，用于标识控件。若需要使用业务标识，可使用bizAlias字段替代。
- **Q2：发起审批实例时，approvers中的actionType有哪些取值？**

  actionType支持NONE（单人审批）、OR（或签，任一审批人同意即通过）、AND（会签，所有审批人均需同意）等取值，具体以API文档为准。
- **Q3：如何获取未保存的processCode？**

  若未保存创建审批模板时返回的processCode，可登录钉钉OA审批管理后台查看获取，或调用获取模板code接口查询。
- **Q4：审批附件上传需要先获取钉盘空间信息吗？**

  是的。添加审批评论附件前，需先调用获取审批钉盘空间信息接口获取spaceId和上传权限，再通过JSAPI上传文件至钉盘空间，最后调用添加审批评论接口关联附件。
- **Q5：审批回调事件如何配置？**

  需在开放平台控制台配置事件订阅，选择"审批任务变更"和"审批实例变更"两类事件，填写业务系统的回调URL。具体操作参考[配置事件推送方式](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md)。
