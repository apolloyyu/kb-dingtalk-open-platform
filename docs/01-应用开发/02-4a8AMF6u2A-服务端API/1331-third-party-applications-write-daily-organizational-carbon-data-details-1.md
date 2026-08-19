---
title: "写入每日组织碳数据明细信息"
source_url: "https://open.dingtalk.com/document/development/third-party-applications-write-daily-organizational-carbon-data-details-1"
namespace: "development"
slug: "third-party-applications-write-daily-organizational-carbon-data-details-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉钉碳中和 > 写入每日组织碳数据明细信息"
doc_id: "3rrWiWMZ5X"
updated_at: "2026-01-29 14:20:20"
---

> Source: https://open.dingtalk.com/document/development/third-party-applications-write-daily-organizational-carbon-data-details-1
> Path: 应用开发 / 服务端API / 更多开放 > 钉钉碳中和 > 写入每日组织碳数据明细信息
> Updated: 2026-01-29 14:20:20

# 写入每日组织碳数据明细信息

通过此接口可上报组织每日的碳减排明细数据，包括减碳行为类型、减碳量、发生时间等信息，用于企业碳排放管理平台的数据同步与统计分析。

## 接口调用说明

适用于企业或第三方环保应用每日向钉钉平台同步组织级减碳明细数据。典型业务场景包括：

- 企业内部碳管理平台按日汇总各部门员工的绿色办公行为（如无纸化审批、在线会议）并上报减排数据。
- 第三方环保应用对接钉钉，将用户在应用内的低碳行为（如电子签章使用、远程打卡）转化为碳能量，并按部门维度批量上报。
- 支持基于`actionId`进行数据订正，确保碳数据的准确性和可追溯性。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/carbon/orgDetails/write |
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
| orgDetailsList | Array | 是 | 请求参数。 |
| actionId | String | 是 | 全局唯一ID，用于数据订正。 |
| corpId | String | 是 | 钉钉组织的corpId。 |
| deptId | Long | 是 | 钉钉部门ID。 |
| actionType | String | 是 | 碳能量减排来源。 |
| carbonAmount | String | 是 | 碳能量克数。 |
| actionTime | String | 是 | 减排行为发生时间。 |
| version | Integer | 是 | 版本号，默认为1。 |

### 请求示例

HTTP

