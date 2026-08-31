---
title: "创建项目任务和工时"
source_url: "https://open.dingtalk.com/document/development/team-ambition-project-operation-process"
namespace: "development"
slug: "team-ambition-project-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 使用教程 > 创建项目任务和工时"
doc_id: "Qt7r0qL0vF"
updated_at: "2026-07-20 09:21:53"
---

> Source: https://open.dingtalk.com/document/development/team-ambition-project-operation-process
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 使用教程 > 创建项目任务和工时
> Updated: 2026-07-20 09:21:53

# 创建项目任务和工时

本文档展示了，创建一个企业内部应用，使用Teambition项目管理提供的API，实现企业项目的相关操作流程。

## **流程简介**

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，点击应用开发-企业内部开发，根据[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)文档，创建企业内部应用。

步骤二：单击基础信息 > 应用信息，获取应用AppKey和AppSecret。

步骤三：根据[添加接口调用权限](0003-add-api-permission.md)文档，搜索“项目”，申请项目管理的接口权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤五：调用项目管理相关API：

1. 根据企业项目模板创建企业项目：

   1. 创建企业项目模板，完成模板创建。
   2. 调用服务端API-[搜索企业项目模板](1216-search-for-enterprise-custom-templates-by-project-template-name.md)接口，获取企业项目模板ID。
   3. 根据企业项目模板ID。调用服务端API-[根据项目模板创建项目](1217-create-a-project-from-a-project-template.md)接口，实现企业项目的创建。获取项目ID。
2. 项目分组创建：

   1. 创建企业项目分组，完成分组创建。
   2. 调用服务端API-[查询员工可见的项目分组](1218-query-available-project-groups.md)接口，实现获取会议室列表内容。获取项目分组ID。
   3. 根据企业项目ID和项目分组ID，调用服务端API-[更新项目所在的分组](1219-update-project-grouping.md)接口，完成企业项目迁移至对应项目分组。
3. 企业项目操作操作流程：

   1. 根据企业项目ID，调用服务端API-[添加项目成员](1212-add-project-members.md)接口，实现企业项目成员添加操作。
   2. 调用服务端API-[查询优先级列表](1244-query-a-priority-list.md)接口，获取优先级内容信息。
   3. 根据企业项目ID，调用服务端API-[创建项目任务](1222-create-a-project-task.md)接口，实现企业项目具体任务创建流程。获取项目任务taskId。
   4. 根据项目任务taskId，调用服务端API-[添加任务的关联内容](1230-create-a-linked-object-associated-with-a-task.md)接口，添加项目任务关联说明。
   5. 根据企业项目ID，调用服务端API-[查询项目中的任务](1229-query-tasks-in-a-project.md)接口，查询项目中的任务信息。
   6. 根据项目任务taskId，调用服务端API-[创建计划工时](1253-create-planned-work.md)接口，完成单个企业项目任务添加计划工时。
   7. 根据项目任务taskId，调用服务端API-[创建实际工时](1254-create-actual-work.md)接口，完成单个企业项目任务添加计划工时。

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

