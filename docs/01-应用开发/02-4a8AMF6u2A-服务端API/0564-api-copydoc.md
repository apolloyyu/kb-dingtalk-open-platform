---
title: "复制文档"
source_url: "https://open.dingtalk.com/document/development/api-copydoc"
namespace: "development"
slug: "api-copydoc"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 知识库 > 知识库目录树管理 > 复制文档"
doc_id: "Cb7CJKB51v"
updated_at: "2026-06-03 10:13:07"
---

> Source: https://open.dingtalk.com/document/development/api-copydoc
> Path: 应用开发 / 服务端API / 文档/文件 > 知识库 > 知识库目录树管理 > 复制文档
> Updated: 2026-06-03 10:13:07

# 复制文档

调用本接口，复制知识库或钉盘文档。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/doc/dentries/copy |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-SNS.Document.WorkspaceDocument.Write-SNS知识库文档写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，通过调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| param | Object | 是 | 必选参数。 |
| sourceDentryUuid | String | 是 | 源文件唯一标识，调用[搜索文件](0638-search-for-files.md)接口获取的dentryUUid字段值。 |
| targetParentDentryUuid | String | 是 | 目标文件唯一标识，调用[搜索文件](0638-search-for-files.md)接口获取的dentryUUid字段值。 |
| targetPreDentryUuid | String | 否 | 目标的上一个文件唯一标识（可选），调用[搜索文件](0638-search-for-files.md)接口获取的dentryUUid字段值。 |

### 请求示例

HTTP

