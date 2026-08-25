---
title: "新购授权订单"
source_url: "https://open.dingtalk.com/document/development/new-order-authorization"
namespace: "development"
slug: "new-order-authorization"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 权益 > 新购授权订单"
doc_id: "jHHVD7eNGW"
updated_at: "2025-09-08 19:03:52"
---

> Source: https://open.dingtalk.com/document/development/new-order-authorization
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 权益 > 新购授权订单
> Updated: 2025-09-08 19:03:52

# 新购授权订单

调用本接口通过应用授权服务发起多渠道新购。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，宜搭接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 宜搭接口相关文档，已于**2022年3月14日**迁移至**历史文档（不推荐）**目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | 暂不支持 |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/yida/appAuthorizations/order HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "produceCode" : "String",
  "instanceId" : "String",
  "instanceName" : "String",
  "accessKey" : "String",
  "callerUnionId" : "String",
  "chargeType" : "String",
  "endTimeGMT" : Long,
  "beginTimeGMT" : Long,
  "accountNumber" : "String",
  "commerceType" : "String",
  "commodityType" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)获取。 - 第三方企业应用调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| produceCode | String | 否 | 阿里云产品码。 |
| instanceId | String | 否 | 实例ID。 |
| instanceName | String | 否 | 实例名称。 |
| accessKey | String | 否 | 访问秘钥。 |
| callerUnionId | String | 否 | 调用者的unionId。 |
| chargeType | String | 否 | 付费方式，预付费：   - PREPAY：预付费 |
| endTimeGMT | Long | 否 | 结束时间。 |
| beginTimeGMT | Long | 否 | 开始时间。 |
| accountNumber | String | 否 | 账户号。 |
| commerceType | String | 否 | 商业类型。 |
| commodityType | String | 否 | 宜搭产品版本，取值：   - free：普惠版 - standard：标准版 - enterprise：企业版 - vip：尊享版 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Boolean | 调用是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/yida/appAuthorizations/order HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "produceCode" : "yun-1234",
  "instanceId" : "12",
  "instanceName" : "A发起的实例",
  "accessKey" : "hexaaaa",
  "callerUnionId" : "44234122",
  "chargeType" : "PREPAY",
  "endTimeGMT" : 1234567891234,
  "beginTimeGMT" : 1234567891234,
  "accountNumber" : "123",
  "commerceType" : "subscribe",
  "commodityType" : "Business"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkyida_1_0.*;
