---
title: "修改日程"
source_url: "https://open.dingtalk.com/document/development/modify-event"
namespace: "development"
slug: "modify-event"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 日程 > 修改日程"
doc_id: "68Mxcrdh14"
updated_at: "2026-06-02 09:24:59"
---

> Source: https://open.dingtalk.com/document/development/modify-event
> Path: 应用开发 / 服务端API / 日程 > 日程 > 修改日程
> Updated: 2026-06-02 09:24:59

# 修改日程

调用本接口，修改单个日程信息。

## 接口调用说明

- 目前仅允许组织者修改日程，因此path中的userId字段必须是组织者的unionId。
- 请求中仅传需要修改的字段即可，未传的字段保持不变。
- 每次日程参与者操作最大支持500人，最大支持操作5000人的日程。
- 日程参与者的添加和删除：建议使用[添加日程参与者](0256-add-schedule-participant.md)和[删除日程参与者](0257-delete-schedule-participant.md)接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId} |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Event.Write-日历应用中日程写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-client-token | String | 否 | 幂等校验。       - 相同的`x-client-token`表示同一次请求。 - 过期失效，1天。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 日程组织者的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历ID，统一为primary，表示用户的主日历。 |
| eventId | String | 是 | 日程ID，可调用[查询日程列表](0254-query-an-event-list.md)接口获取id参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| summary | String | 否 | 日程标题。 |
| id | String | 是 | 日程ID。 |
| description | String | 否 | 日程描述。 |
| start | Object | 否 | 日程开始时间。 |
| date | String | 否 | 日程开始日期，格式：yyyy-MM-dd。     - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 否 | 日程开始时间，格式为ISO-8601的date-time格式。     - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 否 | 日程开始时间所属时区，TZ database name格式。     - 全天日程必须留空 - 非全天日程必须有值 |
| end | Object | 否 | 日程结束时间。    日程循环次数**numberOfOccurrences**和日程结束时间**end**不可同时设置。 |
| date | String | 否 | 日程结束日期，格式：yyyy-MM-dd。     - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 否 | 日程结束时间，格式为ISO-8601的date-time格式。     - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 否 | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。     - 全天日程必须留空 - 非全天日程必须有值 |
| isAllDay | Boolean | 否 | 是否全天日程。   - **true**：是 - **false**：不是 |
| recurrence | Object | 否 | 日程循环规则。 |
| pattern | Object | 否 | 循环规则。 |
| type | String | 否 | 循环规则类型。   - **daily**：每**interval**天重复 - **weekly**：每**interval**周的第**daysOfWeek**天重复 - **absoluteMonthly**：每**interval**月的第**dayOfMonth**天重复 - **relativeMonthly**：每**interval**月的第**index**周的第**daysOfWeek**天重复 - **absoluteYearly**：每**interval**年重复 |
| dayOfMonth | Integer | 否 | 当循环规则的**type**值为**absoluteMonthly**时，用于指定是每个月的第几天。 |
| daysOfWeek | String | 否 | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| index | String | 否 | 当type值为relativeMonthly时，用于指定每月第几周。   - **first**：第一周 - **second**：第二周 - **third**：第三周 - **fourth**：第四周 - **last**：最后一周 |
| interval | Integer | 否 | 循环间隔，根据type不同单位不同。      例如：   - 当**type**取值为**daily**时表示间隔N天。 - 当**type**取值为**absoluteYearly**则表示间隔N年。 |
| firstDayOfWeek | String | 否 | 一周起始日，可取值包括：sunday、monday、tuesday、wednesday、thursday、friday、saturday。 默认值为“sunday”。 |
| range | Object | 否 | 循环范围。 |
| type | String | 否 | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| endDate | String | 否 | 循环结束时间。      **endDate**和**numberOfOccurrences**不可同时设定。 |
| numberOfOccurrences | Integer | 否 | 循环次数。      **endDate**和**numberOfOccurrences**不可同时设定。 |
| attendees | Array | 否 | 日程参与人列表。 |
| id | String | 否 | 用户的unionId。 |
| email | String | 否 | 邮箱。 |
| isOptional | Boolean | 否 | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| location | Object | 否 | 日程地点。 |
| displayName | String | 否 | 日程地点的名称。 |
| extra | Map<String, String> | 否 | JSON格式的扩展能力开关，选填，具体属性定义如下。   - **noPushNotification**：创建日程时是否向关联人员发送钉钉推送通知。    - **true**：不发送   - **false**：发送 - **noChatNotification**：创建日程时是否向参与人发送单聊卡片。    - **true**：不发送   - **false**：发送 |
| reminders | Array | 否 | 日程提醒，可以添加多个。   - 如果不传默认提醒时间为：    - **非全天日程**：开始前15分钟提醒   - **全天日程**：开始前一天9点提醒 - 如果传空数据表示不创建任何提醒。 |
| method | String | 否 | 提醒方式。   - **dingtalk**: 钉钉内提醒 |
| minutes | Integer | 否 | 在日程开始前N分钟发出提醒。 |
| onlineMeetingInfo | Object | 否 | 视频会议。  在更新时传入此字段会新建视频会议，在已存在视频会议的情况下传入此字段会覆盖原有视频会议。 |
| type | String | 否 | 线上会议类型。   - **dingtalk**: 钉钉视频会议 |
| richTextDescription | Object | 否 | 富文本字段。 |
| text | String | 否 | 富文本值。 |
| uiConfigs | Array | 否 | UI配置，控制日程详情页内组件的展示。 |
| uiName | String | 是 | 组件名称，可取值（持续更新）：   - **updateEventButton**：编辑日程按钮 - **deleteEventButton**：删除日程按钮 - **transferEventButton**：转让日程按钮 - **attendee**：参与人区域 - **comment**：日程评论区域 |
| uiStatus | String | 是 | 组件状态，可取值：   - **hide**：隐藏 - **disable**: 禁用（新版详情页支持，低版本暂不支持disable，组件将被隐藏）    按钮类：无法点击。   区域类：无法交互。如将评论区域设置为disable，那么无法写评论，但是评论内容依然可见。 - **enable**：可使用（默认状态） |

