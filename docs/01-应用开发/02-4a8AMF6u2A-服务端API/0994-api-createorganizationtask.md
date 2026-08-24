---
title: "创建自由任务"
source_url: "https://open.dingtalk.com/document/development/api-createorganizationtask"
namespace: "development"
slug: "api-createorganizationtask"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉快办 > 创建自由任务"
doc_id: "F5BpXQdBIL"
updated_at: "2026-06-04 14:24:31"
---

> Source: https://open.dingtalk.com/document/development/api-createorganizationtask
> Path: 应用开发 / 服务端API / 钉钉快办 > 创建自由任务
> Updated: 2026-06-04 14:24:31

# 创建自由任务

调用本接口，创建一个钉钉快办自由任务（非协作空间的任务）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/teamSphere/organizations/users/{userId}/tasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-TeamSphere.Project.ReadWrite-钉钉快办管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作人userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| content | String | 是 | 任务标题。 |
| note | String | 否 | 任务备注。 |
| involveMembers | Array of String | 否 | 参与者id。 |
| executorId | String | 否 | 执行者id。 |
| dueDate | String | 否 | 任务截止日期。 |
| visible | String | 是 | 任务可见性。involves：仅参与者可见。 |
| disableNotification | Boolean | 否 | 是否禁止通知：   - true：禁止 - false：不禁止 |
| disableActivity | Boolean | 否 | 是否禁止动态：   - true：禁止 - false：不禁止 |

### 请求示例

HTTP

