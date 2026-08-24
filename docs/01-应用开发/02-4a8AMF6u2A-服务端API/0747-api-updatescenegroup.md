---
title: "更新场景群"
source_url: "https://open.dingtalk.com/document/development/api-updatescenegroup"
namespace: "development"
slug: "api-updatescenegroup"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 更新场景群"
doc_id: "VHFU1ECTWm"
updated_at: "2026-06-10 18:24:31"
---

> Source: https://open.dingtalk.com/document/development/api-updatescenegroup
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 更新场景群
> Updated: 2026-06-10 18:24:31

# 更新场景群

调用本接口，根据群ID更新群信息，适用于企业需要对已创建的群聊信息进行修改的场景，如调整群名称、群主、群权限等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroup/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 群ID，调用[创建场景群](0746-create-a-scene-group.md)接口获取open\_conversation\_id参数值。 |
| title | String | 否 | 群名称，最长不超过30字符，建议长度在10字符以内。 |
| icon | String | 否 | 群头像，通过[上传媒体文件](0646-upload-media-files.md)接口上传头像后获取mediaId。 |
| owner\_user\_id | String | 否 | 群主userId。 |
| owner\_union\_id | String | 否 | 群主unionId。 |
| management\_options | Object | 否 | 属性配置。 |
| mention\_all\_authority | Integer | 否 | @all 权限：   - **0**（默认）：所有人都可以@all - **1**：仅群主可@all |
| show\_history\_type | Integer | 否 | 新成员是否可查看聊天历史消息：   - **0**（默认）：不可以查看历史记录 - **1**：可以查看历史记录 |
| validation\_type | Integer | 否 | 入群是否需要验证：   - **0**（默认）：不验证入群 - **1**：入群验证 |
| searchable | Integer | 否 | 是否开启群禁言：   - **0**（默认）：不禁言 - **1**：全员禁言 |
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
| plugin\_customize\_verify | Integer | 否 | 自定义群插件是否需要群主和管理员审批：   - **0**（默认）：不需要审批 - **1**：需要审批 |
| not\_quit\_when\_emp\_leave | Integer | 否 | 员工离职后是否不退出群   - **0**（默认）：退组织时退出群 - **1**：退组织时不退出群       只对外部群生效。 |
| only\_admin\_can\_add\_mem | Integer | 否 | 仅群主/管理员可邀人，   - **0**：默认，所有人可邀人 - **1**：仅群主/管理员       `management_type`为1时，这个配置才生效。 |

### 请求示例

HTTP

