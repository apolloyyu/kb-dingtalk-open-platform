---
title: "创建、获取、查询及审批宜搭审批单"
source_url: "https://open.dingtalk.com/document/development/suitable-for-the-basic-operation-process-of-approval"
namespace: "development"
slug: "suitable-for-the-basic-operation-process-of-approval"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 使用教程 > 创建、获取、查询及审批宜搭审批单"
doc_id: "F3JUb2d9be"
updated_at: "2026-05-15 09:04:55"
---

> Source: https://open.dingtalk.com/document/development/suitable-for-the-basic-operation-process-of-approval
> Path: 应用开发 / 服务端 API / 宜搭 > 使用教程 > 创建、获取、查询及审批宜搭审批单
> Updated: 2026-05-15 09:04:55

# 创建、获取、查询及审批宜搭审批单

本文档介绍了如何调用宜搭相关接口实现宜搭审批操作的相关流程。首先创建一个企业内部应用，再使用宜搭提供的API，实现创建宜搭审批单、获取宜搭审批单详情、查询宜搭审批流节点信息、同意或拒绝宜搭审批单流程。

## **预期效果**

- 发起审批界面，如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0530708661/p515965.png)
- 撤销审批界面，如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0530708661/p515967.png)
- 同意审批后界面，如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0530708661/p515969.png)

## 流程简介

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)并获取AppKey和AppSecret。

步骤二：根据[添加接口调用权限](0003-add-api-permission.md)说明，申请相应的权限。

步骤三：调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口，获取应用访问凭证。

步骤四：调用服务端宜搭相关API。

1. 调用服务端API-[发起宜搭审批流程](0311-api-startinstance-v2.md)接口，创建宜搭审批单流程，获取宜搭审批单的流程实例formInstanceId。
2. 根据审批单流程实例formInstanceId，实现审批单实例操作流程：

   1. 根据审批单流程实例formInstanceId，调用服务端API-[终止流程实例](0308-terminate-a-process-instance.md)接口，实现宜搭审批单撤销操作。
   2. 如需删除流程实例数据，调用服务端API-[删除流程实例](0309-delete-the-process-instance.md)接口，实现删除宜搭审批单数据信息。
   3. 实现宜搭审批单同意或拒绝流程：

      1. 根据审批单流程实例formInstanceId，调用服务端API-[根据流程实例ID获取流程实例](0315-api-getinstancebyid-v2.md)接口，获取宜搭审批单的详情信息。
      2. 根据审批单流程实例formInstanceId，调用服务端API-[查询流程运行任务（VPC）](0346-query-process-running-tasks-vpc.md)接口，获取宜搭审批单的节点信息taskId。
      3. 根据审批单流程实例formInstanceId和任务节点taskId，调用服务端API-[同意或拒绝宜搭审批任务](0345-execute-approval-tasks.md)接口，执行同意或者拒绝宜搭审批单。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   - 应用类型：选择H5微应用。
   - 开发方式：选择企业自主开发。![0815创建企业内部应用 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5513450661/p477411.png)

## 步骤二：获取AppKey和AppSecret

获取应用AppKey和AppSecret信息。![0815获取Appkey值 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5513450661/p477413.png)

## 步骤三：添加接口权限

[申请宜搭接口权限](0003-add-api-permission.md)，搜索“宜搭”，申请相应接口的权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0530708661/p515937.png)

## 步骤四：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[旧版API VS 新版API](https://open.dingtalk.com/document/development/how-to-call-apis#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

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

## 步骤五：调用服务端宜搭相关API

