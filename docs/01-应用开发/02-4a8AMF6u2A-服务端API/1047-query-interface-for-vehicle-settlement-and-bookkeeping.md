---
title: "查询用车结算记账记录"
source_url: "https://open.dingtalk.com/document/development/query-interface-for-vehicle-settlement-and-bookkeeping"
namespace: "development"
slug: "query-interface-for-vehicle-settlement-and-bookkeeping"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 账单管理 > 查询用车结算记账记录"
doc_id: "t9useW0Cqi"
updated_at: "2026-01-29 14:31:12"
---

> Source: https://open.dingtalk.com/document/development/query-interface-for-vehicle-settlement-and-bookkeeping
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 账单管理 > 查询用车结算记账记录
> Updated: 2026-01-29 14:31:12

# 查询用车结算记账记录

调用本接口查询商旅用车的结算记账数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/billSettlements/cars |
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
| corpId | String | 否 | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| category | Long | 否 | 类目：机酒火车：   - **0**：火车 - **1**：机票 - **2**：酒店 - **4**：用车 - **6**：商旅火车票 |
| pageSize | Long | 否 | 每页数据量，默认100，最高100。 |
| periodStart | String | 否 | 记账更新开始日期。 |
| periodEnd | String | 否 | 记账更新结束日期。 |
| pageNumber | Long | 否 | 页数，从1开始。 |

### 请求示例

HTTP

