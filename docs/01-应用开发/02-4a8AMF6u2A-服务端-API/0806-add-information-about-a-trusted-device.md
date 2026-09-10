---
title: "新增可信设备信息"
source_url: "https://open.dingtalk.com/document/development/add-information-about-a-trusted-device"
namespace: "development"
slug: "add-information-about-a-trusted-device"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 可信设备 > 新增可信设备信息"
doc_id: "aCpQpr13IR"
updated_at: "2026-06-02 19:10:59"
---

> Source: https://open.dingtalk.com/document/development/add-information-about-a-trusted-device
> Path: 应用开发 / 服务端 API / 专属钉钉 > 可信设备 > 新增可信设备信息
> Updated: 2026-06-02 19:10:59

# 新增可信设备信息

调用本接口新增一个可信设备。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/trustedDevices |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.TrustedDevice.ReadWrite-专属钉钉可信设备信息读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 员工userid，为0时表示这个设备为公共设备。 |
| platform | String | 是 | 平台类型，目前仅支持Mac和Win两种类型。 |
| macAddress | String | 否 | 可信设备mac地址。 |
| did | String | 否 | 设备唯一标识。 |
| status | Integer | 否 | 设备状态，取值：   - **1**：待审批 - **2**：可信 - **3**：挂失 - **4**：拒绝 |
| title | String | 否 | 设备标题。 |
| serialNumber | String | 否 | 设备序列号。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/trustedDevices HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2f52ee3a01c034068c935bce9c5ce510
Content-Type:application/json

{
  "userId" : "6522xxxx9784",
  "platform" : "Mac",
  "macAddress" : "88:xx:xx:xx:xx:xx",
  "did" : "1234567",
  "status" : 2,
  "title" : "张三的设备",
  "serialNumber" : "123"
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
        com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceHeaders createTrustedDeviceHeaders = new com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceHeaders();
        createTrustedDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceRequest createTrustedDeviceRequest = new com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceRequest()
                .setUserId("6522xxxx9784")
                .setPlatform("Mac")
                .setMacAddress("88:xx:xx:xx:xx:xx")
                .setDid("1234567")
                .setStatus(2)
                .setTitle("张三的设备")
                .setSerialNumber("123");
        try {
            client.createTrustedDeviceWithOptions(createTrustedDeviceRequest, createTrustedDeviceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_trusted_device_headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceHeaders()
        create_trusted_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_trusted_device_request = dingtalkexclusive__1__0_models.CreateTrustedDeviceRequest(
            user_id='6522xxxx9784',
            platform='Mac',
            mac_address='88:xx:xx:xx:xx:xx',
            did='1234567',
            status=2,
            title='张三的设备',
            serial_number='123'
        )
        try:
            client.create_trusted_device_with_options(create_trusted_device_request, create_trusted_device_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_trusted_device_headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceHeaders()
        create_trusted_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_trusted_device_request = dingtalkexclusive__1__0_models.CreateTrustedDeviceRequest(
            user_id='6522xxxx9784',
            platform='Mac',
            mac_address='88:xx:xx:xx:xx:xx',
            did='1234567',
            status=2,
            title='张三的设备',
            serial_number='123'
        )
        try:
            await client.create_trusted_device_with_options_async(create_trusted_device_request, create_trusted_device_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CreateTrustedDeviceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CreateTrustedDeviceRequest;
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
        $createTrustedDeviceHeaders = new CreateTrustedDeviceHeaders([]);
        $createTrustedDeviceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createTrustedDeviceRequest = new CreateTrustedDeviceRequest([
            "userId" => "6522xxxx9784",
            "platform" => "Mac",
            "macAddress" => "88:xx:xx:xx:xx:xx",
            "did" => "1234567",
            "status" => 2,
            "title" => "张三的设备",
            "serialNumber" => "123"
        ]);
        try {
            $client->createTrustedDeviceWithOptions($createTrustedDeviceRequest, $createTrustedDeviceHeaders, new RuntimeOptions([]));
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

  createTrustedDeviceHeaders := &dingtalkexclusive_1_0.CreateTrustedDeviceHeaders{}
  createTrustedDeviceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createTrustedDeviceRequest := &dingtalkexclusive_1_0.CreateTrustedDeviceRequest{
    UserId: tea.String("6522xxxx9784"),
    Platform: tea.String("Mac"),
    MacAddress: tea.String("88:xx:xx:xx:xx:xx"),
    Did: tea.String("1234567"),
    Status: tea.Int32(2),
    Title: tea.String("张三的设备"),
    SerialNumber: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTrustedDeviceWithOptions(createTrustedDeviceRequest, createTrustedDeviceHeaders, &util.RuntimeOptions{})
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
    let createTrustedDeviceHeaders = new dingtalkexclusive_1_0.CreateTrustedDeviceHeaders({ });
    createTrustedDeviceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createTrustedDeviceRequest = new dingtalkexclusive_1_0.CreateTrustedDeviceRequest({
      userId: '6522xxxx9784',
      platform: 'Mac',
      macAddress: '88:xx:xx:xx:xx:xx',
      did: '1234567',
      status: 2,
      title: '张三的设备',
      serialNumber: '123',
    });
    try {
      await client.createTrustedDeviceWithOptions(createTrustedDeviceRequest, createTrustedDeviceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceHeaders createTrustedDeviceHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceHeaders();
            createTrustedDeviceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceRequest createTrustedDeviceRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceRequest
            {
                UserId = "6522xxxx9784",
                Platform = "Mac",
                MacAddress = "88:xx:xx:xx:xx:xx",
                Did = "1234567",
                Status = 2,
                Title = "张三的设备",
                SerialNumber = "123",
            };
            try
            {
                client.CreateTrustedDeviceWithOptions(createTrustedDeviceRequest, createTrustedDeviceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 查询结果。  **[!NOTE]**    添加是否成功由http状态码表示，状态码**200**表示添加成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | insert.repeat.error | 重复插入 | 重复插入 |
| 400 | param.format.error | 参数格式错误 | 参数格式错误 |
| 400 | param.missing | 参数不合法 | 参数不合法 |
| 400 | employee.not.found | userId错误 | userId错误 |
| 500 | service.error | 系统内部调用错误 | 系统内部调用错误 |