1. 调用服务端API-[发起宜搭审批流程](0311-api-startinstance-v2.md)接口，创建宜搭审批单流程，获取宜搭审批单的流程实例formInstanceId。

   ```
   public void processesInstancesStart() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);
           StartInstanceHeaders startInstanceHeaders = new StartInstanceHeaders();
           startInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           StartInstanceRequest startInstanceRequest = new StartInstanceRequest()
                   .setAppType("APP_IE*****SY47KISEL8RXQ")
                   .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
                   .setUserId("manager7675")
                   .setLanguage("zh_CN")
                   .setFormUuid("FORM-4W8667*******C7UFKA0Q5TH83BZJ2OAALQ")
                   .setFormDataJson("{\"textField_laao2rcb\": \"测试单行输入框\",\"textareaField_laao2rcc\": \"测试多行输入框\",\"numberField_laao2rcd\": 50,\"radioField_laao2rce\": \"选项一\",\"checkboxField_laao2rcf\": [\"选项一\",\"选项二\"],\"cascadeDateField_laao2rcl\": [\"1668063209000\",\"1668066809000\"],\"attachmentField_laao2rcm\": [{\"downloadUrl\":\"/ossFileHandle?appType=APP_IE*****SY47KISEL8RXQ&fileName=APP_IE*****SY47KISEL8RXQ_bWFuYWdlcjc2NzVfNU85NjZHRDFQQkM1NjI0SjdJTUZQNFUwU0E4STM1SkVYT0FBTFVX.png&instId=&type=download&originalFileName=mylike.png\",\"name\":\"mylike.png\",\"previewUrl\":\"/ossFileHandle?appType=APP_IE*****SY47KISEL8RXQ&fileName=APP_IE*****SY47KISEL8RXQ_bWFuYWdlcjc2NzVfNU85NjZHRDFQQkM1NjI0SjdJTUZQNFUwU0E4STM1SkVYT0FBTFVX.png&instId=&type=open\",\"size\":5909,\"url\":\"/ossFileHandle?appType=APP_IE*****SY47KISEL8RXQ&fileName=APP_IE*****SY47KISEL8RXQ_bWFuYWdlcjc2NzVfNU85NjZHRDFQQkM1NjI0SjdJTUZQNFUwU0E4STM1SkVYT0FBTFVX.png&instId=&type=download\"}],\"employeeField_laao2rcn\":[\"manager7675\"]}")
                   .setProcessCode("TPROC--4W8667D1*******UFKA0Q5TH83CZJ2OAALR");
           try {
               StartInstanceResponse startInstanceResponse = client.startInstanceWithOptions(startInstanceRequest, startInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(startInstanceResponse.getBody()));
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
2. 根据审批单流程实例formInstanceId，实现审批单实例操作流程：

   1. 根据审批单流程实例formInstanceId，调用服务端API-[终止流程实例](0308-terminate-a-process-instance.md)接口，实现宜搭审批单撤销操作。

      ```
      public void  instancesTerminate() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);
              TerminateInstanceHeaders terminateInstanceHeaders = new TerminateInstanceHeaders();
              terminateInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
              TerminateInstanceRequest terminateInstanceRequest = new TerminateInstanceRequest()
                      .setAppType("APP_IE*****SY47KISEL8RXQ")
                      .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
                      .setUserId("manager7675")
                      .setLanguage("zh_CN")
                      .setProcessInstanceId("9a198552-306c-49f3-88b2-52d90843018b");
              try {
                  client.terminateInstanceWithOptions(terminateInstanceRequest, terminateInstanceHeaders, new RuntimeOptions());
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
   2. 如需删除流程实例数据，调用服务端API-[删除流程实例](0309-delete-the-process-instance.md)接口，实现删除宜搭审批单数据信息。

      ```
      public void instancesDelete() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);
              DeleteInstanceHeaders deleteInstanceHeaders = new DeleteInstanceHeaders();
              deleteInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
              DeleteInstanceRequest deleteInstanceRequest = new DeleteInstanceRequest()
                      .setAppType("APP_IE*****SY47KISEL8RXQ")
                      .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
                      .setUserId("manager7675")
                      .setLanguage("zh_CN")
                      .setProcessInstanceId("9a198552-306c-49f3-88b2-52d90843018b");
              try {
                 client.deleteInstanceWithOptions(deleteInstanceRequest, deleteInstanceHeaders, new RuntimeOptions());
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
   3. 实现宜搭审批单同意或拒绝流程：

      1. 根据审批单流程实例formInstanceId，调用服务端API-[根据流程实例ID获取流程实例](0315-api-getinstancebyid-v2.md)接口，获取宜搭审批单的详情信息。

         ```
          public void instancesInfos() throws Exception {
                 Config config = new Config();
                 config.protocol = "https";
                 config.regionId = "central";
                 com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);
                 GetInstanceByIdHeaders getInstanceByIdHeaders = new GetInstanceByIdHeaders();
                 getInstanceByIdHeaders.xAcsDingtalkAccessToken = "accessToken";
                 GetInstanceByIdRequest getInstanceByIdRequest = new GetInstanceByIdRequest()
                         .setAppType("APP_IE*****SY47KISEL8RXQ")
                         .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
                         .setUserId("manager7675")
                         .setLanguage("zh_CN");
                 try {
                     GetInstanceByIdResponse instanceByIdWithOptions = client.getInstanceByIdWithOptions("9a3f8aa3-2bf4-49a9-9789-a4b78aaf64a6", getInstanceByIdRequest, getInstanceByIdHeaders, new RuntimeOptions());
                     System.out.println(JSON.toJSONString(instanceByIdWithOptions.getBody()));
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
      2. 根据审批单流程实例formInstanceId，调用服务端API-[查询流程运行任务（VPC）](0346-query-process-running-tasks-vpc.md)接口，获取宜搭审批单的节点信息taskId。

         ```
         public void RunningTasks() throws Exception {
                 Config config = new Config();
                 config.protocol = "https";
                 config.regionId = "central";
                 com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);
                 GetRunningTasksHeaders getRunningTasksHeaders = new GetRunningTasksHeaders();
                 getRunningTasksHeaders.xAcsDingtalkAccessToken = "accessToken";
                 GetRunningTasksRequest getRunningTasksRequest = new GetRunningTasksRequest()
                         .setProcessInstanceId("9a3f8aa3-2bf4-49a9-9789-a4b78aaf64a6")
                         .setAppType("APP_IE*****SY47KISEL8RXQ")
                         .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
                         .setLanguage("zh_CN")
                         .setUserId("manager7675");
                 try {
                     GetRunningTasksResponse runningTasksWithOptions = client.getRunningTasksWithOptions(getRunningTasksRequest, getRunningTasksHeaders, new RuntimeOptions());
                     System.out.println(JSON.toJSONString(runningTasksWithOptions.getBody()));
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
      3. 根据审批单流程实例formInstanceId和任务节点taskId，调用服务端API-[同意或拒绝宜搭审批任务](0345-execute-approval-tasks.md)接口，执行同意或者拒绝宜搭审批单。

         ```
         public void tasksExecute() throws Exception {
                 Config config = new Config();
                 config.protocol = "https";
                 config.regionId = "central";
                 com.aliyun.dingtalkyida_1_0.Client client = new com.aliyun.dingtalkyida_1_0.Client(config);
                 ExecuteTaskHeaders executeTaskHeaders = new ExecuteTaskHeaders();
                 executeTaskHeaders.xAcsDingtalkAccessToken = "accessToken";
                 ExecuteTaskRequest executeTaskRequest = new ExecuteTaskRequest()
                         .setOutResult("AGREE")
                         .setAppType("APP_IE*****SY47KISEL8RXQ")
                         .setSystemToken("TD666Z91R3A5******JY150439DO3T0A2OAALWS")
                         .setLanguage("zh_CN")
                         .setRemark("确认同意")
                         .setProcessInstanceId("9a3f8aa3-2bf4-49a9-9789-a4b78aaf64a6")
                         .setUserId("manager7675")
                         .setTaskId(5578876505L);
                 try {
                     client.executeTaskWithOptions(executeTaskRequest, executeTaskHeaders, new RuntimeOptions());
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

> **[!NOTE]**
>
> 如果宜搭审批单调用过[转交任务](0341-transfer-tasks.md)接口，taskId值是会发生变化，调用[同意或拒绝宜搭审批任务](0345-execute-approval-tasks.md)接口时，需要再次调用[查询流程运行任务（VPC）](0346-query-process-running-tasks-vpc.md)接口，获取最新的taskId值。
