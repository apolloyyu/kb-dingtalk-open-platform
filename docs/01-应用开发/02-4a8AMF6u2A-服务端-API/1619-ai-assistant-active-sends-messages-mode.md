---
title: "AI助理发消息（主动发送模式）"
source_url: "https://open.dingtalk.com/document/development/ai-assistant-active-sends-messages-mode"
namespace: "development"
slug: "ai-assistant-active-sends-messages-mode"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 智能交互 > AI助理发消息（主动发送模式）"
doc_id: "qvurwjsHWP"
updated_at: "2026-08-25 09:39:14"
---

> Source: https://open.dingtalk.com/document/development/ai-assistant-active-sends-messages-mode
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 智能交互 > AI助理发消息（主动发送模式）
> Updated: 2026-08-25 09:39:14

# AI助理发消息（主动发送模式）

开发者可以通过钉钉 AI 助理主动给用户发送自定义智能消息。主动发送可以分为：分步发送（预备、更新和结束）和直接发送。本文档介绍的接口是直接发送接口，调用该接口就可以通过 AI 助理发送一条智能消息。

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
POST /v1.0/aiInteraction/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "openConversationId" : "String",
  "unionId" : "String",
  "contentType" : "String",
  "content" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 否 | 会话 ID。支持单聊和群聊场景。 |
| unionId | String | 否 | 用户 ID。仅用于单聊场景。 |
| contentType | String | 是 | 消息体类型：   - **basic\_card\_schema**：普通卡片（Schema模式） |
| content | String | 否 | 消息体内容，与消息体类型对应，必须是 **JSON** 格式。详见[普通卡片（Schema模式）](1620-message-content-filling-guidance.md#d1806d6452z8o)。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 请求结果。 |
| success | Boolean | 接口调用是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/aiInteraction/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:82c1****54aa
Content-Type:application/json

{
  "openConversationId" : "cidxxxx",
  "contentType" : "basic_card_schema",
  "content" : "{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}"
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
        com.aliyun.dingtalkai_interaction_1_0.models.SendHeaders sendHeaders = new com.aliyun.dingtalkai_interaction_1_0.models.SendHeaders();
        sendHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkai_interaction_1_0.models.SendRequest sendRequest = new com.aliyun.dingtalkai_interaction_1_0.models.SendRequest()
                .setOpenConversationId("cidxxxx")
                .setUnionId("sFGAuxxxxxx")
                .setContentType("ai_card")
                .setContent("{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}");
        try {
            client.sendWithOptions(sendRequest, sendHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        send_headers = dingtalkai_interaction__1__0_models.SendHeaders()
        send_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_request = dingtalkai_interaction__1__0_models.SendRequest(
            open_conversation_id='cidxxxx',
            union_id='sFGAuxxxxxx',
            content_type='ai_card',
            content='{"header": {"title": {"type":"text","text":"这是 basic_card_schema 模式卡片"},"logo":"@lALPDfJ6V_FPDmvNAfTNAfQ"},"contents":[{"type":"text","text":"小心感冒~","id": "text_1711949486176"}]}'
        )
        try:
            client.send_with_options(send_request, send_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_headers = dingtalkai_interaction__1__0_models.SendHeaders()
        send_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_request = dingtalkai_interaction__1__0_models.SendRequest(
            open_conversation_id='cidxxxx',
            union_id='sFGAuxxxxxx',
            content_type='ai_card',
            content='{"header": {"title": {"type":"text","text":"这是 basic_card_schema 模式卡片"},"logo":"@lALPDfJ6V_FPDmvNAfTNAfQ"},"contents":[{"type":"text","text":"小心感冒~","id": "text_1711949486176"}]}'
        )
        try:
            await client.send_with_options_async(send_request, send_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vai_interaction_1_0\Models\SendHeaders;
use AlibabaCloud\SDK\Dingtalk\Vai_interaction_1_0\Models\SendRequest;
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
        $sendHeaders = new SendHeaders([]);
        $sendHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendRequest = new SendRequest([
            "openConversationId" => "cidxxxx",
            "unionId" => "sFGAuxxxxxx",
            "contentType" => "ai_card",
            "content" => "{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}"
        ]);
        try {
            $client->sendWithOptions($sendRequest, $sendHeaders, new RuntimeOptions([]));
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

  sendHeaders := &dingtalkaiinteraction_1_0.SendHeaders{}
  sendHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendRequest := &dingtalkaiinteraction_1_0.SendRequest{
    OpenConversationId: tea.String("cidxxxx"),
    UnionId: tea.String("sFGAuxxxxxx"),
    ContentType: tea.String("ai_card"),
    Content: tea.String("{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendWithOptions(sendRequest, sendHeaders, &util.RuntimeOptions{})
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
    let sendHeaders = new dingtalkaiInteraction_1_0.SendHeaders({ });
    sendHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let sendRequest = new dingtalkaiInteraction_1_0.SendRequest({
      openConversationId: 'cidxxxx',
      unionId: 'sFGAuxxxxxx',
      contentType: 'ai_card',
      content: '{"header": {"title": {"type":"text","text":"这是 basic_card_schema 模式卡片"},"logo":"@lALPDfJ6V_FPDmvNAfTNAfQ"},"contents":[{"type":"text","text":"小心感冒~","id": "text_1711949486176"}]}',
    });
    try {
      await client.sendWithOptions(sendRequest, sendHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.SendHeaders sendHeaders = new AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.SendHeaders();
            sendHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.SendRequest sendRequest = new AlibabaCloud.SDK.Dingtalkai_interaction_1_0.Models.SendRequest
            {
                OpenConversationId = "cidxxxx",
                UnionId = "sFGAuxxxxxx",
                ContentType = "ai_card",
                Content = "{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}",
            };
            try
            {
                client.SendWithOptions(sendRequest, sendHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## 参数补充说明

- 如果你的发消息场景是单聊，你可以这么请求：

  ```
  {
    "unionId": "sFxxxx",
    "contentType": "basic_card_schema",
    "content" : "{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}"
  }
  ```
- 如果你的发消息场景是群聊，你可以这么请求：

  ```
  {
    "openConversationId": "cidxxx",
    "contentType": "basic_card_schema",
    "content" : "{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}"
  }
  ```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.param | invalid openConversationId | 会话 ID 不合法。 |
| 400 | invalid.param | invalid unionId | 用户 ID 不合法。 |
| 400 | invalid.param | ai assistant not found | 无法找到 AI 助理。请使用 AI 助理的 ClientID/ClientSecret 获取访问凭证。 |
| 400 | invalid.content.type | invalid content type | 消息体类型不合法。 |
| 500 | system.error | system error | 未知的系统内部错误。 |
