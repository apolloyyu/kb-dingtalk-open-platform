---
title: "批量同意或拒绝审批任务"
source_url: "https://open.dingtalk.com/document/development/api-premiumbatchexecuteprocessinstances"
namespace: "development"
slug: "api-premiumbatchexecuteprocessinstances"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批任务 > 批量同意或拒绝审批任务"
doc_id: "F9q1n3Pi47"
updated_at: "2026-06-03 10:12:55"
---

> Source: https://open.dingtalk.com/document/development/api-premiumbatchexecuteprocessinstances
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批任务 > 批量同意或拒绝审批任务
> Updated: 2026-06-03 10:12:55

# 批量同意或拒绝审批任务

调用本接口，使用指定的userId和任务result及评论remark，对一批具有不同审批实例ID、任务节点ID的审批任务，进行批量处理。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

审批流程可以包含多个审批节点，单个审批节点可能包含一个或多个审批任务。操作单个审批任务，不代表审批流程结束。

> **[!NOTE]**
>
> 批量同意或拒绝审批任务暂不支持上传附件。

- 审批流程只有一个审批人，对单个审批任务操作同意或拒绝，审批流程结束。

  ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1064156361/p349526.png)
- 审批流程有多个审批人，整个审批流程受多个任务影响。

  - 对单个审批任务操作拒绝，审批流程结束。
  - 对单个审批任务操作同意，审批流程转到下一个审批人。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5772540871/p1076253.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processInstances/batchExecute |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskInfoList | Array | 是 | 任务详情列表。  最多一次可以提交10个 |
| taskId | Long | 是 | 任务ID，可调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取`taskId`参数值。 |
| processInstanceId | String | 是 | 审批实例ID。   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| actionerUserId | String | 是 | 实际执行人用户ID，可通过调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取。 |
| result | String | 是 | 审批操作，取值：   - **agree**：同意 - **refuse**：拒绝 |
| remark | String | 否 | 审批意见，可为空。      最长1024个字符。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processInstances/batchExecute HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:9e86b42f968c3b958d
Content-Type:application/json