```
POST /v2.0/doc/dentries/copy HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:example-token
Content-Type:application/json

{
  "param" : {
    "sourceDentryUuid" : "dentryUuid",
    "targetParentDentryUuid" : "dentryUuid",
    "targetPreDentryUuid" : "dentryUuid"
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
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkdoc_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdoc_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_2_0.models.CopyDocHeaders copyDocHeaders = new com.aliyun.dingtalkdoc_2_0.models.CopyDocHeaders();
        copyDocHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_2_0.models.CopyDocRequest.CopyDocRequestParam param = new com.aliyun.dingtalkdoc_2_0.models.CopyDocRequest.CopyDocRequestParam()
                .setSourceDentryUuid("dentryUuid")
                .setTargetParentDentryUuid("dentryUuid")
                .setTargetPreDentryUuid("dentryUuid");
        com.aliyun.dingtalkdoc_2_0.models.CopyDocRequest copyDocRequest = new com.aliyun.dingtalkdoc_2_0.models.CopyDocRequest()
                .setParam(param);
        try {
            client.copyDocWithOptions(copyDocRequest, copyDocHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.doc_2_0.client import Client as dingtalkdoc_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_2_0 import models as dingtalkdoc__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        copy_doc_headers = dingtalkdoc__2__0_models.CopyDocHeaders()
        copy_doc_headers.x_acs_dingtalk_access_token = '<your access token>'
        param = dingtalkdoc__2__0_models.CopyDocRequestParam(
            source_dentry_uuid='dentryUuid',
            target_parent_dentry_uuid='dentryUuid',
            target_pre_dentry_uuid='dentryUuid'
        )
        copy_doc_request = dingtalkdoc__2__0_models.CopyDocRequest(
            param=param
        )
        try:
            client.copy_doc_with_options(copy_doc_request, copy_doc_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        copy_doc_headers = dingtalkdoc__2__0_models.CopyDocHeaders()
        copy_doc_headers.x_acs_dingtalk_access_token = '<your access token>'
        param = dingtalkdoc__2__0_models.CopyDocRequestParam(
            source_dentry_uuid='dentryUuid',
            target_parent_dentry_uuid='dentryUuid',
            target_pre_dentry_uuid='dentryUuid'
        )
        copy_doc_request = dingtalkdoc__2__0_models.CopyDocRequest(
            param=param
        )
        try:
            await client.copy_doc_with_options_async(copy_doc_request, copy_doc_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\CopyDocHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\CopyDocRequest\param;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\CopyDocRequest;
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
        $copyDocHeaders = new CopyDocHeaders([]);
        $copyDocHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $param = new param([
            "sourceDentryUuid" => "dentryUuid",
            "targetParentDentryUuid" => "dentryUuid",
            "targetPreDentryUuid" => "dentryUuid"
        ]);
        $copyDocRequest = new CopyDocRequest([
            "param" => $param
        ]);
        try {
            $client->copyDocWithOptions($copyDocRequest, $copyDocHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_2_0  "github.com/alibabacloud-go/dingtalk/doc_2_0"
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
func CreateClient () (_result *dingtalkdoc_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_2_0.Client{}
  _result, _err = dingtalkdoc_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  copyDocHeaders := &dingtalkdoc_2_0.CopyDocHeaders{}
  copyDocHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  param := &dingtalkdoc_2_0.CopyDocRequestParam{
    SourceDentryUuid: tea.String("dentryUuid"),
    TargetParentDentryUuid: tea.String("dentryUuid"),
    TargetPreDentryUuid: tea.String("dentryUuid"),
  }
  copyDocRequest := &dingtalkdoc_2_0.CopyDocRequest{
    Param: param,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CopyDocWithOptions(copyDocRequest, copyDocHeaders, &util.RuntimeOptions{})
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
const dingtalkdoc_2_0 = require('@alicloud/dingtalk/doc_2_0');
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
    return new dingtalkdoc_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let copyDocHeaders = new dingtalkdoc_2_0.CopyDocHeaders({ });
    copyDocHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let param = new dingtalkdoc_2_0.CopyDocRequestParam({
      sourceDentryUuid: 'dentryUuid',
      targetParentDentryUuid: 'dentryUuid',
      targetPreDentryUuid: 'dentryUuid',
    });
    let copyDocRequest = new dingtalkdoc_2_0.CopyDocRequest({
      param: param,
    });
    try {
      await client.copyDocWithOptions(copyDocRequest, copyDocHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdoc_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.CopyDocHeaders copyDocHeaders = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.CopyDocHeaders();
            copyDocHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.CopyDocRequest.CopyDocRequestParam param = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.CopyDocRequest.CopyDocRequestParam
            {
                SourceDentryUuid = "dentryUuid",
                TargetParentDentryUuid = "dentryUuid",
                TargetPreDentryUuid = "dentryUuid",
            };
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.CopyDocRequest copyDocRequest = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.CopyDocRequest
            {
                Param = param,
            };
            try
            {
                client.CopyDocWithOptions(copyDocRequest, copyDocHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| isAsync | Boolean | 本次操作是否为异步，若为异步则需要通过 taskId 去轮询异步任务的结果。 |
| taskId | String | 任务id，异步时才有该字段。 |
| syncCopyResult | Object | 同步操作的结果，需要注意当 isAsync 为 true 时，该字段仍会返回值。 |
| dentryUuid | String | 文件唯一ID。 |
| driveSpaceId | String | 存储层空间ID。 |
| driveDentryId | String | 存储层文件ID。 |
| extension | String | 文件后缀名。 |
| name | String | 节点名称。 |
| url | String | 节点访问链接。 |
| spaceInfo | Object | 节点所在空间信息。 |
| sceneType | String | 资源所属场景。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "isAsync" : true,
  "taskId" : "true",
  "syncCopyResult" : {
    "dentryUuid" : "dentryUuid",
    "driveSpaceId" : "driveSpaceId",
    "driveDentryId" : "driveDentryId",
    "extension" : "docx",
    "name" : "name",
    "url" : "https://example.com",
    "spaceInfo" : {
      "sceneType" : "im"
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | documentNotExist | %s | 文档不存在或格式不支持 |
| 500 | permissionDenied | %s | 无复制权限 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
