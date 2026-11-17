---
title: "获取企业内部网页应用列表"
source_url: "https://open.dingtalk.com/document/development/api-listinnerwebapps"
namespace: "development"
slug: "api-listinnerwebapps"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 应用管理 > 获取企业内部网页应用列表"
doc_id: "rVQcGF1ICO"
updated_at: "2026-10-27 18:04:44"
---

> Source: https://open.dingtalk.com/document/development/api-listinnerwebapps
> Path: 应用开发 / 服务端 API / 钉钉应用 > 应用管理 > 获取企业内部网页应用列表
> Updated: 2026-10-27 18:04:44

# 获取企业内部网页应用列表

查询调用方所属企业的内部应用列表，支持按网页能力筛选，并按需分页返回应用标识、名称、首页地址及已配置的机器人、酷应用等信息。适用于企业同步网页应用清单、汇总应用入口等场景。

## **接口调用说明**

### 调用说明

- 查询访问凭证所属企业的内部应用，不能通过本接口指定其他企业进行查询。
- 查询网页应用时，必须显式传入 `app_type=webApp`（区分大小写）；不传 `app_type` 时，不按网页能力筛选。该参数没有默认值。
- 网页筛选以应用已生效的网页能力配置为准，不按 PC 端和移动端分别筛选。仅添加能力但尚未形成生效配置的应用，可能不在网页结果中。
- 同一应用可以同时配置网页、机器人和酷应用能力，因此网页应用结果中也可能包含 `robotInfo` 或 `coolAppInfo`。
- 网页筛选结果仅覆盖符合条件的有效企业内部应用，不包含第三方应用、快捷链接、工作台及低代码等特殊应用类型。

### 使用场景

- 企业系统同步当前企业的网页应用清单。
- 汇总应用的移动端、PC 端及管理后台入口。
- 按需读取应用已配置的机器人和已发布酷应用信息。

### 分页说明

- 建议显式传入 `offset` 和 `size` 分页查询；返回结果按 `agentId` 降序排列。
- `offset` 表示跳过的符合当前筛选条件的应用数量，从 `0` 开始。`size` 表示本次最多返回数量，取值范围为 `1`～`1000`。
- 只要传入 `offset` 或 `size` 中的任意一个参数，就启用分页；未传 `offset` 时按 `0` 处理，未传 `size` 时按 `100` 处理。
- `offset` 和 `size` 均不传时，不启用分页，返回全部符合条件的应用；应用数量较多时建议分页获取。
- 连续分页时，保持 `app_type` 和 `size` 不变，每次将 `offset` 加上本次实际返回数量。返回数量小于 `size` 或 `appList` 为空数组时，可结束查询。
- 响应中的 `appList` 是本次返回的列表，不提供总数量或下一页游标。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/innerWebApps |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_get\_microapp\_list-企业已安装的应用列表查询权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| app\_type | String | 否 | 应用筛选类型，可选值为 `webApp`（区分大小写），表示仅查询具有已生效网页能力的企业内部应用。  **[!NOTE]**   - 不传时不按网页能力筛选，无默认值。 - 不支持其他取值，也不区分 PC 端与移动端。 |
| offset | Integer | 否 | 跳过的符合当前筛选条件的应用数量，大于或等于 `0` 的整数，从 `0` 开始。  **[!NOTE]**   - 传入 `offset` 或 `size` 任意一个参数时启用分页，未传 `offset` 时按 `0` 处理。 - 两个参数均不传时返回全部符合条件的应用。 |
| size | Integer | 否 | 本次最多返回的应用数量，取值范围为 `1`～`1000`。  **[!NOTE]**   - 传入 `offset` 或 `size` 任意一个参数时启用分页，未传 `size` 时按 `100` 处理。 - 两个参数均不传时返回全部符合条件的应用。 |

### **请求示例**

HTTP

```
GET /v1.0/microApp/innerWebApps?app_type=webApp&offset=0&size=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:YOUR_ACCESS_TOKEN
Content-Type:application/json
```

Java

