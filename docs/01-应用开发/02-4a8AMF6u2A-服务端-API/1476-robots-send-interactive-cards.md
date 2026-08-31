---
title: "机器人发送互动卡片（普通版）"
source_url: "https://open.dingtalk.com/document/development/robots-send-interactive-cards"
namespace: "development"
slug: "robots-send-interactive-cards"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 机器人发送互动卡片（普通版）"
doc_id: "sbFLvRZ4H1"
updated_at: "2026-08-25 09:37:05"
---

> Source: https://open.dingtalk.com/document/development/robots-send-interactive-cards
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 机器人 > 机器人发送互动卡片（普通版）
> Updated: 2026-08-25 09:37:05

# 机器人发送互动卡片（普通版）

本文档介绍了机器人发送互动卡片（普通版）。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建并投放卡片](0783-create-and-deliver-cards.md)接口，已接入用户不受影响。

### 接口功能介绍

通过应用机器人发送普通版互动卡片消息，相比于高级版，普通版通过内置卡片模板，减少卡片模板构建过程，以提升开发效率，更多详情参见[互动卡片普通版](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0001-platform-building-overview.md)。

**桌面端：**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5281267871/p1096170.png)

**移动端：**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5281267871/p1096171.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/im/v1.0/robot/interactiveCards/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "String",
  "openConversationId" : "String",
  "singleChatReceiver" : "String",
  "cardBizId" : "String",
  "robotCode" : "String",
  "callbackUrl" : "String",
  "cardData" : "String",
  "userIdPrivateDataMap" : "String",
  "unionIdPrivateDataMap" : "String",
  "sendOptions" : {
    "atUserListJson" : "String",
    "atAll" : Boolean,
    "receiverListJson" : "String",
    "cardPropertyJson" : "String"
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
| cardTemplateId | String | 是 | 卡片搭建平台模板ID，固定值填写为`StandardCard`。 |
| openConversationId | String | 否 | 接收卡片的加密群ID，特指多人群会话（非单聊）。  **[!NOTE]**   - 基于群模板创建的群，请参考[创建群](1486-create-a-scene-group-v2.md)。 - 安装群聊酷应用的群，请参考[酷应用](../01-XOnnmGCTbn-开发指南/0042-coolapp-overview.md)。   `openConversationId`和`singleChatReceiver` 二选一必填。 |
| singleChatReceiver | String | 否 | 单聊会话接收者json串。  **[!NOTE]**  `openConversationId`和`singleChatReceiver` 二选一必填。 |
| cardBizId | String | 是 | 唯一标识一张卡片的外部ID，卡片幂等ID，可用于更新或重复发送同一卡片到多个群会话。  **[!NOTE]**   - 不超过100字符，建议64字符以内。 - 若使用新的 `cardTemplateId` 或 `cardData` 等参数，则需要生成一个全新的 outTrackId，否则更改不会生效。 |
| robotCode | String | 是 | 机器人的编码，参见[机器人名词表-robotCode](0698-development-robot-overview.md)内容，获取`robotCode`。 |
| callbackUrl | String | 否 | 可控制卡片回调的URL，不填则无需回调。 |
| cardData | String | 是 | 卡片模板文本内容参数，卡片json结构体。 |
| userIdPrivateDataMap | String | 否 | 卡片模板userId差异用户参数，json结构体。 |
| unionIdPrivateDataMap | String | 否 | 卡片模板unionId差异用户参数，json结构体。 |
| sendOptions | Object | 否 | 互动卡片发送选项。 |
| atUserListJson | String | 否 | 消息@人，最大@人员人数为30。  JSON格式如下：   ``` [     {         "nickName": "张三",         "userId": "userId0001"     },     {         "nickName": "李四",         "unionId": "unionId001"     } ] ``` |
| atAll | Boolean | 否 | 是否@所有人。 |
| receiverListJson | String | 否 | 消息仅部分人可见的接收人列表。  **[!NOTE]**    为空时则群所有人可见。  JSON格式：   ``` [     {         "userId": "userId0001"     },     {         "unionId": "unionId001"     } ] ``` |
| cardPropertyJson | String | 否 | 卡片特殊属性json字符串。 |
| pullStrategy | Boolean | 否 | 是否开启卡片纯拉模式：   - true：开启卡片纯拉模式 - false：不开启卡片纯拉模式   **[!NOTE]**  纯拉模式，参见[实现置顶卡片纯拉模式](0736-pure-pull-mode-process-guide.md)。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| processQueryKey | String | 用于业务方后续查看已读列表的查询key。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/v1.0/robot/interactiveCards/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "cardTemplateId" : "xxxxxxxx",
  "openConversationId" : "cidXXXX",
  "singleChatReceiver" : "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
  "cardBizId" : "cardXXXX01",
  "robotCode" : "xxxxxx",
  "callbackUrl" : "https://***",
  "cardData" : "{   \"config\": {     \"autoLayout\": true,     \"enableForward\": true   },   \"header\": {     \"title\": {       \"type\": \"text\",       \"text\": \"钉钉卡片\"     },     \"logo\": \"@lALPDfJ6V_FPDmvNAfTNAfQ\"   },   \"contents\": [     {       \"type\": \"text\",       \"text\": \"钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。\",       \"id\": \"text_1658220665485\" } ]}",
  "userIdPrivateDataMap" : "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
  "unionIdPrivateDataMap" : "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
  "sendOptions" : {
    "atUserListJson" : "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
    "atAll" : false,
    "receiverListJson" : "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
    "cardPropertyJson" : "{}"
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
        SendRobotInteractiveCardHeaders sendRobotInteractiveCardHeaders = new SendRobotInteractiveCardHeaders();
        sendRobotInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendRobotInteractiveCardRequest.SendRobotInteractiveCardRequestSendOptions sendOptions = new SendRobotInteractiveCardRequest.SendRobotInteractiveCardRequestSendOptions()
                .setAtUserListJson("[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]")
                .setAtAll(false)
                .setReceiverListJson("[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]")
                .setCardPropertyJson("{}");
        SendRobotInteractiveCardRequest sendRobotInteractiveCardRequest = new SendRobotInteractiveCardRequest()
                .setCardTemplateId("xxxxxxxx")
                .setOpenConversationId("cidXXXX")
                .setSingleChatReceiver("以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}")
                .setCardBizId("cardXXXX01")
                .setRobotCode("xxxxxx")
                .setCallbackUrl("https://***")
                .setCardData("{   \"config\": {     \"autoLayout\": true,     \"enableForward\": true   },   \"header\": {     \"title\": {       \"type\": \"text\",       \"text\": \"钉钉卡片\"     },     \"logo\": \"@lALPDfJ6V_FPDmvNAfTNAfQ\"   },   \"contents\": [     {       \"type\": \"text\",       \"text\": \"钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。\",       \"id\": \"text_1658220665485\" } ]}")
                .setUserIdPrivateDataMap("{\"userId0001\":{\"xxxx\":\"xxxx\"}}")
                .setUnionIdPrivateDataMap("{\"unionId0001\":{\"xxxx\":\"xxxx\"}}")
                .setSendOptions(sendOptions)
                .setPullStrategy(false);
        try {
            client.sendRobotInteractiveCardWithOptions(sendRobotInteractiveCardRequest, sendRobotInteractiveCardHeaders, new RuntimeOptions());
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
        send_robot_interactive_card_headers = dingtalkim__1__0_models.SendRobotInteractiveCardHeaders()
        send_robot_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_options = dingtalkim__1__0_models.SendRobotInteractiveCardRequestSendOptions(
            at_user_list_json='[{"nickName":"张三","userId":"userId0001"},{"nickName":"李四","unionId":"unionId001"}]',
            at_all=False,
            receiver_list_json='[{"userId":"userId0001"},{"unionId":"unionId001"}]',
            card_property_json='{}'
        )
        send_robot_interactive_card_request = dingtalkim__1__0_models.SendRobotInteractiveCardRequest(
            card_template_id='xxxxxxxx',
            open_conversation_id='cidXXXX',
            single_chat_receiver='以userId为例：{"userId":"userId0001"}；以unionId为例{"unionId":"unionId001"}',
            card_biz_id='cardXXXX01',
            robot_code='xxxxxx',
            callback_url='https://***',
            card_data='{   "config": {     "autoLayout": true,     "enableForward": true   },   "header": {     "title": {       "type": "text",       "text": "钉钉卡片"     },     "logo": "@lALPDfJ6V_FPDmvNAfTNAfQ"   },   "contents": [     {       "type": "text",       "text": "钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。",       "id": "text_1658220665485" } ]}',
            user_id_private_data_map='{"userId0001":{"xxxx":"xxxx"}}',
            union_id_private_data_map='{"unionId0001":{"xxxx":"xxxx"}}',
            send_options=send_options,
            pull_strategy=False
        )
        try:
            client.send_robot_interactive_card_with_options(send_robot_interactive_card_request, send_robot_interactive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_robot_interactive_card_headers = dingtalkim__1__0_models.SendRobotInteractiveCardHeaders()
        send_robot_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_options = dingtalkim__1__0_models.SendRobotInteractiveCardRequestSendOptions(
            at_user_list_json='[{"nickName":"张三","userId":"userId0001"},{"nickName":"李四","unionId":"unionId001"}]',
            at_all=False,
            receiver_list_json='[{"userId":"userId0001"},{"unionId":"unionId001"}]',
            card_property_json='{}'
        )
        send_robot_interactive_card_request = dingtalkim__1__0_models.SendRobotInteractiveCardRequest(
            card_template_id='xxxxxxxx',
            open_conversation_id='cidXXXX',
            single_chat_receiver='以userId为例：{"userId":"userId0001"}；以unionId为例{"unionId":"unionId001"}',
            card_biz_id='cardXXXX01',
            robot_code='xxxxxx',
            callback_url='https://***',
            card_data='{   "config": {     "autoLayout": true,     "enableForward": true   },   "header": {     "title": {       "type": "text",       "text": "钉钉卡片"     },     "logo": "@lALPDfJ6V_FPDmvNAfTNAfQ"   },   "contents": [     {       "type": "text",       "text": "钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。",       "id": "text_1658220665485" } ]}',
            user_id_private_data_map='{"userId0001":{"xxxx":"xxxx"}}',
            union_id_private_data_map='{"unionId0001":{"xxxx":"xxxx"}}',
            send_options=send_options,
            pull_strategy=False
        )
        try:
            await client.send_robot_interactive_card_with_options_async(send_robot_interactive_card_request, send_robot_interactive_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendRobotInteractiveCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendRobotInteractiveCardRequest\sendOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendRobotInteractiveCardRequest;
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
        $sendRobotInteractiveCardHeaders = new SendRobotInteractiveCardHeaders([]);
        $sendRobotInteractiveCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendOptions = new sendOptions([
            "atUserListJson" => "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
            "atAll" => false,
            "receiverListJson" => "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
            "cardPropertyJson" => "{}"
        ]);
        $sendRobotInteractiveCardRequest = new SendRobotInteractiveCardRequest([
            "cardTemplateId" => "xxxxxxxx",
            "openConversationId" => "cidXXXX",
            "singleChatReceiver" => "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
            "cardBizId" => "cardXXXX01",
            "robotCode" => "xxxxxx",
            "callbackUrl" => "https://***",
            "cardData" => "{   \"config\": {     \"autoLayout\": true,     \"enableForward\": true   },   \"header\": {     \"title\": {       \"type\": \"text\",       \"text\": \"钉钉卡片\"     },     \"logo\": \"@lALPDfJ6V_FPDmvNAfTNAfQ\"   },   \"contents\": [     {       \"type\": \"text\",       \"text\": \"钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。\",       \"id\": \"text_1658220665485\" } ]}",
            "userIdPrivateDataMap" => "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
            "unionIdPrivateDataMap" => "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
            "sendOptions" => $sendOptions,
            "pullStrategy" => false
        ]);
        try {
            $client->sendRobotInteractiveCardWithOptions($sendRobotInteractiveCardRequest, $sendRobotInteractiveCardHeaders, new RuntimeOptions([]));
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

  sendRobotInteractiveCardHeaders := &dingtalkim_1_0.SendRobotInteractiveCardHeaders{}
  sendRobotInteractiveCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendOptions := &dingtalkim_1_0.SendRobotInteractiveCardRequestSendOptions{
    AtUserListJson: tea.String("[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]"),
    AtAll: tea.Bool(false),
    ReceiverListJson: tea.String("[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]"),
    CardPropertyJson: tea.String("{}"),
  }
  sendRobotInteractiveCardRequest := &dingtalkim_1_0.SendRobotInteractiveCardRequest{
    CardTemplateId: tea.String("xxxxxxxx"),
    OpenConversationId: tea.String("cidXXXX"),
    SingleChatReceiver: tea.String("以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}"),
    CardBizId: tea.String("cardXXXX01"),
    RobotCode: tea.String("xxxxxx"),
    CallbackUrl: tea.String("https://***"),
    CardData: tea.String("{   \"config\": {     \"autoLayout\": true,     \"enableForward\": true   },   \"header\": {     \"title\": {       \"type\": \"text\",       \"text\": \"钉钉卡片\"     },     \"logo\": \"@lALPDfJ6V_FPDmvNAfTNAfQ\"   },   \"contents\": [     {       \"type\": \"text\",       \"text\": \"钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。\",       \"id\": \"text_1658220665485\" } ]}"),
    UserIdPrivateDataMap: tea.String("{\"userId0001\":{\"xxxx\":\"xxxx\"}}"),
    UnionIdPrivateDataMap: tea.String("{\"unionId0001\":{\"xxxx\":\"xxxx\"}}"),
    SendOptions: sendOptions,
    PullStrategy: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendRobotInteractiveCardWithOptions(sendRobotInteractiveCardRequest, sendRobotInteractiveCardHeaders, &util.RuntimeOptions{})
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
    let sendRobotInteractiveCardHeaders = new $dingtalkim_1_0.SendRobotInteractiveCardHeaders({ });
    sendRobotInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sendOptions = new $dingtalkim_1_0.SendRobotInteractiveCardRequestSendOptions({
      atUserListJson: "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
      atAll: false,
      receiverListJson: "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
      cardPropertyJson: "{}",
    });
    let sendRobotInteractiveCardRequest = new $dingtalkim_1_0.SendRobotInteractiveCardRequest({
      cardTemplateId: "xxxxxxxx",
      openConversationId: "cidXXXX",
      singleChatReceiver: "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
      cardBizId: "cardXXXX01",
      robotCode: "xxxxxx",
      callbackUrl: "https://***",
      cardData: "{   \"config\": {     \"autoLayout\": true,     \"enableForward\": true   },   \"header\": {     \"title\": {       \"type\": \"text\",       \"text\": \"钉钉卡片\"     },     \"logo\": \"@lALPDfJ6V_FPDmvNAfTNAfQ\"   },   \"contents\": [     {       \"type\": \"text\",       \"text\": \"钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。\",       \"id\": \"text_1658220665485\" } ]}",
      userIdPrivateDataMap: "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
      unionIdPrivateDataMap: "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
      sendOptions: sendOptions,
      pullStrategy: false,
    });
    try {
      await client.sendRobotInteractiveCardWithOptions(sendRobotInteractiveCardRequest, sendRobotInteractiveCardHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotInteractiveCardHeaders sendRobotInteractiveCardHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotInteractiveCardHeaders();
            sendRobotInteractiveCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotInteractiveCardRequest.SendRobotInteractiveCardRequestSendOptions sendOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotInteractiveCardRequest.SendRobotInteractiveCardRequestSendOptions
            {
                AtUserListJson = "[{\"nickName\":\"张三\",\"userId\":\"userId0001\"},{\"nickName\":\"李四\",\"unionId\":\"unionId001\"}]",
                AtAll = false,
                ReceiverListJson = "[{\"userId\":\"userId0001\"},{\"unionId\":\"unionId001\"}]",
                CardPropertyJson = "{}",
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotInteractiveCardRequest sendRobotInteractiveCardRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotInteractiveCardRequest
            {
                CardTemplateId = "xxxxxxxx",
                OpenConversationId = "cidXXXX",
                SingleChatReceiver = "以userId为例：{\"userId\":\"userId0001\"}；以unionId为例{\"unionId\":\"unionId001\"}",
                CardBizId = "cardXXXX01",
                RobotCode = "xxxxxx",
                CallbackUrl = "https://***",
                CardData = "{   \"config\": {     \"autoLayout\": true,     \"enableForward\": true   },   \"header\": {     \"title\": {       \"type\": \"text\",       \"text\": \"钉钉卡片\"     },     \"logo\": \"@lALPDfJ6V_FPDmvNAfTNAfQ\"   },   \"contents\": [     {       \"type\": \"text\",       \"text\": \"钉钉正在为各行各业提供专业解决方案，沉淀钉钉1900万企业组织核心业务场景，提供专属钉钉、教育、医疗、新零售等多行业多维度的解决方案。\",       \"id\": \"text_1658220665485\" } ]}",
                UserIdPrivateDataMap = "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
                UnionIdPrivateDataMap = "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
                SendOptions = sendOptions,
                PullStrategy = false,
            };
            try
            {
                client.SendRobotInteractiveCardWithOptions(sendRobotInteractiveCardRequest, sendRobotInteractiveCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | system.error | 未知的系统错误 | 未知的系统错误 |
| 400 | param.error | 参数无效 | 参数无效 |
| 400 | param.isNotJson | 参数必须是json | 参数必须是json |
| 400 | invalid.user | 无效的用户ID | 无效的用户ID |
| 400 | invalid.openConversationId | 无效的openConversationId | 无效的openConversationId |
| 400 | invalid.robotCode | 无效的机器人标识 | 无效的机器人标识 |
| 400 | template.isNotExist | 模板不存在 | 模板不存在 |
| 400 | create.cardInstance.failed | 创建互动卡片实例失败 | 创建互动卡片实例失败 |
| 400 | send.cardMsg.failed | 发送互动卡片消息失败 | 发送互动卡片消息失败 |
| 400 | invalid.bizId | 互动卡片BIZID无效 | 互动卡片BIZID无效 |
| 400 | cardInstance.notExist | 互动卡片实例不存在 | 互动卡片实例不存在 |
| 400 | cardMessage.sendFailed | 发送互动卡片消息失败 | 发送互动卡片消息失败 |
