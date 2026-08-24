---
title: "获取人脸对比接口调用记录"
source_url: "https://open.dingtalk.com/document/development/you-can-call-this-operation-to-query-the-call-records"
namespace: "development"
slug: "you-can-call-this-operation-to-query-the-call-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 获取人脸对比接口调用记录"
doc_id: "esQ6obvUzK"
updated_at: "2026-06-02 19:19:57"
---

> Source: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-query-the-call-records
> Path: 应用开发 / 服务端API / 专属钉钉 > 获取人脸对比接口调用记录
> Updated: 2026-06-02 19:19:57

# 获取人脸对比接口调用记录

用于获取人脸对比接口调用记录。调用时通过 POST 请求提交 fromTime、toTime、agentId、userIds、nextToken、maxResults 等业务字段。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/faces/recognizeRecords/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.Ding.Face.Recognize-专属钉钉人脸识别权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| fromTime | Long | 否 | 记录开始时间戳，单位毫秒。 |
| toTime | Long | 否 | 记录结束时间戳，单位毫秒。 |
| agentId | Long | 否 | 应用唯一标识。 |
| userIds | Array of String | 否 | 员工userId列表。 |
| nextToken | Long | 是 | 分页游标，从0开始。 |
| maxResults | Integer | 是 | 每页最大条目数，最大50。 |
| faceCompareResult | Integer | 否 | 人脸对比结果。   - 1：成功 - 2：失败 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/faces/recognizeRecords/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "fromTime" : 1667000000,
  "toTime" : 1669000000,
  "agentId" : 123333,
  "userIds" : [ "123" ],
  "nextToken" : 0,
  "maxResults" : 10,
  "faceCompareResult" : 1
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.GetRecognizeRecordsHeaders getRecognizeRecordsHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetRecognizeRecordsHeaders();
        getRecognizeRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetRecognizeRecordsRequest getRecognizeRecordsRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetRecognizeRecordsRequest()
                .setFromTime(1667000000L)
                .setToTime(1669000000L)
                .setAgentId(123333L)
                .setUserIds(java.util.Arrays.asList(
                    "123"
                ))
                .setNextToken(0L)
                .setMaxResults(10)
                .setFaceCompareResult(1);
        try {
            client.getRecognizeRecordsWithOptions(getRecognizeRecordsRequest, getRecognizeRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_recognize_records_headers = dingtalkexclusive__1__0_models.GetRecognizeRecordsHeaders()
        get_recognize_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_recognize_records_request = dingtalkexclusive__1__0_models.GetRecognizeRecordsRequest(
            from_time=1667000000,
            to_time=1669000000,
            agent_id=123333,
            user_ids=[
                '123'
            ],
            next_token=0,
            max_results=10,
            face_compare_result=1
        )
        try:
            client.get_recognize_records_with_options(get_recognize_records_request, get_recognize_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_recognize_records_headers = dingtalkexclusive__1__0_models.GetRecognizeRecordsHeaders()
        get_recognize_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_recognize_records_request = dingtalkexclusive__1__0_models.GetRecognizeRecordsRequest(
            from_time=1667000000,
            to_time=1669000000,
            agent_id=123333,
            user_ids=[
                '123'
            ],
            next_token=0,
            max_results=10,
            face_compare_result=1
        )
        try:
            await client.get_recognize_records_with_options_async(get_recognize_records_request, get_recognize_records_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetRecognizeRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetRecognizeRecordsRequest;
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
        $getRecognizeRecordsHeaders = new GetRecognizeRecordsHeaders([]);
        $getRecognizeRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getRecognizeRecordsRequest = new GetRecognizeRecordsRequest([
            "fromTime" => 1667000000,
            "toTime" => 1669000000,
            "agentId" => 123333,
            "userIds" => [
                "123"
            ],
            "nextToken" => 0,
            "maxResults" => 10,
            "faceCompareResult" => 1
        ]);
        try {
            $client->getRecognizeRecordsWithOptions($getRecognizeRecordsRequest, $getRecognizeRecordsHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getRecognizeRecordsHeaders := &dingtalkexclusive_1_0.GetRecognizeRecordsHeaders{}
  getRecognizeRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getRecognizeRecordsRequest := &dingtalkexclusive_1_0.GetRecognizeRecordsRequest{
    FromTime: tea.Int64(1667000000),
    ToTime: tea.Int64(1669000000),
    AgentId: tea.Int64(123333),
    UserIds: []*string{tea.String("123")},
    NextToken: tea.Int64(0),
    MaxResults: tea.Int32(10),
    FaceCompareResult: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetRecognizeRecordsWithOptions(getRecognizeRecordsRequest, getRecognizeRecordsHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getRecognizeRecordsHeaders = new $dingtalkexclusive_1_0.GetRecognizeRecordsHeaders({ });
    getRecognizeRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getRecognizeRecordsRequest = new $dingtalkexclusive_1_0.GetRecognizeRecordsRequest({
      fromTime: 1667000000,
      toTime: 1669000000,
      agentId: 123333,
      userIds: [
        "123"
      ],
      nextToken: 0,
      maxResults: 10,
      faceCompareResult: 1,
    });
    try {
      await client.getRecognizeRecordsWithOptions(getRecognizeRecordsRequest, getRecognizeRecordsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetRecognizeRecordsHeaders getRecognizeRecordsHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetRecognizeRecordsHeaders();
            getRecognizeRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetRecognizeRecordsRequest getRecognizeRecordsRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetRecognizeRecordsRequest
            {
                FromTime = 1667000000,
                ToTime = 1669000000,
                AgentId = 123333,
                UserIds = new List<string>
                {
                    "123"
                },
                NextToken = 0,
                MaxResults = 10,
                FaceCompareResult = 1,
            };
            try
            {
                client.GetRecognizeRecordsWithOptions(getRecognizeRecordsRequest, getRecognizeRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | Long | 分页游标。 |
| total | Integer | 总数据数。 |
| data | Array | 数据信息列表。 |
| agentId | Long | 应用的agentId。 |
| userId | String | 用户userId。 |
| invokeTime | Long | 接口调用时间戳，单位毫秒。 |
| faceCompareResult | Integer | 人脸对比结果。   - 1：成功    - 2：失败 |
| platform | Integer | 平台。   - 0：Android - 1：iOS |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : 1,
  "total" : 20,
  "data" : [ {
    "userId" : "1234",
    "invokeTime" : 166700000,
    "faceCompareResult" : 1,
    "platform" : 1
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | app.not.exist | app不存在 | app不存在 |
| 400 | batch.exceed | 每批获取量超最大值 | 每批获取量超最大值 |
| 400 | time.should.close | 时间段需要闭合(fromTime和toTime需都传或都不传) | 时间段需要闭合(fromTime和toTime需都传或都不传) |
