---
title: "创建、更新和获取自由任务"
source_url: "https://open.dingtalk.com/document/development/teambition-free-task-operation-process"
namespace: "development"
slug: "teambition-free-task-operation-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 使用教程 > 创建、更新和获取自由任务"
doc_id: "3BLXr0Tomu"
updated_at: "2026-07-20 09:21:51"
---

> Source: https://open.dingtalk.com/document/development/teambition-free-task-operation-process
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 使用教程 > 创建、更新和获取自由任务
> Updated: 2026-07-20 09:21:51

# 创建、更新和获取自由任务

本文档展示了，创建一个企业内部应用，使用Teambition项目管理提供的API，实现自由任务的相关操作流程

## **预期效果**

创建自有任务后，界面如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1150154871/p525634.png)

## **流程简介**

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，点击应用开发-企业内部开发，根据[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)文档，创建企业内部应用。

步骤二：单击基础信息 > 应用信息，获取应用AppKey和AppSecret。

步骤三：根据[添加接口调用权限](0003-add-api-permission.md)文档，搜索“项目”，申请项目管理的接口权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤五：调用项目管理相关API：

1. 创建自由任务：

   1. 调用服务端API-[创建自由任务](1242-create-a-free-task.md)接口，实现自由任务创建，获取自由任务ID。
2. 自由任务管理相关操作：

   - 根据自由任务ID，调用服务端API-[更新自由任务的优先级](1250-change-free-task-priority.md)接口，实现自由任务优先级更新操作。
   - 根据自由任务ID，调用服务端API-[更新自由任务标题](1246-change-free-task-title.md)接口，实现自由任务标题更新操作。
   - 根据自由任务ID，调用服务端API-[更新自由任务截止时间](1251-change-free-task-deadline.md)接口，实现自由任务截止时间更新操作。
   - 根据自由任务ID，调用服务端API-[更新自由任务执行者](1249-change-free-task-executor.md)接口，实现自由任务执行者更新操作。
   - 根据自由任务ID，调用服务端API-[增加或删除自由任务的参与者](1252-change-task-participant.md)接口，实现自由任务参与者更新操作。
   - 根据自由任务ID，调用服务端API-[更新自由任务备注](1248-update-free-task-notes.md)接口，实现自由任务备注更新操作。
   - 根据自由任务ID，调用服务端API-[更新自由任务状态](1247-change-free-task-status.md)接口，实现完成自由任务。
3. 自由任务查询相关操作：

   - 根据自由任务ID，调用服务端API-[获取自由任务详情](1243-queries-free-task-details.md)接口，实现获取单个自由任务的详细信息。
   - 根据自由任务ID，调用服务端API-[批量获取自由任务详情](1245-obtains-details-about-multiple-free-tasks.md)接口，实现获取多个自由任务的详细信息。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二：获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三：添加接口权限

根据[添加接口调用权限](0003-add-api-permission.md)文档，搜索“项目”，申请项目管理的接口权限。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1150154871/p524594.png)

## 步骤四：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

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

## **步骤五：调用项目管理相关API**

