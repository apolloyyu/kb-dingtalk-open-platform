---
title: "获取所有字段"
source_url: "https://open.dingtalk.com/document/development/api-noatable-getallfields"
namespace: "development"
slug: "api-noatable-getallfields"
group: "应用开发"
tab: "服务端API"
breadcrumb: "AI 表格 > 字段 > 获取所有字段"
doc_id: "x9fg5rS3OB"
updated_at: "2025-09-12 17:20:56"
---

> Source: https://open.dingtalk.com/document/development/api-noatable-getallfields
> Path: 应用开发 / 服务端API / AI 表格 > 字段 > 获取所有字段
> Updated: 2025-09-12 17:20:56

# 获取所有字段

调用本接口，在数据表中的所有字段。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/notable/bases/{baseId}/sheets/{sheetIdOrName}/fields |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Notable.Base.Read.All-AI 表格应用读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| baseId | String | 是 | AI表格ID，获取方式请参考[数据结构](0457-data-structure.md#e2156ac0b1eko)。 |
| sheetIdOrName | String | 是 | 数据表ID或数据表名称。数据表ID可通过[获取所有数据表](0461-api-notable-getallsheets.md)或[获取数据表](0460-api-notable-getsheet.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可通过以下两种方式获取：   - 调用[查询用户详情](0056-query-user-details.md)接口获取。 - 调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/notable/bases/xxxxx/sheets/数据表/fields?operatorId=xxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
    public static com.aliyun.dingtalknotable_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalknotable_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalknotable_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalknotable_1_0.models.GetAllFieldsHeaders getAllFieldsHeaders = new com.aliyun.dingtalknotable_1_0.models.GetAllFieldsHeaders();
        getAllFieldsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalknotable_1_0.models.GetAllFieldsRequest getAllFieldsRequest = new com.aliyun.dingtalknotable_1_0.models.GetAllFieldsRequest()
                .setOperatorId("xxxxx");
        try {
            client.getAllFieldsWithOptions("xxxxx", "数据表", getAllFieldsRequest, getAllFieldsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.notable_1_0.client import Client as dingtalknotable_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.notable_1_0 import models as dingtalknotable__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalknotable_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalknotable_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_all_fields_headers = dingtalknotable__1__0_models.GetAllFieldsHeaders()
        get_all_fields_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_all_fields_request = dingtalknotable__1__0_models.GetAllFieldsRequest(
            operator_id='xxxxx'
        )
        try:
            client.get_all_fields_with_options('xxxxx', '数据表', get_all_fields_request, get_all_fields_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_all_fields_headers = dingtalknotable__1__0_models.GetAllFieldsHeaders()
        get_all_fields_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_all_fields_request = dingtalknotable__1__0_models.GetAllFieldsRequest(
            operator_id='xxxxx'
        )
        try:
            await client.get_all_fields_with_options_async('xxxxx', '数据表', get_all_fields_request, get_all_fields_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vnotable_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vnotable_1_0\Models\GetAllFieldsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vnotable_1_0\Models\GetAllFieldsRequest;
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
        $getAllFieldsHeaders = new GetAllFieldsHeaders([]);
        $getAllFieldsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getAllFieldsRequest = new GetAllFieldsRequest([
            "operatorId" => "xxxxx"
        ]);
        try {
            $client->getAllFieldsWithOptions("xxxxx", "数据表", $getAllFieldsRequest, $getAllFieldsHeaders, new RuntimeOptions([]));
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
  dingtalknotable_1_0  "github.com/alibabacloud-go/dingtalk/notable_1_0"
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
func CreateClient () (_result *dingtalknotable_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalknotable_1_0.Client{}
  _result, _err = dingtalknotable_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getAllFieldsHeaders := &dingtalknotable_1_0.GetAllFieldsHeaders{}
  getAllFieldsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getAllFieldsRequest := &dingtalknotable_1_0.GetAllFieldsRequest{
    OperatorId: tea.String("xxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAllFieldsWithOptions(tea.String("xxxxx"), tea.String("数据表"), getAllFieldsRequest, getAllFieldsHeaders, &util.RuntimeOptions{})
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
const dingtalknotable_1_0 = require('@alicloud/dingtalk/notable_1_0');
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
    return new dingtalknotable_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getAllFieldsHeaders = new dingtalknotable_1_0.GetAllFieldsHeaders({ });
    getAllFieldsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getAllFieldsRequest = new dingtalknotable_1_0.GetAllFieldsRequest({
      operatorId: 'xxxxx',
    });
    try {
      await client.getAllFieldsWithOptions('xxxxx', '数据表', getAllFieldsRequest, getAllFieldsHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalknotable_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalknotable_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalknotable_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalknotable_1_0.Models.GetAllFieldsHeaders getAllFieldsHeaders = new AlibabaCloud.SDK.Dingtalknotable_1_0.Models.GetAllFieldsHeaders();
            getAllFieldsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalknotable_1_0.Models.GetAllFieldsRequest getAllFieldsRequest = new AlibabaCloud.SDK.Dingtalknotable_1_0.Models.GetAllFieldsRequest
            {
                OperatorId = "xxxxx",
            };
            try
            {
                client.GetAllFieldsWithOptions("xxxxx", "数据表", getAllFieldsRequest, getAllFieldsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| value | Array | 字段列表。 |
| id | String | 字段ID。 |
| name | String | 字段名。 |
| type | String | 字段类型。 |
| property | Map<String, Any> | 字段属性，具体格式请参考[字段属性](0457-data-structure.md#e1e0d1e78820h)。 |
|  | Any | 字段属性。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "value" : [ {
    "id" : "xxxxx",
    "name" : "姓名",
    "type" : "text",
    "property" : {
      "key" : "{}"
    }
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.document.stillInitializing | The document is under initialization. Please try again later | 文档初始化中，请稍后重试 |
| 400 | invalidRequest.document.broken | The document is broken and the server is unable to complete your request. | 文档已损坏 |
| 403 | forbidden.operationIllegal | %s | 无权限 |
| 403 | invalidRequest.document.typeIllegal | %s | 不支持的文档类型，请检查baseId |
| 404 | invalidRequest.document.notFound | Fail to find the requested resource by the given baseId. Please make sure the given baseId is valid, and the operatorId has permission to access it. | 文档不存在 |
| 404 | invalidRequest.resource.notFound | %s | 资源不存在，数据不存在或被彻底删除 |
| 504 | service.timeout | The server is busy and unable to complete your request. Please try again later. | 请求超时 |
