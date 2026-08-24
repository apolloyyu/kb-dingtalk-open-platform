---
title: "设置列隐藏或显示"
source_url: "https://open.dingtalk.com/document/development/set-column-visibility"
namespace: "development"
slug: "set-column-visibility"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 表格 > 行列 > 设置列隐藏或显示"
doc_id: "3RJ5NUqDwe"
updated_at: "2026-06-04 19:09:11"
---

> Source: https://open.dingtalk.com/document/development/set-column-visibility
> Path: 应用开发 / 服务端API / 文档/文件 > 表格 > 行列 > 设置列隐藏或显示
> Updated: 2026-06-04 19:09:11

# 设置列隐藏或显示

调用本接口，设置列的可见性。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/setColumnsVisibility |
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
| sheetId | String | 是 | 工作表的ID或标题。   - 企业内部应用，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id或者传工作表的标题。 - 第三方企业应用，建议传递工作表的标题。   工作表的标题查看步骤如下图。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| column | Long | 是 | 要显示或隐藏的第一列的游标，从0开始。 |
| columnCount | Long | 是 | 要显示或隐藏的列的数量。 |
| visibility | String | 是 | 可见性。   - **visible**：可见 - **hidden**：隐藏 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/setColumnsVisibility?operatorId=ppgAxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "column" : 0,
  "columnCount" : 1,
  "visibility" : "hidden"
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
        com.aliyun.dingtalkdoc_1_0.models.SetColumnsVisibilityHeaders setColumnsVisibilityHeaders = new com.aliyun.dingtalkdoc_1_0.models.SetColumnsVisibilityHeaders();
        setColumnsVisibilityHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.SetColumnsVisibilityRequest setColumnsVisibilityRequest = new com.aliyun.dingtalkdoc_1_0.models.SetColumnsVisibilityRequest()
                .setOperatorId("ppgAxxx")
                .setColumn(0L)
                .setColumnCount(1L)
                .setVisibility("hidden");
        try {
            client.setColumnsVisibilityWithOptions("e54Lq3xxx", "Sheet1", setColumnsVisibilityRequest, setColumnsVisibilityHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        set_columns_visibility_headers = dingtalkdoc__1__0_models.SetColumnsVisibilityHeaders()
        set_columns_visibility_headers.x_acs_dingtalk_access_token = '<your access token>'
        set_columns_visibility_request = dingtalkdoc__1__0_models.SetColumnsVisibilityRequest(
            operator_id='ppgAxxx',
            column=0,
            column_count=1,
            visibility='hidden'
        )
        try:
            client.set_columns_visibility_with_options('e54Lq3xxx', 'Sheet1', set_columns_visibility_request, set_columns_visibility_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        set_columns_visibility_headers = dingtalkdoc__1__0_models.SetColumnsVisibilityHeaders()
        set_columns_visibility_headers.x_acs_dingtalk_access_token = '<your access token>'
        set_columns_visibility_request = dingtalkdoc__1__0_models.SetColumnsVisibilityRequest(
            operator_id='ppgAxxx',
            column=0,
            column_count=1,
            visibility='hidden'
        )
        try:
            await client.set_columns_visibility_with_options_async('e54Lq3xxx', 'Sheet1', set_columns_visibility_request, set_columns_visibility_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SetColumnsVisibilityHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SetColumnsVisibilityRequest;
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
        $setColumnsVisibilityHeaders = new SetColumnsVisibilityHeaders([]);
        $setColumnsVisibilityHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $setColumnsVisibilityRequest = new SetColumnsVisibilityRequest([
            "operatorId" => "ppgAxxx",
            "column" => 0,
            "columnCount" => 1,
            "visibility" => "hidden"
        ]);
        try {
            $client->setColumnsVisibilityWithOptions("e54Lq3xxx", "Sheet1", $setColumnsVisibilityRequest, $setColumnsVisibilityHeaders, new RuntimeOptions([]));
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

  setColumnsVisibilityHeaders := &dingtalkdoc_1_0.SetColumnsVisibilityHeaders{}
  setColumnsVisibilityHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  setColumnsVisibilityRequest := &dingtalkdoc_1_0.SetColumnsVisibilityRequest{
    OperatorId: tea.String("ppgAxxx"),
    Column: tea.Int64(0),
    ColumnCount: tea.Int64(1),
    Visibility: tea.String("hidden"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SetColumnsVisibilityWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), setColumnsVisibilityRequest, setColumnsVisibilityHeaders, &util.RuntimeOptions{})
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
    let setColumnsVisibilityHeaders = new $dingtalkdoc_1_0.SetColumnsVisibilityHeaders({ });
    setColumnsVisibilityHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let setColumnsVisibilityRequest = new $dingtalkdoc_1_0.SetColumnsVisibilityRequest({
      operatorId: "ppgAxxx",
      column: 0,
      columnCount: 1,
      visibility: "hidden",
    });
    try {
      await client.setColumnsVisibilityWithOptions("e54Lq3xxx", "Sheet1", setColumnsVisibilityRequest, setColumnsVisibilityHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SetColumnsVisibilityHeaders setColumnsVisibilityHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SetColumnsVisibilityHeaders();
            setColumnsVisibilityHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SetColumnsVisibilityRequest setColumnsVisibilityRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SetColumnsVisibilityRequest
            {
                OperatorId = "ppgAxxx",
                Column = 0,
                ColumnCount = 1,
                Visibility = "hidden",
            };
            try
            {
                client.SetColumnsVisibilityWithOptions("e54Lq3xxx", "Sheet1", setColumnsVisibilityRequest, setColumnsVisibilityHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 工作表ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "stxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.inputArgs.operatorIdIllegal | The operatorId is illegal. | operatorId不合法。 |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
| 503 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
