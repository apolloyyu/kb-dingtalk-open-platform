---
title: "在钉钉客联互通群中使用机器人发送消息"
source_url: "https://open.dingtalk.com/document/development/group-robots-send-messages"
namespace: "development"
slug: "group-robots-send-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 在钉钉客联互通群中使用机器人发送消息"
doc_id: "RGf2c17jLo"
updated_at: "2026-08-28 10:26:42"
---

> Source: https://open.dingtalk.com/document/development/group-robots-send-messages
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 钉钉客联 > 在钉钉客联互通群中使用机器人发送消息
> Updated: 2026-08-28 10:26:42

# 在钉钉客联互通群中使用机器人发送消息

调用本接口，通过互通群内机器人向群内发送消息，本接口只支持互通普通群和跨钉两人群使用，钉外两人群和店铺群暂不支持机器人发送群消息且仅针对钉钉客联创建的会话生效。

> **[!IMPORTANT]**
>
> - 在创建互通群时，会自动添加群内机器人，调用本接口可使用内置的群机器人发送群消息。
> - 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## **消息格式说明**

本接口支持的群消息类型有文本、图片、markdown和卡片。

- **文本信息**

  ```
  { "content": "我就是我, 是不一样的烟火"}
  ```
- **图片信息**

  > **[!NOTE]**
  >
  > 图片地址需为图片上传后的http或者https的url地址。

  ```
  {"img_media_id": "https://lmg.jj20.com/up/axxxx55-0-lp.jpg"}
  ```
- **markdown信息**

  ```
  {
    "title": "标题",
    "markdown_content": "# 测试内容"
  }
  ```
