---
title: "设置场景群成员禁言状态"
source_url: "https://open.dingtalk.com/document/development/set-group-members-access-control"
namespace: "development"
slug: "set-group-members-access-control"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 设置场景群成员禁言状态"
doc_id: "8ncPWvbEFF"
updated_at: "2026-08-14 09:41:59"
---

> Source: https://open.dingtalk.com/document/development/set-group-members-access-control
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 设置场景群成员禁言状态
> Updated: 2026-08-14 09:41:59

# 设置场景群成员禁言状态

调用本接口设置场景群内的群成员禁言状态，可设置指定群成员禁言或解除禁言，适用于企业群管理员对群内成员进行管理，需要对违规成员进行禁言或解除禁言的场景。

## 接口调用说明

支持以下场景使用：

- 基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/muteMembers/set |
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
| userIdList | Array of String | 是 | 需要禁言或取消禁言的群成员userId列表。     - 群主和群管理员无法被设置禁言。 - 最多传999个。 |
| openConversationId | String | 是 | 群ID，通过[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |
| muteStatus | Integer | 是 | 禁言状态：   - **0**：取消禁言 - **1**：禁言 |
| muteDuration | Long | 是 | 禁言持续时长，单位：毫秒。 |

### 请求示例

HTTP

```
POST /v1.0/im/sceneGroups/muteMembers/set HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2107d7ae16466433794062053d0587
Content-Type:application/json

{
  "userIdList" : [ "0104440938191508" ],
  "openConversationId" : "cid5d5uM3XEw3gxbNc/n7EQ4g==",
  "muteStatus" : 1,
  "muteDuration" : 300000
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
        UpdateMemberBanWordsHeaders updateMemberBanWordsHeaders = new UpdateMemberBanWordsHeaders();
        updateMemberBanWordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateMemberBanWordsRequest updateMemberBanWordsRequest = new UpdateMemberBanWordsRequest()
                .setUserIdList(java.util.Arrays.asList(
                    "0104440938191508"
                ))
                .setOpenConversationId("cid5d5uM3XEw3gxbNc/n7EQ4g==")
                .setMuteStatus(1)
                .setMuteDuration(300000L);
        try {
            client.updateMemberBanWordsWithOptions(updateMemberBanWordsRequest, updateMemberBanWordsHeaders, new RuntimeOptions());
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
        update_member_ban_words_headers = dingtalkim__1__0_models.UpdateMemberBanWordsHeaders()
        update_member_ban_words_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_member_ban_words_request = dingtalkim__1__0_models.UpdateMemberBanWordsRequest(
            user_id_list=[
                '0104440938191508'
            ],
            open_conversation_id='cid5d5uM3XEw3gxbNc/n7EQ4g==',
            mute_status=1,
            mute_duration=300000
        )
        try:
            client.update_member_ban_words_with_options(update_member_ban_words_request, update_member_ban_words_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_member_ban_words_headers = dingtalkim__1__0_models.UpdateMemberBanWordsHeaders()
        update_member_ban_words_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_member_ban_words_request = dingtalkim__1__0_models.UpdateMemberBanWordsRequest(
            user_id_list=[
                '0104440938191508'
            ],
            open_conversation_id='cid5d5uM3XEw3gxbNc/n7EQ4g==',
            mute_status=1,
            mute_duration=300000
        )
        try:
            await client.update_member_ban_words_with_options_async(update_member_ban_words_request, update_member_ban_words_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateMemberBanWordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateMemberBanWordsRequest;
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
        $updateMemberBanWordsHeaders = new UpdateMemberBanWordsHeaders([]);
        $updateMemberBanWordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateMemberBanWordsRequest = new UpdateMemberBanWordsRequest([
            "userIdList" => [
                "0104440938191508"
            ],
            "openConversationId" => "cid5d5uM3XEw3gxbNc/n7EQ4g==",
            "muteStatus" => 1,
            "muteDuration" => 300000
        ]);
        try {
            $client->updateMemberBanWordsWithOptions($updateMemberBanWordsRequest, $updateMemberBanWordsHeaders, new RuntimeOptions([]));
        }
        catch (Exception $err) {
            if (!($err instanceof TeaError)) {
                $err = new TeaError([], $err->getMessage(), $err->getCode(), $err);
            }
            if (!Utils::empty_($err->code) && !Utils::empty_($err->message)) {
                // err 中含��� code 和 message 属性，可帮助开发定位问题
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

  updateMemberBanWordsHeaders := &dingtalkim_1_0.UpdateMemberBanWordsHeaders{}
  updateMemberBanWordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateMemberBanWordsRequest := &dingtalkim_1_0.UpdateMemberBanWordsRequest{
    UserIdList: []*string{tea.String("0104440938191508")},
    OpenConversationId: tea.String("cid5d5uM3XEw3gxbNc/n7EQ4g=="),
    MuteStatus: tea.Int32(1),
    MuteDuration: tea.Int64(300000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateMemberBanWordsWithOptions(updateMemberBanWordsRequest, updateMemberBanWordsHeaders, &util.RuntimeOptions{})
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
    let updateMemberBanWordsHeaders = new $dingtalkim_1_0.UpdateMemberBanWordsHeaders({ });
    updateMemberBanWordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateMemberBanWordsRequest = new $dingtalkim_1_0.UpdateMemberBanWordsRequest({
      userIdList: [
        "0104440938191508"
      ],
      openConversationId: "cid5d5uM3XEw3gxbNc/n7EQ4g==",
      muteStatus: 1,
      muteDuration: 300000,
    });
    try {
      await client.updateMemberBanWordsWithOptions(updateMemberBanWordsRequest, updateMemberBanWordsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberBanWordsHeaders updateMemberBanWordsHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberBanWordsHeaders();
            updateMemberBanWordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberBanWordsRequest updateMemberBanWordsRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberBanWordsRequest
            {
                UserIdList = new List<string>
                {
                    "0104440938191508"
                },
                OpenConversationId = "cid5d5uM3XEw3gxbNc/n7EQ4g==",
                MuteStatus = 1,
                MuteDuration = 300000,
            };
            try
            {
                client.UpdateMemberBanWordsWithOptions(updateMemberBanWordsRequest, updateMemberBanWordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.openConversationIdDecError | 会话ID解密失败 | 会话ID解密失败 |
| 400 | invalidParameter.userIdList | 不合法的群成员列表 | 不合法的群成员列表 |
| 400 | invalidParameter.muteStatusError | 不合法的的禁言状态 | 不合法的的禁言状态 |
| 400 | invalidParameter.openConversationIdError | 不合法的会话ID | 不合法的会话ID |
| 400 | cannot.ban.owner | 不允许禁言群主 | 不允许禁言群主 |
| 400 | cannot.find.user | 找不到该用户 | 找不到该用户 |
| 400 | invalidGroupParams | 群不存在或者群成员为空 | 群不存在或者群成员为空 |
| 400 | group.org.checkFailed | 无权限，群不属于当前企业 | 无权限，群不属于当前企业 |
| 500 | system.error | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
