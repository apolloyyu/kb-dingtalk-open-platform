---
title: "查询视频会议设备信息"
source_url: "https://open.dingtalk.com/document/development/querying-video-conference-device-information"
namespace: "development"
slug: "querying-video-conference-device-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 查询视频会议设备信息"
doc_id: "zAZFE2V9tG"
updated_at: "2026-06-02 13:04:58"
---

> Source: https://open.dingtalk.com/document/development/querying-video-conference-device-information
> Path: 应用开发 / 服务端 API / 音视频 > 智能会议室 > 会议室 > 查询视频会议设备信息
> Updated: 2026-06-02 13:04:58

# 查询视频会议设备信息

调用本接口，查询视频会议设备信息。

## 接口调用说明

调用本接口之前，需要先接入[事件订阅](0014-event-subscription-overview.md)并订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/devices |
| HTTP Method | GET |
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
| deviceId | String | 否 | 需要查询的设备ID，该参数从订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件中获取。  **[!NOTE]**    `deviceId`字段或`deviceUnionId`字段，必须二选一。 |
| deviceUnionId | String | 否 | 需要查询的设备unionId，该参数从订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件中获取。  **[!NOTE]**    `deviceId`字段或`deviceUnionId`字段，必须二选一。 |

### 请求示例

HTTP

