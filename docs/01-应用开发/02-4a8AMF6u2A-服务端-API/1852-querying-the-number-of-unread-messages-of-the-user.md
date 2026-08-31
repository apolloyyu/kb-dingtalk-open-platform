---
title: "查询钉钉客联钉外账号未读消息数"
source_url: "https://open.dingtalk.com/document/development/querying-the-number-of-unread-messages-of-the-user"
namespace: "development"
slug: "querying-the-number-of-unread-messages-of-the-user"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 查询钉钉客联钉外账号未读消息数"
doc_id: "RshzjSg0ev"
updated_at: "2026-08-27 14:23:30"
---

> Source: https://open.dingtalk.com/document/development/querying-the-number-of-unread-messages-of-the-user
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 钉钉客联 > 查询钉钉客联钉外账号未读消息数
> Updated: 2026-08-27 14:23:30

# 查询钉钉客联钉外账号未读消息数

调用该接口，查询钉外账号未读消息的数量。

> **[!IMPORTANT]**
>
> 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## **接口说明**

- 可指定钉外账号标识查询所有该钉外账号所在群的未读消息数量。
- 可指定钉外账号标识和群会话openConversationId查询钉外账号在指定的群内未读消息数量。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/im/interconnections/unReadMsgs/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "appUserId" : "String",
  "openConversationIds" : [ "String" ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appUserId | String | 是 | 钉外账号在业务系统内的唯一标志，调用[创建钉钉客联钉外账号](1847-create-bc-account-association.md)接口获取，长度限制为1～64个字符。 |
| openConversationIds | Array of String | 否 | 群会话openConversationId，可调用[创建钉钉客联普通互通群](1848-create-common-group-new-version.md) / [创建钉钉客联两人互通群](1849-creating-two-groups-of-people.md)接口获取，长度限制为1～32个字符。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| unReadCount | Long | 钉外账号有未读消息的群会话总数。 |
| unReadItems | Array | 钉外账号未读消息列表。 |
| openConversationId | String | 群会话openConversationId。  **[!NOTE]**  客联的群会话id与钉钉IM的群会话ID不同，客联的群会话ID是随机生成的，在使用时不可混用。 |
| unReadCount | Long | 钉外账号对应群会话未读消息数。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/unReadMsgs/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "appUserId" : "1107****2120",
  "openConversationIds" : [ "14da****2760" ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_1_0.models.QueryUnReadMessageHeaders queryUnReadMessageHeaders = new com.aliyun.dingtalkim_1_0.models.QueryUnReadMessageHeaders();
        queryUnReadMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.QueryUnReadMessageRequest queryUnReadMessageRequest = new com.aliyun.dingtalkim_1_0.models.QueryUnReadMessageRequest()
                .setAppUserId("1107****2120")
                .setOpenConversationIds(java.util.Arrays.asList(
                    "14da****2760"
                ));
        try {
            client.queryUnReadMessageWithOptions(queryUnReadMessageRequest, queryUnReadMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_un_read_message_headers = dingtalkim__1__0_models.QueryUnReadMessageHeaders()
        query_un_read_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_un_read_message_request = dingtalkim__1__0_models.QueryUnReadMessageRequest(
            app_user_id='1107****2120',
            open_conversation_ids=[
                '14da****2760'
            ]
        )
        try:
            client.query_un_read_message_with_options(query_un_read_message_request, query_un_read_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_un_read_message_headers = dingtalkim__1__0_models.QueryUnReadMessageHeaders()
        query_un_read_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_un_read_message_request = dingtalkim__1__0_models.QueryUnReadMessageRequest(
            app_user_id='1107****2120',
            open_conversation_ids=[
                '14da****2760'
            ]
        )
        try:
            await client.query_un_read_message_with_options_async(query_un_read_message_request, query_un_read_message_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QueryUnReadMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QueryUnReadMessageRequest;
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
        $queryUnReadMessageHeaders = new QueryUnReadMessageHeaders([]);
        $queryUnReadMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryUnReadMessageRequest = new QueryUnReadMessageRequest([
            "appUserId" => "1107****2120",
            "openConversationIds" => [
                "14da****2760"
            ]
        ]);
        try {
            $client->queryUnReadMessageWithOptions($queryUnReadMessageRequest, $queryUnReadMessageHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
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

  queryUnReadMessageHeaders := &dingtalkim_1_0.QueryUnReadMessageHeaders{}
  queryUnReadMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryUnReadMessageRequest := &dingtalkim_1_0.QueryUnReadMessageRequest{
    AppUserId: tea.String("1107****2120"),
    OpenConversationIds: []*string{tea.String("14da****2760")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryUnReadMessageWithOptions(queryUnReadMessageRequest, queryUnReadMessageHeaders, &util.RuntimeOptions{})
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
const dingtalkim_1_0 = require('@alicloud/dingtalk/im_1_0');
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
    return new dingtalkim_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryUnReadMessageHeaders = new dingtalkim_1_0.QueryUnReadMessageHeaders({ });
    queryUnReadMessageHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryUnReadMessageRequest = new dingtalkim_1_0.QueryUnReadMessageRequest({
      appUserId: '1107****2120',
      openConversationIds: [
        '14da****2760'
      ],
    });
    try {
      await client.queryUnReadMessageWithOptions(queryUnReadMessageRequest, queryUnReadMessageHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryUnReadMessageHeaders queryUnReadMessageHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryUnReadMessageHeaders();
            queryUnReadMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryUnReadMessageRequest queryUnReadMessageRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryUnReadMessageRequest
            {
                AppUserId = "1107****2120",
                OpenConversationIds = new List<string>
                {
                    "14da****2760"
                },
            };
            try
            {
                client.QueryUnReadMessageWithOptions(queryUnReadMessageRequest, queryUnReadMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "unReadCount" : 10,
  "unReadItems" : [ {
    "openConversationId" : "14da****2760",
    "unReadCount" : 10
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否缺少必要参数或内容不正确 | 输入参数有误，请检查是否缺少必要参数或内容不正确 |
| 400 | group.nonexist | 群不存在，请检查 | 群不存在，请检查 |
| 400 | group.notReady | 群会话仍在创建中，请稍后重试 | 群会话仍在创建中，请稍后重试 |
| 500 | system.error | 系统异常 | 系统异常 |
