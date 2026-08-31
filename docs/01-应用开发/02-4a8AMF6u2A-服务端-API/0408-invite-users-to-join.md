---
title: "邀请用户入会"
source_url: "https://open.dingtalk.com/document/development/invite-users-to-join"
namespace: "development"
slug: "invite-users-to-join"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 邀请用户入会"
doc_id: "dvHKY3iwga"
updated_at: "2026-06-02 12:05:48"
---

> Source: https://open.dingtalk.com/document/development/invite-users-to-join
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 邀请用户入会
> Updated: 2026-06-02 12:05:48

# 邀请用户入会

会议过程中，邀请新的用户加入会议，调用该接口后，被邀请用户会收到加入会议的通知。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/users/invite |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conferenceId | String | 否 | 会议id，可调用[创建视频会议](0399-create-a-video-conference.md)接口获取返回参数`conferenceId`字段。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 否 | 操作用户unionId。  **[!NOTE]**    如果不填，呼叫条无法显示邀请者姓名。 |
| inviteeList | Array | 否 | 被邀请人列表。 |
| unionId | String | 否 | 被邀请用户unionId。 |
| nick | String | 是 | 被邀请人姓名。 |
| phoneInviteeList | Array | 否 | 被邀请人手机号列表。 |
| phoneNumber | String | 否 | 被邀请用户手机号。 |
| nick | String | 否 | 被邀请人姓名。 |

### 请求示例

HTTP

