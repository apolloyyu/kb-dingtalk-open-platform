---
title: "创建协作空间任务"
source_url: "https://open.dingtalk.com/document/development/api-createtask"
namespace: "development"
slug: "api-createtask"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉快办 > 创建协作空间任务"
doc_id: "XrBO1KkjsM"
updated_at: "2026-06-04 14:25:10"
---

> Source: https://open.dingtalk.com/document/development/api-createtask
> Path: 应用开发 / 服务端API / 钉钉快办 > 创建协作空间任务
> Updated: 2026-06-04 14:25:10

# 创建协作空间任务

调用本接口，创建一个协作空间任务。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/tasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-TeamSphere.Project.ReadWrite-钉钉快办管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| projectId | String | 是 | 协作空间id。 |
| content | String | 是 | 任务标题。 |
| executorId | String | 否 | 执行者userId。 |
| dueDate | String | 否 | 任务截止时间。 |
| note | String | 否 | 任务备注。 |
| customfields | Array | 否 | 自定义字段列表。 |
| customfieldName | String | 否 | 自定义字段名称。 |
| customfieldId | String | 否 | 自定义字段id。 |
| value | Array | 否 | 自定义字段值。 |
| title | String | 否 | 自定义字段显示值。 |
| id | String | 否 | 字段值ID。  **[!NOTE]**    用于统计, 自动化触发条件作用; 对于成员类型的字段这个值需要填写用户ID, 可以利用通讯录接口响应中的 userId 字段。 |
| thumbUrl | String | 否 | 用户头像地址。  **[!NOTE]**    对于成员类型的字段这个值需要填写用户头像的地址, 可以利用通讯录接口响应中的 thumbUrl 字段。 |
| disableNotification | Boolean | 否 | 是否禁止通知：   - true：禁止 - false：不禁止 |
| disableActivity | Boolean | 否 | 是否禁止动态：   - true：禁止 - false：不禁止 |

### 请求示例

HTTP

