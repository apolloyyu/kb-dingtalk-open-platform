---
title: "获取用户创建的AI助理列表"
source_url: "https://open.dingtalk.com/document/development/assistant-acquires-list-assistants-created-by-users"
namespace: "development"
slug: "assistant-acquires-list-assistants-created-by-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 助理管理 > 获取用户创建的AI助理列表"
doc_id: "kZdhPeCErE"
updated_at: "2026-03-06 09:22:52"
---

> Source: https://open.dingtalk.com/document/development/assistant-acquires-list-assistants-created-by-users
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 助理管理 > 获取用户创建的AI助理列表
> Updated: 2026-03-06 09:22:52

# 获取用户创建的AI助理列表

获取用户创建的AI助理列表，需要传入助理创建者的用户 ID （Union ID）。

> **[!IMPORTANT]**
>
> 本文档已于 2026年 03 月 05 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
GET /v1.0/assistant/list?unionId=String&cursor=Long&pageSize=Integer HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 助理创建者的 Union ID。 |
| cursor | Long | 否 | 分页查询的游标，下一次游标值通过该接口的响应中 nextCursor 参数确定。 |
| pageSize | Integer | 是 | 每页的元素个数。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| hasMore | Boolean | 是否有下一页。 |
| nextCursor | Long | 下一页的游标值。 |
| totalCount | Integer | 结果总数。 |
| list | Array | 助理列表。 |
| assistantId | String | AI 助理的唯一标识符。 |
| name | String | 助理的名称。 |
| description | String | 助理的描述。 |
| icon | String | 助理的头像，采用钉钉多媒体文件标识符 Media ID 表示。 |
| creatorUnionId | String | 助理创建者 ID（Union ID）。 |
| createdAt | Long | 助理的创建时间，Unix 时间戳格式，单位秒。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/assistant/list?unionId=H20***wiE&cursor=0&pageSize=20 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:17c***209
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
        com.aliyun.dingtalkassistant_1_0.models.ListAssistantHeaders listAssistantHeaders = new com.aliyun.dingtalkassistant_1_0.models.ListAssistantHeaders();
        listAssistantHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkassistant_1_0.models.ListAssistantRequest listAssistantRequest = new com.aliyun.dingtalkassistant_1_0.models.ListAssistantRequest()
                .setUnionId("H20***wiE")
                .setCursor(0L)
                .setPageSize(20);
        try {
            client.listAssistantWithOptions(listAssistantRequest, listAssistantHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_assistant_headers = dingtalkassistant__1__0_models.ListAssistantHeaders()
        list_assistant_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_assistant_request = dingtalkassistant__1__0_models.ListAssistantRequest(
            union_id='H20***wiE',
            cursor=0,
            page_size=20
        )
        try:
            client.list_assistant_with_options(list_assistant_request, list_assistant_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_assistant_headers = dingtalkassistant__1__0_models.ListAssistantHeaders()
        list_assistant_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_assistant_request = dingtalkassistant__1__0_models.ListAssistantRequest(
            union_id='H20***wiE',
            cursor=0,
            page_size=20
        )
        try:
            await client.list_assistant_with_options_async(list_assistant_request, list_assistant_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\ListAssistantHeaders;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\ListAssistantRequest;
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
        $listAssistantHeaders = new ListAssistantHeaders([]);
        $listAssistantHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listAssistantRequest = new ListAssistantRequest([
            "unionId" => "H20***wiE",
            "cursor" => 0,
            "pageSize" => 20
        ]);
        try {
            $client->listAssistantWithOptions($listAssistantRequest, $listAssistantHeaders, new RuntimeOptions([]));
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

  listAssistantHeaders := &dingtalkassistant_1_0.ListAssistantHeaders{}
  listAssistantHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listAssistantRequest := &dingtalkassistant_1_0.ListAssistantRequest{
    UnionId: tea.String("H20***wiE"),
    Cursor: tea.Int64(0),
    PageSize: tea.Int32(20),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListAssistantWithOptions(listAssistantRequest, listAssistantHeaders, &util.RuntimeOptions{})
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
    let listAssistantHeaders = new dingtalkassistant_1_0.ListAssistantHeaders({ });
    listAssistantHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listAssistantRequest = new dingtalkassistant_1_0.ListAssistantRequest({
      unionId: 'H20***wiE',
      cursor: 0,
      pageSize: 20,
    });
    try {
      await client.listAssistantWithOptions(listAssistantRequest, listAssistantHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.ListAssistantHeaders listAssistantHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.ListAssistantHeaders();
            listAssistantHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.ListAssistantRequest listAssistantRequest = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.ListAssistantRequest
            {
                UnionId = "H20***wiE",
                Cursor = 0,
                PageSize = 20,
            };
            try
            {
                client.ListAssistantWithOptions(listAssistantRequest, listAssistantHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "hasMore" : true,
  "nextCursor" : 65536,
  "totalCount" : 128,
  "list" : [ {
    "assistantId" : "5eb***296",
    "name" : "天气助理",
    "description" : "查看最新的天气信息",
    "icon" : "@lQ***ZAA",
    "creatorUnionId" : "H20***wiE",
    "createdAt" : 1722947268
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.parameter | 参数错误 | 参数错误 |
| 500 | system.error | 系统异常 | 系统异常 |
