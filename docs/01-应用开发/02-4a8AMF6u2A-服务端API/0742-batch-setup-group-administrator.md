---
title: "批量设置企业群管理员"
source_url: "https://open.dingtalk.com/document/development/batch-setup-group-administrator"
namespace: "development"
slug: "batch-setup-group-administrator"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 批量设置企业群管理员"
doc_id: "2e31sgGFPZ"
updated_at: "2026-06-15 10:56:53"
---

> Source: https://open.dingtalk.com/document/development/batch-setup-group-administrator
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 群管理 > 批量设置企业群管理员
> Updated: 2026-06-15 10:56:53

# 批量设置企业群管理员

调用本接口，可以批量设置企业群内用户为管理员身份， 也可以批量取消企业群内用户的管理员身份。本接口适用于企业群规模较大，需要批量调整群管理员以提高管理效率的场景或者企业组织架构调整，需要重新设置群管理员的场景。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/subAdministrators |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 开放群ID。可以调用[创建群会话](0738-create-common-group-new-version-v2.md)接口获取openConversationId参数值。 |
| userIds | Array of String | 是 | 企业员工userid列表。可以调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取userid\_list参数值。 |
| role | Integer | 是 | 设置类型，取值：   - **2**：添加为管理员 - **3**：删除该管理员 |

### 请求示例

HTTP

```
POST /v1.0/im/subAdministrators HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:862bcxxx
Content-Type:application/json

{
  "openConversationId" : "cidVwhmrlxsR3sL3+JdH1LjUA==",
  "userIds" : [ "wZ1vjnPOIdKrq_5c7As20B9RMTGJGy" ],
  "role" : 2
}
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
        ChatSubAdminUpdateHeaders chatSubAdminUpdateHeaders = new ChatSubAdminUpdateHeaders();
        chatSubAdminUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ChatSubAdminUpdateRequest chatSubAdminUpdateRequest = new ChatSubAdminUpdateRequest()
                .setOpenConversationId("cidVwhmrlxsR3sL3+JdH1LjUA==")
                .setUserIds(java.util.Arrays.asList(
                    "wZ1vjnPOIdKrq_5c7As20B9RMTGJGy"
                ))
                .setRole(2);
        try {
            client.chatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, new RuntimeOptions());
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
        chat_sub_admin_update_headers = dingtalkim__1__0_models.ChatSubAdminUpdateHeaders()
        chat_sub_admin_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        chat_sub_admin_update_request = dingtalkim__1__0_models.ChatSubAdminUpdateRequest(
            open_conversation_id='cidVwhmrlxsR3sL3+JdH1LjUA==',
            user_ids=[
                'wZ1vjnPOIdKrq_5c7As20B9RMTGJGy'
            ],
            role=2
        )
        try:
            client.chat_sub_admin_update_with_options(chat_sub_admin_update_request, chat_sub_admin_update_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        chat_sub_admin_update_headers = dingtalkim__1__0_models.ChatSubAdminUpdateHeaders()
        chat_sub_admin_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        chat_sub_admin_update_request = dingtalkim__1__0_models.ChatSubAdminUpdateRequest(
            open_conversation_id='cidVwhmrlxsR3sL3+JdH1LjUA==',
            user_ids=[
                'wZ1vjnPOIdKrq_5c7As20B9RMTGJGy'
            ],
            role=2
        )
        try:
            await client.chat_sub_admin_update_with_options_async(chat_sub_admin_update_request, chat_sub_admin_update_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\ChatSubAdminUpdateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\ChatSubAdminUpdateRequest;
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
        $chatSubAdminUpdateHeaders = new ChatSubAdminUpdateHeaders([]);
        $chatSubAdminUpdateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $chatSubAdminUpdateRequest = new ChatSubAdminUpdateRequest([
            "openConversationId" => "cidVwhmrlxsR3sL3+JdH1LjUA==",
            "userIds" => [
                "wZ1vjnPOIdKrq_5c7As20B9RMTGJGy"
            ],
            "role" => 2
        ]);
        try {
            $client->chatSubAdminUpdateWithOptions($chatSubAdminUpdateRequest, $chatSubAdminUpdateHeaders, new RuntimeOptions([]));
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

  chatSubAdminUpdateHeaders := &dingtalkim_1_0.ChatSubAdminUpdateHeaders{}
  chatSubAdminUpdateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  chatSubAdminUpdateRequest := &dingtalkim_1_0.ChatSubAdminUpdateRequest{
    OpenConversationId: tea.String("cidVwhmrlxsR3sL3+JdH1LjUA=="),
    UserIds: []*string{tea.String("wZ1vjnPOIdKrq_5c7As20B9RMTGJGy")},
    Role: tea.Int32(2),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, &util.RuntimeOptions{})
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
    let chatSubAdminUpdateHeaders = new $dingtalkim_1_0.ChatSubAdminUpdateHeaders({ });
    chatSubAdminUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let chatSubAdminUpdateRequest = new $dingtalkim_1_0.ChatSubAdminUpdateRequest({
      openConversationId: "cidVwhmrlxsR3sL3+JdH1LjUA==",
      userIds: [
        "wZ1vjnPOIdKrq_5c7As20B9RMTGJGy"
      ],
      role: 2,
    });
    try {
      await client.chatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChatSubAdminUpdateHeaders chatSubAdminUpdateHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChatSubAdminUpdateHeaders();
            chatSubAdminUpdateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChatSubAdminUpdateRequest chatSubAdminUpdateRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChatSubAdminUpdateRequest
            {
                OpenConversationId = "cidVwhmrlxsR3sL3+JdH1LjUA==",
                UserIds = new List<string>
                {
                    "wZ1vjnPOIdKrq_5c7As20B9RMTGJGy"
                },
                Role = 2,
            };
            try
            {
                client.ChatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkim_1_0::ChatSubAdminUpdateHeaders> chatSubAdminUpdateHeaders = make_shared<Alibabacloud_Dingtalkim_1_0::ChatSubAdminUpdateHeaders>();
  chatSubAdminUpdateHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkim_1_0::ChatSubAdminUpdateRequest> chatSubAdminUpdateRequest = make_shared<Alibabacloud_Dingtalkim_1_0::ChatSubAdminUpdateRequest>(map<string, boost::any>({
    {"openConversationId", boost::any(string("cidVwhmrlxsR3sL3+JdH1LjUA=="))},
    {"userIds", boost::any(vector<string>({
      "wZ1vjnPOIdKrq_5c7As20B9RMTGJGy"
    }))},
    {"role", boost::any(2)}
  }));
  try {
    client->chatSubAdminUpdateWithOptions(chatSubAdminUpdateRequest, chatSubAdminUpdateHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| success | String | 调用是否成功。true表示调用成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : "true"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.openConversationId.invalid | 无效的会话id | 无效的会话id |
| 400 | invalidParameter.orgId.invalid | 无效的企业ID | 无效的企业ID |
| 400 | invalid.staffid | 无效的userId | 无效的userId |
| 400 | subadmin.exceed | 管理员超限 | 管理员超限 |
| 400 | invalidParamter.role | 无效的role | 无效的role |
| 400 | staff.not.found | 员工不存在 | 员工不存在 |
| 400 | group.diaband | 群已经解散 | 群已经解散 |
| 500 | system.error | 系统错误 | 系统错误 |
