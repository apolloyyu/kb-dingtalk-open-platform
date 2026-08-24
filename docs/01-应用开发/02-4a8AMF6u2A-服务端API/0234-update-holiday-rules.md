---
title: "更新假期规则"
source_url: "https://open.dingtalk.com/document/development/update-holiday-rules"
namespace: "development"
slug: "update-holiday-rules"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 更新假期规则"
doc_id: "srZ9Fyuwom"
updated_at: "2026-06-02 09:24:53"
---

> Source: https://open.dingtalk.com/document/development/update-holiday-rules
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 更新假期规则
> Updated: 2026-06-02 09:24:53

# 更新假期规则

调用本接口，更新指定假期的相关规则。

## **接口调用说明**

创建假期规则有2种方式，通过调用接口创建、通过钉钉官方应用考勤产品创建：

| 创建假期规则方式 | 调用本接口是否支持更新假期类型 |
| --- | --- |
| 调用[添加假期规则](0233-add-holiday-rules.md)接口创建的假期类型。 | 支持 |
| 企业管理后台考勤应用创建的假期类型。   - 考勤应用系统默认创建。 - 通过考勤应用后台创建 。 | 不支持 |

如下图所示，在**考勤应用** > **假期管理** > **假期规则**页面，可以查看共4个假期规则。

- 接口添加的假期1、接口添加的假期2，是通过接口创建的假期类型。调用本接口，可以更新假期相关的信息，如请假名称、请假单位、计算请假时长方式、余额范围等。
- 事假、调休，是考勤应用系统默认创建的假期类型。调用本接口，无法更新假期类型，报以下错误信息：errcode:880015,errmsg:批量leaveCode或userId都不存在。

