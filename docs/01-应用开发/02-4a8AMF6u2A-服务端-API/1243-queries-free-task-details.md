---
title: "获取自由任务详情"
source_url: "https://open.dingtalk.com/document/development/queries-free-task-details"
namespace: "development"
slug: "queries-free-task-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 任务 > 自由任务 > 获取自由任务详情"
doc_id: "UMuTDwzqSD"
updated_at: "2026-06-04 19:11:44"
---

> Source: https://open.dingtalk.com/document/development/queries-free-task-details
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 任务 > 自由任务 > 获取自由任务详情
> Updated: 2026-06-04 19:11:44

# 获取自由任务详情

调用本接口，通过任务ID获取自由任务的详情，包括创建者、执行者、截止时间等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/tasks/{taskId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Read.All-项目应用中任务读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 是 | 任务id，调用[创建自由任务](1242-create-a-free-task.md)接口获取的id值。 |
| userId | String | 是 | 操作者userId。 |

### 请求示例

HTTP

```
GET /v1.0/project/organizations/users/0715xxxx/tasks/62a010c153c2ef52xxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkproject_1_0.*;
import com.aliyun.dingtalkproject_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkproject_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkproject_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkproject_1_0.Client client = Sample.createClient();
        GetOrganizationTaskHeaders getOrganizationTaskHeaders = new GetOrganizationTaskHeaders();
        getOrganizationTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getOrganizationTaskWithOptions("62a010c153c2ef52xxxx", "0715xxxx", getOrganizationTaskHeaders, new RuntimeOptions());
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
        get_organization_task_headers = dingtalkproject__1__0_models.GetOrganizationTaskHeaders()
        get_organization_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_organization_task_with_options('62a010c153c2ef52xxxx', '0715xxxx', get_organization_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_organization_task_headers = dingtalkproject__1__0_models.GetOrganizationTaskHeaders()
        get_organization_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_organization_task_with_options_async('62a010c153c2ef52xxxx', '0715xxxx', get_organization_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\GetOrganizationTaskHeaders;
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
        $getOrganizationTaskHeaders = new GetOrganizationTaskHeaders([]);
        $getOrganizationTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getOrganizationTaskWithOptions("62a010c153c2ef52xxxx", "0715xxxx", $getOrganizationTaskHeaders, new RuntimeOptions([]));
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

  getOrganizationTaskHeaders := &dingtalkproject_1_0.GetOrganizationTaskHeaders{}
  getOrganizationTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetOrganizationTaskWithOptions(tea.String("62a010c153c2ef52xxxx"), tea.String("0715xxxx"), getOrganizationTaskHeaders, &util.RuntimeOptions{})
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
    let getOrganizationTaskHeaders = new $dingtalkproject_1_0.GetOrganizationTaskHeaders({ });
    getOrganizationTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.getOrganizationTaskWithOptions("62a010c153c2ef52xxxx", "0715xxxx", getOrganizationTaskHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetOrganizationTaskHeaders getOrganizationTaskHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetOrganizationTaskHeaders();
            getOrganizationTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetOrganizationTaskWithOptions("62a010c153c2ef52xxxx", "0715xxxx", getOrganizationTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| note | String | 任务备注。 |
| visible | String | 任务可见性。   - **involves**：仅参与者可见 - **members**：所有人可见 |
| executorId | String | 执行者userId。 |
| created | String | 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。      转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| dueDate | String | 任务截止时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。      转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| creatorId | String | 创建者userId。 |
| involveMembers | Array of String | 任务参与者userId列表。 |
| priority | Integer | 自由任务优先级。   - 使用项目默认的优先级，如下图所示。优先级默认为以下。    - **-10**：较低，默认值。   - **0**：普通   - **1**：紧急   - **2**：非常紧急      - 用户自定义优先级，如下图所示，新增一般紧急。   该参数值以接口实际调用结果为准。优先级越高，数值越大。 |
| isDone | Boolean | 任务是否已完成。   - **true**：未完成 - **false**：已完成 |
| content | String | 任务标题。 |
| labels | Array of String | 任务自定义标记。 |
| isDeleted | Boolean | 任务是否已删除。   - **true**：已删除 - **false**：未删除 |
| ancestorIds | Array of String | 该任务父任务的id。 |
| taskId | String | 任务id。 |
| updated | String | 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。      转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| startDate | String | 任务开始时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。      转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "note" : "我是一条备注哦",
    "visible" : "members",
    "executorId" : "0715xxxx",
    "created" : "2021-08-13T07:36:50.318Z",
    "dueDate" : "2021-08-13T07:36:50.318Z",
    "creatorId" : "0715xxxx",
    "involveMembers" : [ "173xxxx" ],
    "priority" : -10,
    "isDone" : false,
    "content" : "明天12点前写好周报",
    "labels" : [ "xxxx" ],
    "isDeleted" : false,
    "ancestorIds" : [ "62a010c153c2efxxxxxxx" ],
    "taskId" : "62a010c153c2exxxxxxxxx",
    "updated" : "2021-08-13T07:36:50.318Z",
    "startDate" : "2021-08-13T07:36:50.318Z"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在 |
| 500 | server.error | system error | 系统内部服务错误 |
