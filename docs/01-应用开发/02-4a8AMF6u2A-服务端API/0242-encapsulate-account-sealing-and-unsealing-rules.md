---
title: "查询指定用户的封账规则"
source_url: "https://open.dingtalk.com/document/development/encapsulate-account-sealing-and-unsealing-rules"
namespace: "development"
slug: "encapsulate-account-sealing-and-unsealing-rules"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 封账规则 > 查询指定用户的封账规则"
doc_id: "lAWfGwjzvn"
updated_at: "2026-06-08 11:46:50"
---

> Source: https://open.dingtalk.com/document/development/encapsulate-account-sealing-and-unsealing-rules
> Path: 应用开发 / 服务端API / 考勤 > 封账规则 > 查询指定用户的封账规则
> Updated: 2026-06-08 11:46:50

# 查询指定用户的封账规则

调用本接口查询指定用户的封账和解封规则。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/closingAccounts/rules/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Pro.AttendanceAccounts.Read-考勤场景封账规则数据的读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 人员userId列表。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/closingAccounts/rules/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxx
Content-Type:application/json

{
  "userIds" : [ "user001" ]
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
        com.aliyun.dingtalkattendance_1_0.models.GetClosingAccountsHeaders getClosingAccountsHeaders = new com.aliyun.dingtalkattendance_1_0.models.GetClosingAccountsHeaders();
        getClosingAccountsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.GetClosingAccountsRequest getClosingAccountsRequest = new com.aliyun.dingtalkattendance_1_0.models.GetClosingAccountsRequest()
                .setUserIds(java.util.Arrays.asList(
                    "user001"
                ));
        try {
            client.getClosingAccountsWithOptions(getClosingAccountsRequest, getClosingAccountsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_closing_accounts_headers = dingtalkattendance__1__0_models.GetClosingAccountsHeaders()
        get_closing_accounts_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_closing_accounts_request = dingtalkattendance__1__0_models.GetClosingAccountsRequest(
            user_ids=[
                'user001'
            ]
        )
        try:
            client.get_closing_accounts_with_options(get_closing_accounts_request, get_closing_accounts_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_closing_accounts_headers = dingtalkattendance__1__0_models.GetClosingAccountsHeaders()
        get_closing_accounts_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_closing_accounts_request = dingtalkattendance__1__0_models.GetClosingAccountsRequest(
            user_ids=[
                'user001'
            ]
        )
        try:
            await client.get_closing_accounts_with_options_async(get_closing_accounts_request, get_closing_accounts_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetClosingAccountsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetClosingAccountsRequest;
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
        $getClosingAccountsHeaders = new GetClosingAccountsHeaders([]);
        $getClosingAccountsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getClosingAccountsRequest = new GetClosingAccountsRequest([
            "userIds" => [
                "user001"
            ]
        ]);
        try {
            $client->getClosingAccountsWithOptions($getClosingAccountsRequest, $getClosingAccountsHeaders, new RuntimeOptions([]));
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
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  getClosingAccountsHeaders := &dingtalkattendance_1_0.GetClosingAccountsHeaders{}
  getClosingAccountsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getClosingAccountsRequest := &dingtalkattendance_1_0.GetClosingAccountsRequest{
    UserIds: []*string{tea.String("user001")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetClosingAccountsWithOptions(getClosingAccountsRequest, getClosingAccountsHeaders, &util.RuntimeOptions{})
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
    let getClosingAccountsHeaders = new $dingtalkattendance_1_0.GetClosingAccountsHeaders({ });
    getClosingAccountsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getClosingAccountsRequest = new $dingtalkattendance_1_0.GetClosingAccountsRequest({
      userIds: [
        "user001"
      ],
    });
    try {
      await client.getClosingAccountsWithOptions(getClosingAccountsRequest, getClosingAccountsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetClosingAccountsHeaders getClosingAccountsHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetClosingAccountsHeaders();
            getClosingAccountsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetClosingAccountsRequest getClosingAccountsRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetClosingAccountsRequest
            {
                UserIds = new List<string>
                {
                    "user001"
                },
            };
            try
            {
                client.GetClosingAccountsWithOptions(getClosingAccountsRequest, getClosingAccountsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 规则列表。 |
| userId | String | 人员userId。 |
| switchOn | Boolean | 规则标识：   - **true**：开 - **false**：关 |
| closingAccountModel | Object | 封账规则。 |
| closingDay | Integer | 封账时间，单位日，例如：每月的30日。 |
| closingHourMinutes | Long | 封账时间中时分转换的时间戳，例如：16:00。 |
| startMonth | Integer | 封账开始范围中的月。   - **-2**：上上月 - **-1**：上月 - **0**：本月 |
| startDay | Integer | 封账开始范围中的日，例如1日。 |
| endMonth | Integer | 封账结束范围中的月：   - **-2**：上上月 - **-1**：上月 - **0**：本月 |
| endDay | Integer | 封账结束范围中的日，例如30日。 |
| unsealClosingAccountModel | Object | 解封规则。 |
| invalidTimeStamp | Long | 解封时间戳，单位毫秒。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "userId" : "user001",
    "switchOn" : true,
    "closingAccountModel" : {
      "closingDay" : 30,
      "closingHourMinutes" : 28800000,
      "startMonth" : -1,
      "startDay" : 1,
      "endMonth" : -1,
      "endDay" : 30
    },
    "unsealClosingAccountModel" : {
      "invalidTimeStamp" : 1625097600000
    }
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 参数异常 |
| 500 | systemError | 系统异常 | 系统异常 |