> **[!NOTE]**
>
> 可调用[查询假期规则列表](0238-holiday-type-query.md)接口，查询哪些假期规则是通过接口创建的。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7747369361/p369550.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/leaves/types |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_holiday\_manage-钉钉假期管理的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUserId | String | 是 | 操作者userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| leaveName | String | 否 | 假期名称。 |
| leaveViewUnit | String | 是 | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| bizType | String | 是 | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| naturalDayLeave | Boolean | 否 | 是否按照自然日统计请假时长。   - **true**：是 - **false**：否     例如，员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。   - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者法定节假日。 |
| hoursInPerDay | Long | 否 | 每天折算的工作时长，为参数值的百分之一。    例如，某企业员工所在的班次工时是8小时，则该参数值为8\*100=800。 |
| leaveCode | String | 是 | 接口添加的假期规则标识，leave\_code必须是通过接口添加的假期类型。   - 企业内部应用，调用[添加假期规则](https://open.dingtalk.com/document/orgapp/holiday-type-added)接口获取的leave\_code参数值。 - 第三方企业应用，调用[添加假期规则](https://open.dingtalk.com/document/isvapp/holiday-type-added)接口获取的leave\_code参数值。 |
| extras | String | 否 | 调休假有效期规则。   - **validity\_type**：有效类型    - **absolute\_time**：绝对时间   - **relative\_time**：相对时间 - **validity\_value**：延长日期    - 当validity\_type为**absolute\_time**，该值不为空且满足“yy-mm”格式。   - 当validity\_type为**relative\_time**，该值为大于1的整数。 |
| visibilityRules | Array | 否 | 适用范围规则列表，不传默认为全公司。 |
| visible | Array of String | 否 | 适用范围内数据列表。   - 当type=staff时，传员工userId列表。 - 当type=dept时，传部门id列表。 - 当type=label时，传角色id列表。 |
| type | String | 否 | 适用范围规则类型。   - **dept**：部门 - **staff**：员工 - **label**：角色 |
| submitTimeRule | Object | 否 | 限时提交规则。 |
| timeValue | Long | 否 | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天。 - 当timeUnit为**hour**时，有效值范围是0至24小时。 |
| timeUnit | String | 否 | 时间单位。   - **day**：天 - **hour**：小时 |
| timeType | String | 否 | 限制类型。   - **before**：提前 - **after**：补交 |
| enableTimeLimit | Boolean | 否 | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| leaveCertificate | Object | 否 | 请假证明。 |
| unit | String | 否 | 请假证明单位。   - **hour**：小时 - **day**：天 |
| duration | double | 否 | 超过多长时间需提供请假证明。 |
| enable | Boolean | 否 | 是否开启请假证明。   - **true**：开启 - **false**：不开启 |
| promptInformation | String | 否 | 请假提示文案。 |

### 请求示例

HTTP

```
PUT /v1.0/attendance/leaves/types?opUserId=user01 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1d97cxxx
Content-Type:application/json

{
  "leaveName" : "年假",
  "leaveViewUnit" : "day",
  "bizType" : "general_leave",
  "naturalDayLeave" : true,
  "hoursInPerDay" : 1000,
  "leaveCode" : "047477ae-1009-4632-b8e9-e919ae5e7973",
  "extras" : "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
  "visibilityRules" : [ {
    "visible" : [ "user01" ],
    "type" : "staff"
  } ],
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
  }
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
        com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeHeaders updateLeaveTypeHeaders = new com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeHeaders();
        updateLeaveTypeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestLeaveCertificate leaveCertificate = new com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestLeaveCertificate()
                .setUnit("hour")
                .setDuration(1D)
                .setEnable(false)
                .setPromptInformation("请假文案");
        com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestSubmitTimeRule submitTimeRule = new com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestSubmitTimeRule()
                .setTimeValue(2L)
                .setTimeUnit("day")
                .setTimeType("before")
                .setEnableTimeLimit(true);
        com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestVisibilityRules visibilityRules0 = new com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestVisibilityRules()
                .setVisible(java.util.Arrays.asList(
                    "user01"
                ))
                .setType("staff");
        com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest updateLeaveTypeRequest = new com.aliyun.dingtalkattendance_1_0.models.UpdateLeaveTypeRequest()
                .setOpUserId("user01")
                .setLeaveName("年假")
                .setLeaveViewUnit("day")
                .setBizType("general_leave")
                .setNaturalDayLeave(true)
                .setHoursInPerDay(1000L)
                .setLeaveCode("047477ae-1009-4632-b8e9-e919ae5e7973")
                .setExtras("{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}")
                .setVisibilityRules(java.util.Arrays.asList(
                    visibilityRules0
                ))
                .setSubmitTimeRule(submitTimeRule)
                .setLeaveCertificate(leaveCertificate);
        try {
            client.updateLeaveTypeWithOptions(updateLeaveTypeRequest, updateLeaveTypeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_leave_type_headers = dingtalkattendance__1__0_models.UpdateLeaveTypeHeaders()
        update_leave_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        leave_certificate = dingtalkattendance__1__0_models.UpdateLeaveTypeRequestLeaveCertificate(
            unit='hour',
            duration=1,
            enable=False,
            prompt_information='请假文案'
        )
        submit_time_rule = dingtalkattendance__1__0_models.UpdateLeaveTypeRequestSubmitTimeRule(
            time_value=2,
            time_unit='day',
            time_type='before',
            enable_time_limit=True
        )
        visibility_rules_0 = dingtalkattendance__1__0_models.UpdateLeaveTypeRequestVisibilityRules(
            visible=[
                'user01'
            ],
            type='staff'
        )
        update_leave_type_request = dingtalkattendance__1__0_models.UpdateLeaveTypeRequest(
            op_user_id='user01',
            leave_name='年假',
            leave_view_unit='day',
            biz_type='general_leave',
            natural_day_leave=True,
            hours_in_per_day=1000,
            leave_code='047477ae-1009-4632-b8e9-e919ae5e7973',
            extras='{"validity_type":"absolute_time","validity_value":"12-31"}',
            visibility_rules=[
                visibility_rules_0
            ],
            submit_time_rule=submit_time_rule,
            leave_certificate=leave_certificate
        )
        try:
            client.update_leave_type_with_options(update_leave_type_request, update_leave_type_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_leave_type_headers = dingtalkattendance__1__0_models.UpdateLeaveTypeHeaders()
        update_leave_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        leave_certificate = dingtalkattendance__1__0_models.UpdateLeaveTypeRequestLeaveCertificate(
            unit='hour',
            duration=1,
            enable=False,
            prompt_information='请假文案'
        )
        submit_time_rule = dingtalkattendance__1__0_models.UpdateLeaveTypeRequestSubmitTimeRule(
            time_value=2,
            time_unit='day',
            time_type='before',
            enable_time_limit=True
        )
        visibility_rules_0 = dingtalkattendance__1__0_models.UpdateLeaveTypeRequestVisibilityRules(
            visible=[
                'user01'
            ],
            type='staff'
        )
        update_leave_type_request = dingtalkattendance__1__0_models.UpdateLeaveTypeRequest(
            op_user_id='user01',
            leave_name='年假',
            leave_view_unit='day',
            biz_type='general_leave',
            natural_day_leave=True,
            hours_in_per_day=1000,
            leave_code='047477ae-1009-4632-b8e9-e919ae5e7973',
            extras='{"validity_type":"absolute_time","validity_value":"12-31"}',
            visibility_rules=[
                visibility_rules_0
            ],
            submit_time_rule=submit_time_rule,
            leave_certificate=leave_certificate
        )
        try:
            await client.update_leave_type_with_options_async(update_leave_type_request, update_leave_type_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\UpdateLeaveTypeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\UpdateLeaveTypeRequest\leaveCertificate;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\UpdateLeaveTypeRequest\submitTimeRule;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\UpdateLeaveTypeRequest\visibilityRules;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\UpdateLeaveTypeRequest;
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
        $updateLeaveTypeHeaders = new UpdateLeaveTypeHeaders([]);
        $updateLeaveTypeHeaders->xAcsDingtalkAccessToken = "<your access token>";
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
        $updateLeaveTypeRequest = new UpdateLeaveTypeRequest([
            "opUserId" => "user01",
            "leaveName" => "年假",
            "leaveViewUnit" => "day",
            "bizType" => "general_leave",
            "naturalDayLeave" => true,
            "hoursInPerDay" => 1000,
            "leaveCode" => "047477ae-1009-4632-b8e9-e919ae5e7973",
            "extras" => "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
            "visibilityRules" => [
                $visibilityRules0
            ],
            "submitTimeRule" => $submitTimeRule,
            "leaveCertificate" => $leaveCertificate
        ]);
        try {
            $client->updateLeaveTypeWithOptions($updateLeaveTypeRequest, $updateLeaveTypeHeaders, new RuntimeOptions([]));
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

  updateLeaveTypeHeaders := &dingtalkattendance_1_0.UpdateLeaveTypeHeaders{}
  updateLeaveTypeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  leaveCertificate := &dingtalkattendance_1_0.UpdateLeaveTypeRequestLeaveCertificate{
    Unit: tea.String("hour"),
    Duration: tea.Float64(1),
    Enable: tea.Bool(false),
    PromptInformation: tea.String("请假文案"),
  }
  submitTimeRule := &dingtalkattendance_1_0.UpdateLeaveTypeRequestSubmitTimeRule{
    TimeValue: tea.Int64(2),
    TimeUnit: tea.String("day"),
    TimeType: tea.String("before"),
    EnableTimeLimit: tea.Bool(true),
  }
  visibilityRules0 := &dingtalkattendance_1_0.UpdateLeaveTypeRequestVisibilityRules{
    Visible: []*string{tea.String("user01")},
    Type: tea.String("staff"),
  }
  updateLeaveTypeRequest := &dingtalkattendance_1_0.UpdateLeaveTypeRequest{
    OpUserId: tea.String("user01"),
    LeaveName: tea.String("年假"),
    LeaveViewUnit: tea.String("day"),
    BizType: tea.String("general_leave"),
    NaturalDayLeave: tea.Bool(true),
    HoursInPerDay: tea.Int64(1000),
    LeaveCode: tea.String("047477ae-1009-4632-b8e9-e919ae5e7973"),
    Extras: tea.String("{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}"),
    VisibilityRules: []*dingtalkattendance_1_0.UpdateLeaveTypeRequestVisibilityRules{visibilityRules0},
    SubmitTimeRule: submitTimeRule,
    LeaveCertificate: leaveCertificate,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateLeaveTypeWithOptions(updateLeaveTypeRequest, updateLeaveTypeHeaders, &util.RuntimeOptions{})
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
    let updateLeaveTypeHeaders = new $dingtalkattendance_1_0.UpdateLeaveTypeHeaders({ });
    updateLeaveTypeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let leaveCertificate = new $dingtalkattendance_1_0.UpdateLeaveTypeRequestLeaveCertificate({
      unit: "hour",
      duration: 1,
      enable: false,
      promptInformation: "请假文案",
    });
    let submitTimeRule = new $dingtalkattendance_1_0.UpdateLeaveTypeRequestSubmitTimeRule({
      timeValue: 2,
      timeUnit: "day",
      timeType: "before",
      enableTimeLimit: true,
    });
    let visibilityRules0 = new $dingtalkattendance_1_0.UpdateLeaveTypeRequestVisibilityRules({
      visible: [
        "user01"
      ],
      type: "staff",
    });
    let updateLeaveTypeRequest = new $dingtalkattendance_1_0.UpdateLeaveTypeRequest({
      opUserId: "user01",
      leaveName: "年假",
      leaveViewUnit: "day",
      bizType: "general_leave",
      naturalDayLeave: true,
      hoursInPerDay: 1000,
      leaveCode: "047477ae-1009-4632-b8e9-e919ae5e7973",
      extras: "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
      visibilityRules: [
        visibilityRules0
      ],
      submitTimeRule: submitTimeRule,
      leaveCertificate: leaveCertificate,
    });
    try {
      await client.updateLeaveTypeWithOptions(updateLeaveTypeRequest, updateLeaveTypeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeHeaders updateLeaveTypeHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeHeaders();
            updateLeaveTypeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestLeaveCertificate leaveCertificate = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestLeaveCertificate
            {
                Unit = "hour",
                Duration = 1,
                Enable = false,
                PromptInformation = "请假文案",
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestSubmitTimeRule submitTimeRule = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestSubmitTimeRule
            {
                TimeValue = 2,
                TimeUnit = "day",
                TimeType = "before",
                EnableTimeLimit = true,
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestVisibilityRules visibilityRules0 = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestVisibilityRules
            {
                Visible = new List<string>
                {
                    "user01"
                },
                Type = "staff",
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest updateLeaveTypeRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest
            {
                OpUserId = "user01",
                LeaveName = "年假",
                LeaveViewUnit = "day",
                BizType = "general_leave",
                NaturalDayLeave = true,
                HoursInPerDay = 1000,
                LeaveCode = "047477ae-1009-4632-b8e9-e919ae5e7973",
                Extras = "{\"validity_type\":\"absolute_time\",\"validity_value\":\"12-31\"}",
                VisibilityRules = new List<AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.UpdateLeaveTypeRequest.UpdateLeaveTypeRequestVisibilityRules>
                {
                    visibilityRules0
                },
                SubmitTimeRule = submitTimeRule,
                LeaveCertificate = leaveCertificate,
            };
            try
            {
                client.UpdateLeaveTypeWithOptions(updateLeaveTypeRequest, updateLeaveTypeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回值。 |
| leaveName | String | 假期名称。 |
| leaveCode | String | 假期类型唯一标识。 |
| leaveViewUnit | String | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| bizType | String | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| naturalDayLeave | Boolean | 是否按照自然日统计请假时长。   - **true**：是 - **false**：否     例如,员工小明提交请假审批单，开始时间是2022年4月11日上午9:30，结束时间是2022年4月18日下午18:30，其中4月16和4月17为周六日休息。   - 当该参数传true时，小明发起该请假审批单后，计入的请假天数为8天。包含员工未排班的休息日或者法定节假日。 - 当该参数传false时，小明发起该请假审批单后，计入的请假天数为6天。不包含员工未排班的休息日或者法定节假日。 |
| hoursInPerDay | Long | 每天折算的工作时长，为参数值的百分之一。    例如，某企业员工所在的班次工时是8小时，则该字段值为8\*100=800。 |
| visibilityRules | Array | 适用范围规则列表，不传默认为全公司。 |
| visible | Array of String | 适用范围内数据列表。   - 当type=staff时，传员工userId列表。 - 当type=dept时，传部门id列表。 - 当type=label时，传角色id列表。 |
| type | String | 适用范围规则类型。   - **dept**：部门 - **staff**：员工 - **label**：角色 |
| submitTimeRule | Object | 限时提交规则。 |
| timeValue | Long | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天； - 当timeUnit为**hour**时，有效值范围是0至24小时。 |
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
| 400 | bizTypeCannotModified | 假期业务类型不能修改 | 假期业务类型不能修改 |
| 400 | lieuLeaveOnlyOne | 加班调休全局只能有一个 | 加班调休全局只能有一个 |
| 400 | bizTypeIncorrect | 假期业务类型不正确 | 假期业务类型不正确 |
| 400 | unitIncorrect | 假期单位不正确 | 假期单位不正确 |
| 400 | nameTooLong | 假期名称过长 | 假期名称过长 |
| 400 | nameAlreadyExists | 已存在相同假期名称 | 已存在相同假期名称 |
| 400 | leaveOrgIsUsed | 只允许企业接入使用 | 只允许企业接入使用 |
| 400 | notPermission | 无访问权限 | 无访问权限 |
| 400 | notManage | 部门的管理员不存在 | 部门的管理员不存在 |
| 400 | notFound | 未找到该假期类型 | 未找到该假期类型 |
| 400 | notUpdateType | 假期业务类型不能修改 | 假期业务类型不能修改 |
| 400 | tryAgainLater | 更新失败，请稍后重试 | 更新失败，请稍后重试 |
| 400 | updateSpeedfast | 亲，该操作速度过快，请5分钟后再试 | 亲，该操作速度过快，请5分钟后再试 |
| 400 | systemError | 系统错误 | 系统错误 |
| 400 | invalidParam | 参数错误 | 参数错误 |
