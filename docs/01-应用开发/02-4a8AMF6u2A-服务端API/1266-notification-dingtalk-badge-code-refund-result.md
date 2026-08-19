---
title: "通知退款结果"
source_url: "https://open.dingtalk.com/document/development/notification-dingtalk-badge-code-refund-result"
namespace: "development"
slug: "notification-dingtalk-badge-code-refund-result"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 通知退款结果"
doc_id: "ZVlykdzN9D"
updated_at: "2025-09-11 21:03:36"
---

> Source: https://open.dingtalk.com/document/development/notification-dingtalk-badge-code-refund-result
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 通知退款结果
> Updated: 2025-09-11 21:03:36

# 通知退款结果

调用本接口，同步退款结果，生成对应账单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/badge/codes/refundResults |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Badge.Common.Write-钉工牌基础数据写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业corpId。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/)首页查看。 |
| userId | String | 是 | 用户userId，需要与生成码时使用的**userId**保持一致。 |
| tradeNo | String | 是 | 交易订单号，自定义，接入方针对交易生成的唯一订单号。 |
| refundOrderNo | String | 是 | 本次退款订单号，自定义，接入方针对交易生成的唯一退款订单号。 |
| remark | String | 是 | 备注。 |
| refundAmount | String | 是 | 退款金额。 |
| refundPromotionAmount | String | 是 | 退款的优惠金额。 |
| gmtRefund | String | 是 | 退款时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| payChannelDetailList | Array | 是 | 支付渠道明细信息。 |
| payChannelName | String | 是 | 支付渠道名称。 |
| payChannelType | String | 是 | 支付渠道类型，取值：   - **ALIPAY**：支付宝 - **BALANCE**：余额 |
| amount | String | 是 | 金额。 |
| payChannelOrderNo | String | 是 | 支付渠道号，调用方接入的支付渠道的单号。 |
| payChannelRefundOrderNo | String | 是 | 支付渠道退款号，调用方接入的支付渠道的退款单号。 |
| promotionAmount | String | 是 | 优惠金额。 |
| fundToolDetailList | Array | 是 | 支付资金列表。 |
| fundToolName | String | 是 | 资金工具名称。 |
| amount | String | 是 | 金额。 |
| gmtCreate | String | 是 | 创建时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| gmtFinish | String | 是 | 完成时间。  格式：yyyy-MM-dd HH:mm:ss。 |
| promotionFundTool | Boolean | 是 | 是否是优惠工具。   - **true**：是 - **false**：不是 |
| extInfo | String | 否 | 扩展信息。 |
| payCode | String | 是 | 支付时使用的付款码。 |

### 请求示例

HTTP

