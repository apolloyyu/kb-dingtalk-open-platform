---
title: "获取候选人的面试信息"
source_url: "https://open.dingtalk.com/document/development/query-the-interview-list"
namespace: "development"
slug: "query-the-interview-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 获取候选人的面试信息"
doc_id: "HwlNtBXeui"
updated_at: "2026-06-04 19:10:33"
---

> Source: https://open.dingtalk.com/document/development/query-the-interview-list
> Path: 应用开发 / 服务端 API / 智能招聘 > 获取候选人的面试信息
> Updated: 2026-06-04 19:10:33

# 获取候选人的面试信息

调用本接口分页查询候选人的面试信息，包括面试标识ID、面试的职务ID和面试官userId等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/interviews/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_recruitment\_plugin-智能招聘插件管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizCode | String | 否 | 业务标识，默认值为`ddats`。    如果传该参数，只支持`ddats`。 |
| nextToken | String | 否 | 分页游标。   - 首次调用，该参数不传。 - 非首次调用，该参数传上次调用返回的nextToken值。 |
| size | Long | 否 | 每页条目数，最大值200。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| startTimeBeginMillis | Long | 是 | 面试开始的结束时间，单位毫秒。    面试开始时间和面试结束时间跨度最大不能超过30天。 |
| startTimeEndMillis | Long | 是 | 面试开始的结束时间，单位毫秒。    面试开始时间和面试结束时间跨度最大不能超过30天。 |
| candidateId | String | 是 | 候选人标识，可调用[根据手机号获取候选人信息](0965-obtain-candidate-information-based-on-mobile-phone-number.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/ats/interviews/query?bizCode=ddats&nextToken=10&size=100 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "startTimeBeginMillis" : 1626858000000,
  "startTimeEndMillis" : 1626861600000,
  "candidateId" : "34"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkats_1_0.*;
import com.aliyun.dingtalkats_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkats_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkats_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkats_1_0.Client client = Sample.createClient();
        QueryInterviewsHeaders queryInterviewsHeaders = new QueryInterviewsHeaders();
        queryInterviewsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryInterviewsRequest queryInterviewsRequest = new QueryInterviewsRequest()
                .setStartTimeBeginMillis(1626858000000L)
                .setStartTimeEndMillis(1626861600000L)
                .setCandidateId("34");
        try {
            client.queryInterviewsWithOptions(queryInterviewsRequest, queryInterviewsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.ats_1_0.client import Client as dingtalkats_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.ats_1_0 import models as dingtalkats__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkats_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkats_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_interviews_headers = dingtalkats__1__0_models.QueryInterviewsHeaders()
        query_interviews_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_interviews_request = dingtalkats__1__0_models.QueryInterviewsRequest(
            start_time_begin_millis=1626858000000,
            start_time_end_millis=1626861600000,
            candidate_id='34'
        )
        try:
            client.query_interviews_with_options(query_interviews_request, query_interviews_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_interviews_headers = dingtalkats__1__0_models.QueryInterviewsHeaders()
        query_interviews_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_interviews_request = dingtalkats__1__0_models.QueryInterviewsRequest(
            start_time_begin_millis=1626858000000,
            start_time_end_millis=1626861600000,
            candidate_id='34'
        )
        try:
            await client.query_interviews_with_options_async(query_interviews_request, query_interviews_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\QueryInterviewsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\QueryInterviewsRequest;
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
        $queryInterviewsHeaders = new QueryInterviewsHeaders([]);
        $queryInterviewsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryInterviewsRequest = new QueryInterviewsRequest([
            "startTimeBeginMillis" => 1626858000000,
            "startTimeEndMillis" => 1626861600000,
            "candidateId" => "34"
        ]);
        try {
            $client->queryInterviewsWithOptions($queryInterviewsRequest, $queryInterviewsHeaders, new RuntimeOptions([]));
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
  dingtalkats_1_0  "github.com/alibabacloud-go/dingtalk/ats_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkats_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkats_1_0.Client{}
  _result, _err = dingtalkats_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryInterviewsHeaders := &dingtalkats_1_0.QueryInterviewsHeaders{}
  queryInterviewsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryInterviewsRequest := &dingtalkats_1_0.QueryInterviewsRequest{
    StartTimeBeginMillis: tea.Int64(1626858000000),
    StartTimeEndMillis: tea.Int64(1626861600000),
    CandidateId: tea.String("34"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryInterviewsWithOptions(queryInterviewsRequest, queryInterviewsHeaders, &util.RuntimeOptions{})
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
import dingtalkats_1_0, * as $dingtalkats_1_0 from '@alicloud/dingtalk/ats_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkats_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkats_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryInterviewsHeaders = new $dingtalkats_1_0.QueryInterviewsHeaders({ });
    queryInterviewsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryInterviewsRequest = new $dingtalkats_1_0.QueryInterviewsRequest({
      startTimeBeginMillis: 1626858000000,
      startTimeEndMillis: 1626861600000,
      candidateId: "34",
    });
    try {
      await client.queryInterviewsWithOptions(queryInterviewsRequest, queryInterviewsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkats_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkats_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkats_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.QueryInterviewsHeaders queryInterviewsHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.QueryInterviewsHeaders();
            queryInterviewsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.QueryInterviewsRequest queryInterviewsRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.QueryInterviewsRequest
            {
                StartTimeBeginMillis = 1626858000000,
                StartTimeEndMillis = 1626861600000,
                CandidateId = "34",
            };
            try
            {
                client.QueryInterviewsWithOptions(queryInterviewsRequest, queryInterviewsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkats__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkats_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkats_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkats_1_0::Client> client = make_shared<Alibabacloud_Dingtalkats_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkats_1_0::QueryInterviewsHeaders> queryInterviewsHeaders = make_shared<Alibabacloud_Dingtalkats_1_0::QueryInterviewsHeaders>();
  queryInterviewsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkats_1_0::QueryInterviewsRequest> queryInterviewsRequest = make_shared<Alibabacloud_Dingtalkats_1_0::QueryInterviewsRequest>(map<string, boost::any>({
    {"startTimeBeginMillis", boost::any(1626858000000)},
    {"startTimeEndMillis", boost::any(1626861600000)},
    {"candidateId", boost::any(string("34"))}
  }));
  try {
    client->queryInterviewsWithOptions(queryInterviewsRequest, queryInterviewsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| totalCount | Long | 数据总数。 |
| hasMore | Boolean | 是否有更多数据。   - **true**：有更多数据。 - **false**：无更多数据。 |
| nextToken | String | 下一页查询的分页游标。 |
| list | Array | 获取的面试列表。 |
| interviewId | String | 面试标识ID。 |
| jobId | String | 职位标识ID。 |
| startTimeMillis | Long | 面试开始时间，单位毫秒。 |
| endTimeMillis | Long | 面试结束时间，单位毫秒。 |
| cancelled | Boolean | 面试是否已取消。   - **true**：已取消 - **false**：未取消 |
| creatorUserId | String | 面试负责人的userId。 |
| interviewers | Array | 面试官信息列表。 |
| userId | String | 面试官userId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 23153,
  "hasMore" : true,
  "nextToken" : "100",
  "list" : [ {
    "interviewId" : "23",
    "jobId" : "45",
    "startTimeMillis" : 1626858000000,
    "endTimeMillis" : 1626861600000,
    "cancelled" : false,
    "creatorUserId" : "user01",
    "interviewers" : [ {
      "userId" : "manager01"
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | %s | 无效参数 |
| 500 | systemError | 系统错误 | 系统错误 |
