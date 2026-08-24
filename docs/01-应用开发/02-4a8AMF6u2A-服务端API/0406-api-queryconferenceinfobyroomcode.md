---
title: "根据会议号查询会议信息"
source_url: "https://open.dingtalk.com/document/development/api-queryconferenceinfobyroomcode"
namespace: "development"
slug: "api-queryconferenceinfobyroomcode"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 根据会议号查询会议信息"
doc_id: "CqizOT6d6d"
updated_at: "2026-06-02 12:05:02"
---

> Source: https://open.dingtalk.com/document/development/api-queryconferenceinfobyroomcode
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 根据会议号查询会议信息
> Updated: 2026-06-02 12:05:02

# 根据会议号查询会议信息

调用本接口，根据会议 roomCode 和分页参数会议信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/roomCodes/{roomCode}/infos |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| roomCode | String | 是 | 会议码。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标。 |
| maxResults | Integer | 否 | 分页大小。 |

### 请求示例

HTTP

```
GET /v1.0/conference/roomCodes/4272xxxxx/infos?nextToken=0&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1803b054eb783eb6a4030369xxx10476
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
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconference_1_0.models.QueryConferenceInfoByRoomCodeHeaders queryConferenceInfoByRoomCodeHeaders = new com.aliyun.dingtalkconference_1_0.models.QueryConferenceInfoByRoomCodeHeaders();
        queryConferenceInfoByRoomCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.QueryConferenceInfoByRoomCodeRequest queryConferenceInfoByRoomCodeRequest = new com.aliyun.dingtalkconference_1_0.models.QueryConferenceInfoByRoomCodeRequest()
                .setNextToken("0")
                .setMaxResults(10);
        try {
            client.queryConferenceInfoByRoomCodeWithOptions("4272xxxxx", queryConferenceInfoByRoomCodeRequest, queryConferenceInfoByRoomCodeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.conference_1_0.client import Client as dingtalkconference_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.conference_1_0 import models as dingtalkconference__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconference_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconference_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_conference_info_by_room_code_headers = dingtalkconference__1__0_models.QueryConferenceInfoByRoomCodeHeaders()
        query_conference_info_by_room_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_conference_info_by_room_code_request = dingtalkconference__1__0_models.QueryConferenceInfoByRoomCodeRequest(
            next_token='0',
            max_results=10
        )
        try:
            client.query_conference_info_by_room_code_with_options('4272xxxxx', query_conference_info_by_room_code_request, query_conference_info_by_room_code_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_conference_info_by_room_code_headers = dingtalkconference__1__0_models.QueryConferenceInfoByRoomCodeHeaders()
        query_conference_info_by_room_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_conference_info_by_room_code_request = dingtalkconference__1__0_models.QueryConferenceInfoByRoomCodeRequest(
            next_token='0',
            max_results=10
        )
        try:
            await client.query_conference_info_by_room_code_with_options_async('4272xxxxx', query_conference_info_by_room_code_request, query_conference_info_by_room_code_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceInfoByRoomCodeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceInfoByRoomCodeRequest;
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
        $queryConferenceInfoByRoomCodeHeaders = new QueryConferenceInfoByRoomCodeHeaders([]);
        $queryConferenceInfoByRoomCodeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryConferenceInfoByRoomCodeRequest = new QueryConferenceInfoByRoomCodeRequest([
            "nextToken" => "0",
            "maxResults" => 10
        ]);
        try {
            $client->queryConferenceInfoByRoomCodeWithOptions("4272xxxxx", $queryConferenceInfoByRoomCodeRequest, $queryConferenceInfoByRoomCodeHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
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
func CreateClient () (_result *dingtalkconference_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconference_1_0.Client{}
  _result, _err = dingtalkconference_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryConferenceInfoByRoomCodeHeaders := &dingtalkconference_1_0.QueryConferenceInfoByRoomCodeHeaders{}
  queryConferenceInfoByRoomCodeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryConferenceInfoByRoomCodeRequest := &dingtalkconference_1_0.QueryConferenceInfoByRoomCodeRequest{
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryConferenceInfoByRoomCodeWithOptions(tea.String("4272xxxxx"), queryConferenceInfoByRoomCodeRequest, queryConferenceInfoByRoomCodeHeaders, &util.RuntimeOptions{})
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
const dingtalkconference_1_0 = require('@alicloud/dingtalk/conference_1_0');
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
    return new dingtalkconference_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryConferenceInfoByRoomCodeHeaders = new dingtalkconference_1_0.QueryConferenceInfoByRoomCodeHeaders({ });
    queryConferenceInfoByRoomCodeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryConferenceInfoByRoomCodeRequest = new dingtalkconference_1_0.QueryConferenceInfoByRoomCodeRequest({
      nextToken: '0',
      maxResults: 10,
    });
    try {
      await client.queryConferenceInfoByRoomCodeWithOptions('4272xxxxx', queryConferenceInfoByRoomCodeRequest, queryConferenceInfoByRoomCodeHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkconference_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconference_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconference_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoByRoomCodeHeaders queryConferenceInfoByRoomCodeHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoByRoomCodeHeaders();
            queryConferenceInfoByRoomCodeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoByRoomCodeRequest queryConferenceInfoByRoomCodeRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoByRoomCodeRequest
            {
                NextToken = "0",
                MaxResults = 10,
            };
            try
            {
                client.QueryConferenceInfoByRoomCodeWithOptions("4272xxxxx", queryConferenceInfoByRoomCodeRequest, queryConferenceInfoByRoomCodeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | String | 分页游标。 |
| hasMore | Boolean | 是否更多。 |
| totalCount | Integer | 结果总数。 |
| conferenceList | Array | 会议信息列表，如果会议码对应的会议为预约会议、周期会议，则会议码可能对应多个会议实例信息。 |
| conferenceId | String | 会议ID。 |
| title | String | 会议标题。 |
| roomCode | String | 会议码。 |
| externalLinkUrl | String | 会议的入会链接。 |
| status | Integer | 会议状态：   - 0：初始化 - 1：会议结束 - 2：会议开始 |
| startTime | Long | 会议开始时间戳，单位毫秒。 |
| endTime | Long | 会议结束时间戳，单位毫秒，会议结束后，返回该字段。 |
| confDuration | Long | 会议时长，单位毫秒，会议结束后，返回该字段。 |
| creatorId | String | 会议创建人的unionId。 |
| creatorNick | String | 会议创建人的昵称。 |
| scheduleConferenceId | String | 预约会议id。 |
| bizType | String | 会议业务类型：   - 0：即时视频会议 - 3：预约会议 - audio\_conf：语音会议 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "10",
  "hasMore" : true,
  "totalCount" : 15,
  "conferenceList" : [ {
    "conferenceId" : "6323dxxxxx",
    "title" : "标题",
    "roomCode" : "4272xxxxx",
    "externalLinkUrl" : "https://meeting.dingtalk.com/app?roomCode=42726xxx&token=1_7ac9xxx",
    "status" : 1,
    "startTime" : 1664175001000,
    "endTime" : 1663294270000,
    "confDuration" : 1000000,
    "creatorId" : "2iPOLxxxxx",
    "creatorNick" : "小钉",
    "scheduleConferenceId" : "4331d******",
    "bizType" : "0"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRoomCode | invalidRoomCode | 会议码无效 |
| 400 | missingRoomCode | missingRoomCode | 会议码缺失 |
| 400 | paramError | paramError | 参数错误 |
| 403 | noPermission | noPermission | 无权限 |
| 500 | systemError | systemError | 系统错误 |
