---
title: "获取行业角色下的用户列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-users-under-an-industry-role"
namespace: "development"
slug: "obtains-a-list-of-users-under-an-industry-role"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 行业角色管理 > 获取行业角色下的用户列表"
doc_id: "5hUYgHoy0a"
updated_at: "2025-09-23 19:23:35"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-users-under-an-industry-role
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 行业角色管理 > 获取行业角色下的用户列表
> Updated: 2025-09-23 19:23:35

# 获取行业角色下的用户列表

根据行业角色编码获取角色下的人员列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/resident/industryRoles/users |
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
| tagCode | String | 是 | 行业角色编码，有以下取值：   - **通用管理角色**    - **super-admin**：创建者   - **main-admin**：主管理员   - **sub-admin**：子管理员 - **乡村行业**    - **Villager**：村民   - **Leaseholder**：租客   - **GroupManager**：组长   - **HeadOfHouseHold**：户主   - **HouseAdmin**：家庭管理员   - **Party**：党员   - **Probationary**：预备党员   - **FlowParty**：流动党员   - **YouthLeagueMember**：青年团员   - **Secretary**：书记   - **Abbreviation**：村委   - **VillageRepresentative**：村民代表   - **Women**：妇女 - **小区行业**    - **ProjectManager**：项目经理   - **EngineeringDirector**：工程主管   - **EngineeringMember**：工程队员   - **SecurityDirector**：安保主管   - **SecurityLeader**：安保班长   - **SecurityMember**：安保队员   - **CustomerServiceDirector**：客服主管   - **CustomerServiceMember**：前台客服   - **Housekeeper**：管家   - **CleaningDirector**：保洁主管   - **CleaningStaff**：保洁员 - **物业行业**    - **OrgPrinciple**：企业负责人   - **ChargeManager**：财务部经理   - **ChargeStaff**：财务部员工   - **EngineerManager**：工程部经理   - **EngineerStaff**：工程部员工   - **SecurityManager**：安保部经理   - **SecurityStaff**：安保部员工   - **SupportManager**：客服部经理   - **SupportStaff**：客服部员工   - **EnvironmentManager**：环境部经理   - **EnvironmentStaff**：环境部员工   - **QualityManager**：品质部经理   - **QualityStaff**：品质部员工 |

### 请求示例

HTTP

```
GET /v1.0/resident/industryRoles/users?tagCode=SecurityManager HTTP/1.1
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
        ListIndustryRoleUsersHeaders listIndustryRoleUsersHeaders = new ListIndustryRoleUsersHeaders();
        listIndustryRoleUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListIndustryRoleUsersRequest listIndustryRoleUsersRequest = new ListIndustryRoleUsersRequest()
                .setTagCode("SecurityManager");
        try {
            client.listIndustryRoleUsersWithOptions(listIndustryRoleUsersRequest, listIndustryRoleUsersHeaders, new RuntimeOptions());
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
        list_industry_role_users_headers = dingtalkresident__1__0_models.ListIndustryRoleUsersHeaders()
        list_industry_role_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_industry_role_users_request = dingtalkresident__1__0_models.ListIndustryRoleUsersRequest(
            tag_code='SecurityManager'
        )
        try:
            client.list_industry_role_users_with_options(list_industry_role_users_request, list_industry_role_users_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_industry_role_users_headers = dingtalkresident__1__0_models.ListIndustryRoleUsersHeaders()
        list_industry_role_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_industry_role_users_request = dingtalkresident__1__0_models.ListIndustryRoleUsersRequest(
            tag_code='SecurityManager'
        )
        try:
            await client.list_industry_role_users_with_options_async(list_industry_role_users_request, list_industry_role_users_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\ListIndustryRoleUsersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\ListIndustryRoleUsersRequest;
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
        $listIndustryRoleUsersHeaders = new ListIndustryRoleUsersHeaders([]);
        $listIndustryRoleUsersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listIndustryRoleUsersRequest = new ListIndustryRoleUsersRequest([
            "tagCode" => "SecurityManager"
        ]);
        try {
            $client->listIndustryRoleUsersWithOptions($listIndustryRoleUsersRequest, $listIndustryRoleUsersHeaders, new RuntimeOptions([]));
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

  listIndustryRoleUsersHeaders := &dingtalkresident_1_0.ListIndustryRoleUsersHeaders{}
  listIndustryRoleUsersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listIndustryRoleUsersRequest := &dingtalkresident_1_0.ListIndustryRoleUsersRequest{
    TagCode: tea.String("SecurityManager"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListIndustryRoleUsersWithOptions(listIndustryRoleUsersRequest, listIndustryRoleUsersHeaders, &util.RuntimeOptions{})
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
    let listIndustryRoleUsersHeaders = new $dingtalkresident_1_0.ListIndustryRoleUsersHeaders({ });
    listIndustryRoleUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listIndustryRoleUsersRequest = new $dingtalkresident_1_0.ListIndustryRoleUsersRequest({
      tagCode: "SecurityManager",
    });
    try {
      await client.listIndustryRoleUsersWithOptions(listIndustryRoleUsersRequest, listIndustryRoleUsersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListIndustryRoleUsersHeaders listIndustryRoleUsersHeaders = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListIndustryRoleUsersHeaders();
            listIndustryRoleUsersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListIndustryRoleUsersRequest listIndustryRoleUsersRequest = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListIndustryRoleUsersRequest
            {
                TagCode = "SecurityManager",
            };
            try
            {
                client.ListIndustryRoleUsersWithOptions(listIndustryRoleUsersRequest, listIndustryRoleUsersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| userIdList | Array of String | 用户userId列表。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "userIdList" : [ "12345" ]
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