```
POST /v1.0/carbon/orgDetails/write HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "orgDetailsList" : [ {
    "actionId" : "110120211202",
    "corpId" : "ding123",
    "deptId" : 1101,
    "actionType" : "SALARYSHEET",
    "carbonAmount" : "2.1",
    "actionTime" : "2021-12-01 14:52:31",
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
        WriteOrgCarbonHeaders writeOrgCarbonHeaders = new WriteOrgCarbonHeaders();
        writeOrgCarbonHeaders.xAcsDingtalkAccessToken = "<your access token>";
        WriteOrgCarbonRequest.WriteOrgCarbonRequestOrgDetailsList orgDetailsList0 = new WriteOrgCarbonRequest.WriteOrgCarbonRequestOrgDetailsList()
                .setActionId("110120211202")
                .setCorpId("ding123")
                .setDeptId(1101L)
                .setActionType("SALARYSHEET")
                .setCarbonAmount("2.1")
                .setActionTime("2021-12-01 14:52:31")
                .setVersion(1);
        WriteOrgCarbonRequest writeOrgCarbonRequest = new WriteOrgCarbonRequest()
                .setOrgDetailsList(java.util.Arrays.asList(
                    orgDetailsList0
                ));
        try {
            client.writeOrgCarbonWithOptions(writeOrgCarbonRequest, writeOrgCarbonHeaders, new RuntimeOptions());
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
        write_org_carbon_headers = dingtalkcarbon__1__0_models.WriteOrgCarbonHeaders()
        write_org_carbon_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_details_list_0 = dingtalkcarbon__1__0_models.WriteOrgCarbonRequestOrgDetailsList(
            action_id='110120211202',
            corp_id='ding123',
            dept_id=1101,
            action_type='SALARYSHEET',
            carbon_amount='2.1',
            action_time='2021-12-01 14:52:31',
            version=1
        )
        write_org_carbon_request = dingtalkcarbon__1__0_models.WriteOrgCarbonRequest(
            org_details_list=[
                org_details_list_0
            ]
        )
        try:
            client.write_org_carbon_with_options(write_org_carbon_request, write_org_carbon_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        write_org_carbon_headers = dingtalkcarbon__1__0_models.WriteOrgCarbonHeaders()
        write_org_carbon_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_details_list_0 = dingtalkcarbon__1__0_models.WriteOrgCarbonRequestOrgDetailsList(
            action_id='110120211202',
            corp_id='ding123',
            dept_id=1101,
            action_type='SALARYSHEET',
            carbon_amount='2.1',
            action_time='2021-12-01 14:52:31',
            version=1
        )
        write_org_carbon_request = dingtalkcarbon__1__0_models.WriteOrgCarbonRequest(
            org_details_list=[
                org_details_list_0
            ]
        )
        try:
            await client.write_org_carbon_with_options_async(write_org_carbon_request, write_org_carbon_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Models\WriteOrgCarbonHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Models\WriteOrgCarbonRequest\orgDetailsList;
use AlibabaCloud\SDK\Dingtalk\Vcarbon_1_0\Models\WriteOrgCarbonRequest;
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
        $writeOrgCarbonHeaders = new WriteOrgCarbonHeaders([]);
        $writeOrgCarbonHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $orgDetailsList0 = new orgDetailsList([
            "actionId" => "110120211202",
            "corpId" => "ding123",
            "deptId" => 1101,
            "actionType" => "SALARYSHEET",
            "carbonAmount" => "2.1",
            "actionTime" => "2021-12-01 14:52:31",
            "version" => 1
        ]);
        $writeOrgCarbonRequest = new WriteOrgCarbonRequest([
            "orgDetailsList" => [
                $orgDetailsList0
            ]
        ]);
        try {
            $client->writeOrgCarbonWithOptions($writeOrgCarbonRequest, $writeOrgCarbonHeaders, new RuntimeOptions([]));
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

  writeOrgCarbonHeaders := &dingtalkcarbon_1_0.WriteOrgCarbonHeaders{}
  writeOrgCarbonHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  orgDetailsList0 := &dingtalkcarbon_1_0.WriteOrgCarbonRequestOrgDetailsList{
    ActionId: tea.String("110120211202"),
    CorpId: tea.String("ding123"),
    DeptId: tea.Int64(1101),
    ActionType: tea.String("SALARYSHEET"),
    CarbonAmount: tea.String("2.1"),
    ActionTime: tea.String("2021-12-01 14:52:31"),
    Version: tea.Int32(1),
  }
  writeOrgCarbonRequest := &dingtalkcarbon_1_0.WriteOrgCarbonRequest{
    OrgDetailsList: []*dingtalkcarbon_1_0.WriteOrgCarbonRequestOrgDetailsList{orgDetailsList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.WriteOrgCarbonWithOptions(writeOrgCarbonRequest, writeOrgCarbonHeaders, &util.RuntimeOptions{})
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
    let writeOrgCarbonHeaders = new $dingtalkcarbon_1_0.WriteOrgCarbonHeaders({ });
    writeOrgCarbonHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let orgDetailsList0 = new $dingtalkcarbon_1_0.WriteOrgCarbonRequestOrgDetailsList({
      actionId: "110120211202",
      corpId: "ding123",
      deptId: 1101,
      actionType: "SALARYSHEET",
      carbonAmount: "2.1",
      actionTime: "2021-12-01 14:52:31",
      version: 1,
    });
    let writeOrgCarbonRequest = new $dingtalkcarbon_1_0.WriteOrgCarbonRequest({
      orgDetailsList: [
        orgDetailsList0
      ],
    });
    try {
      await client.writeOrgCarbonWithOptions(writeOrgCarbonRequest, writeOrgCarbonHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonHeaders writeOrgCarbonHeaders = new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonHeaders();
            writeOrgCarbonHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonRequest.WriteOrgCarbonRequestOrgDetailsList orgDetailsList0 = new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonRequest.WriteOrgCarbonRequestOrgDetailsList
            {
                ActionId = "110120211202",
                CorpId = "ding123",
                DeptId = 1101,
                ActionType = "SALARYSHEET",
                CarbonAmount = "2.1",
                ActionTime = "2021-12-01 14:52:31",
                Version = 1,
            };
            AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonRequest writeOrgCarbonRequest = new AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonRequest
            {
                OrgDetailsList = new List<AlibabaCloud.SDK.Dingtalkcarbon_1_0.Models.WriteOrgCarbonRequest.WriteOrgCarbonRequestOrgDetailsList>
                {
                    orgDetailsList0
                },
            };
            try
            {
                client.WriteOrgCarbonWithOptions(writeOrgCarbonRequest, writeOrgCarbonHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonHeaders> writeOrgCarbonHeaders = make_shared<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonHeaders>();
  writeOrgCarbonHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonRequestOrgDetailsList> orgDetailsList0 = make_shared<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonRequestOrgDetailsList>(map<string, boost::any>({
    {"actionId", boost::any(string("110120211202"))},
    {"corpId", boost::any(string("ding123"))},
    {"deptId", boost::any(1101)},
    {"actionType", boost::any(string("SALARYSHEET"))},
    {"carbonAmount", boost::any(string("2.1"))},
    {"actionTime", boost::any(string("2021-12-01 14:52:31"))},
    {"version", boost::any(1)}
  }));
  shared_ptr<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonRequest> writeOrgCarbonRequest = make_shared<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonRequest>(map<string, boost::any>({
    {"orgDetailsList", boost::any(vector<Alibabacloud_Dingtalkcarbon_1_0::WriteOrgCarbonRequestOrgDetailsList>({
      orgDetailsList0
    }))}
  }));
  try {
    client->writeOrgCarbonWithOptions(writeOrgCarbonRequest, writeOrgCarbonHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Integer | 写入成功的条数。 |

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
