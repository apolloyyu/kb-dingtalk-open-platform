---
title: "任务协同提效：创建自由任务与生命周期管理"
source_url: "https://open.dingtalk.com/document/development/teambition-free-task-operation-process"
namespace: "development"
slug: "teambition-free-task-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 集成方案 > 任务协同提效：创建自由任务与生命周期管理"
doc_id: "3BLXr0Tomu"
updated_at: "2026-10-20 09:09:19"
---

> Source: https://open.dingtalk.com/document/development/teambition-free-task-operation-process
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 集成方案 > 任务协同提效：创建自由任务与生命周期管理
> Updated: 2026-10-20 09:09:19

# 任务协同提效：创建自由任务与生命周期管理

## **概述**

本方案基于钉钉Teambition项目管理API，实现企业内部自由任务的自动化创建、属性更新、状态流转及批量查询，打通业务系统与任务管理平台的无缝集成。

### **方案背景**

企业在日常运营中常面临以下痛点：

- **任务创建分散低效**：周报、审批、待办等任务需手动在Teambition中逐个创建，耗时且易遗漏关键信息。
- **任务属性变更繁琐**：优先级调整、截止时间延期、执行者更换等操作需多次点击界面，无法批量处理。
- **任务进度追踪困难**：缺乏统一的API查询入口，管理者难以实时掌握多个任务的完成状态和执行详情。
- **跨系统数据割裂**：业务系统产生的任务需求无法自动同步至Teambition，形成信息孤岛。

### **核心价值**

本方案提供从任务创建到状态闭环的全链路API能力，具体价值包括：

- **自动化任务创建**：通过API一键创建自由任务，支持标题、备注、优先级、执行者、参与者、截止时间等字段批量填充。
- **灵活属性更新**：支持对任务的优先级、标题、截止时间、执行者、参与者、备注、状态等7类属性独立更新，无需重新创建任务。
- **高效批量查询**：支持单任务和批量任务的详情查询，便于下游系统实时同步任务状态。
- **通知与活动可控**：每次更新操作可独立控制是否发送钉钉通知、是否记录活动日志，避免消息轰炸。

### **适用场景**

本方案适用于以下典型业务场景：

- **周报自动创建**：每周五下午5点自动为部门成员创建"本周周报撰写"任务，设置截止时间为周日24点，执行者为对应员工。
- **审批联动建任务**：OA审批通过后，自动在Teambition中创建后续执行任务，并将审批发起人设为参与者。
- **项目里程碑跟踪**：项目经理通过API批量创建项目各阶段里程碑任务，并按进度动态更新截止时间和执行者。

## **典型业务场景**

### **场景一：周报自动创建与提醒**

#### **痛点分析**

传统周报管理依赖人工提醒和手动建任务，存在以下问题：

- 管理员每周需逐一联系团队成员确认周报提交情况，沟通成本高。
- 部分员工忘记提交周报，导致周报复盘数据缺失，影响管理决策。
- 周报提交时间不统一，汇总整理耗时费力。

#### **价值验证**

- **自动化流程**

  ![场景一-周报自动创建与提醒_20261019_121050](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9558542971/p1106900.png)
- **核心优势**

  - **定时自动触发**：通过定时任务或业务系统事件驱动，每周固定时间自动为全员创建周报任务，零人工干预。
  - **标准化信息录入**：任务标题、备注、截止时间等字段由系统统一填充，确保格式规范、信息完整。
  - **钉钉消息精准触达**：任务创建后自动推送钉钉通知给执行者，提醒及时填写，覆盖率100%。

### **场景二：审批联动任务创建与进度追踪**

#### **痛点分析**

OA审批与后续执行任务脱节，导致：

- 审批通过后，执行人不知晓需跟进的具体任务，依赖口头传达易遗漏。
- 管理者无法实时查看审批关联任务的执行进度，需手动登录Teambition逐个查询。
- 任务属性变更（如延期、换人）需线下沟通后再手动修改，响应滞后。

#### **价值验证**

- **自动化流程**

  ![场景二-审批联动任务创建与进度追踪_20261019_121152](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9558542971/p1106901.png)
- **核心优势**

  - **审批-任务无缝衔接**：审批通过事件触发API自动创建执行任务，审批信息自动填入任务备注，上下文完整保留。
  - **多维度属性动态更新**：支持通过API实时更新任务优先级、截止时间、执行者等，适应业务变化。
  - **批量查询实时同步**：下游系统通过批量查询API定期拉取任务状态，自动生成进度报表供管理层决策。

## **实施指南**

### **技术架构**

- **接口调用层**：基于钉钉服务端SDK调用Teambition项目管理API，涵盖任务创建、属性更新、状态变更、详情查询等10个核心接口。
- **应用认证层**：通过AppKey和AppSecret换取accessToken，作为所有API调用的身份鉴权凭证，支持缓存复用降低请求频次。
- **任务管理层**：封装自由任务的全生命周期操作，包括创建、更新优先级/标题/截止时间/执行者/参与者/备注/状态，以及单任务和批量查询。
- **错误处理层**：捕获TeaException异常，解析err.code和err.message定位问题，支持重试机制和告警通知。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - Project.Task.Write.All （项目任务写权限）
  - Project.Task.Read.All （项目任务读权限）

