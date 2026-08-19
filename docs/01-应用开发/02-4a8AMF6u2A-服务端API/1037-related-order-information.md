---
title: "关联单号查询相关订单信息列表"
source_url: "https://open.dingtalk.com/document/development/related-order-information"
namespace: "development"
slug: "related-order-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 关联单号查询相关订单信息列表"
doc_id: "4ssTACVSx8"
updated_at: "2026-01-29 14:31:13"
---

> Source: https://open.dingtalk.com/document/development/related-order-information
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 关联单号查询相关订单信息列表
> Updated: 2026-01-29 14:31:13

# 关联单号查询相关订单信息列表

通过本接口，可根据申请单中的关联单号获取对应的机票、火车票、酒店及用车等订单信息，实现多类型差旅订单的统一查询与管理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/unionOrders |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限点 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 第三方企业corpId。 |
| thirdPartApplyId | String | 否 | 第三方申请单ID。 |
| unionNo | String | 否 | 关联单号ID。 |

### 请求示例

HTTP

```
GET /v1.0/alitrip/unionOrders?corpId=ding213sxxx&thirdPartApplyId=32dsa4a&unionNo=2345543 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BWxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkalitrip_1_0.*;
import com.aliyun.dingtalkalitrip_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkalitrip_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkalitrip_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkalitrip_1_0.Client client = Sample.createClient();
        QueryUnionOrderHeaders queryUnionOrderHeaders = new QueryUnionOrderHeaders();
        queryUnionOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryUnionOrderRequest queryUnionOrderRequest = new QueryUnionOrderRequest()
                .setCorpId("ding213sxxx")
                .setThirdPartApplyId("32dsa4a")
                .setUnionNo("2345543");
        try {
            client.queryUnionOrderWithOptions(queryUnionOrderRequest, queryUnionOrderHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.alitrip_1_0.client import Client as dingtalkalitrip_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.alitrip_1_0 import models as dingtalkalitrip__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkalitrip_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkalitrip_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_union_order_headers = dingtalkalitrip__1__0_models.QueryUnionOrderHeaders()
        query_union_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_union_order_request = dingtalkalitrip__1__0_models.QueryUnionOrderRequest(
            corp_id='ding213sxxx',
            third_part_apply_id='32dsa4a',
            union_no='2345543'
        )
        try:
            client.query_union_order_with_options(query_union_order_request, query_union_order_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_union_order_headers = dingtalkalitrip__1__0_models.QueryUnionOrderHeaders()
        query_union_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_union_order_request = dingtalkalitrip__1__0_models.QueryUnionOrderRequest(
            corp_id='ding213sxxx',
            third_part_apply_id='32dsa4a',
            union_no='2345543'
        )
        try:
            await client.query_union_order_with_options_async(query_union_order_request, query_union_order_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\QueryUnionOrderHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\QueryUnionOrderRequest;
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
        $queryUnionOrderHeaders = new QueryUnionOrderHeaders([]);
        $queryUnionOrderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryUnionOrderRequest = new QueryUnionOrderRequest([
            "corpId" => "ding213sxxx",
            "thirdPartApplyId" => "32dsa4a",
            "unionNo" => "2345543"
        ]);
        try {
            $client->queryUnionOrderWithOptions($queryUnionOrderRequest, $queryUnionOrderHeaders, new RuntimeOptions([]));
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
  dingtalkalitrip_1_0  "github.com/alibabacloud-go/dingtalk/alitrip_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkalitrip_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkalitrip_1_0.Client{}
  _result, _err = dingtalkalitrip_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryUnionOrderHeaders := &dingtalkalitrip_1_0.QueryUnionOrderHeaders{}
  queryUnionOrderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryUnionOrderRequest := &dingtalkalitrip_1_0.QueryUnionOrderRequest{
    CorpId: tea.String("ding213sxxx"),
    ThirdPartApplyId: tea.String("32dsa4a"),
    UnionNo: tea.String("2345543"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryUnionOrderWithOptions(queryUnionOrderRequest, queryUnionOrderHeaders, &util.RuntimeOptions{})
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
import dingtalkalitrip_1_0, * as $dingtalkalitrip_1_0 from '@alicloud/dingtalk/alitrip_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkalitrip_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkalitrip_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryUnionOrderHeaders = new $dingtalkalitrip_1_0.QueryUnionOrderHeaders({ });
    queryUnionOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryUnionOrderRequest = new $dingtalkalitrip_1_0.QueryUnionOrderRequest({
      corpId: "ding213sxxx",
      thirdPartApplyId: "32dsa4a",
      unionNo: "2345543",
    });
    try {
      await client.queryUnionOrderWithOptions(queryUnionOrderRequest, queryUnionOrderHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryUnionOrderHeaders queryUnionOrderHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryUnionOrderHeaders();
            queryUnionOrderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryUnionOrderRequest queryUnionOrderRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryUnionOrderRequest
            {
                CorpId = "ding213sxxx",
                ThirdPartApplyId = "32dsa4a",
                UnionNo = "2345543",
            };
            try
            {
                client.QueryUnionOrderWithOptions(queryUnionOrderRequest, queryUnionOrderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkalitrip__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkalitrip_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkalitrip_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::Client> client = make_shared<Alibabacloud_Dingtalkalitrip_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::QueryUnionOrderHeaders> queryUnionOrderHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::QueryUnionOrderHeaders>();
  queryUnionOrderHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::QueryUnionOrderRequest> queryUnionOrderRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::QueryUnionOrderRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding213sxxx"))},
    {"thirdPartApplyId", boost::any(string("32dsa4a"))},
    {"unionNo", boost::any(string("2345543"))}
  }));
  try {
    client->queryUnionOrderWithOptions(queryUnionOrderRequest, queryUnionOrderHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| flightList | Array | 飞机订单信息列表。 |
| flightOrderId | Long | 飞机票订单ID。 |
| flightOrderStatus | Long | 订单状态，取值：   - **0**：待支付 - **1**：出票中 - **2**：已关闭 - **3**：有改签单 - **4**：有退票单 - **5**：出票成功 - **6**：退票申请中 - **7**：改签申请中 |
| corpId | String | 企业corpId。 |
| trainList | Array | 火车订单信息列表。 |
| trainOrderId | Long | 火车票订单号。 |
| trainOrderstatus | Long | 订单状态，取值：   - **0**：待支付 - **1**：出票中 - **2**：已关闭 - **3**：改签成功 - **4**：退票成功 - **5**：出票完成 - **6**：退票申请中 - **7**：改签申请中 - **8**：已出票,已发货 - **9**：出票失败 - **10**：改签失败 - **11**：退票失败 |
| hotelList | Array | 酒店订单信息列表。 |
| hotelOrderId | Long | 酒店订单号。 |
| hotelOrderStatus | Long | 订单状态，取值：   - **1**：等待确认 - **2**：等待付款 - **3**：预订成功 - **4**：申请退款 - **5**：退款成功 - **6**：已关闭 - **7**：结账成功 - **8**：支付成功 |
| vehicleList | Array | 用车订单信息列表。 |
| vehicleOrderId | Long | 用车订单号。 |
| vehicleOrderStatus | Long | 订单状态，取值：   - **0**：初始状态 - **1**：已超时 - **2**：派单成功 - **3**：派单失败 - **4**：已退款 - **5**：已支付 - **6**：已取消 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "flightList" : [ {
    "flightOrderId" : 1231,
    "flightOrderStatus" : 1
  } ],
  "corpId" : "tanant1231",
  "trainList" : [ {
    "trainOrderId" : 231231,
    "trainOrderstatus" : 1
  } ],
  "hotelList" : [ {
    "hotelOrderId" : 12312,
    "hotelOrderStatus" : 1
  } ],
  "vehicleList" : [ {
    "vehicleOrderId" : 1231,
    "vehicleOrderStatus" : 1
  } ]
}
```
