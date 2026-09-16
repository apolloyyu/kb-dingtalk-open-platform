---
title: "获取企业内部应用的accessToken"
source_url: "https://open.dingtalk.com/document/development/obtain-the-access-token-of-an-internal-app"
namespace: "development"
slug: "obtain-the-access-token-of-an-internal-app"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 访问凭证 > 应用身份凭证 > 获取企业内部应用的accessToken"
doc_id: "yCG0X9Q1im"
updated_at: "2026-08-25 09:36:27"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-access-token-of-an-internal-app
> Path: 应用开发 / 服务端 API / 认证与授权 > 访问凭证 > 应用身份凭证 > 获取企业内部应用的accessToken
> Updated: 2026-08-25 09:36:27

# 获取企业内部应用的accessToken

企业内部应用调用本接口获取访问凭证（accessToken）。在调用钉钉服务端API时，需通过accessToken进行身份鉴权，以确保请求来源合法并具备相应权限。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/accessToken |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| appKey | String | 是 | dingeqqpkv3xxxxxx | 已创建的企业内部应用的 Client ID，获取方式可参考[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)文档说明。 |
| appSecret | String | 是 | GT-lsu-taDAxxxsTsxxxx | 已创建的企业内部应用的 Client Secre ，获取方式可参考[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)文档说明。    请妥善保管Client Secret，避免泄露。 |

### **请求示例**

HTTP

```
POST /v1.0/oauth2/accessToken HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "appKey" : "dingeqqpkv3xxxxxx",
  "appSecret" : "GT-lsu-taDAxxxsTsxxxx"
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
  public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
    com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
    config.protocol = "https";
    config.regionId = "central";
    return new com.aliyun.dingtalkoauth2_1_0.Client(config);
  }

  public static void main(String[] args_) throws Exception {
    java.util.List<String> args = java.util.Arrays.asList(args_);
    com.aliyun.dingtalkoauth2_1_0.Client client = Sample.createClient();
    com.aliyun.dingtalkoauth2_1_0.models.GetAccessTokenRequest getAccessTokenRequest = new com.aliyun.dingtalkoauth2_1_0.models.GetAccessTokenRequest()
      .setAppKey("dingeqqpkv3xxxxxx")
      .setAppSecret("GT-lsu-taDAxxxsTsxxxx");
    try {
      client.getAccessToken(getAccessTokenRequest);
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
    get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
      app_key='dingeqqpkv3xxxxxx',
      app_secret='GT-lsu-taDAxxxsTsxxxx'
    )
    try:
      client.get_access_token(get_access_token_request)
    except Exception as err:
      if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
        # err 中含有 code 和 message 属性，可帮助开发定位问题
        pass

  @staticmethod
  async def main_async(
    args: List[str],
  ) -> None:
    client = Sample.create_client()
    get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
      app_key='dingeqqpkv3xxxxxx',
      app_secret='GT-lsu-taDAxxxsTsxxxx'
    )
    try:
      await client.get_access_token_async(get_access_token_request)
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
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetAccessTokenRequest;

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
        $getAccessTokenRequest = new GetAccessTokenRequest([
            "appKey" => "dingeqqpkv3xxxxxx",
            "appSecret" => "GT-lsu-taDAxxxsTsxxxx"
        ]);
        try {
            $client->getAccessToken($getAccessTokenRequest);
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
  dingtalkoauth2_1_0  "github.com/alibabacloud-go/dingtalk/oauth2_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  getAccessTokenRequest := &dingtalkoauth2_1_0.GetAccessTokenRequest{
    AppKey: tea.String("dingeqqpkv3xxxxxx"),
    AppSecret: tea.String("GT-lsu-taDAxxxsTsxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAccessToken(getAccessTokenRequest)
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
import Util from '@alicloud/tea-util';
import dingtalkoauth2_1_0, * as $dingtalkoauth2_1_0 from '@alicloud/dingtalk/oauth2_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkoauth2_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkoauth2_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getAccessTokenRequest = new $dingtalkoauth2_1_0.GetAccessTokenRequest({
      appKey: "dingeqqpkv3xxxxxx",
      appSecret: "GT-lsu-taDAxxxsTsxxxx",
    });
    try {
      await client.getAccessToken(getAccessTokenRequest);
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
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetAccessTokenRequest getAccessTokenRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetAccessTokenRequest
            {
                AppKey = "dingeqqpkv3xxxxxx",
                AppSecret = "GT-lsu-taDAxxxsTsxxxx",
            };
            try
            {
                client.GetAccessToken(getAccessTokenRequest);
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
| accessToken | String | fw8ef8we8f76e6f7s8dxxxx | 生成的accessToken。    在使用accessToken时，请注意以下几点：   - 开发者应自行缓存accessToken，并根据应用维度进行区分存储，因为每个企业内部应用的accessToken相互独立。 - 不可频繁调用本接口获取凭证，建议结合缓存机制控制调用频次，防止被系统限流。 |
| expireIn | Long | 7200 | accessToken的过期时间，单位秒。    accessToken的有效期为7200秒（2小时），有效期内重复获取会返回相同结果并自动续期，过期后获取会返回新的accessToken。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "accessToken" : "fw8ef8we8f76e6f7s8dxxxx",
  "expireIn" : 7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidClientIdOrSecret | 无效的clientId或者clientSecret | 无效的clientId或者clientSecret |
