---
title: "关闭互动卡片吊顶"
source_url: "https://open.dingtalk.com/document/development/close-interactive-card-ceiling"
namespace: "development"
slug: "close-interactive-card-ceiling"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群吊顶 > 关闭互动卡片吊顶"
doc_id: "QtNY01jfis"
updated_at: "2026-07-14 09:29:44"
---

> Source: https://open.dingtalk.com/document/development/close-interactive-card-ceiling
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 场景群 > 群吊顶 > 关闭互动卡片吊顶
> Updated: 2026-07-14 09:29:44

# 关闭互动卡片吊顶

调用本接口关闭会话中的互动卡片吊顶。

## **接口调用说明**

- 对于群聊会话类型，支持以下场景使用：

  - 基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。
  - 安装群聊酷应用的群，详情参见[酷应用](../01-XOnnmGCTbn-开发指南/0044-coolapp-overview.md)。
- 对于单聊助手会话类型，支持以下场景：

  此接口只适用于已经建立会话的单聊助手，即第一次开启吊顶前，需要先使用机器人给用户发送单聊消息，以建立单聊助手会话。

  调用[创建并投放卡片](0783-create-and-deliver-cards.md)接口或[批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/im/topBoxes/close |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 卡片的外部ID，最大长度64，与[创建卡片](0780-interface-for-creating-a-card-instance.md)/[创建并投放卡片](0783-create-and-deliver-cards.md)中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取：  image |
| conversationType | Integer | 是 | 会话类型：   - **1**：群聊 - **2**：单聊助手 |
| openConversationId | String | 否 | 会话id：   - **群聊**（此参数必传）：    - 基于群模板创建的群，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。   - 安装群聊酷应用的群，通过[感知群变化（事件订阅）](../01-XOnnmGCTbn-开发指南/0060-group-chat-coolapp-event.md)获取回调参数`OpenConversationId`参数值。 - **单聊助手**：不传入此参数。 |
| userId | String | 否 | 用户userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)或[查询用户详情](0056-query-user-details.md)接口获取。   - 当会话类型为单聊助手时，userId和unionId二选一必填。 - 其他会话类型，不需要传入此参数。 |
| unoinId | String | 否 | 用户unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取。   - 当会话类型为单聊助手时，userId和unionId二选一必填。 - 其他会话类型，不需要传入此参数。 |
| robotCode | String | 否 | 机器人编码：   - **单聊助手**（此参数必填）：    - 企业内部开发-机器人应用的AppKey值。   - 企业内部应用机器人。   - 第三方企业应用机器人 - 其他会话类型，不需要传入此参数 |
| coolAppCode | String | 否 | 酷应用编码：   - **群聊**：    - 基于群模板创建的群，不需要传入此参数。   - 安装群聊酷应用的群，**必须**传入此参数。 - **单聊助手**：不需传入此参数。 |
| groupTemplateId | String | 否 | 群模板id：   - **群聊**：    - 基于群模板创建的群，**必须**传入此参数。   - 安装群聊酷应用的群，不需要传入此参数。 - 其他会话类型，不需传入此参数。 |

### 请求示例

HTTP

