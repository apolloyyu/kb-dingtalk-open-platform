---
title: "查询可信设备详细信息"
source_url: "https://open.dingtalk.com/document/development/query-trusted-device-details"
namespace: "development"
slug: "query-trusted-device-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 可信设备 > 查询可信设备详细信息"
doc_id: "b5ViWzhSvi"
updated_at: "2026-06-04 19:09:55"
---

> Source: https://open.dingtalk.com/document/development/query-trusted-device-details
> Path: 应用开发 / 服务端 API / 专属钉钉 > 可信设备 > 查询可信设备详细信息
> Updated: 2026-06-04 19:09:55

# 查询可信设备详细信息

调用本接口，查询组织内员工的可信设备详细信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/trustedDevices/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Custom.TrustedDevice.ReadWrite-暂不支持 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIds | Array of String | 否 | 用户userid列表。 |
| gmtCreateStart | Long | 否 | 设备创建时间起。 |
| gmtCreateEnd | Long | 否 | 设备创建时间止。 |
| gmtModifiedStart | Long | 否 | 设备修改时间起。 |
| gmtModifiedEnd | Long | 否 | 设备修改时间止。 |
| pageSize | Long | 否 | 每页数据条数。 |
| pageNumber | Long | 否 | 页码，从1开始。 |
| platform | String | 否 | 设备类型：   - iOS - Android - Win - Mac |
| macAddress | String | 否 | 设备mac地址。 |
| status | Integer | 否 | 设备状态：   - 1: 待审批 - 2: 可信 - 3: 挂失 - 4: 拒绝 |
| serialNumber | String | 否 | 设备序列号。 |
| deviceUuid | String | 否 | 设备uuid。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/trustedDevices/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "userIds" : [ "652241xxx" ],
  "gmtCreateStart" : 1724256000000,
  "gmtCreateEnd" : 1724256000000,
  "gmtModifiedStart" : 1724256000000,
  "gmtModifiedEnd" : 1724256000000,
  "pageSize" : 50,
  "pageNumber" : 1,
  "platform" : "Win",
  "macAddress" : "66:55:44:33:22:11",
  "serialNumber" : "123",
  "deviceUuid" : "123"
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
        com.aliyun.dingtalkexclusive_1_0.models.GetTrustDeviceListHeaders getTrustDeviceListHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetTrustDeviceListHeaders();
        getTrustDeviceListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetTrustDeviceListRequest getTrustDeviceListRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetTrustDeviceListRequest()
                .setUserIds(java.util.Arrays.asList(
                    "652241xxx"
                ))
                .setGmtCreateStart(1724256000000L)
                .setGmtCreateEnd(1724256000000L)
                .setGmtModifiedStart(1724256000000L)
                .setGmtModifiedEnd(1724256000000L)
                .setPageSize(50L)
                .setPageNumber(1L)
                .setPlatform("Win")
                .setMacAddress("66:55:44:33:22:11")
                .setSerialNumber("123")
                .setDeviceUuid("123");
        try {
            client.getTrustDeviceListWithOptions(getTrustDeviceListRequest, getTrustDeviceListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_trust_device_list_headers = dingtalkexclusive__1__0_models.GetTrustDeviceListHeaders()
        get_trust_device_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_trust_device_list_request = dingtalkexclusive__1__0_models.GetTrustDeviceListRequest(
            user_ids=[
                '652241xxx'
            ],
            gmt_create_start=1724256000000,
            gmt_create_end=1724256000000,
            gmt_modified_start=1724256000000,
            gmt_modified_end=1724256000000,
            page_size=50,
            page_number=1,
            platform='Win',
            mac_address='66:55:44:33:22:11',
            serial_number='123',
            device_uuid='123'
        )
        try:
            client.get_trust_device_list_with_options(get_trust_device_list_request, get_trust_device_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_trust_device_list_headers = dingtalkexclusive__1__0_models.GetTrustDeviceListHeaders()
        get_trust_device_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_trust_device_list_request = dingtalkexclusive__1__0_models.GetTrustDeviceListRequest(
            user_ids=[
                '652241xxx'
            ],
            gmt_create_start=1724256000000,
            gmt_create_end=1724256000000,
            gmt_modified_start=1724256000000,
            gmt_modified_end=1724256000000,
            page_size=50,
            page_number=1,
            platform='Win',
            mac_address='66:55:44:33:22:11',
            serial_number='123',
            device_uuid='123'
        )
        try:
            await client.get_trust_device_list_with_options_async(get_trust_device_list_request, get_trust_device_list_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetTrustDeviceListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetTrustDeviceListRequest;
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
        $getTrustDeviceListHeaders = new GetTrustDeviceListHeaders([]);
        $getTrustDeviceListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getTrustDeviceListRequest = new GetTrustDeviceListRequest([
            "userIds" => [
                "652241xxx"
            ],
            "gmtCreateStart" => 1724256000000,
            "gmtCreateEnd" => 1724256000000,
            "gmtModifiedStart" => 1724256000000,
            "gmtModifiedEnd" => 1724256000000,
            "pageSize" => 50,
            "pageNumber" => 1,
            "platform" => "Win",
            "macAddress" => "66:55:44:33:22:11",
            "serialNumber" => "123",
            "deviceUuid" => "123"
        ]);
        try {
            $client->getTrustDeviceListWithOptions($getTrustDeviceListRequest, $getTrustDeviceListHeaders, new RuntimeOptions([]));
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

  getTrustDeviceListHeaders := &dingtalkexclusive_1_0.GetTrustDeviceListHeaders{}
  getTrustDeviceListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getTrustDeviceListRequest := &dingtalkexclusive_1_0.GetTrustDeviceListRequest{
    UserIds: []*string{tea.String("652241xxx")},
    GmtCreateStart: tea.Int64(1724256000000),
    GmtCreateEnd: tea.Int64(1724256000000),
    GmtModifiedStart: tea.Int64(1724256000000),
    GmtModifiedEnd: tea.Int64(1724256000000),
    PageSize: tea.Int64(50),
    PageNumber: tea.Int64(1),
    Platform: tea.String("Win"),
    MacAddress: tea.String("66:55:44:33:22:11"),
    SerialNumber: tea.String("123"),
    DeviceUuid: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetTrustDeviceListWithOptions(getTrustDeviceListRequest, getTrustDeviceListHeaders, &util.RuntimeOptions{})
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
    let getTrustDeviceListHeaders = new dingtalkexclusive_1_0.GetTrustDeviceListHeaders({ });
    getTrustDeviceListHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getTrustDeviceListRequest = new dingtalkexclusive_1_0.GetTrustDeviceListRequest({
      userIds: [
        '652241xxx'
      ],
      gmtCreateStart: 1724256000000,
      gmtCreateEnd: 1724256000000,
      gmtModifiedStart: 1724256000000,
      gmtModifiedEnd: 1724256000000,
      pageSize: 50,
      pageNumber: 1,
      platform: 'Win',
      macAddress: '66:55:44:33:22:11',
      serialNumber: '123',
      deviceUuid: '123',
    });
    try {
      await client.getTrustDeviceListWithOptions(getTrustDeviceListRequest, getTrustDeviceListHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetTrustDeviceListHeaders getTrustDeviceListHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetTrustDeviceListHeaders();
            getTrustDeviceListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetTrustDeviceListRequest getTrustDeviceListRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetTrustDeviceListRequest
            {
                UserIds = new List<string>
                {
                    "652241xxx"
                },
                GmtCreateStart = 1724256000000,
                GmtCreateEnd = 1724256000000,
                GmtModifiedStart = 1724256000000,
                GmtModifiedEnd = 1724256000000,
                PageSize = 50,
                PageNumber = 1,
                Platform = "Win",
                MacAddress = "66:55:44:33:22:11",
                SerialNumber = "123",
                DeviceUuid = "123",
            };
            try
            {
                client.GetTrustDeviceListWithOptions(getTrustDeviceListRequest, getTrustDeviceListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Array | 查询结果。 |
| userId | String | 员工userId。 |
| platform | String | 平台类型，目前仅支持Mac和Win两种类型。 |
| macAddress | String | 可信设备mac地址。 |
| status | Integer | 设备状态，取值：   - **1**：待审批 - **2**：可信 - **3**：挂失 - **4**：拒绝 |
| createTime | Long | 创建时间，时间戳。 |
| title | String | 设备名称。 |
| model | String | 版本信息：   - Android端：示例值，Android,10。 - IOS端：示例值，iOS,12.0.1。 |
| modifiedTime | Long | 修改时间。 |
| id | Long | 设备编号。 |
| serialNumber | String | 设备序列号。 |
| deviceUuid | String | 设备uuid。 |
| total | Long | 总数据条数。 |
| pageSize | Long | 当前页数据条数。 |
| currentPage | Long | 当前页码。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "userId" : "65224xxxx39784",
    "platform" : "Mac",
    "macAddress" : "88:92:xx:xx:xx:xx",
    "status" : 2,
    "createTime" : 1628650483,
    "title" : "我的PC",
    "model" : "Android,10",
    "modifiedTime" : 1628650483,
    "id" : 123,
    "serialNumber" : "123",
    "deviceUuid" : "123"
  } ],
  "total" : 1000,
  "pageSize" : 50,
  "currentPage" : 1
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | staff.not.found | userId错误 | userId错误 |
| 400 | param.illegal | 参数不合法 | 参数不合法 |
| 500 | service.error | 系统错误 | 系统错误 |
