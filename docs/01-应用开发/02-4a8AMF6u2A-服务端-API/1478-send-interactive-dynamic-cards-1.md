---
title: "发送钉钉互动卡片（高级版）"
source_url: "https://open.dingtalk.com/document/development/send-interactive-dynamic-cards-1"
namespace: "development"
slug: "send-interactive-dynamic-cards-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 发送钉钉互动卡片（高级版）"
doc_id: "PUyAQbbw90"
updated_at: "2026-08-25 09:37:06"
---

> Source: https://open.dingtalk.com/document/development/send-interactive-dynamic-cards-1
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 机器人 > 发送钉钉互动卡片（高级版）
> Updated: 2026-08-25 09:37:06

# 发送钉钉互动卡片（高级版）

调用本接口发送钉钉互动卡片。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建并投放卡片](0783-create-and-deliver-cards.md)接口，已接入用户不受影响。

## **接口调用说明**

### 卡片特殊能力用法

- 循环组件用法：内容塞入

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6281267871/p1096181.png)
- 会话列表最后一条信息显示：

  - 什么是最后一条信息

    指的是在会话列表页面透出的消息

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6281267871/p1096182.png)
  - 设置特殊key：`sys_lastMessageI18n`。
  - value值：

    `{\"zh_CN\":\"蚂蚁分工\",\"zh_TW\":\"螞蟻分工\",\"zh_HK\":\"螞蟻分工\",\"ja_JP\":\"アリの分業\",\"en_US\":\"Ant division of labor\"}"`
  - 举例说明：

    `"cardData": { "cardParamMap": { "sys_lastMessageI18n": "{\"zh_CN\":\"蚂蚁分工\",\"zh_TW\":\"螞蟻分工\",\"zh_HK\":\"螞蟻分工\",\"ja_JP\":\"アリの分業\",\"en_US\":\"Ant division of labor\"}"}}`

### 特殊使用场景说明

