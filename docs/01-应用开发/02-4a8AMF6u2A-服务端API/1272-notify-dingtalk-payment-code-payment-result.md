---
title: "通知支付结果"
source_url: "https://open.dingtalk.com/document/development/notify-dingtalk-payment-code-payment-result"
namespace: "development"
slug: "notify-dingtalk-payment-code-payment-result"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 通知支付结果"
doc_id: "PqbYz11gEh"
updated_at: "2025-09-11 21:03:40"
---

> Source: https://open.dingtalk.com/document/development/notify-dingtalk-payment-code-payment-result
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 通知支付结果
> Updated: 2025-09-11 21:03:40

# 通知支付结果

用户使用钉工牌码扫码支付完成后，可调用本接口同步支付结果，并通知用户完成消费，同时为用户记录账单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/finance/payCodes/payResults/notify |
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
| payCode | String | 是 | 码值，使用硬件设备扫描获取的码值。 |
| corpId | String | 是 | 企业corpId。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/)首页查看。 |
| userId | String | 是 | 用户的userId，需要与创建码时的userid保持一致。 |
| gmtTradeCreate | String | 是 | 交易开始时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| gmtTradeFinish | String | 是 | 交易结束时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| tradeNo | String | 是 | 交易号，调用方生成的交易号。 |
| tradeStatus | String | 是 | 交易状态，取值。   - **SUCCESS**：成功 - **FALL**：失败 |
| title | String | 是 | 订单标题。 |
| remark | String | 是 | 备注。 |
| amount | String | 是 | 订单金额。 |
| promotionAmount | String | 是 | 订单优惠金额，如果没有传0.00。 |
| chargeAmount | String | 是 | 收费金额。       - 该笔交易针对收款方的收费金额, 如果没有传0.00。 - 收单情况下，支付宝向调用方收取的手续费。 |
| payChannelDetailList | Array | 是 | 支付渠道明细信息。   - 如果**tradeStatus**为**SUCCESS**（支付成功），支付渠道信息则必传。 - 如果**tradeStatus**为**FAIL**（支付失败），同时需要传入**tradeErrorCode**, **tradeErrorMsg**，用于告知用户扣款失败原因。 |
| payChannelName | String | 是 | 支付渠道名称。 |
| gmtCreate | String | 否 | 开始时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| gmtFinish | String | 否 | 结束时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| payChannelType | String | 是 | 支付渠道类型，取值。   - **ALIPAY**：支付宝 - **BALANCE**：余额 |
| amount | String | 是 | 支付金额。 |
| payChannelOrderNo | String | 是 | 支付渠道单号，调用方自身集成的支付渠道单号。 |
| promotionAmount | String | 是 | 优惠金额。 |
| fundToolDetailList | Array | 是 | 资金工具明细。 |
| fundToolName | String | 是 | 资金渠道名称。 |
| amount | String | 是 | 金额。 |
| gmtCreate | String | 是 | 开始时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| gmtFinish | String | 是 | 结束时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| promotionFundTool | Boolean | 是 | 是否是优惠工具。   - **true**：是 - **false**：不是 |
| extInfo | String | 否 | 扩展信息。 |
| tradeErrorCode | String | 否 | 支付失败错误码，当**tradeStatus**为**FAIL**时必须传入。 |
| tradeErrorMsg | String | 否 | 支付失败信息，当**tradeStatus**为**FAIL**时必须传入。 |
| extInfo | String | 否 | 扩展信息。 |
| merchantName | String | 是 | 商户名称。 |

### 请求示例

HTTP

