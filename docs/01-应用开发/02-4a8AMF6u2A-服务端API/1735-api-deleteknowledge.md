---
title: "助理删除知识"
source_url: "https://open.dingtalk.com/document/development/api-deleteknowledge"
namespace: "development"
slug: "api-deleteknowledge"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 助理管理 > 知识管理 > 助理删除知识"
doc_id: "0xwiuFTQRf"
updated_at: "2026-03-06 09:22:58"
---

> Source: https://open.dingtalk.com/document/development/api-deleteknowledge
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 助理管理 > 知识管理 > 助理删除知识
> Updated: 2026-03-06 09:22:58

# 助理删除知识

调用本接口，删除知识。

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
DELETE /v1.0/assistant/knowledges/items?assistantId=String&studyId=String HTTP/1.1
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
| studyId | String | 是 | 学习的唯一标识。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 是否成功。 |

## 示例

**请求示例**

HTTP

```
DELETE /v1.0/assistant/knowledges/items?assistantId=123-456&studyId=123 HTTP/1.1
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
        
        com.aliyun.dingtalkassistant_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkassistant_1_0.models.DeleteKnowledgeHeaders deleteKnowledgeHeaders = new com.aliyun.dingtalkassistant_1_0.models.DeleteKnowledgeHeaders();
        deleteKnowledgeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkassistant_1_0.models.DeleteKnowledgeRequest deleteKnowledgeRequest = new com.aliyun.dingtalkassistant_1_0.models.DeleteKnowledgeRequest()
                .setAssistantId("123-456")
                .setStudyId("123");
        try {
            client.deleteKnowledgeWithOptions(deleteKnowledgeRequest, deleteKnowledgeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        delete_knowledge_headers = dingtalkassistant__1__0_models.DeleteKnowledgeHeaders()
        delete_knowledge_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_knowledge_request = dingtalkassistant__1__0_models.DeleteKnowledgeRequest(
            assistant_id='123-456',
            study_id='123'
        )
        try:
            client.delete_knowledge_with_options(delete_knowledge_request, delete_knowledge_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_knowledge_headers = dingtalkassistant__1__0_models.DeleteKnowledgeHeaders()
        delete_knowledge_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_knowledge_request = dingtalkassistant__1__0_models.DeleteKnowledgeRequest(
            assistant_id='123-456',
            study_id='123'
        )
        try:
            await client.delete_knowledge_with_options_async(delete_knowledge_request, delete_knowledge_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\DeleteKnowledgeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\DeleteKnowledgeRequest;
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
        $deleteKnowledgeHeaders = new DeleteKnowledgeHeaders([]);
        $deleteKnowledgeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteKnowledgeRequest = new DeleteKnowledgeRequest([
            "assistantId" => "123-456",
            "studyId" => "123"
        ]);
        try {
            $client->deleteKnowledgeWithOptions($deleteKnowledgeRequest, $deleteKnowledgeHeaders, new RuntimeOptions([]));
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

  deleteKnowledgeHeaders := &dingtalkassistant_1_0.DeleteKnowledgeHeaders{}
  deleteKnowledgeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteKnowledgeRequest := &dingtalkassistant_1_0.DeleteKnowledgeRequest{
    AssistantId: tea.String("123-456"),
    StudyId: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteKnowledgeWithOptions(deleteKnowledgeRequest, deleteKnowledgeHeaders, &util.RuntimeOptions{})
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
    let deleteKnowledgeHeaders = new dingtalkassistant_1_0.DeleteKnowledgeHeaders({ });
    deleteKnowledgeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let deleteKnowledgeRequest = new dingtalkassistant_1_0.DeleteKnowledgeRequest({
      assistantId: '123-456',
      studyId: '123',
    });
    try {
      await client.deleteKnowledgeWithOptions(deleteKnowledgeRequest, deleteKnowledgeHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.DeleteKnowledgeHeaders deleteKnowledgeHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.DeleteKnowledgeHeaders();
            deleteKnowledgeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.DeleteKnowledgeRequest deleteKnowledgeRequest = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.DeleteKnowledgeRequest
            {
                AssistantId = "123-456",
                StudyId = "123",
            };
            try
            {
                client.DeleteKnowledgeWithOptions(deleteKnowledgeRequest, deleteKnowledgeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "success" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | url.parameter.error | 参数错误:%s | 参数错误 |
