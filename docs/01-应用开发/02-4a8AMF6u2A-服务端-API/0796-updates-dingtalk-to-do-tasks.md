---
title: "更新钉钉待办任务"
source_url: "https://open.dingtalk.com/document/development/updates-dingtalk-to-do-tasks"
namespace: "development"
slug: "updates-dingtalk-to-do-tasks"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 更新钉钉待办任务"
doc_id: "7jxhP6sBwc"
updated_at: "2026-06-02 19:09:48"
---

> Source: https://open.dingtalk.com/document/development/updates-dingtalk-to-do-tasks
> Path: 应用开发 / 服务端 API / 待办任务 > 更新钉钉待办任务
> Updated: 2026-06-02 19:09:48

# 更新钉钉待办任务

调用本接口，根据待办ID，更新指定钉钉待办的任务信息及状态。ISV在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks/{taskId} |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Todo.Todo.Write-待办应用中待办写权限,待办应用中待办读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 当前访问资源所归属用户的unionId，需要操作者的unionId保持一致，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
| taskId | String | 是 | 待办ID。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 否 | 当前操作者的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| subject | String | 否 | 待办标题，最大长度1024。 |
| description | String | 否 | 待办描述，最大长度4096。 |
| dueTime | Long | 否 | 截止时间，Unix时间戳，单位毫秒。 |
| done | Boolean | 否 | 完成状态。   - **true**：已完成 - **false**：未完成 |
| executorIds | Array of String | 否 | 执行者的unionId列表，可调用[查询用户详情](0056-query-user-details.md)接口获取，最大数量1000。 |
| participantIds | Array of String | 否 | 参与者的unionId列表，可调用[查询用户详情](0056-query-user-details.md)接口获取，最大数量1000。 |
| contentFieldList | Array | 否 | 内容区表单字段配置。 |
| fieldKey | String | 否 | 字段唯一标识。 |
| fieldValue | String | 否 | 字段值。 |

### 请求示例

HTTP

```
PUT /v1.0/todo/users/PUoiinxxx/tasks/OPJpwtxxx?operatorId=PUoiinWxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b3ba0xxx
Content-Type:application/json

{
  "subject" : "更新钉钉待办",
  "description" : "应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。",
  "dueTime" : 1617675000000,
  "done" : true,
  "executorIds" : [ "PUoiinWxxx" ],
  "participantIds" : [ "PUoiinWIpxxx" ],
  "contentFieldList" : [ {
    "fieldKey" : "来源应用",
    "fieldValue" : "自建审批系统"
  } ]
}
```

Java

