---
title: "查询看鉴记录详情"
source_url: "https://open.dingtalk.com/document/development/api-getkanjianrecord"
namespace: "development"
slug: "api-getkanjianrecord"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > DingTalk BV > 看鉴记录 > 查询看鉴记录详情"
doc_id: "doc_e287c1a5c4114e43"
updated_at: "2026-11-17 17:35:09"
---

> Source: https://open.dingtalk.com/document/development/api-getkanjianrecord
> Path: 应用开发 / 服务端 API / 视听智能服务 > DingTalk BV > 看鉴记录 > 查询看鉴记录详情
> Updated: 2026-11-17 17:35:09

# 查询看鉴记录详情

调用本接口，按记录 ID 查询看鉴 BV 记录详情，返回基础信息、媒体地址、分析版本、AI 描述和当前分析版本生成的总结报告。未生成总结时该字段为空。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/records/detail |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Record.Read-钉钉AI看鉴记录数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recordId | String | 是 | 记录 ID，可通过[分页查询看鉴记录列表](1293-api-listkanjianrecords.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/bv/kanjian/records/detail?recordId=record0001 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0917xxxx18901d52
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
        com.aliyun.dingtalkdvi_1_0.models.GetKanjianRecordHeaders getKanjianRecordHeaders = new com.aliyun.dingtalkdvi_1_0.models.GetKanjianRecordHeaders();
        getKanjianRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.GetKanjianRecordRequest getKanjianRecordRequest = new com.aliyun.dingtalkdvi_1_0.models.GetKanjianRecordRequest()
                .setRecordId("record0001");
        try {
            client.getKanjianRecordWithOptions(getKanjianRecordRequest, getKanjianRecordHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_kanjian_record_headers = dingtalkdvi__1__0_models.GetKanjianRecordHeaders()
        get_kanjian_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_kanjian_record_request = dingtalkdvi__1__0_models.GetKanjianRecordRequest(
            record_id='record0001'
        )
        try:
            client.get_kanjian_record_with_options(get_kanjian_record_request, get_kanjian_record_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_kanjian_record_headers = dingtalkdvi__1__0_models.GetKanjianRecordHeaders()
        get_kanjian_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_kanjian_record_request = dingtalkdvi__1__0_models.GetKanjianRecordRequest(
            record_id='record0001'
        )
        try:
            await client.get_kanjian_record_with_options_async(get_kanjian_record_request, get_kanjian_record_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetKanjianRecordHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetKanjianRecordRequest;
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
        $getKanjianRecordHeaders = new GetKanjianRecordHeaders([]);
        $getKanjianRecordHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getKanjianRecordRequest = new GetKanjianRecordRequest([
            "recordId" => "record0001"
        ]);
        try {
            $client->getKanjianRecordWithOptions($getKanjianRecordRequest, $getKanjianRecordHeaders, new RuntimeOptions([]));
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

  getKanjianRecordHeaders := &dingtalkdvi_1_0.GetKanjianRecordHeaders{}
  getKanjianRecordHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getKanjianRecordRequest := &dingtalkdvi_1_0.GetKanjianRecordRequest{
    RecordId: tea.String("record0001"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetKanjianRecordWithOptions(getKanjianRecordRequest, getKanjianRecordHeaders, &util.RuntimeOptions{})
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
    let getKanjianRecordHeaders = new dingtalkdvi_1_0.GetKanjianRecordHeaders({ });
    getKanjianRecordHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getKanjianRecordRequest = new dingtalkdvi_1_0.GetKanjianRecordRequest({
      recordId: 'record0001',
    });
    try {
      await client.getKanjianRecordWithOptions(getKanjianRecordRequest, getKanjianRecordHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetKanjianRecordHeaders getKanjianRecordHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetKanjianRecordHeaders();
            getKanjianRecordHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetKanjianRecordRequest getKanjianRecordRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetKanjianRecordRequest
            {
                RecordId = "record0001",
            };
            try
            {
                client.GetKanjianRecordWithOptions(getKanjianRecordRequest, getKanjianRecordHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 业务结果。 |
| aiDescription | String | AI 描述文本。 |
| deviceSn | String | 设备序列号。 |
| duration | Long | 时长，毫秒。 |
| endTime | Long | 录制结束时间，毫秒时间戳。 |
| executionId | String | 本次返回内容对应的分析版本 ID。 |
| mainTaskId | String | 关联主任务 ID。 |
| mainTaskTitle | String | 关联主任务标题。 |
| mediaUrl | String | 视频临时签名 URL。 |
| recordId | String | 记录 ID。 |
| reportContent | String | 主任务配置的报告要求文本，不是生成的报告。 |
| startTime | Long | 录制开始时间，毫秒时间戳。 |
| status | String | 记录状态   - **uploading**：上传中 - **uploaded**：已上传 - **pendingAnalysis**：待分析 - **analyzed**：已分析 - **aiSummaried**：已总结 |
| thumbnailUrl | String | 封面临时签名 URL。 |
| title | String | 记录标题。 |
| uploadProgress | Long | 上传进度百分比。 |
| versionNo | Long | 分析版本号。 |
| summary | String | 看鉴总结。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "aiDescription" : "store is clean",
    "deviceSn" : "BV0000000001",
    "duration" : 600000,
    "endTime" : 1760000600000,
    "executionId" : "exec0001",
    "mainTaskId" : "task0001",
    "mainTaskTitle" : "daily-check",
    "mediaUrl" : "https://example.com/media.mp4",
    "recordId" : "record0001",
    "reportContent" : "check shelf and price tags",
    "startTime" : 1760000000000,
    "status" : "aiSummaried",
    "thumbnailUrl" : "https://example.com/thumb.jpg",
    "title" : "store-check",
    "uploadProgress" : 100,
    "versionNo" : 1,
    "summary" : "store check passed"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 参数为空。recordId 必填 | 参数为空。recordId 必填 |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | record.notFound | 看鉴记录不存在或已删除 | 看鉴记录不存在或已删除 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
