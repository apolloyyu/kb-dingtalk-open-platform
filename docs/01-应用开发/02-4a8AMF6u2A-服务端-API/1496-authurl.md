---
title: "获取授权的页面地址"
source_url: "https://open.dingtalk.com/document/development/authurl"
namespace: "development"
slug: "authurl"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 鉴权 > 获取授权的页面地址"
doc_id: "IQ4NPdJxy5"
updated_at: "2026-08-25 09:37:25"
---

> Source: https://open.dingtalk.com/document/development/authurl
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > e签宝 1.0 > 鉴权 > 获取授权的页面地址
> Updated: 2026-08-25 09:37:25

# 获取授权的页面地址

获取企业授权的页面地址，企业授权使用e签宝提供的功能。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取授权的页面地址](1072-obtain-the-address-of-the-authorized-page.md)接口，已接入用户不受影响。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/esign/auths/url |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 不支持新增 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| redirectUrl | String | 否 | 获取到的重定向地址。  地址后会携带授权结果，例如：`status=SUCCESS&taskid=AUTH-AB312C2CA3EC4876BAC10FB112C22348`其中：   - **status**：表示状态，`SUCCESS`为成功，`FAIL`为失败。 - **taskid**：表示任务id。 |

### **请求示例**

HTTP

```
POST /v1.0/esign/auths/url HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxxxxx
Content-Type:application/json

{
  "redirectUrl" : "http://ddxxx.com"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_1_0.*;
import com.aliyun.dingtalkesign_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_1_0.Client client = Sample.createClient();
        AuthUrlHeaders authUrlHeaders = new AuthUrlHeaders();
        authUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AuthUrlRequest authUrlRequest = new AuthUrlRequest()
                .setRedirectUrl("http://ddxxx.com");
        try {
            client.authUrlWithOptions(authUrlRequest, authUrlHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_1_0.client import Client as dingtalkesign_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        auth_url_headers = dingtalkesign__1__0_models.AuthUrlHeaders()
        auth_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        auth_url_request = dingtalkesign__1__0_models.AuthUrlRequest(
            redirect_url='http://ddxxx.com'
        )
        try:
            client.auth_url_with_options(auth_url_request, auth_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        auth_url_headers = dingtalkesign__1__0_models.AuthUrlHeaders()
        auth_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        auth_url_request = dingtalkesign__1__0_models.AuthUrlRequest(
            redirect_url='http://ddxxx.com'
        )
        try:
            await client.auth_url_with_options_async(auth_url_request, auth_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\AuthUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\AuthUrlRequest;
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
        $authUrlHeaders = new AuthUrlHeaders([]);
        $authUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $authUrlRequest = new AuthUrlRequest([
            "redirectUrl" => "http://ddxxx.com"
        ]);
        try {
            $client->authUrlWithOptions($authUrlRequest, $authUrlHeaders, new RuntimeOptions([]));
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
  dingtalkesign_1_0  ""github.com/alibabacloud-go/dingtalk/esign_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_1_0.Client{}
  _result, _err = dingtalkesign_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  authUrlHeaders := &dingtalkesign_1_0.AuthUrlHeaders{}
  authUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  authUrlRequest := &dingtalkesign_1_0.AuthUrlRequest{
    RedirectUrl: tea.String("http://ddxxx.com"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AuthUrlWithOptions(authUrlRequest, authUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_1_0, * as $dingtalkesign_1_0 from '"@alicloud/dingtalk/esign_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let authUrlHeaders = new $dingtalkesign_1_0.AuthUrlHeaders({ });
    authUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let authUrlRequest = new $dingtalkesign_1_0.AuthUrlRequest({
      redirectUrl: "http://ddxxx.com",
    });
    try {
      await client.authUrlWithOptions(authUrlRequest, authUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.AuthUrlHeaders authUrlHeaders = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.AuthUrlHeaders();
            authUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.AuthUrlRequest authUrlRequest = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.AuthUrlRequest
            {
                RedirectUrl = "http://ddxxx.com",
            };
            try
            {
                client.AuthUrlWithOptions(authUrlRequest, authUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::AuthUrlHeaders> authUrlHeaders = make_shared<Alibabacloud_Dingtalkesign_1_0::AuthUrlHeaders>();
  authUrlHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::AuthUrlRequest> authUrlRequest = make_shared<Alibabacloud_Dingtalkesign_1_0::AuthUrlRequest>(map<string, boost::any>({
    {"redirectUrl", boost::any(string("http://ddxxx.com"))}
  }));
  try {
    client->authUrlWithOptions(authUrlRequest, authUrlHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| data | Object | 返回结果。 |
| taskId | String | 任务ID。 |
| mobileUrl | String | 授权手机地址。 |
| pcUrl | String | 授权PC地址。 |
| code | Integer | 返回码。 |
| message | String | 返回码描述。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : {
    "taskId" : "123",
    "mobileUrl" : "https://aaa.com",
    "pcUrl" : "https://aaa.com"
  },
  "code" : 0,
  "message" : "成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.invalidAguemnts | 参数错误:%s | 参数错误 |