- 场景群机器人发送：场景群使用**robotCode**来发送，**chatBotId**不填写。
- 非场景群企业机器人发送：填写**robotCode**来发送，**chatBotId**不填写。
- 非场景群机器人单聊发送：**chatBotId**和**robotCode**都不填写，直接用支持单聊的机器人应用来发送。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/im/interactiveCards/send HTTP/1.1
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
| cardTemplateId | String | 是 | 互动卡片的消息模板ID，获取方式请参考[管理消息模板](0765-manage-message-templates.md)介绍。 |
| openConversationId | String | 否 | 群ID：   - 基于群模板创建的群，请参考[创建群](1486-create-a-scene-group-v2.md)。 - 安装群聊酷应用的群，通过[群内安装酷应用事件](../04-LFcRvVD08N-事件订阅/0308-install-group-extension-event-in-the-group-stream.md)获取回调参数`OpenConversationId`参数值。 |
| receiverUserIdList | Array of String | 否 | 接收人userId列表。   - receiverUserIdList填写分为以下情况：    - 单聊：      - 填写用户ID，最大值20。   - 群聊：      - 填写用户ID，表示群内指定用户可见。     - 不填写，表示群内所有用户可见。 - 对应privateData、userIdType字段关于用户ID的值填写方式：    - **userId模式**：key填写用户userId。   - **unionId模式**：key填写用户unionId。 |
| outTrackId | String | 是 | 唯一标示卡片的外部编码。  **[!NOTE]**   - 不超过100字符，建议64字符以内。 - 是由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到**outTrackId**的场景，帮助开发者对TrackId进行记录。   若使用新的 `cardTemplateId` 或 `cardData` 等参数，则需要生成一个全新的 outTrackId，否则更改不会生效。 |
| robotCode | String | 否 | 机器人的编码，参见[机器人名词表-robotCode](0698-development-robot-overview.md)内容，获取`robotCode`。  **[!NOTE]**   - 场景群机器人发送群聊：场景群使用**robotCode**来发送，**chatBotId**不填写。 - 非场景群的企业内部开发-机器人发送群聊：填写**robotCode**来发送，**chatBotId**不填写。 - 非场景群的企业内部开发-机器人发送单聊：**chatBotId**和**robotCode**都不填写，直接用支持单聊的机器人应用来发送。 |
| conversationType | Integer | 是 | 发送的会话类型：   - **0**：单聊    - **openConversationId**不用填写。   - **receiverUserIdList**填写用户ID，最大值20。 - **1**：群聊 |
| callbackRouteKey | String | 否 | 卡片回调时的路由Key，用于查询注册的**callbackUrl**。  **[!NOTE]**  不填写默认无需回调。 |
| cardData | Object | 是 | 卡片公有数据。  **[!NOTE]**   - `cardData`数据长度和`privateData`数据长度总和不能超过100KB。 - 若因指定私有数据的人数太多导致的数据过长，可参见[变量与卡片的关系](../../05-互动卡片/03-MhNX42mFB1-模板搭建器/0003-relationship-between-variables-and-cards.md)目录节点下内容的相关特性来缩短长度。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，普通文本类型。  **[!NOTE]**   - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| cardMediaIdParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，多媒体类型。 |
| privateData | Map<String, Object> | 否 | 卡片私有数据。   - **key**：用户userId。 - **value**：用户数据。   卡片公有数据。  **[!NOTE]**   - `cardData`数据长度和`privateData`数据长度总和不能超过100KB。 - 若因指定私有数据的人数太多导致的数据过长，可参见[变量与卡片的关系](../../05-互动卡片/03-MhNX42mFB1-模板搭建器/0003-relationship-between-variables-and-cards.md)目录节点下内容的相关特性来缩短长度。 - 对应receiverUserIdList、userIdType字段关于用户ID的值填写方式：    - **userId模式**：key填写用户userId。   - **unionId模式**：key填写用户unionId。 |
|  | Object | 否 | 指定用户可见的按钮列表。   - **key**：用户userId。 - **value**：用户数据。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板的文本内容参数。  **[!NOTE]**   - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| cardMediaIdParamMap | Map<String, String> | 否 | 卡片模板的图片内容参数。  **[!NOTE]**  仅支持开放平台文件存储的mediaId。 |
| chatBotId | String | 否 | 企业机器人ID，填写企业内部开发-机器人的AppKey。    **[!NOTE]**   - 场景群机器人发送群聊：场景群使用**robotCode**来发送，**chatBotId**不填写。 - 非场景群的企业内部开发-机器人发送群聊：填写**robotCode**来发送，**chatBotId**不填写。 - 非场景群的企业内部开发-机器人发送单聊：**chatBotId**和**robotCode**都不填写，直接用支持单聊的机器人应用来发送。 |
| userIdType | Integer | 否 | 用户ID类型：   - **1**（默认）：userid模式 - **2**：unionId模式   **[!NOTE]**    对应receiverUserIdList、privateData字段关于用户id的值填写方式。 |
| atOpenIds | Map<String, String> | 否 | 消息@人。格式：`{"key":"value"}`。   - **key**：用户ID，根据userIdType设置。 - **value**：用户名。   例如：{123456:"钉三多"}  **[!NOTE]**  如果key、value都为\*\*@ALL\*\*则判断@所有人。 |
| cardOptions | Object | 否 | 卡片操作。 |
| supportForward | Boolean | 否 | 是否支持转发。   - **true**：支持 - **false**：不支持 |
| pullStrategy | Boolean | 否 | 是否开启卡片纯拉模式，   - true：开启卡片纯拉模式 - false：不开启卡片纯拉模式   **[!NOTE]**  纯拉模式，参见[实现置顶卡片纯拉模式](0736-pure-pull-mode-process-guide.md)。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 返回结果。 |
| result | Object | 创建卡片结果。 |
| processQueryKey | String | 用于业务方后续查看已读列表的查询key。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interactiveCards/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxx
Content-Type:application/json

