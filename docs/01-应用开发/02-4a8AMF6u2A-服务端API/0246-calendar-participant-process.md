---
title: "添加、获取及删除日程参与者"
source_url: "https://open.dingtalk.com/document/development/calendar-participant-process"
namespace: "development"
slug: "calendar-participant-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 使用教程 > 添加、获取及删除日程参与者"
doc_id: "fRiCYfHaWR"
updated_at: "2026-07-02 10:36:22"
---

> Source: https://open.dingtalk.com/document/development/calendar-participant-process
> Path: 应用开发 / 服务端API / 日程 > 使用教程 > 添加、获取及删除日程参与者
> Updated: 2026-07-02 10:36:22

# 添加、获取及删除日程参与者

本文档介绍了如何调用日程相关接口实现日程参与者的相关流程。首先创建一个企业内部应用，再使用日程提供的API，实现创建日程、添加日程参与者、获取日程参与者、设置日程响应邀请状态、删除日程参与者流程。

## **预期效果**

日程创建成功后，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2879592871/p486863.png)

## 接入流程简介

本文档展示了创建一个企业内部应用，再使用日程提供的API，实现日程参与者的相关操作流程。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请日程相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端日程相关API。

1. 调用服务端API-[创建日程](0250-create-schedule.md)接口，进行创建日程。获取日程`id`。
2. 根据日程`id`，调用服务端API-[添加日程参与者](0256-add-schedule-participant.md)接口，进行日程参与者的添加操作。
3. 根据日程`id`，调用服务端API-[获取日程参与者](0259-get-the-participants-of-a-schedule.md)接口，获取日程参与人的信息。
4. 根据日程`id`，调用服务端API-[设置日程响应邀请状态](0258-configure-response-status.md)接口，进行日程参与者响应的邀请状态。
5. 根据日程`id`，调用服务端API-[删除日程参与者](0257-delete-schedule-participant.md)接口，进行日程参与者的删除操作。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`Calendar.Event.Write`和`Calendar.Event.Read`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。

```
 public void getAccessToken() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("ding*********hgn")
                .setAppSecret("9G_O**********xamBkhgGIO");
        GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
        System.out.println(JSON.toJSONString(accessToken.getBody()));
    }
```

## 步骤四：调用服务端日程相关API

1. 调用服务端API-[创建日程](0250-create-schedule.md)接口，进行创建日程，获取日程`id`。

   ```
   public void createCalendar() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcalendar_1_0.Client client = new com.aliyun.dingtalkcalendar_1_0.Client(config);
           CreateEventHeaders createEventHeaders = new CreateEventHeaders();
           createEventHeaders.xAcsDingtalkAccessToken = "accessToken";
           java.util.Map<String, String> extra = TeaConverter.buildMap(
                   new TeaPair("noChatNotification", "false"),
                   new TeaPair("noPushNotification","false")
           );
           CreateEventRequest.CreateEventRequestOnlineMeetingInfo onlineMeetingInfo = new CreateEventRequest.CreateEventRequestOnlineMeetingInfo()
                   .setType("dingtalk");
           CreateEventRequest.CreateEventRequestReminders reminders0 = new CreateEventRequest.CreateEventRequestReminders()
                   .setMethod("dingtalk")
                   .setMinutes(15);
           CreateEventRequest.CreateEventRequestLocation location = new CreateEventRequest.CreateEventRequestLocation()
                   .setDisplayName("********A座9F");
           CreateEventRequest.CreateEventRequestAttendees attendees0 = new CreateEventRequest.CreateEventRequestAttendees()
                   .setId("日程参与者unionId")
                   .setIsOptional(false);
           CreateEventRequest.CreateEventRequestRecurrenceRange recurrenceRange = new CreateEventRequest.CreateEventRequestRecurrenceRange()
                   .setType("numbered")
                   .setNumberOfOccurrences(1);
           CreateEventRequest.CreateEventRequestRecurrencePattern recurrencePattern = new CreateEventRequest.CreateEventRequestRecurrencePattern()
                   .setType("daily")
                   .setInterval(1);
           CreateEventRequest.CreateEventRequestRecurrence recurrence = new CreateEventRequest.CreateEventRequestRecurrence()
                   .setPattern(recurrencePattern)
                   .setRange(recurrenceRange);
           CreateEventRequest.CreateEventRequestEnd end = new CreateEventRequest.CreateEventRequestEnd()
                   .setDate("2022-09-07");
   //                .setDateTime("2021-09-20T10:15:30+08:00")
   //                .setTimeZone("Asia/Shanghai");
           CreateEventRequest.CreateEventRequestStart start = new CreateEventRequest.CreateEventRequestStart()
                   .setDate("2022-09-07");
   //                .setDateTime("2021-09-20T10:15:30+08:00")
   //                .setTimeZone("Asia/Shanghai");
           CreateEventRequest createEventRequest = new CreateEventRequest()
                   .setSummary("创建日程")
                   .setDescription("这是创建的一个日程")
                   .setStart(start)
                   .setEnd(end)
                   .setIsAllDay(true)
                   .setRecurrence(recurrence)
                   .setAttendees(java.util.Arrays.asList(
                           attendees0
                   ))
                   .setLocation(location)
                   .setReminders(java.util.Arrays.asList(
                           reminders0
                   ))
                   .setOnlineMeetingInfo(onlineMeetingInfo)
                   .setExtra(extra);
           try {
               CreateEventResponse eventWithOptions = client.createEventWithOptions("日程组织者unionId", "primary", createEventRequest, createEventHeaders, new RuntimeOptions());
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
2. 根据日程`id`，调用服务端API-[添加日程参与者](0256-add-schedule-participant.md)接口，进行日程参与者的添加操作。

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
3. 根据日程`id`，调用服务端API-[获取日程参与者](0259-get-the-participants-of-a-schedule.md)接口，获取日程参与人的信息。

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
4. 根据日程`id`，调用服务端API-[设置日程响应邀请状态](0258-configure-response-status.md)接口，进行日程参与者响应的邀请状态。

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
5. 根据日程`id`，调用服务端API-[删除日程参与者](0257-delete-schedule-participant.md)接口，进行日程参与者的删除操作。

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
