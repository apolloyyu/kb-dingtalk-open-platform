---
title: "发送服务群消息"
source_url: "https://open.dingtalk.com/document/development/service-group-message-sending-interface"
namespace: "development"
slug: "service-group-message-sending-interface"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 发送服务群消息"
doc_id: "oMZLOhjdmK"
updated_at: "2026-06-04 19:11:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-message-sending-interface
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 服务群 > 发送服务群消息
> Updated: 2026-06-04 19:11:22

# 发送服务群消息

调用本接口，根据服务群ID给指定的服务群发送群消息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/messages/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ServiceGroup.Message.Send-场景服务群发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| targetOpenConversationId | String | 是 | 开放群ID，可调用[创建场景服务群](1120-create-a-scenario-service-group.md)接口获取openConversationId参数值。 |
| title | String | 是 | 发送消息的标题。 |
| content | String | 是 | 发送消息的内容。 |
| isAtAll | Boolean | 否 | 是否 at所有人：   - **true**：是 - **false**：否 |
| atMobiles | Array of String | 否 | 被@人的手机号列表。 |
| atDingtalkIds | Array of String | 否 | 被@人的dingtalkId列表。 |
| atUnionIds | Array of String | 否 | 被@人的unionId列表，可通过[查询用户详情](0056-query-user-details.md)接口获取用户unionId值。 |
| receiverMobiles | Array of String | 否 | 接收者的手机号列表。 |
| receiverDingtalkIds | Array of String | 否 | 接收者的dingtalkId列表。 |
| receiverUnionIds | Array of String | 否 | 接收者unionId列表。 |
| messageType | String | 是 | 消息类型，取值。   - **MARKDOWN**：markdown消息 - **ACTIONCARD**：卡片消息     markdown消息不能使用消息按钮。 |
| btnOrientation | String | 否 | 排列方式：   - **0**：按钮竖直排列 - **1**：按钮横向排列 |
| btns | Array | 否 | actionCard按钮。 |
| actionURL | String | 否 | 按钮跳转地址。 |
| title | String | 否 | 按钮名称。 |
| hasContentLinks | Boolean | 否 | 消息内容是否含有链接。   - **false**：当btns只有1个按钮，移动端点击消息卡片的任意内容将只会跳转到按钮的链接。 - **true**：无论btns多少，内容中的链接与按钮链接互不影响。 |

### 请求示例

HTTP

