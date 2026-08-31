---
title: "查询场景群禁言状态"
source_url: "https://open.dingtalk.com/document/development/query-group-silence-status"
namespace: "development"
slug: "query-group-silence-status"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群禁言状态"
doc_id: "5pLM3VRQar"
updated_at: "2026-08-14 09:41:55"
---

> Source: https://open.dingtalk.com/document/development/query-group-silence-status
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群禁言状态
> Updated: 2026-08-14 09:41:55

# 查询场景群禁言状态

通过本接口查询群和群内成员的禁言状态，适用于企业管理员需要查看群和群成员禁言状态的场景，如处理群内违规行为、管理群秩序等。

## 接口调用说明

支持以下场景使用：

- 基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/muteSettings |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_read-钉钉群基础信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 群成员userId。 |
| openConversationId | String | 是 | 群ID，通过[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`字段值。 |

### 请求示例

HTTP

```
GET /v1.0/im/sceneGroups/muteSettings?userId=004741900&openConversationId=cidCtneF+XyQjcyF2ROdgSeIg== HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2107d7ae16466433794062053d0587
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkim_1_0.*;
import com.aliyun.dingtalkim_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        QueryGroupMuteStatusHeaders queryGroupMuteStatusHeaders = new QueryGroupMuteStatusHeaders();
        queryGroupMuteStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryGroupMuteStatusRequest queryGroupMuteStatusRequest = new QueryGroupMuteStatusRequest()
                .setUserId("004741900")
                .setOpenConversationId("cidCtneF+XyQjcyF2ROdgSeIg==");
        try {
            client.queryGroupMuteStatusWithOptions(queryGroupMuteStatusRequest, queryGroupMuteStatusHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.im_1_0.client import Client as dingtalkim_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.im_1_0 import models as dingtalkim__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkim_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_group_mute_status_headers = dingtalkim__1__0_models.QueryGroupMuteStatusHeaders()
        query_group_mute_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_group_mute_status_request = dingtalkim__1__0_models.QueryGroupMuteStatusRequest(
            user_id='004741900',
            open_conversation_id='cidCtneF+XyQjcyF2ROdgSeIg=='
        )
        try:
            client.query_group_mute_status_with_options(query_group_mute_status_request, query_group_mute_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_group_mute_status_headers = dingtalkim__1__0_models.QueryGroupMuteStatusHeaders()
        query_group_mute_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_group_mute_status_request = dingtalkim__1__0_models.QueryGroupMuteStatusRequest(
            user_id='004741900',
            open_conversation_id='cidCtneF+XyQjcyF2ROdgSeIg=='
        )
        try:
            await client.query_group_mute_status_with_options_async(query_group_mute_status_request, query_group_mute_status_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QueryGroupMuteStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QueryGroupMuteStatusRequest;
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
        $queryGroupMuteStatusHeaders = new QueryGroupMuteStatusHeaders([]);
        $queryGroupMuteStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryGroupMuteStatusRequest = new QueryGroupMuteStatusRequest([
            "userId" => "004741900",
            "openConversationId" => "cidCtneF+XyQjcyF2ROdgSeIg=="
        ]);
        try {
            $client->queryGroupMuteStatusWithOptions($queryGroupMuteStatusRequest, $queryGroupMuteStatusHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkim_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkim_1_0.Client{}
  _result, _err = dingtalkim_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryGroupMuteStatusHeaders := &dingtalkim_1_0.QueryGroupMuteStatusHeaders{}
  queryGroupMuteStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryGroupMuteStatusRequest := &dingtalkim_1_0.QueryGroupMuteStatusRequest{
    UserId: tea.String("004741900"),
    OpenConversationId: tea.String("cidCtneF+XyQjcyF2ROdgSeIg=="),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryGroupMuteStatusWithOptions(queryGroupMuteStatusRequest, queryGroupMuteStatusHeaders, &util.RuntimeOptions{})
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
import dingtalkim_1_0, * as $dingtalkim_1_0 from '@alicloud/dingtalk/im_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkim_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkim_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryGroupMuteStatusHeaders = new $dingtalkim_1_0.QueryGroupMuteStatusHeaders({ });
    queryGroupMuteStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryGroupMuteStatusRequest = new $dingtalkim_1_0.QueryGroupMuteStatusRequest({
      userId: "004741900",
      openConversationId: "cidCtneF+XyQjcyF2ROdgSeIg==",
    });
    try {
      await client.queryGroupMuteStatusWithOptions(queryGroupMuteStatusRequest, queryGroupMuteStatusHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkim_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkim_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkim_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMuteStatusHeaders queryGroupMuteStatusHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMuteStatusHeaders();
            queryGroupMuteStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMuteStatusRequest queryGroupMuteStatusRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMuteStatusRequest
            {
                UserId = "004741900",
                OpenConversationId = "cidCtneF+XyQjcyF2ROdgSeIg==",
            };
            try
            {
                client.QueryGroupMuteStatusWithOptions(queryGroupMuteStatusRequest, queryGroupMuteStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkim__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkim_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkim_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkim_1_0::Client> client = make_shared<Alibabacloud_Dingtalkim_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkim_1_0::QueryGroupMuteStatusHeaders> queryGroupMuteStatusHeaders = make_shared<Alibabacloud_Dingtalkim_1_0::QueryGroupMuteStatusHeaders>();
  queryGroupMuteStatusHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkim_1_0::QueryGroupMuteStatusRequest> queryGroupMuteStatusRequest = make_shared<Alibabacloud_Dingtalkim_1_0::QueryGroupMuteStatusRequest>(map<string, boost::any>({
    {"userId", boost::any(string("004741900"))},
    {"openConversationId", boost::any(string("cidCtneF+XyQjcyF2ROdgSeIg=="))}
  }));
  try {
    client->queryGroupMuteStatusWithOptions(queryGroupMuteStatusRequest, queryGroupMuteStatusHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| groupMuteMode | Boolean | 群禁言状态。   - **true**：禁言。 - **false**：未禁言。 |
| userMuteResult | Object | 群禁言状态结果。 |
| userMuteMode | Boolean | 成员禁言状态。   - **true**：禁言。 - **false**：未禁言。 |
| muteStartTime | Long | 禁言开始时间。Unix时间戳，单位毫秒。 |
| muteEndTime | Long | 禁言结束时间。Unix时间戳，单位毫秒。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "groupMuteMode" : true,
  "userMuteResult" : {
    "userMuteMode" : true,
    "muteStartTime" : 1645315682000,
    "muteEndTime" : 1645315682000
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam.openConversationIdDecryptFailed | 会话ID解密失败 | 会话ID解密失败 |
| 400 | invalidParam.openConversationIdEmpry | 不合法的会话ID | 不合法的会话ID |
| 400 | group.org.checkFailed | 无权限，群不属于当前企业 | 无权限，群不属于当前企业 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 500 | systemInnerError | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
