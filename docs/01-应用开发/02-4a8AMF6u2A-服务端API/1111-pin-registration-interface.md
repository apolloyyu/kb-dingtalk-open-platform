---
title: "注册设备到钉钉"
source_url: "https://open.dingtalk.com/document/development/pin-registration-interface"
namespace: "development"
slug: "pin-registration-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 设备上钉 > 注册设备到钉钉"
doc_id: "mhxV1eITvd"
updated_at: "2025-09-23 19:22:24"
---

> Source: https://open.dingtalk.com/document/development/pin-registration-interface
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 设备上钉 > 注册设备到钉钉
> Updated: 2025-09-23 19:22:24

# 注册设备到钉钉

调用本接口可以将设备注册到钉钉上，用于后期的设备管理及业务处理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/devicemng/customers/devices/registerAndActivate |
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
| deviceCode | String | 是 | 设备号。  **[!NOTE]**    用户自定义参数，要求企业内每一个设备的设备码必须唯一。 |
| deviceName | String | 是 | 设备名称。  **[!NOTE]**    用户自定义参数。 |
| introduction | String | 否 | 设备的简介。 |
| typeUuid | String | 否 | 设备型号。 |
| userIds | Array of String | 否 | 设备管理员的userId列表。 |
| roleUuid | String | 否 | 角色标识。 |
| deviceDetailUrl | String | 否 | 设备详情链接，最大长度2048字符。 |
| deviceCallbackUrl | String | 否 | 设备回调链接，最大长度2048字符。 |
| deviceCategory | Integer | 否 | 设备分类。   - 0：设备 - 1：助手 |

### 请求示例

HTTP

