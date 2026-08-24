---
title: "查询通过流程中心集成的OA审批任务"
source_url: "https://open.dingtalk.com/document/development/query-oa-approval-tasks-integrated-through-process-center"
namespace: "development"
slug: "query-oa-approval-tasks-integrated-through-process-center"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 流程中心任务 > 查询通过流程中心集成的OA审批任务"
doc_id: "C8Qb22xkQL"
updated_at: "2026-06-03 10:12:40"
---

> Source: https://open.dingtalk.com/document/development/query-oa-approval-tasks-integrated-through-process-center
> Path: 应用开发 / 服务端API / OA 审批 > 自有 OA 审批 > 流程中心任务 > 查询通过流程中心集成的OA审批任务
> Updated: 2026-06-03 10:12:40

# 查询通过流程中心集成的OA审批任务

调用本接口，可以查询到用户运行中的审批任务。

## **接口调用说明**

- 本接口只能查询一年内的待办任务数据。
- 本接口可查询通过创建流程中心待处理任务接口，创建的的用户待处理的待办任务事项，该待办事项会同步到钉钉待办，可以在**钉钉客户端 > 待办> OA审批**中查看。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/todoTasks |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_aflow-审批流数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 任务执行人的用户userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| pageSize | Integer | 是 | 分页大小，从1开始，最大值40。 |
| pageNumber | Integer | 是 | 页码，从1开始。 |
| createBefore | Long | 否 | 查询的时间起点。    该时间距离当前时间不能超过一年。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/processCentres/todoTasks?userId=manager001&pageSize=1&pageNumber=1&createBefore=1660036833411 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.QueryIntegratedTodoTaskHeaders queryIntegratedTodoTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.QueryIntegratedTodoTaskHeaders();
        queryIntegratedTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.QueryIntegratedTodoTaskRequest queryIntegratedTodoTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.QueryIntegratedTodoTaskRequest()
                .setUserId("manager001")
                .setPageSize(1)
                .setPageNumber(1)
                .setCreateBefore(1660036833411L);
        try {
            client.queryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_integrated_todo_task_headers = dingtalkworkflow__1__0_models.QueryIntegratedTodoTaskHeaders()
        query_integrated_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_integrated_todo_task_request = dingtalkworkflow__1__0_models.QueryIntegratedTodoTaskRequest(
            user_id='manager001',
            page_size=1,
            page_number=1,
            create_before=1660036833411
        )
        try:
            client.query_integrated_todo_task_with_options(query_integrated_todo_task_request, query_integrated_todo_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_integrated_todo_task_headers = dingtalkworkflow__1__0_models.QueryIntegratedTodoTaskHeaders()
        query_integrated_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_integrated_todo_task_request = dingtalkworkflow__1__0_models.QueryIntegratedTodoTaskRequest(
            user_id='manager001',
            page_size=1,
            page_number=1,
            create_before=1660036833411
        )
        try:
            await client.query_integrated_todo_task_with_options_async(query_integrated_todo_task_request, query_integrated_todo_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\QueryIntegratedTodoTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\QueryIntegratedTodoTaskRequest;
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
        $queryIntegratedTodoTaskHeaders = new QueryIntegratedTodoTaskHeaders([]);
        $queryIntegratedTodoTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryIntegratedTodoTaskRequest = new QueryIntegratedTodoTaskRequest([
            "userId" => "manager001",
            "pageSize" => 1,
            "pageNumber" => 1,
            "createBefore" => 1660036833411
        ]);
        try {
            $client->queryIntegratedTodoTaskWithOptions($queryIntegratedTodoTaskRequest, $queryIntegratedTodoTaskHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryIntegratedTodoTaskHeaders := &dingtalkworkflow_1_0.QueryIntegratedTodoTaskHeaders{}
  queryIntegratedTodoTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryIntegratedTodoTaskRequest := &dingtalkworkflow_1_0.QueryIntegratedTodoTaskRequest{
    UserId: tea.String("manager001"),
    PageSize: tea.Int32(1),
    PageNumber: tea.Int32(1),
    CreateBefore: tea.Int64(1660036833411),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, &util.RuntimeOptions{})
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
import dingtalkworkflow_1_0, * as $dingtalkworkflow_1_0 from '@alicloud/dingtalk/workflow_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkflow_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkflow_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryIntegratedTodoTaskHeaders = new $dingtalkworkflow_1_0.QueryIntegratedTodoTaskHeaders({ });
    queryIntegratedTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryIntegratedTodoTaskRequest = new $dingtalkworkflow_1_0.QueryIntegratedTodoTaskRequest({
      userId: "manager001",
      pageSize: 1,
      pageNumber: 1,
      createBefore: 1660036833411,
    });
    try {
      await client.queryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QueryIntegratedTodoTaskHeaders queryIntegratedTodoTaskHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QueryIntegratedTodoTaskHeaders();
            queryIntegratedTodoTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QueryIntegratedTodoTaskRequest queryIntegratedTodoTaskRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QueryIntegratedTodoTaskRequest
            {
                UserId = "manager001",
                PageSize = 1,
                PageNumber = 1,
                CreateBefore = 1660036833411,
            };
            try
            {
                client.QueryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求ID。 |
| taskPage | Object | 分页结果封装。 |
| hasMore | Boolean | 是否还有下一页。   - **true**：有 - **false**：没有 |
| list | Array | 任务列表。 |
| taskId | Long | OA审批任务ID。 |
| activityId | String | 待办组ID。 |
| userId | String | 任务发起人的用户userId。 |
| status | String | 任务状态。 |
| result | String | 任务处理结果。   - **agree**：同意 - **refuse**：拒绝 |
| createTime | Long | OA审批任务创建时间。 |
| finishTime | String | OA审批任务完成时间。 |
| processInstanceId | String | 流程实例ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "axxxx1",
  "taskPage" : {
    "hasMore" : true,
    "list" : [ {
      "taskId" : 1234567,
      "activityId" : "act_0001",
      "userId" : "manager001",
      "status" : "RUNNING",
      "result" : "agree",
      "createTime" : 1660036833411,
      "finishTime" : "1660036833411",
      "processInstanceId" : "Siw2WNVZS4KiUt3tTmaNKg04*****809950"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | integrated.params.error | 参数非法，请检查分页参数跟起始时间 | 参数非法，请检查分页参数跟起始时间 |
| 400 | integrated.params.error | 用户ID不能为空，请检查 | 用户ID不能为空，请检查 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | system.error | 系统错误 | 系统错误 |
