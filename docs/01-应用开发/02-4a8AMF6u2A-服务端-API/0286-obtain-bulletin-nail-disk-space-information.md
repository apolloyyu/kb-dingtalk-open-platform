---
title: "获取公告钉盘空间信息"
source_url: "https://open.dingtalk.com/document/development/obtain-bulletin-nail-disk-space-information"
namespace: "development"
slug: "obtain-bulletin-nail-disk-space-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "公告 > 获取公告钉盘空间信息"
doc_id: "gjbgp3b9B3"
updated_at: "2026-06-01 18:25:09"
---

> Source: https://open.dingtalk.com/document/development/obtain-bulletin-nail-disk-space-information
> Path: 应用开发 / 服务端 API / 公告 > 获取公告钉盘空间信息
> Updated: 2026-06-01 18:25:09

# 获取公告钉盘空间信息

调用本接口，获取企业组织公告的钉盘空间信息，用于发公告时可携带附件信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/blackboard/spaces |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_read-读取钉钉公告微应用数据的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operationUserId | String | 是 | 操作人userId。 |

### 请求示例

HTTP

```
GET /v1.0/blackboard/spaces?operationUserId=manager01 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkblackboard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkblackboard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkblackboard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardSpaceHeaders queryBlackboardSpaceHeaders = new com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardSpaceHeaders();
        queryBlackboardSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardSpaceRequest queryBlackboardSpaceRequest = new com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardSpaceRequest()
                .setOperationUserId("manager01");
        try {
            client.queryBlackboardSpaceWithOptions(queryBlackboardSpaceRequest, queryBlackboardSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.blackboard_1_0.client import Client as dingtalkblackboard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.blackboard_1_0 import models as dingtalkblackboard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkblackboard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkblackboard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_blackboard_space_headers = dingtalkblackboard__1__0_models.QueryBlackboardSpaceHeaders()
        query_blackboard_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_blackboard_space_request = dingtalkblackboard__1__0_models.QueryBlackboardSpaceRequest(
            operation_user_id='manager01'
        )
        try:
            client.query_blackboard_space_with_options(query_blackboard_space_request, query_blackboard_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_blackboard_space_headers = dingtalkblackboard__1__0_models.QueryBlackboardSpaceHeaders()
        query_blackboard_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_blackboard_space_request = dingtalkblackboard__1__0_models.QueryBlackboardSpaceRequest(
            operation_user_id='manager01'
        )
        try:
            await client.query_blackboard_space_with_options_async(query_blackboard_space_request, query_blackboard_space_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Models\QueryBlackboardSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Models\QueryBlackboardSpaceRequest;
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
        $queryBlackboardSpaceHeaders = new QueryBlackboardSpaceHeaders([]);
        $queryBlackboardSpaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryBlackboardSpaceRequest = new QueryBlackboardSpaceRequest([
            "operationUserId" => "manager01"
        ]);
        try {
            $client->queryBlackboardSpaceWithOptions($queryBlackboardSpaceRequest, $queryBlackboardSpaceHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkblackboard_1_0  "github.com/alibabacloud-go/dingtalk/blackboard_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkblackboard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkblackboard_1_0.Client{}
  _result, _err = dingtalkblackboard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryBlackboardSpaceHeaders := &dingtalkblackboard_1_0.QueryBlackboardSpaceHeaders{}
  queryBlackboardSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryBlackboardSpaceRequest := &dingtalkblackboard_1_0.QueryBlackboardSpaceRequest{
    OperationUserId: tea.String("manager01"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryBlackboardSpaceWithOptions(queryBlackboardSpaceRequest, queryBlackboardSpaceHeaders, &util.RuntimeOptions{})
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
import dingtalkblackboard_1_0, * as $dingtalkblackboard_1_0 from '@alicloud/dingtalk/blackboard_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkblackboard_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkblackboard_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryBlackboardSpaceHeaders = new $dingtalkblackboard_1_0.QueryBlackboardSpaceHeaders({ });
    queryBlackboardSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryBlackboardSpaceRequest = new $dingtalkblackboard_1_0.QueryBlackboardSpaceRequest({
      operationUserId: "manager01",
    });
    try {
      await client.queryBlackboardSpaceWithOptions(queryBlackboardSpaceRequest, queryBlackboardSpaceHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkblackboard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardSpaceHeaders queryBlackboardSpaceHeaders = new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardSpaceHeaders();
            queryBlackboardSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardSpaceRequest queryBlackboardSpaceRequest = new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardSpaceRequest
            {
                OperationUserId = "manager01",
            };
            try
            {
                client.QueryBlackboardSpaceWithOptions(queryBlackboardSpaceRequest, queryBlackboardSpaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| spaceId | String | 当前组织的公告对应的钉盘空间id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "spaceId" : "100"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 403 | accessDenied | %s | 请求被拒绝，请确认企业开通了公告微应用，并且用户id正确。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
