---
title: "查询离职记录列表"
source_url: "https://open.dingtalk.com/document/development/query-the-details-of-employees-who-have-left-office"
namespace: "development"
slug: "query-the-details-of-employees-who-have-left-office"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 查询离职记录列表"
doc_id: "9mv5tZHHHP"
updated_at: "2026-06-01 15:20:41"
---

> Source: https://open.dingtalk.com/document/development/query-the-details-of-employees-who-have-left-office
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 查询离职记录列表
> Updated: 2026-06-01 15:20:41

# 查询离职记录列表

调用本接口查询企业离职记录列表，包含离职员工的离职日期、手机号码和退出企业方式等信息。

## 接口调用说明

例如，在企业智能人事应用中，2022年06月01日至2022年06月07日的离职记录如下图所示，员工小钉2的离职日期是2022年06月07日，钉钉测试的离职日期是2022年06月07日。

调用本接口查询2022年06月01日至2022年06月07日的离职记录，可获取员工小钉2和钉钉测试的离开组织的时间、手机号码和退出企业方式等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/empLeaveRecords |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.Common.Read-通讯录基本数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| startTime | String | 是 | 开始时间。  格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601/RFC 3339）。 |
| endTime | String | 否 | 结束时间。  格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601/RFC 3339）。  **[!NOTE]**     - 如果该参数不传，开始时间距离当前时间不能超过365天。 - 如果该参数传参，开始时间和结束时间跨度不能超过365天。 |
| nextToken | String | 否 | 分页游标。   - 首次查询，该参数传0。 - 非首次查询，该参数传上次调用本接口返回的nextToken。 |
| maxResults | Integer | 是 | 每页最大条目数，最大值50。 |

### 请求示例

HTTP

```
GET /v1.0/contact/empLeaveRecords?startTime=2020-07-10T00:00:00Z&endTime=2020-08-10T00:00:00Z&nextToken=0&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:afe814xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcontact_1_0.*;
import com.aliyun.dingtalkcontact_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        ListEmpLeaveRecordsHeaders listEmpLeaveRecordsHeaders = new ListEmpLeaveRecordsHeaders();
        listEmpLeaveRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListEmpLeaveRecordsRequest listEmpLeaveRecordsRequest = new ListEmpLeaveRecordsRequest()
                .setStartTime("2020-07-10T00:00:00Z")
                .setEndTime("2020-08-10T00:00:00Z")
                .setNextToken("0")
                .setMaxResults(10);
        try {
            client.listEmpLeaveRecordsWithOptions(listEmpLeaveRecordsRequest, listEmpLeaveRecordsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_emp_leave_records_headers = dingtalkcontact__1__0_models.ListEmpLeaveRecordsHeaders()
        list_emp_leave_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_emp_leave_records_request = dingtalkcontact__1__0_models.ListEmpLeaveRecordsRequest(
            start_time='2020-07-10T00:00:00Z',
            end_time='2020-08-10T00:00:00Z',
            next_token='0',
            max_results=10
        )
        try:
            client.list_emp_leave_records_with_options(list_emp_leave_records_request, list_emp_leave_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_emp_leave_records_headers = dingtalkcontact__1__0_models.ListEmpLeaveRecordsHeaders()
        list_emp_leave_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_emp_leave_records_request = dingtalkcontact__1__0_models.ListEmpLeaveRecordsRequest(
            start_time='2020-07-10T00:00:00Z',
            end_time='2020-08-10T00:00:00Z',
            next_token='0',
            max_results=10
        )
        try:
            await client.list_emp_leave_records_with_options_async(list_emp_leave_records_request, list_emp_leave_records_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListEmpLeaveRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListEmpLeaveRecordsRequest;
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
        $listEmpLeaveRecordsHeaders = new ListEmpLeaveRecordsHeaders([]);
        $listEmpLeaveRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listEmpLeaveRecordsRequest = new ListEmpLeaveRecordsRequest([
            "startTime" => "2020-07-10T00:00:00Z",
            "endTime" => "2020-08-10T00:00:00Z",
            "nextToken" => "0",
            "maxResults" => 10
        ]);
        try {
            $client->listEmpLeaveRecordsWithOptions($listEmpLeaveRecordsRequest, $listEmpLeaveRecordsHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listEmpLeaveRecordsHeaders := &dingtalkcontact_1_0.ListEmpLeaveRecordsHeaders{}
  listEmpLeaveRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listEmpLeaveRecordsRequest := &dingtalkcontact_1_0.ListEmpLeaveRecordsRequest{
    StartTime: tea.String("2020-07-10T00:00:00Z"),
    EndTime: tea.String("2020-08-10T00:00:00Z"),
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListEmpLeaveRecordsWithOptions(listEmpLeaveRecordsRequest, listEmpLeaveRecordsHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listEmpLeaveRecordsHeaders = new $dingtalkcontact_1_0.ListEmpLeaveRecordsHeaders({ });
    listEmpLeaveRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listEmpLeaveRecordsRequest = new $dingtalkcontact_1_0.ListEmpLeaveRecordsRequest({
      startTime: "2020-07-10T00:00:00Z",
      endTime: "2020-08-10T00:00:00Z",
      nextToken: "0",
      maxResults: 10,
    });
    try {
      await client.listEmpLeaveRecordsWithOptions(listEmpLeaveRecordsRequest, listEmpLeaveRecordsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListEmpLeaveRecordsHeaders listEmpLeaveRecordsHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListEmpLeaveRecordsHeaders();
            listEmpLeaveRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListEmpLeaveRecordsRequest listEmpLeaveRecordsRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListEmpLeaveRecordsRequest
            {
                StartTime = "2020-07-10T00:00:00Z",
                EndTime = "2020-08-10T00:00:00Z",
                NextToken = "0",
                MaxResults = 10,
            };
            try
            {
                client.ListEmpLeaveRecordsWithOptions(listEmpLeaveRecordsRequest, listEmpLeaveRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcontact__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcontact_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcontact_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcontact_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::ListEmpLeaveRecordsHeaders> listEmpLeaveRecordsHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::ListEmpLeaveRecordsHeaders>();
  listEmpLeaveRecordsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::ListEmpLeaveRecordsRequest> listEmpLeaveRecordsRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::ListEmpLeaveRecordsRequest>(map<string, boost::any>({
    {"startTime", boost::any(string("2020-07-10T00:00:00Z"))},
    {"endTime", boost::any(string("2020-08-10T00:00:00Z"))},
    {"nextToken", boost::any(string("0"))},
    {"maxResults", boost::any(10)}
  }));
  try {
    client->listEmpLeaveRecordsWithOptions(listEmpLeaveRecordsRequest, listEmpLeaveRecordsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| nextToken | String | 下一次请求的分页token。 |
| records | Array | 离职记录列表。 |
| userId | String | 员工的userId。 |
| name | String | 员工名字。 |
| stateCode | String | 国际电话区号。 |
| mobile | String | 手机号码。 |
| leaveTime | String | 离开组织的时间。  格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601/RFC 3339）。 |
| leaveReason | String | 退出企业方式，取值：   - **oapi**：调用接口删除 - **cancel**：注销 - **leave**：主动离职 - **unknown**：未知原因 - **delete**：管理员删除 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "DCCD7A656FFA6F07",
  "records" : [ {
    "userId" : "10000",
    "name" : "张三",
    "stateCode" : "86",
    "mobile" : "185xxxx7676",
    "leaveTime" : "2021-01-06T11:47:37Z",
    "leaveReason" : "oapi"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.param.invalid | 入参错误：%s | 入参错误 |
| 500 | system.error | 系统错误 | 系统错误 |
