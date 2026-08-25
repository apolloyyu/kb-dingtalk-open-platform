---
title: "更新机器人发送互动卡片（普通版）"
source_url: "https://open.dingtalk.com/document/development/update-the-robot-to-send-interactive-cards"
namespace: "development"
slug: "update-the-robot-to-send-interactive-cards"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 更新机器人发送互动卡片（普通版）"
doc_id: "MjvbWTjG4V"
updated_at: "2026-08-25 09:37:12"
---

> Source: https://open.dingtalk.com/document/development/update-the-robot-to-send-interactive-cards
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 机器人 > 更新机器人发送互动卡片（普通版）
> Updated: 2026-08-25 09:37:12

# 更新机器人发送互动卡片（普通版）

更新机器人发送互动卡片。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新卡片](0782-interactive-card-update-interface.md)接口，已接入用户不受影响。

如何发送互动卡片普通版流程，详情参见[互动卡片普通版接入流程](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0010-ding-card-interactive-card-operation-process.md)。

互动卡片示例一：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2381267871/p1096273.png)

互动卡片示例二：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2381267871/p1096274.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
PUT /v1.0/im/robots/interactiveCards HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardBizId" : "String",
  "cardData" : "String",
  "userIdPrivateDataMap" : "String",
  "unionIdPrivateDataMap" : "String",
  "updateOptions" : {
    "updateCardDataByKey" : Boolean,
    "updatePrivateDataByKey" : Boolean
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
| cardBizId | String | 是 | 唯一标识一张卡片的外部ID（卡片幂等ID，可用于更新或重复发送同一卡片到多个群会话）。需与机器人发送互动卡片（普通版）接口Body参数中cardBizId保持一致，请参见[机器人发送互动卡片（普通版）](1474-robots-send-interactive-cards.md)接口。 |
| cardData | String | 否 | 卡片模板文本内容，在[卡片搭建平台](https://card.dingtalk.com/card-builder)设计模板后，复制右侧示例代码信息即为该参数值。a6bdd5ba-48bb-4697-8e59-8d4639a97324 |
| userIdPrivateDataMap | String | 否 | 卡片模板userId差异用户参数，json结构体，表示特殊消息接收人接收卡片的具体内容信息。  例如：群主为userId为userId0001，需要展示不同与普通群员cardData的数据内容信息，可以使用userIdPrivateDataMap实现数据差异化。  参数格式为：`"{"userId值":{卡片消息cardData参数值}}"`。 |
| unionIdPrivateDataMap | String | 否 | 卡片模板unionId差异用户参数，json结构体，表示特殊消息接收人接收卡片的具体内容信息。  例如：群主为unionId为unionId0001，需要展示不同与普通群员cardData的数据内容信息，可以使用**unionIdPrivateDataMap**实现数据差异化。  参数格式为：`"{"unionId值":{卡片消息cardData参数值}}"`。 |
| updateOptions | Object | 否 | 互动卡片更新选项。 |
| updateCardDataByKey | Boolean | 否 | 是否按key更新数据（默认全局更新）：   - true：按key更新数据。 - false：全局更新。 |
| updatePrivateDataByKey | Boolean | 否 | 是否按key更新数据（默认全局更新）：   - true：按key更新数据。 - false：全局更新。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| processQueryKey | String | 加密消息id，根据此id可查询消息已读状态和撤回消息，请参考[查询企业机器人群聊消息用户已读状态](0722-chatbot-queries-the-read-status-of-a-message.md)和[企业机器人撤回内部群消息](0725-enterprise-chatbot-withdraws-internal-group-messages.md)。 |

## 示例

**请求示例**

HTTP

```
PUT /v1.0/im/robots/interactiveCards HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "cardBizId" : "cardXXXX01",
  "cardData" : "根据具体的cardTemplateId参考文档格式",
  "userIdPrivateDataMap" : "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
  "unionIdPrivateDataMap" : "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
  "updateOptions" : {
    "updateCardDataByKey" : false,
    "updatePrivateDataByKey" : false
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
        UpdateRobotInteractiveCardHeaders updateRobotInteractiveCardHeaders = new UpdateRobotInteractiveCardHeaders();
        updateRobotInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateRobotInteractiveCardRequest.UpdateRobotInteractiveCardRequestUpdateOptions updateOptions = new UpdateRobotInteractiveCardRequest.UpdateRobotInteractiveCardRequestUpdateOptions()
                .setUpdateCardDataByKey(false)
                .setUpdatePrivateDataByKey(false);
        UpdateRobotInteractiveCardRequest updateRobotInteractiveCardRequest = new UpdateRobotInteractiveCardRequest()
                .setCardBizId("cardXXXX01")
                .setCardData("根据具体的cardTemplateId参考文档格式")
                .setUserIdPrivateDataMap("{\"userId0001\":{\"xxxx\":\"xxxx\"}}")
                .setUnionIdPrivateDataMap("{\"unionId0001\":{\"xxxx\":\"xxxx\"}}")
                .setUpdateOptions(updateOptions);
        try {
            client.updateRobotInteractiveCardWithOptions(updateRobotInteractiveCardRequest, updateRobotInteractiveCardHeaders, new RuntimeOptions());
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
        update_robot_interactive_card_headers = dingtalkim__1__0_models.UpdateRobotInteractiveCardHeaders()
        update_robot_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_options = dingtalkim__1__0_models.UpdateRobotInteractiveCardRequestUpdateOptions(
            update_card_data_by_key=False,
            update_private_data_by_key=False
        )
        update_robot_interactive_card_request = dingtalkim__1__0_models.UpdateRobotInteractiveCardRequest(
            card_biz_id='cardXXXX01',
            card_data='根据具体的cardTemplateId参考文档格式',
            user_id_private_data_map='{"userId0001":{"xxxx":"xxxx"}}',
            union_id_private_data_map='{"unionId0001":{"xxxx":"xxxx"}}',
            update_options=update_options
        )
        try:
            client.update_robot_interactive_card_with_options(update_robot_interactive_card_request, update_robot_interactive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_robot_interactive_card_headers = dingtalkim__1__0_models.UpdateRobotInteractiveCardHeaders()
        update_robot_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_options = dingtalkim__1__0_models.UpdateRobotInteractiveCardRequestUpdateOptions(
            update_card_data_by_key=False,
            update_private_data_by_key=False
        )
        update_robot_interactive_card_request = dingtalkim__1__0_models.UpdateRobotInteractiveCardRequest(
            card_biz_id='cardXXXX01',
            card_data='根据具体的cardTemplateId参考文档格式',
            user_id_private_data_map='{"userId0001":{"xxxx":"xxxx"}}',
            union_id_private_data_map='{"unionId0001":{"xxxx":"xxxx"}}',
            update_options=update_options
        )
        try:
            await client.update_robot_interactive_card_with_options_async(update_robot_interactive_card_request, update_robot_interactive_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateRobotInteractiveCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateRobotInteractiveCardRequest\updateOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateRobotInteractiveCardRequest;
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
        $updateRobotInteractiveCardHeaders = new UpdateRobotInteractiveCardHeaders([]);
        $updateRobotInteractiveCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateOptions = new updateOptions([
            "updateCardDataByKey" => false,
            "updatePrivateDataByKey" => false
        ]);
        $updateRobotInteractiveCardRequest = new UpdateRobotInteractiveCardRequest([
            "cardBizId" => "cardXXXX01",
            "cardData" => "根据具体的cardTemplateId参考文档格式",
            "userIdPrivateDataMap" => "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
            "unionIdPrivateDataMap" => "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
            "updateOptions" => $updateOptions
        ]);
        try {
            $client->updateRobotInteractiveCardWithOptions($updateRobotInteractiveCardRequest, $updateRobotInteractiveCardHeaders, new RuntimeOptions([]));
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

  updateRobotInteractiveCardHeaders := &dingtalkim_1_0.UpdateRobotInteractiveCardHeaders{}
  updateRobotInteractiveCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateOptions := &dingtalkim_1_0.UpdateRobotInteractiveCardRequestUpdateOptions{
    UpdateCardDataByKey: tea.Bool(false),
    UpdatePrivateDataByKey: tea.Bool(false),
  }
  updateRobotInteractiveCardRequest := &dingtalkim_1_0.UpdateRobotInteractiveCardRequest{
    CardBizId: tea.String("cardXXXX01"),
    CardData: tea.String("根据具体的cardTemplateId参考文档格式"),
    UserIdPrivateDataMap: tea.String("{\"userId0001\":{\"xxxx\":\"xxxx\"}}"),
    UnionIdPrivateDataMap: tea.String("{\"unionId0001\":{\"xxxx\":\"xxxx\"}}"),
    UpdateOptions: updateOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateRobotInteractiveCardWithOptions(updateRobotInteractiveCardRequest, updateRobotInteractiveCardHeaders, &util.RuntimeOptions{})
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
    let updateRobotInteractiveCardHeaders = new $dingtalkim_1_0.UpdateRobotInteractiveCardHeaders({ });
    updateRobotInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateOptions = new $dingtalkim_1_0.UpdateRobotInteractiveCardRequestUpdateOptions({
      updateCardDataByKey: false,
      updatePrivateDataByKey: false,
    });
    let updateRobotInteractiveCardRequest = new $dingtalkim_1_0.UpdateRobotInteractiveCardRequest({
      cardBizId: "cardXXXX01",
      cardData: "根据具体的cardTemplateId参考文档格式",
      userIdPrivateDataMap: "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
      unionIdPrivateDataMap: "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
      updateOptions: updateOptions,
    });
    try {
      await client.updateRobotInteractiveCardWithOptions(updateRobotInteractiveCardRequest, updateRobotInteractiveCardHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateRobotInteractiveCardHeaders updateRobotInteractiveCardHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateRobotInteractiveCardHeaders();
            updateRobotInteractiveCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateRobotInteractiveCardRequest.UpdateRobotInteractiveCardRequestUpdateOptions updateOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateRobotInteractiveCardRequest.UpdateRobotInteractiveCardRequestUpdateOptions
            {
                UpdateCardDataByKey = false,
                UpdatePrivateDataByKey = false,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateRobotInteractiveCardRequest updateRobotInteractiveCardRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateRobotInteractiveCardRequest
            {
                CardBizId = "cardXXXX01",
                CardData = "根据具体的cardTemplateId参考文档格式",
                UserIdPrivateDataMap = "{\"userId0001\":{\"xxxx\":\"xxxx\"}}",
                UnionIdPrivateDataMap = "{\"unionId0001\":{\"xxxx\":\"xxxx\"}}",
                UpdateOptions = updateOptions,
            };
            try
            {
                client.UpdateRobotInteractiveCardWithOptions(updateRobotInteractiveCardRequest, updateRobotInteractiveCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | invalid.user | 无效的用户ID | 无效的用户ID |
| 400 | invalid.openConversationId | 无效的openConversationId | 无效的openConversationId |
| 400 | invalid.robotCode | 无效的机器人标识 | 无效的机器人标识 |
| 400 | create.cardInstance.failed | 创建互动卡片实例失败 | 创建互动卡片实例失败 |
| 400 | send.cardMsg.failed | 发送互动卡片消息失败 | 发送互动卡片消息失败 |
| 400 | invalid.bizId | 互动卡片BIZID无效 | 互动卡片BIZID无效 |
