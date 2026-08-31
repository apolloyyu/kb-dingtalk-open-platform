---
title: "查询企业机器人群聊消息用户已读状态"
source_url: "https://open.dingtalk.com/document/development/chatbot-queries-the-read-status-of-a-message"
namespace: "development"
slug: "chatbot-queries-the-read-status-of-a-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 消息查询 > 查询企业机器人群聊消息用户已读状态"
doc_id: "wLxSK5YifM"
updated_at: "2026-06-05 13:49:01"
---

> Source: https://open.dingtalk.com/document/development/chatbot-queries-the-read-status-of-a-message
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 消息查询 > 查询企业机器人群聊消息用户已读状态
> Updated: 2026-06-05 13:49:01

# 查询企业机器人群聊消息用户已读状态

调用本接口可用于获取机器人消息发送状态、消息已读成员userId等信息，例如当企业机器人在内部群会话发送群聊消息后，使用本接口，能查询到已读用户的userId。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/groupMessages/query |
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
| openConversationId | String | 否 | 群ID，可通过客户端 [chooseChat](../03-Ogu5SlPY4t-客户端-JSAPI/0318-jsapi-choose-chat.md)获取群会话 openConversationId。  需要与[机器人发送群聊消息](0716-the-robot-sends-a-group-message.md)接口时使用的openConversationId一致。 |
| robotCode | String | 否 | 机器人的编码，详情参考[机器人 ID](https://open.dingtalk.com/document/development/robot-overview)。  需要与[机器人发送群聊消息](0716-the-robot-sends-a-group-message.md)接口时使用的robotCode一致。 |
| processQueryKey | String | 是 | 消息唯一标识，通过[机器人发送群聊消息](0716-the-robot-sends-a-group-message.md)接口返回参数processQueryKey字段中获取。 |
| maxResults | Long | 否 | 分页查询每页的数量，最大值200。 |
| nextToken | String | 否 | 分页游标，置空表示从首页开始查询。 |

### 请求示例

HTTP

```
POST /v1.0/robot/groupMessages/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:qkopsdangcfoonacviojsdjn
Content-Type:application/json

{
  "openConversationId" : "cid6KeBBL****5x7EeiodoA==",
  "robotCode" : "dingue****yn0pjqd",
  "processQueryKey" : "Kna29Ra5p*****DzgfxZLapw55G7x0Q=",
  "maxResults" : 50,
  "nextToken" : "50"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkrobot_1_0.*;
import com.aliyun.dingtalkrobot_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkrobot_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrobot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrobot_1_0.Client client = Sample.createClient();
        OrgGroupQueryHeaders orgGroupQueryHeaders = new OrgGroupQueryHeaders();
        orgGroupQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        OrgGroupQueryRequest orgGroupQueryRequest = new OrgGroupQueryRequest()
                .setOpenConversationId("cid6KeBBLoveMJOGXoYKF5x7EeiodoA==")
                .setRobotCode("dingue4kfzdxbyn0pjqd")
                .setProcessQueryKey("Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=")
                .setMaxResults(50L)
                .setNextToken("50");
        try {
            client.orgGroupQueryWithOptions(orgGroupQueryRequest, orgGroupQueryHeaders, new RuntimeOptions());
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
        org_group_query_headers = dingtalkrobot__1__0_models.OrgGroupQueryHeaders()
        org_group_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_group_query_request = dingtalkrobot__1__0_models.OrgGroupQueryRequest(
            open_conversation_id='cid6KeBBLoveMJOGXoYKF5x7EeiodoA==',
            robot_code='dingue4kfzdxbyn0pjqd',
            process_query_key='Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=',
            max_results=50,
            next_token='50'
        )
        try:
            client.org_group_query_with_options(org_group_query_request, org_group_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        org_group_query_headers = dingtalkrobot__1__0_models.OrgGroupQueryHeaders()
        org_group_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_group_query_request = dingtalkrobot__1__0_models.OrgGroupQueryRequest(
            open_conversation_id='cid6KeBBLoveMJOGXoYKF5x7EeiodoA==',
            robot_code='dingue4kfzdxbyn0pjqd',
            process_query_key='Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=',
            max_results=50,
            next_token='50'
        )
        try:
            await client.org_group_query_with_options_async(org_group_query_request, org_group_query_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\OrgGroupQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\OrgGroupQueryRequest;
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
        $orgGroupQueryHeaders = new OrgGroupQueryHeaders([]);
        $orgGroupQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $orgGroupQueryRequest = new OrgGroupQueryRequest([
            "openConversationId" => "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
            "robotCode" => "dingue4kfzdxbyn0pjqd",
            "processQueryKey" => "Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
            "maxResults" => 50,
            "nextToken" => "50"
        ]);
        try {
            $client->orgGroupQueryWithOptions($orgGroupQueryRequest, $orgGroupQueryHeaders, new RuntimeOptions([]));
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
  dingtalkrobot_1_0  "github.com/alibabacloud-go/dingtalk/robot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  orgGroupQueryHeaders := &dingtalkrobot_1_0.OrgGroupQueryHeaders{}
  orgGroupQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  orgGroupQueryRequest := &dingtalkrobot_1_0.OrgGroupQueryRequest{
    OpenConversationId: tea.String("cid6KeBBLoveMJOGXoYKF5x7EeiodoA=="),
    RobotCode: tea.String("dingue4kfzdxbyn0pjqd"),
    ProcessQueryKey: tea.String("Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q="),
    MaxResults: tea.Int64(50),
    NextToken: tea.String("50"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.OrgGroupQueryWithOptions(orgGroupQueryRequest, orgGroupQueryHeaders, &util.RuntimeOptions{})
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
    let orgGroupQueryHeaders = new $dingtalkrobot_1_0.OrgGroupQueryHeaders({ });
    orgGroupQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let orgGroupQueryRequest = new $dingtalkrobot_1_0.OrgGroupQueryRequest({
      openConversationId: "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
      robotCode: "dingue4kfzdxbyn0pjqd",
      processQueryKey: "Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
      maxResults: 50,
      nextToken: "50",
    });
    try {
      await client.orgGroupQueryWithOptions(orgGroupQueryRequest, orgGroupQueryHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupQueryHeaders orgGroupQueryHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupQueryHeaders();
            orgGroupQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupQueryRequest orgGroupQueryRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupQueryRequest
            {
                OpenConversationId = "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
                RobotCode = "dingue4kfzdxbyn0pjqd",
                ProcessQueryKey = "Kna29Ra5pdJznx1ghavbumkQKwDzgfxZLapw55G7x0Q=",
                MaxResults = 50,
                NextToken = "50",
            };
            try
            {
                client.OrgGroupQueryWithOptions(orgGroupQueryRequest, orgGroupQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| sendStatus | String | 消息发送状态：   - SUCCESS：成功 - RECALLED：已撤回 - PROCESSING：处理中 |
| readUserIds | Array of String | 消息已读人的userId。 |
| nextToken | String | 下次分页查询的游标。 |
| hasMore | Boolean | 分页查询是否还有人员可查询消息已读状态。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "sendStatus" : "SUCCESS",
  "readUserIds" : [ "manager1234" ],
  "nextToken" : "Kna29Ra5pdJ****mkQKwDzgfxZLapw55G7x0Q=",
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
| 400 | invalidParameter.invalid | token对应机器人不存在 | token对应机器人不存在，请检查机器人是否在群内 |
| 400 | invalidParameter.robotCode.invalid | 无效的robotCode | 无效的robotCode |
| 400 | invalid.openConversationId | 无效的openConversationId | 无效的openConversationId |
| 400 | openConversationId.notExisted | openConversationId不能和token同时为空 | openConversationId不能和token同时为空 |
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