```
POST /v2.0/im/topBoxes/close HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "outTrackId" : "xxx",
  "conversationType" : 1,
  "openConversationId" : "cidxxxxx==",
  "userId" : "xxx",
  "unoinId" : "xxx",
  "robotCode" : "xxx",
  "coolAppCode" : "COOLAPP-x-xxx",
  "groupTemplateId" : "xxx-xxx-xxx"
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
    public static com.aliyun.dingtalkim_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_2_0.models.CloseTopboxHeaders closeTopboxHeaders = new com.aliyun.dingtalkim_2_0.models.CloseTopboxHeaders();
        closeTopboxHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_2_0.models.CloseTopboxRequest closeTopboxRequest = new com.aliyun.dingtalkim_2_0.models.CloseTopboxRequest()
                .setOutTrackId("xxx")
                .setConversationType(1)
                .setOpenConversationId("cidxxxxx==")
                .setUserId("xxx")
                .setUnoinId("xxx")
                .setRobotCode("xxx")
                .setCoolAppCode("COOLAPP-x-xxx")
                .setGroupTemplateId("xxx-xxx-xxx");
        try {
            client.closeTopboxWithOptions(closeTopboxRequest, closeTopboxHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.im_2_0.client import Client as dingtalkim_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.im_2_0 import models as dingtalkim__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkim_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        close_topbox_headers = dingtalkim__2__0_models.CloseTopboxHeaders()
        close_topbox_headers.x_acs_dingtalk_access_token = '<your access token>'
        close_topbox_request = dingtalkim__2__0_models.CloseTopboxRequest(
            out_track_id='xxx',
            conversation_type=1,
            open_conversation_id='cidxxxxx==',
            user_id='xxx',
            unoin_id='xxx',
            robot_code='xxx',
            cool_app_code='COOLAPP-x-xxx',
            group_template_id='xxx-xxx-xxx'
        )
        try:
            client.close_topbox_with_options(close_topbox_request, close_topbox_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        close_topbox_headers = dingtalkim__2__0_models.CloseTopboxHeaders()
        close_topbox_headers.x_acs_dingtalk_access_token = '<your access token>'
        close_topbox_request = dingtalkim__2__0_models.CloseTopboxRequest(
            out_track_id='xxx',
            conversation_type=1,
            open_conversation_id='cidxxxxx==',
            user_id='xxx',
            unoin_id='xxx',
            robot_code='xxx',
            cool_app_code='COOLAPP-x-xxx',
            group_template_id='xxx-xxx-xxx'
        )
        try:
            await client.close_topbox_with_options_async(close_topbox_request, close_topbox_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CloseTopboxHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CloseTopboxRequest;
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
        $closeTopboxHeaders = new CloseTopboxHeaders([]);
        $closeTopboxHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $closeTopboxRequest = new CloseTopboxRequest([
            "outTrackId" => "xxx",
            "conversationType" => 1,
            "openConversationId" => "cidxxxxx==",
            "userId" => "xxx",
            "unoinId" => "xxx",
            "robotCode" => "xxx",
            "coolAppCode" => "COOLAPP-x-xxx",
            "groupTemplateId" => "xxx-xxx-xxx"
        ]);
        try {
            $client->closeTopboxWithOptions($closeTopboxRequest, $closeTopboxHeaders, new RuntimeOptions([]));
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
  dingtalkim_2_0  "github.com/alibabacloud-go/dingtalk/im_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkim_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkim_2_0.Client{}
  _result, _err = dingtalkim_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  closeTopboxHeaders := &dingtalkim_2_0.CloseTopboxHeaders{}
  closeTopboxHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  closeTopboxRequest := &dingtalkim_2_0.CloseTopboxRequest{
    OutTrackId: tea.String("xxx"),
    ConversationType: tea.Int32(1),
    OpenConversationId: tea.String("cidxxxxx=="),
    UserId: tea.String("xxx"),
    UnoinId: tea.String("xxx"),
    RobotCode: tea.String("xxx"),
    CoolAppCode: tea.String("COOLAPP-x-xxx"),
    GroupTemplateId: tea.String("xxx-xxx-xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CloseTopboxWithOptions(closeTopboxRequest, closeTopboxHeaders, &util.RuntimeOptions{})
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
import dingtalkim_2_0, * as $dingtalkim_2_0 from '@alicloud/dingtalk/im_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkim_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkim_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let closeTopboxHeaders = new $dingtalkim_2_0.CloseTopboxHeaders({ });
    closeTopboxHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let closeTopboxRequest = new $dingtalkim_2_0.CloseTopboxRequest({
      outTrackId: "xxx",
      conversationType: 1,
      openConversationId: "cidxxxxx==",
      userId: "xxx",
      unoinId: "xxx",
      robotCode: "xxx",
      coolAppCode: "COOLAPP-x-xxx",
      groupTemplateId: "xxx-xxx-xxx",
    });
    try {
      await client.closeTopboxWithOptions(closeTopboxRequest, closeTopboxHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkim_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkim_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkim_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CloseTopboxHeaders closeTopboxHeaders = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CloseTopboxHeaders();
            closeTopboxHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CloseTopboxRequest closeTopboxRequest = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CloseTopboxRequest
            {
                OutTrackId = "xxx",
                ConversationType = 1,
                OpenConversationId = "cidxxxxx==",
                UserId = "xxx",
                UnoinId = "xxx",
                RobotCode = "xxx",
                CoolAppCode = "COOLAPP-x-xxx",
                GroupTemplateId = "xxx-xxx-xxx",
            };
            try
            {
                client.CloseTopboxWithOptions(closeTopboxRequest, closeTopboxHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

python2

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys

from alibabacloud_dingtalkim_2_0.client import Client as dingtalkim_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalkim_2_0 import models as dingtalkim__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client():
        """
        使用 Token 初始化账号Client

        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_2_0Client(config)

    @staticmethod
    def main(args):
        client = Sample.create_client()
        close_topbox_headers = dingtalkim__2__0_models.CloseTopboxHeaders()
        close_topbox_headers.x_acs_dingtalk_access_token = '<your access token>'
        close_topbox_request = dingtalkim__2__0_models.CloseTopboxRequest(
            out_track_id='xxx',
            conversation_type=1,
            open_conversation_id='cidxxxxx==',
            user_id='xxx',
            unoin_id='xxx',
            robot_code='xxx',
            cool_app_code='COOLAPP-x-xxx',
            group_template_id='xxx-xxx-xxx'
        )
        try:
            client.close_topbox_with_options(close_topbox_request, close_topbox_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

Swift

```
#!/usr/bin/env xcrun swift

