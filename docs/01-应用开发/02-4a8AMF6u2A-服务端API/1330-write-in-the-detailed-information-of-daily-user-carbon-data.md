---
title: "写入每日用户碳数据明细信息"
source_url: "https://open.dingtalk.com/document/development/write-in-the-detailed-information-of-daily-user-carbon-data"
namespace: "development"
slug: "write-in-the-detailed-information-of-daily-user-carbon-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉钉碳中和 > 写入每日用户碳数据明细信息"
doc_id: "Tm83JqBQNd"
updated_at: "2026-01-29 14:20:20"
---

> Source: https://open.dingtalk.com/document/development/write-in-the-detailed-information-of-daily-user-carbon-data
> Path: 应用开发 / 服务端API / 更多开放 > 钉钉碳中和 > 写入每日用户碳数据明细信息
> Updated: 2026-01-29 14:20:20

# 写入每日用户碳数据明细信息

通过此接口可写入用户的每日碳减排行为明细数据，包括减碳方式、减碳量、行为时间等详细信息，用于企业碳账户统计、绿色办公分析等场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/carbon/userDetails/write |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Carbon.Common.Read-调用企业API基础权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userDetailsList | Array | 是 | 请求参数。 |
| actionId | String | 是 | 全局唯一ID，用于数据订正。 |
| userId | String | 是 | 钉钉用户id |
| corpId | String | 是 | 钉钉组织corpId。 |
| deptId | Long | 是 | 钉钉部门ID。 |
| actionType | String | 是 | 碳能量减排来源。 |
| carbonAmount | String | 是 | 碳能量克数。 |
| actionStartTime | String | 是 | 减排行为开始时间。 |
| actionEndTime | String | 是 | 减排行为结束时间。 |
| version | Integer | 是 | 版本号，默认为1。 |

### 请求示例

HTTP

