---
title: "日程参会人精细化管理：状态追踪与动态调整"
source_url: "https://open.dingtalk.com/document/development/calendar-participant-process"
namespace: "development"
slug: "calendar-participant-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 使用教程 > 日程参会人精细化管理：状态追踪与动态调整"
doc_id: "fRiCYfHaWR"
updated_at: "2026-09-23 12:04:35"
---

> Source: https://open.dingtalk.com/document/development/calendar-participant-process
> Path: 应用开发 / 服务端 API / 日程 > 使用教程 > 日程参会人精细化管理：状态追踪与动态调整
> Updated: 2026-09-23 12:04:35

# 日程参会人精细化管理：状态追踪与动态调整

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现日程参会人的添加、查询、状态设置及删除操作，支持将业务系统中的参会人员信息自动同步至钉钉日程，实现统一参会人管理。

## 概述

本方案提供一套完整的日程参会人管理解决方案，通过钉钉开放平台的日程参与者API，实现将企业自有系统中的会议参会人员自动添加至钉钉日程，并支持查询参会人信息、设置响应状态、删除参会人等完整操作流程。

### 方案背景

企业在日常运营中常面临以下痛点：

- **参会人手动添加耗时**：业务系统中已确定的参会人员，仍需人工逐个在钉钉日程中添加邀请，大型会议动辄数十人，重复操作效率极低。
- **响应状态无法追踪**：外部系统添加的参会人是否接受邀请、是否出席，缺乏统一的响应状态视图，组织者难以掌握实际参会情况。
- **变更通知依赖人工**：参会人增减或会议时间调整时，需人工重新发送通知，容易遗漏部分人员导致信息不同步。
- **数据孤岛阻碍协同**：参会人数据未与企业通讯录、考勤、审批等模块打通，无法基于组织架构自动匹配相关人员。

### 核心价值

本方案提供一套完整的日程参会人管理解决方案，通过钉钉开放平台的日程参与者API，实现将企业自有系统中的会议参会人员自动添加至钉钉日程，并支持查询参会人信息、设置响应状态、删除参会人等完整操作流程。

- **参会人自动添加**：业务系统确定参会名单后一键同步至钉钉日程，无需人工逐个邀请，大幅提升会议筹备效率。
- **响应状态实时追踪**：支持查询每位参会人的响应状态（接受/拒绝/暂定），组织者实时掌握实际参会情况。
- **变更自动通知**：参会人增减或会议调整时自动推送更新通知，确保所有相关人员及时获知最新信息。
- **组织架构联动**：基于钉钉通讯录自动匹配参会人员，支持按部门、角色批量添加，减少手动查找成本。

### 适用场景

本方案适用于以下典型业务场景：

- **企业内部会议管理系统参会人同步**：自研会议管理系统中的会议室预订和参会安排自动同步至钉钉日程参会人列表，避免人工重复录入。
- **项目管理工具里程碑事件参会人管理**：Jira、禅道等工具中的版本发布、评审会等关键节点自动添加项目负责人和核心成员为参会人，确保相关人员及时获知。
- **CRM客户拜访计划参会人同步**：销售人员的客户拜访计划从CRM系统自动同步至钉钉日程并添加相关同事为参会人，便于团队协作跟进。
- **培训报名系统与钉钉日程参会人联动**：培训课程信息自动创建为钉钉日程事件，报名学员一键加入为参会人，自动接收课程提醒。

## 典型业务场景

### 场景一：内部会议系统参会人同步至钉钉日程

#### 痛点分析

企业使用自研会议管理系统安排会议室和参会人员，但员工仍需在钉钉日程中手动添加参会人，导致：

- 重复录入，效率低下且易出错
- 参会人变更时两个系统不同步，产生信息差
- 无法利用钉钉的参会人响应状态追踪功能

#### 价值验证

- **自动化流程**

  ![meeting_participant_sync_flow](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5726310971/p1103285.png)
- **关键优势**

  - **秒级自动同步**：会议创建后1秒内自动将所有参会人添加至钉钉日程，无需手动操作。
  - **状态实时回写**：支持参会人响应状态（接受/拒绝/待定）实时回写至会议系统，确保双端数据一致。
  - **变更自动通知**：参会人增减时自动推送更新通知，无需人工干预。

