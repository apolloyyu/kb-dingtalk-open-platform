---
title: "增加或删除自由任务的参与者"
source_url: "https://open.dingtalk.com/document/development/change-task-participant"
namespace: "development"
slug: "change-task-participant"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 任务 > 自由任务 > 增加或删除自由任务的参与者"
doc_id: "drFZ3Xrsnl"
updated_at: "2025-10-09 18:07:02"
---

> Source: https://open.dingtalk.com/document/development/change-task-participant
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 任务 > 自由任务 > 增加或删除自由任务的参与者
> Updated: 2025-10-09 18:07:02

# 增加或删除自由任务的参与者

更新自由任务参与者

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/organizations/users/{userId}/tasks/{taskId}/involveMembers |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Write.All-项目应用中任务写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 是 | 任务id，调用[创建自由任务](1242-create-a-free-task.md)接口获取的id值。 |
| userId | String | 是 | 操作者userId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| involveMembers | Array of String | 否 | 所有参与者userId列表，建议参与者总人数不超过20个。 |
| addInvolvers | Array of String | 否 | 增加的参与者userId列表，建议参与者总人数不超过20个。 |
| delInvolvers | Array of String | 否 | 删除的参与者userId列表。 |
| disableActivity | Boolean | 否 | 是否禁止动态。   - **true**：禁止，不显示该任务动态信息。 - **false**：不禁止，显示该任务动态信息。 |
| disableNotification | Boolean | 否 | 是否禁止通知。   - **true**：禁止，不显示通知。 - **false**：不禁止，显示通知。 |

### 请求示例

HTTP

