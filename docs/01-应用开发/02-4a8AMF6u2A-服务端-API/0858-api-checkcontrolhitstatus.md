---
title: "企业员工专属安全管控功能命中查询"
source_url: "https://open.dingtalk.com/document/development/api-checkcontrolhitstatus"
namespace: "development"
slug: "api-checkcontrolhitstatus"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 企业员工专属安全管控功能命中查询"
doc_id: "BJ2pcqJYSJ"
updated_at: "2026-06-02 19:19:59"
---

> Source: https://open.dingtalk.com/document/development/api-checkcontrolhitstatus
> Path: 应用开发 / 服务端 API / 专属钉钉 > 企业员工专属安全管控功能命中查询
> Updated: 2026-06-02 19:19:59

# 企业员工专属安全管控功能命中查询

调用本接口，查询企业员工专属安全管控功能命中情况。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/soc/functionHitStatuses/check |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.Common.ReadWrite-专属钉钉基础数据读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 查询的员工userId。 |
| needMissedFunction | Boolean | 否 | 是否需要返回未命中的功能点，默认不返回。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/soc/functionHitStatuses/check?userId=userId&needMissedFunction=false HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token_test
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.CheckControlHitStatusHeaders checkControlHitStatusHeaders = new com.aliyun.dingtalkexclusive_1_0.models.CheckControlHitStatusHeaders();
        checkControlHitStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.CheckControlHitStatusRequest checkControlHitStatusRequest = new com.aliyun.dingtalkexclusive_1_0.models.CheckControlHitStatusRequest()
                .setUserId("userId")
                .setNeedMissedFunction(false);
        try {
            client.checkControlHitStatusWithOptions(checkControlHitStatusRequest, checkControlHitStatusHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        check_control_hit_status_headers = dingtalkexclusive__1__0_models.CheckControlHitStatusHeaders()
        check_control_hit_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        check_control_hit_status_request = dingtalkexclusive__1__0_models.CheckControlHitStatusRequest(
            user_id='userId',
            need_missed_function=False
        )
        try:
            client.check_control_hit_status_with_options(check_control_hit_status_request, check_control_hit_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_control_hit_status_headers = dingtalkexclusive__1__0_models.CheckControlHitStatusHeaders()
        check_control_hit_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        check_control_hit_status_request = dingtalkexclusive__1__0_models.CheckControlHitStatusRequest(
            user_id='userId',
            need_missed_function=False
        )
        try:
            await client.check_control_hit_status_with_options_async(check_control_hit_status_request, check_control_hit_status_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CheckControlHitStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CheckControlHitStatusRequest;
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
        $checkControlHitStatusHeaders = new CheckControlHitStatusHeaders([]);
        $checkControlHitStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $checkControlHitStatusRequest = new CheckControlHitStatusRequest([
            "userId" => "userId",
            "needMissedFunction" => false
        ]);
        try {
            $client->checkControlHitStatusWithOptions($checkControlHitStatusRequest, $checkControlHitStatusHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
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

  checkControlHitStatusHeaders := &dingtalkexclusive_1_0.CheckControlHitStatusHeaders{}
  checkControlHitStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  checkControlHitStatusRequest := &dingtalkexclusive_1_0.CheckControlHitStatusRequest{
    UserId: tea.String("userId"),
    NeedMissedFunction: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CheckControlHitStatusWithOptions(checkControlHitStatusRequest, checkControlHitStatusHeaders, &util.RuntimeOptions{})
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
const dingtalkexclusive_1_0 = require('@alicloud/dingtalk/exclusive_1_0');
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
    return new dingtalkexclusive_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let checkControlHitStatusHeaders = new dingtalkexclusive_1_0.CheckControlHitStatusHeaders({ });
    checkControlHitStatusHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let checkControlHitStatusRequest = new dingtalkexclusive_1_0.CheckControlHitStatusRequest({
      userId: 'userId',
      needMissedFunction: false,
    });
    try {
      await client.checkControlHitStatusWithOptions(checkControlHitStatusRequest, checkControlHitStatusHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CheckControlHitStatusHeaders checkControlHitStatusHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CheckControlHitStatusHeaders();
            checkControlHitStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CheckControlHitStatusRequest checkControlHitStatusRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CheckControlHitStatusRequest
            {
                UserId = "userId",
                NeedMissedFunction = false,
            };
            try
            {
                client.CheckControlHitStatusWithOptions(checkControlHitStatusRequest, checkControlHitStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回管控查询结果。 |
| controlStatus | Integer | 管控状态：   - 0：主企业设置错误 - 1：到管控 - 2：异常需排查 |
| reason | String | 未管控原因。 |
| controlList | Array of String | 用户命中的管控功能信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "controlStatus" : 1,
    "reason" : "主企业设置错误",
    "controlList" : [ "信息保护_下载看看中的图片及视频管控:生效中" ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequestParams | 必填请求参数缺失 | 必填请求参数缺失 |
| 500 | systemError | 系统繁忙，请稍后再试 | 兜底错误码 |
