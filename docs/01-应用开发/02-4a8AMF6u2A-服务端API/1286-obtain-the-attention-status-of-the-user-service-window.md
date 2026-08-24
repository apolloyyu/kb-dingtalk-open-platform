---
title: "获取用户服务窗关注状态"
source_url: "https://open.dingtalk.com/document/development/obtain-the-attention-status-of-the-user-service-window"
namespace: "development"
slug: "obtain-the-attention-status-of-the-user-service-window"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 服务窗 > 获取用户服务窗关注状态"
doc_id: "Ywh6VqyHNI"
updated_at: "2026-06-04 19:12:02"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-attention-status-of-the-user-service-window
> Path: 应用开发 / 服务端API / 更多开放 > 服务窗 > 获取用户服务窗关注状态
> Updated: 2026-06-04 19:12:02

# 获取用户服务窗关注状态

调用本接口获取用户服务窗关注状态。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/link/followers/statuses |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-OfficialAccount.Contact.Read-服务窗联系人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 待查询的服务窗关注者userId，可通过调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取返回参数`userid`字段值。     - 需使用[自建服务窗应用](1279-self-built-service-window-application.md)，免登获取的`userId`，否则接口无法正确调用。 - `unionId`和`userId`二选一填写。 |
| unionId | String | 否 | 待查询的服务窗关注者unionId，可通过调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取返回参数`unionid`字段值。       - 需使用企业内部应用，免登获取的`unionid`，否则接口无法正确调用。 - `unionId`和`userId`二选一填写。 |
| accountId | String | 否 | 服务窗账号ID，通过[获取企业下服务窗列表](1282-queries-the-list-of-services-under-an-enterprise.md)接口获得。 |

### 请求示例

HTTP

```
GET /v1.0/link/followers/statuses?userId=Rp3Rqcts7BE08y49Jr6iu6xW4iQ&unionId=UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ&accountId=ding1234 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a3b89df4dfaaccd5b
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
    public static com.aliyun.dingtalklink_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalklink_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalklink_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalklink_1_0.models.GetUserFollowStatusHeaders getUserFollowStatusHeaders = new com.aliyun.dingtalklink_1_0.models.GetUserFollowStatusHeaders();
        getUserFollowStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalklink_1_0.models.GetUserFollowStatusRequest getUserFollowStatusRequest = new com.aliyun.dingtalklink_1_0.models.GetUserFollowStatusRequest()
                .setUserId("Rp3Rqcts7BE08y49Jr6iu6xW4iQ")
                .setUnionId("UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ")
                .setAccountId("ding1234");
        try {
            client.getUserFollowStatusWithOptions(getUserFollowStatusRequest, getUserFollowStatusHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.link_1_0.client import Client as dingtalklink_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.link_1_0 import models as dingtalklink__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalklink_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalklink_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_follow_status_headers = dingtalklink__1__0_models.GetUserFollowStatusHeaders()
        get_user_follow_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_follow_status_request = dingtalklink__1__0_models.GetUserFollowStatusRequest(
            user_id='Rp3Rqcts7BE08y49Jr6iu6xW4iQ',
            union_id='UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ',
            account_id='ding1234'
        )
        try:
            client.get_user_follow_status_with_options(get_user_follow_status_request, get_user_follow_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_follow_status_headers = dingtalklink__1__0_models.GetUserFollowStatusHeaders()
        get_user_follow_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_follow_status_request = dingtalklink__1__0_models.GetUserFollowStatusRequest(
            user_id='Rp3Rqcts7BE08y49Jr6iu6xW4iQ',
            union_id='UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ',
            account_id='ding1234'
        )
        try:
            await client.get_user_follow_status_with_options_async(get_user_follow_status_request, get_user_follow_status_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Models\GetUserFollowStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Models\GetUserFollowStatusRequest;
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
        $getUserFollowStatusHeaders = new GetUserFollowStatusHeaders([]);
        $getUserFollowStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUserFollowStatusRequest = new GetUserFollowStatusRequest([
            "userId" => "Rp3Rqcts7BE08y49Jr6iu6xW4iQ",
            "unionId" => "UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ",
            "accountId" => "ding1234"
        ]);
        try {
            $client->getUserFollowStatusWithOptions($getUserFollowStatusRequest, $getUserFollowStatusHeaders, new RuntimeOptions([]));
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
  dingtalklink_1_0  "github.com/alibabacloud-go/dingtalk/link_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalklink_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalklink_1_0.Client{}
  _result, _err = dingtalklink_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUserFollowStatusHeaders := &dingtalklink_1_0.GetUserFollowStatusHeaders{}
  getUserFollowStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUserFollowStatusRequest := &dingtalklink_1_0.GetUserFollowStatusRequest{
    UserId: tea.String("Rp3Rqcts7BE08y49Jr6iu6xW4iQ"),
    UnionId: tea.String("UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ"),
    AccountId: tea.String("ding1234"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserFollowStatusWithOptions(getUserFollowStatusRequest, getUserFollowStatusHeaders, &util.RuntimeOptions{})
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
import dingtalklink_1_0, * as $dingtalklink_1_0 from '@alicloud/dingtalk/link_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalklink_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalklink_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUserFollowStatusHeaders = new $dingtalklink_1_0.GetUserFollowStatusHeaders({ });
    getUserFollowStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUserFollowStatusRequest = new $dingtalklink_1_0.GetUserFollowStatusRequest({
      userId: "Rp3Rqcts7BE08y49Jr6iu6xW4iQ",
      unionId: "UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ",
      accountId: "ding1234",
    });
    try {
      await client.getUserFollowStatusWithOptions(getUserFollowStatusRequest, getUserFollowStatusHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalklink_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalklink_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalklink_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetUserFollowStatusHeaders getUserFollowStatusHeaders = new AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetUserFollowStatusHeaders();
            getUserFollowStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetUserFollowStatusRequest getUserFollowStatusRequest = new AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetUserFollowStatusRequest
            {
                UserId = "Rp3Rqcts7BE08y49Jr6iu6xW4iQ",
                UnionId = "UgIzXXo+Rp3Rqcts7BE08y49Jr6iu6xW4iQ",
                AccountId = "ding1234",
            };
            try
            {
                client.GetUserFollowStatusWithOptions(getUserFollowStatusRequest, getUserFollowStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 响应结果。 |
| status | String | 用户关注服务窗的状态：   - **FOLLOWED**：已关注。 - **UNFOLLOW**：未关注。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "status" : "UNFOLLOW"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.fast | request too fast. | 请求过快被限流。 |
| 400 | illegalRequest | illegal request. | 请求异常。 |
| 400 | illegalParameter.unionId | illegal union id. | unionId不正确。 |
| 400 | illegalRequest.account | illegal account. | 服务窗账号不正确。 |
| 400 | illegalParameter.userId | illegal user id. | userId参数不正确。 |
| 500 | systemError | system error. | 系统处理出错。 |
