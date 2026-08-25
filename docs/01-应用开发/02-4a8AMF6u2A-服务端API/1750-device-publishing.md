---
title: "设备账号向目标用户发送DING消息"
source_url: "https://open.dingtalk.com/document/development/device-publishing"
namespace: "development"
slug: "device-publishing"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 行业连接 > 设备账号向目标用户发送DING消息"
doc_id: "PNkWQFXsD5"
updated_at: "2025-09-08 19:05:13"
---

> Source: https://open.dingtalk.com/document/development/device-publishing
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 行业连接 > 设备账号向目标用户发送DING消息
> Updated: 2025-09-08 19:05:13

# 设备账号向目标用户发送DING消息

调用本接口使用设备对应的钉钉账号，向指定人员发送DING消息

![](https://img.alicdn.com/imgextra/i4/O1CN01zmEBjG259isht7208_!!6000000007484-2-tps-600-315.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 制造业设备DING消息发送权限 | 暂不支持 |
| 第三方企业应用 | 支持 | 制造业设备DING消息发送权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 制造业设备DING消息发送权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/devicemng/ding HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "paramsJson" : "String",
  "deviceKey" : "String",
  "receiverUserIdList" : [ "String" ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| paramsJson | String | 否 | 消息体动态参数，JSON格式为DING消息模板中的变量赋值，取值如下：   - **msgContent**：消息体内容 - **detailUrl**：消息详情链接 - **orgName**：组织名称 |
| deviceKey | String | 是 | 设备标识，生产设备的唯一标识，将据此生成钉钉账号。 |
| receiverUserIdList | Array of String | 是 | 接收消息的人员userid列表。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | String | 发送消息成功后的回执ID。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/devicemng/ding HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:3d60a2xxx
Content-Type:application/json

{
  "paramsJson" : "{   \"msgContent\": \"test msg!\",   \"detailUrl\": \"https://open.dingtalk.com/\",   \"orgName\": \"钉钉行业化\" }",
  "deviceKey" : "xxxx",
  "receiverUserIdList" : [ "manager123" ]
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
        DeviceDingHeaders deviceDingHeaders = new DeviceDingHeaders();
        deviceDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DeviceDingRequest deviceDingRequest = new DeviceDingRequest()
                .setParamsJson("{   \"msgContent\": \"test msg!\",   \"detailUrl\": \"https://open.dingtalk.com/\",   \"orgName\": \"钉钉行业化\" }")
                .setDeviceKey("xxxx")
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "manager123"
                ));
        try {
            client.deviceDingWithOptions(deviceDingRequest, deviceDingHeaders, new RuntimeOptions());
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
        device_ding_headers = dingtalkdevicemng__1__0_models.DeviceDingHeaders()
        device_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        device_ding_request = dingtalkdevicemng__1__0_models.DeviceDingRequest(
            params_json='{   "msgContent": "test msg!",   "detailUrl": "https://open.dingtalk.com/",   "orgName": "钉钉行业化" }',
            device_key='xxxx',
            receiver_user_id_list=[
                'manager123'
            ]
        )
        try:
            client.device_ding_with_options(device_ding_request, device_ding_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        device_ding_headers = dingtalkdevicemng__1__0_models.DeviceDingHeaders()
        device_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        device_ding_request = dingtalkdevicemng__1__0_models.DeviceDingRequest(
            params_json='{   "msgContent": "test msg!",   "detailUrl": "https://open.dingtalk.com/",   "orgName": "钉钉行业化" }',
            device_key='xxxx',
            receiver_user_id_list=[
                'manager123'
            ]
        )
        try:
            await client.device_ding_with_options_async(device_ding_request, device_ding_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\DeviceDingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\DeviceDingRequest;
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
        $deviceDingHeaders = new DeviceDingHeaders([]);
        $deviceDingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deviceDingRequest = new DeviceDingRequest([
            "paramsJson" => "{   \"msgContent\": \"test msg!\",   \"detailUrl\": \"https://open.dingtalk.com/\",   \"orgName\": \"钉钉行业化\" }",
            "deviceKey" => "xxxx",
            "receiverUserIdList" => [
                "manager123"
            ]
        ]);
        try {
            $client->deviceDingWithOptions($deviceDingRequest, $deviceDingHeaders, new RuntimeOptions([]));
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

  deviceDingHeaders := &dingtalkdevicemng_1_0.DeviceDingHeaders{}
  deviceDingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deviceDingRequest := &dingtalkdevicemng_1_0.DeviceDingRequest{
    ParamsJson: tea.String("{   \"msgContent\": \"test msg!\",   \"detailUrl\": \"https://open.dingtalk.com/\",   \"orgName\": \"钉钉行业化\" }"),
    DeviceKey: tea.String("xxxx"),
    ReceiverUserIdList: []*string{tea.String("manager123")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeviceDingWithOptions(deviceDingRequest, deviceDingHeaders, &util.RuntimeOptions{})
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
    let deviceDingHeaders = new $dingtalkdevicemng_1_0.DeviceDingHeaders({ });
    deviceDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deviceDingRequest = new $dingtalkdevicemng_1_0.DeviceDingRequest({
      paramsJson: "{   \"msgContent\": \"test msg!\",   \"detailUrl\": \"https://open.dingtalk.com/\",   \"orgName\": \"钉钉行业化\" }",
      deviceKey: "xxxx",
      receiverUserIdList: [
        "manager123"
      ],
    });
    try {
      await client.deviceDingWithOptions(deviceDingRequest, deviceDingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.DeviceDingHeaders deviceDingHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.DeviceDingHeaders();
            deviceDingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.DeviceDingRequest deviceDingRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.DeviceDingRequest
            {
                ParamsJson = "{   \"msgContent\": \"test msg!\",   \"detailUrl\": \"https://open.dingtalk.com/\",   \"orgName\": \"钉钉行业化\" }",
                DeviceKey = "xxxx",
                ReceiverUserIdList = new List<string>
                {
                    "manager123"
                },
            };
            try
            {
                client.DeviceDingWithOptions(deviceDingRequest, deviceDingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdevicemng__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdevicemng_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdevicemng_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::DeviceDingHeaders> deviceDingHeaders = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::DeviceDingHeaders>();
  deviceDingHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::DeviceDingRequest> deviceDingRequest = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::DeviceDingRequest>(map<string, boost::any>({
    {"paramsJson", boost::any(string("{   "msgContent": "test msg!",   "detailUrl": "https://open.dingtalk.com/",   "orgName": "钉钉行业化" }"))},
    {"deviceKey", boost::any(string("xxxx"))},
    {"receiverUserIdList", boost::any(vector<string>({
      "manager123"
    }))}
  }));
  try {
    client->deviceDingWithOptions(deviceDingRequest, deviceDingHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "result" : "MSxxx"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | deviceNotExist | 找不到设备 | 找不到设备 |
| 400 | deviceKeyDuplicate | 设备key重复 | 设备key重复 |
| 400 | sendDingFail | 机器人发送ding消息失败 | 机器人发送ding消息失败 |
| 500 | systemError | 系统错误 | 系统错误 |
