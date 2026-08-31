---
title: "AI卡片流式更新"
source_url: "https://open.dingtalk.com/document/development/api-streamingupdate"
namespace: "development"
slug: "api-streamingupdate"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > AI卡片流式更新"
doc_id: "qEwYdVxzG4"
updated_at: "2026-06-04 14:08:38"
---

> Source: https://open.dingtalk.com/document/development/api-streamingupdate
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > AI卡片流式更新
> Updated: 2026-06-04 14:08:38

# AI卡片流式更新

本接口旨在为AIGC产生的内容提供一种持续更新的能力，通过本接口持续更新的内容，在客户端会呈现一种打字机效果。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/streaming |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Streaming.Write-AI卡片流式更新权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 外部卡片实例Id，与[创建卡片](0780-interface-for-creating-a-card-instance.md)/[创建并投放卡片](0783-create-and-deliver-cards.md)中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取：  image |
| guid | String | 是 | 请求调用的唯一标志，系统内部用于幂等判断。 |
| key | String | 是 | 需要进行流式更新的变量。 |
| content | String | 是 | 此更新的流式内容。  **[!NOTE]**   - 由于 markdown 需要服务端进行格式转换，必须要保证是全量的内容及markdown 语法的完整性。 - 内容 size 单次不要超过 1 K，总大小建议不要超过 3 K。 |
| isFull | Boolean | 否 | 是否全量：   - **true**：全量 - **false**：非全量（默认）   **[!NOTE]**   - 如果是true，则内部以覆盖的方式进行更新，如果是 false，则内部以增量的方式进行更新。 - 如果流式变量绑定的是 markdown，该参数必须设置为 true，否则会报错。 |
| isFinalize | Boolean | 否 | 是否是最后一帧：   - **true**：最后一帧 - **false**：不是最后一帧（默认）   **[!NOTE]**  如果设置为 true，AI卡片将从「输入中」状态切换为「完成」状态。卡片状态信息请参考文档[AI 卡片模板](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0002-ai-card-template.md)。 |
| isError | Boolean | 否 | 是否出错：   - **true**：出错 - **false**：没有出错（默认）   **[!NOTE]**  如果设置为 true，AI卡片将从「输入中」状态切换为「出错」状态，卡片状态信息请参考文档[AI 卡片模板](../../05-互动卡片/01-N4KJ5HbqnQ-开发指南/0002-ai-card-template.md)。 |

### 请求示例

HTTP

```
PUT /v1.0/card/streaming HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a7e06cc6114c3ddc8e0ab7d7cbdc34a4
Content-Type:application/json

{
  "outTrackId" : "your-out-track-id",
  "guid" : "0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8",
  "key" : "your-ai-param",
  "content" : "test",
  "isFull" : false,
  "isFinalize" : false,
  "isError" : false
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.StreamingUpdateHeaders streamingUpdateHeaders = new com.aliyun.dingtalkcard_1_0.models.StreamingUpdateHeaders();
        streamingUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.StreamingUpdateRequest streamingUpdateRequest = new com.aliyun.dingtalkcard_1_0.models.StreamingUpdateRequest()
                .setOutTrackId("your-out-track-id")
                .setGuid("0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8")
                .setKey("your-ai-param")
                .setContent("test")
                .setIsFull(false)
                .setIsFinalize(false)
                .setIsError(false);
        try {
            client.streamingUpdateWithOptions(streamingUpdateRequest, streamingUpdateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        streaming_update_headers = dingtalkcard__1__0_models.StreamingUpdateHeaders()
        streaming_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        streaming_update_request = dingtalkcard__1__0_models.StreamingUpdateRequest(
            out_track_id='your-out-track-id',
            guid='0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8',
            key='your-ai-param',
            content='test',
            is_full=False,
            is_finalize=False,
            is_error=False
        )
        try:
            client.streaming_update_with_options(streaming_update_request, streaming_update_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        streaming_update_headers = dingtalkcard__1__0_models.StreamingUpdateHeaders()
        streaming_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        streaming_update_request = dingtalkcard__1__0_models.StreamingUpdateRequest(
            out_track_id='your-out-track-id',
            guid='0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8',
            key='your-ai-param',
            content='test',
            is_full=False,
            is_finalize=False,
            is_error=False
        )
        try:
            await client.streaming_update_with_options_async(streaming_update_request, streaming_update_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\StreamingUpdateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\StreamingUpdateRequest;
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
        $streamingUpdateHeaders = new StreamingUpdateHeaders([]);
        $streamingUpdateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $streamingUpdateRequest = new StreamingUpdateRequest([
            "outTrackId" => "your-out-track-id",
            "guid" => "0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8",
            "key" => "your-ai-param",
            "content" => "test",
            "isFull" => false,
            "isFinalize" => false,
            "isError" => false
        ]);
        try {
            $client->streamingUpdateWithOptions($streamingUpdateRequest, $streamingUpdateHeaders, new RuntimeOptions([]));
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
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  streamingUpdateHeaders := &dingtalkcard_1_0.StreamingUpdateHeaders{}
  streamingUpdateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  streamingUpdateRequest := &dingtalkcard_1_0.StreamingUpdateRequest{
    OutTrackId: tea.String("your-out-track-id"),
    Guid: tea.String("0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8"),
    Key: tea.String("your-ai-param"),
    Content: tea.String("test"),
    IsFull: tea.Bool(false),
    IsFinalize: tea.Bool(false),
    IsError: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.StreamingUpdateWithOptions(streamingUpdateRequest, streamingUpdateHeaders, &util.RuntimeOptions{})
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
const dingtalkcard_1_0 = require('@alicloud/dingtalk/card_1_0');
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
    return new dingtalkcard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let streamingUpdateHeaders = new dingtalkcard_1_0.StreamingUpdateHeaders({ });
    streamingUpdateHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let streamingUpdateRequest = new dingtalkcard_1_0.StreamingUpdateRequest({
      outTrackId: 'your-out-track-id',
      guid: '0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8',
      key: 'your-ai-param',
      content: 'test',
      isFull: false,
      isFinalize: false,
      isError: false,
    });
    try {
      await client.streamingUpdateWithOptions(streamingUpdateRequest, streamingUpdateHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.StreamingUpdateHeaders streamingUpdateHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.StreamingUpdateHeaders();
            streamingUpdateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.StreamingUpdateRequest streamingUpdateRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.StreamingUpdateRequest
            {
                OutTrackId = "your-out-track-id",
                Guid = "0F714542-0AFC-2B0E-CF14-E2D39F5BFFE8",
                Key = "your-ai-param",
                Content = "test",
                IsFull = false,
                IsFinalize = false,
                IsError = false,
            };
            try
            {
                client.StreamingUpdateWithOptions(streamingUpdateRequest, streamingUpdateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.stream.keyEmpty | param.stream.keyEmpty | streaming更新key为空 |
| 400 | param.stream.contentEmpty | param.stream.contentEmpty | streaming更新content为空 |
| 400 | param.stream.guidEmpty | param.stream.guidEmpty | streaming更新guid为空 |
| 400 | param.stream.outTrackId | card is not exist | 卡片不存在 |
| 400 | param.stream.isFull | streaming update the parameter isFull is null | isFull字段为空 |
| 400 | param.stream.content | content is too large | 200092 |
