---
title: "查询视频会议成员"
source_url: "https://open.dingtalk.com/document/development/querying-video-conference-members"
namespace: "development"
slug: "querying-video-conference-members"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 查询视频会议成员"
doc_id: "Gu3lyRg4cG"
updated_at: "2026-06-02 09:18:03"
---

> Source: https://open.dingtalk.com/document/development/querying-video-conference-members
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 查询视频会议成员
> Updated: 2026-06-02 09:18:03

# 查询视频会议成员

调用本接口，分页查询视频会议成员信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/members |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conferenceId | String | 是 | 会议conferenceId，可通过[创建视频会议](0399-create-a-video-conference.md)接口获取conferenceId。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用本接口，该参数不需要传或者传0。 - 如果是非首次调用本接口，该参数值传上次调用本接口返回的nextToken。 |
| maxResults | Integer | 否 | 每页最大条目数，默认值128，无最大值限制。 |

### 请求示例

HTTP

```
GET /v1.0/conference/videoConferences/6323dxxxxx/members?nextToken=0&maxResults=20 HTTP/1.1
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
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconference_1_0.models.QueryConferenceMembersHeaders queryConferenceMembersHeaders = new com.aliyun.dingtalkconference_1_0.models.QueryConferenceMembersHeaders();
        queryConferenceMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.QueryConferenceMembersRequest queryConferenceMembersRequest = new com.aliyun.dingtalkconference_1_0.models.QueryConferenceMembersRequest()
                .setNextToken("0")
                .setMaxResults(20);
        try {
            client.queryConferenceMembersWithOptions("6323dxxxxx", queryConferenceMembersRequest, queryConferenceMembersHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_conference_members_headers = dingtalkconference__1__0_models.QueryConferenceMembersHeaders()
        query_conference_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_conference_members_request = dingtalkconference__1__0_models.QueryConferenceMembersRequest(
            next_token='0',
            max_results=20
        )
        try:
            client.query_conference_members_with_options('6323dxxxxx', query_conference_members_request, query_conference_members_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_conference_members_headers = dingtalkconference__1__0_models.QueryConferenceMembersHeaders()
        query_conference_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_conference_members_request = dingtalkconference__1__0_models.QueryConferenceMembersRequest(
            next_token='0',
            max_results=20
        )
        try:
            await client.query_conference_members_with_options_async('6323dxxxxx', query_conference_members_request, query_conference_members_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceMembersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceMembersRequest;
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
        $queryConferenceMembersHeaders = new QueryConferenceMembersHeaders([]);
        $queryConferenceMembersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryConferenceMembersRequest = new QueryConferenceMembersRequest([
            "nextToken" => "0",
            "maxResults" => 20
        ]);
        try {
            $client->queryConferenceMembersWithOptions("6323dxxxxx", $queryConferenceMembersRequest, $queryConferenceMembersHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  queryConferenceMembersHeaders := &dingtalkconference_1_0.QueryConferenceMembersHeaders{}
  queryConferenceMembersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryConferenceMembersRequest := &dingtalkconference_1_0.QueryConferenceMembersRequest{
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(20),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryConferenceMembersWithOptions(tea.String("6323dxxxxx"), queryConferenceMembersRequest, queryConferenceMembersHeaders, &util.RuntimeOptions{})
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
import dingtalkconference_1_0, * as $dingtalkconference_1_0 from '@alicloud/dingtalk/conference_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkconference_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkconference_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryConferenceMembersHeaders = new $dingtalkconference_1_0.QueryConferenceMembersHeaders({ });
    queryConferenceMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryConferenceMembersRequest = new $dingtalkconference_1_0.QueryConferenceMembersRequest({
      nextToken: "0",
      maxResults: 20,
    });
    try {
      await client.queryConferenceMembersWithOptions("6323dxxxxx", queryConferenceMembersRequest, queryConferenceMembersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceMembersHeaders queryConferenceMembersHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceMembersHeaders();
            queryConferenceMembersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceMembersRequest queryConferenceMembersRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceMembersRequest
            {
                NextToken = "0",
                MaxResults = 20,
            };
            try
            {
                client.QueryConferenceMembersWithOptions("6323dxxxxx", queryConferenceMembersRequest, queryConferenceMembersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| memberModels | Array | 成员列表。 |
| unionId | String | 成员的unionId。 |
| conferenceId | String | 视频会议ID。 |
| userNick | String | 成员的昵称。 |
| joinTime | Long | 成员入会时间戳，单位毫秒。 |
| leaveTime | Long | 成员离会时间戳，单位毫秒。 |
| duration | Long | 在会时长，单位毫秒。 |
| host | Boolean | 是否是主持人。   - true：是 - false：否 |
| attendStatus | Integer | 成员状态 。   - 1：初始化 - 2：呼叫中 - 3：活跃（在会） - 4：入会失败（拒接等） - 5：被踢 - 6：离会 |
| outerOrgMember | Boolean | 是否非会议所属企业内成员。   - true：是 - false：否       如果当前参会人是所属企业内成员，该字段不返回。 |
| pstnJoin | Boolean | 是否为电话号码入会。   - true：是 - false：否 |
| coHost | Boolean | 是否为联席主持人。   - true：是 - false：否 |
| nextToken | String | 分页游标。 |
| totalCount | Integer | 总数量。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "memberModels" : [ {
    "unionId" : "2iPOLxxxxx",
    "conferenceId" : "6323dxxxxx",
    "userNick" : "小钉",
    "joinTime" : 1663293270000,
    "leaveTime" : 1663293280000,
    "duration" : 10000,
    "host" : false,
    "attendStatus" : 6,
    "outerOrgMember" : true,
    "pstnJoin" : false,
    "coHost" : false
  } ],
  "nextToken" : "123000000",
  "totalCount" : 20
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | missingRoomId | MISSING ROOM ID | 会议id参数缺失 |
| 400 | paramError | PARAM ERROR | 参数错误 |
| 403 | noPermission | NO PERMISSION | 无权查询会议 |
| 404 | roomNotFound | ROOM NOT FOUND | 查不到该会议 |
| 500 | systemError | SYSTEM ERROR | 系统内部错误 |
