---
title: "批量获取文件缩略图"
source_url: "https://open.dingtalk.com/document/development/get-file-thumbnails-in-bulk"
namespace: "development"
slug: "get-file-thumbnails-in-bulk"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 批量获取文件缩略图"
doc_id: "mS8pSXRxNj"
updated_at: "2026-06-15 11:26:25"
---

> Source: https://open.dingtalk.com/document/development/get-file-thumbnails-in-bulk
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 批量获取文件缩略图
> Updated: 2026-06-15 11:26:25

# 批量获取文件缩略图

调用本接口，批量获取文件的缩略图信息。

## **接口调用说明**

在存储空间内上传的图片、wps格式文档（Word、Excel和PowerPoint）、PDF格式文件和txt格式文件，会异步自动生成缩略图。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/thumbnails/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Read-企业存储文件读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间ID，调用[添加空间](0652-add-space.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dentryIds | Array of String | 是 | 文件ID，最大值30，调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取id参数值。 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/785xxxxx/thumbnails/query?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "dentryIds" : [ "790xxxxx" ]
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
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.GetDentryThumbnailsHeaders getDentryThumbnailsHeaders = new com.aliyun.dingtalkstorage_1_0.models.GetDentryThumbnailsHeaders();
        getDentryThumbnailsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.GetDentryThumbnailsRequest getDentryThumbnailsRequest = new com.aliyun.dingtalkstorage_1_0.models.GetDentryThumbnailsRequest();
        try {
            client.getDentryThumbnailsWithOptions("", getDentryThumbnailsRequest, getDentryThumbnailsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.storage_1_0.client import Client as dingtalkstorage_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_1_0 import models as dingtalkstorage__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_dentry_thumbnails_headers = dingtalkstorage__1__0_models.GetDentryThumbnailsHeaders()
        get_dentry_thumbnails_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_dentry_thumbnails_request = dingtalkstorage__1__0_models.GetDentryThumbnailsRequest()
        try:
            client.get_dentry_thumbnails_with_options('', get_dentry_thumbnails_request, get_dentry_thumbnails_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_dentry_thumbnails_headers = dingtalkstorage__1__0_models.GetDentryThumbnailsHeaders()
        get_dentry_thumbnails_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_dentry_thumbnails_request = dingtalkstorage__1__0_models.GetDentryThumbnailsRequest()
        try:
            await client.get_dentry_thumbnails_with_options_async('', get_dentry_thumbnails_request, get_dentry_thumbnails_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetDentryThumbnailsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetDentryThumbnailsRequest;
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
        $getDentryThumbnailsHeaders = new GetDentryThumbnailsHeaders([]);
        $getDentryThumbnailsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getDentryThumbnailsRequest = new GetDentryThumbnailsRequest([]);
        try {
            $client->getDentryThumbnailsWithOptions("", $getDentryThumbnailsRequest, $getDentryThumbnailsHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
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
func CreateClient () (_result *dingtalkstorage_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_1_0.Client{}
  _result, _err = dingtalkstorage_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getDentryThumbnailsHeaders := &dingtalkstorage_1_0.GetDentryThumbnailsHeaders{}
  getDentryThumbnailsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getDentryThumbnailsRequest := &dingtalkstorage_1_0.GetDentryThumbnailsRequest{}
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetDentryThumbnailsWithOptions(tea.String(""), getDentryThumbnailsRequest, getDentryThumbnailsHeaders, &util.RuntimeOptions{})
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
const dingtalkstorage_1_0 = require('@alicloud/dingtalk/storage_1_0');
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
    return new dingtalkstorage_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getDentryThumbnailsHeaders = new dingtalkstorage_1_0.GetDentryThumbnailsHeaders({ });
    getDentryThumbnailsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getDentryThumbnailsRequest = new dingtalkstorage_1_0.GetDentryThumbnailsRequest({ });
    try {
      await client.getDentryThumbnailsWithOptions('', getDentryThumbnailsRequest, getDentryThumbnailsHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryThumbnailsHeaders getDentryThumbnailsHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryThumbnailsHeaders();
            getDentryThumbnailsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryThumbnailsRequest getDentryThumbnailsRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryThumbnailsRequest();
            try
            {
                client.GetDentryThumbnailsWithOptions("", getDentryThumbnailsRequest, getDentryThumbnailsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| resultItems | Array | 缩略图获取结果列表。 |
| spaceId | String | 文件所在空间ID。 |
| dentryId | String | 文件ID。 |
| success | Boolean | 是否成功获取到缩略图信息，true表示成功。 |
| errorCode | String | 错误原因。 |
| thumbnail | Object | 缩略图信息。 |
| width | Integer | 缩略图宽度，单位px。 |
| height | Integer | 缩略图高度，单位px。 |
| url | String | 缩略图url。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "resultItems" : [ {
    "spaceId" : "785xxxxx",
    "dentryId" : "790xxxxx",
    "success" : true,
    "errorCode" : "permissionDenied",
    "thumbnail" : {
      "width" : 64,
      "height" : 64,
      "url" : "url"
    }
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryIds | %s | 参数错误-dentryIds |
| 400 | permissionDenied | %s | 无权限获取缩略图 |
| 400 | dentryNotExist | %s | 文件不存在 |
| 400 | dentryFormatNotSupport | %s | 该格式不支持获取缩略图 |
| 400 | fileViral | %s | 病毒文件 |
| 400 | fileMalicious | %s | 恶意文件 |
| 403 | thumbnailNotExist | %s | 缩略图不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