### 场景二：项目里程碑事件参会人管理

#### 痛点分析

项目管理工具中的关键节点（如版本发布、评审会、交付日）仅存在于项目系统中，团队成员容易遗忘：

- 非项目成员无法感知关键时间节点，需人工逐个通知
- 缺乏统一的参会人响应状态视图，组织者难以掌握实际出席情况
- 到期前无主动提醒，依赖人工跟进确认
- 跨项目协调时，无法快速查看各里程碑的参会人覆盖情况

#### 价值验证

- **自动化流程**

  ![milestone_participant_sync_flow](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5726310971/p1103286.png)
- **关键优势**

  - **自动关联核心成员**：里程碑事件自动将项目负责人和核心成员添加为参会人，无需手动逐个邀请。
  - **DING紧急提醒**：支持提前N天触发钉钉DING紧急提醒，确保重要节点不遗漏。
  - **响应状态闭环追踪**：里程碑完成后自动统计参会人响应状态（接受/拒绝/暂定），形成完整的项目进度闭环。

## 实施指南

### 技术架构

- **接口调用层**：调用日程服务端API实现参会人的添加、查询、状态设置、删除操作。
- **参会人数据同步层**：调用日程服务端API将自有系统的参会人信息同步到钉钉日程应用。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- 应用准备：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- 权限要求：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Calendar.Event.Write`（日程写权限）
  - `Calendar.Event.Read`（日程读权限）
- 开发环境：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- SDK准备：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请日程相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端日程相关API。

1. 调用服务端API-[创建日程](0252-create-schedule.md)接口，进行创建日程，获取日程`id`。
2. 根据日程`id`，调用服务端API-[添加日程参与者](0258-add-schedule-participant.md)接口，进行日程参与者的添加操作。
3. 根据日程`id`，调用服务端API-[获取日程参与者](0261-get-the-participants-of-a-schedule.md)接口，获取日程参与人的信息。
4. 根据日程`id`，调用服务端API-[设置日程响应邀请状态](0260-configure-response-status.md)接口，进行日程参与者响应的邀请状态。
5. 根据日程`id`，调用服务端API-[删除日程参与者](0259-delete-schedule-participant.md)接口，进行日程参与者的删除操作。

## **实施步骤**

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

   - `Calendar.Event.Write`（日历应用中日程写权限）— 用于添加、删除日程参会人，设置参会人响应状态。
   - `Calendar.Event.Read`（日历应用中日程读权限）— 用于查询日程参会人信息及响应状态。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

```
public String getAccessToken() {
    com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
    config.protocol = "https";
    config.regionId = "central";
    try {
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("dingeqqpkv3xxxxxx")
                .setAppSecret("GT-lsu-taDAxxxsTsxxxx");
        GetAccessTokenResponse response = client.getAccessToken(getAccessTokenRequest);
        System.out.println(response.getBody());
        return response.getBody().getAccessToken();
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：核心API调用**

1. **创建日程**：调用服务端API-[创建日程](0252-create-schedule.md)接口，将自有系统的会议、任务等事件创建到钉钉日历，并获取日程`id`。

   ```
   public void createCalendar() throws Exception {
       // 初始化客户端配置
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       com.aliyun.dingtalkcalendar_1_0.Client client = new com.aliyun.dingtalkcalendar_1_0.Client(config);

       // 设置请求头
       CreateEventHeaders createEventHeaders = new CreateEventHeaders();
       createEventHeaders.xAcsDingtalkAccessToken = "accessToken";

       // 扩展参数
       java.util.Map<String, String> extra = TeaConverter.buildMap(
               new TeaPair("noChatNotification", "false"),
               new TeaPair("noPushNotification", "false")
       );

       // 在线会议信息
       CreateEventRequest.CreateEventRequestOnlineMeetingInfo onlineMeetingInfo =
               new CreateEventRequest.CreateEventRequestOnlineMeetingInfo()
                       .setType("dingtalk");

       // 提醒设置
       CreateEventRequest.CreateEventRequestReminders reminders0 =
               new CreateEventRequest.CreateEventRequestReminders()
                       .setMethod("dingtalk")
                       .setMinutes(15);

       // 地点信息
       CreateEventRequest.CreateEventRequestLocation location =
               new CreateEventRequest.CreateEventRequestLocation()
                       .setDisplayName("********A座9F");

       // 参与人列表
       CreateEventRequest.CreateEventRequestAttendees attendees0 =
               new CreateEventRequest.CreateEventRequestAttendees()
                       .setId("日程参与人unionId")
                       .setIsOptional(false);
       CreateEventRequest.CreateEventRequestAttendees attendees1 =
               new CreateEventRequest.CreateEventRequestAttendees()
                       .setId("日程参与人unionId")
                       .setIsOptional(false);
       CreateEventRequest.CreateEventRequestAttendees attendees2 =
               new CreateEventRequest.CreateEventRequestAttendees()
                       .setId("日程参与人unionId")
                       .setIsOptional(false);

       // 循环规则
       CreateEventRequest.CreateEventRequestRecurrenceRange recurrenceRange =
               new CreateEventRequest.CreateEventRequestRecurrenceRange()
                       .setType("numbered")
                       .setNumberOfOccurrences(2);
       CreateEventRequest.CreateEventRequestRecurrencePattern recurrencePattern =
               new CreateEventRequest.CreateEventRequestRecurrencePattern()
                       .setType("daily")
                       .setInterval(1);
       CreateEventRequest.CreateEventRequestRecurrence recurrence =
               new CreateEventRequest.CreateEventRequestRecurrence()
                       .setPattern(recurrencePattern)
                       .setRange(recurrenceRange);

       // 日程时间（全天日程使用 date，非全天使用 dateTime + timeZone）
       CreateEventRequest.CreateEventRequestEnd end =
               new CreateEventRequest.CreateEventRequestEnd()
                       .setDate("2022-09-03");
       // .setDateTime("2021-09-20T10:15:30+08:00")
       // .setTimeZone("Asia/Shanghai");

       CreateEventRequest.CreateEventRequestStart start =
               new CreateEventRequest.CreateEventRequestStart()
                       .setDate("2022-09-02");
       // .setDateTime("2021-09-20T10:15:30+08:00")
       // .setTimeZone("Asia/Shanghai");

       // 构建创建日程请求
       CreateEventRequest createEventRequest = new CreateEventRequest()
               .setSummary("0902创建日程")
               .setDescription("这是0902创建的一个日程")
               .setStart(start)
               .setEnd(end)
               .setIsAllDay(true)
               .setRecurrence(recurrence)
               .setAttendees(java.util.Arrays.asList(attendees0, attendees1, attendees2))
               .setLocation(location)
               .setReminders(java.util.Arrays.asList(reminders0))
               .setOnlineMeetingInfo(onlineMeetingInfo)
               .setExtra(extra);

       try {
           CreateEventResponse eventWithOptions = client.createEventWithOptions(
                   "日程组织人unionId", "primary", createEventRequest, createEventHeaders, new RuntimeOptions());
           System.out.println(JSON.toJSONString(eventWithOptions.getBody()));
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
2. **添加日程参与者**：根据日程`id`，调用服务端API-[添加日程参与者](0258-add-schedule-participant.md)接口，进行日程参与者的添加操作。

   ```
   public void addCalendarParticipants() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client  = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           AddAttendeeHeaders addAttendeeHeaders = new AddAttendeeHeaders();
           addAttendeeHeaders.xAcsDingtalkAccessToken = "accessToken";
           AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd attendeesToAdd0 = new AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd()
                   .setId("日程参与者unionId")
                   .setIsOptional(false);
           AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd attendeesToAdd1 = new AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd()
                   .setId("日程参与者unionId")
                   .setIsOptional(false);
           AddAttendeeRequest addAttendeeRequest = new AddAttendeeRequest()
                   .setAttendeesToAdd(java.util.Arrays.asList(
                           attendeesToAdd0,
                           attendeesToAdd1
                   ));
           try {
               client.addAttendeeWithOptions("日程组织者unionId", "primary", "日程id", addAttendeeRequest, addAttendeeHeaders, new RuntimeOptions());
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
3. **获取日程参与者**：根据日程`id`，调用服务端API-[获取日程参与者](0261-get-the-participants-of-a-schedule.md)接口，获取日程参与人的信息。

   ```
   public void getCalendarParticipants() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client  = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           ListAttendeesHeaders listAttendeesHeaders = new ListAttendeesHeaders();
           listAttendeesHeaders.xAcsDingtalkAccessToken = "accessToken";
           ListAttendeesRequest listAttendeesRequest = new ListAttendeesRequest()
                   .setMaxResults(100);
           try {
               ListAttendeesResponse listAttendeesResponse = client.listAttendeesWithOptions("日程组织者unionId", "primary", "日程id", listAttendeesRequest, listAttendeesHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(listAttendeesResponse.getBody()));
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
4. **设置日程响应邀请状态**：根据日程`id`，调用服务端API-[设置日程响应邀请状态](0260-configure-response-status.md)接口，进行日程参与者响应的邀请状态。

   ```
   public void setCalendarResponseStatus() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client  = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           RespondEventHeaders respondEventHeaders = new RespondEventHeaders();
           respondEventHeaders.xAcsDingtalkAccessToken = "accessToken";
           RespondEventRequest respondEventRequest = new RespondEventRequest()
                   .setResponseStatus("accepted");
           try {
               client.respondEventWithOptions("日程参与者unionId", "primary", "日程id", respondEventRequest, respondEventHeaders, new RuntimeOptions());
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

   - `userId`（Path参数）：日程参与者的unionId
   - `calendarId`（Path参数）：日历ID，统一为`primary`
   - `eventId`（Path参数）：日程ID
   - `responseStatus`：**重点参数**，响应状态取值：`accepted`（已接受）、`declined`（已拒绝）、`tentative`（暂定）、`needsAction`（未操作，默认状态）
5. 删除日程参与者：根据日程`id`，调用服务端API-[删除日程参与者](0259-delete-schedule-participant.md)接口，进行日程参与者的删除操作。

   ```
   public void deleteCalendarParticipants() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client  = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           RemoveAttendeeHeaders removeAttendeeHeaders = new RemoveAttendeeHeaders();
           removeAttendeeHeaders.xAcsDingtalkAccessToken = "accessToken";
           RemoveAttendeeRequest.RemoveAttendeeRequestAttendeesToRemove attendeesToRemove0 = new RemoveAttendeeRequest.RemoveAttendeeRequestAttendeesToRemove()
                   .setId("日程参与者unionId");
           RemoveAttendeeRequest removeAttendeeRequest = new RemoveAttendeeRequest()
                   .setAttendeesToRemove(java.util.Arrays.asList(
                           attendeesToRemove0
                   ));
           try {
               client.removeAttendeeWithOptions("日程组织者unionId", "primary", "日程id", removeAttendeeRequest, removeAttendeeHeaders, new RuntimeOptions());
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

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ 日程读写权限申请成功。
- ✅ access\_token获取成功。
- ✅ 创建日程接口调用成功，日程出现在钉钉日历。
- ✅ 添加参会人接口调用成功，参会人出现在日程参会人列表。
- ✅ 查询参会人接口调用成功，返回正确的参会人信息。
- ✅ 设置响应状态接口调用成功，参会人状态已更新。
- ✅ 删除参会人接口调用成功，参会人已从日程移除。

## 常见问题（FAQ）

- **Q1：添加参会人时必填哪些参数？**

  A：必填参数包括：

  - `userId`：组织者unionId
  - `eventId`：日程ID
  - `attendees`：参会人列表，每个参会人包含 `userid`（参会人unionId）和 `isOptional`（是否可选参会人）

    可选参数包括 `responseStatus`（初始响应状态）。
- **Q2：参会人响应状态有哪些取值？**

  A：响应状态包括：

  - `needsAction`：未操作（默认状态）
  - `accepted`：已接受
  - `declined`：已拒绝
  - `tentative`：暂定
- **Q3：参会人同步失败的常见原因有哪些？**

  A：常见原因包括：

  - userId不正确（必须是钉钉组织架构中存在的员工unionId）
  - eventId不正确（必须是已创建的日程ID）
  - access\_token无效或已过期
  - 应用未申请日程相关权限
  - 网络请求超时或服务器异常
- **Q4：批量添加参会人的最佳实践是什么？**

  A：当前接口支持单次添加多个参会人（最多500人）。如需批量添加，建议在 `attendees` 数组中传入多个参会人对象，注意控制调用频率避免触发限流。
