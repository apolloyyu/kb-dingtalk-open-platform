---
title: "人员标签数据查询"
source_url: "https://open.dingtalk.com/document/development/api-stafflabelrecordsquery"
namespace: "development"
slug: "api-stafflabelrecordsquery"
group: "应用开发"
tab: "服务端API"
breadcrumb: "组织大脑 > 人才档案 > 人员标签数据查询"
doc_id: "Bxjqum7tcN"
updated_at: "2026-06-02 19:34:56"
---

> Source: https://open.dingtalk.com/document/development/api-stafflabelrecordsquery
> Path: 应用开发 / 服务端API / 组织大脑 > 人才档案 > 人员标签数据查询
> Updated: 2026-06-02 19:34:56

# 人员标签数据查询

调用本接口，分页查询组织人员标签数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/labelRecords/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Hrbrain.Data.Read-组织大脑数据查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dingCorpId | String | 否 | 组织ID。 |
| maxResult | Integer | 否 | 分页条数。 |
| nextToken | String | 否 | 分页起始位置。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 否 | 查询人员信息。 |
| userId | String | 否 | 钉钉用户 UserId。 |
| labels | Array | 否 | 标签列表。 |
| typeCode | String | 否 | 分类 Code。 |
| code | String | 否 | 标签 Code。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/labelRecords/query?dingCorpId=ding3b***********88&maxResult=10&nextToken=100 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f562a63089343de7999bf20e6de46412
Content-Type:application/json

