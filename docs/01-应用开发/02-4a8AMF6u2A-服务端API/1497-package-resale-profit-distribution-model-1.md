---
title: "套餐转售（分润模式）"
source_url: "https://open.dingtalk.com/document/development/package-resale-profit-distribution-model-1"
namespace: "development"
slug: "package-resale-profit-distribution-model-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 套餐 > 套餐转售（分润模式）"
doc_id: "IEM394BPCe"
updated_at: "2026-06-23 18:10:33"
---

> Source: https://open.dingtalk.com/document/development/package-resale-profit-distribution-model-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > e签宝 1.0 > 套餐 > 套餐转售（分润模式）
> Updated: 2026-06-23 18:10:33

# 套餐转售（分润模式）

调用本接口在e签宝下转售订单给最终真正使用电子合同的用户。调用接口时需要传入本次用户订购的套餐，e签宝会对应给用户下这个套餐。

## **接口调用说明**

当前接口已完成升级迭代且不再支持新应用申请，存量应用调用不受影响，建议未接入的开发者使用[套餐转售—分润模式](1074-package-resale-1-distribution-mode.md)接口，已接入的开发者结合实际尽快完成迁移。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/esign/orders/channel |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 不支持新增申请 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| itemCode | String | 是 | 商品id。 |
| itemName | String | 是 | 商品名称。 |
| orderCreateTime | Long | 否 | 下单时间，Unix时间戳。 |
| orderId | String | 是 | ISV方订单Id，用于幂等，请保证唯一性。 |
| payFee | Long | 是 | 支付金额，以分为单位。  **[!NOTE]**    仅作记录，不作为凭证。 |
| quantity | Long | 是 | 购买数量。 |

### **请求示例**

HTTP

```
POST /v1.0/esign/orders/channel HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE34466XXXX
Content-Type:application/json

{
  "itemCode" : "1213",
  "itemName" : "商品",
  "orderCreateTime" : 1555307607000,
  "orderId" : "sas1",
  "payFee" : 100000,
  "quantity" : 1
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_1_0.*;
import com.aliyun.dingtalkesign_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_1_0.Client client = Sample.createClient();
        ChannelOrderHeaders channelOrderHeaders = new ChannelOrderHeaders();
        channelOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ChannelOrderRequest channelOrderRequest = new ChannelOrderRequest()
                .setItemCode("1213")
                .setItemName("商品")
                .setOrderCreateTime(1555307607000L)
                .setOrderId("sas1")
                .setPayFee(100000L)
                .setQuantity(1L);
        try {
            client.channelOrderWithOptions(channelOrderRequest, channelOrderHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_1_0.client import Client as dingtalkesign_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        channel_order_headers = dingtalkesign__1__0_models.ChannelOrderHeaders()
        channel_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        channel_order_request = dingtalkesign__1__0_models.ChannelOrderRequest(
            item_code='1213',
            item_name='商品',
            order_create_time=1555307607000,
            order_id='sas1',
            pay_fee=100000,
            quantity=1
        )
        try:
            client.channel_order_with_options(channel_order_request, channel_order_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        channel_order_headers = dingtalkesign__1__0_models.ChannelOrderHeaders()
        channel_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        channel_order_request = dingtalkesign__1__0_models.ChannelOrderRequest(
            item_code='1213',
            item_name='商品',
            order_create_time=1555307607000,
            order_id='sas1',
            pay_fee=100000,
            quantity=1
        )
        try:
            await client.channel_order_with_options_async(channel_order_request, channel_order_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\ChannelOrderHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\ChannelOrderRequest;
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
        $channelOrderHeaders = new ChannelOrderHeaders([]);
        $channelOrderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $channelOrderRequest = new ChannelOrderRequest([
            "itemCode" => "1213",
            "itemName" => "商品",
            "orderCreateTime" => 1555307607000,
            "orderId" => "sas1",
            "payFee" => 100000,
            "quantity" => 1
        ]);
        try {
            $client->channelOrderWithOptions($channelOrderRequest, $channelOrderHeaders, new RuntimeOptions([]));
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
  dingtalkesign_1_0  ""github.com/alibabacloud-go/dingtalk/esign_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_1_0.Client{}
  _result, _err = dingtalkesign_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  channelOrderHeaders := &dingtalkesign_1_0.ChannelOrderHeaders{}
  channelOrderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  channelOrderRequest := &dingtalkesign_1_0.ChannelOrderRequest{
    ItemCode: tea.String("1213"),
    ItemName: tea.String("商品"),
    OrderCreateTime: tea.Int64(1555307607000),
    OrderId: tea.String("sas1"),
    PayFee: tea.Int64(100000),
    Quantity: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChannelOrderWithOptions(channelOrderRequest, channelOrderHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_1_0, * as $dingtalkesign_1_0 from '"@alicloud/dingtalk/esign_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let channelOrderHeaders = new $dingtalkesign_1_0.ChannelOrderHeaders({ });
    channelOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let channelOrderRequest = new $dingtalkesign_1_0.ChannelOrderRequest({
      itemCode: "1213",
      itemName: "商品",
      orderCreateTime: 1555307607000,
      orderId: "sas1",
      payFee: 100000,
      quantity: 1,
    });
    try {
      await client.channelOrderWithOptions(channelOrderRequest, channelOrderHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ChannelOrderHeaders channelOrderHeaders = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ChannelOrderHeaders();
            channelOrderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ChannelOrderRequest channelOrderRequest = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ChannelOrderRequest
            {
                ItemCode = "1213",
                ItemName = "商品",
                OrderCreateTime = 1555307607000,
                OrderId = "sas1",
                PayFee = 100000,
                Quantity = 1,
            };
            try
            {
                client.ChannelOrderWithOptions(channelOrderRequest, channelOrderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::ChannelOrderHeaders> channelOrderHeaders = make_shared<Alibabacloud_Dingtalkesign_1_0::ChannelOrderHeaders>();
  channelOrderHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::ChannelOrderRequest> channelOrderRequest = make_shared<Alibabacloud_Dingtalkesign_1_0::ChannelOrderRequest>(map<string, boost::any>({
    {"itemCode", boost::any(string("1213"))},
    {"itemName", boost::any(string("商品"))},
    {"orderCreateTime", boost::any(1555307607000)},
    {"orderId", boost::any(string("sas1"))},
    {"payFee", boost::any(100000)},
    {"quantity", boost::any(1)}
  }));
  try {
    client->channelOrderWithOptions(channelOrderRequest, channelOrderHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | Integer | 返回码。 |
| message | String | 返回码描述。 |
| data | Object | 返回结果。 |
| esignOrderId | String | e签宝订单Id。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : 0,
  "message" : "成功",
  "data" : {
    "esignOrderId" : "ab312c2c-a3ec-4876-xxxx-0fb112c22348"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.invalidAguemnts | invalid arguments | 参数错误 |
