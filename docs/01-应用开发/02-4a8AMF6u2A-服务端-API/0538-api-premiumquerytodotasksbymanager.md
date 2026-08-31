---
title: "管理员查询指定员工的待处理任务列表"
source_url: "https://open.dingtalk.com/document/development/api-premiumquerytodotasksbymanager"
namespace: "development"
slug: "api-premiumquerytodotasksbymanager"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批任务 > 管理员查询指定员工的待处理任务列表"
doc_id: "iGvGnFyrnC"
updated_at: "2026-06-03 10:12:56"
---

> Source: https://open.dingtalk.com/document/development/api-premiumquerytodotasksbymanager
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批任务 > 管理员查询指定员工的待处理任务列表
> Updated: 2026-06-03 10:12:56

# 管理员查询指定员工的待处理任务列表

本接口为组织管理员提供待处理任务查询服务，通过管理员(managerUserId) 查询当前审批人UserId的所有待处理的OA审批任务信息，支持在职员工和离职员工的待处理任务查询。

## **接口调用说明**

当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/tasks/todoTasks |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | Integer | 是 | 分页标识，从1开始。 |
| maxResults | Integer | 是 | 分页大小，最大值20。 |
| actionerUserId | String | 是 | 操作人userId。 |
| managerUserId | String | 是 | 管理员userId。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/premium/tasks/todoTasks?nextToken=1&maxResults=20&actionerUserId=staffId123&managerUserId=manager123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumQueryTodoTasksByManagerHeaders premiumQueryTodoTasksByManagerHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumQueryTodoTasksByManagerHeaders();
        premiumQueryTodoTasksByManagerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumQueryTodoTasksByManagerRequest premiumQueryTodoTasksByManagerRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumQueryTodoTasksByManagerRequest()
                .setNextToken(1)
                .setMaxResults(20)
                .setActionerUserId("staffId123")
                .setManagerUserId("manager123");
        try {
            client.premiumQueryTodoTasksByManagerWithOptions(premiumQueryTodoTasksByManagerRequest, premiumQueryTodoTasksByManagerHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_query_todo_tasks_by_manager_headers = dingtalkworkflow__1__0_models.PremiumQueryTodoTasksByManagerHeaders()
        premium_query_todo_tasks_by_manager_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_query_todo_tasks_by_manager_request = dingtalkworkflow__1__0_models.PremiumQueryTodoTasksByManagerRequest(
            next_token=1,
            max_results=20,
            actioner_user_id='staffId123',
            manager_user_id='manager123'
        )
        try:
            client.premium_query_todo_tasks_by_manager_with_options(premium_query_todo_tasks_by_manager_request, premium_query_todo_tasks_by_manager_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_query_todo_tasks_by_manager_headers = dingtalkworkflow__1__0_models.PremiumQueryTodoTasksByManagerHeaders()
        premium_query_todo_tasks_by_manager_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_query_todo_tasks_by_manager_request = dingtalkworkflow__1__0_models.PremiumQueryTodoTasksByManagerRequest(
            next_token=1,
            max_results=20,
            actioner_user_id='staffId123',
            manager_user_id='manager123'
        )
        try:
            await client.premium_query_todo_tasks_by_manager_with_options_async(premium_query_todo_tasks_by_manager_request, premium_query_todo_tasks_by_manager_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumQueryTodoTasksByManagerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumQueryTodoTasksByManagerRequest;
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
        $premiumQueryTodoTasksByManagerHeaders = new PremiumQueryTodoTasksByManagerHeaders([]);
        $premiumQueryTodoTasksByManagerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumQueryTodoTasksByManagerRequest = new PremiumQueryTodoTasksByManagerRequest([
            "nextToken" => 1,
            "maxResults" => 20,
            "actionerUserId" => "staffId123",
            "managerUserId" => "manager123"
        ]);
        try {
            $client->premiumQueryTodoTasksByManagerWithOptions($premiumQueryTodoTasksByManagerRequest, $premiumQueryTodoTasksByManagerHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
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

  premiumQueryTodoTasksByManagerHeaders := &dingtalkworkflow_1_0.PremiumQueryTodoTasksByManagerHeaders{}
  premiumQueryTodoTasksByManagerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumQueryTodoTasksByManagerRequest := &dingtalkworkflow_1_0.PremiumQueryTodoTasksByManagerRequest{
    NextToken: tea.Int32(1),
    MaxResults: tea.Int32(20),
    ActionerUserId: tea.String("staffId123"),
    ManagerUserId: tea.String("manager123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumQueryTodoTasksByManagerWithOptions(premiumQueryTodoTasksByManagerRequest, premiumQueryTodoTasksByManagerHeaders, &util.RuntimeOptions{})
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
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
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
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let premiumQueryTodoTasksByManagerHeaders = new dingtalkworkflow_1_0.PremiumQueryTodoTasksByManagerHeaders({ });
    premiumQueryTodoTasksByManagerHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumQueryTodoTasksByManagerRequest = new dingtalkworkflow_1_0.PremiumQueryTodoTasksByManagerRequest({
      nextToken: 1,
      maxResults: 20,
      actionerUserId: 'staffId123',
      managerUserId: 'manager123',
    });
    try {
      await client.premiumQueryTodoTasksByManagerWithOptions(premiumQueryTodoTasksByManagerRequest, premiumQueryTodoTasksByManagerHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQueryTodoTasksByManagerHeaders premiumQueryTodoTasksByManagerHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQueryTodoTasksByManagerHeaders();
            premiumQueryTodoTasksByManagerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQueryTodoTasksByManagerRequest premiumQueryTodoTasksByManagerRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQueryTodoTasksByManagerRequest
            {
                NextToken = 1,
                MaxResults = 20,
                ActionerUserId = "staffId123",
                ManagerUserId = "manager123",
            };
            try
            {
                client.PremiumQueryTodoTasksByManagerWithOptions(premiumQueryTodoTasksByManagerRequest, premiumQueryTodoTasksByManagerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| hasMore | Boolean | 是否有下一页。 |
| list | Array | 结果列表。 |
| taskId | Long | OA审批任务ID。 |
| processCode | String | 审批模板唯一编码。 |
| title | String | 任务标题。 |
| businessId | String | 流程实例业务编号ID。 |
| processInstanceId | String | 流程实例ID。 |
| userId | String | OA审批任务发起人的用户userId。 |
| canRedirect | Boolean | 是否可转交。（基础规则，例如外部审批流程任务，不可转交） |
| createTime | Long | 审批任务创建时间，时间戳格式。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "hasMore" : true,
    "list" : [ {
      "taskId" : 1234567,
      "processCode" : "PROC-abcd",
      "title" : "xxx提交的通用审批",
      "businessId" : "202212061736000123456",
      "processInstanceId" : "Siw2WNVZS4KiUt3tTmaNKg04*****809950",
      "userId" : "userId-A",
      "canRedirect" : true,
      "createTime" : 1670319395000
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.user.notexist | 查询的staffId不存在 | 查询的userId在当前组织不存在 |
| 400 | param.manager.notexist | 查询的managerUserId不存在 | 查询的managerUserId无管理权限 |
| 400 | qps.exceed.limit | 请求过于频繁 | 超过调用并发上限 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 500 | system.error | 系统错误 | 系统错误 |
