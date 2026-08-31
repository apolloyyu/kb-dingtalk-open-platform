---
title: "查询日程列表"
source_url: "https://open.dingtalk.com/document/development/query-an-event-list"
namespace: "development"
slug: "query-an-event-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 日程 > 查询日程列表"
doc_id: "6CtAUmz22W"
updated_at: "2026-06-02 09:25:01"
---

> Source: https://open.dingtalk.com/document/development/query-an-event-list
> Path: 应用开发 / 服务端 API / 日程 > 日程 > 查询日程列表
> Updated: 2026-06-02 09:25:01

# 查询日程列表

调用本接口，查询某用户在某段时间内的日程列表，可以获取到日程标题、日程的开始日期、开始时间、结束日期、结束时间等信息。

## 接口调用说明

- 对于循环日程，会返回所有过去的循环日程实例，但是未来的不会返回，例如有一个从1.1号开始的每日循环日程，查询时已经是1.4号，那么会返回1.1～1.4号的循环日程实例，但是不会返回1.4号之后的 。
- 可以根据返回的日程对象recurrenceId是不是为空，来判断该日程是否为一个循环日程的实例。
- 默认不会返回已删除的日程，如果需要返回可以设置`showDeleted=true`，当返回的是已删除的日程时，此时调用[查询单个日程详情](0253-query-details-about-an-event.md)接口会返回**instanceNotExist**的错误。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events |
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
| userId | String | 是 | 查询目标用户的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历id，统一为primary，表示用户的主日历。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| timeMin | String | 否 | 日程开始时间的最小值，格式为ISO-8601的date-time格式，可不填。      `timeMin`和 `timeMax`最大差值为一年。 |
| timeMax | String | 否 | 日程开始时间的最大值，格式为ISO-8601的date-time格式，可不填。      `timeMin`和 `timeMax`最大差值为一年。 |
| showDeleted | Boolean | 否 | 是否返回已删除的日程：   - **true**：返回 - **false**（默认）：不返回 |
| maxResults | Integer | 否 | 最大返回记录数，最大值100，默认值100。 |
| maxAttendees | Integer | 否 | 每个日程的参与者查询个数，默认100，最大100。 如果参会人数超过100人，需要拉取全部参会人请使用[获取日程参与者](0259-get-the-participants-of-a-schedule.md)接口获取。 |
| nextToken | String | 否 | 分页游标。      如果一个查询条件一次无法全部返回结果，会返回分页token，下次查询带上该token后会返回后续数据，直到分页token为null表示数据已经全部查询完毕。 |
| syncToken | String | 否 | 同步token，用于增量数据同步场景，一个查询条件已经返回全部数据后（如果数据比较多会分页返回，调用方需要连续使用nextToken查询，直到所有分页都查完nextToken返回null之后），会返回一个syncToken，下次带着该token来查询会返回两次查询之间发生变更的增量数据。      如果传入了timeMax，则不会返回syncToken。 |
| seriesMasterId | String | 否 | 重复日程的主日程id，非重复日程为空。 |

### 请求示例

HTTP

