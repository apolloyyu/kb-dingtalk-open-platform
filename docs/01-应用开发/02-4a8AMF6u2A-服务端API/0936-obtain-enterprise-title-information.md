---
title: "获取企业职务列表"
source_url: "https://open.dingtalk.com/document/development/obtain-enterprise-title-information"
namespace: "development"
slug: "obtain-enterprise-title-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 职位管理 > 获取企业职务列表"
doc_id: "WXTBvHIiX3"
updated_at: "2026-07-14 09:22:32"
---

> Source: https://open.dingtalk.com/document/development/obtain-enterprise-title-information
> Path: 应用开发 / 服务端API / 智能人事 > 职位管理 > 获取企业职务列表
> Updated: 2026-07-14 09:22:32

# 获取企业职务列表

调用本接口，分页查询企业的职务相关信息，包括职务的ID、职务名称和职务描述等信息。

## **接口调用说明**

智能人事升级职位管理功能后，需注意：

- 调用通讯录[更新用户信息v1](1455-update-user-details.md)接口和[更新用户信息v2](0057-user-information-update.md)接口更新员工部门或者员工职位时，接口会出现报错，报错信息如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0512993871/p1087123.png)
- 如果需要更新员工部门或者员工职位，请参考使用[智能人事员工调岗](0954-intelligent-personnel-staff-transfer.md)接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/jobs |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| jobName | String | 否 | 职务名称。   - **首次查询**：需先调用本接口获取jobName。 - **非首次查询**：从首次查询中的信息获取需要的jobName值。       该参数为非必填参数。 |
| nextToken | Integer | 是 | 分页游标。   - 首次调用，该参数传0。 - 非首次调用，该参数传上次调用本接口返回的nextToken。 |
| maxResults | Integer | 是 | 每页最大条目数，最大值100。 |

### 请求示例

HTTP

```
GET /v1.0/hrm/jobs?jobName=工程师&nextToken=0&maxResults=20 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:werty123
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkhrm_1_0.*;
import com.aliyun.dingtalkhrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        QueryJobsHeaders queryJobsHeaders = new QueryJobsHeaders();
        queryJobsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryJobsRequest queryJobsRequest = new QueryJobsRequest()
                .setJobName("工程师")
                .setNextToken(0)
                .setMaxResults(20);
        try {
            client.queryJobsWithOptions(queryJobsRequest, queryJobsHeaders, new RuntimeOptions());
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
        query_jobs_headers = dingtalkhrm__1__0_models.QueryJobsHeaders()
        query_jobs_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_jobs_request = dingtalkhrm__1__0_models.QueryJobsRequest(
            job_name='工程师',
            next_token=0,
            max_results=20
        )
        try:
            client.query_jobs_with_options(query_jobs_request, query_jobs_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_jobs_headers = dingtalkhrm__1__0_models.QueryJobsHeaders()
        query_jobs_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_jobs_request = dingtalkhrm__1__0_models.QueryJobsRequest(
            job_name='工程师',
            next_token=0,
            max_results=20
        )
        try:
            await client.query_jobs_with_options_async(query_jobs_request, query_jobs_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryJobsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryJobsRequest;
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
        $queryJobsHeaders = new QueryJobsHeaders([]);
        $queryJobsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryJobsRequest = new QueryJobsRequest([
            "jobName" => "工程师",
            "nextToken" => 0,
            "maxResults" => 20
        ]);
        try {
            $client->queryJobsWithOptions($queryJobsRequest, $queryJobsHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  queryJobsHeaders := &dingtalkhrm_1_0.QueryJobsHeaders{}
  queryJobsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryJobsRequest := &dingtalkhrm_1_0.QueryJobsRequest{
    JobName: tea.String("工程师"),
    NextToken: tea.Int32(0),
    MaxResults: tea.Int32(20),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryJobsWithOptions(queryJobsRequest, queryJobsHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryJobsHeaders = new $dingtalkhrm_1_0.QueryJobsHeaders({ });
    queryJobsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryJobsRequest = new $dingtalkhrm_1_0.QueryJobsRequest({
      jobName: "工程师",
      nextToken: 0,
      maxResults: 20,
    });
    try {
      await client.queryJobsWithOptions(queryJobsRequest, queryJobsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobsHeaders queryJobsHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobsHeaders();
            queryJobsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobsRequest queryJobsRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobsRequest
            {
                JobName = "工程师",
                NextToken = 0,
                MaxResults = 20,
            };
            try
            {
                client.QueryJobsWithOptions(queryJobsRequest, queryJobsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | Long | 分页游标。      如果该字段未返回，表示数据已经读取完毕。 |
| hasMore | Boolean | 是否有更多数据。   - **true**：是 - **false**：否 |
| list | Array | 职务信息列表。 |
| jobId | String | 职务ID。 |
| jobName | String | 职务名称。 |
| jobDescription | String | 职务描述。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : 0,
  "hasMore" : true,
  "list" : [ {
    "jobId" : "ac67286db74c48e28d787173ccc1a111",
    "jobName" : "总裁",
    "jobDescription" : "职务描述"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 参数错误 |
| 500 | systemError | 系统异常 | 系统异常 |
