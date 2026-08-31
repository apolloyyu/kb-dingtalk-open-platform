---
title: "创建钉钉个人待办任务"
source_url: "https://open.dingtalk.com/document/development/api-createpersonaltodotask"
namespace: "development"
slug: "api-createpersonaltodotask"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 创建钉钉个人待办任务"
doc_id: "Qc9y8MHf0N"
updated_at: "2026-06-04 19:09:50"
---

> Source: https://open.dingtalk.com/document/development/api-createpersonaltodotask
> Path: 应用开发 / 服务端 API / 待办任务 > 创建钉钉个人待办任务
> Updated: 2026-06-04 19:09:50

# 创建钉钉个人待办任务

调用本接口，创建一个钉钉“个人待办“任务。此任务将在钉钉移动应用中显示，在客户端点击这个待办任务时，系统将自动跳转至钉钉官方的标准待办任务页面。

## 接口调用说明

如果要打开自定义的 url 地址，请参考[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/me/personalTasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Todo.PersonalTodo.Write-以用户的个人身份创建或更新个人待办数据 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| subject | String | 是 | 待办标题，最大长度1024字节。 |
| description | String | 否 | 待办备注，最大长度4096字节。 |
| dueTime | Long | 否 | 截止时间，Unix时间戳，单位毫秒。 |
| executorIds | Array of String | 是 | 执行者列表，需传用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取，最大数量100。 |
| participantIds | Array of String | 否 | 参与者列表，需传用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取，最大长度100。 |
| notifyConfigs | Object | 否 | 通知提醒设置。 |
| dingNotify | String | 否 | 是否发送钉钉弹框通知：   - 1：发送待办弹窗通知 |
| reminderTimeStamp | Long | 否 | 待办任务的提醒时间，Unix时间戳，单位毫秒。要求必须大于当前时间，推荐设置为早于待办截止时间的5～10分钟。 |

### 请求示例

HTTP

```
POST /v1.0/todo/users/me/personalTasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e41e901aa7293468b9a9f4afasdxcbbc
Content-Type:application/json

{
  "subject" : "待办标题",
  "description" : "待办备注信息",
  "dueTime" : 1703750708595,
  "executorIds" : [ "executorUnionId" ],
  "participantIds" : [ "participantUnionId" ],
  "notifyConfigs" : {
    "dingNotify" : "1"
  }
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
    public static com.aliyun.dingtalktodo_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktodo_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalktodo_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalktodo_1_0.models.CreatePersonalTodoTaskHeaders createPersonalTodoTaskHeaders = new com.aliyun.dingtalktodo_1_0.models.CreatePersonalTodoTaskHeaders();
        createPersonalTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalktodo_1_0.models.CreatePersonalTodoTaskRequest.CreatePersonalTodoTaskRequestNotifyConfigs notifyConfigs = new com.aliyun.dingtalktodo_1_0.models.CreatePersonalTodoTaskRequest.CreatePersonalTodoTaskRequestNotifyConfigs()
                .setDingNotify("1");
        com.aliyun.dingtalktodo_1_0.models.CreatePersonalTodoTaskRequest createPersonalTodoTaskRequest = new com.aliyun.dingtalktodo_1_0.models.CreatePersonalTodoTaskRequest()
                .setSubject("待办标题")
                .setDescription("待办备注信息")
                .setDueTime(1703750708595L)
                .setExecutorIds(java.util.Arrays.asList(
                    "executorUnionId"
                ))
                .setParticipantIds(java.util.Arrays.asList(
                    "participantUnionId"
                ))
                .setNotifyConfigs(notifyConfigs);
        try {
            client.createPersonalTodoTaskWithOptions(createPersonalTodoTaskRequest, createPersonalTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_personal_todo_task_headers = dingtalktodo__1__0_models.CreatePersonalTodoTaskHeaders()
        create_personal_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        notify_configs = dingtalktodo__1__0_models.CreatePersonalTodoTaskRequestNotifyConfigs(
            ding_notify='1'
        )
        create_personal_todo_task_request = dingtalktodo__1__0_models.CreatePersonalTodoTaskRequest(
            subject='待办标题',
            description='待办备注信息',
            due_time=1703750708595,
            executor_ids=[
                'executorUnionId'
            ],
            participant_ids=[
                'participantUnionId'
            ],
            notify_configs=notify_configs
        )
        try:
            client.create_personal_todo_task_with_options(create_personal_todo_task_request, create_personal_todo_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_personal_todo_task_headers = dingtalktodo__1__0_models.CreatePersonalTodoTaskHeaders()
        create_personal_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        notify_configs = dingtalktodo__1__0_models.CreatePersonalTodoTaskRequestNotifyConfigs(
            ding_notify='1'
        )
        create_personal_todo_task_request = dingtalktodo__1__0_models.CreatePersonalTodoTaskRequest(
            subject='待办标题',
            description='待办备注信息',
            due_time=1703750708595,
            executor_ids=[
                'executorUnionId'
            ],
            participant_ids=[
                'participantUnionId'
            ],
            notify_configs=notify_configs
        )
        try:
            await client.create_personal_todo_task_with_options_async(create_personal_todo_task_request, create_personal_todo_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreatePersonalTodoTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreatePersonalTodoTaskRequest\notifyConfigs;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreatePersonalTodoTaskRequest;
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
        $createPersonalTodoTaskHeaders = new CreatePersonalTodoTaskHeaders([]);
        $createPersonalTodoTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $notifyConfigs = new notifyConfigs([
            "dingNotify" => "1"
        ]);
        $createPersonalTodoTaskRequest = new CreatePersonalTodoTaskRequest([
            "subject" => "待办标题",
            "description" => "待办备注信息",
            "dueTime" => 1703750708595,
            "executorIds" => [
                "executorUnionId"
            ],
            "participantIds" => [
                "participantUnionId"
            ],
            "notifyConfigs" => $notifyConfigs
        ]);
        try {
            $client->createPersonalTodoTaskWithOptions($createPersonalTodoTaskRequest, $createPersonalTodoTaskHeaders, new RuntimeOptions([]));
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
  dingtalktodo_1_0  "github.com/alibabacloud-go/dingtalk/todo_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  createPersonalTodoTaskHeaders := &dingtalktodo_1_0.CreatePersonalTodoTaskHeaders{}
  createPersonalTodoTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  notifyConfigs := &dingtalktodo_1_0.CreatePersonalTodoTaskRequestNotifyConfigs{
    DingNotify: tea.String("1"),
  }
  createPersonalTodoTaskRequest := &dingtalktodo_1_0.CreatePersonalTodoTaskRequest{
    Subject: tea.String("待办标题"),
    Description: tea.String("待办备注信息"),
    DueTime: tea.Int64(1703750708595),
    ExecutorIds: []*string{tea.String("executorUnionId")},
    ParticipantIds: []*string{tea.String("participantUnionId")},
    NotifyConfigs: notifyConfigs,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreatePersonalTodoTaskWithOptions(createPersonalTodoTaskRequest, createPersonalTodoTaskHeaders, &util.RuntimeOptions{})
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
import dingtalktodo_1_0, * as $dingtalktodo_1_0 from '@alicloud/dingtalk/todo_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalktodo_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalktodo_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createPersonalTodoTaskHeaders = new $dingtalktodo_1_0.CreatePersonalTodoTaskHeaders({ });
    createPersonalTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let notifyConfigs = new $dingtalktodo_1_0.CreatePersonalTodoTaskRequestNotifyConfigs({
      dingNotify: "1",
    });
    let createPersonalTodoTaskRequest = new $dingtalktodo_1_0.CreatePersonalTodoTaskRequest({
      subject: "待办标题",
      description: "待办备注信息",
      dueTime: 1703750708595,
      executorIds: [
        "executorUnionId"
      ],
      participantIds: [
        "participantUnionId"
      ],
      notifyConfigs: notifyConfigs,
    });
    try {
      await client.createPersonalTodoTaskWithOptions(createPersonalTodoTaskRequest, createPersonalTodoTaskHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreatePersonalTodoTaskHeaders createPersonalTodoTaskHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreatePersonalTodoTaskHeaders();
            createPersonalTodoTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreatePersonalTodoTaskRequest.CreatePersonalTodoTaskRequestNotifyConfigs notifyConfigs = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreatePersonalTodoTaskRequest.CreatePersonalTodoTaskRequestNotifyConfigs
            {
                DingNotify = "1",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreatePersonalTodoTaskRequest createPersonalTodoTaskRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreatePersonalTodoTaskRequest
            {
                Subject = "待办标题",
                Description = "待办备注信息",
                DueTime = 1703750708595,
                ExecutorIds = new List<string>
                {
                    "executorUnionId"
                },
                ParticipantIds = new List<string>
                {
                    "participantUnionId"
                },
                NotifyConfigs = notifyConfigs,
            };
            try
            {
                client.CreatePersonalTodoTaskWithOptions(createPersonalTodoTaskRequest, createPersonalTodoTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| taskId | String | 待办ID。 |
| createdTime | Long | 创建时间，Unix时间戳，单位毫秒。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "taskId" : "task123abc",
  "createdTime" : 1703750708595
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.taskCreate.lockError | todo.taskCreate.lockError | 创建待办根据sourceId加锁失败 |
| 400 | todo.taskCreate.paramError | task exist | 待办任务已存在 |
| 400 | todo.taskCreate.paramError | subject is oversize | 待办标题长度超出限制 |
| 400 | todo.taskCreate.paramError | description is oversize | 待办描述长度超出限制 |
| 400 | todo.taskCreate.paramError | executors is oversize | 待办执行人超出限制 |
| 400 | todo.taskCreate.paramError | participants is oversize | 待办参与人超出限制 |
| 400 | todo.taskCreate.paramError | dueTime is invalid | 待办截止时间非法 |
| 400 | todo.taskCreate.paramError | todo.taskCreate.paramError | 创建待办参数异常 |
| 400 | todo.taskCreate.flowControlError | flowControl because of executorId or orgId | 创建待办针对执行者或者企业进行了限流处理 |
| 400 | todo.taskCreate.systemError | todo.taskCreate.systemError | 创建待办系统内部异常 |
| 400 | todo.taskCreate.tokenTypeError | token type is not match | 授权类型错误，本接口需要使用个人身份访问凭证 |
