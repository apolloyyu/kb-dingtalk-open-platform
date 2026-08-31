---
title: "查询用户任务信息列表"
source_url: "https://open.dingtalk.com/document/development/querying-user-tasks"
namespace: "development"
slug: "querying-user-tasks"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 查询用户任务信息列表"
doc_id: "CU2N8OF8ec"
updated_at: "2026-06-03 09:26:07"
---

> Source: https://open.dingtalk.com/document/development/querying-user-tasks
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 任务 > 项目任务 > 查询用户任务信息列表
> Updated: 2026-06-03 09:26:07

# 查询用户任务信息列表

调用本接口查询用户任务信息列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/search |
| HTTP Method | POST |
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
| roleTypes | String | 是 | 用户的任务角色。  **[!NOTE]**  `creator`、`executor`、`involveMember` 中的一个或多个，多个以英文逗号拼接。例如：`creator,executor`。 |
| tql | String | 否 | tql内容，详情参见[任务筛选TQL说明](1257-the-description-of-the-tql-task.md)使用说明。 |
| nextToken | String | 否 | 分页标，从上一次请求结果中获取。  **[!NOTE]**    nextToken传入后，返回参数为空，则表示数据已全部查询完毕。 |
| maxResults | Integer | 否 | 每页返回最大数量。  **[!NOTE]**    默认10，最大100。 |

### 请求示例

HTTP

```
POST /v1.0/project/users/0517xxx/tasks/search?roleTypes=creator&tql=(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)&nextToken=f279e812xxxxxx&maxResults=10 HTTP/1.1
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
        com.aliyun.dingtalkproject_1_0.models.SearchUserTaskHeaders searchUserTaskHeaders = new com.aliyun.dingtalkproject_1_0.models.SearchUserTaskHeaders();
        searchUserTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.SearchUserTaskRequest searchUserTaskRequest = new com.aliyun.dingtalkproject_1_0.models.SearchUserTaskRequest()
                .setRoleTypes("creator")
                .setTql("(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)")
                .setNextToken("f279e812xxxxxx")
                .setMaxResults("10");
        try {
            client.searchUserTaskWithOptions("0517xxx", searchUserTaskRequest, searchUserTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        search_user_task_headers = dingtalkproject__1__0_models.SearchUserTaskHeaders()
        search_user_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_user_task_request = dingtalkproject__1__0_models.SearchUserTaskRequest(
            role_types='creator',
            tql="(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)",
            next_token='f279e812xxxxxx',
            max_results='10'
        )
        try:
            client.search_user_task_with_options('0517xxx', search_user_task_request, search_user_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_user_task_headers = dingtalkproject__1__0_models.SearchUserTaskHeaders()
        search_user_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_user_task_request = dingtalkproject__1__0_models.SearchUserTaskRequest(
            role_types='creator',
            tql="(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)",
            next_token='f279e812xxxxxx',
            max_results='10'
        )
        try:
            await client.search_user_task_with_options_async('0517xxx', search_user_task_request, search_user_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\SearchUserTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\SearchUserTaskRequest;
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
        $searchUserTaskHeaders = new SearchUserTaskHeaders([]);
        $searchUserTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $searchUserTaskRequest = new SearchUserTaskRequest([
            "roleTypes" => "creator",
            "tql" => "(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)",
            "nextToken" => "f279e812xxxxxx",
            "maxResults" => "10"
        ]);
        try {
            $client->searchUserTaskWithOptions("0517xxx", $searchUserTaskRequest, $searchUserTaskHeaders, new RuntimeOptions([]));
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

  searchUserTaskHeaders := &dingtalkproject_1_0.SearchUserTaskHeaders{}
  searchUserTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  searchUserTaskRequest := &dingtalkproject_1_0.SearchUserTaskRequest{
    RoleTypes: tea.String("creator"),
    Tql: tea.String("(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)"),
    NextToken: tea.String("f279e812xxxxxx"),
    MaxResults: tea.String("10"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SearchUserTaskWithOptions(tea.String("0517xxx"), searchUserTaskRequest, searchUserTaskHeaders, &util.RuntimeOptions{})
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
    let searchUserTaskHeaders = new $dingtalkproject_1_0.SearchUserTaskHeaders({ });
    searchUserTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let searchUserTaskRequest = new $dingtalkproject_1_0.SearchUserTaskRequest({
      roleTypes: "creator",
      tql: "(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)",
      nextToken: "f279e812xxxxxx",
      maxResults: "10",
    });
    try {
      await client.searchUserTaskWithOptions("0517xxx", searchUserTaskRequest, searchUserTaskHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchUserTaskHeaders searchUserTaskHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchUserTaskHeaders();
            searchUserTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchUserTaskRequest searchUserTaskRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchUserTaskRequest
            {
                RoleTypes = "creator",
                Tql = "(text ~ '阅读') AND (executorId = 60c971f3357b5a0a6df0cfd7)",
                NextToken = "f279e812xxxxxx",
                MaxResults = "10",
            };
            try
            {
                client.SearchUserTaskWithOptions("0517xxx", searchUserTaskRequest, searchUserTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| priority | Integer | 任务优先级：   - **-10**：较低 - **0**：普通 - **1**：紧急 - **2**：非常紧急 |
| storyPoint | String | StoryPoint。 |
| recurrence | Array of String | 重复规则。 |
| isDone | Boolean | 是否任务已完成。 |
| isArchived | Boolean | 是否任务放入回收站。 |
| visible | String | 任务隐私性：   - **involves**：表达仅参与者可见 - **members**：表达项目成员可见 |
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
| requestId | String | 请求 ID，请求异常时可提供此 ID，进行问题排查。 |
| nextToken | String | 分页游标。  **[!NOTE]**    nextToken传入后，返回参数为空，则表示数据已全部查询完毕。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "taskId" : "6437c8bc25ca812472212589",
    "content" : "标题",
    "note" : "任务备注",
    "projectId" : "6437c85ba8b58d2b36272aac",
    "ancestorIds" : [ "6437c8bc25ca8124723124123" ],
    "parentTaskId" : "6437c8bc25ca8124723143568",
    "taskflowStatusId" : "6437c85b11c154236add1b9d",
    "taskListId" : "6437c85b11c154236abb1b9c",
    "taskStageId" : "6437c87d8cdf39926535a6fe",
    "tagIds" : [ "XXXXXX" ],
    "creatorId" : "01472825524039877041",
    "executorId" : "01472825524039877041",
    "involveMembers" : [ "01472825524039877041" ],
    "priority" : 0,
    "storyPoint" : "XXXX",
    "recurrence" : [ "XXXXX" ],
    "isDone" : true,
    "isArchived" : false,
    "visible" : "members",
    "uniqueId" : "XXXXX",
    "startDate" : "2022-07-04T03:29:34.770Z",
    "dueDate" : "2022-07-05T03:29:34.770Z",
    "accomplishTime" : "2022-07-05T03:29:34.770Z",
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z",
    "scenarioFieldConfigId" : "6437c85b11c154236add1bb5",
    "sprintId" : "xxxxxxx",
    "customFields" : [ {
      "customFieldId" : "XXXXX",
      "type" : "number",
      "value" : [ {
        "customFieldValueId" : "642fb16c4a622b2e3184229c",
        "title" : "标题",
        "metaString" : "元数据内容"
      } ]
    } ]
  } ],
  "requestId" : "1E4D3C5F-3244-7564-834E-C6F5E78E67A7",
  "nextToken" : "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAbMXT4WVjNKbUstaldRX3lOOHNBbElzcjA5Zw=="
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
