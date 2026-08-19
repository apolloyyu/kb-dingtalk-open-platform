---
title: "钉工牌通知消息"
source_url: "https://open.dingtalk.com/document/development/dingtalk-badge-notification-message"
namespace: "development"
slug: "dingtalk-badge-notification-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 钉工牌通知消息"
doc_id: "oNh5Q8FhiJ"
updated_at: "2025-09-11 21:03:36"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-badge-notification-message
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 钉工牌通知消息
> Updated: 2025-09-11 21:03:36

# 钉工牌通知消息

调用本接口，在企业钉工牌页面，发送企业针对员工的通知消息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/badge/notices |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Badge.Common.Write-钉工牌基础数据写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户userId。 |
| msgId | String | 是 | 消息传入，调用方传入，唯一标识消息。 |
| msgType | String | 是 | 消息类型，取值：   - **DING\_BADGE\_NOTIFY**：钉工牌通知场景 |
| content | String | 是 | 通知内容。  钉工牌场景必传字段：   - **title**：标题 - **subTitle**：备注 - **imageUrl**：图片地址 - **url**：跳转地址   示例：   ``` {     "title":"标题",     "subTitle":"备注",     "imageUrl":"ds7868av787Url",     "url":"ds7868av787Url" } ``` |

### 请求示例

HTTP

