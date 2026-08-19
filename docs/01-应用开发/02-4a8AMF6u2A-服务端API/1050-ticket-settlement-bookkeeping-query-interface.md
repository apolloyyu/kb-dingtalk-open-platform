---
title: "查询机票结算记账数据"
source_url: "https://open.dingtalk.com/document/development/ticket-settlement-bookkeeping-query-interface"
namespace: "development"
slug: "ticket-settlement-bookkeeping-query-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 账单管理 > 查询机票结算记账数据"
doc_id: "zfJAIWh7oY"
updated_at: "2026-01-29 14:31:10"
---

> Source: https://open.dingtalk.com/document/development/ticket-settlement-bookkeeping-query-interface
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 账单管理 > 查询机票结算记账数据
> Updated: 2026-01-29 14:31:10

# 查询机票结算记账数据

通过此接口查询阿里商旅中的机票结算记账数据，支持按企业、时间范围、分页等条件筛选，适用于财务对账、自动化记账系统对接等场景。

## 接口调用说明

本接口主要用于以下业务场景：

- **企业财务月度对账**：财务系统定期拉取上月机票消费明细，用于生成财务报表和成本分析。
- **自动化记账系统对接**：与企业ERP或财务软件集成，自动同步商旅消费数据，减少人工录入。
- **费用审计与合规检查**：结合审批单号（applyId）和订单信息，验证差旅行为是否符合公司政策。
- **成本中心与项目核算**：根据部门、项目代码、成本中心等字段进行多维度费用归集。

