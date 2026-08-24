---
title: "查询数据资产平台服务最新数据日期"
source_url: "https://open.dingtalk.com/document/dataopen/api-querygeneraldataupdatedate"
namespace: "dataopen"
slug: "api-querygeneraldataupdatedate"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "API 参考 > 查询数据资产平台服务最新数据日期"
doc_id: "cdr56xbXLM"
updated_at: "2026-06-15 10:33:48"
---

> Source: https://open.dingtalk.com/document/dataopen/api-querygeneraldataupdatedate
> Path: 数据资产 / 平台介绍 / API 参考 > 查询数据资产平台服务最新数据日期
> Updated: 2026-06-15 10:33:48

# 查询数据资产平台服务最新数据日期

通过该接口，查询数据资产平台创建的数据服务的最新数据日期。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/datacenter/dataUpdateDates |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-DataCenter.GeneralDataSet.Read-数据服务目录资产服务读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceId | String | 是 | 数据服务 ID。 |

### 请求示例

HTTP

```
GET /v1.0/datacenter/dataUpdateDates?serviceId=API-xxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:4f29c24cf71d3423b57d0e8678c2dd
Content-Type:application/json
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
        com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataUpdateDateHeaders queryGeneralDataUpdateDateHeaders = new com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataUpdateDateHeaders();
        queryGeneralDataUpdateDateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataUpdateDateRequest queryGeneralDataUpdateDateRequest = new com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataUpdateDateRequest()
                .setServiceId("API-xxxxx");
        try {
            client.queryGeneralDataUpdateDateWithOptions(queryGeneralDataUpdateDateRequest, queryGeneralDataUpdateDateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_general_data_update_date_headers = dingtalkdatacenter__1__0_models.QueryGeneralDataUpdateDateHeaders()
        query_general_data_update_date_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_general_data_update_date_request = dingtalkdatacenter__1__0_models.QueryGeneralDataUpdateDateRequest(
            service_id='API-xxxxx'
        )
        try:
            client.query_general_data_update_date_with_options(query_general_data_update_date_request, query_general_data_update_date_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_general_data_update_date_headers = dingtalkdatacenter__1__0_models.QueryGeneralDataUpdateDateHeaders()
        query_general_data_update_date_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_general_data_update_date_request = dingtalkdatacenter__1__0_models.QueryGeneralDataUpdateDateRequest(
            service_id='API-xxxxx'
        )
        try:
            await client.query_general_data_update_date_with_options_async(query_general_data_update_date_request, query_general_data_update_date_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\QueryGeneralDataUpdateDateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\QueryGeneralDataUpdateDateRequest;
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
        $queryGeneralDataUpdateDateHeaders = new QueryGeneralDataUpdateDateHeaders([]);
        $queryGeneralDataUpdateDateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryGeneralDataUpdateDateRequest = new QueryGeneralDataUpdateDateRequest([
            "serviceId" => "API-xxxxx"
        ]);
        try {
            $client->queryGeneralDataUpdateDateWithOptions($queryGeneralDataUpdateDateRequest, $queryGeneralDataUpdateDateHeaders, new RuntimeOptions([]));
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

  queryGeneralDataUpdateDateHeaders := &dingtalkdatacenter_1_0.QueryGeneralDataUpdateDateHeaders{}
  queryGeneralDataUpdateDateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryGeneralDataUpdateDateRequest := &dingtalkdatacenter_1_0.QueryGeneralDataUpdateDateRequest{
    ServiceId: tea.String("API-xxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryGeneralDataUpdateDateWithOptions(queryGeneralDataUpdateDateRequest, queryGeneralDataUpdateDateHeaders, &util.RuntimeOptions{})
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
    let queryGeneralDataUpdateDateHeaders = new dingtalkdatacenter_1_0.QueryGeneralDataUpdateDateHeaders({ });
    queryGeneralDataUpdateDateHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryGeneralDataUpdateDateRequest = new dingtalkdatacenter_1_0.QueryGeneralDataUpdateDateRequest({
      serviceId: 'API-xxxxx',
    });
    try {
      await client.queryGeneralDataUpdateDateWithOptions(queryGeneralDataUpdateDateRequest, queryGeneralDataUpdateDateHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataUpdateDateHeaders queryGeneralDataUpdateDateHeaders = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataUpdateDateHeaders();
            queryGeneralDataUpdateDateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataUpdateDateRequest queryGeneralDataUpdateDateRequest = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataUpdateDateRequest
            {
                ServiceId = "API-xxxxx",
            };
            try
            {
                client.QueryGeneralDataUpdateDateWithOptions(queryGeneralDataUpdateDateRequest, queryGeneralDataUpdateDateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| updateDate | String | 数据日期，格式：yyyyMMdd。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "updateDate" : "20240617"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](../../01-应用开发/02-4a8AMF6u2A-服务端API/0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | service.code.invalid | 数据服务编码无效 | 数据服务编码无效 |
| 500 | service.not.found | 数据服务未找到 | 数据服务未找到 |
| 500 | service.code.invalid | 数据服务编码无效:serviceId不属于本组织 | 数据服务编码无效:serviceId不属于本组织 |
