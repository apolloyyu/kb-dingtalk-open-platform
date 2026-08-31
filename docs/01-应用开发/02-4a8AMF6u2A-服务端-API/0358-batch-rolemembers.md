---
title: "批量更新宜搭角色成员"
source_url: "https://open.dingtalk.com/document/development/batch-rolemembers"
namespace: "development"
slug: "batch-rolemembers"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 平台管理 > 批量更新宜搭角色成员"
doc_id: "y9m8nhOqfC"
updated_at: "2026-06-15 10:47:32"
---

> Source: https://open.dingtalk.com/document/development/batch-rolemembers
> Path: 应用开发 / 服务端 API / 宜搭 > 平台管理 > 批量更新宜搭角色成员
> Updated: 2026-06-15 10:47:32

# 批量更新宜搭角色成员

调用本接口，根据角色uuid批量新增或更新宜搭角色成员（可同时指定成员的角色管理范围）

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/yida/forms/resources/roles/upsert |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Yida.PlatformResource.Write-宜搭平台资源写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageSize | Integer | 否 | 分页大小。 |
| pageNumber | Integer | 否 | 分页页码。 |
| roleUuid | String | 是 | 角色唯一标识，获取方式：平台管理-角色管理-宜搭角色-角色ID。 |
| corpId | String | 是 | 组织的corpId。 |
| userId | String | 是 | 用户的userid。 |
| token | String | 是 | 验权token。  校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。  **[!NOTE]**    每个企业有自己的唯一code。 |
| membersInfo | String | 是 | memberId为新增或者更新的userId  manageScopes为管理范围，其中all代表管理范围为「所有人」。 |

### **请求示例**

HTTP

```
POST /v2.0/yida/forms/resources/roles/upsert HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "pageSize" : 10,
  "pageNumber" : 1,
  "roleUuid" : "ROLE-71dcxxxx31f42",
  "corpId" : "dingxxxx",
  "userId" : "manager123",
  "token" : "IASUDYxxx",
  "membersInfo" : "[{\"memberId\":\"5014533041684xx\",\"manageScopes\":\"8360866xx,430181xx,429821xx\"},{\"memberId\":\"014329103xx\",\"manageScopes\":\"all\"}]"
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
    public static com.aliyun.dingtalkyida_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkyida_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkyida_2_0.models.BatchAddOrUpdateRoleMembersHeaders batchAddOrUpdateRoleMembersHeaders = new com.aliyun.dingtalkyida_2_0.models.BatchAddOrUpdateRoleMembersHeaders();
        batchAddOrUpdateRoleMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkyida_2_0.models.BatchAddOrUpdateRoleMembersRequest batchAddOrUpdateRoleMembersRequest = new com.aliyun.dingtalkyida_2_0.models.BatchAddOrUpdateRoleMembersRequest();
        try {
            client.batchAddOrUpdateRoleMembersWithOptions(batchAddOrUpdateRoleMembersRequest, batchAddOrUpdateRoleMembersHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.yida_2_0.client import Client as dingtalkyida_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_2_0 import models as dingtalkyida__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_add_or_update_role_members_headers = dingtalkyida__2__0_models.BatchAddOrUpdateRoleMembersHeaders()
        batch_add_or_update_role_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_add_or_update_role_members_request = dingtalkyida__2__0_models.BatchAddOrUpdateRoleMembersRequest()
        try:
            client.batch_add_or_update_role_members_with_options(batch_add_or_update_role_members_request, batch_add_or_update_role_members_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_add_or_update_role_members_headers = dingtalkyida__2__0_models.BatchAddOrUpdateRoleMembersHeaders()
        batch_add_or_update_role_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_add_or_update_role_members_request = dingtalkyida__2__0_models.BatchAddOrUpdateRoleMembersRequest()
        try:
            await client.batch_add_or_update_role_members_with_options_async(batch_add_or_update_role_members_request, batch_add_or_update_role_members_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\BatchAddOrUpdateRoleMembersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\BatchAddOrUpdateRoleMembersRequest;
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
        $batchAddOrUpdateRoleMembersHeaders = new BatchAddOrUpdateRoleMembersHeaders([]);
        $batchAddOrUpdateRoleMembersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchAddOrUpdateRoleMembersRequest = new BatchAddOrUpdateRoleMembersRequest([]);
        try {
            $client->batchAddOrUpdateRoleMembersWithOptions($batchAddOrUpdateRoleMembersRequest, $batchAddOrUpdateRoleMembersHeaders, new RuntimeOptions([]));
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
  dingtalkyida_2_0  "github.com/alibabacloud-go/dingtalk/yida_2_0"
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
func CreateClient () (_result *dingtalkyida_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_2_0.Client{}
  _result, _err = dingtalkyida_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchAddOrUpdateRoleMembersHeaders := &dingtalkyida_2_0.BatchAddOrUpdateRoleMembersHeaders{}
  batchAddOrUpdateRoleMembersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchAddOrUpdateRoleMembersRequest := &dingtalkyida_2_0.BatchAddOrUpdateRoleMembersRequest{}
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchAddOrUpdateRoleMembersWithOptions(batchAddOrUpdateRoleMembersRequest, batchAddOrUpdateRoleMembersHeaders, &util.RuntimeOptions{})
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
const dingtalkyida_2_0 = require('@alicloud/dingtalk/yida_2_0');
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
    return new dingtalkyida_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let batchAddOrUpdateRoleMembersHeaders = new dingtalkyida_2_0.BatchAddOrUpdateRoleMembersHeaders({ });
    batchAddOrUpdateRoleMembersHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let batchAddOrUpdateRoleMembersRequest = new dingtalkyida_2_0.BatchAddOrUpdateRoleMembersRequest({ });
    try {
      await client.batchAddOrUpdateRoleMembersWithOptions(batchAddOrUpdateRoleMembersRequest, batchAddOrUpdateRoleMembersHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.BatchAddOrUpdateRoleMembersHeaders batchAddOrUpdateRoleMembersHeaders = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.BatchAddOrUpdateRoleMembersHeaders();
            batchAddOrUpdateRoleMembersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.BatchAddOrUpdateRoleMembersRequest batchAddOrUpdateRoleMembersRequest = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.BatchAddOrUpdateRoleMembersRequest();
            try
            {
                client.BatchAddOrUpdateRoleMembersWithOptions(batchAddOrUpdateRoleMembersRequest, batchAddOrUpdateRoleMembersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 返回结果。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": "1734xxxxxxe08500e",
  "request_id": "5kaikoe9uc8i"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | invalidState.role.roleNotExist | 角色不存在:%s | 角色不存在 |
| 500 | unclassifiedError | 宜搭未分类的异常信息:%s | 宜搭未分类的异常信息 |
| 500 | failure.user.userNotExist | 用户不存在:%s | 用户不存在 |
| 500 | invalidParameter.corp.corpNotExist | 企业不存在:%s | 企业不存在 |
| 500 | invalidState.authorization.invalidAuthorizationInformation | 无效的认证信息:%s | 无效的认证信息 |
| 500 | failure.operation.tooManyVisitors | 平台当前访问人数过多，请稍后重试:%s | 平台当前访问人数过多，请稍后重试 |
| 500 | invalidParameter.validation.parameterValidationFailed | 参数校验失败:%s | 参数校验失败 |
| 500 | noPermission.permission.deny | 没有权限:%s | 没有权限 |
