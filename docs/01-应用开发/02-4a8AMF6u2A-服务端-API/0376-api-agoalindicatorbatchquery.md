---
title: "通过指标编码批量查询指标列表"
source_url: "https://open.dingtalk.com/document/development/api-agoalindicatorbatchquery"
namespace: "development"
slug: "api-agoalindicatorbatchquery"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Agoal > 指标库 > 通过指标编码批量查询指标列表"
doc_id: "yzaqdR9GOw"
updated_at: "2026-06-15 10:39:07"
---

> Source: https://open.dingtalk.com/document/development/api-agoalindicatorbatchquery
> Path: 应用开发 / 服务端 API / Agoal > 指标库 > 通过指标编码批量查询指标列表
> Updated: 2026-06-15 10:39:07

# 通过指标编码批量查询指标列表

通过该接口，使用Agoal系统中的指标编码批量查询指标的详情信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/agoal/indicator/batch/query |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Agoal.Indicator.Read-Agoal指标读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| codeList | Array of String | 否 | 指标编码。 |

### **请求示例**

HTTP

```
GET /v1.0/agoal/indicator/batch/query?codeList=["code_xxxxd98w3ifdsj"] HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:ajsdhiq3984hf
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
        com.aliyun.dingtalkagoal_1_0.models.AgoalIndicatorBatchQueryHeaders agoalIndicatorBatchQueryHeaders = new com.aliyun.dingtalkagoal_1_0.models.AgoalIndicatorBatchQueryHeaders();
        agoalIndicatorBatchQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkagoal_1_0.models.AgoalIndicatorBatchQueryRequest agoalIndicatorBatchQueryRequest = new com.aliyun.dingtalkagoal_1_0.models.AgoalIndicatorBatchQueryRequest();
        try {
            client.agoalIndicatorBatchQueryWithOptions(agoalIndicatorBatchQueryRequest, agoalIndicatorBatchQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        agoal_indicator_batch_query_headers = dingtalkagoal__1__0_models.AgoalIndicatorBatchQueryHeaders()
        agoal_indicator_batch_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_indicator_batch_query_request = dingtalkagoal__1__0_models.AgoalIndicatorBatchQueryRequest()
        try:
            client.agoal_indicator_batch_query_with_options(agoal_indicator_batch_query_request, agoal_indicator_batch_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        agoal_indicator_batch_query_headers = dingtalkagoal__1__0_models.AgoalIndicatorBatchQueryHeaders()
        agoal_indicator_batch_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_indicator_batch_query_request = dingtalkagoal__1__0_models.AgoalIndicatorBatchQueryRequest()
        try:
            await client.agoal_indicator_batch_query_with_options_async(agoal_indicator_batch_query_request, agoal_indicator_batch_query_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalIndicatorBatchQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalIndicatorBatchQueryRequest;
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
        $agoalIndicatorBatchQueryHeaders = new AgoalIndicatorBatchQueryHeaders([]);
        $agoalIndicatorBatchQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $agoalIndicatorBatchQueryRequest = new AgoalIndicatorBatchQueryRequest([]);
        try {
            $client->agoalIndicatorBatchQueryWithOptions($agoalIndicatorBatchQueryRequest, $agoalIndicatorBatchQueryHeaders, new RuntimeOptions([]));
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

  agoalIndicatorBatchQueryHeaders := &dingtalkagoal_1_0.AgoalIndicatorBatchQueryHeaders{}
  agoalIndicatorBatchQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  agoalIndicatorBatchQueryRequest := &dingtalkagoal_1_0.AgoalIndicatorBatchQueryRequest{}
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AgoalIndicatorBatchQueryWithOptions(agoalIndicatorBatchQueryRequest, agoalIndicatorBatchQueryHeaders, &util.RuntimeOptions{})
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
    let agoalIndicatorBatchQueryHeaders = new dingtalkagoal_1_0.AgoalIndicatorBatchQueryHeaders({ });
    agoalIndicatorBatchQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let agoalIndicatorBatchQueryRequest = new dingtalkagoal_1_0.AgoalIndicatorBatchQueryRequest({ });
    try {
      await client.agoalIndicatorBatchQueryWithOptions(agoalIndicatorBatchQueryRequest, agoalIndicatorBatchQueryHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalIndicatorBatchQueryHeaders agoalIndicatorBatchQueryHeaders = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalIndicatorBatchQueryHeaders();
            agoalIndicatorBatchQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalIndicatorBatchQueryRequest agoalIndicatorBatchQueryRequest = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalIndicatorBatchQueryRequest();
            try
            {
                client.AgoalIndicatorBatchQueryWithOptions(agoalIndicatorBatchQueryRequest, agoalIndicatorBatchQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否请求成功。 |
| result | Array | 结果数据。 |
| id | String | 指标唯一标识。 |
| code | String | 指标编码。 |
| title | String | 指标标题。 |
| description | String | 指标描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": "1734xxxxxxe08500e",
  "request_id": "5kaikoe9uc8i"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | organization.not.found | 当前组织不存在 | 当前组织不存在 |
