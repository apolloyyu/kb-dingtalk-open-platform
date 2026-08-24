---
title: "添加假期规则"
source_url: "https://open.dingtalk.com/document/development/add-holiday-rules"
namespace: "development"
slug: "add-holiday-rules"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 添加假期规则"
doc_id: "ISJffNAr7n"
updated_at: "2026-06-01 16:58:42"
---

> Source: https://open.dingtalk.com/document/development/add-holiday-rules
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 添加假期规则
> Updated: 2026-06-01 16:58:42

# 添加假期规则

调用本接口，新建一个假期规则。

## 接口调用说明

调用本接口创建的假期规则主要有两类：

- 普通假期规则，例如事假、婚假等，此类假期规则可以修改余额，调用本接口创建普通假期后，余额默认是0，需要再调用[初始化假期余额](0236-initialize-holiday-balance.md)接口，初始化假期余额。
- 调休假期规则，调用本接口添加的调休假期，默认余额规则是**加班时长自动计入调休余额**，无需调用初始化余额接口。 ![图示](https://img.alicdn.com/imgextra/i4/O1CN01w35q5j1b14xOtYzDs_!!6000000003404-2-tps-1532-718.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/leaves/types |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_holiday\_manage-钉钉假期管理的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUserId | String | 是 | 管理员userId，同时该管理员需拥有OA审批应用的管理权限。  **[!NOTE]**  如果不满足条件，接口会报错，提示部门的管理员不存在。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| leaveName | String | 是 | 假期规则名称。 |
| leaveViewUnit | String | 是 | 请假时长单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| bizType | String | 是 | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休   **[!NOTE]**    一个企业只能存在一个加班转调休的假期规则。 |
| naturalDayLeave | Boolean | 是 | 是否按照自然日统计请假时长。   - **true**：是 - **false**：否   **[!NOTE]**    例如，员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。   - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者法定节假日。 |
| hoursInPerDay | Long | 是 | 每天折算的工作时长，为参数值的百分之一。  **[!NOTE]**    例如，某企业员工所在的班次工时是8小时，则该参数值为8\*100=800。 |
| extras | String | 否 | 调休假有效期规则。   - **validity\_type**：有效类型    - **absolute\_time**：绝对时间   - **relative\_time**：相对时间 - **validity\_value**：延长日期    - 当validity\_type为**absolute\_time**，该值不为空且满足“yy-mm”格式。   - 当validity\_type为**relative\_time**，该值为大于1的整数。   **[!NOTE]**  假期类型biz\_type值为**lieu\_leave**时，该参数必传。 |
| paidLeave | Boolean | 否 | 是否带薪假。 |
| paidLeave | Boolean | 否 | 是否带薪假。 |
| visibilityRules | Array | 否 | 适用范围规则列表，不传默认为全公司。 |
| visible | Array of String | 否 | 适用范围内数据列表。   - 当type=staff时，传员工userId列表。 - 当type=dept时，传部门id列表。 - 当type=label时，传角色id列表。 |
| type | String | 否 | 适用范围规则类型。   - **dept**：部门 - **staff**：员工 - **label**：角色 |
| whenCanLeave | String | 否 | 何时可请假。  **[!NOTE]**  第三方企业应用专属字段。   - **entry** 表示入职可用。 - **formal** 表示转正可用。 |
| leaveTimeCeilMinUnit | String | 否 | 请假时长向上取整时的最小时长单位。  **[!NOTE]**  第三方企业应用专属字段。   - **hour** 小时，不足1小时按照1小时计算 - **halfHour** 半小时，不足半小时按照半小时计算 |
| leaveTimeCeil | Boolean | 否 | 请假时长是否向上取整。  **[!NOTE]**  第三方企业应用专属字段。 |
| minLeaveHour | double | 否 | 最小请假时长（请假单位为hour时生效），请假时长小于该值时自动取该值。  **[!NOTE]**  第三方企业应用专属字段。 |
| submitTimeRule | Object | 否 | 限时提交规则。 |
| timeValue | Long | 否 | 限制值。   - 当timeUnit为day时，有效值范围是0至30天。 - 当timeUnit为hour时，有效值范围是0至24小时。 |
| timeUnit | String | 否 | 时间单位。   - **day**：天 - **hour**：小时 |
| timeType | String | 否 | 限制类型。   - **before**：提前 - **after**：补交 |
| enableTimeLimit | Boolean | 否 | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| leaveCertificate | Object | 否 | 请假证明。 |
| unit | String | 否 | 需提供请假证明时长单位。   - **hour**：小时 - **day**：天 |
| duration | double | 否 | 超过多长时间需提供请假证明。   - 如果unit值为day，表示请假超过一天，需要提供请假证明。 - 如果unit值为hour，表示请假超过一小时，需要提供请假证明。   **[!NOTE]**  提交请假超过设置时间，审批单会自动出现请假证明填写项。 |
| enable | Boolean | 否 | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| promptInformation | String | 否 | 请假提示文案。 |
| maxLeaveTime | Long | 否 | 最大请假时长（请假单位为hour或day时生效）。  **[!NOTE]**  第三方企业应用专属字段。 |
| leaveHourCeil | String | 否 | 请假时长是否向上取整：  **[!NOTE]**  第三方企业应用专属字段。   - **up** 向上取整 - **down** 向下取整 - **none** 不取整 |
| freedomLeave | Boolean | 否 | 不需要余额控制的请假类型（如事假）。  **[!NOTE]**  第三方企业应用专属字段。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/leaves/types?opUserId=user01 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1d97cxxx
Content-Type:application/json

{
  "leaveName" : "年假",
  "leaveViewUnit" : "day",
  "bizType" : "general_leave",
  "naturalDayLeave" : true,
  "hoursInPerDay" : 1000,
  "extras" : "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
  "paidLeave" : true,
  "visibilityRules" : [ {
    "visible" : [ "user01" ],
    "type" : "staff"
  } ],
  "whenCanLeave" : "entry",
  "leaveTimeCeilMinUnit" : "hour",
  "leaveTimeCeil" : false,
  "minLeaveHour" : 1.0,
  "submitTimeRule" : {
    "timeValue" : 2,
    "timeUnit" : "day",
    "timeType" : "before",
    "enableTimeLimit" : true
  },
  "leaveCertificate" : {
    "unit" : "hour",
    "duration" : 1.0,
    "enable" : false,
    "promptInformation" : "请假文案"
  },
  "maxLeaveTime" : 3,
  "leaveHourCeil" : "up",
  "freedomLeave" : true
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
        com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeHeaders addLeaveTypeHeaders = new com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeHeaders();
        addLeaveTypeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest.AddLeaveTypeRequestLeaveCertificate leaveCertificate = new com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest.AddLeaveTypeRequestLeaveCertificate()
                .setUnit("hour")
                .setDuration(1D)
                .setEnable(false)
                .setPromptInformation("请假文案");
        com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest.AddLeaveTypeRequestSubmitTimeRule submitTimeRule = new com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest.AddLeaveTypeRequestSubmitTimeRule()
                .setTimeValue(2L)
                .setTimeUnit("day")
                .setTimeType("before")
                .setEnableTimeLimit(true);
        com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest.AddLeaveTypeRequestVisibilityRules visibilityRules0 = new com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest.AddLeaveTypeRequestVisibilityRules()
                .setVisible(java.util.Arrays.asList(
                    "user01"
                ))
                .setType("staff");
        com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest addLeaveTypeRequest = new com.aliyun.dingtalkattendance_1_0.models.AddLeaveTypeRequest()
                .setOpUserId("user01")
                .setLeaveName("年假")
                .setLeaveViewUnit("day")
                .setBizType("general_leave")
                .setNaturalDayLeave(true)
                .setHoursInPerDay(1000L)
                .setExtras("{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}")
                .setPaidLeave(true)
                .setVisibilityRules(java.util.Arrays.asList(
                    visibilityRules0
                ))
                .setWhenCanLeave("entry")
                .setLeaveTimeCeilMinUnit("hour")
                .setLeaveTimeCeil(false)
                .setMinLeaveHour(1D)
                .setSubmitTimeRule(submitTimeRule)
                .setLeaveCertificate(leaveCertificate)
                .setMaxLeaveTime(3L)
                .setLeaveHourCeil("up")
                .setFreedomLeave(true);
        try {
            client.addLeaveTypeWithOptions(addLeaveTypeRequest, addLeaveTypeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_leave_type_headers = dingtalkattendance__1__0_models.AddLeaveTypeHeaders()
        add_leave_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        leave_certificate = dingtalkattendance__1__0_models.AddLeaveTypeRequestLeaveCertificate(
            unit='hour',
            duration=1,
            enable=False,
            prompt_information='请假文案'
        )
        submit_time_rule = dingtalkattendance__1__0_models.AddLeaveTypeRequestSubmitTimeRule(
            time_value=2,
            time_unit='day',
            time_type='before',
            enable_time_limit=True
        )
        visibility_rules_0 = dingtalkattendance__1__0_models.AddLeaveTypeRequestVisibilityRules(
            visible=[
                'user01'
            ],
            type='staff'
        )
        add_leave_type_request = dingtalkattendance__1__0_models.AddLeaveTypeRequest(
            op_user_id='user01',
            leave_name='年假',
            leave_view_unit='day',
            biz_type='general_leave',
            natural_day_leave=True,
            hours_in_per_day=1000,
            extras='{"validity_type":"absolute_time","validity_value":"12-31"}',
            paid_leave=True,
            visibility_rules=[
                visibility_rules_0
            ],
            when_can_leave='entry',
            leave_time_ceil_min_unit='hour',
            leave_time_ceil=False,
            min_leave_hour=1,
            submit_time_rule=submit_time_rule,
            leave_certificate=leave_certificate,
            max_leave_time=3,
            leave_hour_ceil='up',
            freedom_leave=True
        )
        try:
            client.add_leave_type_with_options(add_leave_type_request, add_leave_type_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_leave_type_headers = dingtalkattendance__1__0_models.AddLeaveTypeHeaders()
        add_leave_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        leave_certificate = dingtalkattendance__1__0_models.AddLeaveTypeRequestLeaveCertificate(
            unit='hour',
            duration=1,
            enable=False,
            prompt_information='请假文案'
        )
        submit_time_rule = dingtalkattendance__1__0_models.AddLeaveTypeRequestSubmitTimeRule(
            time_value=2,
            time_unit='day',
            time_type='before',
            enable_time_limit=True
        )
        visibility_rules_0 = dingtalkattendance__1__0_models.AddLeaveTypeRequestVisibilityRules(
            visible=[
                'user01'
            ],
            type='staff'
        )
        add_leave_type_request = dingtalkattendance__1__0_models.AddLeaveTypeRequest(
            op_user_id='user01',
            leave_name='年假',
            leave_view_unit='day',
            biz_type='general_leave',
            natural_day_leave=True,
            hours_in_per_day=1000,
            extras='{"validity_type":"absolute_time","validity_value":"12-31"}',
            paid_leave=True,
            visibility_rules=[
                visibility_rules_0
            ],
            when_can_leave='entry',
            leave_time_ceil_min_unit='hour',
            leave_time_ceil=False,
            min_leave_hour=1,
            submit_time_rule=submit_time_rule,
            leave_certificate=leave_certificate,
            max_leave_time=3,
            leave_hour_ceil='up',
            freedom_leave=True
        )
        try:
            await client.add_leave_type_with_options_async(add_leave_type_request, add_leave_type_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\AddLeaveTypeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\AddLeaveTypeRequest\leaveCertificate;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\AddLeaveTypeRequest\submitTimeRule;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\AddLeaveTypeRequest\visibilityRules;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\AddLeaveTypeRequest;
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
        $addLeaveTypeHeaders = new AddLeaveTypeHeaders([]);
        $addLeaveTypeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $leaveCertificate = new leaveCertificate([
            "unit" => "hour",
            "duration" => 1,
            "enable" => false,
            "promptInformation" => "请假文案"
        ]);
        $submitTimeRule = new submitTimeRule([
            "timeValue" => 2,
            "timeUnit" => "day",
            "timeType" => "before",
            "enableTimeLimit" => true
        ]);
        $visibilityRules0 = new visibilityRules([
            "visible" => [
                "user01"
            ],
            "type" => "staff"
        ]);
        $addLeaveTypeRequest = new AddLeaveTypeRequest([
            "opUserId" => "user01",
            "leaveName" => "年假",
            "leaveViewUnit" => "day",
            "bizType" => "general_leave",
            "naturalDayLeave" => true,
            "hoursInPerDay" => 1000,
            "extras" => "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
            "paidLeave" => true,
            "visibilityRules" => [
                $visibilityRules0
            ],
            "whenCanLeave" => "entry",
            "leaveTimeCeilMinUnit" => "hour",
            "leaveTimeCeil" => false,
            "minLeaveHour" => 1,
            "submitTimeRule" => $submitTimeRule,
            "leaveCertificate" => $leaveCertificate,
            "maxLeaveTime" => 3,
            "leaveHourCeil" => "up",
            "freedomLeave" => true
        ]);
        try {
            $client->addLeaveTypeWithOptions($addLeaveTypeRequest, $addLeaveTypeHeaders, new RuntimeOptions([]));
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

  addLeaveTypeHeaders := &dingtalkattendance_1_0.AddLeaveTypeHeaders{}
  addLeaveTypeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  leaveCertificate := &dingtalkattendance_1_0.AddLeaveTypeRequestLeaveCertificate{
    Unit: tea.String("hour"),
    Duration: tea.Float64(1),
    Enable: tea.Bool(false),
    PromptInformation: tea.String("请假文案"),
  }
  submitTimeRule := &dingtalkattendance_1_0.AddLeaveTypeRequestSubmitTimeRule{
    TimeValue: tea.Int64(2),
    TimeUnit: tea.String("day"),
    TimeType: tea.String("before"),
    EnableTimeLimit: tea.Bool(true),
  }
  visibilityRules0 := &dingtalkattendance_1_0.AddLeaveTypeRequestVisibilityRules{
    Visible: []*string{tea.String("user01")},
    Type: tea.String("staff"),
  }
  addLeaveTypeRequest := &dingtalkattendance_1_0.AddLeaveTypeRequest{
    OpUserId: tea.String("user01"),
    LeaveName: tea.String("年假"),
    LeaveViewUnit: tea.String("day"),
    BizType: tea.String("general_leave"),
    NaturalDayLeave: tea.Bool(true),
    HoursInPerDay: tea.Int64(1000),
    Extras: tea.String("{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}"),
    PaidLeave: tea.Bool(true),
    VisibilityRules: []*dingtalkattendance_1_0.AddLeaveTypeRequestVisibilityRules{visibilityRules0},
    WhenCanLeave: tea.String("entry"),
    LeaveTimeCeilMinUnit: tea.String("hour"),
    LeaveTimeCeil: tea.Bool(false),
    MinLeaveHour: tea.Float64(1),
    SubmitTimeRule: submitTimeRule,
    LeaveCertificate: leaveCertificate,
    MaxLeaveTime: tea.Int64(3),
    LeaveHourCeil: tea.String("up"),
    FreedomLeave: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddLeaveTypeWithOptions(addLeaveTypeRequest, addLeaveTypeHeaders, &util.RuntimeOptions{})
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
    let addLeaveTypeHeaders = new $dingtalkattendance_1_0.AddLeaveTypeHeaders({ });
    addLeaveTypeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let leaveCertificate = new $dingtalkattendance_1_0.AddLeaveTypeRequestLeaveCertificate({
      unit: "hour",
      duration: 1,
      enable: false,
      promptInformation: "请假文案",
    });
    let submitTimeRule = new $dingtalkattendance_1_0.AddLeaveTypeRequestSubmitTimeRule({
      timeValue: 2,
      timeUnit: "day",
      timeType: "before",
      enableTimeLimit: true,
    });
    let visibilityRules0 = new $dingtalkattendance_1_0.AddLeaveTypeRequestVisibilityRules({
      visible: [
        "user01"
      ],
      type: "staff",
    });
    let addLeaveTypeRequest = new $dingtalkattendance_1_0.AddLeaveTypeRequest({
      opUserId: "user01",
      leaveName: "年假",
      leaveViewUnit: "day",
      bizType: "general_leave",
      naturalDayLeave: true,
      hoursInPerDay: 1000,
      extras: "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
      paidLeave: true,
      visibilityRules: [
        visibilityRules0
      ],
      whenCanLeave: "entry",
      leaveTimeCeilMinUnit: "hour",
      leaveTimeCeil: false,
      minLeaveHour: 1,
      submitTimeRule: submitTimeRule,
      leaveCertificate: leaveCertificate,
      maxLeaveTime: 3,
      leaveHourCeil: "up",
      freedomLeave: true,
    });
    try {
      await client.addLeaveTypeWithOptions(addLeaveTypeRequest, addLeaveTypeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeHeaders addLeaveTypeHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeHeaders();
            addLeaveTypeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestLeaveCertificate leaveCertificate = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestLeaveCertificate
            {
                Unit = "hour",
                Duration = 1,
                Enable = false,
                PromptInformation = "请假文案",
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestSubmitTimeRule submitTimeRule = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestSubmitTimeRule
            {
                TimeValue = 2,
                TimeUnit = "day",
                TimeType = "before",
                EnableTimeLimit = true,
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestVisibilityRules visibilityRules0 = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestVisibilityRules
            {
                Visible = new List<string>
                {
                    "user01"
                },
                Type = "staff",
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest addLeaveTypeRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest
            {
                OpUserId = "user01",
                LeaveName = "年假",
                LeaveViewUnit = "day",
                BizType = "general_leave",
                NaturalDayLeave = true,
                HoursInPerDay = 1000,
                Extras = "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
                PaidLeave = true,
                VisibilityRules = new List<AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.AddLeaveTypeRequest.AddLeaveTypeRequestVisibilityRules>
                {
                    visibilityRules0
                },
                WhenCanLeave = "entry",
                LeaveTimeCeilMinUnit = "hour",
                LeaveTimeCeil = false,
                MinLeaveHour = 1,
                SubmitTimeRule = submitTimeRule,
                LeaveCertificate = leaveCertificate,
                MaxLeaveTime = 3,
                LeaveHourCeil = "up",
                FreedomLeave = true,
            };
            try
            {
                client.AddLeaveTypeWithOptions(addLeaveTypeRequest, addLeaveTypeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回信息。 |
| leaveName | String | 假期名称。 |
| leaveCode | String | 假期规则唯一标识。 |
| leaveViewUnit | String | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| bizType | String | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| naturalDayLeave | Boolean | 是否按照自然日统计请假时长。   - **true**：是 - **false**：否   **[!NOTE]**    当为false的时候，用户发起请假时候会根据用户在请假时间段内的排班情况来计算请假时长。 |
| hoursInPerDay | Long | 每天折算的工作时长，为参数值的百分之一。  例如，某企业每天的工作时长设置为10小时，则该参数值为10\*100=1000。 |
| visibilityRules | Array | 适用范围规则列表，不传默认为全公司。 |
| visible | Array of String | 适用范围内数据列表。   - 当type=staff时，传员工userId列表。 - 当type=dept时，传部门id列表。 - 当type=label时，传角色id列表。 |
| type | String | 适用范围规则类型。   - **dept**：部门 - **staff**：员工 - **label**：角色 |
| submitTimeRule | Object | 限时提交规则。 |
| timeValue | Long | 限制值。   - 当timeUnit为day时，有效值范围是0至30天。 - 当timeUnit为hour时，有效值范围是0至24小时。 |
| timeUnit | String | 时间单位。   - **day**：天 - **hour**：小时 |
| timeType | String | 限制类型。   - **before**：提前 - **after**：补交 |
| enableTimeLimit | Boolean | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| leaveCertificate | Object | 请假证明。 |
| unit | String | 请假证明时长单位。   - **hour**：小时 - **day**：天 |
| duration | double | 超过多长时间需提供请假证明。 |
| enable | Boolean | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| promptInformation | String | 请假提示文案。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "leaveName" : "年假",
    "leaveCode" : "037477ae-1009-4632-b8e9-e919ae5e7973",
    "leaveViewUnit" : "day",
    "bizType" : "general_leave",
    "naturalDayLeave" : true,
    "hoursInPerDay" : 1000,
    "visibilityRules" : [ {
      "visible" : [ "user01" ],
      "type" : "staff"
    } ],
    "submitTimeRule" : {
      "timeValue" : 1,
      "timeUnit" : "day",
      "timeType" : "before",
      "enableTimeLimit" : false
    },
    "leaveCertificate" : {
      "unit" : "hour",
      "duration" : 1,
      "enable" : false,
      "promptInformation" : "请假文案"
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | lieuLeaveValidityIncorrect | 调休假有效期不正确 | 调休假有效期不正确 |
| 400 | lieuLeaveOnlyOne | 加班调休全局只能有一个 | 加班调休全局只能有一个 |
| 400 | bizTypeIncorrect | 假期业务类型不正确 | 假期业务类型不正确 |
| 400 | unitIncorrect | 假期单位不正确 | 假期单位不正确 |
| 400 | nameTooLong | 假期名称过长 | 假期名称过长 |
| 400 | nameAlreadyExists | 已存在相同假期名称 | 已存在相同假期名称 |
| 400 | leaveOrgIsUsed | 只允许企业接入使用 | 只允许企业接入使用 |
| 400 | notPermission | 无访问权限 | 无访问权限 |
| 400 | notManage | 部门的管理员不存在 | 部门的管理员不存在 |
| 400 | notFound | 未找到该假期类型 | 未找到该假期类型 |
| 400 | tryAgainLater | 更新失败，请稍后重试 | 更新失败，请稍后重试 |
| 400 | updateSpeedfast | 亲，该操作速度过快，请5分钟后再试 | 亲，该操作速度过快，请5分钟后再试 |
| 400 | systemError | 系统错误 | 系统错误 |
| 400 | invalidParam | 参数错误 | 参数错误 |
