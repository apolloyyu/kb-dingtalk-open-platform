---
title: "查询公共设备"
source_url: "https://open.dingtalk.com/document/development/query-public-equipment"
namespace: "development"
slug: "query-public-equipment"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 可信设备 > 查询公共设备"
doc_id: "PFrPfVam5O"
updated_at: "2026-08-12 09:21:14"
---

> Source: https://open.dingtalk.com/document/development/query-public-equipment
> Path: 应用开发 / 服务端 API / 专属钉钉 > 可信设备 > 查询公共设备
> Updated: 2026-08-12 09:21:14

# 查询公共设备

调用本接口查询查询公共设备。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/trusts/publicDevices |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.TrustedDevice.ReadWrite-专属钉钉可信设备信息读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| platform | String | 否 | 系统：   - **Mac**：Mac端 - **Win**：Windows端 - **iOS**：iOS 端 - **Android**: Android端 |
| startTime | Long | 否 | 注册或申请的开始时间，单位毫秒。 |
| endTime | Long | 否 | 注册或申请截止时间，单位毫秒。 |
| pageSize | Integer | 否 | 单页返回的数据条数。  **[!NOTE]**  - 最小值10。 - 最大值200。 |
| pageNumber | Integer | 否 | 页码。 |
| title | String | 否 | 设备标题。 |
| macAddress | String | 否 | 设备mac地址。 |
| serialNumber | String | 否 | 设备序列号。 |
| deviceUuid | String | 否 | 设备uuid。 |
| serialNumberList | Array of String | 否 | 设备序列号。 |
| encryptDeviceIdList | Array of String | 否 | 加密设备ID。 |
| didList | Array of String | 否 | 三方设备id。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/trusts/publicDevices?platform=Mac&startTime=1671767361000&endTime=1671767361000&pageSize=100&pageNumber=1&title=这是标题&macAddress=88:66:5a:07:2b:04&serialNumber=11-22-33-44&deviceUuid=123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e29ed86dfc0a3cf0b32c9f4*****16
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.GetPublicDevicesHeaders getPublicDevicesHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetPublicDevicesHeaders();
        getPublicDevicesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetPublicDevicesRequest getPublicDevicesRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetPublicDevicesRequest()
                .setPlatform("Mac")
                .setStartTime(1671767361000L)
                .setEndTime(1671767361000L)
                .setPageSize(100)
                .setPageNumber(1)
                .setTitle("这是标题")
                .setMacAddress("88:66:5a:07:2b:04")
                .setSerialNumber("11-22-33-44")
                .setDeviceUuid("123");
        try {
            client.getPublicDevicesWithOptions(getPublicDevicesRequest, getPublicDevicesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_public_devices_headers = dingtalkexclusive__1__0_models.GetPublicDevicesHeaders()
        get_public_devices_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_public_devices_request = dingtalkexclusive__1__0_models.GetPublicDevicesRequest(
            platform='Mac',
            start_time=1671767361000,
            end_time=1671767361000,
            page_size=100,
            page_number=1,
            title='这是标题',
            mac_address='88:66:5a:07:2b:04',
            serial_number='11-22-33-44',
            device_uuid='123'
        )
        try:
            client.get_public_devices_with_options(get_public_devices_request, get_public_devices_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_public_devices_headers = dingtalkexclusive__1__0_models.GetPublicDevicesHeaders()
        get_public_devices_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_public_devices_request = dingtalkexclusive__1__0_models.GetPublicDevicesRequest(
            platform='Mac',
            start_time=1671767361000,
            end_time=1671767361000,
            page_size=100,
            page_number=1,
            title='这是标题',
            mac_address='88:66:5a:07:2b:04',
            serial_number='11-22-33-44',
            device_uuid='123'
        )
        try:
            await client.get_public_devices_with_options_async(get_public_devices_request, get_public_devices_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetPublicDevicesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetPublicDevicesRequest;
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
        $getPublicDevicesHeaders = new GetPublicDevicesHeaders([]);
        $getPublicDevicesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getPublicDevicesRequest = new GetPublicDevicesRequest([
            "platform" => "Mac",
            "startTime" => 1671767361000,
            "endTime" => 1671767361000,
            "pageSize" => 100,
            "pageNumber" => 1,
            "title" => "这是标题",
            "macAddress" => "88:66:5a:07:2b:04",
            "serialNumber" => "11-22-33-44",
            "deviceUuid" => "123"
        ]);
        try {
            $client->getPublicDevicesWithOptions($getPublicDevicesRequest, $getPublicDevicesHeaders, new RuntimeOptions([]));
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

  getPublicDevicesHeaders := &dingtalkexclusive_1_0.GetPublicDevicesHeaders{}
  getPublicDevicesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getPublicDevicesRequest := &dingtalkexclusive_1_0.GetPublicDevicesRequest{
    Platform: tea.String("Mac"),
    StartTime: tea.Int64(1671767361000),
    EndTime: tea.Int64(1671767361000),
    PageSize: tea.Int32(100),
    PageNumber: tea.Int32(1),
    Title: tea.String("这是标题"),
    MacAddress: tea.String("88:66:5a:07:2b:04"),
    SerialNumber: tea.String("11-22-33-44"),
    DeviceUuid: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetPublicDevicesWithOptions(getPublicDevicesRequest, getPublicDevicesHeaders, &util.RuntimeOptions{})
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
    let getPublicDevicesHeaders = new dingtalkexclusive_1_0.GetPublicDevicesHeaders({ });
    getPublicDevicesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getPublicDevicesRequest = new dingtalkexclusive_1_0.GetPublicDevicesRequest({
      platform: 'Mac',
      startTime: 1671767361000,
      endTime: 1671767361000,
      pageSize: 100,
      pageNumber: 1,
      title: '这是标题',
      macAddress: '88:66:5a:07:2b:04',
      serialNumber: '11-22-33-44',
      deviceUuid: '123',
    });
    try {
      await client.getPublicDevicesWithOptions(getPublicDevicesRequest, getPublicDevicesHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPublicDevicesHeaders getPublicDevicesHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPublicDevicesHeaders();
            getPublicDevicesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPublicDevicesRequest getPublicDevicesRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetPublicDevicesRequest
            {
                Platform = "Mac",
                StartTime = 1671767361000,
                EndTime = 1671767361000,
                PageSize = 100,
                PageNumber = 1,
                Title = "这是标题",
                MacAddress = "88:66:5a:07:2b:04",
                SerialNumber = "11-22-33-44",
                DeviceUuid = "123",
            };
            try
            {
                client.GetPublicDevicesWithOptions(getPublicDevicesRequest, getPublicDevicesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCnt | Long | 数据总数。 |
| dataCnt | Integer | 当前页数据量。 |
| data | Array | 设备列表。 |
| gmtCreate | Long | 创建时间。 |
| gmtModified | Long | 修改时间。 |
| title | String | 设备标题。 |
| macAddress | String | Mac地址。 |
| platform | String | 系统：   - **Mac**：Mac端 - **Win**：Windows端 - **iOS**：iOS端 - **Android**：Android端 |
| deviceScopeType | Integer | 生效范围：   - **1**: 全员生效 - **2**: 部分生效 |
| deviceStaffs | Array | 员工列表。  **[!NOTE]**  仅生效范围是部分生效时有效。 |
| userId | String | 员工id。 |
| name | String | 员工姓名。 |
| deviceDepts | Array | 部门列表。  **[!NOTE]**  仅生效范围是部分生效时有效。 |
| id | Long | 部门id。 |
| name | String | 部门名称。 |
| deviceRoles | Array | 角色列表。  **[!NOTE]**  仅生效范围是部分生效时有效。 |
| tagCode | String | 角色code。 |
| name | String | 角色名称。 |
| serialNumber | String | 设备序列号。 |
| deviceUuid | String | 设备uuid。 |
| retryPermission | String | 是否允许再次申请：   - **0**: 否 - **1**: 是 |
| status | Integer | 设备状态，取值：   - **1**：待审批 - **2**：可信 - **3**：挂失 - **4**：拒绝 |
| did | String | 三方设备id。 |
| encryptDeviceId | String | 加密设备id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCnt" : 100,
  "dataCnt" : 100,
  "data" : [ {
    "gmtCreate" : 1671767361000,
    "gmtModified" : 1671767361000,
    "title" : "公共设备",
    "macAddress" : "88:66:5a:07:2b:04",
    "platform" : "Mac",
    "deviceScopeType" : 1,
    "deviceStaffs" : [ {
      "userId" : "123",
      "name" : "张三"
    } ],
    "deviceDepts" : [ {
      "id" : 123,
      "name" : "测试部门"
    } ],
    "deviceRoles" : [ {
      "tagCode" : "123",
      "name" : "测试角色"
    } ],
    "serialNumber" : "123",
    "deviceUuid" : "123",
    "retryPermission" : "1",
    "status" : 1
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | 参数不合法 | 参数不合法，请确认分页参数是否正确。 |
| 500 | service.error | 系统错误 | 系统错误 |
| 500 | org.noauth.noauth | 权限不足，请确认应用权限 | 权限不足，请确认应用权限 |
