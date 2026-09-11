---
title: "更新企业内部应用的可使用范围"
source_url: "https://open.dingtalk.com/document/development/update-the-visible-range-of-micro-applications"
namespace: "development"
slug: "update-the-visible-range-of-micro-applications"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 使用范围 > 更新企业内部应用的可使用范围"
doc_id: "XiNPty8ODR"
updated_at: "2026-07-14 09:22:23"
---

> Source: https://open.dingtalk.com/document/development/update-the-visible-range-of-micro-applications
> Path: 应用开发 / 服务端 API / 钉钉应用 > 使用范围 > 更新企业内部应用的可使用范围
> Updated: 2026-07-14 09:22:23

# 更新企业内部应用的可使用范围

通过此接口，可更新企业内部应用的可使用范围，实现对用户、部门和角色的灵活权限管理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/apps/{agentId}/scopes |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-管理微应用的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | Long | 是 | 应用agentId，参考[AgentId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ef841f7f37kba)。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| addUserIds | Array of String | 否 | 待添加的用户userId列表，最大长度100。      添加后总用户数不得超过2000，否则将返回错误。 |
| delUserIds | Array of String | 否 | 删除的可使用用户userId列表，最大长度100。 |
| addDeptIds | Array of Long | 否 | 待添加的部门ID列表，最大长度100。      添加后总部门数不得超过2000，否则将返回错误。 |
| delDeptIds | Array of Long | 否 | 待删除的部门ID列表，最大长度100。 |
| addRoleIds | Array of Long | 否 | 待添加的角色ID列表，最大长度100。可通过[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取具体ID值。      添加后总角色数不得超过2000，否则接口会报错。 |
| delRoleIds | Array of Long | 否 | 删除的可使用角色列表，最大长度100。可通过[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取id参数值。 |
| onlyAdminVisible | Boolean | 否 | 是否仅管理员可使用。   - **true**： 是 - **false**：否 |

### 请求示例

HTTP

```
POST /v1.0/microApp/apps/111/scopes HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "addUserIds" : [ "manager123" ],
  "delUserIds" : [ "manager123" ],
  "addDeptIds" : [ 1 ],
  "delDeptIds" : [ 1 ],
  "addRoleIds" : [ 2 ],
  "delRoleIds" : [ 2 ],
  "onlyAdminVisible" : true
}
```

Java

```
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.SetMicroAppScopeHeaders setMicroAppScopeHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.SetMicroAppScopeHeaders();
        setMicroAppScopeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.SetMicroAppScopeRequest setMicroAppScopeRequest = new com.aliyun.dingtalkmicro_app_1_0.models.SetMicroAppScopeRequest()
                .setAddUserIds(java.util.Arrays.asList(
                    "manager123"
                ))
                .setDelUserIds(java.util.Arrays.asList(
                    "manager123"
                ))
                .setAddDeptIds(java.util.Arrays.asList(
                    1L
                ))
                .setDelDeptIds(java.util.Arrays.asList(
                    1L
                ))
                .setAddRoleIds(java.util.Arrays.asList(
                    2L
                ))
                .setDelRoleIds(java.util.Arrays.asList(
                    2L
                ))
                .setOnlyAdminVisible(true);
        try {
            client.setMicroAppScopeWithOptions("111", setMicroAppScopeRequest, setMicroAppScopeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.micro_app_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmicroApp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmicroApp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        set_micro_app_scope_headers = dingtalkmicro_app__1__0_models.SetMicroAppScopeHeaders()
        set_micro_app_scope_headers.x_acs_dingtalk_access_token = '<your access token>'
        set_micro_app_scope_request = dingtalkmicro_app__1__0_models.SetMicroAppScopeRequest(
            add_user_ids=[
                'manager123'
            ],
            del_user_ids=[
                'manager123'
            ],
            add_dept_ids=[
                1
            ],
            del_dept_ids=[
                1
            ],
            add_role_ids=[
                2
            ],
            del_role_ids=[
                2
            ],
            only_admin_visible=True
        )
        try:
            client.set_micro_app_scope_with_options('111', set_micro_app_scope_request, set_micro_app_scope_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        set_micro_app_scope_headers = dingtalkmicro_app__1__0_models.SetMicroAppScopeHeaders()
        set_micro_app_scope_headers.x_acs_dingtalk_access_token = '<your access token>'
        set_micro_app_scope_request = dingtalkmicro_app__1__0_models.SetMicroAppScopeRequest(
            add_user_ids=[
                'manager123'
            ],
            del_user_ids=[
                'manager123'
            ],
            add_dept_ids=[
                1
            ],
            del_dept_ids=[
                1
            ],
            add_role_ids=[
                2
            ],
            del_role_ids=[
                2
            ],
            only_admin_visible=True
        )
        try:
            await client.set_micro_app_scope_with_options_async('111', set_micro_app_scope_request, set_micro_app_scope_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\SetMicroAppScopeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\SetMicroAppScopeRequest;
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
        $setMicroAppScopeHeaders = new SetMicroAppScopeHeaders([]);
        $setMicroAppScopeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $setMicroAppScopeRequest = new SetMicroAppScopeRequest([
            "addUserIds" => [
                "manager123"
            ],
            "delUserIds" => [
                "manager123"
            ],
            "addDeptIds" => [
                1
            ],
            "delDeptIds" => [
                1
            ],
            "addRoleIds" => [
                2
            ],
            "delRoleIds" => [
                2
            ],
            "onlyAdminVisible" => true
        ]);
        try {
            $client->setMicroAppScopeWithOptions("111", $setMicroAppScopeRequest, $setMicroAppScopeHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
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
func CreateClient () (_result *dingtalkmicroapp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmicroapp_1_0.Client{}
  _result, _err = dingtalkmicroapp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  setMicroAppScopeHeaders := &dingtalkmicroapp_1_0.SetMicroAppScopeHeaders{}
  setMicroAppScopeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  setMicroAppScopeRequest := &dingtalkmicroapp_1_0.SetMicroAppScopeRequest{
    AddUserIds: []*string{tea.String("manager123")},
    DelUserIds: []*string{tea.String("manager123")},
    AddDeptIds: []*int64{tea.Int64(1)},
    DelDeptIds: []*int64{tea.Int64(1)},
    AddRoleIds: []*int64{tea.Int64(2)},
    DelRoleIds: []*int64{tea.Int64(2)},
    OnlyAdminVisible: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SetMicroAppScopeWithOptions(tea.String("111"), setMicroAppScopeRequest, setMicroAppScopeHeaders, &util.RuntimeOptions{})
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
const dingtalkmicroApp_1_0 = require('@alicloud/dingtalk/microApp_1_0');
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
    return new dingtalkmicroApp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let setMicroAppScopeHeaders = new dingtalkmicroApp_1_0.SetMicroAppScopeHeaders({ });
    setMicroAppScopeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let setMicroAppScopeRequest = new dingtalkmicroApp_1_0.SetMicroAppScopeRequest({
      addUserIds: [
        'manager123'
      ],
      delUserIds: [
        'manager123'
      ],
      addDeptIds: [
        1
      ],
      delDeptIds: [
        1
      ],
      addRoleIds: [
        2
      ],
      delRoleIds: [
        2
      ],
      onlyAdminVisible: true,
    });
    try {
      await client.setMicroAppScopeWithOptions('111', setMicroAppScopeRequest, setMicroAppScopeHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SetMicroAppScopeHeaders setMicroAppScopeHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SetMicroAppScopeHeaders();
            setMicroAppScopeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SetMicroAppScopeRequest setMicroAppScopeRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SetMicroAppScopeRequest
            {
                AddUserIds = new List<string>
                {
                    "manager123"
                },
                DelUserIds = new List<string>
                {
                    "manager123"
                },
                AddDeptIds = new List<long?>
                {
                    1
                },
                DelDeptIds = new List<long?>
                {
                    1
                },
                AddRoleIds = new List<long?>
                {
                    2
                },
                DelRoleIds = new List<long?>
                {
                    2
                },
                OnlyAdminVisible = true,
            };
            try
            {
                client.SetMicroAppScopeWithOptions("111", setMicroAppScopeRequest, setMicroAppScopeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否更新成功，true表示更新成功。 |

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
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 500 | systemError | 系统繁忙 | 系统繁忙 |
