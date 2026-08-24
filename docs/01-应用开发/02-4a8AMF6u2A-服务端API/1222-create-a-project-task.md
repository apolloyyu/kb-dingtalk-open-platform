---
title: "创建项目任务"
source_url: "https://open.dingtalk.com/document/development/create-a-project-task"
namespace: "development"
slug: "create-a-project-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 创建项目任务"
doc_id: "42SwEyXX6I"
updated_at: "2026-06-03 09:26:02"
---

> Source: https://open.dingtalk.com/document/development/create-a-project-task
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务 > 项目任务 > 创建项目任务
> Updated: 2026-06-03 09:26:02

# 创建项目任务

调用本接口，创建一个钉钉项目任务。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/tasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Write.All-项目应用任务写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| projectId | String | 是 | 项目id。  **[!NOTE]**    目前需要从项目链接中获取该参数值，获取步骤：进入**项目** > 右上角单击**菜单** > **复制链接** 得到的项目链接示例：https://www.teambition.com/project/62c794xxxxx，project下一级路径的值就是项目id。 |
| content | String | 是 | 任务标题。 |
| executorId | String | 否 | 任务执行者userId。 |
| dueDate | String | 否 | 任务截止时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| note | String | 否 | 任务备注。 |
| priority | Integer | 否 | 任务优先级，调用[查询优先级列表](1244-query-a-priority-list.md)接口获取priorityId值。 |
| customfields | Array | 否 | 自定义字段列表。  **[!NOTE]**    自定义字段目前只支持单选、多选、数字、文本和日期，其他类型暂不支持。 |
| customfieldName | String | 否 | 自定义字段名称。  **[!NOTE]**    该字段值需要与自定义字段名保持完全一致。 |
| customfieldId | String | 否 | 自定义字段ID。  **[!NOTE]**    自定义字段ID，暂未透出，目前该参数字段值不填即可。 |
| value | Array | 否 | 自定义字段值列表。 |
| title | String | 否 | 自定义字段值。   - 如果自定义字段为单选或多选类型，该参数值需要与设置的选项值保持完全一致。 - 如果自定义字段为日期类型，该参数值格式为yyyy-MM-dd HH:mm:ss。 |
| id | String | 否 | 字段值id，如果该字段是成员字段，那么此处应该填写成员的在Teambition系统中的userId，获取Teambition用户id请参阅文档[根据userId获取Teambition项目用户ID](1256-obtain-dingtalk-teambition-user-id-based-on-userid.md)。 |
| thumbUrl | String | 否 | 如果该字段是成员字段，那么此处应该填写成员的头像地址。 |
| stageId | String | 否 | 任务列表ID，可调用[查询项目中的任务](1229-query-tasks-in-a-project.md)接口获取stageId。 |
| parentTaskId | String | 否 | 父任务id，可调用[查询项目中的任务](1229-query-tasks-in-a-project.md)接口获取taskId。 |
| scenariofieldconfigId | String | 否 | 任务类型id，任务类型比如：缺陷、需求，可调用[查询项目中的任务](1229-query-tasks-in-a-project.md)接口获取scenariofieldconfigId。 |
| startDate | String | 否 | 任务开始时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| visible | String | 否 | 任务的可见性规则。   - involves：仅任务参与者可见 - members：项目成员可见 |

### 请求示例

HTTP

