---
title: "修改权限"
source_url: "https://open.dingtalk.com/document/development/modify-storage-permissions"
namespace: "development"
slug: "modify-storage-permissions"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 存储管理 > 权限管理 > 修改权限"
doc_id: "UWVq1YSI1V"
updated_at: "2026-08-25 09:38:57"
---

> Source: https://open.dingtalk.com/document/development/modify-storage-permissions
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 存储管理 > 权限管理 > 修改权限
> Updated: 2026-08-25 09:38:57

# 修改权限

调用本接口，修改存储空间的权限。

> **[!IMPORTANT]**
>
> - 新老接口中的ID不兼容, 不支持混用。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[修改权限](0683-modify-permissions-file.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
PUT /v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/permissions?unionId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "roleId" : "String",
  "members" : [ {
    "type" : "String",
    "id" : "String",
    "corpId" : "String"
  } ],
  "option" : {
    "duration" : Long
  }
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| dentryId | String | 是 | 文件或文件夹id，调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取id参数值。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作用户的unionId，调用[查询用户详情](0056-query-user-details.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| roleId | String | 是 | 权限角色Id。   - **OWNER**：拥有者 - **MANAGER**：管理者 - **EDITOR**：编辑者 - **DOWNLOADER**：下载者 - **READER**：查看者 |
| members | Array | 是 | 权限成员列表，最大值30。 |
| type | String | 是 | 权限成员类型：   - **ORG**：企业 - **DEPT**：部门 - **TAG**：自定义tag - **CONVERSATION**：会话 - **USER**：用户 |
| id | String | 是 | 权限成员id。   - 如果type参数值为**ORG**，该参数值传企业**corpId**。 - 如果type参数值为**DEPT**，该参数值传部门**deptId**，调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取。 - 如果type参数值为**TAG**，该参数值传**tag名称**。 - 如果type参数值为**CONVERSATION**，该参数值传会话**openConversationId**。    - 通过[创建群](1481-session-management-creates-groups.md)接口获取openConversationId参数值。   - 通过[创建群](1484-create-a-scene-group-v2.md)接口获取open\_conversation\_id参数值。 - 如果type参数值为**USER**，该参数传用户**unionId**，调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| corpId | String | 否 | 权限归属的企业corpId。   - type为DEPT或TAG时，该参数必填。 - type为USER时，该参数选填。   **[!NOTE]**  传入该参数，表示对应type下的员工在离职时，会自动清理权限。 |
| option | Object | 否 | 可选参数。 |
| duration | Long | 否 | 授权有效时长，单位秒，最大值3600。默认值为-1，表示永久有效。   - 被添加权限的空间类型是APP时，授权有效时长生效。 - 被添加权限的空间类型是USER时，授权有效时长无效，默认为永久有效。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 本次操作是否成功。   - **true**：成功 - **false**：失败 |

## 示例

**请求示例**

HTTP

```
PUT /v1.0/storage/spaces/854xxxxx/dentries/634xxxxx/permissions?unionId=cHtUYxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "roleId" : "MANAGER",
  "members" : [ {
    "type" : "USER",
    "id" : "cHtUYxxxxx",
    "corpId" : "ding123xxxxx"
  } ],
  "option" : {
    "duration" : 3600
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkstorage_1_0.*;
import com.aliyun.dingtalkstorage_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        UpdatePermissionHeaders updatePermissionHeaders = new UpdatePermissionHeaders();
        updatePermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdatePermissionRequest.UpdatePermissionRequestOption option = new UpdatePermissionRequest.UpdatePermissionRequestOption()
                .setDuration(3600L);
        UpdatePermissionRequest.UpdatePermissionRequestMembers members0 = new UpdatePermissionRequest.UpdatePermissionRequestMembers()
                .setType("USER")
                .setId("cHtUYxxxxx")
                .setCorpId("ding123xxxxx");
        UpdatePermissionRequest updatePermissionRequest = new UpdatePermissionRequest()
                .setUnionId("cHtUYxxxxx")
                .setRoleId("MANAGER")
                .setMembers(java.util.Arrays.asList(
                    members0
                ))
                .setOption(option);
        try {
            client.updatePermissionWithOptions("854xxxxx", "634xxxxx", updatePermissionRequest, updatePermissionHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.storage_1_0.client import Client as dingtalkstorage_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_1_0 import models as dingtalkstorage__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_permission_headers = dingtalkstorage__1__0_models.UpdatePermissionHeaders()
        update_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.UpdatePermissionRequestOption(
            duration=3600
        )
        members_0 = dingtalkstorage__1__0_models.UpdatePermissionRequestMembers(
            type='USER',
            id='cHtUYxxxxx',
            corp_id='ding123xxxxx'
        )
        update_permission_request = dingtalkstorage__1__0_models.UpdatePermissionRequest(
            union_id='cHtUYxxxxx',
            role_id='MANAGER',
            members=[
                members_0
            ],
            option=option
        )
        try:
            client.update_permission_with_options('854xxxxx', '634xxxxx', update_permission_request, update_permission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_permission_headers = dingtalkstorage__1__0_models.UpdatePermissionHeaders()
        update_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.UpdatePermissionRequestOption(
            duration=3600
        )
        members_0 = dingtalkstorage__1__0_models.UpdatePermissionRequestMembers(
            type='USER',
            id='cHtUYxxxxx',
            corp_id='ding123xxxxx'
        )
        update_permission_request = dingtalkstorage__1__0_models.UpdatePermissionRequest(
            union_id='cHtUYxxxxx',
            role_id='MANAGER',
            members=[
                members_0
            ],
            option=option
        )
        try:
            await client.update_permission_with_options_async('854xxxxx', '634xxxxx', update_permission_request, update_permission_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdatePermissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdatePermissionRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdatePermissionRequest\members;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdatePermissionRequest;
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
        $updatePermissionHeaders = new UpdatePermissionHeaders([]);
        $updatePermissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "duration" => 3600
        ]);
        $members0 = new members([
            "type" => "USER",
            "id" => "cHtUYxxxxx",
            "corpId" => "ding123xxxxx"
        ]);
        $updatePermissionRequest = new UpdatePermissionRequest([
            "unionId" => "cHtUYxxxxx",
            "roleId" => "MANAGER",
            "members" => [
                $members0
            ],
            "option" => $option
        ]);
        try {
            $client->updatePermissionWithOptions("854xxxxx", "634xxxxx", $updatePermissionRequest, $updatePermissionHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkstorage_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_1_0.Client{}
  _result, _err = dingtalkstorage_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updatePermissionHeaders := &dingtalkstorage_1_0.UpdatePermissionHeaders{}
  updatePermissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.UpdatePermissionRequestOption{
    Duration: tea.Int64(3600),
  }
  members0 := &dingtalkstorage_1_0.UpdatePermissionRequestMembers{
    Type: tea.String("USER"),
    Id: tea.String("cHtUYxxxxx"),
    CorpId: tea.String("ding123xxxxx"),
  }
  updatePermissionRequest := &dingtalkstorage_1_0.UpdatePermissionRequest{
    UnionId: tea.String("cHtUYxxxxx"),
    RoleId: tea.String("MANAGER"),
    Members: []*dingtalkstorage_1_0.UpdatePermissionRequestMembers{members0},
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdatePermissionWithOptions(tea.String("854xxxxx"), tea.String("634xxxxx"), updatePermissionRequest, updatePermissionHeaders, &util.RuntimeOptions{})
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
import dingtalkstorage_1_0, * as $dingtalkstorage_1_0 from '@alicloud/dingtalk/storage_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkstorage_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkstorage_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let updatePermissionHeaders = new $dingtalkstorage_1_0.UpdatePermissionHeaders({ });
    updatePermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let option = new $dingtalkstorage_1_0.UpdatePermissionRequestOption({
      duration: 3600,
    });
    let members0 = new $dingtalkstorage_1_0.UpdatePermissionRequestMembers({
      type: "USER",
      id: "cHtUYxxxxx",
      corpId: "ding123xxxxx",
    });
    let updatePermissionRequest = new $dingtalkstorage_1_0.UpdatePermissionRequest({
      unionId: "cHtUYxxxxx",
      roleId: "MANAGER",
      members: [
        members0
      ],
      option: option,
    });
    try {
      await client.updatePermissionWithOptions("854xxxxx", "634xxxxx", updatePermissionRequest, updatePermissionHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionHeaders updatePermissionHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionHeaders();
            updatePermissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest.UpdatePermissionRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest.UpdatePermissionRequestOption
            {
                Duration = 3600,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest.UpdatePermissionRequestMembers members0 = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest.UpdatePermissionRequestMembers
            {
                Type = "USER",
                Id = "cHtUYxxxxx",
                CorpId = "ding123xxxxx",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest updatePermissionRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest
            {
                UnionId = "cHtUYxxxxx",
                RoleId = "MANAGER",
                Members = new List<AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdatePermissionRequest.UpdatePermissionRequestMembers>
                {
                    members0
                },
                Option = option,
            };
            try
            {
                client.UpdatePermissionWithOptions("854xxxxx", "634xxxxx", updatePermissionRequest, updatePermissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | paramError.roleId | %s | 参数错误-roleId |
| 400 | paramError.permissionMemberType | %s | 参数错误-permissionMemberType |
| 400 | spaceNotExist | %s | 空间不存在 |
| 400 | dentryNotExist | %s | 文件不存在 |
| 403 | permissionDenied | %s | 用户缺少授权的权限 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
