---
title: "获取用户登录凭证"
source_url: "https://open.dingtalk.com/document/development/obtains-the-user-login-credential-of-the-third-party-system-of"
namespace: "development"
slug: "obtains-the-user-login-credential-of-the-third-party-system-of"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 小蜜客服 > 获取用户登录凭证"
doc_id: "WbXA9ZWlz7"
updated_at: "2025-09-08 19:06:30"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-user-login-credential-of-the-third-party-system-of
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 小蜜客服 > 获取用户登录凭证
> Updated: 2025-09-08 19:06:30

# 获取用户登录凭证

调用本接口获取用户的登录凭证，在小蜜客服提供的网页渠道中接入三方业务系统时需要使用该凭证获取用户登录状态。

> **[!NOTE]**
>
> - 确保调用本接口前充分了解小蜜客服产品的收费方式和[价格](https://www.yuque.com/dingdingxiaomikefu/cdvg5o/ptd0qr)。
> - 只有开通购买过小蜜客服对应收费版本才支持调用本接口，如有需要请先加入小蜜客服服务群联系相关客服。
> - 接口详细使用方法，请参考 [获取网页渠道三方系统用户登录凭证](https://www.yuque.com/dingdingxiaomikefu/cdvg5o/iugtax)。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 小蜜客服智能客服数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingmi_1.0%23GetWebChannelUserToken) |
| 第三方企业应用 | 暂不支持 | 小蜜客服智能客服数据管理权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 小蜜客服智能客服数据管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/dingmi/webChannels/userTokens HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "source" : Long,
  "nick" : "String",
  "foreignId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| source | Long | 是 | 调用方在小蜜客服平台申请的业务账号体系的id。 |
| nick | String | 是 | 登录用户在业务账号体系内的昵称。 |
| foreignId | String | 是 | 登录用户在业务账号体系内的用户id。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | String | token值，用于小蜜客服提供的网页渠道中接入三方业务系统获取自己的用户登录状态。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/dingmi/webChannels/userTokens HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6edfgcxxxx
Content-Type:application/json

{
  "source" : 123,
  "nick" : "客户abc",
  "foreignId" : "123abc"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdingmi_1_0.*;
import com.aliyun.dingtalkdingmi_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdingmi_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdingmi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdingmi_1_0.Client client = Sample.createClient();
        GetWebChannelUserTokenHeaders getWebChannelUserTokenHeaders = new GetWebChannelUserTokenHeaders();
        getWebChannelUserTokenHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetWebChannelUserTokenRequest getWebChannelUserTokenRequest = new GetWebChannelUserTokenRequest()
                .setSource(123L)
                .setNick("客户abc")
                .setForeignId("123abc");
        try {
            client.getWebChannelUserTokenWithOptions(getWebChannelUserTokenRequest, getWebChannelUserTokenHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.dingmi_1_0.client import Client as dingtalkdingmi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dingmi_1_0 import models as dingtalkdingmi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdingmi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdingmi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_web_channel_user_token_headers = dingtalkdingmi__1__0_models.GetWebChannelUserTokenHeaders()
        get_web_channel_user_token_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_web_channel_user_token_request = dingtalkdingmi__1__0_models.GetWebChannelUserTokenRequest(
            source=123,
            nick='客户abc',
            foreign_id='123abc'
        )
        try:
            client.get_web_channel_user_token_with_options(get_web_channel_user_token_request, get_web_channel_user_token_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_web_channel_user_token_headers = dingtalkdingmi__1__0_models.GetWebChannelUserTokenHeaders()
        get_web_channel_user_token_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_web_channel_user_token_request = dingtalkdingmi__1__0_models.GetWebChannelUserTokenRequest(
            source=123,
            nick='客户abc',
            foreign_id='123abc'
        )
        try:
            await client.get_web_channel_user_token_with_options_async(get_web_channel_user_token_request, get_web_channel_user_token_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\GetWebChannelUserTokenHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\GetWebChannelUserTokenRequest;
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
        $getWebChannelUserTokenHeaders = new GetWebChannelUserTokenHeaders([]);
        $getWebChannelUserTokenHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getWebChannelUserTokenRequest = new GetWebChannelUserTokenRequest([
            "source" => 123,
            "nick" => "客户abc",
            "foreignId" => "123abc"
        ]);
        try {
            $client->getWebChannelUserTokenWithOptions($getWebChannelUserTokenRequest, $getWebChannelUserTokenHeaders, new RuntimeOptions([]));
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
  dingtalkdingmi_1_0  "github.com/alibabacloud-go/dingtalk/dingmi_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdingmi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdingmi_1_0.Client{}
  _result, _err = dingtalkdingmi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getWebChannelUserTokenHeaders := &dingtalkdingmi_1_0.GetWebChannelUserTokenHeaders{}
  getWebChannelUserTokenHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getWebChannelUserTokenRequest := &dingtalkdingmi_1_0.GetWebChannelUserTokenRequest{
    Source: tea.Int64(123),
    Nick: tea.String("客户abc"),
    ForeignId: tea.String("123abc"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetWebChannelUserTokenWithOptions(getWebChannelUserTokenRequest, getWebChannelUserTokenHeaders, &util.RuntimeOptions{})
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
import dingtalkdingmi_1_0, * as $dingtalkdingmi_1_0 from '@alicloud/dingtalk/dingmi_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdingmi_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdingmi_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getWebChannelUserTokenHeaders = new $dingtalkdingmi_1_0.GetWebChannelUserTokenHeaders({ });
    getWebChannelUserTokenHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getWebChannelUserTokenRequest = new $dingtalkdingmi_1_0.GetWebChannelUserTokenRequest({
      source: 123,
      nick: "客户abc",
      foreignId: "123abc",
    });
    try {
      await client.getWebChannelUserTokenWithOptions(getWebChannelUserTokenRequest, getWebChannelUserTokenHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetWebChannelUserTokenHeaders getWebChannelUserTokenHeaders = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetWebChannelUserTokenHeaders();
            getWebChannelUserTokenHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetWebChannelUserTokenRequest getWebChannelUserTokenRequest = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetWebChannelUserTokenRequest
            {
                Source = 123,
                Nick = "客户abc",
                ForeignId = "123abc",
            };
            try
            {
                client.GetWebChannelUserTokenWithOptions(getWebChannelUserTokenRequest, getWebChannelUserTokenHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdingmi__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdingmi_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdingmi_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdingmi_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::GetWebChannelUserTokenHeaders> getWebChannelUserTokenHeaders = make_shared<Alibabacloud_Dingtalkdingmi_1_0::GetWebChannelUserTokenHeaders>();
  getWebChannelUserTokenHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::GetWebChannelUserTokenRequest> getWebChannelUserTokenRequest = make_shared<Alibabacloud_Dingtalkdingmi_1_0::GetWebChannelUserTokenRequest>(map<string, boost::any>({
    {"source", boost::any(123)},
    {"nick", boost::any(string("客户abc"))},
    {"foreignId", boost::any(string("123abc"))}
  }));
  try {
    client->getWebChannelUserTokenWithOptions(getWebChannelUserTokenRequest, getWebChannelUserTokenHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : "ding123"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | 参数错误 | 接口参数错误 |
| 500 | system.error | 系统错误:%s | 系统错误 |
