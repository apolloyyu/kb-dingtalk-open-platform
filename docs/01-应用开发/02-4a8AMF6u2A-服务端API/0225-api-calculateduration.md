---
title: "预计算时长"
source_url: "https://open.dingtalk.com/document/development/api-calculateduration"
namespace: "development"
slug: "api-calculateduration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假勤审批 > 预计算时长"
doc_id: "aK9WEUzrWH"
updated_at: "2026-06-01 16:53:34"
---

> Source: https://open.dingtalk.com/document/development/api-calculateduration
> Path: 应用开发 / 服务端API / 考勤 > 假勤审批 > 预计算时长
> Updated: 2026-06-01 16:53:34

# 预计算时长

调用本接口，根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。

## 接口调用说明

例如，企业某员工11月2日排班（上班时间09:00，下班时间18:00），11月3日排休。

该员工计划需要请假，请假开始时间是11月02日的09:00:00，结束是11月3日的18:00:00，那么调用本接口可获取这个请假时长范围内，该员工预计请假的时长只有一天。

> **[!NOTE]**
>
> - 请假日期未加入考勤组或未排班的员工请假时，请假时长按照默认考勤时间计算。
> - 默认考勤时间设置路径：**【手机端钉钉】>【工作台】>【考勤打卡】>【设置】>【更多设置】>【假勤审批】>【默认考勤时间】**，说明如下：
>
>   例如，企业某员工11月2日排班（上班时间09:00，下班时间18:00），11月3日未排班。默认班次为（8:30-17:30）该员工计划需要请假，请假开始时间是11月02日的09:00:00，结束是11月3日的18:00:00，那么调用本接口可获取这个请假时长范围内，该员工预计请假的时长2天。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/approvals/durations/calculate |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 用户userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizType | Long | 否 | 审批单类型：   - 1：加班 - 2：出差 - 3：请假 |
| fromTime | String | 否 | 开始时间。开始时间不能早于当前时间前31天。支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 |
| toTime | String | 否 | 结束时间。   - biz\_type为1时，结束时间减去开始时间不能超过1天。 - biz\_type为2或3时，结束时间减去开始时间的天数不能超过31天。   支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 |
| durationUnit | String | 否 | 时长单位，支持格式如下：   - day - halfDay - hour：biz\_type为1时仅支持hour。   时间格式必须与时长单位对应：   - 2019-08-15对应day - 2019-08-15 AM对应halfDay - 2019-08-15 12:43对应hour |
| calculateModel | Long | 否 | 计算方法：   - 0：按自然日计算 - 1：按工作日计算 |
| leaveCode | String | 否 | 假期规则唯一标识。选填 仅支持bizType=3 请假时传不为空，可以支持根据假期类型设置的取整规则进行时长取整。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/approvals/durations/calculate?userId=manager123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:234sad32qr4q32xxx
Content-Type:application/json

