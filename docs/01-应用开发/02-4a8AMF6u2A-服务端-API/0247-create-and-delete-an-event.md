---
title: "日程全生命周期管理：从创建到删除的完整流程"
source_url: "https://open.dingtalk.com/document/development/create-and-delete-an-event"
namespace: "development"
slug: "create-and-delete-an-event"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 使用教程 > 日程全生命周期管理：从创建到删除的完整流程"
doc_id: "OwdmZThLzn"
updated_at: "2026-09-23 12:04:33"
---

> Source: https://open.dingtalk.com/document/development/create-and-delete-an-event
> Path: 应用开发 / 服务端 API / 日程 > 使用教程 > 日程全生命周期管理：从创建到删除的完整流程
> Updated: 2026-09-23 12:04:33

# 日程全生命周期管理：从创建到删除的完整流程

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现日程的创建、修改、查询及删除，支持将业务系统中的会议、任务等事件自动同步至钉钉日历，实现统一日程管理。

## 概述

本方案提供一套完整的日程数据同步解决方案，通过钉钉开放平台的日程管理API，实现将企业自有系统中的会议、任务、里程碑等事件自动同步至钉钉日历应用。

### 方案背景

企业在日常运营中常面临以下痛点：

- **日程分散**：业务系统、OA系统、项目管理工具中的日程各自独立，员工需在多个平台间切换查看
- **通知缺失**：外部系统创建的日程无法触发钉钉消息提醒，容易遗漏重要事项
- **协同困难**：跨部门会议安排依赖人工沟通，缺乏统一的日程视图和冲突检测机制
- **数据孤岛**：日程数据未与企业通讯录、考勤、审批等模块打通，无法形成完整的数字化办公闭环

### 核心价值

本方案提供一套完整的日程数据同步解决方案，通过钉钉开放平台的日程管理API，实现将企业自有系统中的会议、任务、里程碑等事件自动同步至钉钉日历应用。

- **统一入口**：所有日程汇聚至钉钉日历，员工无需切换多个系统即可查看完整日程安排
- **智能提醒**：同步后的日程自动触发钉钉消息、DING通知，确保重要事项不遗漏
- **高效协同**：基于钉钉组织架构自动匹配参会人员，支持日程冲突检测和空闲时段推荐
- **数据联动**：日程与考勤、审批、待办等模块联动，例如会议结束后自动生成会议纪要待办

### 适用场景

本方案适用于以下典型业务场景：

- **企业内部会议管理系统与钉钉日历同步**：自研会议管理系统中的会议室预订和参会安排自动同步至钉钉日历
- **项目管理工具里程碑事件同步**：将外部工具中的版本发布、评审会等关键节点同步至团队成员钉钉日历
- **CRM客户拜访计划同步**：销售人员的客户拜访计划从CRM系统自动同步至钉钉日历并触发提醒
- **培训报名系统与钉钉日历联动**：培训课程信息自动创建为钉钉日历事件，学员一键加入日程

## 典型业务场景

### 场景一：内部会议系统同步至钉钉日历

#### 痛点分析

企业使用自研会议管理系统安排会议室和参会人员，但员工仍需在钉钉日历中手动创建对应日程，导致：

- 重复录入，效率低下且易出错
- 会议变更时两个系统不同步，产生信息差
- 无法利用钉钉的日程提醒和冲突检测功能

#### 价值验证

- **自动化流程**

  ![meeting_sync_flow](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3726310971/p1103229.png)
- **关键优势**

  - **秒级自动同步**：会议创建后1秒内自动同步至所有参会者钉钉日历，无需手动操作。
  - **状态实时回写**：支持会议室预订状态实时回写至会议系统，确保双端数据一致。
  - **变更自动通知**：会议时间、地点、参会人变更时自动推送更新通知，无需人工干预。

### 场景二：项目里程碑事件同步

#### 痛点分析

项目管理工具中的关键节点（如版本发布、评审会、交付日）仅存在于项目系统中，团队成员容易遗忘：