![](https://img.alicdn.com/imgextra/i1/O1CN01n4X0Xi1l85B2rfyCq_!!6000000004773-2-tps-1524-678.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/billSettlements/flights |
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
| corpId | String | 否 | 第三方企业的CorpId。 |
| category | Long | 否 | 类目，取值：   - **0**：火车 - **1**：机票 - **2**：酒店 - **4**：用车 - **6**：商旅火车票 |
| pageSize | Long | 否 | 分页参数，每页数据量。默认值100，最大值500。 |
| periodStart | String | 否 | 记账更新开始日期。 |
| pageNumber | Long | 否 | 分页参数，页码，从1开始。 |
| periodEnd | String | 否 | 记账更新结束日期。 |

### 请求示例

HTTP

```
GET /v1.0/alitrip/billSettlements/flights?corpId=corpx&category=1&pageSize=100&periodStart=2021-10-01&pageNumber=1&periodEnd=2021-10-01 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:x-acs-dingtalk-access-token.
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
        BillSettementFlightHeaders billSettementFlightHeaders = new BillSettementFlightHeaders();
        billSettementFlightHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BillSettementFlightRequest billSettementFlightRequest = new BillSettementFlightRequest()
                .setCorpId("corpx")
                .setCategory(1L)
                .setPageSize(100L)
                .setPeriodStart("2021-10-01")
                .setPageNumber(1L)
                .setPeriodEnd("2021-10-01");
        try {
            client.billSettementFlightWithOptions(billSettementFlightRequest, billSettementFlightHeaders, new RuntimeOptions());
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
        bill_settement_flight_headers = dingtalkalitrip__1__0_models.BillSettementFlightHeaders()
        bill_settement_flight_headers.x_acs_dingtalk_access_token = '<your access token>'
        bill_settement_flight_request = dingtalkalitrip__1__0_models.BillSettementFlightRequest(
            corp_id='corpx',
            category=1,
            page_size=100,
            period_start='2021-10-01',
            page_number=1,
            period_end='2021-10-01'
        )
        try:
            client.bill_settement_flight_with_options(bill_settement_flight_request, bill_settement_flight_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        bill_settement_flight_headers = dingtalkalitrip__1__0_models.BillSettementFlightHeaders()
        bill_settement_flight_headers.x_acs_dingtalk_access_token = '<your access token>'
        bill_settement_flight_request = dingtalkalitrip__1__0_models.BillSettementFlightRequest(
            corp_id='corpx',
            category=1,
            page_size=100,
            period_start='2021-10-01',
            page_number=1,
            period_end='2021-10-01'
        )
        try:
            await client.bill_settement_flight_with_options_async(bill_settement_flight_request, bill_settement_flight_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\BillSettementFlightHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\BillSettementFlightRequest;
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
        $billSettementFlightHeaders = new BillSettementFlightHeaders([]);
        $billSettementFlightHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $billSettementFlightRequest = new BillSettementFlightRequest([
            "corpId" => "corpx",
            "category" => 1,
            "pageSize" => 100,
            "periodStart" => "2021-10-01",
            "pageNumber" => 1,
            "periodEnd" => "2021-10-01"
        ]);
        try {
            $client->billSettementFlightWithOptions($billSettementFlightRequest, $billSettementFlightHeaders, new RuntimeOptions([]));
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

  billSettementFlightHeaders := &dingtalkalitrip_1_0.BillSettementFlightHeaders{}
  billSettementFlightHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  billSettementFlightRequest := &dingtalkalitrip_1_0.BillSettementFlightRequest{
    CorpId: tea.String("corpx"),
    Category: tea.Int64(1),
    PageSize: tea.Int64(100),
    PeriodStart: tea.String("2021-10-01"),
    PageNumber: tea.Int64(1),
    PeriodEnd: tea.String("2021-10-01"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BillSettementFlightWithOptions(billSettementFlightRequest, billSettementFlightHeaders, &util.RuntimeOptions{})
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
    let billSettementFlightHeaders = new $dingtalkalitrip_1_0.BillSettementFlightHeaders({ });
    billSettementFlightHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let billSettementFlightRequest = new $dingtalkalitrip_1_0.BillSettementFlightRequest({
      corpId: "corpx",
      category: 1,
      pageSize: 100,
      periodStart: "2021-10-01",
      pageNumber: 1,
      periodEnd: "2021-10-01",
    });
    try {
      await client.billSettementFlightWithOptions(billSettementFlightRequest, billSettementFlightHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementFlightHeaders billSettementFlightHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementFlightHeaders();
            billSettementFlightHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementFlightRequest billSettementFlightRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementFlightRequest
            {
                CorpId = "corpx",
                Category = 1,
                PageSize = 100,
                PeriodStart = "2021-10-01",
                PageNumber = 1,
                PeriodEnd = "2021-10-01",
            };
            try
            {
                client.BillSettementFlightWithOptions(billSettementFlightRequest, billSettementFlightHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::BillSettementFlightHeaders> billSettementFlightHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::BillSettementFlightHeaders>();
  billSettementFlightHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::BillSettementFlightRequest> billSettementFlightRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::BillSettementFlightRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("corpx"))},
    {"category", boost::any(1)},
    {"pageSize", boost::any(100)},
    {"periodStart", boost::any(string("2021-10-01"))},
    {"pageNumber", boost::any(1)},
    {"periodEnd", boost::any(string("2021-10-01"))}
  }));
  try {
    client->billSettementFlightWithOptions(billSettementFlightRequest, billSettementFlightHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| resultMsg | String | 结果msg。 |
| module | Object | module。 |
| category | Long | 类目：机酒火车：   - **0**：火车 - **1**：机票 - **2**：酒店 - **4**：用车 - **6**：商旅火车票 |
| corpId | String | 企业id。 |
| dataList | Array | 数据集合。 |
| advanceDay | Long | 提前预定天数。 |
| airlineCorpCode | String | 航司二字码。 |
| airlineCorpName | String | 航司名称。 |
| alipayTradeNo | String | 交易流水号。 |
| applyId | String | 审批单号。 |
| arrAirportCode | String | 到达机场三字码。 |
| arrCity | String | 到达城市。 |
| arrDate | String | 到达日期。 |
| arrStation | String | 到达机场。 |
| arrTime | String | 到达时间。 |
| bookTime | String | 预定时间。 |
| bookerId | String | 预订人use id。 |
| bookerName | String | 预订人名称。 |
| btripCouponFee | double | 商旅优惠金额。 |
| buildFee | double | 基建费。 |
| cabin | String | 舱位。 |
| cabinClass | String | 舱位代码。 |
| capitalDirection | String | 资金方向：   - **1**：支出 - **2**：收入 |
| cascadeDepartment | String | 级联部门。 |
| changeFee | double | 改签费用。 |
| corpPayOrderFee | double | 订单金额。 |
| costCenter | String | 成本中心名称。 |
| costCenterNumber | String | 成本中心编号。 |
| coupon | double | 优惠券。 |
| depAirportCode | String | 起飞机场三字码。 |
| department | String | 末级部门。 |
| departmentId | String | 部门id。 |
| deptCity | String | 起飞城市。 |
| deptDate | String | 起飞日期。 |
| deptStation | String | 起飞机场。 |
| deptTime | String | 起飞时间。 |
| discount | String | 折扣率。 |
| feeType | String | 费用类型：   - **10101**：机票预订 - **10202**：机票改签手续费 - **10203**：机票改签差价 - **10301**：机票退款 - **10302**：机票改签退款 - **10303**：机票补退 - **10401**：机票保险-航意险购买 - **10501**：机票保险-航意险退保 - **11001**：机票的预订服务费 - **11002**：机票改签服务费 - **20101**：酒店预订 - **20103**：酒店退款 - **20111**：酒店预订服务费 - **20112**：酒店托管服务费 - **40101**：用车预订 - **40103**：用车退款 - **40107**：用车取消订单收取费用 - **40111**：用车预订服务费 - **6001**：火车票预订 - **6003**：火车票改签差价 - **6004**：火车票改签手续费 - **6005**：火车票退票 - **6007**：火车票预订服务费 - **6008**：火车票改签服务费 - **6009**：火车票预订退款 - **6010**：火车票改签退款 - **1201**：赔付 - **2001**：冲正 |
| flightNo | String | 航班号。 |
| index | String | 序号。 |
| insuranceFee | double | 保险费。 |
| invoiceTitle | String | 发票抬头。 |
| itineraryNum | String | 行程单打印序号。 |
| itineraryPrice | double | 行程单金额。 |
| mostDifferenceDeptTime | String | 低价提醒（起飞时间）。 |
| mostDifferenceDiscount | String | 低价提醒（折扣）。 |
| mostDifferenceFlightNo | String | 低价提醒(航班号)。 |
| mostDifferencePrice | double | 低价提醒(与最低价差额)。 |
| mostDifferenceReason | String | 不选低价原因。 |
| mostPrice | double | 低价航班价格。 |
| negotiationCouponFee | double | 协议价优惠金额。 |
| oilFee | double | 燃油费。 |
| orderId | String | 订单号。 |
| overApplyId | String | 超标审批单号。 |
| primaryId | Long | 主键id，遇到相同id，已最新为准（数据会更新）。 |
| projectCode | String | 项目代码。 |
| projectName | String | 项目名称。 |
| refundFee | double | 退款手续费。 |
| refundUpgradeCost | double | 改签退票手续费。 |
| repeatRefund | String | 是否重复退。 |
| sealPrice | double | 销售价。 |
| serviceFee | double | 服务费，仅在feeType 11001、11002中展示。 |
| settlementFee | double | 结算金额。 |
| settlementTime | String | 结算时间。 |
| settlementType | String | 结算类型：   - **1**：个人现付 - **2**：企业现付 - **4**：企业月结 - **8**：企业预存 |
| status | Long | 入账状态：   - **-1**：个人支付不入账 - **0**：待入账 - **1**：入账成功 |
| ticketId | String | 行程单号。 |
| travelerId | String | 出行人use id。 |
| travelerName | String | 出行人名称。 |
| upgradeCost | double | 改签差价。 |
| bookerJobNo | String | 预订人工号。 |
| travelerJobNo | String | 出行人工号。 |
| voucherType | Long | 发票类型：   - **11**：增值税普通发票 - **12**：增值税专用发票 - **1**：增值税发票 - **2**：机票行程单 - **5**：火车票凭证 - **6**：定额发票 - **99**：不提供票据 - **7**：线下制票 |
| billRecordTime | String | 入账时间。 |
| settlementGrantFee | double | 预存赠送金额消费。 |
| remark | String | 备注。 |
| periodEnd | String | 记账更新开始日期。 |
| periodStart | String | 记账更新结束日期。 |
| totalNum | Long | 总数据量。 |
| success | Boolean | 是否成功。 |
| resultCode | Long | 结果code。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "resultMsg" : "成功",
  "module" : {
    "category" : 1,
    "corpId" : "ding0e577cd03421a",
    "dataList" : [ {
      "advanceDay" : 1,
      "airlineCorpCode" : "MU",
      "airlineCorpName" : "中国东方航空",
      "alipayTradeNo" : "24234343325",
      "applyId" : "34534545",
      "arrAirportCode" : "CAN",
      "arrCity" : "广州",
      "arrDate" : "2021-10-13",
      "arrStation" : "白云国际机场",
      "arrTime" : "13:46:05",
      "bookTime" : "2021-10-12 13:51:43",
      "bookerId" : "al_xinuan.zsy",
      "bookerName" : "张三",
      "btripCouponFee" : 234,
      "buildFee" : 123,
      "cabin" : "经济舱",
      "cabinClass" : "R",
      "capitalDirection" : "1",
      "cascadeDepartment" : "中国东南分公司-业务部",
      "changeFee" : 34,
      "corpPayOrderFee" : 23432.45,
      "costCenter" : "张三成本中心",
      "costCenterNumber" : "42342343242343",
      "coupon" : 1,
      "depAirportCode" : "KHN",
      "department" : "业务部",
      "departmentId" : "234234343555",
      "deptCity" : "南昌",
      "deptDate" : "2021-10-13",
      "deptStation" : "昌北国际机场",
      "deptTime" : "10:46:05",
      "discount" : "51%",
      "feeType" : "1",
      "flightNo" : "MU9684",
      "index" : "1",
      "insuranceFee" : 23.34,
      "invoiceTitle" : "张三发票抬头",
      "itineraryNum" : "5334916421",
      "itineraryPrice" : 2343.34,
      "mostDifferenceDeptTime" : "2021-10-01 00:17:13",
      "mostDifferenceDiscount" : 23,
      "mostDifferenceFlightNo" : "MU9684",
      "mostDifferencePrice" : 124,
      "mostDifferenceReason" : "不选",
      "mostPrice" : 1222.12,
      "negotiationCouponFee" : 2334.1,
      "oilFee" : 234.2,
      "orderId" : "214234345235",
      "overApplyId" : "3423432235",
      "primaryId" : 567563532,
      "projectCode" : "4234234324",
      "projectName" : "张三项目名称",
      "refundFee" : 452.45,
      "refundUpgradeCost" : 22.44,
      "repeatRefund" : "否",
      "sealPrice" : 2211.2,
      "serviceFee" : 222.33,
      "settlementFee" : 222.21,
      "settlementTime" : "2021-10-14 00:17:13",
      "settlementType" : "1",
      "status" : 1,
      "ticketId" : "781-6586234234324",
      "travelerId" : "al_xinuan.zsy",
      "travelerName" : "张三",
      "upgradeCost" : 231,
      "bookerJobNo" : "1242343204",
      "travelerJobNo" : "56756754"
    } ],
    "periodEnd" : "2021-10-13",
    "periodStart" : "2021-10-14",
    "totalNum" : 345435
  },
  "success" : true,
  "resultCode" : 0
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.authority | 没有操作企业数据权限 | 没有操作企业数据权限 |
| 400 | invalid.param.userId | 参数userId有误 | 参数userId有误 |
