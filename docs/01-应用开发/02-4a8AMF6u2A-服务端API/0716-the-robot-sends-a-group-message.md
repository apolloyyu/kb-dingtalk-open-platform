---
title: "机器人发送群聊消息"
source_url: "https://open.dingtalk.com/document/development/the-robot-sends-a-group-message"
namespace: "development"
slug: "the-robot-sends-a-group-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 发送普通消息 > 机器人发送群聊消息"
doc_id: "D0ciWlxnVB"
updated_at: "2026-07-14 09:29:38"
---

> Source: https://open.dingtalk.com/document/development/the-robot-sends-a-group-message
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 发送普通消息 > 机器人发送群聊消息
> Updated: 2026-07-14 09:29:38

# 机器人发送群聊消息

本文档介绍了通过应用机器人发送群聊消息。

## 接口调用说明

本接口支持企业内部应用机器人，详情参考[创建企业内部应用机器人](../01-XOnnmGCTbn-开发指南/0076-configure-the-robot-application.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/groupMessages/send |
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
| msgParam | String | 是 | 消息模板参数，详情参考[消息发送与接收类型](0699-robot-message-type.md)。长度限制 15000 字节以内。 |
| msgKey | String | 是 | 消息模板key，详情参考[消息发送与接收类型](0699-robot-message-type.md)。 |
| openConversationId | String | 是 | 会话ID：   - 如果是企业内部群    - 新创建企业内部群，企业内部应用，可调用[创建企业内部群](https://open.dingtalk.com/document/development/create-group-session)接口获取。已存在的企业内部群，可调用[chooseChat](../03-Ogu5SlPY4t-客户端JSAPI/0318-jsapi-choose-chat.md)获取。 - 如果是场景群    - 企业内部应用，可调用[创建场景群](1486-create-a-scene-group-v2.md)接口获取。已存在的场景群，可调用 [chooseChat](https://open.dingtalk.com/document/orgapp/jsapi-choose-chat) 选择会话 JSAPI 获取。 |
| robotCode | String | 是 | 机器人的编码，详情参考[机器人 ID](0698-development-robot-overview.md)。 |
| coolAppCode | String | 否 | 群聊酷应用编码，详情参考[群聊酷应用](../01-XOnnmGCTbn-开发指南/0044-configuration-group-chat-quick-entry.md)。    当使用群聊酷应用的方式安装机器人时，**必须**传入此参数。 |

### 请求示例

HTTP

```
POST /v1.0/robot/groupMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:nvosnghskaknz8an3b82
Content-Type:application/json

{
  "msgParam" : "{\"content\":\"钉钉，让进步发生\"}",
  "msgKey" : "sampleText",
  "openConversationId" : "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
  "robotCode" : "dingue4kfzdxbynxxxxxx",
  "coolAppCode" : "COOLAPP-1-10182EEDD1AC0BA600D9000J"
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
        com.aliyun.dingtalkrobot_1_0.models.OrgGroupSendHeaders orgGroupSendHeaders = new com.aliyun.dingtalkrobot_1_0.models.OrgGroupSendHeaders();
        orgGroupSendHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.OrgGroupSendRequest orgGroupSendRequest = new com.aliyun.dingtalkrobot_1_0.models.OrgGroupSendRequest()
                .setMsgParam("{\"content\":\"钉钉，让进步发生\"}")
                .setMsgKey("sampleText")
                .setOpenConversationId("cid6KeBBLoveMJOGXoYKF5x7EeiodoA==")
                .setRobotCode("dingue4kfzdxbynxxxxxx")
                .setCoolAppCode("COOLAPP-1-10182EEDD1AC0BA600D9000J");
        try {
            client.orgGroupSendWithOptions(orgGroupSendRequest, orgGroupSendHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        org_group_send_headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        org_group_send_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_group_send_request = dingtalkrobot__1__0_models.OrgGroupSendRequest(
            msg_param='{"content":"钉钉，让进步发生"}',
            msg_key='sampleText',
            open_conversation_id='cid6KeBBLoveMJOGXoYKF5x7EeiodoA==',
            robot_code='dingue4kfzdxbynxxxxxx',
            cool_app_code='COOLAPP-1-10182EEDD1AC0BA600D9000J'
        )
        try:
            client.org_group_send_with_options(org_group_send_request, org_group_send_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        org_group_send_headers = dingtalkrobot__1__0_models.OrgGroupSendHeaders()
        org_group_send_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_group_send_request = dingtalkrobot__1__0_models.OrgGroupSendRequest(
            msg_param='{"content":"钉钉，让进步发生"}',
            msg_key='sampleText',
            open_conversation_id='cid6KeBBLoveMJOGXoYKF5x7EeiodoA==',
            robot_code='dingue4kfzdxbynxxxxxx',
            cool_app_code='COOLAPP-1-10182EEDD1AC0BA600D9000J'
        )
        try:
            await client.org_group_send_with_options_async(org_group_send_request, org_group_send_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\OrgGroupSendHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\OrgGroupSendRequest;
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
        $orgGroupSendHeaders = new OrgGroupSendHeaders([]);
        $orgGroupSendHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $orgGroupSendRequest = new OrgGroupSendRequest([
            "msgParam" => "{\"content\":\"钉钉，让进步发生\"}",
            "msgKey" => "sampleText",
            "openConversationId" => "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
            "robotCode" => "dingue4kfzdxbynxxxxxx",
            "coolAppCode" => "COOLAPP-1-10182EEDD1AC0BA600D9000J"
        ]);
        try {
            $client->orgGroupSendWithOptions($orgGroupSendRequest, $orgGroupSendHeaders, new RuntimeOptions([]));
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

  orgGroupSendHeaders := &dingtalkrobot_1_0.OrgGroupSendHeaders{}
  orgGroupSendHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  orgGroupSendRequest := &dingtalkrobot_1_0.OrgGroupSendRequest{
    MsgParam: tea.String("{\"content\":\"钉钉，让进步发生\"}"),
    MsgKey: tea.String("sampleText"),
    OpenConversationId: tea.String("cid6KeBBLoveMJOGXoYKF5x7EeiodoA=="),
    RobotCode: tea.String("dingue4kfzdxbynxxxxxx"),
    CoolAppCode: tea.String("COOLAPP-1-10182EEDD1AC0BA600D9000J"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.OrgGroupSendWithOptions(orgGroupSendRequest, orgGroupSendHeaders, &util.RuntimeOptions{})
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
    let orgGroupSendHeaders = new $dingtalkrobot_1_0.OrgGroupSendHeaders({ });
    orgGroupSendHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let orgGroupSendRequest = new $dingtalkrobot_1_0.OrgGroupSendRequest({
      msgParam: "{\"content\":\"钉钉，让进步发生\"}",
      msgKey: "sampleText",
      openConversationId: "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
      robotCode: "dingue4kfzdxbynxxxxxx",
      coolAppCode: "COOLAPP-1-10182EEDD1AC0BA600D9000J",
    });
    try {
      await client.orgGroupSendWithOptions(orgGroupSendRequest, orgGroupSendHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupSendHeaders orgGroupSendHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupSendHeaders();
            orgGroupSendHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupSendRequest orgGroupSendRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.OrgGroupSendRequest
            {
                MsgParam = "{\"content\":\"钉钉，让进步发生\"}",
                MsgKey = "sampleText",
                OpenConversationId = "cid6KeBBLoveMJOGXoYKF5x7EeiodoA==",
                RobotCode = "dingue4kfzdxbynxxxxxx",
                CoolAppCode = "COOLAPP-1-10182EEDD1AC0BA600D9000J",
            };
            try
            {
                client.OrgGroupSendWithOptions(orgGroupSendRequest, orgGroupSendHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| processQueryKey | String | 加密消息id，根据此id可查询消息已读状态和撤回消息，调用[查询人与人会话中机器人消息已读列表](0721-query-the-read-list-of-robot-messages-in-person-to-person-conversations.md)和[企业机器人撤回内部群消息](0725-enterprise-chatbot-withdraws-internal-group-messages.md)接口。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "processQueryKey" : "jkasdfb8va9hndjksnvzkj"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.robotCode.empty | 机器人robotCode为空 | 机器人robotCode无效，请检查机器人是否在群内 |
| 400 | invalidParameter.robotCode.auth | 此应用appkey和机器人robotCode不匹配，请使用机器人应用的appkey | 此应用appkey和机器人robotCode不匹配，请使用机器人应用的appkey |
| 400 | invalidParameter.robotCode.auth | 此应用suiteKey和机器人不匹配，请使用机器人绑定的ISV应用的suiteKey发送消息 | 此应用suiteKey和机器人不匹配，请使用机器人绑定的ISV应用的suiteKey发送消息 |
| 400 | invalidParameter.robotCode.coolApp | 酷应用编码无效 | 酷应用编码无效 |
| 400 | invalidParameter.robotCode.coolApp | 酷应用编码和机器人不匹配，请使用此酷应用绑定的机器人发送消息 | 酷应用编码和机器人不匹配，请使用此酷应用绑定的机器人发送消息 |
| 400 | invalidParameter.robotCode.coolApp | 绑定这个机器人的酷应用没有在群中被使用 | 绑定这个机器人的酷应用没有在群中被使用 |
| 400 | invalidParameter.robotCode.auth | 只有酷应用身份才可使用这个机器人 | 只有酷应用身份才可使用这个机器人 |
| 400 | invalidParameter.userIds.empty | 用户userId列表为空 | 用户userId列表为空 |
| 400 | invalidParameter.userIds.overMax | 用户userId列表超过最大限制 | 用户userId列表超过最大限制 |
| 400 | invalidParameter.msgKey.empty | 缺少msgKey | 缺少msgKey |
| 400 | invalidParameter.msgKey.invalid | msgKey无效 | msgKey无效 |
| 400 | invalidParameter.msgParam.invalid | msgParam必须是json格式 | msgParam必须是json格式 |
| 400 | invalidParameter.param.invalid | 参数不合法 | 参数不合法 |
| 400 | invalidParameter.msg.unsupport | 不支持的消息类型 | 不支持的消息类型 |
| 400 | invalidParameter.msgParam.tooLong | 消息内容太长 | 消息内容太长 |
| 400 | invalidParameter.robotCode.notExsit | 机器人不存在 | 机器人不存在 |
| 400 | unknown.send.result | 未知的发送结果 | 未知的发送结果 |
| 400 | invalidParameter.msgBody.invalid | body必须是JSON | body必须是JSON |
| 400 | invalidParameter.robotCode.missing | 缺少robotCode | 缺少robotCode |
| 400 | invalidParameter.userId.empty | 缺少staffId | 缺少staffId |
| 400 | invalidParameter.token.invalid | 无授权的token | 无授权的token |
| 400 | invalidParameter.processQueryKey.missing | 缺少processQueryKey | 缺少processQueryKey |
| 400 | invalidParameter.robotCode.invalid | 无效的robotCode | 无效的robotCode |
| 400 | invalid.processQueryKey | 无效的processQueryKey | 无效的processQueryKey |
| 400 | miss.openConversationId | 缺少openConversationId | 缺少openConversationId |
| 400 | invalid.openConversationId | 无效的openConversationId | 无效的openConversationId |
| 400 | group.disbanded | 群已经解散 | 群已经解散 |
| 400 | token.notExisted | TOKEN不存在 | TOKEN不存在 |
| 400 | bot.stopped | 群机器人已经停用 | 群机器人已经停用 |
| 400 | template.not.existed | 机器人模板不存在 | 机器人模板不存在 |
| 400 | template.stopped | 机器人模板已经停用 | 机器人模板已经停用 |
| 400 | miss.param.text | 需要text属性 | 需要text属性 |
| 400 | miss.param.contentOfText | 需要text->content属性 | 需要text->content属性 |
| 400 | miss.param.link | 需要link属性 | 需要link属性 |
| 400 | miss.param.textOfLink | 需要link->text属性 | 需要link->text属性 |
| 400 | miss.param.titleOfLink | 需要link->title属性 | 需要link->title属性 |
| 400 | miss.param.messageUrlOfLink | 需要link->messageUrl属性 | 需要link->messageUrl属性 |
| 400 | miss.param.markdown | 需要markdown属性 | 需要markdown属性 |
| 400 | miss.param.markdownTotitle | 需要markdown->text属性 | 需要markdown->text属性 |
| 400 | miss.param.markdownTotext | 需要markdown->text属性 | 需要markdown->text属性 |
| 400 | miss.param.actionCard | 需要actionCard属性 | 需要actionCard属性 |
| 400 | miss.param.actionCardTotitle | 需要actionCard->title属性 | 需要actionCard->title属性 |
| 400 | miss.param.actionCardTotext | 需要actionCard->text属性 | 需要actionCard->text属性 |
| 400 | miss.param.actionCardTosingleTitle | 需要actionCard->singleTitle属性 | 需要actionCard->singleTitle属性 |
| 400 | miss.param.actionCardTosingleUrl | 需要actionCard->singleURL属性 | 需要actionCard->singleURL属性 |
| 400 | miss.param.actionCardTobtns | 需要actionCard->btns属性 | 需要actionCard->btns属性 |
| 400 | miss.param.actionCardTobtnsTotitle | 需要actionCard->btns->title属性 | 需要actionCard->btns->title属性 |
| 400 | miss.param.actionCardTobtnsToactionUrl | 需要actionCard->btns->actionURL属性 | 需要actionCard->btns->actionURL属性 |
| 400 | invalid.param.actionCardTobtnOrientation | 错误的actionCard->btnOrientation | 错误的actionCard->btnOrientation |
| 400 | invalid.param.actionCardTocanForward | 错误的actionCard->canForward | 错误的actionCard->canForward |
| 400 | miss.param.feedCard | 需要feedCard属性 | 需要feedCard属性 |
| 400 | miss.param.feedCardTolinks | 需要feedCard->links属性 | 需要feedCard->links属性 |
| 400 | miss.param.feedCardTolinksTotitle | 需要feedCard->links->title属性 | 需要feedCard->links->title属性 |
| 400 | miss.param.feedCardTolinksTomessageUrl | 需要feedCard->links->messageURL属性 | 需要feedCard->links->messageURL属性 |
| 400 | miss.param.feedCardTolinksTopicUrl | 需要feedCard->links->picURL属性 | 需要feedCard->links->picURL属性 |
| 400 | miss.param.photo | 需要photo属性 | 需要photo属性 |
| 400 | miss.param.photoTophotoUrl | 需要photo->photoURL属性 | 需要photo->photoURL属性 |
| 400 | miss.param.image | 需要image属性 | 需要image属性 |
| 400 | miss.param.imageTopicUrl | 需要image->picURL属性 | 需要image->picURL属性 |
| 400 | miss.param.beautifulCard | 需要beautifulCard属性 | 需要beautifulCard属性 |
| 400 | miss.param.beautifulCardToimage | 需要beautifulCard->image属性 | 需要beautifulCard->image属性 |
| 400 | miss.param.beautifulCardTotitle | 需要beautifulCard->title属性 | 需要beautifulCard->title属性 |
| 400 | miss.param.beautifulCardToactionUrl | 需要beautifulCard->actionUrl属性 | 需要beautifulCard->actionUrl属性 |
| 400 | miss.param.beautifulCardTointroduction | 需要beautifulCard->introduction属性 | 需要beautifulCard->introduction属性 |
| 400 | send.byToken.tooFast | 用TOKEN发送限流错误 | 用TOKEN发送限流错误 |
| 400 | send.too.fast | 限流错误 | 限流错误 |
| 400 | send.forbidden | 禁止发送 | 禁止发送 |
| 400 | ip.not.match | IP不匹配 | IP不匹配 |
| 400 | keywords.not.match | 关键词不匹配 | 关键词不匹配 |
| 400 | sign.not.match | 签名不匹配 | 签名不匹配 |
| 400 | contain.unsafe.url | 含有不安全的外链 | 含有不安全的外链 |
| 400 | contain.notAllowed.text | 含有不合适的文本 | 含有不合适的文本 |
| 400 | contain.notAllowed.picture | 含有不合适的图片 | 含有不合适的图片 |
| 400 | contain.notAllowed.content | 含有不合适的内容 | 含有不合适的内容 |
| 400 | illegal.receivers | 接收者名单不合法 | 接收者名单不合法 |
| 400 | receivers.exceed | 接收者名单超限 | 接收者名单超限 |
| 400 | illegal.excludes | 不接收者名单不合法 | 不接收者名单不合法 |
| 400 | too.many.group | 发送频繁限流 | 发送频繁限流 |
| 400 | too.many.people | 发送频繁限流 | 发送频繁限流 |
| 400 | only.groupAdmin.canAtAll | 仅群主可@所有人 | 仅群主可@所有人 |
| 400 | bot.forbidden.sendMessage | 账户被禁言 | 账户被禁言 |
| 400 | session.notExisted | session不存在 | session不存在 |
| 400 | session.expired | session已过期 | session已过期 |
| 400 | staffId.notExisted | staffId不存在 | staffId不存在 |
| 400 | chatbotId.notAllow.sendOTO | 不允许主动发单聊 | 不允许主动发单聊 |
| 400 | robot.oto.notExist | 没有有效的机器人单聊会话 | 没有有效的机器人单聊会话 |
| 400 | sendMessage.model.notMatch | 无匹配的消息模型 | 无匹配的消息模型 |
| 400 | miss.param.file | %s | 消息内容不合法，需要file属性 |
| 400 | miss.param.video | %s | 消息内容不合法，需要video->videoMediaId属性 |
| 400 | miss.param.audio | %s | 消息内容不合法，需要audio属性 |
| 400 | conversation.org.notMatch | 会话所属组织信息不匹配 | 请确认token是否有权限操作对于此会话进行操作 |
| 400 | resource.not.found | %s | 资源不存在，可能是机器人不存在 |
| 400 | unauthorized | %s | 未授权 |
| 400 | auth.error | %s | 权限不足，不允许操作 |
| 400 | resource.unavailable | %s | 资源不可用，可能是机器人已停用或会话未安装酷应用 |
| 500 | system.error | 未知的系统错误 | 未知的系统错误 |
| 500 | send.ding.exception | 发送DING消息异常 | 发送DING消息异常 |
