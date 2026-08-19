---
title: "查询ASR转写结果"
source_url: "https://open.dingtalk.com/document/development/api-getasrtranscription"
namespace: "development"
slug: "api-getasrtranscription"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 视听智能服务 > 查询ASR转写结果"
doc_id: "WDfu3TWxLL"
updated_at: "2026-05-28 17:05:30"
---

> Source: https://open.dingtalk.com/document/development/api-getasrtranscription
> Path: 应用开发 / 服务端API / 更多开放 > 视听智能服务 > 查询ASR转写结果
> Updated: 2026-05-28 17:05:30

# 查询ASR转写结果

通过本接口，查询[创建ASR离线转写任务]的转写结果。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/asr/transcriptions |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Audio.Analysis.Read-钉钉语音智能分析结果读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 是 | ASR离线转写任务ID，通过[创建ASR离线转写任务](1306-api-createasrtranscription.md)接口返回。 |
| maxResults | Integer | 否 | 返回的数据条数，最大50。 |
| nextToken | String | 否 | 下一页的数据的查询标识，首次查询为空，分页查询中后续的每一次查询需要传入上次返回的nextToken。 |

### 请求示例

HTTP

```
GET /v1.0/dvi/asr/transcriptions?taskId=v059146****ba075&maxResults=20&nextToken=3780*****7ffce6 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:36f****e91c
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
        com.aliyun.dingtalkdvi_1_0.models.GetAsrTranscriptionHeaders getAsrTranscriptionHeaders = new com.aliyun.dingtalkdvi_1_0.models.GetAsrTranscriptionHeaders();
        getAsrTranscriptionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.GetAsrTranscriptionRequest getAsrTranscriptionRequest = new com.aliyun.dingtalkdvi_1_0.models.GetAsrTranscriptionRequest()
                .setTaskId("v059146****ba075")
                .setMaxResults(20)
                .setNextToken("3780*****7ffce6");
        try {
            client.getAsrTranscriptionWithOptions(getAsrTranscriptionRequest, getAsrTranscriptionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_asr_transcription_headers = dingtalkdvi__1__0_models.GetAsrTranscriptionHeaders()
        get_asr_transcription_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_asr_transcription_request = dingtalkdvi__1__0_models.GetAsrTranscriptionRequest(
            task_id='v059146****ba075',
            max_results=20,
            next_token='3780*****7ffce6'
        )
        try:
            client.get_asr_transcription_with_options(get_asr_transcription_request, get_asr_transcription_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_asr_transcription_headers = dingtalkdvi__1__0_models.GetAsrTranscriptionHeaders()
        get_asr_transcription_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_asr_transcription_request = dingtalkdvi__1__0_models.GetAsrTranscriptionRequest(
            task_id='v059146****ba075',
            max_results=20,
            next_token='3780*****7ffce6'
        )
        try:
            await client.get_asr_transcription_with_options_async(get_asr_transcription_request, get_asr_transcription_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetAsrTranscriptionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetAsrTranscriptionRequest;
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
        $getAsrTranscriptionHeaders = new GetAsrTranscriptionHeaders([]);
        $getAsrTranscriptionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getAsrTranscriptionRequest = new GetAsrTranscriptionRequest([
            "taskId" => "v059146****ba075",
            "maxResults" => 20,
            "nextToken" => "3780*****7ffce6"
        ]);
        try {
            $client->getAsrTranscriptionWithOptions($getAsrTranscriptionRequest, $getAsrTranscriptionHeaders, new RuntimeOptions([]));
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

  getAsrTranscriptionHeaders := &dingtalkdvi_1_0.GetAsrTranscriptionHeaders{}
  getAsrTranscriptionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getAsrTranscriptionRequest := &dingtalkdvi_1_0.GetAsrTranscriptionRequest{
    TaskId: tea.String("v059146****ba075"),
    MaxResults: tea.Int32(20),
    NextToken: tea.String("3780*****7ffce6"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAsrTranscriptionWithOptions(getAsrTranscriptionRequest, getAsrTranscriptionHeaders, &util.RuntimeOptions{})
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
    let getAsrTranscriptionHeaders = new dingtalkdvi_1_0.GetAsrTranscriptionHeaders({ });
    getAsrTranscriptionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getAsrTranscriptionRequest = new dingtalkdvi_1_0.GetAsrTranscriptionRequest({
      taskId: 'v059146****ba075',
      maxResults: 20,
      nextToken: '3780*****7ffce6',
    });
    try {
      await client.getAsrTranscriptionWithOptions(getAsrTranscriptionRequest, getAsrTranscriptionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAsrTranscriptionHeaders getAsrTranscriptionHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAsrTranscriptionHeaders();
            getAsrTranscriptionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAsrTranscriptionRequest getAsrTranscriptionRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAsrTranscriptionRequest
            {
                TaskId = "v059146****ba075",
                MaxResults = 20,
                NextToken = "3780*****7ffce6",
            };
            try
            {
                client.GetAsrTranscriptionWithOptions(getAsrTranscriptionRequest, getAsrTranscriptionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 分页查询结果。 |
| taskId | String | 任务ID。 |
| bizKey | String | 调用方传入的业务key。 |
| taskStatus | String | 任务状态：   - **PENDING**：待执行 - **RUNNING**：转写中 - **SUCCEEDED**：转写成功 - **FAILED**：转写失败 |
| resultInfo | Object | 转写结果，只有状态是成功时返回转写结果。 |
| paragraphList | Array | 对话章节。 |
| speakerId | String | 发言人编号。 |
| startTime | Long | 发言开始时间（毫秒），相对整段音频的时间偏移量。 |
| endTime | Long | 发言结束时间（毫秒），相对整段音频的时间偏移量。 |
| paragraph | String | 发言段落文本。 |
| nextToken | String | 有多页数据时，下一页数据的起始标识。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "taskId" : "v059146****ba075",
    "bizKey" : "20260429*****1234",
    "taskStatus" : "SUCCEEDED",
    "resultInfo" : {
      "paragraphList" : [ {
        "speakerId" : "1",
        "startTime" : 200,
        "endTime" : 2520,
        "paragraph" : "你好，欢迎光临。"
      } ]
    },
    "nextToken" : "2f728ff***8b33d"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | task.notFound | task.not.found | task not found |
| 500 | systemError | system error. | 系统异常 |