[ {
  "userId" : "0140180438261064274667",
  "labels" : [ {
    "typeCode" : "values",
    "code" : "long_termism_score"
  } ]
} ]
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
        com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryHeaders staffLabelRecordsQueryHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryHeaders();
        staffLabelRecordsQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBodyLabels body0Labels0 = new com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBodyLabels()
                .setTypeCode("values")
                .setCode("long_termism_score");
        com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody body0 = new com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody()
                .setUserId("0140180438261064274667")
                .setLabels(java.util.Arrays.asList(
                    body0Labels0
                ));
        com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryRequest staffLabelRecordsQueryRequest = new com.aliyun.dingtalkhrbrain_1_0.models.StaffLabelRecordsQueryRequest()
                .setDingCorpId("ding3b***********88")
                .setMaxResult(10)
                .setNextToken("100")
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.staffLabelRecordsQueryWithOptions(staffLabelRecordsQueryRequest, staffLabelRecordsQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        staff_label_records_query_headers = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryHeaders()
        staff_label_records_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0labels_0 = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryRequestBodyLabels(
            type_code='values',
            code='long_termism_score'
        )
        body_0 = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryRequestBody(
            user_id='0140180438261064274667',
            labels=[
                body_0labels_0
            ]
        )
        staff_label_records_query_request = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryRequest(
            ding_corp_id='ding3b***********88',
            max_result=10,
            next_token='100',
            body=[
                body_0
            ]
        )
        try:
            client.staff_label_records_query_with_options(staff_label_records_query_request, staff_label_records_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        staff_label_records_query_headers = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryHeaders()
        staff_label_records_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0labels_0 = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryRequestBodyLabels(
            type_code='values',
            code='long_termism_score'
        )
        body_0 = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryRequestBody(
            user_id='0140180438261064274667',
            labels=[
                body_0labels_0
            ]
        )
        staff_label_records_query_request = dingtalkhrbrain__1__0_models.StaffLabelRecordsQueryRequest(
            ding_corp_id='ding3b***********88',
            max_result=10,
            next_token='100',
            body=[
                body_0
            ]
        )
        try:
            await client.staff_label_records_query_with_options_async(staff_label_records_query_request, staff_label_records_query_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\StaffLabelRecordsQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\StaffLabelRecordsQueryRequest\body\labels;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\StaffLabelRecordsQueryRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\StaffLabelRecordsQueryRequest;
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
        $staffLabelRecordsQueryHeaders = new StaffLabelRecordsQueryHeaders([]);
        $staffLabelRecordsQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0Labels0 = new labels([
            "typeCode" => "values",
            "code" => "long_termism_score"
        ]);
        $body0 = new body([
            "userId" => "0140180438261064274667",
            "labels" => [
                $body0Labels0
            ]
        ]);
        $staffLabelRecordsQueryRequest = new StaffLabelRecordsQueryRequest([
            "dingCorpId" => "ding3b***********88",
            "maxResult" => 10,
            "nextToken" => "100",
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->staffLabelRecordsQueryWithOptions($staffLabelRecordsQueryRequest, $staffLabelRecordsQueryHeaders, new RuntimeOptions([]));
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

  staffLabelRecordsQueryHeaders := &dingtalkhrbrain_1_0.StaffLabelRecordsQueryHeaders{}
  staffLabelRecordsQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0Labels0 := &dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequestBodyLabels{
    TypeCode: tea.String("values"),
    Code: tea.String("long_termism_score"),
  }
  body0 := &dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequestBody{
    UserId: tea.String("0140180438261064274667"),
    Labels: []*dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequestBodyLabels{body0Labels0},
  }
  staffLabelRecordsQueryRequest := &dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequest{
    DingCorpId: tea.String("ding3b***********88"),
    MaxResult: tea.Int32(10),
    NextToken: tea.String("100"),
    Body: []*dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.StaffLabelRecordsQueryWithOptions(staffLabelRecordsQueryRequest, staffLabelRecordsQueryHeaders, &util.RuntimeOptions{})
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
    let staffLabelRecordsQueryHeaders = new dingtalkhrbrain_1_0.StaffLabelRecordsQueryHeaders({ });
    staffLabelRecordsQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let body0Labels0 = new dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequestBodyLabels({
      typeCode: 'values',
      code: 'long_termism_score',
    });
    let body0 = new dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequestBody({
      userId: '0140180438261064274667',
      labels: [
        body0Labels0
      ],
    });
    let staffLabelRecordsQueryRequest = new dingtalkhrbrain_1_0.StaffLabelRecordsQueryRequest({
      dingCorpId: 'ding3b***********88',
      maxResult: 10,
      nextToken: '100',
      body: [
        body0
      ],
    });
    try {
      await client.staffLabelRecordsQueryWithOptions(staffLabelRecordsQueryRequest, staffLabelRecordsQueryHeaders, new Util.RuntimeOptions({ }));
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
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
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryHeaders staffLabelRecordsQueryHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryHeaders();
            staffLabelRecordsQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody.StaffLabelRecordsQueryRequestBodyLabels body0Labels0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody.StaffLabelRecordsQueryRequestBodyLabels
            {
                TypeCode = "values",
                Code = "long_termism_score",
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody body0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody
            {
                UserId = "0140180438261064274667",
                Labels = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody.StaffLabelRecordsQueryRequestBodyLabels>
                {
                    body0Labels0
                },
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest staffLabelRecordsQueryRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest
            {
                DingCorpId = "ding3b***********88",
                MaxResult = 10,
                NextToken = "100",
                Body = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.StaffLabelRecordsQueryRequest.StaffLabelRecordsQueryRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.StaffLabelRecordsQueryWithOptions(staffLabelRecordsQueryRequest, staffLabelRecordsQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求ID。 |
| success | Boolean | 调用状态。 |
| result | Boolean | 执行结果。 |
| content | Object | 返回结果。 |
| nextToken | String | 分页查询凭证。 |
| maxResults | Long | 每页条数。 |
| totalCountt | Long | 总记录数。 |
| data | Array | 人员标签信息。 |
| labels | Array | 标签信息。 |
| code | String | 标签 Code。 |
| guid | String | 标签唯一 ID。 |
| name | String | 标签名称。 |
| options | Array | 标签选项列表。 |
| label | String | 选项名称。 |
| tip | String | 选项说明。 |
| value | String | 选项值。 |
| typeCode | String | 标签分类 Code。 |
| typeName | String | 标签分类名称。 |
| value | String | 标签值。 |
| userId | String | 钉钉用户 UserId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "0140180438261064274667",
  "success" : true,
  "result" : true,
  "content" : {
    "nextToken" : "100",
    "maxResults" : 10,
    "totalCountt" : 100,
    "data" : [ {
      "labels" : [ {
        "code" : "long_termism_score",
        "guid" : "values.long_termism_score",
        "name" : "持续业绩",
        "options" : [ {
          "label" : "选项名称",
          "tip" : "选项说明",
          "value" : "选项值"
        } ],
        "typeCode" : "values",
        "typeName" : "价值",
        "value" : "5（总是）"
      } ],
      "userId" : "0140180438261064274667"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illagal. %s | 入参错误 |
