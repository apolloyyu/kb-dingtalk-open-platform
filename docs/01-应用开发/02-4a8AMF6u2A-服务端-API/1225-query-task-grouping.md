---
title: "查询任务分组"
source_url: "https://open.dingtalk.com/document/development/query-task-grouping"
namespace: "development"
slug: "query-task-grouping"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 查询任务分组"
doc_id: "hLaA3cmg8i"
updated_at: "2026-06-03 09:26:04"
---

> Source: https://open.dingtalk.com/document/development/query-task-grouping
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 任务 > 项目任务 > 查询任务分组
> Updated: 2026-06-03 09:26:04

# 查询任务分组

调用本接口查询任务分组。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/taskLists/search |
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
| projectId | String | 是 | 项目ID，可通过调用[查询项目](https://open.dingtalk.com/document/isvapp/query-enterprise-all-projects)接口，获取返回参数`projectId`字段。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| query | String | 否 | 模糊任务分组名字。 |
| maxResults | Integer | 否 | 每页返回最大数量。  **[!NOTE]**    默认10，最大300。 |
| nextToken | String | 否 | 分页标，从上一次请求结果中获取。 |
| taskListIds | String | 否 | 任务分组ID集合，多个使用英文逗号隔开，可调用[查询项目](1207-query-enterprise-all-projects.md)接口，获取返回参数`taskListId`字段。 |

### 请求示例

HTTP

```
POST /v1.0/project/users/0517xxx/projects/62c25e3b376ecxxxxxxx/taskLists/search?query=自定义分组1&maxResults=10&nextToken=f279e812xxxxxx&taskListIds=60a2187eb72xxxxxxx,60a2187eb72xxxxxxx HTTP/1.1
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
        com.aliyun.dingtalkproject_1_0.models.SearchTaskListHeaders searchTaskListHeaders = new com.aliyun.dingtalkproject_1_0.models.SearchTaskListHeaders();
        searchTaskListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.SearchTaskListRequest searchTaskListRequest = new com.aliyun.dingtalkproject_1_0.models.SearchTaskListRequest()
                .setQuery("自定义分组1")
                .setMaxResults(10)
                .setNextToken("f279e812xxxxxx")
                .setTaskListIds("60a2187eb72xxxxxxx,60a2187eb72xxxxxxx");
        try {
            client.searchTaskListWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", searchTaskListRequest, searchTaskListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        search_task_list_headers = dingtalkproject__1__0_models.SearchTaskListHeaders()
        search_task_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_task_list_request = dingtalkproject__1__0_models.SearchTaskListRequest(
            query='自定义分组1',
            max_results=10,
            next_token='f279e812xxxxxx',
            task_list_ids='60a2187eb72xxxxxxx,60a2187eb72xxxxxxx'
        )
        try:
            client.search_task_list_with_options('0517xxx', '62c25e3b376ecxxxxxxx', search_task_list_request, search_task_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_task_list_headers = dingtalkproject__1__0_models.SearchTaskListHeaders()
        search_task_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_task_list_request = dingtalkproject__1__0_models.SearchTaskListRequest(
            query='自定义分组1',
            max_results=10,
            next_token='f279e812xxxxxx',
            task_list_ids='60a2187eb72xxxxxxx,60a2187eb72xxxxxxx'
        )
        try:
            await client.search_task_list_with_options_async('0517xxx', '62c25e3b376ecxxxxxxx', search_task_list_request, search_task_list_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\SearchTaskListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\SearchTaskListRequest;
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
        $searchTaskListHeaders = new SearchTaskListHeaders([]);
        $searchTaskListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $searchTaskListRequest = new SearchTaskListRequest([
            "query" => "自定义分组1",
            "maxResults" => 10,
            "nextToken" => "f279e812xxxxxx",
            "taskListIds" => "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx"
        ]);
        try {
            $client->searchTaskListWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", $searchTaskListRequest, $searchTaskListHeaders, new RuntimeOptions([]));
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

  searchTaskListHeaders := &dingtalkproject_1_0.SearchTaskListHeaders{}
  searchTaskListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  searchTaskListRequest := &dingtalkproject_1_0.SearchTaskListRequest{
    Query: tea.String("自定义分组1"),
    MaxResults: tea.Int32(10),
    NextToken: tea.String("f279e812xxxxxx"),
    TaskListIds: tea.String("60a2187eb72xxxxxxx,60a2187eb72xxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SearchTaskListWithOptions(tea.String("0517xxx"), tea.String("62c25e3b376ecxxxxxxx"), searchTaskListRequest, searchTaskListHeaders, &util.RuntimeOptions{})
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
    let searchTaskListHeaders = new $dingtalkproject_1_0.SearchTaskListHeaders({ });
    searchTaskListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let searchTaskListRequest = new $dingtalkproject_1_0.SearchTaskListRequest({
      query: "自定义分组1",
      maxResults: 10,
      nextToken: "f279e812xxxxxx",
      taskListIds: "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
    });
    try {
      await client.searchTaskListWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", searchTaskListRequest, searchTaskListHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskListHeaders searchTaskListHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskListHeaders();
            searchTaskListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskListRequest searchTaskListRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskListRequest
            {
                Query = "自定义分组1",
                MaxResults = 10,
                NextToken = "f279e812xxxxxx",
                TaskListIds = "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
            };
            try
            {
                client.SearchTaskListWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", searchTaskListRequest, searchTaskListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 任务分组列表。 |
| taskListId | String | 任务分组ID。 |
| title | String | 任务分组名称。 |
| description | String | 任务分组名称。 |
| projectId | String | 项目ID。 |
| creatorId | String | 创建者用户ID。 |
| created | String | 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| updated | String | 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| nextToken | String | 分页标，供分页使用，下一页token。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "taskListId" : "60a2187eb72xxxxxxx",
    "title" : "自定义分组1",
    "description" : "描述...",
    "projectId" : "62c25e3b376ecxxxxxxx",
    "creatorId" : "0715153011125xxxx",
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z"
  } ],
  "nextToken" : "f279e812-e431-428d-846d-cxxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
