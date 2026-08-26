---
title: "设备入会"
source_url: "https://open.dingtalk.com/document/development/equipment-membership"
namespace: "development"
slug: "equipment-membership"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉物联 > 设备入会"
doc_id: "GS9AfJYFOa"
updated_at: "2025-09-08 19:06:10"
---

> Source: https://open.dingtalk.com/document/development/equipment-membership
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉物联 > 设备入会
> Updated: 2025-09-08 19:06:10

# 设备入会

本接口用于将设备等加入会议。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，钉钉物联接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 钉钉物联接口相关文档，已于2023年01月02日迁移至历史文档（不推荐）目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

![](https://img.alicdn.com/imgextra/i4/O1CN014ewGCH1HML2cskyf3_!!6000000000743-2-tps-1028-658.png)

> **[!NOTE]**
>
> 本接口支持以下场景：
>
> - 创建新的会议，将设备和设备负责人加入会议。
> - 加入已存在会议，只支持将设备加入会议，不支持将设备负责人加入会议。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 暂不支持 | — | — |

## 请求方法

```
POST /v1.0/diot/deviceConferences/initiate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "confTitle" : "String",
  "conferenceId" : "String",
  "conferencePassword" : "String",
  "deviceIds" : [ "String" ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| confTitle | String | 是 | 会议主题，最多不能超20个中文。 |
| conferenceId | String | 否 | 钉钉会议ID。   - 创建新的会议，不填写该字段。 - 加入已存在的会议，必填。 |
| conferencePassword | String | 否 | 钉钉会议密码。   - 创建新的会议，不填写该字段。 - 加入已存在的会议，必填。 |
| deviceIds | Array of String | 是 | 邀请的设备ID，最多5个。   - 企业内部应用，调用[注册设备](https://open.dingtalk.com/document/orgapp/register-devices)或者[批量注册设备](https://open.dingtalk.com/document/orgapp/batchregister-devices)接口获取。 - 第三方企业应用，调用[注册设备](https://open.dingtalk.com/document/isvapp/register-devices)或者[批量注册设备](https://open.dingtalk.com/document/isvapp/batchregister-devices)接口获取。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| conferenceId | String | 会议ID。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/diot/deviceConferences/initiate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:98b4f2xxx
Content-Type:application/json

{
  "confTitle" : "设备的应急会议",
  "conferenceId" : "12345678",
  "conferencePassword" : "123456",
  "deviceIds" : [ "001" ]
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
    public static com.aliyun.dingtalkdiot_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdiot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdiot_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdiot_1_0.models.DeviceConferenceHeaders deviceConferenceHeaders = new com.aliyun.dingtalkdiot_1_0.models.DeviceConferenceHeaders();
        deviceConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdiot_1_0.models.DeviceConferenceRequest deviceConferenceRequest = new com.aliyun.dingtalkdiot_1_0.models.DeviceConferenceRequest()
                .setConfTitle("设备的应急会议")
                .setConferenceId("12345678")
                .setConferencePassword("123456")
                .setDeviceIds(java.util.Arrays.asList(
                    "001"
                ));
        try {
            client.deviceConferenceWithOptions(deviceConferenceRequest, deviceConferenceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.diot_1_0.client import Client as dingtalkdiot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.diot_1_0 import models as dingtalkdiot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdiot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdiot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        device_conference_headers = dingtalkdiot__1__0_models.DeviceConferenceHeaders()
        device_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        device_conference_request = dingtalkdiot__1__0_models.DeviceConferenceRequest(
            conf_title='设备的应急会议',
            conference_id='12345678',
            conference_password='123456',
            device_ids=[
                '001'
            ]
        )
        try:
            client.device_conference_with_options(device_conference_request, device_conference_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        device_conference_headers = dingtalkdiot__1__0_models.DeviceConferenceHeaders()
        device_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        device_conference_request = dingtalkdiot__1__0_models.DeviceConferenceRequest(
            conf_title='设备的应急会议',
            conference_id='12345678',
            conference_password='123456',
            device_ids=[
                '001'
            ]
        )
        try:
            await client.device_conference_with_options_async(device_conference_request, device_conference_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\DeviceConferenceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\DeviceConferenceRequest;
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
        $deviceConferenceHeaders = new DeviceConferenceHeaders([]);
        $deviceConferenceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deviceConferenceRequest = new DeviceConferenceRequest([
            "confTitle" => "设备的应急会议",
            "conferenceId" => "12345678",
            "conferencePassword" => "123456",
            "deviceIds" => [
                "001"
            ]
        ]);
        try {
            $client->deviceConferenceWithOptions($deviceConferenceRequest, $deviceConferenceHeaders, new RuntimeOptions([]));
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
  dingtalkdiot_1_0  "github.com/alibabacloud-go/dingtalk/diot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdiot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdiot_1_0.Client{}
  _result, _err = dingtalkdiot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deviceConferenceHeaders := &dingtalkdiot_1_0.DeviceConferenceHeaders{}
  deviceConferenceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deviceConferenceRequest := &dingtalkdiot_1_0.DeviceConferenceRequest{
    ConfTitle: tea.String("设备的应急会议"),
    ConferenceId: tea.String("12345678"),
    ConferencePassword: tea.String("123456"),
    DeviceIds: []*string{tea.String("001")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeviceConferenceWithOptions(deviceConferenceRequest, deviceConferenceHeaders, &util.RuntimeOptions{})
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
import dingtalkdiot_1_0, * as $dingtalkdiot_1_0 from '@alicloud/dingtalk/diot_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdiot_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdiot_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let deviceConferenceHeaders = new $dingtalkdiot_1_0.DeviceConferenceHeaders({ });
    deviceConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deviceConferenceRequest = new $dingtalkdiot_1_0.DeviceConferenceRequest({
      confTitle: "设备的应急会议",
      conferenceId: "12345678",
      conferencePassword: "123456",
      deviceIds: [
        "001"
      ],
    });
    try {
      await client.deviceConferenceWithOptions(deviceConferenceRequest, deviceConferenceHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdiot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdiot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.DeviceConferenceHeaders deviceConferenceHeaders = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.DeviceConferenceHeaders();
            deviceConferenceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.DeviceConferenceRequest deviceConferenceRequest = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.DeviceConferenceRequest
            {
                ConfTitle = "设备的应急会议",
                ConferenceId = "12345678",
                ConferencePassword = "123456",
                DeviceIds = new List<string>
                {
                    "001"
                },
            };
            try
            {
                client.DeviceConferenceWithOptions(deviceConferenceRequest, deviceConferenceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "conferenceId" : "123456789"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 401 | system.not.exist | 系统未注册 | 系统未在钉钉物联平台注册 |
| 401 | corp.not.bind | 组织未绑定 | 钉钉组织未绑定该系统 |
| 500 | system.error | 系统异常 | 系统异常 |
| 500 | crop.not.install | 企业未安装钉钉物联应用，请联系我们(https://open.dingtalk.com/document/orgapp-server/dingtalk-iot-overview) | 企业未安装钉钉物联应用 |
