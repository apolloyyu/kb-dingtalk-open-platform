---
title: "获取工作台插件权限点"
source_url: "https://open.dingtalk.com/document/development/obtain-the-permissions-of-the-workbench-plug-in"
namespace: "development"
slug: "obtain-the-permissions-of-the-workbench-plug-in"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉工作台 > 获取工作台插件权限点"
doc_id: "ME725ZfY5b"
updated_at: "2025-09-11 21:03:44"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-permissions-of-the-workbench-plug-in
> Path: 应用开发 / 服务端API / 钉钉工作台 > 获取工作台插件权限点
> Updated: 2025-09-11 21:03:44

# 获取工作台插件权限点

调用本接口可以获取工作台插件对应的权限点。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workbench/plugins/permissions |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Workbench.Component.Read-工作台组件信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，请参考[调用工作台 API](https://open.dingtalk.com/document/dingstart/workbench)。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| miniAppId | String | 否 | 插件ID。 |

### 请求示例

HTTP

```
GET /v1.0/workbench/plugins/permissions?miniAppId=2021001xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2021001xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkworkbench_1_0.*;
import com.aliyun.dingtalkworkbench_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkworkbench_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkbench_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkbench_1_0.Client client = Sample.createClient();
        GetPluginPermissionPointHeaders getPluginPermissionPointHeaders = new GetPluginPermissionPointHeaders();
        getPluginPermissionPointHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetPluginPermissionPointRequest getPluginPermissionPointRequest = new GetPluginPermissionPointRequest()
                .setMiniAppId("2021001xxx");
        try {
            client.getPluginPermissionPointWithOptions(getPluginPermissionPointRequest, getPluginPermissionPointHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.workbench_1_0.client import Client as dingtalkworkbench_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workbench_1_0 import models as dingtalkworkbench__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkbench_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkbench_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_plugin_permission_point_headers = dingtalkworkbench__1__0_models.GetPluginPermissionPointHeaders()
        get_plugin_permission_point_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_plugin_permission_point_request = dingtalkworkbench__1__0_models.GetPluginPermissionPointRequest(
            mini_app_id='2021001xxx'
        )
        try:
            client.get_plugin_permission_point_with_options(get_plugin_permission_point_request, get_plugin_permission_point_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_plugin_permission_point_headers = dingtalkworkbench__1__0_models.GetPluginPermissionPointHeaders()
        get_plugin_permission_point_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_plugin_permission_point_request = dingtalkworkbench__1__0_models.GetPluginPermissionPointRequest(
            mini_app_id='2021001xxx'
        )
        try:
            await client.get_plugin_permission_point_with_options_async(get_plugin_permission_point_request, get_plugin_permission_point_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Models\GetPluginPermissionPointHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Models\GetPluginPermissionPointRequest;
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
        $getPluginPermissionPointHeaders = new GetPluginPermissionPointHeaders([]);
        $getPluginPermissionPointHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getPluginPermissionPointRequest = new GetPluginPermissionPointRequest([
            "miniAppId" => "2021001xxx"
        ]);
        try {
            $client->getPluginPermissionPointWithOptions($getPluginPermissionPointRequest, $getPluginPermissionPointHeaders, new RuntimeOptions([]));
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
  dingtalkworkbench_1_0  "github.com/alibabacloud-go/dingtalk/workbench_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkworkbench_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkbench_1_0.Client{}
  _result, _err = dingtalkworkbench_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getPluginPermissionPointHeaders := &dingtalkworkbench_1_0.GetPluginPermissionPointHeaders{}
  getPluginPermissionPointHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getPluginPermissionPointRequest := &dingtalkworkbench_1_0.GetPluginPermissionPointRequest{
    MiniAppId: tea.String("2021001xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetPluginPermissionPointWithOptions(getPluginPermissionPointRequest, getPluginPermissionPointHeaders, &util.RuntimeOptions{})
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
import dingtalkworkbench_1_0, * as $dingtalkworkbench_1_0 from '@alicloud/dingtalk/workbench_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkbench_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkbench_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getPluginPermissionPointHeaders = new $dingtalkworkbench_1_0.GetPluginPermissionPointHeaders({ });
    getPluginPermissionPointHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getPluginPermissionPointRequest = new $dingtalkworkbench_1_0.GetPluginPermissionPointRequest({
      miniAppId: "2021001xxx",
    });
    try {
      await client.getPluginPermissionPointWithOptions(getPluginPermissionPointRequest, getPluginPermissionPointHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkbench_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.GetPluginPermissionPointHeaders getPluginPermissionPointHeaders = new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.GetPluginPermissionPointHeaders();
            getPluginPermissionPointHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.GetPluginPermissionPointRequest getPluginPermissionPointRequest = new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.GetPluginPermissionPointRequest
            {
                MiniAppId = "2021001xxx",
            };
            try
            {
                client.GetPluginPermissionPointWithOptions(getPluginPermissionPointRequest, getPluginPermissionPointHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkworkbench__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkworkbench_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkworkbench_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkworkbench_1_0::Client> client = make_shared<Alibabacloud_Dingtalkworkbench_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkworkbench_1_0::GetPluginPermissionPointHeaders> getPluginPermissionPointHeaders = make_shared<Alibabacloud_Dingtalkworkbench_1_0::GetPluginPermissionPointHeaders>();
  getPluginPermissionPointHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkworkbench_1_0::GetPluginPermissionPointRequest> getPluginPermissionPointRequest = make_shared<Alibabacloud_Dingtalkworkbench_1_0::GetPluginPermissionPointRequest>(map<string, boost::any>({
    {"miniAppId", boost::any(string("2021001xxx"))}
  }));
  try {
    client->getPluginPermissionPointWithOptions(getPluginPermissionPointRequest, getPluginPermissionPointHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| permissionPointList | Array of String | 插件权限点列表。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "permissionPointList" : [ "setClipboard" ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.param.empty | 入参为空 | 入参为空 |
| 400 | corpId.illegal | 所在组织没有对应插件的权限 | 所在组织没有对应插件的权限 |
| 400 | miniAppId.illegal | appId对应插件不存在 | appId对应插件不存在 |
| 500 | system.error | 系统错误 | 系统错误 |
