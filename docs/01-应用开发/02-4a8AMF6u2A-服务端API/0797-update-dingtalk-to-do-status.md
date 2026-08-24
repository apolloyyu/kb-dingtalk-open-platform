---
title: "更新钉钉待办执行者状态"
source_url: "https://open.dingtalk.com/document/development/update-dingtalk-to-do-status"
namespace: "development"
slug: "update-dingtalk-to-do-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "待办任务 > 更新钉钉待办执行者状态"
doc_id: "jrOWc9Mf63"
updated_at: "2026-06-04 19:09:52"
---

> Source: https://open.dingtalk.com/document/development/update-dingtalk-to-do-status
> Path: 应用开发 / 服务端API / 待办任务 > 更新钉钉待办执行者状态
> Updated: 2026-06-04 19:09:52

# 更新钉钉待办执行者状态

调用本接口，当待办存在多个执行者时，可更新部分执行者的完成状态。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks/{taskId}/executorStatus |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Todo.Todo.Write-待办应用中待办写权限,待办应用中待办读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 当前访问的资源所归属用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| taskId | String | 是 | 待办ID。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 否 | 当前操作者的用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| executorStatusList | Array | 否 | 执行者状态列表，id需传用户的unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值，最大数量1000。 |
| id | String | 否 | 执行者的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| isDone | Boolean | 否 | 执行者完成状态。 |

### 请求示例

HTTP

