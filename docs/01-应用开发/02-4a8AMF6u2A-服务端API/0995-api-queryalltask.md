---
title: "查询任务详情"
source_url: "https://open.dingtalk.com/document/development/api-queryalltask"
namespace: "development"
slug: "api-queryalltask"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉快办 > 查询任务详情"
doc_id: "2AbmrsOgVb"
updated_at: "2026-06-02 19:46:15"
---

> Source: https://open.dingtalk.com/document/development/api-queryalltask
> Path: 应用开发 / 服务端API / 钉钉快办 > 查询任务详情
> Updated: 2026-06-02 19:46:15

# 查询任务详情

调用本接口，根据任务id查询自由任务或项目任务详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/tasks/query |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-TeamSphere.Project.ReadWrite-钉钉快办管理权限 |

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
| taskId | String | 是 | 任务ID集合,使用逗号分隔。 |

### 请求示例

HTTP

```
GET /v1.0/teamSphere/users/0517xxx/tasks/query?taskId=67497ca091df9843288**** HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1234
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
    public static com.aliyun.dingtalkteam_sphere_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkteam_sphere_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkteam_sphere_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkteam_sphere_1_0.models.QueryAllTaskHeaders queryAllTaskHeaders = new com.aliyun.dingtalkteam_sphere_1_0.models.QueryAllTaskHeaders();
        queryAllTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkteam_sphere_1_0.models.QueryAllTaskRequest queryAllTaskRequest = new com.aliyun.dingtalkteam_sphere_1_0.models.QueryAllTaskRequest()
                .setTaskId("67497ca091df9843288****");
        try {
            client.queryAllTaskWithOptions("0517xxx", queryAllTaskRequest, queryAllTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_all_task_headers = dingtalkteam_sphere__1__0_models.QueryAllTaskHeaders()
        query_all_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_all_task_request = dingtalkteam_sphere__1__0_models.QueryAllTaskRequest(
            task_id='67497ca091df9843288****'
        )
        try:
            client.query_all_task_with_options('0517xxx', query_all_task_request, query_all_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_all_task_headers = dingtalkteam_sphere__1__0_models.QueryAllTaskHeaders()
        query_all_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_all_task_request = dingtalkteam_sphere__1__0_models.QueryAllTaskRequest(
            task_id='67497ca091df9843288****'
        )
        try:
            await client.query_all_task_with_options_async('0517xxx', query_all_task_request, query_all_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\QueryAllTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\QueryAllTaskRequest;
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
        $queryAllTaskHeaders = new QueryAllTaskHeaders([]);
        $queryAllTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryAllTaskRequest = new QueryAllTaskRequest([
            "taskId" => "67497ca091df9843288****"
        ]);
        try {
            $client->queryAllTaskWithOptions("0517xxx", $queryAllTaskRequest, $queryAllTaskHeaders, new RuntimeOptions([]));
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

  queryAllTaskHeaders := &dingtalkteamsphere_1_0.QueryAllTaskHeaders{}
  queryAllTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryAllTaskRequest := &dingtalkteamsphere_1_0.QueryAllTaskRequest{
    TaskId: tea.String("67497ca091df9843288****"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryAllTaskWithOptions(tea.String("0517xxx"), queryAllTaskRequest, queryAllTaskHeaders, &util.RuntimeOptions{})
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
    let queryAllTaskHeaders = new dingtalkteamSphere_1_0.QueryAllTaskHeaders({ });
    queryAllTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryAllTaskRequest = new dingtalkteamSphere_1_0.QueryAllTaskRequest({
      taskId: '67497ca091df9843288****',
    });
    try {
      await client.queryAllTaskWithOptions('0517xxx', queryAllTaskRequest, queryAllTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.QueryAllTaskHeaders queryAllTaskHeaders = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.QueryAllTaskHeaders();
            queryAllTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.QueryAllTaskRequest queryAllTaskRequest = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.QueryAllTaskRequest
            {
                TaskId = "67497ca091df9843288****",
            };
            try
            {
                client.QueryAllTaskWithOptions("0517xxx", queryAllTaskRequest, queryAllTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 任务ID。 |
| taskId | String | 任务ID。 |
| content | String | 任务标题。 |
| note | String | 任务备注。 |
| projectId | String | 项目ID。 |
| ancestorIds | Array of String | 祖先任务ID。 |
| parentTaskId | String | 父任务ID。 |
| tfsId | String | 任务状态ID。 |
| tasklistId | String | 任务分组ID。 |
| stageId | String | 任务列ID。 |
| tagIds | Array of String | 标签ID。 |
| creatorId | String | 创建人ID。 |
| executorId | String | 执行人ID。 |
| involveMembers | Array of String | 参与者ID。 |
| priority | Integer | 任务优先级。 |
| isDone | Boolean | 是否任务已完成。 |
| isArchived | Boolean | 是否任务放入回收站。 |
| visible | String | 任务隐私性，'involves'表达仅参与者可见; 'members'表达项目成员可见。 |
| uniqueId | String | 任务数字ID。 |
| startDate | String | 任务开始时间(UTC)。 |
| dueDate | String | 任务截止时间(UTC)。 |
| accomplishTime | String | 任务完成时间(UTC)。 |
| created | String | 创建时间(UTC)。 |
| updated | String | 更新时间(UTC)。 |
| sfcId | String | 任务类型ID。 |
| customfields | Array | 自定义字段值集合。 |
| cfId | String | 自定义字段ID。 |
| type | String | 自定义字段类型。 |
| value | Array | 字段值集合。 |
| id | String | 字段值ID。 |
| title | String | 字段值内容。 |
| metaString | String | 字段值元属性。 |
| requestId | String | 请求 ID，请求异常时可提供此 ID，进行问题排查。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "id" : "1234",
    "taskId" : "1234",
    "content" : "test",
    "note" : "test",
    "projectId" : "1234",
    "ancestorIds" : [ "1234" ],
    "parentTaskId" : "1234",
    "tfsId" : "1234",
    "tasklistId" : "1234",
    "stageId" : "1234",
    "tagIds" : [ "1234" ],
    "creatorId" : "1234",
    "executorId" : "1234",
    "involveMembers" : [ "1234" ],
    "priority" : 0,
    "isDone" : true,
    "isArchived" : true,
    "visible" : "invovles",
    "uniqueId" : "1234",
    "startDate" : "2022-07-04T03:29:34.770Z",
    "dueDate" : "2022-07-04T03:29:34.770Z",
    "accomplishTime" : "2022-07-04T03:29:34.770Z",
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z",
    "sfcId" : "1234",
    "customfields" : [ {
      "cfId" : "1234",
      "type" : "string",
      "value" : [ {
        "id" : "1234",
        "title" : "标题字段",
        "metaString" : "string"
      } ]
    } ]
  } ],
  "requestId" : "1234"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在快办中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
