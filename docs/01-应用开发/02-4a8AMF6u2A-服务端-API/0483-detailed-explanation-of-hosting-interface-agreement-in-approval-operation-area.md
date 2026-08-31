---
title: "审批操作区托管接口协议详解"
source_url: "https://open.dingtalk.com/document/development/detailed-explanation-of-hosting-interface-agreement-in-approval-operation-area"
namespace: "development"
slug: "detailed-explanation-of-hosting-interface-agreement-in-approval-operation-area"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > 审批页面托管 > 审批操作区托管接口协议详解"
doc_id: "yUlBMf9JNL"
updated_at: "2026-07-10 10:11:27"
---

> Source: https://open.dingtalk.com/document/development/detailed-explanation-of-hosting-interface-agreement-in-approval-operation-area
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > 审批页面托管 > 审批操作区托管接口协议详解
> Updated: 2026-07-10 10:11:27

# 审批操作区托管接口协议详解

## 审批操作区介绍

红框部分为审批详情页中的主要操作区，通俗的说就是审批的主要操作按钮，在审批单托管模式中此部分区域可由三方业务实现自定义灵活配置。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7849463871/p844719.png)

## **审批操作区机制说明**

三方业务在创建审批模板/创建审批实例时可注册审批操作区自定义渲染按钮&提交请求的回调，因此需要提供两个接口用于托管渲染和处理用户请求。一个用于回调三方获取操作区按钮数据的定义（按钮渲染），一个用于回调三方接口进行接收和处理用户的审批提交操作（操作审批）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1405165271/p844682.png)

## **核心模型定义**

- **ProcessFeatureConfig 流程中心集成配置**

  以流程中心模式集成时，通过该配置支持三方进行自定义配置某些业务功能模块的实现逻辑，在此基础上，审批页面托管方案支持详情页中整个审批操作区按钮由三方业务灵活自定义，因此需新增两个回调接口配置，CUSTOM\_ACTION\_DEFINITION用于回调三方获取操作区按钮数据的定义（按钮渲染），CUSTOM\_ACTION\_APPLY用于回调三方接口进行接收和处理用户的审批提交操作（操作审批）。

  ```
  "featureConfig":{
    "features":  [
      {
        // 表示获取操作区（按钮）数据的回调地址（按钮渲染）
        "name":"CUSTOM_ACTION_DEFINITION",  
        "runType":"OUTBIZ_CUSTOM",
        "callback":{
          "apiKey":"customActionDefinitionApiKey",
          "appUuid":"appUuid",
          "version":"1"
        }
      },
      {
        // 表示进行审批操作时回调的回调地址（操作审批）
        "name":"CUSTOM_ACTION_APPLY",  
        "runType":"OUTBIZ_CUSTOM",
        "callback":{
          "apiKey":"customActionApplyApiKey",
          "appUuid":"appUuid",
          "version":"1"
        }
      }
    ]
  }
  ```