```
POST /v1.0/project/users/173xxxx/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxx
Content-Type:application/json

{
  "projectId" : "adbx22xxxxx",
  "content" : "我是标题",
  "executorId" : "173xxxx",
  "dueDate" : "2022-08-13T07:36:50.318Z",
  "note" : "我是一条备注",
  "priority" : -10,
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
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkproject_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkproject_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkproject_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkproject_1_0.models.CreateTaskHeaders createTaskHeaders = new com.aliyun.dingtalkproject_1_0.models.CreateTaskHeaders();
        createTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfieldsValue customfields0Value0 = new com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfieldsValue()
                .setTitle("我是自定义字段显示值");
        com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfields customfields0 = new com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest.CreateTaskRequestCustomfields()
                .setCustomfieldName("自定义字段-文本")
                .setCustomfieldId("62fb0bxxxxxxx")
                .setValue(java.util.Arrays.asList(
                    customfields0Value0
                ));
        com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest createTaskRequest = new com.aliyun.dingtalkproject_1_0.models.CreateTaskRequest()
                .setProjectId("adbx22xxxxx")
                .setContent("我是标题")
                .setExecutorId("173xxxx")
                .setDueDate("2022-08-13T07:36:50.318Z")
                .setNote("我是一条备注")
                .setPriority(-10)
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
import sys

from typing import List

from alibabacloud_dingtalk.project_1_0.client import Client as dingtalkproject_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.project_1_0 import models as dingtalkproject__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkproject_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkproject_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_task_headers = dingtalkproject__1__0_models.CreateTaskHeaders()
        create_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        customfields_0value_0 = dingtalkproject__1__0_models.CreateTaskRequestCustomfieldsValue(
            title='我是自定义字段显示值'
        )
        customfields_0 = dingtalkproject__1__0_models.CreateTaskRequestCustomfields(
            customfield_name='自定义字段-文本',
            customfield_id='62fb0bxxxxxxx',
            value=[
                customfields_0value_0
            ]
        )
        create_task_request = dingtalkproject__1__0_models.CreateTaskRequest(
            project_id='adbx22xxxxx',
            content='我是标题',
            executor_id='173xxxx',
            due_date='2022-08-13T07:36:50.318Z',
            note='我是一条备注',
            priority=-10,
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
        create_task_headers = dingtalkproject__1__0_models.CreateTaskHeaders()
        create_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        customfields_0value_0 = dingtalkproject__1__0_models.CreateTaskRequestCustomfieldsValue(
            title='我是自定义字段显示值'
        )
        customfields_0 = dingtalkproject__1__0_models.CreateTaskRequestCustomfields(
            customfield_name='自定义字段-文本',
            customfield_id='62fb0bxxxxxxx',
            value=[
                customfields_0value_0
            ]
        )
        create_task_request = dingtalkproject__1__0_models.CreateTaskRequest(
            project_id='adbx22xxxxx',
            content='我是标题',
            executor_id='173xxxx',
            due_date='2022-08-13T07:36:50.318Z',
            note='我是一条备注',
            priority=-10,
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

use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateTaskRequest\customfields\value;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateTaskRequest\customfields;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateTaskRequest;
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
            "projectId" => "adbx22xxxxx",
            "content" => "我是标题",
            "executorId" => "173xxxx",
            "dueDate" => "2022-08-13T07:36:50.318Z",
            "note" => "我是一条备注",
            "priority" => -10,
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
  "os"
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkproject_1_0  "github.com/alibabacloud-go/dingtalk/project_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkproject_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkproject_1_0.Client{}
  _result, _err = dingtalkproject_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createTaskHeaders := &dingtalkproject_1_0.CreateTaskHeaders{}
  createTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  customfields0Value0 := &dingtalkproject_1_0.CreateTaskRequestCustomfieldsValue{
    Title: tea.String("我是自定义字段显示值"),
  }
  customfields0 := &dingtalkproject_1_0.CreateTaskRequestCustomfields{
    CustomfieldName: tea.String("自定义字段-文本"),
    CustomfieldId: tea.String("62fb0bxxxxxxx"),
    Value: []*dingtalkproject_1_0.CreateTaskRequestCustomfieldsValue{customfields0Value0},
  }
  createTaskRequest := &dingtalkproject_1_0.CreateTaskRequest{
    ProjectId: tea.String("adbx22xxxxx"),
    Content: tea.String("我是标题"),
    ExecutorId: tea.String("173xxxx"),
    DueDate: tea.String("2022-08-13T07:36:50.318Z"),
    Note: tea.String("我是一条备注"),
    Priority: tea.Int32(-10),
    Customfields: []*dingtalkproject_1_0.CreateTaskRequestCustomfields{customfields0},
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
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkproject_1_0, * as $dingtalkproject_1_0 from '@alicloud/dingtalk/project_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkproject_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkproject_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createTaskHeaders = new $dingtalkproject_1_0.CreateTaskHeaders({ });
    createTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let customfields0Value0 = new $dingtalkproject_1_0.CreateTaskRequestCustomfieldsValue({
      title: "我是自定义字段显示值",
    });
    let customfields0 = new $dingtalkproject_1_0.CreateTaskRequestCustomfields({
      customfieldName: "自定义字段-文本",
      customfieldId: "62fb0bxxxxxxx",
      value: [
        customfields0Value0
      ],
    });
    let createTaskRequest = new $dingtalkproject_1_0.CreateTaskRequest({
      projectId: "adbx22xxxxx",
      content: "我是标题",
      executorId: "173xxxx",
      dueDate: "2022-08-13T07:36:50.318Z",
      note: "我是一条备注",
      priority: -10,
      customfields: [
        customfields0
      ],
    });
    try {
      await client.createTaskWithOptions("173xxxx", createTaskRequest, createTaskHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkproject_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkproject_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkproject_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskHeaders createTaskHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskHeaders();
            createTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields.CreateTaskRequestCustomfieldsValue customfields0Value0 = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields.CreateTaskRequestCustomfieldsValue
            {
                Title = "我是自定义字段显示值",
            };
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields customfields0 = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields
            {
                CustomfieldName = "自定义字段-文本",
                CustomfieldId = "62fb0bxxxxxxx",
                Value = new List<AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields.CreateTaskRequestCustomfieldsValue>
                {
                    customfields0Value0
                },
            };
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest createTaskRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest
            {
                ProjectId = "adbx22xxxxx",
                Content = "我是标题",
                ExecutorId = "173xxxx",
                DueDate = "2022-08-13T07:36:50.318Z",
                Note = "我是一条备注",
                Priority = -10,
                Customfields = new List<AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateTaskRequest.CreateTaskRequestCustomfields>
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
| involveMembers | Array of String | 参与者userId列表。 |
| projectId | String | 项目id。 |
| executorId | String | 任务执行者userId。 |
| creatorId | String | 任务创建者userId。 |
| created | String | 任务创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| updated | String | 任务更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| note | String | 任务备注。 |
| dueDate | String | 任务截止时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| priority | Integer | 任务优先级。   - 使用项目默认的优先级，如下图所示。优先级默认为以下。    - **-10**：较低，默认值。   - **0**：普通   - **1**：紧急   - **2**：非常紧急      - 用户自定义优先级，如下图所示，新增一般紧急并调整优先级顺序等。该参数值以接口实际调用结果为准。优先级越高，数值越大。 |
| customfields | Array | 自定义字段列表。 |
| customfieldId | String | 自定义字段ID。  **[!NOTE]**    该参数暂未透出，目前不返回。 |
| value | Array | 自定义字段值列表。 |
| title | String | 自定义字段值。 |

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