```
POST /v1.0/conference/videoConferences/644272f14ba33101xxxxxxxx/users/invite HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:0198da4df0e33395904073f1b8a192da
Content-Type:application/json

{
  "unionId" : "qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx",
  "inviteeList" : [ {
    "unionId" : "exxxxxxal40ofA6gexxxxxxxxxx",
    "nick" : "测试用户"
  } ],
  "phoneInviteeList" : [ {
    "phoneNumber" : "1xxxxxxxxxx",
    "nick" : "测试电话用户"
  } ]
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
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconference_1_0.models.InviteUsersHeaders inviteUsersHeaders = new com.aliyun.dingtalkconference_1_0.models.InviteUsersHeaders();
        inviteUsersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.InviteUsersRequest.InviteUsersRequestPhoneInviteeList phoneInviteeList0 = new com.aliyun.dingtalkconference_1_0.models.InviteUsersRequest.InviteUsersRequestPhoneInviteeList()
                .setPhoneNumber("1xxxxxxxxxx")
                .setNick("测试电话用户");
        com.aliyun.dingtalkconference_1_0.models.InviteUsersRequest.InviteUsersRequestInviteeList inviteeList0 = new com.aliyun.dingtalkconference_1_0.models.InviteUsersRequest.InviteUsersRequestInviteeList()
                .setUnionId("exxxxxxal40ofA6gexxxxxxxxxx")
                .setNick("测试用户");
        com.aliyun.dingtalkconference_1_0.models.InviteUsersRequest inviteUsersRequest = new com.aliyun.dingtalkconference_1_0.models.InviteUsersRequest()
                .setUnionId("qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx")
                .setInviteeList(java.util.Arrays.asList(
                    inviteeList0
                ))
                .setPhoneInviteeList(java.util.Arrays.asList(
                    phoneInviteeList0
                ));
        try {
            client.inviteUsersWithOptions("644272f14ba33101xxxxxxxx", inviteUsersRequest, inviteUsersHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.conference_1_0.client import Client as dingtalkconference_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.conference_1_0 import models as dingtalkconference__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconference_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconference_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        invite_users_headers = dingtalkconference__1__0_models.InviteUsersHeaders()
        invite_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        phone_invitee_list_0 = dingtalkconference__1__0_models.InviteUsersRequestPhoneInviteeList(
            phone_number='1xxxxxxxxxx',
            nick='测试电话用户'
        )
        invitee_list_0 = dingtalkconference__1__0_models.InviteUsersRequestInviteeList(
            union_id='exxxxxxal40ofA6gexxxxxxxxxx',
            nick='测试用户'
        )
        invite_users_request = dingtalkconference__1__0_models.InviteUsersRequest(
            union_id='qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx',
            invitee_list=[
                invitee_list_0
            ],
            phone_invitee_list=[
                phone_invitee_list_0
            ]
        )
        try:
            client.invite_users_with_options('644272f14ba33101xxxxxxxx', invite_users_request, invite_users_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        invite_users_headers = dingtalkconference__1__0_models.InviteUsersHeaders()
        invite_users_headers.x_acs_dingtalk_access_token = '<your access token>'
        phone_invitee_list_0 = dingtalkconference__1__0_models.InviteUsersRequestPhoneInviteeList(
            phone_number='1xxxxxxxxxx',
            nick='测试电话用户'
        )
        invitee_list_0 = dingtalkconference__1__0_models.InviteUsersRequestInviteeList(
            union_id='exxxxxxal40ofA6gexxxxxxxxxx',
            nick='测试用户'
        )
        invite_users_request = dingtalkconference__1__0_models.InviteUsersRequest(
            union_id='qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx',
            invitee_list=[
                invitee_list_0
            ],
            phone_invitee_list=[
                phone_invitee_list_0
            ]
        )
        try:
            await client.invite_users_with_options_async('644272f14ba33101xxxxxxxx', invite_users_request, invite_users_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\InviteUsersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\InviteUsersRequest\phoneInviteeList;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\InviteUsersRequest\inviteeList;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\InviteUsersRequest;
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
        $inviteUsersHeaders = new InviteUsersHeaders([]);
        $inviteUsersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $phoneInviteeList0 = new phoneInviteeList([
            "phoneNumber" => "1xxxxxxxxxx",
            "nick" => "测试电话用户"
        ]);
        $inviteeList0 = new inviteeList([
            "unionId" => "exxxxxxal40ofA6gexxxxxxxxxx",
            "nick" => "测试用户"
        ]);
        $inviteUsersRequest = new InviteUsersRequest([
            "unionId" => "qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx",
            "inviteeList" => [
                $inviteeList0
            ],
            "phoneInviteeList" => [
                $phoneInviteeList0
            ]
        ]);
        try {
            $client->inviteUsersWithOptions("644272f14ba33101xxxxxxxx", $inviteUsersRequest, $inviteUsersHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkconference_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconference_1_0.Client{}
  _result, _err = dingtalkconference_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  inviteUsersHeaders := &dingtalkconference_1_0.InviteUsersHeaders{}
  inviteUsersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  phoneInviteeList0 := &dingtalkconference_1_0.InviteUsersRequestPhoneInviteeList{
    PhoneNumber: tea.String("1xxxxxxxxxx"),
    Nick: tea.String("测试电话用户"),
  }
  inviteeList0 := &dingtalkconference_1_0.InviteUsersRequestInviteeList{
    UnionId: tea.String("exxxxxxal40ofA6gexxxxxxxxxx"),
    Nick: tea.String("测试用户"),
  }
  inviteUsersRequest := &dingtalkconference_1_0.InviteUsersRequest{
    UnionId: tea.String("qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx"),
    InviteeList: []*dingtalkconference_1_0.InviteUsersRequestInviteeList{inviteeList0},
    PhoneInviteeList: []*dingtalkconference_1_0.InviteUsersRequestPhoneInviteeList{phoneInviteeList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.InviteUsersWithOptions(tea.String("644272f14ba33101xxxxxxxx"), inviteUsersRequest, inviteUsersHeaders, &util.RuntimeOptions{})
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
const dingtalkconference_1_0 = require('@alicloud/dingtalk/conference_1_0');
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
    return new dingtalkconference_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let inviteUsersHeaders = new dingtalkconference_1_0.InviteUsersHeaders({ });
    inviteUsersHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let phoneInviteeList0 = new dingtalkconference_1_0.InviteUsersRequestPhoneInviteeList({
      phoneNumber: '1xxxxxxxxxx',
      nick: '测试电话用户',
    });
    let inviteeList0 = new dingtalkconference_1_0.InviteUsersRequestInviteeList({
      unionId: 'exxxxxxal40ofA6gexxxxxxxxxx',
      nick: '测试用户',
    });
    let inviteUsersRequest = new dingtalkconference_1_0.InviteUsersRequest({
      unionId: 'qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx',
      inviteeList: [
        inviteeList0
      ],
      phoneInviteeList: [
        phoneInviteeList0
      ],
    });
    try {
      await client.inviteUsersWithOptions('644272f14ba33101xxxxxxxx', inviteUsersRequest, inviteUsersHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkconference_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconference_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconference_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersHeaders inviteUsersHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersHeaders();
            inviteUsersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest.InviteUsersRequestPhoneInviteeList phoneInviteeList0 = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest.InviteUsersRequestPhoneInviteeList
            {
                PhoneNumber = "1xxxxxxxxxx",
                Nick = "测试电话用户",
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest.InviteUsersRequestInviteeList inviteeList0 = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest.InviteUsersRequestInviteeList
            {
                UnionId = "exxxxxxal40ofA6gexxxxxxxxxx",
                Nick = "测试用户",
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest inviteUsersRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest
            {
                UnionId = "qzR1iSMDvzR9iP7P0ZKZobSxxxxxxxx",
                InviteeList = new List<AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest.InviteUsersRequestInviteeList>
                {
                    inviteeList0
                },
                PhoneInviteeList = new List<AlibabaCloud.SDK.Dingtalkconference_1_0.Models.InviteUsersRequest.InviteUsersRequestPhoneInviteeList>
                {
                    phoneInviteeList0
                },
            };
            try
            {
                client.InviteUsersWithOptions("644272f14ba33101xxxxxxxx", inviteUsersRequest, inviteUsersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否成功。 |

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
| 400 | unknownUserError | unknownUserError | 无法识别的用户 |
| 400 | paramsError | error:%s | 参数错误，缺失会议id |
| 500 | systemError | systemError:%s | 系统错误 |
