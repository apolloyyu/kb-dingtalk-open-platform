---
title: "查询DingTalkA1小助理分析"
source_url: "https://open.dingtalk.com/document/development/api-querysmartdeviceaisummary"
namespace: "development"
slug: "api-querysmartdeviceaisummary"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 智能硬件 > DingTalk A1 > 查询DingTalkA1小助理分析"
doc_id: "L1hDQhqKPd"
updated_at: "2026-07-03 10:11:27"
---

> Source: https://open.dingtalk.com/document/development/api-querysmartdeviceaisummary
> Path: 应用开发 / 服务端API / 更多开放 > 智能硬件 > DingTalk A1 > 查询DingTalkA1小助理分析
> Updated: 2026-07-03 10:11:27

# 查询DingTalkA1小助理分析

调用本接口，查询DingTalkA1小助理分析结果。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/minutes/smartdevice/aisummary |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Minutes.Content.Read-闪记内容读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | String | 否 | 小助理id，接入[DingTalkA1小助理总结完成事件](../04-LFcRvVD08N-事件订阅/0118-events-aone-assistant-summary-change.md)获取agentId。 |
| openFileId | String | 否 | 录音文件id，接入[DingTalkA1小助理总结完成事件](../04-LFcRvVD08N-事件订阅/0118-events-aone-assistant-summary-change.md)获取fileId。 |

### **请求示例**

HTTP

