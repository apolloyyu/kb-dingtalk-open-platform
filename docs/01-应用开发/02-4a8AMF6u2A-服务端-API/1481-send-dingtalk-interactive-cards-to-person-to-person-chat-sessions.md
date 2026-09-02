---
title: "人与人会话中机器人发送互动卡片"
source_url: "https://open.dingtalk.com/document/development/send-dingtalk-interactive-cards-to-person-to-person-chat-sessions"
namespace: "development"
slug: "send-dingtalk-interactive-cards-to-person-to-person-chat-sessions"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 人与人会话中机器人发送互动卡片"
doc_id: "t1PQsi1bR6"
updated_at: "2026-08-25 09:37:10"
---

> Source: https://open.dingtalk.com/document/development/send-dingtalk-interactive-cards-to-person-to-person-chat-sessions
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 机器人 > 人与人会话中机器人发送互动卡片
> Updated: 2026-08-25 09:37:10

# 人与人会话中机器人发送互动卡片

调用本接口实现人与人会话中机器人发送互动卡片。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建并投放卡片](0783-create-and-deliver-cards.md)接口，已接入用户不受影响。

### 接口功能介绍

- 循环组件用法：内容塞入

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0381267871/p1096183.png)
- 会话列表lastMessage显示：

  - 什么是lastmessage，指的是在会话列表页面透出的消息。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0381267871/p1096184.png)
  - 设置特殊key：`sys_lastMessageI18n`。
  - value值：
    `{\"zh_CN\":\"蚂蚁分工\",\"zh_TW\":\"螞蟻分工\",\"zh_HK\":\"螞蟻分工\",\"ja_JP\":\"アリの分業\",\"en_US\":\"Ant division of labor\"}"`
  - 举例说明：
    `"cardData": { "cardParamMap": { "sys_lastMessageI18n": "{\"zh_CN\":\"蚂蚁分工\",\"zh_TW\":\"螞蟻分工\",\"zh_HK\":\"螞蟻分工\",\"ja_JP\":\"アリの分業\",\"en_US\":\"Ant division of labor\"}"}}`

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/im/privateChat/interactiveCards/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "String",
  "openConversationId" : "String",
  "receiverUserIdList" : [ "String" ],
  "outTrackId" : "String",
  "robotCode" : "String",
  "callbackRouteKey" : "String",
  "cardData" : {
    "cardParamMap" : {
      "key" : "String"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "String"
      }
    }
  },
  "userIdType" : Integer,
  "atOpenIds" : {
    "key" : "String"
  },
  "cardOptions" : {
    "supportForward" : Boolean
  },
  "pullStrategy" : Boolean
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cardTemplateId | String | 是 | 卡片模板ID，可通过[卡片平台](https://open-dev.dingtalk.com/fe/card)创建消息卡片，参见[管理消息模板](0765-manage-message-templates.md)介绍。 |
| openConversationId | String | 否 | 会话ID，可通过[批量安装酷应用到单聊会话](../03-Ogu5SlPY4t-客户端-JSAPI/0277-batch-chat-session.md)或监听[单聊酷应用事件](../04-LFcRvVD08N-事件订阅/0352-one-on-one-chat-cool-application-extension-event.md)获取`OpenConversationId`参数值。 |
| receiverUserIdList | Array of String | 否 | 用户ID列表。 |
| outTrackId | String | 是 | 唯一标示卡片的外部编码。  **[!NOTE]**  是由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。 |
| robotCode | String | 否 | 机器人编码，参见[机器人名词表-robotCode](0698-development-robot-overview.md)内容，获取`robotCode`。 |
| callbackRouteKey | String | 否 | 卡片回调时的路由Key，用于查询注册的callbackUrl。  **[!NOTE]**  不填写默认无需回调。 |
| cardData | Object | 是 | 卡片模板内容。 |
| cardParamMap | Map<String, String> | 否 | 卡片公有数据。 |
| privateData | Map<String, Object> | 否 | 指定用户可见的按钮列表：   - key：用户userId。 - value：用户数据。   **[!NOTE]**  对应receiverUserIdList、userIdType字段关于用户ID的值填写方式：   - **userId模式**：key填写用户userId。 - **unionId模式**：key填写用户unionId。 |
|  | Object | 否 | 指定用户可见的按钮列表：   - **key**：用户userId。 - **value**：用户数据。 |
| cardParamMap | Map<String, String> | 否 | 卡片私有数据。 |
| userIdType | Integer | 否 | 用户ID类型：   - **1**（默认）：userid模式。 - **2**：unionId模式。 |
| atOpenIds | Map<String, String> | 否 | 消息@人。格式：`{"key":"value"}`。   - key：用户ID，根据userIdType设置。 - value：用户名。例如：`{123456:"钉三多"}`。   **[!NOTE]**    如果key、value都为\*\*@ALL\*\*则判断@所有人。 |
| cardOptions | Object | 否 | 卡片属性。 |
| supportForward | Boolean | 否 | 是否支持转发：   - **true**：支持 - **false**：不支持 |
| pullStrategy | Boolean | 否 | 是否开启卡片纯拉模式：   - **true**：开启 - **false**：不开启 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 接口调用是否成功。 |
| result | Object | 创建卡片结果。 |
| processQueryKey | String | 用于业务方后续查看已读列表的查询key。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/privateChat/interactiveCards/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxx
Content-Type:application/json

{
  "cardTemplateId" : "d842d15e-1cfb-****-****-b06448995d0a",
  "openConversationId" : "cidvookR*******SNe3DM/iuSg5a4QY=",
  "receiverUserIdList" : [ "1001,01472825524039877041" ],
  "outTrackId" : "privateChat_20221118_1001",
  "robotCode" : "dingqgb*****iz3agi",
  "callbackRouteKey" : "test",
  "cardData" : {
    "cardParamMap" : {
      "key" : "test"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "test"
      }
    }
  },
  "userIdType" : 1,
  "atOpenIds" : {
    "key" : "{123456:\"钉三多\"}"
  },
  "cardOptions" : {
    "supportForward" : true
  },
  "pullStrategy" : false
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
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardHeaders sendOTOInteractiveCardHeaders = new com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardHeaders();
        sendOTOInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardOptions cardOptions = new com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardOptions()
                .setSupportForward(true);
        java.util.Map<String, String> atOpenIds = TeaConverter.buildMap(
            new TeaPair("key", "{123456:\"钉三多\"}")
        );
        java.util.Map<String, String> privateDataValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "test")
        );
        com.aliyun.dingtalkim_1_0.models.PrivateDataValue privateDataValueKey = new com.aliyun.dingtalkim_1_0.models.PrivateDataValue()
                .setCardParamMap(privateDataValueKeyCardParamMap);
        java.util.Map<String, com.aliyun.dingtalkim_1_0.models.PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "test")
        );
        com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardData cardData = new com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardData()
                .setCardParamMap(cardDataCardParamMap);
        com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardRequest sendOTOInteractiveCardRequest = new com.aliyun.dingtalkim_1_0.models.SendOTOInteractiveCardRequest()
                .setCardTemplateId("d842d15e-1cfb-****-****-b06448995d0a")
                .setOpenConversationId("cidvookR*******SNe3DM/iuSg5a4QY=")
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "1001,01472825524039877041"
                ))
                .setOutTrackId("privateChat_20221118_1001")
                .setRobotCode("dingqgb*****iz3agi")
                .setCallbackRouteKey("test")
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setUserIdType(1)
                .setAtOpenIds(atOpenIds)
                .setCardOptions(cardOptions)
                .setPullStrategy(false);
        try {
            client.sendOTOInteractiveCardWithOptions(sendOTOInteractiveCardRequest, sendOTOInteractiveCardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        send_otointeractive_card_headers = dingtalkim__1__0_models.SendOTOInteractiveCardHeaders()
        send_otointeractive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_options = dingtalkim__1__0_models.SendOTOInteractiveCardRequestCardOptions(
            support_forward=True
        )
        at_open_ids = {
            'key': '{123456:"钉三多"}'
        }
        private_data_value_key_card_param_map = {
            'key': 'test'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_param_map = {
            'key': 'test'
        }
        card_data = dingtalkim__1__0_models.SendOTOInteractiveCardRequestCardData(
            card_param_map=card_data_card_param_map
        )
        send_otointeractive_card_request = dingtalkim__1__0_models.SendOTOInteractiveCardRequest(
            card_template_id='d842d15e-1cfb-****-****-b06448995d0a',
            open_conversation_id='cidvookR*******SNe3DM/iuSg5a4QY=',
            receiver_user_id_list=[
                '1001,01472825524039877041'
            ],
            out_track_id='privateChat_20221118_1001',
            robot_code='dingqgb*****iz3agi',
            callback_route_key='test',
            card_data=card_data,
            private_data=private_data,
            user_id_type=1,
            at_open_ids=at_open_ids,
            card_options=card_options,
            pull_strategy=False
        )
        try:
            client.send_otointeractive_card_with_options(send_otointeractive_card_request, send_otointeractive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_otointeractive_card_headers = dingtalkim__1__0_models.SendOTOInteractiveCardHeaders()
        send_otointeractive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_options = dingtalkim__1__0_models.SendOTOInteractiveCardRequestCardOptions(
            support_forward=True
        )
        at_open_ids = {
            'key': '{123456:"钉三多"}'
        }
        private_data_value_key_card_param_map = {
            'key': 'test'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_param_map = {
            'key': 'test'
        }
        card_data = dingtalkim__1__0_models.SendOTOInteractiveCardRequestCardData(
            card_param_map=card_data_card_param_map
        )
        send_otointeractive_card_request = dingtalkim__1__0_models.SendOTOInteractiveCardRequest(
            card_template_id='d842d15e-1cfb-****-****-b06448995d0a',
            open_conversation_id='cidvookR*******SNe3DM/iuSg5a4QY=',
            receiver_user_id_list=[
                '1001,01472825524039877041'
            ],
            out_track_id='privateChat_20221118_1001',
            robot_code='dingqgb*****iz3agi',
            callback_route_key='test',
            card_data=card_data,
            private_data=private_data,
            user_id_type=1,
            at_open_ids=at_open_ids,
            card_options=card_options,
            pull_strategy=False
        )
        try:
            await client.send_otointeractive_card_with_options_async(send_otointeractive_card_request, send_otointeractive_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendOTOInteractiveCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendOTOInteractiveCardRequest\cardOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\PrivateDataValue;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendOTOInteractiveCardRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendOTOInteractiveCardRequest;
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
        $sendOTOInteractiveCardHeaders = new SendOTOInteractiveCardHeaders([]);
        $sendOTOInteractiveCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cardOptions = new cardOptions([
            "supportForward" => true
        ]);
        $atOpenIds = [
            "key" => "{123456:\"钉三多\"}"
        ];
        $privateDataValueKeyCardParamMap = [
            "key" => "test"
        ];
        $privateDataValueKey = new PrivateDataValue([
            "cardParamMap" => $privateDataValueKeyCardParamMap
        ]);
        $privateData = [
            "privateDataValueKey" => $privateDataValueKey
        ];
        $cardDataCardParamMap = [
            "key" => "test"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap
        ]);
        $sendOTOInteractiveCardRequest = new SendOTOInteractiveCardRequest([
            "cardTemplateId" => "d842d15e-1cfb-****-****-b06448995d0a",
            "openConversationId" => "cidvookR*******SNe3DM/iuSg5a4QY=",
            "receiverUserIdList" => [
                "1001,01472825524039877041"
            ],
            "outTrackId" => "privateChat_20221118_1001",
            "robotCode" => "dingqgb*****iz3agi",
            "callbackRouteKey" => "test",
            "cardData" => $cardData,
            "privateData" => $privateData,
            "userIdType" => 1,
            "atOpenIds" => $atOpenIds,
            "cardOptions" => $cardOptions,
            "pullStrategy" => false
        ]);
        try {
            $client->sendOTOInteractiveCardWithOptions($sendOTOInteractiveCardRequest, $sendOTOInteractiveCardHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  sendOTOInteractiveCardHeaders := &dingtalkim_1_0.SendOTOInteractiveCardHeaders{}
  sendOTOInteractiveCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cardOptions := &dingtalkim_1_0.SendOTOInteractiveCardRequestCardOptions{
    SupportForward: tea.Bool(true),
  }
  atOpenIds := map[string]*string{
    "key": tea.String("{123456:\"钉三多\"}"),
  }
  privateDataValueKeyCardParamMap := map[string]*string{
    "key": tea.String("test"),
  }
  privateDataValueKey := &dingtalkim_1_0.PrivateDataValue{
    CardParamMap: privateDataValueKeyCardParamMap,
  }
  privateData := map[string]*dingtalkim_1_0.PrivateDataValue{
    "privateDataValueKey": privateDataValueKey,
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("test"),
  }
  cardData := &dingtalkim_1_0.SendOTOInteractiveCardRequestCardData{
    CardParamMap: cardDataCardParamMap,
  }
  sendOTOInteractiveCardRequest := &dingtalkim_1_0.SendOTOInteractiveCardRequest{
    CardTemplateId: tea.String("d842d15e-1cfb-****-****-b06448995d0a"),
    OpenConversationId: tea.String("cidvookR*******SNe3DM/iuSg5a4QY="),
    ReceiverUserIdList: []*string{tea.String("1001,01472825524039877041")},
    OutTrackId: tea.String("privateChat_20221118_1001"),
    RobotCode: tea.String("dingqgb*****iz3agi"),
    CallbackRouteKey: tea.String("test"),
    CardData: cardData,
    PrivateData: privateData,
    UserIdType: tea.Int32(1),
    AtOpenIds: atOpenIds,
    CardOptions: cardOptions,
    PullStrategy: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendOTOInteractiveCardWithOptions(sendOTOInteractiveCardRequest, sendOTOInteractiveCardHeaders, &util.RuntimeOptions{})
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
    let sendOTOInteractiveCardHeaders = new $dingtalkim_1_0.SendOTOInteractiveCardHeaders({ });
    sendOTOInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let cardOptions = new $dingtalkim_1_0.SendOTOInteractiveCardRequestCardOptions({
      supportForward: true,
    });
    let atOpenIds = {
      key: "{123456:\"钉三多\"}",
    };
    let privateDataValueKeyCardParamMap = {
      key: "test",
    };
    let privateDataValueKey = new $dingtalkim_1_0.PrivateDataValue({
      cardParamMap: privateDataValueKeyCardParamMap,
    });
    let privateData = {
      privateDataValueKey: privateDataValueKey,
    };
    let cardDataCardParamMap = {
      key: "test",
    };
    let cardData = new $dingtalkim_1_0.SendOTOInteractiveCardRequestCardData({
      cardParamMap: cardDataCardParamMap,
    });
    let sendOTOInteractiveCardRequest = new $dingtalkim_1_0.SendOTOInteractiveCardRequest({
      cardTemplateId: "d842d15e-1cfb-****-****-b06448995d0a",
      openConversationId: "cidvookR*******SNe3DM/iuSg5a4QY=",
      receiverUserIdList: [
        "1001,01472825524039877041"
      ],
      outTrackId: "privateChat_20221118_1001",
      robotCode: "dingqgb*****iz3agi",
      callbackRouteKey: "test",
      cardData: cardData,
      privateData: privateData,
      userIdType: 1,
      atOpenIds: atOpenIds,
      cardOptions: cardOptions,
      pullStrategy: false,
    });
    try {
      await client.sendOTOInteractiveCardWithOptions(sendOTOInteractiveCardRequest, sendOTOInteractiveCardHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardHeaders sendOTOInteractiveCardHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardHeaders();
            sendOTOInteractiveCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardOptions cardOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardOptions
            {
                SupportForward = true,
            };
            Dictionary<string, string> atOpenIds = new Dictionary<string, string>
            {
                {"key", "{123456:\"钉三多\"}"},
            };
            Dictionary<string, string> privateDataValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "test"},
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue privateDataValueKey = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue
            {
                CardParamMap = privateDataValueKeyCardParamMap,
            };
            Dictionary<string, AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue> privateData = new Dictionary<string, AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue>
            {
                {"privateDataValueKey", privateDataValueKey},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "test"},
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardRequest.SendOTOInteractiveCardRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardRequest sendOTOInteractiveCardRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendOTOInteractiveCardRequest
            {
                CardTemplateId = "d842d15e-1cfb-****-****-b06448995d0a",
                OpenConversationId = "cidvookR*******SNe3DM/iuSg5a4QY=",
                ReceiverUserIdList = new List<string>
                {
                    "1001,01472825524039877041"
                },
                OutTrackId = "privateChat_20221118_1001",
                RobotCode = "dingqgb*****iz3agi",
                CallbackRouteKey = "test",
                CardData = cardData,
                PrivateData = privateData,
                UserIdType = 1,
                AtOpenIds = atOpenIds,
                CardOptions = cardOptions,
                PullStrategy = false,
            };
            try
            {
                client.SendOTOInteractiveCardWithOptions(sendOTOInteractiveCardRequest, sendOTOInteractiveCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "success" : true,
  "result" : {
    "processQueryKey" : "xxxxxx"
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | callbackUrl.empty | 回调地址为空 | 回调地址为空 |
| 400 | param.invalid | 无效参数 | 无效参数 |
| 400 | permission.checkFailed | 发送动态卡片权限校验失败 | 发送动态卡片权限校验失败 |
| 400 | queryChatbot.wrong | 查询机器人失败 | 查询机器人失败 |
| 400 | cardInstance.wrong | 创建卡片实例失败，先检查卡片模板是否已发布 | 创建卡片实例失败，先检查卡片模板是否已发布 |
| 400 | cidParse.wrong | 单聊会话ID解码失败 | 单聊会话ID解码失败 |
| 400 | card.templateEmpty | 卡片模板ID为空 | 卡片模板ID为空 |
| 400 | userInfo.convertError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | card.outTraceIdError | 卡片业务标识信息格式非法 | 卡片业务标识信息格式非法 |
| 400 | card.outTraceIdEmpty | 业务标识outTrackId为空 | 业务标识outTrackId为空 |
| 400 | chatbot.notFound | 机器人不存在 | 机器人不存在 |
| 400 | invalidParameter.cid.empty | 单聊会话id为空 | 单聊会话id为空 |
| 400 | sendCardMessageFailed | 发送卡片失败 | 发送卡片失败 |
| 400 | duplicateKey | 卡片模板占位符有重复Key | 卡片模板占位符有重复Key |
| 400 | getPictureFailed | 获取图片url失败 | 获取图片url失败 |
| 400 | org.notOwn.group | 单聊会话不属于当前企业 | 单聊会话不属于当前企业 |
| 400 | send.oa.timeout | 发工作通知超时，请稍后重试 | 发工作通知超时，请稍后重试 |
| 400 | outTrackId.exceed.limit | outTrackId长度超限 | outTrackId长度超限 |
| 500 | systemBusy | 系统繁忙 | 系统异常错误 |
| 500 | systemError | 系统错误 | 系统错误 |
