---
title: "创建客户群"
source_url: "https://open.dingtalk.com/document/development/create-a-customer-group"
namespace: "development"
slug: "create-a-customer-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 创建客户群"
doc_id: "PVk5TzO3B9"
updated_at: "2025-10-09 18:06:20"
---

> Source: https://open.dingtalk.com/document/development/create-a-customer-group
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户群 > 创建客户群
> Updated: 2025-10-09 18:06:20

# 创建客户群

调用本接口，用于创建客户群。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/groups |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Crm.CustomerGroup.Write-客户管理客户群写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| groupName | String | 是 | 群名称。 |
| ownerUserId | String | 是 | 群主userId。 |
| memberUserIds | String | 否 | 群成员userId。 |
| relationType | String | 是 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |

### 请求示例

HTTP

```
POST /v1.0/crm/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:abc
Content-Type:application/json

{
  "groupName" : "abc",
  "ownerUserId" : "abc123",
  "memberUserIds" : "a,b,c",
  "relationType" : "abc"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcrm_1_0.*;
import com.aliyun.dingtalkcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        CreateGroupHeaders createGroupHeaders = new CreateGroupHeaders();
        createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateGroupRequest createGroupRequest = new CreateGroupRequest()
                .setGroupName("abc")
                .setOwnerUserId("abc123")
                .setMemberUserIds("a,b,c")
                .setRelationType("abc");
        try {
            client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_group_headers = dingtalkcrm__1__0_models.CreateGroupHeaders()
        create_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_request = dingtalkcrm__1__0_models.CreateGroupRequest(
            group_name='abc',
            owner_user_id='abc123',
            member_user_ids='a,b,c',
            relation_type='abc'
        )
        try:
            client.create_group_with_options(create_group_request, create_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_group_headers = dingtalkcrm__1__0_models.CreateGroupHeaders()
        create_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_request = dingtalkcrm__1__0_models.CreateGroupRequest(
            group_name='abc',
            owner_user_id='abc123',
            member_user_ids='a,b,c',
            relation_type='abc'
        )
        try:
            await client.create_group_with_options_async(create_group_request, create_group_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\CreateGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\CreateGroupRequest;
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
        $createGroupHeaders = new CreateGroupHeaders([]);
        $createGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createGroupRequest = new CreateGroupRequest([
            "groupName" => "abc",
            "ownerUserId" => "abc123",
            "memberUserIds" => "a,b,c",
            "relationType" => "abc"
        ]);
        try {
            $client->createGroupWithOptions($createGroupRequest, $createGroupHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createGroupHeaders := &dingtalkcrm_1_0.CreateGroupHeaders{}
  createGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createGroupRequest := &dingtalkcrm_1_0.CreateGroupRequest{
    GroupName: tea.String("abc"),
    OwnerUserId: tea.String("abc123"),
    MemberUserIds: tea.String("a,b,c"),
    RelationType: tea.String("abc"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateGroupWithOptions(createGroupRequest, createGroupHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createGroupHeaders = new $dingtalkcrm_1_0.CreateGroupHeaders({ });
    createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createGroupRequest = new $dingtalkcrm_1_0.CreateGroupRequest({
      groupName: "abc",
      ownerUserId: "abc123",
      memberUserIds: "a,b,c",
      relationType: "abc",
    });
    try {
      await client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupHeaders createGroupHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupHeaders();
            createGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupRequest createGroupRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupRequest
            {
                GroupName = "abc",
                OwnerUserId = "abc123",
                MemberUserIds = "a,b,c",
                RelationType = "abc",
            };
            try
            {
                client.CreateGroupWithOptions(createGroupRequest, createGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| openConversationId | String | 创建的客户群openConversationId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openConversationId" : "abc"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | illegalParameter.groupName | 参数错误：群名称 | 参数错误：群名称 |
| 400 | illegalParameter.ownerUserId | 参数错误：群主id | 参数错误：群主id |
| 400 | illegalParameter | 参数错误：缺少必传参数 | 参数错误：缺少必传参数 |
| 400 | orgNotAuthed | 企业未完成高级认证 | 企业未完成高级认证 |
| 400 | ownerCantBeManager | 群主不能是群管理员 | 群主不能是群管理员 |
| 400 | duplicateOperation | 重复操作 | 重复操作 |
| 400 | creatorNotInOrg | 创建人已离职 | 创建人已离职 |
| 400 | groupRelationSchemaNotExist | 群关系模板不存在 | 群关系模板不存在 |
| 400 | groupQRCodeExpired | 对不起，由于群二维码配置失效，您的本次请求失败，请联系功能提供方 | 对不起，由于群二维码配置失效，您的本次请求失败，请联系功能提供方 |
| 500 | systemError.busy | 请求太频繁 | 请求被限流 |
| 500 | systemError | system error %s | 系统错误 |