```
GET /v1.0/rooms/devices?operatorUnionId=lmvxxxxx&deviceId=1234&deviceUnionId=lmvUxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomDeviceHeaders queryMeetingRoomDeviceHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomDeviceHeaders();
        queryMeetingRoomDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomDeviceRequest queryMeetingRoomDeviceRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomDeviceRequest()
                .setOperatorUnionId("lmvxxxxx")
                .setDeviceId("1234")
                .setDeviceUnionId("lmvUxxxxx");
        try {
            client.queryMeetingRoomDeviceWithOptions(queryMeetingRoomDeviceRequest, queryMeetingRoomDeviceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_meeting_room_device_headers = dingtalkrooms__1__0_models.QueryMeetingRoomDeviceHeaders()
        query_meeting_room_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_device_request = dingtalkrooms__1__0_models.QueryMeetingRoomDeviceRequest(
            operator_union_id='lmvxxxxx',
            device_id='1234',
            device_union_id='lmvUxxxxx'
        )
        try:
            client.query_meeting_room_device_with_options(query_meeting_room_device_request, query_meeting_room_device_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_meeting_room_device_headers = dingtalkrooms__1__0_models.QueryMeetingRoomDeviceHeaders()
        query_meeting_room_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_device_request = dingtalkrooms__1__0_models.QueryMeetingRoomDeviceRequest(
            operator_union_id='lmvxxxxx',
            device_id='1234',
            device_union_id='lmvUxxxxx'
        )
        try:
            await client.query_meeting_room_device_with_options_async(query_meeting_room_device_request, query_meeting_room_device_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomDeviceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomDeviceRequest;
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
        $queryMeetingRoomDeviceHeaders = new QueryMeetingRoomDeviceHeaders([]);
        $queryMeetingRoomDeviceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryMeetingRoomDeviceRequest = new QueryMeetingRoomDeviceRequest([
            "operatorUnionId" => "lmvxxxxx",
            "deviceId" => "1234",
            "deviceUnionId" => "lmvUxxxxx"
        ]);
        try {
            $client->queryMeetingRoomDeviceWithOptions($queryMeetingRoomDeviceRequest, $queryMeetingRoomDeviceHeaders, new RuntimeOptions([]));
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

  queryMeetingRoomDeviceHeaders := &dingtalkrooms_1_0.QueryMeetingRoomDeviceHeaders{}
  queryMeetingRoomDeviceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryMeetingRoomDeviceRequest := &dingtalkrooms_1_0.QueryMeetingRoomDeviceRequest{
    OperatorUnionId: tea.String("lmvxxxxx"),
    DeviceId: tea.String("1234"),
    DeviceUnionId: tea.String("lmvUxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryMeetingRoomDeviceWithOptions(queryMeetingRoomDeviceRequest, queryMeetingRoomDeviceHeaders, &util.RuntimeOptions{})
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
    let queryMeetingRoomDeviceHeaders = new $dingtalkrooms_1_0.QueryMeetingRoomDeviceHeaders({ });
    queryMeetingRoomDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryMeetingRoomDeviceRequest = new $dingtalkrooms_1_0.QueryMeetingRoomDeviceRequest({
      operatorUnionId: "lmvxxxxx",
      deviceId: "1234",
      deviceUnionId: "lmvUxxxxx",
    });
    try {
      await client.queryMeetingRoomDeviceWithOptions(queryMeetingRoomDeviceRequest, queryMeetingRoomDeviceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomDeviceHeaders queryMeetingRoomDeviceHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomDeviceHeaders();
            queryMeetingRoomDeviceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomDeviceRequest queryMeetingRoomDeviceRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomDeviceRequest
            {
                OperatorUnionId = "lmvxxxxx",
                DeviceId = "1234",
                DeviceUnionId = "lmvUxxxxx",
            };
            try
            {
                client.QueryMeetingRoomDeviceWithOptions(queryMeetingRoomDeviceRequest, queryMeetingRoomDeviceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 响应结果。 |
| deviceId | String | 设备ID。 |
| deviceUnionId | String | 设备unionId。 |
| openRoomId | String | 设备绑定的会议室ID。 |
| corpId | String | 所属企业corpId。 |
| deviceName | String | 设备名称。 |
| shareCode | String | 设备投屏码。 |
| deviceSn | String | 设备sn码。 |
| deviceMac | String | 设备mac地址。 |
| deviceType | String | 设备类型。   - touyingyi：视频会议设备 - meetingaccessory：设备控制器 |
| deviceServiceId | Integer | 设备注册serviceId。 |
| deviceModel | String | 设备型号。 |
| deviceStatus | String | 设备状态。   - idle：空闲 - projection：投屏中 - conf\_incoming：会议响铃中 - conf\_running： 会议中 - white\_board：使用白板中 - offline：离线 |
| controllers | Array | 设备控制器信息列表。 |
| deviceId | String | 控制器设备ID。 |
| deviceUnionId | String | 设备控制器unionId。 |
| openRoomId | String | 设备控制器绑定的会议室ID。 |
| corpId | String | 所属企业corpId。 |
| shareCode | String | 设备控制器投屏码。 |
| deviceSn | String | 设备控制器sn码。 |
| deviceType | String | 设备类型：   - touyingyi：视频会议设备 - meetingaccessory：设备控制器 |
| deviceServiceId | Integer | 设备控制器注册serviceId。 |
| deviceModel | String | 设备控制器型号。 |
| deviceName | String | 设备控制器名称。 |
| deviceStatus | String | 设备控制器状态。   - idle：空闲 - projection：投屏中 - conf\_incoming：会议响铃中 - conf\_running： 会议中 - white\_board：使用白板中 - offline：离线 |
| deviceMac | String | 设备控制器mac地址。 |
| creatorUnionId | String | 创建操作人。 |
| roomName | String | 所属会议室名称。 |
| firmwareVersion | String | 设备固件版本。 |
| softwareVersion | String | 设备软件版本。 |
| activeTime | Long | 设备激活时间。 |
| devNetType | String | 设备网络类型。 |
| devNetIp | String | 设备Ip。 |
| devWifiMac | String | 设备无线mac地址。 |
| devWireMac | String | 设备有线mac地址。 |
| devCamera | String | 摄像头型号。 |
| devMic | String | 麦克风型号。 |
| devVoice | String | 扬声器型号。 |
| devMirror | String | 镜像状态。 |
| devHdmi | String | HDMI输出状态。 |
| sipAccountName | String | sip账号。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "deviceId" : "1234",
    "deviceUnionId" : "lmvUxxxxx",
    "openRoomId" : "7263xxxxx",
    "corpId" : "ding99xxxxx",
    "deviceName" : "钉钉会议设备_xxxx",
    "shareCode" : "123456",
    "deviceSn" : "02caxxxxx",
    "deviceMac" : "14:85:7f:xx:xx:xx",
    "deviceType" : "touyingyi",
    "deviceServiceId" : 1204,
    "deviceModel" : "winbox",
    "deviceStatus" : "offline",
    "controllers" : [ {
      "deviceId" : "2345",
      "deviceUnionId" : "lmvUxxxxx",
      "openRoomId" : "7263xxxxx",
      "corpId" : "ding99xxxxx",
      "shareCode" : "234567",
      "deviceSn" : "02caxxxxx",
      "deviceType" : "touyingyi",
      "deviceServiceId" : 1190,
      "deviceModel" : "AILABS_S3_T1",
      "deviceName" : "会控平板_xxxx",
      "deviceStatus" : "white_board",
      "deviceMac" : "d8:2f:e6:xx:xx:xx"
    } ],
    "creatorUnionId" : "lPHhSZDLXXXXXXpBlC9lxLwiEiE",
    "roomName" : "测试会议室",
    "firmwareVersion" : "LMVXXX.20XX0818",
    "softwareVersion" : "7.14.1",
    "activeTime" : 1697198045000,
    "devNetType" : "net_wired",
    "devNetIp" : "127.0.0.10",
    "devWifiMac" : "d4:aa:ee:e8:4d:55",
    "devWireMac" : "d4:3a:ee:aa:45:85",
    "devCamera" : "Smart Camera",
    "devMic" : "Microphone (2- Built-in Audio)",
    "devVoice" : "Speaker (2- Built-in Audio)",
    "devMirror" : "false",
    "devHdmi" : "false",
    "sipAccountName" : "sip13492"
  }
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
