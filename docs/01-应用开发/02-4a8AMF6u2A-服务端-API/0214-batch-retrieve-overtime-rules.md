---
title: "批量获取加班规则设置"
source_url: "https://open.dingtalk.com/document/development/batch-retrieve-overtime-rules"
namespace: "development"
slug: "batch-retrieve-overtime-rules"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤规则 > 批量获取加班规则设置"
doc_id: "pZoXVk6uHj"
updated_at: "2026-06-01 16:47:21"
---

> Source: https://open.dingtalk.com/document/development/batch-retrieve-overtime-rules
> Path: 应用开发 / 服务端 API / 考勤 > 考勤规则 > 批量获取加班规则设置
> Updated: 2026-06-01 16:47:21

# 批量获取加班规则设置

调用本接口，根据多个加班规则ID，批量获取加班规则设置详情。

## 接口调用说明

例如，企业考勤组内设置的加班规则是**以审批时间计算加班**，如下图所示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3885238471/p961095.png)调用本接口，获取**以审批时间计算加班**加班规则的设置详情信息，包括规则名称、加班计算方式等。 ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3885238471/p961092.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/overtimeSettings/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| overtimeSettingIds | Array of Long | 否 | 加班规则设置id，可调用[查询成员排班信息](0205-query-scheduling-for-a-day.md)接口获取，对应features内的overtimeSettingId字段。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/overtimeSettings/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1d96xxxx
Content-Type:application/json

