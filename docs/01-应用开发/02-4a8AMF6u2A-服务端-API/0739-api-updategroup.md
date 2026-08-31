---
title: "更新群会话"
source_url: "https://open.dingtalk.com/document/development/api-updategroup"
namespace: "development"
slug: "api-updategroup"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 群管理 > 更新群会话"
doc_id: "f6IWfELX1j"
updated_at: "2026-06-02 19:00:12"
---

> Source: https://open.dingtalk.com/document/development/api-updategroup
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 群管理 > 更新群会话
> Updated: 2026-06-02 19:00:12

# 更新群会话

调用本接口，通过群chatid更新指定群会话的基本信息及成员。可用于修改群相关信息，包括群名称、群主、成员列表、群头像等，适用于群管理员修改群设置、调整群成员等场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/group/update |
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
| chatid | String | 是 | 群会话ID，可通过调用[创建群会话](0738-create-common-group-new-version-v2.md)接口获取的chatid参数值。  **[!NOTE]**    不支持通过调用前端JSAPI获取的chatid。 |
| name | String | 否 | 群名称，长度限制为1~20个字符。 |
| owner | String | 否 | 群主的userId，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId。  **[!NOTE]**    该员工必须为会话useridlist的成员之一。 |
| ownerType | String | 否 | 群主类型。   - **emp**：企业员工 - **ext**：外部联系人 |
| add\_useridlist | Array of String | 否 | userId列表。 |
| del\_useridlist | Array of String | 否 | userId列表。 |
| add\_extidlist | Array of String | 否 | unionid列表，可通过[查询用户详情](0063-query-users-by-phone-number.md)接口获取。 |
| del\_extidlist | Array of String | 否 | unionId列表，可通过[查询用户详情](0063-query-users-by-phone-number.md)接口获取。 |
| icon | String | 否 | 群头像的mediaId，可通过[上传媒体文件](0646-upload-media-files.md)接口获取media\_id参数值。 |
| managementOptions | Object | 否 | 群属性。 |
| mentionAllAuthority | Integer | 否 | @all 使用范围。   - **0**（默认）：所有人可使用 - **1**：仅群主可@all |
| showHistoryType | Integer | 否 | 新成员是否可查看100条历史消息。   - **1**：可查看 - **0**：不可查看   **[!NOTE]**    如果不传值，代表不可查看。 |
| validationType | Integer | 否 | 入群是否需要验证。   - **0**（默认）：不验证 - **1**：入群验证 |
| searchable | Integer | 否 | 群是否可以被搜索。   - 0（默认）：不可搜索 - 1：可搜索 |
| chatBannedType | Integer | 否 | 是否开启群禁言。   - **0**（默认）：不禁言 - **1**：全员禁言 |
| managementType | Integer | 否 | 群管理类型。   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |

### 请求示例

HTTP

