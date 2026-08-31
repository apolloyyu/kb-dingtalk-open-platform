---
title: "AI 助理结束发消息（主动发送模式）"
source_url: "https://open.dingtalk.com/document/development/api-finish"
namespace: "development"
slug: "api-finish"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 智能交互 > AI 助理结束发消息（主动发送模式）"
doc_id: "IIwWFiBV62"
updated_at: "2026-08-25 09:39:13"
---

> Source: https://open.dingtalk.com/document/development/api-finish
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 智能交互 > AI 助理结束发消息（主动发送模式）
> Updated: 2026-08-25 09:39:13

# AI 助理结束发消息（主动发送模式）

开发者可以通过钉钉 AI 助理主动给用户发送自定义智能消息。主动发送的步骤可以分为：[预备](1616-api-prepare.md)、[更新](1617-the-ai-assistant-updates-active-message-sending-mode.md)和[结束](#)三步。本文档介绍的接口是结束接口，该接口能结束消息框的更新。

> **[!IMPORTANT]**
>
> 本接口仅保持现有功能，不再新增支持其他能力。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 暂不支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/aiInteraction/finish HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "conversationToken" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conversationToken | String | 是 | 会话凭证。  **[!NOTE]**  会话凭证中保存了会话的上下文信息，包括：聊天场景（如单聊、群聊等）、聊天对象（如 AI 助理、机器人等）、用户信息等。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 请求结果。 |
| success | Boolean | 接口调用是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/aiInteraction/finish HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:82c1****54aa
Content-Type:application/json

{
  "conversationToken" : "ctxxxx"
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
    public static com.aliyun.dingtalkai_interaction_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkai_interaction_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkai_interaction_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkai_interaction_1_0.models.FinishHeaders finishHeaders = new com.aliyun.dingtalkai_interaction_1_0.models.FinishHeaders();
        finishHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkai_interaction_1_0.models.FinishRequest finishRequest = new com.aliyun.dingtalkai_interaction_1_0.models.FinishRequest()
                .setConversationToken("ctxxxx");
        try {
            client.finishWithOptions(finishRequest, finishHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.aiInteraction_1_0.client import Client as dingtalkaiInteraction_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.aiInteraction_1_0 import models as dingtalkai_interaction__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkaiInteraction_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkaiInteraction_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        finish_headers = dingtalkai_interaction__1__0_models.FinishHeaders()
        finish_headers.x_acs_dingtalk_access_token = '<your access token>'
        finish_request = dingtalkai_interaction__1__0_models.FinishRequest(
            conversation_token='ctxxxx'
        )
        try:
            client.finish_with_options(finish_request, finish_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        finish_headers = dingtalkai_interaction__1__0_models.FinishHeaders()
        finish_headers.x_acs_dingtalk_access_token = '<your access token>'
        finish_request = dingtalkai_interaction__1__0_models.FinishRequest(
            conversation_token='ctxxxx'
        )
        try:
            await client.finish_with_options_async(finish_request, finish_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vai_interaction_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vai_interaction_1_0\Models\FinishHeaders;
use AlibabaCloud\SDK\Dingtalk\Vai_interaction_1_0\Models\FinishRequest;
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
        $finishHeaders = new FinishHeaders([]);
        $finishHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $finishRequest = new FinishRequest([
            "conversationToken" => "ctxxxx"
        ]);
        try {
            $client->finishWithOptions($finishRequest, $finishHeaders, new RuntimeOptions([]));
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
  dingtalkaiinteraction_1_0  "github.com/alibabacloud-go/dingtalk/aiInteraction_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkaiinteraction_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkaiinteraction_1_0.Client{}
  _result, _err = dingtalkaiinteraction_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  finishHeaders := &dingtalkaiinteraction_1_0.FinishHeaders{}
  finishHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  finishRequest := &dingtalkaiinteraction_1_0.FinishRequest{
    ConversationToken: tea.String("ctxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.FinishWithOptions(finishRequest, finishHeaders, &util.RuntimeOptions{})
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
const dingtalkaiInteraction_1_0 = require('@alicloud/dingtalk/aiInteraction_1_0');
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
    return new dingtalkaiInteraction_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let finishHeaders = new dingtalkaiInteraction_1_0.FinishHeaders({ });
    finishHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let finishRequest = new dingtalkaiInteraction_1_0.FinishRequest({
      conversationToken: 'ctxxxx',
    });
    try {
      await client.finishWithOptions(finishRequest, finishHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.FinishHeaders finishHeaders = new AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.FinishHeaders();
            finishHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.FinishRequest finishRequest = new AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.FinishRequest
            {
                ConversationToken = "ctxxxx",
            };
            try
            {
                client.FinishWithOptions(finishRequest, finishHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "success" : true
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.conversation.token | invalid conversation token | 不合法的会话凭证。 |
| 500 | system.error | system error | 未知的系统内部错误。 |
