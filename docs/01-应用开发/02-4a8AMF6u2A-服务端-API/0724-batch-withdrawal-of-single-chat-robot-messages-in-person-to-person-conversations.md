---
title: "批量撤回人与人会话中机器人消息"
source_url: "https://open.dingtalk.com/document/development/batch-withdrawal-of-single-chat-robot-messages-in-person-to-person-conversations"
namespace: "development"
slug: "batch-withdrawal-of-single-chat-robot-messages-in-person-to-person-conversations"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 消息撤回 > 批量撤回人与人会话中机器人消息"
doc_id: "4sQMa1PPDS"
updated_at: "2026-06-05 13:49:04"
---

> Source: https://open.dingtalk.com/document/development/batch-withdrawal-of-single-chat-robot-messages-in-person-to-person-conversations
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 消息撤回 > 批量撤回人与人会话中机器人消息
> Updated: 2026-06-05 13:49:04

# 批量撤回人与人会话中机器人消息

调用本接口，根据会话ID，机器人编码和消息ID列表，实现批量撤回人与人会话中的机器人消息，适用于撤回企业消息发送错误的场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/privateChatMessages/batchRecall |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_robot\_sendmsg-企业内机器人发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 会话ID，需要与[人与人会话中机器人发送普通消息](0715-the-robot-sends-ordinary-messages-in-a-person-to-person-conversation.md)接口或[创建并投放卡片](0783-create-and-deliver-cards.md)接口使用的openConversationId保持一致。 |
| robotCode | String | 是 | 机器人的编码，可参考[机器人 ID](https://open.dingtalk.com/document/development/robot-overview)。  需要与[人与人会话中机器人发送普通消息](0715-the-robot-sends-ordinary-messages-in-a-person-to-person-conversation.md)接口使用的robotCode保持一致。 |
| processQueryKeys | Array of String | 是 | 消息id。   - 企业内部应用，可通过[创建并投放卡片](0783-create-and-deliver-cards.md)接口或[人与人会话中机器人发送普通消息](0715-the-robot-sends-ordinary-messages-in-a-person-to-person-conversation.md)接口，获取`processQueryKey`参数值。 |

### 请求示例

HTTP

```
POST /v1.0/robot/privateChatMessages/batchRecall HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:8ca04016xxx
Content-Type:application/json

{
  "openConversationId" : "cidfCSpXXXXXXXXXXXchatbotId",
  "robotCode" : "dingzxcifuvdfbvegdf",
  "processQueryKeys" : [ "b5fe11095f46315d8d30d3f8XXXXXX" ]
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
    public static com.aliyun.dingtalkrobot_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrobot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrobot_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrobot_1_0.models.BatchRecallPrivateChatHeaders batchRecallPrivateChatHeaders = new com.aliyun.dingtalkrobot_1_0.models.BatchRecallPrivateChatHeaders();
        batchRecallPrivateChatHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.BatchRecallPrivateChatRequest batchRecallPrivateChatRequest = new com.aliyun.dingtalkrobot_1_0.models.BatchRecallPrivateChatRequest()
                .setOpenConversationId("cidfCSpXXXXXXXXXXXchatbotId")
                .setRobotCode("dingzxcifuvdfbvegdf")
                .setProcessQueryKeys(java.util.Arrays.asList(
                    "b5fe11095f46315d8d30d3f8XXXXXX"
                ));
        try {
            client.batchRecallPrivateChatWithOptions(batchRecallPrivateChatRequest, batchRecallPrivateChatHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import sys

from typing import List

from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrobot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrobot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_recall_private_chat_headers = dingtalkrobot__1__0_models.BatchRecallPrivateChatHeaders()
        batch_recall_private_chat_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_recall_private_chat_request = dingtalkrobot__1__0_models.BatchRecallPrivateChatRequest(
            open_conversation_id='cidfCSpXXXXXXXXXXXchatbotId',
            robot_code='dingzxcifuvdfbvegdf',
            process_query_keys=[
                'b5fe11095f46315d8d30d3f8XXXXXX'
            ]
        )
        try:
            client.batch_recall_private_chat_with_options(batch_recall_private_chat_request, batch_recall_private_chat_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_recall_private_chat_headers = dingtalkrobot__1__0_models.BatchRecallPrivateChatHeaders()
        batch_recall_private_chat_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_recall_private_chat_request = dingtalkrobot__1__0_models.BatchRecallPrivateChatRequest(
            open_conversation_id='cidfCSpXXXXXXXXXXXchatbotId',
            robot_code='dingzxcifuvdfbvegdf',
            process_query_keys=[
                'b5fe11095f46315d8d30d3f8XXXXXX'
            ]
        )
        try:
            await client.batch_recall_private_chat_with_options_async(batch_recall_private_chat_request, batch_recall_private_chat_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchRecallPrivateChatHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchRecallPrivateChatRequest;
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
        $batchRecallPrivateChatHeaders = new BatchRecallPrivateChatHeaders([]);
        $batchRecallPrivateChatHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchRecallPrivateChatRequest = new BatchRecallPrivateChatRequest([
            "openConversationId" => "cidfCSpXXXXXXXXXXXchatbotId",
            "robotCode" => "dingzxcifuvdfbvegdf",
            "processQueryKeys" => [
                "b5fe11095f46315d8d30d3f8XXXXXX"
            ]
        ]);
        try {
            $client->batchRecallPrivateChatWithOptions($batchRecallPrivateChatRequest, $batchRecallPrivateChatHeaders, new RuntimeOptions([]));
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
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkrobot_1_0  "github.com/alibabacloud-go/dingtalk/robot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrobot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrobot_1_0.Client{}
  _result, _err = dingtalkrobot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchRecallPrivateChatHeaders := &dingtalkrobot_1_0.BatchRecallPrivateChatHeaders{}
  batchRecallPrivateChatHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchRecallPrivateChatRequest := &dingtalkrobot_1_0.BatchRecallPrivateChatRequest{
    OpenConversationId: tea.String("cidfCSpXXXXXXXXXXXchatbotId"),
    RobotCode: tea.String("dingzxcifuvdfbvegdf"),
    ProcessQueryKeys: []*string{tea.String("b5fe11095f46315d8d30d3f8XXXXXX")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchRecallPrivateChatWithOptions(batchRecallPrivateChatRequest, batchRecallPrivateChatHeaders, &util.RuntimeOptions{})
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
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkrobot_1_0, * as $dingtalkrobot_1_0 from '@alicloud/dingtalk/robot_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrobot_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrobot_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let batchRecallPrivateChatHeaders = new $dingtalkrobot_1_0.BatchRecallPrivateChatHeaders({ });
    batchRecallPrivateChatHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let batchRecallPrivateChatRequest = new $dingtalkrobot_1_0.BatchRecallPrivateChatRequest({
      openConversationId: "cidfCSpXXXXXXXXXXXchatbotId",
      robotCode: "dingzxcifuvdfbvegdf",
      processQueryKeys: [
        "b5fe11095f46315d8d30d3f8XXXXXX"
      ],
    });
    try {
      await client.batchRecallPrivateChatWithOptions(batchRecallPrivateChatRequest, batchRecallPrivateChatHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

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
        public static AlibabaCloud.SDK.Dingtalkrobot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrobot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallPrivateChatHeaders batchRecallPrivateChatHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallPrivateChatHeaders();
            batchRecallPrivateChatHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallPrivateChatRequest batchRecallPrivateChatRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallPrivateChatRequest
            {
                OpenConversationId = "cidfCSpXXXXXXXXXXXchatbotId",
                RobotCode = "dingzxcifuvdfbvegdf",
                ProcessQueryKeys = new List<string>
                {
                    "b5fe11095f46315d8d30d3f8XXXXXX"
                },
            };
            try
            {
                client.BatchRecallPrivateChatWithOptions(batchRecallPrivateChatRequest, batchRecallPrivateChatHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| successResult | Array of String | 撤回成功的消息id。 |
| failedResult | Map<String, String> | 撤回失败的消息id列表及原因。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "successResult" : [ "5fe11095f46315d8d30d3f8XXXXXX" ],
  "failedResult" : {
    "key" : "SYSTEM_ERROR"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.openConversationId | %s | 无效的openConversationId，请检查openConversationId是否正确 |
| 400 | invalidParameter.robotCode | %s | 无效的robotCode，请检查机器人是否在群内 |
| 400 | invalidParameter.processQueryKeys.overMax | %s | processQueryKeys超过数量上限20，请将processQueryKeys拆分成多个长度不超过20的数组，分批次调用此接口 |
| 400 | not.allowed.robotCode | %s | 未被授权的robotCode |
| 400 | invalidParameter.param.invalid | %s | 参数不合法，请检查参数是否为空 |
| 400 | invalidParameter.robotCode.notExsit | %s | 机器人不存在，请检查会话内是否安装了robotCode对应的机器人 |
| 400 | miss.chatbotId | %s | 缺少robotCode |
| 400 | invalidParameter.processQueryKey.missing | %s | 缺少processQueryKey |
| 400 | invalid.processQueryKey | %s | 无效的processQueryKey，请检查processQueryKey是否正确 |
| 400 | miss.openConversationId | %s | 缺少openConversationId |
| 400 | bot.stopped | %s | 群机器人已经停用 |
| 400 | template.not.existed | %s | 机器人模板不存在 |
| 400 | template.stopped | %s | 机器人模板已经停用 |
| 400 | unauthorized | %s | 未授权，不允许操作 |
| 400 | resource.not.found | %s | 机器人不存在 |
| 500 | system.error | %s | 未知的系统错误 |
