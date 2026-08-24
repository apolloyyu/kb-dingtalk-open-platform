---
title: "获取资源上传信息"
source_url: "https://open.dingtalk.com/document/development/api-getresourceuploadinfo"
namespace: "development"
slug: "api-getresourceuploadinfo"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 文档 > 文档 > 获取资源上传信息"
doc_id: "vbphfGspL2"
updated_at: "2026-06-02 18:38:02"
---

> Source: https://open.dingtalk.com/document/development/api-getresourceuploadinfo
> Path: 应用开发 / 服务端API / 文档/文件 > 文档 > 文档 > 获取资源上传信息
> Updated: 2026-06-02 18:38:02

# 获取资源上传信息

调用该接口可以查询文档指定资源的上传地址。

## 接口调用说明

资源指文档中的图片/文件等附件。该接口一般配合其它产品的上传附件接口使用。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/docs/resources/{docId}/uploadInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.File.Read-企业存储文件读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| docId | String | 是 | 文档ID (dentryUuid/documentId/workbookId/baseId)，可通过以下两种方式获取：   - 调用[创建知识库文档](0567-create-team-space-document.md)接口获取。 - 调用[获取节点列表](0571-get-node-list.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人的unionId，可通过调用[查询用户详情](0056-query-user-details.md)接口或[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| size | Long | 是 | 资源大小，单位：字节。 |
| mediaType | String | 是 | 资源类型，具体值请参考 [MIME Types](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/MIME_types/Common_types)。 |
| resourceName | String | 是 | 资源名称。 |

### 请求示例

HTTP

```
POST /v1.0/doc/docs/resources/xxxxx/uploadInfos/query?operatorId=xxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "size" : 200,
  "mediaType" : "image/jpeg",
  "resourceName" : "logo.jpg"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
        com.aliyun.dingtalkdoc_1_0.models.GetResourceUploadInfoHeaders getResourceUploadInfoHeaders = new com.aliyun.dingtalkdoc_1_0.models.GetResourceUploadInfoHeaders();
        getResourceUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.GetResourceUploadInfoRequest getResourceUploadInfoRequest = new com.aliyun.dingtalkdoc_1_0.models.GetResourceUploadInfoRequest()
                .setOperatorId("xxxxx")
                .setSize(200L)
                .setMediaType("image/jpeg")
                .setResourceName("logo.jpg");
        try {
            client.getResourceUploadInfoWithOptions("xxxxx", getResourceUploadInfoRequest, getResourceUploadInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_resource_upload_info_headers = dingtalkdoc__1__0_models.GetResourceUploadInfoHeaders()
        get_resource_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_resource_upload_info_request = dingtalkdoc__1__0_models.GetResourceUploadInfoRequest(
            operator_id='xxxxx',
            size=200,
            media_type='image/jpeg',
            resource_name='logo.jpg'
        )
        try:
            client.get_resource_upload_info_with_options('xxxxx', get_resource_upload_info_request, get_resource_upload_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_resource_upload_info_headers = dingtalkdoc__1__0_models.GetResourceUploadInfoHeaders()
        get_resource_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_resource_upload_info_request = dingtalkdoc__1__0_models.GetResourceUploadInfoRequest(
            operator_id='xxxxx',
            size=200,
            media_type='image/jpeg',
            resource_name='logo.jpg'
        )
        try:
            await client.get_resource_upload_info_with_options_async('xxxxx', get_resource_upload_info_request, get_resource_upload_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetResourceUploadInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetResourceUploadInfoRequest;
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
        $getResourceUploadInfoHeaders = new GetResourceUploadInfoHeaders([]);
        $getResourceUploadInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getResourceUploadInfoRequest = new GetResourceUploadInfoRequest([
            "operatorId" => "xxxxx",
            "size" => 200,
            "mediaType" => "image/jpeg",
            "resourceName" => "logo.jpg"
        ]);
        try {
            $client->getResourceUploadInfoWithOptions("xxxxx", $getResourceUploadInfoRequest, $getResourceUploadInfoHeaders, new RuntimeOptions([]));
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

  getResourceUploadInfoHeaders := &dingtalkdoc_1_0.GetResourceUploadInfoHeaders{}
  getResourceUploadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getResourceUploadInfoRequest := &dingtalkdoc_1_0.GetResourceUploadInfoRequest{
    OperatorId: tea.String("xxxxx"),
    Size: tea.Int64(200),
    MediaType: tea.String("image/jpeg"),
    ResourceName: tea.String("logo.jpg"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetResourceUploadInfoWithOptions(tea.String("xxxxx"), getResourceUploadInfoRequest, getResourceUploadInfoHeaders, &util.RuntimeOptions{})
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
    let getResourceUploadInfoHeaders = new dingtalkdoc_1_0.GetResourceUploadInfoHeaders({ });
    getResourceUploadInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getResourceUploadInfoRequest = new dingtalkdoc_1_0.GetResourceUploadInfoRequest({
      operatorId: 'xxxxx',
      size: 200,
      mediaType: 'image/jpeg',
      resourceName: 'logo.jpg',
    });
    try {
      await client.getResourceUploadInfoWithOptions('xxxxx', getResourceUploadInfoRequest, getResourceUploadInfoHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetResourceUploadInfoHeaders getResourceUploadInfoHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetResourceUploadInfoHeaders();
            getResourceUploadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetResourceUploadInfoRequest getResourceUploadInfoRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetResourceUploadInfoRequest
            {
                OperatorId = "xxxxx",
                Size = 200,
                MediaType = "image/jpeg",
                ResourceName = "logo.jpg",
            };
            try
            {
                client.GetResourceUploadInfoWithOptions("xxxxx", getResourceUploadInfoRequest, getResourceUploadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否成功。 |
| result | Object | 结果。 |
| uploadUrl | String | 上传url。 |
| resourceId | String | 资源ID。 |
| resourceUrl | String | 资源路径。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "uploadUrl" : "https://xxx.com?Expires=xxx&Signature=xxx",
    "resourceId" : "6c6a466c-6a52-4aa0-a80f-13896e635145",
    "resourceUrl" : "/core/api/resources/img/xxx"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 403 | permissionDenied | %s | 无权限 |
| 404 | docNotExist | %s | 文档不存在 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
