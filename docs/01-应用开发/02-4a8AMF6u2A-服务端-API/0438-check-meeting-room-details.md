---
title: "查询会议室详情"
source_url: "https://open.dingtalk.com/document/development/check-meeting-room-details"
namespace: "development"
slug: "check-meeting-room-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 查询会议室详情"
doc_id: "zc7fIwbqpM"
updated_at: "2026-06-03 10:12:08"
---

> Source: https://open.dingtalk.com/document/development/check-meeting-room-details
> Path: 应用开发 / 服务端 API / 音视频 > 智能会议室 > 会议室 > 查询会议室详情
> Updated: 2026-06-03 10:12:08

# 查询会议室详情

调用本接口，查询会议室详情，包括会议室名称、可容纳人数、位置信息等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/meetingRooms/{roomId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：  企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。  第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| roomId | String | 是 | 会议室ID，可调用[查询会议室列表](0437-check-the-meeting-room-list.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取获取。 |

### 请求示例

HTTP

```
GET /v1.0/rooms/meetingRooms/0ffb7xxxxx?unionId=2iPOLxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomHeaders queryMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomHeaders();
        queryMeetingRoomHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomRequest queryMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomRequest()
                .setUnionId("2iPOLxxxxx");
        try {
            client.queryMeetingRoomWithOptions("0ffb7xxxxx", queryMeetingRoomRequest, queryMeetingRoomHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_meeting_room_headers = dingtalkrooms__1__0_models.QueryMeetingRoomHeaders()
        query_meeting_room_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_request = dingtalkrooms__1__0_models.QueryMeetingRoomRequest(
            union_id='2iPOLxxxxx'
        )
        try:
            client.query_meeting_room_with_options('0ffb7xxxxx', query_meeting_room_request, query_meeting_room_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_meeting_room_headers = dingtalkrooms__1__0_models.QueryMeetingRoomHeaders()
        query_meeting_room_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_request = dingtalkrooms__1__0_models.QueryMeetingRoomRequest(
            union_id='2iPOLxxxxx'
        )
        try:
            await client.query_meeting_room_with_options_async('0ffb7xxxxx', query_meeting_room_request, query_meeting_room_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomRequest;
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
        $queryMeetingRoomHeaders = new QueryMeetingRoomHeaders([]);
        $queryMeetingRoomHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryMeetingRoomRequest = new QueryMeetingRoomRequest([
            "unionId" => "2iPOLxxxxx"
        ]);
        try {
            $client->queryMeetingRoomWithOptions("0ffb7xxxxx", $queryMeetingRoomRequest, $queryMeetingRoomHeaders, new RuntimeOptions([]));
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

  queryMeetingRoomHeaders := &dingtalkrooms_1_0.QueryMeetingRoomHeaders{}
  queryMeetingRoomHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryMeetingRoomRequest := &dingtalkrooms_1_0.QueryMeetingRoomRequest{
    UnionId: tea.String("2iPOLxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryMeetingRoomWithOptions(tea.String("0ffb7xxxxx"), queryMeetingRoomRequest, queryMeetingRoomHeaders, &util.RuntimeOptions{})
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
    let queryMeetingRoomHeaders = new dingtalkrooms_1_0.QueryMeetingRoomHeaders({ });
    queryMeetingRoomHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryMeetingRoomRequest = new dingtalkrooms_1_0.QueryMeetingRoomRequest({
      unionId: '2iPOLxxxxx',
    });
    try {
      await client.queryMeetingRoomWithOptions('0ffb7xxxxx', queryMeetingRoomRequest, queryMeetingRoomHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomHeaders queryMeetingRoomHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomHeaders();
            queryMeetingRoomHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomRequest queryMeetingRoomRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomRequest
            {
                UnionId = "2iPOLxxxxx",
            };
            try
            {
                client.QueryMeetingRoomWithOptions("0ffb7xxxxx", queryMeetingRoomRequest, queryMeetingRoomHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 会议室详情。 |
| roomId | String | 会议室ID。 |
| roomStaffId | String | 会议室的企业员工Id。      预留字段，暂无使用场景。 |
| corpId | String | 会议室所在的企业CorpId。 |
| roomName | String | 会议室名称。 |
| roomStatus | Integer | 会议室状态：   - **0**：全员可用 - **1**：仅管理员可用 - **2**：部分有权限 |
| roomLabels | Array | 会议室标签列表。 |
| labelId | Long | 标签ID：   - **1**：电视 - **2**：电话 - **3**：投影仪 - **4**：白板 - **5**：视频会议 |
| labelName | String | 标签名称。 |
| roomCapacity | Integer | 会议室可容纳人数。 |
| roomLocation | Object | 会议室位置信息。 |
| title | String | 会议室位置名称。 |
| desc | String | 会议室位置详细信息。 |
| roomPicture | String | 会议室图片。 |
| isvRoomId | String | 调用方外部会议室ID。 |
| roomGroup | Object | 会议室分组信息。 |
| groupId | Long | 分组ID。 |
| groupName | String | 分组名称。 |
| parentId | Long | 父分组ID。 |
| deviceUnionIds | Array of String | UnionId列表。 |
| reservationAuthority | Object | roomStatus部分权限时，设置的会议室预定权限。 |
| authorizedMembers | Array | 有权限的成员列表。 |
| memberId | String | 成员的id，memberType设置  人员：成员unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取获取。  部门：部门id，dept\_id，可调用[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取。 |
| memberType | String | 成员的类型，类型：   - **人员**：user - **部门**：dept |
| memberName | String | 成员的名称：   - **人员**：人员昵称 - **部门**：部门名称 |
| enableCycleReservation | Boolean | 会议室是否支持循环周期预定：   - **true**：是 - **false**：否 |
| roomUnionId | String | 会议室unionId。 |
| extensionConfig | Object | 会议室更多配置。 |
| openReservation | Boolean | 会议室是否开放预定:   - **true**：是 - **false**：否 |
| maxReservationTimeInterval | Integer | 单次可预定最长时段，单位分钟      值为0表示无限制。 |
| minReservationTimeInterval | Integer | 单次可预定最小时段，单位分钟。 |
| advanceReservation | Object | 最早可提前预定时间。 |
| advanceReservationTime | Integer | 提前可预订时间具体值，单位参考advanceReservationTimeUnit字段。 |
| advanceReservationTimeUnit | String | 时间单位：   - **days**：表示天 - **weeks**：表示周 - **months**：表示月 - **years**：表示年 |
| advanceBookTimeFormat | String | 精确到几点钟。 |
| reservationCloseDetail | Object | 关闭预定具体信息。 |
| taskStartTime | Long | 会议室关闭预定的开始时间，时间戳，单位毫秒。 |
| taskEndTime | Long | 会议室关闭预定的结束时间。时间戳，单位毫秒。      值为空表示永久关闭。 |
| closeReason | String | 关闭预定的原因。 |
| contactUnionId | String | 联系人的unionId。 |
| contactNick | String | 联系人昵称。 |
| sendNotify | Boolean | 是否发送通知给已预订会议室的员工。 |
| approvalSwitch | Boolean | 是否开启审批开关   - **true**：已开启 - **false**：未开启 |
| approvalType | Integer | 审批类型：   - **1**：标准审批 - **2**：自定义审批 |
| roomDescription | String | 会议室描述信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "roomId" : "0ffb7184xxxxx",
    "roomStaffId" : "0122414",
    "corpId" : "ding994axxxxx",
    "roomName" : "测试会议室",
    "roomStatus" : 0,
    "roomLabels" : [ {
      "labelId" : 1,
      "labelName" : "电视"
    } ],
    "roomCapacity" : 10,
    "roomLocation" : {
      "title" : "xxx公司",
      "desc" : "xx市xx区xx街道xx号"
    },
    "roomPicture" : "https://static.dingtalk.com/media/lADxxxxx.jpg",
    "isvRoomId" : "xxxIsvRoomId",
    "roomGroup" : {
      "groupId" : 1,
      "groupName" : "测试分组",
      "parentId" : 0
    },
    "deviceUnionIds" : [ "2iPOLbpxxxxuwggiiqiPwiEiF" ],
    "reservationAuthority" : {
      "authorizedMembers" : [ {
        "memberId" : "lPHhSZDLXXXXXXpBlC9lxLwiEiE",
        "memberType" : "user",
        "memberName" : "张三"
      } ]
    },
    "enableCycleReservation" : false,
    "roomUnionId" : "DtB8VDzXXXXXX41rgiE",
    "extensionConfig" : {
      "openReservation" : true,
      "maxReservationTimeInterval" : 60,
      "minReservationTimeInterval" : 15,
      "advanceReservation" : {
        "advanceReservationTime" : 3,
        "advanceReservationTimeUnit" : "days",
        "advanceBookTimeFormat" : "09:00"
      },
      "reservationCloseDetail" : {
        "taskStartTime" : 1740463800000,
        "taskEndTime" : 1740045030000,
        "closeReason" : "因为装修临时关闭预定",
        "contactUnionId" : "2iPOLbpxxxxuwggiiqiPwiEiF",
        "contactNick" : "nick",
        "sendNotify" : true
      },
      "approvalSwitch" : false,
      "approvalType" : 1
    },
    "roomDescription" : "此处添加对会议室的描述信息"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数缺失错误 |
| 400 | org.not.found | Org Not Found | 企业找不到 |
| 500 | system.error | System Error | 系统错误 |
