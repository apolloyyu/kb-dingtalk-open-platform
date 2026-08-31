---
title: "获取群存储空间信息"
source_url: "https://open.dingtalk.com/document/development/obtain-group-storage-space-information"
namespace: "development"
slug: "obtain-group-storage-space-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 群文件 > 获取群存储空间信息"
doc_id: "9wzsNj8pi8"
updated_at: "2026-07-14 09:21:52"
---

> Source: https://open.dingtalk.com/document/development/obtain-group-storage-space-information
> Path: 应用开发 / 服务端 API / 文档/文件 > 群文件 > 获取群存储空间信息
> Updated: 2026-07-14 09:21:52

# 获取群存储空间信息

调用本接口，可获取某个指定群的存储空间信息，包括群存储空间的ID、群存储空间创建的时间和修改时间等。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/convFile/conversations/spaces/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ConvFile.Space.Read-群文件空间读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 会话openConversationId，可调用[创建群](https://open.dingtalk.com/document/development/create-group-session)接口获取openConversationId参数值。 |

### 请求示例

HTTP

```
POST /v1.0/convFile/conversations/spaces/query?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "openConversationId" : "cid9FTRQSLo+sKxxxx"
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
    public static com.aliyun.dingtalkconv_file_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconv_file_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconv_file_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconv_file_1_0.models.GetSpaceHeaders getSpaceHeaders = new com.aliyun.dingtalkconv_file_1_0.models.GetSpaceHeaders();
        getSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconv_file_1_0.models.GetSpaceRequest getSpaceRequest = new com.aliyun.dingtalkconv_file_1_0.models.GetSpaceRequest()
                .setUnionId("chyxxxxx")
                .setOpenConversationId("cid9FTRQSLo+sKxxxx");
        try {
            client.getSpaceWithOptions(getSpaceRequest, getSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.conv_file_1_0.client import Client as dingtalkconvFile_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.conv_file_1_0 import models as dingtalkconv_file__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconvFile_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconvFile_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_space_headers = dingtalkconv_file__1__0_models.GetSpaceHeaders()
        get_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_space_request = dingtalkconv_file__1__0_models.GetSpaceRequest(
            union_id='chyxxxxx',
            open_conversation_id='cid9FTRQSLo+sKxxxx'
        )
        try:
            client.get_space_with_options(get_space_request, get_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_space_headers = dingtalkconv_file__1__0_models.GetSpaceHeaders()
        get_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_space_request = dingtalkconv_file__1__0_models.GetSpaceRequest(
            union_id='chyxxxxx',
            open_conversation_id='cid9FTRQSLo+sKxxxx'
        )
        try:
            await client.get_space_with_options_async(get_space_request, get_space_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconv_file_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconv_file_1_0\Models\GetSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconv_file_1_0\Models\GetSpaceRequest;
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
        $getSpaceHeaders = new GetSpaceHeaders([]);
        $getSpaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSpaceRequest = new GetSpaceRequest([
            "unionId" => "chyxxxxx",
            "openConversationId" => "cid9FTRQSLo+sKxxxx"
        ]);
        try {
            $client->getSpaceWithOptions($getSpaceRequest, $getSpaceHeaders, new RuntimeOptions([]));
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
  dingtalkconvfile_1_0  "github.com/alibabacloud-go/dingtalk/convFile_1_0"
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
func CreateClient () (_result *dingtalkconvfile_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconvfile_1_0.Client{}
  _result, _err = dingtalkconvfile_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getSpaceHeaders := &dingtalkconvfile_1_0.GetSpaceHeaders{}
  getSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSpaceRequest := &dingtalkconvfile_1_0.GetSpaceRequest{
    UnionId: tea.String("chyxxxxx"),
    OpenConversationId: tea.String("cid9FTRQSLo+sKxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSpaceWithOptions(getSpaceRequest, getSpaceHeaders, &util.RuntimeOptions{})
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
const dingtalkconvFile_1_0 = require('@alicloud/dingtalk/convFile_1_0');
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
    return new dingtalkconvFile_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getSpaceHeaders = new dingtalkconvFile_1_0.GetSpaceHeaders({ });
    getSpaceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getSpaceRequest = new dingtalkconvFile_1_0.GetSpaceRequest({
      unionId: 'chyxxxxx',
      openConversationId: 'cid9FTRQSLo+sKxxxx',
    });
    try {
      await client.getSpaceWithOptions(getSpaceRequest, getSpaceHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkconv_file_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconv_file_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconv_file_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.GetSpaceHeaders getSpaceHeaders = new AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.GetSpaceHeaders();
            getSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.GetSpaceRequest getSpaceRequest = new AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.GetSpaceRequest
            {
                UnionId = "chyxxxxx",
                OpenConversationId = "cid9FTRQSLo+sKxxxx",
            };
            try
            {
                client.GetSpaceWithOptions(getSpaceRequest, getSpaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| space | Object | 会话存储空间信息。 |
| spaceId | String | 会话存储空间ID。 |
| corpId | String | 空间归属企业的corpId。 |
| createTime | String | 群存储空间的创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 群存储空间的修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "space" : {
    "spaceId" : "798xxxxx",
    "corpId" : "ding1234xxxxx",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.conversationId | %s | 参数错误-conversationId |
| 403 | permissionDenied | %s | 用户缺少获取IM会话存储空间的权限 |
| 403 | acrossOrgAccessForbidden | %s | 禁止跨企业访问 |
| 404 | conversationNotExist | %s | 目标会话不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
