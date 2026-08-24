---
title: "获取群会话的OpenConversationId"
source_url: "https://open.dingtalk.com/document/development/obtain-group-openconversationid"
namespace: "development"
slug: "obtain-group-openconversationid"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 获取群会话的OpenConversationId"
doc_id: "tYVT3gUuIb"
updated_at: "2026-08-13 09:03:31"
---

> Source: https://open.dingtalk.com/document/development/obtain-group-openconversationid
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 群管理 > 获取群会话的OpenConversationId
> Updated: 2026-08-13 09:03:31

# 获取群会话的OpenConversationId

调用本接口，通过chatId查询OpenConversationId，适用于在创建群会话时未保存 OpenConversationId，后续业务需要使用该 ID 的场景。

## 接口调用说明

如果在调用[创建群会话](0738-create-common-group-new-version-v2.md)接口时没有保存OpenConversationId，可以通过调用本接口通过chatId获取OpenConversationId。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/chat/{chatId}/convertToOpenConversationId |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_read-钉钉群基础信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| chatId | String | 是 | 群会话chatId：   - **服务端**：通过[创建群会话](0738-create-common-group-new-version-v2.md)接口获取。 - **客户端**：通过[chooseChat](../03-Ogu5SlPY4t-客户端JSAPI/0318-jsapi-choose-chat.md)JSAPI获取。 |

### 请求示例

HTTP

```
POST /v1.0/im/chat/chatfaaxxxx3f061e/convertToOpenConversationId HTTP/1.1
Host:api.dingtalk.com
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
        ChatIdToOpenConversationIdHeaders chatIdToOpenConversationIdHeaders = new ChatIdToOpenConversationIdHeaders();
        chatIdToOpenConversationIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.chatIdToOpenConversationIdWithOptions("chatfaabe59a460527f5fb72fbbdfe3f061e", chatIdToOpenConversationIdHeaders, new RuntimeOptions());
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
        chat_id_to_open_conversation_id_headers = dingtalkim__1__0_models.ChatIdToOpenConversationIdHeaders()
        chat_id_to_open_conversation_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.chat_id_to_open_conversation_id_with_options('chatfaabe59a460527f5fb72fbbdfe3f061e', chat_id_to_open_conversation_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        chat_id_to_open_conversation_id_headers = dingtalkim__1__0_models.ChatIdToOpenConversationIdHeaders()
        chat_id_to_open_conversation_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.chat_id_to_open_conversation_id_with_options_async('chatfaabe59a460527f5fb72fbbdfe3f061e', chat_id_to_open_conversation_id_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\ChatIdToOpenConversationIdHeaders;
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
        $chatIdToOpenConversationIdHeaders = new ChatIdToOpenConversationIdHeaders([]);
        $chatIdToOpenConversationIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->chatIdToOpenConversationIdWithOptions("chatfaabe59a460527f5fb72fbbdfe3f061e", $chatIdToOpenConversationIdHeaders, new RuntimeOptions([]));
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

  chatIdToOpenConversationIdHeaders := &dingtalkim_1_0.ChatIdToOpenConversationIdHeaders{}
  chatIdToOpenConversationIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChatIdToOpenConversationIdWithOptions(tea.String("chatfaabe59a460527f5fb72fbbdfe3f061e"), chatIdToOpenConversationIdHeaders, &util.RuntimeOptions{})
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
    let chatIdToOpenConversationIdHeaders = new $dingtalkim_1_0.ChatIdToOpenConversationIdHeaders({ });
    chatIdToOpenConversationIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.chatIdToOpenConversationIdWithOptions("chatfaabe59a460527f5fb72fbbdfe3f061e", chatIdToOpenConversationIdHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChatIdToOpenConversationIdHeaders chatIdToOpenConversationIdHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChatIdToOpenConversationIdHeaders();
            chatIdToOpenConversationIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.ChatIdToOpenConversationIdWithOptions("chatfaabe59a460527f5fb72fbbdfe3f061e", chatIdToOpenConversationIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

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
  shared_ptr<Alibabacloud_Dingtalkim_1_0::ChatIdToOpenConversationIdHeaders> chatIdToOpenConversationIdHeaders = make_shared<Alibabacloud_Dingtalkim_1_0::ChatIdToOpenConversationIdHeaders>();
  chatIdToOpenConversationIdHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->chatIdToOpenConversationIdWithOptions(make_shared<string>("chatfaabe59a460527f5fb72fbbdfe3f061e"), chatIdToOpenConversationIdHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| openConversationId | String | 群会话openConversationId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openConversationId" : "cidl1B8RVUFmkO50OC9uEbySQ=="
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalideChatId | 不合法的chatId | 不合法的chatId |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
