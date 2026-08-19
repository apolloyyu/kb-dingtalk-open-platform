---
title: "创建自由任务"
source_url: "https://open.dingtalk.com/document/development/create-a-free-task"
namespace: "development"
slug: "create-a-free-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务 > 自由任务 > 创建自由任务"
doc_id: "PV6r1qh7mH"
updated_at: "2025-10-09 18:06:54"
---

> Source: https://open.dingtalk.com/document/development/create-a-free-task
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务 > 自由任务 > 创建自由任务
> Updated: 2025-10-09 18:06:54

# 创建自由任务

调用本接口，创建一个钉钉自由任务（非加入项目的任务）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/tasks |
| HTTP Method | POST |
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

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| content | String | 是 | 任务标题。 |
| note | String | 否 | 任务备注。 |
| priority | Integer | 是 | 自由任务优先级，如下图所示。用户是否有自定义更新优先级，获取该参数方法不同。   - 用户未更新优先级。该参数默认为以下值：    - **较低，默认值**：10   - **普通**：0   - **紧急**：1   - **非常紧急**：2      - 用户自定义优先级，如下图所示，新增**一般紧急**并调整优先级顺序等，需要通过调用[查询优先级列表](1244-query-a-priority-list.md)接口获取接口获取该参数值。     **[!NOTE]**     - 优先级数值越大，优先级越高。 - 自定义优先级需要开通企业版或者旗舰版项目，开通请参考[开通企业版或旗舰版](https://www.teambition.com/pricing/)。 |
| involveMembers | Array of String | 否 | 参与者userId列表，建议参与者总人数不超过20个。 |
| executorId | String | 否 | 执行者userId。 |
| dueDate | String | 否 | 任务截止日期，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| createTime | String | 否 | 任务创建日期，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| visible | String | 是 | 任务可见性。   - **involves**：仅参与者可见 - **members**：所有人可见 |
| disableNotification | Boolean | 否 | 是否禁止通知。   - **true**：禁止，不显示通知。 - **false**：不禁止，显示通知。 |
| disableActivity | Boolean | 否 | 是否禁止动态。   - **true**：禁止，不显示该任务动态信息。 - **false**：不禁止，显示该任务动态信息。 |

### 请求示例

HTTP

```
POST /v1.0/project/organizations/users/0152xxxx/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "content" : "明天12点前完成周报撰写",
  "note" : "任务备注信息",
  "priority" : -10,
  "involveMembers" : [ "0152xxxx" ],
  "executorId" : "0152xxxx",
  "dueDate" : "2021-08-13T07:36:50.318Z",
  "createTime" : "2021-08-13T07:36:50.318Z",
  "visible" : "members",
  "disableNotification" : false,
  "disableActivity" : false
}
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
        CreateOrganizationTaskHeaders createOrganizationTaskHeaders = new CreateOrganizationTaskHeaders();
        createOrganizationTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateOrganizationTaskRequest createOrganizationTaskRequest = new CreateOrganizationTaskRequest()
                .setContent("明天12点前完成周报撰写")
                .setNote("任务备注信息")
                .setPriority(-10)
                .setInvolveMembers(java.util.Arrays.asList(
                    "0152xxxx"
                ))
                .setExecutorId("0152xxxx")
                .setDueDate("2021-08-13T07:36:50.318Z")
                .setCreateTime("2021-08-13T07:36:50.318Z")
                .setVisible("members")
                .setDisableNotification(false)
                .setDisableActivity(false);
        try {
            client.createOrganizationTaskWithOptions("0152xxxx", createOrganizationTaskRequest, createOrganizationTaskHeaders, new RuntimeOptions());
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
        create_organization_task_headers = dingtalkproject__1__0_models.CreateOrganizationTaskHeaders()
        create_organization_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_organization_task_request = dingtalkproject__1__0_models.CreateOrganizationTaskRequest(
            content='明天12点前完成周报撰写',
            note='任务备注信息',
            priority=-10,
            involve_members=[
                '0152xxxx'
            ],
            executor_id='0152xxxx',
            due_date='2021-08-13T07:36:50.318Z',
            create_time='2021-08-13T07:36:50.318Z',
            visible='members',
            disable_notification=False,
            disable_activity=False
        )
        try:
            client.create_organization_task_with_options('0152xxxx', create_organization_task_request, create_organization_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_organization_task_headers = dingtalkproject__1__0_models.CreateOrganizationTaskHeaders()
        create_organization_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_organization_task_request = dingtalkproject__1__0_models.CreateOrganizationTaskRequest(
            content='明天12点前完成周报撰写',
            note='任务备注信息',
            priority=-10,
            involve_members=[
                '0152xxxx'
            ],
            executor_id='0152xxxx',
            due_date='2021-08-13T07:36:50.318Z',
            create_time='2021-08-13T07:36:50.318Z',
            visible='members',
            disable_notification=False,
            disable_activity=False
        )
        try:
            await client.create_organization_task_with_options_async('0152xxxx', create_organization_task_request, create_organization_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateOrganizationTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateOrganizationTaskRequest;
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
        $createOrganizationTaskHeaders = new CreateOrganizationTaskHeaders([]);
        $createOrganizationTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createOrganizationTaskRequest = new CreateOrganizationTaskRequest([
            "content" => "明天12点前完成周报撰写",
            "note" => "任务备注信息",
            "priority" => -10,
            "involveMembers" => [
                "0152xxxx"
            ],
            "executorId" => "0152xxxx",
            "dueDate" => "2021-08-13T07:36:50.318Z",
            "createTime" => "2021-08-13T07:36:50.318Z",
            "visible" => "members",
            "disableNotification" => false,
            "disableActivity" => false
        ]);
        try {
            $client->createOrganizationTaskWithOptions("0152xxxx", $createOrganizationTaskRequest, $createOrganizationTaskHeaders, new RuntimeOptions([]));
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

  createOrganizationTaskHeaders := &dingtalkproject_1_0.CreateOrganizationTaskHeaders{}
  createOrganizationTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createOrganizationTaskRequest := &dingtalkproject_1_0.CreateOrganizationTaskRequest{
    Content: tea.String("明天12点前完成周报撰写"),
    Note: tea.String("任务备注信息"),
    Priority: tea.Int32(-10),
    InvolveMembers: []*string{tea.String("0152xxxx")},
    ExecutorId: tea.String("0152xxxx"),
    DueDate: tea.String("2021-08-13T07:36:50.318Z"),
    CreateTime: tea.String("2021-08-13T07:36:50.318Z"),
    Visible: tea.String("members"),
    DisableNotification: tea.Bool(false),
    DisableActivity: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateOrganizationTaskWithOptions(tea.String("0152xxxx"), createOrganizationTaskRequest, createOrganizationTaskHeaders, &util.RuntimeOptions{})
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
    let createOrganizationTaskHeaders = new $dingtalkproject_1_0.CreateOrganizationTaskHeaders({ });
    createOrganizationTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createOrganizationTaskRequest = new $dingtalkproject_1_0.CreateOrganizationTaskRequest({
      content: "明天12点前完成周报撰写",
      note: "任务备注信息",
      priority: -10,
      involveMembers: [
        "0152xxxx"
      ],
      executorId: "0152xxxx",
      dueDate: "2021-08-13T07:36:50.318Z",
      createTime: "2021-08-13T07:36:50.318Z",
      visible: "members",
      disableNotification: false,
      disableActivity: false,
    });
    try {
      await client.createOrganizationTaskWithOptions("0152xxxx", createOrganizationTaskRequest, createOrganizationTaskHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateOrganizationTaskHeaders createOrganizationTaskHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateOrganizationTaskHeaders();
            createOrganizationTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateOrganizationTaskRequest createOrganizationTaskRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateOrganizationTaskRequest
            {
                Content = "明天12点前完成周报撰写",
                Note = "任务备注信息",
                Priority = -10,
                InvolveMembers = new List<string>
                {
                    "0152xxxx"
                },
                ExecutorId = "0152xxxx",
                DueDate = "2021-08-13T07:36:50.318Z",
                CreateTime = "2021-08-13T07:36:50.318Z",
                Visible = "members",
                DisableNotification = false,
                DisableActivity = false,
            };
            try
            {
                client.CreateOrganizationTaskWithOptions("0152xxxx", createOrganizationTaskRequest, createOrganizationTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dueDate | String | 任务截止日期，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| executor | Object | 执行者。 |
| avatarUrl | String | 执行者头像地址。 |
| name | String | 执行者姓名。 |
| userId | String | 执行者userId。 |
| id | String | 任务id。  **[!NOTE]**    暂无其他接口可获取任务id值，请妥善保存任务id。 |
| visible | String | 任务可见性。   - **involves**：仅参与者可见 - **members**：所有人可见 |
| created | String | 创建时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| priority | Integer | 自由任务优先级。   - 使用项目默认的优先级，如下图所示。优先级默认为以下。    - **-10**：较低，默认值。   - **0**：普通   - **1**：紧急   - **2**：非常紧急      - 用户自定义优先级，如下图所示，新增一般紧急并调整优先级顺序等。该参数值以接口实际调用结果为准。优先级越高，数值越大。 |
| involvers | Array | 参与者信息列表。 |
| avatarUrl | String | 参与者头像地址。 |
| name | String | 参与者名字。 |
| id | String | 参与者userId。 |
| updated | String | 更新时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。  **[!NOTE]**    转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |
| note | String | 任务备注。 |
| hasReminder | Boolean | 任务是否有提醒。   - **true**：有提醒 - **false**：无提醒 |
| creatorId | String | 创建者userId。 |
| content | String | 任务标题。 |
| attachmentsCount | Integer | 附件数量。 |
| isDeleted | Boolean | 是否删除。   - **ture**：已删除 - **false**：未删除 |
| ancestorIds | Array of String | 该任务父任务的id。 |
| creator | Object | 创建者对象。 |
| avatarUrl | String | 创建者头像地址。 |
| name | String | 创建者姓名。 |
| userId | String | 创建者userId。 |
| executorId | String | 执行者userId。 |
| involveMembers | Array of String | 参与者userId列表。 |
| isDone | String | 是否完成。   - **true**：已完成 - **false**：未完成 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "dueDate" : "2021-08-13T07:36:50.318Z",
    "executor" : {
      "avatarUrl" : "https://example.com",
      "name" : "小钉",
      "userId" : "0152xxxx"
    },
    "id" : "62a697c053c2ef5xxxxxx",
    "visible" : "members",
    "created" : "2021-08-13T07:36:50.318Z",
    "priority" : -10,
    "involvers" : [ {
      "avatarUrl" : "httpx://example.com",
      "name" : "小钉",
      "id" : "0152xxxx"
    } ],
    "updated" : "2021-08-13T07:36:50.318Z",
    "note" : "任务备注信息",
    "hasReminder" : false,
    "creatorId" : "0152xxxx",
    "content" : "明天12点前写好周报",
    "attachmentsCount" : 0,
    "isDeleted" : false,
    "ancestorIds" : [ "62a697c053c2ef5xxx" ],
    "creator" : {
      "avatarUrl" : "https://example.com",
      "name" : "小钉",
      "userId" : "0152xxxx"
    },
    "executorId" : "0152xxxx",
    "involveMembers" : [ "0152xxxx" ],
    "isDone" : "false"
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
