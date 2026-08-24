---
title: "查询考勤机信息"
source_url: "https://open.dingtalk.com/document/development/query-attendance-machine-information"
namespace: "development"
slug: "query-attendance-machine-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤机管理 > 查询考勤机信息"
doc_id: "5NXcD5WqDT"
updated_at: "2026-06-02 09:24:51"
---

> Source: https://open.dingtalk.com/document/development/query-attendance-machine-information
> Path: 应用开发 / 服务端API / 考勤 > 考勤机管理 > 查询考勤机信息
> Updated: 2026-06-02 09:24:51

# 查询考勤机信息

调用本接口，可根据考勤机设备ID查询考勤机信息，包括考勤机设备ID、设备名称、设备类型名称、固件版本等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/machines/{devId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| devId | Long | 是 | 考勤机设备ID，可调用[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取device\_id参数值。 |

### 请求示例

HTTP

```
GET /v1.0/attendance/machines/236847095 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7ed0axxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkattendance_1_0.*;
import com.aliyun.dingtalkattendance_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        GetMachineHeaders getMachineHeaders = new GetMachineHeaders();
        getMachineHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getMachineWithOptions("236847095", getMachineHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.attendance_1_0.client import Client as dingtalkattendance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.attendance_1_0 import models as dingtalkattendance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkattendance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkattendance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_machine_headers = dingtalkattendance__1__0_models.GetMachineHeaders()
        get_machine_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_machine_with_options('236847095', get_machine_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_machine_headers = dingtalkattendance__1__0_models.GetMachineHeaders()
        get_machine_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_machine_with_options_async('236847095', get_machine_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetMachineHeaders;
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
        $getMachineHeaders = new GetMachineHeaders([]);
        $getMachineHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getMachineWithOptions("236847095", $getMachineHeaders, new RuntimeOptions([]));
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
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkattendance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkattendance_1_0.Client{}
  _result, _err = dingtalkattendance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getMachineHeaders := &dingtalkattendance_1_0.GetMachineHeaders{}
  getMachineHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetMachineWithOptions(tea.String("236847095"), getMachineHeaders, &util.RuntimeOptions{})
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
import dingtalkattendance_1_0, * as $dingtalkattendance_1_0 from '@alicloud/dingtalk/attendance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkattendance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkattendance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getMachineHeaders = new $dingtalkattendance_1_0.GetMachineHeaders({ });
    getMachineHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.getMachineWithOptions("236847095", getMachineHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkattendance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkattendance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetMachineHeaders getMachineHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetMachineHeaders();
            getMachineHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetMachineWithOptions("236847095", getMachineHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkattendance__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

using namespace std;

Alibabacloud_Dingtalkattendance_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkattendance_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::Client> client = make_shared<Alibabacloud_Dingtalkattendance_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::GetMachineHeaders> getMachineHeaders = make_shared<Alibabacloud_Dingtalkattendance_1_0::GetMachineHeaders>();
  getMachineHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->getMachineWithOptions(make_shared<string>("236847095"), getMachineHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 考勤机的相关信息。 |
| deviceId | String | 加密后的考勤机设备ID。 |
| devId | Long | 考勤机设备ID。 |
| deviceName | String | 设备名称。 |
| productName | String | 设备类型名称。 |
| netStatus | String | 网络状态，取值。   - **1**：激活 - **2**：未激活 - **3**：已连接 - **4**：已断开 |
| productVersion | String | 固件版本。 |
| deviceSn | String | 设备序列号。 |
| maxFace | Integer | 人脸容量。 |
| voiceMode | Integer | 音量模式。 |
| atmManagerList | Array of String | 设备管理员列表。 |
| machineBluetoothVO | Object | 考勤机蓝牙相关设置信息。 |
| bluetoothValue | Boolean | 蓝牙是否打开打卡。   - **true**：打开 - **false**：未打开 |
| bluetoothCheckWithFace | Boolean | 蓝牙是否打开打卡人脸识别。   - **true**：打开 - **false**：未打开 |
| bluetoothDistanceMode | String | 蓝牙打卡范围。 |
| bluetoothDistanceModeDesc | String | 蓝牙打卡范围描述。 |
| monitorLocationAbnormal | Boolean | 是否打开位置异常监控。   - **true**：打开 - **false**：未打开 |
| address | String | 地址位置描述。 |
| longitude | double | 经度。 |
| latitude | double | 纬度。 |
| limitUserDeviceCount | Boolean | 是否限制员工常用手机。   - **true**：限制 - **false**：不限制 |
| userDeviceCount | Integer | 员工常用手机数量。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "deviceId" : "2078053438",
    "devId" : 1406333705,
    "deviceName" : "泱云❄️的体00056",
    "productName" : "M1F",
    "netStatus" : "4",
    "productVersion" : "1.0.1-R-20200326.1543",
    "deviceSn" : "0601IFW201001N000056",
    "maxFace" : 10000,
    "voiceMode" : 2,
    "atmManagerList" : [ "013139614537671030352" ],
    "machineBluetoothVO" : {
      "bluetoothValue" : true,
      "bluetoothCheckWithFace" : true,
      "bluetoothDistanceMode" : "default",
      "bluetoothDistanceModeDesc" : "默认 (最远5-10米)",
      "monitorLocationAbnormal" : true,
      "address" : "绿城-未来park",
      "longitude" : 120.01757758246528,
      "latitude" : 30.285871310763888,
      "limitUserDeviceCount" : true,
      "userDeviceCount" : 1
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 参数错误 |
| 500 | systemError | 系统异常 | 系统异常 |
