---
title: "通知审批通过"
source_url: "https://open.dingtalk.com/document/development/api-processapprovefinish"
namespace: "development"
slug: "api-processapprovefinish"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假勤审批 > 通知审批通过"
doc_id: "Cyq6WFJlau"
updated_at: "2026-06-02 09:24:51"
---

> Source: https://open.dingtalk.com/document/development/api-processapprovefinish
> Path: 应用开发 / 服务端API / 考勤 > 假勤审批 > 通知审批通过
> Updated: 2026-06-02 09:24:51

# 通知审批通过

通过本接口，通知审批通过，支持加班、请假、外出和出差类型。

## 接口调用说明

例如，员工今日排班是8：00-18：00，在企业自有审批系统提交了请假，审批通过后通过本接口通知钉钉考勤，今天该员工无需打卡，不会被记为旷工，状态会显示为请假。 例如，员工小钉在11月15日未执行打卡，考勤统计中显示如下图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1943630871/p1075898.png)

调用本接口，通知审批通过，可实现修改员工小钉在11月15日的考勤为请假、出差或者加班，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1943630871/p1075899.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/approvals/finish |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过以下方式获取：   - 企业内部应用可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 员工的userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| topCalculateApproveDurationParam | Object | 否 | 时长相关入参。 |
| bizType | Long | 否 | 审批单类型，可取值：   - **1**：加班 - **2**：出差、外出 - **3**：请假 |
| fromTime | String | 否 | 开始时间。开始时间不能早于当前时间前31天。 支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 |
| toTime | String | 否 | 结束时间。 支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43        - 结束时间不能早于开始时间； - 时间跨度不能超过360天； - 结束时间减去开始时间的天数不能超过31天； - `biz_type`为1时，结束时间减去开始时间的天数不能超过1天。 |
| durationUnit | String | 否 | 时长单位，支持格式如下：   - **day** - **halfDay** - **hour**：`biz_type`为1时仅支持hour。   时间格式必须与时长单位对应：   - 2019-08-15对应day - 2019-08-15 AM对应halfDay - 2019-08-15 12:43对应hour |
| calculateModel | Long | 否 | 计算方法：   - **0**：按自然日计算 - **1**：按工作日计算 |
| leaveCode | String | 否 | 假期规则唯一标识。选填。      仅支持`bizType=3`请假时传不为空，可以支持根据假期类型设置的取整规则进行时长取整。 |
| tagName | String | 否 | 审批单类型名称，最大长度20个字符，支持类型：请假、出差、外出、加班。 |
| subType | String | 否 | 子类型名称，最大长度64个字符。      审批单类型biz\_type=3时，该参数必传。 |
| approveId | String | 否 | 审批单ID，最大长度100个字符，自定义值。      第三方企业应用需要自行保存，通知审批撤销时需要使用参数。approveId不变的情况下再次调用本接口是更新操作。 |
| jumpUrl | String | 否 | 审批单跳转地址，最大长度200个字符。      第三方企业应用在考勤统计页面点击会根据该地址进行跳转，可传对应的审批单详情地址。 |
| overtimeDuration | String | 否 | biz\_type为1时必传，加班时长单位小时。 |
| overTimeToMore | Long | 否 | biz\_type为1时必传：   - **1**：加班转调休 - **2**：加班转工资 |

### 请求示例

HTTP

```
POST /v1.0/attendance/approvals/finish?userId=manager123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:234adfw423xxx
Content-Type:application/json

{
  "topCalculateApproveDurationParam" : {
    "bizType" : 3,
    "fromTime" : "2019-08-15",
    "toTime" : "2019-08-15",
    "durationUnit" : "day",
    "calculateModel" : 1,
    "leaveCode" : "3afdsf-143dsadw3-ad23"
  },
  "tagName" : "请假",
  "subType" : "年假",
  "approveId" : "1234abcd",
  "dingtalkApproveId" : "https://open.dingtalk.com/",
  "jumpUrl" : "https://open.dingtalk.com/",
  "overtimeDuration" : "1.07",
  "overTimeToMore" : 1
}
```

Java

