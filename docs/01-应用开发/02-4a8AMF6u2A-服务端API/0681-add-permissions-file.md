---
title: "添加权限"
source_url: "https://open.dingtalk.com/document/development/add-permissions-file"
namespace: "development"
slug: "add-permissions-file"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 权限管理 > 添加权限"
doc_id: "9tMIdlAdNV"
updated_at: "2026-07-08 14:38:35"
---

> Source: https://open.dingtalk.com/document/development/add-permissions-file
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 权限管理 > 添加权限
> Updated: 2026-07-08 14:38:35

# 添加权限

调用本接口，根据文件uuid、操作者unionId和权限id等信息，实现权限成员权限的添加。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/storage/spaces/dentries/{dentryUuid}/permissions |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.Permission.Write-企业存储授权信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dentryUuid | String | 是 | 文件uuid：可调用[搜索文件](0638-search-for-files.md)接口或[获取dentryUuid信息](0672-api-getuuidbydentryid.md)接口，获取返回参数`dentryUuid`字段。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| roleId | String | 是 | 角色id，枚举值：   - **OWNER**：拥有者，具有以下权限点：    - PermissionPrivilegeEnum.INFO   - PermissionPrivilegeEnum.LIST   - PermissionPrivilegeEnum.PREVIEW   - PermissionPrivilegeEnum.READ   - PermissionPrivilegeEnum.WRITE   - PermissionPrivilegeEnum.DOWNLOAD   - PermissionPrivilegeEnum.ADD   - PermissionPrivilegeEnum.DELETE   - PermissionPrivilegeEnum.MODIFY   - PermissionPrivilegeEnum.COPY   - PermissionPrivilegeEnum.RENAME   - PermissionPrivilegeEnum.READ\_PERMISSION   - PermissionPrivilegeEnum.WRITE\_PERMISSION   - PermissionPrivilegeEnum.ASSIGN - **MANAGER**：管理者，具有以下权限点：    - PermissionPrivilegeEnum.INFO   - PermissionPrivilegeEnum.LIST   - PermissionPrivilegeEnum.PREVIEW   - PermissionPrivilegeEnum.READ   - PermissionPrivilegeEnum.WRITE   - PermissionPrivilegeEnum.DOWNLOAD   - PermissionPrivilegeEnum.ADD   - PermissionPrivilegeEnum.DELETE   - PermissionPrivilegeEnum.MODIFY   - PermissionPrivilegeEnum.COPY   - PermissionPrivilegeEnum.RENAME   - PermissionPrivilegeEnum.READ\_PERMISSION   - PermissionPrivilegeEnum.WRITE\_PERMISSION - **EDITOR**：编辑者，具有以下权限点：    - PermissionPrivilegeEnum.INFO   - PermissionPrivilegeEnum.LIST   - PermissionPrivilegeEnum.PREVIEW   - PermissionPrivilegeEnum.READ   - PermissionPrivilegeEnum.WRITE   - PermissionPrivilegeEnum.DOWNLOAD   - PermissionPrivilegeEnum.ADD - **DOWNLOADER**：查看下载者，具有以下权限点：    - PermissionPrivilegeEnum.INFO   - PermissionPrivilegeEnum.LIST   - PermissionPrivilegeEnum.PREVIEW   - PermissionPrivilegeEnum.READ   - PermissionPrivilegeEnum.DOWNLOAD - **READER**：仅可查看者，具有以下权限点：    - PermissionPrivilegeEnum.INFO   - PermissionPrivilegeEnum.LIST   - PermissionPrivilegeEnum.PREVIEW |
| members | Array | 是 | 权限成员列表，最多30个。 |
| type | String | 是 | 权限成员类型，枚举值：   - **ORG**：企业 - **DEPT**：部门 - **TAG**：自定义tag - **CONVERSATION**：会话 - **USER**：用户 - **DYNAMIC\_GROUP**：动态用户组 |
| id | String | 是 | 权限成员id：   - `type=ORG`时，id为企业ID - `type=DEPT`时，id为部门ID - `type=TAG`时，id为标签ID - `type=CONVERSATION`时，id为会话ID - `type=USER`时，id为员工userId - `type=DYNAMIC_GROUP`时，id为动态用户组groupCode |
| corpId | String | 否 | 权限归属的企业：       - 如果存在企业id，对应member离职的时候会自动清理权限。 - 如果memberType是dept类型，必须要有企业id。 |
| name | String | 否 | 用户名:   - `type=ORG`时，name为企业名称 - `type=DEPT`时，name为部门名称 - `type=TAG`时，name为标签名称 - `type=CONVERSATION`时，name为会话名称 - `type=USER`时，name为员工姓名 - `type=DYNAMIC_GROUP`时，name不需要填写 |
| option | Object | 否 | 可选参数。 |
| duration | Long | 否 | 有效时间（秒）。       - 目前仅OwnerType为APP的Space支持临时权限。 - 最大值3600。 |

