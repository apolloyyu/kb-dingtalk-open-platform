---
title: "发送电话DING"
source_url: "https://open.dingtalk.com/document/development/outgoing-phone-ding"
namespace: "development"
slug: "outgoing-phone-ding"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > DING > 发送电话DING"
doc_id: "yipD1SpZtj"
updated_at: "2026-08-25 09:37:22"
---

> Source: https://open.dingtalk.com/document/development/outgoing-phone-ding
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > DING > 发送电话DING
> Updated: 2026-08-25 09:37:22

# 发送电话DING

调用本接口，可以通过互动服务窗的服务号发送电话DING。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[发送DING消息](0712-robot-sends-nail-message.md)接口，已接入用户不受影响。

### 接口调用流程

调用本接口发送电话DING消息，需要完成以下配置，步骤如下：

步骤一：登录[钉钉管理后台](https://oa.dingtalk.com)。

步骤二：在**钉钉管理后台**页面，依次单击**专属钉钉 > 专属开放 > DING服务 > 电话DING容量**，完成如下图所示配置。
![](https://img.alicdn.com/imgextra/i4/O1CN01JOFadM1RcVBjPhkOU_!!6000000002132-2-tps-2526-1260.png)

> **[!NOTE]**
>
> DING电话推送号，需要先在当前组织内的**互动服务窗**应用中添加，如下图所示。添加完成后，再去**钉钉管理后台**的**电话DING容量**页面配置。
> ![](https://img.alicdn.com/imgextra/i2/O1CN01g5dsIh1hc4fdLy2KI_!!6000000004297-2-tps-2624-1120.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  不支持新增 | — |
| 第三方企业应用 | 暂不支持 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/exclusive/phoneDings/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userids" : [ "String" ],
  "content" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userids | Array of String | 是 | 接收DING消息的用户userId列表，最大值20。 |
| content | String | 是 | 消息内容。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 发送Ding消息是否成功。   - **true**：成功 - **false**：失败 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/exclusive/phoneDings/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "userids" : [ "user123" ],
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
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.SendPhoneDingHeaders sendPhoneDingHeaders = new com.aliyun.dingtalkexclusive_1_0.models.SendPhoneDingHeaders();
        sendPhoneDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.SendPhoneDingRequest sendPhoneDingRequest = new com.aliyun.dingtalkexclusive_1_0.models.SendPhoneDingRequest()
                .setUserids(java.util.Arrays.asList(
                    "user123"
                ))
                .setContent("开会");
        try {
            client.sendPhoneDingWithOptions(sendPhoneDingRequest, sendPhoneDingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        send_phone_ding_headers = dingtalkexclusive__1__0_models.SendPhoneDingHeaders()
        send_phone_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_phone_ding_request = dingtalkexclusive__1__0_models.SendPhoneDingRequest(
            userids=[
                'user123'
            ],
            content='开会'
        )
        try:
            client.send_phone_ding_with_options(send_phone_ding_request, send_phone_ding_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_phone_ding_headers = dingtalkexclusive__1__0_models.SendPhoneDingHeaders()
        send_phone_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_phone_ding_request = dingtalkexclusive__1__0_models.SendPhoneDingRequest(
            userids=[
                'user123'
            ],
            content='开会'
        )
        try:
            await client.send_phone_ding_with_options_async(send_phone_ding_request, send_phone_ding_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendPhoneDingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendPhoneDingRequest;
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
        $sendPhoneDingHeaders = new SendPhoneDingHeaders([]);
        $sendPhoneDingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendPhoneDingRequest = new SendPhoneDingRequest([
            "userids" => [
                "user123"
            ],
            "content" => "开会"
        ]);
        try {
            $client->sendPhoneDingWithOptions($sendPhoneDingRequest, $sendPhoneDingHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  sendPhoneDingHeaders := &dingtalkexclusive_1_0.SendPhoneDingHeaders{}
  sendPhoneDingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendPhoneDingRequest := &dingtalkexclusive_1_0.SendPhoneDingRequest{
    Userids: []*string{tea.String("user123")},
    Content: tea.String("开会"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendPhoneDingWithOptions(sendPhoneDingRequest, sendPhoneDingHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let sendPhoneDingHeaders = new $dingtalkexclusive_1_0.SendPhoneDingHeaders({ });
    sendPhoneDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sendPhoneDingRequest = new $dingtalkexclusive_1_0.SendPhoneDingRequest({
      userids: [
        "user123"
      ],
      content: "开会",
    });
    try {
      await client.sendPhoneDingWithOptions(sendPhoneDingRequest, sendPhoneDingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendPhoneDingHeaders sendPhoneDingHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendPhoneDingHeaders();
            sendPhoneDingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendPhoneDingRequest sendPhoneDingRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendPhoneDingRequest
            {
                Userids = new List<string>
                {
                    "user123"
                },
                Content = "开会",
            };
            try
            {
                client.SendPhoneDingWithOptions(sendPhoneDingRequest, sendPhoneDingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | assign.lack | 管理员未签署协议 | 管理员未签署协议 |
| 400 | message.duplicate | 重复内容，发送失败 | 重复内容，发送失败 |
| 400 | param.illegal | 参数不合法 | 参数不合法 |
| 400 | publisher.notexist | 服务号不存在 | 服务号不存在 |
| 400 | volume.lack | 电话DING额度不足 | 电话DING额度不足 |
| 400 | batch.toolarge | 每批接受人数超20 | 每批接受人数超20 |
| 400 | phoneding.reachlimit | 电话DING发送已达上限 | 电话DING发送已达上限 |
| 400 | send.toofast | 发送频繁，请稍后再试 | 发送频繁，请稍后再试 |
