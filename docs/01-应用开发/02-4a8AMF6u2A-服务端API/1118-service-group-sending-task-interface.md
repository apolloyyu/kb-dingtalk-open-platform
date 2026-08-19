---
title: "群发任务"
source_url: "https://open.dingtalk.com/document/development/service-group-sending-task-interface"
namespace: "development"
slug: "service-group-sending-task-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 群发任务"
doc_id: "wX4Rd0AFnr"
updated_at: "2026-04-22 20:24:46"
---

> Source: https://open.dingtalk.com/document/development/service-group-sending-task-interface
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 服务群 > 群发任务
> Updated: 2026-04-22 20:24:46

# 群发任务

调用本接口新增群发任务，实现效果与下图类似：

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/messages/tasks/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ServiceGroup.Message.Send-场景服务群发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openTeamId | String | 是 | 团队ID。  image |
| taskName | String | 是 | 群发任务名称。 |
| messageContent | Object | 是 | 群发内容。 |
| atAll | Boolean | 否 | 是否@全部人员：   - **true**：是 - **false**：否 |
| atActiveUser | Boolean | 否 | 是否@活跃成员：   - **true**：是 - **false**：否 |
| messageType | String | 是 | 消息类型，取值：   - **MARKDOWN**：markdowm消息 - **ACTIONCARD**：卡片消息 - **NOTICE**：群公告 |
| title | String | 否 | 标题。 |
| content | String | 否 | 消息内容。 |
| images | Array of String | 否 | 图片链接。 |
| btns | Array | 否 | 按钮列表。 |
| actionURL | String | 否 | 按钮链接。 |
| title | String | 否 | 按钮标题。 |
| atActiveMemberNum | Long | 否 | @活跃成员数量。 |
| top | Boolean | 否 | 是否置顶。   - **true**：置顶 - **false**：不置顶 |
| remind | Boolean | 否 | 是否钉群成员。   - **true**：是 - **false**：否 |
| queryGroup | Object | 是 | 查询条件。 |
| queryType | String | 是 | 群发圈选类型，取值：   - **AIMED**：精准圈选 - **MULTI\_CONDITIONS**：多条件圈选 |
| openConversationIds | Array of String | 否 | 单个会话ID。 |
| lastActiveTimeStart | String | 否 | 最近活跃时间的开始时间。 |
| lastActiveTimeEnd | String | 否 | 最近活跃时间的结束时间。 |
| lastActiveDateFilterType | String | 否 | 活跃日期筛选类型，取值：   - **ACTIVE**：活跃 - **NOTACTIVE**：不活跃 |
| groupTagNames | Array of String | 否 | 群标签。 |
| openGroupSetId | String | 否 | 群分组ID。  image |
| sendConfig | Object | 是 | 发送配置。 |
| sendType | String | 是 | 发送类型，取值：   - **TIMING**：定时执行 - **INSTANT**：立即执行 |
| sendTime | String | 否 | 执行时间。    当**sendType**的值为**TIMING**时传入。 |
| needUrlTrack | Boolean | 否 | 是否链接追踪。 |
| urlTrackConfig | Array | 否 | 只有needUrlTrack取值true时，才需要进行链接跟踪配置。 |
| trackUrl | String | 否 | 跟踪链接URL。 |
| title | String | 否 | 跟踪链接的标题。 |
| trackId | String | 否 | 跟踪链接的唯一标识，sg开头。 |

### 请求示例

HTTP

