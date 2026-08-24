---
title: "获取筛选"
source_url: "https://open.dingtalk.com/document/development/api-getfilter"
namespace: "development"
slug: "api-getfilter"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 表格 > 筛选 > 获取筛选"
doc_id: "uo7JbFYiNL"
updated_at: "2026-06-08 12:02:07"
---

> Source: https://open.dingtalk.com/document/development/api-getfilter
> Path: 应用开发 / 服务端API / 文档/文件 > 表格 > 筛选 > 获取筛选
> Updated: 2026-06-08 12:02:07

# 获取筛选

调用本接口可查询指定工作表上当前生效的全局筛选信息，返回筛选 ID、筛选范围及各列已设置的筛选条件。适用于在修改筛选条件前先确认当前筛选状态，或在程序中读取筛选配置以进行后续处理的场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/filter/getFilter |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Document.Workbook.Read-钉钉表格读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](0570-get-knowledge-base-acquisition-node.md)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表ID或名称，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id或name参数值。  **[!NOTE]**  若工作表上不存在筛选，接口将返回 404 错误。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId。   - 可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取unionid参数值。 - 可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。       若操作人无权限，接口会报错`The operator has no permission`。 |

### 请求示例

HTTP

```
GET /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/filter/getFilter?operatorId=ppgAxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f86e0bxxx
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
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_1_0.models.GetFilterHeaders getFilterHeaders = new com.aliyun.dingtalkdoc_1_0.models.GetFilterHeaders();
        getFilterHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.GetFilterRequest getFilterRequest = new com.aliyun.dingtalkdoc_1_0.models.GetFilterRequest()
                .setOperatorId("ppgAxxx");
        try {
            client.getFilterWithOptions("e54Lq3xxx", "Sheet1", getFilterRequest, getFilterHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_filter_headers = dingtalkdoc__1__0_models.GetFilterHeaders()
        get_filter_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_filter_request = dingtalkdoc__1__0_models.GetFilterRequest(
            operator_id='ppgAxxx'
        )
        try:
            client.get_filter_with_options('e54Lq3xxx', 'Sheet1', get_filter_request, get_filter_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_filter_headers = dingtalkdoc__1__0_models.GetFilterHeaders()
        get_filter_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_filter_request = dingtalkdoc__1__0_models.GetFilterRequest(
            operator_id='ppgAxxx'
        )
        try:
            await client.get_filter_with_options_async('e54Lq3xxx', 'Sheet1', get_filter_request, get_filter_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetFilterHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetFilterRequest;
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
        $getFilterHeaders = new GetFilterHeaders([]);
        $getFilterHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFilterRequest = new GetFilterRequest([
            "operatorId" => "ppgAxxx"
        ]);
        try {
            $client->getFilterWithOptions("e54Lq3xxx", "Sheet1", $getFilterRequest, $getFilterHeaders, new RuntimeOptions([]));
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

  getFilterHeaders := &dingtalkdoc_1_0.GetFilterHeaders{}
  getFilterHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFilterRequest := &dingtalkdoc_1_0.GetFilterRequest{
    OperatorId: tea.String("ppgAxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFilterWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), getFilterRequest, getFilterHeaders, &util.RuntimeOptions{})
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
    let getFilterHeaders = new dingtalkdoc_1_0.GetFilterHeaders({ });
    getFilterHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getFilterRequest = new dingtalkdoc_1_0.GetFilterRequest({
      operatorId: 'ppgAxxx',
    });
    try {
      await client.getFilterWithOptions('e54Lq3xxx', 'Sheet1', getFilterRequest, getFilterHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetFilterHeaders getFilterHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetFilterHeaders();
            getFilterHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetFilterRequest getFilterRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetFilterRequest
            {
                OperatorId = "ppgAxxx",
            };
            try
            {
                client.GetFilterWithOptions("e54Lq3xxx", "Sheet1", getFilterRequest, getFilterHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 筛选的唯一标识 ID |
| range | String | 筛选范围，A1 表示法 |
| criteria | Map<String, Object> | 所有列的筛选条件映射。key 为列偏移量（相对于筛选范围首列，从 0 开始），value 为该列的筛选条件对象。如果没有设置筛选条件，返回空对象 `{}`。 |
|  | Object | 当前列的筛选条件 |
| filterType | String | 筛选类型。可选值：   - **values**：按值筛选 - **color**：按颜色筛选 - **condition**：按条件筛选 |
| visibleValues | Array of String | 可见值 |
| conditions | Array | 按条件筛选时的条件列表。仅当 `filterType` 为 `condition` 时返回。 |
| operator | String | 条件操作符。取值：   - **equal**：等于 - **not-equal**：不等于 - **contains**：包含 - **not-contains**：不包含 - **starts-with**：开头是 - **not-starts-with**：开头不是 - **ends-with**：结尾是 - **not-ends-with**：结尾不是 - **greater**：大于 - **greater-equal**：大于等于 - **less**：小于 - **less-equal**：小于等于 |
| value | String | 条件值 |
| conditionOperator | String | 多个条件之间的逻辑关系（`and` 或 `or`）。仅当 `filterType` 为 `condition` 时返回。 |
| backgroundColor | String | 按背景色筛选时的可见颜色，16 进制格式。仅当 `filterType` 为 `color` 且按背景色筛选时返回。 |
| fontColor | String | 按字体色筛选时的可见颜色，16 进制格式。仅当 `filterType` 为 `color` 且按字体色筛选时返回。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
    "id": "filter-xxxxx",
    "range": "A1:D10",
    "criteria": {
        "key": {
            "filterType": "values",
            "visibleValues": [
                "123"
            ],
        }
    }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.resource.notWorkbook | %s | 不支持的文档类型，请检查workbookId。 |
| 400 | invalidRequest.document.stillInitializing | The document is still initializing. Please try again later. | 文档初始化中，请稍后重试。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
