---
title: "创建、修改、查询及删除日程"
source_url: "https://open.dingtalk.com/document/development/create-and-delete-an-event"
namespace: "development"
slug: "create-and-delete-an-event"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 使用教程 > 创建、修改、查询及删除日程"
doc_id: "OwdmZThLzn"
updated_at: "2026-07-02 10:36:20"
---

> Source: https://open.dingtalk.com/document/development/create-and-delete-an-event
> Path: 应用开发 / 服务端API / 日程 > 使用教程 > 创建、修改、查询及删除日程
> Updated: 2026-07-02 10:36:20

# 创建、修改、查询及删除日程

本文档介绍了如何调用日程接口创建日程等流程。首先创建一个企业内部应用，再使用日程提供的API，实现创建日程、修改日程、查询单个日程详情、删除日程流程。

## **预期效果**

创建日程后，效果如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0879592871/p485300.png)

## 接入流程简介

本文档展示了创建一个企业内部应用，再使用日程提供的API，实现创建日程、修改日程、查询单个日程详情、删除日程流程。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请日程相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端日程相关API：

1. 调用服务端API-[创建日程](0250-create-schedule.md)接口，进行创建日程。获取日程`id`。
2. 根据日程`id`，调用服务端API-[修改日程](0252-modify-event.md)接口，进行日程信息修改。
3. 根据日程`id`，调用服务端API-[查询单个日程详情](0253-query-details-about-an-event.md)接口，获取日程详情信息。
4. 根据日程`id`，调用服务端API-[删除日程](0251-delete-event.md)接口，删除创建的日程。

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

1. 调用服务端API-[创建日程](0250-create-schedule.md)接口，进行创建日程。获取日程`id`。

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
                   .setId("日程参与人unionId")
                   .setIsOptional(false);
           CreateEventRequest.CreateEventRequestAttendees attendees1 = new CreateEventRequest.CreateEventRequestAttendees()
                   .setId("日程参与人unionId")
                   .setIsOptional(false);
           CreateEventRequest.CreateEventRequestAttendees attendees2 = new CreateEventRequest.CreateEventRequestAttendees()
                   .setId("日程参与人unionId")
                   .setIsOptional(false);
           CreateEventRequest.CreateEventRequestRecurrenceRange recurrenceRange = new CreateEventRequest.CreateEventRequestRecurrenceRange()
                   .setType("numbered")
                   .setNumberOfOccurrences(2);
           CreateEventRequest.CreateEventRequestRecurrencePattern recurrencePattern = new CreateEventRequest.CreateEventRequestRecurrencePattern()
                   .setType("daily")
                   .setInterval(1);
           CreateEventRequest.CreateEventRequestRecurrence recurrence = new CreateEventRequest.CreateEventRequestRecurrence()
                   .setPattern(recurrencePattern)
                   .setRange(recurrenceRange);
           CreateEventRequest.CreateEventRequestEnd end = new CreateEventRequest.CreateEventRequestEnd()
                   .setDate("2022-09-03");
   //                .setDateTime("2021-09-20T10:15:30+08:00")
   //                .setTimeZone("Asia/Shanghai");
           CreateEventRequest.CreateEventRequestStart start = new CreateEventRequest.CreateEventRequestStart()
                   .setDate("2022-09-02");
   //                .setDateTime("2021-09-20T10:15:30+08:00")
   //                .setTimeZone("Asia/Shanghai");
           CreateEventRequest createEventRequest = new CreateEventRequest()
                   .setSummary("0902创建日程")
                   .setDescription("这是0902创建的一个日程")
                   .setStart(start)
                   .setEnd(end)
                   .setIsAllDay(true)
                   .setRecurrence(recurrence)
                   .setAttendees(java.util.Arrays.asList(
                           attendees0,
                           attendees1,
                           attendees2
                   ))
                   .setLocation(location)
                   .setReminders(java.util.Arrays.asList(
                           reminders0
                   ))
                   .setOnlineMeetingInfo(onlineMeetingInfo)
                   .setExtra(extra);
           try {
               CreateEventResponse eventWithOptions = client.createEventWithOptions("日程组织人unionId", "primary", createEventRequest, createEventHeaders, new RuntimeOptions());
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
2. 根据日程`id`，调用服务端API-[修改日程](0252-modify-event.md)接口，进行日程信息修改。

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
3. 根据日程`id`，调用服务端API-[查询单个日程详情](0253-query-details-about-an-event.md)接口，获取日程详情信息。

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
4. 根据日程`id`，调用服务端API-[删除日程](0251-delete-event.md)接口，删除创建的日程。

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

> **[!NOTE]**
>
> 支持以下2种删除场景：
>
> - 当组织者删除日程时（Path参数中的userId参数使用组织者uninoId），所有参与者会收到日程取消通知，同时日程将从所有参与者的日历中删除。
> - 当参与者删除日程时（Path参数中的userId参数使用参与者uninoId），仅将日程从自己的日历中删除，其他日程参与者不受影响。
