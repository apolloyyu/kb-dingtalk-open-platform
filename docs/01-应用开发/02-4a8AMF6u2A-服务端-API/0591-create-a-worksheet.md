---
title: "创建工作表"
source_url: "https://open.dingtalk.com/document/development/create-a-worksheet"
namespace: "development"
slug: "create-a-worksheet"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 工作表 > 创建工作表"
doc_id: "97be9xkSfY"
updated_at: "2026-06-04 19:09:05"
---

> Source: https://open.dingtalk.com/document/development/create-a-worksheet
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 工作表 > 创建工作表
> Updated: 2026-06-04 19:09:05

# 创建工作表

调用本接口，在表格文档中创建一个新的工作表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Document.Workbook.Write-钉钉表格写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](https://open.dingtalk.com/document/development/get-node)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。    若操作人无权限，接口会报错`The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 工作表的名称。    当指定的工作表名称和已有的工作表名称重复时，将自动重命名为合法值。 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lqxxx/sheets?operatorId=ppgAQuHfOoNVpJiStDwWCEgiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "name" : "Sheet1"
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
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_1_0.models.CreateSheetHeaders createSheetHeaders = new com.aliyun.dingtalkdoc_1_0.models.CreateSheetHeaders();
        createSheetHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.CreateSheetRequest createSheetRequest = new com.aliyun.dingtalkdoc_1_0.models.CreateSheetRequest()
                .setOperatorId("ppgAQuHfOoNVpJiStDwWCEgiEiE")
                .setName("Sheet1");
        try {
            client.createSheetWithOptions("e54Lqxxx", createSheetRequest, createSheetHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import sys

from typing import List

from alibabacloud_dingtalk.doc_1_0.client import Client as dingtalkdoc_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_1_0 import models as dingtalkdoc__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_sheet_headers = dingtalkdoc__1__0_models.CreateSheetHeaders()
        create_sheet_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_sheet_request = dingtalkdoc__1__0_models.CreateSheetRequest(
            operator_id='ppgAQuHfOoNVpJiStDwWCEgiEiE',
            name='Sheet1'
        )
        try:
            client.create_sheet_with_options('e54Lqxxx', create_sheet_request, create_sheet_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_sheet_headers = dingtalkdoc__1__0_models.CreateSheetHeaders()
        create_sheet_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_sheet_request = dingtalkdoc__1__0_models.CreateSheetRequest(
            operator_id='ppgAQuHfOoNVpJiStDwWCEgiEiE',
            name='Sheet1'
        )
        try:
            await client.create_sheet_with_options_async('e54Lqxxx', create_sheet_request, create_sheet_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateSheetHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateSheetRequest;
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
        $createSheetHeaders = new CreateSheetHeaders([]);
        $createSheetHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createSheetRequest = new CreateSheetRequest([
            "operatorId" => "ppgAQuHfOoNVpJiStDwWCEgiEiE",
            "name" => "Sheet1"
        ]);
        try {
            $client->createSheetWithOptions("e54Lqxxx", $createSheetRequest, $createSheetHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdoc_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_1_0.Client{}
  _result, _err = dingtalkdoc_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createSheetHeaders := &dingtalkdoc_1_0.CreateSheetHeaders{}
  createSheetHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createSheetRequest := &dingtalkdoc_1_0.CreateSheetRequest{
    OperatorId: tea.String("ppgAQuHfOoNVpJiStDwWCEgiEiE"),
    Name: tea.String("Sheet1"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateSheetWithOptions(tea.String("e54Lqxxx"), createSheetRequest, createSheetHeaders, &util.RuntimeOptions{})
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
import dingtalkdoc_1_0, * as $dingtalkdoc_1_0 from '@alicloud/dingtalk/doc_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdoc_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdoc_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createSheetHeaders = new $dingtalkdoc_1_0.CreateSheetHeaders({ });
    createSheetHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createSheetRequest = new $dingtalkdoc_1_0.CreateSheetRequest({
      operatorId: "ppgAQuHfOoNVpJiStDwWCEgiEiE",
      name: "Sheet1",
    });
    try {
      await client.createSheetWithOptions("e54Lqxxx", createSheetRequest, createSheetHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdoc_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateSheetHeaders createSheetHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateSheetHeaders();
            createSheetHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateSheetRequest createSheetRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateSheetRequest
            {
                OperatorId = "ppgAQuHfOoNVpJiStDwWCEgiEiE",
                Name = "Sheet1",
            };
            try
            {
                client.CreateSheetWithOptions("e54Lqxxx", createSheetRequest, createSheetHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| visibility | String | 工作表可见性，固定值为visible。 |
| name | String | 工作表的名称。 |
| id | String | 工作表的ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "visibility" : "visible",
  "name" : "Sheet1",
  "id" : "st-xxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.inputArgs.operatorIdIllegal | The operatorId is illegal. | operatorId不合法。 |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法。可能的错误包含range地址不正确，输入参数数据维度不正确，颜色格式不正确等。具体错误请查看错误信息。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法。可能的错误包含没有权限访问被锁定的单元格，修改数据透视表、待办相关的单元格等。具体错误请查看错误信息。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
| 503 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
