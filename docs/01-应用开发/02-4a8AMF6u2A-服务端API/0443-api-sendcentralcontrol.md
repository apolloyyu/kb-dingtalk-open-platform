---
title: "发送Rooms中控API信令"
source_url: "https://open.dingtalk.com/document/development/api-sendcentralcontrol"
namespace: "development"
slug: "api-sendcentralcontrol"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 发送Rooms中控API信令"
doc_id: "sbQF2AGf9U"
updated_at: "2026-06-01 14:27:50"
---

> Source: https://open.dingtalk.com/document/development/api-sendcentralcontrol
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 会议室 > 发送Rooms中控API信令
> Updated: 2026-06-01 14:27:50

# 发送Rooms中控API信令

给会议室中的设备发送中控信令，属于高级功能。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/central/control |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 否 | 操作人unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| roomId | String | 否 | 会议室ID，可通过调用[查询会议室列表](0437-check-the-meeting-room-list.md) 接口获取。 |
| controlBody | String | 否 | 中控信令。  **[!NOTE]**    该参数请联系对应的客户经理获取。 |

### 请求示例

HTTP

```
POST /v1.0/rooms/central/control HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2WCDFxxxxx
Content-Type:application/json

{
  "unionId" : "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
  "roomId" : "0ffb7xxxxx",
  "controlBody" : "{   \"version\": \"1.0.0\",    \"request\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"method\": \"subscribe\"    } }"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.SendCentralControlHeaders sendCentralControlHeaders = new com.aliyun.dingtalkrooms_1_0.models.SendCentralControlHeaders();
        sendCentralControlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.SendCentralControlRequest sendCentralControlRequest = new com.aliyun.dingtalkrooms_1_0.models.SendCentralControlRequest()
                .setUnionId("2iPOLbpUNMLzB5LuwggiiqiPwiEiE")
                .setRoomId("0ffb7xxxxx")
                .setControlBody("{   \"version\": \"1.0.0\",    \"request\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"method\": \"subscribe\"    } }");
        try {
            client.sendCentralControlWithOptions(sendCentralControlRequest, sendCentralControlHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.rooms_1_0.client import Client as dingtalkrooms_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.rooms_1_0 import models as dingtalkrooms__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrooms_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrooms_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_central_control_headers = dingtalkrooms__1__0_models.SendCentralControlHeaders()
        send_central_control_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_central_control_request = dingtalkrooms__1__0_models.SendCentralControlRequest(
            union_id='2iPOLbpUNMLzB5LuwggiiqiPwiEiE',
            room_id='0ffb7xxxxx',
            control_body='{   "version": "1.0.0",    "request": {     "requestId": "xxxx",      "service": "DTRooms.Meeting",      "method": "subscribe"    } }'
        )
        try:
            client.send_central_control_with_options(send_central_control_request, send_central_control_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_central_control_headers = dingtalkrooms__1__0_models.SendCentralControlHeaders()
        send_central_control_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_central_control_request = dingtalkrooms__1__0_models.SendCentralControlRequest(
            union_id='2iPOLbpUNMLzB5LuwggiiqiPwiEiE',
            room_id='0ffb7xxxxx',
            control_body='{   "version": "1.0.0",    "request": {     "requestId": "xxxx",      "service": "DTRooms.Meeting",      "method": "subscribe"    } }'
        )
        try:
            await client.send_central_control_with_options_async(send_central_control_request, send_central_control_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\SendCentralControlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\SendCentralControlRequest;
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
        $sendCentralControlHeaders = new SendCentralControlHeaders([]);
        $sendCentralControlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendCentralControlRequest = new SendCentralControlRequest([
            "unionId" => "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
            "roomId" => "0ffb7xxxxx",
            "controlBody" => "{   \"version\": \"1.0.0\",    \"request\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"method\": \"subscribe\"    } }"
        ]);
        try {
            $client->sendCentralControlWithOptions($sendCentralControlRequest, $sendCentralControlHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalkrooms_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrooms_1_0.Client{}
  _result, _err = dingtalkrooms_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendCentralControlHeaders := &dingtalkrooms_1_0.SendCentralControlHeaders{}
  sendCentralControlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendCentralControlRequest := &dingtalkrooms_1_0.SendCentralControlRequest{
    UnionId: tea.String("2iPOLbpUNMLzB5LuwggiiqiPwiEiE"),
    RoomId: tea.String("0ffb7xxxxx"),
    ControlBody: tea.String("{   \"version\": \"1.0.0\",    \"request\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"method\": \"subscribe\"    } }"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendCentralControlWithOptions(sendCentralControlRequest, sendCentralControlHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkrooms_1_0 = require('@alicloud/dingtalk/rooms_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkrooms_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let sendCentralControlHeaders = new dingtalkrooms_1_0.SendCentralControlHeaders({ });
    sendCentralControlHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let sendCentralControlRequest = new dingtalkrooms_1_0.SendCentralControlRequest({
      unionId: '2iPOLbpUNMLzB5LuwggiiqiPwiEiE',
      roomId: '0ffb7xxxxx',
      controlBody: '{   "version": "1.0.0",    "request": {     "requestId": "xxxx",      "service": "DTRooms.Meeting",      "method": "subscribe"    } }',
    });
    try {
      await client.sendCentralControlWithOptions(sendCentralControlRequest, sendCentralControlHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkrooms_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrooms_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.SendCentralControlHeaders sendCentralControlHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.SendCentralControlHeaders();
            sendCentralControlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.SendCentralControlRequest sendCentralControlRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.SendCentralControlRequest
            {
                UnionId = "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
                RoomId = "0ffb7xxxxx",
                ControlBody = "{   \"version\": \"1.0.0\",    \"request\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"method\": \"subscribe\"    } }",
            };
            try
            {
                client.SendCentralControlWithOptions(sendCentralControlRequest, sendCentralControlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数缺失错误 |
| 400 | user.not.org | User Not In Org | 用户不在组织内 |
| 400 | api.control.close | API CONTROL ClOSE | 会议室未开启中控能力 |
| 500 | system.error | System Error | 系统错误 |
