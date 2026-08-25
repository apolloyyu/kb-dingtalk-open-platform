---
title: "注册设备"
source_url: "https://open.dingtalk.com/document/development/register-devices"
namespace: "development"
slug: "register-devices"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉物联 > 注册设备"
doc_id: "AgWT8iRX9A"
updated_at: "2025-09-08 19:06:07"
---

> Source: https://open.dingtalk.com/document/development/register-devices
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉物联 > 注册设备
> Updated: 2025-09-08 19:06:07

# 注册设备

本接口用于将企业设备信息注册到钉钉物联应用。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，钉钉物联接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 钉钉物联接口相关文档，已于2023年01月02日迁移至历史文档（不推荐）目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

在钉钉物联应用-设备管理页面，展示新注册的设备。如图所示：![](https://img.alicdn.com/imgextra/i2/O1CN01P3UemN1rN5rPQ3tvr_!!6000000005618-2-tps-1090-669.png)

> **[!NOTE]**
>
> 调用本接口，需要开通**钉钉物联应用**，请参考[如何接入钉钉物联接口能力](https://open.dingtalk.com/document/orgapp/ding-iot-overview)。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 暂不支持 | — | — |

## 请求方法

```
POST /v1.0/diot/devices/register HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "corpId" : "String",
  "id" : "String",
  "deviceName" : "String",
  "nickName" : "String",
  "location" : "String",
  "deviceStatus" : Integer,
  "deviceType" : "String",
  "deviceTypeName" : "String",
  "parentId" : "String",
  "productType" : "String",
  "liveUrls" : {
    "hls" : "String",
    "flv" : "String",
    "rtmp" : "String"
  }
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
| id | String | 是 | 设备ID，自定义参数，需要全局唯一。 |
| deviceName | String | 是 | 设备名称，该参数值自定义。  例如：办公一区摄像头。 |
| nickName | String | 否 | 设备昵称，该参数值自定义。  例如：一区摄像头。 |
| location | String | 否 | 设备地址，该参数值自定义。  例如：办公一区。 |
| deviceStatus | Integer | 是 | 设备状态，取值：   - **0**：在线 - **1**：离线 |
| deviceType | String | 是 | 设备类型，该参数值自定义。  例如：camera。 |
| deviceTypeName | String | 是 | 设备类型名称，该参数值自定义，与deviceType对应。  例如：摄像头。 |
| parentId | String | 否 | 设备父节点ID。 |
| productType | String | 是 | 设备类型，取值：   - **CAMERA**：摄像头 - **OTHERS**：其它 |
| liveUrls | Object | 否 | 视频流地址直播流地址，支持rtmp、flv、hls等格式，需要https协议。 |
| hls | String | 否 | hls格式视频流地址。 |
| flv | String | 否 | flv格式视频流。 |
| rtmp | String | 否 | rtmp格式视频流。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| deviceId | String | 设备ID。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/diot/devices/register HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:67c8a6xxx
Content-Type:application/json

{
  "corpId" : "ding123",
  "id" : "002",
  "deviceName" : "摄像头1",
  "nickName" : "摄像头1",
  "location" : "东南门",
  "deviceStatus" : 0,
  "deviceType" : "Camera",
  "deviceTypeName" : "摄像头",
  "parentId" : "001",
  "productType" : "CAMERA",
  "liveUrls" : {
    "hls" : "https://abc.stream.m3u8",
    "flv" : "https://abc.stream.flv",
    "rtmp" : "rtmp://abc.stream"
  }
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
        RegisterDeviceHeaders registerDeviceHeaders = new RegisterDeviceHeaders();
        registerDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        RegisterDeviceRequest.RegisterDeviceRequestLiveUrls liveUrls = new RegisterDeviceRequest.RegisterDeviceRequestLiveUrls()
                .setHls("https://abc.stream.m3u8")
                .setFlv("https://abc.stream.flv")
                .setRtmp("rtmp://abc.stream");
        RegisterDeviceRequest registerDeviceRequest = new RegisterDeviceRequest()
                .setCorpId("ding123")
                .setId("002")
                .setDeviceName("摄像头1")
                .setNickName("摄像头1")
                .setLocation("东南门")
                .setDeviceStatus(0)
                .setDeviceType("Camera")
                .setDeviceTypeName("摄像头")
                .setParentId("001")
                .setProductType("CAMERA")
                .setLiveUrls(liveUrls);
        try {
            client.registerDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, new RuntimeOptions());
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
        register_device_headers = dingtalkdiot__1__0_models.RegisterDeviceHeaders()
        register_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        live_urls = dingtalkdiot__1__0_models.RegisterDeviceRequestLiveUrls(
            hls='https://abc.stream.m3u8',
            flv='https://abc.stream.flv',
            rtmp='rtmp://abc.stream'
        )
        register_device_request = dingtalkdiot__1__0_models.RegisterDeviceRequest(
            corp_id='ding123',
            id='002',
            device_name='摄像头1',
            nick_name='摄像头1',
            location='东南门',
            device_status=0,
            device_type='Camera',
            device_type_name='摄像头',
            parent_id='001',
            product_type='CAMERA',
            live_urls=live_urls
        )
        try:
            client.register_device_with_options(register_device_request, register_device_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_device_headers = dingtalkdiot__1__0_models.RegisterDeviceHeaders()
        register_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        live_urls = dingtalkdiot__1__0_models.RegisterDeviceRequestLiveUrls(
            hls='https://abc.stream.m3u8',
            flv='https://abc.stream.flv',
            rtmp='rtmp://abc.stream'
        )
        register_device_request = dingtalkdiot__1__0_models.RegisterDeviceRequest(
            corp_id='ding123',
            id='002',
            device_name='摄像头1',
            nick_name='摄像头1',
            location='东南门',
            device_status=0,
            device_type='Camera',
            device_type_name='摄像头',
            parent_id='001',
            product_type='CAMERA',
            live_urls=live_urls
        )
        try:
            await client.register_device_with_options_async(register_device_request, register_device_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\RegisterDeviceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\RegisterDeviceRequest\liveUrls;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\RegisterDeviceRequest;
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
        $registerDeviceHeaders = new RegisterDeviceHeaders([]);
        $registerDeviceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $liveUrls = new liveUrls([
            "hls" => "https://abc.stream.m3u8",
            "flv" => "https://abc.stream.flv",
            "rtmp" => "rtmp://abc.stream"
        ]);
        $registerDeviceRequest = new RegisterDeviceRequest([
            "corpId" => "ding123",
            "id" => "002",
            "deviceName" => "摄像头1",
            "nickName" => "摄像头1",
            "location" => "东南门",
            "deviceStatus" => 0,
            "deviceType" => "Camera",
            "deviceTypeName" => "摄像头",
            "parentId" => "001",
            "productType" => "CAMERA",
            "liveUrls" => $liveUrls
        ]);
        try {
            $client->registerDeviceWithOptions($registerDeviceRequest, $registerDeviceHeaders, new RuntimeOptions([]));
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

  registerDeviceHeaders := &dingtalkdiot_1_0.RegisterDeviceHeaders{}
  registerDeviceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  liveUrls := &dingtalkdiot_1_0.RegisterDeviceRequestLiveUrls{
    Hls: tea.String("https://abc.stream.m3u8"),
    Flv: tea.String("https://abc.stream.flv"),
    Rtmp: tea.String("rtmp://abc.stream"),
  }
  registerDeviceRequest := &dingtalkdiot_1_0.RegisterDeviceRequest{
    CorpId: tea.String("ding123"),
    Id: tea.String("002"),
    DeviceName: tea.String("摄像头1"),
    NickName: tea.String("摄像头1"),
    Location: tea.String("东南门"),
    DeviceStatus: tea.Int32(0),
    DeviceType: tea.String("Camera"),
    DeviceTypeName: tea.String("摄像头"),
    ParentId: tea.String("001"),
    ProductType: tea.String("CAMERA"),
    LiveUrls: liveUrls,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RegisterDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, &util.RuntimeOptions{})
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
    let registerDeviceHeaders = new $dingtalkdiot_1_0.RegisterDeviceHeaders({ });
    registerDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let liveUrls = new $dingtalkdiot_1_0.RegisterDeviceRequestLiveUrls({
      hls: "https://abc.stream.m3u8",
      flv: "https://abc.stream.flv",
      rtmp: "rtmp://abc.stream",
    });
    let registerDeviceRequest = new $dingtalkdiot_1_0.RegisterDeviceRequest({
      corpId: "ding123",
      id: "002",
      deviceName: "摄像头1",
      nickName: "摄像头1",
      location: "东南门",
      deviceStatus: 0,
      deviceType: "Camera",
      deviceTypeName: "摄像头",
      parentId: "001",
      productType: "CAMERA",
      liveUrls: liveUrls,
    });
    try {
      await client.registerDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.RegisterDeviceHeaders registerDeviceHeaders = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.RegisterDeviceHeaders();
            registerDeviceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.RegisterDeviceRequest.RegisterDeviceRequestLiveUrls liveUrls = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.RegisterDeviceRequest.RegisterDeviceRequestLiveUrls
            {
                Hls = "https://abc.stream.m3u8",
                Flv = "https://abc.stream.flv",
                Rtmp = "rtmp://abc.stream",
            };
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.RegisterDeviceRequest registerDeviceRequest = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.RegisterDeviceRequest
            {
                CorpId = "ding123",
                Id = "002",
                DeviceName = "摄像头1",
                NickName = "摄像头1",
                Location = "东南门",
                DeviceStatus = 0,
                DeviceType = "Camera",
                DeviceTypeName = "摄像头",
                ParentId = "001",
                ProductType = "CAMERA",
                LiveUrls = liveUrls,
            };
            try
            {
                client.RegisterDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::RegisterDeviceHeaders> registerDeviceHeaders = make_shared<Alibabacloud_Dingtalkdiot_1_0::RegisterDeviceHeaders>();
  registerDeviceHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::RegisterDeviceRequestLiveUrls> liveUrls = make_shared<Alibabacloud_Dingtalkdiot_1_0::RegisterDeviceRequestLiveUrls>(map<string, boost::any>({
    {"hls", boost::any(string("https://abc.stream.m3u8"))},
    {"flv", boost::any(string("https://abc.stream.flv"))},
    {"rtmp", boost::any(string("rtmp://abc.stream"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::RegisterDeviceRequest> registerDeviceRequest = make_shared<Alibabacloud_Dingtalkdiot_1_0::RegisterDeviceRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding123"))},
    {"id", boost::any(string("002"))},
    {"deviceName", boost::any(string("摄像头1"))},
    {"nickName", boost::any(string("摄像头1"))},
    {"location", boost::any(string("东南门"))},
    {"deviceStatus", boost::any(0)},
    {"deviceType", boost::any(string("Camera"))},
    {"deviceTypeName", boost::any(string("摄像头"))},
    {"parentId", boost::any(string("001"))},
    {"productType", boost::any(string("CAMERA"))},
    {"liveUrls", !liveUrls ? boost::any() : boost::any(*liveUrls)}
  }));
  try {
    client->registerDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "deviceId" : "1"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 401 | corp.not.bind | 组织未绑定 | 钉钉组织未绑定该系统 |
| 401 | system.not.exist | 系统未注册 | 系统未在钉钉物联平台注册 |
| 500 | system.error | 系统异常 | 系统异常 |
| 500 | crop.not.install | 企业未安装钉钉物联应用，请联系我们(https://open.dingtalk.com/document/orgapp-server/dingtalk-iot-overview) | 企业未安装钉钉物联应用 |
