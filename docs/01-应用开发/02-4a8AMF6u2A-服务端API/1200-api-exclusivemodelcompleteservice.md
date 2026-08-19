---
title: "大模型推理服务（文生文模型）"
source_url: "https://open.dingtalk.com/document/development/api-exclusivemodelcompleteservice"
namespace: "development"
slug: "api-exclusivemodelcompleteservice"
group: "应用开发"
tab: "服务端API"
breadcrumb: "炼丹炉（模型服务） > 大模型推理服务（文生文模型）"
doc_id: "7h1JMtQnLk"
updated_at: "2025-10-09 18:07:13"
---

> Source: https://open.dingtalk.com/document/development/api-exclusivemodelcompleteservice
> Path: 应用开发 / 服务端API / 炼丹炉（模型服务） > 大模型推理服务（文生文模型）
> Updated: 2025-10-09 18:07:13

# 大模型推理服务（文生文模型）

钉钉官方提供的大模型推理服务接口，使用该服务可以访问钉钉大模型服务平台“炼丹炉”上发布的模型服务。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/aiPaaS/ai/complete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-AIPaaS.Model.Read-大模型读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| model | String | 是 | 模型名称：   - `qwen-plus` - `qwq-plus` - `qwen3-235b` |
| messages | Array | 是 | 消息数组信息。 |
| role | String | 是 | 角色信息：   - system：系统参数 - user：用户参数 |
| content | String | 是 | prompt 信息。 |
| temperature | double | 否 | 采样温度 (temperature)，用于控制模型生成文本的多样性。  **[!NOTE]**     - **temperature** 越高，生成的文本越多样； - **temperature** 越低，生成的文本越确定。 - **取值范围**: [0, 2) - **注意**: temperature 与 top\_p 均可以控制生成文本的多样性，因此建议您只设置其中一个值。 |
| top\_p | double | 否 | 核采样的概率阈值，用于控制模型生成文本的多样性。`top_p` 值越高，生成的文本越多样化；反之，生成的文本则更加确定。取值范围为：( (0, 1.0] )。  **[!NOTE]**    由于 `temperature` 与 `top_p` 均可用于控制生成文本的多样性，建议您在使用时仅设置其中一个参数。 |
| max\_tokens | Integer | 否 | 请求返回的最大 Token 数， `max_tokens` 的设置不会影响大模型的生成过程，但如果模型生成的 Token 数超过了设定的 `max_tokens`，本次请求将返回截断后的内容。  **[!NOTE]**     - **默认值**: 模型的最大输出长度 - **最大值**: 模型的最大输出长度 - 请根据具体需求合理设置 `max_tokens` 的值，以达到预期效果。 |
| enable\_search | Boolean | 否 | 用于控制模型在生成文本时是否使用互联网搜索：  **[!NOTE]**     - `true`：启用互联网搜索。模型会在生成文本时参考搜索结果，但最终是否使用这些结果取决于模型的内部逻辑。若模型不具备搜索能力，建议优化提示词（Prompt）。 - `false`（默认）：禁用互联网搜索。 - 启用互联网搜索功能可能会增加 Token 的消耗。如果您通过 Python SDK 调用来设置此参数，可以通过 `extra_body` 进行配置。配置示例如下：     ```   extra_body = {"enable_search": True}   ``` |
| stream | Boolean | 否 | 控制是否启用流式输出回复：   - true：是 - false：否   默认为：false；  **[!NOTE]**     - `false` :   模型生成完所有内容后一次性返回结果。 - `true` :   边生成边输出，即每生成一部分内容就立即输出一个片段（chunk）。您需要实时地逐个读取这些片段以获得完整的结果。 |

### 请求示例

HTTP

