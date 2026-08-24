---
title: "更新卡片"
source_url: "https://open.dingtalk.com/document/development/interactive-card-update-interface"
namespace: "development"
slug: "interactive-card-update-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 互动卡片 > 更新卡片"
doc_id: "IUu2CZbgZs"
updated_at: "2026-06-04 10:49:19"
---

> Source: https://open.dingtalk.com/document/development/interactive-card-update-interface
> Path: 应用开发 / 服务端API / 即时通信 > 互动卡片 > 更新卡片
> Updated: 2026-06-04 10:49:19

# 更新卡片

调用本接口实现更新卡片。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/instances |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Instance.Write-互动卡片实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 外部卡片实例Id。  **[!NOTE]**    由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。 |
| cardData | Object | 否 | 卡片数据，示例：   ``` "cardData": {     "cardParamMap": {         "title": "设计中心周会",         "date": "3月24日 周五 18:00-17:00",         "location": "湖畔 大梅沙",         "image1": "mediaIdXXXXX1",         "image2": "mediaIdXXXXX2"     } } ``` |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - key：参数名（最长不超过100B） - value: 参数值（最长不超过1KB）   **[!NOTE]**     - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[API 卡片数据的填写说明](0789-instructions-for-filling-in-api-card-data.md)。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| privateData | Map<String, Object> | 否 | 用户的私有数据：   - key：userId - value：用户私有数据   示例：   ``` "privateData": {     "manager1234": {         "cardParamMap": {             "attendee": "小明、小王",              "image1": "mediaIdXXXXX1"         }     } } ``` |
|  | Object | 否 | 私有用户userId信息。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - key：参数名（最长不超过100B） - value: 参数值（最长不超过1KB）   **[!NOTE]**     - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[API 卡片数据的填写说明](0789-instructions-for-filling-in-api-card-data.md)。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| cardUpdateOptions | Object | 否 | 卡片更新选项。 |
| updateCardDataByKey | Boolean | 否 | 更新 cardData 数据的方式：   - **true**：按 key 更新 cardData 数据 - **false**：覆盖更新 cardData 数据   **[!NOTE]**    不填默认覆盖更新。 |
| updatePrivateDataByKey | Boolean | 否 | 更新 privateData 数据的方式：   - **true**：按 key 更新 privateData 数据 - **false**：覆盖更新 privateData 数据   **[!NOTE]**    不填默认覆盖更新。 |
| userIdType | Integer | 否 | 用户id类型：   - **1**（默认）：userid模式 - **2**：unionId模式   **[!NOTE]**    `userIdType` 字段的填写请参考：[userIdType 字段的填写说明](0790-faq-card.md#8cad7f90a8mzg)。 |

### 请求示例

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:example-token
Content-Type:application/json

{
  "outTrackId" : "example-out-track-id",
  "cardData" : {
    "cardParamMap" : {
      "key" : "example-value"
    }
  },
  "privateData" : {
    "key" : {
      "cardParamMap" : {
        "key" : "example-value"
      }
    }
  },
  "cardUpdateOptions" : {
    "updateCardDataByKey" : true,
    "updatePrivateDataByKey" : false
  },
  "userIdType" : 1
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
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders updateCardHeaders = new com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions cardUpdateOptions = new com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true)
                .setUpdatePrivateDataByKey(false);
        java.util.Map<String, String> privateDataValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "example-value")
        );
        com.aliyun.dingtalkcard_1_0.models.PrivateDataValue privateDataValueKey = new com.aliyun.dingtalkcard_1_0.models.PrivateDataValue()
                .setCardParamMap(privateDataValueKeyCardParamMap);
        java.util.Map<String, com.aliyun.dingtalkcard_1_0.models.PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "example-value")
        );
        com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData cardData = new com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData()
                .setCardParamMap(cardDataCardParamMap);
        com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest updateCardRequest = new com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest()
                .setOutTrackId("example-out-track-id")
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions)
                .setUserIdType(1);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_card_headers = dingtalkcard__1__0_models.UpdateCardHeaders()
        update_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_update_options = dingtalkcard__1__0_models.UpdateCardRequestCardUpdateOptions(
            update_card_data_by_key=True,
            update_private_data_by_key=False
        )
        private_data_value_key_card_param_map = {
            'key': 'example-value'
        }
        private_data_value_key = dingtalkcard__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_param_map = {
            'key': 'example-value'
        }
        card_data = dingtalkcard__1__0_models.UpdateCardRequestCardData(
            card_param_map=card_data_card_param_map
        )
        update_card_request = dingtalkcard__1__0_models.UpdateCardRequest(
            out_track_id='example-out-track-id',
            card_data=card_data,
            private_data=private_data,
            card_update_options=card_update_options,
            user_id_type=1
        )
        try:
            client.update_card_with_options(update_card_request, update_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_card_headers = dingtalkcard__1__0_models.UpdateCardHeaders()
        update_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_update_options = dingtalkcard__1__0_models.UpdateCardRequestCardUpdateOptions(
            update_card_data_by_key=True,
            update_private_data_by_key=False
        )
        private_data_value_key_card_param_map = {
            'key': 'example-value'
        }
        private_data_value_key = dingtalkcard__1__0_models.PrivateDataValue(
            card_param_map=private_data_value_key_card_param_map
        )
        private_data = {
            'privateDataValueKey': private_data_value_key
        }
        card_data_card_param_map = {
            'key': 'example-value'
        }
        card_data = dingtalkcard__1__0_models.UpdateCardRequestCardData(
            card_param_map=card_data_card_param_map
        )
        update_card_request = dingtalkcard__1__0_models.UpdateCardRequest(
            out_track_id='example-out-track-id',
            card_data=card_data,
            private_data=private_data,
            card_update_options=card_update_options,
            user_id_type=1
        )
        try:
            await client.update_card_with_options_async(update_card_request, update_card_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateCardRequest\cardUpdateOptions;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\PrivateDataValue;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateCardRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateCardRequest;
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
        $updateCardHeaders = new UpdateCardHeaders([]);
        $updateCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cardUpdateOptions = new cardUpdateOptions([
            "updateCardDataByKey" => true,
            "updatePrivateDataByKey" => false
        ]);
        $privateDataValueKeyCardParamMap = [
            "key" => "example-value"
        ];
        $privateDataValueKey = new PrivateDataValue([
            "cardParamMap" => $privateDataValueKeyCardParamMap
        ]);
        $privateData = [
            "privateDataValueKey" => $privateDataValueKey
        ];
        $cardDataCardParamMap = [
            "key" => "example-value"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap
        ]);
        $updateCardRequest = new UpdateCardRequest([
            "outTrackId" => "example-out-track-id",
            "cardData" => $cardData,
            "privateData" => $privateData,
            "cardUpdateOptions" => $cardUpdateOptions,
            "userIdType" => 1
        ]);
        try {
            $client->updateCardWithOptions($updateCardRequest, $updateCardHeaders, new RuntimeOptions([]));
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
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateCardHeaders := &dingtalkcard_1_0.UpdateCardHeaders{}
  updateCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cardUpdateOptions := &dingtalkcard_1_0.UpdateCardRequestCardUpdateOptions{
    UpdateCardDataByKey: tea.Bool(true),
    UpdatePrivateDataByKey: tea.Bool(false),
  }
  privateDataValueKeyCardParamMap := map[string]*string{
    "key": tea.String("example-value"),
  }
  privateDataValueKey := &dingtalkcard_1_0.PrivateDataValue{
    CardParamMap: privateDataValueKeyCardParamMap,
  }
  privateData := map[string]*dingtalkcard_1_0.PrivateDataValue{
    "privateDataValueKey": privateDataValueKey,
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("example-value"),
  }
  cardData := &dingtalkcard_1_0.UpdateCardRequestCardData{
    CardParamMap: cardDataCardParamMap,
  }
  updateCardRequest := &dingtalkcard_1_0.UpdateCardRequest{
    OutTrackId: tea.String("example-out-track-id"),
    CardData: cardData,
    PrivateData: privateData,
    CardUpdateOptions: cardUpdateOptions,
    UserIdType: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateCardWithOptions(updateCardRequest, updateCardHeaders, &util.RuntimeOptions{})
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
import dingtalkcard_1_0, * as $dingtalkcard_1_0 from '@alicloud/dingtalk/card_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcard_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcard_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let updateCardHeaders = new $dingtalkcard_1_0.UpdateCardHeaders({ });
    updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let cardUpdateOptions = new $dingtalkcard_1_0.UpdateCardRequestCardUpdateOptions({
      updateCardDataByKey: true,
      updatePrivateDataByKey: false,
    });
    let privateDataValueKeyCardParamMap = {
      key: "example-value",
    };
    let privateDataValueKey = new $dingtalkcard_1_0.PrivateDataValue({
      cardParamMap: privateDataValueKeyCardParamMap,
    });
    let privateData = {
      privateDataValueKey: privateDataValueKey,
    };
    let cardDataCardParamMap = {
      key: "example-value",
    };
    let cardData = new $dingtalkcard_1_0.UpdateCardRequestCardData({
      cardParamMap: cardDataCardParamMap,
    });
    let updateCardRequest = new $dingtalkcard_1_0.UpdateCardRequest({
      outTrackId: "example-out-track-id",
      cardData: cardData,
      privateData: privateData,
      cardUpdateOptions: cardUpdateOptions,
      userIdType: 1,
    });
    try {
      await client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardHeaders updateCardHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardHeaders();
            updateCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions cardUpdateOptions = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions
            {
                UpdateCardDataByKey = true,
                UpdatePrivateDataByKey = false,
            };
            Dictionary<string, string> privateDataValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "example-value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue privateDataValueKey = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue
            {
                CardParamMap = privateDataValueKeyCardParamMap,
            };
            Dictionary<string, AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue> privateData = new Dictionary<string, AlibabaCloud.SDK.Dingtalkcard_1_0.Models.PrivateDataValue>
            {
                {"privateDataValueKey", privateDataValueKey},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "example-value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardRequest.UpdateCardRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardRequest.UpdateCardRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardRequest updateCardRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateCardRequest
            {
                OutTrackId = "example-out-track-id",
                CardData = cardData,
                PrivateData = privateData,
                CardUpdateOptions = cardUpdateOptions,
                UserIdType = 1,
            };
            try
            {
                client.UpdateCardWithOptions(updateCardRequest, updateCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 请求是否成功。 |
| result | Boolean | 更新是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.cardDataAndPrivateDataBothEmpty | param.cardDataAndPrivateDataBothEmpty | cardData 和 privateData 同时为空 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识 outTrackId 为空 |
| 400 | param.userIdNotExist | param.userIdNotExist | 用户 userId 不存在 |
| 400 | param.contentUnsafe | param.contentUnsafe | 卡片数据不能通过安全审查 |
| 400 | param.cardNotExist | param.cardNotExist | 卡片不存在 |
| 500 | system.busy | system.busy | 系统繁忙 |