- **CustomActionDefinition 自定义操作按钮**

  - **详情页操作区详解**

    | 官方OA审批：  分享、下载、打印、再次提交、编辑模板  同意、拒绝、修改、撤销、转交、加签、退回、评论、发起群聊、自动化、删除审批单  image | 流程中心ORIGIN托管模式：  分享、下载、打印  同意、拒绝、评论、建群讨论、删除、返回原表单  image |
    | --- | --- |
  - **详情页操作区按钮分类**

    - ##### **通用按钮**

      指钉钉OA审批单详情页托管平台默认提供的按钮能力，可直接复用，不需要接入方回传数据。交互以默认实现为准，支持业务方配置按钮是否展示。

      | 按钮标识【actionType】 | 能力 | 交互形态类型 | 说明 |
      | --- | --- | --- | --- |
      | INSTANCE\_SHARE | 分享审批单到群聊 | 点击唤起选群组件，确定后执行回调 | 交互以默认实现为准，支持业务方配置按钮是否展示。 |
      | INSTANCE\_DOWNLOAD | 下载审批单，文件将以工作通知发送 | 点击执行回调，同时弹出提示框 | 交互以默认实现为准，支持业务方配置按钮是否展示。 |
      | INSTANCE\_PRINT | 打印审批单 | 点击弹出按钮组 | 交互以默认实现为准，支持业务方配置按钮是否展示。 |
      | INSTANCE\_DING | 催办：审批流程发起人，向当前节点审批人发送催办消息 | 点击唤起发DING组件 | 交互以默认实现为准，支持业务方配置按钮是否展示。 |
      | INSTANCE\_IM\_GROUP | 基于实例建群讨论 | 点击弹出选人组件，选人后弹出二次确认框 | 交互以默认实现为准，支持业务方配置按钮是否展示。 |
      | INSTANCE\_COMMENT | 评论审批单 | 点击弹出评论二次确认框 | 交互以默认实现为准，支持业务方配置按钮是否展示。 |
    - ##### **预定义按钮**

      指单据托管预置的一些审批操作按钮，自动实现了一些常用的交互机制，这些按钮需要业务方根据当前流程和人员的情况按需传递，实际的能力由接入方进行实现，可能在不同的流程引擎上会有少许差异。

      | 按钮标识【actionType】 | 能力 | 说明 |
      | --- | --- | --- |
      | TASK\_APPROVE | 同意审批任务 | 交互固定。按钮文案、回调实现逻辑支持自定义 |
      | TASK\_REJECT | 拒绝审批任务 | 交互固定。按钮文案、回调实现逻辑支持自定义 |
      | TASK\_FORWARD | 转交审批任务 | 交互固定。按钮文案、可选人员列表、回调实现逻辑支持自定义 |
      | TASK\_APPEND | 加签 | 交互固定。按钮文案、加签审批人可选人员列表、加签方式、回调实现逻辑支持自定义 |
      | INSTANCE\_REVERT | 退回 | 交互固定。按钮文案、退回到节点列表、回调实现逻辑支持自定义 |
      | INSTANCE\_MODIFY | 修改审批单 | 交互固定。按钮文案、是否置灰、置灰原因等支持自定义 |
      | INSTANCE\_TERMINATE | 撤销审批单 | 交互固定。按钮文案、二次确认提示文案、回调实现逻辑支持自定义 |
      | INSTANCE\_DELETE | 删除审批单 | 交互固定。按钮文案、二次确认提示文案、回调实现逻辑支持自定义 |
      | INSTANCE\_EXTERNAL\_DETAIL | 返回原表单：审批详情页展示外部详情页跳转按钮 | 交互固定。按钮文案、是否展示支持自定义 |
    - ##### **业务自定义按钮**

      指三方接入系统自行定义的按钮，可以通过简单的配置，让这些按钮拥有类似于预定义按钮的样式，在用户点击时，通过审批操作接口，将数据回调到接入方的系统上，执行自定义的操作逻辑。

      | 按钮标识【actionType】 | 能力 | 交互形态类型 | 说明 |
      | --- | --- | --- | --- |
      | CUSTOM\_ACTION\_xxx | 业务自定义按钮 | 平台可支持的标准交互类型  - link：直接跳转） - confirm：二次确认框 - modal：打开弹窗（弹窗内的组件内容可支持业务自定义 | 不能与托管平台的预留标识重名 |
  - **按钮排序、渲染规则**

    托管平台默认对接入方传的按钮进行排序修饰。

    - 检查是否需要增加通用按钮，如果是，则由托管平台增加
    - 回调三方获取操作区按钮数据的定义（按钮渲染），按三方返回的数据进行渲染；回调异常则按现有ORIGIN托管方案中已有按钮做兜底。（分享、下载、打印、同意、拒绝、评论、建群讨论、删除、返回原表单）
    - 全部按钮排序

      - 通用按钮按照特定顺序排在前面
      - 预定义按钮+自定义按钮按照传入顺序跟在后面
