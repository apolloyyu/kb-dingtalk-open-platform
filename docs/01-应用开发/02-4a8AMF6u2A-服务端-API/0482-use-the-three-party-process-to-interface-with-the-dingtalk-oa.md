---
title: "审批页面托管：三方流程与钉钉页面对接"
source_url: "https://open.dingtalk.com/document/development/use-the-three-party-process-to-interface-with-the-dingtalk-oa"
namespace: "development"
slug: "use-the-three-party-process-to-interface-with-the-dingtalk-oa"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > 审批页面托管 > 审批页面托管：三方流程与钉钉页面对接"
doc_id: "LCCWJvMCnZ"
updated_at: "2026-07-10 10:11:25"
---

> Source: https://open.dingtalk.com/document/development/use-the-three-party-process-to-interface-with-the-dingtalk-oa
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > 审批页面托管 > 审批页面托管：三方流程与钉钉页面对接
> Updated: 2026-07-10 10:11:25

# 审批页面托管：三方流程与钉钉页面对接

## 场景介绍

### 方案说明

**审批页面托管集成模式：使用三方流程和钉钉OA审批页面对接。**

1、可在业务系统发起流程，基于钉钉官方OA审批提供的**审批单据详情页搭建能力**，调用钉钉接口**用三方流程业务数据渲染钉钉OA审批页面**，在钉钉端打开钉钉官方OA审批详情页处理流程。

2、使用该解决方案依赖部分OA审批高级版专享OpenAPI，需要开通钉钉OA审批高级版才可申请使用。

### **方案特点&价值**

**更灵活**

1、灵活对接，将不同业务系统的审批单结构、样式统一，为用户提供多端（移动端/PC/平板）一致体验。

2、托管后可0成本实现与钉钉IM、待办等一方功能打通，拥有多个提升审批效率和体验的功能，实现三方即一方的审批体验。且详情页中的审批操作区按钮（同意、拒绝、转交等）可支持由三方业务灵活自定义配置。

3、托管后三方审批流转情况将汇集到钉钉官方审批效率看板中，管理层可通过流程效率统计报告全方位诊断企业的审批效率和合理性。

### **适用场景**

客户业务系统自有流程引擎，希望以自有OA审批模式集成钉钉审批，但自有业务系统没有pc端/移动端详情页面。希望能复用钉钉官方OA审批详情页样式，用统一的审批界面集成自己的待办和审批，以解决现在各系统审批界面不统一的问题，提升体验。同时希望审批操作区按钮可灵活自定义配置，满足不同业务定制化诉求。

场景1：如果公司存在审批系统不支持移动端/h5页面，使得员工尤其是管理层，无法在钉钉场景下审批。通过审批托管可以低成本拥有优秀的钉钉多端（移动端/PC/平板）统一审批体验。

场景2：如果公司审批人希望审批与钉钉一方功能更好的打通，提高审批的效率，托管后的一键拉群、分享到聊天、复制链接到聊天/文档、打印、下载等功能可以0成本拥有，而这些功能单独开发要大量人日的开发成本。

场景3：如果公司的管理层提出希望对公司的流程效率进行系统分析治理，托管后的效率诊断和流程挖掘，可以系统的发现效率、流程合理性等问题，并基于钉钉的流程治理实践，给出优化建议。

## 业务流程

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3716224271/p835400.png)

## **实现效果**

- 支持三方业务使用钉钉官方统一详情页样式，低成本拥有钉钉一方功能

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5849463871/p844675.png)
- 支持三方业务自定义配置/渲染审批操作区按钮（同意、拒绝等），且可透出三方业务执行异常报错文案详情

  红框部分为审批详情页中的主要操作区，通俗的说就是审批的主要操作按钮，在审批单托管模式中此部分区域可由三方业务实现自定义灵活配置。

  | image | image |
  | --- | --- |
- 支持查看流程效率统计报告

  流程效率统计报告相关数据，可以通过OA审批助手推送 或 移动端—OA审批—统计 模块查看。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5849463871/p844680.png)

## 开发流程

### **流程图**

以企业开发一个内部应用实现能力集成举例，实现审批页面托管模式集成：即在业务系统发起流程，基于钉钉官方OA审批提供的**审批单据详情页搭建能力**，调用钉钉接口**用三方流程业务数据渲染钉钉OA审批页面**，在钉钉端打开钉钉官方OA审批详情页处理流程。具体实现流程如下图所示：

三方业务在创建审批模板/创建审批实例时可注册审批操作区自定义渲染按钮&提交请求的回调，因此需要提供两个接口用于托管渲染和处理用户请求。一个用于回调三方获取操作区按钮数据的定义（按钮渲染），一个用于回调三方接口进行接收和处理用户的审批提交操作（操作审批）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1405165271/p844682.png)

详细流程，如下图所示：

![审批托管完整流程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1405165271/p844706.png)

### **接入流程简介**

本文档展示了，创建一个企业内部应用，使用OA审批流程中心页面托管集成模式相关的API，通过创建/更新/删除三方审批模板、创建/更新审批实例、注册审批操作区自定义按钮渲染/执行回调、创建/更新/查询审批待办任务等API，实现业务系统发起，钉钉端内打开自定义审批详情页进行审批单据托管集成的场景案例。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. **注册自定义审批操作按钮区callback回调接口：**一个用于回调三方获取操作区按钮数据的定义（按钮渲染），一个用于回调三方接口进行接收和处理用户的审批提交操作（操作审批）。接口协议详细参考：[审批操作区托管接口协议详解](0483-detailed-explanation-of-hosting-interface-agreement-in-approval-operation-area.md)。
2. **同步审批模板数据到钉钉****：**调用新版服务端API-[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)，获取模板的唯一编码`processCode`。

   **注意：该场景需对processFeatureConfig中的CUSTOM\_ACTION\_DEFINITION（表示获取操作区按钮数据的回调地址，即按钮渲染回调）、CUSTOM\_ACTION\_APPLY（表示进行审批操作时回调的回调地址，即操作审批回调）模块进行自定义配置。**

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
3. 如果没有保存`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。
4. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. **同步审批实例数据到钉钉：**根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批任务](0544-api-premiumsaveintegratedtask.md)发起审批实例，获取审批实例`processInstanceId`。

   **注意：若在创建审批模板时未注册自定义审批操作按钮相关配置，也支持在创建实例维度进行指定，若同时在模板/实例维度进行了配置，优先以实例维度为准。**

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
6. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. **同步审批任务数据到钉钉：**根据审批实例`processInstanceId`和待办事项列表tasks，调用[保存流程中心外部集成审批任务](0544-api-premiumsaveintegratedtask.md)，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。

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
8. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
9. **自定义同意/拒绝审批任务：**审批人从钉钉端打开自定义审批页进行审批时，操作同意/拒绝等功能模块，将会回调[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)接口中**CUSTOM\_ACTION\_APPLY**模块中配置的回调接口，三方在执行自身业务逻辑完之后，需主动同步任务状态至钉钉。根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。

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
10. **同步审批实例状态到钉钉：**根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0514-update-instance-status.md)或 [批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。
11. 最后，若需要对审批模板数据进行清理，可以调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。
