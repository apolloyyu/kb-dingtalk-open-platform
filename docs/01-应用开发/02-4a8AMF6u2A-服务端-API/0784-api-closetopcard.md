---
title: "关闭吊顶卡片"
source_url: "https://open.dingtalk.com/document/development/api-closetopcard"
namespace: "development"
slug: "api-closetopcard"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > 关闭吊顶卡片"
doc_id: "dHqFcriJKF"
updated_at: "2026-07-14 09:22:15"
---

> Source: https://open.dingtalk.com/document/development/api-closetopcard
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > 关闭吊顶卡片
> Updated: 2026-07-14 09:22:15

# 关闭吊顶卡片

调用本接口可关闭通过卡片投放接口投放的吊顶卡片。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/tops/close |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Instance.Write-互动卡片实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 外部卡片实例Id，与[创建卡片](0780-interface-for-creating-a-card-instance.md)/[创建并投放卡片](0783-create-and-deliver-cards.md)中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取：  image      由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。 |
| openConversationId | String | 是 | 会话 id：   - **群聊**（此参数必传）：    - 基于群模板创建的群，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。   - 安装群聊酷应用的群，通过[感知群变化（事件订阅）](../01-XOnnmGCTbn-开发指南/0060-group-chat-coolapp-event.md)获取回调参数`OpenConversationId`参数值。 - **单聊助手**：不传入此参数。 |

### 请求示例

HTTP

```
POST /v1.0/card/tops/close?outTrackId=example_out_track_id&openConversationId=example_open_conversation_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token-xxx
Content-Type:application/json
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
        com.aliyun.dingtalkcard_1_0.models.CloseTopCardHeaders closeTopCardHeaders = new com.aliyun.dingtalkcard_1_0.models.CloseTopCardHeaders();
        closeTopCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.CloseTopCardRequest closeTopCardRequest = new com.aliyun.dingtalkcard_1_0.models.CloseTopCardRequest()
                .setOutTrackId("example_out_track_id")
                .setOpenConversationId("example_open_conversation_id");
        try {
            client.closeTopCardWithOptions(closeTopCardRequest, closeTopCardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        close_top_card_headers = dingtalkcard__1__0_models.CloseTopCardHeaders()
        close_top_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        close_top_card_request = dingtalkcard__1__0_models.CloseTopCardRequest(
            out_track_id='example_out_track_id',
            open_conversation_id='example_open_conversation_id'
        )
        try:
            client.close_top_card_with_options(close_top_card_request, close_top_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        close_top_card_headers = dingtalkcard__1__0_models.CloseTopCardHeaders()
        close_top_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        close_top_card_request = dingtalkcard__1__0_models.CloseTopCardRequest(
            out_track_id='example_out_track_id',
            open_conversation_id='example_open_conversation_id'
        )
        try:
            await client.close_top_card_with_options_async(close_top_card_request, close_top_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CloseTopCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CloseTopCardRequest;
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
        $closeTopCardHeaders = new CloseTopCardHeaders([]);
        $closeTopCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $closeTopCardRequest = new CloseTopCardRequest([
            "outTrackId" => "example_out_track_id",
            "openConversationId" => "example_open_conversation_id"
        ]);
        try {
            $client->closeTopCardWithOptions($closeTopCardRequest, $closeTopCardHeaders, new RuntimeOptions([]));
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

  closeTopCardHeaders := &dingtalkcard_1_0.CloseTopCardHeaders{}
  closeTopCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  closeTopCardRequest := &dingtalkcard_1_0.CloseTopCardRequest{
    OutTrackId: tea.String("example_out_track_id"),
    OpenConversationId: tea.String("example_open_conversation_id"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CloseTopCardWithOptions(closeTopCardRequest, closeTopCardHeaders, &util.RuntimeOptions{})
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
    let closeTopCardHeaders = new dingtalkcard_1_0.CloseTopCardHeaders({ });
    closeTopCardHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let closeTopCardRequest = new dingtalkcard_1_0.CloseTopCardRequest({
      outTrackId: 'example_out_track_id',
      openConversationId: 'example_open_conversation_id',
    });
    try {
      await client.closeTopCardWithOptions(closeTopCardRequest, closeTopCardHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CloseTopCardHeaders closeTopCardHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CloseTopCardHeaders();
            closeTopCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CloseTopCardRequest closeTopCardRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CloseTopCardRequest
            {
                OutTrackId = "example_out_track_id",
                OpenConversationId = "example_open_conversation_id",
            };
            try
            {
                client.CloseTopCardWithOptions(closeTopCardRequest, closeTopCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口是否调用成功。 |
| result | Boolean | 是否成功关闭吊顶。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | param.empty | 参数为空 |
| 400 | param.conversationIdInvalid | param.openConversationIdInvalid | openConversationId不符合规范 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识outTrackId为空 |
| 400 | param.cardNotExist | param.cardNotExist | 卡片不存在 |
| 500 | system.busy | system.busy | 系统繁忙 |
