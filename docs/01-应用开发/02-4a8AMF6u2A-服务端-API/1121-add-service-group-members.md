---
title: "添加服务群成员"
source_url: "https://open.dingtalk.com/document/development/add-service-group-members"
namespace: "development"
slug: "add-service-group-members"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 添加服务群成员"
doc_id: "kx2sMzdKPC"
updated_at: "2026-06-03 09:11:04"
---

> Source: https://open.dingtalk.com/document/development/add-service-group-members
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 服务群 > 添加服务群成员
> Updated: 2026-06-03 09:11:04

# 添加服务群成员

调用本接口，将企业下成员添加到智能服务群中。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/groups/members |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ServiceGroup.Group.ReadWrite-场景服务群读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openTeamId | String | 是 | 开放团队ID。如下图所示，查看**ID信息**内的**团队ID**值。 |
| openConversationId | String | 是 | 服务群openConversionId，可调用[创建场景服务群](1120-create-a-scenario-service-group.md)接口获取openConversationId参数值。 |
| userIds | Array of String | 是 | 待添加员工在钉钉组织内的的userId列表，最大值100。  **[!NOTE]**    请确保userId值的正确性，如果userId值不正确，该接口不会报错，添加时会自动忽略该成员。 |

### 请求示例

HTTP

```
POST /v1.0/serviceGroup/groups/members HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "openTeamId" : "Jciwnfw",
  "openConversationId" : "cidxxxxxx==",
  "userIds" : [ "manager123" ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkservice_group_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkservice_group_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkservice_group_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupHeaders addMemberToServiceGroupHeaders = new com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupHeaders();
        addMemberToServiceGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupRequest addMemberToServiceGroupRequest = new com.aliyun.dingtalkservice_group_1_0.models.AddMemberToServiceGroupRequest()
                .setOpenTeamId("Jciwnfw")
                .setOpenConversationId("cidxxxxxx==")
                .setUserIds(java.util.Arrays.asList(
                    "manager123"
                ));
        try {
            client.addMemberToServiceGroupWithOptions(addMemberToServiceGroupRequest, addMemberToServiceGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.serviceGroup_1_0.client import Client as dingtalkserviceGroup_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.serviceGroup_1_0 import models as dingtalkservice_group__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkserviceGroup_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkserviceGroup_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_member_to_service_group_headers = dingtalkservice_group__1__0_models.AddMemberToServiceGroupHeaders()
        add_member_to_service_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_member_to_service_group_request = dingtalkservice_group__1__0_models.AddMemberToServiceGroupRequest(
            open_team_id='Jciwnfw',
            open_conversation_id='cidxxxxxx==',
            user_ids=[
                'manager123'
            ]
        )
        try:
            client.add_member_to_service_group_with_options(add_member_to_service_group_request, add_member_to_service_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_member_to_service_group_headers = dingtalkservice_group__1__0_models.AddMemberToServiceGroupHeaders()
        add_member_to_service_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_member_to_service_group_request = dingtalkservice_group__1__0_models.AddMemberToServiceGroupRequest(
            open_team_id='Jciwnfw',
            open_conversation_id='cidxxxxxx==',
            user_ids=[
                'manager123'
            ]
        )
        try:
            await client.add_member_to_service_group_with_options_async(add_member_to_service_group_request, add_member_to_service_group_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\AddMemberToServiceGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\AddMemberToServiceGroupRequest;
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
        $addMemberToServiceGroupHeaders = new AddMemberToServiceGroupHeaders([]);
        $addMemberToServiceGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addMemberToServiceGroupRequest = new AddMemberToServiceGroupRequest([
            "openTeamId" => "Jciwnfw",
            "openConversationId" => "cidxxxxxx==",
            "userIds" => [
                "manager123"
            ]
        ]);
        try {
            $client->addMemberToServiceGroupWithOptions($addMemberToServiceGroupRequest, $addMemberToServiceGroupHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkservicegroup_1_0  "github.com/alibabacloud-go/dingtalk/serviceGroup_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkservicegroup_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkservicegroup_1_0.Client{}
  _result, _err = dingtalkservicegroup_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addMemberToServiceGroupHeaders := &dingtalkservicegroup_1_0.AddMemberToServiceGroupHeaders{}
  addMemberToServiceGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addMemberToServiceGroupRequest := &dingtalkservicegroup_1_0.AddMemberToServiceGroupRequest{
    OpenTeamId: tea.String("Jciwnfw"),
    OpenConversationId: tea.String("cidxxxxxx=="),
    UserIds: []*string{tea.String("manager123")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddMemberToServiceGroupWithOptions(addMemberToServiceGroupRequest, addMemberToServiceGroupHeaders, &util.RuntimeOptions{})
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
import dingtalkserviceGroup_1_0, * as $dingtalkserviceGroup_1_0 from '@alicloud/dingtalk/serviceGroup_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkserviceGroup_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkserviceGroup_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addMemberToServiceGroupHeaders = new $dingtalkserviceGroup_1_0.AddMemberToServiceGroupHeaders({ });
    addMemberToServiceGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let addMemberToServiceGroupRequest = new $dingtalkserviceGroup_1_0.AddMemberToServiceGroupRequest({
      openTeamId: "Jciwnfw",
      openConversationId: "cidxxxxxx==",
      userIds: [
        "manager123"
      ],
    });
    try {
      await client.addMemberToServiceGroupWithOptions(addMemberToServiceGroupRequest, addMemberToServiceGroupHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.AddMemberToServiceGroupHeaders addMemberToServiceGroupHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.AddMemberToServiceGroupHeaders();
            addMemberToServiceGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.AddMemberToServiceGroupRequest addMemberToServiceGroupRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.AddMemberToServiceGroupRequest
            {
                OpenTeamId = "Jciwnfw",
                OpenConversationId = "cidxxxxxx==",
                UserIds = new List<string>
                {
                    "manager123"
                },
            };
            try
            {
                client.AddMemberToServiceGroupWithOptions(addMemberToServiceGroupRequest, addMemberToServiceGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 添加是否成功，true表示成功。 |

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
| 400 | illegalParameter | 参数非法 | 参数非法，openTeamId不正确 |
| 500 | invalidParameter | 参数无效 | 参数无效，openConversationId不正确 |
