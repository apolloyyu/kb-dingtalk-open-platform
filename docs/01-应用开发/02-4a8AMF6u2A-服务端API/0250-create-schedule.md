---
title: "创建日程"
source_url: "https://open.dingtalk.com/document/development/create-schedule"
namespace: "development"
slug: "create-schedule"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 日程 > 创建日程"
doc_id: "RXmKYv9nS7"
updated_at: "2026-06-02 09:24:57"
---

> Source: https://open.dingtalk.com/document/development/create-schedule
> Path: 应用开发 / 服务端API / 日程 > 日程 > 创建日程
> Updated: 2026-06-02 09:24:57

# 创建日程

调用本接口，创建一个日程。

## 接口调用说明

- 每次日程参与者操作最大支持500人，最大支持操作5000人的日程。
- 日程参与者的添加和删除：建议使用[新增日程参与人](0256-add-schedule-participant.md)和[删除日程参与人](0257-delete-schedule-participant.md)接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Event.Write-日历应用中日程写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-client-token | String | 否 | 幂等校验。    - 相同的`x-client-token`表示同一次请求。 - 过期失效，1天。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取企业accessToken(应用商店应用)](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 日程组织者的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历ID，统一为**primary**，表示用户的主日历。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| summary | String | 是 | 日程标题，最大不超过2048个字符。 |
| description | String | 否 | 日程描述，最大不超过5000个字符。 |
| start | Object | 是 | 日程开始时间。 |
| date | String | 否 | 日程开始日期，格式：yyyy-MM-dd。    - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 否 | 日程开始时间，格式为ISO-8601的date-time格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 否 | 日程开始时间所属时区，TZ database name格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| end | Object | 否 | 日程结束时间。 |
| date | String | 否 | 日程结束日期，格式：yyyy-MM-dd。    - 全天日程：    - 必须有值   - 结束时间需传 T+1   例如 **2024-06-01** 的全天日程，开始时间为 **2024-06-01**，则结束时间应该写 **2024-06-02。**   - 非全天日程必须留空 |
| dateTime | String | 否 | 日程结束时间，格式为ISO-8601的date-time格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 否 | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| isAllDay | Boolean | 否 | 是否全天日程。   - **true**：是 - **false**：不是 |
| recurrence | Object | 否 | 日程循环规则。 |
| pattern | Object | 否 | 循环规则。 |
| type | String | 否 | 循环规则类型。   - **daily**：每**interval**天重复 - **weekly**：每**interval**周的第**daysOfWeek**天重复 - **absoluteMonthly**：每**interval**月的第**dayOfMonth**天重复 - **relativeMonthly**：每**interval**月的第**index**周的第**daysOfWeek**天重复 - **absoluteYearly**：每**interval**年重复 |
| dayOfMonth | Integer | 否 | 当循环规则的**type**值为**absoluteMonthly**时，用于指定是每个月的第几天。 |
| daysOfWeek | String | 否 | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| index | String | 否 | 当**type**值为**relativeMonthly**时，用于指定每月第几周。   - **first**：第一周 - **second**：第二周 - **third**：第三周 - **fourth**：第四周 - **last**：最后一周 |
| interval | Integer | 否 | 循环间隔，根据type不同单位不同。    例如：   - 当**type**取值为**daily**时表示间隔N天。 - 当**type**取值为**absoluteYearly**则表示间隔N年。 |
| firstDayOfWeek | String | 否 | 一周起始日，可取值包括：sunday、monday、tuesday、wednesday、thursday、friday、saturday。 默认值为“sunday”。 |
| range | Object | 否 | 循环范围。 |
| type | String | 否 | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| endDate | String | 否 | 循环结束时间。    **endDate**和**numberOfOccurrences**不可同时设定。 |
| numberOfOccurrences | Integer | 否 | 循环次数。    **endDate**和**numberOfOccurrences**不可同时设定。 |
| attendees | Array | 否 | 日程参与人列表，最多支持500个参与人。 |
| id | String | 否 | 用户的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| isOptional | Boolean | 否 | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| location | Object | 否 | 日程地点。 |
| displayName | String | 否 | 日程地点的名称。 |
| reminders | Array | 否 | 日程提醒，可以添加多个。   - 如果不传默认提醒时间为：开始前15分钟提醒。 - 如果传空数据表示不创建任何提醒。 |
| method | String | 否 | 提醒方式。   - **dingtalk**: 钉钉内提醒 |
| minutes | Integer | 否 | 在日程开始前N分钟发出提醒。 |
| onlineMeetingInfo | Object | 否 | 创建日程同时创建线上会议。 |
| type | String | 否 | 线上会议类型。   - **dingtalk**: 钉钉视频会议 |
| extra | Map<String, String> | 否 | JSON格式的扩展能力开关，选填，具体属性定义如下。   - **noPushNotification**：创建日程时是否向关联人员发送钉钉推送通知。    - **true**：不发送   - **false**：发送 - **noChatNotification**：创建日程时是否向参与人发送单聊卡片。    - **true**：不发送   - **false**：发送 |
| uiConfigs | Array | 否 | UI配置，控制日程详情页内组件的展示。 |
| uiName | String | 否 | 组件名称，可取值（持续更新）：   - **updateEventButton**：编辑日程按钮 - **deleteEventButton**：删除日程按钮 - **transferEventButton**：转让日程按钮 - **attendee**：参与人区域 - **comment**：日程评论区域 |
| uiStatus | String | 否 | 组件状态，可取值：   - **hide**：隐藏 - **disable**: 禁用（新版详情页支持，低版本暂不支持disable，组件将被隐藏）    按钮类：无法点击。   区域类：无法交互。如将评论区域设置为disable，那么无法写评论，但是评论内容依然可见。 - **enable**：可使用（默认状态） |
| richTextDescription | Object | 否 | 富文本描述。 |
| text | String | 否 | 富文本描述内容。 |

### 请求示例

HTTP

```
POST /v1.0/calendar/users/iiiP35sJadba8aBSgjrwPRKgiEiF/calendars/primary/events HTTP/1.1
Host:api.dingtalk.com
x-client-token:******
x-acs-dingtalk-access-token:cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT01
Content-Type:application/json

{
  "summary" : "test event",
  "description" : "something about this event",
  "start" : {
    "date" : "2021-09-20",
    "dateTime" : "2021-09-20T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "end" : {
    "date" : "2020-09-21",
    "dateTime" : "2021-09-20T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "isAllDay" : false,
  "recurrence" : {
    "pattern" : {
      "type" : "daily",
      "dayOfMonth" : 1,
      "daysOfWeek" : "monday",
      "index" : "last",
      "interval" : 1,
      "firstDayOfWeek" : "monday"
    },
    "range" : {
      "type" : "endDate",
      "endDate" : "2021-12-31T10:15:30+08:00",
      "numberOfOccurrences" : 5
    }
  },
  "attendees" : [ {
    "id" : "iiiP35sJxxx",
    "isOptional" : false
  } ],
  "location" : {
    "displayName" : "dingtalk"
  },
  "reminders" : [ {
    "method" : "dingtalk",
    "minutes" : 15
  } ],
  "onlineMeetingInfo" : {
    "type" : "dingtalk"
  },
 "extra" : {
    {"noChatNotification": "true", "noPushNotification": "true" }
  },
  "uiConfigs" : [ {
    "uiName" : "updateEventButton",
    "uiStatus" : "hide"
  } ],
  "richTextDescription" : {
    "text" : "<div class=\\\"__aliyun_email_body_block\\\"><div  style=\\\"clear:both;\\\"><span  style=\\\"text-decoration:line-through;\\\">测试测试</span></div><div  style=\\\"clear:both;\\\"><span  style=\\\"color:#ff0000;\\\">热热热</span></div><div  style=\\\"clear:both;\\\"><span  style=\\\"text-decoration:underline;\\\">单独的</span></div><div  style=\\\"clear:both;\\\"><span  style=\\\"font-weight:700;\\\">啊啊啊</span></div><div  style=\\\"clear:both;\\\"><span  style=\\\"font-weight:700;font-style:italic;\\\">事实上</span></div></div>"
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcalendar_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcalendar_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcalendar_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventHeaders createEventHeaders = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventHeaders();
        createEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRichTextDescription richTextDescription = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRichTextDescription()
                .setText("<div class=\"__aliyun_email_body_block\"><div  style=\"clear:both;\"><span  style=\"text-decoration:line-through;\">测试测试</span></div><div  style=\"clear:both;\"><span  style=\"color:#ff0000;\">热热热</span></div><div  style=\"clear:both;\"><span  style=\"text-decoration:underline;\">单独的</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;\">啊啊啊</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;font-style:italic;\">事实上</span></div></div>");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestUiConfigs uiConfigs0 = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestUiConfigs()
                .setUiName("updateEventButton")
                .setUiStatus("hide");
       java.util.Map<String, String> extra = TeaConverter.buildMap(
                new TeaPair("noChatNotification", "true"),
                new TeaPair("noPushNotification","true")
        );
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestOnlineMeetingInfo onlineMeetingInfo = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestOnlineMeetingInfo()
                .setType("dingtalk");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestReminders reminders0 = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestReminders()
                .setMethod("dingtalk")
                .setMinutes(15);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestLocation location = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestLocation()
                .setDisplayName("dingtalk");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestAttendees attendees0 = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestAttendees()
                .setId("iiiP35sJxxx")
                .setIsOptional(false);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrenceRange recurrenceRange = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrenceRange()
                .setType("endDate")
                .setEndDate("2021-12-31T10:15:30+08:00")
                .setNumberOfOccurrences(5);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrencePattern recurrencePattern = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrencePattern()
                .setType("daily")
                .setDayOfMonth(1)
                .setDaysOfWeek("monday")
                .setIndex("last")
                .setInterval(1)
                .setFirstDayOfWeek("monday");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrence recurrence = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestRecurrence()
                .setPattern(recurrencePattern)
                .setRange(recurrenceRange);
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestEnd end = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestEnd()
                .setDate("2020-09-21")
                .setDateTime("2021-09-20T10:15:30+08:00")
                .setTimeZone("Asia/Shanghai");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestStart start = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest.CreateEventRequestStart()
                .setDate("2021-09-20")
                .setDateTime("2021-09-20T10:15:30+08:00")
                .setTimeZone("Asia/Shanghai");
        com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest createEventRequest = new com.aliyun.dingtalkcalendar_1_0.models.CreateEventRequest()
                .setSummary("test event")
                .setDescription("something about this event")
                .setStart(start)
                .setEnd(end)
                .setIsAllDay(false)
                .setRecurrence(recurrence)
                .setAttendees(java.util.Arrays.asList(
                    attendees0
                ))
                .setLocation(location)
                .setReminders(java.util.Arrays.asList(
                    reminders0
                ))
                .setOnlineMeetingInfo(onlineMeetingInfo)
                .setExtra(extra)
                .setUiConfigs(java.util.Arrays.asList(
                    uiConfigs0
                ))
                .setRichTextDescription(richTextDescription);
        try {
            client.createEventWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "primary", createEventRequest, createEventHeaders, new com.aliyun.teautil.models.RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

Python

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_dingtalk.calendar_1_0.client import Client as dingtalkcalendar_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.calendar_1_0 import models as dingtalkcalendar__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcalendar_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcalendar_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_event_headers = dingtalkcalendar__1__0_models.CreateEventHeaders()
        create_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        rich_text_description = dingtalkcalendar__1__0_models.CreateEventRequestRichTextDescription(
            text='<div class="__aliyun_email_body_block"><div  style="clear:both;"><span  style="text-decoration:line-through;">测试测试</span></div><div  style="clear:both;"><span  style="color:#ff0000;">热热热</span></div><div  style="clear:both;"><span  style="text-decoration:underline;">单独的</span></div><div  style="clear:both;"><span  style="font-weight:700;">啊啊啊</span></div><div  style="clear:both;"><span  style="font-weight:700;font-style:italic;">事实上</span></div></div>'
        )
        ui_configs_0 = dingtalkcalendar__1__0_models.CreateEventRequestUiConfigs(
            ui_name='updateEventButton',
            ui_status='hide'
        )
        extra = {
            'noChatNotification': 'true', 
            'noPushNotification': 'true'
        }
        online_meeting_info = dingtalkcalendar__1__0_models.CreateEventRequestOnlineMeetingInfo(
            type='dingtalk'
        )
        reminders_0 = dingtalkcalendar__1__0_models.CreateEventRequestReminders(
            method='dingtalk',
            minutes=15
        )
        location = dingtalkcalendar__1__0_models.CreateEventRequestLocation(
            display_name='dingtalk'
        )
        attendees_0 = dingtalkcalendar__1__0_models.CreateEventRequestAttendees(
            id='iiiP35sJxxx',
            is_optional=False
        )
        recurrence_range = dingtalkcalendar__1__0_models.CreateEventRequestRecurrenceRange(
            type='endDate',
            end_date='2021-12-31T10:15:30+08:00',
            number_of_occurrences=5
        )
        recurrence_pattern = dingtalkcalendar__1__0_models.CreateEventRequestRecurrencePattern(
            type='daily',
            day_of_month=1,
            days_of_week='monday',
            index='last',
            interval=1,
            first_day_of_week='monday'
        )
        recurrence = dingtalkcalendar__1__0_models.CreateEventRequestRecurrence(
            pattern=recurrence_pattern,
            range=recurrence_range
        )
        end = dingtalkcalendar__1__0_models.CreateEventRequestEnd(
            date='2020-09-21',
            date_time='2021-09-20T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        start = dingtalkcalendar__1__0_models.CreateEventRequestStart(
            date='2021-09-20',
            date_time='2021-09-20T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        create_event_request = dingtalkcalendar__1__0_models.CreateEventRequest(
            summary='test event',
            description='something about this event',
            start=start,
            end=end,
            is_all_day=False,
            recurrence=recurrence,
            attendees=[
                attendees_0
            ],
            location=location,
            reminders=[
                reminders_0
            ],
            online_meeting_info=online_meeting_info,
            extra=extra,
            ui_configs=[
                ui_configs_0
            ],
            rich_text_description=rich_text_description
        )
        try:
            client.create_event_with_options('iiiP35sJadba8aBSgjrwPRKgiEiF', 'primary', create_event_request, create_event_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_event_headers = dingtalkcalendar__1__0_models.CreateEventHeaders()
        create_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        rich_text_description = dingtalkcalendar__1__0_models.CreateEventRequestRichTextDescription(
            text='<div class="__aliyun_email_body_block"><div  style="clear:both;"><span  style="text-decoration:line-through;">滚滚滚</span></div><div  style="clear:both;"><span  style="color:#ff0000;">热热热</span></div><div  style="clear:both;"><span  style="text-decoration:underline;">单独的</span></div><div  style="clear:both;"><span  style="font-weight:700;">啊啊啊</span></div><div  style="clear:both;"><span  style="font-weight:700;font-style:italic;">事实上</span></div></div>'
        )
        ui_configs_0 = dingtalkcalendar__1__0_models.CreateEventRequestUiConfigs(
            ui_name='updateEventButton',
            ui_status='hide'
        )
        extra = {
            'key': 'noPushNotification'
        }
        online_meeting_info = dingtalkcalendar__1__0_models.CreateEventRequestOnlineMeetingInfo(
            type='dingtalk'
        )
        reminders_0 = dingtalkcalendar__1__0_models.CreateEventRequestReminders(
            method='dingtalk',
            minutes=15
        )
        location = dingtalkcalendar__1__0_models.CreateEventRequestLocation(
            display_name='dingtalk'
        )
        attendees_0 = dingtalkcalendar__1__0_models.CreateEventRequestAttendees(
            id='iiiP35sJxxx',
            is_optional=False
        )
        recurrence_range = dingtalkcalendar__1__0_models.CreateEventRequestRecurrenceRange(
            type='endDate',
            end_date='2021-12-31T10:15:30+08:00',
            number_of_occurrences=5
        )
        recurrence_pattern = dingtalkcalendar__1__0_models.CreateEventRequestRecurrencePattern(
            type='daily',
            day_of_month=1,
            days_of_week='monday',
            index='last',
            interval=1,
            first_day_of_week='monday'
        )
        recurrence = dingtalkcalendar__1__0_models.CreateEventRequestRecurrence(
            pattern=recurrence_pattern,
            range=recurrence_range
        )
        end = dingtalkcalendar__1__0_models.CreateEventRequestEnd(
            date='2020-09-21',
            date_time='2021-09-20T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        start = dingtalkcalendar__1__0_models.CreateEventRequestStart(
            date='2021-09-20',
            date_time='2021-09-20T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        create_event_request = dingtalkcalendar__1__0_models.CreateEventRequest(
            summary='test event',
            description='something about this event',
            start=start,
            end=end,
            is_all_day=False,
            recurrence=recurrence,
            attendees=[
                attendees_0
            ],
            location=location,
            reminders=[
                reminders_0
            ],
            online_meeting_info=online_meeting_info,
            extra=extra,
            ui_configs=[
                ui_configs_0
            ],
            rich_text_description=rich_text_description
        )
        try:
            await client.create_event_with_options_async('iiiP35sJadba8aBSgjrwPRKgiEiF', 'primary', create_event_request, create_event_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

PHP

```
<?php

// This file is auto-generated, don't edit it. Thanks.
namespace AlibabaCloud\SDK\Sample;

use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\richTextDescription;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\uiConfigs;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\onlineMeetingInfo;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\reminders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\location;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\attendees;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\recurrence\range;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\recurrence\pattern;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\recurrence;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\end;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest\start;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateEventRequest;
use AlibabaCloud\Tea\Utils\Utils\RuntimeOptions;

class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Dingtalk Client
     */
    public static function createClient(){
        $config = new Config([]);
        $config->protocol = "https";
        $config->regionId = "central";
        return new Dingtalk($config);
    }

    /**
     * @param string[] $args
     * @return void
     */
    public static function main($args){
        $client = self::createClient();
        $createEventHeaders = new CreateEventHeaders([]);
        $createEventHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $richTextDescription = new richTextDescription([
            "text" => "<div class=\"__aliyun_email_body_block\"><div  style=\"clear:both;\"><span  style=\"text-decoration:line-through;\">测试测试</span></div><div  style=\"clear:both;\"><span  style=\"color:#ff0000;\">热热热</span></div><div  style=\"clear:both;\"><span  style=\"text-decoration:underline;\">单独的</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;\">啊啊啊</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;font-style:italic;\">事实上</span></div></div>"
        ]);
        $uiConfigs0 = new uiConfigs([
            "uiName" => "updateEventButton",
            "uiStatus" => "hide"
        ]);
        $extra = [
            "noChatNotification" => "true”,
            "noPushNotification" => "true"
        ];
        $onlineMeetingInfo = new onlineMeetingInfo([
            "type" => "dingtalk"
        ]);
        $reminders0 = new reminders([
            "method" => "dingtalk",
            "minutes" => 15
        ]);
        $location = new location([
            "displayName" => "dingtalk"
        ]);
        $attendees0 = new attendees([
            "id" => "iiiP35sJxxx",
            "isOptional" => false
        ]);
        $recurrenceRange = new range([
            "type" => "endDate",
            "endDate" => "2021-12-31T10:15:30+08:00",
            "numberOfOccurrences" => 5
        ]);
        $recurrencePattern = new pattern([
            "type" => "daily",
            "dayOfMonth" => 1,
            "daysOfWeek" => "monday",
            "index" => "last",
            "interval" => 1,
            "firstDayOfWeek" => "monday"
        ]);
        $recurrence = new recurrence([
            "pattern" => $recurrencePattern,
            "range" => $recurrenceRange
        ]);
        $end = new end([
            "date" => "2020-09-21",
            "dateTime" => "2021-09-20T10:15:30+08:00",
            "timeZone" => "Asia/Shanghai"
        ]);
        $start = new start([
            "date" => "2021-09-20",
            "dateTime" => "2021-09-20T10:15:30+08:00",
            "timeZone" => "Asia/Shanghai"
        ]);
        $createEventRequest = new CreateEventRequest([
            "summary" => "test event",
            "description" => "something about this event",
            "start" => $start,
            "end" => $end,
            "isAllDay" => false,
            "recurrence" => $recurrence,
            "attendees" => [
                $attendees0
            ],
            "location" => $location,
            "reminders" => [
                $reminders0
            ],
            "onlineMeetingInfo" => $onlineMeetingInfo,
            "extra" => $extra,
            "uiConfigs" => [
                $uiConfigs0
            ],
            "richTextDescription" => $richTextDescription
        ]);
        try {
            $client->createEventWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "primary", $createEventRequest, $createEventHeaders, new RuntimeOptions([]));
        }
        catch (Exception $err) {
            if (!($err instanceof TeaError)) {
                $err = new TeaError([], $err->getMessage(), $err->getCode(), $err);
            }
            if (!Utils::empty_($err->code) && !Utils::empty_($err->message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }
        }
    }
}
$path = __DIR__ . \DIRECTORY_SEPARATOR . '..' . \DIRECTORY_SEPARATOR . 'vendor' . \DIRECTORY_SEPARATOR . 'autoload.php';
if (file_exists($path)) {
    require_once $path;
}
Sample::main(array_slice($argv, 1));
```

Go

```
// This file is auto-generated, don't edit it. Thanks.
package main

