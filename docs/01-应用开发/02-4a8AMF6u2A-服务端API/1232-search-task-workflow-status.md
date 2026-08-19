---
title: "搜索任务工作流状态"
source_url: "https://open.dingtalk.com/document/development/search-task-workflow-status"
namespace: "development"
slug: "search-task-workflow-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 搜索任务工作流状态"
doc_id: "oUJsLLP2uK"
updated_at: "2025-10-09 18:06:46"
---

> Source: https://open.dingtalk.com/document/development/search-task-workflow-status
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务 > 项目任务 > 搜索任务工作流状态
> Updated: 2025-10-09 18:06:46

# 搜索任务工作流状态

调用本接口，搜索任务工作流状态。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/taskflowStatuses/search |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Read.All-项目应用项目读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |
| projectId | String | 是 | 项目ID，可通过调用[根据项目模板创建项目](1217-create-a-project-from-a-project-template.md)接口，获取返回参数`id`字段值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| query | String | 否 | 模糊查询工作流状态名字。 |
| maxResults | Integer | 否 | 每页返回最大数量。      默认10，最大300。 |
| nextToken | String | 否 | 分页标，从上一次请求结果中获取。 |
| tfIds | String | 否 | 工作流ID集合。      多个ID用英文逗号隔开。 |
| tfsIds | String | 否 | 工作流状态ID集合。      多个ID用英文逗号隔开。 |

### 请求示例

HTTP

