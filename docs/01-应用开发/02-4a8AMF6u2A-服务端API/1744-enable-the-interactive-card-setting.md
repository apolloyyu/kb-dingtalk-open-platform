---
title: "开启互动卡片实例置顶"
source_url: "https://open.dingtalk.com/document/development/enable-the-interactive-card-setting"
namespace: "development"
slug: "enable-the-interactive-card-setting"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 酷应用 > 开启互动卡片实例置顶"
doc_id: "fIzwh8hMJW"
updated_at: "2025-09-08 19:04:17"
---

> Source: https://open.dingtalk.com/document/development/enable-the-interactive-card-setting
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 酷应用 > 开启互动卡片实例置顶
> Updated: 2025-09-08 19:04:17

# 开启互动卡片实例置顶

调用本接口开启群会话中的互动卡片实例的置顶，此接口只适用于场景群和酷应用。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对互动卡片吊顶接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年11月20日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[创建并开启互动卡片吊顶](https://open.dingtalk.com/document/orgapp/create-and-open-an-interactive-card-ceiling)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

吊顶卡片如下图所示：

![吊顶卡片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8402227361/p354973.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | chat相关接口的管理权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 支持 | chat相关接口的管理权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 暂不支持 | chat相关接口的管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/topBoxes/open HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "conversationType" : Integer,
  "openConversationId" : "String",
  "receiverUserIdList" : [ "String" ],
  "robotCode" : "String",
  "outTrackId" : "String",
  "coolAppCode" : "String",
  "expiredTime" : Long,
  "platforms" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conversationType | Integer | 否 | 会话类型：   - **0**：单聊 - **1**：群聊   **[!NOTE]**  - 单聊包括用户与用户之间的单聊，用户与机器人之间的单聊。 - 此值若为空，则默认会话类型为群聊。 |
| openConversationId | String | 否 | 群的openConversationId，可调用[创建群](https://open.dingtalk.com/document/orgapp/create-a-scene-group-v2)接口获取。  **[!NOTE]**  会话类型为群聊时需要传入此值。 |
| receiverUserIdList | Array of String | 否 | 可接收人userId，最多可传100个userId。  **[!NOTE]**  - 会话类型为单聊：    - 用户与用户之间的单聊，需要传入双方用户的userId。   - 用户与机器人之间的单聊，需要传入用户的userId。 - 会话类型为群聊:    - 不传入此值，则默认吊顶对群内所有人可见。   - 传入用户userId，则吊顶仅对userId对应用户可见。 |
| robotCode | String | 否 | 机器人编码。 |
| outTrackId | String | 是 | 唯一标识一张卡片的外部ID。  **[!NOTE]**  卡片幂等ID，可用于更新或重复发送同一卡片到多个群会话。 |
| coolAppCode | String | 否 | 酷应用编码。  **[!NOTE]**  酷应用发送吊顶时，此值必传。 |
| expiredTime | Long | 否 | 置顶的过期时间，毫秒级时间戳。 |
| platforms | String | 否 | 期望置顶的端，如果有多个用“｜”分隔。 例如：ios|mac|android|win表示iOS、MAC、安卓和windows端。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/topBoxes/open HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxxx
Content-Type:application/json

{
  "openConversationId" : "g280xxx",
  "receiverUserIdList" : [ "manager7675" ],
  "outTrackId" : "23088u2gxxx",
  "coolAppCode" : "Coolxxxxxx",
  "expiredTime" : 1850042969000,
  "platforms" : "ios|mac|android|win"
}
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
        TopboxOpenHeaders topboxOpenHeaders = new TopboxOpenHeaders();
        topboxOpenHeaders.xAcsDingtalkAccessToken = "<your access token>";
        TopboxOpenRequest topboxOpenRequest = new TopboxOpenRequest()
                .setOpenConversationId("g280xxx")
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "manager7675"
                ))
                .setOutTrackId("23088u2gxxx")
                .setCoolAppCode("Coolxxxxxx")
                .setExpiredTime(1850042969000L)
                .setPlatforms("ios|mac|android|win");
        try {
            client.topboxOpenWithOptions(topboxOpenRequest, topboxOpenHeaders, new RuntimeOptions());
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
        topbox_open_headers = dingtalkim__1__0_models.TopboxOpenHeaders()
        topbox_open_headers.x_acs_dingtalk_access_token = '<your access token>'
        topbox_open_request = dingtalkim__1__0_models.TopboxOpenRequest(
            open_conversation_id='g280xxx',
            receiver_user_id_list=[
                'manager7675'
            ],
            out_track_id='23088u2gxxx',
            cool_app_code='Coolxxxxxx',
            expired_time=1850042969000,
            platforms='ios|mac|android|win'
        )
        try:
            client.topbox_open_with_options(topbox_open_request, topbox_open_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        topbox_open_headers = dingtalkim__1__0_models.TopboxOpenHeaders()
        topbox_open_headers.x_acs_dingtalk_access_token = '<your access token>'
        topbox_open_request = dingtalkim__1__0_models.TopboxOpenRequest(
            open_conversation_id='g280xxx',
            receiver_user_id_list=[
                'manager7675'
            ],
            out_track_id='23088u2gxxx',
            cool_app_code='Coolxxxxxx',
            expired_time=1850042969000,
            platforms='ios|mac|android|win'
        )
        try:
            await client.topbox_open_with_options_async(topbox_open_request, topbox_open_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\TopboxOpenHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\TopboxOpenRequest;
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
        $topboxOpenHeaders = new TopboxOpenHeaders([]);
        $topboxOpenHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $topboxOpenRequest = new TopboxOpenRequest([
            "openConversationId" => "g280xxx",
            "receiverUserIdList" => [
                "manager7675"
            ],
            "outTrackId" => "23088u2gxxx",
            "coolAppCode" => "Coolxxxxxx",
            "expiredTime" => 1850042969000,
            "platforms" => "ios|mac|android|win"
        ]);
        try {
            $client->topboxOpenWithOptions($topboxOpenRequest, $topboxOpenHeaders, new RuntimeOptions([]));
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

  topboxOpenHeaders := &dingtalkim_1_0.TopboxOpenHeaders{}
  topboxOpenHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  topboxOpenRequest := &dingtalkim_1_0.TopboxOpenRequest{
    OpenConversationId: tea.String("g280xxx"),
    ReceiverUserIdList: []*string{tea.String("manager7675")},
    OutTrackId: tea.String("23088u2gxxx"),
    CoolAppCode: tea.String("Coolxxxxxx"),
    ExpiredTime: tea.Int64(1850042969000),
    Platforms: tea.String("ios|mac|android|win"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.TopboxOpenWithOptions(topboxOpenRequest, topboxOpenHeaders, &util.RuntimeOptions{})
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
    let topboxOpenHeaders = new $dingtalkim_1_0.TopboxOpenHeaders({ });
    topboxOpenHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let topboxOpenRequest = new $dingtalkim_1_0.TopboxOpenRequest({
      openConversationId: "g280xxx",
      receiverUserIdList: [
        "manager7675"
      ],
      outTrackId: "23088u2gxxx",
      coolAppCode: "Coolxxxxxx",
      expiredTime: 1850042969000,
      platforms: "ios|mac|android|win",
    });
    try {
      await client.topboxOpenWithOptions(topboxOpenRequest, topboxOpenHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.TopboxOpenHeaders topboxOpenHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.TopboxOpenHeaders();
            topboxOpenHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.TopboxOpenRequest topboxOpenRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.TopboxOpenRequest
            {
                OpenConversationId = "g280xxx",
                ReceiverUserIdList = new List<string>
                {
                    "manager7675"
                },
                OutTrackId = "23088u2gxxx",
                CoolAppCode = "Coolxxxxxx",
                ExpiredTime = 1850042969000,
                Platforms = "ios|mac|android|win",
            };
            try
            {
                client.TopboxOpenWithOptions(topboxOpenRequest, topboxOpenHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | coolAppNotInstalled | 该酷应用未安装到目标会话内 | 该酷应用未安装到目标会话内 |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | param.invalid | 无效参数 | 无效参数 |
| 400 | openTopbox.failed | 开启吊顶失败 | 开启吊顶失败 |
| 400 | queryCard.failed | 查询卡片失败 | 查询卡片失败 |
| 400 | openConversationId.decryptFailed | openConversationId解密错误 | openConversationId解密错误 |
| 400 | empNotFound | 员工不存在 | 员工不存在 |
| 400 | chatbotNotFound | 机器人不存在 | 机器人不存在 |
| 400 | group.org.checkFailed | 群不属于当前企业 | 群不属于当前企业 |
| 400 | topbox.auth.checkFailed | 酷应用或场景群权限校验失败 | 酷应用或场景群权限校验失败 |
| 500 | systemBusy | 系统繁忙 | 系统异常错误 |
