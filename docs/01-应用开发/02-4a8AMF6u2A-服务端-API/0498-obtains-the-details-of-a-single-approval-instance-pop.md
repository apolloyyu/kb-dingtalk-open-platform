---
title: "获取单个审批实例详情"
source_url: "https://open.dingtalk.com/document/development/obtains-the-details-of-a-single-approval-instance-pop"
namespace: "development"
slug: "obtains-the-details-of-a-single-approval-instance-pop"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批实例 > 获取单个审批实例详情"
doc_id: "DuRiZXutk0"
updated_at: "2026-08-19 09:09:34"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-details-of-a-single-approval-instance-pop
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批实例 > 获取单个审批实例详情
> Updated: 2026-08-19 09:09:34

# 获取单个审批实例详情

调用本接口可以获取审批实例详情数据，根据审批实例ID，获取审批实例详情，包括审批实例标题、发起人userId、审批人userId、操作记录等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Instance.Read-工作流实例读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 审批实例ID。   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值： - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/processInstances?processInstanceId=a171de6c-8bxxxx HTTP/1.1
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
        com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders getProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders();
        getProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest getProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest()
                .setProcessInstanceId("a171de6c-8bxxxx");
        try {
            client.getProcessInstanceWithOptions(getProcessInstanceRequest, getProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_process_instance_headers = dingtalkworkflow__1__0_models.GetProcessInstanceHeaders()
        get_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_process_instance_request = dingtalkworkflow__1__0_models.GetProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx'
        )
        try:
            client.get_process_instance_with_options(get_process_instance_request, get_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_process_instance_headers = dingtalkworkflow__1__0_models.GetProcessInstanceHeaders()
        get_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_process_instance_request = dingtalkworkflow__1__0_models.GetProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx'
        )
        try:
            await client.get_process_instance_with_options_async(get_process_instance_request, get_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetProcessInstanceRequest;
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
        $getProcessInstanceHeaders = new GetProcessInstanceHeaders([]);
        $getProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getProcessInstanceRequest = new GetProcessInstanceRequest([
            "processInstanceId" => "a171de6c-8bxxxx"
        ]);
        try {
            $client->getProcessInstanceWithOptions($getProcessInstanceRequest, $getProcessInstanceHeaders, new RuntimeOptions([]));
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

  getProcessInstanceHeaders := &dingtalkworkflow_1_0.GetProcessInstanceHeaders{}
  getProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getProcessInstanceRequest := &dingtalkworkflow_1_0.GetProcessInstanceRequest{
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetProcessInstanceWithOptions(getProcessInstanceRequest, getProcessInstanceHeaders, &util.RuntimeOptions{})
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
    let getProcessInstanceHeaders = new dingtalkworkflow_1_0.GetProcessInstanceHeaders({ });
    getProcessInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getProcessInstanceRequest = new dingtalkworkflow_1_0.GetProcessInstanceRequest({
      processInstanceId: 'a171de6c-8bxxxx',
    });
    try {
      await client.getProcessInstanceWithOptions(getProcessInstanceRequest, getProcessInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetProcessInstanceHeaders getProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetProcessInstanceHeaders();
            getProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetProcessInstanceRequest getProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetProcessInstanceRequest
            {
                ProcessInstanceId = "a171de6c-8bxxxx",
            };
            try
            {
                client.GetProcessInstanceWithOptions(getProcessInstanceRequest, getProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| title | String | 审批实例标题。 |
| finishTime | String | 结束时间。 |
| originatorUserId | String | 发起人的userId。 |
| originatorDeptId | String | 发起人的部门，-1表示根部门。 |
| originatorDeptName | String | 发起人的部门名称。 |
| status | String | 审批状态：   - **RUNNING**：审批中 - **TERMINATED**：已撤销 - **COMPLETED**：审批完成 |
| approverUserIds | Array of String | 审批人userId。  **[!NOTE]**  - 使用接口发起的审批单返回该参数。 - 在OA审批应用手动发起的审批单不返回该参数。 |
| ccUserIds | Array of String | 抄送人userId。 |
| result | String | 审批结果：   - **agree**：同意 - **refuse**：拒绝   **[!NOTE]**  status为**COMPLETED**且result为**agree**时，表示审批单完结并审批通过。 |
| businessId | String | 审批实例业务编号。 |
| operationRecords | Array | 操作记录列表。 |
| userId | String | 操作人userId。 |
| date | String | 操作时间。 |
| type | String | 操作类型：   - **EXECUTE\_TASK\_NORMAL**：正常执行任务 - **EXECUTE\_TASK\_AGENT**：代理人执行任务 - **APPEND\_TASK\_BEFORE**：前加签任务 - **APPEND\_TASK\_AFTER**：后加签任务 - **REDIRECT\_TASK**：转交任务 - **START\_PROCESS\_INSTANCE**：发起流程实例 - **TERMINATE\_PROCESS\_INSTANCE**：终止(撤销)流程实例 - **FINISH\_PROCESS\_INSTANCE**：结束流程实例 - **ADD\_REMARK**：添加评论 - **REDIRECT\_PROCESS**：审批退回 - **PROCESS\_CC**：抄送 |
| result | String | 操作结果：   - **AGREE**：同意 - **REFUSE**：拒绝 - **NONE**：未处理 |
| remark | String | 评论内容。  **[!NOTE]**  审批操作附带评论时才返回该字段。 |
| attachments | Array | 评论附件列表。 |
| fileName | String | 附件名称。 |
| fileSize | String | 附件大小。 |
| fileId | String | 附件ID。 |
| fileType | String | 附件类型。 |
| spaceId | String | 附件的钉盘空间ID |
| ccUserIds | Array of String | 抄送人userIds列表。 |
| activityId | String | 任务节点ID。 |
| showName | String | 任务节点名称。 |
| images | Array of String | 单个图片链接。 |
| tasks | Array | 任务列表。 |
| taskId | Long | 任务ID。 |
| userId | String | 任务处理人。 |
| status | String | 任务状态：   - **NEW**：未启动 - **RUNNING**：处理中 - **PAUSED**：暂停 - **CANCELED**：取消 - **COMPLETED**：完成 - **TERMINATED**：终止 |
| result | String | 结果：   - **AGREE**：同意 - **REFUSE**：拒绝 - **REDIRECTED**：转交 |
| createTime | String | 开始时间。 |
| finishTime | String | 结束时间。 |
| mobileUrl | String | 移动端任务URL。 |
| pcUrl | String | PC端任务URL。 |
| processInstanceId | String | 实例ID。 |
| activityId | String | 任务节点ID。 |
| taskGroupName | String | 审批组名称。 |
| bizAction | String | 审批实例业务动作：   - **MODIFY**：表示该审批实例是基于原来的实例修改而来 - **REVOKE**：表示该审批实例是由原来的实例撤销后重新发起的 - **NONE**：表示正常发起 |
| bizData | String | 用户自定义业务参数透出。 |
| attachedProcessInstanceIds | Array of String | 审批附属实例。 |
| mainProcessInstanceId | String | 主流程实例标识。 |
| formComponentValues | Array | 表单组件详情列表。 |
| id | String | 组件ID。 |
| name | String | 组件名称。 |
| value | String | 标签值。 |
| extValue | String | 标签扩展值。 |
| componentType | String | 组件类型。 |
| bizAlias | String | 组件别名。 |
| createTime | String | 创建时间。 |
| success | String | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "title" : "xx提交的请假申请",
    "finishTime" : "2022-08-31T11:52Z",
    "originatorUserId" : "manager1",
    "originatorDeptId" : "-1",
    "originatorDeptName" : "测试",
    "status" : "RUNNING",
    "approverUserIds" : [ "manager1" ],
    "ccUserIds" : [ "manager1" ],
    "result" : "agree",
    "businessId" : "111",
    "operationRecords" : [ {
      "userId" : "manager1",
      "date" : "2022-08-31T11:52Z",
      "type" : "EXECUTE_TASK_NORMAL",
      "result" : "AGREE",
      "remark" : "评论",
      "attachments" : [ {
        "fileName" : "学历证明",
        "fileSize" : "1024",
        "fileId" : "111",
        "fileType" : "pdf",
        "spaceId" : "12345"
      } ],
      "ccUserIds" : [ "0417****4537" ],
      "activityId" : "aabb-ccdd",
      "showName" : "审批人",
      "images" : [ "https://static.dingtalk.com/media/xxxx_1280_720.jpg" ]
    } ],
    "tasks" : [ {
      "taskId" : 111,
      "userId" : "manager1",
      "status" : "NEW",
      "result" : "REDIRECTED",
      "createTime" : "2022-08-31T11:52Z",
      "finishTime" : "2022-08-31T11:52Z",
      "mobileUrl" : "https://www.xxxx.com",
      "pcUrl" : "https://www.xxxx.com",
      "processInstanceId" : "111",
      "activityId" : "111",
      "taskGroupName" : "审批人1"
    } ],
    "bizAction" : "MODIFY",
    "bizData" : "{\"mykey\": \"myData\"}",
    "attachedProcessInstanceIds" : [ "instance1" ],
    "mainProcessInstanceId" : "111",
    "formComponentValues" : [ {
      "id" : "DDHolidayField-J2Bxxxx",
      "name" : "组件1",
      "value" : "示例值",
      "extValue" : "示例值",
      "componentType" : "DDSelectField",
      "bizAlias" : "TextField-bizAlias"
    } ],
    "createTime" : "2022-08-31T11:52Z"
  },
  "success" : "true"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | targetSelectApproverScopeError | 自选审批人不在规定范围内 | 自选审批人不在规定范围内 |
| 400 | targetSelectApproverMissing | 自选审批人缺失 | 自选审批人缺失 |
| 400 | invalidParameter | 获取单个审批实例详情参数错误 | 获取单个审批实例详情参数错误 |
| 400 | processInstanceInvalidParameter | 审批实例参数错误 | 审批实例参数错误 |
| 400 | processInstanceStartFailed | 创建审批实例失败 | 创建审批实例失败 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | processGroupGetFailed | 获取审批流分组失败 | 获取审批流分组失败 |
| 400 | processCodeError | 获取审批模板失败或者模板已被删除 | 获取审批模板失败或者模板已被删除 |
| 400 | processSetupNoPermission | 无操作审批流的权限 | 无操作审批流的权限 |
| 400 | processGetFailed | 获取审批流失败 | 获取审批流失败 |
| 400 | formConverterError | 表单数据校验失败，失败控件：%s | 表单数据校验失败 |
| 400 | illegalComponent | 表单组件入参错误 | 表单组件入参错误 |
| 400 | processInstanceIdError | processInstanceId参数无效 | processInstanceId参数无效 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | processFormDataIsNull | 流程表单数据为空 | 流程表单数据为空 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | processInstanceNotExist | 审批实例不存在 | 审批实例不存在 |
| 500 | systemError | 系统异常 | 系统异常 |
| 500 | systemError | 系统异常 | 系统异常 |
