---
title: "套餐转售—分润模式"
source_url: "https://open.dingtalk.com/document/development/package-resale-1-distribution-mode"
namespace: "development"
slug: "package-resale-1-distribution-mode"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 套餐 > 套餐转售—分润模式"
doc_id: "NFFvkaecLg"
updated_at: "2025-09-23 19:21:35"
---

> Source: https://open.dingtalk.com/document/development/package-resale-1-distribution-mode
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 套餐 > 套餐转售—分润模式
> Updated: 2025-09-23 19:21:35

# 套餐转售—分润模式

调用本接口为使用电子合同的用户创建转售订单。

## **接口调用说明**

- 该模式是ISV售卖电子合同的收入和e签宝进行分润，需要提前和商务同学确定好分润比例并签订商务合同。
- 必须在企业实名后才能调该接口转售（转售对象必须为实名企业），否则转售会报错。
- ISV联系e签宝人员拿到e签宝的售卖套餐列表，需提前在ISV自己应用内售卖的套餐和对应的商品ID给到e签宝，否则无法下单（e签宝拿到ISV的商品ID后需要维护ISV商品ID和e签宝内部商品ID的对应关系，后续ISV传入客户购买的商品ID，e签宝对应找到内部商品去下单）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/orders/channel |
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
| orderId | String | 是 | 第三方的订单ID，需保证唯一性。 |
| itemCode | String | 是 | 商品ID。 |
| itemName | String | 是 | 商品名称。 |
| quantity | Float | 是 | 购买数量。 |
| payFee | Float | 否 | 支付金额，单位：分。      仅作记录不作为凭证。 |
| orderCreateTime | Float | 是 | 下单时间。 |

### 请求示例

HTTP

```
POST /v2.0/esign/orders/channel HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "orderId" : "23756345",
  "itemCode" : "lansheng_test_01",
  "itemName" : "套餐转授测试",
  "quantity" : 1.0,
  "payFee" : 666.0,
  "orderCreateTime" : 1.61674324E12
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
        ChannelOrdersHeaders channelOrdersHeaders = new ChannelOrdersHeaders();
        channelOrdersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ChannelOrdersRequest channelOrdersRequest = new ChannelOrdersRequest()
                .setOrderId("23756345")
                .setItemCode("lansheng_test_01")
                .setItemName("套餐转授测试")
                .setQuantity(1F)
                .setPayFee(666F)
                .setOrderCreateTime(1616743200000F);
        try {
            client.channelOrdersWithOptions(channelOrdersRequest, channelOrdersHeaders, new RuntimeOptions());
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
        channel_orders_headers = dingtalkesign__2__0_models.ChannelOrdersHeaders()
        channel_orders_headers.x_acs_dingtalk_access_token = '<your access token>'
        channel_orders_request = dingtalkesign__2__0_models.ChannelOrdersRequest(
            order_id='23756345',
            item_code='lansheng_test_01',
            item_name='套餐转授测试',
            quantity=1,
            pay_fee=666,
            order_create_time=1616743200000
        )
        try:
            client.channel_orders_with_options(channel_orders_request, channel_orders_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        channel_orders_headers = dingtalkesign__2__0_models.ChannelOrdersHeaders()
        channel_orders_headers.x_acs_dingtalk_access_token = '<your access token>'
        channel_orders_request = dingtalkesign__2__0_models.ChannelOrdersRequest(
            order_id='23756345',
            item_code='lansheng_test_01',
            item_name='套餐转授测试',
            quantity=1,
            pay_fee=666,
            order_create_time=1616743200000
        )
        try:
            await client.channel_orders_with_options_async(channel_orders_request, channel_orders_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ChannelOrdersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ChannelOrdersRequest;
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
        $channelOrdersHeaders = new ChannelOrdersHeaders([]);
        $channelOrdersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $channelOrdersRequest = new ChannelOrdersRequest([
            "orderId" => "23756345",
            "itemCode" => "lansheng_test_01",
            "itemName" => "套餐转授测试",
            "quantity" => 1,
            "payFee" => 666,
            "orderCreateTime" => 1616743200000
        ]);
        try {
            $client->channelOrdersWithOptions($channelOrdersRequest, $channelOrdersHeaders, new RuntimeOptions([]));
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

  channelOrdersHeaders := &dingtalkesign_2_0.ChannelOrdersHeaders{}
  channelOrdersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  channelOrdersRequest := &dingtalkesign_2_0.ChannelOrdersRequest{
    OrderId: tea.String("23756345"),
    ItemCode: tea.String("lansheng_test_01"),
    ItemName: tea.String("套餐转授测试"),
    Quantity: tea.Float32(1),
    PayFee: tea.Float32(666),
    OrderCreateTime: tea.Float32(1616743200000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChannelOrdersWithOptions(channelOrdersRequest, channelOrdersHeaders, &util.RuntimeOptions{})
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
    let channelOrdersHeaders = new $dingtalkesign_2_0.ChannelOrdersHeaders({ });
    channelOrdersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let channelOrdersRequest = new $dingtalkesign_2_0.ChannelOrdersRequest({
      orderId: "23756345",
      itemCode: "lansheng_test_01",
      itemName: "套餐转授测试",
      quantity: 1,
      payFee: 666,
      orderCreateTime: 1616743200000,
    });
    try {
      await client.channelOrdersWithOptions(channelOrdersRequest, channelOrdersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ChannelOrdersHeaders channelOrdersHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ChannelOrdersHeaders();
            channelOrdersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ChannelOrdersRequest channelOrdersRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ChannelOrdersRequest
            {
                OrderId = "23756345",
                ItemCode = "lansheng_test_01",
                ItemName = "套餐转授测试",
                Quantity = 1f,
                PayFee = 666f,
                OrderCreateTime = 1616743200000f,
            };
            try
            {
                client.ChannelOrdersWithOptions(channelOrdersRequest, channelOrdersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ChannelOrdersHeaders> channelOrdersHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::ChannelOrdersHeaders>();
  channelOrdersHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ChannelOrdersRequest> channelOrdersRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::ChannelOrdersRequest>(map<string, boost::any>({
    {"orderId", boost::any(string("23756345"))},
    {"itemCode", boost::any(string("lansheng_test_01"))},
    {"itemName", boost::any(string("套餐转授测试"))},
    {"quantity", boost::any(1)},
    {"payFee", boost::any(666)},
    {"orderCreateTime", boost::any(1616743200000)}
  }));
  try {
    client->channelOrdersWithOptions(channelOrdersRequest, channelOrdersHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "esignOrderId" : "1616743"
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
