---
title: "数据集成奖励信息删除"
source_url: "https://open.dingtalk.com/document/development/api-hrbraindeleteawardrecords"
namespace: "development"
slug: "api-hrbraindeleteawardrecords"
group: "应用开发"
tab: "服务端API"
breadcrumb: "组织大脑 > 数据集成 > 绩效与奖惩 > 数据集成奖励信息删除"
doc_id: "CtF2AUoZYr"
updated_at: "2026-06-02 19:31:20"
---

> Source: https://open.dingtalk.com/document/development/api-hrbraindeleteawardrecords
> Path: 应用开发 / 服务端API / 组织大脑 > 数据集成 > 绩效与奖惩 > 数据集成奖励信息删除
> Updated: 2026-06-02 19:31:20

# 数据集成奖励信息删除

调用本接口，删除已同步至组织大脑的奖励记录，支持批量删除。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/awardRecords/remove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Hrbrain.Import.Write-组织大脑数据集成写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| params | Array | 否 | 参数组。 |
| awardDate | String | 否 | 奖励颁发日期。 |
| awardName | String | 否 | 奖励名称。 |
| workNo | String | 是 | 钉钉 UserId。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/awardRecords/remove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:480021443f9f37fcbf464c4a6b85d299
Content-Type:application/json

{
  "params" : [ {
    "awardDate" : "2024-10-10",
    "awardName" : "奖励名称",
    "workNo" : "123456789"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainDeleteAwardRecordsHeaders hrbrainDeleteAwardRecordsHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainDeleteAwardRecordsHeaders();
        hrbrainDeleteAwardRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainDeleteAwardRecordsRequest.HrbrainDeleteAwardRecordsRequestParams params0 = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainDeleteAwardRecordsRequest.HrbrainDeleteAwardRecordsRequestParams()
                .setAwardDate("2024-10-10")
                .setAwardName("奖励名称")
                .setWorkNo("123456789");
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainDeleteAwardRecordsRequest hrbrainDeleteAwardRecordsRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainDeleteAwardRecordsRequest()
                .setParams(java.util.Arrays.asList(
                    params0
                ));
        try {
            client.hrbrainDeleteAwardRecordsWithOptions(hrbrainDeleteAwardRecordsRequest, hrbrainDeleteAwardRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from typing import List

from alibabacloud_dingtalk.hrbrain_1_0.client import Client as dingtalkhrbrain_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrbrain_1_0 import models as dingtalkhrbrain__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrbrain_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrbrain_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_delete_award_records_headers = dingtalkhrbrain__1__0_models.HrbrainDeleteAwardRecordsHeaders()
        hrbrain_delete_award_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        params_0 = dingtalkhrbrain__1__0_models.HrbrainDeleteAwardRecordsRequestParams(
            award_date='2024-10-10',
            award_name='奖励名称',
            work_no='123456789'
        )
        hrbrain_delete_award_records_request = dingtalkhrbrain__1__0_models.HrbrainDeleteAwardRecordsRequest(
            params=[
                params_0
            ]
        )
        try:
            client.hrbrain_delete_award_records_with_options(hrbrain_delete_award_records_request, hrbrain_delete_award_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_delete_award_records_headers = dingtalkhrbrain__1__0_models.HrbrainDeleteAwardRecordsHeaders()
        hrbrain_delete_award_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        params_0 = dingtalkhrbrain__1__0_models.HrbrainDeleteAwardRecordsRequestParams(
            award_date='2024-10-10',
            award_name='奖励名称',
            work_no='123456789'
        )
        hrbrain_delete_award_records_request = dingtalkhrbrain__1__0_models.HrbrainDeleteAwardRecordsRequest(
            params=[
                params_0
            ]
        )
        try:
            await client.hrbrain_delete_award_records_with_options_async(hrbrain_delete_award_records_request, hrbrain_delete_award_records_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainDeleteAwardRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainDeleteAwardRecordsRequest\params;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainDeleteAwardRecordsRequest;
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
        $hrbrainDeleteAwardRecordsHeaders = new HrbrainDeleteAwardRecordsHeaders([]);
        $hrbrainDeleteAwardRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $params0 = new params([
            "awardDate" => "2024-10-10",
            "awardName" => "奖励名称",
            "workNo" => "123456789"
        ]);
        $hrbrainDeleteAwardRecordsRequest = new HrbrainDeleteAwardRecordsRequest([
            "params" => [
                $params0
            ]
        ]);
        try {
            $client->hrbrainDeleteAwardRecordsWithOptions($hrbrainDeleteAwardRecordsRequest, $hrbrainDeleteAwardRecordsHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkhrbrain_1_0  "github.com/alibabacloud-go/dingtalk/hrbrain_1_0"
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
func CreateClient () (_result *dingtalkhrbrain_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrbrain_1_0.Client{}
  _result, _err = dingtalkhrbrain_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrbrainDeleteAwardRecordsHeaders := &dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsHeaders{}
  hrbrainDeleteAwardRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  params0 := &dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsRequestParams{
    AwardDate: tea.String("2024-10-10"),
    AwardName: tea.String("奖励名称"),
    WorkNo: tea.String("123456789"),
  }
  hrbrainDeleteAwardRecordsRequest := &dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsRequest{
    Params: []*dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsRequestParams{params0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainDeleteAwardRecordsWithOptions(hrbrainDeleteAwardRecordsRequest, hrbrainDeleteAwardRecordsHeaders, &util.RuntimeOptions{})
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
const dingtalkhrbrain_1_0 = require('@alicloud/dingtalk/hrbrain_1_0');
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
    return new dingtalkhrbrain_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let hrbrainDeleteAwardRecordsHeaders = new dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsHeaders({ });
    hrbrainDeleteAwardRecordsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let params0 = new dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsRequestParams({
      awardDate: '2024-10-10',
      awardName: '奖励名称',
      workNo: '123456789',
    });
    let hrbrainDeleteAwardRecordsRequest = new dingtalkhrbrain_1_0.HrbrainDeleteAwardRecordsRequest({
      params: [
        params0
      ],
    });
    try {
      await client.hrbrainDeleteAwardRecordsWithOptions(hrbrainDeleteAwardRecordsRequest, hrbrainDeleteAwardRecordsHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsHeaders hrbrainDeleteAwardRecordsHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsHeaders();
            hrbrainDeleteAwardRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsRequest.HrbrainDeleteAwardRecordsRequestParams params0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsRequest.HrbrainDeleteAwardRecordsRequestParams
            {
                AwardDate = "2024-10-10",
                AwardName = "奖励名称",
                WorkNo = "123456789",
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsRequest hrbrainDeleteAwardRecordsRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsRequest
            {
                Params = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainDeleteAwardRecordsRequest.HrbrainDeleteAwardRecordsRequestParams>
                {
                    params0
                },
            };
            try
            {
                client.HrbrainDeleteAwardRecordsWithOptions(hrbrainDeleteAwardRecordsRequest, hrbrainDeleteAwardRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| requestId | String | 请求 ID。 |
| success | Boolean | 接口调用是否成功。 |
| result | Boolean | 删除是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "480021443f9f37fcbf464c4a6b85d299",
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illegal. %s | 入参错误 |
