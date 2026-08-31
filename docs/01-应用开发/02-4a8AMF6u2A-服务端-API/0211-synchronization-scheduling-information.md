---
title: "配置考勤排班附加信息"
source_url: "https://open.dingtalk.com/document/development/synchronization-scheduling-information"
namespace: "development"
slug: "synchronization-scheduling-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤排班 > 配置考勤排班附加信息"
doc_id: "munK7AQDGM"
updated_at: "2026-06-15 10:56:03"
---

> Source: https://open.dingtalk.com/document/development/synchronization-scheduling-information
> Path: 应用开发 / 服务端 API / 考勤 > 考勤排班 > 配置考勤排班附加信息
> Updated: 2026-06-15 10:56:03

# 配置考勤排班附加信息

调用本接口配置排班维度信息，例如打卡位置、打卡 WiFi 等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/schedules/additionalInfo |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Pro.AttendanceGroup.Write-考勤组信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| scheduleInfos | Array | 是 | 排班信息列表。 |
| planId | Long | 是 | 待更新的排班ID，可调用[查询企业考勤排班详情](0209-interface-for-daily-full-query-of-attendance-scheduling-information.md)接口获取。 |
| wifiKeys | Array of String | 否 | 待添加的WIFI列表。 |
| positionKeys | Array of String | 否 | 待添加的位置列表。 |
| retainAttendanceCheck | Boolean | 否 | 是否保留考勤打卡设置。 |
| opUserId | String | 是 | 操作者的userId。 |

### 请求示例

HTTP

