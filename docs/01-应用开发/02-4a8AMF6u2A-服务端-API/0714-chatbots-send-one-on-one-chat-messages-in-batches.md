---
title: "批量发送人与机器人会话中机器人消息"
source_url: "https://open.dingtalk.com/document/development/chatbots-send-one-on-one-chat-messages-in-batches"
namespace: "development"
slug: "chatbots-send-one-on-one-chat-messages-in-batches"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 发送普通消息 > 批量发送人与机器人会话中机器人消息"
doc_id: "yeB1dR8qqc"
updated_at: "2026-07-14 09:29:36"
---

> Source: https://open.dingtalk.com/document/development/chatbots-send-one-on-one-chat-messages-in-batches
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 发送普通消息 > 批量发送人与机器人会话中机器人消息
> Updated: 2026-07-14 09:29:36

# 批量发送人与机器人会话中机器人消息

调用本接口，批量发送人与机器人会话（人与机器人单聊）中机器人消息。适用于需要向多个用户（最多20个）批量发送机器人消息的场景，如企业通知、系统告警推送等场景。

## **接口调用说明**

本接口支持企业内部应用机器人，详情参考[配置企业机器人](../01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend |
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
| robotCode | String | 是 | 机器人的编码，该参数必须使用企业内部应用机器人的robotCode，详情参考[机器人 ID](0698-development-robot-overview.md#447ec33014hrl)。 |
| userIds | Array of String | 是 | 接收消息的用户userId列表，每次最多传20个，可通过[查询用户详情](0056-query-user-details.md)或[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| msgKey | String | 是 | 消息模板key，详情参考[消息发送与接收类型](0699-robot-message-type.md)。 |
| msgParam | String | 是 | 消息模板参数，消息模板参数，详情参考[消息发送与接收类型](0699-robot-message-type.md)。 |

### 请求示例

HTTP

```
POST /v1.0/robot/oToMessages/batchSend HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:asdasdasdasd
Content-Type:application/json

{
  "robotCode" : "dingxxxxxx",
  "userIds" : [ "manager1234" ],
  "msgKey" : "sampleMarkdown",
  "msgParam" : "{\"text\": \"hello text\",\"title\": \"hello title\"}"
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
        BatchSendOTOHeaders batchSendOTOHeaders = new BatchSendOTOHeaders();
        batchSendOTOHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchSendOTORequest batchSendOTORequest = new BatchSendOTORequest()
                .setRobotCode("dingxxxxxx")
                .setUserIds(java.util.Arrays.asList(
                    "manager1234"
                ))
                .setMsgKey("sampleMarkdown")
                .setMsgParam("{\"text\": \"hello text\",\"title\": \"hello title\"}");
        try {
            client.batchSendOTOWithOptions(batchSendOTORequest, batchSendOTOHeaders, new RuntimeOptions());
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
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = '<your access token>'
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code='dingxxxxxx',
            user_ids=[
                'manager1234'
            ],
            msg_key='sampleMarkdown',
            msg_param='{"text": "hello text","title": "hello title"}'
        )
        try:
            client.batch_send_otowith_options(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = '<your access token>'
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code='dingxxxxxx',
            user_ids=[
                'manager1234'
            ],
            msg_key='sampleMarkdown',
            msg_param='{"text": "hello text","title": "hello title"}'
        )
        try:
            await client.batch_send_otowith_options_async(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchSendOTOHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchSendOTORequest;
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
        $batchSendOTOHeaders = new BatchSendOTOHeaders([]);
        $batchSendOTOHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchSendOTORequest = new BatchSendOTORequest([
            "robotCode" => "dingxxxxxx",
            "userIds" => [
                "manager1234"
            ],
            "msgKey" => "sampleMarkdown",
            "msgParam" => "{\"text\": \"hello text\",\"title\": \"hello title\"}"
        ]);
        try {
            $client->batchSendOTOWithOptions($batchSendOTORequest, $batchSendOTOHeaders, new RuntimeOptions([]));
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

  batchSendOTOHeaders := &dingtalkrobot_1_0.BatchSendOTOHeaders{}
  batchSendOTOHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchSendOTORequest := &dingtalkrobot_1_0.BatchSendOTORequest{
    RobotCode: tea.String("dingxxxxxx"),
    UserIds: []*string{tea.String("manager1234")},
    MsgKey: tea.String("sampleMarkdown"),
    MsgParam: tea.String("{\"text\": \"hello text\",\"title\": \"hello title\"}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchSendOTOWithOptions(batchSendOTORequest, batchSendOTOHeaders, &util.RuntimeOptions{})
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
    let batchSendOTOHeaders = new $dingtalkrobot_1_0.BatchSendOTOHeaders({ });
    batchSendOTOHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let batchSendOTORequest = new $dingtalkrobot_1_0.BatchSendOTORequest({
      robotCode: "dingxxxxxx",
      userIds: [
        "manager1234"
      ],
      msgKey: "sampleMarkdown",
      msgParam: "{\"text\": \"hello text\",\"title\": \"hello title\"}",
    });
    try {
      await client.batchSendOTOWithOptions(batchSendOTORequest, batchSendOTOHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchSendOTOHeaders batchSendOTOHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchSendOTOHeaders();
            batchSendOTOHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchSendOTORequest batchSendOTORequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchSendOTORequest
            {
                RobotCode = "dingxxxxxx",
                UserIds = new List<string>
                {
                    "manager1234"
                },
                MsgKey = "sampleMarkdown",
                MsgParam = "{\"text\": \"hello text\",\"title\": \"hello title\"}",
            };
            try
            {
                client.BatchSendOTOWithOptions(batchSendOTORequest, batchSendOTOHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkrobot__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkrobot_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkrobot_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::Client> client = make_shared<Alibabacloud_Dingtalkrobot_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::BatchSendOTOHeaders> batchSendOTOHeaders = make_shared<Alibabacloud_Dingtalkrobot_1_0::BatchSendOTOHeaders>();
  batchSendOTOHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::BatchSendOTORequest> batchSendOTORequest = make_shared<Alibabacloud_Dingtalkrobot_1_0::BatchSendOTORequest>(map<string, boost::any>({
    {"robotCode", boost::any(string("dingxxxxxx"))},
    {"userIds", boost::any(vector<string>({
      "manager1234"
    }))},
    {"msgKey", boost::any(string("sampleMarkdown"))},
    {"msgParam", boost::any(string("{"text": "hello text","title": "hello title"}"))}
  }));
  try {
    client->batchSendOTOWithOptions(batchSendOTORequest, batchSendOTOHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| processQueryKey | String | 消息id，可用于[批量查询人与机器人会话机器人消息是否已读](0720-chatbot-batch-query-the-read-status-of-messages.md)和[批量撤回人与机器人会话中机器人消息](0723-batch-message-recall-chat.md)接口，查询消息是否已读和撤回消息。 |
| invalidStaffIdList | Array of String | 无效的用户userId列表。 |
| flowControlledStaffIdList | Array of String | 被限流的userId列表。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "processQueryKey" : "zcxxczasdafasd",
  "invalidStaffIdList" : [ "manage25231" ],
  "flowControlledStaffIdList" : [ "manage25232" ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.robotCode.empty | %s | 机器人robotCode无效 |
| 400 | invalidParameter.userIds.empty | %s | 用户userId列表为空 |
| 400 | invalidParameter.userIds.overMax | %s | 用户userId列表超过最大限制100,请将userId拆分成多个长度不超过100的数组，分批次调用此接口 |
| 400 | invalidParameter.msgKey.empty | %s | msgKey为空 |
| 400 | invalidParameter.msgKey.invalid | %s | msgKey无效，请传入正确的msgKey |
| 400 | invalidParameter.msgParam.invalid | %s | msgParam格式非法，必须是json格式 |
| 400 | invalidParameter.param.invalid | %s | 参数不合法，请检查是否有参数为空 |
| 400 | invalidParameter.msg.unsupport | %s | 不支持的消息类型 |
| 400 | invalidParameter.msgParam.tooLong | %s | 消息内容太长消息内容太长，请缩减内容长度 |
| 400 | invalidParameter.robotCode.notExsit | %s | 机器人不存在，请检查企业内是否安装了robotCode对应的机器人 |
| 400 | invalidParameter.msgBody.invalid | %s | 消息体必须是JSON格式 |
| 400 | invalidParameter.userId.empty | %s | 缺少staffId |
| 400 | invalidParameter.token.invalid | %s | 无授权的token |
| 400 | invalidParameter.robotCode.invalid | %s | 无效的robotCode |
| 400 | token.notExisted | %s | TOKEN不存在 |
| 400 | template.not.existed | %s | 机器人模板不存在，请检查robotCode是否正确 |
| 400 | template.stopped | %s | 机器人模板已经停用，请检查机器人状态 |
| 400 | miss.param.text | %s | 消息内容不合法，需要text属性 |
| 400 | miss.param.contentOfText | %s | 消息内容不合法，需要text->content属性 |
| 400 | miss.param.link | %s | 消息内容不合法，需要link属性 |
| 400 | miss.param.textOfLink | %s | 消息内容不合法，需要link->text属性 |
| 400 | miss.param.titleOfLink | %s | 消息内容不合法，需要link->title属性 |
| 400 | miss.param.messageUrlOfLink | %s | 消息内容不合法，需要link->messageUrl属性 |
| 400 | miss.param.markdown | %s | 消息内容不合法，需要markdown属性 |
| 400 | miss.param.markdownTotitle | %s | 消息内容不合法，需要markdown->text属性 |
| 400 | miss.param.markdownTotext | %s | 消息内容不合法，需要markdown->text属性 |
| 400 | miss.param.actionCard | %s | 消息内容不合法，需要actionCard属性 |
| 400 | miss.param.actionCardTotitle | %s | 消息内容不合法，需要actionCard->title属性 |
| 400 | miss.param.actionCardTotext | %s | 消息内容不合法，需要actionCard->text属性 |
| 400 | miss.param.actionCardTosingleTitle | %s | 消息内容不合法，需要actionCard->singleTitle属性 |
| 400 | miss.param.actionCardTosingleUrl | %s | 消息内容不合法，需要actionCard->singleURL属性 |
| 400 | miss.param.actionCardTobtns | %s | 消息内容不合法，需要actionCard->btns属性 |
| 400 | miss.param.actionCardTobtnsTotitle | %s | 消息内容不合法，需要actionCard->btns->title属性 |
| 400 | miss.param.actionCardTobtnsToactionUrl | %s | 消息内容不合法，需要actionCard->btns->actionURL属性 |
| 400 | invalid.param.actionCardTobtnOrientation | %s | 消息内容不合法，错误的actionCard->btnOrientation |
| 400 | invalid.param.actionCardTocanForward | %s | 消息内容不合法，错误的actionCard->canForward |
| 400 | miss.param.feedCard | %s | 消息内容不合法，需要feedCard属性 |
| 400 | miss.param.feedCardTolinks | %s | 消息内容不合法，需要feedCard->links属性 |
| 400 | miss.param.feedCardTolinksTotitle | %s | 消息内容不合法，需要feedCard->links->title属性 |
| 400 | miss.param.feedCardTolinksTomessageUrl | %s | 消息内容不合法，需要feedCard->links->messageURL属性 |
| 400 | miss.param.feedCardTolinksTopicUrl | %s | 消息内容不合法，需要feedCard->links->picURL属性 |
| 400 | miss.param.photo | %s | 消息内容不合法，需要photo属性 |
| 400 | miss.param.photoTophotoUrl | %s | 消息内容不合法，需要photo->photoURL属性 |
| 400 | miss.param.image | %s | 消息内容不合法，需要image属性 |
| 400 | miss.param.imageTopicUrl | %s | 消息内容不合法，需要image->picURL属性 |
| 400 | miss.param.beautifulCard | %s | 消息内容不合法，需要beautifulCard属性 |
| 400 | miss.param.beautifulCardToimage | %s | 消息内容不合法，需要beautifulCard->image属性 |
| 400 | miss.param.beautifulCardTotitle | %s | 消息内容不合法，需要beautifulCard->title属性 |
| 400 | miss.param.beautifulCardToactionUrl | %s | 消息内容不合法，需要beautifulCard->actionUrl属性 |
| 400 | miss.param.beautifulCardTointroduction | %s | 消息内容不合法，需要beautifulCard->introduction属性 |
| 400 | send.byToken.tooFast | %s | 用TOKEN发送限流错误，请稍后再试 |
| 400 | send.too.fast | %s | 发送消息频率过快，请稍后再试 |
| 400 | send.forbidden | %s | 此机器人禁止发送消息 |
| 400 | ip.not.match | %s | IP不匹配，无权限使用此机器人发送消息 |
| 400 | keywords.not.match | %s | 机器人发送消息的关键词不匹配 |
| 400 | sign.not.match | %s | 签名不匹配，无权限发送消息 |
| 400 | contain.unsafe.url | %s | 含有不安全的外链 |
| 400 | contain.notAllowed.text | %s | 含有不合适的文本 |
| 400 | contain.notAllowed.picture | %s | 含有不合适的图片 |
| 400 | contain.notAllowed.content | %s | 含有不合适的内容 |
| 400 | illegal.receivers | %s | 接收者名单不合法 |
| 400 | receivers.exceed | %s | 接收者名单超限 |
| 400 | illegal.excludes | %s | 不接收者名单不合法 |
| 400 | too.many.group | %s | 发送频繁限流 |
| 400 | too.many.people | %s | 发送频繁限流 |
| 400 | bot.forbidden.sendMessage | %s | 账户被禁言 |
| 400 | session.notExisted | %s | session不存在 |
| 400 | session.expired | %s | session已过期 |
| 400 | staffId.notExisted | %s | staffId不存在 |
| 400 | chatbotId.notAllow.sendOTO | %s | 不允许主动发单聊，请检查机器人状态是否已启用 |
| 400 | robot.oto.notExist | %s | 没有有效的机器人单聊会话 |
| 400 | sendMessage.model.notMatch | %s | 无匹配的消息模型 |
| 400 | miss.param.file | %s | 消息内容不合法，需要file属性 |
| 400 | miss.param.video | %s | 消息内容不合法，需要video->videoMediaId属性 |
| 400 | miss.param.audio | %s | 消息内容不合法，需要audio属性 |
| 500 | system.error | %s | 未知的系统错误 |
