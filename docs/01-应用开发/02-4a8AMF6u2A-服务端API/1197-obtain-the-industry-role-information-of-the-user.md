---
title: "获取用户所在的行业角色信息"
source_url: "https://open.dingtalk.com/document/development/obtain-the-industry-role-information-of-the-user"
namespace: "development"
slug: "obtain-the-industry-role-information-of-the-user"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 行业角色管理 > 获取用户所在的行业角色信息"
doc_id: "xQoGxEOxs7"
updated_at: "2025-09-23 19:23:34"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-industry-role-information-of-the-user
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 行业角色管理 > 获取用户所在的行业角色信息
> Updated: 2025-09-23 19:23:34

# 获取用户所在的行业角色信息

根据用户userId，获取员工所在的角色信息，如角色名称、角色编码和角色ID。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/resident/users/industryRoles |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Village.Contact.Read-数字区县居民通讯录读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户userId，可通过调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/resident/users/industryRoles?userId=12345 HTTP/1.1
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
import com.aliyun.dingtalkresident_1_0.*;
import com.aliyun.dingtalkresident_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkresident_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkresident_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkresident_1_0.Client client = Sample.createClient();
        ListUserIndustryRolesHeaders listUserIndustryRolesHeaders = new ListUserIndustryRolesHeaders();
        listUserIndustryRolesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListUserIndustryRolesRequest listUserIndustryRolesRequest = new ListUserIndustryRolesRequest()
                .setUserId("12345");
        try {
            client.listUserIndustryRolesWithOptions(listUserIndustryRolesRequest, listUserIndustryRolesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.resident_1_0.client import Client as dingtalkresident_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.resident_1_0 import models as dingtalkresident__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkresident_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkresident_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_user_industry_roles_headers = dingtalkresident__1__0_models.ListUserIndustryRolesHeaders()
        list_user_industry_roles_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_user_industry_roles_request = dingtalkresident__1__0_models.ListUserIndustryRolesRequest(
            user_id='12345'
        )
        try:
            client.list_user_industry_roles_with_options(list_user_industry_roles_request, list_user_industry_roles_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_user_industry_roles_headers = dingtalkresident__1__0_models.ListUserIndustryRolesHeaders()
        list_user_industry_roles_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_user_industry_roles_request = dingtalkresident__1__0_models.ListUserIndustryRolesRequest(
            user_id='12345'
        )
        try:
            await client.list_user_industry_roles_with_options_async(list_user_industry_roles_request, list_user_industry_roles_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\ListUserIndustryRolesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\ListUserIndustryRolesRequest;
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
        $listUserIndustryRolesHeaders = new ListUserIndustryRolesHeaders([]);
        $listUserIndustryRolesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listUserIndustryRolesRequest = new ListUserIndustryRolesRequest([
            "userId" => "12345"
        ]);
        try {
            $client->listUserIndustryRolesWithOptions($listUserIndustryRolesRequest, $listUserIndustryRolesHeaders, new RuntimeOptions([]));
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
  dingtalkresident_1_0  "github.com/alibabacloud-go/dingtalk/resident_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkresident_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkresident_1_0.Client{}
  _result, _err = dingtalkresident_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listUserIndustryRolesHeaders := &dingtalkresident_1_0.ListUserIndustryRolesHeaders{}
  listUserIndustryRolesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listUserIndustryRolesRequest := &dingtalkresident_1_0.ListUserIndustryRolesRequest{
    UserId: tea.String("12345"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListUserIndustryRolesWithOptions(listUserIndustryRolesRequest, listUserIndustryRolesHeaders, &util.RuntimeOptions{})
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
import dingtalkresident_1_0, * as $dingtalkresident_1_0 from '@alicloud/dingtalk/resident_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkresident_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkresident_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listUserIndustryRolesHeaders = new $dingtalkresident_1_0.ListUserIndustryRolesHeaders({ });
    listUserIndustryRolesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listUserIndustryRolesRequest = new $dingtalkresident_1_0.ListUserIndustryRolesRequest({
      userId: "12345",
    });
    try {
      await client.listUserIndustryRolesWithOptions(listUserIndustryRolesRequest, listUserIndustryRolesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkresident_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkresident_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkresident_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListUserIndustryRolesHeaders listUserIndustryRolesHeaders = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListUserIndustryRolesHeaders();
            listUserIndustryRolesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListUserIndustryRolesRequest listUserIndustryRolesRequest = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListUserIndustryRolesRequest
            {
                UserId = "12345",
            };
            try
            {
                client.ListUserIndustryRolesWithOptions(listUserIndustryRolesRequest, listUserIndustryRolesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| roleList | Array | 角色列表。 |
| roleId | Long | 角色ID。  **[!NOTE]**  以下管理角色没有角色ID，即该参数为空。   - super-admin：创建者 - main-admin：主管理员 - sub-admin：子管理员 |
| roleName | String | 角色名称。 |
| tagCode | String | 角色编码。  **[!NOTE]**  如果是自定义角色，该参数值为空。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "roleList" : [ {
    "roleId" : 312423423,
    "roleName" : "安保部经理",
    "tagCode" : "SecurityManager"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | service.org.error | %s | 企业信息获取异常 |
| 500 | service.user.error | %s | 用户信息获取异常 |
| 500 | service.role.error | %s | 用户角色信息获取异常 |
| 500 | service.common.error | %s | 系统错误 |
