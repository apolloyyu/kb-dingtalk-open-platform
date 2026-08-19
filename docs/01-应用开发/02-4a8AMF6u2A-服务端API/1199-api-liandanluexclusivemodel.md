---
title: "炼丹炉专属模型服务"
source_url: "https://open.dingtalk.com/document/development/api-liandanluexclusivemodel"
namespace: "development"
slug: "api-liandanluexclusivemodel"
group: "应用开发"
tab: "服务端API"
breadcrumb: "炼丹炉（模型服务） > 炼丹炉专属模型服务"
doc_id: "HHkcQSu1d8"
updated_at: "2025-10-09 18:07:13"
---

> Source: https://open.dingtalk.com/document/development/api-liandanluexclusivemodel
> Path: 应用开发 / 服务端API / 炼丹炉（模型服务） > 炼丹炉专属模型服务
> Updated: 2025-10-09 18:07:13

# 炼丹炉专属模型服务

通过使用炼丹炉训练得到专属模型，使用该服务可以访问炼丹炉上发布的模型服务。

## 接口调用说明

本接口已发布迭代，请参考符合行业规范的大模型接口，参考[大模型推理服务（文生文模型）](1200-api-exclusivemodelcompleteservice.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/aiPaaS/ai/generate |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-AIPaaS.Model.Read-炼丹炉模型读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| module | String | 是 | 功能模块标识，主要是记录使用大模型使用场景，用户自己定义该参数值，纯英文格式。 |
| modelId | String | 是 | 模型ID，炼丹炉平台内模型上线部署后，点击查看，可获取模型ID。 |
| prompt | String | 是 | 输入的问题。 |
| userId | String | 是 | 当前用户的userId。 |

### 请求示例

HTTP

```
POST /v1.0/aiPaaS/ai/generate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token
Content-Type:application/json

{
  "module" : "QA",
  "modelId" : "maas1234",
  "prompt" : "OKR是什么",
  "userId" : "123"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkai_paa_s_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkai_paa_s_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkai_paa_s_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkai_paa_s_1_0.models.LiandanluExclusiveModelHeaders liandanluExclusiveModelHeaders = new com.aliyun.dingtalkai_paa_s_1_0.models.LiandanluExclusiveModelHeaders();
        liandanluExclusiveModelHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkai_paa_s_1_0.models.LiandanluExclusiveModelRequest liandanluExclusiveModelRequest = new com.aliyun.dingtalkai_paa_s_1_0.models.LiandanluExclusiveModelRequest()
                .setModuleType("GENERAL")
                .setModelCode("maas1234")
                .setPrompt("OKR是什么")
                .setUserId("使用该功能的用户id");
        try {
            client.liandanluExclusiveModelWithOptions(liandanluExclusiveModelRequest, liandanluExclusiveModelHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.aiPaaS_1_0.client import Client as dingtalkaiPaaS_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.aiPaaS_1_0 import models as dingtalkai_paa_s__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkaiPaaS_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkaiPaaS_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        liandanlu_exclusive_model_headers = dingtalkai_paa_s__1__0_models.LiandanluExclusiveModelHeaders()
        liandanlu_exclusive_model_headers.x_acs_dingtalk_access_token = '<your access token>'
        liandanlu_exclusive_model_request = dingtalkai_paa_s__1__0_models.LiandanluExclusiveModelRequest(
            module_type='GENERAL',
            model_code='maas1234',
            prompt='OKR是什么',
            user_id='使用该功能的用户id'
        )
        try:
            client.liandanlu_exclusive_model_with_options(liandanlu_exclusive_model_request, liandanlu_exclusive_model_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        liandanlu_exclusive_model_headers = dingtalkai_paa_s__1__0_models.LiandanluExclusiveModelHeaders()
        liandanlu_exclusive_model_headers.x_acs_dingtalk_access_token = '<your access token>'
        liandanlu_exclusive_model_request = dingtalkai_paa_s__1__0_models.LiandanluExclusiveModelRequest(
            module_type='GENERAL',
            model_code='maas1234',
            prompt='OKR是什么',
            user_id='使用该功能的用户id'
        )
        try:
            await client.liandanlu_exclusive_model_with_options_async(liandanlu_exclusive_model_request, liandanlu_exclusive_model_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Models\LiandanluExclusiveModelHeaders;
use AlibabaCloud\SDK\Dingtalk\Vai_paa_s_1_0\Models\LiandanluExclusiveModelRequest;
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
        $liandanluExclusiveModelHeaders = new LiandanluExclusiveModelHeaders([]);
        $liandanluExclusiveModelHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $liandanluExclusiveModelRequest = new LiandanluExclusiveModelRequest([
            "moduleType" => "GENERAL",
            "modelCode" => "maas1234",
            "prompt" => "OKR是什么",
            "userId" => "使用该功能的用户id"
        ]);
        try {
            $client->liandanluExclusiveModelWithOptions($liandanluExclusiveModelRequest, $liandanluExclusiveModelHeaders, new RuntimeOptions([]));
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
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkaipaas_1_0  "github.com/alibabacloud-go/dingtalk/aiPaaS_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkaipaas_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkaipaas_1_0.Client{}
  _result, _err = dingtalkaipaas_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  liandanluExclusiveModelHeaders := &dingtalkaipaas_1_0.LiandanluExclusiveModelHeaders{}
  liandanluExclusiveModelHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  liandanluExclusiveModelRequest := &dingtalkaipaas_1_0.LiandanluExclusiveModelRequest{
    ModuleType: tea.String("GENERAL"),
    ModelCode: tea.String("maas1234"),
    Prompt: tea.String("OKR是什么"),
    UserId: tea.String("使用该功能的用户id"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.LiandanluExclusiveModelWithOptions(liandanluExclusiveModelRequest, liandanluExclusiveModelHeaders, &util.RuntimeOptions{})
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
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkaiPaaS_1_0, * as $dingtalkaiPaaS_1_0 from '@alicloud/dingtalk/aiPaaS_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkaiPaaS_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkaiPaaS_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let liandanluExclusiveModelHeaders = new $dingtalkaiPaaS_1_0.LiandanluExclusiveModelHeaders({ });
    liandanluExclusiveModelHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let liandanluExclusiveModelRequest = new $dingtalkaiPaaS_1_0.LiandanluExclusiveModelRequest({
      moduleType: "GENERAL",
      modelCode: "maas1234",
      prompt: "OKR是什么",
      userId: "使用该功能的用户id",
    });
    try {
      await client.liandanluExclusiveModelWithOptions(liandanluExclusiveModelRequest, liandanluExclusiveModelHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.LiandanluExclusiveModelHeaders liandanluExclusiveModelHeaders = new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.LiandanluExclusiveModelHeaders();
            liandanluExclusiveModelHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.LiandanluExclusiveModelRequest liandanluExclusiveModelRequest = new AlibabaCloud.SDK.Dingtalkai_paa_s_1_0.Models.LiandanluExclusiveModelRequest
            {
                ModuleType = "GENERAL",
                ModelCode = "maas1234",
                Prompt = "OKR是什么",
                UserId = "使用该功能的用户id",
            };
            try
            {
                client.LiandanluExclusiveModelWithOptions(liandanluExclusiveModelRequest, liandanluExclusiveModelHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求标识 |
| result | Map | 结果对象,不同平台训练能力返回结构不一样，通用模型训练，数据模型，指令模型返回对应的JSON结构。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "request_123",
  "result" : {
    "content" : "OKR 全称为 Objective and Key Results，即目标与关键结果法，是一套明确和跟踪目标及其完成情况的管理工具和方法。"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceId.error | 模型id设置错误 | 模型信息不正确，请在炼丹炉上确认模型是否正确 |
| 400 | user.error | 用户信息缺失 | 请设置正确的用户信息 |
| 500 | model.timeout | 模型超时 | 模型服务超时，请稍后再试 |
| 500 | model.absent | 模型不存在 | 模型不存在，请确认模型是否部署 |
