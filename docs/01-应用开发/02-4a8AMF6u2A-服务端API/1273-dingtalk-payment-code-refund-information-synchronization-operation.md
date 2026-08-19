---
title: "通知退款结果"
source_url: "https://open.dingtalk.com/document/development/dingtalk-payment-code-refund-information-synchronization-operation"
namespace: "development"
slug: "dingtalk-payment-code-refund-information-synchronization-operation"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 通知退款结果"
doc_id: "hoseKMoApA"
updated_at: "2025-09-11 21:03:41"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-payment-code-refund-information-synchronization-operation
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 通知退款结果
> Updated: 2025-09-11 21:03:41

# 通知退款结果

用户使用钉工牌码支付后，如果发生退款，退款完成后，调用本接口同步退款结果，生成对应账单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/finance/payCodes/refundResults/notify |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Finance.PayCode.Write-钉钉付款码信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业corpId。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/)首页查看。 |
| userId | String | 是 | 用户userId，需要和创建码时传入的userId保持一致。 |
| tradeNo | String | 是 | 交易订单号，调用方生成。 |
| refundOrderNo | String | 是 | 本次退款订单号，由调用方生成。 |
| remark | String | 是 | 备注。 |
| refundAmount | String | 是 | 退款金额。 |
| refundPromotionAmount | String | 是 | 退款的优惠金额。 |
| gmtRefund | String | 是 | 退款时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| payChannelDetailList | Array | 是 | 支付渠道明细信息。 |
| payChannelName | String | 是 | 支付渠道名称，最终展示在钉钉用户账单明细中。例如：支付宝、食堂点券等。 |
| payChannelType | String | 是 | 支付渠道类型，取值：   - **ALIPAY**：支付宝 - **BALANCE**：余额 |
| amount | String | 是 | 支付渠道金额。 |
| payChannelOrderNo | String | 是 | 支付渠道订单号。 |
| payChannelRefundOrderNo | String | 是 | 支付渠道退款订单号。 |
| promotionAmount | String | 是 | 优惠金额。 |
| fundToolDetailList | Array | 是 | 资金工具明细。 |
| fundToolName | String | 是 | 资金工具名称。例如：余额。 |
| amount | String | 是 | 金额。 |
| gmtCreate | String | 是 | 开始时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| gmtFinish | String | 是 | 结束时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| promotionFundTool | Boolean | 是 | 是否优惠资金工具。   - **true**：是 - **false**：不是 |
| extInfo | String | 否 | 扩展信息。 |
| payCode | String | 是 | 付款码。 |

### 请求示例

HTTP