{
  "cardTemplateId" : "card",
  "openConversationId" : "cid",
  "receiverUserIdList" : [ "user1" ],
  "outTrackId" : "trackId",
  "robotCode" : "robot",
  "conversationType" : 1,
  "callbackRouteKey" : "eafsingjdlsxxx",
  "cardData" : {
    "cardParamMap" : {
      "key" : "test"
    },
    "cardMediaIdParamMap" : {
      "key" : "test"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "test"
      },
      "cardMediaIdParamMap" : {
        "key" : "test"
      }
    }
  },
  "chatBotId" : "123",
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
        SendInteractiveCardHeaders sendInteractiveCardHeaders = new SendInteractiveCardHeaders();
        sendInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendInteractiveCardRequest.SendInteractiveCardRequestCardOptions cardOptions = new SendInteractiveCardRequest.SendInteractiveCardRequestCardOptions()
                .setSupportForward(true);
        java.util.Map<String, String> atOpenIds = TeaConverter.buildMap(
            new TeaPair("key", "{123456:\"钉三多\"}")
        );
        java.util.Map<String, String> privateDataValueKeyCardMediaIdParamMap = TeaConverter.buildMap(
            new TeaPair("key", "test")
        );
        java.util.Map<String, String> privateDataValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "test")
        );
        PrivateDataValue privateDataValueKey = new PrivateDataValue()
                .setCardParamMap(privateDataValueKeyCardParamMap)
                .setCardMediaIdParamMap(privateDataValueKeyCardMediaIdParamMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        java.util.Map<String, String> cardDataCardMediaIdParamMap = TeaConverter.buildMap(
            new TeaPair("key", "test")
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "test")
        );
        SendInteractiveCardRequest.SendInteractiveCardRequestCardData cardData = new SendInteractiveCardRequest.SendInteractiveCardRequestCardData()
                .setCardParamMap(cardDataCardParamMap)
                .setCardMediaIdParamMap(cardDataCardMediaIdParamMap);
        SendInteractiveCardRequest sendInteractiveCardRequest = new SendInteractiveCardRequest()
                .setCardTemplateId("card")
                .setOpenConversationId("cid")
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "user1"
                ))
                .setOutTrackId("trackId")
                .setRobotCode("robot")
                .setConversationType(1)
                .setCallbackRouteKey("eafsingjdlsxxx")
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setChatBotId("123")
                .setUserIdType(1)
                .setAtOpenIds(atOpenIds)
                .setCardOptions(cardOptions)
                .setPullStrategy(false);
        try {
            client.sendInteractiveCardWithOptions(sendInteractiveCardRequest, sendInteractiveCardHeaders, new RuntimeOptions());
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
        send_interactive_card_headers = dingtalkim__1__0_models.SendInteractiveCardHeaders()
        send_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_options = dingtalkim__1__0_models.SendInteractiveCardRequestCardOptions(
            support_forward=True
        )
        at_open_ids = {
            'key': '{123456:"钉三多"}'
        }
        private_data_value_key_card_media_id_param_map = {
            'key': 'test'
        }
        private_data_value_key_card_param_map = {
            'key': 'test'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map,
            card_media_id_param_map=private_data_value_key_card_media_id_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_media_id_param_map = {
            'key': 'test'
        }
        card_data_card_param_map = {
            'key': 'test'
        }
        card_data = dingtalkim__1__0_models.SendInteractiveCardRequestCardData(
            card_param_map=card_data_card_param_map,
            card_media_id_param_map=card_data_card_media_id_param_map
        )
        send_interactive_card_request = dingtalkim__1__0_models.SendInteractiveCardRequest(
            card_template_id='card',
            open_conversation_id='cid',
            receiver_user_id_list=[
                'user1'
            ],
            out_track_id='trackId',
            robot_code='robot',
            conversation_type=1,
            callback_route_key='eafsingjdlsxxx',
            card_data=card_data,
            private_data=private_data,
            chat_bot_id='123',
            user_id_type=1,
            at_open_ids=at_open_ids,
            card_options=card_options,
            pull_strategy=False
        )
        try:
            client.send_interactive_card_with_options(send_interactive_card_request, send_interactive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_interactive_card_headers = dingtalkim__1__0_models.SendInteractiveCardHeaders()
        send_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_options = dingtalkim__1__0_models.SendInteractiveCardRequestCardOptions(
            support_forward=True
        )
        at_open_ids = {
            'key': '{123456:"钉三多"}'
        }
        private_data_value_key_card_media_id_param_map = {
            'key': 'test'
        }
        private_data_value_key_card_param_map = {
            'key': 'test'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map,
            card_media_id_param_map=private_data_value_key_card_media_id_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_media_id_param_map = {
            'key': 'test'
        }
        card_data_card_param_map = {
            'key': 'test'
        }
        card_data = dingtalkim__1__0_models.SendInteractiveCardRequestCardData(
            card_param_map=card_data_card_param_map,
            card_media_id_param_map=card_data_card_media_id_param_map
        )
        send_interactive_card_request = dingtalkim__1__0_models.SendInteractiveCardRequest(
            card_template_id='card',
            open_conversation_id='cid',
            receiver_user_id_list=[
                'user1'
            ],
            out_track_id='trackId',
            robot_code='robot',
            conversation_type=1,
            callback_route_key='eafsingjdlsxxx',
            card_data=card_data,
            private_data=private_data,
            chat_bot_id='123',
            user_id_type=1,
            at_open_ids=at_open_ids,
            card_options=card_options,
            pull_strategy=False
        )
        try:
            await client.send_interactive_card_with_options_async(send_interactive_card_request, send_interactive_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendInteractiveCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendInteractiveCardRequest\cardOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\PrivateDataValue;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendInteractiveCardRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendInteractiveCardRequest;
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
        $sendInteractiveCardHeaders = new SendInteractiveCardHeaders([]);
        $sendInteractiveCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cardOptions = new cardOptions([
            "supportForward" => true
        ]);
        $atOpenIds = [
            "key" => "{123456:\"钉三多\"}"
        ];
        $privateDataValueKeyCardMediaIdParamMap = [
            "key" => "test"
        ];
        $privateDataValueKeyCardParamMap = [
            "key" => "test"
        ];
        $privateDataValueKey = new PrivateDataValue([
            "cardParamMap" => $privateDataValueKeyCardParamMap,
            "cardMediaIdParamMap" => $privateDataValueKeyCardMediaIdParamMap
        ]);
        $privateData = [
            "privateDataValueKey" => $privateDataValueKey
        ];
        $cardDataCardMediaIdParamMap = [
            "key" => "test"
        ];
        $cardDataCardParamMap = [
            "key" => "test"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap,
            "cardMediaIdParamMap" => $cardDataCardMediaIdParamMap
        ]);
        $sendInteractiveCardRequest = new SendInteractiveCardRequest([
            "cardTemplateId" => "card",
            "openConversationId" => "cid",
            "receiverUserIdList" => [
                "user1"
            ],
            "outTrackId" => "trackId",
            "robotCode" => "robot",
            "conversationType" => 1,
            "callbackRouteKey" => "eafsingjdlsxxx",
            "cardData" => $cardData,
            "privateData" => $privateData,
            "chatBotId" => "123",
            "userIdType" => 1,
            "atOpenIds" => $atOpenIds,
            "cardOptions" => $cardOptions,
            "pullStrategy" => false
        ]);
        try {
            $client->sendInteractiveCardWithOptions($sendInteractiveCardRequest, $sendInteractiveCardHeaders, new RuntimeOptions([]));
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

  sendInteractiveCardHeaders := &dingtalkim_1_0.SendInteractiveCardHeaders{}
  sendInteractiveCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cardOptions := &dingtalkim_1_0.SendInteractiveCardRequestCardOptions{
    SupportForward: tea.Bool(true),
  }
  atOpenIds := map[string]*string{
    "key": tea.String("{123456:\"钉三多\"}"),
  }
  privateDataValueKeyCardMediaIdParamMap := map[string]*string{
    "key": tea.String("test"),
  }
  privateDataValueKeyCardParamMap := map[string]*string{
    "key": tea.String("test"),
  }
  privateDataValueKey := &dingtalkim_1_0.PrivateDataValue{
    CardParamMap: privateDataValueKeyCardParamMap,
    CardMediaIdParamMap: privateDataValueKeyCardMediaIdParamMap,
  }
  privateData := map[string]*dingtalkim_1_0.PrivateDataValue{
    "privateDataValueKey": privateDataValueKey,
  }
  cardDataCardMediaIdParamMap := map[string]*string{
    "key": tea.String("test"),
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("test"),
  }
  cardData := &dingtalkim_1_0.SendInteractiveCardRequestCardData{
    CardParamMap: cardDataCardParamMap,
    CardMediaIdParamMap: cardDataCardMediaIdParamMap,
  }
  sendInteractiveCardRequest := &dingtalkim_1_0.SendInteractiveCardRequest{
    CardTemplateId: tea.String("card"),
    OpenConversationId: tea.String("cid"),
    ReceiverUserIdList: []*string{tea.String("user1")},
    OutTrackId: tea.String("trackId"),
    RobotCode: tea.String("robot"),
    ConversationType: tea.Int32(1),
    CallbackRouteKey: tea.String("eafsingjdlsxxx"),
    CardData: cardData,
    PrivateData: privateData,
    ChatBotId: tea.String("123"),
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
    _, _err = client.SendInteractiveCardWithOptions(sendInteractiveCardRequest, sendInteractiveCardHeaders, &util.RuntimeOptions{})
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
    let sendInteractiveCardHeaders = new $dingtalkim_1_0.SendInteractiveCardHeaders({ });
    sendInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let cardOptions = new $dingtalkim_1_0.SendInteractiveCardRequestCardOptions({
      supportForward: true,
    });
    let atOpenIds = {
      key: "{123456:\"钉三多\"}",
    };
    let privateDataValueKeyCardMediaIdParamMap = {
      key: "test",
    };
    let privateDataValueKeyCardParamMap = {
      key: "test",
    };
    let privateDataValueKey = new $dingtalkim_1_0.PrivateDataValue({
      cardParamMap: privateDataValueKeyCardParamMap,
      cardMediaIdParamMap: privateDataValueKeyCardMediaIdParamMap,
    });
    let privateData = {
      privateDataValueKey: privateDataValueKey,
    };
    let cardDataCardMediaIdParamMap = {
      key: "test",
    };
    let cardDataCardParamMap = {
      key: "test",
    };
    let cardData = new $dingtalkim_1_0.SendInteractiveCardRequestCardData({
      cardParamMap: cardDataCardParamMap,
      cardMediaIdParamMap: cardDataCardMediaIdParamMap,
    });
    let sendInteractiveCardRequest = new $dingtalkim_1_0.SendInteractiveCardRequest({
      cardTemplateId: "card",
      openConversationId: "cid",
      receiverUserIdList: [
        "user1"
      ],
      outTrackId: "trackId",
      robotCode: "robot",
      conversationType: 1,
      callbackRouteKey: "eafsingjdlsxxx",
      cardData: cardData,
      privateData: privateData,
      chatBotId: "123",
      userIdType: 1,
      atOpenIds: atOpenIds,
      cardOptions: cardOptions,
      pullStrategy: false,
    });
    try {
      await client.sendInteractiveCardWithOptions(sendInteractiveCardRequest, sendInteractiveCardHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardHeaders sendInteractiveCardHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardHeaders();
            sendInteractiveCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardRequest.SendInteractiveCardRequestCardOptions cardOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardRequest.SendInteractiveCardRequestCardOptions
            {
                SupportForward = true,
            };
            Dictionary<string, string> atOpenIds = new Dictionary<string, string>
            {
                {"key", "{123456:\"钉三多\"}"},
            };
            Dictionary<string, string> privateDataValueKeyCardMediaIdParamMap = new Dictionary<string, string>
            {
                {"key", "test"},
            };
            Dictionary<string, string> privateDataValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "test"},
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
                {"key", "test"},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "test"},
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardRequest.SendInteractiveCardRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardRequest.SendInteractiveCardRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
                CardMediaIdParamMap = cardDataCardMediaIdParamMap,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardRequest sendInteractiveCardRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendInteractiveCardRequest
            {
                CardTemplateId = "card",
                OpenConversationId = "cid",
                ReceiverUserIdList = new List<string>
                {
                    "user1"
                },
                OutTrackId = "trackId",
                RobotCode = "robot",
                ConversationType = 1,
                CallbackRouteKey = "eafsingjdlsxxx",
                CardData = cardData,
                PrivateData = privateData,
                ChatBotId = "123",
                UserIdType = 1,
                AtOpenIds = atOpenIds,
                CardOptions = cardOptions,
                PullStrategy = false,
            };
            try
            {
                client.SendInteractiveCardWithOptions(sendInteractiveCardRequest, sendInteractiveCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | sceneGroup.checkFailed | 场景群权限校验失败 | 场景群权限校验失败 |
| 400 | queryChatbot.wrong | 查询机器人失败 | 查询机器人失败 |
| 400 | cardInstance.wrong | 创建卡片实例失败，先检查卡片模板是否已发布 | 创建卡片实例失败，先检查卡片模板是否已发布 |
| 400 | cidParse.wrong | 群ID解码失败 | 群ID解码失败 |
| 400 | card.templateEmpty | 卡片模板ID为空 | 卡片模板ID为空 |
| 400 | userInfo.convertError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | card.outTraceIdError | 卡片业务标识信息格式非法 | 卡片业务标识信息格式非法 |
| 400 | card.outTraceIdEmpty | 业务标识outTrackId为空 | 业务标识outTrackId为空 |
| 400 | chatbot.notFound | 机器人不存在 | 机器人不存在 |
| 400 | invalidParameter.cid.empty | 群id为空 | 群id为空 |
| 400 | sendCardMessageFailed | 发送卡片失败 | 发送卡片失败 |
| 400 | sceneGroupNotFound | 非场景群 | 非场景群 |
| 400 | duplicateKey | 卡片模板占位符有重复Key | 卡片模板占位符有重复Key |
| 400 | getPictureFailed | 获取图片url失败 | 获取图片url失败 |
| 400 | org.notOwn.group | 群不属于当前企业 | 群不属于当前企业 |
| 400 | send.oa.failed | 发工作通知失败，请稍后重试 | 发工作通知失败，请稍后重试 |
| 400 | outTrackId.exceed.limit | outTrackId长度超限 | outTrackId长度超限 |
| 400 | invalid.robotCode | 无效的robotCode | 无效的robotCode |
| 500 | systemBusy | 系统繁忙 | 系统异常错误 |
| 500 | systemError | 系统错误 | 系统错误 |
