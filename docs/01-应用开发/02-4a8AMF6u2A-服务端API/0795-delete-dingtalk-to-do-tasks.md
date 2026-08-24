---
title: "删除钉钉待办任务"
source_url: "https://open.dingtalk.com/document/development/delete-dingtalk-to-do-tasks"
namespace: "development"
slug: "delete-dingtalk-to-do-tasks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "待办任务 > 删除钉钉待办任务"
doc_id: "luZvsbYUIa"
updated_at: "2026-06-04 19:09:51"
---

> Source: https://open.dingtalk.com/document/development/delete-dingtalk-to-do-tasks
> Path: 应用开发 / 服务端API / 待办任务 > 删除钉钉待办任务
> Updated: 2026-06-04 19:09:51

# 删除钉钉待办任务

调用本接口，删除钉钉待办任务信息，ISV在自身应用待办数据被删除后，需调用本接口将钉钉侧待办数据同步删除。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks/{taskId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Todo.Todo.Write-待办应用中待办写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 当前访问资源所归属用户的unionId，和操作者的unionId保持一致，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| taskId | String | 是 | 待办ID。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 否 | 当前操作者的用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
DELETE /v1.0/todo/users/PUoiinWIpa2yH2ymhiiGiP6g/tasks/OPJpwtwPVNGIFKURjrzd?operatorId=PUoiinWIpa2yH2ymhiiGiP6g HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b3ba046c118a3445b111db282824c0b4
Content-Type:application/json
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
        DeleteTodoTaskHeaders deleteTodoTaskHeaders = new DeleteTodoTaskHeaders();
        deleteTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DeleteTodoTaskRequest deleteTodoTaskRequest = new DeleteTodoTaskRequest()
                .setOperatorId("PUoiinWIpa2yH2ymhiiGiP6g");
        try {
            client.deleteTodoTaskWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", deleteTodoTaskRequest, deleteTodoTaskHeaders, new RuntimeOptions());
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
        delete_todo_task_headers = dingtalktodo__1__0_models.DeleteTodoTaskHeaders()
        delete_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_todo_task_request = dingtalktodo__1__0_models.DeleteTodoTaskRequest(
            operator_id='PUoiinWIpa2yH2ymhiiGiP6g'
        )
        try:
            client.delete_todo_task_with_options('PUoiinWIpa2yH2ymhiiGiP6g', 'OPJpwtwPVNGIFKURjrzd', delete_todo_task_request, delete_todo_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_todo_task_headers = dingtalktodo__1__0_models.DeleteTodoTaskHeaders()
        delete_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_todo_task_request = dingtalktodo__1__0_models.DeleteTodoTaskRequest(
            operator_id='PUoiinWIpa2yH2ymhiiGiP6g'
        )
        try:
            await client.delete_todo_task_with_options_async('PUoiinWIpa2yH2ymhiiGiP6g', 'OPJpwtwPVNGIFKURjrzd', delete_todo_task_request, delete_todo_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\DeleteTodoTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\DeleteTodoTaskRequest;
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
        $deleteTodoTaskHeaders = new DeleteTodoTaskHeaders([]);
        $deleteTodoTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteTodoTaskRequest = new DeleteTodoTaskRequest([
            "operatorId" => "PUoiinWIpa2yH2ymhiiGiP6g"
        ]);
        try {
            $client->deleteTodoTaskWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", $deleteTodoTaskRequest, $deleteTodoTaskHeaders, new RuntimeOptions([]));
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

  deleteTodoTaskHeaders := &dingtalktodo_1_0.DeleteTodoTaskHeaders{}
  deleteTodoTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteTodoTaskRequest := &dingtalktodo_1_0.DeleteTodoTaskRequest{
    OperatorId: tea.String("PUoiinWIpa2yH2ymhiiGiP6g"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteTodoTaskWithOptions(tea.String("PUoiinWIpa2yH2ymhiiGiP6g"), tea.String("OPJpwtwPVNGIFKURjrzd"), deleteTodoTaskRequest, deleteTodoTaskHeaders, &util.RuntimeOptions{})
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
    let deleteTodoTaskHeaders = new $dingtalktodo_1_0.DeleteTodoTaskHeaders({ });
    deleteTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deleteTodoTaskRequest = new $dingtalktodo_1_0.DeleteTodoTaskRequest({
      operatorId: "PUoiinWIpa2yH2ymhiiGiP6g",
    });
    try {
      await client.deleteTodoTaskWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", deleteTodoTaskRequest, deleteTodoTaskHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.DeleteTodoTaskHeaders deleteTodoTaskHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.DeleteTodoTaskHeaders();
            deleteTodoTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.DeleteTodoTaskRequest deleteTodoTaskRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.DeleteTodoTaskRequest
            {
                OperatorId = "PUoiinWIpa2yH2ymhiiGiP6g",
            };
            try
            {
                client.DeleteTodoTaskWithOptions("PUoiinWIpa2yH2ymhiiGiP6g", "OPJpwtwPVNGIFKURjrzd", deleteTodoTaskRequest, deleteTodoTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::DeleteTodoTaskHeaders> deleteTodoTaskHeaders = make_shared<Alibabacloud_Dingtalktodo_1_0::DeleteTodoTaskHeaders>();
  deleteTodoTaskHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::DeleteTodoTaskRequest> deleteTodoTaskRequest = make_shared<Alibabacloud_Dingtalktodo_1_0::DeleteTodoTaskRequest>(map<string, boost::any>({
    {"operatorId", boost::any(string("PUoiinWIpa2yH2ymhiiGiP6g"))}
  }));
  try {
    client->deleteTodoTaskWithOptions(make_shared<string>("PUoiinWIpa2yH2ymhiiGiP6g"), make_shared<string>("OPJpwtwPVNGIFKURjrzd"), deleteTodoTaskRequest, deleteTodoTaskHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Boolean | 删除结果，true表示删除成功。 |
| requestId | String | 请求ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true,
  "requestId" : "PUoixxxxiiGiP6g"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.taskDelete.paramError | todo.taskDelete.paramError | 删除待办参数异常 |
| 400 | todo.taskDelete.paramError | task not exist | 待办任务不存在 |
| 500 | todo.taskDelete.systemError | todo.taskDelete.systemError | 删除待办系统异常 |