```
PUT /v1.0/todo/users/PUoiinWIpa2yH2ymhiiGiP6g/tasks/OPJpwtwPVNGIFKURjrzd/executorStatus?operatorId=PUoiinWIpa2yH2ymhiiGiP6g HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b3ba046c118a3445b111db282824c0b4
Content-Type:application/json

{
  "executorStatusList" : [ {
    "id" : "PUoiinWIpa2yH2ymhiiGiP6g",
    "isDone" : true
  } ]
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
        UpdateTodoTaskExecutorStatusHeaders updateTodoTaskExecutorStatusHeaders = new UpdateTodoTaskExecutorStatusHeaders();
        updateTodoTaskExecutorStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateTodoTaskExecutorStatusRequest.UpdateTodoTaskExecutorStatusRequestExecutorStatusList executorStatusList0 = new UpdateTodoTaskExecutorStatusRequest.UpdateTodoTaskExecutorStatusRequestExecutorStatusList()
                .setId("PUoiinWIpa2yH2ymhiiGiP6g")
                .setIsDone(true);
        UpdateTodoTaskExecutorStatusRequest updateTodoTaskExecutorStatusRequest = new UpdateTodoTaskExecutorStatusRequest()
                .setExecutorStatusList(java.util.Arrays.asList(
                    executorStatusList0
                ));
        try {
            client.updateTodoTaskExecutorStatusWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", updateTodoTaskExecutorStatusRequest, updateTodoTaskExecutorStatusHeaders, new RuntimeOptions());
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
        update_todo_task_executor_status_headers = dingtalktodo__1__0_models.UpdateTodoTaskExecutorStatusHeaders()
        update_todo_task_executor_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        executor_status_list_0 = dingtalktodo__1__0_models.UpdateTodoTaskExecutorStatusRequestExecutorStatusList(
            id='PUoiinWIpa2yH2ymhiiGiP6g',
            is_done=True
        )
        update_todo_task_executor_status_request = dingtalktodo__1__0_models.UpdateTodoTaskExecutorStatusRequest(
            executor_status_list=[
                executor_status_list_0
            ]
        )
        try:
            client.update_todo_task_executor_status_with_options('PUoiinWIpa2yH2ymhiiGiP6g', 'OPJpwtwPVNGIFKURjrzd', update_todo_task_executor_status_request, update_todo_task_executor_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_todo_task_executor_status_headers = dingtalktodo__1__0_models.UpdateTodoTaskExecutorStatusHeaders()
        update_todo_task_executor_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        executor_status_list_0 = dingtalktodo__1__0_models.UpdateTodoTaskExecutorStatusRequestExecutorStatusList(
            id='PUoiinWIpa2yH2ymhiiGiP6g',
            is_done=True
        )
        update_todo_task_executor_status_request = dingtalktodo__1__0_models.UpdateTodoTaskExecutorStatusRequest(
            executor_status_list=[
                executor_status_list_0
            ]
        )
        try:
            await client.update_todo_task_executor_status_with_options_async('PUoiinWIpa2yH2ymhiiGiP6g', 'OPJpwtwPVNGIFKURjrzd', update_todo_task_executor_status_request, update_todo_task_executor_status_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTaskExecutorStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTaskExecutorStatusRequest\executorStatusList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTaskExecutorStatusRequest;
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
        $updateTodoTaskExecutorStatusHeaders = new UpdateTodoTaskExecutorStatusHeaders([]);
        $updateTodoTaskExecutorStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $executorStatusList0 = new executorStatusList([
            "id" => "PUoiinWIpa2yH2ymhiiGiP6g",
            "isDone" => true
        ]);
        $updateTodoTaskExecutorStatusRequest = new UpdateTodoTaskExecutorStatusRequest([
            "executorStatusList" => [
                $executorStatusList0
            ]
        ]);
        try {
            $client->updateTodoTaskExecutorStatusWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", $updateTodoTaskExecutorStatusRequest, $updateTodoTaskExecutorStatusHeaders, new RuntimeOptions([]));
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
  dingtalktodo_1_0  ""github.com/alibabacloud-go/dingtalk/todo_1_0"
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

  updateTodoTaskExecutorStatusHeaders := &dingtalktodo_1_0.UpdateTodoTaskExecutorStatusHeaders{}
  updateTodoTaskExecutorStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  executorStatusList0 := &dingtalktodo_1_0.UpdateTodoTaskExecutorStatusRequestExecutorStatusList{
    Id: tea.String("PUoiinWIpa2yH2ymhiiGiP6g"),
    IsDone: tea.Bool(true),
  }
  updateTodoTaskExecutorStatusRequest := &dingtalktodo_1_0.UpdateTodoTaskExecutorStatusRequest{
    ExecutorStatusList: []*dingtalktodo_1_0.UpdateTodoTaskExecutorStatusRequestExecutorStatusList{executorStatusList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateTodoTaskExecutorStatusWithOptions(tea.String("PUoiinWIpa2yH2ymhiiGiP6g"), tea.String("OPJpwtwPVNGIFKURjrzd"), updateTodoTaskExecutorStatusRequest, updateTodoTaskExecutorStatusHeaders, &util.RuntimeOptions{})
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
import dingtalktodo_1_0, * as $dingtalktodo_1_0 from '"@alicloud/dingtalk/todo_1_0';
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
    let updateTodoTaskExecutorStatusHeaders = new $dingtalktodo_1_0.UpdateTodoTaskExecutorStatusHeaders({ });
    updateTodoTaskExecutorStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let executorStatusList0 = new $dingtalktodo_1_0.UpdateTodoTaskExecutorStatusRequestExecutorStatusList({
      id: "PUoiinWIpa2yH2ymhiiGiP6g",
      isDone: true,
    });
    let updateTodoTaskExecutorStatusRequest = new $dingtalktodo_1_0.UpdateTodoTaskExecutorStatusRequest({
      executorStatusList: [
        executorStatusList0
      ],
    });
    try {
      await client.updateTodoTaskExecutorStatusWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", updateTodoTaskExecutorStatusRequest, updateTodoTaskExecutorStatusHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusHeaders updateTodoTaskExecutorStatusHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusHeaders();
            updateTodoTaskExecutorStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusRequest.UpdateTodoTaskExecutorStatusRequestExecutorStatusList executorStatusList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusRequest.UpdateTodoTaskExecutorStatusRequestExecutorStatusList
            {
                Id = "PUoiinWIpa2yH2ymhiiGiP6g",
                IsDone = true,
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusRequest updateTodoTaskExecutorStatusRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusRequest
            {
                ExecutorStatusList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTaskExecutorStatusRequest.UpdateTodoTaskExecutorStatusRequestExecutorStatusList>
                {
                    executorStatusList0
                },
            };
            try
            {
                client.UpdateTodoTaskExecutorStatusWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", updateTodoTaskExecutorStatusRequest, updateTodoTaskExecutorStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
#include <vector>

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
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusHeaders> updateTodoTaskExecutorStatusHeaders = make_shared<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusHeaders>();
  updateTodoTaskExecutorStatusHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusRequestExecutorStatusList> executorStatusList0 = make_shared<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusRequestExecutorStatusList>(map<string, boost::any>({
    {"id", boost::any(string("PUoiinWIpa2yH2ymhiiGiP6g"))},
    {"isDone", boost::any(true)}
  }));
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusRequest> updateTodoTaskExecutorStatusRequest = make_shared<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusRequest>(map<string, boost::any>({
    {"executorStatusList", boost::any(vector<Alibabacloud_Dingtalktodo_1_0::UpdateTodoTaskExecutorStatusRequestExecutorStatusList>({
      executorStatusList0
    }))}
  }));
  try {
    client->updateTodoTaskExecutorStatusWithOptions(make_shared<string>("PUoiinWIpa2yH2ymhiiGiP6g"), make_shared<string>("OPJpwtwPVNGIFKURjrzd"), updateTodoTaskExecutorStatusRequest, updateTodoTaskExecutorStatusHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Boolean | 更新结果。true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.taskExecutorStatusUpdate.paramError | todo.taskExecutorStatusUpdate.paramError | 更新待办执行者状态参数异常 |
| 400 | todo.taskExecutorStatusUpdate.paramError | task not exist | 待办任务不存在 |
| 400 | todo.taskExecutorStatusUpdate.paramError | task not belong to bizTag | 待办任务不属于该应用 |
| 400 | todo.taskExecutorStatusUpdate.paramError | executors is oversize | 待办执行人超出限制 |
| 500 | todo.taskExecutorStatusUpdate.systemError | todo.taskExecutorStatusUpdate.systemError | 更新待办执行者状态系统异常 |
