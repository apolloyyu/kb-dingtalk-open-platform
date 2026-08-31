---
title: "获取用户token"
source_url: "https://open.dingtalk.com/document/development/obtain-user-token"
namespace: "development"
slug: "obtain-user-token"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 访问凭证 > 用户个人身份凭证 > 获取用户token"
doc_id: "9O6rh2mMjw"
updated_at: "2026-06-30 16:50:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-user-token
> Path: 应用开发 / 服务端 API / 认证与授权 > 访问凭证 > 用户个人身份凭证 > 获取用户token
> Updated: 2026-06-30 16:50:33

# 获取用户token

通过此接口获取用户级别的访问令牌（access token），支持 OAuth 2.0 授权码模式和刷新令牌模式，适用于需要以用户身份调用钉钉开放平台 API 的第三方个人应用。

## 使用场景

该接口用于获取用户的`accessToken`，是实现用户身份认证的关键步骤。常见使用场景包括：

- 用户登录后，通过授权码（`code`）换取有效的访问凭证。
- 在`accessToken`过期前，使用`refreshToken`自动续期，避免频繁重新授权。
- 第三方企业应用集成钉钉统一登录体系，实现单点登录（SSO）。
- 企业应用在后台服务中代表用户调用受保护的 API 接口。

开发者应妥善管理`accessToken`的生命周期，建议在本地缓存并设置自动刷新机制，确保调用稳定性。

> **[!NOTE]**
>
> 在使用accessToken时，请注意：
>
> - `accessToken`的有效期为7200秒（2小时），有效期内重复获取将返回相同结果并自动续期；过期后获取会返回新的`accessToken`。
> - 每个应用的`accessToken`相互独立，缓存时需按应用维度进行存储，防止混淆。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/userAccessToken |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用appType-第三方个人应用 |
| 权限要求 | permission-open\_app\_api\_base-获取钉钉开放接口用户访问凭证的基础权限 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| clientId | String | 是 | dingxxx | 应用id。可使用扫码登录应用或者第三方个人小程序的appId。   - 企业内部应用传应用的**AppKey** - 第三方企业应用传应用的**SuiteKey** - 第三方个人应用传应用的**AppId** |
| clientSecret | String | 是 | 1234 | 应用密钥。   - 企业内部应用传应用的**AppSecret** - 第三方企业应用传应用的**SuiteSecret** - 第三方个人应用传应用的**AppSecret** |
| code | String | 否 | abcd | OAuth 2.0 临时授权码，第三方企业应用需要[接入统一授权套件](0010-unified-licensing-suite-sdk.md)/[获取登录用户的访问凭证](0029-obtain-identity-credentials.md)，获取临时授权码authCode。 |
| refreshToken | String | 否 | abcd | OAuth 2.0 刷新令牌，从上一次接口返回结果中获取。有效期为 30 天。 |
| grantType | String | 是 | authorization\_code | - 如果使用授权码换token：传`authorization_code`，此时必须填写`code`参数。 - 使用刷新 token 换新 token：传`refresh_token`，此时必须填写`refreshToken`参数。 |

### **请求示例**

curl

```
curl -X POST 'https://api.dingtalk.com/v1.0/oauth2/userAccessToken' \
  -H 'Content-Type: application/json' \
  -d '{
    "clientId": "dingxxx",
    "clientSecret": "1234",
    "code": "abcd",
    "refreshToken": "abcd",
    "grantType": "authorization_code"
  }'
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
        GetUserTokenRequest getUserTokenRequest = new GetUserTokenRequest()
                .setClientId("dingxxx")
                .setClientSecret("1234")
                .setCode("abcd")
                .setRefreshToken("abcd")
                .setGrantType("authorization_code");
        try {
            client.getUserToken(getUserTokenRequest);
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
        get_user_token_request = dingtalkoauth_2__1__0_models.GetUserTokenRequest(
            client_id='dingxxx',
            client_secret='1234',
            code='abcd',
            refresh_token='abcd',
            grant_type='authorization_code'
        )
        try:
            client.get_user_token(get_user_token_request)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_token_request = dingtalkoauth_2__1__0_models.GetUserTokenRequest(
            client_id='dingxxx',
            client_secret='1234',
            code='abcd',
            refresh_token='abcd',
            grant_type='authorization_code'
        )
        try:
            await client.get_user_token_async(get_user_token_request)
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
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetUserTokenRequest;

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
        $getUserTokenRequest = new GetUserTokenRequest([
            "clientId" => "dingxxx",
            "clientSecret" => "1234",
            "code" => "abcd",
            "refreshToken" => "abcd",
            "grantType" => "authorization_code"
        ]);
        try {
            $client->getUserToken($getUserTokenRequest);
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

  getUserTokenRequest := &dingtalkoauth2_1_0.GetUserTokenRequest{
    ClientId: tea.String("dingxxx"),
    ClientSecret: tea.String("1234"),
    Code: tea.String("abcd"),
    RefreshToken: tea.String("abcd"),
    GrantType: tea.String("authorization_code"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserToken(getUserTokenRequest)
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
    let getUserTokenRequest = new $dingtalkoauth2_1_0.GetUserTokenRequest({
      clientId: "dingxxx",
      clientSecret: "1234",
      code: "abcd",
      refreshToken: "abcd",
      grantType: "authorization_code",
    });
    try {
      await client.getUserToken(getUserTokenRequest);
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
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetUserTokenRequest getUserTokenRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetUserTokenRequest
            {
                ClientId = "dingxxx",
                ClientSecret = "1234",
                Code = "abcd",
                RefreshToken = "abcd",
                GrantType = "authorization_code",
            };
            try
            {
                client.GetUserToken(getUserTokenRequest);
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkoauth_2__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkoauth2_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkoauth2_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkoauth2_1_0::Client> client = make_shared<Alibabacloud_Dingtalkoauth2_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkoauth2_1_0::GetUserTokenRequest> getUserTokenRequest = make_shared<Alibabacloud_Dingtalkoauth2_1_0::GetUserTokenRequest>(map<string, boost::any>({
    {"clientId", boost::any(string("dingxxx"))},
    {"clientSecret", boost::any(string("1234"))},
    {"code", boost::any(string("abcd"))},
    {"refreshToken", boost::any(string("abcd"))},
    {"grantType", boost::any(string("authorization_code"))}
  }));
  try {
    client->getUserToken(getUserTokenRequest);
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| accessToken | String | abcd | 生成的accessToken，用于后续 API 调用的身份验证。 |
| refreshToken | String | abcd | 生成的refresh\_token。可以使用此刷新token，定期的获取用户的accessToken |
| expireIn | Long | 7200 | 超时时间，单位秒。 |
| corpId | String | corpxxxx | 所选企业corpId。 |

### **响应示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "accessToken" : "abcd",
  "refreshToken" : "abcd",
  "expireIn" : 7200,
  "corpId" : "corpxxxx"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
