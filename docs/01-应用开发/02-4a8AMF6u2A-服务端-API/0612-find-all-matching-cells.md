---
title: "查找所有符合条件的单元格"
source_url: "https://open.dingtalk.com/document/development/find-all-matching-cells"
namespace: "development"
slug: "find-all-matching-cells"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 单元格区域 > 查找所有符合条件的单元格"
doc_id: "uqCf5wxLRc"
updated_at: "2026-06-04 19:09:15"
---

> Source: https://open.dingtalk.com/document/development/find-all-matching-cells
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 单元格区域 > 查找所有符合条件的单元格
> Updated: 2026-06-04 19:09:15

# 查找所有符合条件的单元格

调用本接口，可在钉钉表格的指定工作表中搜索所有包含目标文本的单元格，并返回匹配单元格的位置列表。适用于在大量数据中批量定位特定内容的场景，支持精确匹配、大小写敏感、正则表达式及公式内搜索等多种查找模式。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/findAll |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Document.Workbook.Read-钉钉表格读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](https://open.dingtalk.com/document/development/get-node)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表ID或标题，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id和工作表的标题。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。      若操作人无权限，接口会报错 `The operator has no permission`。 |
| select | String | 否 | 筛选要返回的字段，该参数不传则返回所有字段。   - 如select=a1Notation，该接口只返回a1Notation字段。 - 返回多个字段时，使用逗号分隔，例如select=a1Notation,values，该接口只返回a1Notation和values字段。       建议指定此参数以提高性能，并避免后续增加返回值时造成API超时。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| text | String | 是 | 要查找的文本。 如果开启了 **useRegExp**，则为正则模式，示例："\\d+" |
| findOptions | Object | 是 | 查找选项。 |
| matchEntireCell | Boolean | 否 | 匹配整个单元格，可选值：   - **true**：是 - **false**：否（默认值） |
| matchCase | Boolean | 否 | 匹配大小写，可选值：   - **true**：是 - **false**：否（默认值） |
| useRegExp | Boolean | 否 | text 是否为正则表达式，可选值：   - **true**：是 - **false**：否（默认值） |
| matchFormulaText | Boolean | 否 | 是否按照公式原始文本查找，可选值：   - **true**：是 - **false**：否（默认值）   例如，某单元格填充公式 "=A1+B1"，展示值为 4   - 当查找文本为 "4"，matchFormulaText 为 true 时，不在结果内。 - 当查找文本为 "=A1"，matchFormulaText 为 true 时，在结果内。 |
| scope | String | 否 | 搜索范围。格式为A1表示法指代的Range地址。 |
| includeHidden | Boolean | 否 | 是否包含隐藏的单元格，即隐藏行列、筛选、分组等功能导致的不可见单元格，但不包含无权限查看的单元格。可选值：   - **true**：是 - **false**：否（默认值） |
| unionCells | Boolean | 是 | 是否对找到的单元格地址做聚合。建议进行聚合，否则可能返回大量地址。可选值：   - **true**：是 - **false**：否（默认值） |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/findAll?operatorId=ppgAxxx&select=a1Notation HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f86e0bxxx
Content-Type:application/json

{
  "text" : "DingTalk",
  "findOptions" : {
    "matchEntireCell" : true,
    "matchCase" : true,
    "useRegExp" : true,
    "matchFormulaText" : true,
    "scope" : "A:A",
    "includeHidden" : false,
    "unionCells" : true
  }
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
        com.aliyun.dingtalkdoc_1_0.models.SheetFindAllHeaders sheetFindAllHeaders = new com.aliyun.dingtalkdoc_1_0.models.SheetFindAllHeaders();
        sheetFindAllHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.SheetFindAllRequest.SheetFindAllRequestFindOptions findOptions = new com.aliyun.dingtalkdoc_1_0.models.SheetFindAllRequest.SheetFindAllRequestFindOptions()
                .setMatchEntireCell(true)
                .setMatchCase(true)
                .setUseRegExp(true)
                .setMatchFormulaText(true)
                .setScope("A:A")
                .setIncludeHidden(false)
                .setUnionCells(true);
        com.aliyun.dingtalkdoc_1_0.models.SheetFindAllRequest sheetFindAllRequest = new com.aliyun.dingtalkdoc_1_0.models.SheetFindAllRequest()
                .setOperatorId("ppgAxxx")
                .setSelect("a1Notation")
                .setText("DingTalk")
                .setFindOptions(findOptions);
        try {
            client.sheetFindAllWithOptions("e54Lq3xxx", "Sheet1", sheetFindAllRequest, sheetFindAllHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        sheet_find_all_headers = dingtalkdoc__1__0_models.SheetFindAllHeaders()
        sheet_find_all_headers.x_acs_dingtalk_access_token = '<your access token>'
        find_options = dingtalkdoc__1__0_models.SheetFindAllRequestFindOptions(
            match_entire_cell=True,
            match_case=True,
            use_reg_exp=True,
            match_formula_text=True,
            scope='A:A',
            include_hidden=False,
            union_cells=True
        )
        sheet_find_all_request = dingtalkdoc__1__0_models.SheetFindAllRequest(
            operator_id='ppgAxxx',
            select='a1Notation',
            text='DingTalk',
            find_options=find_options
        )
        try:
            client.sheet_find_all_with_options('e54Lq3xxx', 'Sheet1', sheet_find_all_request, sheet_find_all_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sheet_find_all_headers = dingtalkdoc__1__0_models.SheetFindAllHeaders()
        sheet_find_all_headers.x_acs_dingtalk_access_token = '<your access token>'
        find_options = dingtalkdoc__1__0_models.SheetFindAllRequestFindOptions(
            match_entire_cell=True,
            match_case=True,
            use_reg_exp=True,
            match_formula_text=True,
            scope='A:A',
            include_hidden=False,
            union_cells=True
        )
        sheet_find_all_request = dingtalkdoc__1__0_models.SheetFindAllRequest(
            operator_id='ppgAxxx',
            select='a1Notation',
            text='DingTalk',
            find_options=find_options
        )
        try:
            await client.sheet_find_all_with_options_async('e54Lq3xxx', 'Sheet1', sheet_find_all_request, sheet_find_all_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SheetFindAllHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SheetFindAllRequest\findOptions;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SheetFindAllRequest;
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
        $sheetFindAllHeaders = new SheetFindAllHeaders([]);
        $sheetFindAllHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $findOptions = new findOptions([
            "matchEntireCell" => true,
            "matchCase" => true,
            "useRegExp" => true,
            "matchFormulaText" => true,
            "scope" => "A:A",
            "includeHidden" => false,
            "unionCells" => true
        ]);
        $sheetFindAllRequest = new SheetFindAllRequest([
            "operatorId" => "ppgAxxx",
            "select" => "a1Notation",
            "text" => "DingTalk",
            "findOptions" => $findOptions
        ]);
        try {
            $client->sheetFindAllWithOptions("e54Lq3xxx", "Sheet1", $sheetFindAllRequest, $sheetFindAllHeaders, new RuntimeOptions([]));
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

  sheetFindAllHeaders := &dingtalkdoc_1_0.SheetFindAllHeaders{}
  sheetFindAllHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  findOptions := &dingtalkdoc_1_0.SheetFindAllRequestFindOptions{
    MatchEntireCell: tea.Bool(true),
    MatchCase: tea.Bool(true),
    UseRegExp: tea.Bool(true),
    MatchFormulaText: tea.Bool(true),
    Scope: tea.String("A:A"),
    IncludeHidden: tea.Bool(false),
    UnionCells: tea.Bool(true),
  }
  sheetFindAllRequest := &dingtalkdoc_1_0.SheetFindAllRequest{
    OperatorId: tea.String("ppgAxxx"),
    Select: tea.String("a1Notation"),
    Text: tea.String("DingTalk"),
    FindOptions: findOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SheetFindAllWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), sheetFindAllRequest, sheetFindAllHeaders, &util.RuntimeOptions{})
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
    let sheetFindAllHeaders = new $dingtalkdoc_1_0.SheetFindAllHeaders({ });
    sheetFindAllHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let findOptions = new $dingtalkdoc_1_0.SheetFindAllRequestFindOptions({
      matchEntireCell: true,
      matchCase: true,
      useRegExp: true,
      matchFormulaText: true,
      scope: "A:A",
      includeHidden: false,
      unionCells: true,
    });
    let sheetFindAllRequest = new $dingtalkdoc_1_0.SheetFindAllRequest({
      operatorId: "ppgAxxx",
      select: "a1Notation",
      text: "DingTalk",
      findOptions: findOptions,
    });
    try {
      await client.sheetFindAllWithOptions("e54Lq3xxx", "Sheet1", sheetFindAllRequest, sheetFindAllHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SheetFindAllHeaders sheetFindAllHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SheetFindAllHeaders();
            sheetFindAllHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SheetFindAllRequest.SheetFindAllRequestFindOptions findOptions = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SheetFindAllRequest.SheetFindAllRequestFindOptions
            {
                MatchEntireCell = true,
                MatchCase = true,
                UseRegExp = true,
                MatchFormulaText = true,
                Scope = "A:A",
                IncludeHidden = false,
                UnionCells = true,
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SheetFindAllRequest sheetFindAllRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SheetFindAllRequest
            {
                OperatorId = "ppgAxxx",
                Select = "a1Notation",
                Text = "DingTalk",
                FindOptions = findOptions,
            };
            try
            {
                client.SheetFindAllWithOptions("e54Lq3xxx", "Sheet1", sheetFindAllRequest, sheetFindAllHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| value | Array | 如果没有查到内容，value 会是一个空数组。 |
| a1Notation | String | 找到的单元格的地址。   - 如果 `unionCells` 设为 `true`，聚合后的地址可能为 `A1:B3` - 如果 `unionCells` 设为 `false`，则为单个单元格的地址，例如 `A1` |
| values | Array |  |
|  | Array of Any | 找到的单元格中的值（为展示文本）。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "value" : [ {
    "a1Notation" : "A1:B3",
    "values" : [ [ "1" ] ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.inputArgs.operatorIdIllegal | The operatorId is illegal. | operatorId不合法。 |
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.resource.notWorkbook | %s | 不支持的文档类型，请检查workbookId。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
| 503 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