- **开发环境**：已安装Java开发环境(JDK1.6及以上)及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请项目相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：创建自由任务

1. 调用服务端API-[创建自由任务](1242-create-a-free-task.md)接口，实现自由任务创建，获取自由任务ID。

步骤五：自由任务管理

- 根据自由任务ID，调用服务端API-[更新自由任务的优先级](1250-change-free-task-priority.md)接口，实现自由任务优先级更新操作。
- 根据自由任务ID，调用服务端API-[更新自由任务标题](1246-change-free-task-title.md)接口，实现自由任务标题更新操作。
- 根据自由任务ID，调用服务端API-[更新自由任务截止时间](1251-change-free-task-deadline.md)接口，实现自由任务截止时间更新操作。
- 根据自由任务ID，调用服务端API-[更新自由任务执行者](1249-change-free-task-executor.md)接口，实现自由任务执行者更新操作。
- 根据自由任务ID，调用服务端API-[增加或删除自由任务的参与者](1252-change-task-participant.md)接口，实现自由任务参与者更新操作。
- 根据自由任务ID，调用服务端API-[更新自由任务备注](1248-update-free-task-notes.md)接口，实现自由任务备注更新操作。
- 根据自由任务ID，调用服务端API-[更新自由任务状态](1247-change-free-task-status.md)接口，实现完成自由任务。

步骤六：查询自由任务查询

- 根据自由任务ID，调用服务端API-[获取自由任务详情](1243-queries-free-task-details.md)接口，实现获取单个自由任务的详细信息。
- 根据自由任务ID，调用服务端API-[批量获取自由任务详情](1245-obtains-details-about-multiple-free-tasks.md)接口，实现获取多个自由任务的详细信息。

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

   - Project.Task.Write.All （项目任务写权限）— 用于创建、更新自由任务的属性和状态。
   - Project.Task.Read.All （项目任务读权限）— 用于查询自由任务详情。

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

### **步骤四：创建自由任务**

调用服务端API-[创建自由任务](1242-create-a-free-task.md)接口，实现自由任务创建，获取自由任务ID。

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

**参数说明**：

- `content`：任务标题。
- `note`：任务备注。
- `priority`：任务优先级，数值越小优先级越高。
- `involveMembers`：参与者userId列表。
- `executorId`：执行者userId。
- `dueDate`：截止时间，ISO 8601格式。
- `createTime`：创建时间，ISO 8601格式。
- `visible`：可见范围，`involves`表示仅参与者可见。
- `disableNotification`：是否禁用钉钉通知，`false`表示发送通知。
- `disableActivity`：是否禁用活动记录，`false`表示记录活动。

**返回字段**：

- `id`：自由任务ID，字符串类型，用于后续更新和查询操作。
- `content`：任务标题。
- `priority`：自由任务优先级。

### **步骤五：自由任务管理**

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

  **参数说明**：

  - `taskId`：任务id（路径参数），调用创建自由任务接口获取的id值。
  - `userId`：操作者userId（路径参数）。
  - `priority`：自由任务优先级。默认值：-10（较低）、0（普通）、1（紧急）、2（非常紧急）。
  - `disableActivity`：是否禁止动态。true：禁止；false：不禁止。
  - `disableNotification`：是否禁止通知。true：禁止；false：不禁止。

  **返回字段**：

  - `content`：更新后的任务标题。
  - `updated`：更新任务标题的时间。
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

  **参数说明**：

  - `taskId`：任务id（路径参数），调用创建自由任务接口获取的id值。
  - `userId`：操作者userId（路径参数）。
  - `content`：任务标题。
  - `disableActivity`：是否禁止动态。true：禁止；false：不禁止。
  - `disableNotification`：是否禁止通知。true：禁止；false：不禁止。

  **返回字段**：

  - `dueDate`：更新后的任务截止时间。
  - `updateTime`：任务截止时间被更新的时间。
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

  **参数说明**：

  - `taskId`：任务id（路径参数），调用创建自由任务接口获取的id值。
  - `userId`：操作者userId（路径参数）。
  - `dueDate`：任务截止时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。
  - `disableActivity`：是否禁止动态。true：禁止；false：不禁止。
  - `disableNotification`：是否禁止通知。true：禁止；false：不禁止。

  **返回字段**：

  - `executorId`：更新后的执行者`userId`。
  - `updated`：更新执行者的时间，格式：YYYY-MM-DDTHH:mm:ssZ。
  - `executor`：执行者信息，含`avatarUrl`、`name`、`userId`。
  - `involvers`：参与者userId列表，含`avatarUrl`、`name`、`userId`。
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

  **参数说明**：

  - `taskId`：任务id，路径参数。
  - `userId`：操作者userId，路径参数。
  - `executorId`：新的执行者userId。
  - `disableActivity`：是否禁用活动记录。
  - `disableNotification`：是否禁用钉钉通知。

  **返回字段**：

  - `involvers`：参与者userId列表，含`avatarUrl`、`name`、`userId`。
  - `updated`：更新参与者的时间。
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

  **参数说明**：

  - `taskId`：任务id，路径参数。
  - `userId`：操作者userId，路径参数。
  - `addInvolvers`：新增参与者userId列表。
  - `disableActivity`：是否禁用活动记录。
  - `disableNotification`：是否禁用钉钉通知。

  **返回字段**：

  - `note`：更新后的任务备注。
  - `updated`：更新任务备注的时间。
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

  **参数说明**：

  - `taskId`：任务id（路径参数）。
  - `userId`：操作者userId（路径参数）。
  - `note`：任务备注。
  - `disableActivity`：是否禁止动态。true：禁止；false：不禁止。
  - `disableNotification`：是否禁止通知。true：禁止；false：不禁止。

  **返回字段**：

  - `isDone`：自由任务状态。true：完成；false：未完成。
  - `updateTime`：更新任务状态的时间。
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

  **参数说明**：

  - `taskId`：任务id（路径参数）。
  - `userId`：操作者userId（路径参数）。
  - `isDone`：自由任务状态。true：完成；false：未完成。
  - `disableActivity`：是否禁止动态。true：禁止；false：不禁止。
  - `disableNotification`：是否禁止通知。true：禁止；false：不禁止。

  **返回字段**：

  - `priority`：更新后的自由任务优先级。
  - `updated`：更新优先级的时间。

