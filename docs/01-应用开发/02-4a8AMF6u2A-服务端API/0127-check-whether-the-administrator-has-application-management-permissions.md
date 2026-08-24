---
title: "查询管理员是否有应用管理权限"
source_url: "https://open.dingtalk.com/document/development/check-whether-the-administrator-has-application-management-permissions"
namespace: "development"
slug: "check-whether-the-administrator-has-application-management-permissions"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 企业管理 > 查询管理员是否有应用管理权限"
doc_id: "IFROzfBJX5"
updated_at: "2026-06-01 16:10:32"
---

> Source: https://open.dingtalk.com/document/development/check-whether-the-administrator-has-application-management-permissions
> Path: 应用开发 / 服务端API / 通讯录管理 > 企业管理 > 查询管理员是否有应用管理权限
> Updated: 2026-06-01 16:10:32

# 查询管理员是否有应用管理权限

调用本接口，用于查询企业管理员是否有应用的管理权限。

## 接口调用说明

例如，产品服务商上架了第三方企业应用，名称为三方ISV小程序。某个测试企业开通了三方ISV小程序，小明是测试企业的管理员。产品服务商调用本接口，可查询小明是否拥有三方ISV小程序应用的管理权限。如图： ![](https://img.alicdn.com/imgextra/i2/O1CN01hIxCzR1OjsgzEugxy_!!6000000001742-2-tps-2788-1328.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/apps/{agentId}/users/{userId}/adminAccess |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | Long | 是 | 授权企业安装三方应用时的agentId，可调用[获取企业开通应用后的授权信息](0045-obtains-the-authorization-information-after-the-enterprise-activates-the-application-1.md)接口获取agentId参数值。 |
| userId | String | 是 | 授权企业管理员userId，可调用[获取管理员列表](0068-query-the-administrator-list.md)接口获取userid参数值。 |

### 请求示例

HTTP

```
GET /v1.0/microApp/apps/111/users/manager1123/adminAccess HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkmicro_app_1_0.*;
import com.aliyun.dingtalkmicro_app_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        GetMicroAppUserAccessHeaders getMicroAppUserAccessHeaders = new GetMicroAppUserAccessHeaders();
        getMicroAppUserAccessHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getMicroAppUserAccessWithOptions("111", "manager1123", getMicroAppUserAccessHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.microApp_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.microApp_1_0 import models as dingtalkmicro_app__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmicroApp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmicroApp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_micro_app_user_access_headers = dingtalkmicro_app__1__0_models.GetMicroAppUserAccessHeaders()
        get_micro_app_user_access_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_micro_app_user_access_with_options('111', 'manager1123', get_micro_app_user_access_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_micro_app_user_access_headers = dingtalkmicro_app__1__0_models.GetMicroAppUserAccessHeaders()
        get_micro_app_user_access_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_micro_app_user_access_with_options_async('111', 'manager1123', get_micro_app_user_access_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\GetMicroAppUserAccessHeaders;
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
        $getMicroAppUserAccessHeaders = new GetMicroAppUserAccessHeaders([]);
        $getMicroAppUserAccessHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getMicroAppUserAccessWithOptions("111", "manager1123", $getMicroAppUserAccessHeaders, new RuntimeOptions([]));
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
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkmicroapp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmicroapp_1_0.Client{}
  _result, _err = dingtalkmicroapp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getMicroAppUserAccessHeaders := &dingtalkmicroapp_1_0.GetMicroAppUserAccessHeaders{}
  getMicroAppUserAccessHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetMicroAppUserAccessWithOptions(tea.String("111"), tea.String("manager1123"), getMicroAppUserAccessHeaders, &util.RuntimeOptions{})
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
import dingtalkmicroApp_1_0, * as $dingtalkmicroApp_1_0 from '@alicloud/dingtalk/microApp_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkmicroApp_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkmicroApp_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getMicroAppUserAccessHeaders = new $dingtalkmicroApp_1_0.GetMicroAppUserAccessHeaders({ });
    getMicroAppUserAccessHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.getMicroAppUserAccessWithOptions("111", "manager1123", getMicroAppUserAccessHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.GetMicroAppUserAccessHeaders getMicroAppUserAccessHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.GetMicroAppUserAccessHeaders();
            getMicroAppUserAccessHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetMicroAppUserAccessWithOptions("111", "manager1123", getMicroAppUserAccessHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkmicro_app__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

using namespace std;

Alibabacloud_Dingtalkmicro_app_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkmicro_app_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkmicro_app_1_0::Client> client = make_shared<Alibabacloud_Dingtalkmicro_app_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkmicro_app_1_0::GetMicroAppUserAccessHeaders> getMicroAppUserAccessHeaders = make_shared<Alibabacloud_Dingtalkmicro_app_1_0::GetMicroAppUserAccessHeaders>();
  getMicroAppUserAccessHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->getMicroAppUserAccessWithOptions(make_shared<string>("111"), make_shared<string>("manager1123"), getMicroAppUserAccessHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Boolean | 结果。   - true：有管理权限。 - false：无管理权限。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidUserId | 无效的userId | 无效的userId |
| 400 | invalidAgentId | 无效的agentId | 不合法的agentId |
| 500 | systemError | 系统繁忙 | 系统繁忙 |