### 请求示例

HTTP

```
POST /v2.0/storage/spaces/dentries/EpGBxxxx7R35y/permissions?unionId=tXguNxxxxAiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "roleId" : "MANAGER",
  "members" : [ {
    "type" : "USER",
    "id" : "01472825524039877041",
    "corpId" : "ding16b241fd05********288"
  } ],
  "option" : {
    "duration" : 3600
  }
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
    public static com.aliyun.dingtalkstorage_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkstorage_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_2_0.models.AddPermissionHeaders addPermissionHeaders = new com.aliyun.dingtalkstorage_2_0.models.AddPermissionHeaders();
        addPermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_2_0.models.AddPermissionRequest.AddPermissionRequestOption option = new com.aliyun.dingtalkstorage_2_0.models.AddPermissionRequest.AddPermissionRequestOption()
                .setDuration(3600L);
        com.aliyun.dingtalkstorage_2_0.models.AddPermissionRequest.AddPermissionRequestMembers members0 = new com.aliyun.dingtalkstorage_2_0.models.AddPermissionRequest.AddPermissionRequestMembers()
                .setType("USER")
                .setId("01472825524039877041")
                .setCorpId("ding16b241fd05********288");
        com.aliyun.dingtalkstorage_2_0.models.AddPermissionRequest addPermissionRequest = new com.aliyun.dingtalkstorage_2_0.models.AddPermissionRequest()
                .setUnionId("tXguNxxxxAiEiE")
                .setRoleId("MANAGER")
                .setMembers(java.util.Arrays.asList(
                    members0
                ))
                .setOption(option);
        try {
            client.addPermissionWithOptions("EpGBxxxx7R35y", addPermissionRequest, addPermissionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.storage_2_0.client import Client as dingtalkstorage_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_2_0 import models as dingtalkstorage__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_permission_headers = dingtalkstorage__2__0_models.AddPermissionHeaders()
        add_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__2__0_models.AddPermissionRequestOption(
            duration=3600
        )
        members_0 = dingtalkstorage__2__0_models.AddPermissionRequestMembers(
            type='USER',
            id='01472825524039877041',
            corp_id='ding16b241fd05********288'
        )
        add_permission_request = dingtalkstorage__2__0_models.AddPermissionRequest(
            union_id='tXguNxxxxAiEiE',
            role_id='MANAGER',
            members=[
                members_0
            ],
            option=option
        )
        try:
            client.add_permission_with_options('EpGBxxxx7R35y', add_permission_request, add_permission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_permission_headers = dingtalkstorage__2__0_models.AddPermissionHeaders()
        add_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__2__0_models.AddPermissionRequestOption(
            duration=3600
        )
        members_0 = dingtalkstorage__2__0_models.AddPermissionRequestMembers(
            type='USER',
            id='01472825524039877041',
            corp_id='ding16b241fd05********288'
        )
        add_permission_request = dingtalkstorage__2__0_models.AddPermissionRequest(
            union_id='tXguNxxxxAiEiE',
            role_id='MANAGER',
            members=[
                members_0
            ],
            option=option
        )
        try:
            await client.add_permission_with_options_async('EpGBxxxx7R35y', add_permission_request, add_permission_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\AddPermissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\AddPermissionRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\AddPermissionRequest\members;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\AddPermissionRequest;
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
        $option = new option([
            "duration" => 3600
        ]);
        $members0 = new members([
            "type" => "USER",
            "id" => "01472825524039877041",
            "corpId" => "ding16b241fd05********288"
        ]);
        $addPermissionRequest = new AddPermissionRequest([
            "unionId" => "tXguNxxxxAiEiE",
            "roleId" => "MANAGER",
            "members" => [
                $members0
            ],
            "option" => $option
        ]);
        try {
            $client->addPermissionWithOptions("EpGBxxxx7R35y", $addPermissionRequest, $addPermissionHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_2_0  "github.com/alibabacloud-go/dingtalk/storage_2_0"
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
func CreateClient () (_result *dingtalkstorage_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_2_0.Client{}
  _result, _err = dingtalkstorage_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addPermissionHeaders := &dingtalkstorage_2_0.AddPermissionHeaders{}
  addPermissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_2_0.AddPermissionRequestOption{
    Duration: tea.Int64(3600),
  }
  members0 := &dingtalkstorage_2_0.AddPermissionRequestMembers{
    Type: tea.String("USER"),
    Id: tea.String("01472825524039877041"),
    CorpId: tea.String("ding16b241fd05********288"),
  }
  addPermissionRequest := &dingtalkstorage_2_0.AddPermissionRequest{
    UnionId: tea.String("tXguNxxxxAiEiE"),
    RoleId: tea.String("MANAGER"),
    Members: []*dingtalkstorage_2_0.AddPermissionRequestMembers{members0},
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddPermissionWithOptions(tea.String("EpGBxxxx7R35y"), addPermissionRequest, addPermissionHeaders, &util.RuntimeOptions{})
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
const dingtalkstorage_2_0 = require('@alicloud/dingtalk/storage_2_0');
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
    return new dingtalkstorage_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let addPermissionHeaders = new dingtalkstorage_2_0.AddPermissionHeaders({ });
    addPermissionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let option = new dingtalkstorage_2_0.AddPermissionRequestOption({
      duration: 3600,
    });
    let members0 = new dingtalkstorage_2_0.AddPermissionRequestMembers({
      type: 'USER',
      id: '01472825524039877041',
      corpId: 'ding16b241fd05********288',
    });
    let addPermissionRequest = new dingtalkstorage_2_0.AddPermissionRequest({
      unionId: 'tXguNxxxxAiEiE',
      roleId: 'MANAGER',
      members: [
        members0
      ],
      option: option,
    });
    try {
      await client.addPermissionWithOptions('EpGBxxxx7R35y', addPermissionRequest, addPermissionHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionHeaders addPermissionHeaders = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionHeaders();
            addPermissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest.AddPermissionRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest.AddPermissionRequestOption
            {
                Duration = 3600,
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest.AddPermissionRequestMembers members0 = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest.AddPermissionRequestMembers
            {
                Type = "USER",
                Id = "01472825524039877041",
                CorpId = "ding16b241fd05********288",
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest addPermissionRequest = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest
            {
                UnionId = "tXguNxxxxAiEiE",
                RoleId = "MANAGER",
                Members = new List<AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.AddPermissionRequest.AddPermissionRequestMembers>
                {
                    members0
                },
                Option = option,
            };
            try
            {
                client.AddPermissionWithOptions("EpGBxxxx7R35y", addPermissionRequest, addPermissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 本次操作是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.dentryUuid | %s | 参数错误-dentryUuid |
| 400 | paramError.roleId | %s | 参数错误-roleId |
| 400 | paramError.permissionMemberType | %s | 参数错误-permissionMemberType |
| 403 | permissionDenied | %s | 用户缺少授权的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
