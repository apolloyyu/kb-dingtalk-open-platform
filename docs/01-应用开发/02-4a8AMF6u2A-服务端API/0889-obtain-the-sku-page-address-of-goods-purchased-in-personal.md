---
title: "获取个人应用内购商品SKU页面地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-sku-page-address-of-goods-purchased-in-personal"
namespace: "development"
slug: "obtain-the-sku-page-address-of-goods-purchased-in-personal"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 获取个人应用内购商品SKU页面地址"
doc_id: "A54sYJQ764"
updated_at: "2026-07-08 14:13:52"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-sku-page-address-of-goods-purchased-in-personal
> Path: 应用开发 / 服务端API / 应用市场 > 获取个人应用内购商品SKU页面地址
> Updated: 2026-07-08 14:13:52

# 获取个人应用内购商品SKU页面地址

调用本接口获取内购商品SKU页面地址。调用本接口可获取个人应用内购商品的SKU选择页面URL，用于前端跳转或分享。该接口适用于动态配置价格的内购场景，支持非固定规格商品的价格传入。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/appMarket/internals/skuPages/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方个人应用 |
| 权限要求 | permission-Market.PersonalAppInternal.Read-个人应用在应用市场开通购买的数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| goodsCode | String | 是 | 内购商品码。 |
| itemCode | String | 否 | 内购规格码。 |
| callbackPage | String | 否 | 回调页面（需进行UrlEncode处理），为小程序页面路径地址。 |
| extendParam | String | 否 | 调用方扩展参数：   - 如果是非固定规格内购商品，该参数必填，用于指定商品价格。 参数格式为{"outDefinedPrice":199}，表示该商品价格为1.99元。     `extend_param`参数必须UrlEncode处理。若为固定规格内购商品，该参数可选，无需填写。 |

### 请求示例

HTTP

