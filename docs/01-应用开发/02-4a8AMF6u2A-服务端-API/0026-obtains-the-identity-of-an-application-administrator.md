---
title: "获取应用管理后台免登的用户信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-identity-of-an-application-administrator"
namespace: "development"
slug: "obtains-the-identity-of-an-application-administrator"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 获取应用管理后台免登的用户信息"
doc_id: "1wYLAZ8PbB"
updated_at: "2026-04-29 22:27:35"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-identity-of-an-application-administrator
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 获取应用管理后台免登的用户信息
> Updated: 2026-04-29 22:27:35

# 获取应用管理后台免登的用户信息

在应用管理后台免登场景中，需要本接口通过获取到的免登授权码code和获取到的应用后台免登的access\_token来换取应用管理员的身份信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/ssoUserInfo |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_omp\_sso\_userinfo-企业OA后台免登访问权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | tokenxxxx | 调用该接口的访问凭证，这里需要使用微应用后台免登的access\_token，可以通过调用[获取微应用后台免登的accessToken](0025-obtain-the-access-token-of-the-micro-application-background-without-log-on.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| code | String | 是 | tokenxxxx20260429\_Hangzhou | 临时授权码，管理员在钉钉管理后台，跳转到应用管理页面时，该授权码会附带在URL中。 |

### **请求示例**

curl

```
curl -X GET 'https://api.dingtalk.com/v1.0/oauth2/ssoUserInfo' \
  -H 'x-acs-dingtalk-access-token: tokenxxxx' \
  -d '{"code": "tokenxxxx20260429_Hangzhou"}'
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
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
        GetSsoUserInfoHeaders getSsoUserInfoHeaders = new GetSsoUserInfoHeaders();
        getSsoUserInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetSsoUserInfoRequest getSsoUserInfoRequest = new GetSsoUserInfoRequest()
                .setCode("tokenxxxx");
        try {
            client.getSsoUserInfoWithOptions(getSsoUserInfoRequest, getSsoUserInfoHeaders, new RuntimeOptions());
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
from alibabacloud_tea_util import models as util_models
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
        get_sso_user_info_headers = dingtalkoauth_2__1__0_models.GetSsoUserInfoHeaders()
        get_sso_user_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_sso_user_info_request = dingtalkoauth_2__1__0_models.GetSsoUserInfoRequest(
            code='tokenxxxx'
        )
        try:
            client.get_sso_user_info_with_options(get_sso_user_info_request, get_sso_user_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_sso_user_info_headers = dingtalkoauth_2__1__0_models.GetSsoUserInfoHeaders()
        get_sso_user_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_sso_user_info_request = dingtalkoauth_2__1__0_models.GetSsoUserInfoRequest(
            code='tokenxxxx'
        )
        try:
            await client.get_sso_user_info_with_options_async(get_sso_user_info_request, get_sso_user_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetSsoUserInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetSsoUserInfoRequest;
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
        $getSsoUserInfoHeaders = new GetSsoUserInfoHeaders([]);
        $getSsoUserInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSsoUserInfoRequest = new GetSsoUserInfoRequest([
            "code" => "tokenxxxx"
        ]);
        try {
            $client->getSsoUserInfoWithOptions($getSsoUserInfoRequest, $getSsoUserInfoHeaders, new RuntimeOptions([]));
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

  getSsoUserInfoHeaders := &dingtalkoauth2_1_0.GetSsoUserInfoHeaders{}
  getSsoUserInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSsoUserInfoRequest := &dingtalkoauth2_1_0.GetSsoUserInfoRequest{
    Code: tea.String("tokenxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSsoUserInfoWithOptions(getSsoUserInfoRequest, getSsoUserInfoHeaders, &util.RuntimeOptions{})
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
    let getSsoUserInfoHeaders = new $dingtalkoauth2_1_0.GetSsoUserInfoHeaders({ });
    getSsoUserInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getSsoUserInfoRequest = new $dingtalkoauth2_1_0.GetSsoUserInfoRequest({
      code: "tokenxxxx",
    });
    try {
      await client.getSsoUserInfoWithOptions(getSsoUserInfoRequest, getSsoUserInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetSsoUserInfoHeaders getSsoUserInfoHeaders = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetSsoUserInfoHeaders();
            getSsoUserInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetSsoUserInfoRequest getSsoUserInfoRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetSsoUserInfoRequest
            {
                Code = "tokenxxxx",
            };
            try
            {
                client.GetSsoUserInfoWithOptions(getSsoUserInfoRequest, getSsoUserInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkoauth2_1_0::GetSsoUserInfoHeaders> getSsoUserInfoHeaders = make_shared<Alibabacloud_Dingtalkoauth2_1_0::GetSsoUserInfoHeaders>();
  getSsoUserInfoHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkoauth2_1_0::GetSsoUserInfoRequest> getSsoUserInfoRequest = make_shared<Alibabacloud_Dingtalkoauth2_1_0::GetSsoUserInfoRequest>(map<string, boost::any>({
    {"code", boost::any(string("tokenxxxx"))}
  }));
  try {
    client->getSsoUserInfoWithOptions(getSsoUserInfoRequest, getSsoUserInfoHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| corpId | String | corpxxx | 微应用免登用户所在企业的corpId。 |
| corpName | String | 免登测试企业 | 微应用免登用户所在企业名称。 |
| userId | String | manager7777 | 用户userid。 |
| email | String | xxxx@xxxx | 用户邮箱。 |
| userName | String | 测试人员 | 用户名称。 |
| avatar | String | https://xxxx | 用户头像链接。 |
| isAdmin | Boolean | true | 是否为企业管理员。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "corpId" : "corpxxx",
  "corpName" : "免登测试企业",
  "userId" : "manager7777",
  "email" : "xxxx@xxxx",
  "userName" : "测试人员",
  "avatar" : "https://xxxx",
  "isAdmin" : true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidCode | 无效的授权码 | 无效的授权码 |
| 400 | invalidToken | 无效的token | 无效的token |
