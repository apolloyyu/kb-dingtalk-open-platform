---
title: "审批流程托管：钉钉流程与三方页面对接"
source_url: "https://open.dingtalk.com/document/development/approval-process-hosting-integration-mode-use-the-dingtalk-official-oa"
namespace: "development"
slug: "approval-process-hosting-integration-mode-use-the-dingtalk-official-oa"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 官方OA 审批 > 审批流程托管：钉钉流程与三方页面对接"
doc_id: "cIjO2lxlyi"
updated_at: "2026-07-10 10:11:39"
---

> Source: https://open.dingtalk.com/document/development/approval-process-hosting-integration-mode-use-the-dingtalk-official-oa
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 官方OA 审批 > 审批流程托管：钉钉流程与三方页面对接
> Updated: 2026-07-10 10:11:39

# 审批流程托管：钉钉流程与三方页面对接

## **场景介绍**

### **方案说明**

**审批流程托管集成模式：使用钉钉官方OA审批流程和三方自研页面对接。**可在业务系统发起流程，调用钉钉**官方OA审批相关接口**创建钉钉OA审批流程，**并指定第三方审批系统中审批单详情页跳转地址**，然后在钉钉端打开钉钉审批详情页时就会**跳转到对应业务系统详情页**中处理流程。

### **方案特点&价值**

**更灵活**

1、灵活对接，使用钉钉OA审批官方工作流 + 三方业务自研页面集成。**可直接复用钉钉官方OA审批流程引擎的工作流能力**，无缝和钉钉聊天、待办、通知连接，高效审批。

2、审批详情页采用三方业务自研页面，**用于满足三方部分业务表单页面较复杂的场景**。无需把所有表单控件字段同步至钉钉，简化对接成本，延续用户原来使用的流程和页面习惯，低成本快速使用。

## **业务流程**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2294471471/p927000.png)

## **实现效果**

- 支持直接复用钉钉官方OA审批的工作流引擎能力

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9949463871/p926996.png)
- 支持从业务系统发起流程，调用钉钉官方OA审批接口创建OA审批流程

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9949463871/p926994.png)
- 支持指定三方业务系统详情页面，从钉钉OA审批/待办/消息卡片等入口直接打开业务系统自研页面审批

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9949463871/p926995.png)

## **开发流程**

### **流程图**

![企业系统和钉钉工作流打通开发流程 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9949463871/p926993.png)

### **接入流程简介**

本文档展示了，创建一个企业内部应用，使用**官方OA审批**相关API，通过创建/更新官方审批模板、发起/撤销/评论审批实例、同意/拒绝/转交审批任务、上传/下载审批附件等API，以及官方OA审批实例/审批任务回调事件。实现业务系统发起，**并指定第三方审批系统中审批单详情页跳转地址**进行集成的场景案例，**用于满足三方业务自研页面 + OA审批官方工作流集成的复杂业务场景诉求。**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. **创建官方OA审批模板：**管理员可在OA管理后台手动操作创建；或业务系统调用新版服务端API-[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。若没有保存接口返回的模板编码`processCode`，可登录钉钉管理后台查看获取。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9949463871/p926992.png)

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
2. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看/**编辑**官方OA审批单模板、查看/搜索模板数据、导出/删除模板数据等。
3. **发起官方OA审批实例：**三方业务系统可根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0497-create-an-approval-instance.md)接口发起审批实例，**并指定第三方审批系统中审批单详情页跳转地址****进行集成**（若指定了bizDetailPageUrl，在钉钉OA审批、钉钉待办、消息卡片等入口点击跳转时，将会直接跳转对应业务系统详情页地址），获取审批实例`instanceId`。

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
4. 发起审批实例成功后，用户可进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
5. **添加审批评论附件：**若需要添加审批评论附件，需先将文件上传至审批钉盘空间，再调用新版服务端API-[添加审批评论](0500-official-approval-adds-approval-comments.md)接口。具体使用教程参考：[评论及撤销审批流](0485-comment-and-revoke-approval-flow.md)。
6. 需先调用新版服务端API-[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
7. 调用客户端JSAPI-[uploadAttachmentToDingTalk](../03-Ogu5SlPY4t-客户端-JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息，本流程示例使用[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10318)实现。
8. 获取审批钉盘空间spaceId后，可根据审批实例`instanceId`，调用新版服务端API-[添加审批评论](0500-official-approval-adds-approval-comments.md)接口，实现审批单的添加评论操作。

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
9. **预览下载审批附件：**若需要预览/下载附件，可调用服务端API-[授权下载审批钉盘文件](0504-download-the-approval-nail-file.md)、[授权预览审批附件](0503-official-authorized-preview-approval-attachment.md)接口，进行审批钉盘文件的授权操作，再调用服务端API-[下载审批附件](0505-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。具体使用教程参考：[审批附件的操作流程](0487-new-version-of-attachment-approval-process.md)。
10. **同意/拒绝审批任务：**审批人可通过钉钉OA审批中心、钉钉待办中心、OA审批消息卡片手动操作同意/拒绝审批任务；或业务系统根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情，获取审批任务各个任务节点信息`taskId`。
11. 根据审批实例`instanceId`和相应的任务节点`taskId`信息，调用新版服务端API-[同意或拒绝审批任务](0506-approve-or-reject-the-approval-task.md)接口，实现审批任务的操作，所有审批节点同意后，则该审批单通过。

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
12. 撤销官方OA审批实例：查看审批后，若发现提交的审批单有误需撤销该审批实例，可根据审批实例`instanceId`，调用新版服务端API-[撤销审批实例](0499-revoke-an-approval-instance.md)，实现审批单的撤销操作。

    ```
    {
        "isSystem": true,
        "processInstanceId": "oKPAxjtgSP-AqeVTk-xxxx",
        "operatingUserId": "manager98xx",
        "remark": "撤销审批实例"
    }
    ```
13. 审批单状态发生变化后，OA审批支持将[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)和[审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)等回调事件推送至业务系统侧，可以让企业应用能够更深度地与钉钉平台集成，实现信息共享和业务协同。具体使用教程参考：[事件订阅操作指南](0014-event-subscription-overview.md)。
