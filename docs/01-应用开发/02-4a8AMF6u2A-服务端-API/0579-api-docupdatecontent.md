---
title: "覆写文档（个人授权）"
source_url: "https://open.dingtalk.com/document/development/api-docupdatecontent"
namespace: "development"
slug: "api-docupdatecontent"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 文档 > 覆写文档（个人授权）"
doc_id: "SSu4t5hgp9"
updated_at: "2026-06-15 10:20:44"
---

> Source: https://open.dingtalk.com/document/development/api-docupdatecontent
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 文档 > 覆写文档（个人授权）
> Updated: 2026-06-15 10:20:44

# 覆写文档（个人授权）

调用本接口，通过Markdown的形式覆写文档。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/doc/me/suites/documents/{docKey}/overwriteContent |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Document.Document.Write-文档应用中文档写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过 [获取用户token](0032-obtain-user-token.md) 接口获取 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| docKey | String | 是 | 文档id（doc\_key or dentryUuid）。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dataType | String | 否 | 覆盖内容的数据类型。 |
| content | String | 是 | 内容正文。 |

### **请求示例**

HTTP

```
POST /v2.0/doc/me/suites/documents/Z90D4da/overwriteContent HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "dataType" : "markdown",
  "content" : "# Heading"
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
        com.aliyun.dingtalkdoc_2_0.models.DocUpdateContentWithDelegatedPermissionHeaders docUpdateContentWithDelegatedPermissionHeaders = new com.aliyun.dingtalkdoc_2_0.models.DocUpdateContentWithDelegatedPermissionHeaders();
        docUpdateContentWithDelegatedPermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_2_0.models.DocUpdateContentWithDelegatedPermissionRequest docUpdateContentWithDelegatedPermissionRequest = new com.aliyun.dingtalkdoc_2_0.models.DocUpdateContentWithDelegatedPermissionRequest()
                .setDataType("markdown")
                .setContent("# Heading");
        try {
            client.docUpdateContentWithDelegatedPermissionWithOptions("Z90D4da", docUpdateContentWithDelegatedPermissionRequest, docUpdateContentWithDelegatedPermissionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        doc_update_content_with_delegated_permission_headers = dingtalkdoc__2__0_models.DocUpdateContentWithDelegatedPermissionHeaders()
        doc_update_content_with_delegated_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_update_content_with_delegated_permission_request = dingtalkdoc__2__0_models.DocUpdateContentWithDelegatedPermissionRequest(
            data_type='markdown',
            content='# Heading'
        )
        try:
            client.doc_update_content_with_delegated_permission_with_options('Z90D4da', doc_update_content_with_delegated_permission_request, doc_update_content_with_delegated_permission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        doc_update_content_with_delegated_permission_headers = dingtalkdoc__2__0_models.DocUpdateContentWithDelegatedPermissionHeaders()
        doc_update_content_with_delegated_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_update_content_with_delegated_permission_request = dingtalkdoc__2__0_models.DocUpdateContentWithDelegatedPermissionRequest(
            data_type='markdown',
            content='# Heading'
        )
        try:
            await client.doc_update_content_with_delegated_permission_with_options_async('Z90D4da', doc_update_content_with_delegated_permission_request, doc_update_content_with_delegated_permission_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\DocUpdateContentWithDelegatedPermissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\DocUpdateContentWithDelegatedPermissionRequest;
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
        $docUpdateContentWithDelegatedPermissionHeaders = new DocUpdateContentWithDelegatedPermissionHeaders([]);
        $docUpdateContentWithDelegatedPermissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $docUpdateContentWithDelegatedPermissionRequest = new DocUpdateContentWithDelegatedPermissionRequest([
            "dataType" => "markdown",
            "content" => "# Heading"
        ]);
        try {
            $client->docUpdateContentWithDelegatedPermissionWithOptions("Z90D4da", $docUpdateContentWithDelegatedPermissionRequest, $docUpdateContentWithDelegatedPermissionHeaders, new RuntimeOptions([]));
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

  docUpdateContentWithDelegatedPermissionHeaders := &dingtalkdoc_2_0.DocUpdateContentWithDelegatedPermissionHeaders{}
  docUpdateContentWithDelegatedPermissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  docUpdateContentWithDelegatedPermissionRequest := &dingtalkdoc_2_0.DocUpdateContentWithDelegatedPermissionRequest{
    DataType: tea.String("markdown"),
    Content: tea.String("# Heading"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DocUpdateContentWithDelegatedPermissionWithOptions(tea.String("Z90D4da"), docUpdateContentWithDelegatedPermissionRequest, docUpdateContentWithDelegatedPermissionHeaders, &util.RuntimeOptions{})
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
    let docUpdateContentWithDelegatedPermissionHeaders = new dingtalkdoc_2_0.DocUpdateContentWithDelegatedPermissionHeaders({ });
    docUpdateContentWithDelegatedPermissionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let docUpdateContentWithDelegatedPermissionRequest = new dingtalkdoc_2_0.DocUpdateContentWithDelegatedPermissionRequest({
      dataType: 'markdown',
      content: '# Heading',
    });
    try {
      await client.docUpdateContentWithDelegatedPermissionWithOptions('Z90D4da', docUpdateContentWithDelegatedPermissionRequest, docUpdateContentWithDelegatedPermissionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.DocUpdateContentWithDelegatedPermissionHeaders docUpdateContentWithDelegatedPermissionHeaders = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.DocUpdateContentWithDelegatedPermissionHeaders();
            docUpdateContentWithDelegatedPermissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.DocUpdateContentWithDelegatedPermissionRequest docUpdateContentWithDelegatedPermissionRequest = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.DocUpdateContentWithDelegatedPermissionRequest
            {
                DataType = "markdown",
                Content = "# Heading",
            };
            try
            {
                client.DocUpdateContentWithDelegatedPermissionWithOptions("Z90D4da", docUpdateContentWithDelegatedPermissionRequest, docUpdateContentWithDelegatedPermissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| data | Map<String, Any> | 返回结果。 |
|  | Any | 返回结果。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : {
    "key" : "success:true"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 403 | permissionDenied | %s | 无权限 |
| 404 | documentNotExist | %s | 文档不存在 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