```
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
    public static com.aliyun.dingtalktodo_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktodo_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalktodo_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTaskHeaders updateTodoTaskHeaders = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTaskHeaders();
        updateTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTaskRequest.UpdateTodoTaskRequestContentFieldList contentFieldList0 = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTaskRequest.UpdateTodoTaskRequestContentFieldList()
                .setFieldKey("来源应用")
                .setFieldValue("自建审批系统");
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTaskRequest updateTodoTaskRequest = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTaskRequest()
                .setOperatorId("PUoiinWxxx")
                .setSubject("更新钉钉待办")
                .setDescription("应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。")
                .setDueTime(1617675000000L)
                .setDone(true)
                .setExecutorIds(java.util.Arrays.asList(
                    "PUoiinWxxx"
                ))
                .setParticipantIds(java.util.Arrays.asList(
                    "PUoiinWIpxxx"
                ))
                .setContentFieldList(java.util.Arrays.asList(
                    contentFieldList0
                ));
        try {
            client.updateTodoTaskWithOptions("PUoiinxxx", "OPJpwtxxx", updateTodoTaskRequest, updateTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.todo_1_0.client import Client as dingtalktodo_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.todo_1_0 import models as dingtalktodo__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalktodo_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalktodo_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_todo_task_headers = dingtalktodo__1__0_models.UpdateTodoTaskHeaders()
        update_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        content_field_list_0 = dingtalktodo__1__0_models.UpdateTodoTaskRequestContentFieldList(
            field_key='来源应用',
            field_value='自建审批系统'
        )
        update_todo_task_request = dingtalktodo__1__0_models.UpdateTodoTaskRequest(
            operator_id='PUoiinWxxx',
            subject='更新钉钉待办',
            description='应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。',
            due_time=1617675000000,
            done=True,
            executor_ids=[
                'PUoiinWxxx'
            ],
            participant_ids=[
                'PUoiinWIpxxx'
            ],
            content_field_list=[
                content_field_list_0
            ]
        )
        try:
            client.update_todo_task_with_options('PUoiinxxx', 'OPJpwtxxx', update_todo_task_request, update_todo_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_todo_task_headers = dingtalktodo__1__0_models.UpdateTodoTaskHeaders()
        update_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        content_field_list_0 = dingtalktodo__1__0_models.UpdateTodoTaskRequestContentFieldList(
            field_key='来源应用',
            field_value='自建审批系统'
        )
        update_todo_task_request = dingtalktodo__1__0_models.UpdateTodoTaskRequest(
            operator_id='PUoiinWxxx',
            subject='更新钉钉待办',
            description='应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。',
            due_time=1617675000000,
            done=True,
            executor_ids=[
                'PUoiinWxxx'
            ],
            participant_ids=[
                'PUoiinWIpxxx'
            ],
            content_field_list=[
                content_field_list_0
            ]
        )
        try:
            await client.update_todo_task_with_options_async('PUoiinxxx', 'OPJpwtxxx', update_todo_task_request, update_todo_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTaskRequest\contentFieldList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTaskRequest;
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
        $updateTodoTaskHeaders = new UpdateTodoTaskHeaders([]);
        $updateTodoTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $contentFieldList0 = new contentFieldList([
            "fieldKey" => "来源应用",
            "fieldValue" => "自建审批系统"
        ]);
        $updateTodoTaskRequest = new UpdateTodoTaskRequest([
            "operatorId" => "PUoiinWxxx",
            "subject" => "更新钉钉待办",
            "description" => "应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。",
            "dueTime" => 1617675000000,
            "done" => true,
            "executorIds" => [
                "PUoiinWxxx"
            ],
            "participantIds" => [
                "PUoiinWIpxxx"
            ],
            "contentFieldList" => [
                $contentFieldList0
            ]
        ]);
        try {
            $client->updateTodoTaskWithOptions("PUoiinxxx", "OPJpwtxxx", $updateTodoTaskRequest, $updateTodoTaskHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalktodo_1_0  "github.com/alibabacloud-go/dingtalk/todo_1_0"
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
func CreateClient () (_result *dingtalktodo_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalktodo_1_0.Client{}
  _result, _err = dingtalktodo_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateTodoTaskHeaders := &dingtalktodo_1_0.UpdateTodoTaskHeaders{}
  updateTodoTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  contentFieldList0 := &dingtalktodo_1_0.UpdateTodoTaskRequestContentFieldList{
    FieldKey: tea.String("来源应用"),
    FieldValue: tea.String("自建审批系统"),
  }
  updateTodoTaskRequest := &dingtalktodo_1_0.UpdateTodoTaskRequest{
    OperatorId: tea.String("PUoiinWxxx"),
    Subject: tea.String("更新钉钉待办"),
    Description: tea.String("应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。"),
    DueTime: tea.Int64(1617675000000),
    Done: tea.Bool(true),
    ExecutorIds: []*string{tea.String("PUoiinWxxx")},
    ParticipantIds: []*string{tea.String("PUoiinWIpxxx")},
    ContentFieldList: []*dingtalktodo_1_0.UpdateTodoTaskRequestContentFieldList{contentFieldList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateTodoTaskWithOptions(tea.String("PUoiinxxx"), tea.String("OPJpwtxxx"), updateTodoTaskRequest, updateTodoTaskHeaders, &util.RuntimeOptions{})
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
const dingtalktodo_1_0 = require('@alicloud/dingtalk/todo_1_0');
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
    return new dingtalktodo_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateTodoTaskHeaders = new dingtalktodo_1_0.UpdateTodoTaskHeaders({ });
    updateTodoTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let contentFieldList0 = new dingtalktodo_1_0.UpdateTodoTaskRequestContentFieldList({
      fieldKey: '来源应用',
      fieldValue: '自建审批系统',
    });
    let updateTodoTaskRequest = new dingtalktodo_1_0.UpdateTodoTaskRequest({
      operatorId: 'PUoiinWxxx',
      subject: '更新钉钉待办',
      description: '应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。',
      dueTime: 1617675000000,
      done: true,
      executorIds: [
        'PUoiinWxxx'
      ],
      participantIds: [
        'PUoiinWIpxxx'
      ],
      contentFieldList: [
        contentFieldList0
      ],
    });
    try {
      await client.updateTodoTaskWithOptions('PUoiinxxx', 'OPJpwtxxx', updateTodoTaskRequest, updateTodoTaskHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalktodo_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalktodo_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalktodo_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskHeaders updateTodoTaskHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskHeaders();
            updateTodoTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskRequest.UpdateTodoTaskRequestContentFieldList contentFieldList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskRequest.UpdateTodoTaskRequestContentFieldList
            {
                FieldKey = "来源应用",
                FieldValue = "自建审批系统",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskRequest updateTodoTaskRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskRequest
            {
                OperatorId = "PUoiinWxxx",
                Subject = "更新钉钉待办",
                Description = "应用可以调用该接口更新钉钉待办任务信息及状态，isv在自身应用待办数据被更新后，需调用该接口将钉钉侧待办数据同步更新。",
                DueTime = 1617675000000,
                Done = true,
                ExecutorIds = new List<string>
                {
                    "PUoiinWxxx"
                },
                ParticipantIds = new List<string>
                {
                    "PUoiinWIpxxx"
                },
                ContentFieldList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskRequest.UpdateTodoTaskRequestContentFieldList>
                {
                    contentFieldList0
                },
            };
            try
            {
                client.UpdateTodoTaskWithOptions("PUoiinxxx", "OPJpwtxxx", updateTodoTaskRequest, updateTodoTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新结果，true表示成功。 |

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
| 400 | todo.taskUpdate.paramError | todo.taskUpdate.paramError | 更新待办参数异常 |
| 400 | todo.taskUpdate.paramError | subject is oversize | 待办标题长度超出限制 |
| 400 | todo.taskUpdate.paramError | description is oversize | 待办描述长度超出限制 |
| 400 | todo.taskUpdate.paramError | executors is oversize | 待办执行人超出限制 |
| 400 | todo.taskUpdate.paramError | participants is oversize | 待办参与人超出限制 |
| 400 | todo.taskUpdate.paramError | dueTime is invalid | 待办截止时间非法 |
| 400 | todo.taskUpdate.paramError | task not exist | 待办任务不存在 |
| 400 | todo.taskUpdate.paramError | task not belong to bizTag | 待办任务不属于该应用 |
| 500 | todo.taskUpdate.systemError | todo.taskUpdate.systemError | 更新待办系统异常 |