```
POST /v1.0/minutes/smartdevice/aisummary HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c4bf1xxxx5e9744
Content-Type:application/json

{
  "agentId" : "test-prod",
  "openFileId" : "1THwXxxxxxxxxxxc305aS"
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
    public static com.aliyun.dingtalkminutes_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkminutes_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkminutes_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkminutes_1_0.models.QuerySmartDeviceAiSummaryHeaders querySmartDeviceAiSummaryHeaders = new com.aliyun.dingtalkminutes_1_0.models.QuerySmartDeviceAiSummaryHeaders();
        querySmartDeviceAiSummaryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkminutes_1_0.models.QuerySmartDeviceAiSummaryRequest querySmartDeviceAiSummaryRequest = new com.aliyun.dingtalkminutes_1_0.models.QuerySmartDeviceAiSummaryRequest()
                .setAgentId("test-prod")
                .setOpenFileId("1THwXxxxxxxxxxxc305aS");
        try {
            client.querySmartDeviceAiSummaryWithOptions(querySmartDeviceAiSummaryRequest, querySmartDeviceAiSummaryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.minutes_1_0.client import Client as dingtalkminutes_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.minutes_1_0 import models as dingtalkminutes__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkminutes_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkminutes_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_smart_device_ai_summary_headers = dingtalkminutes__1__0_models.QuerySmartDeviceAiSummaryHeaders()
        query_smart_device_ai_summary_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_smart_device_ai_summary_request = dingtalkminutes__1__0_models.QuerySmartDeviceAiSummaryRequest(
            agent_id='test-prod',
            open_file_id='1THwXxxxxxxxxxxc305aS'
        )
        try:
            client.query_smart_device_ai_summary_with_options(query_smart_device_ai_summary_request, query_smart_device_ai_summary_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_smart_device_ai_summary_headers = dingtalkminutes__1__0_models.QuerySmartDeviceAiSummaryHeaders()
        query_smart_device_ai_summary_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_smart_device_ai_summary_request = dingtalkminutes__1__0_models.QuerySmartDeviceAiSummaryRequest(
            agent_id='test-prod',
            open_file_id='1THwXxxxxxxxxxxc305aS'
        )
        try:
            await client.query_smart_device_ai_summary_with_options_async(query_smart_device_ai_summary_request, query_smart_device_ai_summary_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vminutes_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vminutes_1_0\Models\QuerySmartDeviceAiSummaryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vminutes_1_0\Models\QuerySmartDeviceAiSummaryRequest;
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
        $querySmartDeviceAiSummaryHeaders = new QuerySmartDeviceAiSummaryHeaders([]);
        $querySmartDeviceAiSummaryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $querySmartDeviceAiSummaryRequest = new QuerySmartDeviceAiSummaryRequest([
            "agentId" => "test-prod",
            "openFileId" => "1THwXxxxxxxxxxxc305aS"
        ]);
        try {
            $client->querySmartDeviceAiSummaryWithOptions($querySmartDeviceAiSummaryRequest, $querySmartDeviceAiSummaryHeaders, new RuntimeOptions([]));
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
  dingtalkminutes_1_0  "github.com/alibabacloud-go/dingtalk/minutes_1_0"
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
func CreateClient () (_result *dingtalkminutes_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkminutes_1_0.Client{}
  _result, _err = dingtalkminutes_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  querySmartDeviceAiSummaryHeaders := &dingtalkminutes_1_0.QuerySmartDeviceAiSummaryHeaders{}
  querySmartDeviceAiSummaryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  querySmartDeviceAiSummaryRequest := &dingtalkminutes_1_0.QuerySmartDeviceAiSummaryRequest{
    AgentId: tea.String("test-prod"),
    OpenFileId: tea.String("1THwXxxxxxxxxxxc305aS"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QuerySmartDeviceAiSummaryWithOptions(querySmartDeviceAiSummaryRequest, querySmartDeviceAiSummaryHeaders, &util.RuntimeOptions{})
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
const dingtalkminutes_1_0 = require('@alicloud/dingtalk/minutes_1_0');
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
    return new dingtalkminutes_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let querySmartDeviceAiSummaryHeaders = new dingtalkminutes_1_0.QuerySmartDeviceAiSummaryHeaders({ });
    querySmartDeviceAiSummaryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let querySmartDeviceAiSummaryRequest = new dingtalkminutes_1_0.QuerySmartDeviceAiSummaryRequest({
      agentId: 'test-prod',
      openFileId: '1THwXxxxxxxxxxxc305aS',
    });
    try {
      await client.querySmartDeviceAiSummaryWithOptions(querySmartDeviceAiSummaryRequest, querySmartDeviceAiSummaryHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkminutes_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkminutes_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkminutes_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkminutes_1_0.Models.QuerySmartDeviceAiSummaryHeaders querySmartDeviceAiSummaryHeaders = new AlibabaCloud.SDK.Dingtalkminutes_1_0.Models.QuerySmartDeviceAiSummaryHeaders();
            querySmartDeviceAiSummaryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkminutes_1_0.Models.QuerySmartDeviceAiSummaryRequest querySmartDeviceAiSummaryRequest = new AlibabaCloud.SDK.Dingtalkminutes_1_0.Models.QuerySmartDeviceAiSummaryRequest
            {
                AgentId = "test-prod",
                OpenFileId = "1THwXxxxxxxxxxxc305aS",
            };
            try
            {
                client.QuerySmartDeviceAiSummaryWithOptions(querySmartDeviceAiSummaryRequest, querySmartDeviceAiSummaryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| aiSummaryList | Array | 小助理分析结果列表。 |
| agentId | String | 小助理id。 |
| instanceId | String | 小助理实例id。 |
| templateId | String | 小助理能力模板id。 |
| openFileId | String | 录音文件id。 |
| summary | String | 总结内容。 |
| title | String | 总结标题。 |
| creatorUnionId | String | 创建人unionId。 |
| aiSceneRuleAvatarUrl | String | 小助理能力模板头像。 |
| order | Integer | 小助理分析结果顺序。 |
| state | Integer | 小助理分析结果状态   - **0** ：未生成 - **2** ：已生成 - **3** ：生成失败 - **4** ：生成中 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "aiSummaryList" : [ {
    "agentId" : "test-prod",
    "instanceId" : "eFcgTDZ193gRsbXOZlT5xxxxxxxxxx",
    "templateId" : "test-template-id",
    "openFileId" : "1THwXHxxxxxxxxxylBc305aS",
    "summary" : "summary",
    "title" : "title",
    "creatorUnionId" : "x0iSxxxxiEiE",
    "aiSceneRuleAvatarUrl" : "https://xxx.jpg",
    "order" : 1
  } ],
  "state" : 2
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | query.file.error | query.file.error | 查询文件错误 |