```
PUT /v1.0/project/organizations/users/0715xxxx/tasks/62a010c153c2ef52448xxxx/involveMembers HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json

{
  "involveMembers" : [ "0715xxxx" ],
  "addInvolvers" : [ "0715xxxx" ],
  "delInvolvers" : [ "0715xxxx" ],
  "disableActivity" : true,
  "disableNotification" : true
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
        UpdateOrganizationTaskInvolveMembersHeaders updateOrganizationTaskInvolveMembersHeaders = new UpdateOrganizationTaskInvolveMembersHeaders();
        updateOrganizationTaskInvolveMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateOrganizationTaskInvolveMembersRequest updateOrganizationTaskInvolveMembersRequest = new UpdateOrganizationTaskInvolveMembersRequest()
                .setInvolveMembers(java.util.Arrays.asList(
                    "0715xxxx"
                ))
                .setAddInvolvers(java.util.Arrays.asList(
                    "0715xxxx"
                ))
                .setDelInvolvers(java.util.Arrays.asList(
                    "0715xxxx"
                ))
                .setDisableActivity(true)
                .setDisableNotification(true);
        try {
            client.updateOrganizationTaskInvolveMembersWithOptions("62a010c153c2ef52448xxxx", "0715xxxx", updateOrganizationTaskInvolveMembersRequest, updateOrganizationTaskInvolveMembersHeaders, new RuntimeOptions());
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
        update_organization_task_involve_members_headers = dingtalkproject__1__0_models.UpdateOrganizationTaskInvolveMembersHeaders()
        update_organization_task_involve_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_organization_task_involve_members_request = dingtalkproject__1__0_models.UpdateOrganizationTaskInvolveMembersRequest(
            involve_members=[
                '0715xxxx'
            ],
            add_involvers=[
                '0715xxxx'
            ],
            del_involvers=[
                '0715xxxx'
            ],
            disable_activity=True,
            disable_notification=True
        )
        try:
            client.update_organization_task_involve_members_with_options('62a010c153c2ef52448xxxx', '0715xxxx', update_organization_task_involve_members_request, update_organization_task_involve_members_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_organization_task_involve_members_headers = dingtalkproject__1__0_models.UpdateOrganizationTaskInvolveMembersHeaders()
        update_organization_task_involve_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_organization_task_involve_members_request = dingtalkproject__1__0_models.UpdateOrganizationTaskInvolveMembersRequest(
            involve_members=[
                '0715xxxx'
            ],
            add_involvers=[
                '0715xxxx'
            ],
            del_involvers=[
                '0715xxxx'
            ],
            disable_activity=True,
            disable_notification=True
        )
        try:
            await client.update_organization_task_involve_members_with_options_async('62a010c153c2ef52448xxxx', '0715xxxx', update_organization_task_involve_members_request, update_organization_task_involve_members_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\UpdateOrganizationTaskInvolveMembersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\UpdateOrganizationTaskInvolveMembersRequest;
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
        $updateOrganizationTaskInvolveMembersHeaders = new UpdateOrganizationTaskInvolveMembersHeaders([]);
        $updateOrganizationTaskInvolveMembersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateOrganizationTaskInvolveMembersRequest = new UpdateOrganizationTaskInvolveMembersRequest([
            "involveMembers" => [
                "0715xxxx"
            ],
            "addInvolvers" => [
                "0715xxxx"
            ],
            "delInvolvers" => [
                "0715xxxx"
            ],
            "disableActivity" => true,
            "disableNotification" => true
        ]);
        try {
            $client->updateOrganizationTaskInvolveMembersWithOptions("62a010c153c2ef52448xxxx", "0715xxxx", $updateOrganizationTaskInvolveMembersRequest, $updateOrganizationTaskInvolveMembersHeaders, new RuntimeOptions([]));
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

  updateOrganizationTaskInvolveMembersHeaders := &dingtalkproject_1_0.UpdateOrganizationTaskInvolveMembersHeaders{}
  updateOrganizationTaskInvolveMembersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateOrganizationTaskInvolveMembersRequest := &dingtalkproject_1_0.UpdateOrganizationTaskInvolveMembersRequest{
    InvolveMembers: []*string{tea.String("0715xxxx")},
    AddInvolvers: []*string{tea.String("0715xxxx")},
    DelInvolvers: []*string{tea.String("0715xxxx")},
    DisableActivity: tea.Bool(true),
    DisableNotification: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateOrganizationTaskInvolveMembersWithOptions(tea.String("62a010c153c2ef52448xxxx"), tea.String("0715xxxx"), updateOrganizationTaskInvolveMembersRequest, updateOrganizationTaskInvolveMembersHeaders, &util.RuntimeOptions{})
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
    let updateOrganizationTaskInvolveMembersHeaders = new $dingtalkproject_1_0.UpdateOrganizationTaskInvolveMembersHeaders({ });
    updateOrganizationTaskInvolveMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateOrganizationTaskInvolveMembersRequest = new $dingtalkproject_1_0.UpdateOrganizationTaskInvolveMembersRequest({
      involveMembers: [
        "0715xxxx"
      ],
      addInvolvers: [
        "0715xxxx"
      ],
      delInvolvers: [
        "0715xxxx"
      ],
      disableActivity: true,
      disableNotification: true,
    });
    try {
      await client.updateOrganizationTaskInvolveMembersWithOptions("62a010c153c2ef52448xxxx", "0715xxxx", updateOrganizationTaskInvolveMembersRequest, updateOrganizationTaskInvolveMembersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateOrganizationTaskInvolveMembersHeaders updateOrganizationTaskInvolveMembersHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateOrganizationTaskInvolveMembersHeaders();
            updateOrganizationTaskInvolveMembersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateOrganizationTaskInvolveMembersRequest updateOrganizationTaskInvolveMembersRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.UpdateOrganizationTaskInvolveMembersRequest
            {
                InvolveMembers = new List<string>
                {
                    "0715xxxx"
                },
                AddInvolvers = new List<string>
                {
                    "0715xxxx"
                },
                DelInvolvers = new List<string>
                {
                    "0715xxxx"
                },
                DisableActivity = true,
                DisableNotification = true,
            };
            try
            {
                client.UpdateOrganizationTaskInvolveMembersWithOptions("62a010c153c2ef52448xxxx", "0715xxxx", updateOrganizationTaskInvolveMembersRequest, updateOrganizationTaskInvolveMembersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| involvers | Array | 参与者userId列表。 |
| avatarUrl | String | 参与者头像。 |
| name | String | 参与者名字。 |
| userId | String | 参与者userId。 |
| updated | String | 更新参与者的时间，格式：YYYY-MM-DDTHH:mm:ssZ（ISO 8601/RFC 3339）。      转换成北京时间，需要在参数时间基础上加8小时。例如参数值为2022-06-20T00:00:00Z，表示的北京时间为2022-06-20 08:00:00。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "involvers" : [ {
      "avatarUrl" : "http://example.com",
      "name" : "小钉",
      "userId" : "0715xxxx"
    } ],
    "updated" : "2022-06-13T05:33:42.826Z"
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