```
GET /v1.0/alitrip/billSettlements/cars?corpId=ding0e577cd03421ad0b78f&category=4&pageSize=100&periodStart=2021-10-13&periodEnd=2021-10-14&pageNumber=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dca26861ca183b759de732ea5abe0b79
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
        BillSettementCarHeaders billSettementCarHeaders = new BillSettementCarHeaders();
        billSettementCarHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BillSettementCarRequest billSettementCarRequest = new BillSettementCarRequest()
                .setCorpId("ding0e577cd03421ad0b78f")
                .setCategory(4L)
                .setPageSize(100L)
                .setPeriodStart("2021-10-13")
                .setPeriodEnd("2021-10-14")
                .setPageNumber(1L);
        try {
            client.billSettementCarWithOptions(billSettementCarRequest, billSettementCarHeaders, new RuntimeOptions());
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
        bill_settement_car_headers = dingtalkalitrip__1__0_models.BillSettementCarHeaders()
        bill_settement_car_headers.x_acs_dingtalk_access_token = '<your access token>'
        bill_settement_car_request = dingtalkalitrip__1__0_models.BillSettementCarRequest(
            corp_id='ding0e577cd03421ad0b78f',
            category=4,
            page_size=100,
            period_start='2021-10-13',
            period_end='2021-10-14',
            page_number=1
        )
        try:
            client.bill_settement_car_with_options(bill_settement_car_request, bill_settement_car_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        bill_settement_car_headers = dingtalkalitrip__1__0_models.BillSettementCarHeaders()
        bill_settement_car_headers.x_acs_dingtalk_access_token = '<your access token>'
        bill_settement_car_request = dingtalkalitrip__1__0_models.BillSettementCarRequest(
            corp_id='ding0e577cd03421ad0b78f',
            category=4,
            page_size=100,
            period_start='2021-10-13',
            period_end='2021-10-14',
            page_number=1
        )
        try:
            await client.bill_settement_car_with_options_async(bill_settement_car_request, bill_settement_car_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\BillSettementCarHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\BillSettementCarRequest;
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
        $billSettementCarHeaders = new BillSettementCarHeaders([]);
        $billSettementCarHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $billSettementCarRequest = new BillSettementCarRequest([
            "corpId" => "ding0e577cd03421ad0b78f",
            "category" => 4,
            "pageSize" => 100,
            "periodStart" => "2021-10-13",
            "periodEnd" => "2021-10-14",
            "pageNumber" => 1
        ]);
        try {
            $client->billSettementCarWithOptions($billSettementCarRequest, $billSettementCarHeaders, new RuntimeOptions([]));
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

  billSettementCarHeaders := &dingtalkalitrip_1_0.BillSettementCarHeaders{}
  billSettementCarHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  billSettementCarRequest := &dingtalkalitrip_1_0.BillSettementCarRequest{
    CorpId: tea.String("ding0e577cd03421ad0b78f"),
    Category: tea.Int64(4),
    PageSize: tea.Int64(100),
    PeriodStart: tea.String("2021-10-13"),
    PeriodEnd: tea.String("2021-10-14"),
    PageNumber: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BillSettementCarWithOptions(billSettementCarRequest, billSettementCarHeaders, &util.RuntimeOptions{})
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
    let billSettementCarHeaders = new $dingtalkalitrip_1_0.BillSettementCarHeaders({ });
    billSettementCarHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let billSettementCarRequest = new $dingtalkalitrip_1_0.BillSettementCarRequest({
      corpId: "ding0e577cd03421ad0b78f",
      category: 4,
      pageSize: 100,
      periodStart: "2021-10-13",
      periodEnd: "2021-10-14",
      pageNumber: 1,
    });
    try {
      await client.billSettementCarWithOptions(billSettementCarRequest, billSettementCarHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementCarHeaders billSettementCarHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementCarHeaders();
            billSettementCarHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementCarRequest billSettementCarRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.BillSettementCarRequest
            {
                CorpId = "ding0e577cd03421ad0b78f",
                Category = 4,
                PageSize = 100,
                PeriodStart = "2021-10-13",
                PeriodEnd = "2021-10-14",
                PageNumber = 1,
            };
            try
            {
                client.BillSettementCarWithOptions(billSettementCarRequest, billSettementCarHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::BillSettementCarHeaders> billSettementCarHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::BillSettementCarHeaders>();
  billSettementCarHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::BillSettementCarRequest> billSettementCarRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::BillSettementCarRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding0e577cd03421ad0b78f"))},
    {"category", boost::any(4)},
    {"pageSize", boost::any(100)},
    {"periodStart", boost::any(string("2021-10-13"))},
    {"periodEnd", boost::any(string("2021-10-14"))},
    {"pageNumber", boost::any(1)}
  }));
  try {
    client->billSettementCarWithOptions(billSettementCarRequest, billSettementCarHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| alipayTradeNo | String | 支付交易流水号。 |
| applyId | String | 审批单号。 |
| arrCity | String | 到达城市。 |
| arrDate | String | 到达日期。 |
| arrLocation | String | 到达地。 |
| arrTime | String | 到达时间。 |
| bookTime | String | 预定时间。 |
| bookerId | String | 预定人use id。 |
| bookerName | String | 预订人名称。 |
| businessCategory | String | 用车原因。 |
| capitalDirection | String | 资金方向：   - **1**：支出 - **2**：收入 |
| carLevel | String | 车型。 |
| cascadeDepartment | String | 级联部门。 |
| costCenter | String | 成本中心名称。 |
| costCenterNumber | String | 成本中心编号。 |
| coupon | double | 优惠券。 |
| couponPrice | double | 优惠金额。 |
| department | String | 末级部门。 |
| departmentId | String | 部门id。 |
| deptCity | String | 出发城市。 |
| deptDate | String | 出发日期。 |
| deptLocation | String | 出发地。 |
| deptTime | String | 出发时间。 |
| estimateDriveDistance | String | 预估行驶距离。 |
| estimatePrice | double | 预估金额。 |
| feeType | String | 费用类型：   - **10101**：机票预订 - **10202**：机票改签手续费 - **10203**：机票改签差价 - **10301**：机票退款 - **10302**：机票改签退款 - **10303**：机票补退 - **10401**：机票保险-航意险购买 - **10501**：机票保险-航意险退保 - **11001**：机票的预订服务费 - **11002**：机票改签服务费 - **20101**：酒店预订 - **20103**：酒店退款 - **20111**：酒店预订服务费 - **20112**：酒店托管服务费 - **40101**：用车预订 - **40103**：用车退款 - **40107**：用车取消订单收取费用 - **40111**：用车预订服务费 - **6001**：火车票预订 - **6003**：火车票改签差价 - **6004**：火车票改签手续费 - **6005**：火车票退票 - **6007**：火车票预订服务费 - **6008**：火车票改签服务费 - **6009**：火车票预订退款 - **6010**：火车票改签退款 - **1201**：赔付 - **2001**：冲正 |
| index | String | 序号。 |
| invoiceTitle | String | 发票抬头。 |
| memo | String | 用车事由。 |
| orderId | String | 订单id。 |
| orderPrice | double | 订单金额。 |
| overApplyId | String | 超标审批单号。 |
| personSettleFee | double | 个人支付金额。 |
| primaryId | String | 主键id。 |
| projectCode | String | 项目编码。 |
| projectName | String | 项目名称。 |
| providerName | String | 供应商。 |
| realDriveDistance | String | 实际行驶距离。 |
| realFromAddr | String | 实际上车点。 |
| realToAddr | String | 实际下车点。 |
| serviceFee | String | 服务费，仅在feeType 40111 中展示。 |
| settlementFee | double | 结算金额。 |
| settlementTime | String | 结算时间。 |
| settlementType | String | 结算类型：   - **1**：个人现付 - **2**：企业现付 - **4**：企业月结 - **8**：企业预存 |
| specialOrder | String | 特别关注订单。 |
| specialReason | String | 特别关注原因。 |
| status | Long | 入账状态：   - **-1**：个人支付不入账 - **0**：待入账 - **1**：入账成功 |
| travelerId | String | 出行人use id。 |
| travelerName | String | 出行人名称。 |
| userConfirmDesc | String | 员工是否认可。 |
| bookerJobNo | String | 预订人工号。 |
| travelerJobNo | String | 出行人工号。 |
| voucherType | Long | 发票类型：   - **11**：增值税普通发票 - **12**：增值税专用发票 - **1**：增值税发票 - **2**：机票行程单 - **5**：火车票凭证 - **6**：定额发票 - **99**：不提供票据 - **7**：线下制票 |
| subOrderId | String | 子订单号。 |
| billRecordTime | String | 入账时间。 |
| settlementGrantFee | double | 预存赠送金额消费。 |
| remark | String | 备注。 |
| periodEnd | String | 记账更新开始日期。 |
| periodStart | String | 记账更新结束日期。 |
| totalNum | Long | 总数量。 |
| success | Boolean | 是否成功。 |
| resultCode | Long | 结果code。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "resultMsg" : "resultMsg",
  "module" : {
    "category" : 1,
    "corpId" : "ding3454534543543",
    "dataList" : [ {
      "alipayTradeNo" : "34534543545345",
      "applyId" : "12321213",
      "arrCity" : "杭州市",
      "arrDate" : "2021-10-13",
      "arrLocation" : "杭州东站",
      "arrTime" : "13:46:05",
      "bookTime" : "2021-10-13",
      "bookerId" : "70022164",
      "bookerName" : "张三",
      "businessCategory" : "市内用车",
      "capitalDirection" : "1",
      "carLevel" : "经济型",
      "cascadeDepartment" : "中国东南分公司-业务部",
      "costCenter" : "张三成本中心",
      "costCenterNumber" : "70022164",
      "coupon" : 1,
      "couponPrice" : 4,
      "department" : "业务部",
      "departmentId" : "12321213",
      "deptCity" : "杭州市",
      "deptDate" : "2021-10-13",
      "deptLocation" : "杭州大厦",
      "deptTime" : "12:46:05",
      "estimateDriveDistance" : "28.09",
      "estimatePrice" : 12.7,
      "feeType" : "40107",
      "index" : "1",
      "invoiceTitle" : "张三发票抬头",
      "memo" : "回家",
      "orderId" : "70022164",
      "orderPrice" : 34.8,
      "overApplyId" : "34534543545345345",
      "personSettleFee" : 0,
      "primaryId" : "12345622",
      "projectCode" : "54433",
      "projectName" : "张三项目名称",
      "providerName" : "曹操专车",
      "realDriveDistance" : "30.56",
      "realFromAddr" : "杭州大厦南门",
      "realToAddr" : "杭州东站二楼候车平台",
      "serviceFee" : "3.44",
      "settlementFee" : 28.33,
      "settlementTime" : "2021-10-13 13:51:43",
      "settlementType" : "4",
      "specialOrder" : "是",
      "specialReason" : "关注",
      "status" : 1,
      "travelerId" : "70022164",
      "travelerName" : "张三",
      "userConfirmDesc" : "是",
      "bookerJobNo" : "70022164",
      "travelerJobNo" : "70022164"
    } ],
    "periodEnd" : "2021-10-14",
    "periodStart" : "2021-10-13",
    "totalNum" : 2694
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
