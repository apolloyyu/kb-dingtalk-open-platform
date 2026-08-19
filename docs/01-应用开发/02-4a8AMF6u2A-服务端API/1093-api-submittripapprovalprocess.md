---
title: "提交差旅出差申请单"
source_url: "https://open.dingtalk.com/document/development/api-submittripapprovalprocess"
namespace: "development"
slug: "api-submittripapprovalprocess"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 差旅 > 提交差旅出差申请单"
doc_id: "tEgqHNObcH"
updated_at: "2026-08-07 11:40:59"
---

> Source: https://open.dingtalk.com/document/development/api-submittripapprovalprocess
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 差旅 > 提交差旅出差申请单
> Updated: 2026-08-07 11:40:59

# 提交差旅出差申请单

调用本接口，提交差旅出差申请单。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/trip/approvals |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Trip.MainData.Write-智能差旅审批单主数据写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 员工ID。 |
| reason | String | 否 | 出差事由。 |
| processCode | String | 否 | 审批单模板code。 |
| itineraries | Array | 否 | 日程信息。 |
| vehicle | String | 否 | 出行方式：   - **火车** - **汽车** - **飞机** - **其他** |
| singleOrReturn | String | 否 | - **单程** - **往返** |
| placeOfDeparture | String | 否 | 出发地，城市中文 例如 杭州 |
| placeOfDepartureDetail | String | 否 | 汽车或其他交通工具使用，出发地详细地址。 |
| destination | String | 否 | 目的地，例如杭州。 |
| destinationDetail | String | 否 | 汽车或其他交通工具使用，目的地详细地址。 |
| departureTime | String | 否 | 触出发时间，格式：yyyy-MM-dd HH:mm。 |
| returnTime | String | 否 | 到达时间，格式：yyyy-MM-dd HH:mm。 |

### **请求示例**

HTTP

```
POST /v1.0/trip/approvals HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:abc
Content-Type:application/json

{
  "userId" : "5046195764756652",
  "reason" : "拜访客户",
  "processCode" : "PROC_XXXX",
  "itineraries" : [ {
    "vehicle" : "飞机",
    "singleOrReturn" : "单程",
    "placeOfDeparture" : "杭州",
    "placeOfDepartureDetail" : "余杭区文xxxx号",
    "destination" : "北京",
    "destinationDetail" : "望京xxxx园区",
    "departureTime" : "2026-01-20 09:00",
    "returnTime" : "2026-01-22 09:00"
  } ]
}
```

Java

