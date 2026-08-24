---
title: "查询人与人会话中机器人消息已读列表"
source_url: "https://open.dingtalk.com/document/development/query-the-read-list-of-robot-messages-in-person-to-person-conversations"
namespace: "development"
slug: "query-the-read-list-of-robot-messages-in-person-to-person-conversations"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 消息查询 > 查询人与人会话中机器人消息已读列表"
doc_id: "TgYeILunOm"
updated_at: "2026-06-05 13:57:16"
---

> Source: https://open.dingtalk.com/document/development/query-the-read-list-of-robot-messages-in-person-to-person-conversations
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 消息查询 > 查询人与人会话中机器人消息已读列表
> Updated: 2026-06-05 13:57:16

# 查询人与人会话中机器人消息已读列表

调用本接口，根据群ID、机器人编码和消息ID，查询人与人会话中机器人消息的已读列表信息，适用于企业人员单聊沟通中需要确认机器人消息是否被阅读的场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/privateChatMessages/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_robot\_sendmsg-企业内机器人发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 否 | 人与人单聊开放会话ID，可通过[批量安装酷应用到单聊会话](../03-Ogu5SlPY4t-客户端JSAPI/0276-batch-chat-session.md)并监听[会话管理](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md#260a4e7084gs2)获取OpenConversationId参数值。 |
| robotCode | String | 否 | 机器人的编码，详情参考[机器人 ID](https://open.dingtalk.com/document/development/robot-overview)。 |
| processQueryKey | String | 是 | 消息id，可通过[创建并投放卡片](0783-create-and-deliver-cards.md)接口或[人与人会话中机器人发送普通消息](0715-the-robot-sends-ordinary-messages-in-a-person-to-person-conversation.md)接口，获取`processQueryKey`参数值。 |
| maxResults | Long | 否 | 分页查询每页的数量。 |
| nextToken | String | 否 | 一次查询后返回的加密的分页凭证，首次查询不填。 |

### 请求示例

HTTP

```
POST /v1.0/robot/privateChatMessages/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:8ca04016xxx
Content-Type:application/json

{
  "openConversationId" : "cid6KeBBLo******7EeiodoA==",
  "robotCode" : "ding******dxbyn0pjqd",
  "processQueryKey" : "Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
  "maxResults" : 50,
  "nextToken" : "50"
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
    public static com.aliyun.dingtalkrobot_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrobot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrobot_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrobot_1_0.models.PrivateChatQueryHeaders privateChatQueryHeaders = new com.aliyun.dingtalkrobot_1_0.models.PrivateChatQueryHeaders();
        privateChatQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.PrivateChatQueryRequest privateChatQueryRequest = new com.aliyun.dingtalkrobot_1_0.models.PrivateChatQueryRequest()
                .setOpenConversationId("cid6KeBBLo******7EeiodoA==")
                .setRobotCode("ding******dxbyn0pjqd")
                .setProcessQueryKey("Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=")
                .setMaxResults(50L)
                .setNextToken("50");
        try {
            client.privateChatQueryWithOptions(privateChatQueryRequest, privateChatQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrobot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrobot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        private_chat_query_headers = dingtalkrobot__1__0_models.PrivateChatQueryHeaders()
        private_chat_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        private_chat_query_request = dingtalkrobot__1__0_models.PrivateChatQueryRequest(
            open_conversation_id='cid6KeBBLo******7EeiodoA==',
            robot_code='ding******dxbyn0pjqd',
            process_query_key='Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=',
            max_results=50,
            next_token='50'
        )
        try:
            client.private_chat_query_with_options(private_chat_query_request, private_chat_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        private_chat_query_headers = dingtalkrobot__1__0_models.PrivateChatQueryHeaders()
        private_chat_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        private_chat_query_request = dingtalkrobot__1__0_models.PrivateChatQueryRequest(
            open_conversation_id='cid6KeBBLo******7EeiodoA==',
            robot_code='ding******dxbyn0pjqd',
            process_query_key='Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=',
            max_results=50,
            next_token='50'
        )
        try:
            await client.private_chat_query_with_options_async(private_chat_query_request, private_chat_query_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\PrivateChatQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\PrivateChatQueryRequest;
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
        $privateChatQueryHeaders = new PrivateChatQueryHeaders([]);
        $privateChatQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $privateChatQueryRequest = new PrivateChatQueryRequest([
            "openConversationId" => "cid6KeBBLo******7EeiodoA==",
            "robotCode" => "ding******dxbyn0pjqd",
            "processQueryKey" => "Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
            "maxResults" => 50,
            "nextToken" => "50"
        ]);
        try {
            $client->privateChatQueryWithOptions($privateChatQueryRequest, $privateChatQueryHeaders, new RuntimeOptions([]));
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
  dingtalkrobot_1_0  "github.com/alibabacloud-go/dingtalk/robot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrobot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrobot_1_0.Client{}
  _result, _err = dingtalkrobot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  privateChatQueryHeaders := &dingtalkrobot_1_0.PrivateChatQueryHeaders{}
  privateChatQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  privateChatQueryRequest := &dingtalkrobot_1_0.PrivateChatQueryRequest{
    OpenConversationId: tea.String("cid6KeBBLo******7EeiodoA=="),
    RobotCode: tea.String("ding******dxbyn0pjqd"),
    ProcessQueryKey: tea.String("Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q="),
    MaxResults: tea.Int64(50),
    NextToken: tea.String("50"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PrivateChatQueryWithOptions(privateChatQueryRequest, privateChatQueryHeaders, &util.RuntimeOptions{})
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
import dingtalkrobot_1_0, * as $dingtalkrobot_1_0 from '@alicloud/dingtalk/robot_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrobot_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrobot_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let privateChatQueryHeaders = new $dingtalkrobot_1_0.PrivateChatQueryHeaders({ });
    privateChatQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let privateChatQueryRequest = new $dingtalkrobot_1_0.PrivateChatQueryRequest({
      openConversationId: "cid6KeBBLo******7EeiodoA==",
      robotCode: "ding******dxbyn0pjqd",
      processQueryKey: "Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
      maxResults: 50,
      nextToken: "50",
    });
    try {
      await client.privateChatQueryWithOptions(privateChatQueryRequest, privateChatQueryHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrobot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrobot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.PrivateChatQueryHeaders privateChatQueryHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.PrivateChatQueryHeaders();
            privateChatQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.PrivateChatQueryRequest privateChatQueryRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.PrivateChatQueryRequest
            {
                OpenConversationId = "cid6KeBBLo******7EeiodoA==",
                RobotCode = "ding******dxbyn0pjqd",
                ProcessQueryKey = "Kna******pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
                MaxResults = 50,
                NextToken = "50",
            };
            try
            {
                client.PrivateChatQueryWithOptions(privateChatQueryRequest, privateChatQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| sendStatus | String | 消息发送状态。   - SUCCESS：成功 - RECALLED：已撤回 - PROCESSING：处理中 |
| readUserIds | Array of String | 消息已读人的userId列表。 |
| nextToken | String | 下次分页查询的加密凭证。 |
| hasMore | Boolean | 分页查询是否还有更多信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "sendStatus" : "SUCCESS",
  "readUserIds" : [ "123xxxx" ],
  "nextToken" : "Kna29******znx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
  "hasMore" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.param.invalid | 参数不合法 | 参数不合法，请检查参数是否为空 |
| 400 | invalidParameter.robotCode.notExsit | 机器人不存在 | 机器人不存在，请检查机器人是否在群内 |
| 400 | invalidParameter.robotCode.missing | 缺少robotCode | 缺少robotCode |
| 400 | invalidParameter.processQueryKey.missing | 缺少processQueryKey | 缺少processQueryKey |
| 400 | invalidParameter.cursor.invalid | 无效的nextToken | 无效的nextToken，请检查nextToken是否正确 |
| 400 | invalidParameter.pageSize.invalid | 无效的maxResults | maxResults超出上限200 |
| 400 | invalidParameter.robotCode.invalid | 无效的robotCode | 无效的robotCode |
| 400 | invalid.openConversationId | 无效的openConversationId | 无效的openConversationId |
| 400 | openConversationId.notExisted | openConversationId为空 | openConversationId为空 |
| 400 | invalid.processQueryKey | 无效的processQueryKey | 无效的processQueryKey |
| 400 | bot.stopped | 群机器人已经停用 | 群机器人已经停用 |
| 400 | template.not.existed | 机器人模板不存在 | 机器人模板不存在 |
| 400 | template.stopped | 机器人模板已经停用 | 机器人模板已经停用 |
| 400 | processQueryKey.expireTime | processQueryKey还未生成消息查询数据或已过期 | processQueryKey还未生成消息查询数据或已过期，无法查询消息 |
| 400 | conversation.org.dismatch | 会话不属于当前企业 | 会话不属于当前企业 |
| 400 | resource.not.found | %s | 机器人不存在 |
| 400 | unauthorized | %s | 未授权 |
| 400 | auth.error | %s | 权限不足，不允许操作 |
| 500 | system.error | 未知的系统错误 | 未知的系统错误 |
