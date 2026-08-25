---
title: "获取问答明细"
source_url: "https://open.dingtalk.com/document/development/api-getaskdetail"
namespace: "development"
slug: "api-getaskdetail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 助理管理 > 知识管理 > 获取问答明细"
doc_id: "a9yGyomWOG"
updated_at: "2026-03-06 09:22:59"
---

> Source: https://open.dingtalk.com/document/development/api-getaskdetail
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 助理管理 > 知识管理 > 获取问答明细
> Updated: 2026-03-06 09:22:59

# 获取问答明细

获取问答明细，可以获取到用户问AI助理的明细信息，包括用户的问题，助理的回答，回答的引用来源等。

> **[!IMPORTANT]**
>
> 本文档已于 2026年 03 月 05 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方企业应用 | 暂不支持 | 暂不支持 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
GET /v1.0/assistant/askDetails?assistantId=String&offset=Long&pageSize=Integer&startTime=Long&endTime=Long HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| assistantId | String | 是 | 助理 ID。  **[!NOTE]**    调用该接口前需经**用户委托授权**后才可正常调用，未授权时调用该接口会返回"参数错误"的提示。 |
| offset | Long | 是 | 查询的游标。 |
| pageSize | Integer | 是 | 查询的个数。 |
| startTime | Long | 否 | 查询的开始时间。 |
| endTime | Long | 否 | 查询结束的时间。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 接口是否成功。 |
| result | Object | 结果。 |
| list | Array | 问答明细列表。 |
| nick | String | 提问者昵称。 |
| time | Long | 提问时间。 |
| question | String | 提问问题。 |
| answer | String | 答案。 |
| answerResult | String | 答案来源：   - FROM\_SPECIFIC\_KNOWLEDGE：通过上传知识反馈结果 - NO\_ANSWER：通过上传知识未反馈结果 - FROM\_PUBLIC\_NETWORK：通过网络知识反馈结果 |
| references | Array |  |
| name | String | 文档名称。 |
| url | String | 文档链接。 |
| isMarkResolved | Boolean | 是否被用户标记为有帮助：   - true：标记为有帮助 - false：标记为无帮助 - null：用户未评论 |
| commentTags | Array of String | 用户评论。 |
| hasMore | Boolean | 是否有更多结果。 |
| nextCursor | Long | 下一页的游标。 |
| totalCount | Integer | 结果总数。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/assistant/askDetails?assistantId=02125927e37b4a8f86da0e57125038&offset=0&pageSize=3&startTime=0&endTime=1722505491000 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f2a6d208b64432df8eea4a9a937c95cb
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
    public static com.aliyun.dingtalkassistant_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkassistant_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkassistant_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkassistant_1_0.models.GetAskDetailHeaders getAskDetailHeaders = new com.aliyun.dingtalkassistant_1_0.models.GetAskDetailHeaders();
        getAskDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkassistant_1_0.models.GetAskDetailRequest getAskDetailRequest = new com.aliyun.dingtalkassistant_1_0.models.GetAskDetailRequest()
                .setAssistantId("02125927e37b4a8f86da0e57125038")
                .setOffset(0L)
                .setPageSize(3)
                .setStartTime(0L)
                .setEndTime(1722505491000L);
        try {
            client.getAskDetailWithOptions(getAskDetailRequest, getAskDetailHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.assistant_1_0.client import Client as dingtalkassistant_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.assistant_1_0 import models as dingtalkassistant__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkassistant_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkassistant_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_ask_detail_headers = dingtalkassistant__1__0_models.GetAskDetailHeaders()
        get_ask_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_ask_detail_request = dingtalkassistant__1__0_models.GetAskDetailRequest(
            assistant_id='02125927e37b4a8f86da0e57125038',
            offset=0,
            page_size=3,
            start_time=0,
            end_time=1722505491000
        )
        try:
            client.get_ask_detail_with_options(get_ask_detail_request, get_ask_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_ask_detail_headers = dingtalkassistant__1__0_models.GetAskDetailHeaders()
        get_ask_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_ask_detail_request = dingtalkassistant__1__0_models.GetAskDetailRequest(
            assistant_id='02125927e37b4a8f86da0e57125038',
            offset=0,
            page_size=3,
            start_time=0,
            end_time=1722505491000
        )
        try:
            await client.get_ask_detail_with_options_async(get_ask_detail_request, get_ask_detail_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\GetAskDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\GetAskDetailRequest;
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
        $getAskDetailHeaders = new GetAskDetailHeaders([]);
        $getAskDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getAskDetailRequest = new GetAskDetailRequest([
            "assistantId" => "02125927e37b4a8f86da0e57125038",
            "offset" => 0,
            "pageSize" => 3,
            "startTime" => 0,
            "endTime" => 1722505491000
        ]);
        try {
            $client->getAskDetailWithOptions($getAskDetailRequest, $getAskDetailHeaders, new RuntimeOptions([]));
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
  dingtalkassistant_1_0  "github.com/alibabacloud-go/dingtalk/assistant_1_0"
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
func CreateClient () (_result *dingtalkassistant_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkassistant_1_0.Client{}
  _result, _err = dingtalkassistant_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getAskDetailHeaders := &dingtalkassistant_1_0.GetAskDetailHeaders{}
  getAskDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getAskDetailRequest := &dingtalkassistant_1_0.GetAskDetailRequest{
    AssistantId: tea.String("02125927e37b4a8f86da0e57125038"),
    Offset: tea.Int64(0),
    PageSize: tea.Int32(3),
    StartTime: tea.Int64(0),
    EndTime: tea.Int64(1722505491000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAskDetailWithOptions(getAskDetailRequest, getAskDetailHeaders, &util.RuntimeOptions{})
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
const dingtalkassistant_1_0 = require('@alicloud/dingtalk/assistant_1_0');
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
    return new dingtalkassistant_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getAskDetailHeaders = new dingtalkassistant_1_0.GetAskDetailHeaders({ });
    getAskDetailHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getAskDetailRequest = new dingtalkassistant_1_0.GetAskDetailRequest({
      assistantId: '02125927e37b4a8f86da0e57125038',
      offset: 0,
      pageSize: 3,
      startTime: 0,
      endTime: 1722505491000,
    });
    try {
      await client.getAskDetailWithOptions(getAskDetailRequest, getAskDetailHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkassistant_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkassistant_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.GetAskDetailHeaders getAskDetailHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.GetAskDetailHeaders();
            getAskDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.GetAskDetailRequest getAskDetailRequest = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.GetAskDetailRequest
            {
                AssistantId = "02125927e37b4a8f86da0e57125038",
                Offset = 0,
                PageSize = 3,
                StartTime = 0,
                EndTime = 1722505491000,
            };
            try
            {
                client.GetAskDetailWithOptions(getAskDetailRequest, getAskDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "list" : [ {
      "nick" : "张三",
      "time" : 1722505491000,
      "question" : "钉钉是什么",
      "answer" : "钉钉是",
      "answerResult" : "FROM_SPECIFIC_KNOWLEDGE",
      "references" : [ {
        "name" : "钉钉是什么",
        "url" : "http://www.dingtalk.com"
      } ],
      "isMarkResolved" : true,
      "commentTags" : [ ]
    } ],
    "hasMore" : false,
    "nextCursor" : 3,
    "totalCount" : 3
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | url.parameter.error | 参数错误:%s | 参数错误 |
