---
title: "创建浮动图片"
source_url: "https://open.dingtalk.com/document/development/api-createfloatimage"
namespace: "development"
slug: "api-createfloatimage"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 表格 > 浮动图片 > 创建浮动图片"
doc_id: "mFciIl2alg"
updated_at: "2026-06-02 18:43:00"
---

> Source: https://open.dingtalk.com/document/development/api-createfloatimage
> Path: 应用开发 / 服务端API / 文档/文件 > 表格 > 浮动图片 > 创建浮动图片
> Updated: 2026-06-02 18:43:00

# 创建浮动图片

调用本接口，可获取钉钉表格指定工作表中所有浮动图片的列表信息。适用于需要批量读取工作表内浮动图片的场景，如导出、同步或审计等。返回结果包含每张图片的唯一标识、图片地址、锚点位置及尺寸偏移信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workbooks/{workbookId}/sheets/{sheetId}/floatImages |
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
| operatorId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。  **[!NOTE]**    若操作人无权限，接口会报错 `The operator has no permission`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| src | String | 是 | 浮动图片资源地址，需要通过调用[获取资源上传信息](0581-api-getresourceuploadinfo.md)接口获得 `resourceUrl`。 |
| anchor | Object | 是 | 浮动图片定位信息。 |
| row | Integer | 是 | 相对第几行定位，游标从 0 开始。 |
| col | Integer | 是 | 相对第几列定位，游标从 0 开始。 |
| coordinate | Object | 是 | 设置几何信息。 |
| width | double | 是 | 指定图片宽度，单位：像素。 |
| height | double | 是 | 指定图片高度，单位：像素。 |
| offsetX | double | 是 | 相对定位坐标的横向偏移量，单位：像素。 |
| offsetY | double | 是 | 相对定位坐标的纵向偏移量，单位：像素。 |

### 请求示例

HTTP

