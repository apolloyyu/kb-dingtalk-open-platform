---
title: "更新流程中心任务状态"
source_url: "https://open.dingtalk.com/document/development/update-process-center-task-status"
namespace: "development"
slug: "update-process-center-task-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 流程中心任务 > 更新流程中心任务状态"
doc_id: "J1ZfyML41C"
updated_at: "2026-06-02 15:54:14"
---

> Source: https://open.dingtalk.com/document/development/update-process-center-task-status
> Path: 应用开发 / 服务端API / OA 审批 > 自有 OA 审批 > 流程中心任务 > 更新流程中心任务状态
> Updated: 2026-06-02 15:54:14

# 更新流程中心任务状态

调用本接口，更新流程中心中指定的待办任务状态。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/tasks |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_aflow-审批流数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 否 | OA审批流程实例ID，调用[创建实例](0513-create-a-ticket-approval-instance.md)接口获取`processInstanceId`参数值。 |
| tasks | Array | 是 | OA审批任务列表，最多20个数。 |
| taskId | Long | 是 | OA审批任务ID，可调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口获取taskId参数值。 |
| status | String | 是 | 更新为目标任务状态：   - **CANCELED**：撤销 - **COMPLETED**：完成 |
| result | String | 否 | 示例结果。   - 当status为**COMPLETED**时，必须指定任务结果：    - **AGREE**：同意   - **REFUSE**：拒绝 - 当status为**CANCELED**时，不需要传result。 |

### 请求示例

HTTP

```
PUT /v1.0/workflow/processCentres/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "processInstanceId" : "S3j8rbiNT1CsXXXXXV3Q1Q04431661334483",
  "tasks" : [ {
    "taskId" : 1234567,
    "status" : "COMPLETED",
    "result" : "AGREE"
  } ]
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.UpdateIntegratedTaskHeaders updateIntegratedTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.UpdateIntegratedTaskHeaders();
        updateIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks tasks0 = new com.aliyun.dingtalkworkflow_1_0.models.UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks()
                .setTaskId(1234567L)
                .setStatus("COMPLETED")
                .setResult("AGREE");
        com.aliyun.dingtalkworkflow_1_0.models.UpdateIntegratedTaskRequest updateIntegratedTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.UpdateIntegratedTaskRequest()
                .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                .setTasks(java.util.Arrays.asList(
                    tasks0
                ));
        try {
            client.updateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_integrated_task_headers = dingtalkworkflow__1__0_models.UpdateIntegratedTaskHeaders()
        update_integrated_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        tasks_0 = dingtalkworkflow__1__0_models.UpdateIntegratedTaskRequestTasks(
            task_id=1234567,
            status='COMPLETED',
            result='AGREE'
        )
        update_integrated_task_request = dingtalkworkflow__1__0_models.UpdateIntegratedTaskRequest(
            process_instance_id='S3j8rbiNT1CsXXXXXV3Q1Q04431661334483',
            tasks=[
                tasks_0
            ]
        )
        try:
            client.update_integrated_task_with_options(update_integrated_task_request, update_integrated_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_integrated_task_headers = dingtalkworkflow__1__0_models.UpdateIntegratedTaskHeaders()
        update_integrated_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        tasks_0 = dingtalkworkflow__1__0_models.UpdateIntegratedTaskRequestTasks(
            task_id=1234567,
            status='COMPLETED',
            result='AGREE'
        )
        update_integrated_task_request = dingtalkworkflow__1__0_models.UpdateIntegratedTaskRequest(
            process_instance_id='S3j8rbiNT1CsXXXXXV3Q1Q04431661334483',
            tasks=[
                tasks_0
            ]
        )
        try:
            await client.update_integrated_task_with_options_async(update_integrated_task_request, update_integrated_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\UpdateIntegratedTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\UpdateIntegratedTaskRequest\tasks;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\UpdateIntegratedTaskRequest;
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
        $updateIntegratedTaskHeaders = new UpdateIntegratedTaskHeaders([]);
        $updateIntegratedTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $tasks0 = new tasks([
            "taskId" => 1234567,
            "status" => "COMPLETED",
            "result" => "AGREE"
        ]);
        $updateIntegratedTaskRequest = new UpdateIntegratedTaskRequest([
            "processInstanceId" => "S3j8rbiNT1CsXXXXXV3Q1Q04431661334483",
            "tasks" => [
                $tasks0
            ]
        ]);
        try {
            $client->updateIntegratedTaskWithOptions($updateIntegratedTaskRequest, $updateIntegratedTaskHeaders, new RuntimeOptions([]));
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

  updateIntegratedTaskHeaders := &dingtalkworkflow_1_0.UpdateIntegratedTaskHeaders{}
  updateIntegratedTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tasks0 := &dingtalkworkflow_1_0.UpdateIntegratedTaskRequestTasks{
    TaskId: tea.Int64(1234567),
    Status: tea.String("COMPLETED"),
    Result: tea.String("AGREE"),
  }
  updateIntegratedTaskRequest := &dingtalkworkflow_1_0.UpdateIntegratedTaskRequest{
    ProcessInstanceId: tea.String("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483"),
    Tasks: []*dingtalkworkflow_1_0.UpdateIntegratedTaskRequestTasks{tasks0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, &util.RuntimeOptions{})
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
    let updateIntegratedTaskHeaders = new dingtalkworkflow_1_0.UpdateIntegratedTaskHeaders({ });
    updateIntegratedTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let tasks0 = new dingtalkworkflow_1_0.UpdateIntegratedTaskRequestTasks({
      taskId: 1234567,
      status: 'COMPLETED',
      result: 'AGREE',
    });
    let updateIntegratedTaskRequest = new dingtalkworkflow_1_0.UpdateIntegratedTaskRequest({
      processInstanceId: 'S3j8rbiNT1CsXXXXXV3Q1Q04431661334483',
      tasks: [
        tasks0
      ],
    });
    try {
      await client.updateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskHeaders updateIntegratedTaskHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskHeaders();
            updateIntegratedTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks tasks0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks
            {
                TaskId = 1234567,
                Status = "COMPLETED",
                Result = "AGREE",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskRequest updateIntegratedTaskRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskRequest
            {
                ProcessInstanceId = "S3j8rbiNT1CsXXXXXV3Q1Q04431661334483",
                Tasks = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks>
                {
                    tasks0
                },
            };
            try
            {
                client.UpdateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否更新成功：   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | integrated.permission.error | 非流程中心集成审批流，无权操作 | 非流程中心集成审批流，无权操作 |
| 400 | integrated.permission.error | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | integrated.state.invalid | 流程实例不存在 | 流程实例不存在 |
| 400 | internalError | %s | 系统内部错误 |
| 500 | system.error | 系统错误 | 系统错误 |