```
POST /v1.0/im/sceneGroup/update HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1b*****
Content-Type:application/json

{
  "open_conversation_id" : "cidxxxxxx==",
  "title" : "客户群",
  "icon" : "@lADOADma*****QKA",
  "owner_user_id" : "1107****2120",
  "owner_union_id" : "unionid****",
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
    "plugin_customize_verify" : 0,
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
        com.aliyun.dingtalkim_1_0.models.UpdateSceneGroupHeaders updateSceneGroupHeaders = new com.aliyun.dingtalkim_1_0.models.UpdateSceneGroupHeaders();
        updateSceneGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.UpdateSceneGroupRequest.UpdateSceneGroupRequestManagementOptions managementOptions = new com.aliyun.dingtalkim_1_0.models.UpdateSceneGroupRequest.UpdateSceneGroupRequestManagementOptions()
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
                .setPluginCustomizeVerify(0)
                .setNotQuitWhenEmpLeave(0)
                .setOnlyAdminCanAddMem(0);
        com.aliyun.dingtalkim_1_0.models.UpdateSceneGroupRequest updateSceneGroupRequest = new com.aliyun.dingtalkim_1_0.models.UpdateSceneGroupRequest()
                .setOpenConversationId("cidxxxxxx==")
                .setTitle("客户群")
                .setIcon("@lADOADma*****QKA")
                .setOwnerUserId("1107****2120")
                .setOwnerUnionId("unionid****")
                .setManagementOptions(managementOptions);
        try {
            client.updateSceneGroupWithOptions(updateSceneGroupRequest, updateSceneGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_scene_group_headers = dingtalkim__1__0_models.UpdateSceneGroupHeaders()
        update_scene_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.UpdateSceneGroupRequestManagementOptions(
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
            plugin_customize_verify=0,
            not_quit_when_emp_leave=0,
            only_admin_can_add_mem=0
        )
        update_scene_group_request = dingtalkim__1__0_models.UpdateSceneGroupRequest(
            open_conversation_id='cidxxxxxx==',
            title='客户群',
            icon='@lADOADma*****QKA',
            owner_user_id='1107****2120',
            owner_union_id='unionid****',
            management_options=management_options
        )
        try:
            client.update_scene_group_with_options(update_scene_group_request, update_scene_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_scene_group_headers = dingtalkim__1__0_models.UpdateSceneGroupHeaders()
        update_scene_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_options = dingtalkim__1__0_models.UpdateSceneGroupRequestManagementOptions(
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
            plugin_customize_verify=0,
            not_quit_when_emp_leave=0,
            only_admin_can_add_mem=0
        )
        update_scene_group_request = dingtalkim__1__0_models.UpdateSceneGroupRequest(
            open_conversation_id='cidxxxxxx==',
            title='客户群',
            icon='@lADOADma*****QKA',
            owner_user_id='1107****2120',
            owner_union_id='unionid****',
            management_options=management_options
        )
        try:
            await client.update_scene_group_with_options_async(update_scene_group_request, update_scene_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateSceneGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateSceneGroupRequest\managementOptions;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateSceneGroupRequest;
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
        $updateSceneGroupHeaders = new UpdateSceneGroupHeaders([]);
        $updateSceneGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
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
            "pluginCustomizeVerify" => 0,
            "notQuitWhenEmpLeave" => 0,
            "onlyAdminCanAddMem" => 0
        ]);
        $updateSceneGroupRequest = new UpdateSceneGroupRequest([
            "openConversationId" => "cidxxxxxx==",
            "title" => "客户群",
            "icon" => "@lADOADma*****QKA",
            "ownerUserId" => "1107****2120",
            "ownerUnionId" => "unionid****",
            "managementOptions" => $managementOptions
        ]);
        try {
            $client->updateSceneGroupWithOptions($updateSceneGroupRequest, $updateSceneGroupHeaders, new RuntimeOptions([]));
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

  updateSceneGroupHeaders := &dingtalkim_1_0.UpdateSceneGroupHeaders{}
  updateSceneGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  managementOptions := &dingtalkim_1_0.UpdateSceneGroupRequestManagementOptions{
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
    PluginCustomizeVerify: tea.Int32(0),
    NotQuitWhenEmpLeave: tea.Int32(0),
    OnlyAdminCanAddMem: tea.Int32(0),
  }
  updateSceneGroupRequest := &dingtalkim_1_0.UpdateSceneGroupRequest{
    OpenConversationId: tea.String("cidxxxxxx=="),
    Title: tea.String("客户群"),
    Icon: tea.String("@lADOADma*****QKA"),
    OwnerUserId: tea.String("1107****2120"),
    OwnerUnionId: tea.String("unionid****"),
    ManagementOptions: managementOptions,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateSceneGroupWithOptions(updateSceneGroupRequest, updateSceneGroupHeaders, &util.RuntimeOptions{})
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
    let updateSceneGroupHeaders = new dingtalkim_1_0.UpdateSceneGroupHeaders({ });
    updateSceneGroupHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let managementOptions = new dingtalkim_1_0.UpdateSceneGroupRequestManagementOptions({
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
      pluginCustomizeVerify: 0,
      notQuitWhenEmpLeave: 0,
      onlyAdminCanAddMem: 0,
    });
    let updateSceneGroupRequest = new dingtalkim_1_0.UpdateSceneGroupRequest({
      openConversationId: 'cidxxxxxx==',
      title: '客户群',
      icon: '@lADOADma*****QKA',
      ownerUserId: '1107****2120',
      ownerUnionId: 'unionid****',
      managementOptions: managementOptions,
    });
    try {
      await client.updateSceneGroupWithOptions(updateSceneGroupRequest, updateSceneGroupHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateSceneGroupHeaders updateSceneGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateSceneGroupHeaders();
            updateSceneGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateSceneGroupRequest.UpdateSceneGroupRequestManagementOptions managementOptions = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateSceneGroupRequest.UpdateSceneGroupRequestManagementOptions
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
                PluginCustomizeVerify = 0,
                NotQuitWhenEmpLeave = 0,
                OnlyAdminCanAddMem = 0,
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateSceneGroupRequest updateSceneGroupRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateSceneGroupRequest
            {
                OpenConversationId = "cidxxxxxx==",
                Title = "客户群",
                Icon = "@lADOADma*****QKA",
                OwnerUserId = "1107****2120",
                OwnerUnionId = "unionid****",
                ManagementOptions = managementOptions,
            };
            try
            {
                client.UpdateSceneGroupWithOptions(updateSceneGroupRequest, updateSceneGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
