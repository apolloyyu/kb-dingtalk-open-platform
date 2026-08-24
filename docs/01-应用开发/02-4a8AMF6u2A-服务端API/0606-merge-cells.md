---
title: "合并单元格"
source_url: "https://open.dingtalk.com/document/development/merge-cells"
namespace: "development"
slug: "merge-cells"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 表格 > 单元格区域 > 合并单元格"
doc_id: "QsYE2DvX38"
updated_at: "2026-06-04 19:09:12"
---

> Source: https://open.dingtalk.com/document/development/merge-cells
> Path: 应用开发 / 服务端API / 文档/文件 > 表格 > 单元格区域 > 合并单元格
> Updated: 2026-06-04 19:09:12

# 合并单元格

调用本接口，可将钉钉表格中指定区域内的多个单元格合并为一个整体。适用于制作表头跨列标题、合并相同分类行等需要调整单元格布局的场景。支持全部合并、按行合并、按列合并三种模式，合并后仅保留左上角单元格的数据，其余单元格内容将被清除，接口返回实际操作的单元格地址。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress}/merge |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Document.Workbook.Write-钉钉表格写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的nodeId(dentryUuid)即是表格workbookId，可通过调用[获取节点](0570-get-knowledge-base-acquisition-node.md)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表ID或标题，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id和工作表的标题。 |
| rangeAddress | String | 是 | 需要合并的单元格范围，格式为`区域内左上角单元格:区域内右下角单元格`。  例如：B2:C3 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。      若操作人无权限，接口会报错 `The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| mergeType | String | 否 | 指定合并单元格的方式。可选值：   - **mergeAll**：合并所有单元格（默认值） - **mergeRows**：按行合并，即在选定的区域内，将同一行相邻的单元格合并成一个单元格 - **mergeColumns**：按列合并，即在选定的区域内，将同一列中相邻的单元格合并成一个单元格 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/ranges/A1:B1/merge?operatorId=ppgAQuxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token:f86e0bxxx
Content-Type:application/json

{
  "mergeType" : "mergeRows"
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
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_1_0.models.MergeRangeHeaders mergeRangeHeaders = new com.aliyun.dingtalkdoc_1_0.models.MergeRangeHeaders();
        mergeRangeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.MergeRangeRequest mergeRangeRequest = new com.aliyun.dingtalkdoc_1_0.models.MergeRangeRequest()
                .setOperatorId("ppgAQuxxx")
                .setMergeType("mergeRows");
        try {
            client.mergeRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", mergeRangeRequest, mergeRangeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        merge_range_headers = dingtalkdoc__1__0_models.MergeRangeHeaders()
        merge_range_headers.x_acs_dingtalk_access_token = '<your access token>'
        merge_range_request = dingtalkdoc__1__0_models.MergeRangeRequest(
            operator_id='ppgAQuxxx',
            merge_type='mergeRows'
        )
        try:
            client.merge_range_with_options('e54Lq3xxx', 'Sheet1', 'A1:B1', merge_range_request, merge_range_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        merge_range_headers = dingtalkdoc__1__0_models.MergeRangeHeaders()
        merge_range_headers.x_acs_dingtalk_access_token = '<your access token>'
        merge_range_request = dingtalkdoc__1__0_models.MergeRangeRequest(
            operator_id='ppgAQuxxx',
            merge_type='mergeRows'
        )
        try:
            await client.merge_range_with_options_async('e54Lq3xxx', 'Sheet1', 'A1:B1', merge_range_request, merge_range_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\MergeRangeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\MergeRangeRequest;
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
        $mergeRangeHeaders = new MergeRangeHeaders([]);
        $mergeRangeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $mergeRangeRequest = new MergeRangeRequest([
            "operatorId" => "ppgAQuxxx",
            "mergeType" => "mergeRows"
        ]);
        try {
            $client->mergeRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", $mergeRangeRequest, $mergeRangeHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
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

  mergeRangeHeaders := &dingtalkdoc_1_0.MergeRangeHeaders{}
  mergeRangeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  mergeRangeRequest := &dingtalkdoc_1_0.MergeRangeRequest{
    OperatorId: tea.String("ppgAQuxxx"),
    MergeType: tea.String("mergeRows"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.MergeRangeWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), tea.String("A1:B1"), mergeRangeRequest, mergeRangeHeaders, &util.RuntimeOptions{})
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
const dingtalkdoc_1_0 = require('@alicloud/dingtalk/doc_1_0');
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
    return new dingtalkdoc_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let mergeRangeHeaders = new dingtalkdoc_1_0.MergeRangeHeaders({ });
    mergeRangeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let mergeRangeRequest = new dingtalkdoc_1_0.MergeRangeRequest({
      operatorId: 'ppgAQuxxx',
      mergeType: 'mergeRows',
    });
    try {
      await client.mergeRangeWithOptions('e54Lq3xxx', 'Sheet1', 'A1:B1', mergeRangeRequest, mergeRangeHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.MergeRangeHeaders mergeRangeHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.MergeRangeHeaders();
            mergeRangeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.MergeRangeRequest mergeRangeRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.MergeRangeRequest
            {
                OperatorId = "ppgAQuxxx",
                MergeType = "mergeRows",
            };
            try
            {
                client.MergeRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", mergeRangeRequest, mergeRangeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| a1Notation | String | 合并的单元格范围，格式为`区域内左上角单元格:区域内右下角单元格`。  例如：B2:C3 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "a1Notation" : "A1:B1"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.inputArgs.unionIdIllegal | The operatorId is illegal. | operatorId不合法。 |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
| 503 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
