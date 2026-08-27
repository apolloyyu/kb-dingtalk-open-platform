---
title: "在钉钉客联互通群中使用钉内账号发送消息"
source_url: "https://open.dingtalk.com/document/development/send-b2c-messages"
namespace: "development"
slug: "send-b2c-messages"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 在钉钉客联互通群中使用钉内账号发送消息"
doc_id: "QsuyJ7hnEy"
updated_at: "2026-07-21 10:13:06"
---

> Source: https://open.dingtalk.com/document/development/send-b2c-messages
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 在钉钉客联互通群中使用钉内账号发送消息
> Updated: 2026-07-21 10:13:06

# 在钉钉客联互通群中使用钉内账号发送消息

调用本接口，实现钉内账号给钉外账号或者互通群发送消息。

### 接口使用说明

- 该接口**已经暂停新客户支持**，进入EOL（end of life）阶段，敬请期待新的开放能力支持。
- 调用本接口之前，需要开通钉钉互联应用。

### 消息格式说明

本接口发送消息，只支持文本和链接类型消息，消息格式参考如下：

- **文本消息**

```
{
     "text": {
         "content": "hello world"
     }
}
```

- **链接消息**

```
{
    "link":{
      "messageUrl":"http://dingtalk.com",
      "picUrl":"http://****.png",
      "title":"钉钉",
      "text":"钉钉客联"
    }
}
```

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23sendDingMessage) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23sendDingMessage) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interconnections/dingMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "senderId" : "String",
  "receiverId" : "String",
  "openConversationId" : "String",
  "messageType" : "String",
  "message" : "String",
  "code" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| senderId | String | 是 | 消息发送者，钉内账号userId，长度限制为1～64个字符，例如：1745\*\*\*\*8777。 |
