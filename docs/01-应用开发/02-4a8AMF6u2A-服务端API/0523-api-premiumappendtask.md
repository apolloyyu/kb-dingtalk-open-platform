---
title: "加签审批任务"
source_url: "https://open.dingtalk.com/document/development/api-premiumappendtask"
namespace: "development"
slug: "api-premiumappendtask"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 加签审批任务"
doc_id: "7b39kR5e08"
updated_at: "2026-06-03 10:12:43"
---

> Source: https://open.dingtalk.com/document/development/api-premiumappendtask
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 加签审批任务
> Updated: 2026-06-03 10:12:43

# 加签审批任务

调用本接口，当前审批人可对审批任务进行加签操作，加签方式支持前加签、后加签，审批方式支持或签、会签、依次审批等。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)。

调用本接口，当前审批人可对审批任务进行加签操作，加签方式支持前加签、后加签，审批方式支持或签、会签、依次审批等。接口调用成功后，实现效果如下图所示。

- **或会签**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3672540871/p1076158.png)
- **依次审批（只有审批节点设置为依次审批时，加签时才会有依次审批的选项）**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3672540871/p1076159.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/tasks/append |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | Long | 是 | 审批任务ID。可通过调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取`taskId`参数值。 |
| processInstanceId | String | 是 | 审批实例ID：   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| operateUserId | String | 是 | 操作人的用户ID，需要跟任务的当前执行人保持一致，否则无法通过校验。 |
| appenderUserIds | Array of String | 是 | 加签人用户ID。 |
| remark | String | 否 | 加签备注信息。 |
| activateType | String | 是 | 审批方式：   - **ALL**：或签/或签 - **ONE\_BY\_ONE**： 依次审批 |
| type | String | 是 | 加签方式：   - **before**：前加签 - **after**：后加签 |
| agreeAll | Boolean | 否 | 是否需要全部同意，多人审批时需指定：   - **true**：依次审批 - **true**：会签 - **false**： 或签 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/tasks/append HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:9e86b42f968c3b958d
Content-Type:application/json

