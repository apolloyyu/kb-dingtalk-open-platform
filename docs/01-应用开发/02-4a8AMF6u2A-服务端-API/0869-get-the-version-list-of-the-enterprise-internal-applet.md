---
title: "获取企业内部小程序的版本列表"
source_url: "https://open.dingtalk.com/document/development/get-the-version-list-of-the-enterprise-internal-applet"
namespace: "development"
slug: "get-the-version-list-of-the-enterprise-internal-applet"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 版本管理 > 获取企业内部小程序的版本列表"
doc_id: "LobzbfESdO"
updated_at: "2026-07-14 09:22:21"
---

> Source: https://open.dingtalk.com/document/development/get-the-version-list-of-the-enterprise-internal-applet
> Path: 应用开发 / 服务端 API / 钉钉应用 > 版本管理 > 获取企业内部小程序的版本列表
> Updated: 2026-07-14 09:22:21

# 获取企业内部小程序的版本列表

调用本接口，获取指定企业内部小程序的所有版本信息，包括版本ID、版本号、版本类型、创建时间、更新时间等。

## **接口调用说明**

仅企业内部自建小程序支持调用该接口获取版本数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/versions |
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
| agentId | Long | 是 | 应用AgentId。  image |

### 请求示例

HTTP

```
GET /v1.0/microApp/innerMiniApps/1/versions HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a582bed908a53b819163a7ef8*****ed
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
        com.aliyun.dingtalkmicro_app_1_0.models.ListInnerAppVersionHeaders listInnerAppVersionHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.ListInnerAppVersionHeaders();
        listInnerAppVersionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.listInnerAppVersionWithOptions("1", listInnerAppVersionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_inner_app_version_headers = dingtalkmicro_app__1__0_models.ListInnerAppVersionHeaders()
        list_inner_app_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.list_inner_app_version_with_options('1', list_inner_app_version_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_inner_app_version_headers = dingtalkmicro_app__1__0_models.ListInnerAppVersionHeaders()
        list_inner_app_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.list_inner_app_version_with_options_async('1', list_inner_app_version_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\ListInnerAppVersionHeaders;
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
        $listInnerAppVersionHeaders = new ListInnerAppVersionHeaders([]);
        $listInnerAppVersionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->listInnerAppVersionWithOptions("1", $listInnerAppVersionHeaders, new RuntimeOptions([]));
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

  listInnerAppVersionHeaders := &dingtalkmicroapp_1_0.ListInnerAppVersionHeaders{}
  listInnerAppVersionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListInnerAppVersionWithOptions(tea.String("1"), listInnerAppVersionHeaders, &util.RuntimeOptions{})
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
    let listInnerAppVersionHeaders = new dingtalkmicroApp_1_0.ListInnerAppVersionHeaders({ });
    listInnerAppVersionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    try {
      await client.listInnerAppVersionWithOptions('1', listInnerAppVersionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListInnerAppVersionHeaders listInnerAppVersionHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.ListInnerAppVersionHeaders();
            listInnerAppVersionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.ListInnerAppVersionWithOptions("1", listInnerAppVersionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| appVersionList | Array | 企业内部小程序版本号列表。 |
| appVersionId | Long | 小程序版本id，用于发布和回滚小程序版本唯一标识。 |
| miniAppId | String | 小程序id。 |
| appVersion | String | 小程序版本号。 |
| appVersionType | Integer | 小程序版本类型，取值：   - **0**：开发版本 - **2**：正式版本 - **3**：体验版本 |
| miniAppOnPc | Boolean | 是否支持PC端打开小程序，取值：   - **false**：只支持移动端 - **true**：既支持移动端又支持PC端 |
| createTime | String | 小程序版本创建时间，格式:yyyy-MM-dd HH:mm:ss。 |
| modifyTime | String | 小程序版本号更新时间，格式:yyyy-MM-dd HH:mm:ss。 |
| entranceLink | String | 企业内部小程序版本的跳转链接。      目前只会返回**体验版**小程序的跳转链接。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "appVersionList" : [ {
    "appVersionId" : 1,
    "miniAppId" : "1",
    "appVersion" : "0.0.1",
    "appVersionType" : 0,
    "miniAppOnPc" : false,
    "createTime" : "2023-01-01 00:00:00",
    "modifyTime" : "2023-01-01 00:00:00",
    "entranceLink" : "dingtalk://dingtalkclient/action/open_micro_app?corpId=****&miniAppId=****&source=trial&version=***&agentId=***&pVersion=1&packageType=1"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | appTypeNotSupport | 只支持企业自建小程序调用 | 只支持企业自建小程序调用 |
| 400 | preCheckError | 前置校验失败: %s | 前置校验失败 |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
