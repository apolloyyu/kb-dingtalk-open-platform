---
title: "创建条件格式规则"
source_url: "https://open.dingtalk.com/document/development/create-conditional-formatting-rules"
namespace: "development"
slug: "create-conditional-formatting-rules"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 表格 > 条件格式 > 创建条件格式规则"
doc_id: "yHyPSVrRgg"
updated_at: "2026-06-04 19:09:17"
---

> Source: https://open.dingtalk.com/document/development/create-conditional-formatting-rules
> Path: 应用开发 / 服务端API / 文档/文件 > 表格 > 条件格式 > 创建条件格式规则
> Updated: 2026-06-04 19:09:17

# 创建条件格式规则

调用本接口可在钉钉表格的指定工作表中创建条件格式规则，根据单元格的值或重复情况自动应用高亮样式。适用于需要对数据进行可视化标记的场景，例如将低于目标值的单元格标红、将重复录入的数据高亮显示以便排查，或将某个区间内的数值以特定背景色区分。规则创建后，满足条件的单元格将自动应用指定的字体颜色或背景色，无需手动逐一设置。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/conditionalFormattingRules |
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
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](0553-knowledge-base-overview.md) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](https://open.dingtalk.com/document/development/get-node)和[创建知识库文档](0567-create-team-space-document.md)接口获取。 |
| sheetId | String | 是 | 工作表ID或标题，可调用[获取所有工作表](0595-obtain-all-worksheets.md)接口获取id和工作表的标题。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。      若操作人无权限，接口会报错 `The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| ranges | Array of String | 是 | 单元格地址，使用A1表示法。 |
| duplicateCondition | Object | 否 | 重复值规则。 |
| operator | String | 否 | 运算符。目前仅支持duplicate，代表重复项。 |
| numberCondition | Object | 否 | 数字规则。 |
| operator | String | 否 | 比较运算符。可选值：   - **equal**： 等于 - **not-equal**：不等于 - **greater**：大于 - **greater-equal**：大于等于 - **less**：小于 - **less-equal**：小于等于 - **between**：在两者之间（含边界） - **not-between**：不在两者之间 |
| value1 | Any | 否 | value1 — 第一个比较值（必填）。 |
| value2 | Any | 否 | value2 — 第二个比较值（可选，仅在 operator 为 between 或 not-between 时需要提供，作为范围的上界。 |
| cellStyle | Object | 否 | 设定当前配置的规则的单元格样式。 |
| backgroundColor | String | 否 | 背景色，使用十六进制颜色表示法，如#ff0000。 |
| fontColor | String | 否 | 字体颜色。 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/conditionalFormattingRules?operatorId=ppgAxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "ranges" : [ "A1:B2" ],
  "duplicateCondition" : {
    "operator" : "duplicate"
  },
  "numberCondition" : {
    "operator" : "between",
    "value1" : "10",
    "value2" : "50"
  },
  "cellStyle" : {
    "backgroundColor" : "#ff0000",
    "fontColor" : "#ff0000"
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
        com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleHeaders createConditionalFormattingRuleHeaders = new com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleHeaders();
        createConditionalFormattingRuleHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestCellStyle cellStyle = new com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestCellStyle()
                .setBackgroundColor("#ff0000")
                .setFontColor("#ff0000");
        com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestNumberCondition numberCondition = new com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestNumberCondition()
                .setOperator("between")
                .setValue1(10)
                .setValue2(50);
        com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestDuplicateCondition duplicateCondition = new com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestDuplicateCondition()
                .setOperator("duplicate");
        com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest createConditionalFormattingRuleRequest = new com.aliyun.dingtalkdoc_1_0.models.CreateConditionalFormattingRuleRequest()
                .setOperatorId("ppgAxxx")
                .setRanges(java.util.Arrays.asList(
                    "A1:B2"
                ))
                .setDuplicateCondition(duplicateCondition)
                .setNumberCondition(numberCondition)
                .setCellStyle(cellStyle);
        try {
            client.createConditionalFormattingRuleWithOptions("e54Lq3xxx", "Sheet1", createConditionalFormattingRuleRequest, createConditionalFormattingRuleHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_conditional_formatting_rule_headers = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleHeaders()
        create_conditional_formatting_rule_headers.x_acs_dingtalk_access_token = '<your access token>'
        cell_style = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequestCellStyle(
            background_color='#ff0000',
            font_color='#ff0000'
        )
        number_condition = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequestNumberCondition(
            operator='between',
            value_1=10,
            value_2=50
        )
        duplicate_condition = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequestDuplicateCondition(
            operator='duplicate'
        )
        create_conditional_formatting_rule_request = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequest(
            operator_id='ppgAxxx',
            ranges=[
                'A1:B2'
            ],
            duplicate_condition=duplicate_condition,
            number_condition=number_condition,
            cell_style=cell_style
        )
        try:
            client.create_conditional_formatting_rule_with_options('e54Lq3xxx', 'Sheet1', create_conditional_formatting_rule_request, create_conditional_formatting_rule_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_conditional_formatting_rule_headers = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleHeaders()
        create_conditional_formatting_rule_headers.x_acs_dingtalk_access_token = '<your access token>'
        cell_style = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequestCellStyle(
            background_color='#ff0000',
            font_color='#ff0000'
        )
        number_condition = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequestNumberCondition(
            operator='between',
            value_1=10,
            value_2=50
        )
        duplicate_condition = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequestDuplicateCondition(
            operator='duplicate'
        )
        create_conditional_formatting_rule_request = dingtalkdoc__1__0_models.CreateConditionalFormattingRuleRequest(
            operator_id='ppgAxxx',
            ranges=[
                'A1:B2'
            ],
            duplicate_condition=duplicate_condition,
            number_condition=number_condition,
            cell_style=cell_style
        )
        try:
            await client.create_conditional_formatting_rule_with_options_async('e54Lq3xxx', 'Sheet1', create_conditional_formatting_rule_request, create_conditional_formatting_rule_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateConditionalFormattingRuleHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateConditionalFormattingRuleRequest\cellStyle;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateConditionalFormattingRuleRequest\numberCondition;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateConditionalFormattingRuleRequest\duplicateCondition;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateConditionalFormattingRuleRequest;
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
        $createConditionalFormattingRuleHeaders = new CreateConditionalFormattingRuleHeaders([]);
        $createConditionalFormattingRuleHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cellStyle = new cellStyle([
            "backgroundColor" => "#ff0000",
            "fontColor" => "#ff0000"
        ]);
        $numberCondition = new numberCondition([
            "operator" => "between",
            "value1" => 10,
            "value2" => 50
        ]);
        $duplicateCondition = new duplicateCondition([
            "operator" => "duplicate"
        ]);
        $createConditionalFormattingRuleRequest = new CreateConditionalFormattingRuleRequest([
            "operatorId" => "ppgAxxx",
            "ranges" => [
                "A1:B2"
            ],
            "duplicateCondition" => $duplicateCondition,
            "numberCondition" => $numberCondition,
            "cellStyle" => $cellStyle
        ]);
        try {
            $client->createConditionalFormattingRuleWithOptions("e54Lq3xxx", "Sheet1", $createConditionalFormattingRuleRequest, $createConditionalFormattingRuleHeaders, new RuntimeOptions([]));
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

  createConditionalFormattingRuleHeaders := &dingtalkdoc_1_0.CreateConditionalFormattingRuleHeaders{}
  createConditionalFormattingRuleHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cellStyle := &dingtalkdoc_1_0.CreateConditionalFormattingRuleRequestCellStyle{
    BackgroundColor: tea.String("#ff0000"),
    FontColor: tea.String("#ff0000"),
  }
  numberCondition := &dingtalkdoc_1_0.CreateConditionalFormattingRuleRequestNumberCondition{
    Operator: tea.String("between"),
    Value1: tea.Int(10),
    Value2: tea.Int(50),
  }
  duplicateCondition := &dingtalkdoc_1_0.CreateConditionalFormattingRuleRequestDuplicateCondition{
    Operator: tea.String("duplicate"),
  }
  createConditionalFormattingRuleRequest := &dingtalkdoc_1_0.CreateConditionalFormattingRuleRequest{
    OperatorId: tea.String("ppgAxxx"),
    Ranges: []*string{tea.String("A1:B2")},
    DuplicateCondition: duplicateCondition,
    NumberCondition: numberCondition,
    CellStyle: cellStyle,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateConditionalFormattingRuleWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), createConditionalFormattingRuleRequest, createConditionalFormattingRuleHeaders, &util.RuntimeOptions{})
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
    let createConditionalFormattingRuleHeaders = new dingtalkdoc_1_0.CreateConditionalFormattingRuleHeaders({ });
    createConditionalFormattingRuleHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let cellStyle = new dingtalkdoc_1_0.CreateConditionalFormattingRuleRequestCellStyle({
      backgroundColor: '#ff0000',
      fontColor: '#ff0000',
    });
    let numberCondition = new dingtalkdoc_1_0.CreateConditionalFormattingRuleRequestNumberCondition({
      operator: 'between',
      value1: 10,
      value2: 50,
    });
    let duplicateCondition = new dingtalkdoc_1_0.CreateConditionalFormattingRuleRequestDuplicateCondition({
      operator: 'duplicate',
    });
    let createConditionalFormattingRuleRequest = new dingtalkdoc_1_0.CreateConditionalFormattingRuleRequest({
      operatorId: 'ppgAxxx',
      ranges: [
        'A1:B2'
      ],
      duplicateCondition: duplicateCondition,
      numberCondition: numberCondition,
      cellStyle: cellStyle,
    });
    try {
      await client.createConditionalFormattingRuleWithOptions('e54Lq3xxx', 'Sheet1', createConditionalFormattingRuleRequest, createConditionalFormattingRuleHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleHeaders createConditionalFormattingRuleHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleHeaders();
            createConditionalFormattingRuleHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestCellStyle cellStyle = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestCellStyle
            {
                BackgroundColor = "#ff0000",
                FontColor = "#ff0000",
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestNumberCondition numberCondition = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestNumberCondition
            {
                Operator = "between",
                Value1 = 10,
                Value2 = 50,
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestDuplicateCondition duplicateCondition = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest.CreateConditionalFormattingRuleRequestDuplicateCondition
            {
                Operator = "duplicate",
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest createConditionalFormattingRuleRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateConditionalFormattingRuleRequest
            {
                OperatorId = "ppgAxxx",
                Ranges = new List<string>
                {
                    "A1:B2"
                },
                DuplicateCondition = duplicateCondition,
                NumberCondition = numberCondition,
                CellStyle = cellStyle,
            };
            try
            {
                client.CreateConditionalFormattingRuleWithOptions("e54Lq3xxx", "Sheet1", createConditionalFormattingRuleRequest, createConditionalFormattingRuleHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 条件格式ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "cf-xxxxx"
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
