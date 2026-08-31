---
title: "查询项目中的任务"
source_url: "https://open.dingtalk.com/document/development/query-tasks-in-a-project"
namespace: "development"
slug: "query-tasks-in-a-project"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 查询项目中的任务"
doc_id: "XFxugf87aR"
updated_at: "2026-06-04 19:11:40"
---

> Source: https://open.dingtalk.com/document/development/query-tasks-in-a-project
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 任务 > 项目任务 > 查询项目中的任务
> Updated: 2026-06-04 19:11:40

# 查询项目中的任务

调用本接口，可根据指定条件查询项目中的任务。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/projectIds/{projectId}/tasks |
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
| projectId | String | 是 | 项目ID。      目前需要从项目链接中获取该参数值，获取步骤：进入**项目** > 右上角单击**菜单** > **复制链接**。  得到的项目链接示例：`https://www.teambition.com/project/62c794xxxxx` ，project下一级路径的值就是项目ID。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上次接口返回的nextToken。 |
| maxResults | Integer | 否 | 每页返回最大数量。默认10，最大500。 |
| query | String | 否 | 查询条件，可参考[任务筛选TQL说明](1257-the-description-of-the-tql-task.md)。 |

### 请求示例

HTTP

```
GET /v1.0/project/users/0517xxx/projectIds/62c25exxxxx/tasks?nextToken=f279e8xxxxx&maxResults=10&query=involveMembers NOT IN ["0612xx"] AND executorId="057xxx" AND content~标题2 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
        com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectHeaders queryTaskOfProjectHeaders = new com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectHeaders();
        queryTaskOfProjectHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectRequest queryTaskOfProjectRequest = new com.aliyun.dingtalkproject_1_0.models.QueryTaskOfProjectRequest()
                .setNextToken("f279e8xxxxx")
                .setMaxResults(10)
                .setQuery("involveMembers NOT IN [\"0612xx\"] AND executorId=\"057xxx\" AND content~标题2");
        try {
            client.queryTaskOfProjectWithOptions("0517xxx", "62c25exxxxx", queryTaskOfProjectRequest, queryTaskOfProjectHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_task_of_project_headers = dingtalkproject__1__0_models.QueryTaskOfProjectHeaders()
        query_task_of_project_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_task_of_project_request = dingtalkproject__1__0_models.QueryTaskOfProjectRequest(
            next_token='f279e8xxxxx',
            max_results=10,
            query='involveMembers NOT IN ["0612xx"] AND executorId="057xxx" AND content~标题2'
        )
        try:
            client.query_task_of_project_with_options('0517xxx', '62c25exxxxx', query_task_of_project_request, query_task_of_project_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_task_of_project_headers = dingtalkproject__1__0_models.QueryTaskOfProjectHeaders()
        query_task_of_project_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_task_of_project_request = dingtalkproject__1__0_models.QueryTaskOfProjectRequest(
            next_token='f279e8xxxxx',
            max_results=10,
            query='involveMembers NOT IN ["0612xx"] AND executorId="057xxx" AND content~标题2'
        )
        try:
            await client.query_task_of_project_with_options_async('0517xxx', '62c25exxxxx', query_task_of_project_request, query_task_of_project_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\QueryTaskOfProjectHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\QueryTaskOfProjectRequest;
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
        $queryTaskOfProjectHeaders = new QueryTaskOfProjectHeaders([]);
        $queryTaskOfProjectHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryTaskOfProjectRequest = new QueryTaskOfProjectRequest([
            "nextToken" => "f279e8xxxxx",
            "maxResults" => 10,
            "query" => "involveMembers NOT IN [\"0612xx\"] AND executorId=\"057xxx\" AND content~标题2"
        ]);
        try {
            $client->queryTaskOfProjectWithOptions("0517xxx", "62c25exxxxx", $queryTaskOfProjectRequest, $queryTaskOfProjectHeaders, new RuntimeOptions([]));
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

  queryTaskOfProjectHeaders := &dingtalkproject_1_0.QueryTaskOfProjectHeaders{}
  queryTaskOfProjectHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryTaskOfProjectRequest := &dingtalkproject_1_0.QueryTaskOfProjectRequest{
    NextToken: tea.String("f279e8xxxxx"),
    MaxResults: tea.Int32(10),
    Query: tea.String("involveMembers NOT IN [\"0612xx\"] AND executorId=\"057xxx\" AND content~标题2"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryTaskOfProjectWithOptions(tea.String("0517xxx"), tea.String("62c25exxxxx"), queryTaskOfProjectRequest, queryTaskOfProjectHeaders, &util.RuntimeOptions{})
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
    let queryTaskOfProjectHeaders = new $dingtalkproject_1_0.QueryTaskOfProjectHeaders({ });
    queryTaskOfProjectHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryTaskOfProjectRequest = new $dingtalkproject_1_0.QueryTaskOfProjectRequest({
      nextToken: "f279e8xxxxx",
      maxResults: 10,
      query: "involveMembers NOT IN [\"0612xx\"] AND executorId=\"057xxx\" AND content~标题2",
    });
    try {
      await client.queryTaskOfProjectWithOptions("0517xxx", "62c25exxxxx", queryTaskOfProjectRequest, queryTaskOfProjectHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.QueryTaskOfProjectHeaders queryTaskOfProjectHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.QueryTaskOfProjectHeaders();
            queryTaskOfProjectHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.QueryTaskOfProjectRequest queryTaskOfProjectRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.QueryTaskOfProjectRequest
            {
                NextToken = "f279e8xxxxx",
                MaxResults = 10,
                Query = "involveMembers NOT IN [\"0612xx\"] AND executorId=\"057xxx\" AND content~标题2",
            };
            try
            {
                client.QueryTaskOfProjectWithOptions("0517xxx", "62c25exxxxx", queryTaskOfProjectRequest, queryTaskOfProjectHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCount | Integer | 任务总条数。 |
| nextToken | String | 分页游标。 |
| result | Array | 返回的任务列表。 |
| taskId | String | 任务ID。 |
| content | String | 任务标题。 |
| involveMembers | Array of String | 任务参与者userId。 |
| projectId | String | 项目ID。 |
| executorId | String | 执行者userId。 |
| creatorId | String | 创建者userId。 |
| isDeleted | Boolean | 是否已删除。   - **true**：已删除 - **false**：未删除 |
| labels | String | 任务自定义标识。 |
| created | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| updated | String | 更新时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| scenariofieldconfigId | String | 任务类型ID。 |
| customfields | Array of String | 自定义字段ID。 |
| note | String | 备注。 |
| startDate | String | 任务开始时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| dueDate | String | 任务截止时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| priority | Long | 任务优先级。 |
| taskflowstatusId | String | 任务状态ID。 |
| isDone | Boolean | 任务是否已完成。   - **true**：已完成 - **false**：未完成 |
| isArchived | Boolean | 是否归档，即是否移动到回收站。   - **true**：已归档 - **false**：未归档 |
| visible | String | 任务的可见性规则。   - **involves**：仅任务参与者可见 - **members**：项目成员可见 |
| tagIds | String | 标签ID列表。 |
| stageId | String | 任务列表ID。 |
| sprintId | String | 任务迭代ID，项目应用中开启**迭代**应用，可添加任务的迭代信息。 |
| accomplished | String | 任务完成时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| storyPoint | Integer | 任务估算的工作量。 |
| progress | Integer | 任务进度。 |
| ancestorIds | Array of String | 父任务ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 35,
  "nextToken" : "f279e81xxxxx",
  "result" : [ {
    "taskId" : "62c25e3bbaxxx",
    "content" : "标题2",
    "involveMembers" : [ "62c25e3bba7xxxxxx" ],
    "projectId" : "62c25e3bbaxxxxx",
    "executorId" : "62cxxxxxxx",
    "creatorId" : "62c25e3bba7ce40xxx",
    "isDeleted" : true,
    "labels" : "标签1",
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z",
    "scenariofieldconfigId" : "62c25e3bbxx0xxx",
    "customfields" : [ "62c25e3bbxx0xxx" ],
    "note" : "备注",
    "startDate" : "2022-07-04T03:29:34.770Z",
    "dueDate" : "2022-07-04T03:29:34.770Z",
    "priority" : 0,
    "taskflowstatusId" : "62c25e3bbxx0xxx",
    "isDone" : true,
    "isArchived" : true,
    "visible" : "member",
    "tagIds" : "62c25e3bbxx0xxx",
    "stageId" : "62c25e3bbxx0xxx",
    "sprintId" : "62c25e3bbxx0xxx",
    "accomplished" : "2022-07-04T03:29:34.770Z",
    "storyPoint" : 2,
    "progress" : 0,
    "ancestorIds" : [ "62c25e3bbxx0xxx" ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在 |
| 500 | server.error | system error | 系统内部服务错误 |
