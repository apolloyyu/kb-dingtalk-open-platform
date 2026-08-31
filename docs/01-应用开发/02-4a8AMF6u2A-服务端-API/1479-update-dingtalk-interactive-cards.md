---
title: "更新钉钉互动卡片"
source_url: "https://open.dingtalk.com/document/development/update-dingtalk-interactive-cards"
namespace: "development"
slug: "update-dingtalk-interactive-cards"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 更新钉钉互动卡片"
doc_id: "k74gkdAjXD"
updated_at: "2026-08-25 09:37:07"
---

> Source: https://open.dingtalk.com/document/development/update-dingtalk-interactive-cards
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 机器人 > 更新钉钉互动卡片
> Updated: 2026-08-25 09:37:07

# 更新钉钉互动卡片

调用本接口更新钉钉互动卡片。

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
PUT /v1.0/im/interactiveCards HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "String",
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
  "userIdType" : Integer,
  "cardOptions" : {
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
| outTrackId | String | 否 | 卡片的唯一标识编码。  **[!NOTE]**  是由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到**outTrackId**的场景，帮助开发者对TrackId进行记录。 |
| cardData | Object | 否 | 卡片数据。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，普通文本类型。  **[!NOTE]**   - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| cardMediaIdParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，多媒体类型。 |
| privateData | Map<String, Object> | 否 | 指定用户可见的按钮列表。   - **key**：用户userId - **value**：用户数据 |
|  | Object | 否 | 指定用户可见的按钮列表。   - **key**：用户userId - **value**：用户数据 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，普通文本类型。  **[!NOTE]**     - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| cardMediaIdParamMap | Map<String, String> | 否 | 卡片模板内容替换参数，多媒体类型。 |
| userIdType | Integer | 否 | 用户ID类型：   - **1**：userid模式（默认值） - **2**：unionId模式   对应receiverUserIdList、privateData字段关于用户id的值填写方式。 |
| cardOptions | Object | 否 | 发送可交互卡片的功能选项。 |
| updateCardDataByKey | Boolean | 否 | 按key更新**cardData**数据，不填默认覆盖更新。 |
| updatePrivateDataByKey | Boolean | 否 | 按key更新**privateData**用户数据，不填默认覆盖更新。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | String | 更新结果。 |

## 示例

**请求示例**

HTTP

```
PUT /v1.0/im/interactiveCards HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxxx
Content-Type:application/json

{
  "outTrackId" : "trackId",
  "cardData" : {
    "cardParamMap" : {
      "key" : "测试"
    },
    "cardMediaIdParamMap" : {
      "key" : "测试"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "测试"
      },
      "cardMediaIdParamMap" : {
        "key" : "测试"
      }
    }
  },
  "userIdType" : 1,
  "cardOptions" : {
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
        UpdateInteractiveCardHeaders updateInteractiveCardHeaders = new UpdateInteractiveCardHeaders();
        updateInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardOptions cardOptions = new UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardOptions()
                .setUpdateCardDataByKey(false)
                .setUpdatePrivateDataByKey(false);
        java.util.Map<String, String> privateDataValueKeyCardMediaIdParamMap = TeaConverter.buildMap(
            new TeaPair("key", "测试")
        );
        java.util.Map<String, String> privateDataValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "测试")
        );
        PrivateDataValue privateDataValueKey = new PrivateDataValue()
                .setCardParamMap(privateDataValueKeyCardParamMap)
                .setCardMediaIdParamMap(privateDataValueKeyCardMediaIdParamMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        java.util.Map<String, String> cardDataCardMediaIdParamMap = TeaConverter.buildMap(
            new TeaPair("key", "测试")
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "测试")
        );
        UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardData cardData = new UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardData()
                .setCardParamMap(cardDataCardParamMap)
                .setCardMediaIdParamMap(cardDataCardMediaIdParamMap);
        UpdateInteractiveCardRequest updateInteractiveCardRequest = new UpdateInteractiveCardRequest()
                .setOutTrackId("trackId")
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setUserIdType(1)
                .setCardOptions(cardOptions);
        try {
            client.updateInteractiveCardWithOptions(updateInteractiveCardRequest, updateInteractiveCardHeaders, new RuntimeOptions());
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
        update_interactive_card_headers = dingtalkim__1__0_models.UpdateInteractiveCardHeaders()
        update_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_options = dingtalkim__1__0_models.UpdateInteractiveCardRequestCardOptions(
            update_card_data_by_key=False,
            update_private_data_by_key=False
        )
        private_data_value_key_card_media_id_param_map = {
            'key': '测试'
        }
        private_data_value_key_card_param_map = {
            'key': '测试'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map,
            card_media_id_param_map=private_data_value_key_card_media_id_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_media_id_param_map = {
            'key': '测试'
        }
        card_data_card_param_map = {
            'key': '测试'
        }
        card_data = dingtalkim__1__0_models.UpdateInteractiveCardRequestCardData(
            card_param_map=card_data_card_param_map,
            card_media_id_param_map=card_data_card_media_id_param_map
        )
        update_interactive_card_request = dingtalkim__1__0_models.UpdateInteractiveCardRequest(
            out_track_id='trackId',
            card_data=card_data,
            private_data=private_data,
            user_id_type=1,
            card_options=card_options
        )
        try:
            client.update_interactive_card_with_options(update_interactive_card_request, update_interactive_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_interactive_card_headers = dingtalkim__1__0_models.UpdateInteractiveCardHeaders()
        update_interactive_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_options = dingtalkim__1__0_models.UpdateInteractiveCardRequestCardOptions(
            update_card_data_by_key=False,
            update_private_data_by_key=False
        )
        private_data_value_key_card_media_id_param_map = {
            'key': '测试'
        }
        private_data_value_key_card_param_map = {
            'key': '测试'
        }
        private_data_value_key = dingtalkim__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map,
            card_media_id_param_map=private_data_value_key_card_media_id_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_media_id_param_map = {
            'key': '测试'
        }
        card_data_card_param_map = {
            'key': '测试'
        }
        card_data = dingtalkim__1__0_models.UpdateInteractiveCardRequestCardData(
            card_param_map=card_data_card_param_map,
            card_media_id_param_map=card_data_card_media_id_param_map
        )
        update_interactive_card_request = dingtalkim__1__0_models.UpdateInteractiveCardRequest(
            out_track_id='trackId',
            card_data=card_data,
            private_data=private_data,
            user_id_type=1,
            card_options=card_options
        )
        try:
            await client.update_interactive_card_with_options_async(update_interactive_card_request, update_interactive_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateInteractiveCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateInteractiveCardRequest\cardOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\PrivateDataValue;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateInteractiveCardRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateInteractiveCardRequest;
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
        $updateInteractiveCardHeaders = new UpdateInteractiveCardHeaders([]);
        $updateInteractiveCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cardOptions = new cardOptions([
            "updateCardDataByKey" => false,
            "updatePrivateDataByKey" => false
        ]);
        $privateDataValueKeyCardMediaIdParamMap = [
            "key" => "测试"
        ];
        $privateDataValueKeyCardParamMap = [
            "key" => "测试"
        ];
        $privateDataValueKey = new PrivateDataValue([
            "cardParamMap" => $privateDataValueKeyCardParamMap,
            "cardMediaIdParamMap" => $privateDataValueKeyCardMediaIdParamMap
        ]);
        $privateData = [
            "privateDataValueKey" => $privateDataValueKey
        ];
        $cardDataCardMediaIdParamMap = [
            "key" => "测试"
        ];
        $cardDataCardParamMap = [
            "key" => "测试"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap,
            "cardMediaIdParamMap" => $cardDataCardMediaIdParamMap
        ]);
        $updateInteractiveCardRequest = new UpdateInteractiveCardRequest([
            "outTrackId" => "trackId",
            "cardData" => $cardData,
            "privateData" => $privateData,
            "userIdType" => 1,
            "cardOptions" => $cardOptions
        ]);
        try {
            $client->updateInteractiveCardWithOptions($updateInteractiveCardRequest, $updateInteractiveCardHeaders, new RuntimeOptions([]));
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

  updateInteractiveCardHeaders := &dingtalkim_1_0.UpdateInteractiveCardHeaders{}
  updateInteractiveCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cardOptions := &dingtalkim_1_0.UpdateInteractiveCardRequestCardOptions{
    UpdateCardDataByKey: tea.Bool(false),
    UpdatePrivateDataByKey: tea.Bool(false),
  }
  privateDataValueKeyCardMediaIdParamMap := map[string]*string{
    "key": tea.String("测试"),
  }
  privateDataValueKeyCardParamMap := map[string]*string{
    "key": tea.String("测试"),
  }
  privateDataValueKey := &dingtalkim_1_0.PrivateDataValue{
    CardParamMap: privateDataValueKeyCardParamMap,
    CardMediaIdParamMap: privateDataValueKeyCardMediaIdParamMap,
  }
  privateData := map[string]*dingtalkim_1_0.PrivateDataValue{
    "privateDataValueKey": privateDataValueKey,
  }
  cardDataCardMediaIdParamMap := map[string]*string{
    "key": tea.String("测试"),
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("测试"),
  }
  cardData := &dingtalkim_1_0.UpdateInteractiveCardRequestCardData{
    CardParamMap: cardDataCardParamMap,
    CardMediaIdParamMap: cardDataCardMediaIdParamMap,
  }
  updateInteractiveCardRequest := &dingtalkim_1_0.UpdateInteractiveCardRequest{
    OutTrackId: tea.String("trackId"),
    CardData: cardData,
    PrivateData: privateData,
    UserIdType: tea.Int32(1),
    CardOptions: cardOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateInteractiveCardWithOptions(updateInteractiveCardRequest, updateInteractiveCardHeaders, &util.RuntimeOptions{})
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
    let updateInteractiveCardHeaders = new $dingtalkim_1_0.UpdateInteractiveCardHeaders({ });
    updateInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let cardOptions = new $dingtalkim_1_0.UpdateInteractiveCardRequestCardOptions({
      updateCardDataByKey: false,
      updatePrivateDataByKey: false,
    });
    let privateDataValueKeyCardMediaIdParamMap = {
      key: "测试",
    };
    let privateDataValueKeyCardParamMap = {
      key: "测试",
    };
    let privateDataValueKey = new $dingtalkim_1_0.PrivateDataValue({
      cardParamMap: privateDataValueKeyCardParamMap,
      cardMediaIdParamMap: privateDataValueKeyCardMediaIdParamMap,
    });
    let privateData = {
      privateDataValueKey: privateDataValueKey,
    };
    let cardDataCardMediaIdParamMap = {
      key: "测试",
    };
    let cardDataCardParamMap = {
      key: "测试",
    };
    let cardData = new $dingtalkim_1_0.UpdateInteractiveCardRequestCardData({
      cardParamMap: cardDataCardParamMap,
      cardMediaIdParamMap: cardDataCardMediaIdParamMap,
    });
    let updateInteractiveCardRequest = new $dingtalkim_1_0.UpdateInteractiveCardRequest({
      outTrackId: "trackId",
      cardData: cardData,
      privateData: privateData,
      userIdType: 1,
      cardOptions: cardOptions,
    });
    try {
      await client.updateInteractiveCardWithOptions(updateInteractiveCardRequest, updateInteractiveCardHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardHeaders updateInteractiveCardHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardHeaders();
            updateInteractiveCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardOptions cardOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardOptions
            {
                UpdateCardDataByKey = false,
                UpdatePrivateDataByKey = false,
            };
            Dictionary<string, string> privateDataValueKeyCardMediaIdParamMap = new Dictionary<string, string>
            {
                {"key", "测试"},
            };
            Dictionary<string, string> privateDataValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "测试"},
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
                {"key", "测试"},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "测试"},
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardRequest.UpdateInteractiveCardRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
                CardMediaIdParamMap = cardDataCardMediaIdParamMap,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardRequest updateInteractiveCardRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateInteractiveCardRequest
            {
                OutTrackId = "trackId",
                CardData = cardData,
                PrivateData = privateData,
                UserIdType = 1,
                CardOptions = cardOptions,
            };
            try
            {
                client.UpdateInteractiveCardWithOptions(updateInteractiveCardRequest, updateInteractiveCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardHeaders> updateInteractiveCardHeaders = make_shared<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardHeaders>();
  updateInteractiveCardHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardRequestCardOptions> cardOptions = make_shared<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardRequestCardOptions>(map<string, boost::any>({
    {"updateCardDataByKey", boost::any(false)},
    {"updatePrivateDataByKey", boost::any(false)}
  }));
  shared_ptr<map<string, string>> privateDataValueKeyCardMediaIdParamMap = make_shared<map<string, string>>(map<string, string>({
    {"key", "测试"}
  })
);
  shared_ptr<map<string, string>> privateDataValueKeyCardParamMap = make_shared<map<string, string>>(map<string, string>({
    {"key", "测试"}
  })
);
  shared_ptr<Alibabacloud_Dingtalkim_1_0::PrivateDataValue> privateDataValueKey = make_shared<Alibabacloud_Dingtalkim_1_0::PrivateDataValue>(map<string, boost::any>({
    {"cardParamMap", !privateDataValueKeyCardParamMap ? boost::any() : boost::any(*privateDataValueKeyCardParamMap)},
    {"cardMediaIdParamMap", !privateDataValueKeyCardMediaIdParamMap ? boost::any() : boost::any(*privateDataValueKeyCardMediaIdParamMap)}
  }));
  shared_ptr<map<string, Alibabacloud_Dingtalkim_1_0::PrivateDataValue>> privateData = make_shared<map<string, Alibabacloud_Dingtalkim_1_0::PrivateDataValue>>(map<string, Alibabacloud_Dingtalkim_1_0::PrivateDataValue>({
    {"privateDataValueKey", !privateDataValueKey ? Alibabacloud_Dingtalkim_1_0::PrivateDataValue() : *privateDataValueKey}
  })
);
  shared_ptr<map<string, string>> cardDataCardMediaIdParamMap = make_shared<map<string, string>>(map<string, string>({
    {"key", "测试"}
  })
);
  shared_ptr<map<string, string>> cardDataCardParamMap = make_shared<map<string, string>>(map<string, string>({
    {"key", "测试"}
  })
);
  shared_ptr<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardRequestCardData> cardData = make_shared<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardRequestCardData>(map<string, boost::any>({
    {"cardParamMap", !cardDataCardParamMap ? boost::any() : boost::any(*cardDataCardParamMap)},
    {"cardMediaIdParamMap", !cardDataCardMediaIdParamMap ? boost::any() : boost::any(*cardDataCardMediaIdParamMap)}
  }));
  shared_ptr<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardRequest> updateInteractiveCardRequest = make_shared<Alibabacloud_Dingtalkim_1_0::UpdateInteractiveCardRequest>(map<string, boost::any>({
    {"outTrackId", boost::any(string("trackId"))},
    {"cardData", !cardData ? boost::any() : boost::any(*cardData)},
    {"privateData", !privateData ? boost::any() : boost::any(*privateData)},
    {"userIdType", boost::any(1)},
    {"cardOptions", !cardOptions ? boost::any() : boost::any(*cardOptions)}
  }));
  try {
    client->updateInteractiveCardWithOptions(updateInteractiveCardRequest, updateInteractiveCardHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "success" : "true"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | param.invalid | 请求参数无效 | 请求参数无效 |
| 400 | cardInstance.notExist | 卡片实例不存在 | 卡片实例不存在 |
| 400 | userInfo.convertError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | card.outTraceIdError | 卡片业务标识信息格式非法 | 卡片业务标识信息格式非法 |
| 400 | card.outTraceIdEmpty | 业务标识outTrackId为空 | 业务标识outTrackId为空 |
| 400 | sendCardMessageFailed | 发送卡片失败 | 发送卡片失败 |
| 400 | uidDecryptError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | duplicateKey | 卡片模板占位符有重复Key | 卡片模板占位符有重复Key |
| 400 | getPictureFailed | 获取图片url失败 | 获取图片url失败 |
| 400 | contentCheckError | 卡片内容校验失败 | 卡片内容校验失败 |
| 400 | outTrackIdLengthLimited | 超过卡片业务标识信息长度 | 超过卡片业务标识信息长度 |
| 500 | systemBusy | 系统繁忙 | 系统异常错误 |
