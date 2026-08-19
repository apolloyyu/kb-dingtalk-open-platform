---
title: "创建场景服务群"
source_url: "https://open.dingtalk.com/document/development/create-a-scenario-service-group"
namespace: "development"
slug: "create-a-scenario-service-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 创建场景服务群"
doc_id: "UdNVgTsFMk"
updated_at: "2025-09-23 19:22:32"
---

> Source: https://open.dingtalk.com/document/development/create-a-scenario-service-group
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 服务群 > 创建场景服务群
> Updated: 2025-09-23 19:22:32

# 创建场景服务群

调用本接口创建场景服务群。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/groups |
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
| groupBizId | String | 否 | 业务关联ID，自定义参数值。 |
| openTeamId | String | 是 | 开放团队ID。 |
| openGroupSetId | String | 是 | 开放群组ID。 |
| groupName | String | 是 | 群名称。 |
| ownerStaffId | String | 是 | 群主员工userid。 |
| memberStaffIds | Array of String | 否 | 群成员员工ID列表，最大值20。 |
| groupTagNames | Array of String | 否 | 群标签。 |

### 请求示例

HTTP

```
POST /v1.0/serviceGroup/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a982f822xxxx
Content-Type:application/json

{
  "groupBizId" : "PID123cjj2",
  "openTeamId" : "Jciwnfw",
  "openGroupSetId" : "Jciwnfw",
  "groupName" : "测试服务群",
  "ownerStaffId" : "manager123",
  "memberStaffIds" : [ "user123" ],
  "groupTagNames" : [ "tag" ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkservice_group_1_0.*;
import com.aliyun.dingtalkservice_group_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkservice_group_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkservice_group_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkservice_group_1_0.Client client = Sample.createClient();
        CreateGroupHeaders createGroupHeaders = new CreateGroupHeaders();
        createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateGroupRequest createGroupRequest = new CreateGroupRequest()
                .setGroupBizId("PID123cjj2")
                .setOpenTeamId("Jciwnfw")
                .setOpenGroupSetId("Jciwnfw")
                .setGroupName("测试服务群")
                .setOwnerStaffId("manager123")
                .setMemberStaffIds(java.util.Arrays.asList(
                    "user123"
                ))
                .setGroupTagNames(java.util.Arrays.asList(
                    "tag"
                ));
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
        create_group_headers = dingtalkservice_group__1__0_models.CreateGroupHeaders()
        create_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_request = dingtalkservice_group__1__0_models.CreateGroupRequest(
            group_biz_id='PID123cjj2',
            open_team_id='Jciwnfw',
            open_group_set_id='Jciwnfw',
            group_name='测试服务群',
            owner_staff_id='manager123',
            member_staff_ids=[
                'user123'
            ],
            group_tag_names=[
                'tag'
            ]
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
        create_group_headers = dingtalkservice_group__1__0_models.CreateGroupHeaders()
        create_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_request = dingtalkservice_group__1__0_models.CreateGroupRequest(
            group_biz_id='PID123cjj2',
            open_team_id='Jciwnfw',
            open_group_set_id='Jciwnfw',
            group_name='测试服务群',
            owner_staff_id='manager123',
            member_staff_ids=[
                'user123'
            ],
            group_tag_names=[
                'tag'
            ]
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

use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\CreateGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\CreateGroupRequest;
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
            "groupBizId" => "PID123cjj2",
            "openTeamId" => "Jciwnfw",
            "openGroupSetId" => "Jciwnfw",
            "groupName" => "测试服务群",
            "ownerStaffId" => "manager123",
            "memberStaffIds" => [
                "user123"
            ],
            "groupTagNames" => [
                "tag"
            ]
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
  dingtalkservicegroup_1_0  "github.com/alibabacloud-go/dingtalk/serviceGroup_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  createGroupHeaders := &dingtalkservicegroup_1_0.CreateGroupHeaders{}
  createGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createGroupRequest := &dingtalkservicegroup_1_0.CreateGroupRequest{
    GroupBizId: tea.String("PID123cjj2"),
    OpenTeamId: tea.String("Jciwnfw"),
    OpenGroupSetId: tea.String("Jciwnfw"),
    GroupName: tea.String("测试服务群"),
    OwnerStaffId: tea.String("manager123"),
    MemberStaffIds: []*string{tea.String("user123")},
    GroupTagNames: []*string{tea.String("tag")},
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
    let createGroupHeaders = new $dingtalkserviceGroup_1_0.CreateGroupHeaders({ });
    createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createGroupRequest = new $dingtalkserviceGroup_1_0.CreateGroupRequest({
      groupBizId: "PID123cjj2",
      openTeamId: "Jciwnfw",
      openGroupSetId: "Jciwnfw",
      groupName: "测试服务群",
      ownerStaffId: "manager123",
      memberStaffIds: [
        "user123"
      ],
      groupTagNames: [
        "tag"
      ],
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
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.CreateGroupHeaders createGroupHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.CreateGroupHeaders();
            createGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.CreateGroupRequest createGroupRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.CreateGroupRequest
            {
                GroupBizId = "PID123cjj2",
                OpenTeamId = "Jciwnfw",
                OpenGroupSetId = "Jciwnfw",
                GroupName = "测试服务群",
                OwnerStaffId = "manager123",
                MemberStaffIds = new List<string>
                {
                    "user123"
                },
                GroupTagNames = new List<string>
                {
                    "tag"
                },
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkservice_group__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkservice_group_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkservice_group_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::Client> client = make_shared<Alibabacloud_Dingtalkservice_group_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::CreateGroupHeaders> createGroupHeaders = make_shared<Alibabacloud_Dingtalkservice_group_1_0::CreateGroupHeaders>();
  createGroupHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::CreateGroupRequest> createGroupRequest = make_shared<Alibabacloud_Dingtalkservice_group_1_0::CreateGroupRequest>(map<string, boost::any>({
    {"groupBizId", boost::any(string("PID123cjj2"))},
    {"openTeamId", boost::any(string("Jciwnfw"))},
    {"openGroupSetId", boost::any(string("Jciwnfw"))},
    {"groupName", boost::any(string("测试服务群"))},
    {"ownerStaffId", boost::any(string("manager123"))},
    {"memberStaffIds", boost::any(vector<string>({
      "user123"
    }))},
    {"groupTagNames", boost::any(vector<string>({
      "tag"
    }))}
  }));
  try {
    client->createGroupWithOptions(createGroupRequest, createGroupHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversationId | String | 开放群ID。 |
| groupUrl | String | 加群的url。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openConversationId" : "cidxxxxxx==",
  "groupUrl" : "http://qr.dingtalk.com/xxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | illegalPama | 参数非法 | 参数非法 |
| 500 | systemError | 系统异常 | 系统异常 |