{
  "bizType" : 3,
  "fromTime" : "2019-08-15",
  "toTime" : "2019-08-15",
  "durationUnit" : "day",
  "calculateModel" : 1,
  "leaveCode" : "e2dsad-34dfa-2vas23da"
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
        com.aliyun.dingtalkattendance_1_0.models.CalculateDurationHeaders calculateDurationHeaders = new com.aliyun.dingtalkattendance_1_0.models.CalculateDurationHeaders();
        calculateDurationHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.CalculateDurationRequest calculateDurationRequest = new com.aliyun.dingtalkattendance_1_0.models.CalculateDurationRequest()
                .setUserId("manager123")
                .setBizType(3L)
                .setFromTime("2019-08-15")
                .setToTime("2019-08-15")
                .setDurationUnit("day")
                .setCalculateModel(1L)
                .setLeaveCode("e2dsad-34dfa-2vas23da");
        try {
            client.calculateDurationWithOptions(calculateDurationRequest, calculateDurationHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        calculate_duration_headers = dingtalkattendance__1__0_models.CalculateDurationHeaders()
        calculate_duration_headers.x_acs_dingtalk_access_token = '<your access token>'
        calculate_duration_request = dingtalkattendance__1__0_models.CalculateDurationRequest(
            user_id='manager123',
            biz_type=3,
            from_time='2019-08-15',
            to_time='2019-08-15',
            duration_unit='day',
            calculate_model=1,
            leave_code='e2dsad-34dfa-2vas23da'
        )
        try:
            client.calculate_duration_with_options(calculate_duration_request, calculate_duration_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        calculate_duration_headers = dingtalkattendance__1__0_models.CalculateDurationHeaders()
        calculate_duration_headers.x_acs_dingtalk_access_token = '<your access token>'
        calculate_duration_request = dingtalkattendance__1__0_models.CalculateDurationRequest(
            user_id='manager123',
            biz_type=3,
            from_time='2019-08-15',
            to_time='2019-08-15',
            duration_unit='day',
            calculate_model=1,
            leave_code='e2dsad-34dfa-2vas23da'
        )
        try:
            await client.calculate_duration_with_options_async(calculate_duration_request, calculate_duration_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CalculateDurationHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CalculateDurationRequest;
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
        $calculateDurationHeaders = new CalculateDurationHeaders([]);
        $calculateDurationHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $calculateDurationRequest = new CalculateDurationRequest([
            "userId" => "manager123",
            "bizType" => 3,
            "fromTime" => "2019-08-15",
            "toTime" => "2019-08-15",
            "durationUnit" => "day",
            "calculateModel" => 1,
            "leaveCode" => "e2dsad-34dfa-2vas23da"
        ]);
        try {
            $client->calculateDurationWithOptions($calculateDurationRequest, $calculateDurationHeaders, new RuntimeOptions([]));
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

  calculateDurationHeaders := &dingtalkattendance_1_0.CalculateDurationHeaders{}
  calculateDurationHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  calculateDurationRequest := &dingtalkattendance_1_0.CalculateDurationRequest{
    UserId: tea.String("manager123"),
    BizType: tea.Int64(3),
    FromTime: tea.String("2019-08-15"),
    ToTime: tea.String("2019-08-15"),
    DurationUnit: tea.String("day"),
    CalculateModel: tea.Int64(1),
    LeaveCode: tea.String("e2dsad-34dfa-2vas23da"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CalculateDurationWithOptions(calculateDurationRequest, calculateDurationHeaders, &util.RuntimeOptions{})
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
    let calculateDurationHeaders = new $dingtalkattendance_1_0.CalculateDurationHeaders({ });
    calculateDurationHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let calculateDurationRequest = new $dingtalkattendance_1_0.CalculateDurationRequest({
      userId: "manager123",
      bizType: 3,
      fromTime: "2019-08-15",
      toTime: "2019-08-15",
      durationUnit: "day",
      calculateModel: 1,
      leaveCode: "e2dsad-34dfa-2vas23da",
    });
    try {
      await client.calculateDurationWithOptions(calculateDurationRequest, calculateDurationHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CalculateDurationHeaders calculateDurationHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CalculateDurationHeaders();
            calculateDurationHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CalculateDurationRequest calculateDurationRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CalculateDurationRequest
            {
                UserId = "manager123",
                BizType = 3,
                FromTime = "2019-08-15",
                ToTime = "2019-08-15",
                DurationUnit = "day",
                CalculateModel = 1,
                LeaveCode = "e2dsad-34dfa-2vas23da",
            };
            try
            {
                client.CalculateDurationWithOptions(calculateDurationRequest, calculateDurationHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| duration | double | 总时长，该字段的单位与本企业内对应审批单设置的单位一致。 |
| durationDetail | Array | 详细信息。 |
| date | String | 日期。 |
| duration | double | 每日时长，该字段的单位与本企业内对应审批单设置的单位一致。 |
| success | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "duration" : 2,
    "durationDetail" : [ {
      "date" : "2019-08-15",
      "duration" : 1.6
    } ]
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | illegalCalculateType | 不合法的时长计算模式 | 不合法的时长计算模式 |
| 400 | illegalDurationUnit | 不合法的时长单位 | 不合法的时长单位 |
| 400 | illegalApproveType | 不合法的审批类型 | 不合法的审批类型 |
| 400 | invalidRequestParams | 参数错误（请根据文档检查对应参数） | 参数错误（请根据文档检查对应参数） |
| 400 | illegalOvertimeDurationUnit | 不合法的加班时长单位（加班仅支持按小时） | 不合法的加班时长单位（加班仅支持按小时） |
| 400 | illegalDateTypeForHalfDay | 不合法的开始结束时间格式forDURATION\_UNIT为半天 | 不合法的开始结束时间格式forDURATION\_UNIT为半天 |
| 400 | beginDateCannotAfterEndDate | 开始时间不能晚于结束时间 | 开始时间不能晚于结束时间 |
| 400 | durationTooLong | 开始结束时间跨度过大 | 开始结束时间跨度过大 |
| 400 | dateTooEarly | 时间不能在指定天数之前 | 时间不能在指定天数之前 |
| 400 | overtimeDurationTooLong | 加班时长过长 | 加班时长过长 |
| 400 | systemError | 系统错误 | 系统错误 |
