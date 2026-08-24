---
title: "查询实人认证状态"
source_url: "https://open.dingtalk.com/document/development/queries-the-id-verification-status"
namespace: "development"
slug: "queries-the-id-verification-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 查询实人认证状态"
doc_id: "hLhTovXZJz"
updated_at: "2026-06-02 19:19:55"
---

> Source: https://open.dingtalk.com/document/development/queries-the-id-verification-status
> Path: 应用开发 / 服务端API / 专属钉钉 > 查询实人认证状态
> Updated: 2026-06-02 19:19:55

# 查询实人认证状态

调用本接口，查询实人认证状态。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/persons/identificationStates/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.Ding.RealPeople.Recognize-专属钉钉实人认证权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 员工userId列表。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/persons/identificationStates/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "userIds" : [ "1234" ]
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.GetUserRealPeopleStateHeaders getUserRealPeopleStateHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetUserRealPeopleStateHeaders();
        getUserRealPeopleStateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetUserRealPeopleStateRequest getUserRealPeopleStateRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetUserRealPeopleStateRequest()
                .setUserIds(java.util.Arrays.asList(
                    "1234"
                ));
        try {
            client.getUserRealPeopleStateWithOptions(getUserRealPeopleStateRequest, getUserRealPeopleStateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_real_people_state_headers = dingtalkexclusive__1__0_models.GetUserRealPeopleStateHeaders()
        get_user_real_people_state_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_real_people_state_request = dingtalkexclusive__1__0_models.GetUserRealPeopleStateRequest(
            user_ids=[
                '1234'
            ]
        )
        try:
            client.get_user_real_people_state_with_options(get_user_real_people_state_request, get_user_real_people_state_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_real_people_state_headers = dingtalkexclusive__1__0_models.GetUserRealPeopleStateHeaders()
        get_user_real_people_state_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_real_people_state_request = dingtalkexclusive__1__0_models.GetUserRealPeopleStateRequest(
            user_ids=[
                '1234'
            ]
        )
        try:
            await client.get_user_real_people_state_with_options_async(get_user_real_people_state_request, get_user_real_people_state_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetUserRealPeopleStateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetUserRealPeopleStateRequest;
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
        $getUserRealPeopleStateHeaders = new GetUserRealPeopleStateHeaders([]);
        $getUserRealPeopleStateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUserRealPeopleStateRequest = new GetUserRealPeopleStateRequest([
            "userIds" => [
                "1234"
            ]
        ]);
        try {
            $client->getUserRealPeopleStateWithOptions($getUserRealPeopleStateRequest, $getUserRealPeopleStateHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUserRealPeopleStateHeaders := &dingtalkexclusive_1_0.GetUserRealPeopleStateHeaders{}
  getUserRealPeopleStateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUserRealPeopleStateRequest := &dingtalkexclusive_1_0.GetUserRealPeopleStateRequest{
    UserIds: []*string{tea.String("1234")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserRealPeopleStateWithOptions(getUserRealPeopleStateRequest, getUserRealPeopleStateHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUserRealPeopleStateHeaders = new $dingtalkexclusive_1_0.GetUserRealPeopleStateHeaders({ });
    getUserRealPeopleStateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUserRealPeopleStateRequest = new $dingtalkexclusive_1_0.GetUserRealPeopleStateRequest({
      userIds: [
        "1234"
      ],
    });
    try {
      await client.getUserRealPeopleStateWithOptions(getUserRealPeopleStateRequest, getUserRealPeopleStateHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetUserRealPeopleStateHeaders getUserRealPeopleStateHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetUserRealPeopleStateHeaders();
            getUserRealPeopleStateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetUserRealPeopleStateRequest getUserRealPeopleStateRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetUserRealPeopleStateRequest
            {
                UserIds = new List<string>
                {
                    "1234"
                },
            };
            try
            {
                client.GetUserRealPeopleStateWithOptions(getUserRealPeopleStateRequest, getUserRealPeopleStateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Array | 返回的信息列表。 |
| state | Integer | 认证状态：   - 1：未认证 - 2：已认证 |
| userId | String | 用户userId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "state" : 1,
    "userId" : "001"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | userIds.missing | 请求中不含userIds字段 | 请求中不含userIds字段 |