```
POST /v1.0/badge/notify/create HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fc6ac830f3f232c3a7fb8bfc783815e1
Content-Type:application/json

{
  "staffId" : "234554543",
  "msgId" : "234",
  "msgType" : "MSG_TYPE",
  "content" : "{   \"title\":\"title\",   \"subTitle\":\"subTitle\",   \"imageUrl\":\"imageUrl\",   \"url\":\"url\" }"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkbadge_1_0.*;
import com.aliyun.dingtalkbadge_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkbadge_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkbadge_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkbadge_1_0.Client client = Sample.createClient();
        CreateBadgeNotifyHeaders createBadgeNotifyHeaders = new CreateBadgeNotifyHeaders();
        createBadgeNotifyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateBadgeNotifyRequest createBadgeNotifyRequest = new CreateBadgeNotifyRequest()
                .setStaffId("234554543")
                .setMsgId("234")
                .setMsgType("MSG_TYPE")
                .setContent("{   \"title\":\"title\",   \"subTitle\":\"subTitle\",   \"imageUrl\":\"imageUrl\",   \"url\":\"url\" }");
        try {
            client.createBadgeNotifyWithOptions(createBadgeNotifyRequest, createBadgeNotifyHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.badge_1_0.client import Client as dingtalkbadge_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.badge_1_0 import models as dingtalkbadge__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkbadge_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkbadge_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_badge_notify_headers = dingtalkbadge__1__0_models.CreateBadgeNotifyHeaders()
        create_badge_notify_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_badge_notify_request = dingtalkbadge__1__0_models.CreateBadgeNotifyRequest(
            staff_id='234554543',
            msg_id='234',
            msg_type='MSG_TYPE',
            content='{   "title":"title",   "subTitle":"subTitle",   "imageUrl":"imageUrl",   "url":"url" }'
        )
        try:
            client.create_badge_notify_with_options(create_badge_notify_request, create_badge_notify_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_badge_notify_headers = dingtalkbadge__1__0_models.CreateBadgeNotifyHeaders()
        create_badge_notify_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_badge_notify_request = dingtalkbadge__1__0_models.CreateBadgeNotifyRequest(
            staff_id='234554543',
            msg_id='234',
            msg_type='MSG_TYPE',
            content='{   "title":"title",   "subTitle":"subTitle",   "imageUrl":"imageUrl",   "url":"url" }'
        )
        try:
            await client.create_badge_notify_with_options_async(create_badge_notify_request, create_badge_notify_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\CreateBadgeNotifyHeaders;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\CreateBadgeNotifyRequest;
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
        $createBadgeNotifyHeaders = new CreateBadgeNotifyHeaders([]);
        $createBadgeNotifyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createBadgeNotifyRequest = new CreateBadgeNotifyRequest([
            "staffId" => "234554543",
            "msgId" => "234",
            "msgType" => "MSG_TYPE",
            "content" => "{   \"title\":\"title\",   \"subTitle\":\"subTitle\",   \"imageUrl\":\"imageUrl\",   \"url\":\"url\" }"
        ]);
        try {
            $client->createBadgeNotifyWithOptions($createBadgeNotifyRequest, $createBadgeNotifyHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkbadge_1_0  "github.com/alibabacloud-go/dingtalk/badge_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkbadge_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkbadge_1_0.Client{}
  _result, _err = dingtalkbadge_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createBadgeNotifyHeaders := &dingtalkbadge_1_0.CreateBadgeNotifyHeaders{}
  createBadgeNotifyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createBadgeNotifyRequest := &dingtalkbadge_1_0.CreateBadgeNotifyRequest{
    StaffId: tea.String("234554543"),
    MsgId: tea.String("234"),
    MsgType: tea.String("MSG_TYPE"),
    Content: tea.String("{   \"title\":\"title\",   \"subTitle\":\"subTitle\",   \"imageUrl\":\"imageUrl\",   \"url\":\"url\" }"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateBadgeNotifyWithOptions(createBadgeNotifyRequest, createBadgeNotifyHeaders, &util.RuntimeOptions{})
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
import dingtalkbadge_1_0, * as $dingtalkbadge_1_0 from '@alicloud/dingtalk/badge_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkbadge_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkbadge_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createBadgeNotifyHeaders = new $dingtalkbadge_1_0.CreateBadgeNotifyHeaders({ });
    createBadgeNotifyHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createBadgeNotifyRequest = new $dingtalkbadge_1_0.CreateBadgeNotifyRequest({
      staffId: "234554543",
      msgId: "234",
      msgType: "MSG_TYPE",
      content: "{   \"title\":\"title\",   \"subTitle\":\"subTitle\",   \"imageUrl\":\"imageUrl\",   \"url\":\"url\" }",
    });
    try {
      await client.createBadgeNotifyWithOptions(createBadgeNotifyRequest, createBadgeNotifyHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkbadge_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkbadge_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeNotifyHeaders createBadgeNotifyHeaders = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeNotifyHeaders();
            createBadgeNotifyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeNotifyRequest createBadgeNotifyRequest = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeNotifyRequest
            {
                StaffId = "234554543",
                MsgId = "234",
                MsgType = "MSG_TYPE",
                Content = "{   \"title\":\"title\",   \"subTitle\":\"subTitle\",   \"imageUrl\":\"imageUrl\",   \"url\":\"url\" }",
            };
            try
            {
                client.CreateBadgeNotifyWithOptions(createBadgeNotifyRequest, createBadgeNotifyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkbadge__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkbadge_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkbadge_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::Client> client = make_shared<Alibabacloud_Dingtalkbadge_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeNotifyHeaders> createBadgeNotifyHeaders = make_shared<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeNotifyHeaders>();
  createBadgeNotifyHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeNotifyRequest> createBadgeNotifyRequest = make_shared<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeNotifyRequest>(map<string, boost::any>({
    {"staffId", boost::any(string("234554543"))},
    {"msgId", boost::any(string("234"))},
    {"msgType", boost::any(string("MSG_TYPE"))},
    {"content", boost::any(string("{   "title":"title",   "subTitle":"subTitle",   "imageUrl":"imageUrl",   "url":"url" }"))}
  }));
  try {
    client->createBadgeNotifyWithOptions(createBadgeNotifyRequest, createBadgeNotifyHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Boolean | 发送通知是否成功。true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | missingParameter | 缺少必须参数 | 缺少必须参数 |
| 400 | noAuthority | 无权限调用 | 无权限调用 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | userNotifyExist | 通知消息已经存在 | 通知消息已经存在 |
| 400 | invalidMsgType | 无效的消息类型 | 无效的消息类型 |