```
POST /v1.0/devicemng/customers/devices/registerAndActivate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxx
Content-Type:application/json

{
  "deviceCode" : "ceshi_001",
  "deviceName" : "设备名称",
  "introduction" : "简介",
  "typeUuid" : "xxxxxxx",
  "userIds" : [ "xxxxxx" ],
  "roleUuid" : "xxxxx",
  "deviceDetailUrl" : "http://www.example.com",
  "deviceCallbackUrl" : "http://www.example.com",
  "deviceCategory" : 0
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
        RegisterAndActivateDeviceHeaders registerAndActivateDeviceHeaders = new RegisterAndActivateDeviceHeaders();
        registerAndActivateDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        RegisterAndActivateDeviceRequest registerAndActivateDeviceRequest = new RegisterAndActivateDeviceRequest()
                .setDeviceCode("ceshi_001")
                .setDeviceName("设备名称")
                .setIntroduction("简介")
                .setTypeUuid("xxxxxxx")
                .setUserIds(java.util.Arrays.asList(
                    "xxxxxx"
                ))
                .setRoleUuid("xxxxx")
                .setDeviceDetailUrl("http://www.example.com")
                .setDeviceCallbackUrl("http://www.example.com")
                .setDeviceCategory(0);
        try {
            client.registerAndActivateDeviceWithOptions(registerAndActivateDeviceRequest, registerAndActivateDeviceHeaders, new RuntimeOptions());
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
        register_and_activate_device_headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceHeaders()
        register_and_activate_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_and_activate_device_request = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceRequest(
            device_code='ceshi_001',
            device_name='设备名称',
            introduction='简介',
            type_uuid='xxxxxxx',
            user_ids=[
                'xxxxxx'
            ],
            role_uuid='xxxxx',
            device_detail_url='http://www.example.com',
            device_callback_url='http://www.example.com',
            device_category=0
        )
        try:
            client.register_and_activate_device_with_options(register_and_activate_device_request, register_and_activate_device_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_and_activate_device_headers = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceHeaders()
        register_and_activate_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_and_activate_device_request = dingtalkdevicemng__1__0_models.RegisterAndActivateDeviceRequest(
            device_code='ceshi_001',
            device_name='设备名称',
            introduction='简介',
            type_uuid='xxxxxxx',
            user_ids=[
                'xxxxxx'
            ],
            role_uuid='xxxxx',
            device_detail_url='http://www.example.com',
            device_callback_url='http://www.example.com',
            device_category=0
        )
        try:
            await client.register_and_activate_device_with_options_async(register_and_activate_device_request, register_and_activate_device_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterAndActivateDeviceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterAndActivateDeviceRequest;
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
        $registerAndActivateDeviceHeaders = new RegisterAndActivateDeviceHeaders([]);
        $registerAndActivateDeviceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $registerAndActivateDeviceRequest = new RegisterAndActivateDeviceRequest([
            "deviceCode" => "ceshi_001",
            "deviceName" => "设备名称",
            "introduction" => "简介",
            "typeUuid" => "xxxxxxx",
            "userIds" => [
                "xxxxxx"
            ],
            "roleUuid" => "xxxxx",
            "deviceDetailUrl" => "http://www.example.com",
            "deviceCallbackUrl" => "http://www.example.com",
            "deviceCategory" => 0
        ]);
        try {
            $client->registerAndActivateDeviceWithOptions($registerAndActivateDeviceRequest, $registerAndActivateDeviceHeaders, new RuntimeOptions([]));
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

  registerAndActivateDeviceHeaders := &dingtalkdevicemng_1_0.RegisterAndActivateDeviceHeaders{}
  registerAndActivateDeviceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  registerAndActivateDeviceRequest := &dingtalkdevicemng_1_0.RegisterAndActivateDeviceRequest{
    DeviceCode: tea.String("ceshi_001"),
    DeviceName: tea.String("设备名称"),
    Introduction: tea.String("简介"),
    TypeUuid: tea.String("xxxxxxx"),
    UserIds: []*string{tea.String("xxxxxx")},
    RoleUuid: tea.String("xxxxx"),
    DeviceDetailUrl: tea.String("http://www.example.com"),
    DeviceCallbackUrl: tea.String("http://www.example.com"),
    DeviceCategory: tea.Int32(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RegisterAndActivateDeviceWithOptions(registerAndActivateDeviceRequest, registerAndActivateDeviceHeaders, &util.RuntimeOptions{})
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
    let registerAndActivateDeviceHeaders = new $dingtalkdevicemng_1_0.RegisterAndActivateDeviceHeaders({ });
    registerAndActivateDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let registerAndActivateDeviceRequest = new $dingtalkdevicemng_1_0.RegisterAndActivateDeviceRequest({
      deviceCode: "ceshi_001",
      deviceName: "设备名称",
      introduction: "简介",
      typeUuid: "xxxxxxx",
      userIds: [
        "xxxxxx"
      ],
      roleUuid: "xxxxx",
      deviceDetailUrl: "http://www.example.com",
      deviceCallbackUrl: "http://www.example.com",
      deviceCategory: 0,
    });
    try {
      await client.registerAndActivateDeviceWithOptions(registerAndActivateDeviceRequest, registerAndActivateDeviceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceHeaders registerAndActivateDeviceHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceHeaders();
            registerAndActivateDeviceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceRequest registerAndActivateDeviceRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterAndActivateDeviceRequest
            {
                DeviceCode = "ceshi_001",
                DeviceName = "设备名称",
                Introduction = "简介",
                TypeUuid = "xxxxxxx",
                UserIds = new List<string>
                {
                    "xxxxxx"
                },
                RoleUuid = "xxxxx",
                DeviceDetailUrl = "http://www.example.com",
                DeviceCallbackUrl = "http://www.example.com",
                DeviceCategory = 0,
            };
            try
            {
                client.RegisterAndActivateDeviceWithOptions(registerAndActivateDeviceRequest, registerAndActivateDeviceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |
| result | Object | 响应结果。 |
| deviceCode | String | 设备号。 |
| deviceUuid | String | 钉钉侧设备标识。 |
| deviceName | String | 设备名称。 |
| introduction | String | 设备的简介。 |
| typeUuid | String | 设备型号。 |
| roleUuid | String | 角色标识。 |
| deviceDetailUrl | String | 设备详情链接。 |
| userIds | Array of String | 设备管理员的userId列表，最大值50。 |
| deviceCategory | Integer | 设备分类。   - 0：设备 - 1：助手 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "deviceCode" : "xxxxx",
    "deviceUuid" : "xxxxxx",
    "deviceName" : "测试设备1",
    "introduction" : "简介",
    "typeUuid" : "xxxxxx",
    "roleUuid" : "xxxxxx",
    "deviceDetailUrl" : "http://www.example.com",
    "userIds" : [ "xxxxx" ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | devicekeyAlreadyExist | 30001，设备key已存在 | 设备key已存在 |
| 400 | devicenameAlreadyExist | 30002，设备名称已存在 | 设备名称已存在 |
| 400 | deviceNumLimit | 30008，设备数量达到上限 | 设备数量达到上限 |
| 400 | userNotExisted | %s | 用户信息不存在 |
| 500 | systemError | 100000，系统异常 | 系统异常 |