import (
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcalendar_1_0  "github.com/alibabacloud-go/dingtalk/calendar_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcalendar_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcalendar_1_0.Client{}
  _result, _err = dingtalkcalendar_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createEventHeaders := &dingtalkcalendar_1_0.CreateEventHeaders{}
  createEventHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  richTextDescription := &dingtalkcalendar_1_0.CreateEventRequestRichTextDescription{
    Text: tea.String("<div class=\"__aliyun_email_body_block\"><div  style=\"clear:both;\"><span  style=\"text-decoration:line-through;\">测试测试</span></div><div  style=\"clear:both;\"><span  style=\"color:#ff0000;\">热热热</span></div><div  style=\"clear:both;\"><span  style=\"text-decoration:underline;\">单独的</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;\">啊啊啊</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;font-style:italic;\">事实上</span></div></div>"),
  }
  uiConfigs0 := &dingtalkcalendar_1_0.CreateEventRequestUiConfigs{
    UiName: tea.String("updateEventButton"),
    UiStatus: tea.String("hide"),
  }
  extra := map[string]*string{
    "noChatNotification": tea.String("true"),
    "noPushNotification": tea.String("true"),
  }
  onlineMeetingInfo := &dingtalkcalendar_1_0.CreateEventRequestOnlineMeetingInfo{
    Type: tea.String("dingtalk"),
  }
  reminders0 := &dingtalkcalendar_1_0.CreateEventRequestReminders{
    Method: tea.String("dingtalk"),
    Minutes: tea.Int32(15),
  }
  location := &dingtalkcalendar_1_0.CreateEventRequestLocation{
    DisplayName: tea.String("dingtalk"),
  }
  attendees0 := &dingtalkcalendar_1_0.CreateEventRequestAttendees{
    Id: tea.String("iiiP35sJxxx"),
    IsOptional: tea.Bool(false),
  }
  recurrenceRange := &dingtalkcalendar_1_0.CreateEventRequestRecurrenceRange{
    Type: tea.String("endDate"),
    EndDate: tea.String("2021-12-31T10:15:30+08:00"),
    NumberOfOccurrences: tea.Int32(5),
  }
  recurrencePattern := &dingtalkcalendar_1_0.CreateEventRequestRecurrencePattern{
    Type: tea.String("daily"),
    DayOfMonth: tea.Int32(1),
    DaysOfWeek: tea.String("monday"),
    Index: tea.String("last"),
    Interval: tea.Int32(1),
    FirstDayOfWeek: tea.String("monday"),
  }
  recurrence := &dingtalkcalendar_1_0.CreateEventRequestRecurrence{
    Pattern: recurrencePattern,
    Range: recurrenceRange,
  }
  end := &dingtalkcalendar_1_0.CreateEventRequestEnd{
    Date: tea.String("2020-09-21"),
    DateTime: tea.String("2021-09-20T10:15:30+08:00"),
    TimeZone: tea.String("Asia/Shanghai"),
  }
  start := &dingtalkcalendar_1_0.CreateEventRequestStart{
    Date: tea.String("2021-09-20"),
    DateTime: tea.String("2021-09-20T10:15:30+08:00"),
    TimeZone: tea.String("Asia/Shanghai"),
  }
  createEventRequest := &dingtalkcalendar_1_0.CreateEventRequest{
    Summary: tea.String("test event"),
    Description: tea.String("something about this event"),
    Start: start,
    End: end,
    IsAllDay: tea.Bool(false),
    Recurrence: recurrence,
    Attendees: []*dingtalkcalendar_1_0.CreateEventRequestAttendees{attendees0},
    Location: location,
    Reminders: []*dingtalkcalendar_1_0.CreateEventRequestReminders{reminders0},
    OnlineMeetingInfo: onlineMeetingInfo,
    Extra: extra,
    UiConfigs: []*dingtalkcalendar_1_0.CreateEventRequestUiConfigs{uiConfigs0},
    RichTextDescription: richTextDescription,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateEventWithOptions(tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF"), tea.String("primary"), createEventRequest, createEventHeaders, &util.RuntimeOptions{})
    if _err != nil {
      return _err
    }

    return nil
  }()

  if tryErr != nil {
    var err = &tea.SDKError{}
    if _t, ok := tryErr.(*tea.SDKError); ok {
      err = _t
    } else {
      err.Message = tea.String(tryErr.Error())
    }
    if !tea.BoolValue(util.Empty(err.Code)) && !tea.BoolValue(util.Empty(err.Message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }

  }
  return _err
}

func main() {
  err := _main(tea.StringSlice(os.Args[1:]))
  if err != nil {
    panic(err)
  }
}
```

Node.js

```
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkcalendar_1_0, * as $dingtalkcalendar_1_0 from '@alicloud/dingtalk/calendar_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcalendar_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcalendar_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createEventHeaders = new $dingtalkcalendar_1_0.CreateEventHeaders({ });
    createEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let richTextDescription = new $dingtalkcalendar_1_0.CreateEventRequestRichTextDescription({
      text: "<div class=\"__aliyun_email_body_block\"><div  style=\"clear:both;\"><span  style=\"text-decoration:line-through;\">测试测试</span></div><div  style=\"clear:both;\"><span  style=\"color:#ff0000;\">热热热</span></div><div  style=\"clear:both;\"><span  style=\"text-decoration:underline;\">单独的</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;\">啊啊啊</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;font-style:italic;\">事实上</span></div></div>",
    });
    let uiConfigs0 = new $dingtalkcalendar_1_0.CreateEventRequestUiConfigs({
      uiName: "updateEventButton",
      uiStatus: "hide",
    });
    let extra = {
      noChatNotification: "true",
      noPushNotification: "true",
    };
    let onlineMeetingInfo = new $dingtalkcalendar_1_0.CreateEventRequestOnlineMeetingInfo({
      type: "dingtalk",
    });
    let reminders0 = new $dingtalkcalendar_1_0.CreateEventRequestReminders({
      method: "dingtalk",
      minutes: 15,
    });
    let location = new $dingtalkcalendar_1_0.CreateEventRequestLocation({
      displayName: "dingtalk",
    });
    let attendees0 = new $dingtalkcalendar_1_0.CreateEventRequestAttendees({
      id: "iiiP35sJxxx",
      isOptional: false,
    });
    let recurrenceRange = new $dingtalkcalendar_1_0.CreateEventRequestRecurrenceRange({
      type: "endDate",
      endDate: "2021-12-31T10:15:30+08:00",
      numberOfOccurrences: 5,
    });
    let recurrencePattern = new $dingtalkcalendar_1_0.CreateEventRequestRecurrencePattern({
      type: "daily",
      dayOfMonth: 1,
      daysOfWeek: "monday",
      index: "last",
      interval: 1,
      firstDayOfWeek: "monday",
    });
    let recurrence = new $dingtalkcalendar_1_0.CreateEventRequestRecurrence({
      pattern: recurrencePattern,
      range: recurrenceRange,
    });
    let end = new $dingtalkcalendar_1_0.CreateEventRequestEnd({
      date: "2020-09-21",
      dateTime: "2021-09-20T10:15:30+08:00",
      timeZone: "Asia/Shanghai",
    });
    let start = new $dingtalkcalendar_1_0.CreateEventRequestStart({
      date: "2021-09-20",
      dateTime: "2021-09-20T10:15:30+08:00",
      timeZone: "Asia/Shanghai",
    });
    let createEventRequest = new $dingtalkcalendar_1_0.CreateEventRequest({
      summary: "test event",
      description: "something about this event",
      start: start,
      end: end,
      isAllDay: false,
      recurrence: recurrence,
      attendees: [
        attendees0
      ],
      location: location,
      reminders: [
        reminders0
      ],
      onlineMeetingInfo: onlineMeetingInfo,
      extra: extra,
      uiConfigs: [
        uiConfigs0
      ],
      richTextDescription: richTextDescription,
    });
    try {
      await client.createEventWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "primary", createEventRequest, createEventHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

Client.main(process.argv.slice(2));
```

C#

```
// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

using Tea;
using Tea.Utils;

namespace AlibabaCloud.SDK.Sample
{
    public class Sample 
    {

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventHeaders createEventHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventHeaders();
            createEventHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRichTextDescription richTextDescription = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRichTextDescription
            {
                Text = "<div class=\"__aliyun_email_body_block\"><div  style=\"clear:both;\"><span  style=\"text-decoration:line-through;\">测试测试</span></div><div  style=\"clear:both;\"><span  style=\"color:#ff0000;\">热热热</span></div><div  style=\"clear:both;\"><span  style=\"text-decoration:underline;\">单独的</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;\">啊啊啊</span></div><div  style=\"clear:both;\"><span  style=\"font-weight:700;font-style:italic;\">事实上</span></div></div>",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestUiConfigs uiConfigs0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestUiConfigs
            {
                UiName = "updateEventButton",
                UiStatus = "hide",
            };
            Dictionary<string, string> extra = new Dictionary<string, string>
            {
                {"noChatNotification", “true”},
                {"noPushNotification", "true"},
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestOnlineMeetingInfo onlineMeetingInfo = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestOnlineMeetingInfo
            {
                Type = "dingtalk",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestReminders reminders0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestReminders
            {
                Method = "dingtalk",
                Minutes = 15,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestLocation location = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestLocation
            {
                DisplayName = "dingtalk",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestAttendees attendees0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestAttendees
            {
                Id = "iiiP35sJxxx",
                IsOptional = false,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRecurrence.CreateEventRequestRecurrenceRange recurrenceRange = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRecurrence.CreateEventRequestRecurrenceRange
            {
                Type = "endDate",
                EndDate = "2021-12-31T10:15:30+08:00",
                NumberOfOccurrences = 5,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRecurrence.CreateEventRequestRecurrencePattern recurrencePattern = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRecurrence.CreateEventRequestRecurrencePattern
            {
                Type = "daily",
                DayOfMonth = 1,
                DaysOfWeek = "monday",
                Index = "last",
                Interval = 1,
                FirstDayOfWeek = "monday",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRecurrence recurrence = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestRecurrence
            {
                Pattern = recurrencePattern,
                Range = recurrenceRange,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestEnd end = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestEnd
            {
                Date = "2020-09-21",
                DateTime = "2021-09-20T10:15:30+08:00",
                TimeZone = "Asia/Shanghai",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestStart start = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestStart
            {
                Date = "2021-09-20",
                DateTime = "2021-09-20T10:15:30+08:00",
                TimeZone = "Asia/Shanghai",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest createEventRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest
            {
                Summary = "test event",
                Description = "something about this event",
                Start = start,
                End = end,
                IsAllDay = false,
                Recurrence = recurrence,
                Attendees = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestAttendees>
                {
                    attendees0
                },
                Location = location,
                Reminders = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestReminders>
                {
                    reminders0
                },
                OnlineMeetingInfo = onlineMeetingInfo,
                Extra = extra,
                UiConfigs = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateEventRequest.CreateEventRequestUiConfigs>
                {
                    uiConfigs0
                },
                RichTextDescription = richTextDescription,
            };
            try
            {
                client.CreateEventWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "primary", createEventRequest, createEventHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
            }
            catch (TeaException err)
            {
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
            catch (Exception _err)
            {
                TeaException err = new TeaException(new Dictionary<string, object>
                {
                    { "message", _err.Message }
                });
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
        }

    }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| id | String | 日程ID。 |
| summary | String | 日程标题。 |
| description | String | 日程描述。 |
| start | Object | 日程开始时间。 |
| date | String | 日程开始日期，格式：yyyy-MM-dd。    - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 日程开始时间，格式为ISO-8601的date-time格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 日程开始时间所属时区，TZ database name格式    - 全天日程必须留空 - 非全天日程必须有值 |
| end | Object | 日程结束时间。 |
| date | String | 日程结束日期，格式：yyyy-MM-dd。    - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 日程结束时间，格式为ISO-8601的date-time格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| isAllDay | Boolean | 是否全天日程。   - **true**：是 - **false**：不是 |
| recurrence | Object | 日程循环规则。 |
| pattern | Object | 循环规则。 |
| type | String | 循环规则类型。   - **daily**：每**interval**天重复 - **weekly**：每**interval**周的第**daysOfWeek**天重复 - **absoluteMonthly**：每**interval**月的第**dayOfMonth**天重复 - **relativeMonthly**：每**interval**月的第**index**周的第**daysOfWeek**天重复 - **absoluteYearly**：每**interval**年重复 |
| dayOfMonth | Integer | 当循环规则的**type**值为**absoluteMonthly**时，用于指定是每个月的第几天。 |
| daysOfWeek | String | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| index | String | 当**type**值为**relativeMonthly**时，用于指定每月第几周。   - **first**：第一周 - **second**：第二周 - **third**：第三周 - **fourth**：第四周 - **last**：最后一周 |
| interval | Integer | 循环间隔，根据type不同单位不同。    例如：   - 当**type**取值为**daily**时表示间隔N天。 - 当**type**取值为**absoluteYearly**则表示间隔N年。 |
| firstDayOfWeek | String | 一周起始日，可取值包括：sunday、monday、tuesday、wednesday、thursday、friday、saturday。 默认值为“sunday”。 |
| range | Object | 循环范围。 |
| type | String | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| endDate | String | 循环结束时间。 |
| numberOfOccurrences | Integer | 循环次数。 |
| attendees | Array | 参与人列表。 |
| id | String | 用户的unionId。 |
| displayName | String | 用户姓名。 |
| responseStatus | String | 参会人状态。   - **needsAction**：未操作（默认状态） - **accepted**：已接受 - **declined**：已拒绝 - **tentative**：暂定接受 |
| self | Boolean | 是否当前操作用户。   - **true**：是 - **false**：不是 |
| isOptional | Boolean | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| organizer | Object | 日程组织者。 |
| id | String | 用户的unionId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否当前用户。   - **true**：是 - **false**：不是 |
| location | Object | 日程地点。 |
| displayName | String | 地点名称。 |
| reminders | Array | 日程提醒。 |
| method | String | 提醒方式。   - **dingtalk**：应用内提醒 - **sms**：短信提醒 - **phone**：电话提醒 |
| minutes | String | 提前多久提醒，单位分钟。 |
| createTime | String | 创建时间。 |
| updateTime | String | 更新时间。 |
| onlineMeetingInfo | Object | 线上会议信息。 |
| type | String | 线上会议类型。   - **dingtalk**：钉钉视频会议 |
| conferenceId | String | 会议id。 |
| url | String | 参会url。 |
| extraInfo | Map | 其他扩展信息。 |
| uiConfigs | Array | UI配置，控制日程详情页内组件的展示 |
| uiName | String | 组件名称，可取值（持续更新）：   - **updateEventButton**：编辑日程按钮 - **deleteEventButton**：删除日程按钮 - **transferEventButton**：转让日程按钮 - **attendee**：参与人区域 - **comment**：日程评论区域 |
| uiStatus | String | 组件状态，可取值：   - **hide**：隐藏 - **disable**: 禁用（新版详情页支持，低版本暂不支持disable，组件将被隐藏）    按钮类：无法点击。   区域类：无法交互。如将评论区域设置为disable，那么无法写评论，但是评论内容依然可见。 - **enable**：可使用（默认状态） |
| richTextDescription | Object | 富文本描述。 |
| text | String | 富文本描述内容。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "iiiP35sJadba8aBSgjrwPRKgiEiF",
  "summary" : "some event",
  "description" : "something about this event",
  "start" : {
    "date" : "2020-01-01",
    "dateTime" : "2020-01-01T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "end" : {
    "date" : "2020-01-01",
    "dateTime" : "2020-01-01T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "isAllDay" : false,
  "recurrence" : {
    "pattern" : {
      "type" : "daily",
      "dayOfMonth" : 14,
      "daysOfWeek" : "sunday",
      "index" : "first",
      "interval" : 1
    },
    "range" : {
      "type" : "noEnd",
      "endDate" : "2020-01-01T10:15:30+08:00",
      "numberOfOccurrences" : 5
    }
  },
  "attendees" : [ {
    "id" : "iiiP35sJadba8aBSgjrwPRKgiEiF",
    "displayName" : "jack",
    "responseStatus" : "accepted",
    "self" : false,
    "isOptional" : false
  } ],
  "organizer" : {
    "id" : "iiiP35sJadba8aBSgjrwPRKgiEiF",
    "displayName" : "tony",
    "responseStatus" : "accepted",
    "self" : false
  },
  "location" : {
    "displayName" : "room 1-2-3"
  },
  "reminders" : [ {
    "method" : "dingtalk",
    "minutes" : "15"
  } ],
  "createTime" : "2020-01-01T10:15:30+08:00",
  "updateTime" : "2020-01-01T10:15:30+08:00",
  "onlineMeetingInfo" : {
    "type" : "dingtalk",
    "conferenceId" : "123",
    "url" : "http://meeting"
  },
  "uiConfigs" : [ {
    "uiName" : "updateEventButton",
    "uiStatus" : "hide"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | CalendarId cannot be blank | 日历id不能为空 |
| 400 | invalidParameter | Event must be provided. | 日程不能为空 |
| 400 | invalidParameter | Event summary cannot be blank | 日程标题不能为空 |
| 400 | invalidParameter | Event start time not set. | 日程开始时间未设置 |
| 400 | invalidParameter | Event end time not set. | 日程结束时间未设置 |
| 400 | invalidParameter | Recurrence range numberOfOccurrences must between [1, 99] | numberOfOccurrences需满足区间[1,99] |
| 400 | invalidParameter | Recurrence interval must between [1, 365] | interval需满足区间[1,365] |
| 400 | permissionDeny | permissionDeny | 用户不在授权范围内 |
| 400 | idempotencyProcessing | Idempotency processing | 幂等请求处理中 |
| 400 | flowLimit | current user can not create events exceed 100 per day | 每个用户每天限制创建100个日程 |
| 404 | itemNotFound | forwardErrorMessage | 无法找到指定日程 |