```
POST /v1.0/finance/payCodes/pay/notify HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:00adbxxx
Content-Type:application/json

{
  "payCode" : "26123xxx",
  "corpId" : "ding1234",
  "userId" : "userId1234",
  "gmtTradeCreate" : "2021-01-01 11:11:11",
  "gmtTradeFinish" : "2021-01-01 11:11:11",
  "tradeNo" : "202101012345678",
  "tradeStatus" : "SUCCESS",
  "title" : "晚餐100.0元",
  "remark" : "备注",
  "amount" : "1234.56",
  "promotionAmount" : "1.23",
  "chargeAmount" : "1.00",
  "payChannelDetailList" : [ {
    "payChannelName" : "卡余额",
    "gmtCreate" : "2021-01-01 11:11:11",
    "gmtFinish" : "2021-01-01 11:11:11",
    "payChannelType" : "ALIPAY|BALANCE",
    "amount" : "1.23",
    "payChannelOrderNo" : "20211234",
    "promotionAmount" : "0.00",
    "fundToolDetailList" : [ {
      "fundToolName" : "优惠券",
      "amount" : "1.00",
      "gmtCreate" : "2021-01-01",
      "gmtFinish" : "2021-01-01 11:11:11",
      "promotionFundTool" : true,
      "extInfo" : "{\"key\":\"value\"}"
    } ]
  } ],
  "tradeErrorCode" : "BALANCE_NOT_ENOUGH",
  "tradeErrorMsg" : "余额不足，请充值",
  "extInfo" : "{ \"akey\": \"avalue“}",
  "merchantName" : "merchantName"
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
        NotifyPayCodePayResultHeaders notifyPayCodePayResultHeaders = new NotifyPayCodePayResultHeaders();
        notifyPayCodePayResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
        NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList payChannelDetailList0FundToolDetailList0 = new NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList()
                .setFundToolName("优惠券")
                .setAmount("1.00")
                .setGmtCreate("2021-01-01")
                .setGmtFinish("2021-01-01 11:11:11")
                .setPromotionFundTool(true)
                .setExtInfo("{\"key\":\"value\"}");
        NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList payChannelDetailList0 = new NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList()
                .setPayChannelName("卡余额")
                .setGmtCreate("2021-01-01 11:11:11")
                .setGmtFinish("2021-01-01 11:11:11")
                .setPayChannelType("ALIPAY|BALANCE")
                .setAmount("1.23")
                .setPayChannelOrderNo("20211234")
                .setPromotionAmount("0.00")
                .setFundToolDetailList(java.util.Arrays.asList(
                    payChannelDetailList0FundToolDetailList0
                ));
        NotifyPayCodePayResultRequest notifyPayCodePayResultRequest = new NotifyPayCodePayResultRequest()
                .setPayCode("26123xxx")
                .setCorpId("ding1234")
                .setUserId("userId1234")
                .setGmtTradeCreate("2021-01-01 11:11:11")
                .setGmtTradeFinish("2021-01-01 11:11:11")
                .setTradeNo("202101012345678")
                .setTradeStatus("SUCCESS")
                .setTitle("晚餐100.0元")
                .setRemark("备注")
                .setAmount("1234.56")
                .setPromotionAmount("1.23")
                .setChargeAmount("1.00")
                .setPayChannelDetailList(java.util.Arrays.asList(
                    payChannelDetailList0
                ))
                .setTradeErrorCode("BALANCE_NOT_ENOUGH")
                .setTradeErrorMsg("余额不足，请充值")
                .setExtInfo("{ \"akey\": \"avalue“}")
                .setMerchantName("merchantName");
        try {
            client.notifyPayCodePayResultWithOptions(notifyPayCodePayResultRequest, notifyPayCodePayResultHeaders, new RuntimeOptions());
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
        notify_pay_code_pay_result_headers = dingtalkfinance__1__0_models.NotifyPayCodePayResultHeaders()
        notify_pay_code_pay_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        pay_channel_detail_list_0fund_tool_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList(
            fund_tool_name='优惠券',
            amount='1.00',
            gmt_create='2021-01-01',
            gmt_finish='2021-01-01 11:11:11',
            promotion_fund_tool=True,
            ext_info='{"key":"value"}'
        )
        pay_channel_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodePayResultRequestPayChannelDetailList(
            pay_channel_name='卡余额',
            gmt_create='2021-01-01 11:11:11',
            gmt_finish='2021-01-01 11:11:11',
            pay_channel_type='ALIPAY|BALANCE',
            amount='1.23',
            pay_channel_order_no='20211234',
            promotion_amount='0.00',
            fund_tool_detail_list=[
                pay_channel_detail_list_0fund_tool_detail_list_0
            ]
        )
        notify_pay_code_pay_result_request = dingtalkfinance__1__0_models.NotifyPayCodePayResultRequest(
            pay_code='26123xxx',
            corp_id='ding1234',
            user_id='userId1234',
            gmt_trade_create='2021-01-01 11:11:11',
            gmt_trade_finish='2021-01-01 11:11:11',
            trade_no='202101012345678',
            trade_status='SUCCESS',
            title='晚餐100.0元',
            remark='备注',
            amount='1234.56',
            promotion_amount='1.23',
            charge_amount='1.00',
            pay_channel_detail_list=[
                pay_channel_detail_list_0
            ],
            trade_error_code='BALANCE_NOT_ENOUGH',
            trade_error_msg='余额不足，请充值',
            ext_info='{ "akey": "avalue“}',
            merchant_name='merchantName'
        )
        try:
            client.notify_pay_code_pay_result_with_options(notify_pay_code_pay_result_request, notify_pay_code_pay_result_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_pay_code_pay_result_headers = dingtalkfinance__1__0_models.NotifyPayCodePayResultHeaders()
        notify_pay_code_pay_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        pay_channel_detail_list_0fund_tool_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList(
            fund_tool_name='优惠券',
            amount='1.00',
            gmt_create='2021-01-01',
            gmt_finish='2021-01-01 11:11:11',
            promotion_fund_tool=True,
            ext_info='{"key":"value"}'
        )
        pay_channel_detail_list_0 = dingtalkfinance__1__0_models.NotifyPayCodePayResultRequestPayChannelDetailList(
            pay_channel_name='卡余额',
            gmt_create='2021-01-01 11:11:11',
            gmt_finish='2021-01-01 11:11:11',
            pay_channel_type='ALIPAY|BALANCE',
            amount='1.23',
            pay_channel_order_no='20211234',
            promotion_amount='0.00',
            fund_tool_detail_list=[
                pay_channel_detail_list_0fund_tool_detail_list_0
            ]
        )
        notify_pay_code_pay_result_request = dingtalkfinance__1__0_models.NotifyPayCodePayResultRequest(
            pay_code='26123xxx',
            corp_id='ding1234',
            user_id='userId1234',
            gmt_trade_create='2021-01-01 11:11:11',
            gmt_trade_finish='2021-01-01 11:11:11',
            trade_no='202101012345678',
            trade_status='SUCCESS',
            title='晚餐100.0元',
            remark='备注',
            amount='1234.56',
            promotion_amount='1.23',
            charge_amount='1.00',
            pay_channel_detail_list=[
                pay_channel_detail_list_0
            ],
            trade_error_code='BALANCE_NOT_ENOUGH',
            trade_error_msg='余额不足，请充值',
            ext_info='{ "akey": "avalue“}',
            merchant_name='merchantName'
        )
        try:
            await client.notify_pay_code_pay_result_with_options_async(notify_pay_code_pay_result_request, notify_pay_code_pay_result_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodePayResultHeaders;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodePayResultRequest\payChannelDetailList\fundToolDetailList;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodePayResultRequest\payChannelDetailList;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\NotifyPayCodePayResultRequest;
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
        $notifyPayCodePayResultHeaders = new NotifyPayCodePayResultHeaders([]);
        $notifyPayCodePayResultHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $payChannelDetailList0FundToolDetailList0 = new fundToolDetailList([
            "fundToolName" => "优惠券",
            "amount" => "1.00",
            "gmtCreate" => "2021-01-01",
            "gmtFinish" => "2021-01-01 11:11:11",
            "promotionFundTool" => true,
            "extInfo" => "{\"key\":\"value\"}"
        ]);
        $payChannelDetailList0 = new payChannelDetailList([
            "payChannelName" => "卡余额",
            "gmtCreate" => "2021-01-01 11:11:11",
            "gmtFinish" => "2021-01-01 11:11:11",
            "payChannelType" => "ALIPAY|BALANCE",
            "amount" => "1.23",
            "payChannelOrderNo" => "20211234",
            "promotionAmount" => "0.00",
            "fundToolDetailList" => [
                $payChannelDetailList0FundToolDetailList0
            ]
        ]);
        $notifyPayCodePayResultRequest = new NotifyPayCodePayResultRequest([
            "payCode" => "26123xxx",
            "corpId" => "ding1234",
            "userId" => "userId1234",
            "gmtTradeCreate" => "2021-01-01 11:11:11",
            "gmtTradeFinish" => "2021-01-01 11:11:11",
            "tradeNo" => "202101012345678",
            "tradeStatus" => "SUCCESS",
            "title" => "晚餐100.0元",
            "remark" => "备注",
            "amount" => "1234.56",
            "promotionAmount" => "1.23",
            "chargeAmount" => "1.00",
            "payChannelDetailList" => [
                $payChannelDetailList0
            ],
            "tradeErrorCode" => "BALANCE_NOT_ENOUGH",
            "tradeErrorMsg" => "余额不足，请充值",
            "extInfo" => "{ \"akey\": \"avalue“}",
            "merchantName" => "merchantName"
        ]);
        try {
            $client->notifyPayCodePayResultWithOptions($notifyPayCodePayResultRequest, $notifyPayCodePayResultHeaders, new RuntimeOptions([]));
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

  notifyPayCodePayResultHeaders := &dingtalkfinance_1_0.NotifyPayCodePayResultHeaders{}
  notifyPayCodePayResultHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  payChannelDetailList0FundToolDetailList0 := &dingtalkfinance_1_0.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList{
    FundToolName: tea.String("优惠券"),
    Amount: tea.String("1.00"),
    GmtCreate: tea.String("2021-01-01"),
    GmtFinish: tea.String("2021-01-01 11:11:11"),
    PromotionFundTool: tea.Bool(true),
    ExtInfo: tea.String("{\"key\":\"value\"}"),
  }
  payChannelDetailList0 := &dingtalkfinance_1_0.NotifyPayCodePayResultRequestPayChannelDetailList{
    PayChannelName: tea.String("卡余额"),
    GmtCreate: tea.String("2021-01-01 11:11:11"),
    GmtFinish: tea.String("2021-01-01 11:11:11"),
    PayChannelType: tea.String("ALIPAY|BALANCE"),
    Amount: tea.String("1.23"),
    PayChannelOrderNo: tea.String("20211234"),
    PromotionAmount: tea.String("0.00"),
    FundToolDetailList: []*dingtalkfinance_1_0.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList{payChannelDetailList0FundToolDetailList0},
  }
  notifyPayCodePayResultRequest := &dingtalkfinance_1_0.NotifyPayCodePayResultRequest{
    PayCode: tea.String("26123xxx"),
    CorpId: tea.String("ding1234"),
    UserId: tea.String("userId1234"),
    GmtTradeCreate: tea.String("2021-01-01 11:11:11"),
    GmtTradeFinish: tea.String("2021-01-01 11:11:11"),
    TradeNo: tea.String("202101012345678"),
    TradeStatus: tea.String("SUCCESS"),
    Title: tea.String("晚餐100.0元"),
    Remark: tea.String("备注"),
    Amount: tea.String("1234.56"),
    PromotionAmount: tea.String("1.23"),
    ChargeAmount: tea.String("1.00"),
    PayChannelDetailList: []*dingtalkfinance_1_0.NotifyPayCodePayResultRequestPayChannelDetailList{payChannelDetailList0},
    TradeErrorCode: tea.String("BALANCE_NOT_ENOUGH"),
    TradeErrorMsg: tea.String("余额不足，请充值"),
    ExtInfo: tea.String("{ \"akey\": \"avalue“}"),
    MerchantName: tea.String("merchantName"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.NotifyPayCodePayResultWithOptions(notifyPayCodePayResultRequest, notifyPayCodePayResultHeaders, &util.RuntimeOptions{})
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
    let notifyPayCodePayResultHeaders = new $dingtalkfinance_1_0.NotifyPayCodePayResultHeaders({ });
    notifyPayCodePayResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let payChannelDetailList0FundToolDetailList0 = new $dingtalkfinance_1_0.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList({
      fundToolName: "优惠券",
      amount: "1.00",
      gmtCreate: "2021-01-01",
      gmtFinish: "2021-01-01 11:11:11",
      promotionFundTool: true,
      extInfo: "{\"key\":\"value\"}",
    });
    let payChannelDetailList0 = new $dingtalkfinance_1_0.NotifyPayCodePayResultRequestPayChannelDetailList({
      payChannelName: "卡余额",
      gmtCreate: "2021-01-01 11:11:11",
      gmtFinish: "2021-01-01 11:11:11",
      payChannelType: "ALIPAY|BALANCE",
      amount: "1.23",
      payChannelOrderNo: "20211234",
      promotionAmount: "0.00",
      fundToolDetailList: [
        payChannelDetailList0FundToolDetailList0
      ],
    });
    let notifyPayCodePayResultRequest = new $dingtalkfinance_1_0.NotifyPayCodePayResultRequest({
      payCode: "26123xxx",
      corpId: "ding1234",
      userId: "userId1234",
      gmtTradeCreate: "2021-01-01 11:11:11",
      gmtTradeFinish: "2021-01-01 11:11:11",
      tradeNo: "202101012345678",
      tradeStatus: "SUCCESS",
      title: "晚餐100.0元",
      remark: "备注",
      amount: "1234.56",
      promotionAmount: "1.23",
      chargeAmount: "1.00",
      payChannelDetailList: [
        payChannelDetailList0
      ],
      tradeErrorCode: "BALANCE_NOT_ENOUGH",
      tradeErrorMsg: "余额不足，请充值",
      extInfo: "{ \"akey\": \"avalue“}",
      merchantName: "merchantName",
    });
    try {
      await client.notifyPayCodePayResultWithOptions(notifyPayCodePayResultRequest, notifyPayCodePayResultHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultHeaders notifyPayCodePayResultHeaders = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultHeaders();
            notifyPayCodePayResultHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList payChannelDetailList0FundToolDetailList0 = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList
            {
                FundToolName = "优惠券",
                Amount = "1.00",
                GmtCreate = "2021-01-01",
                GmtFinish = "2021-01-01 11:11:11",
                PromotionFundTool = true,
                ExtInfo = "{\"key\":\"value\"}",
            };
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList payChannelDetailList0 = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList
            {
                PayChannelName = "卡余额",
                GmtCreate = "2021-01-01 11:11:11",
                GmtFinish = "2021-01-01 11:11:11",
                PayChannelType = "ALIPAY|BALANCE",
                Amount = "1.23",
                PayChannelOrderNo = "20211234",
                PromotionAmount = "0.00",
                FundToolDetailList = new List<AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList.NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList>
                {
                    payChannelDetailList0FundToolDetailList0
                },
            };
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest notifyPayCodePayResultRequest = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest
            {
                PayCode = "26123xxx",
                CorpId = "ding1234",
                UserId = "userId1234",
                GmtTradeCreate = "2021-01-01 11:11:11",
                GmtTradeFinish = "2021-01-01 11:11:11",
                TradeNo = "202101012345678",
                TradeStatus = "SUCCESS",
                Title = "晚餐100.0元",
                Remark = "备注",
                Amount = "1234.56",
                PromotionAmount = "1.23",
                ChargeAmount = "1.00",
                PayChannelDetailList = new List<AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.NotifyPayCodePayResultRequest.NotifyPayCodePayResultRequestPayChannelDetailList>
                {
                    payChannelDetailList0
                },
                TradeErrorCode = "BALANCE_NOT_ENOUGH",
                TradeErrorMsg = "余额不足，请充值",
                ExtInfo = "{ \"akey\": \"avalue“}",
                MerchantName = "merchantName",
            };
            try
            {
                client.NotifyPayCodePayResultWithOptions(notifyPayCodePayResultRequest, notifyPayCodePayResultHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultHeaders> notifyPayCodePayResultHeaders = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultHeaders>();
  notifyPayCodePayResultHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList> payChannelDetailList0FundToolDetailList0 = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList>(map<string, boost::any>({
    {"fundToolName", boost::any(string("优惠券"))},
    {"amount", boost::any(string("1.00"))},
    {"gmtCreate", boost::any(string("2021-01-01"))},
    {"gmtFinish", boost::any(string("2021-01-01 11:11:11"))},
    {"promotionFundTool", boost::any(true)},
    {"extInfo", boost::any(string("{"key":"value"}"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequestPayChannelDetailList> payChannelDetailList0 = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequestPayChannelDetailList>(map<string, boost::any>({
    {"payChannelName", boost::any(string("卡余额"))},
    {"gmtCreate", boost::any(string("2021-01-01 11:11:11"))},
    {"gmtFinish", boost::any(string("2021-01-01 11:11:11"))},
    {"payChannelType", boost::any(string("ALIPAY|BALANCE"))},
    {"amount", boost::any(string("1.23"))},
    {"payChannelOrderNo", boost::any(string("20211234"))},
    {"promotionAmount", boost::any(string("0.00"))},
    {"fundToolDetailList", boost::any(vector<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequestPayChannelDetailListFundToolDetailList>({
      payChannelDetailList0FundToolDetailList0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequest> notifyPayCodePayResultRequest = make_shared<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequest>(map<string, boost::any>({
    {"payCode", boost::any(string("26123xxx"))},
    {"corpId", boost::any(string("ding1234"))},
    {"userId", boost::any(string("userId1234"))},
    {"gmtTradeCreate", boost::any(string("2021-01-01 11:11:11"))},
    {"gmtTradeFinish", boost::any(string("2021-01-01 11:11:11"))},
    {"tradeNo", boost::any(string("202101012345678"))},
    {"tradeStatus", boost::any(string("SUCCESS"))},
    {"title", boost::any(string("晚餐100.0元"))},
    {"remark", boost::any(string("备注"))},
    {"amount", boost::any(string("1234.56"))},
    {"promotionAmount", boost::any(string("1.23"))},
    {"chargeAmount", boost::any(string("1.00"))},
    {"payChannelDetailList", boost::any(vector<Alibabacloud_Dingtalkfinance_1_0::NotifyPayCodePayResultRequestPayChannelDetailList>({
      payChannelDetailList0
    }))},
    {"tradeErrorCode", boost::any(string("BALANCE_NOT_ENOUGH"))},
    {"tradeErrorMsg", boost::any(string("余额不足，请充值"))},
    {"extInfo", boost::any(string("{ "akey": "avalue“}"))},
    {"merchantName", boost::any(string("merchantName"))}
  }));
  try {
    client->notifyPayCodePayResultWithOptions(notifyPayCodePayResultRequest, notifyPayCodePayResultHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | String | 处理结果，取值：   - **SUCCESS**：成功 - **FAIL**：失败 |

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
| 500 | unknownError | 未知错误 | 未知错误 |
