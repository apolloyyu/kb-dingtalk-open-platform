---
title: "批量更新实例状态"
source_url: "https://open.dingtalk.com/document/development/self-owned-batch-update-of-instance-status"
namespace: "development"
slug: "self-owned-batch-update-of-instance-status"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 审批实例 > 批量更新实例状态"
doc_id: "iFg0bctLyX"
updated_at: "2026-06-03 10:12:39"
---

> Source: https://open.dingtalk.com/document/development/self-owned-batch-update-of-instance-status
> Path: 应用开发 / 服务端 API / OA 审批 > 自有 OA 审批 > 审批实例 > 批量更新实例状态
> Updated: 2026-06-03 10:12:39

# 批量更新实例状态

调用本接口，批量更新实例状态。

## **接口调用说明**

例如，用户A提交待办任务，待办处理节点有3级，B1、B2、B3三级处理人，当前B1已同意，处理节点在B2，B3尚未收到待办任务。

当调用该接口后，待办状态查询路径如下图所示，状态变更如下表所示：

![](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221121/wati/实例通过.jpg)

以上图中的审批流为例，当状态置为**COMPLETED**时，审批流状态如下：

| 提交/待办处理人 | 更新前 | 更新后 |
| --- | --- | --- |
| 用户A | 工作台-待办-已发起，审批中 | 工作台-待办-已发起，已通过 |
| 审批节点B1 | 工作台-待办-已处理，已通过 | 工作台-待办-已处理，已通过 |
| 审批节点B2 | 无此条待办任务 | 无此条待办任务 |
| 审批节点B3 | 无此条待办任务 | 无此条待办任务 |

以上图中的审批流为例，当状态置为**TERMINATED**时，审批流状态如下：

| 提交/待办处理人 | 更新前 | 更新后 |
| --- | --- | --- |
| 用户A | 工作台-待办-已发起，审批中 | 工作台-待办-已发起，已撤销 |
| 审批节点B1 | 工作台-待办-已处理，已通过 | 工作台-待办-已处理，已撤销 |
| 审批节点B2 | 无此条待办任务 | 无此条待办任务 |
| 审批节点B3 | 无此条待办任务 | 无此条待办任务 |

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/instances/batch |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Instance.Write-工作流实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| updateProcessInstanceRequests | Array | 否 | 实列列表，最大值50。 |
| processInstanceId | String | 是 | 实例ID，调用[创建实例](0513-create-a-ticket-approval-instance.md)接口获取。 |
| status | String | 是 | 实例状态。   - **COMPLETED**：结束审批流 - **TERMINATED**：终止审批流 |
| result | String | 是 | 实例结果。   - 实例状态是**COMPLETED**，必须设置代表以下含义。    - **agree**：同意   - **refuse**：拒绝 - 实例状态为**TERMINATED**，必须设置代表含义，result取值agree和refuse均代表撤销审批流。 |
| notifiers | Array | 否 | 抄送人userId列表，最大值30。 |
| userId | String | 是 | 抄送人userId。 |

### 请求示例

HTTP