```
POST /v1.0/teamSphere/organizations/users/173xxxx/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:be08245012b9364b83a3c1f0d51199a6
Content-Type:application/json

{
  "content" : "明天12点前完成周报撰写",
  "note" : "我是一条任务备注",
  "involveMembers" : [ "173xxxx" ],
  "executorId" : "173xxxx",
  "dueDate" : "2021-08-13T07:36:50.318Z",
  "visible" : "involves",
  "disableNotification" : false,
  "disableActivity" : false
}
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
        com.aliyun.dingtalkteam_sphere_1_0.models.CreateOrganizationTaskHeaders createOrganizationTaskHeaders = new com.aliyun.dingtalkteam_sphere_1_0.models.CreateOrganizationTaskHeaders();
        createOrganizationTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkteam_sphere_1_0.models.CreateOrganizationTaskRequest createOrganizationTaskRequest = new com.aliyun.dingtalkteam_sphere_1_0.models.CreateOrganizationTaskRequest()
                .setContent("明天12点前完成周报撰写")
                .setNote("我是一条任务备注")
                .setInvolveMembers(java.util.Arrays.asList(
                    "173xxxx"
                ))
                .setExecutorId("173xxxx")
                .setDueDate("2021-08-13T07:36:50.318Z")
                .setVisible("involves")
                .setDisableNotification(false)
                .setDisableActivity(false);
        try {
            client.createOrganizationTaskWithOptions("173xxxx", createOrganizationTaskRequest, createOrganizationTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_organization_task_headers = dingtalkteam_sphere__1__0_models.CreateOrganizationTaskHeaders()
        create_organization_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_organization_task_request = dingtalkteam_sphere__1__0_models.CreateOrganizationTaskRequest(
            content='明天12点前完成周报撰写',
            note='我是一条任务备注',
            involve_members=[
                '173xxxx'
            ],
            executor_id='173xxxx',
            due_date='2021-08-13T07:36:50.318Z',
            visible='involves',
            disable_notification=False,
            disable_activity=False
        )
        try:
            client.create_organization_task_with_options('173xxxx', create_organization_task_request, create_organization_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_organization_task_headers = dingtalkteam_sphere__1__0_models.CreateOrganizationTaskHeaders()
        create_organization_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_organization_task_request = dingtalkteam_sphere__1__0_models.CreateOrganizationTaskRequest(
            content='明天12点前完成周报撰写',
            note='我是一条任务备注',
            involve_members=[
                '173xxxx'
            ],
            executor_id='173xxxx',
            due_date='2021-08-13T07:36:50.318Z',
            visible='involves',
            disable_notification=False,
            disable_activity=False
        )
        try:
            await client.create_organization_task_with_options_async('173xxxx', create_organization_task_request, create_organization_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\CreateOrganizationTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\CreateOrganizationTaskRequest;
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
            "note" => "我是一条任务备注",
            "involveMembers" => [
                "173xxxx"
            ],
            "executorId" => "173xxxx",
            "dueDate" => "2021-08-13T07:36:50.318Z",
            "visible" => "involves",
            "disableNotification" => false,
            "disableActivity" => false
        ]);
        try {
            $client->createOrganizationTaskWithOptions("173xxxx", $createOrganizationTaskRequest, $createOrganizationTaskHeaders, new RuntimeOptions([]));
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

  createOrganizationTaskHeaders := &dingtalkteamsphere_1_0.CreateOrganizationTaskHeaders{}
  createOrganizationTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createOrganizationTaskRequest := &dingtalkteamsphere_1_0.CreateOrganizationTaskRequest{
    Content: tea.String("明天12点前完成周报撰写"),
    Note: tea.String("我是一条任务备注"),
    InvolveMembers: []*string{tea.String("173xxxx")},
    ExecutorId: tea.String("173xxxx"),
    DueDate: tea.String("2021-08-13T07:36:50.318Z"),
    Visible: tea.String("involves"),
    DisableNotification: tea.Bool(false),
    DisableActivity: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateOrganizationTaskWithOptions(tea.String("173xxxx"), createOrganizationTaskRequest, createOrganizationTaskHeaders, &util.RuntimeOptions{})
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
    let createOrganizationTaskHeaders = new dingtalkteamSphere_1_0.CreateOrganizationTaskHeaders({ });
    createOrganizationTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createOrganizationTaskRequest = new dingtalkteamSphere_1_0.CreateOrganizationTaskRequest({
      content: '明天12点前完成周报撰写',
      note: '我是一条任务备注',
      involveMembers: [
        '173xxxx'
      ],
      executorId: '173xxxx',
      dueDate: '2021-08-13T07:36:50.318Z',
      visible: 'involves',
      disableNotification: false,
      disableActivity: false,
    });
    try {
      await client.createOrganizationTaskWithOptions('173xxxx', createOrganizationTaskRequest, createOrganizationTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateOrganizationTaskHeaders createOrganizationTaskHeaders = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateOrganizationTaskHeaders();
            createOrganizationTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateOrganizationTaskRequest createOrganizationTaskRequest = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.CreateOrganizationTaskRequest
            {
                Content = "明天12点前完成周报撰写",
                Note = "我是一条任务备注",
                InvolveMembers = new List<string>
                {
                    "173xxxx"
                },
                ExecutorId = "173xxxx",
                DueDate = "2021-08-13T07:36:50.318Z",
                Visible = "involves",
                DisableNotification = false,
                DisableActivity = false,
            };
            try
            {
                client.CreateOrganizationTaskWithOptions("173xxxx", createOrganizationTaskRequest, createOrganizationTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果对象。 |
| dueDate | String | 任务截止日期。 |
| executor | Object | 执行者。 |
| avatarUrl | String | 头像地址。 |
| name | String | 姓名。 |
| userId | String | 执行者id。 |
| id | String | 任务id。 |
| visible | String | 任务可见性：   - involves：仅参与者可见 - members：所有人可见 |
| created | String | 创建时间。 |
| involvers | Array | 参与者列表。 |
| avatarUrl | String | 头像。 |
| name | String | 名字。 |
| id | String | 用户id。 |
| updated | String | 更新时间。 |
| note | String | 任务备注。 |
| hasReminder | Boolean | 是否有提醒。 |
| creatorId | String | 创建者id。 |
| content | String | 任务标题。 |
| attachmentsCount | Integer | 附件数量。 |
| isDeleted | Boolean | 是否删除。 |
| ancestorIds | Array of String | 父任务ID。 |
| creator | Object | 创建者。 |
| avatarUrl | String | 创建者头像地址。 |
| name | String | 创建者姓名。 |
| userId | String | 创建者id。 |
| executorId | String | 执行者id。 |
| involveMembers | Array of String | 参与者id。 |
| isDone | String | 是否完成：   - true：完成 - false：没有完成 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "dueDate" : "2021-08-13T07:36:50.318Z",
    "executor" : {
      "avatarUrl" : "https://xxxxxxxxxx",
      "name" : "鬼斩",
      "userId" : "173xxxx"
    },
    "id" : "62a697c053c2ef5xxxxxx",
    "visible" : "members",
    "created" : "2021-08-13T07:36:50.318Z",
    "involvers" : [ {
      "avatarUrl" : "httpx://xxx",
      "name" : "鬼斩",
      "id" : "173xxxx"
    } ],
    "updated" : "2021-08-13T07:36:50.318Z",
    "note" : "我是一条备注哦",
    "hasReminder" : false,
    "creatorId" : "173xxxx",
    "content" : "明天12点前写好周报",
    "attachmentsCount" : 0,
    "isDeleted" : false,
    "ancestorIds" : [ "62a697c053c2ef5xxx" ],
    "creator" : {
      "avatarUrl" : "https://xxxxxxxxxx",
      "name" : "小钉",
      "userId" : "173xxxx"
    },
    "executorId" : "173xxxx",
    "involveMembers" : [ "173xxxx" ],
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
