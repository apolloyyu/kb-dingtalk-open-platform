---
title: "获取指定宜搭角色的角色详情"
source_url: "https://open.dingtalk.com/document/development/get-roledetailbyid"
namespace: "development"
slug: "get-roledetailbyid"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 平台管理 > 获取指定宜搭角色的角色详情"
doc_id: "WbP6bwhqLH"
updated_at: "2026-06-15 10:49:28"
---

> Source: https://open.dingtalk.com/document/development/get-roledetailbyid
> Path: 应用开发 / 服务端 API / 宜搭 > 平台管理 > 获取指定宜搭角色的角色详情
> Updated: 2026-06-15 10:49:28

# 获取指定宜搭角色的角色详情

调用本接口，获取指定宜搭角色的角色详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/yida/forms/resources/roles |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Yida.PlatformResource.Read-宜搭平台资源读权限 |

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
| token | String | 是 | 验权token。  校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。  **[!NOTE]**  每个企业有自己的唯一code。 |

### **请求示例**

HTTP

```
GET /v2.0/yida/forms/resources/roles?pageSize=1&pageNumber=10&roleUuid=ROLE-71xxxx31f42&corpId=dingxxxx&userId=manager123&token=IASUDYxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json
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
        com.aliyun.dingtalkyida_2_0.models.GetRoleDetailByIdHeaders getRoleDetailByIdHeaders = new com.aliyun.dingtalkyida_2_0.models.GetRoleDetailByIdHeaders();
        getRoleDetailByIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkyida_2_0.models.GetRoleDetailByIdRequest getRoleDetailByIdRequest = new com.aliyun.dingtalkyida_2_0.models.GetRoleDetailByIdRequest();
        try {
            client.getRoleDetailByIdWithOptions(getRoleDetailByIdRequest, getRoleDetailByIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_role_detail_by_id_headers = dingtalkyida__2__0_models.GetRoleDetailByIdHeaders()
        get_role_detail_by_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_role_detail_by_id_request = dingtalkyida__2__0_models.GetRoleDetailByIdRequest()
        try:
            client.get_role_detail_by_id_with_options(get_role_detail_by_id_request, get_role_detail_by_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_role_detail_by_id_headers = dingtalkyida__2__0_models.GetRoleDetailByIdHeaders()
        get_role_detail_by_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_role_detail_by_id_request = dingtalkyida__2__0_models.GetRoleDetailByIdRequest()
        try:
            await client.get_role_detail_by_id_with_options_async(get_role_detail_by_id_request, get_role_detail_by_id_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\GetRoleDetailByIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\GetRoleDetailByIdRequest;
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
        $getRoleDetailByIdHeaders = new GetRoleDetailByIdHeaders([]);
        $getRoleDetailByIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getRoleDetailByIdRequest = new GetRoleDetailByIdRequest([]);
        try {
            $client->getRoleDetailByIdWithOptions($getRoleDetailByIdRequest, $getRoleDetailByIdHeaders, new RuntimeOptions([]));
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

  getRoleDetailByIdHeaders := &dingtalkyida_2_0.GetRoleDetailByIdHeaders{}
  getRoleDetailByIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getRoleDetailByIdRequest := &dingtalkyida_2_0.GetRoleDetailByIdRequest{}
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetRoleDetailByIdWithOptions(getRoleDetailByIdRequest, getRoleDetailByIdHeaders, &util.RuntimeOptions{})
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
    let getRoleDetailByIdHeaders = new dingtalkyida_2_0.GetRoleDetailByIdHeaders({ });
    getRoleDetailByIdHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getRoleDetailByIdRequest = new dingtalkyida_2_0.GetRoleDetailByIdRequest({ });
    try {
      await client.getRoleDetailByIdWithOptions(getRoleDetailByIdRequest, getRoleDetailByIdHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetRoleDetailByIdHeaders getRoleDetailByIdHeaders = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetRoleDetailByIdHeaders();
            getRoleDetailByIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetRoleDetailByIdRequest getRoleDetailByIdRequest = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetRoleDetailByIdRequest();
            try
            {
                client.GetRoleDetailByIdWithOptions(getRoleDetailByIdRequest, getRoleDetailByIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| roleUuid | String | 角色唯一标识。 |
| parentUuid | String | 角色所属分组唯一标识。 |
| name | String | 角色名称。 |
| description | String | 角色描述。 |
| memberTotalCount | Integer | 角色内成员总数。 |
| canModifyOwners | Any | 角色管理员。 |
| members | Object | 角色成员列表详情信息。 |
| currentPage | Integer | 分页页码。 |
| totalCount | Integer | 角色内成员总数。 |
| data | Any | 成员主数据。 |
| success | Boolean | 是否成功。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "roleUuid" : "ROLE-71xxxx5506e31f42",
    "parentUuid" : "GROUP-f5xxxx46a38",
    "name" : "角色名称",
    "description" : "角色描述",
    "memberTotalCount" : 100,
    "canModifyOwners" : "manager123",
    "members" : {
      "currentPage" : 1,
      "totalCount" : 100,
      "data" : "成员主数据"
    }
  },
  "success" : true
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