```
POST /v1.0/carbon/userDetails/write HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "userDetailsList" : [ {
    "actionId" : "110120211202",
    "userId" : 1101,
    "corpId" : "ding123",
    "deptId" : 2202,
    "actionType" : "SALARYSHEET",
    "carbonAmount" : "2.2",
    "actionStartTime" : "2021-12-01 14:52:31",
    "actionEndTime" : "2021-12-01 14:52:31",
    "version" : 1
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcarbon_1_0.*;
import com.aliyun.dingtalkcarbon_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcarbon_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcarbon_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcarbon_1_0.Client client = Sample.createClient();
        WriteUserCarbonHeaders writeUserCarbonHeaders = new WriteUserCarbonHeaders();
        writeUserCarbonHeaders.xAcsDingtalkAccessToken = "<your access token>";
        WriteUserCarbonRequest.WriteUserCarbonRequestUserDetailsList userDetailsList0 = new WriteUserCarbonRequest.WriteUserCarbonRequestUserDetailsList()
                .setActionId("110120211202")
                .setUserId(1101L)
                .setCorpId("ding123")
                .setDeptId(2202L)
                .setActionType("SALARYSHEET")
                .setCarbonAmount("2.2")
                .setActionStartTime("2021-12-01 14:52:31")
                .setActionEndTime("2021-12-01 14:52:31")
                .setVersion(1);
        WriteUserCarbonRequest writeUserCarbonRequest = new WriteUserCarbonRequest()
                .setUserDetailsList(java.util.Arrays.asList(
                    userDetailsList0
                ));
        try {
            client.writeUserCarbonWithOptions(writeUserCarbonRequest, writeUserCarbonHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.carbon_1_0.client import Client as dingtalkcarbon_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.carbon_1_0 import models as dingtalkcarbon__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcarbon_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcarbon_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        write_user_carbon_headers = dingtalkcarbon__1__0_models.WriteUserCarbonHeaders()
        write_user_carbon_headers.x_acs_dingtalk_access_token = '<your access token>'
        user_details_list_0 = dingtalkcarbon__1__0_models.WriteUserCarbonRequestUserDetailsList(
            action_id='110120211202',
            user_id=1101,
            corp_id='ding123',
            dept_id=2202,
            action_type='SALARYSHEET',
            carbon_amount='2.2',
            action_start_time='2021-12-01 14:52:31',
            action_end_time='2021-12-01 14:52:31',
            version=1
        )
        write_user_carbon_request = dingtalkcarbon__1__0_models.WriteUserCarbonRequest(
            user_details_list=[
                user_details_list_0
            ]
        )
        try:
            client.write_user_carbon_with_options(write_user_carbon_request, write_user_carbon_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        write_user_carbon_headers = dingtalkcarbon__1__0_models.WriteUserCarbonHeaders()
        write_user_carbon_headers.x_acs_dingtalk_access_token = '<your access token>'
        user_details_list_0 = dingtalkcarbon__1__0_models.WriteUserCarbonRequestUserDetailsList(
            action_id='110120211202',
            user_id=1101,
            corp_id='ding123',
            dept_id=2202,
            action_type='SALARYSHEET',
            carbon_amount='2.2',
            action_start_time='2021-12-01 14:52:31',
            action_end_time='2021-12-01 14:52:31',
            version=1
        )
        write_user_carbon_request = dingtalkcarbon__1__0_models.WriteUserCarbonRequest(
            user_details_list=[
                user_details_list_0
            ]
        )
        try:
            await client.write_user_carbon_with_options_async(write_user_carbon_request, write_user_carbon_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Models\WriteUserCarbonHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Models\WriteUserCarbonRequest\userDetailsList;
use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Models\WriteUserCarbonRequest;
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
        $writeUserCarbonHeaders = new WriteUserCarbonHeaders([]);
        $writeUserCarbonHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $userDetailsList0 = new userDetailsList([
            "actionId" => "110120211202",
            "userId" => 1101,
            "corpId" => "ding123",
            "deptId" => 2202,
            "actionType" => "SALARYSHEET",
            "carbonAmount" => "2.2",
            "actionStartTime" => "2021-12-01 14:52:31",
            "actionEndTime" => "2021-12-01 14:52:31",
            "version" => 1
        ]);
        $writeUserCarbonRequest = new WriteUserCarbonRequest([
            "userDetailsList" => [
                $userDetailsList0
            ]
        ]);
        try {
            $client->writeUserCarbonWithOptions($writeUserCarbonRequest, $writeUserCarbonHeaders, new RuntimeOptions([]));
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
  dingtalkcarbon_1_0  "github.com/alibabacloud-go/dingtalk/carbon_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcarbon_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcarbon_1_0.Client{}
  _result, _err = dingtalkcarbon_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  writeUserCarbonHeaders := &dingtalkcarbon_1_0.WriteUserCarbonHeaders{}
  writeUserCarbonHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  userDetailsList0 := &dingtalkcarbon_1_0.WriteUserCarbonRequestUserDetailsList{
    ActionId: tea.String("110120211202"),
    UserId: tea.Int64(1101),
    CorpId: tea.String("ding123"),
    DeptId: tea.Int64(2202),
    ActionType: tea.String("SALARYSHEET"),
    CarbonAmount: tea.String("2.2"),
    ActionStartTime: tea.String("2021-12-01 14:52:31"),
    ActionEndTime: tea.String("2021-12-01 14:52:31"),
    Version: tea.Int32(1),
  }
  writeUserCarbonRequest := &dingtalkcarbon_1_0.WriteUserCarbonRequest{
    UserDetailsList: []*dingtalkcarbon_1_0.WriteUserCarbonRequestUserDetailsList{userDetailsList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.WriteUserCarbonWithOptions(writeUserCarbonRequest, writeUserCarbonHeaders, &util.RuntimeOptions{})
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
import dingtalkcarbon_1_0, * as $dingtalkcarbon_1_0 from '@alicloud/dingtalk/carbon_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcarbon_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcarbon_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let writeUserCarbonHeaders = new $dingtalkcarbon_1_0.WriteUserCarbonHeaders({ });
    writeUserCarbonHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let userDetailsList0 = new $dingtalkcarbon_1_0.WriteUserCarbonRequestUserDetailsList({
      actionId: "110120211202",
      userId: 1101,
      corpId: "ding123",
      deptId: 2202,
      actionType: "SALARYSHEET",
      carbonAmount: "2.2",
      actionStartTime: "2021-12-01 14:52:31",
      actionEndTime: "2021-12-01 14:52:31",
      version: 1,
    });
    let writeUserCarbonRequest = new $dingtalkcarbon_1_0.WriteUserCarbonRequest({
      userDetailsList: [
        userDetailsList0
      ],
    });
    try {
      await client.writeUserCarbonWithOptions(writeUserCarbonRequest, writeUserCarbonHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcarbon_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonHeaders writeUserCarbonHeaders = new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonHeaders();
            writeUserCarbonHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonRequest.WriteUserCarbonRequestUserDetailsList userDetailsList0 = new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonRequest.WriteUserCarbonRequestUserDetailsList
            {
                ActionId = "110120211202",
                UserId = 1101,
                CorpId = "ding123",
                DeptId = 2202,
                ActionType = "SALARYSHEET",
                CarbonAmount = "2.2",
                ActionStartTime = "2021-12-01 14:52:31",
                ActionEndTime = "2021-12-01 14:52:31",
                Version = 1,
            };
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonRequest writeUserCarbonRequest = new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonRequest
            {
                UserDetailsList = new List<AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteUserCarbonRequest.WriteUserCarbonRequestUserDetailsList>
                {
                    userDetailsList0
                },
            };
            try
            {
                client.WriteUserCarbonWithOptions(writeUserCarbonRequest, writeUserCarbonHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcarbon__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

Alibabacloud_Dingtalkcarbon_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcarbon_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcarbon_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonHeaders> writeUserCarbonHeaders = make_shared<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonHeaders>();
  writeUserCarbonHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonRequestUserDetailsList> userDetailsList0 = make_shared<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonRequestUserDetailsList>(map<string, boost::any>({
    {"actionId", boost::any(string("110120211202"))},
    {"userId", boost::any(1101)},
    {"corpId", boost::any(string("ding123"))},
    {"deptId", boost::any(2202)},
    {"actionType", boost::any(string("SALARYSHEET"))},
    {"carbonAmount", boost::any(string("2.2"))},
    {"actionStartTime", boost::any(string("2021-12-01 14:52:31"))},
    {"actionEndTime", boost::any(string("2021-12-01 14:52:31"))},
    {"version", boost::any(1)}
  }));
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonRequest> writeUserCarbonRequest = make_shared<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonRequest>(map<string, boost::any>({
    {"userDetailsList", boost::any(vector<Alibabacloud_Dingtalkcarbon_1_0::WriteUserCarbonRequestUserDetailsList>({
      userDetailsList0
    }))}
  }));
  try {
    client->writeUserCarbonWithOptions(writeUserCarbonRequest, writeUserCarbonHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| success | Boolean | 请求是否成功。 |
| result | Integer | 请求返回结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : 1
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | %s | 请求参数错误，请检查方法入参 |
| 400 | invalidParameter | 请求参数列表长度过长，最大长度为100 | 请求参数列表长度过长，最大长度为100 |
| 400 | invalidParameter | 请求参数碳能量类型错误，请核对传递的数据类型 | 请求参数碳能量类型错误，请核对传递的数据类型 |
| 500 | systemError | %s | 系统错误 |
