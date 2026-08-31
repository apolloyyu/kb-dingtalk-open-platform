---
title: "筛选排序"
source_url: "https://open.dingtalk.com/document/development/api-sortfilter"
namespace: "development"
slug: "api-sortfilter"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 筛选 > 筛选排序"
doc_id: "lmwIbIHrNM"
updated_at: "2026-06-04 19:09:19"
---

> Source: https://open.dingtalk.com/document/development/api-sortfilter
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 筛选 > 筛选排序
> Updated: 2026-06-04 19:09:19

# 筛选排序

调用本接口可对全局筛选范围内的数据按指定列进行升序或降序排序，适用于需要对筛选后的数据进行有序展示的场景，例如将销售数据按金额从高到低排列，或将任务列表按截止日期升序排序。

## **接口调用说明**

排序操作会永久改变工作表中数据行的实际存储顺序，而非仅改变显示顺序。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/filter/sort |
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
| workbookId | String | 是 | 表格文件 ID ，[知识库 API](https://open.dingtalk.com/document/orgapp/knowledge-base-overview) 返回的`nodeId(dentryUuid)`即是表格`workbookId`，可通过调用[获取节点](https://open.dingtalk.com/document/orgapp/get-node)和[创建知识库文档](https://open.dingtalk.com/document/orgapp/create-team-space-document)接口获取。 |
| sheetId | String | 是 | 工作表ID或名称，可调用[获取所有工作表](https://open.dingtalk.com/document/orgapp/obtain-all-worksheets)接口获取id或name参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId。   - 可通过[通过免登码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-a-user-by-using-the-log-free)接口获取unionid参数值。 - 可调用[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details)接口获取unionid参数值。       若操作人无权限，接口会报错`The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| field | Object | 是 | 排序规则对象。 |
| column | Long | 是 | 列偏移量，相对于筛选范围首列，从 0 开始。 |
| ascending | Boolean | 否 | 是否升序排序。默认为 `true`（升序）。设置为 `false` 则降序排序。 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/filter/sort?operatorId=ppgAxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f86e0bxxx
Content-Type:application/json

{
  "field" : {
    "column" : 0,
    "ascending" : false
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
        com.aliyun.dingtalkdoc_1_0.models.SortFilterHeaders sortFilterHeaders = new com.aliyun.dingtalkdoc_1_0.models.SortFilterHeaders();
        sortFilterHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.SortFilterRequest.SortFilterRequestField field = new com.aliyun.dingtalkdoc_1_0.models.SortFilterRequest.SortFilterRequestField()
                .setColumn(0L)
                .setAscending(false);
        com.aliyun.dingtalkdoc_1_0.models.SortFilterRequest sortFilterRequest = new com.aliyun.dingtalkdoc_1_0.models.SortFilterRequest()
                .setOperatorId("ppgAxxx")
                .setField(field);
        try {
            client.sortFilterWithOptions("e54Lq3xxx", "Sheet1", sortFilterRequest, sortFilterHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        sort_filter_headers = dingtalkdoc__1__0_models.SortFilterHeaders()
        sort_filter_headers.x_acs_dingtalk_access_token = '<your access token>'
        field = dingtalkdoc__1__0_models.SortFilterRequestField(
            column=0,
            ascending=False
        )
        sort_filter_request = dingtalkdoc__1__0_models.SortFilterRequest(
            operator_id='ppgAxxx',
            field=field
        )
        try:
            client.sort_filter_with_options('e54Lq3xxx', 'Sheet1', sort_filter_request, sort_filter_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sort_filter_headers = dingtalkdoc__1__0_models.SortFilterHeaders()
        sort_filter_headers.x_acs_dingtalk_access_token = '<your access token>'
        field = dingtalkdoc__1__0_models.SortFilterRequestField(
            column=0,
            ascending=False
        )
        sort_filter_request = dingtalkdoc__1__0_models.SortFilterRequest(
            operator_id='ppgAxxx',
            field=field
        )
        try:
            await client.sort_filter_with_options_async('e54Lq3xxx', 'Sheet1', sort_filter_request, sort_filter_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SortFilterHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SortFilterRequest\field;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\SortFilterRequest;
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
        $sortFilterHeaders = new SortFilterHeaders([]);
        $sortFilterHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $field = new field([
            "column" => 0,
            "ascending" => false
        ]);
        $sortFilterRequest = new SortFilterRequest([
            "operatorId" => "ppgAxxx",
            "field" => $field
        ]);
        try {
            $client->sortFilterWithOptions("e54Lq3xxx", "Sheet1", $sortFilterRequest, $sortFilterHeaders, new RuntimeOptions([]));
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

  sortFilterHeaders := &dingtalkdoc_1_0.SortFilterHeaders{}
  sortFilterHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  field := &dingtalkdoc_1_0.SortFilterRequestField{
    Column: tea.Int64(0),
    Ascending: tea.Bool(false),
  }
  sortFilterRequest := &dingtalkdoc_1_0.SortFilterRequest{
    OperatorId: tea.String("ppgAxxx"),
    Field: field,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SortFilterWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), sortFilterRequest, sortFilterHeaders, &util.RuntimeOptions{})
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
    let sortFilterHeaders = new dingtalkdoc_1_0.SortFilterHeaders({ });
    sortFilterHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let field = new dingtalkdoc_1_0.SortFilterRequestField({
      column: 0,
      ascending: false,
    });
    let sortFilterRequest = new dingtalkdoc_1_0.SortFilterRequest({
      operatorId: 'ppgAxxx',
      field: field,
    });
    try {
      await client.sortFilterWithOptions('e54Lq3xxx', 'Sheet1', sortFilterRequest, sortFilterHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SortFilterHeaders sortFilterHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SortFilterHeaders();
            sortFilterHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SortFilterRequest.SortFilterRequestField field = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SortFilterRequest.SortFilterRequestField
            {
                Column = 0,
                Ascending = false,
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SortFilterRequest sortFilterRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.SortFilterRequest
            {
                OperatorId = "ppgAxxx",
                Field = field,
            };
            try
            {
                client.SortFilterWithOptions("e54Lq3xxx", "Sheet1", sortFilterRequest, sortFilterHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 筛选的唯一标识符。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "filter-xxxxx"
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
