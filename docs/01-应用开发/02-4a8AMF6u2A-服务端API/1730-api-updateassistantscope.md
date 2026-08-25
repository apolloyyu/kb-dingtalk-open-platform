---
title: "更新 AI 助理的使用范围"
source_url: "https://open.dingtalk.com/document/development/api-updateassistantscope"
namespace: "development"
slug: "api-updateassistantscope"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 助理管理 > 更新 AI 助理的使用范围"
doc_id: "fpBwuMw45Y"
updated_at: "2026-03-06 09:22:52"
---

> Source: https://open.dingtalk.com/document/development/api-updateassistantscope
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 助理管理 > 更新 AI 助理的使用范围
> Updated: 2026-03-06 09:22:52

# 更新 AI 助理的使用范围

调用本接口，更新 AI 助理的使用范围，包括开启分享和关闭分享等能力。

> **[!IMPORTANT]**
>
> 本文档已于 2026年 03 月 05 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
PUT /v1.0/assistant/scope HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "operatorUnionId" : "String",
  "assistantId" : "String",
  "sharing" : Boolean,
  "scopes" : {
    "deptVisibleScopes" : [ "String" ],
    "userVisibleScopes" : [ "String" ],
    "roleVisibleScopes" : [ "String" ],
    "dynamicGroupScopes" : [ "String" ],
    "isAdmin" : Boolean
  }
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUnionId | String | 是 | 操作者用户 ID（Union ID）。 |
| assistantId | String | 是 | AI 助理唯一标识符。 |
| sharing | Boolean | 否 | 是否开启分享：   - true：开启 - false：关闭， - null ：不做任何处理 |
| scopes | Object | 否 | 助理可见范围参数。 |
| deptVisibleScopes | Array of String | 否 | 部门 ID。 |
| userVisibleScopes | Array of String | 否 | 用户 ID。 |
| roleVisibleScopes | Array of String | 否 | 角色 ID。 |
| dynamicGroupScopes | Array of String | 否 | 动态用户组 ID。 |
| isAdmin | Boolean | 否 | 是否仅管理员可见：   - true：是 - false：否 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
|  | Any | 接口响应信息，可通过 HTTP 状态码判断是否成功。 |

## 示例

**请求示例**

HTTP

