---
title: "发送DING消息"
source_url: "https://open.dingtalk.com/document/development/robot-sends-nail-message"
namespace: "development"
slug: "robot-sends-nail-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 发送DING消息 > 发送DING消息"
doc_id: "b7OGbH7uqQ"
updated_at: "2026-06-05 13:37:43"
---

> Source: https://open.dingtalk.com/document/development/robot-sends-nail-message
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 发送DING消息 > 发送DING消息
> Updated: 2026-06-05 13:37:43

# 发送DING消息

调用本接口，可使用企业内机器人发送DING消息，可发送应用内DING、短信DING、电话DING。

## **接口调用说明**

当前接口为[钉钉专业版](dingtalk://dingtalkclient/page/link?spm=ding_open_doc.document.0.0.18684a70jkC6tM&url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fweb-dd-pro%2Fmobile_microApp%2Findex.html%3FcorpId%3D%26channel%3Dopenpf_web_devdoc_apiDING_trial&web_wnd=general&width=480&height=800)和[钉钉专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_apiDING_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)专享接口，仅限钉钉专业版和钉钉专属版客户使用，并可按需[增购OpenAPI发DING额度](https://oa.dingtalk.com/index.htm?spm=ding_open_doc.document.0.0.361d199cZS1M61#/dataCenter/dingOrder?_dlp_=channel%3Dopenpf_web_devdoc_apiDING)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/ding/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Ding.Write-企业机器人发送撤回DING消息 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| robotCode | String | 是 | 发DING消息的机器人ID，需填写创建企业内部应用机器人后获取的[机器人 ID](0698-development-robot-overview.md#447ec33014hrl)（robotCode）。 |
| remindType | Integer | 是 | DING消息类型：   - **1**：应用内DING - **2**：短信DING - **3**：电话DING      - 短信 DING 和电话 DING 需要单独购买权益包。本接口在没有购买短信 DING 和电话 DING的情况下，仅支持发送应用内 DING。 - 可登录[钉钉管理后台](https://oa.dingtalk.com/)，单击左侧导航栏增值服务 > 产品专区进行购买。 |
| receiverUserIdList | Array of String | 是 | 接收人userId列表，可通过[查询用户详情](0056-query-user-details.md)或[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。   - 应用内DING消息，每次接收人不能超过200个。 - 短信DING和电话DING，每次接收人不能超过20个。 |
| content | String | 是 | DING消息内容。 |
| callVoice | String | 否 | 电话音色，非电话DING该字段无效，目前支持的音色枚举值：   ``` - Standard_Female_Voice - Cantonese_Female_Voice - Gentine_Female_Voice - Overbearing_Female_Voice - Lovely_Girl_Voice - Standard_Male_Voice ```   若为空为标准女性音色。 |

### 请求示例

HTTP

```
POST /v1.0/robot/ding/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b9c5eb0772bf3a3283023ab67c*****
Content-Type:application/json

{
  "robotCode" : "dinggtkolxz1u****eqd",
  "remindType" : 1,
  "receiverUserIdList" : [ "manager7675" ],
  "content" : "钉钉，让进步发生",
  "callVoice" : "● Standard_Female_Voice"
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
    public static com.aliyun.dingtalkrobot_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrobot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkrobot_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrobot_1_0.models.RobotSendDingHeaders robotSendDingHeaders = new com.aliyun.dingtalkrobot_1_0.models.RobotSendDingHeaders();
        robotSendDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.RobotSendDingRequest robotSendDingRequest = new com.aliyun.dingtalkrobot_1_0.models.RobotSendDingRequest()
                .setRobotCode("dinggtkolxz1u****eqd")
                .setRemindType(1)
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "manager7675"
                ))
                .setContent("钉钉，让进步发生")
                .setCallVoice("● Standard_Female_Voice");
        try {
            client.robotSendDingWithOptions(robotSendDingRequest, robotSendDingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        robot_send_ding_headers = dingtalkrobot__1__0_models.RobotSendDingHeaders()
        robot_send_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        robot_send_ding_request = dingtalkrobot__1__0_models.RobotSendDingRequest(
            robot_code='dinggtkolxz1u****eqd',
            remind_type=1,
            receiver_user_id_list=[
                'manager7675'
            ],
            content='钉钉，让进步发生',
            call_voice='● Standard_Female_Voice'
        )
        try:
            client.robot_send_ding_with_options(robot_send_ding_request, robot_send_ding_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        robot_send_ding_headers = dingtalkrobot__1__0_models.RobotSendDingHeaders()
        robot_send_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        robot_send_ding_request = dingtalkrobot__1__0_models.RobotSendDingRequest(
            robot_code='dinggtkolxz1u****eqd',
            remind_type=1,
            receiver_user_id_list=[
                'manager7675'
            ],
            content='钉钉，让进步发生',
            call_voice='● Standard_Female_Voice'
        )
        try:
            await client.robot_send_ding_with_options_async(robot_send_ding_request, robot_send_ding_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\RobotSendDingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\RobotSendDingRequest;
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
        $robotSendDingHeaders = new RobotSendDingHeaders([]);
        $robotSendDingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $robotSendDingRequest = new RobotSendDingRequest([
            "robotCode" => "dinggtkolxz1u****eqd",
            "remindType" => 1,
            "receiverUserIdList" => [
                "manager7675"
            ],
            "content" => "钉钉，让进步发生",
            "callVoice" => "● Standard_Female_Voice"
        ]);
        try {
            $client->robotSendDingWithOptions($robotSendDingRequest, $robotSendDingHeaders, new RuntimeOptions([]));
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
  dingtalkrobot_1_0  "github.com/alibabacloud-go/dingtalk/robot_1_0"
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

  robotSendDingHeaders := &dingtalkrobot_1_0.RobotSendDingHeaders{}
  robotSendDingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  robotSendDingRequest := &dingtalkrobot_1_0.RobotSendDingRequest{
    RobotCode: tea.String("dinggtkolxz1u****eqd"),
    RemindType: tea.Int32(1),
    ReceiverUserIdList: []*string{tea.String("manager7675")},
    Content: tea.String("钉钉，让进步发生"),
    CallVoice: tea.String("● Standard_Female_Voice"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RobotSendDingWithOptions(robotSendDingRequest, robotSendDingHeaders, &util.RuntimeOptions{})
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
const dingtalkrobot_1_0 = require('@alicloud/dingtalk/robot_1_0');
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
    return new dingtalkrobot_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let robotSendDingHeaders = new dingtalkrobot_1_0.RobotSendDingHeaders({ });
    robotSendDingHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let robotSendDingRequest = new dingtalkrobot_1_0.RobotSendDingRequest({
      robotCode: 'dinggtkolxz1u****eqd',
      remindType: 1,
      receiverUserIdList: [
        'manager7675'
      ],
      content: '钉钉，让进步发生',
      callVoice: '● Standard_Female_Voice',
    });
    try {
      await client.robotSendDingWithOptions(robotSendDingRequest, robotSendDingHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotSendDingHeaders robotSendDingHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotSendDingHeaders();
            robotSendDingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotSendDingRequest robotSendDingRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotSendDingRequest
            {
                RobotCode = "dinggtkolxz1u****eqd",
                RemindType = 1,
                ReceiverUserIdList = new List<string>
                {
                    "manager7675"
                },
                Content = "钉钉，让进步发生",
                CallVoice = "● Standard_Female_Voice",
            };
            try
            {
                client.RobotSendDingWithOptions(robotSendDingRequest, robotSendDingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| openDingId | String | 发送的DING消息Id。 |
| failedList | Map | 失败的接收者列表，格式为 `{"错误原因"：[user01, user02]}`。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openDingId" : "54165xxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | send.ding.exception | send.ding.exception %s | 发送DING消息异常 |
| 400 | invalid.chatbotId | invalid.chatbotId %s | 无效的机器人id |
| 400 | miss.staffId | miss.staffId %s | 无效的接收者id |
| 400 | toomuch.msg | send too fast | 消息发送太快，每分钟每机器人发送消息<6000 |
| 400 | invalidParameter.param.invalid | 参数不合法%s | 参数不合法 |
| 400 | ding.receivercount.limit | ding receiver count limit | 钉消息接收人超出限制，应用内<200，短信\电话<20 |
| 400 | ding.serverquota.insufficient | ding server quota insufficient | 发送钉消息权益不足，需充值 |
| 500 | system.error | system.error | 系统异常 |
