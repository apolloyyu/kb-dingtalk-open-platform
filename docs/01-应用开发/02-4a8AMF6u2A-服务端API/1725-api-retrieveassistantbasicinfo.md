---
title: "查询 AI 助理基本信息"
source_url: "https://open.dingtalk.com/document/development/api-retrieveassistantbasicinfo"
namespace: "development"
slug: "api-retrieveassistantbasicinfo"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 助理管理 > 查询 AI 助理基本信息"
doc_id: "g8goNKXdT4"
updated_at: "2026-03-06 09:22:51"
---

> Source: https://open.dingtalk.com/document/development/api-retrieveassistantbasicinfo
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 助理管理 > 查询 AI 助理基本信息
> Updated: 2026-03-06 09:22:51

# 查询 AI 助理基本信息

调用本接口，查询 AI 助理基本信息，包括名称、描述等。

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
GET /v1.0/assistant/basicInfo?unionId=String&assistantId=String HTTP/1.1
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
| unionId | String | 是 | 助理创建人 ID。 |
| assistantId | String | 是 | AI助理的唯一标识符。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| assistantId | String | AI 助理的 ID。 |
| name | String | AI 助理的名称。 |
| description | String | AI 助理的描述。 |
| createdAt | Long | 助理的创建时间，单位：秒。 |
| model | String | 助理使用的大模型。默认为空，表示由钉钉自动选择。 |
| instructions | String | 角色设定。 |
| unifiedAppId | String | 助理管理的应用对应的应用 ID。 |
| icon | String | 助理头像。 |
| welcomeContent | String | 欢迎语。 |
| recommendPrompts | Array of String | 推荐问法。 |
| creatorUnionId | String | 助理创建者的 Union ID。 |
| fallbackContent | String | 兜底回复。 |
| knowledgeFileNames | Array of String | 知识名称。 |
| actionNames | Array of String | 技能名称。 |
| assistantUnionId | String | 助理的 Union ID。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/assistant/basicInfo?unionId=H20***wiE&assistantId=5eb***296 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:ffc***ff6
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
        com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantBasicInfoHeaders retrieveAssistantBasicInfoHeaders = new com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantBasicInfoHeaders();
        retrieveAssistantBasicInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantBasicInfoRequest retrieveAssistantBasicInfoRequest = new com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantBasicInfoRequest()
                .setUnionId("H20***wiE")
                .setAssistantId("5eb***296");
        try {
            client.retrieveAssistantBasicInfoWithOptions(retrieveAssistantBasicInfoRequest, retrieveAssistantBasicInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        retrieve_assistant_basic_info_headers = dingtalkassistant__1__0_models.RetrieveAssistantBasicInfoHeaders()
        retrieve_assistant_basic_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        retrieve_assistant_basic_info_request = dingtalkassistant__1__0_models.RetrieveAssistantBasicInfoRequest(
            union_id='H20***wiE',
            assistant_id='5eb***296'
        )
        try:
            client.retrieve_assistant_basic_info_with_options(retrieve_assistant_basic_info_request, retrieve_assistant_basic_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        retrieve_assistant_basic_info_headers = dingtalkassistant__1__0_models.RetrieveAssistantBasicInfoHeaders()
        retrieve_assistant_basic_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        retrieve_assistant_basic_info_request = dingtalkassistant__1__0_models.RetrieveAssistantBasicInfoRequest(
            union_id='H20***wiE',
            assistant_id='5eb***296'
        )
        try:
            await client.retrieve_assistant_basic_info_with_options_async(retrieve_assistant_basic_info_request, retrieve_assistant_basic_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\RetrieveAssistantBasicInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\RetrieveAssistantBasicInfoRequest;
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
        $retrieveAssistantBasicInfoHeaders = new RetrieveAssistantBasicInfoHeaders([]);
        $retrieveAssistantBasicInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $retrieveAssistantBasicInfoRequest = new RetrieveAssistantBasicInfoRequest([
            "unionId" => "H20***wiE",
            "assistantId" => "5eb***296"
        ]);
        try {
            $client->retrieveAssistantBasicInfoWithOptions($retrieveAssistantBasicInfoRequest, $retrieveAssistantBasicInfoHeaders, new RuntimeOptions([]));
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

  retrieveAssistantBasicInfoHeaders := &dingtalkassistant_1_0.RetrieveAssistantBasicInfoHeaders{}
  retrieveAssistantBasicInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  retrieveAssistantBasicInfoRequest := &dingtalkassistant_1_0.RetrieveAssistantBasicInfoRequest{
    UnionId: tea.String("H20***wiE"),
    AssistantId: tea.String("5eb***296"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RetrieveAssistantBasicInfoWithOptions(retrieveAssistantBasicInfoRequest, retrieveAssistantBasicInfoHeaders, &util.RuntimeOptions{})
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
    let retrieveAssistantBasicInfoHeaders = new dingtalkassistant_1_0.RetrieveAssistantBasicInfoHeaders({ });
    retrieveAssistantBasicInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let retrieveAssistantBasicInfoRequest = new dingtalkassistant_1_0.RetrieveAssistantBasicInfoRequest({
      unionId: 'H20***wiE',
      assistantId: '5eb***296',
    });
    try {
      await client.retrieveAssistantBasicInfoWithOptions(retrieveAssistantBasicInfoRequest, retrieveAssistantBasicInfoHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantBasicInfoHeaders retrieveAssistantBasicInfoHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantBasicInfoHeaders();
            retrieveAssistantBasicInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantBasicInfoRequest retrieveAssistantBasicInfoRequest = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantBasicInfoRequest
            {
                UnionId = "H20***wiE",
                AssistantId = "5eb***296",
            };
            try
            {
                client.RetrieveAssistantBasicInfoWithOptions(retrieveAssistantBasicInfoRequest, retrieveAssistantBasicInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "assistantId" : "5eb***296",
  "name" : "天气助理",
  "description" : "我可以帮助你查看天气",
  "createdAt" : 1722947268,
  "model" : "qwen-max",
  "instructions" : "你是一名***",
  "unifiedAppId" : "7f1***7bc",
  "icon" : "@lQ***ZAA",
  "welcomeContent" : "我是你在职场***",
  "recommendPrompts" : [ "查看明天杭州的天气" ],
  "creatorUnionId" : "H20***wiE",
  "fallbackContent" : "对不起，无法处理这类请求，请联系***",
  "knowledgeFileNames" : [ "天气指南.pdf" ],
  "actionNames" : [ "天气查询" ],
  "assistantUnionId" : "123"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.parameter | 非法参数 | 非法参数 |
| 500 | system.error | 系统异常 | 系统异常 |
