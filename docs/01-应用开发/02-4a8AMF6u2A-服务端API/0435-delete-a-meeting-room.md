---
title: "删除会议室"
source_url: "https://open.dingtalk.com/document/development/delete-a-meeting-room"
namespace: "development"
slug: "delete-a-meeting-room"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 会议室 > 删除会议室"
doc_id: "g9PdFfcRgM"
updated_at: "2026-06-03 10:12:06"
---

> Source: https://open.dingtalk.com/document/development/delete-a-meeting-room
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 会议室 > 删除会议室
> Updated: 2026-06-03 10:12:06

# 删除会议室

调用本接口，删除会议室。

## 接口调用说明

删除会议室，只允许有智能会议室应用管理权限的管理员操作。 ![](https://img.alicdn.com/imgextra/i3/O1CN01v90IEz204A3gSD44X_!!6000000006795-2-tps-2498-1632.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/meetingRooms/{roomId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

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
DELETE /v1.0/rooms/meetingRooms/0ffb7xxxxx?unionId=2iPOLxxxxx HTTP/1.1
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
        com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomHeaders deleteMeetingRoomHeaders = new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomHeaders();
        deleteMeetingRoomHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomRequest deleteMeetingRoomRequest = new com.aliyun.dingtalkrooms_1_0.models.DeleteMeetingRoomRequest()
                .setUnionId("2iPOLxxxxx");
        try {
            client.deleteMeetingRoomWithOptions("0ffb7xxxxx", deleteMeetingRoomRequest, deleteMeetingRoomHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        delete_meeting_room_headers = dingtalkrooms__1__0_models.DeleteMeetingRoomHeaders()
        delete_meeting_room_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_meeting_room_request = dingtalkrooms__1__0_models.DeleteMeetingRoomRequest(
            union_id='2iPOLxxxxx'
        )
        try:
            client.delete_meeting_room_with_options('0ffb7xxxxx', delete_meeting_room_request, delete_meeting_room_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_meeting_room_headers = dingtalkrooms__1__0_models.DeleteMeetingRoomHeaders()
        delete_meeting_room_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_meeting_room_request = dingtalkrooms__1__0_models.DeleteMeetingRoomRequest(
            union_id='2iPOLxxxxx'
        )
        try:
            await client.delete_meeting_room_with_options_async('0ffb7xxxxx', delete_meeting_room_request, delete_meeting_room_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\DeleteMeetingRoomHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\DeleteMeetingRoomRequest;
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
        $deleteMeetingRoomHeaders = new DeleteMeetingRoomHeaders([]);
        $deleteMeetingRoomHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteMeetingRoomRequest = new DeleteMeetingRoomRequest([
            "unionId" => "2iPOLxxxxx"
        ]);
        try {
            $client->deleteMeetingRoomWithOptions("0ffb7xxxxx", $deleteMeetingRoomRequest, $deleteMeetingRoomHeaders, new RuntimeOptions([]));
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

  deleteMeetingRoomHeaders := &dingtalkrooms_1_0.DeleteMeetingRoomHeaders{}
  deleteMeetingRoomHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteMeetingRoomRequest := &dingtalkrooms_1_0.DeleteMeetingRoomRequest{
    UnionId: tea.String("2iPOLxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteMeetingRoomWithOptions(tea.String("0ffb7xxxxx"), deleteMeetingRoomRequest, deleteMeetingRoomHeaders, &util.RuntimeOptions{})
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
    let deleteMeetingRoomHeaders = new $dingtalkrooms_1_0.DeleteMeetingRoomHeaders({ });
    deleteMeetingRoomHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deleteMeetingRoomRequest = new $dingtalkrooms_1_0.DeleteMeetingRoomRequest({
      unionId: "2iPOLxxxxx",
    });
    try {
      await client.deleteMeetingRoomWithOptions("0ffb7xxxxx", deleteMeetingRoomRequest, deleteMeetingRoomHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteMeetingRoomHeaders deleteMeetingRoomHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteMeetingRoomHeaders();
            deleteMeetingRoomHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteMeetingRoomRequest deleteMeetingRoomRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteMeetingRoomRequest
            {
                UnionId = "2iPOLxxxxx",
            };
            try
            {
                client.DeleteMeetingRoomWithOptions("0ffb7xxxxx", deleteMeetingRoomRequest, deleteMeetingRoomHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否成功删除会议室，true表示删除成功。 |

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
| 400 | param.error | Param Error | 参数缺失错误 |
| 400 | user.not.admin | User Not Admin | 用户不是管理员 |
| 400 | room.not.found | Room Not Found | 会议室不存在 |
| 400 | org.not.found | Org Not Found | 企业找不到 |
| 500 | system.error | System Error | 系统错误 |