| receiverId | String | 否 | 钉外账号在业务系统内的唯一标志，调用[创建钉钉客联钉外账号](1847-create-bc-account-association.md)接口获取，长度限制为1～64个字符，例如：1107\*\*\*\*2120。  **[!NOTE]**    单聊场景必填，可实现钉内账号向钉外账号发送单聊消息。 |
| openConversationId | String | 否 | 群会话openConversationId，可调用[创建钉钉客联普通互通群](1848-create-common-group-new-version.md) / [创建钉钉客联两人互通群](1849-creating-two-groups-of-people.md)接口获取，长度限制为1～32个字符，例如：14da\*\*\*\*2760。  **[!NOTE]**    群聊场景必填，可实现钉内账号向互通群内发送群聊信息。 |
| messageType | String | 是 | 消息类型，取值：   - **text**：文本类型 - **link**：链接类型 |
| message | String | 是 | 消息内容。  **[!NOTE]**    请参考本文**消息格式说明**。 |
| code | String | 是 | 发送者在钉钉客联应用内的个人授权码，获取方式：https://login.dingtalk.com/oauth2/auth?redirect\_uri=https%3A%2F%2Fexample.org%2Fa%2Fb&response\_type=code&client\_id=suitezl\*\*\*pimsjn&scope=openid corpid&state=dddd&prompt=consent&corpId=ding3xxx   - **redirect\_uri**地址传企业目标页面地址，必须UrlEncode处理。 - **response\_type**为固定值code。 - **client\_id**为固定值，是钉钉客联应用的suiteKey。 - **scope**可以固定为openid corpid。（中间有空格） - **corpId**传发送者所在企业的corpId值。   **[!NOTE]**    \*\* 每发送一条消息后，都需要重新获取一个新的授权码\*\*。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| requestId | String | 本次发送的请求消息Id。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/dingMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "senderId" : "1745****8777",
  "receiverId" : "1107****2120",
  "openConversationId" : "14da****2760",
  "messageType" : "text",
  "message" : "{      \"text\": {          \"content\": \"hello world\"      } }",
  "code" : "06f4****d1ec"
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
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_1_0.models.SendDingMessageHeaders sendDingMessageHeaders = new com.aliyun.dingtalkim_1_0.models.SendDingMessageHeaders();
        sendDingMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.SendDingMessageRequest sendDingMessageRequest = new com.aliyun.dingtalkim_1_0.models.SendDingMessageRequest()
                .setSenderId("1745****8777")
                .setReceiverId("1107****2120")
                .setOpenConversationId("14da****2760")
                .setMessageType("text")
                .setMessage("{      \"text\": {          \"content\": \"hello world\"      } }")
                .setCode("06f4****d1ec");
        try {
            client.sendDingMessageWithOptions(sendDingMessageRequest, sendDingMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.im_1_0.client import Client as dingtalkim_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.im_1_0 import models as dingtalkim__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkim_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_ding_message_headers = dingtalkim__1__0_models.SendDingMessageHeaders()
        send_ding_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_ding_message_request = dingtalkim__1__0_models.SendDingMessageRequest(
            sender_id='1745****8777',
            receiver_id='1107****2120',
            open_conversation_id='14da****2760',
            message_type='text',
            message='{      "text": {          "content": "hello world"      } }',
            code='06f4****d1ec'
        )
        try:
            client.send_ding_message_with_options(send_ding_message_request, send_ding_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_ding_message_headers = dingtalkim__1__0_models.SendDingMessageHeaders()
        send_ding_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_ding_message_request = dingtalkim__1__0_models.SendDingMessageRequest(
            sender_id='1745****8777',
            receiver_id='1107****2120',
            open_conversation_id='14da****2760',
            message_type='text',
            message='{      "text": {          "content": "hello world"      } }',
            code='06f4****d1ec'
        )
        try:
            await client.send_ding_message_with_options_async(send_ding_message_request, send_ding_message_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendDingMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendDingMessageRequest;
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
        $sendDingMessageHeaders = new SendDingMessageHeaders([]);
        $sendDingMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendDingMessageRequest = new SendDingMessageRequest([
            "senderId" => "1745****8777",
            "receiverId" => "1107****2120",
            "openConversationId" => "14da****2760",
            "messageType" => "text",
            "message" => "{      \"text\": {          \"content\": \"hello world\"      } }",
            "code" => "06f4****d1ec"
        ]);
        try {
            $client->sendDingMessageWithOptions($sendDingMessageRequest, $sendDingMessageHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
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
func CreateClient () (_result *dingtalkim_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkim_1_0.Client{}
  _result, _err = dingtalkim_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendDingMessageHeaders := &dingtalkim_1_0.SendDingMessageHeaders{}
  sendDingMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendDingMessageRequest := &dingtalkim_1_0.SendDingMessageRequest{
    SenderId: tea.String("1745****8777"),
    ReceiverId: tea.String("1107****2120"),
    OpenConversationId: tea.String("14da****2760"),
    MessageType: tea.String("text"),
    Message: tea.String("{      \"text\": {          \"content\": \"hello world\"      } }"),
    Code: tea.String("06f4****d1ec"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendDingMessageWithOptions(sendDingMessageRequest, sendDingMessageHeaders, &util.RuntimeOptions{})
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
const dingtalkim_1_0 = require('@alicloud/dingtalk/im_1_0');
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
    return new dingtalkim_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let sendDingMessageHeaders = new dingtalkim_1_0.SendDingMessageHeaders({ });
    sendDingMessageHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let sendDingMessageRequest = new dingtalkim_1_0.SendDingMessageRequest({
      senderId: '1745****8777',
      receiverId: '1107****2120',
      openConversationId: '14da****2760',
      messageType: 'text',
      message: '{      "text": {          "content": "hello world"      } }',
      code: '06f4****d1ec',
    });
    try {
      await client.sendDingMessageWithOptions(sendDingMessageRequest, sendDingMessageHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkim_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkim_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkim_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendDingMessageHeaders sendDingMessageHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendDingMessageHeaders();
            sendDingMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendDingMessageRequest sendDingMessageRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendDingMessageRequest
            {
                SenderId = "1745****8777",
                ReceiverId = "1107****2120",
                OpenConversationId = "14da****2760",
                MessageType = "text",
                Message = "{      \"text\": {          \"content\": \"hello world\"      } }",
                Code = "06f4****d1ec",
            };
            try
            {
                client.SendDingMessageWithOptions(sendDingMessageRequest, sendDingMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "requestId" : "437B****7DB7"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否同时传了会话id和接收者id或都没传 | 输入参数有误，请检查是否同时传了会话id和接收者id或都没传 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | service.nonexist | 钉内账号不存在，请检查 | 钉内账号不存在，请检查 |
| 400 | group.nonexist | 群不存在，请检查 | 群不存在，请检查 |
| 400 | accesstoken.expired | 用户accessToken过期 | 用户accessToken过期 |
| 400 | group.notReady | 群会话仍在创建中，请稍后重试 | 群会话仍在创建中，请稍后重试 |
| 400 | member.nonexist | 发送者不在群里，请检查 | 发送者不在群里，请检查 |
| 500 | message.send.error | 发送消息失败 | 发送消息失败 |
| 500 | system.error | 系统异常 | 系统异常 |
