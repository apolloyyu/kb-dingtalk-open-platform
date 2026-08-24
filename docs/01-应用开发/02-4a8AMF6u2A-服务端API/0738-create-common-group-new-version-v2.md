---
title: "创建群会话"
source_url: "https://open.dingtalk.com/document/development/create-common-group-new-version-v2"
namespace: "development"
slug: "create-common-group-new-version-v2"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 创建群会话"
doc_id: "bVZ7zI1LZf"
updated_at: "2026-06-04 19:09:49"
---

> Source: https://open.dingtalk.com/document/development/create-common-group-new-version-v2
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 群管理 > 创建群会话
> Updated: 2026-06-04 19:09:49

# 创建群会话

调用本接口，创建内部群跟普通群会话，适用于企业需要快速创建群聊的场景。

## 接口调用说明

本接口默认只支持创建内部群，如果需要创建普通群需要找技术支持加白。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/group/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 群名称，长度限制为1~20个字符。 |
| owner | String | 是 | 群主的userId，可通过根据手机号查询用户接口获取userId。 |
| ownerType | String | 否 | 群主类型。   - **emp**：企业员工 - **ext**：外部联系人 |
| useridlist | Array of String | 是 | 用户的StaffId。 |
| conversationTag | Long | 否 | 会话类型标记。默认内部群，普通群创建需要找技术支持加白   - **0**：普通群 - **2**：内部群 |
| extidlist | Array of String | 否 | 外部联系人 |
| icon | String | 否 | 群头像，需要传递mediaId，可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |
| managementOptions | Object | 否 | 创建群其他属性 |
| mentionAllAuthority | Integer | 否 | @all 使用范围。   - **0**（默认）：所有人可使用 - **1**：仅群主可@all |
| showHistoryType | Integer | 否 | 新成员是否可查看100条历史消息，如果不传值，代表不可查看。   - **1**：可查看 - **0**：不可查看 |
| validationType | Integer | 否 | 入群是否需要验证。 -\*\* 0\*\*（默认）：不验证   - **1**：入群验证 |
| searchable | Integer | 否 | 群是否可以被搜索。 -\*\* 0\*\*（默认）：不可搜索   - **1**：可搜索 |
| chatBannedType | Integer | 否 | 是否开启群禁言。   - **0**（默认）：不禁言 - **1**：全员禁言 |
| managementType | Integer | 否 | 群管理类型。   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |

### 请求示例

HTTP

```
POST /v1.0/im/group/create HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "name" : "测试群",
  "owner" : "manager4220",
  "ownerType" : "emp",
  "useridlist" : [ "userId" ],
  "conversationTag" : 2,
  "extidlist" : [ "unionId" ],
  "icon" : "@mediaId",
  "managementOptions" : {
    "mentionAllAuthority" : 0,
    "showHistoryType" : 0,
    "validationType" : 0,
    "searchable" : 0,
    "chatBannedType" : 0,
    "managementType" : 0
  }
}
```

Java