```
PUT /v1.0/assistant/scope HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:17c***209
Content-Type:application/json

{
  "operatorUnionId" : "H20***wiE",
  "assistantId" : "5eb***296",
  "sharing" : true,
  "scopes" : {
    "deptVisibleScopes" : [ "232***321" ],
    "userVisibleScopes" : [ "Ded***HWs" ],
    "roleVisibleScopes" : [ "381***513" ],
    "dynamicGroupScopes" : [ "735***123" ],
    "isAdmin" : false
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
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkassistant_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkassistant_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkassistant_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkassistant_1_0.models.UpdateAssistantScopeHeaders updateAssistantScopeHeaders = new com.aliyun.dingtalkassistant_1_0.models.UpdateAssistantScopeHeaders();
        updateAssistantScopeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkassistant_1_0.models.UpdateAssistantScopeRequest.UpdateAssistantScopeRequestScopes scopes = new com.aliyun.dingtalkassistant_1_0.models.UpdateAssistantScopeRequest.UpdateAssistantScopeRequestScopes()
                .setDeptVisibleScopes(java.util.Arrays.asList(
                    "232***321"
                ))
                .setUserVisibleScopes(java.util.Arrays.asList(
                    "Ded***HWs"
                ))
                .setRoleVisibleScopes(java.util.Arrays.asList(
                    "381***513"
                ))
                .setDynamicGroupScopes(java.util.Arrays.asList(
                    "735***123"
                ))
                .setIsAdmin(false);
        com.aliyun.dingtalkassistant_1_0.models.UpdateAssistantScopeRequest updateAssistantScopeRequest = new com.aliyun.dingtalkassistant_1_0.models.UpdateAssistantScopeRequest()
                .setOperatorUnionId("H20***wiE")
                .setAssistantId("5eb***296")
                .setSharing(true)
                .setScopes(scopes);
        try {
            client.updateAssistantScopeWithOptions(updateAssistantScopeRequest, updateAssistantScopeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.assistant_1_0.client import Client as dingtalkassistant_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.assistant_1_0 import models as dingtalkassistant__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkassistant_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkassistant_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_assistant_scope_headers = dingtalkassistant__1__0_models.UpdateAssistantScopeHeaders()
        update_assistant_scope_headers.x_acs_dingtalk_access_token = '<your access token>'
        scopes = dingtalkassistant__1__0_models.UpdateAssistantScopeRequestScopes(
            dept_visible_scopes=[
                '232***321'
            ],
            user_visible_scopes=[
                'Ded***HWs'
            ],
            role_visible_scopes=[
                '381***513'
            ],
            dynamic_group_scopes=[
                '735***123'
            ],
            is_admin=False
        )
        update_assistant_scope_request = dingtalkassistant__1__0_models.UpdateAssistantScopeRequest(
            operator_union_id='H20***wiE',
            assistant_id='5eb***296',
            sharing=True,
            scopes=scopes
        )
        try:
            client.update_assistant_scope_with_options(update_assistant_scope_request, update_assistant_scope_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_assistant_scope_headers = dingtalkassistant__1__0_models.UpdateAssistantScopeHeaders()
        update_assistant_scope_headers.x_acs_dingtalk_access_token = '<your access token>'
        scopes = dingtalkassistant__1__0_models.UpdateAssistantScopeRequestScopes(
            dept_visible_scopes=[
                '232***321'
            ],
            user_visible_scopes=[
                'Ded***HWs'
            ],
            role_visible_scopes=[
                '381***513'
            ],
            dynamic_group_scopes=[
                '735***123'
            ],
            is_admin=False
        )
        update_assistant_scope_request = dingtalkassistant__1__0_models.UpdateAssistantScopeRequest(
            operator_union_id='H20***wiE',
            assistant_id='5eb***296',
            sharing=True,
            scopes=scopes
        )
        try:
            await client.update_assistant_scope_with_options_async(update_assistant_scope_request, update_assistant_scope_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\UpdateAssistantScopeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\UpdateAssistantScopeRequest\scopes;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\UpdateAssistantScopeRequest;
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
        $updateAssistantScopeHeaders = new UpdateAssistantScopeHeaders([]);
        $updateAssistantScopeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $scopes = new scopes([
            "deptVisibleScopes" => [
                "232***321"
            ],
            "userVisibleScopes" => [
                "Ded***HWs"
            ],
            "roleVisibleScopes" => [
                "381***513"
            ],
            "dynamicGroupScopes" => [
                "735***123"
            ],
            "isAdmin" => false
        ]);
        $updateAssistantScopeRequest = new UpdateAssistantScopeRequest([
            "operatorUnionId" => "H20***wiE",
            "assistantId" => "5eb***296",
            "sharing" => true,
            "scopes" => $scopes
        ]);
        try {
            $client->updateAssistantScopeWithOptions($updateAssistantScopeRequest, $updateAssistantScopeHeaders, new RuntimeOptions([]));
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
  dingtalkassistant_1_0  "github.com/alibabacloud-go/dingtalk/assistant_1_0"
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
func CreateClient () (_result *dingtalkassistant_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkassistant_1_0.Client{}
  _result, _err = dingtalkassistant_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateAssistantScopeHeaders := &dingtalkassistant_1_0.UpdateAssistantScopeHeaders{}
  updateAssistantScopeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  scopes := &dingtalkassistant_1_0.UpdateAssistantScopeRequestScopes{
    DeptVisibleScopes: []*string{tea.String("232***321")},
    UserVisibleScopes: []*string{tea.String("Ded***HWs")},
    RoleVisibleScopes: []*string{tea.String("381***513")},
    DynamicGroupScopes: []*string{tea.String("735***123")},
    IsAdmin: tea.Bool(false),
  }
  updateAssistantScopeRequest := &dingtalkassistant_1_0.UpdateAssistantScopeRequest{
    OperatorUnionId: tea.String("H20***wiE"),
    AssistantId: tea.String("5eb***296"),
    Sharing: tea.Bool(true),
    Scopes: scopes,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateAssistantScopeWithOptions(updateAssistantScopeRequest, updateAssistantScopeHeaders, &util.RuntimeOptions{})
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
const dingtalkassistant_1_0 = require('@alicloud/dingtalk/assistant_1_0');
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
    return new dingtalkassistant_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateAssistantScopeHeaders = new dingtalkassistant_1_0.UpdateAssistantScopeHeaders({ });
    updateAssistantScopeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let scopes = new dingtalkassistant_1_0.UpdateAssistantScopeRequestScopes({
      deptVisibleScopes: [
        '232***321'
      ],
      userVisibleScopes: [
        'Ded***HWs'
      ],
      roleVisibleScopes: [
        '381***513'
      ],
      dynamicGroupScopes: [
        '735***123'
      ],
      isAdmin: false,
    });
    let updateAssistantScopeRequest = new dingtalkassistant_1_0.UpdateAssistantScopeRequest({
      operatorUnionId: 'H20***wiE',
      assistantId: '5eb***296',
      sharing: true,
      scopes: scopes,
    });
    try {
      await client.updateAssistantScopeWithOptions(updateAssistantScopeRequest, updateAssistantScopeHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkassistant_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkassistant_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.UpdateAssistantScopeHeaders updateAssistantScopeHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.UpdateAssistantScopeHeaders();
            updateAssistantScopeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.UpdateAssistantScopeRequest.UpdateAssistantScopeRequestScopes scopes = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.UpdateAssistantScopeRequest.UpdateAssistantScopeRequestScopes
            {
                DeptVisibleScopes = new List<string>
                {
                    "232***321"
                },
                UserVisibleScopes = new List<string>
                {
                    "Ded***HWs"
                },
                RoleVisibleScopes = new List<string>
                {
                    "381***513"
                },
                DynamicGroupScopes = new List<string>
                {
                    "735***123"
                },
                IsAdmin = false,
            };
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.UpdateAssistantScopeRequest updateAssistantScopeRequest = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.UpdateAssistantScopeRequest
            {
                OperatorUnionId = "H20***wiE",
                AssistantId = "5eb***296",
                Sharing = true,
                Scopes = scopes,
            };
            try
            {
                client.UpdateAssistantScopeWithOptions(updateAssistantScopeRequest, updateAssistantScopeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.parameter | 参数错误 | 参数错误 |
| 400 | assistant.not.exist | AI助理不存在 | AI助理不存在 |
| 500 | system.error | 系统异常 | 系统异常 |