```
POST /v1.0/im/group/update HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "chatid" : "chatxxxx",
  "name" : "全员群。",
  "owner" : "04201724372xxxx",
  "ownerType" : "emp",
  "add_useridlist" : [ "userid1" ],
  "del_useridlist" : [ "userid1" ],
  "add_extidlist" : [ "unionId" ],
  "del_extidlist" : [ "unionId" ],
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
        com.aliyun.dingtalkim_1_0.models.UpdateGroupHeaders updateGroupHeaders = new com.aliyun.dingtalkim_1_0.models.UpdateGroupHeaders();
        updateGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest.UpdateGroupRequestManagementOptions managementOptions = new com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest.UpdateGroupRequestManagementOptions()
                .setMentionAllAuthority(0)
                .setShowHistoryType(0)
                .setValidationType(0)
                .setSearchable(0)
                .setChatBannedType(0)
                .setManagementType(0);
        com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest updateGroupRequest = new com.aliyun.dingtalkim_1_0.models.UpdateGroupRequest()
                .setChatid("chatxxxx")
                .setName("全员群。")
                .setOwner("04201724372xxxx")
                .setOwnerType("emp")
                .setAddUseridlist(java.util.Arrays.asList(
                    "userid1"
                ))
                .setDelUseridlist(java.util.Arrays.asList(
                    "userid1"
                ))
                .setAddExtidlist(java.util.Arrays.asList(
                    "unionId"
                ))
                .setDelExtidlist(java.util.Arrays.asList(
                    "unionId"
                ))
                .setIcon("@mediaId")
                .setManagementOptions(managementOptions);
        try {
            client.updateGroupWithOptions(updateGroupRequest, updateGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_group_headers = dingtalkim__1__0_models.UpdateGroupHeaders()
        update_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.UpdateGroupRequestManagementOptions(
            mention_all_authority=0,
            show_history_type=0,
            validation_type=0,
            searchable=0,
            chat_banned_type=0,
            management_type=0
        )
        update_group_request = dingtalkim__1__0_models.UpdateGroupRequest(
            chatid='chatxxxx',
            name='全员群。',
            owner='04201724372xxxx',
            owner_type='emp',
            add_useridlist=[
                'userid1'
            ],
            del_useridlist=[
                'userid1'
            ],
            add_extidlist=[
                'unionId'
            ],
            del_extidlist=[
                'unionId'
            ],
            icon='@mediaId',
            management_options=management_options
        )
        try:
            client.update_group_with_options(update_group_request, update_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_group_headers = dingtalkim__1__0_models.UpdateGroupHeaders()
        update_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.UpdateGroupRequestManagementOptions(
            mention_all_authority=0,
            show_history_type=0,
            validation_type=0,
            searchable=0,
            chat_banned_type=0,
            management_type=0
        )
        update_group_request = dingtalkim__1__0_models.UpdateGroupRequest(
            chatid='chatxxxx',
            name='全员群。',
            owner='04201724372xxxx',
            owner_type='emp',
            add_useridlist=[
                'userid1'
            ],
            del_useridlist=[
                'userid1'
            ],
            add_extidlist=[
                'unionId'
            ],
            del_extidlist=[
                'unionId'
            ],
            icon='@mediaId',
            management_options=management_options
        )
        try:
            await client.update_group_with_options_async(update_group_request, update_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateGroupRequest\managementOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateGroupRequest;
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
        $updateGroupHeaders = new UpdateGroupHeaders([]);
        $updateGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $managementOptions = new managementOptions([
            "mentionAllAuthority" => 0,
            "showHistoryType" => 0,
            "validationType" => 0,
            "searchable" => 0,
            "chatBannedType" => 0,
            "managementType" => 0
        ]);
        $updateGroupRequest = new UpdateGroupRequest([
            "chatid" => "chatxxxx",
            "name" => "全员群。",
            "owner" => "04201724372xxxx",
            "ownerType" => "emp",
            "addUseridlist" => [
                "userid1"
            ],
            "delUseridlist" => [
                "userid1"
            ],
            "addExtidlist" => [
                "unionId"
            ],
            "delExtidlist" => [
                "unionId"
            ],
            "icon" => "@mediaId",
            "managementOptions" => $managementOptions
        ]);
        try {
            $client->updateGroupWithOptions($updateGroupRequest, $updateGroupHeaders, new RuntimeOptions([]));
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

  updateGroupHeaders := &dingtalkim_1_0.UpdateGroupHeaders{}
  updateGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  managementOptions := &dingtalkim_1_0.UpdateGroupRequestManagementOptions{
    MentionAllAuthority: tea.Int32(0),
    ShowHistoryType: tea.Int32(0),
    ValidationType: tea.Int32(0),
    Searchable: tea.Int32(0),
    ChatBannedType: tea.Int32(0),
    ManagementType: tea.Int32(0),
  }
  updateGroupRequest := &dingtalkim_1_0.UpdateGroupRequest{
    Chatid: tea.String("chatxxxx"),
    Name: tea.String("全员群。"),
    Owner: tea.String("04201724372xxxx"),
    OwnerType: tea.String("emp"),
    AddUseridlist: []*string{tea.String("userid1")},
    DelUseridlist: []*string{tea.String("userid1")},
    AddExtidlist: []*string{tea.String("unionId")},
    DelExtidlist: []*string{tea.String("unionId")},
    Icon: tea.String("@mediaId"),
    ManagementOptions: managementOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateGroupWithOptions(updateGroupRequest, updateGroupHeaders, &util.RuntimeOptions{})
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
    let updateGroupHeaders = new dingtalkim_1_0.UpdateGroupHeaders({ });
    updateGroupHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let managementOptions = new dingtalkim_1_0.UpdateGroupRequestManagementOptions({
      mentionAllAuthority: 0,
      showHistoryType: 0,
      validationType: 0,
      searchable: 0,
      chatBannedType: 0,
      managementType: 0,
    });
    let updateGroupRequest = new dingtalkim_1_0.UpdateGroupRequest({
      chatid: 'chatxxxx',
      name: '全员群。',
      owner: '04201724372xxxx',
      ownerType: 'emp',
      addUseridlist: [
        'userid1'
      ],
      delUseridlist: [
        'userid1'
      ],
      addExtidlist: [
        'unionId'
      ],
      delExtidlist: [
        'unionId'
      ],
      icon: '@mediaId',
      managementOptions: managementOptions,
    });
    try {
      await client.updateGroupWithOptions(updateGroupRequest, updateGroupHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupHeaders updateGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupHeaders();
            updateGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupRequest.UpdateGroupRequestManagementOptions managementOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupRequest.UpdateGroupRequestManagementOptions
            {
                MentionAllAuthority = 0,
                ShowHistoryType = 0,
                ValidationType = 0,
                Searchable = 0,
                ChatBannedType = 0,
                ManagementType = 0,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupRequest updateGroupRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupRequest
            {
                Chatid = "chatxxxx",
                Name = "全员群。",
                Owner = "04201724372xxxx",
                OwnerType = "emp",
                AddUseridlist = new List<string>
                {
                    "userid1"
                },
                DelUseridlist = new List<string>
                {
                    "userid1"
                },
                AddExtidlist = new List<string>
                {
                    "unionId"
                },
                DelExtidlist = new List<string>
                {
                    "unionId"
                },
                Icon = "@mediaId",
                ManagementOptions = managementOptions,
            };
            try
            {
                client.UpdateGroupWithOptions(updateGroupRequest, updateGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | parameter.invalid | 输入参数错误 | 根据接口要求，传入必要参数。 |
| 400 | permession.checkFailed | 权限校验失败 | 权限校验失败 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 500 | system.error | 请重试，若始终失败请提交工单 | 请重试，若始终失败请提交工单 |