```
PUT /v1.0/attendance/schedules/additionalInfo HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1d97cxxx
Content-Type:application/json

{
  "scheduleInfos" : [ {
    "planId" : 12345,
    "wifiKeys" : [ "CA9B334xxx" ],
    "positionKeys" : [ "CA9B334xxx" ],
    "retainAttendanceCheck" : false
  } ],
  "opUserId" : "userid123"
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
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkattendance_1_0.models.SyncScheduleInfoHeaders syncScheduleInfoHeaders = new com.aliyun.dingtalkattendance_1_0.models.SyncScheduleInfoHeaders();
        syncScheduleInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.SyncScheduleInfoRequest.SyncScheduleInfoRequestScheduleInfos scheduleInfos0 = new com.aliyun.dingtalkattendance_1_0.models.SyncScheduleInfoRequest.SyncScheduleInfoRequestScheduleInfos()
                .setPlanId(12345L)
                .setWifiKeys(java.util.Arrays.asList(
                    "CA9B334xxx"
                ))
                .setPositionKeys(java.util.Arrays.asList(
                    "CA9B334xxx"
                ))
                .setRetainAttendanceCheck(false);
        com.aliyun.dingtalkattendance_1_0.models.SyncScheduleInfoRequest syncScheduleInfoRequest = new com.aliyun.dingtalkattendance_1_0.models.SyncScheduleInfoRequest()
                .setScheduleInfos(java.util.Arrays.asList(
                    scheduleInfos0
                ))
                .setOpUserId("userid123");
        try {
            client.syncScheduleInfoWithOptions(syncScheduleInfoRequest, syncScheduleInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        sync_schedule_info_headers = dingtalkattendance__1__0_models.SyncScheduleInfoHeaders()
        sync_schedule_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        schedule_infos_0 = dingtalkattendance__1__0_models.SyncScheduleInfoRequestScheduleInfos(
            plan_id=12345,
            wifi_keys=[
                'CA9B334xxx'
            ],
            position_keys=[
                'CA9B334xxx'
            ],
            retain_attendance_check=False
        )
        sync_schedule_info_request = dingtalkattendance__1__0_models.SyncScheduleInfoRequest(
            schedule_infos=[
                schedule_infos_0
            ],
            op_user_id='userid123'
        )
        try:
            client.sync_schedule_info_with_options(sync_schedule_info_request, sync_schedule_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sync_schedule_info_headers = dingtalkattendance__1__0_models.SyncScheduleInfoHeaders()
        sync_schedule_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        schedule_infos_0 = dingtalkattendance__1__0_models.SyncScheduleInfoRequestScheduleInfos(
            plan_id=12345,
            wifi_keys=[
                'CA9B334xxx'
            ],
            position_keys=[
                'CA9B334xxx'
            ],
            retain_attendance_check=False
        )
        sync_schedule_info_request = dingtalkattendance__1__0_models.SyncScheduleInfoRequest(
            schedule_infos=[
                schedule_infos_0
            ],
            op_user_id='userid123'
        )
        try:
            await client.sync_schedule_info_with_options_async(sync_schedule_info_request, sync_schedule_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\SyncScheduleInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\SyncScheduleInfoRequest\scheduleInfos;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\SyncScheduleInfoRequest;
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
        $syncScheduleInfoHeaders = new SyncScheduleInfoHeaders([]);
        $syncScheduleInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $scheduleInfos0 = new scheduleInfos([
            "planId" => 12345,
            "wifiKeys" => [
                "CA9B334xxx"
            ],
            "positionKeys" => [
                "CA9B334xxx"
            ],
            "retainAttendanceCheck" => false
        ]);
        $syncScheduleInfoRequest = new SyncScheduleInfoRequest([
            "scheduleInfos" => [
                $scheduleInfos0
            ],
            "opUserId" => "userid123"
        ]);
        try {
            $client->syncScheduleInfoWithOptions($syncScheduleInfoRequest, $syncScheduleInfoHeaders, new RuntimeOptions([]));
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
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  syncScheduleInfoHeaders := &dingtalkattendance_1_0.SyncScheduleInfoHeaders{}
  syncScheduleInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  scheduleInfos0 := &dingtalkattendance_1_0.SyncScheduleInfoRequestScheduleInfos{
    PlanId: tea.Int64(12345),
    WifiKeys: []*string{tea.String("CA9B334xxx")},
    PositionKeys: []*string{tea.String("CA9B334xxx")},
    RetainAttendanceCheck: tea.Bool(false),
  }
  syncScheduleInfoRequest := &dingtalkattendance_1_0.SyncScheduleInfoRequest{
    ScheduleInfos: []*dingtalkattendance_1_0.SyncScheduleInfoRequestScheduleInfos{scheduleInfos0},
    OpUserId: tea.String("userid123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SyncScheduleInfoWithOptions(syncScheduleInfoRequest, syncScheduleInfoHeaders, &util.RuntimeOptions{})
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
    let syncScheduleInfoHeaders = new $dingtalkattendance_1_0.SyncScheduleInfoHeaders({ });
    syncScheduleInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let scheduleInfos0 = new $dingtalkattendance_1_0.SyncScheduleInfoRequestScheduleInfos({
      planId: 12345,
      wifiKeys: [
        "CA9B334xxx"
      ],
      positionKeys: [
        "CA9B334xxx"
      ],
      retainAttendanceCheck: false,
    });
    let syncScheduleInfoRequest = new $dingtalkattendance_1_0.SyncScheduleInfoRequest({
      scheduleInfos: [
        scheduleInfos0
      ],
      opUserId: "userid123",
    });
    try {
      await client.syncScheduleInfoWithOptions(syncScheduleInfoRequest, syncScheduleInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoHeaders syncScheduleInfoHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoHeaders();
            syncScheduleInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoRequest.SyncScheduleInfoRequestScheduleInfos scheduleInfos0 = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoRequest.SyncScheduleInfoRequestScheduleInfos
            {
                PlanId = 12345,
                WifiKeys = new List<string>
                {
                    "CA9B334xxx"
                },
                PositionKeys = new List<string>
                {
                    "CA9B334xxx"
                },
                RetainAttendanceCheck = false,
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoRequest syncScheduleInfoRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoRequest
            {
                ScheduleInfos = new List<AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.SyncScheduleInfoRequest.SyncScheduleInfoRequestScheduleInfos>
                {
                    scheduleInfos0
                },
                OpUserId = "userid123",
            };
            try
            {
                client.SyncScheduleInfoWithOptions(syncScheduleInfoRequest, syncScheduleInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | service.error | 服务错误 | 服务错误 |
| 400 | service.invalidParam | 入参错误 | 入参错误 |
| 500 | system.error | 系统繁忙 | 系统繁忙 |
