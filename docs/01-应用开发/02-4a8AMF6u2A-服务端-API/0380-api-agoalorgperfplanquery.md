---
title: "查询企业下的所有考核计划"
source_url: "https://open.dingtalk.com/document/development/api-agoalorgperfplanquery"
namespace: "development"
slug: "api-agoalorgperfplanquery"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Agoal > 绩效考核 > 查询企业下的所有考核计划"
doc_id: "oWVoffjFTx"
updated_at: "2026-06-02 11:54:49"
---

> Source: https://open.dingtalk.com/document/development/api-agoalorgperfplanquery
> Path: 应用开发 / 服务端 API / Agoal > 绩效考核 > 查询企业下的所有考核计划
> Updated: 2026-06-02 11:54:49

# 查询企业下的所有考核计划

用于查询企业下的所有考核计划。调用时通过 GET 请求。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/agoal/org\_perf/plans/query |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Agoal.OrgPerfPlan.Read-Agoal组织绩效计划读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageNumber | Integer | 是 | 分页页码。 |
| pageSize | Integer | 否 | 分页大小。 |

### 请求示例

HTTP

```
GET /v1.0/agoal/org_perf/plans/query?pageNumber=1&pageSize=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:9801a354e3d03539baa83e5f275axxxx
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
    public static com.aliyun.dingtalkagoal_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkagoal_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkagoal_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkagoal_1_0.models.AgoalOrgPerfPlanQueryHeaders agoalOrgPerfPlanQueryHeaders = new com.aliyun.dingtalkagoal_1_0.models.AgoalOrgPerfPlanQueryHeaders();
        agoalOrgPerfPlanQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkagoal_1_0.models.AgoalOrgPerfPlanQueryRequest agoalOrgPerfPlanQueryRequest = new com.aliyun.dingtalkagoal_1_0.models.AgoalOrgPerfPlanQueryRequest()
                .setPageNumber(1)
                .setPageSize(10);
        try {
            client.agoalOrgPerfPlanQueryWithOptions(agoalOrgPerfPlanQueryRequest, agoalOrgPerfPlanQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        agoal_org_perf_plan_query_headers = dingtalkagoal__1__0_models.AgoalOrgPerfPlanQueryHeaders()
        agoal_org_perf_plan_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_org_perf_plan_query_request = dingtalkagoal__1__0_models.AgoalOrgPerfPlanQueryRequest(
            page_number=1,
            page_size=10
        )
        try:
            client.agoal_org_perf_plan_query_with_options(agoal_org_perf_plan_query_request, agoal_org_perf_plan_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        agoal_org_perf_plan_query_headers = dingtalkagoal__1__0_models.AgoalOrgPerfPlanQueryHeaders()
        agoal_org_perf_plan_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_org_perf_plan_query_request = dingtalkagoal__1__0_models.AgoalOrgPerfPlanQueryRequest(
            page_number=1,
            page_size=10
        )
        try:
            await client.agoal_org_perf_plan_query_with_options_async(agoal_org_perf_plan_query_request, agoal_org_perf_plan_query_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalOrgPerfPlanQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalOrgPerfPlanQueryRequest;
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
        $agoalOrgPerfPlanQueryHeaders = new AgoalOrgPerfPlanQueryHeaders([]);
        $agoalOrgPerfPlanQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $agoalOrgPerfPlanQueryRequest = new AgoalOrgPerfPlanQueryRequest([
            "pageNumber" => 1,
            "pageSize" => 10
        ]);
        try {
            $client->agoalOrgPerfPlanQueryWithOptions($agoalOrgPerfPlanQueryRequest, $agoalOrgPerfPlanQueryHeaders, new RuntimeOptions([]));
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

  agoalOrgPerfPlanQueryHeaders := &dingtalkagoal_1_0.AgoalOrgPerfPlanQueryHeaders{}
  agoalOrgPerfPlanQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  agoalOrgPerfPlanQueryRequest := &dingtalkagoal_1_0.AgoalOrgPerfPlanQueryRequest{
    PageNumber: tea.Int32(1),
    PageSize: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AgoalOrgPerfPlanQueryWithOptions(agoalOrgPerfPlanQueryRequest, agoalOrgPerfPlanQueryHeaders, &util.RuntimeOptions{})
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
    let agoalOrgPerfPlanQueryHeaders = new dingtalkagoal_1_0.AgoalOrgPerfPlanQueryHeaders({ });
    agoalOrgPerfPlanQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let agoalOrgPerfPlanQueryRequest = new dingtalkagoal_1_0.AgoalOrgPerfPlanQueryRequest({
      pageNumber: 1,
      pageSize: 10,
    });
    try {
      await client.agoalOrgPerfPlanQueryWithOptions(agoalOrgPerfPlanQueryRequest, agoalOrgPerfPlanQueryHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgPerfPlanQueryHeaders agoalOrgPerfPlanQueryHeaders = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgPerfPlanQueryHeaders();
            agoalOrgPerfPlanQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgPerfPlanQueryRequest agoalOrgPerfPlanQueryRequest = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgPerfPlanQueryRequest
            {
                PageNumber = 1,
                PageSize = 10,
            };
            try
            {
                client.AgoalOrgPerfPlanQueryWithOptions(agoalOrgPerfPlanQueryRequest, agoalOrgPerfPlanQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求Id。 |
| success | Boolean | 请求是否成功。 |
| content | Object | 返回分页结果。 |
| pageNumber | Integer | 分页页码。 |
| pageSize | Integer | 分页大小。 |
| totalCount | Long | 总数量。 |
| result | Array | 返回考核计划对象数组。 |
| OpenOrgPerfPlanDTO | OpenOrgPerfPlanDTO | 考核计划对象。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "E6F8BAA4-6C37-168D-858A-F2A85447755F",
  "success" : true,
  "content" : {
    "pageNumber" : 1,
    "pageSize" : 10,
    "totalCount" : 10,
    "result" : [ {
      "planId" : "68ff23f2699038xxx87e71cf",
      "title" : "考核计划",
      "status" : "PENDING"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | error.systemError | 系统异常 | 系统异常 |
