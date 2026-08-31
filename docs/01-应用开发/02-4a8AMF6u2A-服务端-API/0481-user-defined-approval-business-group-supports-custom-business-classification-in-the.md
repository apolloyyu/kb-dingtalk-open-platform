---
title: "自定义审批业务分组：待办中心业务分类"
source_url: "https://open.dingtalk.com/document/development/user-defined-approval-business-group-supports-custom-business-classification-in-the"
namespace: "development"
slug: "user-defined-approval-business-group-supports-custom-business-classification-in-the"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > 自定义审批业务分组：待办中心业务分类"
doc_id: "NHfanAGPFC"
updated_at: "2026-07-10 10:11:23"
---

> Source: https://open.dingtalk.com/document/development/user-defined-approval-business-group-supports-custom-business-classification-in-the
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > 自定义审批业务分组：待办中心业务分类
> Updated: 2026-07-10 10:11:23

# 自定义审批业务分组：待办中心业务分类

## **场景介绍**

客户希望把多个三方系统的审批任务都集中在钉钉审批中心，做一站式沉浸审批。同时希望**支持自定义审批业务分类**，将三方系统内的业务分组信息同步到钉钉OA审批，并生成对应的**【钉钉待办—OA审批】分类下的二级业务来源分组**。让审批人在钉钉待办中心查阅三方业务系统来源待办更清晰，为用户、特别是审批事项繁多的管理层带来超级体验。

## **业务流程**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925432.png)

## **实现效果**

支持在待办中心自定义业务分类，查阅三方业务系统来源待办更清晰。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925455.png)

## **开发流程**

### **流程图**

以企业开发一个内部应用实现能力集成举例，实现三方业务系统发起，钉钉端内打开业务系统详情页进行审批，并支持自定义审批业务分组。具体实现流程如下图所示：**（注意此场景下，若只需要自定义审批分组，不需要自定义快捷审批按钮，则步骤14之后的流程都不涉及）**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925476.png)

详细流程，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925475.png)

### **接入流程简介**

本文档展示了，创建一个企业内部应用，使用OA审批流程中心提供的API，通过创建/删除业务分组、创建/更新/删除三方审批模板、创建/更新审批实例、创建/更新/查询审批待办任务、清理OA审批数据等API，实现业务系统发起，钉钉端内打开业务系统详情页进行集成，**并支持自定义审批业务分组的场景案例。**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. **同步审批业务分组到钉钉：**调用新版服务端API-[创建或更新业务分组](0540-api-premiuminsertorupdatedir.md)接口，获取分组`dirId`。可以将三方系统内的业务分组信息同步到钉钉OA审批，并生成对应的钉钉待办里OA审批分类下的二级分类。后续在同步待处理任务至钉钉时，可支持指定待办任务所属的业务分组信息，让审批人在查阅三方业务系统来源待办更清晰。

   ```
   请求示例：
   {
     "operateUserId":"manager9814",
     "bizGroup":"administeration",
     "name": "测试",
     "name18n": "{\"en_US\":\"test\",\"ja_JP\":\"test\",\"vi_VN\":\"test\",\"zh_CN\":\"测试\",\"zh_HK\":\"测试\",\"zh_TW\":\"测试\"}",
     "description": "自定义审批业务分组测试"
   }

   返回示例：
   {
     "result": {
       "bizGroup": "348925476_administeration20250210",
       "dirId": "194e436699fe71353fc1f3d498f80e66"
     },
     "success": true
   }
   ```
2. **同步审批模板数据到钉钉：**调用新版服务端API-[保存流程中心外部集成审批模板](0542-api-premiumsaveintegratedprocess.md)接口，获取模板的唯一编码`processCode`。

   **注意：该场景下需通过processFeatureConfig流程中心集成配置中的****AFFILIATION\_DIR****进行配置步骤1返回的dirId分组信息，请求示例如下：**

   ```
   {
     "name": "快捷审批",
     "description": "保存流程中心外部集成审批模板 (高级版专享接口)",
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
       }
     ],
     "processFeatureConfig": {
       "features": [
         {
           "name": "AFFILIATION_DIR",
           "runType": "OUTBIZ_CUSTOM",
           "config": "{\"dirId\":\"194e436699fe71353fc1f3d498f80e66\"}"
         }
       ]
     }
   }
   ```
3. 如果没有保存`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。
4. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. **同步审批实例数据到钉钉：**根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0543-api-premiumexternalintegrationprocessinstance.md)接口发起审批实例，获取审批实例`processInstanceId`。

   **注意：该场景也支持实例维度指定集成配置，通过featureConfig进行配置步骤1返回的dirId分组信息 ，请求示例如下：**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925959.png)

   ```
   {
     "formComponentValueList": [
       {
         "name": "单行输入框",
         "value": "[钉钉](https://www.dingtalk.com/)"
       }
     ],
     "title": "自定义分组快捷审批",
     "processCode": "PROC-3602AF75-58DE-4862-9946-321DE45BBAEE",
     "originatorUserId": "manager9814",
     "url": "http://www.dingtalk.com",
     "featureConfig": {
       "features": [
         {
           "name": "AFFILIATION_DIR",
           "runType": "OUTBIZ_CUSTOM",
           "config": "{\"dirId\":\"194e436699fe71353fc1f3d498f80e66\"}"
         }
       ]
     }
   }
   ```
6. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. **同步审批任务数据到钉钉：**根据审批实例`processInstanceId`和待办事项列表tasks，调用[保存流程中心外部集成审批实例](0543-api-premiumexternalintegrationprocessinstance.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务，**对应的待办任务将在步骤4指定的业务分组中出现。**

   **注意：该场景下不指定自定义快捷审批按钮配置的话，同步的审批任务将会以打开业务系统详情页方式进行审批。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925960.png)

   ```
   {
       "processInstanceId": "skFv-tLeTTWObq_vWiezew09641738995784",
       "activityId": "0210-1",
       "tasks": [
           {
               "userId": "manager9814",
               "url": "https://www.dingtalk.com"
           }
       ]
   }
   ```
8. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
9. **同步审批任务状态到钉钉：**根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
10. **同步审批实例状态到钉钉：**根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)或 [审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)接口，更新实例状态。
11. **删除业务分组：**若需要删除业务分组，可以调用[删除业务分组](0541-api-premiumdeldir.md)接口，将三方系统同步到钉钉OA审批的分组信息进行删除，并同时删除对应的钉钉待办里OA审批分类下的二级分类，对应分类下的钉钉待办数据将移动至OA审批分类下的【其他】分组。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8884471471/p925961.png)
12. 最后，若需要对审批模板数据进行清理，可以调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。