1. 根据企业项目模板创建企业项目：

   1. 创建企业项目模板，完成模板创建。

      ![企业项目模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0311739661/p524570.gif)
   2. 调用服务端API-[搜索企业项目模板](1216-search-for-enterprise-custom-templates-by-project-template-name.md)接口，获取企业项目模板ID。

      ```
      public void queryTemplates() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              SearchProjectTemplateHeaders searchProjectTemplateHeaders = new SearchProjectTemplateHeaders();
              searchProjectTemplateHeaders.xAcsDingtalkAccessToken = "accessToken";
              SearchProjectTemplateRequest searchProjectTemplateRequest = new SearchProjectTemplateRequest()
                      .setKeyword("测试模板");
              try {
                  SearchProjectTemplateResponse searchProjectTemplateResponse = client.searchProjectTemplateWithOptions("manager7675", searchProjectTemplateRequest, searchProjectTemplateHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(searchProjectTemplateResponse.getBody()));
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
   3. 根据企业项目模板ID。调用服务端API-[根据项目模板创建项目](1217-create-a-project-from-a-project-template.md)接口，实现企业项目的创建。获取项目ID。

      ```
        public void createProjectByTemplates() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              CreateProjectByTemplateHeaders createProjectByTemplateHeaders = new CreateProjectByTemplateHeaders();
              createProjectByTemplateHeaders.xAcsDingtalkAccessToken = "accessToken";
              CreateProjectByTemplateRequest createProjectByTemplateRequest = new CreateProjectByTemplateRequest()
                      .setName("project_1125测试项目")
                      .setTemplateId("638063f******10f79");
              try {
                  CreateProjectByTemplateResponse createProjectByTemplateResponse = client.createProjectByTemplateWithOptions("manager7675", createProjectByTemplateRequest, createProjectByTemplateHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(createProjectByTemplateResponse.getBody()));
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
2. 项目分组创建：

   1. 创建企业项目分组，完成分组创建。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9211739661/p524550.png)
   2. 调用服务端API-[查询员工可见的项目分组](1218-query-available-project-groups.md)接口，实现获取会议室列表内容。获取项目分组ID。

      ```
      public void projectGroups() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              GetProjectGroupHeaders getProjectGroupHeaders = new GetProjectGroupHeaders();
              getProjectGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
              GetProjectGroupRequest getProjectGroupRequest = new GetProjectGroupRequest()
                      .setViewerId("manager7675")
                      .setPageSize(10);
              try {
                  GetProjectGroupResponse getProjectGroupResponse = client.getProjectGroupWithOptions("manager7675", getProjectGroupRequest, getProjectGroupHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(getProjectGroupResponse.getBody()));
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
   3. 根据企业项目ID和项目分组ID，调用服务端API-[更新项目所在的分组](1219-update-project-grouping.md)接口，完成企业项目迁移至对应项目分组。

      ```
      public void  updateProjectGroups() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              UpdateProjectGroupHeaders updateProjectGroupHeaders = new UpdateProjectGroupHeaders();
              updateProjectGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
              UpdateProjectGroupRequest updateProjectGroupRequest = new UpdateProjectGroupRequest()
                      .setAddProjectGroupIds(java.util.Arrays.asList(
                              "项目分组ID"
                      ));
              try {
                  UpdateProjectGroupResponse updateProjectGroupResponse = client.updateProjectGroupWithOptions("manager7675", "企业项目ID", updateProjectGroupRequest, updateProjectGroupHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(updateProjectGroupResponse.getBody()));
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
3. 企业项目操作操作流程：

   1. 根据企业项目ID，调用服务端API-[添加项目成员](1212-add-project-members.md)接口，实现企业项目成员添加操作。

      ```
       public void addProjectUser() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              AddProjectMemberHeaders addProjectMemberHeaders = new AddProjectMemberHeaders();
              addProjectMemberHeaders.xAcsDingtalkAccessToken = "accessToken";
              AddProjectMemberRequest addProjectMemberRequest = new AddProjectMemberRequest()
                      .setUserIds(java.util.Arrays.asList(
                              "01472825524039877041"
                      ));
              try {
                  AddProjectMemberResponse addProjectMemberResponse = client.addProjectMemberWithOptions("manager7675", "企业项目ID", addProjectMemberRequest, addProjectMemberHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(addProjectMemberResponse.getBody()));
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
   2. 调用服务端API-[查询优先级列表](1244-query-a-priority-list.md)接口，获取优先级内容信息。

      ```
      public void prioritiesList() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              GetOrganizationPriorityListHeaders getOrganizationPriorityListHeaders = new GetOrganizationPriorityListHeaders();
              getOrganizationPriorityListHeaders.xAcsDingtalkAccessToken = "accessToken";
              try {
                  GetOrganizationPriorityListResponse organizationPriorityListWithOptions = client.getOrganizationPriorityListWithOptions("manager7675", getOrganizationPriorityListHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(organizationPriorityListWithOptions.getBody()));
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
   3. 根据企业项目ID，调用服务端API-[创建项目任务](1222-create-a-project-task.md)接口，实现企业项目具体任务创建流程。获取项目任务taskId。

      ```
       public void createProjectTask() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              com.aliyun.dingtalkproject_1_0.models.CreateTaskHeaders createTaskHeaders = new com.aliyun.dingtalkproject_1_0.models.CreateTaskHeaders();
              createTaskHeaders.xAcsDingtalkAccessToken = "accessToken";

              com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest createTaskRequest = new com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest()
                      .setProjectId("638065*********f66469")
                      .setContent("任务标题：1125标题测试")
                      .setExecutorId("01472825524039877041")
                      .setDueDate("2022-11-28T18:30:00Z")
                      .setNote("备注：1125备注测试")
                      .setPriority(1);
              try {
                  CreateTaskResponse createTaskResponse = client.createTaskWithOptions("manager7675", createTaskRequest, createTaskHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(createTaskResponse.getBody()));
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
   4. 根据项目任务taskId，调用服务端API-[添加任务的关联内容](1230-create-a-linked-object-associated-with-a-task.md)接口，添加项目任务关联说明。

      ```
      public void addObjectLinks() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              CreateTaskObjectLinkHeaders createTaskObjectLinkHeaders = new CreateTaskObjectLinkHeaders();
              createTaskObjectLinkHeaders.xAcsDingtalkAccessToken = "accessToken";
              CreateTaskObjectLinkRequest.CreateTaskObjectLinkRequestLinkedData linkedData = new CreateTaskObjectLinkRequest.CreateTaskObjectLinkRequestLinkedData()
                      .setTitle("关联内容标题：标题测试")
                      .setContent("关联内容：内容测试")
                      .setUrl("https://www.dingtalk.com")
                      .setThumbnailUrl("https://example/k/钉钉图片1.png");
              CreateTaskObjectLinkRequest createTaskObjectLinkRequest = new CreateTaskObjectLinkRequest()
                      .setLinkedData(linkedData);
              try {
                  CreateTaskObjectLinkResponse createTaskObjectLinkResponse = client.createTaskObjectLinkWithOptions("manager7675", "项目任务ID", createTaskObjectLinkRequest, createTaskObjectLinkHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(createTaskObjectLinkResponse.getBody()));
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
   5. 根据企业项目ID，调用服务端API-[查询项目中的任务](1229-query-tasks-in-a-project.md)接口，查询项目中的任务信息。

      ```
      public void queryTasks() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectHeaders queryTaskOfProjectHeaders = new com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectHeaders();
              queryTaskOfProjectHeaders.xAcsDingtalkAccessToken = "accessToken";
              com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectRequest queryTaskOfProjectRequest = new com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectRequest()
                      .setMaxResults(10)
                      .setQuery("executorId IN \"01472825524039877041\" ORDER BY priority DESC");
              try {
                  QueryTaskOfProjectResponse queryTaskOfProjectResponse = client.queryTaskOfProjectWithOptions("manager7675", "企业项目ID", queryTaskOfProjectRequest, queryTaskOfProjectHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(queryTaskOfProjectResponse.getBody()));
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
   6. 根据项目任务taskId，调用服务端API-[创建计划工时](1253-create-planned-work.md)接口，完成单个企业项目任务添加计划工时。

      ```
        public void createPlanTimes() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeHeaders createPlanTimeHeaders = new com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeHeaders();
              createPlanTimeHeaders.xAcsDingtalkAccessToken = "accessToken";
              com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeRequest createPlanTimeRequest = new com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeRequest()
                      .setTenantType("organization")
                      .setExecutorId("01472825524039877041")
                      .setObjectId("6380*********51dfe")
                      .setObjectType("task")
                      .setIsDuration(true)
                      .setIncludesHolidays(true)
                      .setSubmitterId("01472825524039877041")
                      .setStartDate("2022-11-25")
                      .setEndDate("2022-11-25")
                      .setPlanTime(36000000L);
              try {
                  CreatePlanTimeResponse createPlanTimeResponse = client.createPlanTimeWithOptions("manager7675", createPlanTimeRequest, createPlanTimeHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(createPlanTimeResponse.getBody()));
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
   7. 根据项目任务taskId，调用服务端API-[创建实际工时](1254-create-actual-work.md)接口，完成单个企业项目任务添加计划工时。

      ```
      public void createWorkTimes() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkproject_1_0.Client client = new com.aliyun.dingtalkproject_1_0.Client(config);
              com.aliyun.dingtalkproject_1_0.models.CreateWorkTimeHeaders createWorkTimeHeaders = new com.aliyun.dingtalkproject_1_0.models.CreateWorkTimeHeaders();
              createWorkTimeHeaders.xAcsDingtalkAccessToken = "accessToken";
              com.aliyun.dingtalkproject_1_0.models.CreateWorkTimeRequest createWorkTimeRequest = new com.aliyun.dingtalkproject_1_0.models.CreateWorkTimeRequest()
                      .setTenantType("organization")
                      .setExecutorId("01472825524039877041")
                      .setObjectId("63806**********51dfe")
                      .setObjectType("task")
                      .setSubmitterId("01472825524039877041")
                      .setIsDuration(true)
                      .setIncludesHolidays(true)
                      .setStartDate("2022-11-25")
                      .setEndDate("2022-11-25")
                      .setWorkTime(36000000L);
              try {
                  CreateWorkTimeResponse createWorkTimeResponse = client.createWorkTimeWithOptions("manager7675", createWorkTimeRequest, createWorkTimeHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(createWorkTimeResponse.getBody()));
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
