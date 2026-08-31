---
title: "查询用户某段时间内是否处于封账状态"
source_url: "https://open.dingtalk.com/document/development/checks-whether-a-user-has-blocked-accounts-within-a-specified"
namespace: "development"
slug: "checks-whether-a-user-has-blocked-accounts-within-a-specified"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤统计 > 查询用户某段时间内是否处于封账状态"
doc_id: "8mCM14ZVFw"
updated_at: "2026-06-02 09:24:49"
---

> Source: https://open.dingtalk.com/document/development/checks-whether-a-user-has-blocked-accounts-within-a-specified
> Path: 应用开发 / 服务端 API / 考勤 > 考勤统计 > 查询用户某段时间内是否处于封账状态
> Updated: 2026-06-02 09:24:49

# 查询用户某段时间内是否处于封账状态

调用本接口，查询员工一段时间内是否处于封账状态，如果处于封账状态，则不能发起审批、排班、换班等操作。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/closingAccounts/status/query |
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
| userIds | Array of String | 是 | 员工列表。 |
| userTimeRange | Array | 是 | 时间段。 |
| startTime | Long | 是 | 开始日期，Unix时间戳，单位毫秒。 |
| endTime | Long | 是 | 结束日期，Unix时间戳，单位毫秒。 |
| bizCode | String | 是 | 情景：   - **BOSS\_CHECK**：老板改签 - **SCHEDULE**：排班 - **APPROVE**：补卡 - **SPECIAL\_DAYS**：特殊日期修改 |

### 请求示例

HTTP

