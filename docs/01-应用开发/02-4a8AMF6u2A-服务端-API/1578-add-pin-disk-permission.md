---
title: "添加权限"
source_url: "https://open.dingtalk.com/document/development/add-pin-disk-permission"
namespace: "development"
slug: "add-pin-disk-permission"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 权限管理 > 添加权限"
doc_id: "3qEJBE3tDE"
updated_at: "2026-08-25 09:38:34"
---

> Source: https://open.dingtalk.com/document/development/add-pin-disk-permission
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 权限管理 > 添加权限
> Updated: 2026-08-25 09:38:34

# 添加权限

调用本接口添加用户对钉盘空间和文件的权限。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[添加权限](0681-add-permissions-file.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/drive/spaces/{spaceId}/files/{fileId}/permissions HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "role" : "String",
  "members" : [ {
    "corpId" : "String",
    "memberType" : "String",
    "memberId" : "String"
  } ],
  "unionId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 钉盘空间ID，调用[获取空间列表](0636-queries-a-space-list.md)接口获取spaceId参数值。 |
| fileId | String | 是 | 文件ID，调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取fileId参数值。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| role | String | 是 | 权限角色。   - **owner**：所有者 - **admin**：管理员 - **editor**：可编辑 - **viewer**：可查看/下载 - **only\_viewer**：只读 |
| members | Array | 是 | 成员权限列表。 |
| corpId | String | 是 | 企业的CorpId。 |
| memberType | String | 是 | 成员类型。   - **org**：企业 - **department**：部门 - **conversation**：群 - **user**：用户 |
| memberId | String | 是 | 成员ID。   - 当**memberType**为**org**时，取值为**corpId** - 当**memberType**为**department**时，取值为**deptId** - 当**memberType**为**conversation**时，取值为**chatId** - 当**memberType**为**user**时，取值为**staffId** |
| unionId | String | 是 | 用户unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/drive/spaces/<spaceId>/files/<fileId>/permissions HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2db66caxxxx
Content-Type:application/json

{
  "role" : "editor",
  "members" : [ {
    "corpId" : "ding32fffxxxx",
    "memberType" : "user",
    "memberId" : "fejkafe"
  } ],
  "unionId" : "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdrive_1_0.*;
import com.aliyun.dingtalkdrive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdrive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdrive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdrive_1_0.Client client = Sample.createClient();
        AddPermissionHeaders addPermissionHeaders = new AddPermissionHeaders();
        addPermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddPermissionRequest.AddPermissionRequestMembers members0 = new AddPermissionRequest.AddPermissionRequestMembers()
                .setCorpId("ding32fffxxxx")
                .setMemberType("user")
                .setMemberId("fejkafe");
        AddPermissionRequest addPermissionRequest = new AddPermissionRequest()
                .setRole("editor")
                .setMembers(java.util.Arrays.asList(
                    members0
                ))
                .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx");
        try {
            client.addPermissionWithOptions("<spaceId>", "<fileId>", addPermissionRequest, addPermissionHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.drive_1_0.client import Client as dingtalkdrive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.drive_1_0 import models as dingtalkdrive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdrive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdrive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_permission_headers = dingtalkdrive__1__0_models.AddPermissionHeaders()
        add_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        members_0 = dingtalkdrive__1__0_models.AddPermissionRequestMembers(
            corp_id='ding32fffxxxx',
            member_type='user',
            member_id='fejkafe'
        )
        add_permission_request = dingtalkdrive__1__0_models.AddPermissionRequest(
            role='editor',
            members=[
                members_0
            ],
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
        )
        try:
            client.add_permission_with_options('<spaceId>', '<fileId>', add_permission_request, add_permission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_permission_headers = dingtalkdrive__1__0_models.AddPermissionHeaders()
        add_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        members_0 = dingtalkdrive__1__0_models.AddPermissionRequestMembers(
            corp_id='ding32fffxxxx',
            member_type='user',
            member_id='fejkafe'
        )
        add_permission_request = dingtalkdrive__1__0_models.AddPermissionRequest(
            role='editor',
            members=[
                members_0
            ],
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
        )
        try:
            await client.add_permission_with_options_async('<spaceId>', '<fileId>', add_permission_request, add_permission_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddPermissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddPermissionRequest\members;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddPermissionRequest;
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
        $addPermissionHeaders = new AddPermissionHeaders([]);
        $addPermissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $members0 = new members([
            "corpId" => "ding32fffxxxx",
            "memberType" => "user",
            "memberId" => "fejkafe"
        ]);
        $addPermissionRequest = new AddPermissionRequest([
            "role" => "editor",
            "members" => [
                $members0
            ],
            "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
        ]);
        try {
            $client->addPermissionWithOptions("<spaceId>", "<fileId>", $addPermissionRequest, $addPermissionHeaders, new RuntimeOptions([]));
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
  dingtalkdrive_1_0  "github.com/alibabacloud-go/dingtalk/drive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdrive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdrive_1_0.Client{}
  _result, _err = dingtalkdrive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addPermissionHeaders := &dingtalkdrive_1_0.AddPermissionHeaders{}
  addPermissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  members0 := &dingtalkdrive_1_0.AddPermissionRequestMembers{
    CorpId: tea.String("ding32fffxxxx"),
    MemberType: tea.String("user"),
    MemberId: tea.String("fejkafe"),
  }
  addPermissionRequest := &dingtalkdrive_1_0.AddPermissionRequest{
    Role: tea.String("editor"),
    Members: []*dingtalkdrive_1_0.AddPermissionRequestMembers{members0},
    UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddPermissionWithOptions(tea.String("<spaceId>"), tea.String("<fileId>"), addPermissionRequest, addPermissionHeaders, &util.RuntimeOptions{})
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
import dingtalkdrive_1_0, * as $dingtalkdrive_1_0 from '@alicloud/dingtalk/drive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdrive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdrive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addPermissionHeaders = new $dingtalkdrive_1_0.AddPermissionHeaders({ });
    addPermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let members0 = new $dingtalkdrive_1_0.AddPermissionRequestMembers({
      corpId: "ding32fffxxxx",
      memberType: "user",
      memberId: "fejkafe",
    });
    let addPermissionRequest = new $dingtalkdrive_1_0.AddPermissionRequest({
      role: "editor",
      members: [
        members0
      ],
      unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
    });
    try {
      await client.addPermissionWithOptions("<spaceId>", "<fileId>", addPermissionRequest, addPermissionHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdrive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdrive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionHeaders addPermissionHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionHeaders();
            addPermissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionRequest.AddPermissionRequestMembers members0 = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionRequest.AddPermissionRequestMembers
            {
                CorpId = "ding32fffxxxx",
                MemberType = "user",
                MemberId = "fejkafe",
            };
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionRequest addPermissionRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionRequest
            {
                Role = "editor",
                Members = new List<AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddPermissionRequest.AddPermissionRequestMembers>
                {
                    members0
                },
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
            };
            try
            {
                client.AddPermissionWithOptions("<spaceId>", "<fileId>", addPermissionRequest, addPermissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdrive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdrive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdrive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdrive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddPermissionHeaders> addPermissionHeaders = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddPermissionHeaders>();
  addPermissionHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddPermissionRequestMembers> members0 = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddPermissionRequestMembers>(map<string, boost::any>({
    {"corpId", boost::any(string("ding32fffxxxx"))},
    {"memberType", boost::any(string("user"))},
    {"memberId", boost::any(string("fejkafe"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddPermissionRequest> addPermissionRequest = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddPermissionRequest>(map<string, boost::any>({
    {"role", boost::any(string("editor"))},
    {"members", boost::any(vector<Alibabacloud_Dingtalkdrive_1_0::AddPermissionRequestMembers>({
      members0
    }))},
    {"unionId", boost::any(string("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"))}
  }));
  try {
    client->addPermissionWithOptions(make_shared<string>("<spaceId>"), make_shared<string>("<fileId>"), addPermissionRequest, addPermissionHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Invalid Param | 参数错误 |
| 400 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 400 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 400 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 404 | object.not.exist | File does not exist or has been deleted. | 文件不存在或已删除 |
| 500 | unknown.error | Unknown Error | 未知错误 |
