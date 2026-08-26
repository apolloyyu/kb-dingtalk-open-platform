---
title: "创建互动卡片实例"
source_url: "https://open.dingtalk.com/document/development/create-an-interactive-card-instance-2"
namespace: "development"
slug: "create-an-interactive-card-instance-2"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 酷应用 > 创建互动卡片实例"
doc_id: "VaSkh0CIa6"
updated_at: "2025-09-08 19:04:16"
---

> Source: https://open.dingtalk.com/document/development/create-an-interactive-card-instance-2
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 酷应用 > 创建互动卡片实例
> Updated: 2025-09-08 19:04:16

# 创建互动卡片实例

调用本接口创建互动卡片实例。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对互动卡片吊顶接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年11月20日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[创建并开启互动卡片吊顶](https://open.dingtalk.com/document/orgapp/create-and-open-an-interactive-card-ceiling)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

目前本接口创建的互动消息卡片实例主要用于开启和关闭置顶卡片，如下图所示：

![吊顶卡片](https://img.alicdn.com/imgextra/i1/O1CN01Jt1Meg1g3R1lXTVRD_!!6000000004086-2-tps-600-368.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | chat相关接口的管理权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 支持 | chat相关接口的管理权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 暂不支持 | chat相关接口的管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interactiveCards/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "String",
  "openConversationId" : "String",
  "receiverUserIdList" : [ "String" ],
  "outTrackId" : "String",
  "robotCode" : "String",
  "conversationType" : Integer,
  "callbackRouteKey" : "String",
  "cardData" : {
    "cardParamMap" : {
      "key" : "String"
    },
    "cardMediaIdParamMap" : {
      "key" : "String"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "String"
      },
      "cardMediaIdParamMap" : {
        "key" : "String"
      }
    }
  },
  "chatBotId" : "String",
  "userIdType" : Integer,
  "pullStrategy" : Boolean
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cardTemplateId | String | 是 | 卡片模板ID，可通过[创建消息模板](https://open.dingtalk.com/document/orgapp/create-message-template)获得。 |
| openConversationId | String | 否 | 接收卡片的群的openConversationId，可调用[创建群](https://open.dingtalk.com/document/orgapp/create-a-scene-group-v2)接口获取。 |
| receiverUserIdList | Array of String | 否 | 接收人userId。 |
| outTrackId | String | 是 | 唯一标识一张卡片的外部ID。  **[!NOTE]**  卡片幂等ID，可用于更新或重复发送同一卡片到多个群会话。 |
| robotCode | String | 否 | 机器人编码（群模板机器人）。  **[!NOTE]**  **robotCode**和**chatBotId**二选一必填。 |
| conversationType | Integer | 是 | 发送的会话类型：   - **0**：单聊 - **1**：群聊   **[!NOTE]**  单聊时，**openConversationId**不用填写，**receiverUserIdList**填写员工号（两个用户之间的单聊填写双方中任一员工号， 用户与机器人之间的单聊填写用户员工号）。 |
| callbackRouteKey | String | 否 | 可控制卡片回调时的路由Key，用于指定特定的**callbackUrl**。  **[!NOTE]**  可以为空，不填写默认无需回调。 |
| cardData | Object | 是 | 消息卡片。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，普通文本类型。 |
| cardMediaIdParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，多媒体类型。 |
| privateData | Map<String, Object> | 否 | 指定用户可见的按钮列表。   - **key**：用户userId - **value**：用户数据 |
|  | Object | 否 | 指定用户可见的按钮列表。   - **key**：用户userId - **value**：用户数据 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，普通文本类型。 |
| cardMediaIdParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，多媒体类型。 |
| chatBotId | String | 否 | 机器人编码（群模板机器人）。  **[!NOTE]**  **robotCode**和**chatBotId**二选一必填。 |
| userIdType | Integer | 否 | 用户ID类型：   - **1**：userid模式（默认） - **2**：unionId模式   **[!NOTE]**  对应**receiverUserIdList**、**privateData**字段关于用户userid的值填写方式。 |
| pullStrategy | Boolean | 否 | 是否开启卡片纯拉模式：（默认不开启卡片纯拉模式）   - **true**：开启卡片纯拉模式 - **false**：不开启卡片纯拉模式   **[!NOTE]**  - 纯拉模式，请参考[纯拉模式流程指南](https://open.dingtalk.com/document/orgapp/guide-to-pull-mode-process)。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| processQueryKey | String | 用于业务方后续查看已读列表的查询key。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interactiveCards/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxxx
Content-Type:application/json

{
  "cardTemplateId" : "iausfgxxxx",
  "openConversationId" : "fasxxxx",
  "receiverUserIdList" : [ "sadfxxxxx" ],
  "outTrackId" : "asfdxxxxx",
  "robotCode" : "asfdxxxx",
  "conversationType" : 1,
  "callbackRouteKey" : "faxxxx",
  "cardData" : {
    "cardParamMap" : {
      "key" : "afxxxx"
    },
    "cardMediaIdParamMap" : {
      "key" : "sfrtxxxx"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "wwhtxxxx"
      },
      "cardMediaIdParamMap" : {
        "key" : "xxxx"
      }
    }
  },
  "chatBotId" : "gwerxxxx",
  "userIdType" : 1,
  "pullStrategy" : false
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
        InteractiveCardCreateInstanceHeaders interactiveCardCreateInstanceHeaders = new InteractiveCardCreateInstanceHeaders();
        interactiveCardCreateInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> privateDataValueKeyCardMediaIdParamMap = TeaConverter.buildMap(
            new TeaPair("key", "xxxx")
        );
        java.util.Map<String, String> privateDataValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "wwhtxxxx")
        );
        PrivateDataValue privateDataValueKey = new PrivateDataValue()
                .setCardParamMap(privateDataValueKeyCardParamMap)
                .setCardMediaIdParamMap(privateDataValueKeyCardMediaIdParamMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        java.util.Map<String, String> cardDataCardMediaIdParamMap = TeaConverter.buildMap(
            new TeaPair("key", "sfrtxxxx")
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "afxxxx")
        );
        InteractiveCardCreateInstanceRequest.InteractiveCardCreateInstanceRequestCardData cardData = new InteractiveCardCreateInstanceRequest.InteractiveCardCreateInstanceRequestCardData()
                .setCardParamMap(cardDataCardParamMap)
                .setCardMediaIdParamMap(cardDataCardMediaIdParamMap);
        InteractiveCardCreateInstanceRequest interactiveCardCreateInstanceRequest = new InteractiveCardCreateInstanceRequest()
                .setCardTemplateId("iausfgxxxx")
                .setOpenConversationId("fasxxxx")
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "sadfxxxxx"
                ))
                .setOutTrackId("asfdxxxxx")
                .setRobotCode("asfdxxxx")
                .setConversationType(1)
                .setCallbackRouteKey("faxxxx")
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setChatBotId("gwerxxxx")
                .setUserIdType(1)
                .setPullStrategy(false);
        try {
            client.interactiveCardCreateInstanceWithOptions(interactiveCardCreateInstanceRequest, interactiveCardCreateInstanceHeaders, new RuntimeOptions());
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
        interactive_card_create_instance_headers = dingtalkim__1__0_models.InteractiveCardCreateInstanceHeaders()
        interactive_card_create_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        private_data_value_key_card_media_id_param_map = {
            'key': 'xxxx'
        }
        private_data_value_key_card_param_map = {
            'key': 'wwhtxxxx'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map,
            card_media_id_param_map=private_data_value_key_card_media_id_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_media_id_param_map = {
            'key': 'sfrtxxxx'
        }
        card_data_card_param_map = {
            'key': 'afxxxx'
        }
        card_data = dingtalkim__1__0_models.InteractiveCardCreateInstanceRequestCardData(
            card_param_map=card_data_card_param_map,
            card_media_id_param_map=card_data_card_media_id_param_map
        )
        interactive_card_create_instance_request = dingtalkim__1__0_models.InteractiveCardCreateInstanceRequest(
            card_template_id='iausfgxxxx',
            open_conversation_id='fasxxxx',
            receiver_user_id_list=[
                'sadfxxxxx'
            ],
            out_track_id='asfdxxxxx',
            robot_code='asfdxxxx',
            conversation_type=1,
            callback_route_key='faxxxx',
            card_data=card_data,
            private_data=private_data,
            chat_bot_id='gwerxxxx',
            user_id_type=1,
            pull_strategy=False
        )
        try:
            client.interactive_card_create_instance_with_options(interactive_card_create_instance_request, interactive_card_create_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        interactive_card_create_instance_headers = dingtalkim__1__0_models.InteractiveCardCreateInstanceHeaders()
        interactive_card_create_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        private_data_value_key_card_media_id_param_map = {
            'key': 'xxxx'
        }
        private_data_value_key_card_param_map = {
            'key': 'wwhtxxxx'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map,
            card_media_id_param_map=private_data_value_key_card_media_id_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_media_id_param_map = {
            'key': 'sfrtxxxx'
        }
        card_data_card_param_map = {
            'key': 'afxxxx'
        }
        card_data = dingtalkim__1__0_models.InteractiveCardCreateInstanceRequestCardData(
            card_param_map=card_data_card_param_map,
            card_media_id_param_map=card_data_card_media_id_param_map
        )
        interactive_card_create_instance_request = dingtalkim__1__0_models.InteractiveCardCreateInstanceRequest(
            card_template_id='iausfgxxxx',
            open_conversation_id='fasxxxx',
            receiver_user_id_list=[
                'sadfxxxxx'
            ],
            out_track_id='asfdxxxxx',
            robot_code='asfdxxxx',
            conversation_type=1,
            callback_route_key='faxxxx',
            card_data=card_data,
            private_data=private_data,
            chat_bot_id='gwerxxxx',
            user_id_type=1,
            pull_strategy=False
        )
        try:
            await client.interactive_card_create_instance_with_options_async(interactive_card_create_instance_request, interactive_card_create_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\InteractiveCardCreateInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\PrivateDataValue;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\InteractiveCardCreateInstanceRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\InteractiveCardCreateInstanceRequest;
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
        $interactiveCardCreateInstanceHeaders = new InteractiveCardCreateInstanceHeaders([]);
        $interactiveCardCreateInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $privateDataValueKeyCardMediaIdParamMap = [
            "key" => "xxxx"
        ];
        $privateDataValueKeyCardParamMap = [
            "key" => "wwhtxxxx"
        ];
        $privateDataValueKey = new PrivateDataValue([
            "cardParamMap" => $privateDataValueKeyCardParamMap,
            "cardMediaIdParamMap" => $privateDataValueKeyCardMediaIdParamMap
        ]);
        $privateData = [
            "privateDataValueKey" => $privateDataValueKey
        ];
        $cardDataCardMediaIdParamMap = [
            "key" => "sfrtxxxx"
        ];
        $cardDataCardParamMap = [
            "key" => "afxxxx"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap,
            "cardMediaIdParamMap" => $cardDataCardMediaIdParamMap
        ]);
        $interactiveCardCreateInstanceRequest = new InteractiveCardCreateInstanceRequest([
            "cardTemplateId" => "iausfgxxxx",
            "openConversationId" => "fasxxxx",
            "receiverUserIdList" => [
                "sadfxxxxx"
            ],
            "outTrackId" => "asfdxxxxx",
            "robotCode" => "asfdxxxx",
            "conversationType" => 1,
            "callbackRouteKey" => "faxxxx",
            "cardData" => $cardData,
            "privateData" => $privateData,
            "chatBotId" => "gwerxxxx",
            "userIdType" => 1,
            "pullStrategy" => false
        ]);
        try {
            $client->interactiveCardCreateInstanceWithOptions($interactiveCardCreateInstanceRequest, $interactiveCardCreateInstanceHeaders, new RuntimeOptions([]));
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

  interactiveCardCreateInstanceHeaders := &dingtalkim_1_0.InteractiveCardCreateInstanceHeaders{}
  interactiveCardCreateInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  privateDataValueKeyCardMediaIdParamMap := map[string]*string{
    "key": tea.String("xxxx"),
  }
  privateDataValueKeyCardParamMap := map[string]*string{
    "key": tea.String("wwhtxxxx"),
  }
  privateDataValueKey := &dingtalkim_1_0.PrivateDataValue{
    CardParamMap: privateDataValueKeyCardParamMap,
    CardMediaIdParamMap: privateDataValueKeyCardMediaIdParamMap,
  }
  privateData := map[string]*dingtalkim_1_0.PrivateDataValue{
    "privateDataValueKey": privateDataValueKey,
  }
  cardDataCardMediaIdParamMap := map[string]*string{
    "key": tea.String("sfrtxxxx"),
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("afxxxx"),
  }
  cardData := &dingtalkim_1_0.InteractiveCardCreateInstanceRequestCardData{
    CardParamMap: cardDataCardParamMap,
    CardMediaIdParamMap: cardDataCardMediaIdParamMap,
  }
  interactiveCardCreateInstanceRequest := &dingtalkim_1_0.InteractiveCardCreateInstanceRequest{
    CardTemplateId: tea.String("iausfgxxxx"),
    OpenConversationId: tea.String("fasxxxx"),
    ReceiverUserIdList: []*string{tea.String("sadfxxxxx")},
    OutTrackId: tea.String("asfdxxxxx"),
    RobotCode: tea.String("asfdxxxx"),
    ConversationType: tea.Int32(1),
    CallbackRouteKey: tea.String("faxxxx"),
    CardData: cardData,
    PrivateData: privateData,
    ChatBotId: tea.String("gwerxxxx"),
    UserIdType: tea.Int32(1),
    PullStrategy: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.InteractiveCardCreateInstanceWithOptions(interactiveCardCreateInstanceRequest, interactiveCardCreateInstanceHeaders, &util.RuntimeOptions{})
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
    let interactiveCardCreateInstanceHeaders = new $dingtalkim_1_0.InteractiveCardCreateInstanceHeaders({ });
    interactiveCardCreateInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let privateDataValueKeyCardMediaIdParamMap = {
      key: "xxxx",
    };
    let privateDataValueKeyCardParamMap = {
      key: "wwhtxxxx",
    };
    let privateDataValueKey = new $dingtalkim_1_0.PrivateDataValue({
      cardParamMap: privateDataValueKeyCardParamMap,
      cardMediaIdParamMap: privateDataValueKeyCardMediaIdParamMap,
    });
    let privateData = {
      privateDataValueKey: privateDataValueKey,
    };
    let cardDataCardMediaIdParamMap = {
      key: "sfrtxxxx",
    };
    let cardDataCardParamMap = {
      key: "afxxxx",
    };
    let cardData = new $dingtalkim_1_0.InteractiveCardCreateInstanceRequestCardData({
      cardParamMap: cardDataCardParamMap,
      cardMediaIdParamMap: cardDataCardMediaIdParamMap,
    });
    let interactiveCardCreateInstanceRequest = new $dingtalkim_1_0.InteractiveCardCreateInstanceRequest({
      cardTemplateId: "iausfgxxxx",
      openConversationId: "fasxxxx",
      receiverUserIdList: [
        "sadfxxxxx"
      ],
      outTrackId: "asfdxxxxx",
      robotCode: "asfdxxxx",
      conversationType: 1,
      callbackRouteKey: "faxxxx",
      cardData: cardData,
      privateData: privateData,
      chatBotId: "gwerxxxx",
      userIdType: 1,
      pullStrategy: false,
    });
    try {
      await client.interactiveCardCreateInstanceWithOptions(interactiveCardCreateInstanceRequest, interactiveCardCreateInstanceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.InteractiveCardCreateInstanceHeaders interactiveCardCreateInstanceHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.InteractiveCardCreateInstanceHeaders();
            interactiveCardCreateInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> privateDataValueKeyCardMediaIdParamMap = new Dictionary<string, string>
            {
                {"key", "xxxx"},
            };
            Dictionary<string, string> privateDataValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "wwhtxxxx"},
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue privateDataValueKey = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue
            {
                CardParamMap = privateDataValueKeyCardParamMap,
                CardMediaIdParamMap = privateDataValueKeyCardMediaIdParamMap,
            };
            Dictionary<string, AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue> privateData = new Dictionary<string, AlibabaCloud.SDK.Dingtalkim_1_0.Models.PrivateDataValue>
            {
                {"privateDataValueKey", privateDataValueKey},
            };
            Dictionary<string, string> cardDataCardMediaIdParamMap = new Dictionary<string, string>
            {
                {"key", "sfrtxxxx"},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "afxxxx"},
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.InteractiveCardCreateInstanceRequest.InteractiveCardCreateInstanceRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.InteractiveCardCreateInstanceRequest.InteractiveCardCreateInstanceRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
                CardMediaIdParamMap = cardDataCardMediaIdParamMap,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.InteractiveCardCreateInstanceRequest interactiveCardCreateInstanceRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.InteractiveCardCreateInstanceRequest
            {
                CardTemplateId = "iausfgxxxx",
                OpenConversationId = "fasxxxx",
                ReceiverUserIdList = new List<string>
                {
                    "sadfxxxxx"
                },
                OutTrackId = "asfdxxxxx",
                RobotCode = "asfdxxxx",
                ConversationType = 1,
                CallbackRouteKey = "faxxxx",
                CardData = cardData,
                PrivateData = privateData,
                ChatBotId = "gwerxxxx",
                UserIdType = 1,
                PullStrategy = false,
            };
            try
            {
                client.InteractiveCardCreateInstanceWithOptions(interactiveCardCreateInstanceRequest, interactiveCardCreateInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "processQueryKey" : "xxxxxx"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | param.invalid | 请求参数无效 | 请求参数无效 |
| 400 | callbackUrl.empty | 回调地址为空 | 回调地址为空 |
| 400 | permission.checkFailed | 发送动态卡片权限校验失败 | 发送动态卡片权限校验失败 |
| 400 | sceneGroup.checkFailed | 场景群权限校验失败 | 场景群权限校验失败 |
| 400 | cardInstance.wrong | 创建卡片实例失败，先检查卡片模板是否已发布 | 创建卡片实例失败，先检查卡片模板是否已发布 |
| 400 | userInfo.convertError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | card.outTraceIdError | 卡片业务标识信息格式非法 | 卡片业务标识信息格式非法 |
| 400 | card.outTraceIdEmpty | 业务标识outTrackId为空 | 业务标识outTrackId为空 |
| 400 | cidParse.wrong | 群ID解码失败 | 群ID解码失败 |
| 400 | chatbot.notFound | 机器人不存在 | 机器人不存在 |
| 400 | queryChatbot.wrong | 查询机器人失败 | 查询机器人失败 |
| 400 | card.templateEmpty | 卡片模板ID为空 | 卡片模板ID为空 |
| 400 | invalidParameter.cid.empty | 群id为空 | 群id为空 |
| 400 | invalidParameter.cardTemplate.notFound | 不存在的卡片模板 | 不存在的卡片模板 |
| 400 | sendCardMessageFailed | 发送卡片失败 | 发送卡片失败 |
| 400 | sceneGroupNotFound | 非场景群 | 非场景群 |
| 500 | systemBusy | 系统繁忙 | 系统异常错误 |
