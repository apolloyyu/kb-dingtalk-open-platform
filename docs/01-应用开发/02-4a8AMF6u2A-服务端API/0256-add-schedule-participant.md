---
title: "添加日程参与者"
source_url: "https://open.dingtalk.com/document/development/add-schedule-participant"
namespace: "development"
slug: "add-schedule-participant"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 日程参与者 > 添加日程参与者"
doc_id: "8brpIk1ZkD"
updated_at: "2026-06-02 09:25:03"
---

> Source: https://open.dingtalk.com/document/development/add-schedule-participant
> Path: 应用开发 / 服务端API / 日程 > 日程参与者 > 添加日程参与者
> Updated: 2026-06-02 09:25:03

# 添加日程参与者

调用本接口，添加日程参与者。

## 接口调用说明

每次日程参与者操作最大支持500人，最大支持操作5000人的日程。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/attendees |
| HTTP Method | POST |
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
| userId | String | 是 | 日程创建者的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历id，统一为primary，表示用户的主日历。 |
| eventId | String | 是 | 日程ID，可调用[查询日程列表](0254-query-an-event-list.md)接口获取id参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| attendeesToAdd | Array | 是 | 需要添加的参与人列表。 |
| id | String | 否 | 参与人uninonId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| isOptional | Boolean | 否 | 是否为可选参与人。   - **true**：是 - **false**：不是 |
| pushNotification | Boolean | 否 | 是否弹窗提醒。 |
| chatNotification | Boolean | 否 | 是否单聊提醒。 |

### 请求示例

HTTP

```
POST /v1.0/calendar/users/U5KPwll3QjgiG/calendars/primary/events/cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08/attendees HTTP/1.1
Host:api.dingtalk.com
x-client-token:******
x-acs-dingtalk-access-token:dd43888e26953deead8cba556389b063
Content-Type:application/json

{
  "attendeesToAdd" : [ {
    "id" : "iiiP35sJadba8aBSgjrwPRKgiEiF",
    "isOptional" : false
  } ]
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
        com.aliyun.dingtalkcalendar_1_0.models.AddAttendeeHeaders addAttendeeHeaders = new com.aliyun.dingtalkcalendar_1_0.models.AddAttendeeHeaders();
        addAttendeeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd attendeesToAdd0 = new com.aliyun.dingtalkcalendar_1_0.models.AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd()
                .setId("iiiP35sJadba8aBSgjrwPRKgiEiF")
                .setIsOptional(false);
        com.aliyun.dingtalkcalendar_1_0.models.AddAttendeeRequest addAttendeeRequest = new com.aliyun.dingtalkcalendar_1_0.models.AddAttendeeRequest()
                .setAttendeesToAdd(java.util.Arrays.asList(
                    attendeesToAdd0
                ));
        try {
            client.addAttendeeWithOptions("U5KPwll3QjgiG", "primary", "cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08", addAttendeeRequest, addAttendeeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_attendee_headers = dingtalkcalendar__1__0_models.AddAttendeeHeaders()
        add_attendee_headers.x_acs_dingtalk_access_token = '<your access token>'
        attendees_to_add_0 = dingtalkcalendar__1__0_models.AddAttendeeRequestAttendeesToAdd(
            id='iiiP35sJadba8aBSgjrwPRKgiEiF',
            is_optional=False
        )
        add_attendee_request = dingtalkcalendar__1__0_models.AddAttendeeRequest(
            attendees_to_add=[
                attendees_to_add_0
            ]
        )
        try:
            client.add_attendee_with_options('U5KPwll3QjgiG', 'primary', 'cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08', add_attendee_request, add_attendee_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_attendee_headers = dingtalkcalendar__1__0_models.AddAttendeeHeaders()
        add_attendee_headers.x_acs_dingtalk_access_token = '<your access token>'
        attendees_to_add_0 = dingtalkcalendar__1__0_models.AddAttendeeRequestAttendeesToAdd(
            id='iiiP35sJadba8aBSgjrwPRKgiEiF',
            is_optional=False
        )
        add_attendee_request = dingtalkcalendar__1__0_models.AddAttendeeRequest(
            attendees_to_add=[
                attendees_to_add_0
            ]
        )
        try:
            await client.add_attendee_with_options_async('U5KPwll3QjgiG', 'primary', 'cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08', add_attendee_request, add_attendee_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\AddAttendeeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\AddAttendeeRequest\attendeesToAdd;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\AddAttendeeRequest;
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
        $addAttendeeHeaders = new AddAttendeeHeaders([]);
        $addAttendeeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $attendeesToAdd0 = new attendeesToAdd([
            "id" => "iiiP35sJadba8aBSgjrwPRKgiEiF",
            "isOptional" => false
        ]);
        $addAttendeeRequest = new AddAttendeeRequest([
            "attendeesToAdd" => [
                $attendeesToAdd0
            ]
        ]);
        try {
            $client->addAttendeeWithOptions("U5KPwll3QjgiG", "primary", "cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08", $addAttendeeRequest, $addAttendeeHeaders, new RuntimeOptions([]));
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

  addAttendeeHeaders := &dingtalkcalendar_1_0.AddAttendeeHeaders{}
  addAttendeeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  attendeesToAdd0 := &dingtalkcalendar_1_0.AddAttendeeRequestAttendeesToAdd{
    Id: tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF"),
    IsOptional: tea.Bool(false),
  }
  addAttendeeRequest := &dingtalkcalendar_1_0.AddAttendeeRequest{
    AttendeesToAdd: []*dingtalkcalendar_1_0.AddAttendeeRequestAttendeesToAdd{attendeesToAdd0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddAttendeeWithOptions(tea.String("U5KPwll3QjgiG"), tea.String("primary"), tea.String("cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08"), addAttendeeRequest, addAttendeeHeaders, &util.RuntimeOptions{})
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
    let addAttendeeHeaders = new $dingtalkcalendar_1_0.AddAttendeeHeaders({ });
    addAttendeeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let attendeesToAdd0 = new $dingtalkcalendar_1_0.AddAttendeeRequestAttendeesToAdd({
      id: "iiiP35sJadba8aBSgjrwPRKgiEiF",
      isOptional: false,
    });
    let addAttendeeRequest = new $dingtalkcalendar_1_0.AddAttendeeRequest({
      attendeesToAdd: [
        attendeesToAdd0
      ],
    });
    try {
      await client.addAttendeeWithOptions("U5KPwll3QjgiG", "primary", "cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08", addAttendeeRequest, addAttendeeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeHeaders addAttendeeHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeHeaders();
            addAttendeeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd attendeesToAdd0 = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd
            {
                Id = "iiiP35sJadba8aBSgjrwPRKgiEiF",
                IsOptional = false,
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeRequest addAttendeeRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeRequest
            {
                AttendeesToAdd = new List<AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.AddAttendeeRequest.AddAttendeeRequestAttendeesToAdd>
                {
                    attendeesToAdd0
                },
            };
            try
            {
                client.AddAttendeeWithOptions("U5KPwll3QjgiG", "primary", "cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT08", addAttendeeRequest, addAttendeeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | idempotencyProcessing | Idempotency processing | 幂等请求处理中 |
| 404 | itemNotFound | forwardErrorMessage | 无法找到指定日程 |