import Cocoa
import Foundation
import Tea
import TeaUtils
import AlibabacloudDingtalkim20
import AlibabacloudOpenApi

open class Client {
    public static func createClient() throws -> AlibabacloudDingtalkim20.Client {
        var config: AlibabacloudOpenApi.Config = AlibabacloudOpenApi.Config([:])
        config.protocol_ = "https"
        config.regionId = "central"
        return AlibabacloudDingtalkim20.Client(config)
    }

    @available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
    public static func main(_ args: [String]?) async throws -> Void {
        var client: AlibabacloudDingtalkim20.Client = try Client.createClient()
        var closeTopboxHeaders: AlibabacloudDingtalkim20.CloseTopboxHeaders = AlibabacloudDingtalkim20.CloseTopboxHeaders([:])
        closeTopboxHeaders.xAcsDingtalkAccessToken = "<your access token>"
        var closeTopboxRequest: AlibabacloudDingtalkim20.CloseTopboxRequest = AlibabacloudDingtalkim20.CloseTopboxRequest([
            "outTrackId": "xxx",
            "conversationType": 1,
            "openConversationId": "cidxxxxx==",
            "userId": "xxx",
            "unoinId": "xxx",
            "robotCode": "xxx",
            "coolAppCode": "COOLAPP-x-xxx",
            "groupTemplateId": "xxx-xxx-xxx"
        ])
        do {
            try await client.closeTopboxWithOptions(closeTopboxRequest as! AlibabacloudDingtalkim20.CloseTopboxRequest, closeTopboxHeaders as! AlibabacloudDingtalkim20.CloseTopboxHeaders, TeaUtils.RuntimeOptions([:]))
        }
        catch {
            if error is Tea.TeaError {
                var err = error as! Tea.TeaError
                if (!TeaUtils.Client.empty(err.code) && !TeaUtils.Client.empty(err.message)) {
                }
            } else {
                throw error
            }
        }
    }
}

Client.main(CommandLine.arguments)
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 请求是否成功：   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 请求参数为空 | 请求参数为空 |
| 400 | cidParse.wrong | 会话id解码失败 | 会话id解码失败 |
| 400 | chat.notExist | 会话不存在 | 会话不存在 |
| 400 | group.org.checkFailed | 群不属于当前企业 | 群不属于当前企业 |
| 400 | chat.coolApp.notInstalled | 酷应用未安装到会话内 | 酷应用未安装到会话内 |
| 400 | permission.coolApp.checkFailed | 无权限，酷应用不属于当前token对应的应用名下 | 无权限，酷应用不属于当前token对应的应用名下 |
| 400 | group.groupTemplate.notInstalled | 群模板未安装到群内 | 群模板未安装到群内 |
| 400 | permission.sceneGroup.checkFailed | 无权限，该群安装的群模板不属于当前token对应的应用名下 | 无权限，该群安装的群模板不属于当前token对应的应用名下 |
| 400 | close.topbox.failed | 关闭吊顶失败 | 关闭吊顶失败 |
| 400 | user.not.found | 用户不存在 | 用户不存在 |
| 400 | robot.not.found | 机器人不存在 | 机器人不存在 |
| 400 | conversationType.illegal | 会话类型值无效 | 会话类型值无效 |
| 400 | param.illegal | 请求参数无效 | 请求参数无效 |
| 400 | robot.queryFalied | 机器人查询失败 | 机器人查询失败 |
| 400 | mainApp.queryFailed | 主应用查询失败 | 主应用查询失败 |
| 400 | coolAppCode.empty | 酷应用编码为空 | 酷应用编码为空 |
| 400 | openConversationId.empty | 会话id为空 | 会话id为空 |
| 400 | userIdOrUnionId.empty | 用户id为空 | 用户id为空 |
| 400 | robotCode.empty | 机器人编码为空 | 机器人编码为空 |
| 400 | outTrackId.empty | 唯一标识一张卡片的外部ID(outTrackId)为空 | 唯一标识一张卡片的外部ID(outTrackId)为空 |
| 400 | cardTemplate.not.exist | 卡片模板不存在 | 卡片模板不存在 |
| 400 | auth.failed | %s | 权限校验不通过 |
| 500 | system.busy | 系统繁忙 | 系统异常错误 |
