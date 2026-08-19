---
title: "获取用户关注服务窗状态"
source_url: "https://open.dingtalk.com/document/development/third-party-enterprise-application-obtains-user-attention-service-window-status"
namespace: "development"
slug: "third-party-enterprise-application-obtains-user-attention-service-window-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 服务窗 > 获取用户关注服务窗状态"
doc_id: "l7rFDEADoB"
updated_at: "2025-09-11 21:03:50"
---

> Source: https://open.dingtalk.com/document/development/third-party-enterprise-application-obtains-user-attention-service-window-status
> Path: 应用开发 / 服务端API / 更多开放 > 服务窗 > 获取用户关注服务窗状态
> Updated: 2025-09-11 21:03:50

# 获取用户关注服务窗状态

第三方企业应用可通过本接口查询用户是否关注本企业的某一服务窗。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/link/isv/followers/statuses |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-OfficialAccount.Meta.Read-ISV调用服务窗基础数据需要的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 否 | 待查询的服务窗关注者unionId，可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取返回参数`unionid`字段值。 |
| accountId | String | 是 | 服务窗账号ID，通过[获取企业下服务窗列表](1282-queries-the-list-of-services-under-an-enterprise.md)接口获得。 |

### 请求示例

HTTP

```
GET /v1.0/link/isv/followers/statuses?unionId=UgIz*******W4iQ&accountId=ding1234 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:3b89df4dfaaccd
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
        com.aliyun.dingtalklink_1_0.models.QueryUserFollowStatusHeaders queryUserFollowStatusHeaders = new com.aliyun.dingtalklink_1_0.models.QueryUserFollowStatusHeaders();
        queryUserFollowStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalklink_1_0.models.QueryUserFollowStatusRequest queryUserFollowStatusRequest = new com.aliyun.dingtalklink_1_0.models.QueryUserFollowStatusRequest()
                .setUnionId("UgIz*******W4iQ")
                .setAccountId("ding1234");
        try {
            client.queryUserFollowStatusWithOptions(queryUserFollowStatusRequest, queryUserFollowStatusHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_user_follow_status_headers = dingtalklink__1__0_models.QueryUserFollowStatusHeaders()
        query_user_follow_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_follow_status_request = dingtalklink__1__0_models.QueryUserFollowStatusRequest(
            union_id='UgIz*******W4iQ',
            account_id='ding1234'
        )
        try:
            client.query_user_follow_status_with_options(query_user_follow_status_request, query_user_follow_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_user_follow_status_headers = dingtalklink__1__0_models.QueryUserFollowStatusHeaders()
        query_user_follow_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_follow_status_request = dingtalklink__1__0_models.QueryUserFollowStatusRequest(
            union_id='UgIz*******W4iQ',
            account_id='ding1234'
        )
        try:
            await client.query_user_follow_status_with_options_async(query_user_follow_status_request, query_user_follow_status_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Models\QueryUserFollowStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Models\QueryUserFollowStatusRequest;
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
        $queryUserFollowStatusHeaders = new QueryUserFollowStatusHeaders([]);
        $queryUserFollowStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryUserFollowStatusRequest = new QueryUserFollowStatusRequest([
            "unionId" => "UgIz*******W4iQ",
            "accountId" => "ding1234"
        ]);
        try {
            $client->queryUserFollowStatusWithOptions($queryUserFollowStatusRequest, $queryUserFollowStatusHeaders, new RuntimeOptions([]));
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

  queryUserFollowStatusHeaders := &dingtalklink_1_0.QueryUserFollowStatusHeaders{}
  queryUserFollowStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryUserFollowStatusRequest := &dingtalklink_1_0.QueryUserFollowStatusRequest{
    UnionId: tea.String("UgIz*******W4iQ"),
    AccountId: tea.String("ding1234"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryUserFollowStatusWithOptions(queryUserFollowStatusRequest, queryUserFollowStatusHeaders, &util.RuntimeOptions{})
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
    let queryUserFollowStatusHeaders = new $dingtalklink_1_0.QueryUserFollowStatusHeaders({ });
    queryUserFollowStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryUserFollowStatusRequest = new $dingtalklink_1_0.QueryUserFollowStatusRequest({
      unionId: "UgIz*******W4iQ",
      accountId: "ding1234",
    });
    try {
      await client.queryUserFollowStatusWithOptions(queryUserFollowStatusRequest, queryUserFollowStatusHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalklink_1_0.Models.QueryUserFollowStatusHeaders queryUserFollowStatusHeaders = new AlibabaCloud.SDK.Dingtalklink_1_0.Models.QueryUserFollowStatusHeaders();
            queryUserFollowStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklink_1_0.Models.QueryUserFollowStatusRequest queryUserFollowStatusRequest = new AlibabaCloud.SDK.Dingtalklink_1_0.Models.QueryUserFollowStatusRequest
            {
                UnionId = "UgIz*******W4iQ",
                AccountId = "ding1234",
            };
            try
            {
                client.QueryUserFollowStatusWithOptions(queryUserFollowStatusRequest, queryUserFollowStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| status | String | 用户关注服务窗的状态：   - **FOLLOWED**：已关注 - **UNFOLLOW**：未关注 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "status" : "FOLLOWED"
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
