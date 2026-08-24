---
title: "查询单个日程详情"
source_url: "https://open.dingtalk.com/document/development/query-details-about-an-event"
namespace: "development"
slug: "query-details-about-an-event"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 日程 > 查询单个日程详情"
doc_id: "OV2eKcPPgz"
updated_at: "2026-06-02 09:25:00"
---

> Source: https://open.dingtalk.com/document/development/query-details-about-an-event
> Path: 应用开发 / 服务端API / 日程 > 日程 > 查询单个日程详情
> Updated: 2026-06-02 09:25:00

# 查询单个日程详情

调用本接口，根据日程id查询单个日程详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Event.Read-日历应用中日程读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 日程所属用户的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历Id，统一为primary，表示用户的主日历。 |
| eventId | String | 是 | 日程ID，可调用[查询日程列表](0254-query-an-event-list.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| maxAttendees | Long | 否 | 最大参与人数，默认值100，最大值500。 |

### 请求示例

HTTP

```
GET /v1.0/calendar/users/iiiP35sJaxxxxRKgiEiF/calendars/primary/events/cnNTbW1YbUxxxxvdlQrQT09?maxAttendees=100 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dd43888xxx
Content-Type:application/json
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
        com.aliyun.dingtalkcalendar_1_0.models.GetEventHeaders getEventHeaders = new com.aliyun.dingtalkcalendar_1_0.models.GetEventHeaders();
        getEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.GetEventRequest getEventRequest = new com.aliyun.dingtalkcalendar_1_0.models.GetEventRequest()
                .setMaxAttendees(100L);
        try {
            client.getEventWithOptions("iiiP35sJaxxxxRKgiEiF", "primary", "cnNTbW1YbUxxxxvdlQrQT09", getEventRequest, getEventHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_event_headers = dingtalkcalendar__1__0_models.GetEventHeaders()
        get_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_event_request = dingtalkcalendar__1__0_models.GetEventRequest(
            max_attendees=100
        )
        try:
            client.get_event_with_options('iiiP35sJaxxxxRKgiEiF', 'primary', 'cnNTbW1YbUxxxxvdlQrQT09', get_event_request, get_event_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_event_headers = dingtalkcalendar__1__0_models.GetEventHeaders()
        get_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_event_request = dingtalkcalendar__1__0_models.GetEventRequest(
            max_attendees=100
        )
        try:
            await client.get_event_with_options_async('iiiP35sJaxxxxRKgiEiF', 'primary', 'cnNTbW1YbUxxxxvdlQrQT09', get_event_request, get_event_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetEventHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetEventRequest;
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
        $getEventHeaders = new GetEventHeaders([]);
        $getEventHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getEventRequest = new GetEventRequest([
            "maxAttendees" => 100
        ]);
        try {
            $client->getEventWithOptions("iiiP35sJaxxxxRKgiEiF", "primary", "cnNTbW1YbUxxxxvdlQrQT09", $getEventRequest, $getEventHeaders, new RuntimeOptions([]));
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

  getEventHeaders := &dingtalkcalendar_1_0.GetEventHeaders{}
  getEventHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getEventRequest := &dingtalkcalendar_1_0.GetEventRequest{
    MaxAttendees: tea.Int64(100),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetEventWithOptions(tea.String("iiiP35sJaxxxxRKgiEiF"), tea.String("primary"), tea.String("cnNTbW1YbUxxxxvdlQrQT09"), getEventRequest, getEventHeaders, &util.RuntimeOptions{})
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
    let getEventHeaders = new $dingtalkcalendar_1_0.GetEventHeaders({ });
    getEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getEventRequest = new $dingtalkcalendar_1_0.GetEventRequest({
      maxAttendees: 100,
    });
    try {
      await client.getEventWithOptions("iiiP35sJaxxxxRKgiEiF", "primary", "cnNTbW1YbUxxxxvdlQrQT09", getEventRequest, getEventHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetEventHeaders getEventHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetEventHeaders();
            getEventHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetEventRequest getEventRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetEventRequest
            {
                MaxAttendees = 100,
            };
            try
            {
                client.GetEventWithOptions("iiiP35sJaxxxxRKgiEiF", "primary", "cnNTbW1YbUxxxxvdlQrQT09", getEventRequest, getEventHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

python2

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys

from alibabacloud_dingtalkcalendar_1_0.client import Client as dingtalkcalendar_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalkcalendar_1_0 import models as dingtalkcalendar__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client():
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
    def main(args):
        client = Sample.create_client()
        get_event_headers = dingtalkcalendar__1__0_models.GetEventHeaders()
        get_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_event_request = dingtalkcalendar__1__0_models.GetEventRequest(
            max_attendees=100
        )
        try:
            client.get_event_with_options('iiiP35sJaxxxxRKgiEiF', 'primary', 'cnNTbW1YbUxxxxvdlQrQT09', get_event_request, get_event_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

Swift

```
#!/usr/bin/env xcrun swift

import Cocoa
import Foundation
import Tea
import TeaUtils
import AlibabacloudDingtalkcalendar10
import AlibabacloudOpenApi

open class Client {
    public static func createClient() throws -> AlibabacloudDingtalkcalendar10.Client {
        var config: AlibabacloudOpenApi.Config = AlibabacloudOpenApi.Config([:])
        config.protocol_ = "https"
        config.regionId = "central"
        return AlibabacloudDingtalkcalendar10.Client(config)
    }

    @available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
    public static func main(_ args: [String]?) async throws -> Void {
        var client: AlibabacloudDingtalkcalendar10.Client = try Client.createClient()
        var getEventHeaders: AlibabacloudDingtalkcalendar10.GetEventHeaders = AlibabacloudDingtalkcalendar10.GetEventHeaders([:])
        getEventHeaders.xAcsDingtalkAccessToken = "<your access token>"
        var getEventRequest: AlibabacloudDingtalkcalendar10.GetEventRequest = AlibabacloudDingtalkcalendar10.GetEventRequest([
            "maxAttendees": 100
        ])
        do {
            try await client.getEventWithOptions("iiiP35sJaxxxxRKgiEiF", "primary", "cnNTbW1YbUxxxxvdlQrQT09", getEventRequest as! AlibabacloudDingtalkcalendar10.GetEventRequest, getEventHeaders as! AlibabacloudDingtalkcalendar10.GetEventHeaders, TeaUtils.RuntimeOptions([:]))
        }
        catch {
            if error is Tea.TeaError {
                var err = error as! Tea.TeaError
                if (!TeaUtils.Client.empty(err.code) && !TeaUtils.Client.empty(err.message)) {
                }
            } else {
                throw error
            }
        }
    }
}

Client.main(CommandLine.arguments)
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| id | String | 日程id。 |
| summary | String | 日程标题。 |
| description | String | 日程描述。 |
| status | String | 日程状态。   - **confirmed**：正常 - **cancelled**：已取消 |
| start | Object | 日程开始时间。 |
| date | String | 日程开始日期，格式：yyyy-MM-dd。    - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 日程开始时间，格式为ISO-8601的date-time格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 日程开始时间所属时区，TZ database name格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| originStart | Object | 表示循环序列中最初创建时的开始时间。    对于普通单个日程，不返回此属性。 |
| dateTime | String | 其日期和时间信息以 ISO 8601 格式表示，并且始终采用 UTC。 例如：`2023 年 1 月 1 日午夜 UTC 为 2023-01-01T00:00:00Z`。 |
| end | Object | 日程结束时间。 |
| date | String | 日程结束日期，格式：yyyy-MM-dd。    - 全天日程必须有值 - 非全天日程必须留空 |
| dateTime | String | 日程结束时间，格式为ISO-8601的date-time格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| timeZone | String | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。    - 全天日程必须留空 - 非全天日程必须有值 |
| isAllDay | Boolean | 是否为全天日程。   - **true**：是 - **false**：不是 |
| recurrence | Object | 日程循环规则。 |
| pattern | Object | 重复模式。 |
| type | String | 循环规则类型。   - **daily**：每`interval`天重复 - **weekly**：每`interval`周的第`daysOfWeek`天重复 - **absoluteMonthly**：每`interval`月的第`dayOfMonth`天重复 - **relativeMonthly**：每`interval`月的第`index`周的第`daysOfWeek`天重复 - **absoluteYearly**：每`interval`年重复 |
| dayOfMonth | Integer | 当`type=absoluteMonthly`时，用于指定是每个月的第几天。 |
| daysOfWeek | String | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| index | String | 当`type=relativeMonthly`时，用于指定每月第几周。   - **first** - **second** - **third** - **fourth** - **last**   其中`last`表示当月的最后一周。 |
| interval | Integer | 循环间隔，根据type不同单位不同。例如当`type=daily`时表示间隔N天，`type=absoluteYearly`则表示间隔N年。 |
| firstDayOfWeek | String | 一周起始日，可取值包括：sunday、monday、tuesday、wednesday、thursday、friday、saturday。 默认值为“sunday”。 |
| range | Object | 循环范围。 |
| type | String | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| endDate | String | 循环结束时间。 |
| numberOfOccurrences | Integer | 循环次数。 |
| attendees | Array | 参与人列表。 |
| id | String | 用户的unionId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否是当前登录用户。   - **true**：是 - **false**：不是 |
| isOptional | Boolean | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| organizer | Object | 组织者。 |
| id | String | 组织者unionId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否是当前登录用户。   - **true**：是 - **false**：不是 |
| location | Object | 日程地点相关信息。 |
| displayName | String | 日程地点名称。 |
| seriesMasterId | String | 重复日程的主日程id，非重复日程为空。 |
| createTime | String | 创建时间。 |
| updateTime | String | 更新时间。 |
| reminders | Array | 日程提醒 |
| method | String | 提醒方式。 |
| minutes | String | 在日程开始前N分钟发出提醒。 |
| onlineMeetingInfo | Object | 线上会议。 |
| type | String | 线上会议类型，目前支持：   - **dingtalk**：钉钉视频会议 |
| conferenceId | String | 会议ID。 |
| url | String | 参会的url地址。 |
| extraInfo | Map | 其他扩展信息。 |
| extendedProperties | Object | 日程拓展属性。 |
| sharedProperties | Object | 共享属性。 |
| sourceOpenCid | String | 当日程是由某个群内发起的时候，该字段表示日程发起的来源群。 |
| belongCorpId | String | 日程归属的企业corpId。 |
| meetingRooms | Array | 会议室。 |
| roomId | String | 会议室roomId。 |
| responseStatus | String | 会议室响应状态。   - **accepted** : 接受 - **tentative**: 审批中 - **declined** : 审批未通过 |
| displayName | String | 会议室名称。 |
| categories | Array | 日程类型。 |
| displayName | String | 日程类型名称。 |
| richTextDescription | Object | 富文本描述。 |
| text | String | 富文本描述内容。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "iiiP35sJxxxxPRKgiEiF",
  "summary" : "test event",
  "description" : "something about this event",
  "status" : "confirmed",
  "start" : {
    "date" : "2020-01-01",
    "dateTime" : "2020-01-01T10:15:30+08:00",
    "timeZone" : "Asia/Shanghai"
  },
  "originStart" : {
    "dateTime" : "2023-01-01T00:00:00Z"
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
      "daysOfWeek" : "monday",
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
    "id" : "iiiP35sJxxxxPRKgiEiF",
    "displayName" : "jack",
    "responseStatus" : "accepted",
    "self" : false,
    "isOptional" : false
  } ],
  "organizer" : {
    "id" : "iiiP35sJxxxxPRKgiEiF",
    "displayName" : "tony",
    "responseStatus" : "accepted",
    "self" : false
  },
  "location" : {
    "displayName" : "room 1-2-3",
    "meetingRooms" : [ "会议室" ]
  },
  "seriesMasterId" : "cnNTbW1YbxxxxvdlQrQT09",
  "createTime" : "2020-01-01T10:15:30+08:00",
  "updateTime" : "2020-01-01T10:15:30+08:00",
  "reminders" : [ {
    "method" : "dingtalk",
    "minutes" : "15"
  } ],
  "onlineMeetingInfo" : {
    "type" : "dingtalk",
    "conferenceId" : "5c4df21d-xxxx-a6db402b9f3a",
    "url" : "dingtalk://dingtalkclient/page/videoxxxxalendar?confId=5c4df21d-xxxx9f3f&calendarId=127xxxx124"
  },
  "extendedProperties" : {
    "sharedProperties" : {
      "sourceOpenCid" : "zxcvasdfvb123====",
      "belongCorpId" : "dingd*****1231231"
    }
  },
  "meetingRooms" : [ {
    "roomId" : "c10315a8b4e740a317813ab6fxxxxxx",
    "responseStatus" : "accepted",
    "displayName" : "1号会议室"
  } ],
  "categories" : [ {
    "displayName" : "单周会"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 404 | instanceNotExist | instance not exist | 循环日程实例不存在 |
| 404 | itemNotFound | forwardErrorMessage | 无法找到指定日程 |
