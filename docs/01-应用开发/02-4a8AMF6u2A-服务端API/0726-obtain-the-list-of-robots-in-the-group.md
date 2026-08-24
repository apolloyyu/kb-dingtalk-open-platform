---
title: "获取群内机器人列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-list-of-robots-in-the-group"
namespace: "development"
slug: "obtain-the-list-of-robots-in-the-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 机器人管理 > 获取群内机器人列表"
doc_id: "aWHs68krUU"
updated_at: "2026-06-05 13:49:07"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-list-of-robots-in-the-group
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 机器人管理 > 获取群内机器人列表
> Updated: 2026-06-05 13:49:07

# 获取群内机器人列表

调用本接口获取群内机器人列表。

## **接口调用说明**

目前只支持获取企业内部机器人、第三方企业应用机器人，场景群机器人和公共模板机器人四种类型的机器人，其他类型的机器人均无法查询，如小钉。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/groups/robots/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群ID：基于群模板创建的群，调用[创建群](1484-create-a-scene-group-v2.md)接口获取`open_conversation_id`参数值。 |

### 请求示例

HTTP

```
POST /v1.0/robot/groups/robots/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:qkopsdangcfoonacviojsdjn
Content-Type:application/json

{
  "openConversationId" : "cidjknasndcbaXXXXX"
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
        com.aliyun.dingtalkrobot_1_0.models.GetBotListInGroupHeaders getBotListInGroupHeaders = new com.aliyun.dingtalkrobot_1_0.models.GetBotListInGroupHeaders();
        getBotListInGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.GetBotListInGroupRequest getBotListInGroupRequest = new com.aliyun.dingtalkrobot_1_0.models.GetBotListInGroupRequest()
                .setOpenConversationId("cidjknasndcbaXXXXX");
        try {
            client.getBotListInGroupWithOptions(getBotListInGroupRequest, getBotListInGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_bot_list_in_group_headers = dingtalkrobot__1__0_models.GetBotListInGroupHeaders()
        get_bot_list_in_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_bot_list_in_group_request = dingtalkrobot__1__0_models.GetBotListInGroupRequest(
            open_conversation_id='cidjknasndcbaXXXXX'
        )
        try:
            client.get_bot_list_in_group_with_options(get_bot_list_in_group_request, get_bot_list_in_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_bot_list_in_group_headers = dingtalkrobot__1__0_models.GetBotListInGroupHeaders()
        get_bot_list_in_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_bot_list_in_group_request = dingtalkrobot__1__0_models.GetBotListInGroupRequest(
            open_conversation_id='cidjknasndcbaXXXXX'
        )
        try:
            await client.get_bot_list_in_group_with_options_async(get_bot_list_in_group_request, get_bot_list_in_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\GetBotListInGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\GetBotListInGroupRequest;
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
        $getBotListInGroupHeaders = new GetBotListInGroupHeaders([]);
        $getBotListInGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getBotListInGroupRequest = new GetBotListInGroupRequest([
            "openConversationId" => "cidjknasndcbaXXXXX"
        ]);
        try {
            $client->getBotListInGroupWithOptions($getBotListInGroupRequest, $getBotListInGroupHeaders, new RuntimeOptions([]));
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

  getBotListInGroupHeaders := &dingtalkrobot_1_0.GetBotListInGroupHeaders{}
  getBotListInGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getBotListInGroupRequest := &dingtalkrobot_1_0.GetBotListInGroupRequest{
    OpenConversationId: tea.String("cidjknasndcbaXXXXX"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetBotListInGroupWithOptions(getBotListInGroupRequest, getBotListInGroupHeaders, &util.RuntimeOptions{})
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
    let getBotListInGroupHeaders = new $dingtalkrobot_1_0.GetBotListInGroupHeaders({ });
    getBotListInGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getBotListInGroupRequest = new $dingtalkrobot_1_0.GetBotListInGroupRequest({
      openConversationId: "cidjknasndcbaXXXXX",
    });
    try {
      await client.getBotListInGroupWithOptions(getBotListInGroupRequest, getBotListInGroupHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.GetBotListInGroupHeaders getBotListInGroupHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.GetBotListInGroupHeaders();
            getBotListInGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.GetBotListInGroupRequest getBotListInGroupRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.GetBotListInGroupRequest
            {
                OpenConversationId = "cidjknasndcbaXXXXX",
            };
            try
            {
                client.GetBotListInGroupWithOptions(getBotListInGroupRequest, getBotListInGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| chatbotInstanceVOList | Array | 返回的机器人列表。 |
| robotCode | String | 机器人的编码，参见[机器人名词表-robotCode](https://open.dingtalk.com/document/development/robot-overview)内容，获取`robotCode`。 |
| name | String | 机器人的名称。 |
| downloadIconURL | String | 机器人头像的下载链接。 |
| openRobotType | Integer | 机器人的类型：   - **1**：公共模板机器人，如自定义机器人，心知天气等等。 - **2**：企业内部应用机器人。 - **3**：第三方企业应用机器人。 - **4**：场景群机器人。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "chatbotInstanceVOList" : [ {
    "robotCode" : "dingcdsjfXXXXX",
    "name" : "机器人",
    "downloadIconURL" : "https://img.alicdn.comXXXXXX.jpg",
    "openRobotType" : 1
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | unauthorized | %s | 调用权限不足 |
| 400 | illegal.openconevrsation.id | %s | 无效的会话id |
| 400 | reject | %s | 群中机器人数量太多，无法查询 |
| 500 | system.error | %s | 系统错误 |
