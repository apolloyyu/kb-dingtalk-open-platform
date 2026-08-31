---
title: "自有OA审批：三方流程与页面对接"
source_url: "https://open.dingtalk.com/document/development/use-three-party-process-and-page-docking"
namespace: "development"
slug: "use-three-party-process-and-page-docking"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > 自有OA审批：三方流程与页面对接"
doc_id: "jRJBkTCOOK"
updated_at: "2026-07-10 10:11:15"
---

> Source: https://open.dingtalk.com/document/development/use-three-party-process-and-page-docking
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > 自有OA审批：三方流程与页面对接
> Updated: 2026-07-10 10:11:15

# 自有OA审批：三方流程与页面对接

## 场景介绍

### **方案说明**

**自有OA审批集成模式：使用三方流程和页面对接。**可在业务系统发起流程，调用钉钉**自有OA审批相关接口**创建钉钉OA审批流程，在钉钉端打开业务系统审批详情页处理流程。

### **方案特点&价值**

**更轻量**

1、接入简单，直接在钉钉端内打开业务系统页面审批。

2、只有同意拒绝等基础操作，无和钉钉连接操作，如拉群。

3、延续用户原来使用的流程和页面习惯，低成本快速使用。

## 业务流程

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8516224271/p835389.png)

## **实现效果**

- **支持从钉钉OA审批列表打开业务系统审批详情页审批**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5749463871/p835391.png)
- **支持从钉钉待办打开业务系统审批详情页审批**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5749463871/p835392.png)

## 开发流程

### **流程图**

以企业开发一个内部应用实现能力集成举例，实现业务系统发起，钉钉端内打开业务系统详情页进行审批。具体实现流程如下图所示：**（注意此场景下，审批任务的同步流程是按步骤5执行的）**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8516224271/p835394.png)

### **接入流程简介**

本文档展示了，创建一个企业内部应用，使用OA审批流程中心提供的API，通过创建/更新/删除三方审批模板、创建/更新审批实例、创建/更新/查询审批待办任务、清理OA审批数据等API，实现业务系统发起，钉钉端内打开业务系统详情页进行集成的场景案例。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. **同步审批模板数据到钉钉：**调用新版服务端API-[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，获取模板的唯一编码`processCode`。**注意：该场景下无需设置processFeatureConfig流程中心集成相关配置，默认会以打开业务系统详情页方式进行审批。**

   ```
   {

     "name": "使用三方流程和页面对接钉钉OA",
     "description": "钉钉OA审批支持将外部系统（企业自研或采购的第三方系统）的审批任务推送到钉钉审批应用，用户在钉钉审批中即可统一查看和处理所有审批、享受一站式的审批体验。",
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
       "templateConfig": {
           "hiddenProcess": true,
           "createInstanceMobileUrl": "https://www.dingtalk.com",
           "createInstancePcUrl": "https://www.dingtalk.com",
           "templateEditUrl": "https://www.dingtalk.com",
           "disableSendCard": false
       }
   }
   ```
2. 如果没有保存`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。
3. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
4. **同步审批实例数据到钉钉：**根据模板编码`processCode`，调用新版服务端API-[创建实例](0513-create-a-ticket-approval-instance.md)接口发起审批实例，获取审批实例`processInstanceId`。

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
     "title": "使用三方流程和页面对接钉钉OA",
     "processCode": "PROC-39B555F8-FFC6-4CCC-AC5F-xxx",
     "originatorUserId": "manager9814",
     "url": "http://www.dingtalk.com",
     "notifiers": [
       {
         "userid": "manager9814",
         "position": "start"
       }
     ],
     "bizData": "{\"apiKey\":\"apiKey\",\"appUuid\":\"appUuid\",\"version\":\"1\"}"
   }
   ```
5. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
6. **同步审批任务数据到钉钉：**根据审批实例`processInstanceId`和待办事项列表tasks，调用[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。**注意：该场景下同步的审批任务将会以打开业务系统详情页方式进行审批。**

   ```
   {
     "processInstanceId": "zG1X1zwFTEiwzI0JB5w38A0964172381_xxxx",
     "activityId": "activityId_xxx",
     "tasks": [
       {
         "userId": "manager9814",
         "url": "https://www.dingtalk.com"
       }
     ]
   }
   ```
7. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
8. **同步审批任务状态到钉钉：**根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
9. **同步审批实例状态到钉钉：**根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0514-update-instance-status.md)或 [批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。
10. 最后，若需要对审批模板数据进行清理，可以调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

## 客户案例

中集瑞江作为中集集团信息化自研试点中心，内部自研了MES、IOT、SRM等十几个独立运作的业务系统，各系统独立承载特定职能数据和工作流程。然而，这种高度专业化分工的模式在提升单点业务效率的同时，也导致了企业内部信息流的碎片化与断裂问题，阻碍了整体运营效率的优化提升及跨部门协同效应的有效发挥。面对这一深层次的体系性挑战，中集瑞江充分利用了钉钉开放平台的深度整合能力。  
  
通过对接钉钉开放平台，中集瑞江成功将自研业务系统中的审批流程、待办事项以及各类关键工作通知与钉钉无缝集成。这一举措不仅消除了各系统间的壁垒，实现了数据资源的高度共享和流程自动化，而且极大地简化了员工日常操作步骤，显著提升了单一流程处理速度。更为重要的是，这种一体化的协同办公模式增强了企业的响应能力和决策效率，构建了业务中枢，推进了整个组织内信息流通的顺畅度与协同工作的连贯性，进而推动企业数字化转型进程，打造高效协同、智能互联的现代化办公体验。

客户案例：[查看更详细介绍](https://page.dingtalk.com/wow/tianyuan/act/toufang?wh_showError=true&caseId=NTMzNg==)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5749463871/p835396.png)
