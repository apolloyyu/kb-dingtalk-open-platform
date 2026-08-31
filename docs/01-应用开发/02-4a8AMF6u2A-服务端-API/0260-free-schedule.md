---
title: "获取用户忙闲信息"
source_url: "https://open.dingtalk.com/document/development/free-schedule"
namespace: "development"
slug: "free-schedule"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 忙闲 > 获取用户忙闲信息"
doc_id: "1HTjIv98oc"
updated_at: "2026-06-02 09:25:06"
---

> Source: https://open.dingtalk.com/document/development/free-schedule
> Path: 应用开发 / 服务端 API / 日程 > 忙闲 > 获取用户忙闲信息
> Updated: 2026-06-02 09:25:06

# 获取用户忙闲信息

调用本接口，查询指定用户列表在指定时间内的忙闲信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/querySchedule |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.EventSchedule.Read-日历应用中日程闲忙状态读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 本次请求的资源所归属的用户unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 查询目标用户的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。       用户列表最大长度 20。 |
| startTime | String | 是 | 查询的开始时间。 |
| endTime | String | 是 | 查询的结束时间。 |

### 请求示例

HTTP

```
POST /v1.0/calendar/users/iiiP35sJaxx/getSchedule HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dd43888xxx
Content-Type:application/json

{
  "userIds" : [ "iiiP35sJaxxx" ],
  "startTime" : "2020-01-01T10:15:30+08:00",
  "endTime" : "2020-01-01T10:15:30+08:00"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcalendar_1_0.*;
import com.aliyun.dingtalkcalendar_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcalendar_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcalendar_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcalendar_1_0.Client client = Sample.createClient();
        GetScheduleHeaders getScheduleHeaders = new GetScheduleHeaders();
        getScheduleHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetScheduleRequest getScheduleRequest = new GetScheduleRequest()
                .setUserIds(java.util.Arrays.asList(
                    "iiiP35sJaxxx"
                ))
                .setStartTime("2020-01-01T10:15:30+08:00")
                .setEndTime("2020-01-01T10:15:30+08:00");
        try {
            client.getScheduleWithOptions("iiiP35sJaxx", getScheduleRequest, getScheduleHeaders, new RuntimeOptions());
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
        get_schedule_headers = dingtalkcalendar__1__0_models.GetScheduleHeaders()
        get_schedule_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_schedule_request = dingtalkcalendar__1__0_models.GetScheduleRequest(
            user_ids=[
                'iiiP35sJaxxx'
            ],
            start_time='2020-01-01T10:15:30+08:00',
            end_time='2020-01-01T10:15:30+08:00'
        )
        try:
            client.get_schedule_with_options('iiiP35sJaxx', get_schedule_request, get_schedule_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_schedule_headers = dingtalkcalendar__1__0_models.GetScheduleHeaders()
        get_schedule_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_schedule_request = dingtalkcalendar__1__0_models.GetScheduleRequest(
            user_ids=[
                'iiiP35sJaxxx'
            ],
            start_time='2020-01-01T10:15:30+08:00',
            end_time='2020-01-01T10:15:30+08:00'
        )
        try:
            await client.get_schedule_with_options_async('iiiP35sJaxx', get_schedule_request, get_schedule_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetScheduleHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetScheduleRequest;
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
        $getScheduleHeaders = new GetScheduleHeaders([]);
        $getScheduleHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getScheduleRequest = new GetScheduleRequest([
            "userIds" => [
                "iiiP35sJaxxx"
            ],
            "startTime" => "2020-01-01T10:15:30+08:00",
            "endTime" => "2020-01-01T10:15:30+08:00"
        ]);
        try {
            $client->getScheduleWithOptions("iiiP35sJaxx", $getScheduleRequest, $getScheduleHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkcalendar_1_0  "github.com/alibabacloud-go/dingtalk/calendar_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  getScheduleHeaders := &dingtalkcalendar_1_0.GetScheduleHeaders{}
  getScheduleHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getScheduleRequest := &dingtalkcalendar_1_0.GetScheduleRequest{
    UserIds: []*string{tea.String("iiiP35sJaxxx")},
    StartTime: tea.String("2020-01-01T10:15:30+08:00"),
    EndTime: tea.String("2020-01-01T10:15:30+08:00"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetScheduleWithOptions(tea.String("iiiP35sJaxx"), getScheduleRequest, getScheduleHeaders, &util.RuntimeOptions{})
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
    let getScheduleHeaders = new $dingtalkcalendar_1_0.GetScheduleHeaders({ });
    getScheduleHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getScheduleRequest = new $dingtalkcalendar_1_0.GetScheduleRequest({
      userIds: [
        "iiiP35sJaxxx"
      ],
      startTime: "2020-01-01T10:15:30+08:00",
      endTime: "2020-01-01T10:15:30+08:00",
    });
    try {
      await client.getScheduleWithOptions("iiiP35sJaxx", getScheduleRequest, getScheduleHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetScheduleHeaders getScheduleHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetScheduleHeaders();
            getScheduleHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetScheduleRequest getScheduleRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetScheduleRequest
            {
                UserIds = new List<string>
                {
                    "iiiP35sJaxxx"
                },
                StartTime = "2020-01-01T10:15:30+08:00",
                EndTime = "2020-01-01T10:15:30+08:00",
            };
            try
            {
                client.GetScheduleWithOptions("iiiP35sJaxx", getScheduleRequest, getScheduleHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkcalendar__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcalendar_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcalendar_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcalendar_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcalendar_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcalendar_1_0::GetScheduleHeaders> getScheduleHeaders = make_shared<Alibabacloud_Dingtalkcalendar_1_0::GetScheduleHeaders>();
  getScheduleHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcalendar_1_0::GetScheduleRequest> getScheduleRequest = make_shared<Alibabacloud_Dingtalkcalendar_1_0::GetScheduleRequest>(map<string, boost::any>({
    {"userIds", boost::any(vector<string>({
      "iiiP35sJaxxx"
    }))},
    {"startTime", boost::any(string("2020-01-01T10:15:30+08:00"))},
    {"endTime", boost::any(string("2020-01-01T10:15:30+08:00"))}
  }));
  try {
    client->getScheduleWithOptions(make_shared<string>("iiiP35sJaxx"), getScheduleRequest, getScheduleHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| scheduleInformation | Array | 用户忙闲信息。 |
| userId | String | 查询目标用户的unionId。 |
| error | String | 异常信息。 |
| scheduleItems | Array | 忙闲信息列表。 |
| status | String | 状态。   - **BUSY**：繁忙 - **TENTATIVE**：暂定繁忙 |
| start | Object | 日程开始时间。 |
| date | String | 日程开始日期，格式：`yyyy-MM-dd`。 |
| dateTime | String | 日程开始时间，格式为`ISO-8601`的`date-time`格式。 |
| timeZone | String | 时区名称，使用**IANA Time Zone Database**标准，例如：`Asia/Shanghai`。      全天日程时区固定为UTC，非全天日程时区默认为`Asia/Shanghai`。 |
| end | Object | 日程结束时间。 |
| date | String | 日程结束日期，格式：`yyyy-MM-dd`。 |
| dateTime | String | 日程结束时间，格式为`ISO-8601`的`date-time`格式。 |
| timeZone | String | 时区名称，使用**IANA Time Zone Database**标准，例如：`Asia/Shanghai`。      全天日程时区固定为UTC，非全天日程时区默认为`Asia/Shanghai`。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "scheduleInformation" : [ {
    "userId" : "iiiP35sJadxxx",
    "error" : "无权限",
    "scheduleItems" : [ {
      "status" : "BUSY",
      "start" : {
        "date" : "2020-01-01",
        "dateTime" : "2020-01-01T10:15:30+08:00",
        "timeZone" : "Asia/Shanghai"
      },
      "end" : {
        "date" : "2020-01-01",
        "dateTime" : "2020-01-01T10:15:30+08:00",
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
| 400 | paramIllegal | PARAM ILLEGAL | 参数异常 |
