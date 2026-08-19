---
title: "套餐转售—底价结算模式"
source_url: "https://open.dingtalk.com/document/development/package-resale-2-reserve-price-settlement-mode"
namespace: "development"
slug: "package-resale-2-reserve-price-settlement-mode"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 套餐 > 套餐转售—底价结算模式"
doc_id: "3ASxjAMGtq"
updated_at: "2025-09-23 19:21:35"
---

> Source: https://open.dingtalk.com/document/development/package-resale-2-reserve-price-settlement-mode
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 套餐 > 套餐转售—底价结算模式
> Updated: 2025-09-23 19:21:35

# 套餐转售—底价结算模式

企业可以通过此接口直接转售e签宝订单给最终真正使用电子合同的用户。

## **接口调用说明**

- **调用此接口前必需提前和商务同学对接**，确定每份电子合同的底价，并签订商务合同后，才可以使用该模式给用户下单。
- 调用接口时直接传入本次给该企业下单多少份电子合同，e签宝将会充值合同份数到用户账号上。
- 企业可通过该接口直接给真正使用电子签章的企业下订单。
- 必须在企业实名后才能调本接口进行转售（转售对象必须为实名企业），否则转售会报错。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/orders/resale |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-e签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceGroup | String | 否 | 预留参数，此版本无需此参数。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| orderId | String | 是 | isv方的订单ID，用于幂等，请保证唯一性。 |
| quantity | Float | 是 | 购买数量，电子合同份数。 |
| orderCreateTime | Float | 是 | 下单时间。 |
| serviceStartTime | Float | 否 | 合同生效起始时间。 |
| serviceStopTime | Float | 是 | 合同失效截止日期。默认有效时间一年。 |

### 请求示例

HTTP

```
POST /v2.0/esign/orders/resale HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "orderId" : "492112",
  "quantity" : 1.0,
  "orderCreateTime" : 1.5916145E12,
  "serviceStartTime" : 1.5916145E12,
  "serviceStopTime" : 1.59181609E12
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_2_0.*;
import com.aliyun.dingtalkesign_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_2_0.Client client = Sample.createClient();
        ResaleOrderHeaders resaleOrderHeaders = new ResaleOrderHeaders();
        resaleOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ResaleOrderRequest resaleOrderRequest = new ResaleOrderRequest()
                .setOrderId("492112")
                .setQuantity(1F)
                .setOrderCreateTime(1591614500000F)
                .setServiceStartTime(1591614500000F)
                .setServiceStopTime(1591816100000F);
        try {
            client.resaleOrderWithOptions(resaleOrderRequest, resaleOrderHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_2_0.client import Client as dingtalkesign_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        resale_order_headers = dingtalkesign__2__0_models.ResaleOrderHeaders()
        resale_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        resale_order_request = dingtalkesign__2__0_models.ResaleOrderRequest(
            order_id='492112',
            quantity=1,
            order_create_time=1591614500000,
            service_start_time=1591614500000,
            service_stop_time=1591816100000
        )
        try:
            client.resale_order_with_options(resale_order_request, resale_order_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        resale_order_headers = dingtalkesign__2__0_models.ResaleOrderHeaders()
        resale_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        resale_order_request = dingtalkesign__2__0_models.ResaleOrderRequest(
            order_id='492112',
            quantity=1,
            order_create_time=1591614500000,
            service_start_time=1591614500000,
            service_stop_time=1591816100000
        )
        try:
            await client.resale_order_with_options_async(resale_order_request, resale_order_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ResaleOrderHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ResaleOrderRequest;
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
        $resaleOrderHeaders = new ResaleOrderHeaders([]);
        $resaleOrderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $resaleOrderRequest = new ResaleOrderRequest([
            "orderId" => "492112",
            "quantity" => 1,
            "orderCreateTime" => 1591614500000,
            "serviceStartTime" => 1591614500000,
            "serviceStopTime" => 1591816100000
        ]);
        try {
            $client->resaleOrderWithOptions($resaleOrderRequest, $resaleOrderHeaders, new RuntimeOptions([]));
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
  dingtalkesign_2_0  ""github.com/alibabacloud-go/dingtalk/esign_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_2_0.Client{}
  _result, _err = dingtalkesign_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  resaleOrderHeaders := &dingtalkesign_2_0.ResaleOrderHeaders{}
  resaleOrderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  resaleOrderRequest := &dingtalkesign_2_0.ResaleOrderRequest{
    OrderId: tea.String("492112"),
    Quantity: tea.Float32(1),
    OrderCreateTime: tea.Float32(1591614500000),
    ServiceStartTime: tea.Float32(1591614500000),
    ServiceStopTime: tea.Float32(1591816100000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ResaleOrderWithOptions(resaleOrderRequest, resaleOrderHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_2_0, * as $dingtalkesign_2_0 from '"@alicloud/dingtalk/esign_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let resaleOrderHeaders = new $dingtalkesign_2_0.ResaleOrderHeaders({ });
    resaleOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let resaleOrderRequest = new $dingtalkesign_2_0.ResaleOrderRequest({
      orderId: "492112",
      quantity: 1,
      orderCreateTime: 1591614500000,
      serviceStartTime: 1591614500000,
      serviceStopTime: 1591816100000,
    });
    try {
      await client.resaleOrderWithOptions(resaleOrderRequest, resaleOrderHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ResaleOrderHeaders resaleOrderHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ResaleOrderHeaders();
            resaleOrderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ResaleOrderRequest resaleOrderRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ResaleOrderRequest
            {
                OrderId = "492112",
                Quantity = 1f,
                OrderCreateTime = 1591614500000f,
                ServiceStartTime = 1591614500000f,
                ServiceStopTime = 1591816100000f,
            };
            try
            {
                client.ResaleOrderWithOptions(resaleOrderRequest, resaleOrderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__2__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_2_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_2_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_2_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ResaleOrderHeaders> resaleOrderHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::ResaleOrderHeaders>();
  resaleOrderHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ResaleOrderRequest> resaleOrderRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::ResaleOrderRequest>(map<string, boost::any>({
    {"orderId", boost::any(string("492112"))},
    {"quantity", boost::any(1)},
    {"orderCreateTime", boost::any(1591614500000)},
    {"serviceStartTime", boost::any(1591614500000)},
    {"serviceStopTime", boost::any(1591816100000)}
  }));
  try {
    client->resaleOrderWithOptions(resaleOrderRequest, resaleOrderHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| esignOrderId | String | e签宝订单ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "esignOrderId" : "PRO-sdfj32xxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | getOpenIsvInfoError | 获取对接服务商信息异常 | 获取对接服务商信息异常 |
| 400 | requestTooMuch | 请求太频繁了，稍后再试 | 请求太频繁了，稍后再试 |
| 400 | getResaleOrderInfoError | 获取转售订单信息异常 | 获取转售订单信息异常 |
| 400 | doRepeatOrderError | 请勿重复下单 | 请勿重复下单 |
| 400 | doResaleOrderError | 下转售订单失败 | 下转售订单失败 |
