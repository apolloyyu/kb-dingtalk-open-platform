---
title: "更新任务参与者"
source_url: "https://open.dingtalk.com/document/development/update-task-participants"
namespace: "development"
slug: "update-task-participants"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务 > 项目任务 > 更新任务参与者"
doc_id: "Qzp7CKbiIl"
updated_at: "2026-06-03 09:26:13"
---

> Source: https://open.dingtalk.com/document/development/update-task-participants
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务 > 项目任务 > 更新任务参与者
> Updated: 2026-06-03 09:26:13

# 更新任务参与者

调用本接口更新任务参与者。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/tasks/{taskId}/involveMembers |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Write.All-项目应用任务写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |
| taskId | String | 是 | 任务ID，可通过调用[查询项目中的任务](1229-query-tasks-in-a-project.md)接口，获取返回参数`taskId`字段。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| involveMembers | Array of String | 否 | 参与者用户userId。 |
| addInvolvers | Array of String | 否 | 参与者用户userId。 |
| delInvolvers | Array of String | 否 | 参与者用户userId。 |

### 请求示例

HTTP

```
PUT /v1.0/project/users/0517xxx/tasks/60a2187eb72xxxxxxx/involveMembers HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "involveMembers" : [ "0517xxxxxxx" ],
  "addInvolvers" : [ "0517xxxxxxx" ],
  "delInvolvers" : [ "0517xxxxxxx" ]
}
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
        com.aliyun.dingtalkproject_1_0.models.UpdateTaskInvolvemembersHeaders updateTaskInvolvemembersHeaders = new com.aliyun.dingtalkproject_1_0.models.UpdateTaskInvolvemembersHeaders();
        updateTaskInvolvemembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.UpdateTaskInvolvemembersRequest updateTaskInvolvemembersRequest = new com.aliyun.dingtalkproject_1_0.models.UpdateTaskInvolvemembersRequest()
                .setInvolveMembers(java.util.Arrays.asList(
                    "0517xxxxxxx"
                ))
                .setAddInvolvers(java.util.Arrays.asList(
                    "0517xxxxxxx"
                ))
                .setDelInvolvers(java.util.Arrays.asList(
                    "0517xxxxxxx"
                ));
        try {
            client.updateTaskInvolvemembersWithOptions("0517xxx", "60a2187eb72xxxxxxx", updateTaskInvolvemembersRequest, updateTaskInvolvemembersHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_task_involvemembers_headers = dingtalkproject__1__0_models.UpdateTaskInvolvemembersHeaders()
        update_task_involvemembers_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_task_involvemembers_request = dingtalkproject__1__0_models.UpdateTaskInvolvemembersRequest(
            involve_members=[
                '0517xxxxxxx'
            ],
            add_involvers=[
                '0517xxxxxxx'
            ],
            del_involvers=[
                '0517xxxxxxx'
            ]
        )
        try:
            client.update_task_involvemembers_with_options('0517xxx', '60a2187eb72xxxxxxx', update_task_involvemembers_request, update_task_involvemembers_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_task_involvemembers_headers = dingtalkproject__1__0_models.UpdateTaskInvolvemembersHeaders()
        update_task_involvemembers_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_task_involvemembers_request = dingtalkproject__1__0_models.UpdateTaskInvolvemembersRequest(
            involve_members=[
                '0517xxxxxxx'
            ],
            add_involvers=[
                '0517xxxxxxx'
            ],
            del_involvers=[
                '0517xxxxxxx'
            ]
        )
        try:
            await client.update_task_involvemembers_with_options_async('0517xxx', '60a2187eb72xxxxxxx', update_task_involvemembers_request, update_task_involvemembers_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\UpdateTaskInvolvemembersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\UpdateTaskInvolvemembersRequest;
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
        $updateTaskInvolvemembersHeaders = new UpdateTaskInvolvemembersHeaders([]);
        $updateTaskInvolvemembersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateTaskInvolvemembersRequest = new UpdateTaskInvolvemembersRequest([
            "involveMembers" => [
                "0517xxxxxxx"
            ],
            "addInvolvers" => [
                "0517xxxxxxx"
            ],
            "delInvolvers" => [
                "0517xxxxxxx"
            ]
        ]);
        try {
            $client->updateTaskInvolvemembersWithOptions("0517xxx", "60a2187eb72xxxxxxx", $updateTaskInvolvemembersRequest, $updateTaskInvolvemembersHeaders, new RuntimeOptions([]));
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

  updateTaskInvolvemembersHeaders := &dingtalkproject_1_0.UpdateTaskInvolvemembersHeaders{}
  updateTaskInvolvemembersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateTaskInvolvemembersRequest := &dingtalkproject_1_0.UpdateTaskInvolvemembersRequest{
    InvolveMembers: []*string{tea.String("0517xxxxxxx")},
    AddInvolvers: []*string{tea.String("0517xxxxxxx")},
    DelInvolvers: []*string{tea.String("0517xxxxxxx")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateTaskInvolvemembersWithOptions(tea.String("0517xxx"), tea.String("60a2187eb72xxxxxxx"), updateTaskInvolvemembersRequest, updateTaskInvolvemembersHeaders, &util.RuntimeOptions{})
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
    let updateTaskInvolvemembersHeaders = new $dingtalkproject_1_0.UpdateTaskInvolvemembersHeaders({ });
    updateTaskInvolvemembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateTaskInvolvemembersRequest = new $dingtalkproject_1_0.UpdateTaskInvolvemembersRequest({
      involveMembers: [
        "0517xxxxxxx"
      ],
      addInvolvers: [
        "0517xxxxxxx"
      ],
      delInvolvers: [
        "0517xxxxxxx"
      ],
    });
    try {
      await client.updateTaskInvolvemembersWithOptions("0517xxx", "60a2187eb72xxxxxxx", updateTaskInvolvemembersRequest, updateTaskInvolvemembersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateTaskInvolvemembersHeaders updateTaskInvolvemembersHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateTaskInvolvemembersHeaders();
            updateTaskInvolvemembersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateTaskInvolvemembersRequest updateTaskInvolvemembersRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateTaskInvolvemembersRequest
            {
                InvolveMembers = new List<string>
                {
                    "0517xxxxxxx"
                },
                AddInvolvers = new List<string>
                {
                    "0517xxxxxxx"
                },
                DelInvolvers = new List<string>
                {
                    "0517xxxxxxx"
                },
            };
            try
            {
                client.UpdateTaskInvolvemembersWithOptions("0517xxx", "60a2187eb72xxxxxxx", updateTaskInvolvemembersRequest, updateTaskInvolvemembersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 结果 |
| involveMembers | Array of String | 参与者用户userId。 |
| updated | String | 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "involveMembers" : [ "0517xxxxxxx" ],
    "updated" : "2022-07-04T03:29:34.770Z"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
