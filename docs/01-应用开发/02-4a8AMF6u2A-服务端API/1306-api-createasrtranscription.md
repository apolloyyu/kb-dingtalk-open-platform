---
title: "创建ASR离线转写任务"
source_url: "https://open.dingtalk.com/document/development/api-createasrtranscription"
namespace: "development"
slug: "api-createasrtranscription"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 视听智能服务 > 创建ASR离线转写任务"
doc_id: "QnZ6onQ89w"
updated_at: "2026-05-28 17:05:30"
---

> Source: https://open.dingtalk.com/document/development/api-createasrtranscription
> Path: 应用开发 / 服务端API / 更多开放 > 视听智能服务 > 创建ASR离线转写任务
> Updated: 2026-05-28 17:05:30

# 创建ASR离线转写任务

通过本接口，创建音频离线转写任务

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/asr/transcriptions |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Audio.Analysis.Read-钉钉语音智能分析结果读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| url | String | 是 | 音频文件URL，要求可以无身份信息访问。 |
| bizKey | String | 否 | 业务系统自身的ID，可用于异步事件场景与自身的业务系统数据进行关联。 |
| phrases | Array of String | 否 | 热词，不超过10个字符。 |

### 请求示例

HTTP

```
POST /v1.0/dvi/asr/transcriptions HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:3c9f8*****fd2a4f1
Content-Type:application/json

{
  "url" : "https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3",
  "bizKey" : "20260429****1234",
  "phrases" : [ "评测集" ]
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
    public static com.aliyun.dingtalkdvi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdvi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdvi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdvi_1_0.models.CreateAsrTranscriptionHeaders createAsrTranscriptionHeaders = new com.aliyun.dingtalkdvi_1_0.models.CreateAsrTranscriptionHeaders();
        createAsrTranscriptionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.CreateAsrTranscriptionRequest createAsrTranscriptionRequest = new com.aliyun.dingtalkdvi_1_0.models.CreateAsrTranscriptionRequest()
                .setUrl("https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3")
                .setBizKey("20260429****1234")
                .setPhrases(java.util.Arrays.asList(
                    "评测集"
                ));
        try {
            client.createAsrTranscriptionWithOptions(createAsrTranscriptionRequest, createAsrTranscriptionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_asr_transcription_headers = dingtalkdvi__1__0_models.CreateAsrTranscriptionHeaders()
        create_asr_transcription_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_asr_transcription_request = dingtalkdvi__1__0_models.CreateAsrTranscriptionRequest(
            url='https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3',
            biz_key='20260429****1234',
            phrases=[
                '评测集'
            ]
        )
        try:
            client.create_asr_transcription_with_options(create_asr_transcription_request, create_asr_transcription_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_asr_transcription_headers = dingtalkdvi__1__0_models.CreateAsrTranscriptionHeaders()
        create_asr_transcription_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_asr_transcription_request = dingtalkdvi__1__0_models.CreateAsrTranscriptionRequest(
            url='https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3',
            biz_key='20260429****1234',
            phrases=[
                '评测集'
            ]
        )
        try:
            await client.create_asr_transcription_with_options_async(create_asr_transcription_request, create_asr_transcription_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\CreateAsrTranscriptionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\CreateAsrTranscriptionRequest;
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
        $createAsrTranscriptionHeaders = new CreateAsrTranscriptionHeaders([]);
        $createAsrTranscriptionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createAsrTranscriptionRequest = new CreateAsrTranscriptionRequest([
            "url" => "https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3",
            "bizKey" => "20260429****1234",
            "phrases" => [
                "评测集"
            ]
        ]);
        try {
            $client->createAsrTranscriptionWithOptions($createAsrTranscriptionRequest, $createAsrTranscriptionHeaders, new RuntimeOptions([]));
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

  createAsrTranscriptionHeaders := &dingtalkdvi_1_0.CreateAsrTranscriptionHeaders{}
  createAsrTranscriptionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createAsrTranscriptionRequest := &dingtalkdvi_1_0.CreateAsrTranscriptionRequest{
    Url: tea.String("https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3"),
    BizKey: tea.String("20260429****1234"),
    Phrases: []*string{tea.String("评测集")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateAsrTranscriptionWithOptions(createAsrTranscriptionRequest, createAsrTranscriptionHeaders, &util.RuntimeOptions{})
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
    let createAsrTranscriptionHeaders = new dingtalkdvi_1_0.CreateAsrTranscriptionHeaders({ });
    createAsrTranscriptionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createAsrTranscriptionRequest = new dingtalkdvi_1_0.CreateAsrTranscriptionRequest({
      url: 'https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3',
      bizKey: '20260429****1234',
      phrases: [
        '评测集'
      ],
    });
    try {
      await client.createAsrTranscriptionWithOptions(createAsrTranscriptionRequest, createAsrTranscriptionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateAsrTranscriptionHeaders createAsrTranscriptionHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateAsrTranscriptionHeaders();
            createAsrTranscriptionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateAsrTranscriptionRequest createAsrTranscriptionRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateAsrTranscriptionRequest
            {
                Url = "https://**.**.com/audio/2025/07/29/T-6*011A1F_1753773436.mp3",
                BizKey = "20260429****1234",
                Phrases = new List<string>
                {
                    "评测集"
                },
            };
            try
            {
                client.CreateAsrTranscriptionWithOptions(createAsrTranscriptionRequest, createAsrTranscriptionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| taskId | String | 任务ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "taskId" : "v05914****aeba075"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.url.error | URL参数错误 | URL参数错误 |
| 400 | request.permission.denied | api permission denied. | 暂无调用权限 |
| 400 | quotaExceeded.transcription | 转写额度不足 | 转写额度不足 |
| 500 | systemError | 系统异常 | 系统异常 |
