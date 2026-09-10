---
title: "批量新增可信设备"
source_url: "https://open.dingtalk.com/document/development/create-multiple-trusted-devices"
namespace: "development"
slug: "create-multiple-trusted-devices"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 可信设备 > 批量新增可信设备"
doc_id: "PfiDe1Sw0Y"
updated_at: "2026-06-04 19:09:53"
---

> Source: https://open.dingtalk.com/document/development/create-multiple-trusted-devices
> Path: 应用开发 / 服务端 API / 专属钉钉 > 可信设备 > 批量新增可信设备
> Updated: 2026-06-04 19:09:53

# 批量新增可信设备

用于给某个用户批量新增可信设备。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/trusts/devices |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.TrustedDevice.ReadWrite-专属钉钉可信设备信息读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：  企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。  第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 员工userid，为0时表示这个设备为公共设备 |
| platform | String | 是 | 操作端。   - Mac端 - Win端 |
| macAddressList | Array of String | 否 | 设备的Mac地址。 |
| detailList | Array | 否 | 设备列表，如果需要设置mac地址以外的设备信息，优先使用detailList，该列表与macAddressList至少有一项不为空。 |
| title | String | 否 | 设备标题。 |
| macAddress | String | 否 | 设备的Mac地址。 |
| serialNumber | String | 否 | 设备序列号。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/trusts/devices HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:123token
Content-Type:application/json

