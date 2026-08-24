---
title: "获取应用的 Access Token"
source_url: "https://open.dingtalk.com/document/development/api-gettoken"
namespace: "development"
slug: "api-gettoken"
group: "应用开发"
tab: "服务端API"
breadcrumb: "认证与授权 > 访问凭证 > 应用身份凭证 > 获取应用的 Access Token"
doc_id: "Py2b80tmOx"
updated_at: "2026-06-08 12:02:05"
---

> Source: https://open.dingtalk.com/document/development/api-gettoken
> Path: 应用开发 / 服务端API / 认证与授权 > 访问凭证 > 应用身份凭证 > 获取应用的 Access Token
> Updated: 2026-06-08 12:02:05

# 获取应用的 Access Token

如果你的应用需要使用应用权限点，无论是企业内部应用还是第三方企业应用，都应通过本接口获取应用级别的 Access Token。该凭证用于调用钉钉开放平台中受权限保护的 API 接口。

## **接口调用说明**

此接口用于获取企业内部应用或第三方企业应用调用API所需的Access Token，适用于所有需要通过应用身份鉴权调用钉钉开放平台接口的场景。

如果你之前使用：

- 企业内部应用：调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口，获取企业调用接口的凭证信息。
- 第三方企业应用：调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口，获取第三方应用授权企业调用接口的凭证信息。

现在这两种场景统一为一个接口，无需区分应用类型，直接调用本接口即可获取 AccessToken 调用应用权限接口。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/{corpId}/token |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| corpId | String | 是 | ding9f\*\*\*\*41 | 组织ID，应用运行在哪个组织就填写哪个组织的 corpId：   - 企业内部应用：填写本企业 corpId。 - 第三方企业应用：填写开通应用的授权企业的 corpId。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| client\_id | String | 是 | suite123 | 应用的 ClientID。 |
| client\_secret | String | 是 | \*\*\*\*\*\*\*\* | 应用的 ClientSecret。 |
| grant\_type | String | 是 | client\_credentials | 授权类型：client\_credentials |

### **请求示例**

HTTP

```
POST /v1.0/oauth2/ding9f****41/token HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "client_id" : "suite123",
  "client_secret" : "********",
  "grant_type" : "client_credentials"
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
    public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoauth2_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkoauth2_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkoauth2_1_0.models.GetTokenRequest getTokenRequest = new com.aliyun.dingtalkoauth2_1_0.models.GetTokenRequest()
                .setClientId("suite123")
                .setClientSecret("********")
                .setGrantType("client_credentials");
        try {
            client.getToken("ding9f****41", getTokenRequest);
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

from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkoauth2_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkoauth2_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_token_request = dingtalkoauth_2__1__0_models.GetTokenRequest(
            client_id='suite123',
            client_secret='********',
            grant_type='client_credentials'
        )
        try:
            client.get_token('ding9f****41', get_token_request)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_token_request = dingtalkoauth_2__1__0_models.GetTokenRequest(
            client_id='suite123',
            client_secret='********',
            grant_type='client_credentials'
        )
        try:
            await client.get_token_async('ding9f****41', get_token_request)
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

use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetTokenRequest;

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
        $getTokenRequest = new GetTokenRequest([
            "clientId" => "suite123",
            "clientSecret" => "********",
            "grantType" => "client_credentials"
        ]);
        try {
            $client->getToken("ding9f****41", $getTokenRequest);
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
  dingtalkoauth2_1_0  "github.com/alibabacloud-go/dingtalk/oauth2_1_0"
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
func CreateClient () (_result *dingtalkoauth2_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkoauth2_1_0.Client{}
  _result, _err = dingtalkoauth2_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getTokenRequest := &dingtalkoauth2_1_0.GetTokenRequest{
    ClientId: tea.String("suite123"),
    ClientSecret: tea.String("********"),
    GrantType: tea.String("client_credentials"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetToken(tea.String("ding9f****41"), getTokenRequest)
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
const dingtalkoauth2_1_0 = require('@alicloud/dingtalk/oauth2_1_0');
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
    return new dingtalkoauth2_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getTokenRequest = new dingtalkoauth2_1_0.GetTokenRequest({
      clientId: 'suite123',
      clientSecret: '********',
      grantType: 'client_credentials',
    });
    try {
      await client.getToken('ding9f****41', getTokenRequest);
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
        public static AlibabaCloud.SDK.Dingtalkoauth2_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetTokenRequest getTokenRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetTokenRequest
            {
                ClientId = "suite123",
                ClientSecret = "********",
                GrantType = "client_credentials",
            };
            try
            {
                client.GetToken("ding9f****41", getTokenRequest);
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

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| access\_token | String | 2bf\*\*\*\*\*\*9be361a5084f1e2b8 | 访问凭证。 |
| expires\_in | Integer | 7200 | 访问凭证有效的时长，单位秒。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "access_token" : "2bf******9be361a5084f1e2b8",
  "expires_in" : 7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.client | invalid.client | 无效的ClientID或ClientSecret |
| 400 | unsupported.grant.type | unsupported.grant.type | 不支持此授权类型，请检查授权类型参数 |
| 401 | unauthorized.client | unauthorized.client | 应用未被授权 |
| 500 | server.error | server.error | 服务器意外错误 |
