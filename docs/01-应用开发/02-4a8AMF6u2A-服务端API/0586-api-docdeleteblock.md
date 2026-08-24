---
title: "删除块元素"
source_url: "https://open.dingtalk.com/document/development/api-docdeleteblock"
namespace: "development"
slug: "api-docdeleteblock"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 文档 > 文档 > 删除块元素"
doc_id: "qjfMqiMixD"
updated_at: "2026-06-02 18:38:42"
---

> Source: https://open.dingtalk.com/document/development/api-docdeleteblock
> Path: 应用开发 / 服务端API / 文档/文件 > 文档 > 文档 > 删除块元素
> Updated: 2026-06-02 18:38:42

# 删除块元素

调用本接口，可以删除文档中 1 个特定的块元素。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks/{blockId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.File.Write-企业存储文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| docKey | String | 是 | 文档ID（文档的 docKey 或 dentryUuid），通过[创建知识库文档](0567-create-team-space-document.md)接口创建文档后，从返回值中获取`docKey`参数。  **[!NOTE]**    从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。 |
| blockId | String | 是 | 待删除块的 `blockId`，可以通过[查询块元素](0583-api-docblocksquery.md)接口获得 `blockId` 参数。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 用户unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求示例

HTTP

```
DELETE /v1.0/doc/suites/documents/doc_key/blocks/block_id?operatorId=union_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7dc9ec4xxx
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
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_1_0.models.DocDeleteBlockHeaders docDeleteBlockHeaders = new com.aliyun.dingtalkdoc_1_0.models.DocDeleteBlockHeaders();
        docDeleteBlockHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.DocDeleteBlockRequest docDeleteBlockRequest = new com.aliyun.dingtalkdoc_1_0.models.DocDeleteBlockRequest()
                .setOperatorId("union_id");
        try {
            client.docDeleteBlockWithOptions("doc_key", "block_id", docDeleteBlockRequest, docDeleteBlockHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.doc_1_0.client import Client as dingtalkdoc_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_1_0 import models as dingtalkdoc__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        doc_delete_block_headers = dingtalkdoc__1__0_models.DocDeleteBlockHeaders()
        doc_delete_block_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_delete_block_request = dingtalkdoc__1__0_models.DocDeleteBlockRequest(
            operator_id='union_id'
        )
        try:
            client.doc_delete_block_with_options('doc_key', 'block_id', doc_delete_block_request, doc_delete_block_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        doc_delete_block_headers = dingtalkdoc__1__0_models.DocDeleteBlockHeaders()
        doc_delete_block_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_delete_block_request = dingtalkdoc__1__0_models.DocDeleteBlockRequest(
            operator_id='union_id'
        )
        try:
            await client.doc_delete_block_with_options_async('doc_key', 'block_id', doc_delete_block_request, doc_delete_block_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DocDeleteBlockHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DocDeleteBlockRequest;
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
        $docDeleteBlockHeaders = new DocDeleteBlockHeaders([]);
        $docDeleteBlockHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $docDeleteBlockRequest = new DocDeleteBlockRequest([
            "operatorId" => "union_id"
        ]);
        try {
            $client->docDeleteBlockWithOptions("doc_key", "block_id", $docDeleteBlockRequest, $docDeleteBlockHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
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
func CreateClient () (_result *dingtalkdoc_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_1_0.Client{}
  _result, _err = dingtalkdoc_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  docDeleteBlockHeaders := &dingtalkdoc_1_0.DocDeleteBlockHeaders{}
  docDeleteBlockHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  docDeleteBlockRequest := &dingtalkdoc_1_0.DocDeleteBlockRequest{
    OperatorId: tea.String("union_id"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DocDeleteBlockWithOptions(tea.String("doc_key"), tea.String("block_id"), docDeleteBlockRequest, docDeleteBlockHeaders, &util.RuntimeOptions{})
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
const dingtalkdoc_1_0 = require('@alicloud/dingtalk/doc_1_0');
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
    return new dingtalkdoc_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let docDeleteBlockHeaders = new dingtalkdoc_1_0.DocDeleteBlockHeaders({ });
    docDeleteBlockHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let docDeleteBlockRequest = new dingtalkdoc_1_0.DocDeleteBlockRequest({
      operatorId: 'union_id',
    });
    try {
      await client.docDeleteBlockWithOptions('doc_key', 'block_id', docDeleteBlockRequest, docDeleteBlockHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdoc_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocDeleteBlockHeaders docDeleteBlockHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocDeleteBlockHeaders();
            docDeleteBlockHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocDeleteBlockRequest docDeleteBlockRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocDeleteBlockRequest
            {
                OperatorId = "union_id",
            };
            try
            {
                client.DocDeleteBlockWithOptions("doc_key", "block_id", docDeleteBlockRequest, docDeleteBlockHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | invalidRequest.inputArgs.invalid | %s | 参数错误, 请查看错误信息。 |
| 403 | forbidden.accessDenied | %s | 无权限 |
| 404 | docNotExist | %s | 文档不存在 |
| 404 | invalidRequest.resource.notFound | %s | 无法找到要访问的资源 |
| 500 | forbidden.operationIllegal | %s | 请求操作不合法 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