```
POST /v1.0/attendance/closingAccounts/status/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:41f125c5b35e342b9b3c2e7a44c12462
Content-Type:application/json

{
  "userIds" : [ "userId1" ],
  "userTimeRange" : [ {
    "startTime" : 1622549264113,
    "endTime" : 1622549264116
  } ],
  "bizCode" : "BOOS_CHECK"
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
        CheckClosingAccountHeaders checkClosingAccountHeaders = new CheckClosingAccountHeaders();
        checkClosingAccountHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CheckClosingAccountRequest.CheckClosingAccountRequestUserTimeRange userTimeRange0 = new CheckClosingAccountRequest.CheckClosingAccountRequestUserTimeRange()
                .setStartTime(1622549264113L)
                .setEndTime(1622549264116L);
        CheckClosingAccountRequest checkClosingAccountRequest = new CheckClosingAccountRequest()
                .setUserIds(java.util.Arrays.asList(
                    "userId1"
                ))
                .setUserTimeRange(java.util.Arrays.asList(
                    userTimeRange0
                ))
                .setBizCode("BOOS_CHECK");
        try {
            client.checkClosingAccountWithOptions(checkClosingAccountRequest, checkClosingAccountHeaders, new RuntimeOptions());
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
        check_closing_account_headers = dingtalkattendance__1__0_models.CheckClosingAccountHeaders()
        check_closing_account_headers.x_acs_dingtalk_access_token = '<your access token>'
        user_time_range_0 = dingtalkattendance__1__0_models.CheckClosingAccountRequestUserTimeRange(
            start_time=1622549264113,
            end_time=1622549264116
        )
        check_closing_account_request = dingtalkattendance__1__0_models.CheckClosingAccountRequest(
            user_ids=[
                'userId1'
            ],
            user_time_range=[
                user_time_range_0
            ],
            biz_code='BOOS_CHECK'
        )
        try:
            client.check_closing_account_with_options(check_closing_account_request, check_closing_account_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_closing_account_headers = dingtalkattendance__1__0_models.CheckClosingAccountHeaders()
        check_closing_account_headers.x_acs_dingtalk_access_token = '<your access token>'
        user_time_range_0 = dingtalkattendance__1__0_models.CheckClosingAccountRequestUserTimeRange(
            start_time=1622549264113,
            end_time=1622549264116
        )
        check_closing_account_request = dingtalkattendance__1__0_models.CheckClosingAccountRequest(
            user_ids=[
                'userId1'
            ],
            user_time_range=[
                user_time_range_0
            ],
            biz_code='BOOS_CHECK'
        )
        try:
            await client.check_closing_account_with_options_async(check_closing_account_request, check_closing_account_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CheckClosingAccountHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CheckClosingAccountRequest\userTimeRange;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CheckClosingAccountRequest;
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
        $checkClosingAccountHeaders = new CheckClosingAccountHeaders([]);
        $checkClosingAccountHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $userTimeRange0 = new userTimeRange([
            "startTime" => 1622549264113,
            "endTime" => 1622549264116
        ]);
        $checkClosingAccountRequest = new CheckClosingAccountRequest([
            "userIds" => [
                "userId1"
            ],
            "userTimeRange" => [
                $userTimeRange0
            ],
            "bizCode" => "BOOS_CHECK"
        ]);
        try {
            $client->checkClosingAccountWithOptions($checkClosingAccountRequest, $checkClosingAccountHeaders, new RuntimeOptions([]));
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

  checkClosingAccountHeaders := &dingtalkattendance_1_0.CheckClosingAccountHeaders{}
  checkClosingAccountHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  userTimeRange0 := &dingtalkattendance_1_0.CheckClosingAccountRequestUserTimeRange{
    StartTime: tea.Int64(1622549264113),
    EndTime: tea.Int64(1622549264116),
  }
  checkClosingAccountRequest := &dingtalkattendance_1_0.CheckClosingAccountRequest{
    UserIds: []*string{tea.String("userId1")},
    UserTimeRange: []*dingtalkattendance_1_0.CheckClosingAccountRequestUserTimeRange{userTimeRange0},
    BizCode: tea.String("BOOS_CHECK"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CheckClosingAccountWithOptions(checkClosingAccountRequest, checkClosingAccountHeaders, &util.RuntimeOptions{})
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
    let checkClosingAccountHeaders = new $dingtalkattendance_1_0.CheckClosingAccountHeaders({ });
    checkClosingAccountHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let userTimeRange0 = new $dingtalkattendance_1_0.CheckClosingAccountRequestUserTimeRange({
      startTime: 1622549264113,
      endTime: 1622549264116,
    });
    let checkClosingAccountRequest = new $dingtalkattendance_1_0.CheckClosingAccountRequest({
      userIds: [
        "userId1"
      ],
      userTimeRange: [
        userTimeRange0
      ],
      bizCode: "BOOS_CHECK",
    });
    try {
      await client.checkClosingAccountWithOptions(checkClosingAccountRequest, checkClosingAccountHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountHeaders checkClosingAccountHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountHeaders();
            checkClosingAccountHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountRequest.CheckClosingAccountRequestUserTimeRange userTimeRange0 = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountRequest.CheckClosingAccountRequestUserTimeRange
            {
                StartTime = 1622549264113,
                EndTime = 1622549264116,
            };
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountRequest checkClosingAccountRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountRequest
            {
                UserIds = new List<string>
                {
                    "userId1"
                },
                UserTimeRange = new List<AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckClosingAccountRequest.CheckClosingAccountRequestUserTimeRange>
                {
                    userTimeRange0
                },
                BizCode = "BOOS_CHECK",
            };
            try
            {
                client.CheckClosingAccountWithOptions(checkClosingAccountRequest, checkClosingAccountHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountHeaders> checkClosingAccountHeaders = make_shared<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountHeaders>();
  checkClosingAccountHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountRequestUserTimeRange> userTimeRange0 = make_shared<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountRequestUserTimeRange>(map<string, boost::any>({
    {"startTime", boost::any(1622549264113)},
    {"endTime", boost::any(1622549264116)}
  }));
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountRequest> checkClosingAccountRequest = make_shared<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountRequest>(map<string, boost::any>({
    {"userIds", boost::any(vector<string>({
      "userId1"
    }))},
    {"userTimeRange", boost::any(vector<Alibabacloud_Dingtalkattendance_1_0::CheckClosingAccountRequestUserTimeRange>({
      userTimeRange0
    }))},
    {"bizCode", boost::any(string("BOOS_CHECK"))}
  }));
  try {
    client->checkClosingAccountWithOptions(checkClosingAccountRequest, checkClosingAccountHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| mesage | String | 返回码描述。 |
| code | String | 返回码。 |
| pass | Boolean | 处于封账期间返回false，否则返回true。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "mesage" : "success",
  "code" : "0",
  "pass" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 参数异常 |
| 500 | systemError | 系统异常 | 系统异常 |
