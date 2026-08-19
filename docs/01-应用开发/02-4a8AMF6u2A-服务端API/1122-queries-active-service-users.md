---
title: "查询服务群活跃用户"
source_url: "https://open.dingtalk.com/document/development/queries-active-service-users"
namespace: "development"
slug: "queries-active-service-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 查询服务群活跃用户"
doc_id: "AjrbM8o2jX"
updated_at: "2025-09-23 19:22:34"
---

> Source: https://open.dingtalk.com/document/development/queries-active-service-users
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 服务群 > 查询服务群活跃用户
> Updated: 2025-09-23 19:22:34

# 查询服务群活跃用户

调用本接口获取指定服务群内近期活跃的用户。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/groups/queryActiveUsers |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ServiceGroup.Group.ReadWrite-场景服务群读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openTeamId | String | 否 | 开放团队ID。 |
| openConversationId | String | 是 | 群ID。 |

### 请求示例

HTTP

```
GET /v1.0/serviceGroup/groups/queryActiveUsers?openTeamId=KxisoOk&openConversationId=cidxxxxxx==&topN=5 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b280cxxx
Content-Type:application/json
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
        QueryActiveUsersHeaders queryActiveUsersHeaders = new QueryActiveUsersHeaders();
        queryActiveUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryActiveUsersRequest queryActiveUsersRequest = new QueryActiveUsersRequest()
                .setOpenTeamId("KxisoOk")
                .setOpenConversationId("cidxxxxxx==")
                .setTopN(5L);
        try {
            client.queryActiveUsersWithOptions(queryActiveUsersRequest, queryActiveUsersHeaders, new RuntimeOptions());
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
        query_active_users_headers = dingtalkservice_group__1__0_models.QueryActiveUsersHeaders()
        query_active_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_active_users_request = dingtalkservice_group__1__0_models.QueryActiveUsersRequest(
            open_team_id='KxisoOk',
            open_conversation_id='cidxxxxxx==',
            top_n=5
        )
        try:
            client.query_active_users_with_options(query_active_users_request, query_active_users_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_active_users_headers = dingtalkservice_group__1__0_models.QueryActiveUsersHeaders()
        query_active_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_active_users_request = dingtalkservice_group__1__0_models.QueryActiveUsersRequest(
            open_team_id='KxisoOk',
            open_conversation_id='cidxxxxxx==',
            top_n=5
        )
        try:
            await client.query_active_users_with_options_async(query_active_users_request, query_active_users_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\QueryActiveUsersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\QueryActiveUsersRequest;
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
        $queryActiveUsersHeaders = new QueryActiveUsersHeaders([]);
        $queryActiveUsersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryActiveUsersRequest = new QueryActiveUsersRequest([
            "openTeamId" => "KxisoOk",
            "openConversationId" => "cidxxxxxx==",
            "topN" => 5
        ]);
        try {
            $client->queryActiveUsersWithOptions($queryActiveUsersRequest, $queryActiveUsersHeaders, new RuntimeOptions([]));
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

  queryActiveUsersHeaders := &dingtalkservicegroup_1_0.QueryActiveUsersHeaders{}
  queryActiveUsersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryActiveUsersRequest := &dingtalkservicegroup_1_0.QueryActiveUsersRequest{
    OpenTeamId: tea.String("KxisoOk"),
    OpenConversationId: tea.String("cidxxxxxx=="),
    TopN: tea.Int64(5),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryActiveUsersWithOptions(queryActiveUsersRequest, queryActiveUsersHeaders, &util.RuntimeOptions{})
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
    let queryActiveUsersHeaders = new $dingtalkserviceGroup_1_0.QueryActiveUsersHeaders({ });
    queryActiveUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryActiveUsersRequest = new $dingtalkserviceGroup_1_0.QueryActiveUsersRequest({
      openTeamId: "KxisoOk",
      openConversationId: "cidxxxxxx==",
      topN: 5,
    });
    try {
      await client.queryActiveUsersWithOptions(queryActiveUsersRequest, queryActiveUsersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.QueryActiveUsersHeaders queryActiveUsersHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.QueryActiveUsersHeaders();
            queryActiveUsersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.QueryActiveUsersRequest queryActiveUsersRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.QueryActiveUsersRequest
            {
                OpenTeamId = "KxisoOk",
                OpenConversationId = "cidxxxxxx==",
                TopN = 5,
            };
            try
            {
                client.QueryActiveUsersWithOptions(queryActiveUsersRequest, queryActiveUsersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::QueryActiveUsersHeaders> queryActiveUsersHeaders = make_shared<Alibabacloud_Dingtalkservice_group_1_0::QueryActiveUsersHeaders>();
  queryActiveUsersHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::QueryActiveUsersRequest> queryActiveUsersRequest = make_shared<Alibabacloud_Dingtalkservice_group_1_0::QueryActiveUsersRequest>(map<string, boost::any>({
    {"openTeamId", boost::any(string("KxisoOk"))},
    {"openConversationId", boost::any(string("cidxxxxxx=="))},
    {"topN", boost::any(5)}
  }));
  try {
    client->queryActiveUsersWithOptions(queryActiveUsersRequest, queryActiveUsersHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| activeUserInfos | Array | 活跃用户列表。  **[!NOTE]**  返回值为最活跃的用户TOP5，信息包含用户活跃度和行为指数。 |
| unionId | String | 用户unionId。 |
| nickName | String | 昵称。 |
| actionIndexL7d | double | 最近一周的行为指数。 |
| actionIndexL14d | double | 最近二周的行为指数。 |
| actionIndexL30d | double | 最近一个月的行为指数。 |
| activeScore | double | 活跃度。 |
| ranking | Long | 排名。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "activeUserInfos" : [ {
    "unionId" : "P7oD84mAHKbJ7grUw8c9ELAiEiE",
    "nickName" : "张三",
    "actionIndexL7d" : 7.5,
    "actionIndexL14d" : 10,
    "actionIndexL30d" : 10,
    "activeScore" : 8.75,
    "ranking" : 1
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | illegalPama | 参数非法 | 参数非法 |
| 500 | systemError | 系统异常 | 系统异常 |
