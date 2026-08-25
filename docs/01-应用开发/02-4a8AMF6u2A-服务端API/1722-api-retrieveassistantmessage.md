---
title: "获取AI助理的消息体"
source_url: "https://open.dingtalk.com/document/development/api-retrieveassistantmessage"
namespace: "development"
slug: "api-retrieveassistantmessage"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 消息 > 获取AI助理的消息体"
doc_id: "KMQF2pIRMS"
updated_at: "2026-03-06 09:22:46"
---

> Source: https://open.dingtalk.com/document/development/api-retrieveassistantmessage
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 消息 > 获取AI助理的消息体
> Updated: 2026-03-06 09:22:46

# 获取AI助理的消息体

根据线程id和消息id，返回对应的消息。访问本接口请申请应用权限进行访问。

> **[!IMPORTANT]**
>
> 本文档已于 2026年 03 月 05 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方企业应用 | 暂不支持 | 暂不支持 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
GET /v1.0/assistant/threads/{threadId}/messages/{messageId} HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| threadId | String | 是 | 消息关联的线程id。 |
| messageId | String | 是 | 消息id。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| id | String | 消息id。 |
| threadId | String | 消息关联的线程id。 |
| createdAt | Long | 消息创建时间，毫秒时间戳。 |
| role | String | 消息角色，枚举值：   - user：用户 - assistant：助理 - tool: 技能 |
| content | Array of Any | 返回的消息内容。  **[!NOTE]**    如果消息格式是text，则其中map的key值就是text，其中的value对应的是user或者assistant、tool角色的文本内容，annotations为消息的扩展字段，其中的tool表示运行过程中会调用的工具名称。 |
| assisantId | String | 消息关联的助理id。 |
| runId | String | 消息关联的运行任务id。 |
| object | String | 对象类型，默认为thread.message。 |
| metadata | Map | 保留字段，用于扩展使用，暂无实际意义。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/assistant/threads/thread_message_95f***abb/messages/message_801***c52a HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token123
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
    public static com.aliyun.dingtalkassistant_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkassistant_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkassistant_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantMessageHeaders retrieveAssistantMessageHeaders = new com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantMessageHeaders();
        retrieveAssistantMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.retrieveAssistantMessageWithOptions("thread_message_95f***abb", "message_801***c52a", retrieveAssistantMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.assistant_1_0.client import Client as dingtalkassistant_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.assistant_1_0 import models as dingtalkassistant__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkassistant_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkassistant_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        retrieve_assistant_message_headers = dingtalkassistant__1__0_models.RetrieveAssistantMessageHeaders()
        retrieve_assistant_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.retrieve_assistant_message_with_options('thread_message_95f***abb', 'message_801***c52a', retrieve_assistant_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        retrieve_assistant_message_headers = dingtalkassistant__1__0_models.RetrieveAssistantMessageHeaders()
        retrieve_assistant_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.retrieve_assistant_message_with_options_async('thread_message_95f***abb', 'message_801***c52a', retrieve_assistant_message_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\RetrieveAssistantMessageHeaders;
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
        $retrieveAssistantMessageHeaders = new RetrieveAssistantMessageHeaders([]);
        $retrieveAssistantMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->retrieveAssistantMessageWithOptions("thread_message_95f***abb", "message_801***c52a", $retrieveAssistantMessageHeaders, new RuntimeOptions([]));
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
  dingtalkassistant_1_0  "github.com/alibabacloud-go/dingtalk/assistant_1_0"
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
func CreateClient () (_result *dingtalkassistant_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkassistant_1_0.Client{}
  _result, _err = dingtalkassistant_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  retrieveAssistantMessageHeaders := &dingtalkassistant_1_0.RetrieveAssistantMessageHeaders{}
  retrieveAssistantMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RetrieveAssistantMessageWithOptions(tea.String("thread_message_95f***abb"), tea.String("message_801***c52a"), retrieveAssistantMessageHeaders, &util.RuntimeOptions{})
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
const dingtalkassistant_1_0 = require('@alicloud/dingtalk/assistant_1_0');
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
    return new dingtalkassistant_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let retrieveAssistantMessageHeaders = new dingtalkassistant_1_0.RetrieveAssistantMessageHeaders({ });
    retrieveAssistantMessageHeaders.xAcsDingtalkAccessToken = '<your access token>';
    try {
      await client.retrieveAssistantMessageWithOptions('thread_message_95f***abb', 'message_801***c52a', retrieveAssistantMessageHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkassistant_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkassistant_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantMessageHeaders retrieveAssistantMessageHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantMessageHeaders();
            retrieveAssistantMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.RetrieveAssistantMessageWithOptions("thread_message_95f***abb", "message_801***c52a", retrieveAssistantMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "id" : "message_801***c52a",
  "threadId" : "thread_message_95f***abb",
  "createdAt" : 1721980599206,
  "role" : "assistant",
  "content" : [ {
    "type" : "text",
    "text" : {
      "value" : "我将为你写一本小说",
      "annotations" : {
        "tool" : "writer"
      }
    }
  } ],
  "assistantId" : "d748***965",
  "runId" : "run_73d***f2c",
  "object" : "thread.message"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | message.param.invalid | %s | 传入的参数中ThreadId或者MessageId不合法，请检查后重试（E000155） |
| 500 | message.retrieve.exception | %s | 系统异常，请稍后重试(E000189) |
| 500 | message.retrieve.throwable | %s | 系统异常，请稍后重试(E000130) |
| 500 | message.retrieve.error | %s | 系统异常，请稍后重试（E000031） |
