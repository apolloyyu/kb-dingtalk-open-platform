---
title: "数据流通中心获取数据服务"
source_url: "https://open.dingtalk.com/document/dataopen/api-datamarketservice"
namespace: "dataopen"
slug: "api-datamarketservice"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "API 参考 > 获取数据流通中心数据"
doc_id: "b3RF1JZ7hG"
updated_at: "2026-06-15 10:33:50"
---

> Source: https://open.dingtalk.com/document/dataopen/api-datamarketservice
> Path: 数据资产 / 平台介绍 / API 参考 > 获取数据流通中心数据
> Updated: 2026-06-15 10:33:50

# 数据流通中心获取数据服务

通过该接口，获取流通中心的数据API的接口数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/datacenter/dataMarketServices/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-DataCenter.DataMarket.READ-数据流通中心读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| apiId | String | 否 | 数据API的apiId。 |
| args | String | 否 | 数据API传入的参数，详见对应数据API文档里的入参说明。 |

### **请求示例**

HTTP

```
POST /v1.0/datacenter/dataMarketServices/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f2a6d208b64432df8eea4a9a937
Content-Type:application/json

{
  "apiId" : "GS-YS-00001",
  "args" : "{entifno:\"企业名称\"}"
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
    public static com.aliyun.dingtalkdatacenter_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdatacenter_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdatacenter_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdatacenter_1_0.models.DataMarketServiceHeaders dataMarketServiceHeaders = new com.aliyun.dingtalkdatacenter_1_0.models.DataMarketServiceHeaders();
        dataMarketServiceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdatacenter_1_0.models.DataMarketServiceRequest dataMarketServiceRequest = new com.aliyun.dingtalkdatacenter_1_0.models.DataMarketServiceRequest()
                .setApiId("GS-YS-00001")
                .setArgs("{entifno:\"企业名称\"}");
        try {
            client.dataMarketServiceWithOptions(dataMarketServiceRequest, dataMarketServiceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.datacenter_1_0.client import Client as dingtalkdatacenter_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.datacenter_1_0 import models as dingtalkdatacenter__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdatacenter_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdatacenter_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        data_market_service_headers = dingtalkdatacenter__1__0_models.DataMarketServiceHeaders()
        data_market_service_headers.x_acs_dingtalk_access_token = '<your access token>'
        data_market_service_request = dingtalkdatacenter__1__0_models.DataMarketServiceRequest(
            api_id='GS-YS-00001',
            args='{entifno:"企业名称"}'
        )
        try:
            client.data_market_service_with_options(data_market_service_request, data_market_service_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        data_market_service_headers = dingtalkdatacenter__1__0_models.DataMarketServiceHeaders()
        data_market_service_headers.x_acs_dingtalk_access_token = '<your access token>'
        data_market_service_request = dingtalkdatacenter__1__0_models.DataMarketServiceRequest(
            api_id='GS-YS-00001',
            args='{entifno:"企业名称"}'
        )
        try:
            await client.data_market_service_with_options_async(data_market_service_request, data_market_service_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\DataMarketServiceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\DataMarketServiceRequest;
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
        $dataMarketServiceHeaders = new DataMarketServiceHeaders([]);
        $dataMarketServiceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $dataMarketServiceRequest = new DataMarketServiceRequest([
            "apiId" => "GS-YS-00001",
            "args" => "{entifno:\"企业名称\"}"
        ]);
        try {
            $client->dataMarketServiceWithOptions($dataMarketServiceRequest, $dataMarketServiceHeaders, new RuntimeOptions([]));
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
  dingtalkdatacenter_1_0  "github.com/alibabacloud-go/dingtalk/datacenter_1_0"
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
func CreateClient () (_result *dingtalkdatacenter_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdatacenter_1_0.Client{}
  _result, _err = dingtalkdatacenter_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  dataMarketServiceHeaders := &dingtalkdatacenter_1_0.DataMarketServiceHeaders{}
  dataMarketServiceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  dataMarketServiceRequest := &dingtalkdatacenter_1_0.DataMarketServiceRequest{
    ApiId: tea.String("GS-YS-00001"),
    Args: tea.String("{entifno:\"企业名称\"}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DataMarketServiceWithOptions(dataMarketServiceRequest, dataMarketServiceHeaders, &util.RuntimeOptions{})
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
const dingtalkdatacenter_1_0 = require('@alicloud/dingtalk/datacenter_1_0');
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
    return new dingtalkdatacenter_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let dataMarketServiceHeaders = new dingtalkdatacenter_1_0.DataMarketServiceHeaders({ });
    dataMarketServiceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let dataMarketServiceRequest = new dingtalkdatacenter_1_0.DataMarketServiceRequest({
      apiId: 'GS-YS-00001',
      args: '{entifno:"企业名称"}',
    });
    try {
      await client.dataMarketServiceWithOptions(dataMarketServiceRequest, dataMarketServiceHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.DataMarketServiceHeaders dataMarketServiceHeaders = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.DataMarketServiceHeaders();
            dataMarketServiceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.DataMarketServiceRequest dataMarketServiceRequest = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.DataMarketServiceRequest
            {
                ApiId = "GS-YS-00001",
                Args = "{entifno:\"企业名称\"}",
            };
            try
            {
                client.DataMarketServiceWithOptions(dataMarketServiceRequest, dataMarketServiceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | String | 数据API返回的数据。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : "{}"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | inputParams.serviceId.empty | apiId不能为空 | apiId不能为空 |
| 400 | inputParams.agrs.empty | args不能为空 | args不能为空 |
| 400 | inputParams.accountId.empty | accountId不能为空 | accountId不能为空 |
| 400 | inputParams.corpId.empty | corpId不能为空 | corpId不能为空 |
| 400 | inputParams.staffId.empty | userId不能为空 | userId不能为空 |
| 500 | system.error | %s | 系统错误%s |
