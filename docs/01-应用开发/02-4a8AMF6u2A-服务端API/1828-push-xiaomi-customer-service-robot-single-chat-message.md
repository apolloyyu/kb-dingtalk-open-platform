---
title: "推送小蜜机器人单聊O2O消息"
source_url: "https://open.dingtalk.com/document/development/push-xiaomi-customer-service-robot-single-chat-message"
namespace: "development"
slug: "push-xiaomi-customer-service-robot-single-chat-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 小蜜客服 > 推送小蜜机器人单聊O2O消息"
doc_id: "kSYbxbnvG4"
updated_at: "2025-09-08 19:06:31"
---

> Source: https://open.dingtalk.com/document/development/push-xiaomi-customer-service-robot-single-chat-message
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 小蜜客服 > 推送小蜜机器人单聊O2O消息
> Updated: 2025-09-08 19:06:31

# 推送小蜜机器人单聊O2O消息

调用本接口通过小蜜客服机器人发送O2O（即Online To Offline）线上线下消息。

**使用限制**

- 同一个小蜜客服机器人相同消息的内容同一个用户一天只能接收一次。
- 同一个钉小蜜机器人给同一个用户/群发送消息，一天不得超过50次。

![](https://img.alicdn.com/imgextra/i2/O1CN010fQU0u1PWt3hchRK5_!!6000000001849-2-tps-948-228.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 小蜜客服商业化数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingmi_1.0%23PushRobotMessage) |
| 第三方企业应用 | 暂不支持 | 小蜜客服商业化数据管理权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 小蜜客服商业化数据管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/dingmi/robots/oToMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "chatbotId" : "String",
  "userId" : "String",
  "msgKey" : "String",
  "msgParam" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| chatbotId | String | 是 | 机器人标识，由小蜜客服平台提供，加入小蜜客服咨询群联系负责人提供，参考[联系我们](https://open.dingtalk.com/document/orgapp/overview-xiaomi-message-type)。 |
| userId | String | 是 | 用户的userid。 |
| msgKey | String | 是 | 消息类型，详情可参考[消息类型说明](https://open.dingtalk.com/document/orgapp/message-types-xiaomi-customer-service)。 |
| msgParam | String | 是 | 消息内容。  **[!NOTE]**    需要做base64处理。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | String | 推送queryKey。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/dingmi/robots/oToMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6edsfxxxx
Content-Type:application/json

{
  "chatbotId" : "1234",
  "userId" : "123456abc",
  "msgKey" : "sampleText",
  "msgParam" : "{\"content\":\"helloworld\"}"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdingmi_1_0.*;
import com.aliyun.dingtalkdingmi_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdingmi_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdingmi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdingmi_1_0.Client client = Sample.createClient();
        PushRobotMessageHeaders pushRobotMessageHeaders = new PushRobotMessageHeaders();
        pushRobotMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        PushRobotMessageRequest pushRobotMessageRequest = new PushRobotMessageRequest()
                .setChatbotId("1234")
                .setUserId("123456abc")
                .setMsgKey("sampleText")
                .setMsgParam("{\"content\":\"helloworld\"}");
        try {
            client.pushRobotMessageWithOptions(pushRobotMessageRequest, pushRobotMessageHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.dingmi_1_0.client import Client as dingtalkdingmi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dingmi_1_0 import models as dingtalkdingmi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdingmi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdingmi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        push_robot_message_headers = dingtalkdingmi__1__0_models.PushRobotMessageHeaders()
        push_robot_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        push_robot_message_request = dingtalkdingmi__1__0_models.PushRobotMessageRequest(
            chatbot_id='1234',
            user_id='123456abc',
            msg_key='sampleText',
            msg_param='{"content":"helloworld"}'
        )
        try:
            client.push_robot_message_with_options(push_robot_message_request, push_robot_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        push_robot_message_headers = dingtalkdingmi__1__0_models.PushRobotMessageHeaders()
        push_robot_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        push_robot_message_request = dingtalkdingmi__1__0_models.PushRobotMessageRequest(
            chatbot_id='1234',
            user_id='123456abc',
            msg_key='sampleText',
            msg_param='{"content":"helloworld"}'
        )
        try:
            await client.push_robot_message_with_options_async(push_robot_message_request, push_robot_message_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\PushRobotMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\PushRobotMessageRequest;
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
        $pushRobotMessageHeaders = new PushRobotMessageHeaders([]);
        $pushRobotMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pushRobotMessageRequest = new PushRobotMessageRequest([
            "chatbotId" => "1234",
            "userId" => "123456abc",
            "msgKey" => "sampleText",
            "msgParam" => "{\"content\":\"helloworld\"}"
        ]);
        try {
            $client->pushRobotMessageWithOptions($pushRobotMessageRequest, $pushRobotMessageHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkdingmi_1_0  "github.com/alibabacloud-go/dingtalk/dingmi_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdingmi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdingmi_1_0.Client{}
  _result, _err = dingtalkdingmi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  pushRobotMessageHeaders := &dingtalkdingmi_1_0.PushRobotMessageHeaders{}
  pushRobotMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pushRobotMessageRequest := &dingtalkdingmi_1_0.PushRobotMessageRequest{
    ChatbotId: tea.String("1234"),
    UserId: tea.String("123456abc"),
    MsgKey: tea.String("sampleText"),
    MsgParam: tea.String("{\"content\":\"helloworld\"}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PushRobotMessageWithOptions(pushRobotMessageRequest, pushRobotMessageHeaders, &util.RuntimeOptions{})
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
import dingtalkdingmi_1_0, * as $dingtalkdingmi_1_0 from '@alicloud/dingtalk/dingmi_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdingmi_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdingmi_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let pushRobotMessageHeaders = new $dingtalkdingmi_1_0.PushRobotMessageHeaders({ });
    pushRobotMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let pushRobotMessageRequest = new $dingtalkdingmi_1_0.PushRobotMessageRequest({
      chatbotId: "1234",
      userId: "123456abc",
      msgKey: "sampleText",
      msgParam: "{\"content\":\"helloworld\"}",
    });
    try {
      await client.pushRobotMessageWithOptions(pushRobotMessageRequest, pushRobotMessageHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.PushRobotMessageHeaders pushRobotMessageHeaders = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.PushRobotMessageHeaders();
            pushRobotMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.PushRobotMessageRequest pushRobotMessageRequest = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.PushRobotMessageRequest
            {
                ChatbotId = "1234",
                UserId = "123456abc",
                MsgKey = "sampleText",
                MsgParam = "{\"content\":\"helloworld\"}",
            };
            try
            {
                client.PushRobotMessageWithOptions(pushRobotMessageRequest, pushRobotMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkdingmi__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdingmi_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdingmi_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdingmi_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::PushRobotMessageHeaders> pushRobotMessageHeaders = make_shared<Alibabacloud_Dingtalkdingmi_1_0::PushRobotMessageHeaders>();
  pushRobotMessageHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::PushRobotMessageRequest> pushRobotMessageRequest = make_shared<Alibabacloud_Dingtalkdingmi_1_0::PushRobotMessageRequest>(map<string, boost::any>({
    {"chatbotId", boost::any(string("1234"))},
    {"userId", boost::any(string("123456abc"))},
    {"msgKey", boost::any(string("sampleText"))},
    {"msgParam", boost::any(string("{"content":"helloworld"}"))}
  }));
  try {
    client->pushRobotMessageWithOptions(pushRobotMessageRequest, pushRobotMessageHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : "msgqwewe1"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.illegal | 本接口调用次数超过今日上限，请明日再试 | 调用次数超过限制 |
| 400 | param.illegal | 参数错误 | 接口参数错误 |
| 500 | system.error | 推送失败：%s | 系统错误导致推送失败 |
