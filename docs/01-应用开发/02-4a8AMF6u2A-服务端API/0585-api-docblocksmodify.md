---
title: "更新块元素"
source_url: "https://open.dingtalk.com/document/development/api-docblocksmodify"
namespace: "development"
slug: "api-docblocksmodify"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 文档 > 文档 > 更新块元素"
doc_id: "pplS9nSNPE"
updated_at: "2026-06-04 19:09:03"
---

> Source: https://open.dingtalk.com/document/development/api-docblocksmodify
> Path: 应用开发 / 服务端API / 文档/文件 > 文档 > 文档 > 更新块元素
> Updated: 2026-06-04 19:09:03

# 更新块元素

调用本接口，可以更新文档中任意 1 个块元素的内容或属性。

## 接口调用说明

- 本质是PATCH操作（非幂等），仅更新传入的字段，未传入的字段保持不变。
- 目前仅支持更新段落类型的块元素。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/suites/documents/{documentId}/blocks/{blockId} |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.File.Write-企业存储文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| documentId | String | 是 | 文档ID（文档的 docKey 或 dentryUuid），通过[创建知识库文档](0567-create-team-space-document.md)接口创建文档后，从返回值中获取`docKey`参数。      从文档URL获取`dentryUuid`，以https://alidocs.dingtalk.com/i/nodes/Zxxxxa-id为例，dentryUuid就是Zxxxxa-id。 |
| blockId | String | 是 | 目标段落的唯一标识，可以通过[查询块元素](0583-api-docblocksquery.md)接口获得该段落的 `blockId` 参数。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 用户unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| element | Map<String, Any> | 是 | 待更新的块元素 BlockElement 类型和对应类型所需的属性（详情参考[块元素数据结构](0577-block-data-structure.md)），结构如下：   ``` {   "blockType": enum(BlockType),   [blockType]: Object(ElementProperties), } ``` |
|  | Any | 否 | 待更新的块元素属性。 |

### 请求示例

HTTP

```
PUT /v1.0/doc/suites/documents/doc_id/blocks/block_id?operatorId=union_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "element" : {
    "blockType" : "paragraph",
    "paragraph" : {
      "folded": true
    }
  }
}
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
        com.aliyun.dingtalkdoc_1_0.models.DocBlocksModifyHeaders docBlocksModifyHeaders = new com.aliyun.dingtalkdoc_1_0.models.DocBlocksModifyHeaders();
        docBlocksModifyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, java.util.Map<String, Object>> element = TeaConverter.buildMap(
            new TeaPair("key", new java.util.HashMap<>())
        );
        com.aliyun.dingtalkdoc_1_0.models.DocBlocksModifyRequest docBlocksModifyRequest = new com.aliyun.dingtalkdoc_1_0.models.DocBlocksModifyRequest()
                .setOperatorId("union_id")
                .setElement(element);
        try {
            client.docBlocksModifyWithOptions("doc_id", "block_id", docBlocksModifyRequest, docBlocksModifyHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        doc_blocks_modify_headers = dingtalkdoc__1__0_models.DocBlocksModifyHeaders()
        doc_blocks_modify_headers.x_acs_dingtalk_access_token = '<your access token>'
        element = {
            'key': {}
        }
        doc_blocks_modify_request = dingtalkdoc__1__0_models.DocBlocksModifyRequest(
            operator_id='union_id',
            element=element
        )
        try:
            client.doc_blocks_modify_with_options('doc_id', 'block_id', doc_blocks_modify_request, doc_blocks_modify_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        doc_blocks_modify_headers = dingtalkdoc__1__0_models.DocBlocksModifyHeaders()
        doc_blocks_modify_headers.x_acs_dingtalk_access_token = '<your access token>'
        element = {
            'key': {}
        }
        doc_blocks_modify_request = dingtalkdoc__1__0_models.DocBlocksModifyRequest(
            operator_id='union_id',
            element=element
        )
        try:
            await client.doc_blocks_modify_with_options_async('doc_id', 'block_id', doc_blocks_modify_request, doc_blocks_modify_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DocBlocksModifyHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DocBlocksModifyRequest;
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
        $docBlocksModifyHeaders = new DocBlocksModifyHeaders([]);
        $docBlocksModifyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $element = [
            "key" => []
        ];
        $docBlocksModifyRequest = new DocBlocksModifyRequest([
            "operatorId" => "union_id",
            "element" => $element
        ]);
        try {
            $client->docBlocksModifyWithOptions("doc_id", "block_id", $docBlocksModifyRequest, $docBlocksModifyHeaders, new RuntimeOptions([]));
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

  docBlocksModifyHeaders := &dingtalkdoc_1_0.DocBlocksModifyHeaders{}
  docBlocksModifyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  element := map[string]map[string]interface{}{
    "key": map[string]interface{}{},
  }
  docBlocksModifyRequest := &dingtalkdoc_1_0.DocBlocksModifyRequest{
    OperatorId: tea.String("union_id"),
    Element: element,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DocBlocksModifyWithOptions(tea.String("doc_id"), tea.String("block_id"), docBlocksModifyRequest, docBlocksModifyHeaders, &util.RuntimeOptions{})
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
    let docBlocksModifyHeaders = new dingtalkdoc_1_0.DocBlocksModifyHeaders({ });
    docBlocksModifyHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let element = {
      key: { },
    };
    let docBlocksModifyRequest = new dingtalkdoc_1_0.DocBlocksModifyRequest({
      operatorId: 'union_id',
      element: element,
    });
    try {
      await client.docBlocksModifyWithOptions('doc_id', 'block_id', docBlocksModifyRequest, docBlocksModifyHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksModifyHeaders docBlocksModifyHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksModifyHeaders();
            docBlocksModifyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, Dictionary<string, object>> element = new Dictionary<string, Dictionary<string, object>>
            {
                {"key", new Dictionary<string, object>(){}},
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksModifyRequest docBlocksModifyRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DocBlocksModifyRequest
            {
                OperatorId = "union_id",
                Element = element,
            };
            try
            {
                client.DocBlocksModifyWithOptions("doc_id", "block_id", docBlocksModifyRequest, docBlocksModifyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array of Any | 请求结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "result" : [ "{}" ]
  }
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
