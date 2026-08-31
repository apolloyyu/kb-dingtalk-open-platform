---
title: "获取分组管理员信息"
source_url: "https://open.dingtalk.com/document/development/api-querymeetingroomgroupadmin"
namespace: "development"
slug: "api-querymeetingroomgroupadmin"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 智能会议室 > 会议室分组 > 获取分组管理员信息"
doc_id: "KJJcGIuW0z"
updated_at: "2026-07-03 09:40:10"
---

> Source: https://open.dingtalk.com/document/development/api-querymeetingroomgroupadmin
> Path: 应用开发 / 服务端 API / 音视频 > 智能会议室 > 会议室分组 > 获取分组管理员信息
> Updated: 2026-07-03 09:40:10

# 获取分组管理员信息

调用本接口，查询会议室分组管理员信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/groupAdmin/{groupId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| groupId | Long | 否 | 分组ID，可调用[查询会议室分组列表](0448-query-meeting-rooms-groups.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 否 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/rooms/groupAdmin/172?unionId=2iPOLbxxxxqiPwiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupAdminHeaders queryMeetingRoomGroupAdminHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupAdminHeaders();
        queryMeetingRoomGroupAdminHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupAdminRequest queryMeetingRoomGroupAdminRequest = new com.aliyun.dingtalkrooms_1_0.models.QueryMeetingRoomGroupAdminRequest()
                .setUnionId("2iPOLbxxxxqiPwiEiE");
        try {
            client.queryMeetingRoomGroupAdminWithOptions("172", queryMeetingRoomGroupAdminRequest, queryMeetingRoomGroupAdminHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_meeting_room_group_admin_headers = dingtalkrooms__1__0_models.QueryMeetingRoomGroupAdminHeaders()
        query_meeting_room_group_admin_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_group_admin_request = dingtalkrooms__1__0_models.QueryMeetingRoomGroupAdminRequest(
            union_id='2iPOLbxxxxqiPwiEiE'
        )
        try:
            client.query_meeting_room_group_admin_with_options('172', query_meeting_room_group_admin_request, query_meeting_room_group_admin_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_meeting_room_group_admin_headers = dingtalkrooms__1__0_models.QueryMeetingRoomGroupAdminHeaders()
        query_meeting_room_group_admin_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_meeting_room_group_admin_request = dingtalkrooms__1__0_models.QueryMeetingRoomGroupAdminRequest(
            union_id='2iPOLbxxxxqiPwiEiE'
        )
        try:
            await client.query_meeting_room_group_admin_with_options_async('172', query_meeting_room_group_admin_request, query_meeting_room_group_admin_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomGroupAdminHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryMeetingRoomGroupAdminRequest;
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
        $queryMeetingRoomGroupAdminHeaders = new QueryMeetingRoomGroupAdminHeaders([]);
        $queryMeetingRoomGroupAdminHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryMeetingRoomGroupAdminRequest = new QueryMeetingRoomGroupAdminRequest([
            "unionId" => "2iPOLbxxxxqiPwiEiE"
        ]);
        try {
            $client->queryMeetingRoomGroupAdminWithOptions("172", $queryMeetingRoomGroupAdminRequest, $queryMeetingRoomGroupAdminHeaders, new RuntimeOptions([]));
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

  queryMeetingRoomGroupAdminHeaders := &dingtalkrooms_1_0.QueryMeetingRoomGroupAdminHeaders{}
  queryMeetingRoomGroupAdminHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryMeetingRoomGroupAdminRequest := &dingtalkrooms_1_0.QueryMeetingRoomGroupAdminRequest{
    UnionId: tea.String("2iPOLbxxxxqiPwiEiE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryMeetingRoomGroupAdminWithOptions(tea.String("172"), queryMeetingRoomGroupAdminRequest, queryMeetingRoomGroupAdminHeaders, &util.RuntimeOptions{})
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
    let queryMeetingRoomGroupAdminHeaders = new dingtalkrooms_1_0.QueryMeetingRoomGroupAdminHeaders({ });
    queryMeetingRoomGroupAdminHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryMeetingRoomGroupAdminRequest = new dingtalkrooms_1_0.QueryMeetingRoomGroupAdminRequest({
      unionId: '2iPOLbxxxxqiPwiEiE',
    });
    try {
      await client.queryMeetingRoomGroupAdminWithOptions('172', queryMeetingRoomGroupAdminRequest, queryMeetingRoomGroupAdminHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomGroupAdminHeaders queryMeetingRoomGroupAdminHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomGroupAdminHeaders();
            queryMeetingRoomGroupAdminHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomGroupAdminRequest queryMeetingRoomGroupAdminRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryMeetingRoomGroupAdminRequest
            {
                UnionId = "2iPOLbxxxxqiPwiEiE",
            };
            try
            {
                client.QueryMeetingRoomGroupAdminWithOptions("172", queryMeetingRoomGroupAdminRequest, queryMeetingRoomGroupAdminHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 应答信息。 |
| groupId | Long | 分组id。 |
| groupName | String | 分组名称。 |
| groupAdmins | Array | 分组管理员列表。 |
| memberId | String | 人员的unionId。 |
| memberName | String | 成员名称。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "groupId" : 172,
    "groupName" : "测试分组",
    "groupAdmins" : [ {
      "memberId" : "lPHhSZDLXXXXXXpBlC9lxLwiEiE",
      "memberName" : "张三"
    } ]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数缺失错误 |
| 400 | user.not.employee | User Not Employee | 用户不是员工 |
| 500 | system.error | System Error | 系统错误 |
| 500 | group.query.error | Group Query Error | 分组查询错误 |