```
GET /v1.0/calendar/users/iiiP35sJadxxxxPRKgiEiF/calendars/primary/events?timeMin=2022-11-27T00%3A00%3A00%2B08%3A00&timeMax=2022-11-30T00%3A00%3A00%2B08%3A00&showDeleted=false&maxResults=15&maxAttendees=10&nextToken=cnNTbW1xxxxEgvdlQrQT09&syncToken=cnNTbW1YbxxxxdEgvdlQrQT09 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dd43888e269xxxxa556389b064
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
        com.aliyun.dingtalkcalendar_1_0.models.ListEventsHeaders listEventsHeaders = new com.aliyun.dingtalkcalendar_1_0.models.ListEventsHeaders();
        listEventsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.ListEventsRequest listEventsRequest = new com.aliyun.dingtalkcalendar_1_0.models.ListEventsRequest()
                .setTimeMin("2022-11-27T00:00:00+08:00")
                .setTimeMax("2022-11-28T00:00:00+08:00")
                .setShowDeleted(false)
                .setMaxResults(15)
                .setMaxAttendees(10)
                .setNextToken("cnNTbW1xxxxEgvdlQrQT09")
                .setSyncToken("cnNTbW1YbxxxxdEgvdlQrQT09");
        try {
            client.listEventsWithOptions("iiiP35sJadxxxxPRKgiEiF", "primary", listEventsRequest, listEventsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_events_headers = dingtalkcalendar__1__0_models.ListEventsHeaders()
        list_events_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_events_request = dingtalkcalendar__1__0_models.ListEventsRequest(
            time_min='2022-11-27T00:00:00+08:00',
            time_max='2022-11-28T00:00:00+08:00',
            show_deleted=False,
            max_results=15,
            max_attendees=10,
            next_token='cnNTbW1xxxxEgvdlQrQT09',
            sync_token='cnNTbW1YbxxxxdEgvdlQrQT09'
        )
        try:
            client.list_events_with_options('iiiP35sJadxxxxPRKgiEiF', 'primary', list_events_request, list_events_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_events_headers = dingtalkcalendar__1__0_models.ListEventsHeaders()
        list_events_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_events_request = dingtalkcalendar__1__0_models.ListEventsRequest(
            time_min='2022-11-27T00:00:00+08:00',
            time_max='2022-11-28T00:00:00+08:00',
            show_deleted=False,
            max_results=15,
            max_attendees=10,
            next_token='cnNTbW1xxxxEgvdlQrQT09',
            sync_token='cnNTbW1YbxxxxdEgvdlQrQT09'
        )
        try:
            await client.list_events_with_options_async('iiiP35sJadxxxxPRKgiEiF', 'primary', list_events_request, list_events_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\ListEventsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\ListEventsRequest;
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
        $listEventsHeaders = new ListEventsHeaders([]);
        $listEventsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listEventsRequest = new ListEventsRequest([
            "timeMin" => "2022-11-27T00:00:00+08:00",
            "timeMax" => "2022-11-28T00:00:00+08:00",
            "showDeleted" => false,
            "maxResults" => 15,
            "maxAttendees" => 10,
            "nextToken" => "cnNTbW1xxxxEgvdlQrQT09",
            "syncToken" => "cnNTbW1YbxxxxdEgvdlQrQT09"
        ]);
        try {
            $client->listEventsWithOptions("iiiP35sJadxxxxPRKgiEiF", "primary", $listEventsRequest, $listEventsHeaders, new RuntimeOptions([]));
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

  listEventsHeaders := &dingtalkcalendar_1_0.ListEventsHeaders{}
  listEventsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listEventsRequest := &dingtalkcalendar_1_0.ListEventsRequest{
    TimeMin: tea.String("2022-11-27T00:00:00+08:00"),
    TimeMax: tea.String("2022-11-28T00:00:00+08:00"),
    ShowDeleted: tea.Bool(false),
    MaxResults: tea.Int32(15),
    MaxAttendees: tea.Int32(10),
    NextToken: tea.String("cnNTbW1xxxxEgvdlQrQT09"),
    SyncToken: tea.String("cnNTbW1YbxxxxdEgvdlQrQT09"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListEventsWithOptions(tea.String("iiiP35sJadxxxxPRKgiEiF"), tea.String("primary"), listEventsRequest, listEventsHeaders, &util.RuntimeOptions{})
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
    let listEventsHeaders = new $dingtalkcalendar_1_0.ListEventsHeaders({ });
    listEventsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listEventsRequest = new $dingtalkcalendar_1_0.ListEventsRequest({
      timeMin: "2022-11-27T00:00:00+08:00",
      timeMax: "2022-11-28T00:00:00+08:00",
      showDeleted: false,
      maxResults: 15,
      maxAttendees: 10,
      nextToken: "cnNTbW1xxxxEgvdlQrQT09",
      syncToken: "cnNTbW1YbxxxxdEgvdlQrQT09",
    });
    try {
      await client.listEventsWithOptions("iiiP35sJadxxxxPRKgiEiF", "primary", listEventsRequest, listEventsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.ListEventsHeaders listEventsHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.ListEventsHeaders();
            listEventsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.ListEventsRequest listEventsRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.ListEventsRequest
            {
                TimeMin = "2022-11-27T00:00:00+08:00",
                TimeMax = "2022-11-28T00:00:00+08:00",
                ShowDeleted = false,
                MaxResults = 15,
                MaxAttendees = 10,
                NextToken = "cnNTbW1xxxxEgvdlQrQT09",
                SyncToken = "cnNTbW1YbxxxxdEgvdlQrQT09",
            };
            try
            {
                client.ListEventsWithOptions("iiiP35sJadxxxxPRKgiEiF", "primary", listEventsRequest, listEventsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | String | 翻页token。 |
| events | Array | 日程。 |
| id | String | 日程id。 |
| summary | String | 日程标题。 |
| description | String | 日程描述。 |
| start | Object | 日程开始时间。 |
| date | String | 日程开始日期，格式：yyyy-MM-dd。 |
| dateTime | String | 日程开始时间，格式为ISO-8601的date-time格式。 |
| timeZone | String | 日程开始时间所属时区，tz database name格式，参考：https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones |
| originStart | Object | 表示循环序列中最初创建时的开始时间。      对于普通单个日程，不返回此属性。 |
| dateTime | String | 其日期和时间信息以ISO 8601格式表示，并且始终采用 UTC。例如：`2023年1月1日午夜 UTC 为 2023-01-01T00:00:00Z`。 |
| end | Object | 日程结束时间。 |
| date | String | 日程结束日期，格式：yyyy-MM-dd。 |
| dateTime | String | 日程结束时间，格式为ISO-8601的date-time格式。 |
| timeZone | String | 日程结束时间所属时区，必须和开始时间所属时区相同，tz database name格式，参考：https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones |
| isAllDay | Boolean | 是否为全天日程。   - **true**：是 - **false**：不是 |
| recurrence | Object | 日程循环规则。 |
| pattern | Object | 循环模式。 |
| type | String | 循环规则类型。   - **daily**：每`interval`天重复 - **weekly**：每`interval`周的第`daysOfWeek`天重复 - **absoluteMonthly**：每`interval`月的第`dayOfMonth`天重复 - **relativeMonthly**：每`interval`月的第`index`周的第`daysOfWeek`天重复 - **absoluteYearly**：每`interval`年重复 |
| dayOfMonth | Integer | 当`type=absoluteMonthly`时，用于指定是每个月的第几天。 |
| daysOfWeek | String | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| index | String | 当`type=relativeMonthly`时，用于指定每月第几周。   - **first** - **second** - **third** - **fourth** - **last**   其中`last`表示当月的最后一周。 |
| interval | Integer | 循环间隔，根据type不同单位不同。例如当`type=daily`时表示间隔N天，`type=absoluteYearly`则表示间隔N年。 |
| firstDayOfWeek | String | 一周起始日，可取值包括：sunday、monday、tuesday、wednesday、thursday、friday、saturday。 默认值为“sunday”。 |
| range | Object | 循环范围。 |
| type | String | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| endDate | String | 循环结束日期。 |
| numberOfOccurrences | Integer | 重复次数。 |
| attendees | Array | 日程参与人。 |
| id | String | 用户unionId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否是当前登录用户。   - **true**：是 - **false**：不是 |
| isOptional | Boolean | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| organizer | Object | 日程组织人。 |
| id | String | 用户unionId。 |
| displayName | String | 用户名。 |
| responseStatus | String | 回复状态。 |
| self | Boolean | 是否是当前登录用户。   - **true**：是 - **false**：不是 |
| location | Object | 日程地点。 |
| displayName | String | 展示名称。 |
| meetingRooms | Array of String | 会议室 |
| seriesMasterId | String | 重复日程的主日程id，非重复日程为空。 |
| createTime | String | 创建时间。 |
| updateTime | String | 更新时间。 |
| status | String | 日程状态。 |
| onlineMeetingInfo | Object | 线上会议。 |
| type | String | 线上会议类型，目前支持：   - **dingtalk**：钉钉视频会议 |
| conferenceId | String | 会议ID。 |
| url | String | 参会的URL地址。 |
| extraInfo | Map | 其他扩展信息。 |
| reminders | Array | 日程提醒。 |
| method | String | 提醒方式。 |
| minutes | String | 在日程开始前N分钟发出提醒。 |
| extendedProperties | Object | 日程扩展属性。 |
| sharedProperties | Object | 共享字段。 |
| sourceOpenCid | String | 当日程是由某个群内发起的时候，该字段表示日程发起的来源群。 |
| belongCorpId | String | 日程归属企业的corpId。 |
| meetingRooms | Array | 会议室。 |
| roomId | String | 会议室roomId。 |
| responseStatus | String | 会议室响应状态：   - **accepted** : 接受 - **tentative**: 审批中 - **declined** : 审批未通过 |
| displayName | String | 会议室名称。 |
| categories | Array | 日程类型。 |
| displayName | String | 日程类型名称。 |
| richTextDescription | Object | 富文本字段。 |
| text | String | 富文本内容。 |
| syncToken | String | 增量同步token。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "cnNTbW1YbxxxxdlQrQT09",
  "events" : [ {
    "id" : "cnNTbW1YbxxxxdEgvdlQrQT09",
    "summary" : "test event",
    "description" : "something about this event",
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
      "id" : "iiiP35sJaxxxxRKgiEiF",
      "displayName" : "jack",
      "responseStatus" : "accepted",
      "self" : false,
      "isOptional" : false
    } ],
    "organizer" : {
      "id" : "iiiP35xxxxBSgjrwPRKgiEiF",
      "displayName" : "tony",
      "responseStatus" : "accepted",
      "self" : false
    },
    "location" : {
      "displayName" : "room 1-2-3",
      "meetingRooms" : [ "会议室" ]
    },
    "seriesMasterId" : "cnNTbWxxxxaFJZdEgvdlQrQT09",
    "createTime" : "2020-01-01T10:15:30+08:00",
    "updateTime" : "2020-01-01T10:15:30+08:00",
    "status" : "confirmed",
    "onlineMeetingInfo" : {
      "type" : "dingtalk",
      "conferenceId" : "5c4df21dxxxx-a6db402b9f3a",
      "url" : "dingtalk://dingtalkclient/page/videoCoxxxxndar?confId=5c4df21dxxxx2b9f3a&calendarId=92xxxx36"
    },
    "reminders" : [ {
      "method" : "dingtalk",
      "minutes" : "15"
    } ],
    "extendedProperties" : {
      "sharedProperties" : {
        "sourceOpenCid" : "zxcv90asdf123===",
        "belongCorpId" : "ding*********31"
      }
    },
    "meetingRooms" : [ {
      "roomId" : "c10315a8b4e740a317813ab6fxxxxxx",
      "responseStatus" : "accepted",
      "displayName" : "1号会议室"
    } ],
    "categories" : [ {
      "displayName" : "双周会"
    } ]
  } ],
  "syncToken" : "zxcasdfvc000009"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
