---
title: "查询会议室列表"
source_url: "https://open.dingtalk.com/document/development/check-the-meeting-room-list"
namespace: "development"
slug: "check-the-meeting-room-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 查询会议室列表"
doc_id: "nghi2XFjyj"
updated_at: "2026-06-03 10:12:08"
---

> Source: https://open.dingtalk.com/document/development/check-the-meeting-room-list
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 会议室 > 查询会议室列表
> Updated: 2026-06-03 10:12:08

# 查询会议室列表

调用本接口，查询会议室列表，包括会议室的名称、可容纳人数、位置信息等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/meetingRoomLists |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | Long | 否 | 分页游标。   - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上传调用时返回的nextToken。 |
| maxResults | Integer | 否 | 请求分页大小，默认值20，最大值100。 |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取获取。 |

### 请求示例

HTTP

```
GET /v1.0/rooms/meetingRoomLists?nextToken=124&maxResults=20&unionId=2iPOxxxxx HTTP/1.1
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
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListHeaders queryMeetingRoomListHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListHeaders();
        queryMeetingRoomListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListRequest queryMeetingRoomListRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomListRequest()
                .setNextToken(124L)
                .setMaxResults(20)
                .setUnionId("2iPOxxxxx");
        try {
            client.queryMeetingRoomListWithOptions(queryMeetingRoomListRequest, queryMeetingRoomListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_meeting_room_list_headers = dingtalkrooms__1__0_models.QueryMeetingRoomListHeaders()
        query_meeting_room_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_list_request = dingtalkrooms__1__0_models.QueryMeetingRoomListRequest(
            next_token=124,
            max_results=20,
            union_id='2iPOxxxxx'
        )
        try:
            client.query_meeting_room_list_with_options(query_meeting_room_list_request, query_meeting_room_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_meeting_room_list_headers = dingtalkrooms__1__0_models.QueryMeetingRoomListHeaders()
        query_meeting_room_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_list_request = dingtalkrooms__1__0_models.QueryMeetingRoomListRequest(
            next_token=124,
            max_results=20,
            union_id='2iPOxxxxx'
        )
        try:
            await client.query_meeting_room_list_with_options_async(query_meeting_room_list_request, query_meeting_room_list_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomListRequest;
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
        $queryMeetingRoomListHeaders = new QueryMeetingRoomListHeaders([]);
        $queryMeetingRoomListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryMeetingRoomListRequest = new QueryMeetingRoomListRequest([
            "nextToken" => 124,
            "maxResults" => 20,
            "unionId" => "2iPOxxxxx"
        ]);
        try {
            $client->queryMeetingRoomListWithOptions($queryMeetingRoomListRequest, $queryMeetingRoomListHeaders, new RuntimeOptions([]));
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
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  queryMeetingRoomListHeaders := &dingtalkrooms_1_0.QueryMeetingRoomListHeaders{}
  queryMeetingRoomListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryMeetingRoomListRequest := &dingtalkrooms_1_0.QueryMeetingRoomListRequest{
    NextToken: tea.Int64(124),
    MaxResults: tea.Int32(20),
    UnionId: tea.String("2iPOxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryMeetingRoomListWithOptions(queryMeetingRoomListRequest, queryMeetingRoomListHeaders, &util.RuntimeOptions{})
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
import dingtalkrooms_1_0, * as $dingtalkrooms_1_0 from '@alicloud/dingtalk/rooms_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrooms_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrooms_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryMeetingRoomListHeaders = new $dingtalkrooms_1_0.QueryMeetingRoomListHeaders({ });
    queryMeetingRoomListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryMeetingRoomListRequest = new $dingtalkrooms_1_0.QueryMeetingRoomListRequest({
      nextToken: 124,
      maxResults: 20,
      unionId: "2iPOxxxxx",
    });
    try {
      await client.queryMeetingRoomListWithOptions(queryMeetingRoomListRequest, queryMeetingRoomListHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomListHeaders queryMeetingRoomListHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomListHeaders();
            queryMeetingRoomListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomListRequest queryMeetingRoomListRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomListRequest
            {
                NextToken = 124,
                MaxResults = 20,
                UnionId = "2iPOxxxxx",
            };
            try
            {
                client.QueryMeetingRoomListWithOptions(queryMeetingRoomListRequest, queryMeetingRoomListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| hasMore | Boolean | 是否有更多。   - **true**：是 - **false**：否 |
| nextToken | Long | 分页游标。 |
| result | Array | 会议室列表。 |
| roomId | String | 会议室ID。 |
| roomStaffId | String | 会议室的企业员工Id。      预留字段，暂无使用场景。 |
| corpId | String | 会议室所在的企业CorpId。 |
| roomName | String | 会议室名称。 |
| roomStatus | Integer | 会议室状态。   - **0**：全员可见 - **1**：仅管理员可见 - **2**：部分成员可见 |
| roomLabels | Array | 会议室标签列表。 |
| labelId | Long | 标签ID。   - **1**：电视 - **2**：电话 - **3**：投影仪 - **4**：白板 - **5**：视频会议 |
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

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "hasMore" : true,
  "nextToken" : 123,
  "result" : [ {
    "roomId" : "0ffb7xxxxx",
    "roomStaffId" : "012241xxxxx",
    "corpId" : "ding994axxxx",
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
    "roomPicture" : "https://static.dingtalk.com/media/lADPxxxxx.jpg",
    "isvRoomId" : "xxxIsvRoomId",
    "roomGroup" : {
      "groupId" : 1,
      "groupName" : "测试分组",
      "parentId" : 0
    }
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数缺失错误 |
| 400 | user.not.employee | User Not Employee | 用户不在企业 |
| 400 | org.not.found | Org Not Found | 企业找不到 |
| 500 | system.error | System Error | 系统错误 |
