---
title: "获取用户待审批数量"
source_url: "https://open.dingtalk.com/document/development/queries-the-number-of-requests-to-be-approved-by-users"
namespace: "development"
slug: "queries-the-number-of-requests-to-be-approved-by-users"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批任务 > 获取用户待审批数量"
doc_id: "qXRYtE7dlo"
updated_at: "2026-06-03 10:12:35"
---

> Source: https://open.dingtalk.com/document/development/queries-the-number-of-requests-to-be-approved-by-users
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批任务 > 获取用户待审批数量
> Updated: 2026-06-03 10:12:35

# 获取用户待审批数量

调用本接口，根据用户的userId获取该用户待处理的审批数量。

## **接口调用说明**

开发者可以通过以下链接，使用[打开目标](../03-Ogu5SlPY4t-客户端-JSAPI/0187-jsapi-open-link.md)页面跳转到钉钉审批的**待我审批**页面，构造地址示例请参考：https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?showmenu=false&dd\_share=false&corpid=ding1\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*288#/upcoming?swfrom=work\_homepage

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/todoTasks/numbers |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workflow.Instance.Read-工作流实例读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 要查询的用户userId。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/processes/todoTasks/numbers?userId=manager123 HTTP/1.1
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
        com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumHeaders getUserTodoTaskSumHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumHeaders();
        getUserTodoTaskSumHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumRequest getUserTodoTaskSumRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetUserTodoTaskSumRequest()
                .setUserId("manager123");
        try {
            client.getUserTodoTaskSumWithOptions(getUserTodoTaskSumRequest, getUserTodoTaskSumHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_user_todo_task_sum_headers = dingtalkworkflow__1__0_models.GetUserTodoTaskSumHeaders()
        get_user_todo_task_sum_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_todo_task_sum_request = dingtalkworkflow__1__0_models.GetUserTodoTaskSumRequest(
            user_id='manager123'
        )
        try:
            client.get_user_todo_task_sum_with_options(get_user_todo_task_sum_request, get_user_todo_task_sum_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_todo_task_sum_headers = dingtalkworkflow__1__0_models.GetUserTodoTaskSumHeaders()
        get_user_todo_task_sum_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_todo_task_sum_request = dingtalkworkflow__1__0_models.GetUserTodoTaskSumRequest(
            user_id='manager123'
        )
        try:
            await client.get_user_todo_task_sum_with_options_async(get_user_todo_task_sum_request, get_user_todo_task_sum_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetUserTodoTaskSumHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetUserTodoTaskSumRequest;
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
        $getUserTodoTaskSumHeaders = new GetUserTodoTaskSumHeaders([]);
        $getUserTodoTaskSumHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUserTodoTaskSumRequest = new GetUserTodoTaskSumRequest([
            "userId" => "manager123"
        ]);
        try {
            $client->getUserTodoTaskSumWithOptions($getUserTodoTaskSumRequest, $getUserTodoTaskSumHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  getUserTodoTaskSumHeaders := &dingtalkworkflow_1_0.GetUserTodoTaskSumHeaders{}
  getUserTodoTaskSumHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUserTodoTaskSumRequest := &dingtalkworkflow_1_0.GetUserTodoTaskSumRequest{
    UserId: tea.String("manager123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserTodoTaskSumWithOptions(getUserTodoTaskSumRequest, getUserTodoTaskSumHeaders, &util.RuntimeOptions{})
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
    let getUserTodoTaskSumHeaders = new $dingtalkworkflow_1_0.GetUserTodoTaskSumHeaders({ });
    getUserTodoTaskSumHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUserTodoTaskSumRequest = new $dingtalkworkflow_1_0.GetUserTodoTaskSumRequest({
      userId: "manager123",
    });
    try {
      await client.getUserTodoTaskSumWithOptions(getUserTodoTaskSumRequest, getUserTodoTaskSumHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetUserTodoTaskSumHeaders getUserTodoTaskSumHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetUserTodoTaskSumHeaders();
            getUserTodoTaskSumHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetUserTodoTaskSumRequest getUserTodoTaskSumRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetUserTodoTaskSumRequest
            {
                UserId = "manager123",
            };
            try
            {
                client.GetUserTodoTaskSumWithOptions(getUserTodoTaskSumRequest, getUserTodoTaskSumHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Integer | 待处理的审批数量。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : 10
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 获取用户待审批数量参数错误 | 获取用户待审批数量参数错误 |
| 400 | invalidAccessToken | 无权访问 | 无权访问 |
| 400 | invalidGetTodoTaskSumUserId | 获取用户待审批数量，要查询的用户userId不能为空 | 获取用户待审批数量，要查询的用户userId不能为空 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 500 | systemError | 系统异常 | 系统异常 |