```
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalktrip_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktrip_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalktrip_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalktrip_1_0.models.SubmitTripApprovalProcessHeaders submitTripApprovalProcessHeaders = new com.aliyun.dingtalktrip_1_0.models.SubmitTripApprovalProcessHeaders();
        submitTripApprovalProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalktrip_1_0.models.SubmitTripApprovalProcessRequest.SubmitTripApprovalProcessRequestItineraries itineraries0 = new com.aliyun.dingtalktrip_1_0.models.SubmitTripApprovalProcessRequest.SubmitTripApprovalProcessRequestItineraries()
                .setVehicle("飞机")
                .setSingleOrReturn("单程")
                .setPlaceOfDeparture("杭州")
                .setPlaceOfDepartureDetail("余杭区文xxxx号")
                .setDestination("北京")
                .setDestinationDetail("望京xxxx园区")
                .setDepartureTime("2026-01-20 09:00")
                .setReturnTime("2026-01-22 09:00");
        com.aliyun.dingtalktrip_1_0.models.SubmitTripApprovalProcessRequest submitTripApprovalProcessRequest = new com.aliyun.dingtalktrip_1_0.models.SubmitTripApprovalProcessRequest()
                .setUserId("5046195764756652")
                .setReason("拜访客户")
                .setProcessCode("PROC_XXXX")
                .setItineraries(java.util.Arrays.asList(
                    itineraries0
                ));
        try {
            client.submitTripApprovalProcessWithOptions(submitTripApprovalProcessRequest, submitTripApprovalProcessHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys
import json

from typing import List

from alibabacloud_dingtalk.trip_1_0.client import Client as dingtalktrip_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.trip_1_0 import models as dingtalktrip__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalktrip_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalktrip_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        submit_trip_approval_process_headers = dingtalktrip__1__0_models.SubmitTripApprovalProcessHeaders()
        submit_trip_approval_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        itineraries_0 = dingtalktrip__1__0_models.SubmitTripApprovalProcessRequestItineraries(
            vehicle='飞机',
            single_or_return='单程',
            place_of_departure='杭州',
            place_of_departure_detail='余杭区文xxxx号',
            destination='北京',
            destination_detail='望京xxxx园区',
            departure_time='2026-01-20 09:00',
            return_time='2026-01-22 09:00'
        )
        submit_trip_approval_process_request = dingtalktrip__1__0_models.SubmitTripApprovalProcessRequest(
            user_id='5046195764756652',
            reason='拜访客户',
            process_code='PROC_XXXX',
            itineraries=[
                itineraries_0
            ]
        )
        try:
            client.submit_trip_approval_process_with_options(submit_trip_approval_process_request, submit_trip_approval_process_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        submit_trip_approval_process_headers = dingtalktrip__1__0_models.SubmitTripApprovalProcessHeaders()
        submit_trip_approval_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        itineraries_0 = dingtalktrip__1__0_models.SubmitTripApprovalProcessRequestItineraries(
            vehicle='飞机',
            single_or_return='单程',
            place_of_departure='杭州',
            place_of_departure_detail='余杭区文xxxx号',
            destination='北京',
            destination_detail='望京xxxx园区',
            departure_time='2026-01-20 09:00',
            return_time='2026-01-22 09:00'
        )
        submit_trip_approval_process_request = dingtalktrip__1__0_models.SubmitTripApprovalProcessRequest(
            user_id='5046195764756652',
            reason='拜访客户',
            process_code='PROC_XXXX',
            itineraries=[
                itineraries_0
            ]
        )
        try:
            await client.submit_trip_approval_process_with_options_async(submit_trip_approval_process_request, submit_trip_approval_process_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vtrip_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vtrip_1_0\Models\SubmitTripApprovalProcessHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtrip_1_0\Models\SubmitTripApprovalProcessRequest\itineraries;
use AlibabaCloud\SDK\Dingtalk\Vtrip_1_0\Models\SubmitTripApprovalProcessRequest;
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
        $submitTripApprovalProcessHeaders = new SubmitTripApprovalProcessHeaders([]);
        $submitTripApprovalProcessHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $itineraries0 = new itineraries([
            "vehicle" => "飞机",
            "singleOrReturn" => "单程",
            "placeOfDeparture" => "杭州",
            "placeOfDepartureDetail" => "余杭区文xxxx号",
            "destination" => "北京",
            "destinationDetail" => "望京xxxx园区",
            "departureTime" => "2026-01-20 09:00",
            "returnTime" => "2026-01-22 09:00"
        ]);
        $submitTripApprovalProcessRequest = new SubmitTripApprovalProcessRequest([
            "userId" => "5046195764756652",
            "reason" => "拜访客户",
            "processCode" => "PROC_XXXX",
            "itineraries" => [
                $itineraries0
            ]
        ]);
        try {
            $client->submitTripApprovalProcessWithOptions($submitTripApprovalProcessRequest, $submitTripApprovalProcessHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalktrip_1_0  "github.com/alibabacloud-go/dingtalk/trip_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalktrip_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalktrip_1_0.Client{}
  _result, _err = dingtalktrip_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  submitTripApprovalProcessHeaders := &dingtalktrip_1_0.SubmitTripApprovalProcessHeaders{}
  submitTripApprovalProcessHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  itineraries0 := &dingtalktrip_1_0.SubmitTripApprovalProcessRequestItineraries{
    Vehicle: tea.String("飞机"),
    SingleOrReturn: tea.String("单程"),
    PlaceOfDeparture: tea.String("杭州"),
    PlaceOfDepartureDetail: tea.String("余杭区文xxxx号"),
    Destination: tea.String("北京"),
    DestinationDetail: tea.String("望京xxxx园区"),
    DepartureTime: tea.String("2026-01-20 09:00"),
    ReturnTime: tea.String("2026-01-22 09:00"),
  }
  submitTripApprovalProcessRequest := &dingtalktrip_1_0.SubmitTripApprovalProcessRequest{
    UserId: tea.String("5046195764756652"),
    Reason: tea.String("拜访客户"),
    ProcessCode: tea.String("PROC_XXXX"),
    Itineraries: []*dingtalktrip_1_0.SubmitTripApprovalProcessRequestItineraries{itineraries0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SubmitTripApprovalProcessWithOptions(submitTripApprovalProcessRequest, submitTripApprovalProcessHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalktrip_1_0 = require('@alicloud/dingtalk/trip_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalktrip_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let submitTripApprovalProcessHeaders = new dingtalktrip_1_0.SubmitTripApprovalProcessHeaders({ });
    submitTripApprovalProcessHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let itineraries0 = new dingtalktrip_1_0.SubmitTripApprovalProcessRequestItineraries({
      vehicle: '飞机',
      singleOrReturn: '单程',
      placeOfDeparture: '杭州',
      placeOfDepartureDetail: '余杭区文xxxx号',
      destination: '北京',
      destinationDetail: '望京xxxx园区',
      departureTime: '2026-01-20 09:00',
      returnTime: '2026-01-22 09:00',
    });
    let submitTripApprovalProcessRequest = new dingtalktrip_1_0.SubmitTripApprovalProcessRequest({
      userId: '5046195764756652',
      reason: '拜访客户',
      processCode: 'PROC_XXXX',
      itineraries: [
        itineraries0
      ],
    });
    try {
      await client.submitTripApprovalProcessWithOptions(submitTripApprovalProcessRequest, submitTripApprovalProcessHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
Client.main(process.argv.slice(2));
```

C#

```
using Newtonsoft.Json;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalktrip_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalktrip_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalktrip_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessHeaders submitTripApprovalProcessHeaders = new AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessHeaders();
            submitTripApprovalProcessHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessRequest.SubmitTripApprovalProcessRequestItineraries itineraries0 = new AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessRequest.SubmitTripApprovalProcessRequestItineraries
            {
                Vehicle = "飞机",
                SingleOrReturn = "单程",
                PlaceOfDeparture = "杭州",
                PlaceOfDepartureDetail = "余杭区文xxxx号",
                Destination = "北京",
                DestinationDetail = "望京xxxx园区",
                DepartureTime = "2026-01-20 09:00",
                ReturnTime = "2026-01-22 09:00",
            };
            AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessRequest submitTripApprovalProcessRequest = new AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessRequest
            {
                UserId = "5046195764756652",
                Reason = "拜访客户",
                ProcessCode = "PROC_XXXX",
                Itineraries = new List<AlibabaCloud.SDK.Dingtalktrip_1_0.Models.SubmitTripApprovalProcessRequest.SubmitTripApprovalProcessRequestItineraries>
                {
                    itineraries0
                },
            };
            try
            {
                client.SubmitTripApprovalProcessWithOptions(submitTripApprovalProcessRequest, submitTripApprovalProcessHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| instanceId | String | Id of the request |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "instanceId" : "abc"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | %s | 参数错误 |
| 400 | user.notExist | %s | 无法找到用户 |
| 400 | emp.notFound | %s | 无法找到员工信息 |