- **卡片信息**

  ```
  {
    "title": "标题",
    "markdown": "# 测试内容",
    "btn_orientation": "1",
    "btn_title_1": "btn_title_1",
    "action_url_1": "https://www.dingtalk.com/",
    "btn_title_2": "btn_title_2",
    "action_url_2": "https://www.dingtalk.com/",
    "btn_title_3": "btn_title_3",
    "action_url_3": "suitezlqnkv2atcpimsjn_actioncard1",
    "btn_title_4": "btn_title_4",
    "action_url_4": "https://www.dingtalk.com/"
  }
  ```

  **actionCard占位符key值**

  | key | 说明 |
  | --- | --- |
  | title | 会话列表显示标题。 |
  | markdown | 消息内容，支持markdown语法。 |
  | btn\_orientation | 按钮排列方向，仅2个按钮时有效，传值为0时为竖直排列，传值为1时水平排列。 |
  | btn\_title\_1 ~ btn\_title\_4 | 按钮文案，支持最多4个按钮，传空或不传则按钮不显示。 |
  | action\_url\_1 ~ action\_url\_4 | 按钮跳转地址，支持最多4个按钮，传空或不传则按钮不显示。 |

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/im/interconnections/robotMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "openConversationIds" : [ "String" ],
  "robotCode" : "String",
  "msgType" : "String",
  "msgContent" : "String",
  "atDingUserId" : "String",
  "atAppUserId" : "String",
  "atAll" : Boolean
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationIds | Array of String | 是 | 群会话openConversationId，可调用[创建钉钉客联普通互通群](1848-create-common-group-new-version.md) / [创建钉钉客联两人互通群](1849-creating-two-groups-of-people.md)接口获取，长度限制为1～32个字符。 |
| robotCode | String | 否 | 机器人robotId即robotCode，在客联应用的机器人管理中获取robotCode。 |
| msgType | String | 是 | 消息类型，取值：   - **text**：文本消息 - **photo**：图片信息 - **markdown**：markdown消息 - **actionCard**：卡片消息 |
| msgContent | String | 是 | 消息体内容，请参考本文消息格式说明。 |
| atDingUserId | String | 否 | 钉内账号userId，长度限制为1～64个字符。 |
| atAppUserId | String | 否 | 钉外账号在业务系统内的唯一标志，可调用[创建钉钉客联钉外账号](1847-create-bc-account-association.md)接口获取，长度限制为1～64个字符。 |
| atAll | Boolean | 否 | 是否@群所有人：   - **true**：是 - **false**：否 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 是否发送成功：   - **true**：成功 - **false**：失败 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/robotMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "openConversationIds" : [ "1745****8777" ],
  "robotCode" : "kelian-cuxxxxobot-101",
  "msgType" : "text",
  "msgContent" : "{ \"content\": \"我就是我, 是不一样的烟火\"}",
  "atDingUserId" : "1107****2120",
  "atAppUserId" : "1107****2120",
  "atAll" : true
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
        com.aliyun.dingtalkim_1_0.models.SendRobotMessageHeaders sendRobotMessageHeaders = new com.aliyun.dingtalkim_1_0.models.SendRobotMessageHeaders();
        sendRobotMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.SendRobotMessageRequest sendRobotMessageRequest = new com.aliyun.dingtalkim_1_0.models.SendRobotMessageRequest()
                .setOpenConversationIds(java.util.Arrays.asList(
                    "1745****8777"
                ))
                .setRobotCode("kelian-cuxxxxobot-101")
                .setMsgType("text")
                .setMsgContent("{ \"content\": \"我就是我, 是不一样的烟火\"}")
                .setAtDingUserId("1107****2120")
                .setAtAppUserId("1107****2120")
                .setAtAll(true);
        try {
            client.sendRobotMessageWithOptions(sendRobotMessageRequest, sendRobotMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        send_robot_message_headers = dingtalkim__1__0_models.SendRobotMessageHeaders()
        send_robot_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_robot_message_request = dingtalkim__1__0_models.SendRobotMessageRequest(
            open_conversation_ids=[
                '1745****8777'
            ],
            robot_code='kelian-cuxxxxobot-101',
            msg_type='text',
            msg_content='{ "content": "我就是我, 是不一样的烟火"}',
            at_ding_user_id='1107****2120',
            at_app_user_id='1107****2120',
            at_all=True
        )
        try:
            client.send_robot_message_with_options(send_robot_message_request, send_robot_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_robot_message_headers = dingtalkim__1__0_models.SendRobotMessageHeaders()
        send_robot_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_robot_message_request = dingtalkim__1__0_models.SendRobotMessageRequest(
            open_conversation_ids=[
                '1745****8777'
            ],
            robot_code='kelian-cuxxxxobot-101',
            msg_type='text',
            msg_content='{ "content": "我就是我, 是不一样的烟火"}',
            at_ding_user_id='1107****2120',
            at_app_user_id='1107****2120',
            at_all=True
        )
        try:
            await client.send_robot_message_with_options_async(send_robot_message_request, send_robot_message_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendRobotMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\SendRobotMessageRequest;
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
        $sendRobotMessageHeaders = new SendRobotMessageHeaders([]);
        $sendRobotMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendRobotMessageRequest = new SendRobotMessageRequest([
            "openConversationIds" => [
                "1745****8777"
            ],
            "robotCode" => "kelian-cuxxxxobot-101",
            "msgType" => "text",
            "msgContent" => "{ \"content\": \"我就是我, 是不一样的烟火\"}",
            "atDingUserId" => "1107****2120",
            "atAppUserId" => "1107****2120",
            "atAll" => true
        ]);
        try {
            $client->sendRobotMessageWithOptions($sendRobotMessageRequest, $sendRobotMessageHeaders, new RuntimeOptions([]));
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

  sendRobotMessageHeaders := &dingtalkim_1_0.SendRobotMessageHeaders{}
  sendRobotMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendRobotMessageRequest := &dingtalkim_1_0.SendRobotMessageRequest{
    OpenConversationIds: []*string{tea.String("1745****8777")},
    RobotCode: tea.String("kelian-cuxxxxobot-101"),
    MsgType: tea.String("text"),
    MsgContent: tea.String("{ \"content\": \"我就是我, 是不一样的烟火\"}"),
    AtDingUserId: tea.String("1107****2120"),
    AtAppUserId: tea.String("1107****2120"),
    AtAll: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendRobotMessageWithOptions(sendRobotMessageRequest, sendRobotMessageHeaders, &util.RuntimeOptions{})
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
    let sendRobotMessageHeaders = new dingtalkim_1_0.SendRobotMessageHeaders({ });
    sendRobotMessageHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let sendRobotMessageRequest = new dingtalkim_1_0.SendRobotMessageRequest({
      openConversationIds: [
        '1745****8777'
      ],
      robotCode: 'kelian-cuxxxxobot-101',
      msgType: 'text',
      msgContent: '{ "content": "我就是我, 是不一样的烟火"}',
      atDingUserId: '1107****2120',
      atAppUserId: '1107****2120',
      atAll: true,
    });
    try {
      await client.sendRobotMessageWithOptions(sendRobotMessageRequest, sendRobotMessageHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotMessageHeaders sendRobotMessageHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotMessageHeaders();
            sendRobotMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotMessageRequest sendRobotMessageRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.SendRobotMessageRequest
            {
                OpenConversationIds = new List<string>
                {
                    "1745****8777"
                },
                RobotCode = "kelian-cuxxxxobot-101",
                MsgType = "text",
                MsgContent = "{ \"content\": \"我就是我, 是不一样的烟火\"}",
                AtDingUserId = "1107****2120",
                AtAppUserId = "1107****2120",
                AtAll = true,
            };
            try
            {
                client.SendRobotMessageWithOptions(sendRobotMessageRequest, sendRobotMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "success" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否超出最大值或传参规则不正确 | 输入参数有误，请检查是否超出最大值或传参规则不正确 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | corp.robot.nonexist | 该组织机器人不存在，请检查 | 该组织机器人不存在，请检查 |
| 400 | msgContent.error | 发送消息体参数错误 | 发送消息体参数错误 |
| 400 | openConversationIds.error | openConversationIds中存在错误或失效群 | openConversationIds中存在错误或失效群 |
| 400 | image.url.error | 上传图片失败，请检查图片url是否可用或者图片大小超过1M | 上传图片失败，请检查图片url是否可用或者图片大小超过1M |
| 400 | atMember.nonexist | at的人员不存在或者不在群中 | at的人员不存在或者不在群中 |
| 400 | message.notSupportPhoto | 暂不支持发送图片 | 暂不支持发送图片 |
| 500 | robot.sendMessage.error | 机器人发送消息失败 | 机器人发送消息失败 |
| 500 | system.error | 系统异常 | 系统异常 |
