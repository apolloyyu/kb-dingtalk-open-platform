---
title: "查询用户考勤节假日信息"
source_url: "https://open.dingtalk.com/document/development/obtain-user-attendance-and-holiday-information"
namespace: "development"
slug: "obtain-user-attendance-and-holiday-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 查询用户考勤节假日信息"
doc_id: "xV9G9Ibsii"
updated_at: "2026-06-01 16:58:45"
---

> Source: https://open.dingtalk.com/document/development/obtain-user-attendance-and-holiday-information
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 查询用户考勤节假日信息
> Updated: 2026-06-01 16:58:45

# 查询用户考勤节假日信息

调用本接口查询员工一段时间内的节假日信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/holidays |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 员工列表。 |
| workDateFrom | Long | 是 | 开始日期。 |
| workDateTo | Long | 是 | 结束日期。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/holidays HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3XX
Content-Type:application/json

{
  "userIds" : [ "fdfi3435" ],
  "workDateFrom" : 1609430400000,
  "workDateTo" : 1614528000000
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
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkattendance_1_0.models.GetUserHolidaysHeaders getUserHolidaysHeaders = new com.aliyun.dingtalkattendance_1_0.models.GetUserHolidaysHeaders();
        getUserHolidaysHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.GetUserHolidaysRequest getUserHolidaysRequest = new com.aliyun.dingtalkattendance_1_0.models.GetUserHolidaysRequest()
                .setUserIds(java.util.Arrays.asList(
                    "fdfi3435"
                ))
                .setWorkDateFrom(1609430400000L)
                .setWorkDateTo(1614528000000L);
        try {
            client.getUserHolidaysWithOptions(getUserHolidaysRequest, getUserHolidaysHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.attendance_1_0.client import Client as dingtalkattendance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.attendance_1_0 import models as dingtalkattendance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkattendance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkattendance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_holidays_headers = dingtalkattendance__1__0_models.GetUserHolidaysHeaders()
        get_user_holidays_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_holidays_request = dingtalkattendance__1__0_models.GetUserHolidaysRequest(
            user_ids=[
                'fdfi3435'
            ],
            work_date_from=1609430400000,
            work_date_to=1614528000000
        )
        try:
            client.get_user_holidays_with_options(get_user_holidays_request, get_user_holidays_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_holidays_headers = dingtalkattendance__1__0_models.GetUserHolidaysHeaders()
        get_user_holidays_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_holidays_request = dingtalkattendance__1__0_models.GetUserHolidaysRequest(
            user_ids=[
                'fdfi3435'
            ],
            work_date_from=1609430400000,
            work_date_to=1614528000000
        )
        try:
            await client.get_user_holidays_with_options_async(get_user_holidays_request, get_user_holidays_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetUserHolidaysHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetUserHolidaysRequest;
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
        $getUserHolidaysHeaders = new GetUserHolidaysHeaders([]);
        $getUserHolidaysHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUserHolidaysRequest = new GetUserHolidaysRequest([
            "userIds" => [
                "fdfi3435"
            ],
            "workDateFrom" => 1609430400000,
            "workDateTo" => 1614528000000
        ]);
        try {
            $client->getUserHolidaysWithOptions($getUserHolidaysRequest, $getUserHolidaysHeaders, new RuntimeOptions([]));
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
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkattendance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkattendance_1_0.Client{}
  _result, _err = dingtalkattendance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUserHolidaysHeaders := &dingtalkattendance_1_0.GetUserHolidaysHeaders{}
  getUserHolidaysHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUserHolidaysRequest := &dingtalkattendance_1_0.GetUserHolidaysRequest{
    UserIds: []*string{tea.String("fdfi3435")},
    WorkDateFrom: tea.Int64(1609430400000),
    WorkDateTo: tea.Int64(1614528000000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserHolidaysWithOptions(getUserHolidaysRequest, getUserHolidaysHeaders, &util.RuntimeOptions{})
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
import dingtalkattendance_1_0, * as $dingtalkattendance_1_0 from '@alicloud/dingtalk/attendance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkattendance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkattendance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUserHolidaysHeaders = new $dingtalkattendance_1_0.GetUserHolidaysHeaders({ });
    getUserHolidaysHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUserHolidaysRequest = new $dingtalkattendance_1_0.GetUserHolidaysRequest({
      userIds: [
        "fdfi3435"
      ],
      workDateFrom: 1609430400000,
      workDateTo: 1614528000000,
    });
    try {
      await client.getUserHolidaysWithOptions(getUserHolidaysRequest, getUserHolidaysHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkattendance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkattendance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetUserHolidaysHeaders getUserHolidaysHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetUserHolidaysHeaders();
            getUserHolidaysHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetUserHolidaysRequest getUserHolidaysRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetUserHolidaysRequest
            {
                UserIds = new List<string>
                {
                    "fdfi3435"
                },
                WorkDateFrom = 1609430400000,
                WorkDateTo = 1614528000000,
            };
            try
            {
                client.GetUserHolidaysWithOptions(getUserHolidaysRequest, getUserHolidaysHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 员工假期列表。 |
| userId | String | 员工的userid。 |
| holidays | Array | 假期列表。 |
| workDate | Long | 日期。 |
| holidayName | String | 假期名称。 |
| holidayType | String | 假期类型：   - festival：法定节假日 - rest：调休日 - overtime：加班日 |
| realWorkDate | Long | 补休日，只有假期类型为加班日时才有值。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "userId" : "fdfi3435",
    "holidays" : [ {
      "workDate" : 1613059200000,
      "holidayName" : "春节",
      "holidayType" : "festival",
      "realWorkDate" : 1612627200000
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 参数异常 |
| 500 | systemError | 系统异常 | 系统异常 |