```
POST /v1.0/serviceGroup/messages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2bfa9c2xxxx
Content-Type:application/json

{
  "targetOpenConversationId" : "cidxxxxx==",
  "title" : "服务提醒",
  "content" : "你有新的任务待审批",
  "atMobiles" : [ "15011111111" ],
  "atDingtalkIds" : [ "$:LWCP_v1:$xxxxxxx==" ],
  "atUnionIds" : [ "JuSi1Jkl" ],
  "receiverMobiles" : [ "15011111111" ],
  "receiverDingtalkIds" : [ "$:LWCP_v1:$xxxxxxx==" ],
  "receiverUnionIds" : [ "JuSi1Jkl" ],
  "messageType" : "MARKDOWN",
  "btnOrientation" : "0",
  "btns" : [ {
    "actionURL" : "http://www.dingtalk.com",
    "title" : "测试按钮"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkservice_group_1_0.*;
import com.aliyun.dingtalkservice_group_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkservice_group_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkservice_group_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkservice_group_1_0.Client client = Sample.createClient();
        SendServiceGroupMessageHeaders sendServiceGroupMessageHeaders = new SendServiceGroupMessageHeaders();
        sendServiceGroupMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendServiceGroupMessageRequest.SendServiceGroupMessageRequestBtns btns0 = new SendServiceGroupMessageRequest.SendServiceGroupMessageRequestBtns()
                .setActionURL("http://www.dingtalk.com")
                .setTitle("测试按钮");
        SendServiceGroupMessageRequest sendServiceGroupMessageRequest = new SendServiceGroupMessageRequest()
                .setTargetOpenConversationId("cidxxxxx==")
                .setTitle("服务提醒")
                .setContent("你有新的任务待审批")
                .setAtMobiles(java.util.Arrays.asList(
                    "15011111111"
                ))
                .setAtDingtalkIds(java.util.Arrays.asList(
                    "$:LWCP_v1:$xxxxxxx=="
                ))
                .setAtUnionIds(java.util.Arrays.asList(
                    "JuSi1Jkl"
                ))
                .setReceiverMobiles(java.util.Arrays.asList(
                    "15011111111"
                ))
                .setReceiverDingtalkIds(java.util.Arrays.asList(
                    "$:LWCP_v1:$xxxxxxx=="
                ))
                .setReceiverUnionIds(java.util.Arrays.asList(
                    "JuSi1Jkl"
                ))
                .setMessageType("MARKDOWN")
                .setBtnOrientation("0")
                .setBtns(java.util.Arrays.asList(
                    btns0
                ));
        try {
            client.sendServiceGroupMessageWithOptions(sendServiceGroupMessageRequest, sendServiceGroupMessageHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalkservice_group_1_0.client import Client as dingtalkserviceGroup_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalkservice_group_1_0 import models as dingtalkservice_group__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkserviceGroup_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkserviceGroup_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_service_group_message_headers = dingtalkservice_group__1__0_models.SendServiceGroupMessageHeaders()
        send_service_group_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        btns_0 = dingtalkservice_group__1__0_models.SendServiceGroupMessageRequestBtns(
            action_url='http://www.dingtalk.com',
            title='测试按钮'
        )
        send_service_group_message_request = dingtalkservice_group__1__0_models.SendServiceGroupMessageRequest(
            target_open_conversation_id='cidxxxxx==',
            title='服务提醒',
            content='你有新的任务待审批',
            at_mobiles=[
                '15011111111'
            ],
            at_dingtalk_ids=[
                '$:LWCP_v1:$xxxxxxx=='
            ],
            at_union_ids=[
                'JuSi1Jkl'
            ],
            receiver_mobiles=[
                '15011111111'
            ],
            receiver_dingtalk_ids=[
                '$:LWCP_v1:$xxxxxxx=='
            ],
            receiver_union_ids=[
                'JuSi1Jkl'
            ],
            message_type='MARKDOWN',
            btn_orientation='0',
            btns=[
                btns_0
            ]
        )
        try:
            client.send_service_group_message_with_options(send_service_group_message_request, send_service_group_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_service_group_message_headers = dingtalkservice_group__1__0_models.SendServiceGroupMessageHeaders()
        send_service_group_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        btns_0 = dingtalkservice_group__1__0_models.SendServiceGroupMessageRequestBtns(
            action_url='http://www.dingtalk.com',
            title='测试按钮'
        )
        send_service_group_message_request = dingtalkservice_group__1__0_models.SendServiceGroupMessageRequest(
            target_open_conversation_id='cidxxxxx==',
            title='服务提醒',
            content='你有新的任务待审批',
            at_mobiles=[
                '15011111111'
            ],
            at_dingtalk_ids=[
                '$:LWCP_v1:$xxxxxxx=='
            ],
            at_union_ids=[
                'JuSi1Jkl'
            ],
            receiver_mobiles=[
                '15011111111'
            ],
            receiver_dingtalk_ids=[
                '$:LWCP_v1:$xxxxxxx=='
            ],
            receiver_union_ids=[
                'JuSi1Jkl'
            ],
            message_type='MARKDOWN',
            btn_orientation='0',
            btns=[
                btns_0
            ]
        )
        try:
            await client.send_service_group_message_with_options_async(send_service_group_message_request, send_service_group_message_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendServiceGroupMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendServiceGroupMessageRequest\btns;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendServiceGroupMessageRequest;
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
        $sendServiceGroupMessageHeaders = new SendServiceGroupMessageHeaders([]);
        $sendServiceGroupMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $btns0 = new btns([
            "actionURL" => "http://www.dingtalk.com",
            "title" => "测试按钮"
        ]);
        $sendServiceGroupMessageRequest = new SendServiceGroupMessageRequest([
            "targetOpenConversationId" => "cidxxxxx==",
            "title" => "服务提醒",
            "content" => "你有新的任务待审批",
            "atMobiles" => [
                "15011111111"
            ],
            "atDingtalkIds" => [
                "\$:LWCP_v1:\$xxxxxxx=="
            ],
            "atUnionIds" => [
                "JuSi1Jkl"
            ],
            "receiverMobiles" => [
                "15011111111"
            ],
            "receiverDingtalkIds" => [
                "\$:LWCP_v1:\$xxxxxxx=="
            ],
            "receiverUnionIds" => [
                "JuSi1Jkl"
            ],
            "messageType" => "MARKDOWN",
            "btnOrientation" => "0",
            "btns" => [
                $btns0
            ]
        ]);
        try {
            $client->sendServiceGroupMessageWithOptions($sendServiceGroupMessageRequest, $sendServiceGroupMessageHeaders, new RuntimeOptions([]));
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
  dingtalkservicegroup_1_0  "github.com/alibabacloud-go/dingtalk-service_group_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkservicegroup_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkservicegroup_1_0.Client{}
  _result, _err = dingtalkservicegroup_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendServiceGroupMessageHeaders := &dingtalkservicegroup_1_0.SendServiceGroupMessageHeaders{}
  sendServiceGroupMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  btns0 := &dingtalkservicegroup_1_0.SendServiceGroupMessageRequestBtns{
    ActionURL: tea.String("http://www.dingtalk.com"),
    Title: tea.String("测试按钮"),
  }
  sendServiceGroupMessageRequest := &dingtalkservicegroup_1_0.SendServiceGroupMessageRequest{
    TargetOpenConversationId: tea.String("cidxxxxx=="),
    Title: tea.String("服务提醒"),
    Content: tea.String("你有新的任务待审批"),
    AtMobiles: []*string{tea.String("15011111111")},
    AtDingtalkIds: []*string{tea.String("$:LWCP_v1:$xxxxxxx==")},
    AtUnionIds: []*string{tea.String("JuSi1Jkl")},
    ReceiverMobiles: []*string{tea.String("15011111111")},
    ReceiverDingtalkIds: []*string{tea.String("$:LWCP_v1:$xxxxxxx==")},
    ReceiverUnionIds: []*string{tea.String("JuSi1Jkl")},
    MessageType: tea.String("MARKDOWN"),
    BtnOrientation: tea.String("0"),
    Btns: []*dingtalkservicegroup_1_0.SendServiceGroupMessageRequestBtns{btns0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendServiceGroupMessageWithOptions(sendServiceGroupMessageRequest, sendServiceGroupMessageHeaders, &util.RuntimeOptions{})
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
import dingtalkserviceGroup_1_0, * as $dingtalkserviceGroup_1_0 from '"@alicloud/dingtalk/serviceGroup_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkserviceGroup_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkserviceGroup_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let sendServiceGroupMessageHeaders = new $dingtalkserviceGroup_1_0.SendServiceGroupMessageHeaders({ });
    sendServiceGroupMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let btns0 = new $dingtalkserviceGroup_1_0.SendServiceGroupMessageRequestBtns({
      actionURL: "http://www.dingtalk.com",
      title: "测试按钮",
    });
    let sendServiceGroupMessageRequest = new $dingtalkserviceGroup_1_0.SendServiceGroupMessageRequest({
      targetOpenConversationId: "cidxxxxx==",
      title: "服务提醒",
      content: "你有新的任务待审批",
      atMobiles: [
        "15011111111"
      ],
      atDingtalkIds: [
        "$:LWCP_v1:$xxxxxxx=="
      ],
      atUnionIds: [
        "JuSi1Jkl"
      ],
      receiverMobiles: [
        "15011111111"
      ],
      receiverDingtalkIds: [
        "$:LWCP_v1:$xxxxxxx=="
      ],
      receiverUnionIds: [
        "JuSi1Jkl"
      ],
      messageType: "MARKDOWN",
      btnOrientation: "0",
      btns: [
        btns0
      ],
    });
    try {
      await client.sendServiceGroupMessageWithOptions(sendServiceGroupMessageRequest, sendServiceGroupMessageHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageHeaders sendServiceGroupMessageHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageHeaders();
            sendServiceGroupMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageRequest.SendServiceGroupMessageRequestBtns btns0 = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageRequest.SendServiceGroupMessageRequestBtns
            {
                ActionURL = "http://www.dingtalk.com",
                Title = "测试按钮",
            };
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageRequest sendServiceGroupMessageRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageRequest
            {
                TargetOpenConversationId = "cidxxxxx==",
                Title = "服务提醒",
                Content = "你有新的任务待审批",
                AtMobiles = new List<string>
                {
                    "15011111111"
                },
                AtDingtalkIds = new List<string>
                {
                    "$:LWCP_v1:$xxxxxxx=="
                },
                AtUnionIds = new List<string>
                {
                    "JuSi1Jkl"
                },
                ReceiverMobiles = new List<string>
                {
                    "15011111111"
                },
                ReceiverDingtalkIds = new List<string>
                {
                    "$:LWCP_v1:$xxxxxxx=="
                },
                ReceiverUnionIds = new List<string>
                {
                    "JuSi1Jkl"
                },
                MessageType = "MARKDOWN",
                BtnOrientation = "0",
                Btns = new List<AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendServiceGroupMessageRequest.SendServiceGroupMessageRequestBtns>
                {
                    btns0
                },
            };
            try
            {
                client.SendServiceGroupMessageWithOptions(sendServiceGroupMessageRequest, sendServiceGroupMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkservice_group__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkservice_group_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkservice_group_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::Client> client = make_shared<Alibabacloud_Dingtalkservice_group_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageHeaders> sendServiceGroupMessageHeaders = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageHeaders>();
  sendServiceGroupMessageHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageRequestBtns> btns0 = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageRequestBtns>(map<string, boost::any>({
    {"actionURL", boost::any(string("http://www.dingtalk.com"))},
    {"title", boost::any(string("测试按钮"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageRequest> sendServiceGroupMessageRequest = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageRequest>(map<string, boost::any>({
    {"targetOpenConversationId", boost::any(string("cidxxxxx=="))},
    {"title", boost::any(string("服务提醒"))},
    {"content", boost::any(string("你有新的任务待审批"))},
    {"atMobiles", boost::any(vector<string>({
      "15011111111"
    }))},
    {"atDingtalkIds", boost::any(vector<string>({
      "$:LWCP_v1:$xxxxxxx=="
    }))},
    {"atUnionIds", boost::any(vector<string>({
      "JuSi1Jkl"
    }))},
    {"receiverMobiles", boost::any(vector<string>({
      "15011111111"
    }))},
    {"receiverDingtalkIds", boost::any(vector<string>({
      "$:LWCP_v1:$xxxxxxx=="
    }))},
    {"receiverUnionIds", boost::any(vector<string>({
      "JuSi1Jkl"
    }))},
    {"messageType", boost::any(string("MARKDOWN"))},
    {"btnOrientation", boost::any(string("0"))},
    {"btns", boost::any(vector<Alibabacloud_Dingtalkservice_group_1_0::SendServiceGroupMessageRequestBtns>({
      btns0
    }))}
  }));
  try {
    client->sendServiceGroupMessageWithOptions(sendServiceGroupMessageRequest, sendServiceGroupMessageHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openMsgTaskId | String | 开放消息任务ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openMsgTaskId" : "msgxxxxxx=="
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | illegalPama | 参数非法 | 参数非法 |
| 500 | systemError | 系统异常 | 系统异常 |
