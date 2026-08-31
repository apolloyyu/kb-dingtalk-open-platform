---
title: "创建访问控制"
source_url: "https://open.dingtalk.com/document/development/create-schedule-access-control"
namespace: "development"
slug: "create-schedule-access-control"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 用户访问控制 > 创建访问控制"
doc_id: "TrKLkcZ1BY"
updated_at: "2026-06-02 09:24:54"
---

> Source: https://open.dingtalk.com/document/development/create-schedule-access-control
> Path: 应用开发 / 服务端 API / 日程 > 用户访问控制 > 创建访问控制
> Updated: 2026-06-02 09:24:54

# 创建访问控制

调用本接口，可以给指定日历添加访问控制。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/acls |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Acl.Write-日历应用访问控制写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 日程组织者的unionId。   - 企业内部应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，通过[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历ID，统一为primary，表示用户的主日历。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| privilege | String | 是 | 权限信息，取值：   - **free\_busy\_reader**：查看忙闲 - **title\_reader**：查看标题 - **reader**：查看详情 - **writer**：创建和编辑 |
| sendMsg | Boolean | 是 | 是否向授权人发消息。   - **true**：发 - **false**：不发 |
| scope | Object | 是 | 权限范围。 |
| scopeType | String | 是 | 权限类型，目前只支持**user**表示用户。 |
| userId | String | 是 | 用户ID。当**scopeType**取值为**user**时，传入用户的**unionId**。  **[!NOTE]**  单人最多添加500个共享人 。 |

### 请求示例

HTTP

```
POST /v1.0/calendar/users/U5KXX3QjgiG/calendars/primary/acls HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dd438xxx
Content-Type:application/json

{
  "privilege" : "reader",
  "sendMsg" : true,
  "scope" : {
    "scopeType" : "user",
    "userId" : "U5KXX3QjgiG"
  }
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
    public static com.aliyun.dingtalkcalendar_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcalendar_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcalendar_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcalendar_1_0.models.CreateAclsHeaders createAclsHeaders = new com.aliyun.dingtalkcalendar_1_0.models.CreateAclsHeaders();
        createAclsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcalendar_1_0.models.CreateAclsRequest.CreateAclsRequestScope scope = new com.aliyun.dingtalkcalendar_1_0.models.CreateAclsRequest.CreateAclsRequestScope()
                .setScopeType("user");
        com.aliyun.dingtalkcalendar_1_0.models.CreateAclsRequest createAclsRequest = new com.aliyun.dingtalkcalendar_1_0.models.CreateAclsRequest()
                .setPrivilege("reader")
                .setSendMsg(true)
                .setScope(scope);
        try {
            client.createAclsWithOptions("U5KXX3QjgiG", "primary", createAclsRequest, createAclsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.calendar_1_0.client import Client as dingtalkcalendar_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.calendar_1_0 import models as dingtalkcalendar__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcalendar_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcalendar_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_acls_headers = dingtalkcalendar__1__0_models.CreateAclsHeaders()
        create_acls_headers.x_acs_dingtalk_access_token = '<your access token>'
        scope = dingtalkcalendar__1__0_models.CreateAclsRequestScope(
            scope_type='user'
        )
        create_acls_request = dingtalkcalendar__1__0_models.CreateAclsRequest(
            privilege='reader',
            send_msg=True,
            scope=scope
        )
        try:
            client.create_acls_with_options('U5KXX3QjgiG', 'primary', create_acls_request, create_acls_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_acls_headers = dingtalkcalendar__1__0_models.CreateAclsHeaders()
        create_acls_headers.x_acs_dingtalk_access_token = '<your access token>'
        scope = dingtalkcalendar__1__0_models.CreateAclsRequestScope(
            scope_type='user'
        )
        create_acls_request = dingtalkcalendar__1__0_models.CreateAclsRequest(
            privilege='reader',
            send_msg=True,
            scope=scope
        )
        try:
            await client.create_acls_with_options_async('U5KXX3QjgiG', 'primary', create_acls_request, create_acls_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateAclsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateAclsRequest\scope;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\CreateAclsRequest;
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
        $createAclsHeaders = new CreateAclsHeaders([]);
        $createAclsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $scope = new scope([
            "scopeType" => "user"
        ]);
        $createAclsRequest = new CreateAclsRequest([
            "privilege" => "reader",
            "sendMsg" => true,
            "scope" => $scope
        ]);
        try {
            $client->createAclsWithOptions("U5KXX3QjgiG", "primary", $createAclsRequest, $createAclsHeaders, new RuntimeOptions([]));
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
  dingtalkcalendar_1_0  "github.com/alibabacloud-go/dingtalk/calendar_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcalendar_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcalendar_1_0.Client{}
  _result, _err = dingtalkcalendar_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createAclsHeaders := &dingtalkcalendar_1_0.CreateAclsHeaders{}
  createAclsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  scope := &dingtalkcalendar_1_0.CreateAclsRequestScope{
    ScopeType: tea.String("user"),
  }
  createAclsRequest := &dingtalkcalendar_1_0.CreateAclsRequest{
    Privilege: tea.String("reader"),
    SendMsg: tea.Bool(true),
    Scope: scope,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateAclsWithOptions(tea.String("U5KXX3QjgiG"), tea.String("primary"), createAclsRequest, createAclsHeaders, &util.RuntimeOptions{})
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
import dingtalkcalendar_1_0, * as $dingtalkcalendar_1_0 from '@alicloud/dingtalk/calendar_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcalendar_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcalendar_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createAclsHeaders = new $dingtalkcalendar_1_0.CreateAclsHeaders({ });
    createAclsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let scope = new $dingtalkcalendar_1_0.CreateAclsRequestScope({
      scopeType: "user",
    });
    let createAclsRequest = new $dingtalkcalendar_1_0.CreateAclsRequest({
      privilege: "reader",
      sendMsg: true,
      scope: scope,
    });
    try {
      await client.createAclsWithOptions("U5KXX3QjgiG", "primary", createAclsRequest, createAclsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateAclsHeaders createAclsHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateAclsHeaders();
            createAclsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateAclsRequest.CreateAclsRequestScope scope = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateAclsRequest.CreateAclsRequestScope
            {
                ScopeType = "user",
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateAclsRequest createAclsRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.CreateAclsRequest
            {
                Privilege = "reader",
                SendMsg = true,
                Scope = scope,
            };
            try
            {
                client.CreateAclsWithOptions("U5KXX3QjgiG", "primary", createAclsRequest, createAclsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| privilege | String | 权限信息，取值：   - **free\_busy\_reader**：查看忙闲 - **title\_reader**：查看标题 - **reader**：查看详情 - **writer**：创建和编辑 |
| aclId | String | 权限资源ID。 |
| scope | Object | 权限范围。 |
| scopeType | String | 权限类型，目前只支持**user**表示用户。 |
| userId | String | 用户ID。  当**scopeType**取值为**user**时，值为用户的**unionId**。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "privilege" : "reader",
  "aclId" : "VS4yJgnNiiiSRmsqKttYXXXXXX",
  "scope" : {
    "scopeType" : "user",
    "userId" : "U5KXX3QjgiG"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | shareExceedLimit | 共享人数超过上限 |