{
  "overtimeSettingIds" : [ 12345678 ]
}
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
        GetOvertimeSettingHeaders getOvertimeSettingHeaders = new GetOvertimeSettingHeaders();
        getOvertimeSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetOvertimeSettingRequest getOvertimeSettingRequest = new GetOvertimeSettingRequest()
                .setOvertimeSettingIds(java.util.Arrays.asList(
                    12345678L
                ));
        try {
            client.getOvertimeSettingWithOptions(getOvertimeSettingRequest, getOvertimeSettingHeaders, new RuntimeOptions());
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
        get_overtime_setting_headers = dingtalkattendance__1__0_models.GetOvertimeSettingHeaders()
        get_overtime_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_overtime_setting_request = dingtalkattendance__1__0_models.GetOvertimeSettingRequest(
            overtime_setting_ids=[
                12345678
            ]
        )
        try:
            client.get_overtime_setting_with_options(get_overtime_setting_request, get_overtime_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_overtime_setting_headers = dingtalkattendance__1__0_models.GetOvertimeSettingHeaders()
        get_overtime_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_overtime_setting_request = dingtalkattendance__1__0_models.GetOvertimeSettingRequest(
            overtime_setting_ids=[
                12345678
            ]
        )
        try:
            await client.get_overtime_setting_with_options_async(get_overtime_setting_request, get_overtime_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetOvertimeSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetOvertimeSettingRequest;
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
        $getOvertimeSettingHeaders = new GetOvertimeSettingHeaders([]);
        $getOvertimeSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getOvertimeSettingRequest = new GetOvertimeSettingRequest([
            "overtimeSettingIds" => [
                12345678
            ]
        ]);
        try {
            $client->getOvertimeSettingWithOptions($getOvertimeSettingRequest, $getOvertimeSettingHeaders, new RuntimeOptions([]));
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

  getOvertimeSettingHeaders := &dingtalkattendance_1_0.GetOvertimeSettingHeaders{}
  getOvertimeSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getOvertimeSettingRequest := &dingtalkattendance_1_0.GetOvertimeSettingRequest{
    OvertimeSettingIds: []*int64{tea.Int(12345678)},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetOvertimeSettingWithOptions(getOvertimeSettingRequest, getOvertimeSettingHeaders, &util.RuntimeOptions{})
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
    let getOvertimeSettingHeaders = new $dingtalkattendance_1_0.GetOvertimeSettingHeaders({ });
    getOvertimeSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getOvertimeSettingRequest = new $dingtalkattendance_1_0.GetOvertimeSettingRequest({
      overtimeSettingIds: [
        12345678
      ],
    });
    try {
      await client.getOvertimeSettingWithOptions(getOvertimeSettingRequest, getOvertimeSettingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetOvertimeSettingHeaders getOvertimeSettingHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetOvertimeSettingHeaders();
            getOvertimeSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetOvertimeSettingRequest getOvertimeSettingRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetOvertimeSettingRequest
            {
                OvertimeSettingIds = new List<long?>
                {
                    12345678
                },
            };
            try
            {
                client.GetOvertimeSettingWithOptions(getOvertimeSettingRequest, getOvertimeSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

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
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::GetOvertimeSettingHeaders> getOvertimeSettingHeaders = make_shared<Alibabacloud_Dingtalkattendance_1_0::GetOvertimeSettingHeaders>();
  getOvertimeSettingHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::GetOvertimeSettingRequest> getOvertimeSettingRequest = make_shared<Alibabacloud_Dingtalkattendance_1_0::GetOvertimeSettingRequest>(map<string, boost::any>({
    {"overtimeSettingIds", boost::any(vector<long>({
      12345678
    }))}
  }));
  try {
    client->getOvertimeSettingWithOptions(getOvertimeSettingRequest, getOvertimeSettingHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Array | 加班设置详情列表。 |
| settingId | Long | 设置ID。 |
| name | String | 规则名称。 |
| default | Boolean | 是否默认。   - **true**：是 - **false**：不是 |
| durationSettings | Map<String, Object> | 加班规则日期类型列表。 |
|  | Object | 加班规则类型详情。 |
| calcType | Integer | 加班是否需要填写审批单，取值：   - **1**： 需要提交审批单 - **2**：无需提交审批单 - **3**： 不允许加班 |
| durationType | Integer | 计算方式，取值：   - **1**：按审批单时长计算 - **2**：按打卡时长计算。 |
| overtimeRedress | Boolean | 加班时长计为调休或加班费开关。 |
| settings | Map | 取值为**加班开始时间**和**最小加班时间**。 |
| overtimeRedressBy | String | 加班时长计为方式，取值：   - **vacation**：计为调休 - **charge**：计为加班费 - **manual**：员工自主选择 |
| vacationRate | Float | 调休时长计算比例。 |
| skipTime | String | 扣除休息时间，取值：   - **frame**： 按休息时段扣除 - **duration**：按加班时长扣除 |
| skipTimeByFrames | Array | 按休息时段扣除。  **[!NOTE]**    只有**skipTime**等于**frame**时，才有值。 |
| startTime | String | 开始时间，格式为`HH:mm`。 |
| endTime | String | 结束时间，格式为`HH:mm`。 |
| valid | Boolean | 是否生效。   - **true**：生效 - **false**：不生效 |
| skipTimeByDurations | Array | 按加班时长扣除。  **[!NOTE]**    只有**skipTime**等于**duration**才有值。 |
| duration | Long | 每天加班满时长，单位：秒。 |
| minus | Long | 扣除时长，单位：秒。 |
| holidayPlanOvertimeRedress | Boolean | 休息日或节假日排班加班时长计为调休或加班费开关。 |
| holidayPlanOvertimeRedressBy | String | 休息日或节假日排班加班时长计为方式，取值：   - **vacation**：计为调休 - **charge**：计为加班费 - **manual**：员工自主选择 |
| holidayPlanVacationRate | Float | 休息日或节假日排班调休时长计算比例。 |
| warningSettings | Array | 预警设置部分。 |
| time | String | 预警类型，取值：   - **everyday**： 每日 - **everyweek**：每周 - **everymonth**：每月 |
| threshold | Long | 提醒阈值。 |
| action | String | 取值为**风险预警**或**最大加班时间**。 |
| stepType | Integer | 加班时长单位。 |
| stepValue | Float | 加班时长是否取整，单位：小时 ，取值：   - **1**：不取整 - **其他值**：按步长值向下取整及步长值 |
| workMinutesPerDay | Integer | 日折算时长 单位：分钟。 |
| overtimeDivisions | Array | 时间分割规则。 |
| previousDayType | String | 前一日类型。 |
| nextDayType | String | 后一日类型。 |
| timeSplitPoint | String | 分割时间点。 |
| id | Long | 历史加班规则设置ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "settingId" : 841251521,
    "name" : "加班规则名称测试",
    "default" : false,
    "durationSettings" : {
      "key" : {
        "calcType" : 1,
        "durationType" : 2,
        "overtimeRedress" : true,
        "overtimeRedressBy" : "charge",
        "vacationRate" : 1,
        "skipTime" : "frame",
        "skipTimeByFrames" : [ {
          "startTime" : "12:00",
          "endTime" : "13:00",
          "valid" : true
        } ],
        "skipTimeByDurations" : [ {
          "duration" : 18000,
          "minus" : 3600
        } ],
        "holidayPlanOvertimeRedress" : true,
        "holidayPlanOvertimeRedressBy" : "vacation",
        "holidayPlanVacationRate" : 1
      }
    },
    "warningSettings" : [ {
      "time" : "everymonth",
      "threshold" : 129600,
      "action" : "alert"
    } ],
    "stepType" : 0,
    "stepValue" : 1,
    "workMinutesPerDay" : 480,
    "overtimeDivisions" : [ {
      "previousDayType" : "workDay",
      "nextDayType" : "restDay",
      "timeSplitPoint" : "00:00"
    } ],
    "id" : 12345678
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidSize | 不合法的大小 | overtimeSettingIds不合法的大小 |
| 400 | invalidParameter | 参数错误 | overtimeSettingIds参数异常 |
| 500 | systemError | 系统异常 | 系统异常 |
