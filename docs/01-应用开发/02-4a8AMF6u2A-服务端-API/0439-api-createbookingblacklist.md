---
title: "创建会议室预定黑名单"
source_url: "https://open.dingtalk.com/document/development/api-createbookingblacklist"
namespace: "development"
slug: "api-createbookingblacklist"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 创建会议室预定黑名单"
doc_id: "O23nOyz3GL"
updated_at: "2026-06-02 13:04:56"
---

> Source: https://open.dingtalk.com/document/development/api-createbookingblacklist
> Path: 应用开发 / 服务端 API / 音视频 > 智能会议室 > 会议室 > 创建会议室预定黑名单
> Updated: 2026-06-02 13:04:56

# 创建会议室预定黑名单

调用本接口，可以创建会议室预定黑名单

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/bookings/blacklist |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人unionId。 |
| blacklistUnionId | String | 是 | 黑名单用户的unionId。 |
| startTime | Long | 是 | 封禁开始时间，毫秒级UTC时间戳。 |
| endTime | Long | 否 | 封禁结束时间，毫秒级UTC时间戳。不传表示永久封禁。 |
| memo | String | 否 | 备注。 |

### 请求示例

HTTP

```
POST /v1.0/rooms/bookings/blacklist HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:ff1f230ff0c539249b39abcba59c1718
Content-Type:application/json

{
  "unionId" : "2iPOLxxxxx",
  "blacklistUnionId" : "2iPOLxxxxx",
  "startTime" : 1728539655017,
  "endTime" : 1728539655110,
  "memo" : "备注"
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
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.CreateBookingBlacklistHeaders createBookingBlacklistHeaders = new com.aliyun.dingtalkrooms_1_0.models.CreateBookingBlacklistHeaders();
        createBookingBlacklistHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.CreateBookingBlacklistRequest createBookingBlacklistRequest = new com.aliyun.dingtalkrooms_1_0.models.CreateBookingBlacklistRequest()
                .setUnionId("2iPOLxxxxx")
                .setBlacklistUnionId("2iPOLxxxxx")
                .setStartTime(1728539655017L)
                .setEndTime(1728539655110L)
                .setMemo("备注");
        try {
            client.createBookingBlacklistWithOptions(createBookingBlacklistRequest, createBookingBlacklistHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_booking_blacklist_headers = dingtalkrooms__1__0_models.CreateBookingBlacklistHeaders()
        create_booking_blacklist_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_booking_blacklist_request = dingtalkrooms__1__0_models.CreateBookingBlacklistRequest(
            union_id='2iPOLxxxxx',
            blacklist_union_id='2iPOLxxxxx',
            start_time=1728539655017,
            end_time=1728539655110,
            memo='备注'
        )
        try:
            client.create_booking_blacklist_with_options(create_booking_blacklist_request, create_booking_blacklist_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_booking_blacklist_headers = dingtalkrooms__1__0_models.CreateBookingBlacklistHeaders()
        create_booking_blacklist_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_booking_blacklist_request = dingtalkrooms__1__0_models.CreateBookingBlacklistRequest(
            union_id='2iPOLxxxxx',
            blacklist_union_id='2iPOLxxxxx',
            start_time=1728539655017,
            end_time=1728539655110,
            memo='备注'
        )
        try:
            await client.create_booking_blacklist_with_options_async(create_booking_blacklist_request, create_booking_blacklist_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\CreateBookingBlacklistHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\CreateBookingBlacklistRequest;
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
        $createBookingBlacklistHeaders = new CreateBookingBlacklistHeaders([]);
        $createBookingBlacklistHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createBookingBlacklistRequest = new CreateBookingBlacklistRequest([
            "unionId" => "2iPOLxxxxx",
            "blacklistUnionId" => "2iPOLxxxxx",
            "startTime" => 1728539655017,
            "endTime" => 1728539655110,
            "memo" => "备注"
        ]);
        try {
            $client->createBookingBlacklistWithOptions($createBookingBlacklistRequest, $createBookingBlacklistHeaders, new RuntimeOptions([]));
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

  createBookingBlacklistHeaders := &dingtalkrooms_1_0.CreateBookingBlacklistHeaders{}
  createBookingBlacklistHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createBookingBlacklistRequest := &dingtalkrooms_1_0.CreateBookingBlacklistRequest{
    UnionId: tea.String("2iPOLxxxxx"),
    BlacklistUnionId: tea.String("2iPOLxxxxx"),
    StartTime: tea.Int64(1728539655017),
    EndTime: tea.Int64(1728539655110),
    Memo: tea.String("备注"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateBookingBlacklistWithOptions(createBookingBlacklistRequest, createBookingBlacklistHeaders, &util.RuntimeOptions{})
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
    let createBookingBlacklistHeaders = new dingtalkrooms_1_0.CreateBookingBlacklistHeaders({ });
    createBookingBlacklistHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createBookingBlacklistRequest = new dingtalkrooms_1_0.CreateBookingBlacklistRequest({
      unionId: '2iPOLxxxxx',
      blacklistUnionId: '2iPOLxxxxx',
      startTime: 1728539655017,
      endTime: 1728539655110,
      memo: '备注',
    });
    try {
      await client.createBookingBlacklistWithOptions(createBookingBlacklistRequest, createBookingBlacklistHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateBookingBlacklistHeaders createBookingBlacklistHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateBookingBlacklistHeaders();
            createBookingBlacklistHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateBookingBlacklistRequest createBookingBlacklistRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateBookingBlacklistRequest
            {
                UnionId = "2iPOLxxxxx",
                BlacklistUnionId = "2iPOLxxxxx",
                StartTime = 1728539655017,
                EndTime = 1728539655110,
                Memo = "备注",
            };
            try
            {
                client.CreateBookingBlacklistWithOptions(createBookingBlacklistRequest, createBookingBlacklistHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | user.not.admin | User Not Admin | 用户不是管理员 |
| 400 | user.not.org | User Not In Org | 用户不在组织内 |
| 500 | system.error | System Error | 系统错误 |
