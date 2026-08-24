---
title: "人才池在池人员列表"
source_url: "https://open.dingtalk.com/document/development/api-hrbrainemppooluser"
namespace: "development"
slug: "api-hrbrainemppooluser"
group: "应用开发"
tab: "服务端API"
breadcrumb: "组织大脑 > 人才池 > 人才池在池人员列表"
doc_id: "rFQwcFSkvJ"
updated_at: "2026-06-02 19:34:57"
---

> Source: https://open.dingtalk.com/document/development/api-hrbrainemppooluser
> Path: 应用开发 / 服务端API / 组织大脑 > 人才池 > 人才池在池人员列表
> Updated: 2026-06-02 19:34:57

# 人才池在池人员列表

调用本接口，分页获取人才池在池人员列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/empPools/users/lists/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrbrain.Data.Read-组织大脑数据查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | Integer | 否 | 分页起始位置。 |
| maxResults | Integer | 否 | 分页条数，如果未填写，默认100条。 |
| poolCode | String | 否 | 人才池Code。 |
| userId | String | 否 | 操作人id，传值时，会根据应用管理后台配置的人员权限去过滤数据。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/empPools/users/lists/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e0419c1adxxx5e8cb427f
Content-Type:application/json

{
  "nextToken" : 0,
  "maxResults" : 10,
  "poolCode" : "331cd6xxxx4a144a",
  "userId" : "266xxx1968"
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
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainEmpPoolUserHeaders hrbrainEmpPoolUserHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainEmpPoolUserHeaders();
        hrbrainEmpPoolUserHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainEmpPoolUserRequest hrbrainEmpPoolUserRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainEmpPoolUserRequest()
                .setNextToken(0)
                .setMaxResults(10)
                .setPoolCode("331cd6xxxx4a144a")
                .setUserId("266xxx1968");
        try {
            client.hrbrainEmpPoolUserWithOptions(hrbrainEmpPoolUserRequest, hrbrainEmpPoolUserHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        hrbrain_emp_pool_user_headers = dingtalkhrbrain__1__0_models.HrbrainEmpPoolUserHeaders()
        hrbrain_emp_pool_user_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrbrain_emp_pool_user_request = dingtalkhrbrain__1__0_models.HrbrainEmpPoolUserRequest(
            next_token=0,
            max_results=10,
            pool_code='331cd6xxxx4a144a',
            user_id='266xxx1968'
        )
        try:
            client.hrbrain_emp_pool_user_with_options(hrbrain_emp_pool_user_request, hrbrain_emp_pool_user_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_emp_pool_user_headers = dingtalkhrbrain__1__0_models.HrbrainEmpPoolUserHeaders()
        hrbrain_emp_pool_user_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrbrain_emp_pool_user_request = dingtalkhrbrain__1__0_models.HrbrainEmpPoolUserRequest(
            next_token=0,
            max_results=10,
            pool_code='331cd6xxxx4a144a',
            user_id='266xxx1968'
        )
        try:
            await client.hrbrain_emp_pool_user_with_options_async(hrbrain_emp_pool_user_request, hrbrain_emp_pool_user_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainEmpPoolUserHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainEmpPoolUserRequest;
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
        $hrbrainEmpPoolUserHeaders = new HrbrainEmpPoolUserHeaders([]);
        $hrbrainEmpPoolUserHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $hrbrainEmpPoolUserRequest = new HrbrainEmpPoolUserRequest([
            "nextToken" => 0,
            "maxResults" => 10,
            "poolCode" => "331cd6xxxx4a144a",
            "userId" => "266xxx1968"
        ]);
        try {
            $client->hrbrainEmpPoolUserWithOptions($hrbrainEmpPoolUserRequest, $hrbrainEmpPoolUserHeaders, new RuntimeOptions([]));
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

  hrbrainEmpPoolUserHeaders := &dingtalkhrbrain_1_0.HrbrainEmpPoolUserHeaders{}
  hrbrainEmpPoolUserHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  hrbrainEmpPoolUserRequest := &dingtalkhrbrain_1_0.HrbrainEmpPoolUserRequest{
    NextToken: tea.Int32(0),
    MaxResults: tea.Int32(10),
    PoolCode: tea.String("331cd6xxxx4a144a"),
    UserId: tea.String("266xxx1968"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainEmpPoolUserWithOptions(hrbrainEmpPoolUserRequest, hrbrainEmpPoolUserHeaders, &util.RuntimeOptions{})
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
    let hrbrainEmpPoolUserHeaders = new dingtalkhrbrain_1_0.HrbrainEmpPoolUserHeaders({ });
    hrbrainEmpPoolUserHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let hrbrainEmpPoolUserRequest = new dingtalkhrbrain_1_0.HrbrainEmpPoolUserRequest({
      nextToken: 0,
      maxResults: 10,
      poolCode: '331cd6xxxx4a144a',
      userId: '266xxx1968',
    });
    try {
      await client.hrbrainEmpPoolUserWithOptions(hrbrainEmpPoolUserRequest, hrbrainEmpPoolUserHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainEmpPoolUserHeaders hrbrainEmpPoolUserHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainEmpPoolUserHeaders();
            hrbrainEmpPoolUserHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainEmpPoolUserRequest hrbrainEmpPoolUserRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainEmpPoolUserRequest
            {
                NextToken = 0,
                MaxResults = 10,
                PoolCode = "331cd6xxxx4a144a",
                UserId = "266xxx1968",
            };
            try
            {
                client.HrbrainEmpPoolUserWithOptions(hrbrainEmpPoolUserRequest, hrbrainEmpPoolUserHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功：   - **true**：执行成功 - **false**：执行失败 |
| result | Boolean | 查询是否成功：   - **true**：执行成功 - **false**：执行失败 |
| content | Object | 返回结果。 |
| totalCount | Integer | 总记录数。 |
| maxResults | Integer | 每页条数。 |
| nextToken | Integer | 分页起始位置。 |
| empVos | Array | 人员信息列表。 |
| userId | String | 用户ID。 |
| name | String | 姓名。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "331cd6xxxx54a144a",
  "success" : true,
  "result" : true,
  "content" : {
    "totalCount" : 100,
    "maxResults" : 10,
    "nextToken" : 50,
    "empVos" : [ {
      "userId" : "20b52xxxx7cc",
      "name" : "用户A"
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