```
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
        com.aliyun.dingtalkmicro_app_1_0.models.ListInnerWebAppsHeaders listInnerWebAppsHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.ListInnerWebAppsHeaders();
        listInnerWebAppsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.ListInnerWebAppsRequest listInnerWebAppsRequest = new com.aliyun.dingtalkmicro_app_1_0.models.ListInnerWebAppsRequest()
                .setAppType("webApp")
                .setOffset(0)
                .setSize(10);
        try {
            client.listInnerWebAppsWithOptions(listInnerWebAppsRequest, listInnerWebAppsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

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
        list_inner_web_apps_headers = dingtalkmicro_app__1__0_models.ListInnerWebAppsHeaders()
        list_inner_web_apps_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_inner_web_apps_request = dingtalkmicro_app__1__0_models.ListInnerWebAppsRequest(
            app_type='webApp',
            offset=0,
            size=10
        )
        try:
            client.list_inner_web_apps_with_options(list_inner_web_apps_request, list_inner_web_apps_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_inner_web_apps_headers = dingtalkmicro_app__1__0_models.ListInnerWebAppsHeaders()
        list_inner_web_apps_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_inner_web_apps_request = dingtalkmicro_app__1__0_models.ListInnerWebAppsRequest(
            app_type='webApp',
            offset=0,
            size=10
        )
        try:
            await client.list_inner_web_apps_with_options_async(list_inner_web_apps_request, list_inner_web_apps_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\ListInnerWebAppsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\ListInnerWebAppsRequest;
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
        $listInnerWebAppsHeaders = new ListInnerWebAppsHeaders([]);
        $listInnerWebAppsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listInnerWebAppsRequest = new ListInnerWebAppsRequest([
            "appType" => "webApp",
            "offset" => 0,
            "size" => 10
        ]);
        try {
            $client->listInnerWebAppsWithOptions($listInnerWebAppsRequest, $listInnerWebAppsHeaders, new RuntimeOptions([]));
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

  listInnerWebAppsHeaders := &dingtalkmicroapp_1_0.ListInnerWebAppsHeaders{}
  listInnerWebAppsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listInnerWebAppsRequest := &dingtalkmicroapp_1_0.ListInnerWebAppsRequest{
    AppType: tea.String("webApp"),
    Offset: tea.Int32(0),
    Size: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListInnerWebAppsWithOptions(listInnerWebAppsRequest, listInnerWebAppsHeaders, &util.RuntimeOptions{})
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
    let listInnerWebAppsHeaders = new dingtalkmicroApp_1_0.ListInnerWebAppsHeaders({ });
    listInnerWebAppsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listInnerWebAppsRequest = new dingtalkmicroApp_1_0.ListInnerWebAppsRequest({
      appType: 'webApp',
      offset: 0,
      size: 10,
    });
    try {
      await client.listInnerWebAppsWithOptions(listInnerWebAppsRequest, listInnerWebAppsHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListInnerWebAppsHeaders listInnerWebAppsHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListInnerWebAppsHeaders();
            listInnerWebAppsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListInnerWebAppsRequest listInnerWebAppsRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListInnerWebAppsRequest
            {
                AppType = "webApp",
                Offset = 0,
                Size = 10,
            };
            try
            {
                client.ListInnerWebAppsWithOptions(listInnerWebAppsRequest, listInnerWebAppsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| appList | Array | 本次查询返回的应用列表。没有符合条件的应用或分页已结束时返回空数组 `[]`。 |
| agentId | Long | 应用的 `agentId`，用于标识当前企业中的应用。 |
| name | String | 应用名称。 |
| desc | String | 应用描述。 |
| icon | String | 应用图标的 URL。 |
| homepageLink | String | 应用配置的移动端首页地址。  **[!NOTE]**  未配置时可能为空或不返回。 |
| pcHomepageLink | String | 应用配置的 PC 端首页地址。  **[!NOTE]**  未配置时可能为空或不返回。 |
| ompLink | String | 应用配置的管理后台地址。  **[!NOTE]**  未配置时可能为空或不返回。 |
| appId | Long | 第三方应用 ID，企业内部应用返回 `0`。 |
| appStatus | Integer | 应用状态，取值：   - **0**：停用。 - **1**：启用。 - **3**：过期。   本接口查询有效应用，正常返回值为 1。 |
| developType | Integer | 应用开发类型，取值：   - **0**：H5 开发。 - **1**：小程序开发。 - **3**：统一应用开发。   统一应用可配置多种能力，该字段不能单独用于判断是否具有网页能力。 |
| robotInfo | Object | 应用配置的机器人信息。  **[!NOTE]**  未配置时可返回空对象 `{}`。 |
| name | String | 应用所配置机器人的名称。 |
| robotCode | String | 应用所配置机器人的编码。 |
| coolAppInfo | Array | 应用下已发布的酷应用列表。  **[!NOTE]**  未返回时，表示本次响应未包含酷应用信息。 |
| name | String | 已发布酷应用的名称。 |
| coolAppCode | String | 已发布酷应用的编码。 |
| unifiedAppId | String | 统一应用 ID。  **[!NOTE]**  历史应用未关联统一应用时，该字段可能不返回。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "appList" : [ {
    "agentId" : 100001,
    "name" : "示例网页应用",
    "desc" : "企业内部网页应用示例",
    "icon" : "https://example.com/images/app-icon.png",
    "homepageLink" : "https://example.com/app/mobile",
    "pcHomepageLink" : "https://example.com/app/pc",
    "ompLink" : "https://example.com/app/admin",
    "appId" : 0,
    "appStatus" : 1,
    "developType" : 0,
    "robotInfo" : {
      "name" : "示例机器人",
      "robotCode" : "dingexample123456"
    },
    "coolAppInfo" : [ {
      "name" : "示例酷应用",
      "coolAppCode" : "coolapp_example"
    } ],
    "unifiedAppId" : "00000000-0000-4000-8000-000000000001"
  } ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 请求参数不合法 | offset必须为非负整数，size范围为1～1000 |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
