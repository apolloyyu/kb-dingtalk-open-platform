---
title: "查询企业下用户待办列表"
source_url: "https://open.dingtalk.com/document/development/query-the-to-do-list-of-enterprise-users"
namespace: "development"
slug: "query-the-to-do-list-of-enterprise-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "待办任务 > 查询企业下用户待办列表"
doc_id: "UqK09TsE5H"
updated_at: "2026-06-04 19:09:52"
---

> Source: https://open.dingtalk.com/document/development/query-the-to-do-list-of-enterprise-users
> Path: 应用开发 / 服务端API / 待办任务 > 查询企业下用户待办列表
> Updated: 2026-06-04 19:09:52

# 查询企业下用户待办列表

调用本接口，获取该授权企业下某用户的待办列表。

## **接口调用说明**

- 接口最多可以获取到180天内已完成状态的待办任务；未完成状态的待办任务无此限制。
- 必须通过[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)接口发起待办且detailUrl参数不为空，则为企业待办，可通过本接口查询。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/org/tasks/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Todo.Todo.Read-待办应用中待办读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标。    如果一个查询条件一次无法全部返回结果，会返回分页token，下次查询带上该token后会返回后续数据，直到分页token为null表示数据已经全部查询完毕。 |
| isDone | Boolean | 否 | 待办完成状态。   - **true**：已完成 - **false**：未完成 |
| roleTypes | Array of Array | 否 | 查询目标用户角色类型。   - **executor**：执行人 - **creator**：创建人 - **participant**：参与人   可以同时传多个值。外层list表示或的关系，内层list表示与的关系。例如：[["executor"], ["creator"],["participant"]] 或 [["executor", "creator"]]。 |
| todoType | String | 否 | 待办的业务类型，目前支持两种：    不传该入参时，默认查询的是所有业务类型。   - **TODO**：待办业务类型 - **READ**：待阅业务类型 |

### 请求示例

HTTP

