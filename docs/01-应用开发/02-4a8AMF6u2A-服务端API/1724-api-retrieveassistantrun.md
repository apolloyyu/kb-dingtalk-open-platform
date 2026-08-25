---
title: "获取AI助理的运行任务"
source_url: "https://open.dingtalk.com/document/development/api-retrieveassistantrun"
namespace: "development"
slug: "api-retrieveassistantrun"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 运行 > 获取AI助理的运行任务"
doc_id: "kM6NBK4mLN"
updated_at: "2026-03-06 09:22:48"
---

> Source: https://open.dingtalk.com/document/development/api-retrieveassistantrun
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 运行 > 获取AI助理的运行任务
> Updated: 2026-03-06 09:22:48

# 获取AI助理的运行任务

根据线程id和运行任务id，获取对应的运行任务。访问本接口请申请应用权限进行访问。

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
GET /v1.0/assistant/threads/{threadId}/runs/{runId} HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| threadId | String | 是 | 运行任务关联的线程id。 |
| runId | String | 是 | 运行任务id。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| id | String | 运行任务id。 |
| createdAt | Long | 运行任务的创建时间，毫秒时间戳。 |
| threadId | String | 运行任务关联的线程id。 |
| assistantId | String | 运行任务关联的助理id。 |
| status | String | 运行任务的状态，枚举值有：   - queued：运行任务在排队等待 - in\_progress：运行任务正在执行中 - failed：运行任务失败 - completed：运行任务完成 |
| lastErrorMsg | String | 运行任务最新一次失败的失败消息。 |
| expiresAt | Long | 运行任务的过期时间，毫秒时间戳。 |
| startedAt | Long | 运行任务的开始时间，毫秒时间戳。 |
| cancelledAt | Long | 运行任务的取消时间，毫秒时间戳。 |
| failedAt | Long | 运行任务的失败时间，毫秒时间戳。 |
| completedAt | Long | 运行任务的完成时间，毫秒时间戳。 |
| metadata | Map | 保留字段，用于扩展使用，暂无实际意义。 |
| object | String | 对象类型，默认为 thread.run。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/assistant/threads/thread_message_95f***abb/runs/run_73d***f2c HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token123
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
        com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantRunHeaders retrieveAssistantRunHeaders = new com.aliyun.dingtalkassistant_1_0.models.RetrieveAssistantRunHeaders();
        retrieveAssistantRunHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.retrieveAssistantRunWithOptions("thread_message_95f***abb", "run_73d***f2c", retrieveAssistantRunHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        retrieve_assistant_run_headers = dingtalkassistant__1__0_models.RetrieveAssistantRunHeaders()
        retrieve_assistant_run_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.retrieve_assistant_run_with_options('thread_message_95f***abb', 'run_73d***f2c', retrieve_assistant_run_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        retrieve_assistant_run_headers = dingtalkassistant__1__0_models.RetrieveAssistantRunHeaders()
        retrieve_assistant_run_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.retrieve_assistant_run_with_options_async('thread_message_95f***abb', 'run_73d***f2c', retrieve_assistant_run_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\RetrieveAssistantRunHeaders;
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
        $retrieveAssistantRunHeaders = new RetrieveAssistantRunHeaders([]);
        $retrieveAssistantRunHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->retrieveAssistantRunWithOptions("thread_message_95f***abb", "run_73d***f2c", $retrieveAssistantRunHeaders, new RuntimeOptions([]));
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

  retrieveAssistantRunHeaders := &dingtalkassistant_1_0.RetrieveAssistantRunHeaders{}
  retrieveAssistantRunHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RetrieveAssistantRunWithOptions(tea.String("thread_message_95f***abb"), tea.String("run_73d***f2c"), retrieveAssistantRunHeaders, &util.RuntimeOptions{})
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
    let retrieveAssistantRunHeaders = new dingtalkassistant_1_0.RetrieveAssistantRunHeaders({ });
    retrieveAssistantRunHeaders.xAcsDingtalkAccessToken = '<your access token>';
    try {
      await client.retrieveAssistantRunWithOptions('thread_message_95f***abb', 'run_73d***f2c', retrieveAssistantRunHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantRunHeaders retrieveAssistantRunHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.RetrieveAssistantRunHeaders();
            retrieveAssistantRunHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.RetrieveAssistantRunWithOptions("thread_message_95f***abb", "run_73d***f2c", retrieveAssistantRunHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "id" : "run_73d***f2c",
  "createdAt" : 1721980599206,
  "threadId" : "thread_message_95f***abb",
  "assistantId" : "d748***965",
  "status" : "completed",
  "lastErrorMsg" : "null",
  "expiresAt" : 1721980599206,
  "startedAt" : 1721980599206,
  "cancelledAt" : 1721980599206,
  "failedAt" : 1721980599206,
  "completedAt" : 1721980599300,
  "object" : "thread.run"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | run.params.error | %s | 传入的参数中ThreadId或者RunId不存在，请检查后重试 |
| 500 | run.retrieve.exception | %s | 系统繁忙，请稍后重试(E000114) |
| 500 | run.retrieve.error | %s | 系统繁忙，请稍后重试(E000004) |
