---
title: "获取单元格区域"
source_url: "https://open.dingtalk.com/document/development/get-cell-properties"
namespace: "development"
slug: "get-cell-properties"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 单元格区域 > 获取单元格区域"
doc_id: "x4dqwU9M4D"
updated_at: "2026-06-04 19:09:14"
---

> Source: https://open.dingtalk.com/document/development/get-cell-properties
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 单元格区域 > 获取单元格区域
> Updated: 2026-06-04 19:09:14

# 获取单元格区域

调用本接口，获取单元格属性。目前可以获取单元格内的值、公式、显示值、背景色、字体大小、水平对齐方式、垂直对齐方式。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Document.Workbook.Read-钉钉表格读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](https://open.dingtalk.com/document/development/get-node)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表ID或名称，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id或name参数值。 |
| rangeAddress | String | 是 | Range地址。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| select | String | 否 | 筛选要返回的字段，该参数不传则返回所有字段。   - 如`select=values`，该接口只返回values字段。 - 返回多个字段时，使用逗号分隔，例如`select=values,formulas`，该接口只返回values和formulas字段。     建议指定此参数以提高性能，并避免后续增加返回值时造成API超时。 |
| operatorId | String | 是 | 操作人的unionId。   - 可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取unionid参数值。 - 可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。     若操作人无权限，接口会报错`The operator has no permission`。 |

### 请求示例

HTTP

```
GET /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/ranges/A1:B2?select=values&operatorId=ppgAxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f86e0bxxx
Content-Type:application/json
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
        com.aliyun.dingtalkdoc_1_0.models.GetRangeHeaders getRangeHeaders = new com.aliyun.dingtalkdoc_1_0.models.GetRangeHeaders();
        getRangeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.GetRangeRequest getRangeRequest = new com.aliyun.dingtalkdoc_1_0.models.GetRangeRequest()
                .setSelect("values")
                .setOperatorId("ppgAxxx");
        try {
            client.getRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B2", getRangeRequest, getRangeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_range_headers = dingtalkdoc__1__0_models.GetRangeHeaders()
        get_range_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_range_request = dingtalkdoc__1__0_models.GetRangeRequest(
            select='values',
            operator_id='ppgAxxx'
        )
        try:
            client.get_range_with_options('e54Lq3xxx', 'Sheet1', 'A1:B2', get_range_request, get_range_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_range_headers = dingtalkdoc__1__0_models.GetRangeHeaders()
        get_range_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_range_request = dingtalkdoc__1__0_models.GetRangeRequest(
            select='values',
            operator_id='ppgAxxx'
        )
        try:
            await client.get_range_with_options_async('e54Lq3xxx', 'Sheet1', 'A1:B2', get_range_request, get_range_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetRangeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetRangeRequest;
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
        $getRangeHeaders = new GetRangeHeaders([]);
        $getRangeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getRangeRequest = new GetRangeRequest([
            "select" => "values",
            "operatorId" => "ppgAxxx"
        ]);
        try {
            $client->getRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B2", $getRangeRequest, $getRangeHeaders, new RuntimeOptions([]));
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

  getRangeHeaders := &dingtalkdoc_1_0.GetRangeHeaders{}
  getRangeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getRangeRequest := &dingtalkdoc_1_0.GetRangeRequest{
    Select: tea.String("values"),
    OperatorId: tea.String("ppgAxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetRangeWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), tea.String("A1:B2"), getRangeRequest, getRangeHeaders, &util.RuntimeOptions{})
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
    let getRangeHeaders = new $dingtalkdoc_1_0.GetRangeHeaders({ });
    getRangeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getRangeRequest = new $dingtalkdoc_1_0.GetRangeRequest({
      select: "values",
      operatorId: "ppgAxxx",
    });
    try {
      await client.getRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B2", getRangeRequest, getRangeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRangeHeaders getRangeHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRangeHeaders();
            getRangeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRangeRequest getRangeRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRangeRequest
            {
                Select = "values",
                OperatorId = "ppgAxxx",
            };
            try
            {
                client.GetRangeWithOptions("e54Lq3xxx", "Sheet1", "A1:B2", getRangeRequest, getRangeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| values | Array | 单元格的值。    如果单元格是公式，则返回公式计算后的结果。形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的单元格的值。 |
|  | Array of Any | 单元格的值。    如果单元格是公式，则返回公式计算后的结果。形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的单元格的值。 |
| formulas | Array | 单元格的公式。    形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的公式。 |
|  | Array of String | 单元格的公式。    形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的公式。 |
| displayValues | Array | 单元格的显示值。    显示值为在表格界面上所看到的结果。和values相比，其会受到数字格式（如小数位数、百分比、日期格式等）等因素影响。形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的显示值。 |
|  | Array of String | 单元格的显示值。    显示值为在表格界面上所看到的结果。和values相比，其会受到数字格式（如小数位数、百分比、日期格式等）等因素影响。形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的显示值。 |
| backgroundColors | Array | 单元格的背景色。    形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的背景色。 |
|  | Array | 单元格的背景色。    形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的背景色。 |
| red | Integer | RGB值中的红色值。 |
| green | Integer | RGB值中的绿色值。 |
| blue | Integer | RGB值中的蓝色值。 |
| hexString | String | 16进制表示的颜色。 |
| fontSizes | Array | 单元格的字体大小。    形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的字体大小。 |
|  | Array of Integer | 单元格的字体大小。    形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的字体大小。 |
| horizontalAlignments | Array | 单元格的水平对齐方式。      形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的水平对齐方式。 |
|  | Array of String | 单元格的水平对齐方式。      形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的水平对齐方式。 |
| verticalAlignments | Array | 单元格的垂直对齐方式。      形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的垂直对齐方式。 |
|  | Array of String | 单元格的垂直对齐方式。      形式为二维数组，第一维为Range范围内的所有行，第二维为Range范围内每一行的所有单元格的垂直对齐方式。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "values" : [ [ "1" ] ],
  "formulas" : [ [ "=B1+C2" ] ],
  "displayValues" : [ [ "100%" ] ],
  "backgroundColors" : [ [ {
    "red" : 0,
    "green" : 0,
    "blue" : 0,
    "hexString" : "#000000"
  } ] ],
  "fontSizes" : [ [ 14 ] ],
  "horizontalAlignments" : [ [ "general" ] ],
  "verticalAlignments" : [ [ "middle" ] ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.resource.notWorkbook | %s | 不支持的文档类型，请检查workbookId。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