```
POST /v1.0/badge/codes/refundResults HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "corpId" : "ding1234",
  "userId" : "userId",
  "tradeNo" : "tradeNo",
  "refundOrderNo" : "refundOrderNo",
  "remark" : "晚餐退款",
  "refundAmount" : "1.00",
  "refundPromotionAmount" : "0.00",
  "gmtRefund" : "2021-11-11 11:11:11",
  "payChannelDetailList" : [ {
    "payChannelName" : "ALIPAY",
    "payChannelType" : "ALIPAY",
    "amount" : "1.00",
    "payChannelOrderNo" : "20210531123456",
    "payChannelRefundOrderNo" : "2021053112345678",
    "promotionAmount" : "0.00",
    "fundToolDetailList" : [ {
      "fundToolName" : "余额",
      "amount" : "1.00",
      "gmtCreate" : "2021-05-31 11:11:11",
      "gmtFinish" : "2021-05-31 11:11:11",
      "promotionFundTool" : true,
      "extInfo" : "{\"key\":\"value\"}"
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
import com.aliyun.dingtalkbadge_1_0.*;
import com.aliyun.dingtalkbadge_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkbadge_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkbadge_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkbadge_1_0.Client client = Sample.createClient();
        NotifyBadgeCodeRefundResultHeaders notifyBadgeCodeRefundResultHeaders = new NotifyBadgeCodeRefundResultHeaders();
        notifyBadgeCodeRefundResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
        NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList payChannelDetailList0FundToolDetailList0 = new NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList()
                .setFundToolName("余额")
                .setAmount("1.00")
                .setGmtCreate("2021-05-31 11:11:11")
                .setGmtFinish("2021-05-31 11:11:11")
                .setPromotionFundTool(true)
                .setExtInfo("{\"key\":\"value\"}");
        NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList payChannelDetailList0 = new NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList()
                .setPayChannelName("ALIPAY")
                .setPayChannelType("ALIPAY")
                .setAmount("1.00")
                .setPayChannelOrderNo("20210531123456")
                .setPayChannelRefundOrderNo("2021053112345678")
                .setPromotionAmount("0.00")
                .setFundToolDetailList(java.util.Arrays.asList(
                    payChannelDetailList0FundToolDetailList0
                ));
        NotifyBadgeCodeRefundResultRequest notifyBadgeCodeRefundResultRequest = new NotifyBadgeCodeRefundResultRequest()
                .setCorpId("ding1234")
                .setUserId("userId")
                .setTradeNo("tradeNo")
                .setRefundOrderNo("refundOrderNo")
                .setRemark("晚餐退款")
                .setRefundAmount("1.00")
                .setRefundPromotionAmount("0.00")
                .setGmtRefund("2021-11-11 11:11:11")
                .setPayChannelDetailList(java.util.Arrays.asList(
                    payChannelDetailList0
                ))
                .setPayCode("payCode");
        try {
            client.notifyBadgeCodeRefundResultWithOptions(notifyBadgeCodeRefundResultRequest, notifyBadgeCodeRefundResultHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.badge_1_0.client import Client as dingtalkbadge_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.badge_1_0 import models as dingtalkbadge__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkbadge_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkbadge_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_badge_code_refund_result_headers = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultHeaders()
        notify_badge_code_refund_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        pay_channel_detail_list_0fund_tool_detail_list_0 = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList(
            fund_tool_name='余额',
            amount='1.00',
            gmt_create='2021-05-31 11:11:11',
            gmt_finish='2021-05-31 11:11:11',
            promotion_fund_tool=True,
            ext_info='{"key":"value"}'
        )
        pay_channel_detail_list_0 = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequestPayChannelDetailList(
            pay_channel_name='ALIPAY',
            pay_channel_type='ALIPAY',
            amount='1.00',
            pay_channel_order_no='20210531123456',
            pay_channel_refund_order_no='2021053112345678',
            promotion_amount='0.00',
            fund_tool_detail_list=[
                pay_channel_detail_list_0fund_tool_detail_list_0
            ]
        )
        notify_badge_code_refund_result_request = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequest(
            corp_id='ding1234',
            user_id='userId',
            trade_no='tradeNo',
            refund_order_no='refundOrderNo',
            remark='晚餐退款',
            refund_amount='1.00',
            refund_promotion_amount='0.00',
            gmt_refund='2021-11-11 11:11:11',
            pay_channel_detail_list=[
                pay_channel_detail_list_0
            ],
            pay_code='payCode'
        )
        try:
            client.notify_badge_code_refund_result_with_options(notify_badge_code_refund_result_request, notify_badge_code_refund_result_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_badge_code_refund_result_headers = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultHeaders()
        notify_badge_code_refund_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        pay_channel_detail_list_0fund_tool_detail_list_0 = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList(
            fund_tool_name='余额',
            amount='1.00',
            gmt_create='2021-05-31 11:11:11',
            gmt_finish='2021-05-31 11:11:11',
            promotion_fund_tool=True,
            ext_info='{"key":"value"}'
        )
        pay_channel_detail_list_0 = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequestPayChannelDetailList(
            pay_channel_name='ALIPAY',
            pay_channel_type='ALIPAY',
            amount='1.00',
            pay_channel_order_no='20210531123456',
            pay_channel_refund_order_no='2021053112345678',
            promotion_amount='0.00',
            fund_tool_detail_list=[
                pay_channel_detail_list_0fund_tool_detail_list_0
            ]
        )
        notify_badge_code_refund_result_request = dingtalkbadge__1__0_models.NotifyBadgeCodeRefundResultRequest(
            corp_id='ding1234',
            user_id='userId',
            trade_no='tradeNo',
            refund_order_no='refundOrderNo',
            remark='晚餐退款',
            refund_amount='1.00',
            refund_promotion_amount='0.00',
            gmt_refund='2021-11-11 11:11:11',
            pay_channel_detail_list=[
                pay_channel_detail_list_0
            ],
            pay_code='payCode'
        )
        try:
            await client.notify_badge_code_refund_result_with_options_async(notify_badge_code_refund_result_request, notify_badge_code_refund_result_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\NotifyBadgeCodeRefundResultHeaders;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\NotifyBadgeCodeRefundResultRequest\payChannelDetailList\fundToolDetailList;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\NotifyBadgeCodeRefundResultRequest\payChannelDetailList;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\NotifyBadgeCodeRefundResultRequest;
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
        $notifyBadgeCodeRefundResultHeaders = new NotifyBadgeCodeRefundResultHeaders([]);
        $notifyBadgeCodeRefundResultHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $payChannelDetailList0FundToolDetailList0 = new fundToolDetailList([
            "fundToolName" => "余额",
            "amount" => "1.00",
            "gmtCreate" => "2021-05-31 11:11:11",
            "gmtFinish" => "2021-05-31 11:11:11",
            "promotionFundTool" => true,
            "extInfo" => "{\"key\":\"value\"}"
        ]);
        $payChannelDetailList0 = new payChannelDetailList([
            "payChannelName" => "ALIPAY",
            "payChannelType" => "ALIPAY",
            "amount" => "1.00",
            "payChannelOrderNo" => "20210531123456",
            "payChannelRefundOrderNo" => "2021053112345678",
            "promotionAmount" => "0.00",
            "fundToolDetailList" => [
                $payChannelDetailList0FundToolDetailList0
            ]
        ]);
        $notifyBadgeCodeRefundResultRequest = new NotifyBadgeCodeRefundResultRequest([
            "corpId" => "ding1234",
            "userId" => "userId",
            "tradeNo" => "tradeNo",
            "refundOrderNo" => "refundOrderNo",
            "remark" => "晚餐退款",
            "refundAmount" => "1.00",
            "refundPromotionAmount" => "0.00",
            "gmtRefund" => "2021-11-11 11:11:11",
            "payChannelDetailList" => [
                $payChannelDetailList0
            ],
            "payCode" => "payCode"
        ]);
        try {
            $client->notifyBadgeCodeRefundResultWithOptions($notifyBadgeCodeRefundResultRequest, $notifyBadgeCodeRefundResultHeaders, new RuntimeOptions([]));
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
  dingtalkbadge_1_0  "github.com/alibabacloud-go/dingtalk/badge_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkbadge_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkbadge_1_0.Client{}
  _result, _err = dingtalkbadge_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  notifyBadgeCodeRefundResultHeaders := &dingtalkbadge_1_0.NotifyBadgeCodeRefundResultHeaders{}
  notifyBadgeCodeRefundResultHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  payChannelDetailList0FundToolDetailList0 := &dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList{
    FundToolName: tea.String("余额"),
    Amount: tea.String("1.00"),
    GmtCreate: tea.String("2021-05-31 11:11:11"),
    GmtFinish: tea.String("2021-05-31 11:11:11"),
    PromotionFundTool: tea.Bool(true),
    ExtInfo: tea.String("{\"key\":\"value\"}"),
  }
  payChannelDetailList0 := &dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequestPayChannelDetailList{
    PayChannelName: tea.String("ALIPAY"),
    PayChannelType: tea.String("ALIPAY"),
    Amount: tea.String("1.00"),
    PayChannelOrderNo: tea.String("20210531123456"),
    PayChannelRefundOrderNo: tea.String("2021053112345678"),
    PromotionAmount: tea.String("0.00"),
    FundToolDetailList: []*dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList{payChannelDetailList0FundToolDetailList0},
  }
  notifyBadgeCodeRefundResultRequest := &dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequest{
    CorpId: tea.String("ding1234"),
    UserId: tea.String("userId"),
    TradeNo: tea.String("tradeNo"),
    RefundOrderNo: tea.String("refundOrderNo"),
    Remark: tea.String("晚餐退款"),
    RefundAmount: tea.String("1.00"),
    RefundPromotionAmount: tea.String("0.00"),
    GmtRefund: tea.String("2021-11-11 11:11:11"),
    PayChannelDetailList: []*dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequestPayChannelDetailList{payChannelDetailList0},
    PayCode: tea.String("payCode"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.NotifyBadgeCodeRefundResultWithOptions(notifyBadgeCodeRefundResultRequest, notifyBadgeCodeRefundResultHeaders, &util.RuntimeOptions{})
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
import dingtalkbadge_1_0, * as $dingtalkbadge_1_0 from '@alicloud/dingtalk/badge_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkbadge_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkbadge_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let notifyBadgeCodeRefundResultHeaders = new $dingtalkbadge_1_0.NotifyBadgeCodeRefundResultHeaders({ });
    notifyBadgeCodeRefundResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let payChannelDetailList0FundToolDetailList0 = new $dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList({
      fundToolName: "余额",
      amount: "1.00",
      gmtCreate: "2021-05-31 11:11:11",
      gmtFinish: "2021-05-31 11:11:11",
      promotionFundTool: true,
      extInfo: "{\"key\":\"value\"}",
    });
    let payChannelDetailList0 = new $dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequestPayChannelDetailList({
      payChannelName: "ALIPAY",
      payChannelType: "ALIPAY",
      amount: "1.00",
      payChannelOrderNo: "20210531123456",
      payChannelRefundOrderNo: "2021053112345678",
      promotionAmount: "0.00",
      fundToolDetailList: [
        payChannelDetailList0FundToolDetailList0
      ],
    });
    let notifyBadgeCodeRefundResultRequest = new $dingtalkbadge_1_0.NotifyBadgeCodeRefundResultRequest({
      corpId: "ding1234",
      userId: "userId",
      tradeNo: "tradeNo",
      refundOrderNo: "refundOrderNo",
      remark: "晚餐退款",
      refundAmount: "1.00",
      refundPromotionAmount: "0.00",
      gmtRefund: "2021-11-11 11:11:11",
      payChannelDetailList: [
        payChannelDetailList0
      ],
      payCode: "payCode",
    });
    try {
      await client.notifyBadgeCodeRefundResultWithOptions(notifyBadgeCodeRefundResultRequest, notifyBadgeCodeRefundResultHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkbadge_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkbadge_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultHeaders notifyBadgeCodeRefundResultHeaders = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultHeaders();
            notifyBadgeCodeRefundResultHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList payChannelDetailList0FundToolDetailList0 = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList
            {
                FundToolName = "余额",
                Amount = "1.00",
                GmtCreate = "2021-05-31 11:11:11",
                GmtFinish = "2021-05-31 11:11:11",
                PromotionFundTool = true,
                ExtInfo = "{\"key\":\"value\"}",
            };
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList payChannelDetailList0 = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList
            {
                PayChannelName = "ALIPAY",
                PayChannelType = "ALIPAY",
                Amount = "1.00",
                PayChannelOrderNo = "20210531123456",
                PayChannelRefundOrderNo = "2021053112345678",
                PromotionAmount = "0.00",
                FundToolDetailList = new List<AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList.NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList>
                {
                    payChannelDetailList0FundToolDetailList0
                },
            };
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest notifyBadgeCodeRefundResultRequest = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest
            {
                CorpId = "ding1234",
                UserId = "userId",
                TradeNo = "tradeNo",
                RefundOrderNo = "refundOrderNo",
                Remark = "晚餐退款",
                RefundAmount = "1.00",
                RefundPromotionAmount = "0.00",
                GmtRefund = "2021-11-11 11:11:11",
                PayChannelDetailList = new List<AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeRefundResultRequest.NotifyBadgeCodeRefundResultRequestPayChannelDetailList>
                {
                    payChannelDetailList0
                },
                PayCode = "payCode",
            };
            try
            {
                client.NotifyBadgeCodeRefundResultWithOptions(notifyBadgeCodeRefundResultRequest, notifyBadgeCodeRefundResultHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkbadge__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkbadge_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkbadge_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::Client> client = make_shared<Alibabacloud_Dingtalkbadge_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultHeaders> notifyBadgeCodeRefundResultHeaders = make_shared<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultHeaders>();
  notifyBadgeCodeRefundResultHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList> payChannelDetailList0FundToolDetailList0 = make_shared<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList>(map<string, boost::any>({
    {"fundToolName", boost::any(string("余额"))},
    {"amount", boost::any(string("1.00"))},
    {"gmtCreate", boost::any(string("2021-05-31 11:11:11"))},
    {"gmtFinish", boost::any(string("2021-05-31 11:11:11"))},
    {"promotionFundTool", boost::any(true)},
    {"extInfo", boost::any(string("{"key":"value"}"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequestPayChannelDetailList> payChannelDetailList0 = make_shared<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequestPayChannelDetailList>(map<string, boost::any>({
    {"payChannelName", boost::any(string("ALIPAY"))},
    {"payChannelType", boost::any(string("ALIPAY"))},
    {"amount", boost::any(string("1.00"))},
    {"payChannelOrderNo", boost::any(string("20210531123456"))},
    {"payChannelRefundOrderNo", boost::any(string("2021053112345678"))},
    {"promotionAmount", boost::any(string("0.00"))},
    {"fundToolDetailList", boost::any(vector<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequestPayChannelDetailListFundToolDetailList>({
      payChannelDetailList0FundToolDetailList0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequest> notifyBadgeCodeRefundResultRequest = make_shared<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding1234"))},
    {"userId", boost::any(string("userId"))},
    {"tradeNo", boost::any(string("tradeNo"))},
    {"refundOrderNo", boost::any(string("refundOrderNo"))},
    {"remark", boost::any(string("晚餐退款"))},
    {"refundAmount", boost::any(string("1.00"))},
    {"refundPromotionAmount", boost::any(string("0.00"))},
    {"gmtRefund", boost::any(string("2021-11-11 11:11:11"))},
    {"payChannelDetailList", boost::any(vector<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeRefundResultRequestPayChannelDetailList>({
      payChannelDetailList0
    }))},
    {"payCode", boost::any(string("payCode"))}
  }));
  try {
    client->notifyBadgeCodeRefundResultWithOptions(notifyBadgeCodeRefundResultRequest, notifyBadgeCodeRefundResultHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
