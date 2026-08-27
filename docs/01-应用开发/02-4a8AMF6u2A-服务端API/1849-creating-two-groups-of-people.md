---
title: "创建钉钉客联两人互通群"
source_url: "https://open.dingtalk.com/document/development/creating-two-groups-of-people"
namespace: "development"
slug: "creating-two-groups-of-people"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 创建钉钉客联两人互通群"
doc_id: "pfgESeFgAE"
updated_at: "2026-08-27 14:22:53"
---

> Source: https://open.dingtalk.com/document/development/creating-two-groups-of-people
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 创建钉钉客联两人互通群
> Updated: 2026-08-27 14:22:53

# 创建钉钉客联两人互通群

调用本接口创建钉钉客联两人群，即基于钉钉客联系统创建的单聊，可以通过拉人的方式恢复为钉钉客联的普通互通群。

> **[!IMPORTANT]**
>
> 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## **接口说明**

两人群具有以下几个特征：

- 两人群同时具备单聊的效果和群聊的功能，可替代单聊场景。
- 在两人群中，当群成员只有初始创建的两个账号时，群名称和群头像均显示对方账号，仿单聊会话显示效果。
- 在两人群中，可以添加第三方用户进群，聊天记录保留，会话恢复普通群聊显示效果。
- 在两人群中，可以使用群机器人和工具栏。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v2.0/im/interconnections/couples/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "groupTemplateId" : "String",
  "users" : [ {
    "appUserId" : "String",
    "userId" : "String",
    "groupOwner" : Boolean
  } ],
  "operatorId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| groupTemplateId | String | 是 | 群模板Id，通过[群模板配置](1841-interconnections-model.md)获取，群模板可以为群配置群机器人、群工具栏、常用语、欢迎语，长度限制为1～32个字符。例如：8d42\*\*\*\*nkld。 |
| users | Array | 否 | 群成员列表。 |
| appUserId | String | 否 | 钉外账号在业务系统内的唯一标志，调用[创建钉钉客联钉外账号](1847-create-bc-account-association.md)接口获取，通过给该字段赋值来标识当前群成员为钉外账号，长度限制为1～64个字符。  **[!NOTE]**  与userId字段二选一填值，不可都传或都不传。 |
| userId | String | 否 | 钉内账号userId，通过给该字段赋值来标识当前群成员为钉内账号，长度限制为1～64个字符。  **[!NOTE]**  与appUserId字段二选一填值，不可都传或都不传。 |
| groupOwner | Boolean | 是 | 当前用户是否群主。  **[!NOTE]**  在群成员列表中，最多只能设置一个群主。 |
| operatorId | String | 否 | 操作者在业务系统内的唯一标识。支持指定钉内账号或钉外账号为操作者：   - 若是钉内账号userId，长度限制为1～64个字符。 - 若是钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversationId | String | 客联的群会话模板ID。  **[!NOTE]**  客联的群会话id与钉钉IM的群会话ID不同，客联的群会话ID是随机生成的，在使用时不可混用。 |
| conversationId | String | 钉钉群会话Id。 |
| appUserIds | Array of String | 钉外账号在业务系统内的唯一标识。 |
| userIds | Array of String | 钉内账号userId。 |

## 示例

**请求示例**

HTTP