1. 创建自由任务：

   1. 调用服务端API-[创建自由任务](1242-create-a-free-task.md)接口，实现自由任务创建，获取自由任务ID。

      ```
      public void createFreeMission() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              CreateOrganizationTaskHeaders createOrganizationTaskHeaders = new CreateOrganizationTaskHeaders();
              createOrganizationTaskHeaders.xAcsDingtalkAccessToken = "accessToken";
              CreateOrganizationTaskRequest createOrganizationTaskRequest = new CreateOrganizationTaskRequest()
                      .setContent("任务标题：明天12点前完成周报撰写")
                      .setNote("任务备注：任务备注信息")
                      .setPriority(1)
                      .setInvolveMembers(java.util.Arrays.asList(
                              "01472825524039877041","manager7675"
                      ))
                      .setExecutorId("01472825524039877041")
                      .setDueDate("2022-11-30T00:00:00Z")
                      .setCreateTime("2022-11-29T00:00:00Z")
                      .setVisible("involves")
                      .setDisableNotification(false)
                      .setDisableActivity(false);
              try {
                  CreateOrganizationTaskResponse createOrganizationTaskResponse = client.createOrganizationTaskWithOptions("manager7675", createOrganizationTaskRequest, createOrganizationTaskHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(createOrganizationTaskResponse.getBody()));
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
2. 自由任务管理相关操作：

   - 根据自由任务ID，调用服务端API-[更新自由任务的优先级](1250-change-free-task-priority.md)接口，实现自由任务优先级更新操作。

     ```
      public void updateFreeMissionPriorities() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskPriorityHeaders updateOrganizationTaskPriorityHeaders = new UpdateOrganizationTaskPriorityHeaders();
             updateOrganizationTaskPriorityHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskPriorityRequest updateOrganizationTaskPriorityRequest = new UpdateOrganizationTaskPriorityRequest()
                     .setPriority(2)
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskPriorityResponse updateOrganizationTaskPriorityResponse = client.updateOrganizationTaskPriorityWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskPriorityRequest, updateOrganizationTaskPriorityHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskPriorityResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[更新自由任务标题](1246-change-free-task-title.md)接口，实现自由任务标题更新操作。

     ```
     public void updateFreeMissionContent() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskContentHeaders updateOrganizationTaskContentHeaders = new UpdateOrganizationTaskContentHeaders();
             updateOrganizationTaskContentHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskContentRequest updateOrganizationTaskContentRequest = new UpdateOrganizationTaskContentRequest()
                     .setContent("修改后的文档标题：后天12点前完成周报撰写")
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskContentResponse updateOrganizationTaskContentResponse = client.updateOrganizationTaskContentWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskContentRequest, updateOrganizationTaskContentHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskContentResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[更新自由任务截止时间](1251-change-free-task-deadline.md)接口，实现自由任务截止时间更新操作。

     ```
     public void  updateFreeMissionDueDates() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskDueDateHeaders updateOrganizationTaskDueDateHeaders = new UpdateOrganizationTaskDueDateHeaders();
             updateOrganizationTaskDueDateHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskDueDateRequest updateOrganizationTaskDueDateRequest = new UpdateOrganizationTaskDueDateRequest()
                     .setDueDate("2022-12-01T00:00:00Z")
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskDueDateResponse updateOrganizationTaskDueDateResponse = client.updateOrganizationTaskDueDateWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskDueDateRequest, updateOrganizationTaskDueDateHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskDueDateResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[更新自由任务执行者](1249-change-free-task-executor.md)接口，实现自由任务执行者更新操作。

     ```
     public void updateFreeMissionExecutors() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskExecutorHeaders updateOrganizationTaskExecutorHeaders = new UpdateOrganizationTaskExecutorHeaders();
             updateOrganizationTaskExecutorHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskExecutorRequest updateOrganizationTaskExecutorRequest = new UpdateOrganizationTaskExecutorRequest()
                     .setExecutorId("01472825524039877041")
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskExecutorResponse updateOrganizationTaskExecutorResponse = client.updateOrganizationTaskExecutorWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskExecutorRequest, updateOrganizationTaskExecutorHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskExecutorResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[增加或删除自由任务的参与者](1252-change-task-participant.md)接口，实现自由任务参与者更新操作。

     ```
     public void  updateFreeMissionInvolveMembers() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskInvolveMembersHeaders updateOrganizationTaskInvolveMembersHeaders = new UpdateOrganizationTaskInvolveMembersHeaders();
             updateOrganizationTaskInvolveMembersHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskInvolveMembersRequest updateOrganizationTaskInvolveMembersRequest = new UpdateOrganizationTaskInvolveMembersRequest()
                     .setAddInvolvers(java.util.Arrays.asList(
                             "08521816421284272"
                     ))
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskInvolveMembersResponse updateOrganizationTaskInvolveMembersResponse = client.updateOrganizationTaskInvolveMembersWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskInvolveMembersRequest, updateOrganizationTaskInvolveMembersHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskInvolveMembersResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[更新自由任务备注](1248-update-free-task-notes.md)接口，实现自由任务备注更新操作。

     ```
     public void updateFreeMissionNotes() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskNoteHeaders updateOrganizationTaskNoteHeaders = new UpdateOrganizationTaskNoteHeaders();
             updateOrganizationTaskNoteHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskNoteRequest updateOrganizationTaskNoteRequest = new UpdateOrganizationTaskNoteRequest()
                     .setNote("备注：更新后的备注信息")
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskNoteResponse updateOrganizationTaskNoteResponse = client.updateOrganizationTaskNoteWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskNoteRequest, updateOrganizationTaskNoteHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskNoteResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[更新自由任务状态](1247-change-free-task-status.md)接口，实现完成自由任务。

     ```
     public void updateFreeMissionStates() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             UpdateOrganizationTaskStatusHeaders updateOrganizationTaskStatusHeaders = new UpdateOrganizationTaskStatusHeaders();
             updateOrganizationTaskStatusHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateOrganizationTaskStatusRequest updateOrganizationTaskStatusRequest = new UpdateOrganizationTaskStatusRequest()
                     .setIsDone(true)
                     .setDisableActivity(false)
                     .setDisableNotification(false);
             try {
                 UpdateOrganizationTaskStatusResponse updateOrganizationTaskStatusResponse = client.updateOrganizationTaskStatusWithOptions("63856f*****ea3e77f", "manager7675", updateOrganizationTaskStatusRequest, updateOrganizationTaskStatusHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateOrganizationTaskStatusResponse.getBody()));
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
3. 自由任务查询相关操作：

   - 根据自由任务ID，调用服务端API-[获取自由任务详情](1243-queries-free-task-details.md)接口，实现获取单个自由任务的详细信息。

     ```
     public void FreeMissionInfo() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             GetOrganizationTaskHeaders getOrganizationTaskHeaders = new GetOrganizationTaskHeaders();
             getOrganizationTaskHeaders.xAcsDingtalkAccessToken = "accessToken";
             try {
                 GetOrganizationTaskResponse getOrganizationTaskResponse = client.getOrganizationTaskWithOptions("63856f*****ea3e77f", "manager7675", getOrganizationTaskHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(getOrganizationTaskResponse.getBody()));
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
   - 根据自由任务ID，调用服务端API-[批量获取自由任务详情](1245-obtains-details-about-multiple-free-tasks.md)接口，实现获取多个自由任务的详细信息。

     ```
     public void FreeMissionInfoBatch() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
             GetOrganizatioTaskByIdsHeaders getOrganizatioTaskByIdsHeaders = new GetOrganizatioTaskByIdsHeaders();
             getOrganizatioTaskByIdsHeaders.xAcsDingtalkAccessToken = "accessToken";
             GetOrganizatioTaskByIdsRequest getOrganizatioTaskByIdsRequest = new GetOrganizatioTaskByIdsRequest()
                     .setTaskIds("63856f*****ea3e77f,63857b4d*****f97cb4ee");
             try {
                 GetOrganizatioTaskByIdsResponse getOrganizatioTaskByIdsResponse = client.getOrganizatioTaskByIdsWithOptions("manager7675", getOrganizatioTaskByIdsRequest, getOrganizatioTaskByIdsHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(getOrganizatioTaskByIdsResponse.getBody()));
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
