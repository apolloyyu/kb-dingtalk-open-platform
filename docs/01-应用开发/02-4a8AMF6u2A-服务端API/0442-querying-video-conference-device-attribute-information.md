---
title: "查询视频会议设备属性信息"
source_url: "https://open.dingtalk.com/document/development/querying-video-conference-device-attribute-information"
namespace: "development"
slug: "querying-video-conference-device-attribute-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 查询视频会议设备属性信息"
doc_id: "VvB8fihEXU"
updated_at: "2026-06-02 13:04:58"
---

> Source: https://open.dingtalk.com/document/development/querying-video-conference-device-attribute-information
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 会议室 > 查询视频会议设备属性信息
> Updated: 2026-06-02 13:04:58

# 查询视频会议设备属性信息

查询设备属性

## 接口调用说明

调用本接口之前，需要先接入[事件订阅](0014-event-subscription-overview.md)并订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/devices/properties/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUnionId | String | 是 | 操作查询的人员unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取获取。 |
| deviceId | String | 否 | 需要查询的设备ID，该参数从订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件中获取。 |
| deviceUnionId | String | 否 | 需要查询的设备unionId，该参数从订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件中获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| propertyNames | Array of String | 否 | 设备属性名称列表，最大值10。   - dev\_code：投屏码 - dev\_model：设备型号 - dev\_app\_status：设备状态 - dev\_net\_ip：设备ip - dev\_net\_type：设备网络类型 - dev\_wifi\_mac：设备无线mac地址 - dev\_wire\_mac：设备有线mac地址 - dev\_firmware\_v：设备固件版本 - dev\_software\_v：设备软件版本 - dev\_hdmi：设备外接显示器 |

### 请求示例

HTTP

```
POST /v1.0/rooms/devices/properties/query?operatorUnionId=lmvUxxxxx&deviceId=1234&deviceUnionId=lRkpxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "propertyNames" : [ "dev_wifi_mac" ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.QueryDevicePropertiesHeaders queryDevicePropertiesHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryDevicePropertiesHeaders();
        queryDevicePropertiesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.QueryDevicePropertiesRequest queryDevicePropertiesRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryDevicePropertiesRequest()
                .setOperatorUnionId("lmvUxxxxx")
                .setDeviceId("1234")
                .setDeviceUnionId("lRkpxxxxx")
                .setPropertyNames(java.util.Arrays.asList(
                    "dev_wifi_mac"
                ));
        try {
            client.queryDevicePropertiesWithOptions(queryDevicePropertiesRequest, queryDevicePropertiesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.rooms_1_0.client import Client as dingtalkrooms_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.rooms_1_0 import models as dingtalkrooms__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrooms_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrooms_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_device_properties_headers = dingtalkrooms__1__0_models.QueryDevicePropertiesHeaders()
        query_device_properties_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_device_properties_request = dingtalkrooms__1__0_models.QueryDevicePropertiesRequest(
            operator_union_id='lmvUxxxxx',
            device_id='1234',
            device_union_id='lRkpxxxxx',
            property_names=[
                'dev_wifi_mac'
            ]
        )
        try:
            client.query_device_properties_with_options(query_device_properties_request, query_device_properties_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_device_properties_headers = dingtalkrooms__1__0_models.QueryDevicePropertiesHeaders()
        query_device_properties_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_device_properties_request = dingtalkrooms__1__0_models.QueryDevicePropertiesRequest(
            operator_union_id='lmvUxxxxx',
            device_id='1234',
            device_union_id='lRkpxxxxx',
            property_names=[
                'dev_wifi_mac'
            ]
        )
        try:
            await client.query_device_properties_with_options_async(query_device_properties_request, query_device_properties_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryDevicePropertiesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryDevicePropertiesRequest;
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
        $queryDevicePropertiesHeaders = new QueryDevicePropertiesHeaders([]);
        $queryDevicePropertiesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryDevicePropertiesRequest = new QueryDevicePropertiesRequest([
            "operatorUnionId" => "lmvUxxxxx",
            "deviceId" => "1234",
            "deviceUnionId" => "lRkpxxxxx",
            "propertyNames" => [
                "dev_wifi_mac"
            ]
        ]);
        try {
            $client->queryDevicePropertiesWithOptions($queryDevicePropertiesRequest, $queryDevicePropertiesHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrooms_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrooms_1_0.Client{}
  _result, _err = dingtalkrooms_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryDevicePropertiesHeaders := &dingtalkrooms_1_0.QueryDevicePropertiesHeaders{}
  queryDevicePropertiesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryDevicePropertiesRequest := &dingtalkrooms_1_0.QueryDevicePropertiesRequest{
    OperatorUnionId: tea.String("lmvUxxxxx"),
    DeviceId: tea.String("1234"),
    DeviceUnionId: tea.String("lRkpxxxxx"),
    PropertyNames: []*string{tea.String("dev_wifi_mac")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryDevicePropertiesWithOptions(queryDevicePropertiesRequest, queryDevicePropertiesHeaders, &util.RuntimeOptions{})
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
import dingtalkrooms_1_0, * as $dingtalkrooms_1_0 from '@alicloud/dingtalk/rooms_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrooms_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrooms_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryDevicePropertiesHeaders = new $dingtalkrooms_1_0.QueryDevicePropertiesHeaders({ });
    queryDevicePropertiesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryDevicePropertiesRequest = new $dingtalkrooms_1_0.QueryDevicePropertiesRequest({
      operatorUnionId: "lmvUxxxxx",
      deviceId: "1234",
      deviceUnionId: "lRkpxxxxx",
      propertyNames: [
        "dev_wifi_mac"
      ],
    });
    try {
      await client.queryDevicePropertiesWithOptions(queryDevicePropertiesRequest, queryDevicePropertiesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrooms_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrooms_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryDevicePropertiesHeaders queryDevicePropertiesHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryDevicePropertiesHeaders();
            queryDevicePropertiesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryDevicePropertiesRequest queryDevicePropertiesRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryDevicePropertiesRequest
            {
                OperatorUnionId = "lmvUxxxxx",
                DeviceId = "1234",
                DeviceUnionId = "lRkpxxxxx",
                PropertyNames = new List<string>
                {
                    "dev_wifi_mac"
                },
            };
            try
            {
                client.QueryDevicePropertiesWithOptions(queryDevicePropertiesRequest, queryDevicePropertiesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 响应结果信息列表。 |
| propertyName | String | 设备属性名称。   - dev\_code：投屏码 - dev\_model：设备型号 - dev\_app\_status：设备状态 - dev\_net\_ip：设备ip - dev\_net\_type：设备网络类型，该属性有以下值：    - net\_wired：有线网络   - net\_offline：离线   - 具体的ssid：Wi-Fi - dev\_wifi\_mac：设备无线mac地址 - dev\_wire\_mac：设备有线mac地址 - dev\_firmware\_v：设备固件版本 - dev\_software\_v：设备软件版本 - dev\_hdmi：设备外接显示器 |
| propertyValue | String | 设备属性值。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "propertyName" : "dev_app_status",
    "propertyValue" : "idle"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | device.not.found | device not found | 设备不存在 |
| 400 | param.error | param error | operatorUnionId参数为空 |
| 403 | no.permission | no permission | 无查询权限 |
| 500 | system.error | system error | 系统错误 |
