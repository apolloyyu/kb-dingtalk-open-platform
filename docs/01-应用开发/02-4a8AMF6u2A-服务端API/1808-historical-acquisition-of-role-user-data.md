---
title: "获取角色用户数据"
source_url: "https://open.dingtalk.com/document/development/historical-acquisition-of-role-user-data"
namespace: "development"
slug: "historical-acquisition-of-role-user-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 氚云 > 组织和用户 > 获取角色用户数据"
doc_id: "yPbY2yw0MO"
updated_at: "2025-12-05 19:31:31"
---

> Source: https://open.dingtalk.com/document/development/historical-acquisition-of-role-user-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 氚云 > 组织和用户 > 获取角色用户数据
> Updated: 2025-12-05 19:31:31

# 获取角色用户数据

调用本接口可获取指定角色包含的用户。

> **[!IMPORTANT]**
>
> 为了更进一步提升接口质量以及用户体验，我们对本接口文档做出如下调整：
>
> - 自 2024 年 8 月 1 日起，本接口文档将会被迁移至历史文档目录。
> - 氚云接口不再支持新应用接入，已接入应用可继续使用，后续若需要接入氚云接口，请使用[氚云开发者手册](https://help.h3yun.com/channels/899.html)。

![](https://img.alicdn.com/imgextra/i2/O1CN01pw0AIj1k7KtGFthOJ_!!6000000004636-2-tps-886-432.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=h3yun_1.0%23GetRoleUsers) |
| 第三方企业应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=h3yun_1.0%23GetRoleUsers) |
| 第三方个人应用 | 暂不支持 | 氚云数据管理权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/h3yun/roles/roleUsers?roleId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| roleId | String | 是 | 角色ID。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 状态码。 |
| message | String | 状态码描述。 |
| data | Array | 用户信息列表。 |
| userId | String | 用户ID。 |
| name | String | 用户名称。 |
| code | String | 用户编码。 |
| sex | String | 性别，取值：   - **None**：未指定 - **Man**：男性 - **Female**：女性 |
| description | String | 描述。 |
| mobile | String | 手机号码。 |
| email | String | 邮箱。 |
| departmentId | String | 所属部门ID。 |
| departmentName | String | 所属部门名称。 |
| domainType | String | 所属范围，取值：   - **Internal**：内部 - **External**：外部 |
| partDepartmentIds | Array of String | 兼职部门ID集合，含主部门ID。 |
| sortKey | Long | 排序值。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/h3yun/roles/roleUsers?roleId=18f923a7-5a5e-xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bef2xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkh3yun_1_0.*;
import com.aliyun.dingtalkh3yun_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkh3yun_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkh3yun_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkh3yun_1_0.Client client = Sample.createClient();
        GetRoleUsersHeaders getRoleUsersHeaders = new GetRoleUsersHeaders();
        getRoleUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetRoleUsersRequest getRoleUsersRequest = new GetRoleUsersRequest()
                .setRoleId("18f923a7-5a5e-xxx");
        try {
            client.getRoleUsersWithOptions(getRoleUsersRequest, getRoleUsersHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.h3yun_1_0.client import Client as dingtalkh3yun_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.h3yun_1_0 import models as dingtalkh_3yun__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkh3yun_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkh3yun_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_role_users_headers = dingtalkh_3yun__1__0_models.GetRoleUsersHeaders()
        get_role_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_role_users_request = dingtalkh_3yun__1__0_models.GetRoleUsersRequest(
            role_id='18f923a7-5a5e-xxx'
        )
        try:
            client.get_role_users_with_options(get_role_users_request, get_role_users_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_role_users_headers = dingtalkh_3yun__1__0_models.GetRoleUsersHeaders()
        get_role_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_role_users_request = dingtalkh_3yun__1__0_models.GetRoleUsersRequest(
            role_id='18f923a7-5a5e-xxx'
        )
        try:
            await client.get_role_users_with_options_async(get_role_users_request, get_role_users_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\GetRoleUsersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\GetRoleUsersRequest;
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
        $getRoleUsersHeaders = new GetRoleUsersHeaders([]);
        $getRoleUsersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getRoleUsersRequest = new GetRoleUsersRequest([
            "roleId" => "18f923a7-5a5e-xxx"
        ]);
        try {
            $client->getRoleUsersWithOptions($getRoleUsersRequest, $getRoleUsersHeaders, new RuntimeOptions([]));
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
  dingtalkh3yun_1_0  "github.com/alibabacloud-go/dingtalk/h3yun_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkh3yun_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkh3yun_1_0.Client{}
  _result, _err = dingtalkh3yun_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getRoleUsersHeaders := &dingtalkh3yun_1_0.GetRoleUsersHeaders{}
  getRoleUsersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getRoleUsersRequest := &dingtalkh3yun_1_0.GetRoleUsersRequest{
    RoleId: tea.String("18f923a7-5a5e-xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetRoleUsersWithOptions(getRoleUsersRequest, getRoleUsersHeaders, &util.RuntimeOptions{})
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
import dingtalkh3yun_1_0, * as $dingtalkh3yun_1_0 from '@alicloud/dingtalk/h3yun_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkh3yun_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkh3yun_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getRoleUsersHeaders = new $dingtalkh3yun_1_0.GetRoleUsersHeaders({ });
    getRoleUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getRoleUsersRequest = new $dingtalkh3yun_1_0.GetRoleUsersRequest({
      roleId: "18f923a7-5a5e-xxx",
    });
    try {
      await client.getRoleUsersWithOptions(getRoleUsersRequest, getRoleUsersHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetRoleUsersHeaders getRoleUsersHeaders = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetRoleUsersHeaders();
            getRoleUsersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetRoleUsersRequest getRoleUsersRequest = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetRoleUsersRequest
            {
                RoleId = "18f923a7-5a5e-xxx",
            };
            try
            {
                client.GetRoleUsersWithOptions(getRoleUsersRequest, getRoleUsersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkh_3yun__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkh3yun_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkh3yun_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::Client> client = make_shared<Alibabacloud_Dingtalkh3yun_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::GetRoleUsersHeaders> getRoleUsersHeaders = make_shared<Alibabacloud_Dingtalkh3yun_1_0::GetRoleUsersHeaders>();
  getRoleUsersHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::GetRoleUsersRequest> getRoleUsersRequest = make_shared<Alibabacloud_Dingtalkh3yun_1_0::GetRoleUsersRequest>(map<string, boost::any>({
    {"roleId", boost::any(string("18f923a7-5a5e-xxx"))}
  }));
  try {
    client->getRoleUsersWithOptions(getRoleUsersRequest, getRoleUsersHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : "success",
  "message" : "OK",
  "data" : [ {
    "userId" : "9a1-8495-129c6b0d95c5",
    "name" : "张三",
    "code" : "zhangsan",
    "sex" : "Man",
    "description" : "Null",
    "mobile" : "156*******",
    "email" : "xxx@example.com",
    "departmentId" : "18f923a7-5a5e-xxx",
    "departmentName" : "研发中心",
    "domainType" : "Internal",
    "partDepartmentIds" : [ "18f923a7-5a5e-xxx" ],
    "sortKey" : 822126512
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | dataNotExist.role.roleNotExist | 角色无效或不存在 | 无效的roleId参数 |
| 500 | systemError | 系统异常 | 系统异常 |
