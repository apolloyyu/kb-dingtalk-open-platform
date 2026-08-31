---
title: "根据processCode分页获取审批流程数据"
source_url: "https://open.dingtalk.com/document/development/api-premiumgetprocessinstances"
namespace: "development"
slug: "api-premiumgetprocessinstances"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 根据processCode分页获取审批流程数据"
doc_id: "CRVp7xBqB2"
updated_at: "2026-06-03 10:12:49"
---

> Source: https://open.dingtalk.com/document/development/api-premiumgetprocessinstances
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 根据processCode分页获取审批流程数据
> Updated: 2026-06-03 10:12:49

# 根据processCode分页获取审批流程数据

调用本接口，根据processCode分页获取审批流程数据，包括表单提交时间、表单实例ID、提交人姓名、表单实例详情数据等信息。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

- 当前接口针对OA高级版客户可支持查询最多5年内的实例数据（即startTime时间距当前时间不能超过5年）。
- 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天（即一次查询最多只能查询120天的数据），**endTime**不传则默认取当前时间。
- 如果传入**startTime**参数和**endTime**参数，要求时间范围不能超过120天，同时**startTime**时间距当前时间不能超过5年（即最多可支持查询5年内的实例数据）。
- 批量获取的实例ID个数（循环获取），最多不能超过10000个，建议分多次获取。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processes/pages/instances |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，企业内部应用可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数传1。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Long | 是 | 分页参数，每页大小，最多传20。 |
| startTimeInMills | Long | 是 | 审批实例开始时间，Unix时间戳，单位毫秒。       - 例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.10 00:00:00对应的时间戳1586448000000。 - 针对OA高级版用户，**startTime**时间距当前时间不能超过5年，即最多可支持查询5年内的实例数据。 - 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天，即一次查询最多只能查询120天的数据。 |
| endTimeInMills | Long | 否 | 审批实例结束时间，Unix时间戳，单位毫秒。       - 例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.14 23:59:59对应的时间戳1586879999000。 - **endTime**不传则默认取当前时间。 |
| processCode | String | 是 | 模板ID。   - 通过调用[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口获取。 - 通过[OA审批概述-名词解释](0473-workflow-overview.md)获取。 |
| appUuid | String | 否 | 应用搭建ID，默认可传企业corpId值。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/premium/processes/pages/instances?nextToken=1&maxResults=10&startTimeInMills=1631289600000&endTimeInMills=1633795200000&processCode=PROC-C53-example&appUuid=SWAPP-4C2F4B-example HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BWExxx
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
        
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetProcessInstancesHeaders premiumGetProcessInstancesHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetProcessInstancesHeaders();
        premiumGetProcessInstancesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetProcessInstancesRequest premiumGetProcessInstancesRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetProcessInstancesRequest()
                .setNextToken("1")
                .setMaxResults(10L)
                .setStartTimeInMills(1631289600000L)
                .setEndTimeInMills(1633795200000L)
                .setProcessCode("PROC-C53-example")
                .setAppUuid("SWAPP-4C2F4B-example");
        try {
            client.premiumGetProcessInstancesWithOptions(premiumGetProcessInstancesRequest, premiumGetProcessInstancesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_get_process_instances_headers = dingtalkworkflow__1__0_models.PremiumGetProcessInstancesHeaders()
        premium_get_process_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_process_instances_request = dingtalkworkflow__1__0_models.PremiumGetProcessInstancesRequest(
            next_token='1',
            max_results=10,
            start_time_in_mills=1631289600000,
            end_time_in_mills=1633795200000,
            process_code='PROC-C53-example',
            app_uuid='SWAPP-4C2F4B-example'
        )
        try:
            client.premium_get_process_instances_with_options(premium_get_process_instances_request, premium_get_process_instances_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_get_process_instances_headers = dingtalkworkflow__1__0_models.PremiumGetProcessInstancesHeaders()
        premium_get_process_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_process_instances_request = dingtalkworkflow__1__0_models.PremiumGetProcessInstancesRequest(
            next_token='1',
            max_results=10,
            start_time_in_mills=1631289600000,
            end_time_in_mills=1633795200000,
            process_code='PROC-C53-example',
            app_uuid='SWAPP-4C2F4B-example'
        )
        try:
            await client.premium_get_process_instances_with_options_async(premium_get_process_instances_request, premium_get_process_instances_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetProcessInstancesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetProcessInstancesRequest;
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
        $premiumGetProcessInstancesHeaders = new PremiumGetProcessInstancesHeaders([]);
        $premiumGetProcessInstancesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumGetProcessInstancesRequest = new PremiumGetProcessInstancesRequest([
            "nextToken" => "1",
            "maxResults" => 10,
            "startTimeInMills" => 1631289600000,
            "endTimeInMills" => 1633795200000,
            "processCode" => "PROC-C53-example",
            "appUuid" => "SWAPP-4C2F4B-example"
        ]);
        try {
            $client->premiumGetProcessInstancesWithOptions($premiumGetProcessInstancesRequest, $premiumGetProcessInstancesHeaders, new RuntimeOptions([]));
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

  premiumGetProcessInstancesHeaders := &dingtalkworkflow_1_0.PremiumGetProcessInstancesHeaders{}
  premiumGetProcessInstancesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumGetProcessInstancesRequest := &dingtalkworkflow_1_0.PremiumGetProcessInstancesRequest{
    NextToken: tea.String("1"),
    MaxResults: tea.Int64(10),
    StartTimeInMills: tea.Int64(1631289600000),
    EndTimeInMills: tea.Int64(1633795200000),
    ProcessCode: tea.String("PROC-C53-example"),
    AppUuid: tea.String("SWAPP-4C2F4B-example"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumGetProcessInstancesWithOptions(premiumGetProcessInstancesRequest, premiumGetProcessInstancesHeaders, &util.RuntimeOptions{})
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
    let premiumGetProcessInstancesHeaders = new dingtalkworkflow_1_0.PremiumGetProcessInstancesHeaders({ });
    premiumGetProcessInstancesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumGetProcessInstancesRequest = new dingtalkworkflow_1_0.PremiumGetProcessInstancesRequest({
      nextToken: '1',
      maxResults: 10,
      startTimeInMills: 1631289600000,
      endTimeInMills: 1633795200000,
      processCode: 'PROC-C53-example',
      appUuid: 'SWAPP-4C2F4B-example',
    });
    try {
      await client.premiumGetProcessInstancesWithOptions(premiumGetProcessInstancesRequest, premiumGetProcessInstancesHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetProcessInstancesHeaders premiumGetProcessInstancesHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetProcessInstancesHeaders();
            premiumGetProcessInstancesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetProcessInstancesRequest premiumGetProcessInstancesRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetProcessInstancesRequest
            {
                NextToken = "1",
                MaxResults = 10,
                StartTimeInMills = 1631289600000,
                EndTimeInMills = 1633795200000,
                ProcessCode = "PROC-C53-example",
                AppUuid = "SWAPP-4C2F4B-example",
            };
            try
            {
                client.PremiumGetProcessInstancesWithOptions(premiumGetProcessInstancesRequest, premiumGetProcessInstancesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | String | 下一次请求的分页游标。 |
| hasMore | Boolean | 是否有更多数据。 |
| maxResults | Long | 分页大小。 |
| list | Array | 审批流程数据列表。 |
| processInstanceId | String | 流程实例ID。 |
| mainProcessInstanceId | String | 主单实例ID。 |
| finishTime | Long | 审批结束时间。 |
| finishTimeInMills | Long | 审批结束时间，Unix时间戳，单位毫秒。 |
| attachedProcessInstanceIds | String | 附属单信息。 |
| businessId | String | 审批单编号。 |
| title | String | 审批单标题。 |
| originatorDeptId | String | 发起人部门ID。      默认值-1：表示企业根部门。 |
| result | String | 审批结果，取值：   - \*\* agree\*\*：同意 - \*\* refuse\*\*：拒绝 |
| createTime | Long | 审批单创建时间。 |
| createTimeInMills | Long | 审批单创建时间，Unix时间戳，单位毫秒。 |
| originatorUserid | String | 发起者userId。 |
| status | String | 审批单状态，取值：   - **RUNNING**：审批中 - **TERMINATED**：撤销 - **COMPLETED**：审批完成 |
| formComponentValues | Array | 表单实例数据列表。 |
| name | String | 控件名称。 |
| id | String | 控件ID。 |
| value | String | 控件数据。 |
| extValue | String | 控件扩展数据。 |
| operationRecords | Array | 审批单操作记录列表。 |
| timestamp | Long | 操作时间戳。 |
| result | String | 操作结果，取值：   - **AGREE**：同意 - **REFUSE**：拒绝 - **NONE**：未知 |
| operationType | String | 操作类型，取值：   - **EXECUTE\_TASK\_NORMAL**：正常执行任务 - **EXECUTE\_TASK\_AGENT**：代理人执行任务 - **APPEND\_TASK\_BEFORE**：前加签任务 - **APPEND\_TASK\_AFTER**：后加签任务 - **REDIRECT\_TASK**：转交任务 - **START\_PROCESS\_INSTANCE**：发起流程实例 - **TERMINATE\_PROCESS\_INSTANCE**：终止(撤销)流程实例 - **FINISH\_PROCESS\_INSTANCE**：结束流程实例 - **ADD\_REMARK**：添加评论 |
| userId | String | 操作人userId。 |
| remark | String | 评论。 |
| attachments | Array | 评论附件列表。 |
| fileName | String | 附件名称。 |
| fileSize | String | 文件大小。 |
| fileId | String | 附件钉盘ID。 |
| fileType | String | 文件类型。 |
| tasks | Array | 任务列表。 |
| userId | String | 任务处理人。 |
| status | String | 任务状态，取值：   - **RUNNING**：处理中 - **TERMINATED**：撤销 - **COMPLETED**：完成 - **CANCELED**：取消 |
| result | String | 任务结果，取值：   - **AGREE**：同意 - **REFUSE**：拒绝 - **REDIRECTED**：转交 - **NONE**：未知 |
| createTimestamp | Long | 任务创建时间戳 |
| finishTimestamp | Long | 任务结束时间戳 |
| taskId | Long | 任务Id |
| activityId | String | 节点id |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "nextToken" : "10",
    "hasMore" : true,
    "maxResults" : 20,
    "list" : [ {
      "processInstanceId" : "abcdse-dse-example",
      "mainProcessInstanceId" : "dcdse-dae2fd2-example",
      "finishTime" : 1633795200000,
      "finishTimeInMills" : 1633795200000,
      "attachedProcessInstanceIds" : "cdef-dae2fd2-example",
      "businessId" : "202110111558000355024",
      "title" : "员工A提交的小肖审批单",
      "originatorDeptId" : "默认-1，企业根部门",
      "result" : "agree同意，refuse拒绝",
      "createTime" : 1635165470201,
      "createTimeInMills" : 1635165470201,
      "originatorUserid" : "staff1234",
      "status" : "RUNNING审批中、TERMINATED撤销、COMPLETED审批完成、CANCELED取消",
      "formComponentValues" : [ {
        "name" : "姓名",
        "id" : "TextField-a32bcdef",
        "value" : "张三",
        "extValue" : "{\"staffId\":\"abcd\"}"
      } ],
      "operationRecords" : [ {
        "timestamp" : 1657522271000,
        "result" : "AGREE（同意），REFUSE（拒绝），NONE（未知）",
        "operationType" : "EXECUTE_TASK_NORMAL（正常执行任务），EXECUTE_TASK_AGENT（代理人执行任务），APPEND_TASK_BEFORE（前加签任务），APPEND_TASK_AFTER（后加签任务），REDIRECT_TASK（转交任务），START_PROCESS_INSTANCE（发起流程实例），TERMINATE_PROCESS_INSTANCE（终止(撤销)流程实例），FINISH_PROCESS_INSTANCE（结束流程实例），ADD_REMARK（添加评论）",
        "userId" : "manager1",
        "remark" : "同意",
        "attachments" : [ {
          "fileName" : "附件",
          "fileSize" : "123",
          "fileId" : "1234567",
          "fileType" : "pdf"
        } ]
      } ],
      "tasks" : [ {
        "userId" : "staff1234",
        "status" : "NEW（未启动），RUNNING（处理中），PAUSED（暂停），CANCELED（取消），COMPLETED（完成），TERMINATED（终止）",
        "result" : "分为AGREE（同意），REFUSE（拒绝），REDIRECTED（转交）",
        "createTimestamp" : 1657522271000,
        "finishTimestamp" : 1657522271000,
        "taskId" : 123456,
        "activityId" : "1234_abcd"
      } ]
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | userIdList.error | illegal userIdList | 查询userId列表错误 |
| 400 | timeStamp.invalid | illegal timestamp | 查询时间错误 |
| 400 | pageSize.invalid | illegal pageSize | 分页大小错误 |
| 400 | pageIndex.invalid | illegal pageIndex | 游标错误 |
| 400 | permission.error | no permission | 没有权限 |
| 400 | processCode.error | processCode query error | 模板编码查询错误 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 500 | system.error | system error | 系统错误 |
