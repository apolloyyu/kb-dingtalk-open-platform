---
title: "插入下拉列表"
source_url: "https://open.dingtalk.com/document/development/insert-drop-down-list"
namespace: "development"
slug: "insert-drop-down-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 表格 > 单元格区域 > 插入下拉列表"
doc_id: "MV5kqHgic3"
updated_at: "2026-06-04 19:09:13"
---

> Source: https://open.dingtalk.com/document/development/insert-drop-down-list
> Path: 应用开发 / 服务端API / 文档/文件 > 表格 > 单元格区域 > 插入下拉列表
> Updated: 2026-06-04 19:09:13

# 插入下拉列表

调用本接口，可为钉钉表格中指定单元格区域设置下拉列表选项，支持自定义每个选项的文本值和标签颜色。适用于规范数据录入、提供预设选项（如状态、分类等）的场景，设置后用户仅能从预定义选项中选取值。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/ranges/{rangeAddress}/insertDropdownLists |
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
| rangeAddress | String | 是 | Range地址。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。      若操作人无权限，接口会报错 `The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| options | Array | 是 | 下拉列表选项数组。 |
| value | String | 是 | 下拉列表的值。 |
| color | String | 否 | 下拉列表的颜色，使用十六进制表示法，例如#ff0000。 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lq3xxx/sheets/Sheet1/ranges/A1:B1/insertDropdownLists?operatorId=ppgAxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "options" : [ {
    "value" : "选项1",
    "color" : "#ff0000"
  } ]
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
        com.aliyun.dingtalkdoc_1_0.models.InsertDropdownListsHeaders insertDropdownListsHeaders = new com.aliyun.dingtalkdoc_1_0.models.InsertDropdownListsHeaders();
        insertDropdownListsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.InsertDropdownListsRequest.InsertDropdownListsRequestOptions options0 = new com.aliyun.dingtalkdoc_1_0.models.InsertDropdownListsRequest.InsertDropdownListsRequestOptions()
                .setValue("选项1")
                .setColor("#ff0000");
        com.aliyun.dingtalkdoc_1_0.models.InsertDropdownListsRequest insertDropdownListsRequest = new com.aliyun.dingtalkdoc_1_0.models.InsertDropdownListsRequest()
                .setOperatorId("ppgAxxx")
                .setOptions(java.util.Arrays.asList(
                    options0
                ));
        try {
            client.insertDropdownListsWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", insertDropdownListsRequest, insertDropdownListsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        insert_dropdown_lists_headers = dingtalkdoc__1__0_models.InsertDropdownListsHeaders()
        insert_dropdown_lists_headers.x_acs_dingtalk_access_token = '<your access token>'
        options_0 = dingtalkdoc__1__0_models.InsertDropdownListsRequestOptions(
            value='选项1',
            color='#ff0000'
        )
        insert_dropdown_lists_request = dingtalkdoc__1__0_models.InsertDropdownListsRequest(
            operator_id='ppgAxxx',
            options=[
                options_0
            ]
        )
        try:
            client.insert_dropdown_lists_with_options('e54Lq3xxx', 'Sheet1', 'A1:B1', insert_dropdown_lists_request, insert_dropdown_lists_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        insert_dropdown_lists_headers = dingtalkdoc__1__0_models.InsertDropdownListsHeaders()
        insert_dropdown_lists_headers.x_acs_dingtalk_access_token = '<your access token>'
        options_0 = dingtalkdoc__1__0_models.InsertDropdownListsRequestOptions(
            value='选项1',
            color='#ff0000'
        )
        insert_dropdown_lists_request = dingtalkdoc__1__0_models.InsertDropdownListsRequest(
            operator_id='ppgAxxx',
            options=[
                options_0
            ]
        )
        try:
            await client.insert_dropdown_lists_with_options_async('e54Lq3xxx', 'Sheet1', 'A1:B1', insert_dropdown_lists_request, insert_dropdown_lists_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\InsertDropdownListsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\InsertDropdownListsRequest\options;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\InsertDropdownListsRequest;
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
        $insertDropdownListsHeaders = new InsertDropdownListsHeaders([]);
        $insertDropdownListsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $options0 = new options([
            "value" => "选项1",
            "color" => "#ff0000"
        ]);
        $insertDropdownListsRequest = new InsertDropdownListsRequest([
            "operatorId" => "ppgAxxx",
            "options" => [
                $options0
            ]
        ]);
        try {
            $client->insertDropdownListsWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", $insertDropdownListsRequest, $insertDropdownListsHeaders, new RuntimeOptions([]));
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

  insertDropdownListsHeaders := &dingtalkdoc_1_0.InsertDropdownListsHeaders{}
  insertDropdownListsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  options0 := &dingtalkdoc_1_0.InsertDropdownListsRequestOptions{
    Value: tea.String("选项1"),
    Color: tea.String("#ff0000"),
  }
  insertDropdownListsRequest := &dingtalkdoc_1_0.InsertDropdownListsRequest{
    OperatorId: tea.String("ppgAxxx"),
    Options: []*dingtalkdoc_1_0.InsertDropdownListsRequestOptions{options0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.InsertDropdownListsWithOptions(tea.String("e54Lq3xxx"), tea.String("Sheet1"), tea.String("A1:B1"), insertDropdownListsRequest, insertDropdownListsHeaders, &util.RuntimeOptions{})
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
    let insertDropdownListsHeaders = new $dingtalkdoc_1_0.InsertDropdownListsHeaders({ });
    insertDropdownListsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let options0 = new $dingtalkdoc_1_0.InsertDropdownListsRequestOptions({
      value: "选项1",
      color: "#ff0000",
    });
    let insertDropdownListsRequest = new $dingtalkdoc_1_0.InsertDropdownListsRequest({
      operatorId: "ppgAxxx",
      options: [
        options0
      ],
    });
    try {
      await client.insertDropdownListsWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", insertDropdownListsRequest, insertDropdownListsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsHeaders insertDropdownListsHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsHeaders();
            insertDropdownListsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsRequest.InsertDropdownListsRequestOptions options0 = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsRequest.InsertDropdownListsRequestOptions
            {
                Value = "选项1",
                Color = "#ff0000",
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsRequest insertDropdownListsRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsRequest
            {
                OperatorId = "ppgAxxx",
                Options = new List<AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.InsertDropdownListsRequest.InsertDropdownListsRequestOptions>
                {
                    options0
                },
            };
            try
            {
                client.InsertDropdownListsWithOptions("e54Lq3xxx", "Sheet1", "A1:B1", insertDropdownListsRequest, insertDropdownListsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| a1Notation | String | 单元格地址。 |

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
| 400 | invalidRequest.inputArgs.invalid | %s | 请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.resource.notWorkbook | %s | 不支持的文档类型，请检查workbookId。 |
| 400 | invalidRequest.document.stillInitializing | The document is still initializing. Please try again later. | 文档初始化中，请稍后重试。 |
| 403 | forbidden.operationIllegal | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
