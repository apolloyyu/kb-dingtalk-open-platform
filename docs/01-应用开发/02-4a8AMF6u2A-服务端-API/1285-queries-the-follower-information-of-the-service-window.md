---
title: "获取关注服务窗用户信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-follower-information-of-the-service-window"
namespace: "development"
slug: "queries-the-follower-information-of-the-service-window"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 服务窗 > 获取关注服务窗用户信息"
doc_id: "L6CfG9lFWM"
updated_at: "2026-06-05 15:36:42"
---

> Source: https://open.dingtalk.com/document/development/queries-the-follower-information-of-the-service-window
> Path: 应用开发 / 服务端 API / 更多开放 > 服务窗 > 获取关注服务窗用户信息
> Updated: 2026-06-05 15:36:42

# 获取关注服务窗用户信息

调用本接口，获取关注服务窗用户的基本信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/link/followers/infos |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-OfficialAccount.Contact.Read-服务窗联系人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 关注服务窗用户的userId，可调用[批量获取关注服务窗用户信息](1284-obtains-the-follower-information-from-the-service-window.md)获得userId参数值。  **[!NOTE]**     - 服务窗应用场景下，该参数必填，不能使用unionId。 - 非服务窗应用场景下，该参数和unionId任选其一。 |
| unionId | String | 否 | 关注服务窗用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取获取。  **[!NOTE]**     - 服务窗应用场景下，该参数不传。 - 非服务窗应用场景下，该参数和unionId任选其一。 |
| accountId | String | 否 | 服务窗账号ID，通过[获取企业下服务窗列表](1282-queries-the-list-of-services-under-an-enterprise.md)接口获得。  **[!NOTE]**     - 服务窗应用场景下，该参数不传，否则会报错非法请求。 - 非服务窗应用场景下，该参数必填，否则会报错非法服务窗账号。 |

### 请求示例

HTTP

```
GET /v1.0/link/followers/infos?userId=Rpxxxxx&unionId=UgIzxxxxx&accountId=ding1234 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
        com.aliyun.dingtalklink_1_0.models.GetFollowerInfoHeaders getFollowerInfoHeaders = new com.aliyun.dingtalklink_1_0.models.GetFollowerInfoHeaders();
        getFollowerInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalklink_1_0.models.GetFollowerInfoRequest getFollowerInfoRequest = new com.aliyun.dingtalklink_1_0.models.GetFollowerInfoRequest()
                .setUserId("Rpxxxxx")
                .setUnionId("UgIzxxxxx")
                .setAccountId("ding1234");
        try {
            client.getFollowerInfoWithOptions(getFollowerInfoRequest, getFollowerInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_follower_info_headers = dingtalklink__1__0_models.GetFollowerInfoHeaders()
        get_follower_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_follower_info_request = dingtalklink__1__0_models.GetFollowerInfoRequest(
            user_id='Rpxxxxx',
            union_id='UgIzxxxxx',
            account_id='ding1234'
        )
        try:
            client.get_follower_info_with_options(get_follower_info_request, get_follower_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_follower_info_headers = dingtalklink__1__0_models.GetFollowerInfoHeaders()
        get_follower_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_follower_info_request = dingtalklink__1__0_models.GetFollowerInfoRequest(
            user_id='Rpxxxxx',
            union_id='UgIzxxxxx',
            account_id='ding1234'
        )
        try:
            await client.get_follower_info_with_options_async(get_follower_info_request, get_follower_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Models\GetFollowerInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlink_1_0\Models\GetFollowerInfoRequest;
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
        $getFollowerInfoHeaders = new GetFollowerInfoHeaders([]);
        $getFollowerInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFollowerInfoRequest = new GetFollowerInfoRequest([
            "userId" => "Rpxxxxx",
            "unionId" => "UgIzxxxxx",
            "accountId" => "ding1234"
        ]);
        try {
            $client->getFollowerInfoWithOptions($getFollowerInfoRequest, $getFollowerInfoHeaders, new RuntimeOptions([]));
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

  getFollowerInfoHeaders := &dingtalklink_1_0.GetFollowerInfoHeaders{}
  getFollowerInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFollowerInfoRequest := &dingtalklink_1_0.GetFollowerInfoRequest{
    UserId: tea.String("Rpxxxxx"),
    UnionId: tea.String("UgIzxxxxx"),
    AccountId: tea.String("ding1234"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFollowerInfoWithOptions(getFollowerInfoRequest, getFollowerInfoHeaders, &util.RuntimeOptions{})
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
    let getFollowerInfoHeaders = new $dingtalklink_1_0.GetFollowerInfoHeaders({ });
    getFollowerInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getFollowerInfoRequest = new $dingtalklink_1_0.GetFollowerInfoRequest({
      userId: "Rpxxxxx",
      unionId: "UgIzxxxxx",
      accountId: "ding1234",
    });
    try {
      await client.getFollowerInfoWithOptions(getFollowerInfoRequest, getFollowerInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetFollowerInfoHeaders getFollowerInfoHeaders = new AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetFollowerInfoHeaders();
            getFollowerInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetFollowerInfoRequest getFollowerInfoRequest = new AlibabaCloud.SDK.Dingtalklink_1_0.Models.GetFollowerInfoRequest
            {
                UserId = "Rpxxxxx",
                UnionId = "UgIzxxxxx",
                AccountId = "ding1234",
            };
            try
            {
                client.GetFollowerInfoWithOptions(getFollowerInfoRequest, getFollowerInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求ID。 |
| result | Object | 响应结果。 |
| user | Object | 关注服务窗的用户详情。 |
| userId | String | 用户userId。 |
| name | String | 用户姓名。 |
| timestamp | String | 关注时间戳，单位毫秒，可能为空。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "request-id-qwe",
  "result" : {
    "user" : {
      "userId" : "userId",
      "name" : "小钉",
      "timestamp" : "1661918406748"
    }
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
| 400 | illegalRequest.followerNotExist | follower not existed. | 根据传入的unionId或userId未未询到对应的关注人信息。 |
| 500 | systemError | system error. | 系统处理出错。 |
