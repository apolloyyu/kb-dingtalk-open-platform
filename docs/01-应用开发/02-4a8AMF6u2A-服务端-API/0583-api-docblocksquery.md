---
title: "查询块元素"
source_url: "https://open.dingtalk.com/document/development/api-docblocksquery"
namespace: "development"
slug: "api-docblocksquery"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 文档 > 查询块元素"
doc_id: "NRjaJZv9jG"
updated_at: "2026-06-04 19:09:01"
---

> Source: https://open.dingtalk.com/document/development/api-docblocksquery
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 文档 > 查询块元素
> Updated: 2026-06-04 19:09:01

# 查询块元素

调用本接口查询文档下的一级块元素，即根节点下的第一级的块元素，支持按起止位置和块类型进行过滤。

## 接口调用说明

如需要了解文档内容相关的数据结构，请参考[文档数据结构](0576-document-data-structure.md)内容。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.File.Read-企业存储文件读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| docKey | String | 是 | 文档ID（文档的 docKey 或 dentryUuid），通过[创建知识库文档](0567-create-team-space-document.md)接口创建文档后，从返回值中获取`docKey`参数。      从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| startIndex | Integer | 否 | 起始位置，为大于等于 0 的整数，表示从文档下第`startIndex`个块元素开始。 |
| endIndex | Integer | 否 | 终止位置，为大于等于 0 的整数，表示查询到第`endIndex`个块元素为止。 |
| blockType | String | 否 | 指定块元素类型，详情参考[块元素数据结构](0577-block-data-structure.md)。 |
| operatorId | String | 是 | 用户unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求示例

HTTP

```
GET /v1.0/doc/suites/documents/doc_id/blocks?startIndex=0&endIndex=1&blockType=paragraph&operatorId=union_id HTTP/1.1
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
        com.aliyun.dingtalkdoc_1_0.models.DocBlocksQueryHeaders docBlocksQueryHeaders = new com.aliyun.dingtalkdoc_1_0.models.DocBlocksQueryHeaders();
        docBlocksQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.DocBlocksQueryRequest docBlocksQueryRequest = new com.aliyun.dingtalkdoc_1_0.models.DocBlocksQueryRequest()
                .setStartIndex(0)
                .setEndIndex(1)
                .setBlockType("paragraph")
                .setOperatorId("union_id");
        try {
            client.docBlocksQueryWithOptions("doc_id", docBlocksQueryRequest, docBlocksQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        doc_blocks_query_headers = dingtalkdoc__1__0_models.DocBlocksQueryHeaders()
        doc_blocks_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_blocks_query_request = dingtalkdoc__1__0_models.DocBlocksQueryRequest(
            start_index=0,
            end_index=1,
            block_type='paragraph',
            operator_id='union_id'
        )
        try:
            client.doc_blocks_query_with_options('doc_id', doc_blocks_query_request, doc_blocks_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        doc_blocks_query_headers = dingtalkdoc__1__0_models.DocBlocksQueryHeaders()
        doc_blocks_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_blocks_query_request = dingtalkdoc__1__0_models.DocBlocksQueryRequest(
            start_index=0,
            end_index=1,
            block_type='paragraph',
            operator_id='union_id'
        )
        try:
            await client.doc_blocks_query_with_options_async('doc_id', doc_blocks_query_request, doc_blocks_query_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DocBlocksQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DocBlocksQueryRequest;
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
        $docBlocksQueryHeaders = new DocBlocksQueryHeaders([]);
        $docBlocksQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $docBlocksQueryRequest = new DocBlocksQueryRequest([
            "startIndex" => 0,
            "endIndex" => 1,
            "blockType" => "paragraph",
            "operatorId" => "union_id"
        ]);
        try {
            $client->docBlocksQueryWithOptions("doc_id", $docBlocksQueryRequest, $docBlocksQueryHeaders, new RuntimeOptions([]));
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

  docBlocksQueryHeaders := &dingtalkdoc_1_0.DocBlocksQueryHeaders{}
  docBlocksQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  docBlocksQueryRequest := &dingtalkdoc_1_0.DocBlocksQueryRequest{
    StartIndex: tea.Int32(0),
    EndIndex: tea.Int32(1),
    BlockType: tea.String("paragraph"),
    OperatorId: tea.String("union_id"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DocBlocksQueryWithOptions(tea.String("doc_id"), docBlocksQueryRequest, docBlocksQueryHeaders, &util.RuntimeOptions{})
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
    let docBlocksQueryHeaders = new dingtalkdoc_1_0.DocBlocksQueryHeaders({ });
    docBlocksQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let docBlocksQueryRequest = new dingtalkdoc_1_0.DocBlocksQueryRequest({
      startIndex: 0,
      endIndex: 1,
      blockType: 'paragraph',
      operatorId: 'union_id',
    });
    try {
      await client.docBlocksQueryWithOptions('doc_id', docBlocksQueryRequest, docBlocksQueryHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksQueryHeaders docBlocksQueryHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksQueryHeaders();
            docBlocksQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksQueryRequest docBlocksQueryRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksQueryRequest
            {
                StartIndex = 0,
                EndIndex = 1,
                BlockType = "paragraph",
                OperatorId = "union_id",
            };
            try
            {
                client.DocBlocksQueryWithOptions("doc_id", docBlocksQueryRequest, docBlocksQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 请求是否成功。 |
| result | Object | 请求结果。 |
| data | Array of Any | 元素的每一项为 块元素 结构。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success": true,
  "result": {
    "data": [
      {
        "blockType": "paragraph",
        "paragraph": {
          "text": "段落一"
        },
        "id": "lc4si5p3n84zwqxxx",
        "index": 1,
      },
      {
        "blockType": "paragraph",
        "paragraph": {
          "text": "段落二"
        },
        "id": "lc4si5p3n84zwqyyy",
        "index": 1,
      }
    ]
  },
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | invalidRequest.inputArgs.invalid | %s | 参数错误, 请查看错误信息。 |
| 403 | forbidden.accessDenied | %s | 无权限 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 404 | docNotExist | %s | 文档不存在 |
| 404 | invalidRequest.resource.notFound | %s | 无法找到要访问的资源 |
| 500 | forbidden.operationIllegal | %s | 请求操作不合法 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
