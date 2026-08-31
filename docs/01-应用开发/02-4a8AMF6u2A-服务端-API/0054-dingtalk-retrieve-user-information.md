---
title: "获取用户通讯录个人信息"
source_url: "https://open.dingtalk.com/document/development/dingtalk-retrieve-user-information"
namespace: "development"
slug: "dingtalk-retrieve-user-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 获取用户通讯录个人信息"
doc_id: "GGQJ9psxRr"
updated_at: "2026-07-30 10:02:44"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-retrieve-user-information
> Path: 应用开发 / 服务端 API / 通讯录管理 > 获取用户通讯录个人信息
> Updated: 2026-07-30 10:02:44

# 获取用户通讯录个人信息

调用本接口获取企业用户通讯录中的个人信息。

## **接口调用说明**

企业内部应用和第三方企业应用在调用该接口前，需要先获取个人用户的accessToken，获取方式请参考[获取登录用户的访问凭证](0029-obtain-identity-credentials.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/users/{unionId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用appType-第三方个人应用 |
| 权限要求 | permission-Contact.User.Read-通讯录个人信息读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端接口的授权凭证。使用个人用户的accessToken，请参考[获取登录用户的访问凭证](0029-obtain-identity-credentials.md)。 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户的unionId。  **[!NOTE]**    如需获取当前授权人的信息，unionId参数可以传me。 |

### **请求示例**

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcontact_1_0.*;
import com.aliyun.dingtalkcontact_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        GetUserHeaders getUserHeaders = new GetUserHeaders();
        getUserHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getUserWithOptions("z21HjQliSzpw0Yxxxx", getUserHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_headers = dingtalkcontact__1__0_models.GetUserHeaders()
        get_user_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_user_with_options('z21HjQliSzpw0Yxxxx', get_user_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_headers = dingtalkcontact__1__0_models.GetUserHeaders()
        get_user_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_user_with_options_async('z21HjQliSzpw0Yxxxx', get_user_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetUserHeaders;
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
        $getUserHeaders = new GetUserHeaders([]);
        $getUserHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getUserWithOptions("z21HjQliSzpw0Yxxxx", $getUserHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUserHeaders := &dingtalkcontact_1_0.GetUserHeaders{}
  getUserHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserWithOptions(tea.String("z21HjQliSzpw0Yxxxx"), getUserHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUserHeaders = new $dingtalkcontact_1_0.GetUserHeaders({ });
    getUserHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.getUserWithOptions("z21HjQliSzpw0Yxxxx", getUserHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetUserHeaders getUserHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetUserHeaders();
            getUserHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetUserWithOptions("z21HjQliSzpw0Yxxxx", getUserHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcontact__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

using namespace std;

Alibabacloud_Dingtalkcontact_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcontact_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcontact_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetUserHeaders> getUserHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetUserHeaders>();
  getUserHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->getUserWithOptions(make_shared<string>("z21HjQliSzpw0Yxxxx"), getUserHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| nick | String | 用户的钉钉昵称。 |
| avatarUrl | String | 头像URL。 |
| mobile | String | 用户的手机号。  **[!NOTE]**     - 第三方企业应用无法获取用户完整手机号，本接口对手机号进行脱敏处理，第三方企业应用获取手机号示例：`155****3240`。 - 如果要获取用户手机号，需要在[钉钉开发者后台](https://open-dev.dingtalk.com/)申请**个人手机号信息**权限，如下图。个人手机号信息 |
| openId | String | 用户的openId。 |
| unionId | String | 用户的unionId。 |
| email | String | 用户的个人邮箱。  **[!NOTE]**    添加个人邮箱。 |
| stateCode | String | 手机号对应的国家号。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nick" : "zhangsan",
  "avatarUrl" : "https://xxx",
  "mobile" : "150xxxx9144",
  "openId" : "123",
  "unionId" : "z21HjQliSzpw0Yxxxx",
  "email" : "zhangsan@alibaba-inc.com",
  "stateCode" : "86"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 404 | invalidParameter.user.notFound | 找不到该用户 | 用户不存在时返回这个错误码 |
