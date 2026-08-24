---
title: "获取专属存储文件路径"
source_url: "https://open.dingtalk.com/document/development/api-getprivatestorefilepath"
namespace: "development"
slug: "api-getprivatestorefilepath"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 文件 > 获取专属存储文件路径"
doc_id: "9UqpCLY83d"
updated_at: "2026-06-02 19:17:34"
---

> Source: https://open.dingtalk.com/document/development/api-getprivatestorefilepath
> Path: 应用开发 / 服务端API / 专属钉钉 > 文件 > 获取专属存储文件路径
> Updated: 2026-06-02 19:17:34

# 获取专属存储文件路径

调用本接口，根据 spaceId 和 dentryId 获取专属存储文件路径。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/privateStores/filePaths/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.PrivateFile.ReadWrite-专属钉钉专属存储读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | Long | 是 | 文件spaceId |
| dentryId | Long | 是 | 文件dentryId |

### 请求示例

HTTP

```
POST /v1.0/exclusive/privateStores/filePaths/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token1234
Content-Type:application/json

{
  "spaceId" : 1234,
  "dentryId" : 1234
}
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.GetPrivateStoreFilePathHeaders getPrivateStoreFilePathHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetPrivateStoreFilePathHeaders();
        getPrivateStoreFilePathHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetPrivateStoreFilePathRequest getPrivateStoreFilePathRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetPrivateStoreFilePathRequest()
                .setSpaceId(1234L)
                .setDentryId(1234L);
        try {
            client.getPrivateStoreFilePathWithOptions(getPrivateStoreFilePathRequest, getPrivateStoreFilePathHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_private_store_file_path_headers = dingtalkexclusive__1__0_models.GetPrivateStoreFilePathHeaders()
        get_private_store_file_path_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_private_store_file_path_request = dingtalkexclusive__1__0_models.GetPrivateStoreFilePathRequest(
            space_id=1234,
            dentry_id=1234
        )
        try:
            client.get_private_store_file_path_with_options(get_private_store_file_path_request, get_private_store_file_path_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_private_store_file_path_headers = dingtalkexclusive__1__0_models.GetPrivateStoreFilePathHeaders()
        get_private_store_file_path_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_private_store_file_path_request = dingtalkexclusive__1__0_models.GetPrivateStoreFilePathRequest(
            space_id=1234,
            dentry_id=1234
        )
        try:
            await client.get_private_store_file_path_with_options_async(get_private_store_file_path_request, get_private_store_file_path_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetPrivateStoreFilePathHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetPrivateStoreFilePathRequest;
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
        $getPrivateStoreFilePathHeaders = new GetPrivateStoreFilePathHeaders([]);
        $getPrivateStoreFilePathHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getPrivateStoreFilePathRequest = new GetPrivateStoreFilePathRequest([
            "spaceId" => 1234,
            "dentryId" => 1234
        ]);
        try {
            $client->getPrivateStoreFilePathWithOptions($getPrivateStoreFilePathRequest, $getPrivateStoreFilePathHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
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

  getPrivateStoreFilePathHeaders := &dingtalkexclusive_1_0.GetPrivateStoreFilePathHeaders{}
  getPrivateStoreFilePathHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getPrivateStoreFilePathRequest := &dingtalkexclusive_1_0.GetPrivateStoreFilePathRequest{
    SpaceId: tea.Int64(1234),
    DentryId: tea.Int64(1234),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetPrivateStoreFilePathWithOptions(getPrivateStoreFilePathRequest, getPrivateStoreFilePathHeaders, &util.RuntimeOptions{})
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
const dingtalkexclusive_1_0 = require('@alicloud/dingtalk/exclusive_1_0');
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
    return new dingtalkexclusive_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getPrivateStoreFilePathHeaders = new dingtalkexclusive_1_0.GetPrivateStoreFilePathHeaders({ });
    getPrivateStoreFilePathHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getPrivateStoreFilePathRequest = new dingtalkexclusive_1_0.GetPrivateStoreFilePathRequest({
      spaceId: 1234,
      dentryId: 1234,
    });
    try {
      await client.getPrivateStoreFilePathWithOptions(getPrivateStoreFilePathRequest, getPrivateStoreFilePathHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPrivateStoreFilePathHeaders getPrivateStoreFilePathHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPrivateStoreFilePathHeaders();
            getPrivateStoreFilePathHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPrivateStoreFilePathRequest getPrivateStoreFilePathRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPrivateStoreFilePathRequest
            {
                SpaceId = 1234,
                DentryId = 1234,
            };
            try
            {
                client.GetPrivateStoreFilePathWithOptions(getPrivateStoreFilePathRequest, getPrivateStoreFilePathHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| filePath | String | 专属存储文件路径 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "filePath" : "yundisk0/#iAcdjjdsao"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.invalid | 参数不合法 | 参数不合法 |
| 400 | org.no.function | 企业未开启相关功能 | 企业未开启相关功能 |
| 400 | privatefile.not.exist | 专属存储文件不存在 | 专属存储文件不存在 |