```
POST /v1.0/serviceGroup/messages/tasks/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:jsahgxxx
Content-Type:application/json

{
  "openTeamId" : "223588",
  "taskName" : "群发任务",
  "messageContent" : {
    "atAll" : true,
    "atActiveUser" : false,
    "messageType" : "MARKDOWN",
    "title" : "群发内容标题",
    "content" : "群发内容",
    "images" : [ "http://www.baidu.com" ],
    "btns" : [ {
      "actionURL" : "http://www.dingtalk.com",
      "title" : "按钮标题"
    } ],
    "atActiveMemberNum" : 5,
    "top" : true,
    "remind" : true
  },
  "queryGroup" : {
    "queryType" : "MULTI_CONDITIONS",
    "openConversationIds" : [ "cid****" ],
    "lastActiveTimeStart" : "2021-10-01 00:00:00",
    "lastActiveTimeEnd" : "2021-10-03 00:00:00",
    "lastActiveDateFilterType" : "ACTIVE",
    "groupTagNames" : [ "标签1" ],
    "openGroupSetId" : "2222"
  },
  "sendConfig" : {
    "sendType" : "TIMING",
    "sendTime" : "2021-10-03 00:00:00",
    "needUrlTrack" : false,
    "urlTrackConfig" : [ {
      "trackUrl" : "http://www.dingtalk.com",
      "title" : "按钮链接1",
      "trackId" : "sg00001"
    } ]
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkservice_group_1_0.*;
import com.aliyun.dingtalkservice_group_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkservice_group_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkservice_group_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkservice_group_1_0.Client client = Sample.createClient();
        SendMsgByTaskHeaders sendMsgByTaskHeaders = new SendMsgByTaskHeaders();
        sendMsgByTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendMsgByTaskRequest.SendMsgByTaskRequestSendConfigUrlTrackConfig sendConfigUrlTrackConfig0 = new SendMsgByTaskRequest.SendMsgByTaskRequestSendConfigUrlTrackConfig()
                .setTrackUrl("http://www.dingtalk.com")
                .setTitle("按钮链接1")
                .setTrackId("sg00001");
        SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig sendConfig = new SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig()
                .setSendType("TIMING")
                .setSendTime("2021-10-03 00:00:00")
                .setNeedUrlTrack(false)
                .setUrlTrackConfig(java.util.Arrays.asList(
                    sendConfigUrlTrackConfig0
                ));
        SendMsgByTaskRequest.SendMsgByTaskRequestQueryGroup queryGroup = new SendMsgByTaskRequest.SendMsgByTaskRequestQueryGroup()
                .setQueryType("MULTI_CONDITIONS")
                .setOpenConversationIds(java.util.Arrays.asList(
                    "cid****"
                ))
                .setLastActiveTimeStart("2021-10-01 00:00:00")
                .setLastActiveTimeEnd("2021-10-03 00:00:00")
                .setLastActiveDateFilterType("ACTIVE")
                .setGroupTagNames(java.util.Arrays.asList(
                    "标签1"
                ))
                .setOpenGroupSetId("2222");
        SendMsgByTaskRequest.SendMsgByTaskRequestMessageContentBtns messageContentBtns0 = new SendMsgByTaskRequest.SendMsgByTaskRequestMessageContentBtns()
                .setActionURL("http://www.dingtalk.com")
                .setTitle("按钮标题");
        SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent messageContent = new SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent()
                .setAtAll(true)
                .setAtActiveUser(false)
                .setMessageType("MARKDOWN")
                .setTitle("群发内容标题")
                .setContent("群发内容")
                .setImages(java.util.Arrays.asList(
                    "http://www.baidu.com"
                ))
                .setBtns(java.util.Arrays.asList(
                    messageContentBtns0
                ))
                .setAtActiveMemberNum(5L)
                .setTop(true)
                .setRemind(true);
        SendMsgByTaskRequest sendMsgByTaskRequest = new SendMsgByTaskRequest()
                .setOpenTeamId("223588")
                .setTaskName("群发任务")
                .setMessageContent(messageContent)
                .setQueryGroup(queryGroup)
                .setSendConfig(sendConfig);
        try {
            client.sendMsgByTaskWithOptions(sendMsgByTaskRequest, sendMsgByTaskHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.serviceGroup_1_0.client import Client as dingtalkserviceGroup_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.serviceGroup_1_0 import models as dingtalkservice_group__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkserviceGroup_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkserviceGroup_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_msg_by_task_headers = dingtalkservice_group__1__0_models.SendMsgByTaskHeaders()
        send_msg_by_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_config_url_track_config_0 = dingtalkservice_group__1__0_models.SendMsgByTaskRequestSendConfigUrlTrackConfig(
            track_url='http://www.dingtalk.com',
            title='按钮链接1',
            track_id='sg00001'
        )
        send_config = dingtalkservice_group__1__0_models.SendMsgByTaskRequestSendConfig(
            send_type='TIMING',
            send_time='2021-10-03 00:00:00',
            need_url_track=False,
            url_track_config=[
                send_config_url_track_config_0
            ]
        )
        query_group = dingtalkservice_group__1__0_models.SendMsgByTaskRequestQueryGroup(
            query_type='MULTI_CONDITIONS',
            open_conversation_ids=[
                'cid****'
            ],
            last_active_time_start='2021-10-01 00:00:00',
            last_active_time_end='2021-10-03 00:00:00',
            last_active_date_filter_type='ACTIVE',
            group_tag_names=[
                '标签1'
            ],
            open_group_set_id='2222'
        )
        message_content_btns_0 = dingtalkservice_group__1__0_models.SendMsgByTaskRequestMessageContentBtns(
            action_url='http://www.dingtalk.com',
            title='按钮标题'
        )
        message_content = dingtalkservice_group__1__0_models.SendMsgByTaskRequestMessageContent(
            at_all=True,
            at_active_user=False,
            message_type='MARKDOWN',
            title='群发内容标题',
            content='群发内容',
            images=[
                'http://www.baidu.com'
            ],
            btns=[
                message_content_btns_0
            ],
            at_active_member_num=5,
            top=True,
            remind=True
        )
        send_msg_by_task_request = dingtalkservice_group__1__0_models.SendMsgByTaskRequest(
            open_team_id='223588',
            task_name='群发任务',
            message_content=message_content,
            query_group=query_group,
            send_config=send_config
        )
        try:
            client.send_msg_by_task_with_options(send_msg_by_task_request, send_msg_by_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_msg_by_task_headers = dingtalkservice_group__1__0_models.SendMsgByTaskHeaders()
        send_msg_by_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_config_url_track_config_0 = dingtalkservice_group__1__0_models.SendMsgByTaskRequestSendConfigUrlTrackConfig(
            track_url='http://www.dingtalk.com',
            title='按钮链接1',
            track_id='sg00001'
        )
        send_config = dingtalkservice_group__1__0_models.SendMsgByTaskRequestSendConfig(
            send_type='TIMING',
            send_time='2021-10-03 00:00:00',
            need_url_track=False,
            url_track_config=[
                send_config_url_track_config_0
            ]
        )
        query_group = dingtalkservice_group__1__0_models.SendMsgByTaskRequestQueryGroup(
            query_type='MULTI_CONDITIONS',
            open_conversation_ids=[
                'cid****'
            ],
            last_active_time_start='2021-10-01 00:00:00',
            last_active_time_end='2021-10-03 00:00:00',
            last_active_date_filter_type='ACTIVE',
            group_tag_names=[
                '标签1'
            ],
            open_group_set_id='2222'
        )
        message_content_btns_0 = dingtalkservice_group__1__0_models.SendMsgByTaskRequestMessageContentBtns(
            action_url='http://www.dingtalk.com',
            title='按钮标题'
        )
        message_content = dingtalkservice_group__1__0_models.SendMsgByTaskRequestMessageContent(
            at_all=True,
            at_active_user=False,
            message_type='MARKDOWN',
            title='群发内容标题',
            content='群发内容',
            images=[
                'http://www.baidu.com'
            ],
            btns=[
                message_content_btns_0
            ],
            at_active_member_num=5,
            top=True,
            remind=True
        )
        send_msg_by_task_request = dingtalkservice_group__1__0_models.SendMsgByTaskRequest(
            open_team_id='223588',
            task_name='群发任务',
            message_content=message_content,
            query_group=query_group,
            send_config=send_config
        )
        try:
            await client.send_msg_by_task_with_options_async(send_msg_by_task_request, send_msg_by_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskRequest\sendConfig\urlTrackConfig;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskRequest\sendConfig;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskRequest\queryGroup;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskRequest\messageContent\btns;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskRequest\messageContent;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\SendMsgByTaskRequest;
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
        $sendMsgByTaskHeaders = new SendMsgByTaskHeaders([]);
        $sendMsgByTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendConfigUrlTrackConfig0 = new urlTrackConfig([
            "trackUrl" => "http://www.dingtalk.com",
            "title" => "按钮链接1",
            "trackId" => "sg00001"
        ]);
        $sendConfig = new sendConfig([
            "sendType" => "TIMING",
            "sendTime" => "2021-10-03 00:00:00",
            "needUrlTrack" => false,
            "urlTrackConfig" => [
                $sendConfigUrlTrackConfig0
            ]
        ]);
        $queryGroup = new queryGroup([
            "queryType" => "MULTI_CONDITIONS",
            "openConversationIds" => [
                "cid****"
            ],
            "lastActiveTimeStart" => "2021-10-01 00:00:00",
            "lastActiveTimeEnd" => "2021-10-03 00:00:00",
            "lastActiveDateFilterType" => "ACTIVE",
            "groupTagNames" => [
                "标签1"
            ],
            "openGroupSetId" => "2222"
        ]);
        $messageContentBtns0 = new btns([
            "actionURL" => "http://www.dingtalk.com",
            "title" => "按钮标题"
        ]);
        $messageContent = new messageContent([
            "atAll" => true,
            "atActiveUser" => false,
            "messageType" => "MARKDOWN",
            "title" => "群发内容标题",
            "content" => "群发内容",
            "images" => [
                "http://www.baidu.com"
            ],
            "btns" => [
                $messageContentBtns0
            ],
            "atActiveMemberNum" => 5,
            "top" => true,
            "remind" => true
        ]);
        $sendMsgByTaskRequest = new SendMsgByTaskRequest([
            "openTeamId" => "223588",
            "taskName" => "群发任务",
            "messageContent" => $messageContent,
            "queryGroup" => $queryGroup,
            "sendConfig" => $sendConfig
        ]);
        try {
            $client->sendMsgByTaskWithOptions($sendMsgByTaskRequest, $sendMsgByTaskHeaders, new RuntimeOptions([]));
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
  dingtalkservicegroup_1_0  "github.com/alibabacloud-go/dingtalk/serviceGroup_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkservicegroup_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkservicegroup_1_0.Client{}
  _result, _err = dingtalkservicegroup_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendMsgByTaskHeaders := &dingtalkservicegroup_1_0.SendMsgByTaskHeaders{}
  sendMsgByTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendConfigUrlTrackConfig0 := &dingtalkservicegroup_1_0.SendMsgByTaskRequestSendConfigUrlTrackConfig{
    TrackUrl: tea.String("http://www.dingtalk.com"),
    Title: tea.String("按钮链接1"),
    TrackId: tea.String("sg00001"),
  }
  sendConfig := &dingtalkservicegroup_1_0.SendMsgByTaskRequestSendConfig{
    SendType: tea.String("TIMING"),
    SendTime: tea.String("2021-10-03 00:00:00"),
    NeedUrlTrack: tea.Bool(false),
    UrlTrackConfig: []*dingtalkservicegroup_1_0.SendMsgByTaskRequestSendConfigUrlTrackConfig{sendConfigUrlTrackConfig0},
  }
  queryGroup := &dingtalkservicegroup_1_0.SendMsgByTaskRequestQueryGroup{
    QueryType: tea.String("MULTI_CONDITIONS"),
    OpenConversationIds: []*string{tea.String("cid****")},
    LastActiveTimeStart: tea.String("2021-10-01 00:00:00"),
    LastActiveTimeEnd: tea.String("2021-10-03 00:00:00"),
    LastActiveDateFilterType: tea.String("ACTIVE"),
    GroupTagNames: []*string{tea.String("标签1")},
    OpenGroupSetId: tea.String("2222"),
  }
  messageContentBtns0 := &dingtalkservicegroup_1_0.SendMsgByTaskRequestMessageContentBtns{
    ActionURL: tea.String("http://www.dingtalk.com"),
    Title: tea.String("按钮标题"),
  }
  messageContent := &dingtalkservicegroup_1_0.SendMsgByTaskRequestMessageContent{
    AtAll: tea.Bool(true),
    AtActiveUser: tea.Bool(false),
    MessageType: tea.String("MARKDOWN"),
    Title: tea.String("群发内容标题"),
    Content: tea.String("群发内容"),
    Images: []*string{tea.String("http://www.baidu.com")},
    Btns: []*dingtalkservicegroup_1_0.SendMsgByTaskRequestMessageContentBtns{messageContentBtns0},
    AtActiveMemberNum: tea.Int64(5),
    Top: tea.Bool(true),
    Remind: tea.Bool(true),
  }
  sendMsgByTaskRequest := &dingtalkservicegroup_1_0.SendMsgByTaskRequest{
    OpenTeamId: tea.String("223588"),
    TaskName: tea.String("群发任务"),
    MessageContent: messageContent,
    QueryGroup: queryGroup,
    SendConfig: sendConfig,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendMsgByTaskWithOptions(sendMsgByTaskRequest, sendMsgByTaskHeaders, &util.RuntimeOptions{})
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
import dingtalkserviceGroup_1_0, * as $dingtalkserviceGroup_1_0 from '@alicloud/dingtalk/serviceGroup_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkserviceGroup_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkserviceGroup_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let sendMsgByTaskHeaders = new $dingtalkserviceGroup_1_0.SendMsgByTaskHeaders({ });
    sendMsgByTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sendConfigUrlTrackConfig0 = new $dingtalkserviceGroup_1_0.SendMsgByTaskRequestSendConfigUrlTrackConfig({
      trackUrl: "http://www.dingtalk.com",
      title: "按钮链接1",
      trackId: "sg00001",
    });
    let sendConfig = new $dingtalkserviceGroup_1_0.SendMsgByTaskRequestSendConfig({
      sendType: "TIMING",
      sendTime: "2021-10-03 00:00:00",
      needUrlTrack: false,
      urlTrackConfig: [
        sendConfigUrlTrackConfig0
      ],
    });
    let queryGroup = new $dingtalkserviceGroup_1_0.SendMsgByTaskRequestQueryGroup({
      queryType: "MULTI_CONDITIONS",
      openConversationIds: [
        "cid****"
      ],
      lastActiveTimeStart: "2021-10-01 00:00:00",
      lastActiveTimeEnd: "2021-10-03 00:00:00",
      lastActiveDateFilterType: "ACTIVE",
      groupTagNames: [
        "标签1"
      ],
      openGroupSetId: "2222",
    });
    let messageContentBtns0 = new $dingtalkserviceGroup_1_0.SendMsgByTaskRequestMessageContentBtns({
      actionURL: "http://www.dingtalk.com",
      title: "按钮标题",
    });
    let messageContent = new $dingtalkserviceGroup_1_0.SendMsgByTaskRequestMessageContent({
      atAll: true,
      atActiveUser: false,
      messageType: "MARKDOWN",
      title: "群发内容标题",
      content: "群发内容",
      images: [
        "http://www.baidu.com"
      ],
      btns: [
        messageContentBtns0
      ],
      atActiveMemberNum: 5,
      top: true,
      remind: true,
    });
    let sendMsgByTaskRequest = new $dingtalkserviceGroup_1_0.SendMsgByTaskRequest({
      openTeamId: "223588",
      taskName: "群发任务",
      messageContent: messageContent,
      queryGroup: queryGroup,
      sendConfig: sendConfig,
    });
    try {
      await client.sendMsgByTaskWithOptions(sendMsgByTaskRequest, sendMsgByTaskHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskHeaders sendMsgByTaskHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskHeaders();
            sendMsgByTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig.SendMsgByTaskRequestSendConfigUrlTrackConfig sendConfigUrlTrackConfig0 = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig.SendMsgByTaskRequestSendConfigUrlTrackConfig
            {
                TrackUrl = "http://www.dingtalk.com",
                Title = "按钮链接1",
                TrackId = "sg00001",
            };
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig sendConfig = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig
            {
                SendType = "TIMING",
                SendTime = "2021-10-03 00:00:00",
                NeedUrlTrack = false,
                UrlTrackConfig = new List<AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestSendConfig.SendMsgByTaskRequestSendConfigUrlTrackConfig>
                {
                    sendConfigUrlTrackConfig0
                },
            };
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestQueryGroup queryGroup = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestQueryGroup
            {
                QueryType = "MULTI_CONDITIONS",
                OpenConversationIds = new List<string>
                {
                    "cid****"
                },
                LastActiveTimeStart = "2021-10-01 00:00:00",
                LastActiveTimeEnd = "2021-10-03 00:00:00",
                LastActiveDateFilterType = "ACTIVE",
                GroupTagNames = new List<string>
                {
                    "标签1"
                },
                OpenGroupSetId = "2222",
            };
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent.SendMsgByTaskRequestMessageContentBtns messageContentBtns0 = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent.SendMsgByTaskRequestMessageContentBtns
            {
                ActionURL = "http://www.dingtalk.com",
                Title = "按钮标题",
            };
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent messageContent = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent
            {
                AtAll = true,
                AtActiveUser = false,
                MessageType = "MARKDOWN",
                Title = "群发内容标题",
                Content = "群发内容",
                Images = new List<string>
                {
                    "http://www.baidu.com"
                },
                Btns = new List<AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest.SendMsgByTaskRequestMessageContent.SendMsgByTaskRequestMessageContentBtns>
                {
                    messageContentBtns0
                },
                AtActiveMemberNum = 5,
                Top = true,
                Remind = true,
            };
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest sendMsgByTaskRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.SendMsgByTaskRequest
            {
                OpenTeamId = "223588",
                TaskName = "群发任务",
                MessageContent = messageContent,
                QueryGroup = queryGroup,
                SendConfig = sendConfig,
            };
            try
            {
                client.SendMsgByTaskWithOptions(sendMsgByTaskRequest, sendMsgByTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkservice_group__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkservice_group_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkservice_group_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::Client> client = make_shared<Alibabacloud_Dingtalkservice_group_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskHeaders> sendMsgByTaskHeaders = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskHeaders>();
  sendMsgByTaskHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestSendConfigUrlTrackConfig> sendConfigUrlTrackConfig0 = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestSendConfigUrlTrackConfig>(map<string, boost::any>({
    {"trackUrl", boost::any(string("http://www.dingtalk.com"))},
    {"title", boost::any(string("按钮链接1"))},
    {"trackId", boost::any(string("sg00001"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestSendConfig> sendConfig = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestSendConfig>(map<string, boost::any>({
    {"sendType", boost::any(string("TIMING"))},
    {"sendTime", boost::any(string("2021-10-03 00:00:00"))},
    {"needUrlTrack", boost::any(false)},
    {"urlTrackConfig", boost::any(vector<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestSendConfigUrlTrackConfig>({
      sendConfigUrlTrackConfig0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestQueryGroup> queryGroup = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestQueryGroup>(map<string, boost::any>({
    {"queryType", boost::any(string("MULTI_CONDITIONS"))},
    {"openConversationIds", boost::any(vector<string>({
      "cid****"
    }))},
    {"lastActiveTimeStart", boost::any(string("2021-10-01 00:00:00"))},
    {"lastActiveTimeEnd", boost::any(string("2021-10-03 00:00:00"))},
    {"lastActiveDateFilterType", boost::any(string("ACTIVE"))},
    {"groupTagNames", boost::any(vector<string>({
      "标签1"
    }))},
    {"openGroupSetId", boost::any(string("2222"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestMessageContentBtns> messageContentBtns0 = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestMessageContentBtns>(map<string, boost::any>({
    {"actionURL", boost::any(string("http://www.dingtalk.com"))},
    {"title", boost::any(string("按钮标题"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestMessageContent> messageContent = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestMessageContent>(map<string, boost::any>({
    {"atAll", boost::any(true)},
    {"atActiveUser", boost::any(false)},
    {"messageType", boost::any(string("MARKDOWN"))},
    {"title", boost::any(string("群发内容标题"))},
    {"content", boost::any(string("群发内容"))},
    {"images", boost::any(vector<string>({
      "http://www.baidu.com"
    }))},
    {"btns", boost::any(vector<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequestMessageContentBtns>({
      messageContentBtns0
    }))},
    {"atActiveMemberNum", boost::any(5)},
    {"top", boost::any(true)},
    {"remind", boost::any(true)}
  }));
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequest> sendMsgByTaskRequest = make_shared<Alibabacloud_Dingtalkservice_group_1_0::SendMsgByTaskRequest>(map<string, boost::any>({
    {"openTeamId", boost::any(string("223588"))},
    {"taskName", boost::any(string("群发任务"))},
    {"messageContent", !messageContent ? boost::any() : boost::any(*messageContent)},
    {"queryGroup", !queryGroup ? boost::any() : boost::any(*queryGroup)},
    {"sendConfig", !sendConfig ? boost::any() : boost::any(*sendConfig)}
  }));
  try {
    client->sendMsgByTaskWithOptions(sendMsgByTaskRequest, sendMsgByTaskHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openBatchTaskId | String | 开放群发任务ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openBatchTaskId" : "111111"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | sendMessageSendConfigSendTypeInvalid | 群发消息发送配置发送类型无效 | 群发消息发送配置发送类型无效 |
| 400 | sendMessageSendConfigInvalid | 群发消息圈群条件圈群类型无效 | 群发消息圈群条件圈群类型无效 |
| 400 | sendMessageQueryGroupInvalid | 群发消息圈群条件无效 | 群发消息圈群条件无效 |
| 400 | sendMessageMessageContentInvalid | 群发消息内容无效 | 群发消息内容无效 |
| 400 | sendMessageMessageContentTitleInvalid | 群发消息标题无效 | 群发消息标题无效 |
| 400 | sendMessageMessageInvalid | 群发消息参数无效 | 群发消息参数无效 |
| 400 | sendMessageTaskNameInvalid | 群发任务名不正确，为空或者超过128字符 | 群发任务名不正确，为空或者超过128字符 |
| 400 | illegalPama | 参数非法 | 参数非法 |
| 500 | systemError | 系统异常 | 系统异常 |
