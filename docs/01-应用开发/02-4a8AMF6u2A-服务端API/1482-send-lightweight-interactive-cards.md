---
title: "发送轻量级互动卡片"
source_url: "https://open.dingtalk.com/document/development/send-lightweight-interactive-cards"
namespace: "development"
slug: "send-lightweight-interactive-cards"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 发送轻量级互动卡片"
doc_id: "7uDeAL5eRQ"
updated_at: "2026-08-25 09:37:11"
---

> Source: https://open.dingtalk.com/document/development/send-lightweight-interactive-cards
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 机器人 > 发送轻量级互动卡片
> Updated: 2026-08-25 09:37:11

# 发送轻量级互动卡片

调用本接口发动轻量级互动卡片消息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建并投放卡片](0783-create-and-deliver-cards.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/im/interactiveCards/templates/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "String",
  "openConversationId" : "String",
  "singleChatReceiver" : "String",
  "outTrackId" : "String",
  "robotCode" : "String",
  "callbackUrl" : "String",
  "cardData" : "String",
  "sendOptions" : {
    "atUserListJson" : "String",
    "atAll" : Boolean,
    "receiverListJson" : "String",
    "cardPropertyJson" : "String"
  }
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cardTemplateId | String | 是 | 卡片内容模板ID，响应模板目前有：   - **TuWenCard01** - **TuWenCard02** - **TuWenCard03** - **TuWenCard04**   **[!NOTE]**  模板内容详情请参考：[轻量级互动卡片消息](../01-XOnnmGCTbn-开发指南/0095-lightweight-interactive-card-messages.md)。 |
| openConversationId | String | 否 | 接收卡片的加密群ID，特指多人群会话（非单聊）。  **[!NOTE]**  `openConversationId`和`singleChatReceiver`二选一必填。 |
| singleChatReceiver | String | 否 | 单聊会话接收者json字符串。群模板机器人暂不支持单聊，其他企业内部机器人和企业三方机器人有勾选支持单聊选项的可支持单聊。  **[!NOTE]**  `openConversationId`和`singleChatReceiver`二选一必填。 |
| outTrackId | String | 是 | 唯一标识一张卡片的外部ID。  **[!NOTE]**  卡片幂等ID，可用于更新或重复发送同一卡片到多个群会话，如果同一个**outTrackId**重复创建，卡片数据不覆盖更新。 |
| robotCode | String | 是 | 机器人代码。群模板机器人暂不支持单聊，其他企业内部机器人和企业三方机器人有勾选支持单聊选项的可支持单聊。  **[!NOTE]**  企业内部机器人取机器人appKey值，第三方企业机器人或群模板机器人取robotCode值。 |
| callbackUrl | String | 否 | 可控制卡片回调的URL。  **[!NOTE]**  如果不填则默认为无需回调。 |
| cardData | String | 是 | 卡片模板，文本内容参数、  **[!NOTE]**  卡片模板内容请参考：[轻量级互动卡片消息](../01-XOnnmGCTbn-开发指南/0095-lightweight-interactive-card-messages.md)。 |
| sendOptions | Object | 否 | 互动卡片发送选项。 |
| atUserListJson | String | 否 | 消息@人，JSON格式：   ``` [     {         "nickName": "张三",         "userId": "userId0001"     },     {         "nickName": "李四",         "unionId": "unionId001"     } ] ``` |
| atAll | Boolean | 否 | 是否@所有人。 |
| receiverListJson | String | 否 | 消息仅部分人可见的接收人列表，JSON格式：   ``` [     {         "userId": "userId0001"     },     {         "unionId": "unionId001"     } ] ```   **[!NOTE]**  为空则群所有人可见。 |
| cardPropertyJson | String | 否 | 互动卡片发送选项。  **[!NOTE]**   - 会话列表最新提示：`key： "sys_lastMessageI18n"，value："{\"zh_CN\":\"测试中文\",\"en_US\":\"test english\"}"` - 关屏消息提示：`key："sys_xpnContent"，value："XX消息请查收"；` |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| processQueryKey | String | 用于业务方后续查看已读列表的查询key。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interactiveCards/templates/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "cardTemplateId" : "TuWenCard01",
  "singleChatReceiver" : "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
  "outTrackId" : "cardXXXX01",
  "robotCode" : "xxxxxx",
  "callbackUrl" : "https://xxxx.com/xxx/",
  "cardData" : "根据具体的cardTemplateId参考文档格式",
  "sendOptions" : {
    "atUserListJson" : "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
    "atAll" : false,
    "receiverListJson" : "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
    "cardPropertyJson" : "{}"
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkim_1_0.*;
import com.aliyun.dingtalkim_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        SendTemplateInteractiveCardHeaders sendTemplateInteractiveCardHeaders = new SendTemplateInteractiveCardHeaders();
        sendTemplateInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendTemplateInteractiveCardRequest.SendTemplateInteractiveCardRequestSendOptions sendOptions = new SendTemplateInteractiveCardRequest.SendTemplateInteractiveCardRequestSendOptions()
                .setAtUserListJson("[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]")
                .setAtAll(false)
                .setReceiverListJson("[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]")
                .setCardPropertyJson("{}");
        SendTemplateInteractiveCardRequest sendTemplateInteractiveCardRequest = new SendTemplateInteractiveCardRequest()
                .setCardTemplateId("TuWenCard01")
                .setSingleChatReceiver("以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}")
                .setOutTrackId("cardXXXX01")
                .setRobotCode("xxxxxx")
                .setCallbackUrl("https://xxxx.com/xxx/")
                .setCardData("根据具体的cardTemplateId参考文档格式")
                .setSendOptions(sendOptions);
        try {
            client.sendTemplateInteractiveCardWithOptions(sendTemplateInteractiveCardRequest, sendTemplateInteractiveCardHeaders, new RuntimeOptions());
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
        send_template_interactive_card_headers = dingtalkim__1__0_models.SendTemplateInteractiveCardHeaders()
        send_template_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_options = dingtalkim__1__0_models.SendTemplateInteractiveCardRequestSendOptions(
            at_user_list_json='[{"nickName":"张三","userId":"userId0001"},{"nickName":"李四","unionId":"unionId001"}]',
            at_all=False,
            receiver_list_json='[{"userId":"userId0001"},{"unionId":"unionId001"}]',
            card_property_json='{}'
        )
        send_template_interactive_card_request = dingtalkim__1__0_models.SendTemplateInteractiveCardRequest(
            card_template_id='TuWenCard01',
            single_chat_receiver='以userId为例：{"userId":"userId0001"}；以unionId为例{"unionId":"unionId001"}',
            out_track_id='cardXXXX01',
            robot_code='xxxxxx',
            callback_url='https://xxxx.com/xxx/',
            card_data='根据具体的cardTemplateId参考文档格式',
            send_options=send_options
        )
        try:
            client.send_template_interactive_card_with_options(send_template_interactive_card_request, send_template_interactive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_template_interactive_card_headers = dingtalkim__1__0_models.SendTemplateInteractiveCardHeaders()
        send_template_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_options = dingtalkim__1__0_models.SendTemplateInteractiveCardRequestSendOptions(
            at_user_list_json='[{"nickName":"��三","userId":"userId0001"},{"nickName":"李四","unionId":"unionId001"}]',
            at_all=False,
            receiver_list_json='[{"userId":"userId0001"},{"unionId":"unionId001"}]',
            card_property_json='{}'
        )
        send_template_interactive_card_request = dingtalkim__1__0_models.SendTemplateInteractiveCardRequest(
            card_template_id='TuWenCard01',
            single_chat_receiver='以userId为例：{"userId":"userId0001"}；以unionId为例{"unionId":"unionId001"}',
            out_track_id='cardXXXX01',
            robot_code='xxxxxx',
            callback_url='https://xxxx.com/xxx/',
            card_data='根据具体的cardTemplateId参考文档格式',
            send_options=send_options
        )
        try:
            await client.send_template_interactive_card_with_options_async(send_template_interactive_card_request, send_template_interactive_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendTemplateInteractiveCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendTemplateInteractiveCardRequest\sendOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendTemplateInteractiveCardRequest;
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
        $sendTemplateInteractiveCardHeaders = new SendTemplateInteractiveCardHeaders([]);
        $sendTemplateInteractiveCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendOptions = new sendOptions([
            "atUserListJson" => "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
            "atAll" => false,
            "receiverListJson" => "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
            "cardPropertyJson" => "{}"
        ]);
        $sendTemplateInteractiveCardRequest = new SendTemplateInteractiveCardRequest([
            "cardTemplateId" => "TuWenCard01",
            "singleChatReceiver" => "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
            "outTrackId" => "cardXXXX01",
            "robotCode" => "xxxxxx",
            "callbackUrl" => "https://xxxx.com/xxx/",
            "cardData" => "根据具体的cardTemplateId参考文档格式",
            "sendOptions" => $sendOptions
        ]);
        try {
            $client->sendTemplateInteractiveCardWithOptions($sendTemplateInteractiveCardRequest, $sendTemplateInteractiveCardHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  sendTemplateInteractiveCardHeaders := &dingtalkim_1_0.SendTemplateInteractiveCardHeaders{}
  sendTemplateInteractiveCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendOptions := &dingtalkim_1_0.SendTemplateInteractiveCardRequestSendOptions{
    AtUserListJson: tea.String("[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]"),
    AtAll: tea.Bool(false),
    ReceiverListJson: tea.String("[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]"),
    CardPropertyJson: tea.String("{}"),
  }
  sendTemplateInteractiveCardRequest := &dingtalkim_1_0.SendTemplateInteractiveCardRequest{
    CardTemplateId: tea.String("TuWenCard01"),
    SingleChatReceiver: tea.String("以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}"),
    OutTrackId: tea.String("cardXXXX01"),
    RobotCode: tea.String("xxxxxx"),
    CallbackUrl: tea.String("https://xxxx.com/xxx/"),
    CardData: tea.String("根据具体的cardTemplateId参考文档格式"),
    SendOptions: sendOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendTemplateInteractiveCardWithOptions(sendTemplateInteractiveCardRequest, sendTemplateInteractiveCardHeaders, &util.RuntimeOptions{})
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
import dingtalkim_1_0, * as $dingtalkim_1_0 from '@alicloud/dingtalk/im_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkim_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkim_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let sendTemplateInteractiveCardHeaders = new $dingtalkim_1_0.SendTemplateInteractiveCardHeaders({ });
    sendTemplateInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sendOptions = new $dingtalkim_1_0.SendTemplateInteractiveCardRequestSendOptions({
      atUserListJson: "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
      atAll: false,
      receiverListJson: "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
      cardPropertyJson: "{}",
    });
    let sendTemplateInteractiveCardRequest = new $dingtalkim_1_0.SendTemplateInteractiveCardRequest({
      cardTemplateId: "TuWenCard01",
      singleChatReceiver: "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
      outTrackId: "cardXXXX01",
      robotCode: "xxxxxx",
      callbackUrl: "https://xxxx.com/xxx/",
      cardData: "根据具体的cardTemplateId参考文档格式",
      sendOptions: sendOptions,
    });
    try {
      await client.sendTemplateInteractiveCardWithOptions(sendTemplateInteractiveCardRequest, sendTemplateInteractiveCardHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendTemplateInteractiveCardHeaders sendTemplateInteractiveCardHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendTemplateInteractiveCardHeaders();
            sendTemplateInteractiveCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendTemplateInteractiveCardRequest.SendTemplateInteractiveCardRequestSendOptions sendOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendTemplateInteractiveCardRequest.SendTemplateInteractiveCardRequestSendOptions
            {
                AtUserListJson = "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
                AtAll = false,
                ReceiverListJson = "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
                CardPropertyJson = "{}",
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendTemplateInteractiveCardRequest sendTemplateInteractiveCardRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendTemplateInteractiveCardRequest
            {
                CardTemplateId = "TuWenCard01",
                SingleChatReceiver = "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
                OutTrackId = "cardXXXX01",
                RobotCode = "xxxxxx",
                CallbackUrl = "https://xxxx.com/xxx/",
                CardData = "根据具体的cardTemplateId参考文档格式",
                SendOptions = sendOptions,
            };
            try
            {
                client.SendTemplateInteractiveCardWithOptions(sendTemplateInteractiveCardRequest, sendTemplateInteractiveCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkim__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkim_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkim_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkim_1_0::Client> client = make_shared<Alibabacloud_Dingtalkim_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkim_1_0::SendTemplateInteractiveCardHeaders> sendTemplateInteractiveCardHeaders = make_shared<Alibabacloud_Dingtalkim_1_0::SendTemplateInteractiveCardHeaders>();
  sendTemplateInteractiveCardHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkim_1_0::SendTemplateInteractiveCardRequestSendOptions> sendOptions = make_shared<Alibabacloud_Dingtalkim_1_0::SendTemplateInteractiveCardRequestSendOptions>(map<string, boost::any>({
    {"atUserListJson", boost::any(string("[{"nickName":"张三","userId":"userId0001"},{"nickName":"李四","unionId":"unionId001"}]"))},
    {"atAll", boost::any(false)},
    {"receiverListJson", boost::any(string("[{"userId":"userId0001"},{"unionId":"unionId001"}]"))},
    {"cardPropertyJson", boost::any(string("{}"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkim_1_0::SendTemplateInteractiveCardRequest> sendTemplateInteractiveCardRequest = make_shared<Alibabacloud_Dingtalkim_1_0::SendTemplateInteractiveCardRequest>(map<string, boost::any>({
    {"cardTemplateId", boost::any(string("TuWenCard01"))},
    {"singleChatReceiver", boost::any(string("以userId为例：{"userId":"userId0001"}；以unionId为例{"unionId":"unionId001"}"))},
    {"outTrackId", boost::any(string("cardXXXX01"))},
    {"robotCode", boost::any(string("xxxxxx"))},
    {"callbackUrl", boost::any(string("https://xxxx.com/xxx/"))},
    {"cardData", boost::any(string("根据具体的cardTemplateId参考文档格式"))},
    {"sendOptions", !sendOptions ? boost::any() : boost::any(*sendOptions)}
  }));
  try {
    client->sendTemplateInteractiveCardWithOptions(sendTemplateInteractiveCardRequest, sendTemplateInteractiveCardHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "processQueryKey" : "08uvfxxxxxx"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | queryEmployInfoFailed | 查询企业员工信息失败 | 查询企业员工信息失败 |
| 400 | invalidParameter | 无效的参数 | 无效的参数 |
| 400 | notEmptyParameter | 缺失必填的参数 | 缺失必填的参数 |
| 400 | emptyUserId | 用户ID为空 | 用户ID为空 |
| 400 | decryptOpenconversationIdFailed | 群ID解码失败 | 群ID解码失败 |
| 400 | contentSecurityChckFailed | 卡片内容不符合安全规范 | 卡片内容不符合安全规范 |
| 400 | cardTemplateInvalid | 卡片模板无效 | 卡片模板无效 |
| 400 | chatbotNotInstall | 机器人未安装 | 机器人未安装 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | invalidParameter.param.empty | 入参为空 | 入参为空 |
| 400 | invalidParameter.cid.empty | 群id为空 | 群id为空 |
| 400 | invalidParameter.cardTemplate.notFound | 不存在的卡片模板 | 不存在的卡片模板 |
| 400 | paramBlank | 请求参数为空 | 请求参数为空 |
| 400 | sendCardMessageFailed | 发送卡片失败 | 发送卡片失败 |
| 400 | cidDecryptError | 群ID解析失败 | 群ID解析失败 |
| 400 | sceneGroupNotFound | 非场景群 | 非场景群 |
| 400 | chatbotNotFound | 不存在的机器人 | 不存在的机器人 |
| 400 | uidDecryptError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | duplicateKey | 卡片模板占位符有重复Key | 卡片模板占位符有重复Key |
| 400 | getPictureFailed | 获取图片url失败 | 获取图片url失败 |
| 400 | contentCheckError | 卡片内容校验失败 | 卡片内容校验失败 |
| 400 | outTrackIdLengthLimited | 超过卡片业务标识信息长度 | 超过卡片业务标识信息长度 |
| 500 | systemBusy | 系统繁忙 | 系统异常错误 |