```
PUT /v1.0/workflow/processCentres/instances/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:Be3xxxx
Content-Type:application/json

{
  "updateProcessInstanceRequests" : [ {
    "processInstanceId" : "EF6YJL35",
    "status" : "COMPLETED",
    "result" : "agree",
    "notifiers" : [ {
      "userId" : "001"
    } ]
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
        com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceHeaders batchUpdateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceHeaders();
        batchUpdateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers updateProcessInstanceRequests0Notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers()
                .setUserId("001");
        com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests updateProcessInstanceRequests0 = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests()
                .setProcessInstanceId("EF6YJL35")
                .setStatus("COMPLETED")
                .setResult("agree")
                .setNotifiers(java.util.Arrays.asList(
                    updateProcessInstanceRequests0Notifiers0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest batchUpdateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest()
                .setUpdateProcessInstanceRequests(java.util.Arrays.asList(
                    updateProcessInstanceRequests0
                ));
        try {
            client.batchUpdateProcessInstanceWithOptions(batchUpdateProcessInstanceRequest, batchUpdateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        batch_update_process_instance_headers = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceHeaders()
        batch_update_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_process_instance_requests_0notifiers_0 = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers(
            user_id='001'
        )
        update_process_instance_requests_0 = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests(
            process_instance_id='EF6YJL35',
            status='COMPLETED',
            result='agree',
            notifiers=[
                update_process_instance_requests_0notifiers_0
            ]
        )
        batch_update_process_instance_request = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceRequest(
            update_process_instance_requests=[
                update_process_instance_requests_0
            ]
        )
        try:
            client.batch_update_process_instance_with_options(batch_update_process_instance_request, batch_update_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_update_process_instance_headers = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceHeaders()
        batch_update_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_process_instance_requests_0notifiers_0 = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers(
            user_id='001'
        )
        update_process_instance_requests_0 = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests(
            process_instance_id='EF6YJL35',
            status='COMPLETED',
            result='agree',
            notifiers=[
                update_process_instance_requests_0notifiers_0
            ]
        )
        batch_update_process_instance_request = dingtalkworkflow__1__0_models.BatchUpdateProcessInstanceRequest(
            update_process_instance_requests=[
                update_process_instance_requests_0
            ]
        )
        try:
            await client.batch_update_process_instance_with_options_async(batch_update_process_instance_request, batch_update_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\BatchUpdateProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\BatchUpdateProcessInstanceRequest\updateProcessInstanceRequests\notifiers;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\BatchUpdateProcessInstanceRequest\updateProcessInstanceRequests;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\BatchUpdateProcessInstanceRequest;
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
        $batchUpdateProcessInstanceHeaders = new BatchUpdateProcessInstanceHeaders([]);
        $batchUpdateProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateProcessInstanceRequests0Notifiers0 = new notifiers([
            "userId" => "001"
        ]);
        $updateProcessInstanceRequests0 = new updateProcessInstanceRequests([
            "processInstanceId" => "EF6YJL35",
            "status" => "COMPLETED",
            "result" => "agree",
            "notifiers" => [
                $updateProcessInstanceRequests0Notifiers0
            ]
        ]);
        $batchUpdateProcessInstanceRequest = new BatchUpdateProcessInstanceRequest([
            "updateProcessInstanceRequests" => [
                $updateProcessInstanceRequests0
            ]
        ]);
        try {
            $client->batchUpdateProcessInstanceWithOptions($batchUpdateProcessInstanceRequest, $batchUpdateProcessInstanceHeaders, new RuntimeOptions([]));
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

  batchUpdateProcessInstanceHeaders := &dingtalkworkflow_1_0.BatchUpdateProcessInstanceHeaders{}
  batchUpdateProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateProcessInstanceRequests0Notifiers0 := &dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers{
    UserId: tea.String("001"),
  }
  updateProcessInstanceRequests0 := &dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests{
    ProcessInstanceId: tea.String("EF6YJL35"),
    Status: tea.String("COMPLETED"),
    Result: tea.String("agree"),
    Notifiers: []*dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers{updateProcessInstanceRequests0Notifiers0},
  }
  batchUpdateProcessInstanceRequest := &dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequest{
    UpdateProcessInstanceRequests: []*dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests{updateProcessInstanceRequests0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchUpdateProcessInstanceWithOptions(batchUpdateProcessInstanceRequest, batchUpdateProcessInstanceHeaders, &util.RuntimeOptions{})
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
    let batchUpdateProcessInstanceHeaders = new $dingtalkworkflow_1_0.BatchUpdateProcessInstanceHeaders({ });
    batchUpdateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateProcessInstanceRequests0Notifiers0 = new $dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers({
      userId: "001",
    });
    let updateProcessInstanceRequests0 = new $dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests({
      processInstanceId: "EF6YJL35",
      status: "COMPLETED",
      result: "agree",
      notifiers: [
        updateProcessInstanceRequests0Notifiers0
      ],
    });
    let batchUpdateProcessInstanceRequest = new $dingtalkworkflow_1_0.BatchUpdateProcessInstanceRequest({
      updateProcessInstanceRequests: [
        updateProcessInstanceRequests0
      ],
    });
    try {
      await client.batchUpdateProcessInstanceWithOptions(batchUpdateProcessInstanceRequest, batchUpdateProcessInstanceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceHeaders batchUpdateProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceHeaders();
            batchUpdateProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers updateProcessInstanceRequests0Notifiers0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers
            {
                UserId = "001",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests updateProcessInstanceRequests0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests
            {
                ProcessInstanceId = "EF6YJL35",
                Status = "COMPLETED",
                Result = "agree",
                Notifiers = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers>
                {
                    updateProcessInstanceRequests0Notifiers0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest batchUpdateProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest
            {
                UpdateProcessInstanceRequests = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests>
                {
                    updateProcessInstanceRequests0
                },
            };
            try
            {
                client.BatchUpdateProcessInstanceWithOptions(batchUpdateProcessInstanceRequest, batchUpdateProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 操作是否成功，true代表成功。 |

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
| 400 | formContent.error | 表单格式错误 | 表单格式错误 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | updateOverSize | 更新审批单数量超出限制 | 更新审批单数量超出限制 |