```
POST /v1.0/doc/workbooks/e54Lqxxxxx/sheets/Sheet1/floatImages?operatorId=ppgAQuxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f86e0bxxx
Content-Type:application/json

{
  "src" : "/core/api/resources/img/xxx",
  "anchor" : {
    "row" : 1,
    "col" : 1
  },
  "coordinate" : {
    "width" : 300.0,
    "height" : 300.0,
    "offsetX" : 8.0,
    "offsetY" : 8.0
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
        com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageHeaders createFloatImageHeaders = new com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageHeaders();
        createFloatImageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageRequest.CreateFloatImageRequestCoordinate coordinate = new com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageRequest.CreateFloatImageRequestCoordinate()
                .setWidth(300D)
                .setHeight(300D)
                .setOffsetX(8D)
                .setOffsetY(8D);
        com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageRequest.CreateFloatImageRequestAnchor anchor = new com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageRequest.CreateFloatImageRequestAnchor()
                .setRow(1)
                .setCol(1);
        com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageRequest createFloatImageRequest = new com.aliyun.dingtalkdoc_1_0.models.CreateFloatImageRequest()
                .setOperatorId("ppgAQuxxxxx")
                .setSrc("/core/api/resources/img/xxx")
                .setAnchor(anchor)
                .setCoordinate(coordinate);
        try {
            client.createFloatImageWithOptions("e54Lqxxxxx", "Sheet1", createFloatImageRequest, createFloatImageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_float_image_headers = dingtalkdoc__1__0_models.CreateFloatImageHeaders()
        create_float_image_headers.x_acs_dingtalk_access_token = '<your access token>'
        coordinate = dingtalkdoc__1__0_models.CreateFloatImageRequestCoordinate(
            width=300,
            height=300,
            offset_x=8,
            offset_y=8
        )
        anchor = dingtalkdoc__1__0_models.CreateFloatImageRequestAnchor(
            row=1,
            col=1
        )
        create_float_image_request = dingtalkdoc__1__0_models.CreateFloatImageRequest(
            operator_id='ppgAQuxxxxx',
            src='/core/api/resources/img/xxx',
            anchor=anchor,
            coordinate=coordinate
        )
        try:
            client.create_float_image_with_options('e54Lqxxxxx', 'Sheet1', create_float_image_request, create_float_image_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_float_image_headers = dingtalkdoc__1__0_models.CreateFloatImageHeaders()
        create_float_image_headers.x_acs_dingtalk_access_token = '<your access token>'
        coordinate = dingtalkdoc__1__0_models.CreateFloatImageRequestCoordinate(
            width=300,
            height=300,
            offset_x=8,
            offset_y=8
        )
        anchor = dingtalkdoc__1__0_models.CreateFloatImageRequestAnchor(
            row=1,
            col=1
        )
        create_float_image_request = dingtalkdoc__1__0_models.CreateFloatImageRequest(
            operator_id='ppgAQuxxxxx',
            src='/core/api/resources/img/xxx',
            anchor=anchor,
            coordinate=coordinate
        )
        try:
            await client.create_float_image_with_options_async('e54Lqxxxxx', 'Sheet1', create_float_image_request, create_float_image_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateFloatImageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateFloatImageRequest\coordinate;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateFloatImageRequest\anchor;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateFloatImageRequest;
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
        $createFloatImageHeaders = new CreateFloatImageHeaders([]);
        $createFloatImageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $coordinate = new coordinate([
            "width" => 300,
            "height" => 300,
            "offsetX" => 8,
            "offsetY" => 8
        ]);
        $anchor = new anchor([
            "row" => 1,
            "col" => 1
        ]);
        $createFloatImageRequest = new CreateFloatImageRequest([
            "operatorId" => "ppgAQuxxxxx",
            "src" => "/core/api/resources/img/xxx",
            "anchor" => $anchor,
            "coordinate" => $coordinate
        ]);
        try {
            $client->createFloatImageWithOptions("e54Lqxxxxx", "Sheet1", $createFloatImageRequest, $createFloatImageHeaders, new RuntimeOptions([]));
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

  createFloatImageHeaders := &dingtalkdoc_1_0.CreateFloatImageHeaders{}
  createFloatImageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  coordinate := &dingtalkdoc_1_0.CreateFloatImageRequestCoordinate{
    Width: tea.Float64(300),
    Height: tea.Float64(300),
    OffsetX: tea.Float64(8),
    OffsetY: tea.Float64(8),
  }
  anchor := &dingtalkdoc_1_0.CreateFloatImageRequestAnchor{
    Row: tea.Int32(1),
    Col: tea.Int32(1),
  }
  createFloatImageRequest := &dingtalkdoc_1_0.CreateFloatImageRequest{
    OperatorId: tea.String("ppgAQuxxxxx"),
    Src: tea.String("/core/api/resources/img/xxx"),
    Anchor: anchor,
    Coordinate: coordinate,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateFloatImageWithOptions(tea.String("e54Lqxxxxx"), tea.String("Sheet1"), createFloatImageRequest, createFloatImageHeaders, &util.RuntimeOptions{})
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
    let createFloatImageHeaders = new dingtalkdoc_1_0.CreateFloatImageHeaders({ });
    createFloatImageHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let coordinate = new dingtalkdoc_1_0.CreateFloatImageRequestCoordinate({
      width: 300,
      height: 300,
      offsetX: 8,
      offsetY: 8,
    });
    let anchor = new dingtalkdoc_1_0.CreateFloatImageRequestAnchor({
      row: 1,
      col: 1,
    });
    let createFloatImageRequest = new dingtalkdoc_1_0.CreateFloatImageRequest({
      operatorId: 'ppgAQuxxxxx',
      src: '/core/api/resources/img/xxx',
      anchor: anchor,
      coordinate: coordinate,
    });
    try {
      await client.createFloatImageWithOptions('e54Lqxxxxx', 'Sheet1', createFloatImageRequest, createFloatImageHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageHeaders createFloatImageHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageHeaders();
            createFloatImageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageRequest.CreateFloatImageRequestCoordinate coordinate = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageRequest.CreateFloatImageRequestCoordinate
            {
                Width = 300,
                Height = 300,
                OffsetX = 8,
                OffsetY = 8,
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageRequest.CreateFloatImageRequestAnchor anchor = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageRequest.CreateFloatImageRequestAnchor
            {
                Row = 1,
                Col = 1,
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageRequest createFloatImageRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateFloatImageRequest
            {
                OperatorId = "ppgAQuxxxxx",
                Src = "/core/api/resources/img/xxx",
                Anchor = anchor,
                Coordinate = coordinate,
            };
            try
            {
                client.CreateFloatImageWithOptions("e54Lqxxxxx", "Sheet1", createFloatImageRequest, createFloatImageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 浮动图片信息。 |
| id | String | 浮动图片的 id。 |
| src | String | 浮动图片的资源地址。 |
| anchor | Object | 锚点位置，指定图片固定在哪个单元格。 |
| row | Integer | 相对第几行定位，游标从 0 开始。 |
| col | Integer | 相对第几列定位，游标从 0 开始。 |
| coordinate | Object | 图片尺寸与相对锚点单元格的偏移量。 |
| width | double | 浮动图片的宽度。 |
| height | double | 浮动图片的高度。 |
| offsetX | double | 相对锚点单元格左上角的水平偏移量，单位：像素。 |
| offsetY | double | 相对锚点单元格左上角的垂直偏移量，单位：像素。 |
| success | Boolean | 成功状态。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "id" : "xxx",
    "src" : "/core/api/resources/img/xxx",
    "anchor" : {
      "row" : 1,
      "col" : 1
    },
    "coordinate" : {
      "width" : 300,
      "height" : 300,
      "offsetX" : 1,
      "offsetY" : 1
    }
  },
  "success" : true
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
| 403 | forbidden.acrossOrg | %s | 请求操作不合法，请查看错误信息。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 404 | invalidRequest.resource.notFound | %s | 请求失败，无法找到要访问的资源。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
