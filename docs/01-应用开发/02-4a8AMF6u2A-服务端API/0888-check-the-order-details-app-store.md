---
title: "查询应用市场订单详情"
source_url: "https://open.dingtalk.com/document/development/check-the-order-details-app-store"
namespace: "development"
slug: "check-the-order-details-app-store"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 查询应用市场订单详情"
doc_id: "WTmKSr868s"
updated_at: "2025-12-08 15:15:24"
---

> Source: https://open.dingtalk.com/document/development/check-the-order-details-app-store
> Path: 应用开发 / 服务端API / 应用市场 > 查询应用市场订单详情
> Updated: 2025-12-08 15:15:24

# 查询应用市场订单详情

调用本接口查询指定订单的详情信息。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/appMarket/orders/{orderId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Market.Order.Read-开通应用在应用市场订单信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| orderId | Long | 否 | 订单ID，可以从推送信息中获取，请参考[应用市场事件biz\_type=17](../04-LFcRvVD08N-事件订阅/0186-application-market-order.md#section-sample-code)。 |

### 请求示例

HTTP

```
GET /v1.0/appMarket/orders/2091000 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:AC9340BCDMBI13SZBZ
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkapp_market_1_0.*;
import com.aliyun.dingtalkapp_market_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkapp_market_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkapp_market_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkapp_market_1_0.Client client = Sample.createClient();
        QueryMarketOrderHeaders queryMarketOrderHeaders = new QueryMarketOrderHeaders();
        queryMarketOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.queryMarketOrderWithOptions("2091000", queryMarketOrderHeaders, new RuntimeOptions());
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
        query_market_order_headers = dingtalkapp_market__1__0_models.QueryMarketOrderHeaders()
        query_market_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.query_market_order_with_options('2091000', query_market_order_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_market_order_headers = dingtalkapp_market__1__0_models.QueryMarketOrderHeaders()
        query_market_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.query_market_order_with_options_async('2091000', query_market_order_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vapp_market_1_0\Models\QueryMarketOrderHeaders;
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
        $queryMarketOrderHeaders = new QueryMarketOrderHeaders([]);
        $queryMarketOrderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->queryMarketOrderWithOptions("2091000", $queryMarketOrderHeaders, new RuntimeOptions([]));
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
  dingtalkappmarket_1_0  ""github.com/alibabacloud-go/dingtalk/appMarket_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  queryMarketOrderHeaders := &dingtalkappmarket_1_0.QueryMarketOrderHeaders{}
  queryMarketOrderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryMarketOrderWithOptions(tea.String("2091000"), queryMarketOrderHeaders, &util.RuntimeOptions{})
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
import dingtalkappMarket_1_0, * as $dingtalkappMarket_1_0 from '"@alicloud/dingtalk/appMarket_1_0';
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
    let queryMarketOrderHeaders = new $dingtalkappMarket_1_0.QueryMarketOrderHeaders({ });
    queryMarketOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.queryMarketOrderWithOptions("2091000", queryMarketOrderHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkapp_market_1_0.Models.QueryMarketOrderHeaders queryMarketOrderHeaders = new AlibabaCloud.SDK.Dingtalkapp_market_1_0.Models.QueryMarketOrderHeaders();
            queryMarketOrderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.QueryMarketOrderWithOptions("2091000", queryMarketOrderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkapp_market__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

using namespace std;

Alibabacloud_Dingtalkapp_market_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkapp_market_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkapp_market_1_0::Client> client = make_shared<Alibabacloud_Dingtalkapp_market_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkapp_market_1_0::QueryMarketOrderHeaders> queryMarketOrderHeaders = make_shared<Alibabacloud_Dingtalkapp_market_1_0::QueryMarketOrderHeaders>();
  queryMarketOrderHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->queryMarketOrderWithOptions(make_shared<string>("2091000"), queryMarketOrderHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| bizOrderId | Long | 订单ID。 |
| corpId | String | 订单归属的组织corpId。 |
| itemCode | String | 规格编码。 |
| itemName | String | 规格名称。 |
| goodsCode | String | 商品Code。 |
| goodsName | String | 商品名称。 |
| totalActualPayFee | Long | 订单实付金额，单位：分。 |
| status | Long | 订单状态，取值：   - **0**：订单关闭 - **3**：订单支付 - **4**：订单创建 |
| quantity | Long | 购买数量。 |
| paidTimestamp | Long | 支付时间戳，单位：毫秒。 |
| createTimestamp | Long | 创建时间戳，单位：毫秒。 |
| startTimestamp | Long | 开始生效时间，单位：毫秒。 |
| endTimestamp | Long | 生效结束时间，单位：毫秒。 |
| inAppOrder | Boolean | 是否内购订单。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "bizOrderId" : 20923100,
  "corpId" : "ding23219001",
  "itemCode" : "FW_GOODS_31001",
  "itemName" : "测试规格001",
  "goodsCode" : "FW_GOODS_12319001",
  "goodsName" : "测试商品001",
  "totalActualPayFee" : 100,
  "status" : 1,
  "quantity" : 1,
  "paidTimestamp" : 1625019684000,
  "createTimestamp" : 1625019684000,
  "startTimestamp" : 1625019684000,
  "endTimestamp" : 1625019684000,
  "inAppOrder" : false
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | order.not.exist | 订单不存在 | 订单不存在 |
| 400 | illegal.order.principle | 订单归属错误 | 非当前ISV所属订单无查询权限 |
| 400 | goods.not.app | 非应用或内购商品 | 非应用或内购商品 |
