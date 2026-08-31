---
title: "更新实例状态"
source_url: "https://open.dingtalk.com/document/development/update-instance-status"
namespace: "development"
slug: "update-instance-status"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 审批实例 > 更新实例状态"
doc_id: "DejXpndOhg"
updated_at: "2026-06-03 10:12:39"
---

> Source: https://open.dingtalk.com/document/development/update-instance-status
> Path: 应用开发 / 服务端 API / OA 审批 > 自有 OA 审批 > 审批实例 > 更新实例状态
> Updated: 2026-06-03 10:12:39

# 更新实例状态

调用本接口，更新OA审批实例状态。

## **接口调用说明**

例如，用户A提交待办任务，待办处理节点有3级，B1、B2、B3三级处理人，当前B1已同意，处理节点在B2，B3尚未收到待办任务。

当调用本接口后，待办状态查询路径如下图所示，状态变更如下表所示：

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
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/instances |
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
| processInstanceId | String | 是 | 审批实例ID，调用[创建实例](0513-create-a-ticket-approval-instance.md)接口获取`processInstanceId`参数值。 |
| status | String | 是 | 实例状态。   - **COMPLETED**：结束审批流 - **TERMINATED**：终止审批流 |
| result | String | 是 | 实例结果：   - 实例状态是COMPLETED，必须设置代表以下含义。    - **agree**：同意   - **refuse**：拒绝 - 实例状态为**TERMINATED**，必须设置代表含义，result取值agree和refuse均代表撤销审批流。 |
| notifiers | Array | 否 | 抄送人userId列表，最大值30。 |
| userId | String | 是 | 抄送人userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |

### 请求示例

HTTP

```
PUT /v1.0/workflow/processCentres/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processInstanceId" : "proc",
  "status" : "COMPLETED",
  "result" : "agree",
  "notifiers" : [ {
    "userId" : "001"
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
        com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceHeaders updateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceHeaders();
        updateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers()
                .setUserId("001");
        com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest updateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest()
                .setProcessInstanceId("proc")
                .setStatus("COMPLETED")
                .setResult("agree")
                .setNotifiers(java.util.Arrays.asList(
                    notifiers0
                ));
        try {
            client.updateProcessInstanceWithOptions(updateProcessInstanceRequest, updateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_process_instance_headers = dingtalkworkflow__1__0_models.UpdateProcessInstanceHeaders()
        update_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        notifiers_0 = dingtalkworkflow__1__0_models.UpdateProcessInstanceRequestNotifiers(
            user_id='001'
        )
        update_process_instance_request = dingtalkworkflow__1__0_models.UpdateProcessInstanceRequest(
            process_instance_id='proc',
            status='COMPLETED',
            result='agree',
            notifiers=[
                notifiers_0
            ]
        )
        try:
            client.update_process_instance_with_options(update_process_instance_request, update_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_process_instance_headers = dingtalkworkflow__1__0_models.UpdateProcessInstanceHeaders()
        update_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        notifiers_0 = dingtalkworkflow__1__0_models.UpdateProcessInstanceRequestNotifiers(
            user_id='001'
        )
        update_process_instance_request = dingtalkworkflow__1__0_models.UpdateProcessInstanceRequest(
            process_instance_id='proc',
            status='COMPLETED',
            result='agree',
            notifiers=[
                notifiers_0
            ]
        )
        try:
            await client.update_process_instance_with_options_async(update_process_instance_request, update_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\UpdateProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\UpdateProcessInstanceRequest\notifiers;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\UpdateProcessInstanceRequest;
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
        $updateProcessInstanceHeaders = new UpdateProcessInstanceHeaders([]);
        $updateProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $notifiers0 = new notifiers([
            "userId" => "001"
        ]);
        $updateProcessInstanceRequest = new UpdateProcessInstanceRequest([
            "processInstanceId" => "proc",
            "status" => "COMPLETED",
            "result" => "agree",
            "notifiers" => [
                $notifiers0
            ]
        ]);
        try {
            $client->updateProcessInstanceWithOptions($updateProcessInstanceRequest, $updateProcessInstanceHeaders, new RuntimeOptions([]));
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

  updateProcessInstanceHeaders := &dingtalkworkflow_1_0.UpdateProcessInstanceHeaders{}
  updateProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  notifiers0 := &dingtalkworkflow_1_0.UpdateProcessInstanceRequestNotifiers{
    UserId: tea.String("001"),
  }
  updateProcessInstanceRequest := &dingtalkworkflow_1_0.UpdateProcessInstanceRequest{
    ProcessInstanceId: tea.String("proc"),
    Status: tea.String("COMPLETED"),
    Result: tea.String("agree"),
    Notifiers: []*dingtalkworkflow_1_0.UpdateProcessInstanceRequestNotifiers{notifiers0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateProcessInstanceWithOptions(updateProcessInstanceRequest, updateProcessInstanceHeaders, &util.RuntimeOptions{})
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
    let updateProcessInstanceHeaders = new $dingtalkworkflow_1_0.UpdateProcessInstanceHeaders({ });
    updateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let notifiers0 = new $dingtalkworkflow_1_0.UpdateProcessInstanceRequestNotifiers({
      userId: "001",
    });
    let updateProcessInstanceRequest = new $dingtalkworkflow_1_0.UpdateProcessInstanceRequest({
      processInstanceId: "proc",
      status: "COMPLETED",
      result: "agree",
      notifiers: [
        notifiers0
      ],
    });
    try {
      await client.updateProcessInstanceWithOptions(updateProcessInstanceRequest, updateProcessInstanceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceHeaders updateProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceHeaders();
            updateProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers notifiers0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers
            {
                UserId = "001",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceRequest updateProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceRequest
            {
                ProcessInstanceId = "proc",
                Status = "COMPLETED",
                Result = "agree",
                Notifiers = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers>
                {
                    notifiers0
                },
            };
            try
            {
                client.UpdateProcessInstanceWithOptions(updateProcessInstanceRequest, updateProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否执行成功：   - **true**：成功 - **false**：失败 |

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
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | noticerOverLimit | 抄送人数量超过限制 | 抄送人数量超过限制 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | process.inst.notExist | 审批单不存在或已删除 | 审批单不存在或已删除 |
| 500 | system.error | 系统错误 | 系统错误 |