{
  "userId" : "123",
  "platform" : "Win",
  "macAddressList" : [ "6c:96:xx:xx:xx:xx" ],
  "detailList" : [ {
    "title" : "张三的设备",
    "macAddress" : "6c:96:xx:xx:xx:xx",
    "serialNumber" : "123"
  } ]
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
        com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceBatchHeaders createTrustedDeviceBatchHeaders = new com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceBatchHeaders();
        createTrustedDeviceBatchHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceBatchRequest.CreateTrustedDeviceBatchRequestDetailList detailList0 = new com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceBatchRequest.CreateTrustedDeviceBatchRequestDetailList()
                .setTitle("张三的设备")
                .setMacAddress("6c:96:xx:xx:xx:xx")
                .setSerialNumber("123");
        com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceBatchRequest createTrustedDeviceBatchRequest = new com.aliyun.dingtalkexclusive_1_0.models.CreateTrustedDeviceBatchRequest()
                .setUserId("123")
                .setPlatform("Win")
                .setMacAddressList(java.util.Arrays.asList(
                    "6c:96:xx:xx:xx:xx"
                ))
                .setDetailList(java.util.Arrays.asList(
                    detailList0
                ));
        try {
            client.createTrustedDeviceBatchWithOptions(createTrustedDeviceBatchRequest, createTrustedDeviceBatchHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_trusted_device_batch_headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchHeaders()
        create_trusted_device_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_list_0 = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequestDetailList(
            title='张三的设备',
            mac_address='6c:96:xx:xx:xx:xx',
            serial_number='123'
        )
        create_trusted_device_batch_request = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequest(
            user_id='123',
            platform='Win',
            mac_address_list=[
                '6c:96:xx:xx:xx:xx'
            ],
            detail_list=[
                detail_list_0
            ]
        )
        try:
            client.create_trusted_device_batch_with_options(create_trusted_device_batch_request, create_trusted_device_batch_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_trusted_device_batch_headers = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchHeaders()
        create_trusted_device_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_list_0 = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequestDetailList(
            title='张三的设备',
            mac_address='6c:96:xx:xx:xx:xx',
            serial_number='123'
        )
        create_trusted_device_batch_request = dingtalkexclusive__1__0_models.CreateTrustedDeviceBatchRequest(
            user_id='123',
            platform='Win',
            mac_address_list=[
                '6c:96:xx:xx:xx:xx'
            ],
            detail_list=[
                detail_list_0
            ]
        )
        try:
            await client.create_trusted_device_batch_with_options_async(create_trusted_device_batch_request, create_trusted_device_batch_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CreateTrustedDeviceBatchHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CreateTrustedDeviceBatchRequest\detailList;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\CreateTrustedDeviceBatchRequest;
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
        $createTrustedDeviceBatchHeaders = new CreateTrustedDeviceBatchHeaders([]);
        $createTrustedDeviceBatchHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $detailList0 = new detailList([
            "title" => "张三的设备",
            "macAddress" => "6c:96:xx:xx:xx:xx",
            "serialNumber" => "123"
        ]);
        $createTrustedDeviceBatchRequest = new CreateTrustedDeviceBatchRequest([
            "userId" => "123",
            "platform" => "Win",
            "macAddressList" => [
                "6c:96:xx:xx:xx:xx"
            ],
            "detailList" => [
                $detailList0
            ]
        ]);
        try {
            $client->createTrustedDeviceBatchWithOptions($createTrustedDeviceBatchRequest, $createTrustedDeviceBatchHeaders, new RuntimeOptions([]));
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

  createTrustedDeviceBatchHeaders := &dingtalkexclusive_1_0.CreateTrustedDeviceBatchHeaders{}
  createTrustedDeviceBatchHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  detailList0 := &dingtalkexclusive_1_0.CreateTrustedDeviceBatchRequestDetailList{
    Title: tea.String("张三的设备"),
    MacAddress: tea.String("6c:96:xx:xx:xx:xx"),
    SerialNumber: tea.String("123"),
  }
  createTrustedDeviceBatchRequest := &dingtalkexclusive_1_0.CreateTrustedDeviceBatchRequest{
    UserId: tea.String("123"),
    Platform: tea.String("Win"),
    MacAddressList: []*string{tea.String("6c:96:xx:xx:xx:xx")},
    DetailList: []*dingtalkexclusive_1_0.CreateTrustedDeviceBatchRequestDetailList{detailList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTrustedDeviceBatchWithOptions(createTrustedDeviceBatchRequest, createTrustedDeviceBatchHeaders, &util.RuntimeOptions{})
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
    let createTrustedDeviceBatchHeaders = new dingtalkexclusive_1_0.CreateTrustedDeviceBatchHeaders({ });
    createTrustedDeviceBatchHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let detailList0 = new dingtalkexclusive_1_0.CreateTrustedDeviceBatchRequestDetailList({
      title: '张三的设备',
      macAddress: '6c:96:xx:xx:xx:xx',
      serialNumber: '123',
    });
    let createTrustedDeviceBatchRequest = new dingtalkexclusive_1_0.CreateTrustedDeviceBatchRequest({
      userId: '123',
      platform: 'Win',
      macAddressList: [
        '6c:96:xx:xx:xx:xx'
      ],
      detailList: [
        detailList0
      ],
    });
    try {
      await client.createTrustedDeviceBatchWithOptions(createTrustedDeviceBatchRequest, createTrustedDeviceBatchHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchHeaders createTrustedDeviceBatchHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchHeaders();
            createTrustedDeviceBatchHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchRequest.CreateTrustedDeviceBatchRequestDetailList detailList0 = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchRequest.CreateTrustedDeviceBatchRequestDetailList
            {
                Title = "张三的设备",
                MacAddress = "6c:96:xx:xx:xx:xx",
                SerialNumber = "123",
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchRequest createTrustedDeviceBatchRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchRequest
            {
                UserId = "123",
                Platform = "Win",
                MacAddressList = new List<string>
                {
                    "6c:96:xx:xx:xx:xx"
                },
                DetailList = new List<AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.CreateTrustedDeviceBatchRequest.CreateTrustedDeviceBatchRequestDetailList>
                {
                    detailList0
                },
            };
            try
            {
                client.CreateTrustedDeviceBatchWithOptions(createTrustedDeviceBatchRequest, createTrustedDeviceBatchHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 处理结果。   - true：成功 - false：失败 |

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
| 400 | param.invalid | %s | Mac地址有误，请确认地址格式，且不能重复添加 |
| 400 | param.illegal | %s | 参数不合法，请确认userId和platform是否正确 |