### **步骤六：查询自由任务查询**

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

  **参数说明**：

  - `taskId`：任务id（路径参数）。
  - `userId`：操作者userId（路径参数）。

  **返回字段**：

  - `taskId`：任务id。
  - `content`：任务标题。
  - `note`：任务备注。
  - `priority`：自由任务优先级。
  - `isDone`：任务是否已完成。true：未完成；false：已完成。
  - `dueDate`：任务截止时间。
  - `startDate`：任务开始时间。
  - `executorId`：执行者userId。
  - `creatorId`：创建者userId。
  - `involveMembers`：任务参与者userId列表。
  - `labels`：任务自定义标记。
  - `visible`：任务可见性。involves：仅参与者可见；members：所有人可见。
  - `created`：创建时间。
  - `updated`：更新时间。
  - `isDeleted`：任务是否已删除。true：已删除；false：未删除。
  - `ancestorIds`：该任务父任务的id。
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

  **参数说明**：

  - `userId`：操作者userId（路径参数）。
  - `taskIds`：任务id列表（查询参数），多个id用逗号分隔，建议不超过20个。

  **返回字段**：

  - `taskId`：任务id。
  - `content`：任务标题。
  - `note`：任务的备注信息。
  - `priority`：自由任务优先级。
  - `isDone`：任务是否已完成。true：已完成；false：未完成。
  - `dueDate`：任务截止时间。
  - `startDate`：任务开始时间。
  - `executorId`：执行者userId。
  - `creatorId`：创建者userId。
  - `involveMembers`：参与者userId列表。
  - `labels`：任务自定义标记列表。
  - `visible`：任务可见性。
  - `created`：创建时间。
  - `updated`：更新时间。
  - `isDeleted`：任务是否已删除。
  - `ancestorIds`：该任务父任务的id。

**实施完成检查清单**

- ✅ 应用凭证（AppKey和AppSecret）已安全获取并妥善保管。
- ✅ 接口权限（`Project.Task.Write.All`、`Project.Task.Read.All`）已成功添加并生效。
- ✅ accessToken获取与缓存机制已实现并通过测试。
- ✅ 创建自由任务API调用成功，返回任务ID格式符合预期。
- ✅ 7类属性更新API（优先级、标题、截止时间、执行者、参与者、备注、状态）均调用成功。
- ✅ 单任务和批量查询API调用成功，返回字段完整。
- ✅ `disableNotification`和`disableActivity`参数可独立控制通知和活动记录。
- ✅ TeaException异常处理逻辑已实现，可正确解析err.code和err.message。

## **常见问题（FAQ）**

- **Q1：创建任务时返回"权限不足"错误如何处理？**

  A：请检查是否已在开发者后台申请`Project.Task.Write.All`权限，权限添加后需等待1-2分钟生效；若仍报错，重新获取accessToken后再试。
- **Q2：任务ID从哪里获取？**

  A：任务ID由创建自由任务API的返回值中的`id`字段提供，后续所有更新和查询操作均需使用该ID。
- **Q3：如何避免频繁换取accessToken导致限流？**

  A：accessToken有效期为7200秒，建议缓存并在过期前30秒主动刷新；并发调用时共享同一accessToken实例。
- **Q4：更新任务属性时是否需要传入所有字段？**

  A：不需要。每个更新接口仅针对单一属性，只需传入目标属性的新值即可，其他属性保持不变。
- **Q5：批量查询任务时最多支持多少个任务ID？**

  A：单次批量查询建议最多20个任务ID。
