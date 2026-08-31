---
title: "更新会议室信息"
source_url: "https://open.dingtalk.com/document/development/update-meeting-room-information"
namespace: "development"
slug: "update-meeting-room-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 更新会议室信息"
doc_id: "C6fNaiDIR5"
updated_at: "2026-06-03 10:12:07"
---

> Source: https://open.dingtalk.com/document/development/update-meeting-room-information
> Path: 应用开发 / 服务端 API / 音视频 > 智能会议室 > 会议室 > 更新会议室信息
> Updated: 2026-06-03 10:12:07

# 更新会议室信息

调用本接口，更新会议室信息。

## 接口调用说明

更新会议室信息，只允许有智能会议室应用管理权限的管理员操作。 ![](https://img.alicdn.com/imgextra/i3/O1CN01v90IEz204A3gSD44X_!!6000000006795-2-tps-2498-1632.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/meetingRooms |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| roomId | String | 是 | 会议室ID，可调用[查询会议室列表](0437-check-the-meeting-room-list.md)接口获取。 |
| roomName | String | 否 | 会议室名称。 |
| roomCapacity | Integer | 否 | 会议室可容纳人数。 |
| roomPicture | String | 否 | 会议室图片。 |
| roomStatus | Integer | 否 | 会议室状态。   - **0**：全员可用 - **1**：仅管理员可用 - **2**：部分有权限 |
| roomLocation | Object | 否 | 会议室位置信息。 |
| title | String | 否 | 会议室位置标题。 |
| desc | String | 否 | 会议室位置详细信息。 |
| roomLabelIds | Array of Long | 否 | 标签ID。   - **1**：电视 - **2**：电话 - **3**：投影仪 - **4**：白板 - **5**：视频会议 |
| isvRoomId | String | 否 | 调用方外部会议室ID，调用方可传入自有系统内的会议室ID。      若调用方不与外部会议室关联，可传入本企业的实体会议室编号。 |
| groupId | Long | 否 | 会议室所属分组ID，可调用[查询会议室分组列表](0448-query-meeting-rooms-groups.md)接口获取。 |
| reservationAuthority | Object | 否 | roomStatus部分权限时，设置的会议室预定权限。 |
| authorizedMembers | Array | 否 | 有权限的成员列表。 |
| memberId | String | 否 | 成员的id，memberType设置   - **人员**：成员unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取 - **部门**：部门id，dept\_id，可调用[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取dept\_id参数值。 |
| memberType | String | 否 | 成员的类型，类型：   - **人员**：user - **部门**：dept |
| memberName | String | 否 | 成员的名称：   - **人员**：人员昵称 - **部门**：部门名称 |
| enableCycleReservation | Boolean | 否 | 会议室是否支持循环周期预定:   - **true**：是 - **false**：否 |
| openReservation | Boolean | 否 | 会议室是否开放预定:   - **true**：是 - **false**：否 |
| roomDescription | String | 否 | 会议室描述信息。 |

### 请求示例

HTTP

```
PUT /v1.0/rooms/meetingRooms HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "unionId" : "2iPOxxxxx",
  "roomId" : "0ffbxxxxx",
  "roomName" : "测试会议室",
  "roomCapacity" : 10,
  "roomPicture" : "https://static.dingtalk.com/media/lADPxxxxx.jpg",
  "roomStatus" : 0,
  "roomLocation" : {
    "title" : "xxx公司",
    "desc" : "xx市xx区xx路xx号"
  },
  "roomLabelIds" : [ 1 ],
  "isvRoomId" : "xxxIsvRoomId",
  "groupId" : 0,
  "reservationAuthority" : {
    "authorizedMembers" : [ {
      "memberId" : "lPHhSZDLXXXXXXpBlC9lxLwiEiE",
      "memberType" : "user",
      "memberName" : "张三"
    } ]
  },
  "enableCycleReservation" : false,
  "openReservation" : true,
  "roomDescription" : "此处添加对会议室的描述信息"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomHeaders updateMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomHeaders();
        updateMeetingRoomHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers reservationAuthorityAuthorizedMembers0 = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers()
                .setMemberId("lPHhSZDLXXXXXXpBlC9lxLwiEiE")
                .setMemberType("user")
                .setMemberName("张三");
        com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority reservationAuthority = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority()
                .setAuthorizedMembers(java.util.Arrays.asList(
                    reservationAuthorityAuthorizedMembers0
                ));
        com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation roomLocation = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation()
                .setTitle("xxx公司")
                .setDesc("xx市xx区xx路xx号");
        com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest updateMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.UpdateMeetingRoomRequest()
                .setUnionId("2iPOxxxxx")
                .setRoomId("0ffbxxxxx")
                .setRoomName("测试会议室")
                .setRoomCapacity(10)
                .setRoomPicture("https://static.dingtalk.com/media/lADPxxxxx.jpg")
                .setRoomStatus(0)
                .setRoomLocation(roomLocation)
                .setRoomLabelIds(java.util.Arrays.asList(
                    1L
                ))
                .setIsvRoomId("xxxIsvRoomId")
                .setGroupId(0L)
                .setReservationAuthority(reservationAuthority)
                .setEnableCycleReservation(false)
                .setOpenReservation(true)
                .setRoomDescription("此处添加对会议室的描述信息");
        try {
            client.updateMeetingRoomWithOptions(updateMeetingRoomRequest, updateMeetingRoomHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.rooms_1_0.client import Client as dingtalkrooms_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.rooms_1_0 import models as dingtalkrooms__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrooms_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrooms_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_meeting_room_headers = dingtalkrooms__1__0_models.UpdateMeetingRoomHeaders()
        update_meeting_room_headers.x_acs_dingtalk_access_token = '<your access token>'
        reservation_authority_authorized_members_0 = dingtalkrooms__1__0_models.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers(
            member_id='lPHhSZDLXXXXXXpBlC9lxLwiEiE',
            member_type='user',
            member_name='张三'
        )
        reservation_authority = dingtalkrooms__1__0_models.UpdateMeetingRoomRequestReservationAuthority(
            authorized_members=[
                reservation_authority_authorized_members_0
            ]
        )
        room_location = dingtalkrooms__1__0_models.UpdateMeetingRoomRequestRoomLocation(
            title='xxx公司',
            desc='xx市xx区xx路xx号'
        )
        update_meeting_room_request = dingtalkrooms__1__0_models.UpdateMeetingRoomRequest(
            union_id='2iPOxxxxx',
            room_id='0ffbxxxxx',
            room_name='测试会议室',
            room_capacity=10,
            room_picture='https://static.dingtalk.com/media/lADPxxxxx.jpg',
            room_status=0,
            room_location=room_location,
            room_label_ids=[
                1
            ],
            isv_room_id='xxxIsvRoomId',
            group_id=0,
            reservation_authority=reservation_authority,
            enable_cycle_reservation=False,
            open_reservation=True,
            room_description='此处添加对会议室的描述信息'
        )
        try:
            client.update_meeting_room_with_options(update_meeting_room_request, update_meeting_room_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_meeting_room_headers = dingtalkrooms__1__0_models.UpdateMeetingRoomHeaders()
        update_meeting_room_headers.x_acs_dingtalk_access_token = '<your access token>'
        reservation_authority_authorized_members_0 = dingtalkrooms__1__0_models.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers(
            member_id='lPHhSZDLXXXXXXpBlC9lxLwiEiE',
            member_type='user',
            member_name='张三'
        )
        reservation_authority = dingtalkrooms__1__0_models.UpdateMeetingRoomRequestReservationAuthority(
            authorized_members=[
                reservation_authority_authorized_members_0
            ]
        )
        room_location = dingtalkrooms__1__0_models.UpdateMeetingRoomRequestRoomLocation(
            title='xxx公司',
            desc='xx市xx区xx路xx号'
        )
        update_meeting_room_request = dingtalkrooms__1__0_models.UpdateMeetingRoomRequest(
            union_id='2iPOxxxxx',
            room_id='0ffbxxxxx',
            room_name='测试会议室',
            room_capacity=10,
            room_picture='https://static.dingtalk.com/media/lADPxxxxx.jpg',
            room_status=0,
            room_location=room_location,
            room_label_ids=[
                1
            ],
            isv_room_id='xxxIsvRoomId',
            group_id=0,
            reservation_authority=reservation_authority,
            enable_cycle_reservation=False,
            open_reservation=True,
            room_description='此处添加对会议室的描述信息'
        )
        try:
            await client.update_meeting_room_with_options_async(update_meeting_room_request, update_meeting_room_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateMeetingRoomHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateMeetingRoomRequest\reservationAuthority\authorizedMembers;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateMeetingRoomRequest\reservationAuthority;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateMeetingRoomRequest\roomLocation;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateMeetingRoomRequest;
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
        $updateMeetingRoomHeaders = new UpdateMeetingRoomHeaders([]);
        $updateMeetingRoomHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $reservationAuthorityAuthorizedMembers0 = new authorizedMembers([
            "memberId" => "lPHhSZDLXXXXXXpBlC9lxLwiEiE",
            "memberType" => "user",
            "memberName" => "张三"
        ]);
        $reservationAuthority = new reservationAuthority([
            "authorizedMembers" => [
                $reservationAuthorityAuthorizedMembers0
            ]
        ]);
        $roomLocation = new roomLocation([
            "title" => "xxx公司",
            "desc" => "xx市xx区xx路xx号"
        ]);
        $updateMeetingRoomRequest = new UpdateMeetingRoomRequest([
            "unionId" => "2iPOxxxxx",
            "roomId" => "0ffbxxxxx",
            "roomName" => "测试会议室",
            "roomCapacity" => 10,
            "roomPicture" => "https://static.dingtalk.com/media/lADPxxxxx.jpg",
            "roomStatus" => 0,
            "roomLocation" => $roomLocation,
            "roomLabelIds" => [
                1
            ],
            "isvRoomId" => "xxxIsvRoomId",
            "groupId" => 0,
            "reservationAuthority" => $reservationAuthority,
            "enableCycleReservation" => false,
            "openReservation" => true,
            "roomDescription" => "此处添加对会议室的描述信息"
        ]);
        try {
            $client->updateMeetingRoomWithOptions($updateMeetingRoomRequest, $updateMeetingRoomHeaders, new RuntimeOptions([]));
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
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
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
func CreateClient () (_result *dingtalkrooms_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrooms_1_0.Client{}
  _result, _err = dingtalkrooms_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateMeetingRoomHeaders := &dingtalkrooms_1_0.UpdateMeetingRoomHeaders{}
  updateMeetingRoomHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  reservationAuthorityAuthorizedMembers0 := &dingtalkrooms_1_0.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers{
    MemberId: tea.String("lPHhSZDLXXXXXXpBlC9lxLwiEiE"),
    MemberType: tea.String("user"),
    MemberName: tea.String("张三"),
  }
  reservationAuthority := &dingtalkrooms_1_0.UpdateMeetingRoomRequestReservationAuthority{
    AuthorizedMembers: []*dingtalkrooms_1_0.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers{reservationAuthorityAuthorizedMembers0},
  }
  roomLocation := &dingtalkrooms_1_0.UpdateMeetingRoomRequestRoomLocation{
    Title: tea.String("xxx公司"),
    Desc: tea.String("xx市xx区xx路xx号"),
  }
  updateMeetingRoomRequest := &dingtalkrooms_1_0.UpdateMeetingRoomRequest{
    UnionId: tea.String("2iPOxxxxx"),
    RoomId: tea.String("0ffbxxxxx"),
    RoomName: tea.String("测试会议室"),
    RoomCapacity: tea.Int32(10),
    RoomPicture: tea.String("https://static.dingtalk.com/media/lADPxxxxx.jpg"),
    RoomStatus: tea.Int32(0),
    RoomLocation: roomLocation,
    RoomLabelIds: []*int64{tea.Int64(1)},
    IsvRoomId: tea.String("xxxIsvRoomId"),
    GroupId: tea.Int64(0),
    ReservationAuthority: reservationAuthority,
    EnableCycleReservation: tea.Bool(false),
    OpenReservation: tea.Bool(true),
    RoomDescription: tea.String("此处添加对会议室的描述信息"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateMeetingRoomWithOptions(updateMeetingRoomRequest, updateMeetingRoomHeaders, &util.RuntimeOptions{})
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
const dingtalkrooms_1_0 = require('@alicloud/dingtalk/rooms_1_0');
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
    return new dingtalkrooms_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateMeetingRoomHeaders = new dingtalkrooms_1_0.UpdateMeetingRoomHeaders({ });
    updateMeetingRoomHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let reservationAuthorityAuthorizedMembers0 = new dingtalkrooms_1_0.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers({
      memberId: 'lPHhSZDLXXXXXXpBlC9lxLwiEiE',
      memberType: 'user',
      memberName: '张三',
    });
    let reservationAuthority = new dingtalkrooms_1_0.UpdateMeetingRoomRequestReservationAuthority({
      authorizedMembers: [
        reservationAuthorityAuthorizedMembers0
      ],
    });
    let roomLocation = new dingtalkrooms_1_0.UpdateMeetingRoomRequestRoomLocation({
      title: 'xxx公司',
      desc: 'xx市xx区xx路xx号',
    });
    let updateMeetingRoomRequest = new dingtalkrooms_1_0.UpdateMeetingRoomRequest({
      unionId: '2iPOxxxxx',
      roomId: '0ffbxxxxx',
      roomName: '测试会议室',
      roomCapacity: 10,
      roomPicture: 'https://static.dingtalk.com/media/lADPxxxxx.jpg',
      roomStatus: 0,
      roomLocation: roomLocation,
      roomLabelIds: [
        1
      ],
      isvRoomId: 'xxxIsvRoomId',
      groupId: 0,
      reservationAuthority: reservationAuthority,
      enableCycleReservation: false,
      openReservation: true,
      roomDescription: '此处添加对会议室的描述信息',
    });
    try {
      await client.updateMeetingRoomWithOptions(updateMeetingRoomRequest, updateMeetingRoomHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrooms_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrooms_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomHeaders updateMeetingRoomHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomHeaders();
            updateMeetingRoomHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers reservationAuthorityAuthorizedMembers0 = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers
            {
                MemberId = "lPHhSZDLXXXXXXpBlC9lxLwiEiE",
                MemberType = "user",
                MemberName = "张三",
            };
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority reservationAuthority = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority
            {
                AuthorizedMembers = new List<AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestReservationAuthority.UpdateMeetingRoomRequestReservationAuthorityAuthorizedMembers>
                {
                    reservationAuthorityAuthorizedMembers0
                },
            };
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation roomLocation = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest.UpdateMeetingRoomRequestRoomLocation
            {
                Title = "xxx公司",
                Desc = "xx市xx区xx路xx号",
            };
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest updateMeetingRoomRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateMeetingRoomRequest
            {
                UnionId = "2iPOxxxxx",
                RoomId = "0ffbxxxxx",
                RoomName = "测试会议室",
                RoomCapacity = 10,
                RoomPicture = "https://static.dingtalk.com/media/lADPxxxxx.jpg",
                RoomStatus = 0,
                RoomLocation = roomLocation,
                RoomLabelIds = new List<long?>
                {
                    1
                },
                IsvRoomId = "xxxIsvRoomId",
                GroupId = 0,
                ReservationAuthority = reservationAuthority,
                EnableCycleReservation = false,
                OpenReservation = true,
                RoomDescription = "此处添加对会议室的描述信息",
            };
            try
            {
                client.UpdateMeetingRoomWithOptions(updateMeetingRoomRequest, updateMeetingRoomHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否成功更新会议室信息，true表示更新成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Error:%s | 请求参数错误。例如，Error:roomStatus invalid |
| 400 | room.name.unsafe | Room Name Unsafe | 会议室名称不允许 |
| 400 | room.not.found | Room Not Found | 会议室不存在 |
| 400 | room.exist | Room Exsit | 同名会议室已存在 |
| 400 | user.not.admin | User Not Admin | 用户不是管理员 |
| 400 | org.not.found | Org Not Found | 企业找不到 |
| 500 | system.error | System Error | 系统错误 |
