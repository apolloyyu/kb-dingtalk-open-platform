---
title: "获取任务详情"
source_url: "https://open.dingtalk.com/document/development/get-task-details"
namespace: "development"
slug: "get-task-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 获取任务详情"
doc_id: "63nyYsLGSB"
updated_at: "2025-10-09 18:06:40"
---

> Source: https://open.dingtalk.com/document/development/get-task-details
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务 > 项目任务 > 获取任务详情
> Updated: 2025-10-09 18:06:40

# 获取任务详情

调用本接口获取任务详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/tasks |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Read.All-项目应用任务读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 否 | 任务ID集合，多个taskId，使用逗号分隔，可通过调用[查询项目中的任务](1229-query-tasks-in-a-project.md)接口，获取返回参数`taskId`字段。  **[!NOTE]**    与parentTaskId冲突（选其一）。 |
| parentTaskId | String | 否 | 父任务ID。  **[!NOTE]**    与taskId冲突（选其一）。 |

### 请求示例

HTTP

```
GET /v1.0/project/users/0517xxx/tasks?taskId=60a2187eb72xxxxxxx&parentTaskId=60a2187eb72xxxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json
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
        com.aliyun.dingtalkproject_1_0.models.GetTaskByIdsHeaders getTaskByIdsHeaders = new com.aliyun.dingtalkproject_1_0.models.GetTaskByIdsHeaders();
        getTaskByIdsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.GetTaskByIdsRequest getTaskByIdsRequest = new com.aliyun.dingtalkproject_1_0.models.GetTaskByIdsRequest()
                .setTaskId("60a2187eb72xxxxxxx")
                .setParentTaskId("60a2187eb72xxxxxxx");
        try {
            client.getTaskByIdsWithOptions("0517xxx", getTaskByIdsRequest, getTaskByIdsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_task_by_ids_headers = dingtalkproject__1__0_models.GetTaskByIdsHeaders()
        get_task_by_ids_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_task_by_ids_request = dingtalkproject__1__0_models.GetTaskByIdsRequest(
            task_id='60a2187eb72xxxxxxx',
            parent_task_id='60a2187eb72xxxxxxx'
        )
        try:
            client.get_task_by_ids_with_options('0517xxx', get_task_by_ids_request, get_task_by_ids_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_task_by_ids_headers = dingtalkproject__1__0_models.GetTaskByIdsHeaders()
        get_task_by_ids_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_task_by_ids_request = dingtalkproject__1__0_models.GetTaskByIdsRequest(
            task_id='60a2187eb72xxxxxxx',
            parent_task_id='60a2187eb72xxxxxxx'
        )
        try:
            await client.get_task_by_ids_with_options_async('0517xxx', get_task_by_ids_request, get_task_by_ids_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\GetTaskByIdsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\GetTaskByIdsRequest;
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
        $getTaskByIdsHeaders = new GetTaskByIdsHeaders([]);
        $getTaskByIdsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getTaskByIdsRequest = new GetTaskByIdsRequest([
            "taskId" => "60a2187eb72xxxxxxx",
            "parentTaskId" => "60a2187eb72xxxxxxx"
        ]);
        try {
            $client->getTaskByIdsWithOptions("0517xxx", $getTaskByIdsRequest, $getTaskByIdsHeaders, new RuntimeOptions([]));
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
  dingtalkproject_1_0  "github.com/alibabacloud-go/dingtalk/project_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  getTaskByIdsHeaders := &dingtalkproject_1_0.GetTaskByIdsHeaders{}
  getTaskByIdsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getTaskByIdsRequest := &dingtalkproject_1_0.GetTaskByIdsRequest{
    TaskId: tea.String("60a2187eb72xxxxxxx"),
    ParentTaskId: tea.String("60a2187eb72xxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetTaskByIdsWithOptions(tea.String("0517xxx"), getTaskByIdsRequest, getTaskByIdsHeaders, &util.RuntimeOptions{})
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
    let getTaskByIdsHeaders = new $dingtalkproject_1_0.GetTaskByIdsHeaders({ });
    getTaskByIdsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getTaskByIdsRequest = new $dingtalkproject_1_0.GetTaskByIdsRequest({
      taskId: "60a2187eb72xxxxxxx",
      parentTaskId: "60a2187eb72xxxxxxx",
    });
    try {
      await client.getTaskByIdsWithOptions("0517xxx", getTaskByIdsRequest, getTaskByIdsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetTaskByIdsHeaders getTaskByIdsHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetTaskByIdsHeaders();
            getTaskByIdsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetTaskByIdsRequest getTaskByIdsRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetTaskByIdsRequest
            {
                TaskId = "60a2187eb72xxxxxxx",
                ParentTaskId = "60a2187eb72xxxxxxx",
            };
            try
            {
                client.GetTaskByIdsWithOptions("0517xxx", getTaskByIdsRequest, getTaskByIdsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 任务详情集合。 |
| taskId | String | 任务ID。 |
| content | String | 任务标题。 |
| note | String | 任务备注。 |
| projectId | String | 项目ID。 |
| ancestorIds | Array of String | 祖先任务ID。 |
| parentTaskId | String | 父任务ID。 |
| taskflowStatusId | String | 任务状态ID。 |
| taskListId | String | 任务分组ID。 |
| taskStageId | String | 任务列ID。 |
| tagIds | Array of String | 标签ID。 |
| creatorId | String | 创建人ID。 |
| executorId | String | 执行人ID。 |
| involveMembers | Array of String | 参与者ID。 |
| priority | Integer | 任务优先级。 |
| storyPoint | String | StoryPoint。 |
| recurrence | Array of String | 重复规则。 |
| isDone | Boolean | 是否任务已完成。 |
| isArchived | Boolean | 是否任务放入回收站。 |
| visible | String | 任务隐私性：   - involves：表达仅参与者可见 - members：表达项目成员可见 |
| uniqueId | String | 任务数字ID。 |
| startDate | String | 任务开始时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| dueDate | String | 任务截止时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| accomplishTime | String | 任务完成时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| created | String | 创建时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| updated | String | 更新时间(UTC)，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| scenarioFieldConfigId | String | 任务类型ID。 |
| sprintId | String | 迭代ID。 |
| customFields | Array | 自定义字段值集合。 |
| customFieldId | String | 自定义字段ID。 |
| type | String | 自定义字段类型。 |
| value | Array | 字段值集合。 |
| customFieldValueId | String | 字段值ID。 |
| title | String | 字段值内容。 |
| metaString | String | 字段值元属性。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "taskId" : "60a2187eb72xxxxxxx",
    "content" : "任务标题",
    "note" : "任务备注",
    "projectId" : "62c25e3b376ecxxxxxxx",
    "ancestorIds" : [ "60a2187eb72xxxxxxx" ],
    "parentTaskId" : "60a2187eb72xxxxxxx",
    "taskflowStatusId" : "6722xxxxxxxx",
    "taskListId" : "6922xxxxxxxx",
    "taskStageId" : "6622134xxxxxx",
    "tagIds" : [ "6622134xxxxxx" ],
    "creatorId" : "0517xxxxxxx",
    "executorId" : "0517xxxxxxx",
    "involveMembers" : [ "0517xxxxxxx" ],
    "priority" : 0,
    "storyPoint" : "1",
    "recurrence" : [ "RRULE:FREQ=WEEKLY;INTERVAL=1" ],
    "isDone" : true,
    "isArchived" : false,
    "visible" : "member",
    "uniqueId" : "0",
    "startDate" : "2022-07-04T03:29:34.770Z",
    "dueDate" : "2022-07-04T03:29:34.770Z",
    "accomplishTime" : "2022-07-04T03:29:34.770Z",
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z",
    "scenarioFieldConfigId" : "6922xxxxxxxx",
    "sprintId" : "61922xxxxxxxx",
    "customFields" : [ {
      "customFieldId" : "61122xxxxxxxx",
      "type" : "XXXX",
      "value" : [ {
        "customFieldValueId" : "6722223xxxxxxxx",
        "title" : "自定义字段1",
        "metaString" : "拓展数据"
      } ]
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
