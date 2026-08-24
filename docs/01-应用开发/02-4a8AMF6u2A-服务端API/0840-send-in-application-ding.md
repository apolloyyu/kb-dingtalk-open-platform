---
title: "DING服务"
source_url: "https://open.dingtalk.com/document/development/send-in-application-ding"
namespace: "development"
slug: "send-in-application-ding"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > DING > DING服务"
doc_id: "rQ0CAeBIdF"
updated_at: "2026-06-04 19:09:57"
---

> Source: https://open.dingtalk.com/document/development/send-in-application-ding
> Path: 应用开发 / 服务端API / 专属钉钉 > DING > DING服务
> Updated: 2026-06-04 19:09:57

# DING服务

调用本接口通过专属DING服务中设置的互动服务窗来发送应用内DING。

## 接口调用说明

- 该文档将不再维护，如需使用请使用[发送DING消息](0712-robot-sends-nail-message.md)新接口。
- 专属钉钉API接口仅针对专属钉钉客户开放，专属钉钉简介和本文档中API使用问题咨询请[查看专属钉钉说明](https://oa.dingtalk.com/register_new.htm?spm=ding_open_doc.document.0.0.20851fcacmWWQT&source=50061&useMt2=1#/)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/appDings/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.Ding.Send-专属钉钉发DING权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userids | Array of String | 是 | 接收DING消息的用户userid列表。 |
| content | String | 是 | 消息内容。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/appDings/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "userids" : [ "123" ],
  "content" : "开会"
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.SendAppDingHeaders sendAppDingHeaders = new com.aliyun.dingtalkexclusive_1_0.models.SendAppDingHeaders();
        sendAppDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.SendAppDingRequest sendAppDingRequest = new com.aliyun.dingtalkexclusive_1_0.models.SendAppDingRequest()
                .setUserids(java.util.Arrays.asList(
                    "123"
                ))
                .setContent("开会");
        try {
            client.sendAppDingWithOptions(sendAppDingRequest, sendAppDingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_app_ding_headers = dingtalkexclusive__1__0_models.SendAppDingHeaders()
        send_app_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_app_ding_request = dingtalkexclusive__1__0_models.SendAppDingRequest(
            userids=[
                '123'
            ],
            content='开会'
        )
        try:
            client.send_app_ding_with_options(send_app_ding_request, send_app_ding_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_app_ding_headers = dingtalkexclusive__1__0_models.SendAppDingHeaders()
        send_app_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_app_ding_request = dingtalkexclusive__1__0_models.SendAppDingRequest(
            userids=[
                '123'
            ],
            content='开会'
        )
        try:
            await client.send_app_ding_with_options_async(send_app_ding_request, send_app_ding_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendAppDingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendAppDingRequest;
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
        $sendAppDingHeaders = new SendAppDingHeaders([]);
        $sendAppDingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendAppDingRequest = new SendAppDingRequest([
            "userids" => [
                "123"
            ],
            "content" => "开会"
        ]);
        try {
            $client->sendAppDingWithOptions($sendAppDingRequest, $sendAppDingHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
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
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendAppDingHeaders := &dingtalkexclusive_1_0.SendAppDingHeaders{}
  sendAppDingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendAppDingRequest := &dingtalkexclusive_1_0.SendAppDingRequest{
    Userids: []*string{tea.String("123")},
    Content: tea.String("开会"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendAppDingWithOptions(sendAppDingRequest, sendAppDingHeaders, &util.RuntimeOptions{})
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
const dingtalkexclusive_1_0 = require('@alicloud/dingtalk/exclusive_1_0');
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
    return new dingtalkexclusive_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let sendAppDingHeaders = new dingtalkexclusive_1_0.SendAppDingHeaders({ });
    sendAppDingHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let sendAppDingRequest = new dingtalkexclusive_1_0.SendAppDingRequest({
      userids: [
        '123'
      ],
      content: '开会',
    });
    try {
      await client.sendAppDingWithOptions(sendAppDingRequest, sendAppDingHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendAppDingHeaders sendAppDingHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendAppDingHeaders();
            sendAppDingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendAppDingRequest sendAppDingRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendAppDingRequest
            {
                Userids = new List<string>
                {
                    "123"
                },
                Content = "开会",
            };
            try
            {
                client.SendAppDingWithOptions(sendAppDingRequest, sendAppDingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | assign.lack | 管理员未签署协议 | 管理员未签署协议 |
| 400 | volume.lack | 额度不足 | 额度不足 |
| 400 | message.duplicate | 重复内容，发送失败 | 重复内容，发送失败 |
| 400 | param.illegal | 参数不合法 | 参数不合法 |
| 400 | publisher.notexist | 服务号不存在 | 服务号不存在 |
| 500 | system.error | 系统内部错误 | 系统内部错误 |