{
  "taskInfoList" : [ {
    "taskId" : 12345,
    "processInstanceId" : "a171de6c-8bxxxx"
  } ],
  "actionerUserId" : "67583405630",
  "result" : "agree",
  "remark" : "Test for batch agree"
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
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumBatchExecuteProcessInstancesHeaders premiumBatchExecuteProcessInstancesHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumBatchExecuteProcessInstancesHeaders();
        premiumBatchExecuteProcessInstancesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList taskInfoList0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList()
                .setTaskId(12345L)
                .setProcessInstanceId("a171de6c-8bxxxx");
        com.aliyun.dingtalkworkflow_1_0.models.PremiumBatchExecuteProcessInstancesRequest premiumBatchExecuteProcessInstancesRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumBatchExecuteProcessInstancesRequest()
                .setTaskInfoList(java.util.Arrays.asList(
                    taskInfoList0
                ))
                .setActionerUserId("67583405630")
                .setResult("agree")
                .setRemark("Test for batch agree");
        try {
            client.premiumBatchExecuteProcessInstancesWithOptions(premiumBatchExecuteProcessInstancesRequest, premiumBatchExecuteProcessInstancesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_batch_execute_process_instances_headers = dingtalkworkflow__1__0_models.PremiumBatchExecuteProcessInstancesHeaders()
        premium_batch_execute_process_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        task_info_list_0 = dingtalkworkflow__1__0_models.PremiumBatchExecuteProcessInstancesRequestTaskInfoList(
            task_id=12345,
            process_instance_id='a171de6c-8bxxxx'
        )
        premium_batch_execute_process_instances_request = dingtalkworkflow__1__0_models.PremiumBatchExecuteProcessInstancesRequest(
            task_info_list=[
                task_info_list_0
            ],
            actioner_user_id='67583405630',
            result='agree',
            remark='Test for batch agree'
        )
        try:
            client.premium_batch_execute_process_instances_with_options(premium_batch_execute_process_instances_request, premium_batch_execute_process_instances_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_batch_execute_process_instances_headers = dingtalkworkflow__1__0_models.PremiumBatchExecuteProcessInstancesHeaders()
        premium_batch_execute_process_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        task_info_list_0 = dingtalkworkflow__1__0_models.PremiumBatchExecuteProcessInstancesRequestTaskInfoList(
            task_id=12345,
            process_instance_id='a171de6c-8bxxxx'
        )
        premium_batch_execute_process_instances_request = dingtalkworkflow__1__0_models.PremiumBatchExecuteProcessInstancesRequest(
            task_info_list=[
                task_info_list_0
            ],
            actioner_user_id='67583405630',
            result='agree',
            remark='Test for batch agree'
        )
        try:
            await client.premium_batch_execute_process_instances_with_options_async(premium_batch_execute_process_instances_request, premium_batch_execute_process_instances_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumBatchExecuteProcessInstancesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumBatchExecuteProcessInstancesRequest\taskInfoList;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumBatchExecuteProcessInstancesRequest;
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
        $premiumBatchExecuteProcessInstancesHeaders = new PremiumBatchExecuteProcessInstancesHeaders([]);
        $premiumBatchExecuteProcessInstancesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $taskInfoList0 = new taskInfoList([
            "taskId" => 12345,
            "processInstanceId" => "a171de6c-8bxxxx"
        ]);
        $premiumBatchExecuteProcessInstancesRequest = new PremiumBatchExecuteProcessInstancesRequest([
            "taskInfoList" => [
                $taskInfoList0
            ],
            "actionerUserId" => "67583405630",
            "result" => "agree",
            "remark" => "Test for batch agree"
        ]);
        try {
            $client->premiumBatchExecuteProcessInstancesWithOptions($premiumBatchExecuteProcessInstancesRequest, $premiumBatchExecuteProcessInstancesHeaders, new RuntimeOptions([]));
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

  premiumBatchExecuteProcessInstancesHeaders := &dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesHeaders{}
  premiumBatchExecuteProcessInstancesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  taskInfoList0 := &dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesRequestTaskInfoList{
    TaskId: tea.Int64(12345),
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
  }
  premiumBatchExecuteProcessInstancesRequest := &dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesRequest{
    TaskInfoList: []*dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesRequestTaskInfoList{taskInfoList0},
    ActionerUserId: tea.String("67583405630"),
    Result: tea.String("agree"),
    Remark: tea.String("Test for batch agree"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumBatchExecuteProcessInstancesWithOptions(premiumBatchExecuteProcessInstancesRequest, premiumBatchExecuteProcessInstancesHeaders, &util.RuntimeOptions{})
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
    let premiumBatchExecuteProcessInstancesHeaders = new dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesHeaders({ });
    premiumBatchExecuteProcessInstancesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let taskInfoList0 = new dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesRequestTaskInfoList({
      taskId: 12345,
      processInstanceId: 'a171de6c-8bxxxx',
    });
    let premiumBatchExecuteProcessInstancesRequest = new dingtalkworkflow_1_0.PremiumBatchExecuteProcessInstancesRequest({
      taskInfoList: [
        taskInfoList0
      ],
      actionerUserId: '67583405630',
      result: 'agree',
      remark: 'Test for batch agree',
    });
    try {
      await client.premiumBatchExecuteProcessInstancesWithOptions(premiumBatchExecuteProcessInstancesRequest, premiumBatchExecuteProcessInstancesHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesHeaders premiumBatchExecuteProcessInstancesHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesHeaders();
            premiumBatchExecuteProcessInstancesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList taskInfoList0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList
            {
                TaskId = 12345,
                ProcessInstanceId = "a171de6c-8bxxxx",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesRequest premiumBatchExecuteProcessInstancesRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesRequest
            {
                TaskInfoList = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumBatchExecuteProcessInstancesRequest.PremiumBatchExecuteProcessInstancesRequestTaskInfoList>
                {
                    taskInfoList0
                },
                ActionerUserId = "67583405630",
                Result = "agree",
                Remark = "Test for batch agree",
            };
            try
            {
                client.PremiumBatchExecuteProcessInstancesWithOptions(premiumBatchExecuteProcessInstancesRequest, premiumBatchExecuteProcessInstancesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 请求是否成功。 |
| result | Map<String, Object> | 任务结果。      数据格式为map，key是字符串形式taskId。 |
|  | Object | 单个taskId的执行结果。 |
| result | Boolean | 审批结果。 |
| message | String | 审批结果信息。      ok表示无异常，其余会提示异常原因。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "79992131307" : {
      "result" : true,
      "message" : "ok"
    },
    "79843140568" : {
      "result" : false,
      "message" : "任务不属于该流程实例"
    }
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 同意或拒绝审批任务参数错误 | 同意或拒绝审批任务参数错误 |
| 400 | needAuth | 没有同意拒绝审批的权限 | 没有同意拒绝审批的权限 |
| 400 | invalidAgentld | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidInstanceExecuteActionerUserld | 同意拒绝审批任务，操作人的userld不能为空 | 同意拒绝审批任务，操作人的userld不能为空 |
| 400 | invalidInstanceExecuteResult | 同意拒绝审批任务，审批操作取值必填 且值必须为agree或refuse | 同意拒绝审批任务，审批操作取值必填 且值必须为agree或refuse |
| 400 | aflowProcessFormDatalsNull | 流程表单数据为空 | 流程表单数据为空 |
| 400 | aflowProcessInstStatusException | 审批单状态异常 | 审批单状态异常 |
| 400 | taskInfoSizeOverLimit | 任务信息队列超出上限 | 任务信息队列超出上限 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
