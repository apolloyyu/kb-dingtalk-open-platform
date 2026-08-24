---
title: "创建场景群"
source_url: "https://open.dingtalk.com/document/development/create-a-scene-group"
namespace: "development"
slug: "create-a-scene-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 创建场景群"
doc_id: "BxFNKyJ1tp"
updated_at: "2026-06-10 18:24:18"
---

> Source: https://open.dingtalk.com/document/development/create-a-scene-group
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 创建场景群
> Updated: 2026-06-10 18:24:18

# 创建场景群

调用本接口，根据群模板ID创建群。本接口适用于企业需要根据群模板快速创建群聊的场景，如项目协作、活动组织等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroup/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| title | String | 是 | 群名称，最长不超过30字符，建议长度在10字符以内。 |
| icon | String | 否 | 群头像，调用[上传媒体文件](0646-upload-media-files.md)接口上传头像后获取mediaId。 |
| template\_id | String | 是 | 群模板ID，登录[开发者后台 > 开放能力 > 场景群 > 群模板](https://open-dev.dingtalk.com/fe/im?spm=ding_open_doc.document.0.0.704e5d03QQBnaX#/group/list)查看id。 |
| owner\_user\_id | String | 是 | 群主userId。 |
| user\_ids | Array of String | 否 | 群成员userId列表。 |
| subadmin\_ids | Array of String | 否 | 群管理员userId列表。 |
| uuid | String | 否 | 建群去重的业务ID。 |
| management\_options | Object | 否 | 创建属性。 |
| mention\_all\_authority | Integer | 否 | @all 权限：   - **0**（默认）：所有人都可以@all - **1**：仅群主可@all |
| show\_history\_type | Integer | 否 | 新成员是否可查看聊天历史消息：   - **0**（默认）：不可以查看历史记录 - **1**：可以查看历史记录 |
| validation\_type | Integer | 否 | 入群是否需要验证：   - **0**（默认）：不验证入群 - **1**：入群验证 |
| searchable | Integer | 否 | 群是否可搜索：   - **0**（默认）：不可搜索 - **1**：可搜索 |
| chat\_banned\_type | Integer | 否 | 是否开启群禁言：   - **0**（默认）：不禁言 - **1**：全员禁言 |
| management\_type | Integer | 否 | 管理类型：   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |
| only\_admin\_can\_ding | Integer | 否 | 群内发DING权限：   - **0**（默认）：所有人可发DING - **1**：仅群主和管理员可发DING |
| all\_members\_can\_create\_mcs\_conf | Integer | 否 | 群会议权限：   - **0**：仅群主和管理员可发起视频和语音会议 - **1**（默认）：所有人可发起视频和语音会议 |
| all\_members\_can\_create\_calendar | Integer | 否 | 群日历设置项，群内非好友/同事的成员是否可相互发起钉钉日程：   - **0**（默认）：非好友/同事的成员不可发起钉钉日程 - **1**：非好友/同事的成员可以发起钉钉日程 |
| group\_email\_disabled | Integer | 否 | 是否禁止发送群邮件：   - **0**（默认）：群内成员可以对本群发送群邮件 - **1**：群内成员不可对本群发送群邮件 |
| only\_admin\_can\_set\_msg\_top | Integer | 否 | 置顶群消息权限：   - **0**（默认）：所有人可置顶群消息 - **1**：仅群主和管理员可置顶群消息 |
| add\_friend\_forbidden | Integer | 否 | 群成员私聊权限：   - **0**（默认）：所有人可私聊 - **1**：普通群成员之间不能够加好友、单聊，且部分功能使用受限（管理员与非管理员之间不受影响） |
| group\_live\_switch | Integer | 否 | 群直播权限：   - **0**：仅群主与管理员可发起直播 - **1**（默认）：群内任意成员可发起群直播 |
| members\_to\_admin\_chat | Integer | 否 | 是否禁止非管理员向管理员发起单聊：   - **0**（默认）：非管理员可以向管理员发起单聊 - **1**：禁止非管理员向管理员发起单聊 |
| not\_quit\_when\_emp\_leave | Integer | 否 | 员工离职后是否不退出群：   - **0**-默认，退组织时退出群 - **1**-退组织时不退出群       只对外部群生效。 |
| only\_admin\_can\_add\_mem | Integer | 否 | 仅群主/管理员可邀人，   - **0**（默认）：所有人可邀人 - **1**：仅群主/管理员       `management_type`为1时，这个配置才生效。 |

### 请求示例

HTTP

```
POST /v1.0/im/sceneGroup/create HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:beE4*****75d
Content-Type:application/json

{
  "title" : "客户群",
  "icon" : "@lADOADma*****QKA",
  "template_id" : "c354***-***-***-b4ea-6f1ab***65",
  "owner_user_id" : "1107****2120",
  "user_ids" : [ "1107****2120" ],
  "subadmin_ids" : [ "1107****2120" ],
  "uuid" : "asdazxc",
  "management_options" : {
    "mention_all_authority" : 0,
    "show_history_type" : 0,
    "validation_type" : 0,
    "searchable" : 0,
    "chat_banned_type" : 0,
    "management_type" : 0,
    "only_admin_can_ding" : 0,
    "all_members_can_create_mcs_conf" : 0,
    "all_members_can_create_calendar" : 0,
    "group_email_disabled" : 0,
    "only_admin_can_set_msg_top" : 0,
    "add_friend_forbidden" : 0,
    "group_live_switch" : 0,
    "members_to_admin_chat" : 0,
    "not_quit_when_emp_leave" : 0,
    "only_admin_can_add_mem" : 0
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
        com.aliyun.dingtalkim_1_0.models.CreateSceneGroupHeaders createSceneGroupHeaders = new com.aliyun.dingtalkim_1_0.models.CreateSceneGroupHeaders();
        createSceneGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.CreateSceneGroupRequest.CreateSceneGroupRequestManagementOptions managementOptions = new com.aliyun.dingtalkim_1_0.models.CreateSceneGroupRequest.CreateSceneGroupRequestManagementOptions()
                .setMentionAllAuthority(0)
                .setShowHistoryType(0)
                .setValidationType(0)
                .setSearchable(0)
                .setChatBannedType(0)
                .setManagementType(0)
                .setOnlyAdminCanDing(0)
                .setAllMembersCanCreateMcsConf(0)
                .setAllMembersCanCreateCalendar(0)
                .setGroupEmailDisabled(0)
                .setOnlyAdminCanSetMsgTop(0)
                .setAddFriendForbidden(0)
                .setGroupLiveSwitch(0)
                .setMembersToAdminChat(0)
                .setNotQuitWhenEmpLeave(0)
                .setOnlyAdminCanAddMem(0);
        com.aliyun.dingtalkim_1_0.models.CreateSceneGroupRequest createSceneGroupRequest = new com.aliyun.dingtalkim_1_0.models.CreateSceneGroupRequest()
                .setTitle("客户群")
                .setIcon("@lADOADma*****QKA")
                .setTemplateId("c354***-***-***-b4ea-6f1ab***65")
                .setOwnerUserId("1107****2120")
                .setUserIds(java.util.Arrays.asList(
                    "1107****2120"
                ))
                .setSubadminIds(java.util.Arrays.asList(
                    "1107****2120"
                ))
                .setUuid("asdazxc")
                .setManagementOptions(managementOptions);
        try {
            client.createSceneGroupWithOptions(createSceneGroupRequest, createSceneGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_scene_group_headers = dingtalkim__1__0_models.CreateSceneGroupHeaders()
        create_scene_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.CreateSceneGroupRequestManagementOptions(
            mention_all_authority=0,
            show_history_type=0,
            validation_type=0,
            searchable=0,
            chat_banned_type=0,
            management_type=0,
            only_admin_can_ding=0,
            all_members_can_create_mcs_conf=0,
            all_members_can_create_calendar=0,
            group_email_disabled=0,
            only_admin_can_set_msg_top=0,
            add_friend_forbidden=0,
            group_live_switch=0,
            members_to_admin_chat=0,
            not_quit_when_emp_leave=0,
            only_admin_can_add_mem=0
        )
        create_scene_group_request = dingtalkim__1__0_models.CreateSceneGroupRequest(
            title='客户群',
            icon='@lADOADma*****QKA',
            template_id='c354***-***-***-b4ea-6f1ab***65',
            owner_user_id='1107****2120',
            user_ids=[
                '1107****2120'
            ],
            subadmin_ids=[
                '1107****2120'
            ],
            uuid='asdazxc',
            management_options=management_options
        )
        try:
            client.create_scene_group_with_options(create_scene_group_request, create_scene_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_scene_group_headers = dingtalkim__1__0_models.CreateSceneGroupHeaders()
        create_scene_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.CreateSceneGroupRequestManagementOptions(
            mention_all_authority=0,
            show_history_type=0,
            validation_type=0,
            searchable=0,
            chat_banned_type=0,
            management_type=0,
            only_admin_can_ding=0,
            all_members_can_create_mcs_conf=0,
            all_members_can_create_calendar=0,
            group_email_disabled=0,
            only_admin_can_set_msg_top=0,
            add_friend_forbidden=0,
            group_live_switch=0,
            members_to_admin_chat=0,
            not_quit_when_emp_leave=0,
            only_admin_can_add_mem=0
        )
        create_scene_group_request = dingtalkim__1__0_models.CreateSceneGroupRequest(
            title='客户群',
            icon='@lADOADma*****QKA',
            template_id='c354***-***-***-b4ea-6f1ab***65',
            owner_user_id='1107****2120',
            user_ids=[
                '1107****2120'
            ],
            subadmin_ids=[
                '1107****2120'
            ],
            uuid='asdazxc',
            management_options=management_options
        )
        try:
            await client.create_scene_group_with_options_async(create_scene_group_request, create_scene_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateSceneGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateSceneGroupRequest\managementOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateSceneGroupRequest;
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
        $createSceneGroupHeaders = new CreateSceneGroupHeaders([]);
        $createSceneGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $managementOptions = new managementOptions([
            "mentionAllAuthority" => 0,
            "showHistoryType" => 0,
            "validationType" => 0,
            "searchable" => 0,
            "chatBannedType" => 0,
            "managementType" => 0,
            "onlyAdminCanDing" => 0,
            "allMembersCanCreateMcsConf" => 0,
            "allMembersCanCreateCalendar" => 0,
            "groupEmailDisabled" => 0,
            "onlyAdminCanSetMsgTop" => 0,
            "addFriendForbidden" => 0,
            "groupLiveSwitch" => 0,
            "membersToAdminChat" => 0,
            "notQuitWhenEmpLeave" => 0,
            "onlyAdminCanAddMem" => 0
        ]);
        $createSceneGroupRequest = new CreateSceneGroupRequest([
            "title" => "客户群",
            "icon" => "@lADOADma*****QKA",
            "templateId" => "c354***-***-***-b4ea-6f1ab***65",
            "ownerUserId" => "1107****2120",
            "userIds" => [
                "1107****2120"
            ],
            "subadminIds" => [
                "1107****2120"
            ],
            "uuid" => "asdazxc",
            "managementOptions" => $managementOptions
        ]);
        try {
            $client->createSceneGroupWithOptions($createSceneGroupRequest, $createSceneGroupHeaders, new RuntimeOptions([]));
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

  createSceneGroupHeaders := &dingtalkim_1_0.CreateSceneGroupHeaders{}
  createSceneGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  managementOptions := &dingtalkim_1_0.CreateSceneGroupRequestManagementOptions{
    MentionAllAuthority: tea.Int32(0),
    ShowHistoryType: tea.Int32(0),
    ValidationType: tea.Int32(0),
    Searchable: tea.Int32(0),
    ChatBannedType: tea.Int32(0),
    ManagementType: tea.Int32(0),
    OnlyAdminCanDing: tea.Int32(0),
    AllMembersCanCreateMcsConf: tea.Int32(0),
    AllMembersCanCreateCalendar: tea.Int32(0),
    GroupEmailDisabled: tea.Int32(0),
    OnlyAdminCanSetMsgTop: tea.Int32(0),
    AddFriendForbidden: tea.Int32(0),
    GroupLiveSwitch: tea.Int32(0),
    MembersToAdminChat: tea.Int32(0),
    NotQuitWhenEmpLeave: tea.Int32(0),
    OnlyAdminCanAddMem: tea.Int32(0),
  }
  createSceneGroupRequest := &dingtalkim_1_0.CreateSceneGroupRequest{
    Title: tea.String("客户群"),
    Icon: tea.String("@lADOADma*****QKA"),
    TemplateId: tea.String("c354***-***-***-b4ea-6f1ab***65"),
    OwnerUserId: tea.String("1107****2120"),
    UserIds: []*string{tea.String("1107****2120")},
    SubadminIds: []*string{tea.String("1107****2120")},
    Uuid: tea.String("asdazxc"),
    ManagementOptions: managementOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateSceneGroupWithOptions(createSceneGroupRequest, createSceneGroupHeaders, &util.RuntimeOptions{})
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
    let createSceneGroupHeaders = new dingtalkim_1_0.CreateSceneGroupHeaders({ });
    createSceneGroupHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let managementOptions = new dingtalkim_1_0.CreateSceneGroupRequestManagementOptions({
      mentionAllAuthority: 0,
      showHistoryType: 0,
      validationType: 0,
      searchable: 0,
      chatBannedType: 0,
      managementType: 0,
      onlyAdminCanDing: 0,
      allMembersCanCreateMcsConf: 0,
      allMembersCanCreateCalendar: 0,
      groupEmailDisabled: 0,
      onlyAdminCanSetMsgTop: 0,
      addFriendForbidden: 0,
      groupLiveSwitch: 0,
      membersToAdminChat: 0,
      notQuitWhenEmpLeave: 0,
      onlyAdminCanAddMem: 0,
    });
    let createSceneGroupRequest = new dingtalkim_1_0.CreateSceneGroupRequest({
      title: '客户群',
      icon: '@lADOADma*****QKA',
      templateId: 'c354***-***-***-b4ea-6f1ab***65',
      ownerUserId: '1107****2120',
      userIds: [
        '1107****2120'
      ],
      subadminIds: [
        '1107****2120'
      ],
      uuid: 'asdazxc',
      managementOptions: managementOptions,
    });
    try {
      await client.createSceneGroupWithOptions(createSceneGroupRequest, createSceneGroupHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateSceneGroupHeaders createSceneGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateSceneGroupHeaders();
            createSceneGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateSceneGroupRequest.CreateSceneGroupRequestManagementOptions managementOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateSceneGroupRequest.CreateSceneGroupRequestManagementOptions
            {
                MentionAllAuthority = 0,
                ShowHistoryType = 0,
                ValidationType = 0,
                Searchable = 0,
                ChatBannedType = 0,
                ManagementType = 0,
                OnlyAdminCanDing = 0,
                AllMembersCanCreateMcsConf = 0,
                AllMembersCanCreateCalendar = 0,
                GroupEmailDisabled = 0,
                OnlyAdminCanSetMsgTop = 0,
                AddFriendForbidden = 0,
                GroupLiveSwitch = 0,
                MembersToAdminChat = 0,
                NotQuitWhenEmpLeave = 0,
                OnlyAdminCanAddMem = 0,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateSceneGroupRequest createSceneGroupRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateSceneGroupRequest
            {
                Title = "客户群",
                Icon = "@lADOADma*****QKA",
                TemplateId = "c354***-***-***-b4ea-6f1ab***65",
                OwnerUserId = "1107****2120",
                UserIds = new List<string>
                {
                    "1107****2120"
                },
                SubadminIds = new List<string>
                {
                    "1107****2120"
                },
                Uuid = "asdazxc",
                ManagementOptions = managementOptions,
            };
            try
            {
                client.CreateSceneGroupWithOptions(createSceneGroupRequest, createSceneGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| open\_conversation\_id | String | 群会话ID。 |
| chat\_id | String | 群会话ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "open_conversation_id" : "cidxxxxxx==",
  "chat_id" : "chatxxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.invalid | 输入参数错误 | 根据接口要求，传入必要参数。 |
| 400 | member.exceed | 群成员数量超出限制 | 群成员数量超出限制 |
| 400 | groupTemplate.permessionDenied.orgNotInGrayList | 企业未在模板灰度名单内 | 企业未在模板灰度名单内 |
| 400 | groupTemplate.permessionDenied.appNotInstalled | 应用没有安装到目标企业 | 应用没有安装到目标企业 |
| 400 | groupTemplate.permessionDenied.orgNotConsistent | 企业内部应用模板，不能在其他企业使用 | 企业内部应用模板，不能在其他企业使用 |
| 400 | permession.checkFailed | 权限校验失败 | 权限校验失败 |
| 400 | groupTemplate.notFound | 群模板不存在或者已下线 | 群模板不存在或者已下线 |
| 400 | member.notFound | 不存在的员工 | 请确认群主的userid是否正确 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 500 | system.error | 请重试，若始终失败请提交工单 | 请重试，若始终失败请提交工单 |