```
GET /v1.0/project/users/0517xxx/projects/62c25e3b376ecxxxxxxx/taskflowStatuses/search?query=未开始&maxResults=10&nextToken=f279e812xxxxxx&tfIds=60a2187eb72xxxxxxx,60a2187eb72xxxxxxx&tfsIds=60a2187eb72xxxxxxx,60a2187eb72xxxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:04b1f9607e3a37b1ab*****1024
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
        com.aliyun.dingtalkproject_1_0.models.SearchTaskflowStatusHeaders searchTaskflowStatusHeaders = new com.aliyun.dingtalkproject_1_0.models.SearchTaskflowStatusHeaders();
        searchTaskflowStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.SearchTaskflowStatusRequest searchTaskflowStatusRequest = new com.aliyun.dingtalkproject_1_0.models.SearchTaskflowStatusRequest()
                .setQuery("未开始")
                .setMaxResults(10)
                .setNextToken("f279e812xxxxxx")
                .setTfIds("60a2187eb72xxxxxxx,60a2187eb72xxxxxxx")
                .setTfsIds("60a2187eb72xxxxxxx,60a2187eb72xxxxxxx");
        try {
            client.searchTaskflowStatusWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", searchTaskflowStatusRequest, searchTaskflowStatusHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        search_taskflow_status_headers = dingtalkproject__1__0_models.SearchTaskflowStatusHeaders()
        search_taskflow_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_taskflow_status_request = dingtalkproject__1__0_models.SearchTaskflowStatusRequest(
            query='未开始',
            max_results=10,
            next_token='f279e812xxxxxx',
            tf_ids='60a2187eb72xxxxxxx,60a2187eb72xxxxxxx',
            tfs_ids='60a2187eb72xxxxxxx,60a2187eb72xxxxxxx'
        )
        try:
            client.search_taskflow_status_with_options('0517xxx', '62c25e3b376ecxxxxxxx', search_taskflow_status_request, search_taskflow_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_taskflow_status_headers = dingtalkproject__1__0_models.SearchTaskflowStatusHeaders()
        search_taskflow_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_taskflow_status_request = dingtalkproject__1__0_models.SearchTaskflowStatusRequest(
            query='未开始',
            max_results=10,
            next_token='f279e812xxxxxx',
            tf_ids='60a2187eb72xxxxxxx,60a2187eb72xxxxxxx',
            tfs_ids='60a2187eb72xxxxxxx,60a2187eb72xxxxxxx'
        )
        try:
            await client.search_taskflow_status_with_options_async('0517xxx', '62c25e3b376ecxxxxxxx', search_taskflow_status_request, search_taskflow_status_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\SearchTaskflowStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\SearchTaskflowStatusRequest;
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
        $searchTaskflowStatusHeaders = new SearchTaskflowStatusHeaders([]);
        $searchTaskflowStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $searchTaskflowStatusRequest = new SearchTaskflowStatusRequest([
            "query" => "未开始",
            "maxResults" => 10,
            "nextToken" => "f279e812xxxxxx",
            "tfIds" => "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
            "tfsIds" => "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx"
        ]);
        try {
            $client->searchTaskflowStatusWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", $searchTaskflowStatusRequest, $searchTaskflowStatusHeaders, new RuntimeOptions([]));
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

  searchTaskflowStatusHeaders := &dingtalkproject_1_0.SearchTaskflowStatusHeaders{}
  searchTaskflowStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  searchTaskflowStatusRequest := &dingtalkproject_1_0.SearchTaskflowStatusRequest{
    Query: tea.String("未开始"),
    MaxResults: tea.Int32(10),
    NextToken: tea.String("f279e812xxxxxx"),
    TfIds: tea.String("60a2187eb72xxxxxxx,60a2187eb72xxxxxxx"),
    TfsIds: tea.String("60a2187eb72xxxxxxx,60a2187eb72xxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SearchTaskflowStatusWithOptions(tea.String("0517xxx"), tea.String("62c25e3b376ecxxxxxxx"), searchTaskflowStatusRequest, searchTaskflowStatusHeaders, &util.RuntimeOptions{})
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
    let searchTaskflowStatusHeaders = new $dingtalkproject_1_0.SearchTaskflowStatusHeaders({ });
    searchTaskflowStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let searchTaskflowStatusRequest = new $dingtalkproject_1_0.SearchTaskflowStatusRequest({
      query: "未开始",
      maxResults: 10,
      nextToken: "f279e812xxxxxx",
      tfIds: "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
      tfsIds: "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
    });
    try {
      await client.searchTaskflowStatusWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", searchTaskflowStatusRequest, searchTaskflowStatusHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskflowStatusHeaders searchTaskflowStatusHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskflowStatusHeaders();
            searchTaskflowStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskflowStatusRequest searchTaskflowStatusRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.SearchTaskflowStatusRequest
            {
                Query = "未开始",
                MaxResults = 10,
                NextToken = "f279e812xxxxxx",
                TfIds = "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
                TfsIds = "60a2187eb72xxxxxxx,60a2187eb72xxxxxxx",
            };
            try
            {
                client.SearchTaskflowStatusWithOptions("0517xxx", "62c25e3b376ecxxxxxxx", searchTaskflowStatusRequest, searchTaskflowStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 工作流状态列表。 |
| taskflowStatusId | String | 任务工作流状态ID。 |
| name | String | 工作流状态名字。 |
| pos | Integer | 工作流状态位置。 |
| taskflowId | String | 工作流状态ID。 |
| rejectStatusIds | Array of String | 拒绝的工作流状态Id。 |
| kind | String | 任务工作流状态类型：   - **start**: 开始 - **end**: 结束 - **unset**: 未设置 |
| creatorId | String | 创建者ID。 |
| isDeleted | Boolean | 是否已删除。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| isTaskflowstatusruleexector | Boolean | 是否特定任务角色才能流转该工作流状态：   - **true**：是 - **false**：否 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "id" : "60a2187eb72xxxxxxx",
    "name" : "未开始",
    "pos" : 0,
    "taskflowId" : "60a2187eb72xxxxxxx",
    "rejectStatusIds" : [ "60a2187eb72xxxxxxx" ],
    "kind" : "start",
    "creatorId" : "601fdeb17f86xxxxxxxx",
    "isDeleted" : false,
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z",
    "isTaskflowstatusruleexector" : false
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
