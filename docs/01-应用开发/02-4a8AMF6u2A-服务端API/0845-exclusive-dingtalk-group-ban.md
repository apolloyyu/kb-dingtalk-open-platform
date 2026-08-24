---
title: "企业内部群禁言或解除禁言"
source_url: "https://open.dingtalk.com/document/development/exclusive-dingtalk-group-ban"
namespace: "development"
slug: "exclusive-dingtalk-group-ban"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 企业内部群 > 企业内部群禁言或解除禁言"
doc_id: "Nl0I6BexfV"
updated_at: "2026-06-02 19:18:37"
---

> Source: https://open.dingtalk.com/document/development/exclusive-dingtalk-group-ban
> Path: 应用开发 / 服务端API / 专属钉钉 > 企业内部群 > 企业内部群禁言或解除禁言
> Updated: 2026-06-02 19:18:37

# 企业内部群禁言或解除禁言

设置企业内部群禁言或者解除企业内部群禁言。

## 接口调用说明

例如，某专属钉钉组织，企业内部群cid为cid123，调用本接口可以设置群cid123群禁言或解除禁言。实现效果与以下产品操作类似，拥有**专属安全-群管理**权限的管理员登录[钉钉管理后台](https://oa.dingtalk.com) > 专属钉钉 > 专属安全 > 群管理中查看的信息，可以将未禁言的群设置为禁言，或将已设置禁言的群解除禁言，如图 ![](https://img.alicdn.com/imgextra/i4/O1CN01ulZCX71Er4koEQDOM_!!6000000000404-2-tps-2790-1240.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/enterpriseSecurities/banOrOpenGroupWords |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Group.Write-专属钉钉群写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConverationId | String | 是 | 群ID，获取方式如下   1. 拥有**专属安全-群管理**权限的管理员登录[钉钉管理后台](https://oa.dingtalk.com) > 专属钉钉 > 专属安全 > 群管理中读取，如图。 2. 通过接口获取，可调用[查询企业内部群信息](0844-obtain-group-info.md)接口获取。 |
| banWordsType | Integer | 是 | 操作类型。   - **0**：解除禁言 - **1**：开启禁言 |

### 请求示例

HTTP

```
PUT /v1.0/exclusive/enterpriseSecurities/banOrOpenGroupWords HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e5284fe44e283891a8e94e06696d0643
Content-Type:application/json

{
  "openConverationId" : "ciduWplHYmkD1qCYI8HrMjZVw==",
  "banWordsType" : 0
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        BanOrOpenGroupWordsHeaders banOrOpenGroupWordsHeaders = new BanOrOpenGroupWordsHeaders();
        banOrOpenGroupWordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BanOrOpenGroupWordsRequest banOrOpenGroupWordsRequest = new BanOrOpenGroupWordsRequest()
                .setOpenConverationId("ciduWplHYmkD1qCYI8HrMjZVw==")
                .setBanWordsType(0);
        try {
            client.banOrOpenGroupWordsWithOptions(banOrOpenGroupWordsRequest, banOrOpenGroupWordsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        ban_or_open_group_words_headers = dingtalkexclusive__1__0_models.BanOrOpenGroupWordsHeaders()
        ban_or_open_group_words_headers.x_acs_dingtalk_access_token = '<your access token>'
        ban_or_open_group_words_request = dingtalkexclusive__1__0_models.BanOrOpenGroupWordsRequest(
            open_converation_id='ciduWplHYmkD1qCYI8HrMjZVw==',
            ban_words_type=0
        )
        try:
            client.ban_or_open_group_words_with_options(ban_or_open_group_words_request, ban_or_open_group_words_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        ban_or_open_group_words_headers = dingtalkexclusive__1__0_models.BanOrOpenGroupWordsHeaders()
        ban_or_open_group_words_headers.x_acs_dingtalk_access_token = '<your access token>'
        ban_or_open_group_words_request = dingtalkexclusive__1__0_models.BanOrOpenGroupWordsRequest(
            open_converation_id='ciduWplHYmkD1qCYI8HrMjZVw==',
            ban_words_type=0
        )
        try:
            await client.ban_or_open_group_words_with_options_async(ban_or_open_group_words_request, ban_or_open_group_words_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\BanOrOpenGroupWordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\BanOrOpenGroupWordsRequest;
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
        $banOrOpenGroupWordsHeaders = new BanOrOpenGroupWordsHeaders([]);
        $banOrOpenGroupWordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $banOrOpenGroupWordsRequest = new BanOrOpenGroupWordsRequest([
            "openConverationId" => "ciduWplHYmkD1qCYI8HrMjZVw==",
            "banWordsType" => 0
        ]);
        try {
            $client->banOrOpenGroupWordsWithOptions($banOrOpenGroupWordsRequest, $banOrOpenGroupWordsHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  banOrOpenGroupWordsHeaders := &dingtalkexclusive_1_0.BanOrOpenGroupWordsHeaders{}
  banOrOpenGroupWordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  banOrOpenGroupWordsRequest := &dingtalkexclusive_1_0.BanOrOpenGroupWordsRequest{
    OpenConverationId: tea.String("ciduWplHYmkD1qCYI8HrMjZVw=="),
    BanWordsType: tea.Int32(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BanOrOpenGroupWordsWithOptions(banOrOpenGroupWordsRequest, banOrOpenGroupWordsHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let banOrOpenGroupWordsHeaders = new $dingtalkexclusive_1_0.BanOrOpenGroupWordsHeaders({ });
    banOrOpenGroupWordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let banOrOpenGroupWordsRequest = new $dingtalkexclusive_1_0.BanOrOpenGroupWordsRequest({
      openConverationId: "ciduWplHYmkD1qCYI8HrMjZVw==",
      banWordsType: 0,
    });
    try {
      await client.banOrOpenGroupWordsWithOptions(banOrOpenGroupWordsRequest, banOrOpenGroupWordsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.BanOrOpenGroupWordsHeaders banOrOpenGroupWordsHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.BanOrOpenGroupWordsHeaders();
            banOrOpenGroupWordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.BanOrOpenGroupWordsRequest banOrOpenGroupWordsRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.BanOrOpenGroupWordsRequest
            {
                OpenConverationId = "ciduWplHYmkD1qCYI8HrMjZVw==",
                BanWordsType = 0,
            };
            try
            {
                client.BanOrOpenGroupWordsWithOptions(banOrOpenGroupWordsRequest, banOrOpenGroupWordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkexclusive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkexclusive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkexclusive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkexclusive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::BanOrOpenGroupWordsHeaders> banOrOpenGroupWordsHeaders = make_shared<Alibabacloud_Dingtalkexclusive_1_0::BanOrOpenGroupWordsHeaders>();
  banOrOpenGroupWordsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::BanOrOpenGroupWordsRequest> banOrOpenGroupWordsRequest = make_shared<Alibabacloud_Dingtalkexclusive_1_0::BanOrOpenGroupWordsRequest>(map<string, boost::any>({
    {"openConverationId", boost::any(string("ciduWplHYmkD1qCYI8HrMjZVw=="))},
    {"banWordsType", boost::any(0)}
  }));
  try {
    client->banOrOpenGroupWordsWithOptions(banOrOpenGroupWordsRequest, banOrOpenGroupWordsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 返回码。 |
| cause | String | 结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : "200",
  "cause" : "成功"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | not.inner.group | 当前群不是内部群 | 当前群不是内部群 |
| 400 | illegal.parameter.cid | openConverationId参数错误 | 参数漏填或者格式错误 |
| 400 | illegal.parameter.type | banWordsType参数错误 | 参数漏填或者格式错误 |
| 400 | org.not.match | 群的归属组织与操作传入组织不匹配 | 群的归属组织与操作传入组织不匹配 |
