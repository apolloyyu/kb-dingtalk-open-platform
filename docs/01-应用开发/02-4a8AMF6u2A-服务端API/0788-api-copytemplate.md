---
title: "卡片平台模板复制"
source_url: "https://open.dingtalk.com/document/development/api-copytemplate"
namespace: "development"
slug: "api-copytemplate"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 互动卡片 > 卡片平台模板复制"
doc_id: "913BwWz1vf"
updated_at: "2026-07-14 09:22:15"
---

> Source: https://open.dingtalk.com/document/development/api-copytemplate
> Path: 应用开发 / 服务端API / 即时通信 > 互动卡片 > 卡片平台模板复制
> Updated: 2026-07-14 09:22:15

# 卡片平台模板复制

调用本接口，根据模板ID复制模板。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/templates/copy |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Card.Template.ReadWrite.All-卡片模板应用读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，第三方企业应用通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| templateId | String | 是 | 模板id，可通过登录开发者后台 > [卡片平台](https://open-dev.dingtalk.com/fe/card?spm=ding_open_doc.document.0.0.5afe282cILuI9a&hash=%23%2F#/)获取。  image |

### 请求示例

HTTP

```
POST /v1.0/card/templates/copy HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d2ba9b08b9603a12b3ad421dd709fef9
Content-Type:application/json

{
  "templateId" : "27988007-955f-4bdd-8838-58fcdb2e3d9d.schema"
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
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.CopyTemplateHeaders copyTemplateHeaders = new com.aliyun.dingtalkcard_1_0.models.CopyTemplateHeaders();
        copyTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.CopyTemplateRequest copyTemplateRequest = new com.aliyun.dingtalkcard_1_0.models.CopyTemplateRequest()
                .setTemplateId("27988007-955f-4bdd-8838-58fcdb2e3d9d.schema");
        try {
            client.copyTemplateWithOptions(copyTemplateRequest, copyTemplateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        copy_template_headers = dingtalkcard__1__0_models.CopyTemplateHeaders()
        copy_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        copy_template_request = dingtalkcard__1__0_models.CopyTemplateRequest(
            template_id='27988007-955f-4bdd-8838-58fcdb2e3d9d.schema'
        )
        try:
            client.copy_template_with_options(copy_template_request, copy_template_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        copy_template_headers = dingtalkcard__1__0_models.CopyTemplateHeaders()
        copy_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        copy_template_request = dingtalkcard__1__0_models.CopyTemplateRequest(
            template_id='27988007-955f-4bdd-8838-58fcdb2e3d9d.schema'
        )
        try:
            await client.copy_template_with_options_async(copy_template_request, copy_template_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CopyTemplateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CopyTemplateRequest;
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
        $copyTemplateHeaders = new CopyTemplateHeaders([]);
        $copyTemplateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $copyTemplateRequest = new CopyTemplateRequest([
            "templateId" => "27988007-955f-4bdd-8838-58fcdb2e3d9d.schema"
        ]);
        try {
            $client->copyTemplateWithOptions($copyTemplateRequest, $copyTemplateHeaders, new RuntimeOptions([]));
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
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
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
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  copyTemplateHeaders := &dingtalkcard_1_0.CopyTemplateHeaders{}
  copyTemplateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  copyTemplateRequest := &dingtalkcard_1_0.CopyTemplateRequest{
    TemplateId: tea.String("27988007-955f-4bdd-8838-58fcdb2e3d9d.schema"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CopyTemplateWithOptions(copyTemplateRequest, copyTemplateHeaders, &util.RuntimeOptions{})
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
const dingtalkcard_1_0 = require('@alicloud/dingtalk/card_1_0');
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
    return new dingtalkcard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let copyTemplateHeaders = new dingtalkcard_1_0.CopyTemplateHeaders({ });
    copyTemplateHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let copyTemplateRequest = new dingtalkcard_1_0.CopyTemplateRequest({
      templateId: '27988007-955f-4bdd-8838-58fcdb2e3d9d.schema',
    });
    try {
      await client.copyTemplateWithOptions(copyTemplateRequest, copyTemplateHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CopyTemplateHeaders copyTemplateHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CopyTemplateHeaders();
            copyTemplateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CopyTemplateRequest copyTemplateRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CopyTemplateRequest
            {
                TemplateId = "27988007-955f-4bdd-8838-58fcdb2e3d9d.schema",
            };
            try
            {
                client.CopyTemplateWithOptions(copyTemplateRequest, copyTemplateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 成功标识。 |
| data | Object | 响应参数。 |
| templateId | String | 模板id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "data" : {
    "templateId" : "279xxxxhema"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | copy.template.error | Template copy error: %s | 复制模板失败 |
| 400 | template.not.exist | Target template don't exist | 模板不存在 |
