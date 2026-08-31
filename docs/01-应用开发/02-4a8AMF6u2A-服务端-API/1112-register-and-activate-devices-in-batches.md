---
title: "批量注册与激活设备"
source_url: "https://open.dingtalk.com/document/development/register-and-activate-devices-in-batches"
namespace: "development"
slug: "register-and-activate-devices-in-batches"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 设备上钉 > 批量注册与激活设备"
doc_id: "T0z7aC2cQw"
updated_at: "2026-06-03 09:09:32"
---

> Source: https://open.dingtalk.com/document/development/register-and-activate-devices-in-batches
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 设备上钉 > 批量注册与激活设备
> Updated: 2026-06-03 09:09:32

# 批量注册与激活设备

调用本接口批量注册与激活设备。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/devicemng/customers/devices/registrationActivations/batch |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Manufacture.DeviceData.Write-制造业设备信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| registerAndActivateVOS | Array | 否 | 批量注册的设备信息列表，最大值100。 |
| deviceCode | String | 是 | 设备号。  **[!NOTE]**    用户自定义参数，要求企业内每一个设备的设备码必须唯一。 |
| deviceDetailUrl | String | 否 | 设备详情链接，最大长度2048字符。 |
| deviceCallbackUrl | String | 否 | 设备回调链接，最大长度2048字符。 |
| deviceName | String | 是 | 设备名称。  **[!NOTE]**    用户自定义参数。 |
| groupUuid | String | 否 | 分组标识，该参数需要在[如何开通使用设备上钉](1110-overview-of-equipment-nailing.md#section-amr-xz8-i5r)群内咨询。 |
| introduction | String | 否 | 设备的简介。 |
| roleUuid | String | 否 | 角色标识，该参数需要在[如何开通使用设备上钉](1110-overview-of-equipment-nailing.md#section-amr-xz8-i5r)群内咨询。 |
| typeUuid | String | 否 | 设备型号，该参数需要在[如何开通使用设备上钉](1110-overview-of-equipment-nailing.md#section-amr-xz8-i5r)群内咨询。 |
| userIds | Array of String | 否 | 设备管理员的userId列表，最大值50。 |
| deviceCategory | Integer | 否 | 设备分类。   - 0：设备 - 1：助手 |

### 请求示例

HTTP

```
POST /v1.0/devicemng/customers/devices/registrationActivations/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxx
Content-Type:application/json

{
  "registerAndActivateVOS" : [ {
    "deviceCode" : "device_1234",
    "deviceDetailUrl" : "https://www.example.com",
    "deviceCallbackUrl" : "https://www.example.com",
    "deviceName" : "测试设备1",
    "groupUuid" : "xxxxx",
    "introduction" : "测试设备1是.....",
    "roleUuid" : "xxxxx",
    "typeUuid" : "xxxxx",
    "userIds" : [ "xxxxx" ],
    "deviceCategory" : 0
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdevicemng_1_0.*;
import com.aliyun.dingtalkdevicemng_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdevicemng_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdevicemng_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdevicemng_1_0.Client client = Sample.createClient();
        RegisterAndActivateDeviceBatchHeaders registerAndActivateDeviceBatchHeaders = new RegisterAndActivateDeviceBatchHeaders();
        registerAndActivateDeviceBatchHeaders.xAcsDingtalkAccessToken = "<your access token>";
        RegisterAndActivateDeviceBatchRequest.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS registerAndActivateVOS0 = new RegisterAndActivateDeviceBatchRequest.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS()
                .setDeviceCode("device_1234")
                .setDeviceDetailUrl("https://www.example.com")
                .setDeviceCallbackUrl("https://www.example.com")
                .setDeviceName("测试设备1")
                .setGroupUuid("xxxxx")
                .setIntroduction("测试设备1是.....")
                .setRoleUuid("xxxxx")
                .setTypeUuid("xxxxx")
                .setUserIds(java.util.Arrays.asList(
                    "xxxxx"
                ))
                .setDeviceCategory(0);
        RegisterAndActivateDeviceBatchRequest registerAndActivateDeviceBatchRequest = new RegisterAndActivateDeviceBatchRequest()
                .setRegisterAndActivateVOS(java.util.Arrays.asList(
                    registerAndActivateVOS0
                ));
        try {
            client.registerAndActivateDeviceBatchWithOptions(registerAndActivateDeviceBatchRequest, registerAndActivateDeviceBatchHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.devicemng_1_0.client import Client as dingtalkdevicemng_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.devicemng_1_0 import models as dingtalkdevicemng__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdevicemng_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdevicemng_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_and_activate_device_batch_headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchHeaders()
        register_and_activate_device_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_and_activate_vos0 = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS(
            device_code='device_1234',
            device_detail_url='https://www.example.com',
            device_callback_url='https://www.example.com',
            device_name='测试设备1',
            group_uuid='xxxxx',
            introduction='测试设备1是.....',
            role_uuid='xxxxx',
            type_uuid='xxxxx',
            user_ids=[
                'xxxxx'
            ],
            device_category=0
        )
        register_and_activate_device_batch_request = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequest(
            register_and_activate_vos=[
                register_and_activate_vos0
            ]
        )
        try:
            client.register_and_activate_device_batch_with_options(register_and_activate_device_batch_request, register_and_activate_device_batch_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_and_activate_device_batch_headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchHeaders()
        register_and_activate_device_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_and_activate_vos0 = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS(
            device_code='device_1234',
            device_detail_url='https://www.example.com',
            device_callback_url='https://www.example.com',
            device_name='测试设备1',
            group_uuid='xxxxx',
            introduction='测试设备1是.....',
            role_uuid='xxxxx',
            type_uuid='xxxxx',
            user_ids=[
                'xxxxx'
            ],
            device_category=0
        )
        register_and_activate_device_batch_request = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceBatchRequest(
            register_and_activate_vos=[
                register_and_activate_vos0
            ]
        )
        try:
            await client.register_and_activate_device_batch_with_options_async(register_and_activate_device_batch_request, register_and_activate_device_batch_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterAndActivateDeviceBatchHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterAndActivateDeviceBatchRequest\registerAndActivateVOS;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterAndActivateDeviceBatchRequest;
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
        $registerAndActivateDeviceBatchHeaders = new RegisterAndActivateDeviceBatchHeaders([]);
        $registerAndActivateDeviceBatchHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $registerAndActivateVOS0 = new registerAndActivateVOS([
            "deviceCode" => "device_1234",
            "deviceDetailUrl" => "https://www.example.com",
            "deviceCallbackUrl" => "https://www.example.com",
            "deviceName" => "测试设备1",
            "groupUuid" => "xxxxx",
            "introduction" => "测试设备1是.....",
            "roleUuid" => "xxxxx",
            "typeUuid" => "xxxxx",
            "userIds" => [
                "xxxxx"
            ],
            "deviceCategory" => 0
        ]);
        $registerAndActivateDeviceBatchRequest = new RegisterAndActivateDeviceBatchRequest([
            "registerAndActivateVOS" => [
                $registerAndActivateVOS0
            ]
        ]);
        try {
            $client->registerAndActivateDeviceBatchWithOptions($registerAndActivateDeviceBatchRequest, $registerAndActivateDeviceBatchHeaders, new RuntimeOptions([]));
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
  dingtalkdevicemng_1_0  "github.com/alibabacloud-go/dingtalk/devicemng_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdevicemng_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdevicemng_1_0.Client{}
  _result, _err = dingtalkdevicemng_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  registerAndActivateDeviceBatchHeaders := &dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchHeaders{}
  registerAndActivateDeviceBatchHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  registerAndActivateVOS0 := &dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS{
    DeviceCode: tea.String("device_1234"),
    DeviceDetailUrl: tea.String("https://www.example.com"),
    DeviceCallbackUrl: tea.String("https://www.example.com"),
    DeviceName: tea.String("测试设备1"),
    GroupUuid: tea.String("xxxxx"),
    Introduction: tea.String("测试设备1是....."),
    RoleUuid: tea.String("xxxxx"),
    TypeUuid: tea.String("xxxxx"),
    UserIds: []*string{tea.String("xxxxx")},
    DeviceCategory: tea.Int32(0),
  }
  registerAndActivateDeviceBatchRequest := &dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchRequest{
    RegisterAndActivateVOS: []*dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS{registerAndActivateVOS0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RegisterAndActivateDeviceBatchWithOptions(registerAndActivateDeviceBatchRequest, registerAndActivateDeviceBatchHeaders, &util.RuntimeOptions{})
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
import dingtalkdevicemng_1_0, * as $dingtalkdevicemng_1_0 from '@alicloud/dingtalk/devicemng_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdevicemng_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdevicemng_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let registerAndActivateDeviceBatchHeaders = new $dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchHeaders({ });
    registerAndActivateDeviceBatchHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let registerAndActivateVOS0 = new $dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS({
      deviceCode: "device_1234",
      deviceDetailUrl: "https://www.example.com",
      deviceCallbackUrl: "https://www.example.com",
      deviceName: "测试设备1",
      groupUuid: "xxxxx",
      introduction: "测试设备1是.....",
      roleUuid: "xxxxx",
      typeUuid: "xxxxx",
      userIds: [
        "xxxxx"
      ],
      deviceCategory: 0,
    });
    let registerAndActivateDeviceBatchRequest = new $dingtalkdevicemng_1_0.RegisterAndActivateDeviceBatchRequest({
      registerAndActivateVOS: [
        registerAndActivateVOS0
      ],
    });
    try {
      await client.registerAndActivateDeviceBatchWithOptions(registerAndActivateDeviceBatchRequest, registerAndActivateDeviceBatchHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchHeaders registerAndActivateDeviceBatchHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchHeaders();
            registerAndActivateDeviceBatchHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchRequest.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS registerAndActivateVOS0 = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchRequest.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS
            {
                DeviceCode = "device_1234",
                DeviceDetailUrl = "https://www.example.com",
                DeviceCallbackUrl = "https://www.example.com",
                DeviceName = "测试设备1",
                GroupUuid = "xxxxx",
                Introduction = "测试设备1是.....",
                RoleUuid = "xxxxx",
                TypeUuid = "xxxxx",
                UserIds = new List<string>
                {
                    "xxxxx"
                },
                DeviceCategory = 0,
            };
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchRequest registerAndActivateDeviceBatchRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchRequest
            {
                RegisterAndActivateVOS = new List<AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceBatchRequest.RegisterAndActivateDeviceBatchRequestRegisterAndActivateVOS>
                {
                    registerAndActivateVOS0
                },
            };
            try
            {
                client.RegisterAndActivateDeviceBatchWithOptions(registerAndActivateDeviceBatchRequest, registerAndActivateDeviceBatchHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| successItems | Array | 注册成功的设备列表。 |
| errorCode | String | 错误码。  **[!NOTE]**    注册成功，不返回该字段。 |
| errorMsg | String | 错误信息。  **[!NOTE]**    注册成功，不返回该字段。 |
| result | Object | 设备信息。 |
| deviceCallbackUrl | String | 设备回调链接。 |
| deviceCode | String | 设备号。 |
| deviceDetailUrl | String | 设备详情链接。 |
| deviceName | String | 设备名称。 |
| groupUuid | String | 设备分组标识。 |
| icon | String | 设备图标。 |
| introduction | String | 设备简介。 |
| roleUuid | String | 角色标识。 |
| userIds | Array of String | 设备管理员的userId。 |
| status | Long | 设备状态。   - **1**：新建 - **2**：激活 - **3**：注册   **[!NOTE]**    设备注册失败，不返回该字段。 |
| typeUuid | String | 设备型号。 |
| uuid | String | 钉钉侧的设备标识。 |
| deviceCategory | Integer | 设备分类。   - 0：设备 - 1：助手 |
| success | Boolean | 设备注册是否成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |
| failItems | Array | 注册失败的设备列表。 |
| errorCode | String | 错误码。 |
| errorMsg | String | 错误信息。 |
| result | Object | 设备信息。 |
| deviceCallbackUrl | String | 设备回调地址。 |
| deviceCode | String | 设备号。 |
| deviceDetailUrl | String | 设备详情链接。 |
| deviceName | String | 设备名称。 |
| groupUuid | String | 设备分组标识。 |
| icon | String | 设备图标。 |
| introduction | String | 设备的简介。 |
| roleUuid | String | 角色标识。 |
| userIds | Array of String | 设备管理员的userId。 |
| status | Long | 状态标识。   - **1**：新建 - **2**：激活 - **3**：注册   **[!NOTE]**    设备注册失败，不返回该字段。 |
| typeUuid | String | 设备型号。 |
| uuid | String | 钉钉侧设备标识。 |
| deviceCategory | Integer | 设备分类。   - 0：设备 - 1：助手 |
| success | Boolean | 设备注册是否成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "successItems" : [ {
    "errorCode" : "30001",
    "errorMsg" : "设备编号已存在",
    "result" : {
      "deviceCallbackUrl" : "http://www.example.com",
      "deviceCode" : "device_1234",
      "deviceDetailUrl" : "http://www.example.com",
      "deviceName" : "测试设备",
      "groupUuid" : "xxxxxx",
      "icon" : "xxxx",
      "introduction" : "测试设备是",
      "roleUuid" : "xxxxx",
      "userIds" : [ "xxxxx" ],
      "status" : 1,
      "typeUuid" : "xxxx",
      "uuid" : "xxxxx",
      "deviceCategory" : 0
    },
    "success" : true
  } ],
  "success" : true,
  "failItems" : [ {
    "errorCode" : "100000",
    "errorMsg" : "系统异常",
    "result" : {
      "deviceCallbackUrl" : "http://www.example.com",
      "deviceCode" : "device_1234",
      "deviceDetailUrl" : "http://www.example.com",
      "deviceName" : "测试设备1",
      "groupUuid" : "xxxxx",
      "icon" : "xxxxx",
      "introduction" : "测试设备1是。。。。",
      "roleUuid" : "xxxxxx",
      "userIds" : [ "xxxxxx" ],
      "status" : 1,
      "typeUuid" : "xxxxx",
      "uuid" : "xxxxx",
      "deviceCategory" : 1
    },
    "success" : false
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | deviceNumLimit | 300002，设备数量达到上限 | 设备数量达到上限 |
| 400 | devicekeyAlreadyExist | 300001，设备key已经存在 | 设备key已经存在 |
| 500 | systemError | 100000，系统异常 | 系统异常 |