```
POST /v1.0/finance/payCodes/refund/notify HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:00adbxxx
Content-Type:application/json

{
  "corpId" : "ding1234",
  "userId" : "userId",
  "tradeNo" : "tradeNo",
  "refundOrderNo" : "refundOrderNo",
  "remark" : "退款",
  "refundAmount" : "1.00",
  "refundPromotionAmount" : "0.00",
  "gmtRefund" : "2021-11-11 11:11:11",
  "payChannelDetailList" : [ {
    "payChannelName" : "支付宝",
    "payChannelType" : "ALIPAY",
    "amount" : "1.00",
    "payChannelOrderNo" : "2021010123456",
    "payChannelRefundOrderNo" : "2021010123456",
    "promotionAmount" : "0.00",
    "fundToolDetailList" : [ {
      "fundToolName" : "余额",
      "amount" : "1.00",
      "gmtCreate" : "2021-11-11 11:11:11",
      "gmtFinish" : "2021010123456",
      "promotionFundTool" : false,
      "extInfo" : "{\"key1\":\"value1\"}"
    } ]
  } ],
  "payCode" : "payCode"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkfinance_1_0.*;
import com.aliyun.dingtalkfinance_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkfinance_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkfinance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkfinance_1_0.Client client = Sample.createClient();
        NotifyPayCodeRefundResultHeaders notifyPayCodeRefundResultHeaders = new NotifyPayCodeRefundResultHeaders();
        notifyPayCodeRefundResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
        NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList payChannelDetailList0FundToolDetailList0 = new NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList()
                .setFundToolName("余额")
                .setAmount("1.00")
                .setGmtCreate("2021-11-11 11:11:11")
                .setGmtFinish("2021010123456")
                .setPromotionFundTool(false)
                .setExtInfo("{\"key1\":\"value1\"}");
        NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList payChannelDetailList0 = new NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList()
                .setPayChannelName("支付宝")
                .setPayChannelType("ALIPAY")
                .setAmount("1.00")
                .setPayChannelOrderNo("2021010123456")
                .setPayChannelRefundOrderNo("2021010123456")
                .setPromotionAmount("0.00")
                .setFundToolDetailList(java.util.Arrays.asList(
                    payChannelDetailList0FundToolDetailList0
                ));
        NotifyPayCodeRefundResultRequest notifyPayCodeRefundResultRequest = new NotifyPayCodeRefundResultRequest()
                .setCorpId("ding1234")
                .setUserId("userId")
                .setTradeNo("tradeNo")
                .setRefundOrderNo("refundOrderNo")
                .setRemark("退款")
                .setRefundAmount("1.00")
                .setRefundPromotionAmount("0.00")
                .setGmtRefund("2021-11-11 11:11:11")
                .setPayChannelDetailList(java.util.Arrays.asList(
                    payChannelDetailList0
                ))
                .setPayCode("payCode");
        try {
            client.notifyPayCodeRefundResultWithOptions(notifyPayCodeRefundResultRequest, notifyPayCodeRefundResultHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.finance_1_0.client import Client as dingtalkfinance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.finance_1_0 import models as dingtalkfinance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkfinance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkfinance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_pay_code_refund_result_headers = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultHeaders()
        notify_pay_code_refund_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        pay_channel_detail_list_0fund_tool_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList(
            fund_tool_name='余额',
            amount='1.00',
            gmt_create='2021-11-11 11:11:11',
            gmt_finish='2021010123456',
            promotion_fund_tool=False,
            ext_info='{"key1":"value1"}'
        )
        pay_channel_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequestPayChannelDetailList(
            pay_channel_name='支付宝',
            pay_channel_type='ALIPAY',
            amount='1.00',
            pay_channel_order_no='2021010123456',
            pay_channel_refund_order_no='2021010123456',
            promotion_amount='0.00',
            fund_tool_detail_list=[
                pay_channel_detail_list_0fund_tool_detail_list_0
            ]
        )
        notify_pay_code_refund_result_request = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequest(
            corp_id='ding1234',
            user_id='userId',
            trade_no='tradeNo',
            refund_order_no='refundOrderNo',
            remark='退款',
            refund_amount='1.00',
            refund_promotion_amount='0.00',
            gmt_refund='2021-11-11 11:11:11',
            pay_channel_detail_list=[
                pay_channel_detail_list_0
            ],
            pay_code='payCode'
        )
        try:
            client.notify_pay_code_refund_result_with_options(notify_pay_code_refund_result_request, notify_pay_code_refund_result_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_pay_code_refund_result_headers = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultHeaders()
        notify_pay_code_refund_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        pay_channel_detail_list_0fund_tool_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList(
            fund_tool_name='余额',
            amount='1.00',
            gmt_create='2021-11-11 11:11:11',
            gmt_finish='2021010123456',
            promotion_fund_tool=False,
            ext_info='{"key1":"value1"}'
        )
        pay_channel_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequestPayChannelDetailList(
            pay_channel_name='支付宝',
            pay_channel_type='ALIPAY',
            amount='1.00',
            pay_channel_order_no='2021010123456',
            pay_channel_refund_order_no='2021010123456',
            promotion_amount='0.00',
            fund_tool_detail_list=[
                pay_channel_detail_list_0fund_tool_detail_list_0
            ]
        )
        notify_pay_code_refund_result_request = dingtalkfinance__1__0_models.NotifyPayCodeRefundResultRequest(
            corp_id='ding1234',
            user_id='userId',
            trade_no='tradeNo',
            refund_order_no='refundOrderNo',
            remark='退款',
            refund_amount='1.00',
            refund_promotion_amount='0.00',
            gmt_refund='2021-11-11 11:11:11',
            pay_channel_detail_list=[
                pay_channel_detail_list_0
            ],
            pay_code='payCode'
        )
        try:
            await client.notify_pay_code_refund_result_with_options_async(notify_pay_code_refund_result_request, notify_pay_code_refund_result_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodeRefundResultHeaders;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodeRefundResultRequest\payChannelDetailList\fundToolDetailList;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodeRefundResultRequest\payChannelDetailList;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodeRefundResultRequest;
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
        $notifyPayCodeRefundResultHeaders = new NotifyPayCodeRefundResultHeaders([]);
        $notifyPayCodeRefundResultHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $payChannelDetailList0FundToolDetailList0 = new fundToolDetailList([
            "fundToolName" => "余额",
            "amount" => "1.00",
            "gmtCreate" => "2021-11-11 11:11:11",
            "gmtFinish" => "2021010123456",
            "promotionFundTool" => false,
            "extInfo" => "{\"key1\":\"value1\"}"
        ]);
        $payChannelDetailList0 = new payChannelDetailList([
            "payChannelName" => "支付宝",
            "payChannelType" => "ALIPAY",
            "amount" => "1.00",
            "payChannelOrderNo" => "2021010123456",
            "payChannelRefundOrderNo" => "2021010123456",
            "promotionAmount" => "0.00",
            "fundToolDetailList" => [
                $payChannelDetailList0FundToolDetailList0
            ]
        ]);
        $notifyPayCodeRefundResultRequest = new NotifyPayCodeRefundResultRequest([
            "corpId" => "ding1234",
            "userId" => "userId",
            "tradeNo" => "tradeNo",
            "refundOrderNo" => "refundOrderNo",
            "remark" => "退款",
            "refundAmount" => "1.00",
            "refundPromotionAmount" => "0.00",
            "gmtRefund" => "2021-11-11 11:11:11",
            "payChannelDetailList" => [
                $payChannelDetailList0
            ],
            "payCode" => "payCode"
        ]);
        try {
            $client->notifyPayCodeRefundResultWithOptions($notifyPayCodeRefundResultRequest, $notifyPayCodeRefundResultHeaders, new RuntimeOptions([]));
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
  dingtalkfinance_1_0  ""github.com/alibabacloud-go/dingtalk/finance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkfinance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkfinance_1_0.Client{}
  _result, _err = dingtalkfinance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  notifyPayCodeRefundResultHeaders := &dingtalkfinance_1_0.NotifyPayCodeRefundResultHeaders{}
  notifyPayCodeRefundResultHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  payChannelDetailList0FundToolDetailList0 := &dingtalkfinance_1_0.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList{
    FundToolName: tea.String("余额"),
    Amount: tea.String("1.00"),
    GmtCreate: tea.String("2021-11-11 11:11:11"),
    GmtFinish: tea.String("2021010123456"),
    PromotionFundTool: tea.Bool(false),
    ExtInfo: tea.String("{\"key1\":\"value1\"}"),
  }
  payChannelDetailList0 := &dingtalkfinance_1_0.NotifyPayCodeRefundResultRequestPayChannelDetailList{
    PayChannelName: tea.String("支付宝"),
    PayChannelType: tea.String("ALIPAY"),
    Amount: tea.String("1.00"),
    PayChannelOrderNo: tea.String("2021010123456"),
    PayChannelRefundOrderNo: tea.String("2021010123456"),
    PromotionAmount: tea.String("0.00"),
    FundToolDetailList: []*dingtalkfinance_1_0.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList{payChannelDetailList0FundToolDetailList0},
  }
  notifyPayCodeRefundResultRequest := &dingtalkfinance_1_0.NotifyPayCodeRefundResultRequest{
    CorpId: tea.String("ding1234"),
    UserId: tea.String("userId"),
    TradeNo: tea.String("tradeNo"),
    RefundOrderNo: tea.String("refundOrderNo"),
    Remark: tea.String("退款"),
    RefundAmount: tea.String("1.00"),
    RefundPromotionAmount: tea.String("0.00"),
    GmtRefund: tea.String("2021-11-11 11:11:11"),
    PayChannelDetailList: []*dingtalkfinance_1_0.NotifyPayCodeRefundResultRequestPayChannelDetailList{payChannelDetailList0},
    PayCode: tea.String("payCode"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.NotifyPayCodeRefundResultWithOptions(notifyPayCodeRefundResultRequest, notifyPayCodeRefundResultHeaders, &util.RuntimeOptions{})
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
import dingtalkfinance_1_0, * as $dingtalkfinance_1_0 from '"@alicloud/dingtalk/finance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkfinance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkfinance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let notifyPayCodeRefundResultHeaders = new $dingtalkfinance_1_0.NotifyPayCodeRefundResultHeaders({ });
    notifyPayCodeRefundResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let payChannelDetailList0FundToolDetailList0 = new $dingtalkfinance_1_0.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList({
      fundToolName: "余额",
      amount: "1.00",
      gmtCreate: "2021-11-11 11:11:11",
      gmtFinish: "2021010123456",
      promotionFundTool: false,
      extInfo: "{\"key1\":\"value1\"}",
    });
    let payChannelDetailList0 = new $dingtalkfinance_1_0.NotifyPayCodeRefundResultRequestPayChannelDetailList({
      payChannelName: "支付宝",
      payChannelType: "ALIPAY",
      amount: "1.00",
      payChannelOrderNo: "2021010123456",
      payChannelRefundOrderNo: "2021010123456",
      promotionAmount: "0.00",
      fundToolDetailList: [
        payChannelDetailList0FundToolDetailList0
      ],
    });
    let notifyPayCodeRefundResultRequest = new $dingtalkfinance_1_0.NotifyPayCodeRefundResultRequest({
      corpId: "ding1234",
      userId: "userId",
      tradeNo: "tradeNo",
      refundOrderNo: "refundOrderNo",
      remark: "退款",
      refundAmount: "1.00",
      refundPromotionAmount: "0.00",
      gmtRefund: "2021-11-11 11:11:11",
      payChannelDetailList: [
        payChannelDetailList0
      ],
      payCode: "payCode",
    });
    try {
      await client.notifyPayCodeRefundResultWithOptions(notifyPayCodeRefundResultRequest, notifyPayCodeRefundResultHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkfinance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkfinance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultHeaders notifyPayCodeRefundResultHeaders = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultHeaders();
            notifyPayCodeRefundResultHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList payChannelDetailList0FundToolDetailList0 = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList
            {
                FundToolName = "余额",
                Amount = "1.00",
                GmtCreate = "2021-11-11 11:11:11",
                GmtFinish = "2021010123456",
                PromotionFundTool = false,
                ExtInfo = "{\"key1\":\"value1\"}",
            };
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList payChannelDetailList0 = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList
            {
                PayChannelName = "支付宝",
                PayChannelType = "ALIPAY",
                Amount = "1.00",
                PayChannelOrderNo = "2021010123456",
                PayChannelRefundOrderNo = "2021010123456",
                PromotionAmount = "0.00",
                FundToolDetailList = new List<AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList.NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList>
                {
                    payChannelDetailList0FundToolDetailList0
                },
            };
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest notifyPayCodeRefundResultRequest = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest
            {
                CorpId = "ding1234",
                UserId = "userId",
                TradeNo = "tradeNo",
                RefundOrderNo = "refundOrderNo",
                Remark = "退款",
                RefundAmount = "1.00",
                RefundPromotionAmount = "0.00",
                GmtRefund = "2021-11-11 11:11:11",
                PayChannelDetailList = new List<AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodeRefundResultRequest.NotifyPayCodeRefundResultRequestPayChannelDetailList>
                {
                    payChannelDetailList0
                },
                PayCode = "payCode",
            };
            try
            {
                client.NotifyPayCodeRefundResultWithOptions(notifyPayCodeRefundResultRequest, notifyPayCodeRefundResultHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkfinance__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkfinance_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkfinance_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::Client> client = make_shared<Alibabacloud_Dingtalkfinance_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultHeaders> notifyPayCodeRefundResultHeaders = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultHeaders>();
  notifyPayCodeRefundResultHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList> payChannelDetailList0FundToolDetailList0 = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList>(map<string, boost::any>({
    {"fundToolName", boost::any(string("余额"))},
    {"amount", boost::any(string("1.00"))},
    {"gmtCreate", boost::any(string("2021-11-11 11:11:11"))},
    {"gmtFinish", boost::any(string("2021010123456"))},
    {"promotionFundTool", boost::any(false)},
    {"extInfo", boost::any(string("{"key1":"value1"}"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequestPayChannelDetailList> payChannelDetailList0 = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequestPayChannelDetailList>(map<string, boost::any>({
    {"payChannelName", boost::any(string("支付宝"))},
    {"payChannelType", boost::any(string("ALIPAY"))},
    {"amount", boost::any(string("1.00"))},
    {"payChannelOrderNo", boost::any(string("2021010123456"))},
    {"payChannelRefundOrderNo", boost::any(string("2021010123456"))},
    {"promotionAmount", boost::any(string("0.00"))},
    {"fundToolDetailList", boost::any(vector<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequestPayChannelDetailListFundToolDetailList>({
      payChannelDetailList0FundToolDetailList0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequest> notifyPayCodeRefundResultRequest = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding1234"))},
    {"userId", boost::any(string("userId"))},
    {"tradeNo", boost::any(string("tradeNo"))},
    {"refundOrderNo", boost::any(string("refundOrderNo"))},
    {"remark", boost::any(string("退款"))},
    {"refundAmount", boost::any(string("1.00"))},
    {"refundPromotionAmount", boost::any(string("0.00"))},
    {"gmtRefund", boost::any(string("2021-11-11 11:11:11"))},
    {"payChannelDetailList", boost::any(vector<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodeRefundResultRequestPayChannelDetailList>({
      payChannelDetailList0
    }))},
    {"payCode", boost::any(string("payCode"))}
  }));
  try {
    client->notifyPayCodeRefundResultWithOptions(notifyPayCodeRefundResultRequest, notifyPayCodeRefundResultHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | String | 处理结果。   - **SUCCESS**：成功 - **FAIL**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : "SUCCESS"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 无效的请求参数 | 无效的请求参数 |
| 400 | invalidParameter | 无效请求参数 | 无效请求参数 |
| 400 | missingParameter | 缺少必须参数 | 缺少必须参数 |
| 400 | invalidPayCode | 无效payCode | 无效payCode |
| 400 | dataNotConsist | 数据不一致 | 数据不一致 |
| 400 | moneyNotConsist | 金额不一致 | 金额不一致 |
| 500 | unknownError | 未知错误 | 未知错误 |
| 500 | callAlipayFail | 调用支付宝异常 | 无效的请求参数 |
| 500 | callOrgFail | 调用内部通讯录异常 | 调用内部通讯录异常 |
| 500 | accessStorageFail | 访问存储异常 | 访问存储异常 |
