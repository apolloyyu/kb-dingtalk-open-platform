---
title: "获取服务表现数据"
source_url: "https://open.dingtalk.com/document/development/api-getservicequalityinspection"
namespace: "development"
slug: "api-getservicequalityinspection"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 视听智能服务 > 获取服务表现数据"
doc_id: "9AcoQnOWFB"
updated_at: "2026-08-06 09:39:08"
---

> Source: https://open.dingtalk.com/document/development/api-getservicequalityinspection
> Path: 应用开发 / 服务端 API / 更多开放 > 视听智能服务 > 获取服务表现数据
> Updated: 2026-08-06 09:39:08

# 获取服务表现数据

通过本接口，根据服务记录ID，获取AI销售管理中的服务表现数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/service/quality-inspections |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Sale.Service.Read-钉钉AI销售管理服务数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recordId | String | 是 | 服务记录ID，可通过[分页获取企业下的服务记录信息](1311-api-listservicerecord.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/service/quality-inspections?recordId=3cb6f9xxxx75fff7 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:00d5bdce4e390
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
        com.aliyun.dingtalkdvi_1_0.models.GetServiceQualityInspectionHeaders getServiceQualityInspectionHeaders = new com.aliyun.dingtalkdvi_1_0.models.GetServiceQualityInspectionHeaders();
        getServiceQualityInspectionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.GetServiceQualityInspectionRequest getServiceQualityInspectionRequest = new com.aliyun.dingtalkdvi_1_0.models.GetServiceQualityInspectionRequest()
                .setRecordId("3cb6f9xxxx75fff7");
        try {
            client.getServiceQualityInspectionWithOptions(getServiceQualityInspectionRequest, getServiceQualityInspectionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_service_quality_inspection_headers = dingtalkdvi__1__0_models.GetServiceQualityInspectionHeaders()
        get_service_quality_inspection_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_service_quality_inspection_request = dingtalkdvi__1__0_models.GetServiceQualityInspectionRequest(
            record_id='3cb6f9xxxx75fff7'
        )
        try:
            client.get_service_quality_inspection_with_options(get_service_quality_inspection_request, get_service_quality_inspection_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_service_quality_inspection_headers = dingtalkdvi__1__0_models.GetServiceQualityInspectionHeaders()
        get_service_quality_inspection_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_service_quality_inspection_request = dingtalkdvi__1__0_models.GetServiceQualityInspectionRequest(
            record_id='3cb6f9xxxx75fff7'
        )
        try:
            await client.get_service_quality_inspection_with_options_async(get_service_quality_inspection_request, get_service_quality_inspection_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetServiceQualityInspectionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetServiceQualityInspectionRequest;
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
        $getServiceQualityInspectionHeaders = new GetServiceQualityInspectionHeaders([]);
        $getServiceQualityInspectionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getServiceQualityInspectionRequest = new GetServiceQualityInspectionRequest([
            "recordId" => "3cb6f9xxxx75fff7"
        ]);
        try {
            $client->getServiceQualityInspectionWithOptions($getServiceQualityInspectionRequest, $getServiceQualityInspectionHeaders, new RuntimeOptions([]));
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

  getServiceQualityInspectionHeaders := &dingtalkdvi_1_0.GetServiceQualityInspectionHeaders{}
  getServiceQualityInspectionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getServiceQualityInspectionRequest := &dingtalkdvi_1_0.GetServiceQualityInspectionRequest{
    RecordId: tea.String("3cb6f9xxxx75fff7"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetServiceQualityInspectionWithOptions(getServiceQualityInspectionRequest, getServiceQualityInspectionHeaders, &util.RuntimeOptions{})
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
    let getServiceQualityInspectionHeaders = new dingtalkdvi_1_0.GetServiceQualityInspectionHeaders({ });
    getServiceQualityInspectionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getServiceQualityInspectionRequest = new dingtalkdvi_1_0.GetServiceQualityInspectionRequest({
      recordId: '3cb6f9xxxx75fff7',
    });
    try {
      await client.getServiceQualityInspectionWithOptions(getServiceQualityInspectionRequest, getServiceQualityInspectionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetServiceQualityInspectionHeaders getServiceQualityInspectionHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetServiceQualityInspectionHeaders();
            getServiceQualityInspectionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetServiceQualityInspectionRequest getServiceQualityInspectionRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetServiceQualityInspectionRequest
            {
                RecordId = "3cb6f9xxxx75fff7",
            };
            try
            {
                client.GetServiceQualityInspectionWithOptions(getServiceQualityInspectionRequest, getServiceQualityInspectionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 查询结果。 |
| score | Integer | 评分。 |
| summary | String | 质检信息摘要。 |
| groupList | Array | 质检组列表。 |
| name | String | 分组名。 |
| itemList | Array | 质检项列表。 |
| flowName | String | 节点名。 |
| isHit | String | 是否命中规则。 |
| reason | String | 分析建议。 |
| script | String | 示例话述。 |
| score | Integer | 质检得分。 |
| name | String | 质检项名称。 |
| highlights | String | 质检识别的话术亮点。 |
| citations | Array | 对话原文引用。 |
| content | String | 原始对话文本。 |
| time | Long | 原文在音频中的时间位移，单位毫秒。 |
| score | Integer | 当前分组的总分。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result": {
    "score": 8,
    "summary": "客户进店表达需求但未获接待",
    "groupList": [{
      "name": "方案报价",
      "itemList": [{
        "flowName": "多级报价",
        "isHit": "false",
        "reason": "未清晰区分实价、活动价、国补价进行报价说明。",
        "script": "我为你做一份预算报价单",
        "score": 2,
        "name": "优惠说明",
        "highlights": "亮点",
        "citations": {
          "content": "你好，这个份大概的预算为1000元",
          "time": 85395
        }
      }],
      "score": 10
    }]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
