---
title: "获取会议室忙闲信息"
source_url: "https://open.dingtalk.com/document/development/queries-free-and-busy-meeting-room-information"
namespace: "development"
slug: "queries-free-and-busy-meeting-room-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 会议室 > 获取会议室忙闲信息"
doc_id: "sWfRW0nBBV"
updated_at: "2026-06-01 18:18:26"
---

> Source: https://open.dingtalk.com/document/development/queries-free-and-busy-meeting-room-information
> Path: 应用开发 / 服务端API / 日程 > 会议室 > 获取会议室忙闲信息
> Updated: 2026-06-01 18:18:26

# 获取会议室忙闲信息

调用本接口，获取指定会议室忙闲信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/meetingRooms/schedules/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Calendar.Event.Read-日历应用中日程读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 本次请求的资源所归属的用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| roomIds | Array of String | 是 | 待查询的会议室roomId列表，可调用[查询会议室列表](0437-check-the-meeting-room-list.md)接口获取，建议不超过5个。 |
| startTime | String | 是 | 查询开始时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| endTime | String | 是 | 查询结束时间，iso8601格式，例如：2022-07-29T14:55Z。 |

### 请求示例

HTTP

```
POST /v1.0/calendar/users/U5KPxxxxx/meetingRooms/schedules/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "roomIds" : [ "4002xxxxx" ],
  "startTime" : "2020-01-01T10:15:30+08:00",
  "endTime" : "2020-01-01T10:15:30+08:00"
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
        com.aliyun.dingtalkcalendar_1_0.models.GetMeetingRoomsScheduleHeaders getMeetingRoomsScheduleHeaders = new com.aliyun.dingtalkcalendar_1_0.models.GetMeetingRoomsScheduleHeaders();
        getMeetingRoomsScheduleHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.GetMeetingRoomsScheduleRequest getMeetingRoomsScheduleRequest = new com.aliyun.dingtalkcalendar_1_0.models.GetMeetingRoomsScheduleRequest()
                .setRoomIds(java.util.Arrays.asList(
                    "4002xxxxx"
                ))
                .setStartTime("2020-01-01T10:15:30+08:00")
                .setEndTime("2020-01-01T10:15:30+08:00");
        try {
            client.getMeetingRoomsScheduleWithOptions("U5KPxxxxx", getMeetingRoomsScheduleRequest, getMeetingRoomsScheduleHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_meeting_rooms_schedule_headers = dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleHeaders()
        get_meeting_rooms_schedule_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_meeting_rooms_schedule_request = dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleRequest(
            room_ids=[
                '4002xxxxx'
            ],
            start_time='2020-01-01T10:15:30+08:00',
            end_time='2020-01-01T10:15:30+08:00'
        )
        try:
            client.get_meeting_rooms_schedule_with_options('U5KPxxxxx', get_meeting_rooms_schedule_request, get_meeting_rooms_schedule_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_meeting_rooms_schedule_headers = dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleHeaders()
        get_meeting_rooms_schedule_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_meeting_rooms_schedule_request = dingtalkcalendar__1__0_models.GetMeetingRoomsScheduleRequest(
            room_ids=[
                '4002xxxxx'
            ],
            start_time='2020-01-01T10:15:30+08:00',
            end_time='2020-01-01T10:15:30+08:00'
        )
        try:
            await client.get_meeting_rooms_schedule_with_options_async('U5KPxxxxx', get_meeting_rooms_schedule_request, get_meeting_rooms_schedule_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetMeetingRoomsScheduleHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetMeetingRoomsScheduleRequest;
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
        $getMeetingRoomsScheduleHeaders = new GetMeetingRoomsScheduleHeaders([]);
        $getMeetingRoomsScheduleHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getMeetingRoomsScheduleRequest = new GetMeetingRoomsScheduleRequest([
            "roomIds" => [
                "4002xxxxx"
            ],
            "startTime" => "2020-01-01T10:15:30+08:00",
            "endTime" => "2020-01-01T10:15:30+08:00"
        ]);
        try {
            $client->getMeetingRoomsScheduleWithOptions("U5KPxxxxx", $getMeetingRoomsScheduleRequest, $getMeetingRoomsScheduleHeaders, new RuntimeOptions([]));
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

  getMeetingRoomsScheduleHeaders := &dingtalkcalendar_1_0.GetMeetingRoomsScheduleHeaders{}
  getMeetingRoomsScheduleHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getMeetingRoomsScheduleRequest := &dingtalkcalendar_1_0.GetMeetingRoomsScheduleRequest{
    RoomIds: []*string{tea.String("4002xxxxx")},
    StartTime: tea.String("2020-01-01T10:15:30+08:00"),
    EndTime: tea.String("2020-01-01T10:15:30+08:00"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetMeetingRoomsScheduleWithOptions(tea.String("U5KPxxxxx"), getMeetingRoomsScheduleRequest, getMeetingRoomsScheduleHeaders, &util.RuntimeOptions{})
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
    let getMeetingRoomsScheduleHeaders = new $dingtalkcalendar_1_0.GetMeetingRoomsScheduleHeaders({ });
    getMeetingRoomsScheduleHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getMeetingRoomsScheduleRequest = new $dingtalkcalendar_1_0.GetMeetingRoomsScheduleRequest({
      roomIds: [
        "4002xxxxx"
      ],
      startTime: "2020-01-01T10:15:30+08:00",
      endTime: "2020-01-01T10:15:30+08:00",
    });
    try {
      await client.getMeetingRoomsScheduleWithOptions("U5KPxxxxx", getMeetingRoomsScheduleRequest, getMeetingRoomsScheduleHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetMeetingRoomsScheduleHeaders getMeetingRoomsScheduleHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetMeetingRoomsScheduleHeaders();
            getMeetingRoomsScheduleHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetMeetingRoomsScheduleRequest getMeetingRoomsScheduleRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetMeetingRoomsScheduleRequest
            {
                RoomIds = new List<string>
                {
                    "4002xxxxx"
                },
                StartTime = "2020-01-01T10:15:30+08:00",
                EndTime = "2020-01-01T10:15:30+08:00",
            };
            try
            {
                client.GetMeetingRoomsScheduleWithOptions("U5KPxxxxx", getMeetingRoomsScheduleRequest, getMeetingRoomsScheduleHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| scheduleInformation | Array | 会议室的忙闲信息列表。 |
| roomId | String | 会议室roomId。 |
| error | String | 异常信息。 |
| scheduleItems | Array | 忙闲信息列表。  **[!NOTE]**    如果该字段返回为空，表示该会议室在指定时间段内是闲置状态。 |
| status | String | 忙闲状态。   - **BUSY**：繁忙 - **TENTATIVE**：审批中 |
| eventId | String | 日程id。 |
| organizer | Object | 日程组织者信息。 |
| id | String | 组织者unionId。 |
| start | Object | 日程开始时间相关信息。 |
| dateTime | String | 日程开始时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| timeZone | String | 时区名称，使用**IANA Time Zone Database**标准，例如：`Asia/Shanghai`。  **[!NOTE]**    全天日程时区固定为UTC，非全天日程时区默认为`Asia/Shanghai`。 |
| end | Object | 日程结束时间相关信息。 |
| dateTime | String | 日程结束时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| timeZone | String | 时区名称，使用**IANA Time Zone Database**标准，例如：`Asia/Shanghai`。  **[!NOTE]**    全天日程时区固定为UTC，非全天日程时区默认为`Asia/Shanghai`。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "scheduleInformation" : [ {
    "roomId" : "4002f89xxxxx",
    "error" : "无权限",
    "scheduleItems" : [ {
      "status" : "BUSY",
      "eventId" : "UzZvxxxxx",
      "organizer" : {
        "id" : "WWxlK8xxxxx"
      },
      "start" : {
        "dateTime" : "2020-01-01T10:15:30+08:00",
        "timeZone" : "Asia/Shanghai"
      },
      "end" : {
        "dateTime" : "2020-01-02T10:15:30+08:00",
        "timeZone" : "Asia/Shanghai"
      }
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | query ids cannot be empty | 查询id不能为空 |
| 400 | invalidParameter | Cannot get schedule information for more than limit. | 查询数目超出限制 |
| 400 | invalidParameter | Cannot query schedule for more than 90 days. | 查询天数超出限制 |
| 400 | invalidParameter | roomId invalid | roomId不合法 |
| 400 | meetingRoomNotAvailable | room busy | 会议室已被占用 |