```
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
        com.aliyun.dingtalkim_1_0.models.CreateGroupHeaders createGroupHeaders = new com.aliyun.dingtalkim_1_0.models.CreateGroupHeaders();
        createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.CreateGroupRequest.CreateGroupRequestManagementOptions managementOptions = new com.aliyun.dingtalkim_1_0.models.CreateGroupRequest.CreateGroupRequestManagementOptions()
                .setMentionAllAuthority(0)
                .setShowHistoryType(0)
                .setValidationType(0)
                .setSearchable(0)
                .setChatBannedType(0)
                .setManagementType(0);
        com.aliyun.dingtalkim_1_0.models.CreateGroupRequest createGroupRequest = new com.aliyun.dingtalkim_1_0.models.CreateGroupRequest()
                .setName("测试群")
                .setOwner("manager4220")
                .setOwnerType("emp")
                .setUseridlist(java.util.Arrays.asList(
                    "userId"
                ))
                .setConversationTag(2L)
                .setExtidlist(java.util.Arrays.asList(
                    "unionId"
                ))
                .setIcon("@mediaId")
                .setManagementOptions(managementOptions);
        try {
            client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

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
        create_group_headers = dingtalkim__1__0_models.CreateGroupHeaders()
        create_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.CreateGroupRequestManagementOptions(
            mention_all_authority=0,
            show_history_type=0,
            validation_type=0,
            searchable=0,
            chat_banned_type=0,
            management_type=0
        )
        create_group_request = dingtalkim__1__0_models.CreateGroupRequest(
            name='测试群',
            owner='manager4220',
            owner_type='emp',
            useridlist=[
                'userId'
            ],
            conversation_tag=2,
            extidlist=[
                'unionId'
            ],
            icon='@mediaId',
            management_options=management_options
        )
        try:
            client.create_group_with_options(create_group_request, create_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_group_headers = dingtalkim__1__0_models.CreateGroupHeaders()
        create_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.CreateGroupRequestManagementOptions(
            mention_all_authority=0,
            show_history_type=0,
            validation_type=0,
            searchable=0,
            chat_banned_type=0,
            management_type=0
        )
        create_group_request = dingtalkim__1__0_models.CreateGroupRequest(
            name='测试群',
            owner='manager4220',
            owner_type='emp',
            useridlist=[
                'userId'
            ],
            conversation_tag=2,
            extidlist=[
                'unionId'
            ],
            icon='@mediaId',
            management_options=management_options
        )
        try:
            await client.create_group_with_options_async(create_group_request, create_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateGroupRequest\managementOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateGroupRequest;
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
        $createGroupHeaders = new CreateGroupHeaders([]);
        $createGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $managementOptions = new managementOptions([
            "mentionAllAuthority" => 0,
            "showHistoryType" => 0,
            "validationType" => 0,
            "searchable" => 0,
            "chatBannedType" => 0,
            "managementType" => 0
        ]);
        $createGroupRequest = new CreateGroupRequest([
            "name" => "测试群",
            "owner" => "manager4220",
            "ownerType" => "emp",
            "useridlist" => [
                "userId"
            ],
            "conversationTag" => 2,
            "extidlist" => [
                "unionId"
            ],
            "icon" => "@mediaId",
            "managementOptions" => $managementOptions
        ]);
        try {
            $client->createGroupWithOptions($createGroupRequest, $createGroupHeaders, new RuntimeOptions([]));
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

  createGroupHeaders := &dingtalkim_1_0.CreateGroupHeaders{}
  createGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  managementOptions := &dingtalkim_1_0.CreateGroupRequestManagementOptions{
    MentionAllAuthority: tea.Int32(0),
    ShowHistoryType: tea.Int32(0),
    ValidationType: tea.Int32(0),
    Searchable: tea.Int32(0),
    ChatBannedType: tea.Int32(0),
    ManagementType: tea.Int32(0),
  }
  createGroupRequest := &dingtalkim_1_0.CreateGroupRequest{
    Name: tea.String("测试群"),
    Owner: tea.String("manager4220"),
    OwnerType: tea.String("emp"),
    Useridlist: []*string{tea.String("userId")},
    ConversationTag: tea.Int64(2),
    Extidlist: []*string{tea.String("unionId")},
    Icon: tea.String("@mediaId"),
    ManagementOptions: managementOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateGroupWithOptions(createGroupRequest, createGroupHeaders, &util.RuntimeOptions{})
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
    let createGroupHeaders = new dingtalkim_1_0.CreateGroupHeaders({ });
    createGroupHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let managementOptions = new dingtalkim_1_0.CreateGroupRequestManagementOptions({
      mentionAllAuthority: 0,
      showHistoryType: 0,
      validationType: 0,
      searchable: 0,
      chatBannedType: 0,
      managementType: 0,
    });
    let createGroupRequest = new dingtalkim_1_0.CreateGroupRequest({
      name: '测试群',
      owner: 'manager4220',
      ownerType: 'emp',
      useridlist: [
        'userId'
      ],
      conversationTag: 2,
      extidlist: [
        'unionId'
      ],
      icon: '@mediaId',
      managementOptions: managementOptions,
    });
    try {
      await client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupHeaders createGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupHeaders();
            createGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupRequest.CreateGroupRequestManagementOptions managementOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupRequest.CreateGroupRequestManagementOptions
            {
                MentionAllAuthority = 0,
                ShowHistoryType = 0,
                ValidationType = 0,
                Searchable = 0,
                ChatBannedType = 0,
                ManagementType = 0,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupRequest createGroupRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupRequest
            {
                Name = "测试群",
                Owner = "manager4220",
                OwnerType = "emp",
                Useridlist = new List<string>
                {
                    "userId"
                },
                ConversationTag = 2,
                Extidlist = new List<string>
                {
                    "unionId"
                },
                Icon = "@mediaId",
                ManagementOptions = managementOptions,
            };
            try
            {
                client.CreateGroupWithOptions(createGroupRequest, createGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| conversationTag | Long | 群类型：   - **0**：普通群 - **2**：内部群 |
| openConversationId | String | 群会话ID。 |
| chatid | String | 群会话ID，旧参数字段。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "conversationTag" : 2,
  "openConversationId" : "14da****2760",
  "chatid" : "chatxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.invalid | 输入参数错误 | 根据接口要求，传入必要参数。 |
| 400 | permession.checkFailed | 权限校验失败 | 权限校验失败 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 500 | system.error | 请重试，若始终失败请提交工单 | 请重试，若始终失败请提交工单 |
