---
title: "获取用户可见的企业应用列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-list-of-enterprise-applications-visible-to-a-user"
namespace: "development"
slug: "obtains-the-list-of-enterprise-applications-visible-to-a-user"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 应用管理 > 获取用户可见的企业应用列表"
doc_id: "6c54nD3SkA"
updated_at: "2026-06-03 11:49:37"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-list-of-enterprise-applications-visible-to-a-user
> Path: 应用开发 / 服务端 API / 钉钉应用 > 应用管理 > 获取用户可见的企业应用列表
> Updated: 2026-06-03 11:49:37

# 获取用户可见的企业应用列表

调用本接口，获取用户可使用的企业应用列表及应用信息，包括应用名称、应用图标、应用访问地址、应用的状态等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/users/{userId}/apps |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_get\_microapp\_list-企业已安装的应用列表查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 用户的userId值。 |

### 请求示例

HTTP

```
GET /v1.0/microApp/users/user123/apps HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.ListUserVilebleAppHeaders listUserVilebleAppHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.ListUserVilebleAppHeaders();
        listUserVilebleAppHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.listUserVilebleAppWithOptions("user123", listUserVilebleAppHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys

from typing import List

from alibabacloud_dingtalk.micro_app_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
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
        list_user_vileble_app_headers = dingtalkmicro_app__1__0_models.ListUserVilebleAppHeaders()
        list_user_vileble_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.list_user_vileble_app_with_options('user123', list_user_vileble_app_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_user_vileble_app_headers = dingtalkmicro_app__1__0_models.ListUserVilebleAppHeaders()
        list_user_vileble_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.list_user_vileble_app_with_options_async('user123', list_user_vileble_app_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\ListUserVilebleAppHeaders;
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
        $listUserVilebleAppHeaders = new ListUserVilebleAppHeaders([]);
        $listUserVilebleAppHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->listUserVilebleAppWithOptions("user123", $listUserVilebleAppHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
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

  listUserVilebleAppHeaders := &dingtalkmicroapp_1_0.ListUserVilebleAppHeaders{}
  listUserVilebleAppHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListUserVilebleAppWithOptions(tea.String("user123"), listUserVilebleAppHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkmicroApp_1_0 = require('@alicloud/dingtalk/microApp_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkmicroApp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let listUserVilebleAppHeaders = new dingtalkmicroApp_1_0.ListUserVilebleAppHeaders({ });
    listUserVilebleAppHeaders.xAcsDingtalkAccessToken = '<your access token>';
    try {
      await client.listUserVilebleAppWithOptions('user123', listUserVilebleAppHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListUserVilebleAppHeaders listUserVilebleAppHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListUserVilebleAppHeaders();
            listUserVilebleAppHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.ListUserVilebleAppWithOptions("user123", listUserVilebleAppHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| appList | Array | 应用列表。 |
| agentId | Long | 应用AgentId。 |
| name | String | 应用名称。 |
| desc | String | 应用描述。 |
| icon | String | 应用图标。 |
| homepageLink | String | 应用移动端首页地址。 |
| pcHomepageLink | String | 应用PC端首页地址。 |
| ompLink | String | 应用管理后台地址。 |
| appId | Long | 应用ID。   - 基础应用，返回应用对应的AppId值。 - 企业自建应用，AppId值是0。 - 第三方企业应用，返回应用对应的AppId值。 |
| appStatus | Integer | 应用状态，取值：   - **0**：停用 - **1**：启用 - **3**：过期 |
| developType | Integer | 应用类型。   - **0**：表示H5微应用。 - **1**：表示小程序。 |
| unifiedAppId | String | 统一应用ID，详情参考[Unified App ID](https://open.dingtalk.com/document/development/basic-concepts-beta#f20a795ad844u)。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "appList" : [ {
    "agentId" : 1,
    "name" : "name",
    "desc" : "desc",
    "icon" : "icon",
    "homepageLink" : "https://www.dingtalk.com",
    "pcHomepageLink" : "https://www.dingtalk.com",
    "ompLink" : "https://www.dingtalk.com",
    "appId" : 111,
    "appStatus" : 1,
    "developType" : 0,
    "unifiedAppId" : "unifiedAppId"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidUserId | 无效的用户id | 无效的用户id |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
