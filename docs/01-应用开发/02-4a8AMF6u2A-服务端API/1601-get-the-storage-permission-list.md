---
title: "获取权限列表"
source_url: "https://open.dingtalk.com/document/development/get-the-storage-permission-list"
namespace: "development"
slug: "get-the-storage-permission-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 存储管理 > 权限管理 > 获取权限列表"
doc_id: "uXr0mSl7Jh"
updated_at: "2026-08-25 09:38:58"
---

> Source: https://open.dingtalk.com/document/development/get-the-storage-permission-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 存储管理 > 权限管理 > 获取权限列表
> Updated: 2026-08-25 09:38:58

# 获取权限列表

调用本接口，获取存储空间的权限列表。

> **[!IMPORTANT]**
>
> - 新老接口中的ID不兼容, 不支持混用。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取权限列表](0684-get-permission-list.md)接口，已接入用户不受影响。

例如，在对某个存储空间执行查询操作之前，需要先判断当前用户是否拥有对应的权限。
调用本接口可查询某个存储空间内的权限列表。

> **[!NOTE]**
>
> - 存储空间类型为USER时，只有空间拥有者和管理者有操作权限，其他员工均需要授权。
> - 存储空间类型为APP时，任何人操作都需要先进行授权。.
>
> 可调用[添加权限](1598-add-storage-permissions.md)接口进行授权。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/permissions/query?unionId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "option" : {
    "nextToken" : "String",
    "maxResults" : Integer,
    "filterRoleIds" : [ "String" ]
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
| spaceId | String | 是 | 空间Id，调用[添加空间](0652-add-space.md)接口获取id参数值。  **[!NOTE]**  如果空间类型为APP时，当前操作人只能查看本人在该空间内的权限，不能查看全部的权限。 |
| dentryId | String | 是 | 文件或文件夹Id，调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取id参数值。  **[!NOTE]**  该参数值传0时，获取的是空间根目录的权限列表信息。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者的unionId，调用[查询用户详情](0056-query-user-details.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| option | Object | 否 | 可选参数。 |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 每页条目数，默认值50，最大值500。 |
| filterRoleIds | Array of String | 否 | 需要查询的角色Id列表，最大值30。  例如该参数传EDITOR，本接口只查询EDITOR权限列表。   - **OWNER**：拥有者 - **MANAGER**：管理者 - **EDITOR**：编辑者 - **DOWNLOADER**：下载者 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| permissions | Array | 权限列表。 |
| spaceId | String | 空间Id。 |
| dentryId | String | 文件或文件夹Id，0表示本空间。 |
| member | Object | 权限成员。 |
| type | String | 权限成员类型：   - **ORG**：企业 - **DEPT**：部门 - **TAG**：自定义tag - **CONVERSATION**：会话 - **USER**：用户 |
| id | String | 权限成员id。   - 如果type参数值为ORG，该参数值表示企业corpId。 - 如果type参数值为DEPT，该参数值表示部门deptId。 - 如果type参数值为TAG，该参数值表示tag名称。 - 如果type参数值为CONVERSATION，该参数值表示会话openConversationId。 - 如果type参数值为USER，该参数表示用户unionId。 |
| corpId | String | 权限归属的企业corpId。 |
| role | Object | 权限角色。 |
| id | String | 权限角色id。 |
| name | String | 角色名称。 |
| duration | Long | 有效时间。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| operatorId | String | 操作者unionId。 |
| nextToken | String | 分页游标。  **[!NOTE]**  该字段不为空，表示有更多数据。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/storage/spaces/854xxxxx/dentries/0/permissions/query?unionId=cHtUYxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "option" : {
    "nextToken" : "next_token",
    "maxResults" : 30,
    "filterRoleIds" : [ "EDITOR" ]
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
        ListPermissionsHeaders listPermissionsHeaders = new ListPermissionsHeaders();
        listPermissionsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListPermissionsRequest.ListPermissionsRequestOption option = new ListPermissionsRequest.ListPermissionsRequestOption()
                .setNextToken("next_token")
                .setMaxResults(30)
                .setFilterRoleIds(java.util.Arrays.asList(
                    "EDITOR"
                ));
        ListPermissionsRequest listPermissionsRequest = new ListPermissionsRequest()
                .setUnionId("cHtUYxxxxx")
                .setOption(option);
        try {
            client.listPermissionsWithOptions("854xxxxx", "0", listPermissionsRequest, listPermissionsHeaders, new RuntimeOptions());
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
        list_permissions_headers = dingtalkstorage__1__0_models.ListPermissionsHeaders()
        list_permissions_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.ListPermissionsRequestOption(
            next_token='next_token',
            max_results=30,
            filter_role_ids=[
                'EDITOR'
            ]
        )
        list_permissions_request = dingtalkstorage__1__0_models.ListPermissionsRequest(
            union_id='cHtUYxxxxx',
            option=option
        )
        try:
            client.list_permissions_with_options('854xxxxx', '0', list_permissions_request, list_permissions_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_permissions_headers = dingtalkstorage__1__0_models.ListPermissionsHeaders()
        list_permissions_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.ListPermissionsRequestOption(
            next_token='next_token',
            max_results=30,
            filter_role_ids=[
                'EDITOR'
            ]
        )
        list_permissions_request = dingtalkstorage__1__0_models.ListPermissionsRequest(
            union_id='cHtUYxxxxx',
            option=option
        )
        try:
            await client.list_permissions_with_options_async('854xxxxx', '0', list_permissions_request, list_permissions_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListPermissionsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListPermissionsRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListPermissionsRequest;
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
        $listPermissionsHeaders = new ListPermissionsHeaders([]);
        $listPermissionsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "nextToken" => "next_token",
            "maxResults" => 30,
            "filterRoleIds" => [
                "EDITOR"
            ]
        ]);
        $listPermissionsRequest = new ListPermissionsRequest([
            "unionId" => "cHtUYxxxxx",
            "option" => $option
        ]);
        try {
            $client->listPermissionsWithOptions("854xxxxx", "0", $listPermissionsRequest, $listPermissionsHeaders, new RuntimeOptions([]));
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

  listPermissionsHeaders := &dingtalkstorage_1_0.ListPermissionsHeaders{}
  listPermissionsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.ListPermissionsRequestOption{
    NextToken: tea.String("next_token"),
    MaxResults: tea.Int32(30),
    FilterRoleIds: []*string{tea.String("EDITOR")},
  }
  listPermissionsRequest := &dingtalkstorage_1_0.ListPermissionsRequest{
    UnionId: tea.String("cHtUYxxxxx"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListPermissionsWithOptions(tea.String("854xxxxx"), tea.String("0"), listPermissionsRequest, listPermissionsHeaders, &util.RuntimeOptions{})
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
    let listPermissionsHeaders = new $dingtalkstorage_1_0.ListPermissionsHeaders({ });
    listPermissionsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let option = new $dingtalkstorage_1_0.ListPermissionsRequestOption({
      nextToken: "next_token",
      maxResults: 30,
      filterRoleIds: [
        "EDITOR"
      ],
    });
    let listPermissionsRequest = new $dingtalkstorage_1_0.ListPermissionsRequest({
      unionId: "cHtUYxxxxx",
      option: option,
    });
    try {
      await client.listPermissionsWithOptions("854xxxxx", "0", listPermissionsRequest, listPermissionsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListPermissionsHeaders listPermissionsHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListPermissionsHeaders();
            listPermissionsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListPermissionsRequest.ListPermissionsRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListPermissionsRequest.ListPermissionsRequestOption
            {
                NextToken = "next_token",
                MaxResults = 30,
                FilterRoleIds = new List<string>
                {
                    "EDITOR"
                },
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListPermissionsRequest listPermissionsRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListPermissionsRequest
            {
                UnionId = "cHtUYxxxxx",
                Option = option,
            };
            try
            {
                client.ListPermissionsWithOptions("854xxxxx", "0", listPermissionsRequest, listPermissionsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "permissions" : [ {
    "spaceId" : "854xxxxx",
    "dentryId" : "0",
    "member" : {
      "type" : "USER",
      "id" : "cHtUYxxxxx",
      "corpId" : "ding123xxxxx"
    },
    "role" : {
      "id" : "MANAGER",
      "name" : "MANAGER"
    },
    "duration" : 3600,
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "operatorId" : "cxvxxxxx"
  } ],
  "nextToken" : "next_token"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | paramError.roleId | %s | 参数错误-roleId |
| 400 | spaceNotExist | %s | 空间不存在 |
| 400 | dentryNotExist | %s | 文件不存在 |
| 403 | permissionDenied | %s | 用户缺少获取权限列表的权限 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