- 非项目成员无法感知关键时间节点
- 缺乏统一的里程碑视图，跨项目协调困难
- 到期前无主动提醒，依赖人工跟进

#### 价值验证

- **自动化流程**

  ![milestone_sync_flow](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3726310971/p1103231.png)
- **关键优势**

  - **自动关联人员**：里程碑事件自动关联项目负责人和核心成员，无需手动添加参会者。
  - **DING紧急提醒**：支持提前N天触发钉钉DING紧急提醒，确保重要节点不遗漏。
  - **闭环状态标记**：里程碑完成后自动标记日程状态，形成完整的项目进度闭环。

## 实施指南

### 技术架构

- **接口调用层**：调用日程服务端API实现日程的创建、修改、查询、删除操作。
- **用户标识获取层**：调用通讯录服务端API获取部门用户详情，获取企业员工在钉钉组织架构中的userId值信息。
- **日程数据同步层**：调用日程服务端API将自有系统的日程信息同步到钉钉日历应用。

### 前置条件

在实施方案前，需满足以下条件：

- 应用准备：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- 权限要求：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `Calendar.Event.Write`（日历应用中日程写权限）
  - `Calendar.Event.Read`（日历应用中日程读权限）
- 开发环境：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- SDK准备：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请日程相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端日程相关API：

