---
title: "创建用户专属短链"
source_url: "https://open.dingtalk.com/document/development/api-createcustomshortlink"
namespace: "development"
slug: "api-createcustomshortlink"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 创建用户专属短链"
doc_id: "pgSXkO3PWz"
updated_at: "2026-06-02 09:17:58"
---

> Source: https://open.dingtalk.com/document/development/api-createcustomshortlink
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 创建用户专属短链
> Updated: 2026-06-02 09:17:58

# 创建用户专属短链

根据用户信息，创建用户专属短链。用户通过专属短链入会后，可通过客户端jsapi查询该用户的扩展应用业务自定义信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/customShortLinks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| creatorUnionId | String | 是 | 预约会议创建人 unionId。 |
| scheduleConferenceId | String | 是 | 预约会议 id，可通过[创建预约会议](0416-create-appointment-meeting.md)接口获取返回参数`scheduleConferenceId`字段。 |
| coolAppCode | String | 是 | 酷应用 Code。可通过开发者后台，微应用中查看酷应用Code。 |
| extensionAppBizData | String | 否 | 用户维度扩展应用自定义信息。 |
| useExtensionApp | Boolean | 否 | 是否使用扩展应用：   - true：是 - false：否 |

### 请求示例

HTTP

```
POST /v1.0/conference/customShortLinks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1ce64c62b52f370c9421422d1bb87dc1
Content-Type:application/json

{
  "creatorUnionId" : "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
  "scheduleConferenceId" : "f6fb627e-a7e8-403e-b1f8-26e85450f4a9",
  "coolAppCode" : "COOLAPP-0-1026633886192127xxxB000W",
  "extensionAppBizData" : "bizData",
  "useExtensionApp" : true
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
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconference_1_0.models.CreateCustomShortLinkHeaders createCustomShortLinkHeaders = new com.aliyun.dingtalkconference_1_0.models.CreateCustomShortLinkHeaders();
        createCustomShortLinkHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.CreateCustomShortLinkRequest createCustomShortLinkRequest = new com.aliyun.dingtalkconference_1_0.models.CreateCustomShortLinkRequest()
                .setCreatorUnionId("2iPOLbpUNMLzB5LuwggiiqiPwiEiE")
                .setScheduleConferenceId("f6fb627e-a7e8-403e-b1f8-26e85450f4a9")
                .setCoolAppCode("COOLAPP-0-1026633886192127xxxB000W")
                .setExtensionAppBizData("bizData")
                .setUseExtensionApp(true);
        try {
            client.createCustomShortLinkWithOptions(createCustomShortLinkRequest, createCustomShortLinkHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.conference_1_0.client import Client as dingtalkconference_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.conference_1_0 import models as dingtalkconference__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconference_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconference_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_custom_short_link_headers = dingtalkconference__1__0_models.CreateCustomShortLinkHeaders()
        create_custom_short_link_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_custom_short_link_request = dingtalkconference__1__0_models.CreateCustomShortLinkRequest(
            creator_union_id='2iPOLbpUNMLzB5LuwggiiqiPwiEiE',
            schedule_conference_id='f6fb627e-a7e8-403e-b1f8-26e85450f4a9',
            cool_app_code='COOLAPP-0-1026633886192127xxxB000W',
            extension_app_biz_data='bizData',
            use_extension_app=True
        )
        try:
            client.create_custom_short_link_with_options(create_custom_short_link_request, create_custom_short_link_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_custom_short_link_headers = dingtalkconference__1__0_models.CreateCustomShortLinkHeaders()
        create_custom_short_link_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_custom_short_link_request = dingtalkconference__1__0_models.CreateCustomShortLinkRequest(
            creator_union_id='2iPOLbpUNMLzB5LuwggiiqiPwiEiE',
            schedule_conference_id='f6fb627e-a7e8-403e-b1f8-26e85450f4a9',
            cool_app_code='COOLAPP-0-1026633886192127xxxB000W',
            extension_app_biz_data='bizData',
            use_extension_app=True
        )
        try:
            await client.create_custom_short_link_with_options_async(create_custom_short_link_request, create_custom_short_link_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateCustomShortLinkHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateCustomShortLinkRequest;
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
        $createCustomShortLinkHeaders = new CreateCustomShortLinkHeaders([]);
        $createCustomShortLinkHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createCustomShortLinkRequest = new CreateCustomShortLinkRequest([
            "creatorUnionId" => "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
            "scheduleConferenceId" => "f6fb627e-a7e8-403e-b1f8-26e85450f4a9",
            "coolAppCode" => "COOLAPP-0-1026633886192127xxxB000W",
            "extensionAppBizData" => "bizData",
            "useExtensionApp" => true
        ]);
        try {
            $client->createCustomShortLinkWithOptions($createCustomShortLinkRequest, $createCustomShortLinkHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
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
func CreateClient () (_result *dingtalkconference_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconference_1_0.Client{}
  _result, _err = dingtalkconference_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createCustomShortLinkHeaders := &dingtalkconference_1_0.CreateCustomShortLinkHeaders{}
  createCustomShortLinkHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createCustomShortLinkRequest := &dingtalkconference_1_0.CreateCustomShortLinkRequest{
    CreatorUnionId: tea.String("2iPOLbpUNMLzB5LuwggiiqiPwiEiE"),
    ScheduleConferenceId: tea.String("f6fb627e-a7e8-403e-b1f8-26e85450f4a9"),
    CoolAppCode: tea.String("COOLAPP-0-1026633886192127xxxB000W"),
    ExtensionAppBizData: tea.String("bizData"),
    UseExtensionApp: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateCustomShortLinkWithOptions(createCustomShortLinkRequest, createCustomShortLinkHeaders, &util.RuntimeOptions{})
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
const dingtalkconference_1_0 = require('@alicloud/dingtalk/conference_1_0');
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
    return new dingtalkconference_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createCustomShortLinkHeaders = new dingtalkconference_1_0.CreateCustomShortLinkHeaders({ });
    createCustomShortLinkHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createCustomShortLinkRequest = new dingtalkconference_1_0.CreateCustomShortLinkRequest({
      creatorUnionId: '2iPOLbpUNMLzB5LuwggiiqiPwiEiE',
      scheduleConferenceId: 'f6fb627e-a7e8-403e-b1f8-26e85450f4a9',
      coolAppCode: 'COOLAPP-0-1026633886192127xxxB000W',
      extensionAppBizData: 'bizData',
      useExtensionApp: true,
    });
    try {
      await client.createCustomShortLinkWithOptions(createCustomShortLinkRequest, createCustomShortLinkHeaders, new Util.RuntimeOptions({ }));
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkconference_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconference_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconference_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateCustomShortLinkHeaders createCustomShortLinkHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateCustomShortLinkHeaders();
            createCustomShortLinkHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateCustomShortLinkRequest createCustomShortLinkRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateCustomShortLinkRequest
            {
                CreatorUnionId = "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
                ScheduleConferenceId = "f6fb627e-a7e8-403e-b1f8-26e85450f4a9",
                CoolAppCode = "COOLAPP-0-1026633886192127xxxB000W",
                ExtensionAppBizData = "bizData",
                UseExtensionApp = true,
            };
            try
            {
                client.CreateCustomShortLinkWithOptions(createCustomShortLinkRequest, createCustomShortLinkHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 响应结果。 |
| customShortLink | String | 专属短链。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "customShortLink" : "https://meeting.dingtalk.com/j/xBzQxxxY1IB"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | paramError | 参数错误，请检查入参 |
| 400 | creatorUidError | creatorUidError | 创建人错误 |
| 400 | scheduleConferenceIdError | scheduleConferenceIdError | 预约会议id错误 |
| 400 | userNotInOrg | userNotInOrg | 用户不在组织内 |
| 403 | noPermission | noPermission | 无操作权限 |
| 500 | systemError | systemError | 系统错误 |