```
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
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishHeaders processApproveFinishHeaders = new com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishHeaders();
        processApproveFinishHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishRequest.ProcessApproveFinishRequestTopCalculateApproveDurationParam topCalculateApproveDurationParam = new com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishRequest.ProcessApproveFinishRequestTopCalculateApproveDurationParam()
                .setBizType(3L)
                .setFromTime("2019-08-15")
                .setToTime("2019-08-15")
                .setDurationUnit("day")
                .setCalculateModel(1L)
                .setLeaveCode("3afdsf-143dsadw3-ad23");
        com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishRequest processApproveFinishRequest = new com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishRequest()
                .setUserId("manager123")
                .setTopCalculateApproveDurationParam(topCalculateApproveDurationParam)
                .setTagName("请假")
                .setSubType("年假")
                .setApproveId("1234abcd")
                .setJumpUrl("https://open.dingtalk.com/")
                .setOvertimeDuration("1.07")
                .setOverTimeToMore(1L);
        try {
            client.processApproveFinishWithOptions(processApproveFinishRequest, processApproveFinishHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

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
        process_approve_finish_headers = dingtalkattendance__1__0_models.ProcessApproveFinishHeaders()
        process_approve_finish_headers.x_acs_dingtalk_access_token = '<your access token>'
        top_calculate_approve_duration_param = dingtalkattendance__1__0_models.ProcessApproveFinishRequestTopCalculateApproveDurationParam(
            biz_type=3,
            from_time='2019-08-15',
            to_time='2019-08-15',
            duration_unit='day',
            calculate_model=1,
            leave_code='3afdsf-143dsadw3-ad23'
        )
        process_approve_finish_request = dingtalkattendance__1__0_models.ProcessApproveFinishRequest(
            user_id='manager123',
            top_calculate_approve_duration_param=top_calculate_approve_duration_param,
            tag_name='请假',
            sub_type='年假',
            approve_id='1234abcd',
            jump_url='https://open.dingtalk.com/',
            overtime_duration='1.07',
            over_time_to_more=1
        )
        try:
            client.process_approve_finish_with_options(process_approve_finish_request, process_approve_finish_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        process_approve_finish_headers = dingtalkattendance__1__0_models.ProcessApproveFinishHeaders()
        process_approve_finish_headers.x_acs_dingtalk_access_token = '<your access token>'
        top_calculate_approve_duration_param = dingtalkattendance__1__0_models.ProcessApproveFinishRequestTopCalculateApproveDurationParam(
            biz_type=3,
            from_time='2019-08-15',
            to_time='2019-08-15',
            duration_unit='day',
            calculate_model=1,
            leave_code='3afdsf-143dsadw3-ad23'
        )
        process_approve_finish_request = dingtalkattendance__1__0_models.ProcessApproveFinishRequest(
            user_id='manager123',
            top_calculate_approve_duration_param=top_calculate_approve_duration_param,
            tag_name='请假',
            sub_type='年假',
            approve_id='1234abcd',
            jump_url='https://open.dingtalk.com/',
            overtime_duration='1.07',
            over_time_to_more=1
        )
        try:
            await client.process_approve_finish_with_options_async(process_approve_finish_request, process_approve_finish_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\ProcessApproveFinishHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\ProcessApproveFinishRequest\topCalculateApproveDurationParam;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\ProcessApproveFinishRequest;
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
        $processApproveFinishHeaders = new ProcessApproveFinishHeaders([]);
        $processApproveFinishHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $topCalculateApproveDurationParam = new topCalculateApproveDurationParam([
            "bizType" => 3,
            "fromTime" => "2019-08-15",
            "toTime" => "2019-08-15",
            "durationUnit" => "day",
            "calculateModel" => 1,
            "leaveCode" => "3afdsf-143dsadw3-ad23"
        ]);
        $processApproveFinishRequest = new ProcessApproveFinishRequest([
            "userId" => "manager123",
            "topCalculateApproveDurationParam" => $topCalculateApproveDurationParam,
            "tagName" => "请假",
            "subType" => "年假",
            "approveId" => "1234abcd",
            "jumpUrl" => "https://open.dingtalk.com/",
            "overtimeDuration" => "1.07",
            "overTimeToMore" => 1
        ]);
        try {
            $client->processApproveFinishWithOptions($processApproveFinishRequest, $processApproveFinishHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
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

  processApproveFinishHeaders := &dingtalkattendance_1_0.ProcessApproveFinishHeaders{}
  processApproveFinishHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  topCalculateApproveDurationParam := &dingtalkattendance_1_0.ProcessApproveFinishRequestTopCalculateApproveDurationParam{
    BizType: tea.Int64(3),
    FromTime: tea.String("2019-08-15"),
    ToTime: tea.String("2019-08-15"),
    DurationUnit: tea.String("day"),
    CalculateModel: tea.Int64(1),
    LeaveCode: tea.String("3afdsf-143dsadw3-ad23"),
  }
  processApproveFinishRequest := &dingtalkattendance_1_0.ProcessApproveFinishRequest{
    UserId: tea.String("manager123"),
    TopCalculateApproveDurationParam: topCalculateApproveDurationParam,
    TagName: tea.String("请假"),
    SubType: tea.String("年假"),
    ApproveId: tea.String("1234abcd"),
    JumpUrl: tea.String("https://open.dingtalk.com/"),
    OvertimeDuration: tea.String("1.07"),
    OverTimeToMore: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ProcessApproveFinishWithOptions(processApproveFinishRequest, processApproveFinishHeaders, &util.RuntimeOptions{})
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
const dingtalkattendance_1_0 = require('@alicloud/dingtalk/attendance_1_0');
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
    return new dingtalkattendance_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let processApproveFinishHeaders = new dingtalkattendance_1_0.ProcessApproveFinishHeaders({ });
    processApproveFinishHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let topCalculateApproveDurationParam = new dingtalkattendance_1_0.ProcessApproveFinishRequestTopCalculateApproveDurationParam({
      bizType: 3,
      fromTime: '2019-08-15',
      toTime: '2019-08-15',
      durationUnit: 'day',
      calculateModel: 1,
      leaveCode: '3afdsf-143dsadw3-ad23',
    });
    let processApproveFinishRequest = new dingtalkattendance_1_0.ProcessApproveFinishRequest({
      userId: 'manager123',
      topCalculateApproveDurationParam: topCalculateApproveDurationParam,
      tagName: '请假',
      subType: '年假',
      approveId: '1234abcd',
      jumpUrl: 'https://open.dingtalk.com/',
      overtimeDuration: '1.07',
      overTimeToMore: 1,
    });
    try {
      await client.processApproveFinishWithOptions(processApproveFinishRequest, processApproveFinishHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.ProcessApproveFinishHeaders processApproveFinishHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.ProcessApproveFinishHeaders();
            processApproveFinishHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.ProcessApproveFinishRequest.ProcessApproveFinishRequestTopCalculateApproveDurationParam topCalculateApproveDurationParam = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.ProcessApproveFinishRequest.ProcessApproveFinishRequestTopCalculateApproveDurationParam
            {
                BizType = 3,
                FromTime = "2019-08-15",
                ToTime = "2019-08-15",
                DurationUnit = "day",
                CalculateModel = 1,
                LeaveCode = "3afdsf-143dsadw3-ad23",
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.ProcessApproveFinishRequest processApproveFinishRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.ProcessApproveFinishRequest
            {
                UserId = "manager123",
                TopCalculateApproveDurationParam = topCalculateApproveDurationParam,
                TagName = "请假",
                SubType = "年假",
                ApproveId = "1234abcd",
                JumpUrl = "https://open.dingtalk.com/",
                OvertimeDuration = "1.07",
                OverTimeToMore = 1,
            };
            try
            {
                client.ProcessApproveFinishWithOptions(processApproveFinishRequest, processApproveFinishHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| date | String | 审批通过日期。 |
| duration | double | 每日时长。 |
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
      "duration" : 1
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
| 400 | repeatApprovesOverLimit | 时间存在重复的审批单写入超过限制 | 时间存在重复的审批单写入超过限制 |
| 400 | systemError | 系统错误 | 系统错误 |
