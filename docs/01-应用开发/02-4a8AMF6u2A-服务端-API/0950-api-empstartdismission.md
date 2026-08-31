---
title: "员工加入待离职"
source_url: "https://open.dingtalk.com/document/development/api-empstartdismission"
namespace: "development"
slug: "api-empstartdismission"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 员工管理 > 员工加入待离职"
doc_id: "EvaV9iJgJ0"
updated_at: "2026-06-04 19:10:28"
---

> Source: https://open.dingtalk.com/document/development/api-empstartdismission
> Path: 应用开发 / 服务端 API / 智能人事 > 员工管理 > 员工加入待离职
> Updated: 2026-06-04 19:10:28

# 员工加入待离职

给员工办理离职，加入到待离职列表。

## 接口调用说明

后续的确认离职要使用智能人事的接口，如果是通过其他渠道删人的（比如通讯录接口删人），离职原因和备注等信息都会丢失。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/pendingDismission/start |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrm.Process.ReadWrite-智能人事流程读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 离职人userId。 |
| lastWorkDate | Long | 是 | 最后工作日。 |
| terminationReasonVoluntary | Array of String | 否 | 主动离职原因id，可调用[获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md)接口获取。 |
| terminationReasonPassive | Array of String | 否 | 被动离职原因id，可调用[获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md)接口获取。 |
| remark | String | 否 | 备注。 |
| partner | Boolean | 否 | 是否加入HRM统计。 |
| toHireBlackList | Boolean | 否 | 是否加入招聘黑名单。 |
| toHireDismissionTalent | Boolean | 否 | 是否加入招聘人才库。 |
| toHrmBlackList | Boolean | 否 | 是否加入人事黑名单。 |

### 请求示例

HTTP