1. 调用服务端API-[创建日程](0252-create-schedule.md)接口，进行创建日程。获取日程`id`。
2. 根据日程`id`，调用服务端API-[修改日程](0254-modify-event.md)接口，进行日程信息修改。
3. 根据日程`id`，调用服务端API-[查询单个日程详情](0255-query-details-about-an-event.md)接口，获取日程详情信息。
4. 根据日程`id`，调用服务端API-[删除日程](0253-delete-event.md)接口，删除创建的日程。

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

   - `Calendar.Event.Write`（日历应用中日程写权限）— 用于创建、修改、删除日程。
   - `Calendar.Event.Read`（日历应用中日程读权限）— 用于查询日程详情。

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
2. **查询日程详情**：根据日程`id`，调用服务端API-[查询单个日程详情](0255-query-details-about-an-event.md)接口，获取指定日程的完整信息。

   ```
    public void calendarInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           GetEventHeaders getEventHeaders = new GetEventHeaders();
           getEventHeaders.xAcsDingtalkAccessToken = "accessToken";
           GetEventRequest getEventRequest = new GetEventRequest()
                   .setMaxAttendees(100L);
           try {
               GetEventResponse eventWithOptions = client.getEventWithOptions("日程组织者unionId", "primary", "日程id", getEventRequest, getEventHeaders, new RuntimeOptions());
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
3. **修改日程**：根据日程`id`，调用服务端API-[修改日程](0254-modify-event.md)接口，更新已有日程的时间、参与者、描述等信息。

   ```
   public void  updateCalendar() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           PatchEventHeaders patchEventHeaders = new PatchEventHeaders();
           patchEventHeaders.xAcsDingtalkAccessToken = "accessToken";
           PatchEventRequest.PatchEventRequestReminders reminders0 = new PatchEventRequest.PatchEventRequestReminders()
                   .setMethod("dingtalk")
                   .setMinutes(15);
           java.util.Map<String, String> extra = TeaConverter.buildMap(
                   new TeaPair("noChatNotification", "false"),
                   new TeaPair("noPushNotification","false")
           );
           PatchEventRequest.PatchEventRequestLocation location = new PatchEventRequest.PatchEventRequestLocation()
                   .setDisplayName("room 1-2-3");
           PatchEventRequest.PatchEventRequestAttendees attendees0 = new PatchEventRequest.PatchEventRequestAttendees()
                   .setId("日程参与人unionId")
                   .setIsOptional(false);
           PatchEventRequest.PatchEventRequestRecurrenceRange recurrenceRange = new PatchEventRequest.PatchEventRequestRecurrenceRange()
                   .setType("numbered")
                   .setNumberOfOccurrences(1);
           PatchEventRequest.PatchEventRequestRecurrencePattern recurrencePattern = new PatchEventRequest.PatchEventRequestRecurrencePattern()
                   .setType("daily")
                   .setInterval(1);
           PatchEventRequest.PatchEventRequestRecurrence recurrence = new PatchEventRequest.PatchEventRequestRecurrence()
                   .setPattern(recurrencePattern)
                   .setRange(recurrenceRange);
           PatchEventRequest.PatchEventRequestEnd end = new PatchEventRequest.PatchEventRequestEnd()
                   .setDate("2022-09-02");
           PatchEventRequest.PatchEventRequestStart start = new PatchEventRequest.PatchEventRequestStart()
                   .setDate("2022-09-02");
           PatchEventRequest patchEventRequest = new PatchEventRequest()
                   .setSummary("0902修改日程内容")
                   .setId("日程id")
                   .setDescription("这是一个0902修改的日程")
                   .setStart(start)
                   .setEnd(end)
                   .setIsAllDay(true)
                   .setRecurrence(recurrence)
                   .setAttendees(java.util.Arrays.asList(
                           attendees0
                   ))
                   .setLocation(location)
                   .setExtra(extra)
                   .setReminders(java.util.Arrays.asList(
                           reminders0
                   ));
           try {
               PatchEventResponse patchEventResponse = client.patchEventWithOptions("日程组织者unionId", "primary", "日程id", patchEventRequest, patchEventHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(patchEventResponse.getBody()));
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
4. **删除日程**：根据日程`id`，调用服务端API-[删除日程](0253-delete-event.md)接口，移除不再需要的日程。

   > **[!NOTE]**
   >
   > 支持两种删除场景：
   >
   > - **组织者删除**：Path参数中的userId使用组织者unionId，所有参与者会收到日程取消通知，同时日程将从所有参与者的日历中删除。
   > - **参与者删除**：Path参数中的userId使用参与者unionId，仅将日程从自己的日历中删除，其他日程参与者不受影响。

   ```
   public void  deleteCalendar() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           DeleteEventHeaders deleteEventHeaders = new DeleteEventHeaders();
           deleteEventHeaders.xAcsDingtalkAccessToken = "accessToken";
           try {
               client.deleteEventWithOptions("日程组织者unionId", "primary", "日程id", deleteEventHeaders, new RuntimeOptions());
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
- ✅ 查询日程接口调用成功，返回正确的日程详情。
- ✅ 修改日程接口调用成功，日程信息已更新。
- ✅ 删除日程接口调用成功，日程已从日历移除。

## 常见问题（FAQ）

- **Q1：创建日程时必填哪些参数？**

  A：必填参数包括：

  - `calendarId`：日历ID，个人日历使用 `primary`
  - `summary`：日程标题
  - `start`：开始时间（ISO 8601格式）
  - `end`：结束时间（ISO 8601格式）

    可选参数包括 `description`（日程描述）、`attendees`（参会者列表）、`location`（地点）等。
- **Q2：删除日程时组织者和参与者有什么区别？**

  A：当组织者删除日程时（Path参数中的userId使用组织者unionId），所有参与者会收到日程取消通知，同时日程将从所有参与者的日历中删除。当参与者删除日程时（Path参数中的userId使用参与者unionId），仅将日程从自己的日历中删除，其他日程参与者不受影响。
- **Q3：日程同步失败的常见原因有哪些？**

  A：常见原因包括：

  - userId不正确（必须是钉钉组织架构中存在的员工unionId）。
  - 时间格式错误（必须使用ISO 8601格式，如 `2026-09-25T10:00:00+08:00`）。
  - `accessToken`无效或已过期。
  - 应用未申请日程相关权限。
  - 网络请求超时或服务器异常。
- **Q4：批量创建日程的最佳实践是什么？**

  A：当前接口支持单次创建一个日程。如需批量创建，建议在业务层循环调用该接口，注意控制调用频率避免触发限流。
