---
title: "分页查询客户列表"
source_url: "https://open.dingtalk.com/document/development/api-listcustomer"
namespace: "development"
slug: "api-listcustomer"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 视听智能服务 > 分页查询客户列表"
doc_id: "WyhGYBn4H1"
updated_at: "2026-06-24 13:44:35"
---

> Source: https://open.dingtalk.com/document/development/api-listcustomer
> Path: 应用开发 / 服务端 API / 更多开放 > 视听智能服务 > 分页查询客户列表
> Updated: 2026-06-24 13:44:35

# 分页查询客户列表

通过本接口，分页获取AI销售管理中的客户数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/customers |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Sale.Customer.Read-钉钉AI销售管理客户数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| teamCode | String | 是 | 团队或门店ID，可通过[获取团队信息](1294-api-listteam.md)接口获取。 |
| ownerUserId | String | 否 | 客户销售负责人userId。 |
| startTime | Long | 否 | 开始时间戳，单位毫秒（客户创建时间）。 |
| endTime | Long | 否 | 截止时间戳，单位毫秒（客户创建时间区间）。 |
| nextToken | String | 否 | 分页标识。 |
| maxResults | Integer | 否 | 每一页的数据量级。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/customers?teamCode=659550xxxx50c19&ownerUserId=userId&startTime=1765282298606&endTime=1769282298606&nextToken=0cfcaexxxx671af&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:979e2xxxx784bc
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
    public static com.aliyun.dingtalkdvi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdvi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdvi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdvi_1_0.models.ListCustomerHeaders listCustomerHeaders = new com.aliyun.dingtalkdvi_1_0.models.ListCustomerHeaders();
        listCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.ListCustomerRequest listCustomerRequest = new com.aliyun.dingtalkdvi_1_0.models.ListCustomerRequest()
                .setTeamCode("659550xxxx50c19")
                .setOwnerUserId("userId")
                .setStartTime(1765282298606L)
                .setEndTime(1769282298606L)
                .setNextToken("0cfcaexxxx671af")
                .setMaxResults(10);
        try {
            client.listCustomerWithOptions(listCustomerRequest, listCustomerHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.dvi_1_0.client import Client as dingtalkdvi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dvi_1_0 import models as dingtalkdvi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdvi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdvi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_customer_headers = dingtalkdvi__1__0_models.ListCustomerHeaders()
        list_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_customer_request = dingtalkdvi__1__0_models.ListCustomerRequest(
            team_code='659550xxxx50c19',
            owner_user_id='userId',
            start_time=1765282298606,
            end_time=1769282298606,
            next_token='0cfcaexxxx671af',
            max_results=10
        )
        try:
            client.list_customer_with_options(list_customer_request, list_customer_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_customer_headers = dingtalkdvi__1__0_models.ListCustomerHeaders()
        list_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_customer_request = dingtalkdvi__1__0_models.ListCustomerRequest(
            team_code='659550xxxx50c19',
            owner_user_id='userId',
            start_time=1765282298606,
            end_time=1769282298606,
            next_token='0cfcaexxxx671af',
            max_results=10
        )
        try:
            await client.list_customer_with_options_async(list_customer_request, list_customer_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListCustomerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListCustomerRequest;
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
        $listCustomerHeaders = new ListCustomerHeaders([]);
        $listCustomerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listCustomerRequest = new ListCustomerRequest([
            "teamCode" => "659550xxxx50c19",
            "ownerUserId" => "userId",
            "startTime" => 1765282298606,
            "endTime" => 1769282298606,
            "nextToken" => "0cfcaexxxx671af",
            "maxResults" => 10
        ]);
        try {
            $client->listCustomerWithOptions($listCustomerRequest, $listCustomerHeaders, new RuntimeOptions([]));
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
  dingtalkdvi_1_0  "github.com/alibabacloud-go/dingtalk/dvi_1_0"
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
func CreateClient () (_result *dingtalkdvi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdvi_1_0.Client{}
  _result, _err = dingtalkdvi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listCustomerHeaders := &dingtalkdvi_1_0.ListCustomerHeaders{}
  listCustomerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listCustomerRequest := &dingtalkdvi_1_0.ListCustomerRequest{
    TeamCode: tea.String("659550xxxx50c19"),
    OwnerUserId: tea.String("userId"),
    StartTime: tea.Int64(1765282298606),
    EndTime: tea.Int64(1769282298606),
    NextToken: tea.String("0cfcaexxxx671af"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListCustomerWithOptions(listCustomerRequest, listCustomerHeaders, &util.RuntimeOptions{})
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
const dingtalkdvi_1_0 = require('@alicloud/dingtalk/dvi_1_0');
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
    return new dingtalkdvi_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let listCustomerHeaders = new dingtalkdvi_1_0.ListCustomerHeaders({ });
    listCustomerHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listCustomerRequest = new dingtalkdvi_1_0.ListCustomerRequest({
      teamCode: '659550xxxx50c19',
      ownerUserId: 'userId',
      startTime: 1765282298606,
      endTime: 1769282298606,
      nextToken: '0cfcaexxxx671af',
      maxResults: 10,
    });
    try {
      await client.listCustomerWithOptions(listCustomerRequest, listCustomerHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdvi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdvi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListCustomerHeaders listCustomerHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListCustomerHeaders();
            listCustomerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListCustomerRequest listCustomerRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListCustomerRequest
            {
                TeamCode = "659550xxxx50c19",
                OwnerUserId = "userId",
                StartTime = 1765282298606,
                EndTime = 1769282298606,
                NextToken = "0cfcaexxxx671af",
                MaxResults = 10,
            };
            try
            {
                client.ListCustomerWithOptions(listCustomerRequest, listCustomerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 服务记录列表。 |
| id | String | 客户ID。 |
| name | String | 客户名。 |
| teamCode | String | 所属团队/门店编码。 |
| createAt | String | 客户创建时间戳，单位毫秒。 |
| ownerUserId | String | 客户负责人（销售）userId。 |
| totalCount | Integer | 总数 |
| nextToken | String | 下一页查询时的分页token,不存在下一页时此值为空 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "id" : "18675xxxx2b60",
    "name" : "张三",
    "teamCode" : "c024c6xxxx2e3d",
    "createAt" : "1765242298606",
    "ownerUserId" : "userId"
  } ],
  "totalCount" : 78,
  "nextToken" : "d979e2cxxxx7a784b"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | param.nextToken.error | nextToken参数错误 | nextToken参数错误 |
