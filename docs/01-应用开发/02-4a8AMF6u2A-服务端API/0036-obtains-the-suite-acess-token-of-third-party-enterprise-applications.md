---
title: "获取第三方企业应用的suiteAccessToken"
source_url: "https://open.dingtalk.com/document/development/obtains-the-suite-acess-token-of-third-party-enterprise-applications"
namespace: "development"
slug: "obtains-the-suite-acess-token-of-third-party-enterprise-applications"
group: "应用开发"
tab: "服务端API"
breadcrumb: "认证与授权 > 访问凭证 > 应用身份凭证 > 获取第三方企业应用的suiteAccessToken"
doc_id: "5dOoWwTh3G"
updated_at: "2026-06-08 12:02:04"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-suite-acess-token-of-third-party-enterprise-applications
> Path: 应用开发 / 服务端API / 认证与授权 > 访问凭证 > 应用身份凭证 > 获取第三方企业应用的suiteAccessToken
> Updated: 2026-06-08 12:02:04

# 获取第三方企业应用的suiteAccessToken

用于获取第三方企业应用的suiteAccessToken。调用时通过 POST 请求提交 suiteKey、suiteSecret、suiteTicket 等业务字段。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/suiteAccessToken |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_base-三方应用开通使用基础权限 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suiteKey | String | 是 | suitefcurkdvkc1nxxxx | 已创建的第三方企业应用的 Cilent ID（原第三方企业应用SuiteKey）。 |
| suiteSecret | String | 是 | y1ie2Rfb54xxxx | 已创建的第三方企业应用的 Cilent Secret（原第三方企业应用SuiteSecret）。 |
| suiteTicket | String | 是 | test | 钉钉开放平台会向应用的回调URL推送的suite\_ticket（约5个小时推送一次），详细内容请参考[套件票据](../04-LFcRvVD08N-事件订阅/0006-event-suite-ticket.md)。 |

### 请求体示例

HTTP

```
POST /v1.0/oauth2/suiteAccessToken HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "suiteKey" : "suitefcurkdvkc1nxxxx",
  "suiteSecret" : "y1ie2Rfb54xxxx",
  "suiteTicket" : "test"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.dingtalkoauth2_1_0.*;
import com.aliyun.dingtalkoauth2_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoauth2_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkoauth2_1_0.Client client = Sample.createClient();
        GetSuiteAccessTokenRequest getSuiteAccessTokenRequest = new GetSuiteAccessTokenRequest()
                .setSuiteKey("suitefcurkdvkc1nxxxx")
                .setSuiteSecret("y1ie2Rfb54xxxx")
                .setSuiteTicket("test");
        try {
            client.getSuiteAccessToken(getSuiteAccessTokenRequest);
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
        get_suite_access_token_request = dingtalkoauth_2__1__0_models.GetSuiteAccessTokenRequest(
            suite_key='suitefcurkdvkc1nxxxx',
            suite_secret='y1ie2Rfb54xxxx',
            suite_ticket='test'
        )
        try:
            client.get_suite_access_token(get_suite_access_token_request)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_suite_access_token_request = dingtalkoauth_2__1__0_models.GetSuiteAccessTokenRequest(
            suite_key='suitefcurkdvkc1nxxxx',
            suite_secret='y1ie2Rfb54xxxx',
            suite_ticket='test'
        )
        try:
            await client.get_suite_access_token_async(get_suite_access_token_request)
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
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetSuiteAccessTokenRequest;

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
        $getSuiteAccessTokenRequest = new GetSuiteAccessTokenRequest([
            "suiteKey" => "suitefcurkdvkc1nxxxx",
            "suiteSecret" => "y1ie2Rfb54xxxx",
            "suiteTicket" => "test"
        ]);
        try {
            $client->getSuiteAccessToken($getSuiteAccessTokenRequest);
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
  dingtalkoauth2_1_0  "github.com/alibabacloud-go/dingtalk/oauth2_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  getSuiteAccessTokenRequest := &dingtalkoauth2_1_0.GetSuiteAccessTokenRequest{
    SuiteKey: tea.String("suitefcurkdvkc1nxxxx"),
    SuiteSecret: tea.String("y1ie2Rfb54xxxx"),
    SuiteTicket: tea.String("test"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSuiteAccessToken(getSuiteAccessTokenRequest)
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
    let getSuiteAccessTokenRequest = new $dingtalkoauth2_1_0.GetSuiteAccessTokenRequest({
      suiteKey: "suitefcurkdvkc1nxxxx",
      suiteSecret: "y1ie2Rfb54xxxx",
      suiteTicket: "test",
    });
    try {
      await client.getSuiteAccessToken(getSuiteAccessTokenRequest);
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
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetSuiteAccessTokenRequest getSuiteAccessTokenRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetSuiteAccessTokenRequest
            {
                SuiteKey = "suitefcurkdvkc1nxxxx",
                SuiteSecret = "y1ie2Rfb54xxxx",
                SuiteTicket = "test",
            };
            try
            {
                client.GetSuiteAccessToken(getSuiteAccessTokenRequest);
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
| accessToken | String | token | 第三方企业应用的凭证，在调用以下接口时会使用：   - [获取授权应用的基本信息](0043-obtains-application-information-of-an-enterprise.md) - [获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md) |
| expireIn | Long | 7200 | 第三方企业应用的凭证过期时间，单位秒。    suiteAccessToken有效期为7200秒，过期之前建议服务端做定时器主动更新，而不是依赖钉钉的定时推送。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "accessToken" : "token",
  "expireIn" : 7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidSuiteTicket | suiteTicket无效 | suiteTicket无效 |
| 400 | invalidClientIdOrSecret | clientId或者clientSecret错误 | clientId或者clientSecret错误 |
