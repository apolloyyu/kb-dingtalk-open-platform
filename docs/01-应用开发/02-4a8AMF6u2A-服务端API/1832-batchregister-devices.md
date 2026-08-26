---
title: "批量注册设备"
source_url: "https://open.dingtalk.com/document/development/batchregister-devices"
namespace: "development"
slug: "batchregister-devices"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉物联 > 批量注册设备"
doc_id: "zz64rvf2Ij"
updated_at: "2025-09-08 19:06:08"
---

> Source: https://open.dingtalk.com/document/development/batchregister-devices
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉物联 > 批量注册设备
> Updated: 2025-09-08 19:06:08

# 批量注册设备

调用本接口批量注册设备到钉钉物联应用。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，钉钉物联接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 钉钉物联接口相关文档，已于2023年01月02日迁移至历史文档（不推荐）目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

在钉钉物联应用-设备管理页面，展示新注册的设备。如图所示：
![](https://img.alicdn.com/imgextra/i2/O1CN01P3UemN1rN5rPQ3tvr_!!6000000005618-2-tps-1090-669.png)

> **[!NOTE]**
>
> 调用本接口，需要开通钉钉物联应用，请参考[如何接入钉钉物联接口能力](https://open.dingtalk.com/document/orgapp/ding-iot-overview)。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 暂不支持 | — | — |

## 请求方法

```
POST /v1.0/diot/devices/registrations/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "corpId" : "String",
  "devices" : [ {
    "deviceId" : "String",
    "deviceName" : "String",
    "deviceStatus" : Integer,
    "deviceType" : "String",
    "deviceTypeName" : "String",
    "productType" : "String",
    "parentId" : "String",
    "location" : "String",
    "liveUrls" : {
      "hls" : "String",
      "flv" : "String",
      "rtmp" : "String"
    }
  } ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 否 | 钉钉物联组织ID，服务商必填。 |
| devices | Array | 是 | 设备列表。 |
| deviceId | String | 是 | 设备ID，自定义参数，需要全局唯一。 |
| deviceName | String | 是 | 设备名称，该参数值自定义。  例如：办公一区摄像头。 |
| deviceStatus | Integer | 是 | 设备状态，取值：   - **0**：在线 - **1**：离线 |
| deviceType | String | 是 | 设备类型，自定义传入，最多128个字节。  例如：camera。 |
| deviceTypeName | String | 是 | 设备类型名称，该参数值自定义，最多128个字节，与deviceType一一对应。  例如：摄像头。 |
| productType | String | 是 | 产品类型，取值：   - **CAMERA**：摄像头，可看直播 - **OTHERS**：非摄像头 |
| parentId | String | 否 | 外部父设备ID。 |
| location | String | 否 | 设备地址，该参数值自定义。  例如：办公一区。 |
| extraData | Map | 否 | 扩展数据。  **[!NOTE]**  该参数需线下提供，请通过[钉钉物联接口对接群](https://open.dingtalk.com/document/orgapp/ding-iot-overview)咨询。 |
| liveUrls | Object | 否 | 视频流地址直播流地址，支持rtmp、flv、hls等格式，需要https协议。 |
| hls | String | 否 | hls格式视频流地址。 |
| flv | String | 否 | flv格式视频流。 |
| rtmp | String | 否 | rtmp格式视频流。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| deviceIds | Array of String | 注册成功的外部设备ID。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/diot/devices/registrations/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:98b4f2xxx
Content-Type:application/json

{
  "corpId" : "ding123",
  "devices" : [ {
    "deviceId" : "002",
    "deviceName" : "摄像头002",
    "deviceStatus" : 0,
    "deviceType" : "Camera",
    "deviceTypeName" : "摄像头",
    "productType" : "CAMERA",
    "parentId" : "001",
    "location" : "社区南门",
    "liveUrls" : {
      "hls" : "https://abc.stream.m3u8",
      "flv" : "https://abc.stream.flv",
      "rtmp" : "rtmp://abc.stream"
    }
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
import com.aliyun.dingtalkdiot_1_0.*;
import com.aliyun.dingtalkdiot_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdiot_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdiot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdiot_1_0.Client client = Sample.createClient();
        BatchRegisterDeviceHeaders batchRegisterDeviceHeaders = new BatchRegisterDeviceHeaders();
        batchRegisterDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevicesLiveUrls devices0LiveUrls = new BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevicesLiveUrls()
                .setHls("https://abc.stream.m3u8")
                .setFlv("https://abc.stream.flv")
                .setRtmp("rtmp://abc.stream");
        BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices devices0 = new BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices()
                .setDeviceId("002")
                .setDeviceName("摄像头002")
                .setDeviceStatus(0)
                .setDeviceType("Camera")
                .setDeviceTypeName("摄像头")
                .setProductType("CAMERA")
                .setParentId("001")
                .setLocation("社区南门")
                .setLiveUrls(devices0LiveUrls);
        BatchRegisterDeviceRequest batchRegisterDeviceRequest = new BatchRegisterDeviceRequest()
                .setCorpId("ding123")
                .setDevices(java.util.Arrays.asList(
                    devices0
                ));
        try {
            client.batchRegisterDeviceWithOptions(batchRegisterDeviceRequest, batchRegisterDeviceHeaders, new RuntimeOptions());
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
        batch_register_device_headers = dingtalkdiot__1__0_models.BatchRegisterDeviceHeaders()
        batch_register_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        devices_0live_urls = dingtalkdiot__1__0_models.BatchRegisterDeviceRequestDevicesLiveUrls(
            hls='https://abc.stream.m3u8',
            flv='https://abc.stream.flv',
            rtmp='rtmp://abc.stream'
        )
        devices_0 = dingtalkdiot__1__0_models.BatchRegisterDeviceRequestDevices(
            device_id='002',
            device_name='摄像头002',
            device_status=0,
            device_type='Camera',
            device_type_name='摄像头',
            product_type='CAMERA',
            parent_id='001',
            location='社区南门',
            live_urls=devices_0live_urls
        )
        batch_register_device_request = dingtalkdiot__1__0_models.BatchRegisterDeviceRequest(
            corp_id='ding123',
            devices=[
                devices_0
            ]
        )
        try:
            client.batch_register_device_with_options(batch_register_device_request, batch_register_device_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_register_device_headers = dingtalkdiot__1__0_models.BatchRegisterDeviceHeaders()
        batch_register_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        devices_0live_urls = dingtalkdiot__1__0_models.BatchRegisterDeviceRequestDevicesLiveUrls(
            hls='https://abc.stream.m3u8',
            flv='https://abc.stream.flv',
            rtmp='rtmp://abc.stream'
        )
        devices_0 = dingtalkdiot__1__0_models.BatchRegisterDeviceRequestDevices(
            device_id='002',
            device_name='摄像头002',
            device_status=0,
            device_type='Camera',
            device_type_name='摄像头',
            product_type='CAMERA',
            parent_id='001',
            location='社区南门',
            live_urls=devices_0live_urls
        )
        batch_register_device_request = dingtalkdiot__1__0_models.BatchRegisterDeviceRequest(
            corp_id='ding123',
            devices=[
                devices_0
            ]
        )
        try:
            await client.batch_register_device_with_options_async(batch_register_device_request, batch_register_device_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterDeviceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterDeviceRequest\devices\liveUrls;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterDeviceRequest\devices;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterDeviceRequest;
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
        $batchRegisterDeviceHeaders = new BatchRegisterDeviceHeaders([]);
        $batchRegisterDeviceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $devices0LiveUrls = new liveUrls([
            "hls" => "https://abc.stream.m3u8",
            "flv" => "https://abc.stream.flv",
            "rtmp" => "rtmp://abc.stream"
        ]);
        $devices0 = new devices([
            "deviceId" => "002",
            "deviceName" => "摄像头002",
            "deviceStatus" => 0,
            "deviceType" => "Camera",
            "deviceTypeName" => "摄像头",
            "productType" => "CAMERA",
            "parentId" => "001",
            "location" => "社区南门",
            "liveUrls" => $devices0LiveUrls
        ]);
        $batchRegisterDeviceRequest = new BatchRegisterDeviceRequest([
            "corpId" => "ding123",
            "devices" => [
                $devices0
            ]
        ]);
        try {
            $client->batchRegisterDeviceWithOptions($batchRegisterDeviceRequest, $batchRegisterDeviceHeaders, new RuntimeOptions([]));
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
  dingtalkdiot_1_0  "github.com/alibabacloud-go/dingtalk/diot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  batchRegisterDeviceHeaders := &dingtalkdiot_1_0.BatchRegisterDeviceHeaders{}
  batchRegisterDeviceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  devices0LiveUrls := &dingtalkdiot_1_0.BatchRegisterDeviceRequestDevicesLiveUrls{
    Hls: tea.String("https://abc.stream.m3u8"),
    Flv: tea.String("https://abc.stream.flv"),
    Rtmp: tea.String("rtmp://abc.stream"),
  }
  devices0 := &dingtalkdiot_1_0.BatchRegisterDeviceRequestDevices{
    DeviceId: tea.String("002"),
    DeviceName: tea.String("摄像头002"),
    DeviceStatus: tea.Int32(0),
    DeviceType: tea.String("Camera"),
    DeviceTypeName: tea.String("摄像头"),
    ProductType: tea.String("CAMERA"),
    ParentId: tea.String("001"),
    Location: tea.String("社区南门"),
    LiveUrls: devices0LiveUrls,
  }
  batchRegisterDeviceRequest := &dingtalkdiot_1_0.BatchRegisterDeviceRequest{
    CorpId: tea.String("ding123"),
    Devices: []*dingtalkdiot_1_0.BatchRegisterDeviceRequestDevices{devices0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchRegisterDeviceWithOptions(batchRegisterDeviceRequest, batchRegisterDeviceHeaders, &util.RuntimeOptions{})
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
    let batchRegisterDeviceHeaders = new $dingtalkdiot_1_0.BatchRegisterDeviceHeaders({ });
    batchRegisterDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let devices0LiveUrls = new $dingtalkdiot_1_0.BatchRegisterDeviceRequestDevicesLiveUrls({
      hls: "https://abc.stream.m3u8",
      flv: "https://abc.stream.flv",
      rtmp: "rtmp://abc.stream",
    });
    let devices0 = new $dingtalkdiot_1_0.BatchRegisterDeviceRequestDevices({
      deviceId: "002",
      deviceName: "摄像头002",
      deviceStatus: 0,
      deviceType: "Camera",
      deviceTypeName: "摄像头",
      productType: "CAMERA",
      parentId: "001",
      location: "社区南门",
      liveUrls: devices0LiveUrls,
    });
    let batchRegisterDeviceRequest = new $dingtalkdiot_1_0.BatchRegisterDeviceRequest({
      corpId: "ding123",
      devices: [
        devices0
      ],
    });
    try {
      await client.batchRegisterDeviceWithOptions(batchRegisterDeviceRequest, batchRegisterDeviceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceHeaders batchRegisterDeviceHeaders = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceHeaders();
            batchRegisterDeviceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices.BatchRegisterDeviceRequestDevicesLiveUrls devices0LiveUrls = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices.BatchRegisterDeviceRequestDevicesLiveUrls
            {
                Hls = "https://abc.stream.m3u8",
                Flv = "https://abc.stream.flv",
                Rtmp = "rtmp://abc.stream",
            };
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices devices0 = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices
            {
                DeviceId = "002",
                DeviceName = "摄像头002",
                DeviceStatus = 0,
                DeviceType = "Camera",
                DeviceTypeName = "摄像头",
                ProductType = "CAMERA",
                ParentId = "001",
                Location = "社区南门",
                LiveUrls = devices0LiveUrls,
            };
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest batchRegisterDeviceRequest = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest
            {
                CorpId = "ding123",
                Devices = new List<AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterDeviceRequest.BatchRegisterDeviceRequestDevices>
                {
                    devices0
                },
            };
            try
            {
                client.BatchRegisterDeviceWithOptions(batchRegisterDeviceRequest, batchRegisterDeviceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdiot__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdiot_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdiot_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdiot_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceHeaders> batchRegisterDeviceHeaders = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceHeaders>();
  batchRegisterDeviceHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequestDevicesLiveUrls> devices0LiveUrls = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequestDevicesLiveUrls>(map<string, boost::any>({
    {"hls", boost::any(string("https://abc.stream.m3u8"))},
    {"flv", boost::any(string("https://abc.stream.flv"))},
    {"rtmp", boost::any(string("rtmp://abc.stream"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequestDevices> devices0 = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequestDevices>(map<string, boost::any>({
    {"deviceId", boost::any(string("002"))},
    {"deviceName", boost::any(string("摄像头002"))},
    {"deviceStatus", boost::any(0)},
    {"deviceType", boost::any(string("Camera"))},
    {"deviceTypeName", boost::any(string("摄像头"))},
    {"productType", boost::any(string("CAMERA"))},
    {"parentId", boost::any(string("001"))},
    {"location", boost::any(string("社区南门"))},
    {"liveUrls", !devices0LiveUrls ? boost::any() : boost::any(*devices0LiveUrls)}
  }));
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequest> batchRegisterDeviceRequest = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding123"))},
    {"devices", boost::any(vector<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterDeviceRequestDevices>({
      devices0
    }))}
  }));
  try {
    client->batchRegisterDeviceWithOptions(batchRegisterDeviceRequest, batchRegisterDeviceHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "deviceIds" : [ "002" ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 401 | system.not.exist | 系统未注册 | 系统未在钉钉物联平台注册 |
| 401 | corp.not.bind | 组织未绑定 | 钉钉组织未绑定该系统 |
| 500 | system.error | 系统异常 | 系统异常 |
| 500 | crop.not.install | 企业未安装钉钉物联应用，请联系我们(https://open.dingtalk.com/document/orgapp-server/dingtalk-iot-overview) | 未安装钉钉物联应用 |
