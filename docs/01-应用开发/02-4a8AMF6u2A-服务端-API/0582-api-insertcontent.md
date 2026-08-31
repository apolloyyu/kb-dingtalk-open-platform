---
title: "插入内容"
source_url: "https://open.dingtalk.com/document/development/api-insertcontent"
namespace: "development"
slug: "api-insertcontent"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 文档 > 插入内容"
doc_id: "F4EkpmUDTs"
updated_at: "2026-06-04 19:09:01"
---

> Source: https://open.dingtalk.com/document/development/api-insertcontent
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 文档 > 插入内容
> Updated: 2026-06-04 19:09:01

# 插入内容

调用本接口，在文档的指定位置插入一段内容，内容类型支持 Markdown。

## 接口调用说明

插入位置可以是文档根节点的`children`，也可以是支持插入块元素的 `BlockElement`（如高亮块、Table）的 children，通过 `path`和 `index`参数共同确定插入位置。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/suites/documents/{documentId}/content |
| HTTP Method | POST |
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

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 用户unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| path | Array of Integer | 否 | 插入位置。 |
| index | Integer | 否 | 插入位置。 |
| content | Object | 是 | 插入内容。 |
| type | String | 是 | 具体插入的内容类型，目前只支持 `markdown`。 |
| content | String | 是 | 插入的内容文本。 |

### 请求示例

HTTP

```
POST /v1.0/doc/suites/documents/doc_id/content?operatorId=union_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "content" : {
    "content" : "## Heading",
    "type" : "markdown"
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
        com.aliyun.dingtalkdoc_1_0.models.InsertContentHeaders insertContentHeaders = new com.aliyun.dingtalkdoc_1_0.models.InsertContentHeaders();
        insertContentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.InsertContentRequest.InsertContentRequestContent content = new com.aliyun.dingtalkdoc_1_0.models.InsertContentRequest.InsertContentRequestContent()
                .setContent("## Heading")
                .setType("markdown");
        com.aliyun.dingtalkdoc_1_0.models.InsertContentRequest insertContentRequest = new com.aliyun.dingtalkdoc_1_0.models.InsertContentRequest()
                .setOperatorId("union_id")
                .setPath(java.util.Arrays.asList(
                    0
                ))
                .setContent(content);
        try {
            client.insertContentWithOptions("doc_id", insertContentRequest, insertContentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        insert_content_headers = dingtalkdoc__1__0_models.InsertContentHeaders()
        insert_content_headers.x_acs_dingtalk_access_token = '<your access token>'
        content = dingtalkdoc__1__0_models.InsertContentRequestContent(
            content='## Heading',
            type='markdown'
        )
        insert_content_request = dingtalkdoc__1__0_models.InsertContentRequest(
            operator_id='union_id',
            path=[
                0
            ],
            content=content
        )
        try:
            client.insert_content_with_options('doc_id', insert_content_request, insert_content_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        insert_content_headers = dingtalkdoc__1__0_models.InsertContentHeaders()
        insert_content_headers.x_acs_dingtalk_access_token = '<your access token>'
        content = dingtalkdoc__1__0_models.InsertContentRequestContent(
            content='## Heading',
            type='markdown'
        )
        insert_content_request = dingtalkdoc__1__0_models.InsertContentRequest(
            operator_id='union_id',
            path=[
                0
            ],
            content=content
        )
        try:
            await client.insert_content_with_options_async('doc_id', insert_content_request, insert_content_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\InsertContentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\InsertContentRequest\content;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\InsertContentRequest;
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
        $insertContentHeaders = new InsertContentHeaders([]);
        $insertContentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $content = new content([
            "content" => "## Heading",
            "type" => "markdown"
        ]);
        $insertContentRequest = new InsertContentRequest([
            "operatorId" => "union_id",
            "path" => [
                0
            ],
            "content" => $content
        ]);
        try {
            $client->insertContentWithOptions("doc_id", $insertContentRequest, $insertContentHeaders, new RuntimeOptions([]));
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

  insertContentHeaders := &dingtalkdoc_1_0.InsertContentHeaders{}
  insertContentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  content := &dingtalkdoc_1_0.InsertContentRequestContent{
    Content: tea.String("## Heading"),
    Type: tea.String("markdown"),
  }
  insertContentRequest := &dingtalkdoc_1_0.InsertContentRequest{
    OperatorId: tea.String("union_id"),
    Path: []*int32{tea.Int32(0)},
    Content: content,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.InsertContentWithOptions(tea.String("doc_id"), insertContentRequest, insertContentHeaders, &util.RuntimeOptions{})
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
    let insertContentHeaders = new dingtalkdoc_1_0.InsertContentHeaders({ });
    insertContentHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let content = new dingtalkdoc_1_0.InsertContentRequestContent({
      content: '## Heading',
      type: 'markdown',
    });
    let insertContentRequest = new dingtalkdoc_1_0.InsertContentRequest({
      operatorId: 'union_id',
      path: [
        0
      ],
      content: content,
    });
    try {
      await client.insertContentWithOptions('doc_id', insertContentRequest, insertContentHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertContentHeaders insertContentHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertContentHeaders();
            insertContentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertContentRequest.InsertContentRequestContent content = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertContentRequest.InsertContentRequestContent
            {
                Content = "## Heading",
                Type = "markdown",
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertContentRequest insertContentRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertContentRequest
            {
                OperatorId = "union_id",
                Path = new List<int?>
                {
                    0
                },
                Content = content,
            };
            try
            {
                client.InsertContentWithOptions("doc_id", insertContentRequest, insertContentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Map | 请求结果。 |

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
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 404 | docNotExist | %s | 文档不存在 |
| 404 | invalidRequest.resource.notFound | %s | 无法找到要访问的资源 |
| 500 | forbidden.operationIllegal | %s | 请求操作不合法 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
