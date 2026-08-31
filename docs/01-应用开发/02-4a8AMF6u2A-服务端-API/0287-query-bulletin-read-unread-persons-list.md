---
title: "查询公告已读未读人员列表"
source_url: "https://open.dingtalk.com/document/development/query-bulletin-read-unread-persons-list"
namespace: "development"
slug: "query-bulletin-read-unread-persons-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "公告 > 查询公告已读未读人员列表"
doc_id: "Wi2b1zCvgU"
updated_at: "2026-06-01 18:25:31"
---

> Source: https://open.dingtalk.com/document/development/query-bulletin-read-unread-persons-list
> Path: 应用开发 / 服务端 API / 公告 > 查询公告已读未读人员列表
> Updated: 2026-06-01 18:25:31

# 查询公告已读未读人员列表

调用本接口，获取指定公告的已读未读人员列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/blackboard/readers |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_manage-钉钉公告管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operationUserId | String | 是 | 操作人userId。 |
| maxResults | Integer | 是 | 每页条目数，最大500。 |
| nextToken | String | 否 | 分页游标。  **[!NOTE]**     - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| blackboardId | String | 是 | 公告id，可通过调用[获取公告ID列表](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/blackboard/readers?operationUserId=manager01&maxResults=200&nextToken=xb1dc&blackboardId=49dc87dc1b30cd099b13a HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a9deamsdk978
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
    public static com.aliyun.dingtalkblackboard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkblackboard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkblackboard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardReadUnReadHeaders queryBlackboardReadUnReadHeaders = new com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardReadUnReadHeaders();
        queryBlackboardReadUnReadHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardReadUnReadRequest queryBlackboardReadUnReadRequest = new com.aliyun.dingtalkblackboard_1_0.models.QueryBlackboardReadUnReadRequest()
                .setOperationUserId("manager01")
                .setMaxResults(200)
                .setNextToken("xb1dc")
                .setBlackboardId("49dc87dc1b30cd099b13a");
        try {
            client.queryBlackboardReadUnReadWithOptions(queryBlackboardReadUnReadRequest, queryBlackboardReadUnReadHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_blackboard_read_un_read_headers = dingtalkblackboard__1__0_models.QueryBlackboardReadUnReadHeaders()
        query_blackboard_read_un_read_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_blackboard_read_un_read_request = dingtalkblackboard__1__0_models.QueryBlackboardReadUnReadRequest(
            operation_user_id='manager01',
            max_results=200,
            next_token='xb1dc',
            blackboard_id='49dc87dc1b30cd099b13a'
        )
        try:
            client.query_blackboard_read_un_read_with_options(query_blackboard_read_un_read_request, query_blackboard_read_un_read_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_blackboard_read_un_read_headers = dingtalkblackboard__1__0_models.QueryBlackboardReadUnReadHeaders()
        query_blackboard_read_un_read_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_blackboard_read_un_read_request = dingtalkblackboard__1__0_models.QueryBlackboardReadUnReadRequest(
            operation_user_id='manager01',
            max_results=200,
            next_token='xb1dc',
            blackboard_id='49dc87dc1b30cd099b13a'
        )
        try:
            await client.query_blackboard_read_un_read_with_options_async(query_blackboard_read_un_read_request, query_blackboard_read_un_read_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Models\QueryBlackboardReadUnReadHeaders;
use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Models\QueryBlackboardReadUnReadRequest;
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
        $queryBlackboardReadUnReadHeaders = new QueryBlackboardReadUnReadHeaders([]);
        $queryBlackboardReadUnReadHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryBlackboardReadUnReadRequest = new QueryBlackboardReadUnReadRequest([
            "operationUserId" => "manager01",
            "maxResults" => 200,
            "nextToken" => "xb1dc",
            "blackboardId" => "49dc87dc1b30cd099b13a"
        ]);
        try {
            $client->queryBlackboardReadUnReadWithOptions($queryBlackboardReadUnReadRequest, $queryBlackboardReadUnReadHeaders, new RuntimeOptions([]));
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
  dingtalkblackboard_1_0  "github.com/alibabacloud-go/dingtalk/blackboard_1_0"
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

  queryBlackboardReadUnReadHeaders := &dingtalkblackboard_1_0.QueryBlackboardReadUnReadHeaders{}
  queryBlackboardReadUnReadHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryBlackboardReadUnReadRequest := &dingtalkblackboard_1_0.QueryBlackboardReadUnReadRequest{
    OperationUserId: tea.String("manager01"),
    MaxResults: tea.Int32(200),
    NextToken: tea.String("xb1dc"),
    BlackboardId: tea.String("49dc87dc1b30cd099b13a"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryBlackboardReadUnReadWithOptions(queryBlackboardReadUnReadRequest, queryBlackboardReadUnReadHeaders, &util.RuntimeOptions{})
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
const dingtalkblackboard_1_0 = require('@alicloud/dingtalk/blackboard_1_0');
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
    return new dingtalkblackboard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryBlackboardReadUnReadHeaders = new dingtalkblackboard_1_0.QueryBlackboardReadUnReadHeaders({ });
    queryBlackboardReadUnReadHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryBlackboardReadUnReadRequest = new dingtalkblackboard_1_0.QueryBlackboardReadUnReadRequest({
      operationUserId: 'manager01',
      maxResults: 200,
      nextToken: 'xb1dc',
      blackboardId: '49dc87dc1b30cd099b13a',
    });
    try {
      await client.queryBlackboardReadUnReadWithOptions(queryBlackboardReadUnReadRequest, queryBlackboardReadUnReadHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardReadUnReadHeaders queryBlackboardReadUnReadHeaders = new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardReadUnReadHeaders();
            queryBlackboardReadUnReadHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardReadUnReadRequest queryBlackboardReadUnReadRequest = new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.QueryBlackboardReadUnReadRequest
            {
                OperationUserId = "manager01",
                MaxResults = 200,
                NextToken = "xb1dc",
                BlackboardId = "49dc87dc1b30cd099b13a",
            };
            try
            {
                client.QueryBlackboardReadUnReadWithOptions(queryBlackboardReadUnReadRequest, queryBlackboardReadUnReadHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | String | 分页游标。 |
| users | Array | 已读未读用户列表。 |
| userId | String | 员工userId。 |
| read | String | 是否已读：   - **true**：已读 - **false**：未读 |
| readTimestamp | Long | 员工已读的时间戳，单位毫秒。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "sometokenabc",
  "users" : [ {
    "userId" : "12039",
    "read" : "true",
    "readTimestamp" : 1688010569000
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | badRequest | %s | 参数错误，请确保 operationUserId、bid、nextToken 等参数合法。 |
| 403 | accessDenied | %s | 请求被拒绝，请确认操作人是企业主管理员或者是公告的发送人，并且公告归属于当前组织。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