```
POST /v1.0/hrm/pendingDismission/start HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e73d7d0e99d234368c4f5b0088edc9c9
Content-Type:application/json

{
  "userId" : "2163515669935611",
  "lastWorkDate" : 1736489016000,
  "terminationReasonVoluntary" : [ "1" ],
  "terminationReasonPassive" : [ "1" ],
  "remark" : "备注信息",
  "partner" : false,
  "toHireBlackList" : false,
  "toHireDismissionTalent" : false,
  "toHrmBlackList" : false
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.EmpStartDismissionHeaders empStartDismissionHeaders = new com.aliyun.dingtalkhrm_1_0.models.EmpStartDismissionHeaders();
        empStartDismissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.EmpStartDismissionRequest empStartDismissionRequest = new com.aliyun.dingtalkhrm_1_0.models.EmpStartDismissionRequest()
                .setUserId("2163515669935611")
                .setLastWorkDate(1736489016000L)
                .setTerminationReasonVoluntary(java.util.Arrays.asList(
                    "1"
                ))
                .setTerminationReasonPassive(java.util.Arrays.asList(
                    "1"
                ))
                .setRemark("备注信息")
                .setPartner(false)
                .setToHireBlackList(false)
                .setToHireDismissionTalent(false)
                .setToHrmBlackList(false);
        try {
            client.empStartDismissionWithOptions(empStartDismissionRequest, empStartDismissionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrm_1_0.client import Client as dingtalkhrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        emp_start_dismission_headers = dingtalkhrm__1__0_models.EmpStartDismissionHeaders()
        emp_start_dismission_headers.x_acs_dingtalk_access_token = '<your access token>'
        emp_start_dismission_request = dingtalkhrm__1__0_models.EmpStartDismissionRequest(
            user_id='2163515669935611',
            last_work_date=1736489016000,
            termination_reason_voluntary=[
                '1'
            ],
            termination_reason_passive=[
                '1'
            ],
            remark='备注信息',
            partner=False,
            to_hire_black_list=False,
            to_hire_dismission_talent=False,
            to_hrm_black_list=False
        )
        try:
            client.emp_start_dismission_with_options(emp_start_dismission_request, emp_start_dismission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        emp_start_dismission_headers = dingtalkhrm__1__0_models.EmpStartDismissionHeaders()
        emp_start_dismission_headers.x_acs_dingtalk_access_token = '<your access token>'
        emp_start_dismission_request = dingtalkhrm__1__0_models.EmpStartDismissionRequest(
            user_id='2163515669935611',
            last_work_date=1736489016000,
            termination_reason_voluntary=[
                '1'
            ],
            termination_reason_passive=[
                '1'
            ],
            remark='备注信息',
            partner=False,
            to_hire_black_list=False,
            to_hire_dismission_talent=False,
            to_hrm_black_list=False
        )
        try:
            await client.emp_start_dismission_with_options_async(emp_start_dismission_request, emp_start_dismission_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\EmpStartDismissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\EmpStartDismissionRequest;
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
        $empStartDismissionHeaders = new EmpStartDismissionHeaders([]);
        $empStartDismissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $empStartDismissionRequest = new EmpStartDismissionRequest([
            "userId" => "2163515669935611",
            "lastWorkDate" => 1736489016000,
            "terminationReasonVoluntary" => [
                "1"
            ],
            "terminationReasonPassive" => [
                "1"
            ],
            "remark" => "备注信息",
            "partner" => false,
            "toHireBlackList" => false,
            "toHireDismissionTalent" => false,
            "toHrmBlackList" => false
        ]);
        try {
            $client->empStartDismissionWithOptions($empStartDismissionRequest, $empStartDismissionHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
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
func CreateClient () (_result *dingtalkhrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrm_1_0.Client{}
  _result, _err = dingtalkhrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  empStartDismissionHeaders := &dingtalkhrm_1_0.EmpStartDismissionHeaders{}
  empStartDismissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  empStartDismissionRequest := &dingtalkhrm_1_0.EmpStartDismissionRequest{
    UserId: tea.String("2163515669935611"),
    LastWorkDate: tea.Int64(1736489016000),
    TerminationReasonVoluntary: []*string{tea.String("1")},
    TerminationReasonPassive: []*string{tea.String("1")},
    Remark: tea.String("备注信息"),
    Partner: tea.Bool(false),
    ToHireBlackList: tea.Bool(false),
    ToHireDismissionTalent: tea.Bool(false),
    ToHrmBlackList: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.EmpStartDismissionWithOptions(empStartDismissionRequest, empStartDismissionHeaders, &util.RuntimeOptions{})
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
const dingtalkhrm_1_0 = require('@alicloud/dingtalk/hrm_1_0');
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
    return new dingtalkhrm_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let empStartDismissionHeaders = new dingtalkhrm_1_0.EmpStartDismissionHeaders({ });
    empStartDismissionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let empStartDismissionRequest = new dingtalkhrm_1_0.EmpStartDismissionRequest({
      userId: '2163515669935611',
      lastWorkDate: 1736489016000,
      terminationReasonVoluntary: [
        '1'
      ],
      terminationReasonPassive: [
        '1'
      ],
      remark: '备注信息',
      partner: false,
      toHireBlackList: false,
      toHireDismissionTalent: false,
      toHrmBlackList: false,
    });
    try {
      await client.empStartDismissionWithOptions(empStartDismissionRequest, empStartDismissionHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.EmpStartDismissionHeaders empStartDismissionHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.EmpStartDismissionHeaders();
            empStartDismissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.EmpStartDismissionRequest empStartDismissionRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.EmpStartDismissionRequest
            {
                UserId = "2163515669935611",
                LastWorkDate = 1736489016000,
                TerminationReasonVoluntary = new List<string>
                {
                    "1"
                },
                TerminationReasonPassive = new List<string>
                {
                    "1"
                },
                Remark = "备注信息",
                Partner = false,
                ToHireBlackList = false,
                ToHireDismissionTalent = false,
                ToHrmBlackList = false,
            };
            try
            {
                client.EmpStartDismissionWithOptions(empStartDismissionRequest, empStartDismissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求 ID。 |
| success | Boolean | 接口调用是否成功。 |
| result | Boolean | 结果内容。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "679477AA-74B9-764E-9B2C-BD73540FD227",
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 未填最后工作日、离职人userId等 |
| 401 | businessError | 业务异常 | 例如不允许给自己办离职，员工不是正常在职状态等 |
| 500 | systemError | 系统异常 | 系统异常 |
