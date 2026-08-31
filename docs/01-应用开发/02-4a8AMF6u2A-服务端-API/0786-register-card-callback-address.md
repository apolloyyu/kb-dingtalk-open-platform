---
title: "注册卡片回调地址"
source_url: "https://open.dingtalk.com/document/development/register-card-callback-address"
namespace: "development"
slug: "register-card-callback-address"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > 注册卡片回调地址"
doc_id: "fMpsu2f4po"
updated_at: "2026-06-04 10:50:04"
---

> Source: https://open.dingtalk.com/document/development/register-card-callback-address
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > 注册卡片回调地址
> Updated: 2026-06-04 10:50:04

# 注册卡片回调地址

调用本接口注册卡片回调地址。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/callbacks/register |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Instance.Write-互动卡片实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| callbackRouteKey | String | 是 | 回调地址的路由Key。  **[!NOTE]**    一个`callbackRouteKey` 仅可映射一个`callbackUrl`。 |
| callbackUrl | String | 是 | 接受动态卡片回调的 URL 地址。  **[!NOTE]**    必须是公网可访问的 URL。 |
| apiSecret | String | 否 | 加密密钥用于校验来源。 |
| forceUpdate | Boolean | 否 | 是否强制覆盖更新现有的 callbackRouteKey：   - true：覆盖 - false：不覆盖   **[!NOTE]**    强制覆盖更新回调地址，会影响到其他使用该 callbackRouteKey 的卡片。 |

### 请求示例

HTTP

```
POST /v1.0/card/callbacks/register HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "callbackRouteKey" : "example-route-key",
  "callbackUrl" : "https://example/callback",
  "apiSecret" : "example-secret",
  "forceUpdate" : false
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
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.RegisterCallbackHeaders registerCallbackHeaders = new com.aliyun.dingtalkcard_1_0.models.RegisterCallbackHeaders();
        registerCallbackHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.RegisterCallbackRequest registerCallbackRequest = new com.aliyun.dingtalkcard_1_0.models.RegisterCallbackRequest()
                .setCallbackRouteKey("example-route-key")
                .setCallbackUrl("https://example/callback")
                .setApiSecret("example-secret")
                .setForceUpdate(false);
        try {
            client.registerCallbackWithOptions(registerCallbackRequest, registerCallbackHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_callback_headers = dingtalkcard__1__0_models.RegisterCallbackHeaders()
        register_callback_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_callback_request = dingtalkcard__1__0_models.RegisterCallbackRequest(
            callback_route_key='example-route-key',
            callback_url='https://example/callback',
            api_secret='example-secret',
            force_update=False
        )
        try:
            client.register_callback_with_options(register_callback_request, register_callback_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_callback_headers = dingtalkcard__1__0_models.RegisterCallbackHeaders()
        register_callback_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_callback_request = dingtalkcard__1__0_models.RegisterCallbackRequest(
            callback_route_key='example-route-key',
            callback_url='https://example/callback',
            api_secret='example-secret',
            force_update=False
        )
        try:
            await client.register_callback_with_options_async(register_callback_request, register_callback_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\RegisterCallbackHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\RegisterCallbackRequest;
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
        $registerCallbackHeaders = new RegisterCallbackHeaders([]);
        $registerCallbackHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $registerCallbackRequest = new RegisterCallbackRequest([
            "callbackRouteKey" => "example-route-key",
            "callbackUrl" => "https://example/callback",
            "apiSecret" => "example-secret",
            "forceUpdate" => false
        ]);
        try {
            $client->registerCallbackWithOptions($registerCallbackRequest, $registerCallbackHeaders, new RuntimeOptions([]));
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
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  registerCallbackHeaders := &dingtalkcard_1_0.RegisterCallbackHeaders{}
  registerCallbackHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  registerCallbackRequest := &dingtalkcard_1_0.RegisterCallbackRequest{
    CallbackRouteKey: tea.String("example-route-key"),
    CallbackUrl: tea.String("https://example/callback"),
    ApiSecret: tea.String("example-secret"),
    ForceUpdate: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RegisterCallbackWithOptions(registerCallbackRequest, registerCallbackHeaders, &util.RuntimeOptions{})
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
import dingtalkcard_1_0, * as $dingtalkcard_1_0 from '@alicloud/dingtalk/card_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcard_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcard_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let registerCallbackHeaders = new $dingtalkcard_1_0.RegisterCallbackHeaders({ });
    registerCallbackHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let registerCallbackRequest = new $dingtalkcard_1_0.RegisterCallbackRequest({
      callbackRouteKey: "example-route-key",
      callbackUrl: "https://example/callback",
      apiSecret: "example-secret",
      forceUpdate: false,
    });
    try {
      await client.registerCallbackWithOptions(registerCallbackRequest, registerCallbackHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.RegisterCallbackHeaders registerCallbackHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.RegisterCallbackHeaders();
            registerCallbackHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.RegisterCallbackRequest registerCallbackRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.RegisterCallbackRequest
            {
                CallbackRouteKey = "example-route-key",
                CallbackUrl = "https://example/callback",
                ApiSecret = "example-secret",
                ForceUpdate = false,
            };
            try
            {
                client.RegisterCallbackWithOptions(registerCallbackRequest, registerCallbackHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 请求是否成功。 |
| result | Object | 注册回调地址的结果。 |
| callbackUrl | String | 回调 URL 地址。 |
| apiSecret | String | 加密密钥。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "callbackUrl" : "https://example/callback",
    "apiSecret" : "example-secret"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.callbackRouteKeyEmpty | param.callbackRouteKeyEmpty | 回调 RouteKey 为空 |
| 400 | param.callbackUrlEmpty | param.callbackUrlEmpty | 回调 Url 为空 |
| 400 | system.updateCallbackFailed | system.updateCallbackFailed | 更新回调 RouteKey 失败 |
| 400 | param.empty | param.empty | 入参为空 |
| 500 | param.callbackRouteKeyExist | param.callbackRouteKeyExist | 回调 RouteKey 已存在 |
| 500 | system.busy | system.busy | 系统繁忙 |
