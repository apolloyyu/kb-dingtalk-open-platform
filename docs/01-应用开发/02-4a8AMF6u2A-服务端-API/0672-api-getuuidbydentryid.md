---
title: "获取 dentryUuid 信息"
source_url: "https://open.dingtalk.com/document/development/api-getuuidbydentryid"
namespace: "development"
slug: "api-getuuidbydentryid"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 获取 dentryUuid 信息"
doc_id: "gezL8vSCPq"
updated_at: "2026-06-02 18:49:02"
---

> Source: https://open.dingtalk.com/document/development/api-getuuidbydentryid
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 获取 dentryUuid 信息
> Updated: 2026-06-02 18:49:02

# 获取 dentryUuid 信息

根据文件的 spaceId 和 dentryId 获取文件的 dentryUuid 信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/doc/dentries/{dentryId}/queryDentryUuid |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Document.WorkspaceDocument.Read-知识库文档读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dentryId | String | 是 | 当前文件的 ID。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间 ID。 |
| operatorId | String | 是 | 操作人 unionId，调用[查询用户详情](0056-query-user-details.md)接口获取 unionid 参数值。 |

### 请求示例

HTTP

```
GET /v2.0/doc/dentries/1744xxxx000/queryDentryUuid?spaceId=490xxxx76&operatorId=E9CS6xxxxN7QiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:873d8xxxx9380ad
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
    public static com.aliyun.dingtalkdoc_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdoc_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_2_0.models.GetUuidByDentryIdHeaders getUuidByDentryIdHeaders = new com.aliyun.dingtalkdoc_2_0.models.GetUuidByDentryIdHeaders();
        getUuidByDentryIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_2_0.models.GetUuidByDentryIdRequest getUuidByDentryIdRequest = new com.aliyun.dingtalkdoc_2_0.models.GetUuidByDentryIdRequest()
                .setSpaceId("490xxxx76")
                .setOperatorId("E9CS6xxxxN7QiEiE");
        try {
            client.getUuidByDentryIdWithOptions("1744xxxx000", getUuidByDentryIdRequest, getUuidByDentryIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.doc_2_0.client import Client as dingtalkdoc_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_2_0 import models as dingtalkdoc__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_uuid_by_dentry_id_headers = dingtalkdoc__2__0_models.GetUuidByDentryIdHeaders()
        get_uuid_by_dentry_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_uuid_by_dentry_id_request = dingtalkdoc__2__0_models.GetUuidByDentryIdRequest(
            space_id='490xxxx76',
            operator_id='E9CS6xxxxN7QiEiE'
        )
        try:
            client.get_uuid_by_dentry_id_with_options('1744xxxx000', get_uuid_by_dentry_id_request, get_uuid_by_dentry_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_uuid_by_dentry_id_headers = dingtalkdoc__2__0_models.GetUuidByDentryIdHeaders()
        get_uuid_by_dentry_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_uuid_by_dentry_id_request = dingtalkdoc__2__0_models.GetUuidByDentryIdRequest(
            space_id='490xxxx76',
            operator_id='E9CS6xxxxN7QiEiE'
        )
        try:
            await client.get_uuid_by_dentry_id_with_options_async('1744xxxx000', get_uuid_by_dentry_id_request, get_uuid_by_dentry_id_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\GetUuidByDentryIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\GetUuidByDentryIdRequest;
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
        $getUuidByDentryIdHeaders = new GetUuidByDentryIdHeaders([]);
        $getUuidByDentryIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUuidByDentryIdRequest = new GetUuidByDentryIdRequest([
            "spaceId" => "490xxxx76",
            "operatorId" => "E9CS6xxxxN7QiEiE"
        ]);
        try {
            $client->getUuidByDentryIdWithOptions("1744xxxx000", $getUuidByDentryIdRequest, $getUuidByDentryIdHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_2_0  "github.com/alibabacloud-go/dingtalk/doc_2_0"
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
func CreateClient () (_result *dingtalkdoc_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_2_0.Client{}
  _result, _err = dingtalkdoc_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUuidByDentryIdHeaders := &dingtalkdoc_2_0.GetUuidByDentryIdHeaders{}
  getUuidByDentryIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUuidByDentryIdRequest := &dingtalkdoc_2_0.GetUuidByDentryIdRequest{
    SpaceId: tea.String("490xxxx76"),
    OperatorId: tea.String("E9CS6xxxxN7QiEiE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUuidByDentryIdWithOptions(tea.String("1744xxxx000"), getUuidByDentryIdRequest, getUuidByDentryIdHeaders, &util.RuntimeOptions{})
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
const dingtalkdoc_2_0 = require('@alicloud/dingtalk/doc_2_0');
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
    return new dingtalkdoc_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getUuidByDentryIdHeaders = new dingtalkdoc_2_0.GetUuidByDentryIdHeaders({ });
    getUuidByDentryIdHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getUuidByDentryIdRequest = new dingtalkdoc_2_0.GetUuidByDentryIdRequest({
      spaceId: '490xxxx76',
      operatorId: 'E9CS6xxxxN7QiEiE',
    });
    try {
      await client.getUuidByDentryIdWithOptions('1744xxxx000', getUuidByDentryIdRequest, getUuidByDentryIdHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdoc_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.GetUuidByDentryIdHeaders getUuidByDentryIdHeaders = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.GetUuidByDentryIdHeaders();
            getUuidByDentryIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.GetUuidByDentryIdRequest getUuidByDentryIdRequest = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.GetUuidByDentryIdRequest
            {
                SpaceId = "490xxxx76",
                OperatorId = "E9CS6xxxxN7QiEiE",
            };
            try
            {
                client.GetUuidByDentryIdWithOptions("1744xxxx000", getUuidByDentryIdRequest, getUuidByDentryIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dentryUuid | String | 当前文件 UUID。 |
| dentryId | String | 当前文件 ID。 |
| spaceId | String | 当前空间 ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "dentryUuid" : "Qnp9zOxxxx1DK0g6l",
  "dentryId" : "1744xxxx2000",
  "spaceId" : "490xxxx976"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 403 | permissionDenied | The operator has no permission. | 当前用户无此操作权限 |
| 404 | documentNotExist | %s | 文档不存在或格式不支持 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