{
  "taskId" : 1234567,
  "processInstanceId" : "a171de6c-8bxxxx",
  "operateUserId" : "manager001",
  "appenderUserIds" : [ "manager002" ],
  "remark" : "请XX帮忙审批一下",
  "activateType" : "ALL",
  "type" : "after",
  "agreeAll" : true
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
        com.aliyun.dingtalkworkflow_1_0.models.PremiumAppendTaskHeaders premiumAppendTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumAppendTaskHeaders();
        premiumAppendTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumAppendTaskRequest premiumAppendTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumAppendTaskRequest()
                .setTaskId(1234567L)
                .setProcessInstanceId("a171de6c-8bxxxx")
                .setOperateUserId("manager001")
                .setAppenderUserIds(java.util.Arrays.asList(
                    "manager002"
                ))
                .setRemark("请XX帮忙审批一下")
                .setActivateType("ALL")
                .setType("after")
                .setAgreeAll(true);
        try {
            client.premiumAppendTaskWithOptions(premiumAppendTaskRequest, premiumAppendTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_append_task_headers = dingtalkworkflow__1__0_models.PremiumAppendTaskHeaders()
        premium_append_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_append_task_request = dingtalkworkflow__1__0_models.PremiumAppendTaskRequest(
            task_id=1234567,
            process_instance_id='a171de6c-8bxxxx',
            operate_user_id='manager001',
            appender_user_ids=[
                'manager002'
            ],
            remark='请XX帮忙审批一下',
            activate_type='ALL',
            type='after',
            agree_all=True
        )
        try:
            client.premium_append_task_with_options(premium_append_task_request, premium_append_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_append_task_headers = dingtalkworkflow__1__0_models.PremiumAppendTaskHeaders()
        premium_append_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_append_task_request = dingtalkworkflow__1__0_models.PremiumAppendTaskRequest(
            task_id=1234567,
            process_instance_id='a171de6c-8bxxxx',
            operate_user_id='manager001',
            appender_user_ids=[
                'manager002'
            ],
            remark='请XX帮忙审批一下',
            activate_type='ALL',
            type='after',
            agree_all=True
        )
        try:
            await client.premium_append_task_with_options_async(premium_append_task_request, premium_append_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumAppendTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumAppendTaskRequest;
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
        $premiumAppendTaskHeaders = new PremiumAppendTaskHeaders([]);
        $premiumAppendTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumAppendTaskRequest = new PremiumAppendTaskRequest([
            "taskId" => 1234567,
            "processInstanceId" => "a171de6c-8bxxxx",
            "operateUserId" => "manager001",
            "appenderUserIds" => [
                "manager002"
            ],
            "remark" => "请XX帮忙审批一下",
            "activateType" => "ALL",
            "type" => "after",
            "agreeAll" => true
        ]);
        try {
            $client->premiumAppendTaskWithOptions($premiumAppendTaskRequest, $premiumAppendTaskHeaders, new RuntimeOptions([]));
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

  premiumAppendTaskHeaders := &dingtalkworkflow_1_0.PremiumAppendTaskHeaders{}
  premiumAppendTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumAppendTaskRequest := &dingtalkworkflow_1_0.PremiumAppendTaskRequest{
    TaskId: tea.Int64(1234567),
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
    OperateUserId: tea.String("manager001"),
    AppenderUserIds: []*string{tea.String("manager002")},
    Remark: tea.String("请XX帮忙审批一下"),
    ActivateType: tea.String("ALL"),
    Type: tea.String("after"),
    AgreeAll: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumAppendTaskWithOptions(premiumAppendTaskRequest, premiumAppendTaskHeaders, &util.RuntimeOptions{})
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
    let premiumAppendTaskHeaders = new dingtalkworkflow_1_0.PremiumAppendTaskHeaders({ });
    premiumAppendTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumAppendTaskRequest = new dingtalkworkflow_1_0.PremiumAppendTaskRequest({
      taskId: 1234567,
      processInstanceId: 'a171de6c-8bxxxx',
      operateUserId: 'manager001',
      appenderUserIds: [
        'manager002'
      ],
      remark: '请XX帮忙审批一下',
      activateType: 'ALL',
      type: 'after',
      agreeAll: true,
    });
    try {
      await client.premiumAppendTaskWithOptions(premiumAppendTaskRequest, premiumAppendTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumAppendTaskHeaders premiumAppendTaskHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumAppendTaskHeaders();
            premiumAppendTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumAppendTaskRequest premiumAppendTaskRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumAppendTaskRequest
            {
                TaskId = 1234567,
                ProcessInstanceId = "a171de6c-8bxxxx",
                OperateUserId = "manager001",
                AppenderUserIds = new List<string>
                {
                    "manager002"
                },
                Remark = "请XX帮忙审批一下",
                ActivateType = "ALL",
                Type = "after",
                AgreeAll = true,
            };
            try
            {
                client.PremiumAppendTaskWithOptions(premiumAppendTaskRequest, premiumAppendTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否加签成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.blank | %s参数不能为空 | 请参照接口文档检查必填项taskId、processInstanceId、operateUserId、appenderUserIds、activateType、type |
| 400 | param.illegal | 不合法的参数%s | 不合法的参数taskId |
| 400 | task.status.error | 当前任务状态不是运行中不支持加签操作 | 请检查taskId，任务状态是否为RUNNING |
| 400 | instance.status.error | 当前流程实例状态不是运行中不支持加签操作 | 请检查processInstanceId参数，当前审批单状态是否为RUNNING |
| 400 | param.illegal.operator | 操作人的userId必须为当前任务的审批人 | 请检查operatorId参数 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 400 | appender.contains.currentOperator | 加签任务，加签人不能包含当前操作人 | 请检查operatorId、appenderUserIds参数传值 |
| 400 | isvAuth.check.error | 当前isv没有该审批模板的操作权限，请检查企业是否授权了该审批模板给isv | 当前isv没有该审批模板的操作权限，请检查企业是否授权了该审批模板给isv |
| 400 | user.not.exist | 用户ID不存在，请检查operatorId、appenderUserIds中的用户ID是否正确 | 用户ID不存在，请检查operatorId、appenderUserIds中的用户ID是否正确 |
| 500 | system.error | 系统错误 | 系统错误 |