### 请求示例

HTTP

```
PUT /v1.0/calendar/users/iiiP35sJaxxx/calendars/primary/events/cnNTbWxxx HTTP/1.1
Host:api.dingtalk.com
x-client-token:******
x-acs-dingtalk-access-token:dd438xxx
Content-Type:application/json

{
  "summary" : "some event",
  "id" : "cnNTbWxxx",
  "description" : "这是一个日程",
  "start" : {
    "date" : "2020-01-01",
    "dateTime" : "2020-01-01T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "end" : {
    "date" : "2020-01-02",
    "dateTime" : "2020-01-01T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "isAllDay" : false,
  "recurrence" : {
    "pattern" : {
      "type" : "daily",
      "dayOfMonth" : 1,
      "daysOfWeek" : "sunday",
      "index" : "last",
      "interval" : 1
    },
    "range" : {
      "type" : "endDate",
      "endDate" : "2021-12-31T10:15:30+08:00",
      "numberOfOccurrences" : 1
    }
  },
  "attendees" : [ {
    "id" : "iiiP35sJadba8aBSgjrwPRKgiEiF",
    "isOptional" : false
  } ],
  "location" : {
    "displayName" : "room 1-2-3"
  },
  "reminders" : [ {
    "method" : "dingtalk",
    "minutes" : 15
  } ],
  "onlineMeetingInfo" : {
    "type" : "dingtalk"
  },
  "richTextDescription" : { },
  "uiConfigs" : [ { } ]
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
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventHeaders patchEventHeaders = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventHeaders();
        patchEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestUiConfigs uiConfigs0 = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestUiConfigs();
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRichTextDescription richTextDescription = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRichTextDescription();
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestOnlineMeetingInfo onlineMeetingInfo = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestOnlineMeetingInfo()
                .setType("dingtalk");
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestReminders reminders0 = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestReminders()
                .setMethod("dingtalk")
                .setMinutes(15);
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestLocation location = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestLocation()
                .setDisplayName("room 1-2-3");
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestAttendees attendees0 = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestAttendees()
                .setId("iiiP35sJadba8aBSgjrwPRKgiEiF")
                .setIsOptional(false);
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRecurrenceRange recurrenceRange = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRecurrenceRange()
                .setType("endDate")
                .setEndDate("2021-12-31T10:15:30+08:00")
                .setNumberOfOccurrences(1);
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRecurrencePattern recurrencePattern = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRecurrencePattern()
                .setType("daily")
                .setDayOfMonth(1)
                .setDaysOfWeek("sunday")
                .setIndex("last")
                .setInterval(1);
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRecurrence recurrence = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestRecurrence()
                .setPattern(recurrencePattern)
                .setRange(recurrenceRange);
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestEnd end = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestEnd()
                .setDate("2020-01-02")
                .setDateTime("2020-01-01T10:15:30+08:00")
                .setTimeZone("Asia/Shanghai");
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestStart start = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest.PatchEventRequestStart()
                .setDate("2020-01-01")
                .setDateTime("2020-01-01T10:15:30+08:00")
                .setTimeZone("Asia/Shanghai");
        com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest patchEventRequest = new com.aliyun.dingtalkcalendar_1_0.models.PatchEventRequest()
                .setSummary("some event")
                .setId("cnNTbWxxx")
                .setDescription("这是一个日程")
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
                .setRichTextDescription(richTextDescription)
                .setUiConfigs(java.util.Arrays.asList(
                    uiConfigs0
                ));
        try {
            client.patchEventWithOptions("iiiP35sJaxxx", "primary", "cnNTbWxxx", patchEventRequest, patchEventHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        patch_event_headers = dingtalkcalendar__1__0_models.PatchEventHeaders()
        patch_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        ui_configs_0 = dingtalkcalendar__1__0_models.PatchEventRequestUiConfigs()
        rich_text_description = dingtalkcalendar__1__0_models.PatchEventRequestRichTextDescription()
        online_meeting_info = dingtalkcalendar__1__0_models.PatchEventRequestOnlineMeetingInfo(
            type='dingtalk'
        )
        reminders_0 = dingtalkcalendar__1__0_models.PatchEventRequestReminders(
            method='dingtalk',
            minutes=15
        )
        location = dingtalkcalendar__1__0_models.PatchEventRequestLocation(
            display_name='room 1-2-3'
        )
        attendees_0 = dingtalkcalendar__1__0_models.PatchEventRequestAttendees(
            id='iiiP35sJadba8aBSgjrwPRKgiEiF',
            is_optional=False
        )
        recurrence_range = dingtalkcalendar__1__0_models.PatchEventRequestRecurrenceRange(
            type='endDate',
            end_date='2021-12-31T10:15:30+08:00',
            number_of_occurrences=1
        )
        recurrence_pattern = dingtalkcalendar__1__0_models.PatchEventRequestRecurrencePattern(
            type='daily',
            day_of_month=1,
            days_of_week='sunday',
            index='last',
            interval=1
        )
        recurrence = dingtalkcalendar__1__0_models.PatchEventRequestRecurrence(
            pattern=recurrence_pattern,
            range=recurrence_range
        )
        end = dingtalkcalendar__1__0_models.PatchEventRequestEnd(
            date='2020-01-02',
            date_time='2020-01-01T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        start = dingtalkcalendar__1__0_models.PatchEventRequestStart(
            date='2020-01-01',
            date_time='2020-01-01T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        patch_event_request = dingtalkcalendar__1__0_models.PatchEventRequest(
            summary='some event',
            id='cnNTbWxxx',
            description='这是一个日程',
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
            rich_text_description=rich_text_description,
            ui_configs=[
                ui_configs_0
            ]
        )
        try:
            client.patch_event_with_options('iiiP35sJaxxx', 'primary', 'cnNTbWxxx', patch_event_request, patch_event_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        patch_event_headers = dingtalkcalendar__1__0_models.PatchEventHeaders()
        patch_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        ui_configs_0 = dingtalkcalendar__1__0_models.PatchEventRequestUiConfigs()
        rich_text_description = dingtalkcalendar__1__0_models.PatchEventRequestRichTextDescription()
        online_meeting_info = dingtalkcalendar__1__0_models.PatchEventRequestOnlineMeetingInfo(
            type='dingtalk'
        )
        reminders_0 = dingtalkcalendar__1__0_models.PatchEventRequestReminders(
            method='dingtalk',
            minutes=15
        )
        location = dingtalkcalendar__1__0_models.PatchEventRequestLocation(
            display_name='room 1-2-3'
        )
        attendees_0 = dingtalkcalendar__1__0_models.PatchEventRequestAttendees(
            id='iiiP35sJadba8aBSgjrwPRKgiEiF',
            is_optional=False
        )
        recurrence_range = dingtalkcalendar__1__0_models.PatchEventRequestRecurrenceRange(
            type='endDate',
            end_date='2021-12-31T10:15:30+08:00',
            number_of_occurrences=1
        )
        recurrence_pattern = dingtalkcalendar__1__0_models.PatchEventRequestRecurrencePattern(
            type='daily',
            day_of_month=1,
            days_of_week='sunday',
            index='last',
            interval=1
        )
        recurrence = dingtalkcalendar__1__0_models.PatchEventRequestRecurrence(
            pattern=recurrence_pattern,
            range=recurrence_range
        )
        end = dingtalkcalendar__1__0_models.PatchEventRequestEnd(
            date='2020-01-02',
            date_time='2020-01-01T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        start = dingtalkcalendar__1__0_models.PatchEventRequestStart(
            date='2020-01-01',
            date_time='2020-01-01T10:15:30+08:00',
            time_zone='Asia/Shanghai'
        )
        patch_event_request = dingtalkcalendar__1__0_models.PatchEventRequest(
            summary='some event',
            id='cnNTbWxxx',
            description='这是一个日程',
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
            rich_text_description=rich_text_description,
            ui_configs=[
                ui_configs_0
            ]
        )
        try:
            await client.patch_event_with_options_async('iiiP35sJaxxx', 'primary', 'cnNTbWxxx', patch_event_request, patch_event_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\uiConfigs;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\richTextDescription;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\onlineMeetingInfo;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\reminders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\location;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\attendees;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\recurrence\range;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\recurrence\pattern;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\recurrence;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\end;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest\start;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\PatchEventRequest;
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
        $patchEventHeaders = new PatchEventHeaders([]);
        $patchEventHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $uiConfigs0 = new uiConfigs([]);
        $richTextDescription = new richTextDescription([]);
        $onlineMeetingInfo = new onlineMeetingInfo([
            "type" => "dingtalk"
        ]);
        $reminders0 = new reminders([
            "method" => "dingtalk",
            "minutes" => 15
        ]);
        $location = new location([
            "displayName" => "room 1-2-3"
        ]);
        $attendees0 = new attendees([
            "id" => "iiiP35sJadba8aBSgjrwPRKgiEiF",
            "isOptional" => false
        ]);
        $recurrenceRange = new range([
            "type" => "endDate",
            "endDate" => "2021-12-31T10:15:30+08:00",
            "numberOfOccurrences" => 1
        ]);
        $recurrencePattern = new pattern([
            "type" => "daily",
            "dayOfMonth" => 1,
            "daysOfWeek" => "sunday",
            "index" => "last",
            "interval" => 1
        ]);
        $recurrence = new recurrence([
            "pattern" => $recurrencePattern,
            "range" => $recurrenceRange
        ]);
        $end = new end([
            "date" => "2020-01-02",
            "dateTime" => "2020-01-01T10:15:30+08:00",
            "timeZone" => "Asia/Shanghai"
        ]);
        $start = new start([
            "date" => "2020-01-01",
            "dateTime" => "2020-01-01T10:15:30+08:00",
            "timeZone" => "Asia/Shanghai"
        ]);
        $patchEventRequest = new PatchEventRequest([
            "summary" => "some event",
            "id" => "cnNTbWxxx",
            "description" => "这是一个日程",
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
            "richTextDescription" => $richTextDescription,
            "uiConfigs" => [
                $uiConfigs0
            ]
        ]);
        try {
            $client->patchEventWithOptions("iiiP35sJaxxx", "primary", "cnNTbWxxx", $patchEventRequest, $patchEventHeaders, new RuntimeOptions([]));
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

  patchEventHeaders := &dingtalkcalendar_1_0.PatchEventHeaders{}
  patchEventHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  uiConfigs0 := &dingtalkcalendar_1_0.PatchEventRequestUiConfigs{}
  richTextDescription := &dingtalkcalendar_1_0.PatchEventRequestRichTextDescription{}
  onlineMeetingInfo := &dingtalkcalendar_1_0.PatchEventRequestOnlineMeetingInfo{
    Type: tea.String("dingtalk"),
  }
  reminders0 := &dingtalkcalendar_1_0.PatchEventRequestReminders{
    Method: tea.String("dingtalk"),
    Minutes: tea.Int32(15),
  }
  location := &dingtalkcalendar_1_0.PatchEventRequestLocation{
    DisplayName: tea.String("room 1-2-3"),
  }
  attendees0 := &dingtalkcalendar_1_0.PatchEventRequestAttendees{
    Id: tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF"),
    IsOptional: tea.Bool(false),
  }
  recurrenceRange := &dingtalkcalendar_1_0.PatchEventRequestRecurrenceRange{
    Type: tea.String("endDate"),
    EndDate: tea.String("2021-12-31T10:15:30+08:00"),
    NumberOfOccurrences: tea.Int32(1),
  }
  recurrencePattern := &dingtalkcalendar_1_0.PatchEventRequestRecurrencePattern{
    Type: tea.String("daily"),
    DayOfMonth: tea.Int32(1),
    DaysOfWeek: tea.String("sunday"),
    Index: tea.String("last"),
    Interval: tea.Int32(1),
  }
  recurrence := &dingtalkcalendar_1_0.PatchEventRequestRecurrence{
    Pattern: recurrencePattern,
    Range: recurrenceRange,
  }
  end := &dingtalkcalendar_1_0.PatchEventRequestEnd{
    Date: tea.String("2020-01-02"),
    DateTime: tea.String("2020-01-01T10:15:30+08:00"),
    TimeZone: tea.String("Asia/Shanghai"),
  }
  start := &dingtalkcalendar_1_0.PatchEventRequestStart{
    Date: tea.String("2020-01-01"),
    DateTime: tea.String("2020-01-01T10:15:30+08:00"),
    TimeZone: tea.String("Asia/Shanghai"),
  }
  patchEventRequest := &dingtalkcalendar_1_0.PatchEventRequest{
    Summary: tea.String("some event"),
    Id: tea.String("cnNTbWxxx"),
    Description: tea.String("这是一个日程"),
    Start: start,
    End: end,
    IsAllDay: tea.Bool(false),
    Recurrence: recurrence,
    Attendees: []*dingtalkcalendar_1_0.PatchEventRequestAttendees{attendees0},
    Location: location,
    Reminders: []*dingtalkcalendar_1_0.PatchEventRequestReminders{reminders0},
    OnlineMeetingInfo: onlineMeetingInfo,
    RichTextDescription: richTextDescription,
    UiConfigs: []*dingtalkcalendar_1_0.PatchEventRequestUiConfigs{uiConfigs0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PatchEventWithOptions(tea.String("iiiP35sJaxxx"), tea.String("primary"), tea.String("cnNTbWxxx"), patchEventRequest, patchEventHeaders, &util.RuntimeOptions{})
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
    let patchEventHeaders = new $dingtalkcalendar_1_0.PatchEventHeaders({ });
    patchEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let uiConfigs0 = new $dingtalkcalendar_1_0.PatchEventRequestUiConfigs({ });
    let richTextDescription = new $dingtalkcalendar_1_0.PatchEventRequestRichTextDescription({ });
    let onlineMeetingInfo = new $dingtalkcalendar_1_0.PatchEventRequestOnlineMeetingInfo({
      type: "dingtalk",
    });
    let reminders0 = new $dingtalkcalendar_1_0.PatchEventRequestReminders({
      method: "dingtalk",
      minutes: 15,
    });
    let location = new $dingtalkcalendar_1_0.PatchEventRequestLocation({
      displayName: "room 1-2-3",
    });
    let attendees0 = new $dingtalkcalendar_1_0.PatchEventRequestAttendees({
      id: "iiiP35sJadba8aBSgjrwPRKgiEiF",
      isOptional: false,
    });
    let recurrenceRange = new $dingtalkcalendar_1_0.PatchEventRequestRecurrenceRange({
      type: "endDate",
      endDate: "2021-12-31T10:15:30+08:00",
      numberOfOccurrences: 1,
    });
    let recurrencePattern = new $dingtalkcalendar_1_0.PatchEventRequestRecurrencePattern({
      type: "daily",
      dayOfMonth: 1,
      daysOfWeek: "sunday",
      index: "last",
      interval: 1,
    });
    let recurrence = new $dingtalkcalendar_1_0.PatchEventRequestRecurrence({
      pattern: recurrencePattern,
      range: recurrenceRange,
    });
    let end = new $dingtalkcalendar_1_0.PatchEventRequestEnd({
      date: "2020-01-02",
      dateTime: "2020-01-01T10:15:30+08:00",
      timeZone: "Asia/Shanghai",
    });
    let start = new $dingtalkcalendar_1_0.PatchEventRequestStart({
      date: "2020-01-01",
      dateTime: "2020-01-01T10:15:30+08:00",
      timeZone: "Asia/Shanghai",
    });
    let patchEventRequest = new $dingtalkcalendar_1_0.PatchEventRequest({
      summary: "some event",
      id: "cnNTbWxxx",
      description: "这是一个日程",
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
      richTextDescription: richTextDescription,
      uiConfigs: [
        uiConfigs0
      ],
    });
    try {
      await client.patchEventWithOptions("iiiP35sJaxxx", "primary", "cnNTbWxxx", patchEventRequest, patchEventHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventHeaders patchEventHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventHeaders();
            patchEventHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestUiConfigs uiConfigs0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestUiConfigs();
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRichTextDescription richTextDescription = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRichTextDescription();
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestOnlineMeetingInfo onlineMeetingInfo = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestOnlineMeetingInfo
            {
                Type = "dingtalk",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestReminders reminders0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestReminders
            {
                Method = "dingtalk",
                Minutes = 15,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestLocation location = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestLocation
            {
                DisplayName = "room 1-2-3",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestAttendees attendees0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestAttendees
            {
                Id = "iiiP35sJadba8aBSgjrwPRKgiEiF",
                IsOptional = false,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRecurrence.PatchEventRequestRecurrenceRange recurrenceRange = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRecurrence.PatchEventRequestRecurrenceRange
            {
                Type = "endDate",
                EndDate = "2021-12-31T10:15:30+08:00",
                NumberOfOccurrences = 1,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRecurrence.PatchEventRequestRecurrencePattern recurrencePattern = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRecurrence.PatchEventRequestRecurrencePattern
            {
                Type = "daily",
                DayOfMonth = 1,
                DaysOfWeek = "sunday",
                Index = "last",
                Interval = 1,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRecurrence recurrence = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestRecurrence
            {
                Pattern = recurrencePattern,
                Range = recurrenceRange,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestEnd end = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestEnd
            {
                Date = "2020-01-02",
                DateTime = "2020-01-01T10:15:30+08:00",
                TimeZone = "Asia/Shanghai",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestStart start = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestStart
            {
                Date = "2020-01-01",
                DateTime = "2020-01-01T10:15:30+08:00",
                TimeZone = "Asia/Shanghai",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest patchEventRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest
            {
                Summary = "some event",
                Id = "cnNTbWxxx",
                Description = "这是一个日程",
                Start = start,
                End = end,
                IsAllDay = false,
                Recurrence = recurrence,
                Attendees = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestAttendees>
                {
                    attendees0
                },
                Location = location,
                Reminders = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestReminders>
                {
                    reminders0
                },
                OnlineMeetingInfo = onlineMeetingInfo,
                RichTextDescription = richTextDescription,
                UiConfigs = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.PatchEventRequest.PatchEventRequestUiConfigs>
                {
                    uiConfigs0
                },
            };
            try
            {
                client.PatchEventWithOptions("iiiP35sJaxxx", "primary", "cnNTbWxxx", patchEventRequest, patchEventHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 日程id。 |
| summary | String | 日程标题。 |
| description | String | 日程描述。 |
| start | Object | 日程开始时间。 |
| date | String | 日程开始日期，格式：yyyy-MM-dd。       - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 日程开始时间，格式为ISO-8601的date-time格式。       - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 日程开始时间所属时区，TZ database name格式。       - 全天日程必须留空 - 非全天日程必须有值 |
| end | Object | 日程结束时间。 |
| date | String | 日程结束日期，格式：yyyy-MM-dd。       - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 日程结束时间，格式为ISO-8601的date-time格式。       - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。       - 全天日程必须留空 - 非全天日程必须有值 |
| isAllDay | Boolean | 是否全天日程。   - **true**：是 - **false**：不是 |
| recurrence | Object | 日程循环规则。 |
| pattern | Object | 循环规则。 |
| type | String | 循环规则类型。   - **daily**：每**interval**天重复 - **weekly**：每**interval**周的第**daysOfWeek**天重复 - **absoluteMonthly**：每**interval**月的第**dayOfMonth**天重复 - **relativeMonthly**：每**interval**月的第**index**周的第**daysOfWeek**天重复 - **absoluteYearly**：每**interval**年重复 |
| dayOfMonth | Integer | 当循环规则的**type**值为**absoluteMonthly**时，用于指定是每个月的第几天。 |
| daysOfWeek | String | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| index | String | 当type值为relativeMonthly时，用于指定每月第几周。   - **first**：第一周 - **second**：第二周 - **third**：第三周 - **fourth**：第四周 - **last**：最后一周 |
| interval | Integer | 循环间隔，根据type不同单位不同。      例如：   - 当**type**取值为**daily**时表示间隔N天。 - 当**type**取值为**absoluteYearly**则表示间隔N年。 |
| firstDayOfWeek | String | 一周起始日，可取值包括：sunday、monday、tuesday、wednesday、thursday、friday、saturday。 默认值为“sunday”。 |
| range | Object | 循环范围。 |
| type | String | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| endDate | String | 循环结束时间。 |
| numberOfOccurrences | Integer | 循环次数。 |
| attendees | Array | 日程参与人列表。 |
| id | String | 用户unionId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否是当前登录用户。   - **true**：是 - **false**：不是 |
| isOptional | Boolean | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| organizer | Object | 日程组织者。 |
| id | String | 用户uninonId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否是当前登录用户。   - **true**：是 - **false**：不是 |
| location | Object | 日程地点信息。 |
| displayName | String | 日程地点展示名称。 |
| meetingRooms | Array of String | 会议室信息。 |
| reminders | Array | 日程提醒。 |
| method | String | 提醒方式。 |
| minutes | String | 在日程开始前N分钟发出提醒。 |
| createTime | String | 创建时间。 |
| updateTime | String | 更新时间。 |
| onlineMeetingInfo | Object | 线上会议信息。 |
| type | String | 线上会议类型。   - **dingtalk**：钉钉视频会议 |
| conferenceId | String | 会议id。 |
| url | String | 参会url。 |
| richTextDescription | Object | 富文本字段。 |
| text | String | 富文本值。 |
| uiConfigs | Array | UI配置，控制日程详情页内组件的展示。 |
| uiName | String | 组件名称，可取值（持续更新）：   - **updateEventButton**：编辑日程按钮 - **deleteEventButton**：删除日程按钮 - **transferEventButton**：转让日程按钮 - **attendee**：参与人区域 - **comment**：日程评论区域 |
| uiStatus | String | 组件状态，可取值：   - **hide**：隐藏 - **disable**: 禁用（新版详情页支持，低版本暂不支持disable，组件将被隐藏）      按钮类：无法点击。   区域类：无法交互。如将评论区域设置为disable，那么无法写评论，但是评论内容依然可见。 - **enable**：可使用（默认状态） |

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
  "updateTime" : "2020-01-01T10:15:30+08:00"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | CalendarId cannot be blank | 日历id不能为空 |
| 400 | invalidParameter | Event must be provided. | 日程不能为空 |
| 400 | invalidParameter | Event id summary cannot be blank | 日程id不能为空 |
| 400 | invalidParameter | Recurrence range numberOfOccurrences must between [1, 99] | numberOfOccurrences需满足区间[1,99] |
| 400 | invalidParameter | Recurrence interval must between [1, 365] | interval需满足区间[1,365] |
| 400 | invalidParameter | Meeting room invalid | 会议室不可用 |
| 400 | idempotencyProcessing | Idempotency processing | 幂等请求处理中 |
| 404 | itemNotFound | forwardErrorMessage | 无法找到指定日程 |
