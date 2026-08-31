---
title: "查找工作表中的单元格"
source_url: "https://open.dingtalk.com/document/development/find-the-next-eligible-cell"
namespace: "development"
slug: "find-the-next-eligible-cell"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 单元格区域 > 查找工作表中的单元格"
doc_id: "fgJfZ6cq0d"
updated_at: "2026-06-03 16:43:35"
---

> Source: https://open.dingtalk.com/document/development/find-the-next-eligible-cell
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 单元格区域 > 查找工作表中的单元格
> Updated: 2026-06-03 16:43:35

# 查找工作表中的单元格

根据指定的条件查找匹配给定字符串的下一个单元格。搜索范围为指定区域（即 rangeAddress）左上角单元格之后的整个工作表。如果指定了findOptions.scope参数，则搜索范围再与其取交集。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress}/findNext |
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
| workbookId | String | 是 | 表格文件 ID，传递`nodeId`（dentryUuid）即表格`workbookId`，可通过调用[获取节点](0570-get-knowledge-base-acquisition-node.md)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表的ID或标题，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id或者传工作表的标题。  image |
| rangeAddress | String | 是 | 开始查找的起始位置，从该区域左上角的单元格开始（但并不包括该单元格）。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人unionId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| text | String | 是 | 要查找的文本。 |
| findOptions | Object | 否 | 查找选项。 |
| matchEntireCell | Boolean | 否 | 是否匹配整个单元格：   - **true**：是 - **false**：否 |
| matchCase | Boolean | 否 | 是否匹配大小写：   - **true**：是 - **false**：否 |
| useRegExp | Boolean | 否 | text参数是否为正则表达式：   - **true**：是 - **false**：否 |
| matchFormulaText | Boolean | 否 | 是否在公式内搜索：   - **true**：是 - **false**：否 |
| scope | String | 否 | 搜索范围。格式为A1表示法指代的Range地址。 |
| includeHidden | Boolean | 否 | 是否包含隐藏的单元格，即隐藏行列、筛选、分组等功能导致的不可见单元格，但不包含无权限查看的单元格。   - **true**：是 - **false**：否 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/ranges/B2:C3/findNext?operatorId=ppgAxxx HTTP/1.1
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
    "includeHidden" : true
  }
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
        com.aliyun.dingtalkdoc_1_0.models.RangeFindNextHeaders rangeFindNextHeaders = new com.aliyun.dingtalkdoc_1_0.models.RangeFindNextHeaders();
        rangeFindNextHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.RangeFindNextRequest.RangeFindNextRequestFindOptions findOptions = new com.aliyun.dingtalkdoc_1_0.models.RangeFindNextRequest.RangeFindNextRequestFindOptions()
                .setMatchEntireCell(true)
                .setMatchCase(true)
                .setUseRegExp(true)
                .setMatchFormulaText(true)
                .setScope("A:A")
                .setIncludeHidden(true);
        com.aliyun.dingtalkdoc_1_0.models.RangeFindNextRequest rangeFindNextRequest = new com.aliyun.dingtalkdoc_1_0.models.RangeFindNextRequest()
                .setOperatorId("ppgAxxx")
                .setText("DingTalk")
                .setFindOptions(findOptions);
        try {
            client.rangeFindNextWithOptions("e54Lq3xxx", "Sheet1", "B2:C3", rangeFindNextRequest, rangeFindNextHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        range_find_next_headers = dingtalkdoc__1__0_models.RangeFindNextHeaders()
        range_find_next_headers.x_acs_dingtalk_access_token = '<your access token>'
        find_options = dingtalkdoc__1__0_models.RangeFindNextRequestFindOptions(
            match_entire_cell=True,
            match_case=True,
            use_reg_exp=True,
            match_formula_text=True,
            scope='A:A',
            include_hidden=True
        )
        range_find_next_request = dingtalkdoc__1__0_models.RangeFindNextRequest(
            operator_id='ppgAxxx',
            text='DingTalk',
            find_options=find_options
        )
        try:
            client.range_find_next_with_options('e54Lq3xxx', 'Sheet1', 'B2:C3', range_find_next_request, range_find_next_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        range_find_next_headers = dingtalkdoc__1__0_models.RangeFindNextHeaders()
        range_find_next_headers.x_acs_dingtalk_access_token = '<your access token>'
        find_options = dingtalkdoc__1__0_models.RangeFindNextRequestFindOptions(
            match_entire_cell=True,
            match_case=True,
            use_reg_exp=True,
            match_formula_text=True,
            scope='A:A',
            include_hidden=True
        )
        range_find_next_request = dingtalkdoc__1__0_models.RangeFindNextRequest(
            operator_id='ppgAxxx',
            text='DingTalk',
            find_options=find_options
        )
        try:
            await client.range_find_next_with_options_async('e54Lq3xxx', 'Sheet1', 'B2:C3', range_find_next_request, range_find_next_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\RangeFindNextHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\RangeFindNextRequest\findOptions;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\RangeFindNextRequest;
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
        $rangeFindNextHeaders = new RangeFindNextHeaders([]);
        $rangeFindNextHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $findOptions = new findOptions([
            "matchEntireCell" => true,
            "matchCase" => true,
            "useRegExp" => true,
            "matchFormulaText" => true,
            "scope" => "A:A",
            "includeHidden" => true
        ]);
        $rangeFindNextRequest = new RangeFindNextRequest([
            "operatorId" => "ppgAxxx",
            "text" => "DingTalk",
            "findOptions" => $findOptions
        ]);
        try {
            $client->rangeFindNextWithOptions("e54Lq3xxx", "Sheet1", "B2:C3", $rangeFindNextRequest, $rangeFindNextHeaders, new RuntimeOptions([]));
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

  rangeFindNextHeaders := &dingtalkdoc_1_0.RangeFindNextHeaders{}
  rangeFindNextHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  findOptions := &dingtalkdoc_1_0.RangeFindNextRequestFindOptions{
    MatchEntireCell: tea.Bool(true),
    MatchCase: tea.Bool(true),
    UseRegExp: tea.Bool(true),
    MatchFormulaText: tea.Bool(true),
    Scope: tea.String("A:A"),
    IncludeHidden: tea.Bool(true),
  }
  rangeFindNextRequest := &dingtalkdoc_1_0.RangeFindNextRequest{
    OperatorId: tea.String("ppgAxxx"),
    Text: tea.String("DingTalk"),
    FindOptions: findOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RangeFindNextWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), tea.String("B2:C3"), rangeFindNextRequest, rangeFindNextHeaders, &util.RuntimeOptions{})
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
    let rangeFindNextHeaders = new dingtalkdoc_1_0.RangeFindNextHeaders({ });
    rangeFindNextHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let findOptions = new dingtalkdoc_1_0.RangeFindNextRequestFindOptions({
      matchEntireCell: true,
      matchCase: true,
      useRegExp: true,
      matchFormulaText: true,
      scope: 'A:A',
      includeHidden: true,
    });
    let rangeFindNextRequest = new dingtalkdoc_1_0.RangeFindNextRequest({
      operatorId: 'ppgAxxx',
      text: 'DingTalk',
      findOptions: findOptions,
    });
    try {
      await client.rangeFindNextWithOptions('e54Lq3xxx', 'Sheet1', 'B2:C3', rangeFindNextRequest, rangeFindNextHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.RangeFindNextHeaders rangeFindNextHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.RangeFindNextHeaders();
            rangeFindNextHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.RangeFindNextRequest.RangeFindNextRequestFindOptions findOptions = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.RangeFindNextRequest.RangeFindNextRequestFindOptions
            {
                MatchEntireCell = true,
                MatchCase = true,
                UseRegExp = true,
                MatchFormulaText = true,
                Scope = "A:A",
                IncludeHidden = true,
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.RangeFindNextRequest rangeFindNextRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.RangeFindNextRequest
            {
                OperatorId = "ppgAxxx",
                Text = "DingTalk",
                FindOptions = findOptions,
            };
            try
            {
                client.RangeFindNextWithOptions("e54Lq3xxx", "Sheet1", "B2:C3", rangeFindNextRequest, rangeFindNextHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| a1Notation | String | 查找到的单元格的地址，使用A1表示形式。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "a1Notation" : "C2"
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
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