```
POST /v1.0/teamSphere/users/173xxxx/tasks HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "projectId" : "62c25e3b376exxxxxx",
  "content" : "任务标题",
  "executorId" : "173xxxx",
  "dueDate" : "2022-06-13T07:36:50.318Z",
  "note" : "我是一条任务备注",
  "customfields" : [ {
    "customfieldName" : "自定义字段-文本",
    "customfieldId" : "62fb0bxxxxxxx",
    "value" : [ {
      "title" : "我是自定义字段显示值"
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
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkteam_sphere_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkteam_sphere_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkteam_sphere_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskHeaders createTaskHeaders = new com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskHeaders();
        createTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfieldsValue customfields0Value0 = new com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfieldsValue()
                .setTitle("我是自定义字段显示值");
        com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfields customfields0 = new com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfields()
                .setCustomfieldName("自定义字段-文本")
                .setCustomfieldId("62fb0bxxxxxxx")
                .setValue(java.util.Arrays.asList(
                    customfields0Value0
                ));
        com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskRequest createTaskRequest = new com.aliyun.dingtalkteam_sphere_1_0.models.CreateTaskRequest()
                .setProjectId("62c25e3b376exxxxxx")
                .setContent("任务标题")
                .setExecutorId("173xxxx")
                .setDueDate("2022-06-13T07:36:50.318Z")
                .setNote("我是一条任务备注")
                .setCustomfields(java.util.Arrays.asList(
                    customfields0
                ));
        try {
            client.createTaskWithOptions("173xxxx", createTaskRequest, createTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.team_sphere_1_0.client import Client as dingtalkteamSphere_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.team_sphere_1_0 import models as dingtalkteam_sphere__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkteamSphere_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkteamSphere_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_task_headers = dingtalkteam_sphere__1__0_models.CreateTaskHeaders()
        create_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        customfields_0value_0 = dingtalkteam_sphere__1__0_models.CreateTaskRequestCustomfieldsValue(
            title='我是自定义字段显示值'
        )
        customfields_0 = dingtalkteam_sphere__1__0_models.CreateTaskRequestCustomfields(
            customfield_name='自定义字段-文本',
            customfield_id='62fb0bxxxxxxx',
            value=[
                customfields_0value_0
            ]
        )
        create_task_request = dingtalkteam_sphere__1__0_models.CreateTaskRequest(
            project_id='62c25e3b376exxxxxx',
            content='任务标题',
            executor_id='173xxxx',
            due_date='2022-06-13T07:36:50.318Z',
            note='我是一条任务备注',
            customfields=[
                customfields_0
            ]
        )
        try:
            client.create_task_with_options('173xxxx', create_task_request, create_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_task_headers = dingtalkteam_sphere__1__0_models.CreateTaskHeaders()
        create_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        customfields_0value_0 = dingtalkteam_sphere__1__0_models.CreateTaskRequestCustomfieldsValue(
            title='我是自定义字段显示值'
        )
        customfields_0 = dingtalkteam_sphere__1__0_models.CreateTaskRequestCustomfields(
            customfield_name='自定义字段-文本',
            customfield_id='62fb0bxxxxxxx',
            value=[
                customfields_0value_0
            ]
        )
        create_task_request = dingtalkteam_sphere__1__0_models.CreateTaskRequest(
            project_id='62c25e3b376exxxxxx',
            content='任务标题',
            executor_id='173xxxx',
            due_date='2022-06-13T07:36:50.318Z',
            note='我是一条任务备注',
            customfields=[
                customfields_0
            ]
        )
        try:
            await client.create_task_with_options_async('173xxxx', create_task_request, create_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\CreateTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\CreateTaskRequest\customfields\value;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\CreateTaskRequest\customfields;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\CreateTaskRequest;
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
        $createTaskHeaders = new CreateTaskHeaders([]);
        $createTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $customfields0Value0 = new value([
            "title" => "我是自定义字段显示值"
        ]);
        $customfields0 = new customfields([
            "customfieldName" => "自定义字段-文本",
            "customfieldId" => "62fb0bxxxxxxx",
            "value" => [
                $customfields0Value0
            ]
        ]);
        $createTaskRequest = new CreateTaskRequest([
            "projectId" => "62c25e3b376exxxxxx",
            "content" => "任务标题",
            "executorId" => "173xxxx",
            "dueDate" => "2022-06-13T07:36:50.318Z",
            "note" => "我是一条任务备注",
            "customfields" => [
                $customfields0
            ]
        ]);
        try {
            $client->createTaskWithOptions("173xxxx", $createTaskRequest, $createTaskHeaders, new RuntimeOptions([]));
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
  dingtalkteamsphere_1_0  "github.com/alibabacloud-go/dingtalk/teamSphere_1_0"
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
func CreateClient () (_result *dingtalkteamsphere_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkteamsphere_1_0.Client{}
  _result, _err = dingtalkteamsphere_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createTaskHeaders := &dingtalkteamsphere_1_0.CreateTaskHeaders{}
  createTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  customfields0Value0 := &dingtalkteamsphere_1_0.CreateTaskRequestCustomfieldsValue{
    Title: tea.String("我是自定义字段显示值"),
  }
  customfields0 := &dingtalkteamsphere_1_0.CreateTaskRequestCustomfields{
    CustomfieldName: tea.String("自定义字段-文本"),
    CustomfieldId: tea.String("62fb0bxxxxxxx"),
    Value: []*dingtalkteamsphere_1_0.CreateTaskRequestCustomfieldsValue{customfields0Value0},
  }
  createTaskRequest := &dingtalkteamsphere_1_0.CreateTaskRequest{
    ProjectId: tea.String("62c25e3b376exxxxxx"),
    Content: tea.String("任务标题"),
    ExecutorId: tea.String("173xxxx"),
    DueDate: tea.String("2022-06-13T07:36:50.318Z"),
    Note: tea.String("我是一条任务备注"),
    Customfields: []*dingtalkteamsphere_1_0.CreateTaskRequestCustomfields{customfields0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTaskWithOptions(tea.String("173xxxx"), createTaskRequest, createTaskHeaders, &util.RuntimeOptions{})
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
const dingtalkteamSphere_1_0 = require('@alicloud/dingtalk/teamSphere_1_0');
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
    return new dingtalkteamSphere_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createTaskHeaders = new dingtalkteamSphere_1_0.CreateTaskHeaders({ });
    createTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let customfields0Value0 = new dingtalkteamSphere_1_0.CreateTaskRequestCustomfieldsValue({
      title: '我是自定义字段显示值',
    });
    let customfields0 = new dingtalkteamSphere_1_0.CreateTaskRequestCustomfields({
      customfieldName: '自定义字段-文本',
      customfieldId: '62fb0bxxxxxxx',
      value: [
        customfields0Value0
      ],
    });
    let createTaskRequest = new dingtalkteamSphere_1_0.CreateTaskRequest({
      projectId: '62c25e3b376exxxxxx',
      content: '任务标题',
      executorId: '173xxxx',
      dueDate: '2022-06-13T07:36:50.318Z',
      note: '我是一条任务备注',
      customfields: [
        customfields0
      ],
    });
    try {
      await client.createTaskWithOptions('173xxxx', createTaskRequest, createTaskHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskHeaders createTaskHeaders = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskHeaders();
            createTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields.CreateTaskRequestCustomfieldsValue customfields0Value0 = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields.CreateTaskRequestCustomfieldsValue
            {
                Title = "我是自定义字段显示值",
            };
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields customfields0 = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields
            {
                CustomfieldName = "自定义字段-文本",
                CustomfieldId = "62fb0bxxxxxxx",
                Value = new List<AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields.CreateTaskRequestCustomfieldsValue>
                {
                    customfields0Value0
                },
            };
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest createTaskRequest = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest
            {
                ProjectId = "62c25e3b376exxxxxx",
                Content = "任务标题",
                ExecutorId = "173xxxx",
                DueDate = "2022-06-13T07:36:50.318Z",
                Note = "我是一条任务备注",
                Customfields = new List<AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields>
                {
                    customfields0
                },
            };
            try
            {
                client.CreateTaskWithOptions("173xxxx", createTaskRequest, createTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果对象。 |
| taskId | String | 任务id。 |
| content | String | 任务标题。 |
| involveMembers | Array of String | 任务参与者id。 |
| projectId | String | 项目id。 |
| executorId | String | 任务执行者userId。 |
| creatorId | String | 任务创建者userId。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| note | String | 任务备注。 |
| dueDate | String | 任务截止时间。 |
| priority | Integer | 任务优先级。 |
| customfields | Array | 自定义字段列表。 |
| customfieldId | String | 自定义字段id。 |
| value | Array | 自定义字段值列表。 |
| title | String | 自定义字段显示值。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "taskId" : "62a697c053c2ef5xxxxxx",
    "content" : "任务标题",
    "involveMembers" : [ "173xxxx" ],
    "projectId" : "62c25e3b376ecxxxxxx",
    "executorId" : "173xxxx",
    "creatorId" : "173xxxxx",
    "created" : "2021-08-13T07:36:50.318Z",
    "updated" : "2021-08-13T07:36:50.318Z",
    "note" : "我是一条备注",
    "dueDate" : "2022-08-13T07:36:50.318Z",
    "priority" : -10,
    "customfields" : [ {
      "customfieldId" : "625bcxdxxxxxx",
      "value" : [ {
        "title" : "我是自定义字段显示值"
      } ]
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在 |
| 500 | server.error | %s | 请参考ErrorMessage中的errorMessage内容 |