```
POST /v1.0/appMarket/internals/skuPages/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "goodsCode" : "FW_GOODS_1111",
  "itemCode" : "FW_GOODS_1111_1",
  "callbackPage" : "http%3A//dingtalk.com%3Fa%3Db",
  "extendParam" : "%7B%22outDefinedPrice%22%3A19999%7D"
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
    public static com.aliyun.dingtalkapp_market_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkapp_market_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkapp_market_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkapp_market_1_0.models.GetInAppSkuUrlHeaders getInAppSkuUrlHeaders = new com.aliyun.dingtalkapp_market_1_0.models.GetInAppSkuUrlHeaders();
        getInAppSkuUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkapp_market_1_0.models.GetInAppSkuUrlRequest getInAppSkuUrlRequest = new com.aliyun.dingtalkapp_market_1_0.models.GetInAppSkuUrlRequest()
                .setGoodsCode("FW_GOODS_1111")
                .setItemCode("FW_GOODS_1111_1")
                .setCallbackPage("http%3A//dingtalk.com%3Fa%3Db")
                .setExtendParam("%7B%22outDefinedPrice%22%3A19999%7D");
        try {
            client.getInAppSkuUrlWithOptions(getInAppSkuUrlRequest, getInAppSkuUrlHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys

from typing import List

from alibabacloud_dingtalk.appMarket_1_0.client import Client as dingtalkappMarket_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.appMarket_1_0 import models as dingtalkapp_market__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkappMarket_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkappMarket_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_in_app_sku_url_headers = dingtalkapp_market__1__0_models.GetInAppSkuUrlHeaders()
        get_in_app_sku_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_in_app_sku_url_request = dingtalkapp_market__1__0_models.GetInAppSkuUrlRequest(
            goods_code='FW_GOODS_1111',
            item_code='FW_GOODS_1111_1',
            callback_page='http%3A//dingtalk.com%3Fa%3Db',
            extend_param='%7B%22outDefinedPrice%22%3A19999%7D'
        )
        try:
            client.get_in_app_sku_url_with_options(get_in_app_sku_url_request, get_in_app_sku_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_in_app_sku_url_headers = dingtalkapp_market__1__0_models.GetInAppSkuUrlHeaders()
        get_in_app_sku_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_in_app_sku_url_request = dingtalkapp_market__1__0_models.GetInAppSkuUrlRequest(
            goods_code='FW_GOODS_1111',
            item_code='FW_GOODS_1111_1',
            callback_page='http%3A//dingtalk.com%3Fa%3Db',
            extend_param='%7B%22outDefinedPrice%22%3A19999%7D'
        )
        try:
            await client.get_in_app_sku_url_with_options_async(get_in_app_sku_url_request, get_in_app_sku_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vapp_market_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vapp_market_1_0\Models\GetInAppSkuUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vapp_market_1_0\Models\GetInAppSkuUrlRequest;
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
        $getInAppSkuUrlHeaders = new GetInAppSkuUrlHeaders([]);
        $getInAppSkuUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getInAppSkuUrlRequest = new GetInAppSkuUrlRequest([
            "goodsCode" => "FW_GOODS_1111",
            "itemCode" => "FW_GOODS_1111_1",
            "callbackPage" => "http%3A//dingtalk.com%3Fa%3Db",
            "extendParam" => "%7B%22outDefinedPrice%22%3A19999%7D"
        ]);
        try {
            $client->getInAppSkuUrlWithOptions($getInAppSkuUrlRequest, $getInAppSkuUrlHeaders, new RuntimeOptions([]));
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
  dingtalkappmarket_1_0  "github.com/alibabacloud-go/dingtalk/appMarket_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkappmarket_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkappmarket_1_0.Client{}
  _result, _err = dingtalkappmarket_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getInAppSkuUrlHeaders := &dingtalkappmarket_1_0.GetInAppSkuUrlHeaders{}
  getInAppSkuUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getInAppSkuUrlRequest := &dingtalkappmarket_1_0.GetInAppSkuUrlRequest{
    GoodsCode: tea.String("FW_GOODS_1111"),
    ItemCode: tea.String("FW_GOODS_1111_1"),
    CallbackPage: tea.String("http%3A//dingtalk.com%3Fa%3Db"),
    ExtendParam: tea.String("%7B%22outDefinedPrice%22%3A19999%7D"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetInAppSkuUrlWithOptions(getInAppSkuUrlRequest, getInAppSkuUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkappMarket_1_0, * as $dingtalkappMarket_1_0 from '@alicloud/dingtalk/appMarket_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkappMarket_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkappMarket_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getInAppSkuUrlHeaders = new $dingtalkappMarket_1_0.GetInAppSkuUrlHeaders({ });
    getInAppSkuUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getInAppSkuUrlRequest = new $dingtalkappMarket_1_0.GetInAppSkuUrlRequest({
      goodsCode: "FW_GOODS_1111",
      itemCode: "FW_GOODS_1111_1",
      callbackPage: "http%3A//dingtalk.com%3Fa%3Db",
      extendParam: "%7B%22outDefinedPrice%22%3A19999%7D",
    });
    try {
      await client.getInAppSkuUrlWithOptions(getInAppSkuUrlRequest, getInAppSkuUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkapp_market_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkapp_market_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkapp_market_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkapp_market_1_0.Models.GetInAppSkuUrlHeaders getInAppSkuUrlHeaders = new AlibabaCloud.SDK.Dingtalkapp_market_1_0.Models.GetInAppSkuUrlHeaders();
            getInAppSkuUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkapp_market_1_0.Models.GetInAppSkuUrlRequest getInAppSkuUrlRequest = new AlibabaCloud.SDK.Dingtalkapp_market_1_0.Models.GetInAppSkuUrlRequest
            {
                GoodsCode = "FW_GOODS_1111",
                ItemCode = "FW_GOODS_1111_1",
                CallbackPage = "http%3A//dingtalk.com%3Fa%3Db",
                ExtendParam = "%7B%22outDefinedPrice%22%3A19999%7D",
            };
            try
            {
                client.GetInAppSkuUrlWithOptions(getInAppSkuUrlRequest, getInAppSkuUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| url | String | 内购商品SKU页面地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "url" : "https://dingtalk.com 6d1bxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | goodsNotExist | 内购商品不存在 | 内购商品不存在 |
| 400 | goodsItemNotExist | 商品规格不存在 | 商品规格不存在 |
| 400 | notFixedItemExtendParamError | 非固定规格扩展参数异常 | 非固定规格扩展参数异常 |
| 400 | notFixedItemNoPrice | 内购商品非固定规格未传入价格 | 内购商品非固定规格未传入价格 |
| 400 | notFixedItemInvalidPrice | 内购商品非固定规格传入价格异常 | 内购商品非固定规格传入价格异常 |