```
POST /v1.0/todo/users/PUoiinWIpa2yH2ymhiiGiP6g/org/tasks/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b3ba046c118a3445b111db282824c0b4
Content-Type:application/json

{
  "nextToken" : "0",
  "isDone" : true
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalktodo_1_0.*;
import com.aliyun.dingtalktodo_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalktodo_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktodo_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalktodo_1_0.Client client = Sample.createClient();
        QueryOrgTodoTasksHeaders queryOrgTodoTasksHeaders = new QueryOrgTodoTasksHeaders();
        queryOrgTodoTasksHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryOrgTodoTasksRequest queryOrgTodoTasksRequest = new QueryOrgTodoTasksRequest()
                .setNextToken("0")
                .setIsDone(true);
        try {
            client.queryOrgTodoTasksWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", queryOrgTodoTasksRequest, queryOrgTodoTasksHeaders, new RuntimeOptions());
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
        query_org_todo_tasks_headers = dingtalktodo__1__0_models.QueryOrgTodoTasksHeaders()
        query_org_todo_tasks_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_org_todo_tasks_request = dingtalktodo__1__0_models.QueryOrgTodoTasksRequest(
            next_token='0',
            is_done=True
        )
        try:
            client.query_org_todo_tasks_with_options('PUoiinWIpa2yH2ymhiiGiP6g', query_org_todo_tasks_request, query_org_todo_tasks_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_org_todo_tasks_headers = dingtalktodo__1__0_models.QueryOrgTodoTasksHeaders()
        query_org_todo_tasks_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_org_todo_tasks_request = dingtalktodo__1__0_models.QueryOrgTodoTasksRequest(
            next_token='0',
            is_done=True
        )
        try:
            await client.query_org_todo_tasks_with_options_async('PUoiinWIpa2yH2ymhiiGiP6g', query_org_todo_tasks_request, query_org_todo_tasks_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\QueryOrgTodoTasksHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\QueryOrgTodoTasksRequest;
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
        $queryOrgTodoTasksHeaders = new QueryOrgTodoTasksHeaders([]);
        $queryOrgTodoTasksHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryOrgTodoTasksRequest = new QueryOrgTodoTasksRequest([
            "nextToken" => "0",
            "isDone" => true
        ]);
        try {
            $client->queryOrgTodoTasksWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", $queryOrgTodoTasksRequest, $queryOrgTodoTasksHeaders, new RuntimeOptions([]));
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
  dingtalktodo_1_0  "github.com/alibabacloud-go/dingtalk/todo_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  queryOrgTodoTasksHeaders := &dingtalktodo_1_0.QueryOrgTodoTasksHeaders{}
  queryOrgTodoTasksHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryOrgTodoTasksRequest := &dingtalktodo_1_0.QueryOrgTodoTasksRequest{
    NextToken: tea.String("0"),
    IsDone: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryOrgTodoTasksWithOptions(tea.String("PUoiinWIpa2yH2ymhiiGiP6g"), queryOrgTodoTasksRequest, queryOrgTodoTasksHeaders, &util.RuntimeOptions{})
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
    let queryOrgTodoTasksHeaders = new $dingtalktodo_1_0.QueryOrgTodoTasksHeaders({ });
    queryOrgTodoTasksHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryOrgTodoTasksRequest = new $dingtalktodo_1_0.QueryOrgTodoTasksRequest({
      nextToken: "0",
      isDone: true,
    });
    try {
      await client.queryOrgTodoTasksWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", queryOrgTodoTasksRequest, queryOrgTodoTasksHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.QueryOrgTodoTasksHeaders queryOrgTodoTasksHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.QueryOrgTodoTasksHeaders();
            queryOrgTodoTasksHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.QueryOrgTodoTasksRequest queryOrgTodoTasksRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.QueryOrgTodoTasksRequest
            {
                NextToken = "0",
                IsDone = true,
            };
            try
            {
                client.QueryOrgTodoTasksWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", queryOrgTodoTasksRequest, queryOrgTodoTasksHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalktodo__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalktodo_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalktodo_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::Client> client = make_shared<Alibabacloud_Dingtalktodo_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::QueryOrgTodoTasksHeaders> queryOrgTodoTasksHeaders = make_shared<Alibabacloud_Dingtalktodo_1_0::QueryOrgTodoTasksHeaders>();
  queryOrgTodoTasksHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::QueryOrgTodoTasksRequest> queryOrgTodoTasksRequest = make_shared<Alibabacloud_Dingtalktodo_1_0::QueryOrgTodoTasksRequest>(map<string, boost::any>({
    {"nextToken", boost::any(string("0"))},
    {"isDone", boost::any(true)}
  }));
  try {
    client->queryOrgTodoTasksWithOptions(make_shared<string>("PUoiinWIpa2yH2ymhiiGiP6g"), queryOrgTodoTasksRequest, queryOrgTodoTasksHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| nextToken | String | 下一次请求的token。 |
| todoCards | Array | 待办卡片列表。 |
| taskId | String | 待办ID。 |
| subject | String | 待办标题。 |
| dueTime | Long | 待办截止时间。 |
| detailUrl | Object | 详情页链接。 |
| appUrl | String | 移动端url地址。 |
| pcUrl | String | pc端url地址。 |
| priority | Integer | 优先级 |
| createdTime | Long | 创建时间。 |
| modifiedTime | Long | 更新时间。 |
| creatorId | String | 创建者ID。 |
| sourceId | String | 来源ID。 |
| bizTag | String | 所属应用。 |
| isDone | Boolean | 待办完成状态。 |
| todoType | String | 待办的业务类型，目前支持两种：   - **TODO**：待办业务类型 - **READ**：待阅业务类型 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "15",
  "todoCards" : [ {
    "taskId" : "taskOPJpwtwPVNGIFKURjrzd",
    "subject" : "接入钉钉待办",
    "dueTime" : 1617675000000,
    "detailUrl" : {
      "appUrl" : "https://www.dingtalk.com",
      "pcUrl" : "https://www.dingtalk.com"
    },
    "priority" : 10,
    "createdTime" : 1617675000000,
    "modifiedTime" : 1617675000000,
    "creatorId" : "PUoiinWIpa2yH2ymhiiGiP6g",
    "sourceId" : "isv_dingtalkTodo1",
    "bizTag" : "isv_dingtalkTodo",
    "isDone" : true
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.orgTaskQuery.paramError | todo.orgTaskQuery.paramError | 查询企业待办列表系统参数错误 |
| 400 | todo.orgTaskQuery.paramError | nextToken is invalid | 分页游标参数非法 |
| 500 | todo.orgTaskQuery.systemError | todo.orgTaskQuery.systemError | 查询企业待办列表系统内部异常 |