```
POST /v2.0/im/interconnections/couples/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "groupTemplateId" : "8d42****nkld",
  "users" : [ {
    "appUserId" : "1107****2120",
    "userId" : "1745****8778"
  } ],
  "operatorId" : "1745****8777"
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
        com.aliyun.dingtalkim_2_0.models.CreateCoupleGroupHeaders createCoupleGroupHeaders = new com.aliyun.dingtalkim_2_0.models.CreateCoupleGroupHeaders();
        createCoupleGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_2_0.models.CreateCoupleGroupRequest.CreateCoupleGroupRequestUsers users0 = new com.aliyun.dingtalkim_2_0.models.CreateCoupleGroupRequest.CreateCoupleGroupRequestUsers()
                .setAppUserId("1107****2120")
                .setUserId("1745****8778");
        com.aliyun.dingtalkim_2_0.models.CreateCoupleGroupRequest createCoupleGroupRequest = new com.aliyun.dingtalkim_2_0.models.CreateCoupleGroupRequest()
                .setGroupTemplateId("8d42****nkld")
                .setUsers(java.util.Arrays.asList(
                    users0
                ))
                .setOperatorId("1745****8777");
        try {
            client.createCoupleGroupWithOptions(createCoupleGroupRequest, createCoupleGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_couple_group_headers = dingtalkim__2__0_models.CreateCoupleGroupHeaders()
        create_couple_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        users_0 = dingtalkim__2__0_models.CreateCoupleGroupRequestUsers(
            app_user_id='1107****2120',
            user_id='1745****8778'
        )
        create_couple_group_request = dingtalkim__2__0_models.CreateCoupleGroupRequest(
            group_template_id='8d42****nkld',
            users=[
                users_0
            ],
            operator_id='1745****8777'
        )
        try:
            client.create_couple_group_with_options(create_couple_group_request, create_couple_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_couple_group_headers = dingtalkim__2__0_models.CreateCoupleGroupHeaders()
        create_couple_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        users_0 = dingtalkim__2__0_models.CreateCoupleGroupRequestUsers(
            app_user_id='1107****2120',
            user_id='1745****8778'
        )
        create_couple_group_request = dingtalkim__2__0_models.CreateCoupleGroupRequest(
            group_template_id='8d42****nkld',
            users=[
                users_0
            ],
            operator_id='1745****8777'
        )
        try:
            await client.create_couple_group_with_options_async(create_couple_group_request, create_couple_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateCoupleGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateCoupleGroupRequest\users;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateCoupleGroupRequest;
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
        $createCoupleGroupHeaders = new CreateCoupleGroupHeaders([]);
        $createCoupleGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $users0 = new users([
            "appUserId" => "1107****2120",
            "userId" => "1745****8778"
        ]);
        $createCoupleGroupRequest = new CreateCoupleGroupRequest([
            "groupTemplateId" => "8d42****nkld",
            "users" => [
                $users0
            ],
            "operatorId" => "1745****8777"
        ]);
        try {
            $client->createCoupleGroupWithOptions($createCoupleGroupRequest, $createCoupleGroupHeaders, new RuntimeOptions([]));
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

  createCoupleGroupHeaders := &dingtalkim_2_0.CreateCoupleGroupHeaders{}
  createCoupleGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  users0 := &dingtalkim_2_0.CreateCoupleGroupRequestUsers{
    AppUserId: tea.String("1107****2120"),
    UserId: tea.String("1745****8778"),
  }
  createCoupleGroupRequest := &dingtalkim_2_0.CreateCoupleGroupRequest{
    GroupTemplateId: tea.String("8d42****nkld"),
    Users: []*dingtalkim_2_0.CreateCoupleGroupRequestUsers{users0},
    OperatorId: tea.String("1745****8777"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateCoupleGroupWithOptions(createCoupleGroupRequest, createCoupleGroupHeaders, &util.RuntimeOptions{})
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
    let createCoupleGroupHeaders = new $dingtalkim_2_0.CreateCoupleGroupHeaders({ });
    createCoupleGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let users0 = new $dingtalkim_2_0.CreateCoupleGroupRequestUsers({
      appUserId: "1107****2120",
      userId: "1745****8778",
    });
    let createCoupleGroupRequest = new $dingtalkim_2_0.CreateCoupleGroupRequest({
      groupTemplateId: "8d42****nkld",
      users: [
        users0
      ],
      operatorId: "1745****8777",
    });
    try {
      await client.createCoupleGroupWithOptions(createCoupleGroupRequest, createCoupleGroupHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupHeaders createCoupleGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupHeaders();
            createCoupleGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupRequest.CreateCoupleGroupRequestUsers users0 = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupRequest.CreateCoupleGroupRequestUsers
            {
                AppUserId = "1107****2120",
                UserId = "1745****8778",
            };
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupRequest createCoupleGroupRequest = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupRequest
            {
                GroupTemplateId = "8d42****nkld",
                Users = new List<AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateCoupleGroupRequest.CreateCoupleGroupRequestUsers>
                {
                    users0
                },
                OperatorId = "1745****8777",
            };
            try
            {
                client.CreateCoupleGroupWithOptions(createCoupleGroupRequest, createCoupleGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "openConversationId" : "14da****2760",
  "conversationId" : "cidX********xaw==",
  "appUserIds" : [ "1107****2120" ],
  "userIds" : [ "1745****8778" ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否超出最大值或传参规则不正确 | 输入参数有误，请检查是否超出最大值或传参规则不正确 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | service.nonexist | 钉内账号不存在，请检查 | 钉内账号不存在，请检查 |
| 400 | template.nonexist | 群模板不存在，请检查 | 群模板不存在，请检查 |
| 400 | general.enumError | 入参枚举有误，请检查 | 入参枚举有误，请检查 |
| 400 | request.duplicate | 重复请求，请稍后重试 | 重复请求，请稍后重试 |
| 400 | group.memberIllegal | 两人群人数有误，请确保人数有且只有两人 | 两人群人数有误，请确保人数有且只有两人 |
| 400 | group.memberParamIllegal | 群成员参数设置有误，请检查 | 群成员参数设置有误，请检查 |
| 500 | group.create.error | 创建群失败 | 创建群失败 |
| 500 | system.error | 系统异常 | 系统异常 |