```
POST /v1.0/aiPaaS/ai/complete HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c1013786ab8130d593e1cc47e883fb6c
Content-Type:application/json

{
  "model" : "qwen-plus",
  "messages" : [ {
    "role" : "user",
    "content" : "你是谁"
  } ],
  "temperature" : 0.6,
  "top_p" : 1.0,
  "max_tokens" : 2000,
  "enable_search" : false,
  "stream" : false
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
    public static com.aliyun.dingtalkai_paa_s_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkai_paa_s_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkai_paa_s_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkai_paa_s_1_0.models.ExclusiveModelCompleteServiceHeaders exclusiveModelCompleteServiceHeaders = new com.aliyun.dingtalkai_paa_s_1_0.models.ExclusiveModelCompleteServiceHeaders();
        exclusiveModelCompleteServiceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkai_paa_s_1_0.models.ExclusiveModelCompleteServiceRequest.ExclusiveModelCompleteServiceRequestMessages messages0 = new com.aliyun.dingtalkai_paa_s_1_0.models.ExclusiveModelCompleteServiceRequest.ExclusiveModelCompleteServiceRequestMessages()
                .setRole("user")
                .setContent("你是谁");
        com.aliyun.dingtalkai_paa_s_1_0.models.ExclusiveModelCompleteServiceRequest exclusiveModelCompleteServiceRequest = new com.aliyun.dingtalkai_paa_s_1_0.models.ExclusiveModelCompleteServiceRequest()
                .setModel("qwen-plus")
                .setMessages(java.util.Arrays.asList(
                    messages0
                ))
                .setTemperature(0.6D)
                .setTopP(1D)
                .setMaxTokens(2000)
                .setEnableSearch(false)
                .setStream(false);
        try {
            client.exclusiveModelCompleteServiceWithOptions(exclusiveModelCompleteServiceRequest, exclusiveModelCompleteServiceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.ai_paa_s_1_0.client import Client as dingtalkaiPaaS_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.ai_paa_s_1_0 import models as dingtalkai_paa_s__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkaiPaaS_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkaiPaaS_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        exclusive_model_complete_service_headers = dingtalkai_paa_s__1__0_models.ExclusiveModelCompleteServiceHeaders()
        exclusive_model_complete_service_headers.x_acs_dingtalk_access_token = '<your access token>'
        messages_0 = dingtalkai_paa_s__1__0_models.ExclusiveModelCompleteServiceRequestMessages(
            role='user',
            content='你是谁'
        )
        exclusive_model_complete_service_request = dingtalkai_paa_s__1__0_models.ExclusiveModelCompleteServiceRequest(
            model='qwen-plus',
            messages=[
                messages_0
            ],
            temperature=0.6,
            top_p=1,
            max_tokens=2000,
            enable_search=False,
            stream=False
        )
        try:
            client.exclusive_model_complete_service_with_options(exclusive_model_complete_service_request, exclusive_model_complete_service_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        exclusive_model_complete_service_headers = dingtalkai_paa_s__1__0_models.ExclusiveModelCompleteServiceHeaders()
        exclusive_model_complete_service_headers.x_acs_dingtalk_access_token = '<your access token>'
        messages_0 = dingtalkai_paa_s__1__0_models.ExclusiveModelCompleteServiceRequestMessages(
            role='user',
            content='你是谁'
        )
        exclusive_model_complete_service_request = dingtalkai_paa_s__1__0_models.ExclusiveModelCompleteServiceRequest(
            model='qwen-plus',
            messages=[
                messages_0
            ],
            temperature=0.6,
            top_p=1,
            max_tokens=2000,
            enable_search=False,
            stream=False
        )
        try:
            await client.exclusive_model_complete_service_with_options_async(exclusive_model_complete_service_request, exclusive_model_complete_service_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Models\ExclusiveModelCompleteServiceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Models\ExclusiveModelCompleteServiceRequest\messages;
use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Models\ExclusiveModelCompleteServiceRequest;
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
        $exclusiveModelCompleteServiceHeaders = new ExclusiveModelCompleteServiceHeaders([]);
        $exclusiveModelCompleteServiceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $messages0 = new messages([
            "role" => "user",
            "content" => "你是谁"
        ]);
        $exclusiveModelCompleteServiceRequest = new ExclusiveModelCompleteServiceRequest([
            "model" => "qwen-plus",
            "messages" => [
                $messages0
            ],
            "temperature" => 0.6,
            "topP" => 1,
            "maxTokens" => 2000,
            "enableSearch" => false,
            "stream" => false
        ]);
        try {
            $client->exclusiveModelCompleteServiceWithOptions($exclusiveModelCompleteServiceRequest, $exclusiveModelCompleteServiceHeaders, new RuntimeOptions([]));
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
  dingtalkaipaas_1_0  "github.com/alibabacloud-go/dingtalk/aiPaaS_1_0"
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
func CreateClient () (_result *dingtalkaipaas_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkaipaas_1_0.Client{}
  _result, _err = dingtalkaipaas_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  exclusiveModelCompleteServiceHeaders := &dingtalkaipaas_1_0.ExclusiveModelCompleteServiceHeaders{}
  exclusiveModelCompleteServiceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  messages0 := &dingtalkaipaas_1_0.ExclusiveModelCompleteServiceRequestMessages{
    Role: tea.String("user"),
    Content: tea.String("你是谁"),
  }
  exclusiveModelCompleteServiceRequest := &dingtalkaipaas_1_0.ExclusiveModelCompleteServiceRequest{
    Model: tea.String("qwen-plus"),
    Messages: []*dingtalkaipaas_1_0.ExclusiveModelCompleteServiceRequestMessages{messages0},
    Temperature: tea.Float64(0.6),
    TopP: tea.Float64(1),
    MaxTokens: tea.Int32(2000),
    EnableSearch: tea.Bool(false),
    Stream: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ExclusiveModelCompleteServiceWithOptions(exclusiveModelCompleteServiceRequest, exclusiveModelCompleteServiceHeaders, &util.RuntimeOptions{})
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
const dingtalkaiPaaS_1_0 = require('@alicloud/dingtalk/aiPaaS_1_0');
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
    return new dingtalkaiPaaS_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let exclusiveModelCompleteServiceHeaders = new dingtalkaiPaaS_1_0.ExclusiveModelCompleteServiceHeaders({ });
    exclusiveModelCompleteServiceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let messages0 = new dingtalkaiPaaS_1_0.ExclusiveModelCompleteServiceRequestMessages({
      role: 'user',
      content: '你是谁',
    });
    let exclusiveModelCompleteServiceRequest = new dingtalkaiPaaS_1_0.ExclusiveModelCompleteServiceRequest({
      model: 'qwen-plus',
      messages: [
        messages0
      ],
      temperature: 0.6,
      topP: 1,
      maxTokens: 2000,
      enableSearch: false,
      stream: false,
    });
    try {
      await client.exclusiveModelCompleteServiceWithOptions(exclusiveModelCompleteServiceRequest, exclusiveModelCompleteServiceHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceHeaders exclusiveModelCompleteServiceHeaders = new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceHeaders();
            exclusiveModelCompleteServiceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceRequest.ExclusiveModelCompleteServiceRequestMessages messages0 = new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceRequest.ExclusiveModelCompleteServiceRequestMessages
            {
                Role = "user",
                Content = "你是谁",
            };
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceRequest exclusiveModelCompleteServiceRequest = new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceRequest
            {
                Model = "qwen-plus",
                Messages = new List<AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.ExclusiveModelCompleteServiceRequest.ExclusiveModelCompleteServiceRequestMessages>
                {
                    messages0
                },
                Temperature = 0.6,
                TopP = 1,
                MaxTokens = 2000,
                EnableSearch = false,
                Stream = false,
            };
            try
            {
                client.ExclusiveModelCompleteServiceWithOptions(exclusiveModelCompleteServiceRequest, exclusiveModelCompleteServiceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| created | Long | 本次chat请求被创建时的时间戳。 |
| model | String | 本次chat请求使用的模型名称。 |
| id | String | 本次调用的唯一标识符。 |
| choices | Array | 模型生成内容的数组，可以包含一个或多个choices对象。 |
| finishReason | String | 完成原因，当取值为stop时表示输出结束。 |
| message | Object | 消息对象。 |
| role | String | 角色信息：   - assistant：表示模型返回 - user：表示用户输入 - system：表示系统默认参数 |
| content | String | 模型推理结输出的内容。 |
| reasoning\_content | String | 带深度思考的模型的思考内容输出，如deepseek-r1, 通义QwQ模型。 |
| usage | Object | 本次chat请求使用的 Token 信息。 |
| total\_tokens | Integer | 输入输出令牌总数，`prompt_tokens`与`completion_tokens`的总和。 |
| prompt\_tokens | Integer | prompt\_tokens 输入的 Token 长度。 |
| completion\_tokens | Integer | completion\_tokens 输出的 Token 长度。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "created" : 1741330331741,
  "model" : "qwen-plus",
  "id" : "ff87fc51-9b39-94ea-81b4-7199ac2d511e",
  "choices" : [ {
    "finishReason" : "stop",
    "message" : {
      "role" : "assistant",
      "content" : "我是来自阿里云的语言模型，我叫通义千问。",
      "reasoning_content" : "思维链内容"
    }
  } ],
  "usage" : {
    "total_tokens" : 24,
    "prompt_tokens" : 20,
    "completion_tokens" : 4
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.limit | 模型限流 | 模型请求限流，请求稍后重试 |
| 400 | model.exceed.error | 模型执行异常 | 大模型执行异常 |
| 500 | model.timeout | 模型超时 | 模型服务超时，请稍后再试 |
| 500 | model.absent | 模型不存在 | 模型不存在，请确认模型是否部署 |
