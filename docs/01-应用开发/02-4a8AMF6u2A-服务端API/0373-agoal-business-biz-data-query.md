---
title: "Agoal业务数据查询"
source_url: "https://open.dingtalk.com/document/development/agoal-business-biz-data-query"
namespace: "development"
slug: "agoal-business-biz-data-query"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Agoal > 业务实体 > Agoal业务数据查询"
doc_id: "ihOKwvyvLO"
updated_at: "2026-06-02 11:57:10"
---

> Source: https://open.dingtalk.com/document/development/agoal-business-biz-data-query
> Path: 应用开发 / 服务端API / Agoal > 业务实体 > Agoal业务数据查询
> Updated: 2026-06-02 11:57:10

# Agoal业务数据查询

调用本接口，通过业务编码分页查询Agoal业务数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/agoal/bizData/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Agoal.Indicator.Read-Agoal指标读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页位置。 |
| maxResults | Long | 否 | 分页条数。 |
| bizCode | String | 否 | 业务编码。 |

### 请求示例

HTTP

```
POST /v1.0/agoal/bizData/query?nextToken=100&maxResults=10&bizCode=ads_axxxxrt HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fd1c49xxxx33f5e0
Content-Type:application/json
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
    public static com.aliyun.dingtalkagoal_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkagoal_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkagoal_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkagoal_1_0.models.AgoalBizDataQueryHeaders agoalBizDataQueryHeaders = new com.aliyun.dingtalkagoal_1_0.models.AgoalBizDataQueryHeaders();
        agoalBizDataQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkagoal_1_0.models.AgoalBizDataQueryRequest agoalBizDataQueryRequest = new com.aliyun.dingtalkagoal_1_0.models.AgoalBizDataQueryRequest()
                .setNextToken("100")
                .setMaxResults(10L)
                .setBizCode("ads_axxxxrt");
        try {
            client.agoalBizDataQueryWithOptions(agoalBizDataQueryRequest, agoalBizDataQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.agoal_1_0.client import Client as dingtalkagoal_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.agoal_1_0 import models as dingtalkagoal__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkagoal_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkagoal_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        agoal_biz_data_query_headers = dingtalkagoal__1__0_models.AgoalBizDataQueryHeaders()
        agoal_biz_data_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_biz_data_query_request = dingtalkagoal__1__0_models.AgoalBizDataQueryRequest(
            next_token='100',
            max_results=10,
            biz_code='ads_axxxxrt'
        )
        try:
            client.agoal_biz_data_query_with_options(agoal_biz_data_query_request, agoal_biz_data_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        agoal_biz_data_query_headers = dingtalkagoal__1__0_models.AgoalBizDataQueryHeaders()
        agoal_biz_data_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_biz_data_query_request = dingtalkagoal__1__0_models.AgoalBizDataQueryRequest(
            next_token='100',
            max_results=10,
            biz_code='ads_axxxxrt'
        )
        try:
            await client.agoal_biz_data_query_with_options_async(agoal_biz_data_query_request, agoal_biz_data_query_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalBizDataQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalBizDataQueryRequest;
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
        $agoalBizDataQueryHeaders = new AgoalBizDataQueryHeaders([]);
        $agoalBizDataQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $agoalBizDataQueryRequest = new AgoalBizDataQueryRequest([
            "nextToken" => "100",
            "maxResults" => 10,
            "bizCode" => "ads_axxxxrt"
        ]);
        try {
            $client->agoalBizDataQueryWithOptions($agoalBizDataQueryRequest, $agoalBizDataQueryHeaders, new RuntimeOptions([]));
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
  dingtalkagoal_1_0  "github.com/alibabacloud-go/dingtalk/agoal_1_0"
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
func CreateClient () (_result *dingtalkagoal_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkagoal_1_0.Client{}
  _result, _err = dingtalkagoal_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  agoalBizDataQueryHeaders := &dingtalkagoal_1_0.AgoalBizDataQueryHeaders{}
  agoalBizDataQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  agoalBizDataQueryRequest := &dingtalkagoal_1_0.AgoalBizDataQueryRequest{
    NextToken: tea.String("100"),
    MaxResults: tea.Int64(10),
    BizCode: tea.String("ads_axxxxrt"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AgoalBizDataQueryWithOptions(agoalBizDataQueryRequest, agoalBizDataQueryHeaders, &util.RuntimeOptions{})
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
const dingtalkagoal_1_0 = require('@alicloud/dingtalk/agoal_1_0');
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
    return new dingtalkagoal_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let agoalBizDataQueryHeaders = new dingtalkagoal_1_0.AgoalBizDataQueryHeaders({ });
    agoalBizDataQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let agoalBizDataQueryRequest = new dingtalkagoal_1_0.AgoalBizDataQueryRequest({
      nextToken: '100',
      maxResults: 10,
      bizCode: 'ads_axxxxrt',
    });
    try {
      await client.agoalBizDataQueryWithOptions(agoalBizDataQueryRequest, agoalBizDataQueryHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkagoal_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkagoal_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalBizDataQueryHeaders agoalBizDataQueryHeaders = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalBizDataQueryHeaders();
            agoalBizDataQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalBizDataQueryRequest agoalBizDataQueryRequest = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalBizDataQueryRequest
            {
                NextToken = "100",
                MaxResults = 10,
                BizCode = "ads_axxxxrt",
            };
            try
            {
                client.AgoalBizDataQueryWithOptions(agoalBizDataQueryRequest, agoalBizDataQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |
| result | Boolean | 查询是否成功：   - **true**：成功 - **false**：失败 |
| requestId | String | 请求ID。 |
| content | Object | 数据内容。 |
| nextToken | String | 分页起始位置。 |
| maxResults | Long | 分页条数。 |
| bizInfos | Array of Object | 数据内容Map。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true,
  "requestId" : "331cd6dxxxxf54a144a",
  "content" : {
    "nextToken" : "100",
    "maxResults" : 10,
    "bizInfos" : [ {
      "user_id" : "6603cxxxxx2c59b60f",
      "org_id" : "660390xxxx1b9d09",
      "work_no" : "1000****43",
      "show_name" : "*帅",
      "is_dimission" : "N"
    }, {
      "user_id" : "4eaa1bxxxx6a523d",
      "org_id" : "660390xxxx771b9d09",
      "work_no" : "050709454*******16",
      "show_name" : "*启",
      "is_dimission" : "Y"
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
