---
title: "批量取消流程中心待处理任务"
source_url: "https://open.dingtalk.com/document/development/cancel-multiple-oa-approval-tasks"
namespace: "development"
slug: "cancel-multiple-oa-approval-tasks"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 流程中心任务 > 批量取消流程中心待处理任务"
doc_id: "0AYB3HGo9G"
updated_at: "2026-06-02 15:54:15"
---

> Source: https://open.dingtalk.com/document/development/cancel-multiple-oa-approval-tasks
> Path: 应用开发 / 服务端 API / OA 审批 > 自有 OA 审批 > 流程中心任务 > 批量取消流程中心待处理任务
> Updated: 2026-06-02 15:54:15

# 批量取消流程中心待处理任务

用于批量取消流程中心待处理任务。调用时通过 POST 请求提交 processInstanceId、activityId、activityIds 等业务字段。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/tasks/cancel |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Instance.Write-工作流实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | OA审批流程实例ID，调用[创建实例](0513-create-a-ticket-approval-instance.md)接口获取processInstanceId参数值。 |
| activityId | String | 是 | 待办组ID，调用[创建流程中心待处理任务](https://open.dingtalk.com/document/orgapp/create-pending-tasks-in-process-center)接口获取，最大长度512字符。  **[!NOTE]**    需要在调用创建流程中心待处理任务接口时，主动设置该值。 |
| activityIds | Array of String | 否 | 待办组ID列表，调用[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processCentres/tasks/cancel HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json

{
  "processInstanceId" : "tPr_FB_mT_xxxxxxxxx2hQ05201655306463",
  "activityId" : "act_xxxx",
  "activityIds" : [ "act_xxxx" ]
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
        com.aliyun.dingtalkworkflow_1_0.models.CancelIntegratedTaskHeaders cancelIntegratedTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.CancelIntegratedTaskHeaders();
        cancelIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.CancelIntegratedTaskRequest()
                .setProcessInstanceId("tPr_FB_mT_xxxxxxxxx2hQ05201655306463")
                .setActivityId("act_xxxx")
                .setActivityIds(java.util.Arrays.asList(
                    "act_xxxx"
                ));
        try {
            client.cancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        cancel_integrated_task_headers = dingtalkworkflow__1__0_models.CancelIntegratedTaskHeaders()
        cancel_integrated_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        cancel_integrated_task_request = dingtalkworkflow__1__0_models.CancelIntegratedTaskRequest(
            process_instance_id='tPr_FB_mT_xxxxxxxxx2hQ05201655306463',
            activity_id='act_xxxx',
            activity_ids=[
                'act_xxxx'
            ]
        )
        try:
            client.cancel_integrated_task_with_options(cancel_integrated_task_request, cancel_integrated_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        cancel_integrated_task_headers = dingtalkworkflow__1__0_models.CancelIntegratedTaskHeaders()
        cancel_integrated_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        cancel_integrated_task_request = dingtalkworkflow__1__0_models.CancelIntegratedTaskRequest(
            process_instance_id='tPr_FB_mT_xxxxxxxxx2hQ05201655306463',
            activity_id='act_xxxx',
            activity_ids=[
                'act_xxxx'
            ]
        )
        try:
            await client.cancel_integrated_task_with_options_async(cancel_integrated_task_request, cancel_integrated_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CancelIntegratedTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CancelIntegratedTaskRequest;
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
        $cancelIntegratedTaskHeaders = new CancelIntegratedTaskHeaders([]);
        $cancelIntegratedTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cancelIntegratedTaskRequest = new CancelIntegratedTaskRequest([
            "processInstanceId" => "tPr_FB_mT_xxxxxxxxx2hQ05201655306463",
            "activityId" => "act_xxxx",
            "activityIds" => [
                "act_xxxx"
            ]
        ]);
        try {
            $client->cancelIntegratedTaskWithOptions($cancelIntegratedTaskRequest, $cancelIntegratedTaskHeaders, new RuntimeOptions([]));
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

  cancelIntegratedTaskHeaders := &dingtalkworkflow_1_0.CancelIntegratedTaskHeaders{}
  cancelIntegratedTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cancelIntegratedTaskRequest := &dingtalkworkflow_1_0.CancelIntegratedTaskRequest{
    ProcessInstanceId: tea.String("tPr_FB_mT_xxxxxxxxx2hQ05201655306463"),
    ActivityId: tea.String("act_xxxx"),
    ActivityIds: []*string{tea.String("act_xxxx")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, &util.RuntimeOptions{})
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
    let cancelIntegratedTaskHeaders = new dingtalkworkflow_1_0.CancelIntegratedTaskHeaders({ });
    cancelIntegratedTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let cancelIntegratedTaskRequest = new dingtalkworkflow_1_0.CancelIntegratedTaskRequest({
      processInstanceId: 'tPr_FB_mT_xxxxxxxxx2hQ05201655306463',
      activityId: 'act_xxxx',
      activityIds: [
        'act_xxxx'
      ],
    });
    try {
      await client.cancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CancelIntegratedTaskHeaders cancelIntegratedTaskHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CancelIntegratedTaskHeaders();
            cancelIntegratedTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CancelIntegratedTaskRequest
            {
                ProcessInstanceId = "tPr_FB_mT_xxxxxxxxx2hQ05201655306463",
                ActivityId = "act_xxxx",
                ActivityIds = new List<string>
                {
                    "act_xxxx"
                },
            };
            try
            {
                client.CancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 操作是否成功。 true表示成功。 |

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
| 400 | integrated.permission.error | 无操作审批流的权限，请检查审批实例或者模版是否正确 | 无操作审批流的权限，请检查审批实例或者模版是否正确 |
| 400 | integrated.state.invalid | 流程实例不存在 | 流程实例不存在 |
| 400 | integrated.state.invalid | 参数错误，请检查流程实例ID是否正确 | 参数错误，请检查流程实例ID是否正确 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | system.error | 系统错误 | 系统错误 |