import com.aliyun.dingtalkyida_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkyida_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkyida_1_0.Client client = Sample.createClient();
        BuyAuthorizationOrderHeaders buyAuthorizationOrderHeaders = new BuyAuthorizationOrderHeaders();
        buyAuthorizationOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BuyAuthorizationOrderRequest buyAuthorizationOrderRequest = new BuyAuthorizationOrderRequest()
                .setProduceCode("yun-1234")
                .setInstanceId("12")
                .setInstanceName("A发起的实例")
                .setAccessKey("hexaaaa")
                .setCallerUnionId("44234122")
                .setChargeType("PREPAY")
                .setEndTimeGMT(1234567891234L)
                .setBeginTimeGMT(1234567891234L)
                .setAccountNumber("123")
                .setCommerceType("subscribe")
                .setCommodityType("Business");
        try {
            client.buyAuthorizationOrderWithOptions(buyAuthorizationOrderRequest, buyAuthorizationOrderHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        buy_authorization_order_headers = dingtalkyida__1__0_models.BuyAuthorizationOrderHeaders()
        buy_authorization_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        buy_authorization_order_request = dingtalkyida__1__0_models.BuyAuthorizationOrderRequest(
            produce_code='yun-1234',
            instance_id='12',
            instance_name='A发起的实例',
            access_key='hexaaaa',
            caller_union_id='44234122',
            charge_type='PREPAY',
            end_time_gmt=1234567891234,
            begin_time_gmt=1234567891234,
            account_number='123',
            commerce_type='subscribe',
            commodity_type='Business'
        )
        try:
            client.buy_authorization_order_with_options(buy_authorization_order_request, buy_authorization_order_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        buy_authorization_order_headers = dingtalkyida__1__0_models.BuyAuthorizationOrderHeaders()
        buy_authorization_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        buy_authorization_order_request = dingtalkyida__1__0_models.BuyAuthorizationOrderRequest(
            produce_code='yun-1234',
            instance_id='12',
            instance_name='A发起的实例',
            access_key='hexaaaa',
            caller_union_id='44234122',
            charge_type='PREPAY',
            end_time_gmt=1234567891234,
            begin_time_gmt=1234567891234,
            account_number='123',
            commerce_type='subscribe',
            commodity_type='Business'
        )
        try:
            await client.buy_authorization_order_with_options_async(buy_authorization_order_request, buy_authorization_order_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\BuyAuthorizationOrderHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\BuyAuthorizationOrderRequest;
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
        $buyAuthorizationOrderHeaders = new BuyAuthorizationOrderHeaders([]);
        $buyAuthorizationOrderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $buyAuthorizationOrderRequest = new BuyAuthorizationOrderRequest([
            "produceCode" => "yun-1234",
            "instanceId" => "12",
            "instanceName" => "A发起的实例",
            "accessKey" => "hexaaaa",
            "callerUnionId" => "44234122",
            "chargeType" => "PREPAY",
            "endTimeGMT" => 1234567891234,
            "beginTimeGMT" => 1234567891234,
            "accountNumber" => "123",
            "commerceType" => "subscribe",
            "commodityType" => "Business"
        ]);
        try {
            $client->buyAuthorizationOrderWithOptions($buyAuthorizationOrderRequest, $buyAuthorizationOrderHeaders, new RuntimeOptions([]));
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
  dingtalkyida_1_0  "github.com/alibabacloud-go/dingtalk/yida_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkyida_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_1_0.Client{}
  _result, _err = dingtalkyida_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  buyAuthorizationOrderHeaders := &dingtalkyida_1_0.BuyAuthorizationOrderHeaders{}
  buyAuthorizationOrderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  buyAuthorizationOrderRequest := &dingtalkyida_1_0.BuyAuthorizationOrderRequest{
    ProduceCode: tea.String("yun-1234"),
    InstanceId: tea.String("12"),
    InstanceName: tea.String("A发起的实例"),
    AccessKey: tea.String("hexaaaa"),
    CallerUnionId: tea.String("44234122"),
    ChargeType: tea.String("PREPAY"),
    EndTimeGMT: tea.Int64(1234567891234),
    BeginTimeGMT: tea.Int64(1234567891234),
    AccountNumber: tea.String("123"),
    CommerceType: tea.String("subscribe"),
    CommodityType: tea.String("Business"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BuyAuthorizationOrderWithOptions(buyAuthorizationOrderRequest, buyAuthorizationOrderHeaders, &util.RuntimeOptions{})
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
import dingtalkyida_1_0, * as $dingtalkyida_1_0 from '@alicloud/dingtalk/yida_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkyida_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkyida_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let buyAuthorizationOrderHeaders = new $dingtalkyida_1_0.BuyAuthorizationOrderHeaders({ });
    buyAuthorizationOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let buyAuthorizationOrderRequest = new $dingtalkyida_1_0.BuyAuthorizationOrderRequest({
      produceCode: "yun-1234",
      instanceId: "12",
      instanceName: "A发起的实例",
      accessKey: "hexaaaa",
      callerUnionId: "44234122",
      chargeType: "PREPAY",
      endTimeGMT: 1234567891234,
      beginTimeGMT: 1234567891234,
      accountNumber: "123",
      commerceType: "subscribe",
      commodityType: "Business",
    });
    try {
      await client.buyAuthorizationOrderWithOptions(buyAuthorizationOrderRequest, buyAuthorizationOrderHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.BuyAuthorizationOrderHeaders buyAuthorizationOrderHeaders = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.BuyAuthorizationOrderHeaders();
            buyAuthorizationOrderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.BuyAuthorizationOrderRequest buyAuthorizationOrderRequest = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.BuyAuthorizationOrderRequest
            {
                ProduceCode = "yun-1234",
                InstanceId = "12",
                InstanceName = "A发起的实例",
                AccessKey = "hexaaaa",
                CallerUnionId = "44234122",
                ChargeType = "PREPAY",
                EndTimeGMT = 1234567891234,
                BeginTimeGMT = 1234567891234,
                AccountNumber = "123",
                CommerceType = "subscribe",
                CommodityType = "Business",
            };
            try
            {
                client.BuyAuthorizationOrderWithOptions(buyAuthorizationOrderRequest, buyAuthorizationOrderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkyida__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkyida_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkyida_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::Client> client = make_shared<Alibabacloud_Dingtalkyida_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::BuyAuthorizationOrderHeaders> buyAuthorizationOrderHeaders = make_shared<Alibabacloud_Dingtalkyida_1_0::BuyAuthorizationOrderHeaders>();
  buyAuthorizationOrderHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::BuyAuthorizationOrderRequest> buyAuthorizationOrderRequest = make_shared<Alibabacloud_Dingtalkyida_1_0::BuyAuthorizationOrderRequest>(map<string, boost::any>({
    {"produceCode", boost::any(string("yun-1234"))},
    {"instanceId", boost::any(string("12"))},
    {"instanceName", boost::any(string("A发起的实例"))},
    {"accessKey", boost::any(string("hexaaaa"))},
    {"callerUnionId", boost::any(string("44234122"))},
    {"chargeType", boost::any(string("PREPAY"))},
    {"endTimeGMT", boost::any(1234567891234)},
    {"beginTimeGMT", boost::any(1234567891234)},
    {"accountNumber", boost::any(string("123"))},
    {"commerceType", boost::any(string("subscribe"))},
    {"commodityType", boost::any(string("Business"))}
  }));
  try {
    client->buyAuthorizationOrderWithOptions(buyAuthorizationOrderRequest, buyAuthorizationOrderHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "result" : false
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | unclassifiedError | 异常:%s | 通用异常信息 |