- **CustomActionDefinition 模型解析**

  根据以上审批操作区各按钮分类和交互形态，抽象定义操作按钮模型如下：

  | **名称** | **类型** | **含义** | **说明** |
  | --- | --- | --- | --- |
  | actions | list | 审批动作按钮 |  |
  | ∟context | string | 业务方定义的审批上下文，ApplyAction 接口中透传。 | 上下文是指业务方自行定义的一个字符串。当审批回调时，会回传此字符串，帮助业务方理解当前场景信息。 |
  | ∟actionKey | string | 业务方定义的操作 Key，ApplyAction 接口中透传，如配置，需在 actions 数组中唯一。 | 非必须，默认可不传。 |
  | ∟actionType | string | 审批动作的类型，即按钮类型 | 枚举。详见【**详情页操作区按钮分类**】ProcessFeatureEnum枚举 |
  | ∟name | i18n | 审批动作的名称 | 非必须，默认可不传。不传为`actionType`的默认名称。 |
  | ∟icon | string | 按钮icon | 非必须，默认可不传。不传为默认icon图标。  支持传url类型，icon尺寸大小需符合钉钉侧设计规范要求。 |
  | ∟hidden | boolean | 是否隐藏按钮 | 平台内置的通用按钮（分享、下载、打印、评论、建群等）支持业务配置为隐藏 |
  | ∟disabled | boolean | 禁用 | 前端变灰不能点 |
  | ∟disabledReason | i18n | 禁用原因 | 禁用后，tips展示此文案 |
  | ∟primary | boolean | 是否是主按钮 | 主按钮会变大，如同意拒绝按钮。界面同时超过2个后会降级为普通按钮 |
  | ∟behavior | string | 打开方式，可选 | 枚举。详见BehaviorType枚举  - link 打开链接 - modal 打开弹窗 - confirm 打开二次确认框 |
  | ∟behaviorProps | object |  | behavior打开方式对应的具体行为属性  - link类型，需配置具体的打开链接url值 - modal类型，需配置弹窗中具体表单控件schema内容 - confirm类型，需配置二次确认框中的标题和提示文案 |
  | ∟title | string | 标题，可选（behavior为confirm类型时需配置该值） |  |
  | ∟message | string | 提示文案，可选（behavior为confirm类型时需配置该值） |  |
  | ∟link | string | 打开链接，可选（behavior为link类型时需配置该值） |  |
  | ∟schema | json Array  [{  componentName: 'TextareaField',  **props: {**  **id: 'comment',**  **},**  }] | 弹窗中的表单定义组件列表（behavior为modal类型时需配置该值） | 参考[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)中的【**FormComponent参数补充说明**】  - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **TextNote**：文字说明控件 - **DDPhotoField**：图片控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件    - users string[] staffId列表 |
  | ∟componentName | string | 控件类型 |  |
  | ∟props | json | 控件属性 | {  "label": "单行输入框", // 控件标题  "placeholder": "请输入", // 输入提示  "componentId": "TextField\_17EZKEGSOCTC0", // 控件id，表单内唯一，无业务语义  "required": false, // 是否必填，默认非必填  "bizAlias": "staffId" // 控件的业务标识，表单内唯一，与componentId二选一  } |
  | ∟value | string | 控件值 | 参考[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)中的示例 |

  - **详情页操作区按钮分类枚举 ProcessFeatureEnum**

    ```
    public enum ProcessFeatureEnum {
      /**
      * 删除任务
      */
      TASK_DELETE,

      /**
      * 转交任务
      */
      TASK_FORWARD,

      /**
      * 任务加签
      */
      TASK_APPEND,

      /**
      * 任务签阅
      */
      TASK_SIGN,

      /**
      * 分享审批单
      */
      INSTANCE_SHARE,

      /**
      * 审批单下载
      */
      INSTANCE_DOWNLOAD,

      /**
      * 打印审批单
      */
      INSTANCE_PRINT,

      /**
      * 再次提交审批单
      */
      INSTANCE_RESUBMIT,

      /**
      * 发起审批
      */
      INSTANCE_START,

      /**
      * 删除审批实例
      */
      INSTANCE_DELETE,

      /**
      * 展示详情页
      */
      INSTANCE_DETAIL,

      /**
      * 撤销审批单
      */
      INSTANCE_TERMINATE,

      /**
      * 修改审批单
      */
      INSTANCE_MODIFY,

      /**
      * 插销修改
      */
      INSTANCE_REVOKE_MODIFY,

      /**
      * 评论审批单
      */
      INSTANCE_COMMENT,

      /**
      * 基于实例建群讨论
      */
      INSTANCE_IM_GROUP,

      /**
      * 审批单退回
      */
      INSTANCE_REVERT,

      /**
      * 催办
      */
      INSTANCE_DING,

      /**
      * 审批详情页展示外部详情页跳转按钮
      */
      INSTANCE_EXTERNAL_DETAIL
    }
    ```
  - **按钮交互行为类型枚举 CustomActionBehaviorTypeEnum**

    ```
    public enum CustomActionBehaviorTypeEnum {
        /**
         * 打开链接
         */
        LINK("link"),

        /**
         * 打开弹窗
         */
        MODAL("modal"),

        /**
         * 打开二次确认框
         */
        CONFIRM("confirm")
    }
    ```
  - **弹窗中的表单定义组件列表（behavior为modal类型时需配置该值）**

    参考[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)中的【**FormComponent参数补充说明**】，当前支持以下表单组件类型：

    - **TextField**：单行输入框
    - **TextareaField**：多行输入框
    - **DDSelectField**：单选框
    - **DDMultiSelectField**：多选框
    - **TextNote**：文字说明控件
    - **DDPhotoField**：图片控件
    - **DDAttachment**：附件
    - **InnerContactField**：联系人控件

      - users string[] staffId列表
- **CustomActionDefinition 模型示例**

  ```
  {
    "code": 200,
    "body": [
      {
        "actionKey": "default",
        "actionType": "INSTANCE_COMMENT",
        "name": "评论审批单",
        "hidden": true
      },
      {
        "actionKey": "default",
        "actionType": "INSTANCE_DING",
        "name": "催办",
        "disabled": true,
        "disabledReason": "当前审批单不支持此功能"
      },
      {
        "actionKey": "custom",
        "actionType": "INSTANCE_EXTERNAL_DETAIL",
        "name": "返回原表单",
        "icon": "icon1",
        "primary": false,
        "behavior": "link",
        "behaviorProps": {
          "link": "https://www.dingtalk.com"
        }
      },
      {
        "actionKey": "general",
        "actionType": "TASK_APPROVE",
        "name": "同意",
        "icon": "icon1",
        "primary": true,
        "behavior": "modal",
        "behaviorProps": {
          "schema": [
            {
              "componentName": "TextareaField",
              "props": {
                "label": "评论意见",
                "placeholder": "请输入多行文本内容，需要换行时请输入\r\n",
                "id": "TextareaField_comment",
                "required": true,
                "bizAlias": "comment",
                "value": "这是审批意见评论内容\r\n"
              }
            }
          ]
        },
        "context": "{\"command_id\":\"HandleCommand_2\",\"task_id\":\"1xxxxx6-2xx6-4xxd-bxxf-6xxxxxxxxf\",\"node_id\":\"UserTask_4\"}",
        "disabled": false
      },
      {
        "key": "general",
        "actionType": "TASK_FORWARD",
        "name": "同意并转交",
        "icon": "icon2",
        "primary": true,
        "behavior": "modal",
        "behaviorProps": {
          "schema": [
            {
              "componentName": "InnerContactField",
              "props": {
                "label": "转交人",
                "placeholder": "请选择转交人",
                "id": "InnerContactField_forward_user",
                "choice": "1",
                "required": false,
                "bizAlias": "taskForward",
                "users": "[\"0135185610551036178639\",\"0135185610551036178639\"]",
                "value": "[\"0135185610551036178639\"]"
              }
            },
            {
              "componentName": "TextareaField",
              "props": {
                "label": "评论意见",
                "placeholder": "请输入多行文本内容，需要换行时请输入\r\n",
                "id": "TextareaField_comment",
                "required": true,
                "bizAlias": "comment",
                "value": "这是审批意见评论内容\r\n"
                          }
                      }
                  ]
              },
              "context": "{\"command_id\":\"HandleCommand_2\",\"task_id\":\"1xxxxx6-2xx6-4xxd-bxxf-6xxxxxxxxf\",\"node_id\":\"UserTask_4\"}",
              "disabled": false
          }
      ]
  }
  ```

## 接入步骤示例

### **步骤一：注册自定义操作按钮回调**

1. 注册自定义审批操作按钮callback回调示例。

   ```
   {
     // 表示获取操作区（按钮）数据的回调地址（按钮渲染）
     "name": "CUSTOM_ACTION_DEFINITION",
     "runType": "OUTBIZ_CUSTOM",
     "callback": {
       "apiKey": "getIntegratedCustomActionDefinitions",
       "appUuid": "dingecxxxx97fcb1e09",
       "version": "1"
     }
   },
   {
     // 表示进行审批操作时回调的回调地址（操作审批）
     "name": "CUSTOM_ACTION_APPLY",
     "runType": "OUTBIZ_CUSTOM",
     "callback": {
       "apiKey": "applxxxxction",
       "appUuid": "dingecxxxxb1e09",
       "version": "1"
     }
   }
   ```
2. 流程中心获取审批操作区自定义按钮列表。

   - apiKey：getIntegratedCustomActionDefinitions
   - URL：https://connector.dingtalk.com/webhook/flow/d8c375d76acb7eb01019fe0b
   - 参数：corpId,processInstanceId,activityId,taskId,operator,platform,locale,context,customData
   - apiSecret：getIntegratedCustomActionDefinitions

     **请求示例**

     ```
     {
         "activityId": "001",
         "processInstanceId": "fR7Adxxxx1716975",
         "corpId": "dingecxxxxcb1e09",
         "locale": "zh_CN",
         "operator": "manager9814",
         "platform": "pc",
         "taskId": 876xxxx3607,
         "customData": "{\"apiKey\":\"customActionDefinitionApiKey2\",\"appUuid\":\"appUuid2\",\"version\":\"2\"}"
     }
     ```

     **成功响应示例**

     ```
     {
       "success": true,
       "errorCode": "",
       "errorMessage": "",
       "result": [
         {
           "actionKey": "custom",
           "actionType": "INSTANCE_EXTERNAL_DETAIL",
           "name": "返回原表单",
           "icon": "icon1",
           "primary": false,
           "behavior": "link",
           "behaviorProps": {
             "link": "https://www.dingtalk.com"
           }
         },
         {
           "actionKey": "custom",
           "actionType": "INSTANCE_DELETE",
           "name": "删除审批单",
           "icon": "icon1",
           "primary": false,
           "behavior": "confirm",
           "behaviorProps": {
             "title": "确认删除审批单吗？",
             "message": "删除后不可恢复，请三思"
           }
         },
         {
           "actionKey": "general",
           "actionType": "TASK_APPROVE",
           "name": "同意",
           "icon": "icon1",
           "primary": true,
           "behavior": "modal",
           "behaviorProps": {
             "schema": [
               {
                 "componentName": "TextareaField",
                 "props": {
                   "label": "评论意见",
                   "placeholder": "请输入多行文本内容，需要换行时请输入\r\n",
                   "id": "TextareaField_comment",
                   "required": true,
                   "bizAlias": "comment",
                   "value": "这是审批意见评论内容\r\n"
                 }
               }
             ]
           },
           "context": "{\"command_id\":\"HandleCommand_2\",\"task_id\":\"1xxxxx6-2xx6-4xxd-bxxf-6xxxxxxxxf\",\"node_id\":\"UserTask_4\"}",
           "disabled": false
         },
         {
           "key": "general",
           "actionType": "TASK_FORWARD",
           "name": "同意并转交",
           "icon": "icon2",
           "primary": true,
           "behavior": "modal",
           "behaviorProps": {
             "schema": [
               {
                 "componentName": "InnerContactField",
                 "props": {
                   "label": "转交人",
                   "placeholder": "请选择转交人",
                   "id": "InnerContactField_forward_user",
                   "choice": "0",
                   "required": false,
                   "bizAlias": "taskForward",
                   "users": [
                     "0213523642-1025002834",
                     "14516942141077447"
                   ]
                 }
               },
               {
                 "componentName": "TextareaField",
                 "props": {
                   "label": "评论意见",
                   "placeholder": "请输入多行文本内容，需要换行时请输入\r\n",
                   "id": "TextareaField_comment",
                   "required": true,
                   "bizAlias": "comment",
                   "value": "这是审批意见评论内容\r\n"
                 }
               }
             ]
           },
           "context": "{\"command_id\":\"HandleCommand_2\",\"task_id\":\"1xxxxx6-2xx6-4xxd-bxxf-6xxxxxxxxf\",\"node_id\":\"UserTask_4\"}",
           "disabled": false
         }
       ]
     }
     ```

     **异常返回示例**

     ```
     {
         "success": false,
         "errorCode": "FORM_SPI_CUSTOM_ERROR",
         "errorMessage": "三方回调获取审批操作区自定义按钮列表异常",
         "result": []
     }
     ```
3. 流程中心执行自定义按钮审批操作。

   - apiKey：applyIntegratedCustomAction
   - URL：https://connector.dingtalk.com/webhook/flow/a8d743d0afd948bd5d9dc2a8
   - 参数：corpId,processInstanceId,activityId,taskId,operator,platform,locale,context,customData,formDataArray,actionKey,actionType
   - apiSecret：applyIntegratedCustomAction

     **请求示例**

     ```
     {
       "activityId": "001",
       "processInstanceId": "fR7Adw93Rxxxx716975",
       "corpId": "dingecxxxxfcb1e09",
       "locale": "zh_CN",
       "operator": "manager9814",
       "platform": "pc",
       "taskId": 87622494607,
       "customData": "{\"apiKey\":\"customActionDefinitionApiKey2\",\"appUuid\":\"appUuid2\",\"version\":\"2\"}"
     }
     ```

     **成功响应示例**

     ```
     {
       "success": true,
       "errorCode": "",
       "errorMessage": "",
       "result": [
         {
           "actionKey": "custom",
           "actionType": "INSTANCE_EXTERNAL_DETAIL",
           "name": "返回原表单",
           "icon": "icon1",
           "primary": false,
           "behavior": "link",
           "behaviorProps": {
             "link": "https://www.dingtalk.com"
           }
         },
         {
           "actionKey": "custom",
           "actionType": "INSTANCE_DELETE",
           "name": "删除审批单",
           "icon": "icon1",
           "primary": false,
           "behavior": "confirm",
           "behaviorProps": {
             "title": "确认删除审批单吗？",
             "message": "删除后不可恢复，请三思"
           }
         },
         {
           "actionKey": "general",
           "actionType": "TASK_APPROVE",
           "name": "同意",
           "icon": "icon1",
           "primary": true,
           "behavior": "modal",
           "behaviorProps": {
             "schema": [
               {
                 "componentName": "TextareaField",
                 "props": {
                   "label": "评论意见",
                   "placeholder": "请输入多行文本内容，需要换行时请输入\r\n",
                   "id": "TextareaField_comment",
                   "required": true,
                   "bizAlias": "comment",
                   "value": "这是审批意见评论内容\r\n"
                 }
               }
             ]
           },
           "context": "{\"command_id\":\"HandleCommand_2\",\"task_id\":\"1xxxxx6-2xx6-4xxd-bxxf-6xxxxxxxxf\",\"node_id\":\"UserTask_4\"}",
           "disabled": false
         },
         {
           "key": "general",
           "actionType": "TASK_FORWARD",
           "name": "同意并转交",
           "icon": "icon2",
           "primary": true,
           "behavior": "modal",
           "behaviorProps": {
             "schema": [
               {
                 "componentName": "InnerContactField",
                 "props": {
                   "label": "转交人",
                   "placeholder": "请选择转交人",
                   "id": "InnerContactField_forward_user",
                   "choice": "0",
                   "required": false,
                   "bizAlias": "taskForward",
                   "users": [
                     "0213523642-1025002834",
                     "14516942141077447"
                   ]
                 }
               },
               {
                 "componentName": "TextareaField",
                 "props": {
                   "label": "评论意见",
                   "placeholder": "请输入多行文本内容，需要换行时请输入\r\n",
                   "id": "TextareaField_comment",
                   "required": true,
                   "bizAlias": "comment",
                   "value": "这是审批意见评论内容\r\n"
                 }
               }
             ]
           },
           "context": "{\"command_id\":\"HandleCommand_2\",\"task_id\":\"1xxxxx6-2xx6-4xxd-bxxf-6xxxxxxxxf\",\"node_id\":\"UserTask_4\"}",
           "disabled": false
         }
       ]
     }
     ```

     **异常返回示例**

     ```
     {
       "success": false,
       "errorCode": "FORM_SPI_CUSTOM_ERROR",
       "errorMessage": "三方回调获取审批操作区自定义按钮列表异常",
       "result": []
     }
     ```

### **步骤二：保存流程中心审批模板**

**同步审批模板数据到钉钉：**调用新版服务端API-[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)，获取模板的唯一编码`processCode`。

> **[!NOTE]**
>
> 该场景需对processFeatureConfig中的CUSTOM\_ACTION\_DEFINITION（表示获取操作区按钮数据的回调地址，即按钮渲染回调）、CUSTOM\_ACTION\_APPLY（表示进行审批操作时回调的回调地址，即操作审批回调）模块进行自定义配置。

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

### **步骤三：保存流程中心审批实例**

**同步审批实例数据到钉钉**：根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0543-api-premiumexternalintegrationprocessinstance.md)发起审批实例，获取审批实例`processInstanceId`。

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

### **步骤四：保存流程中心审批任务**

**同步审批任务数据到钉钉：**根据审批实例`processInstanceId`和待办事项列表tasks，调用[保存流程中心外部集成审批任务](0544-api-premiumsaveintegratedtask.md)，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。

```
{
  "processInstanceId": "snfwBxxxx392174",
  "activityId": "001",
  "tasks": [
    {
      "userId": "manager9814",
      "url": "https://www.dingtalk.com"
    },
    {
      "userId": "013xxxx639",
      "url": "https://www.dingtalk.com"
    }
  ]
}
```

### **步骤五：更新流程中心审批任务状态**

**自定义同意/拒绝审批任务：**审批人从钉钉端打开自定义审批页进行审批时，操作同意/拒绝等功能模块，将会回调[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)接口中`CUSTOM_ACTION_APPLY`模块中配置的回调接口，三方在执行自身业务逻辑完之后，需主动同步任务状态至钉钉。根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。

```
{
  "processInstanceId": "qZpLKAxxxx43810",
  "tasks": [
    {
      "taskId": 88094338042,
      "status": "COMPLETED",
      "result": "AGREE"
    }
  ]
}
```
