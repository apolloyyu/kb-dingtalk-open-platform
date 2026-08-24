---
title: "查询用户进行中会议列表"
source_url: "https://open.dingtalk.com/document/development/api-queryuserongoingconference"
namespace: "development"
slug: "api-queryuserongoingconference"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 查询用户进行中会议列表"
doc_id: "VZDoUqoA3d"
updated_at: "2026-06-02 12:02:37"
---

> Source: https://open.dingtalk.com/document/development/api-queryuserongoingconference
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 查询用户进行中会议列表
> Updated: 2026-06-02 12:02:37

# 查询用户进行中会议列表

查询用户进行中会议列表，返回进行中会议id列表及该用户在会中对应的成员信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/users/lists |
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
| unionId | String | 是 | 要查询的用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/conference/users/lists?unionId=2iPOLbpUNMLzB5LuwggiiqiPwiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:31c73ec295503618b3a03ddf2dcffef7
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
        com.aliyun.dingtalkconference_1_0.models.QueryUserOnGoingConferenceHeaders queryUserOnGoingConferenceHeaders = new com.aliyun.dingtalkconference_1_0.models.QueryUserOnGoingConferenceHeaders();
        queryUserOnGoingConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.QueryUserOnGoingConferenceRequest queryUserOnGoingConferenceRequest = new com.aliyun.dingtalkconference_1_0.models.QueryUserOnGoingConferenceRequest()
                .setUnionId("2iPOLbpUNMLzB5LuwggiiqiPwiEiE");
        try {
            client.queryUserOnGoingConferenceWithOptions(queryUserOnGoingConferenceRequest, queryUserOnGoingConferenceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_user_on_going_conference_headers = dingtalkconference__1__0_models.QueryUserOnGoingConferenceHeaders()
        query_user_on_going_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_on_going_conference_request = dingtalkconference__1__0_models.QueryUserOnGoingConferenceRequest(
            union_id='2iPOLbpUNMLzB5LuwggiiqiPwiEiE'
        )
        try:
            client.query_user_on_going_conference_with_options(query_user_on_going_conference_request, query_user_on_going_conference_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_user_on_going_conference_headers = dingtalkconference__1__0_models.QueryUserOnGoingConferenceHeaders()
        query_user_on_going_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_on_going_conference_request = dingtalkconference__1__0_models.QueryUserOnGoingConferenceRequest(
            union_id='2iPOLbpUNMLzB5LuwggiiqiPwiEiE'
        )
        try:
            await client.query_user_on_going_conference_with_options_async(query_user_on_going_conference_request, query_user_on_going_conference_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryUserOnGoingConferenceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryUserOnGoingConferenceRequest;
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
        $queryUserOnGoingConferenceHeaders = new QueryUserOnGoingConferenceHeaders([]);
        $queryUserOnGoingConferenceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryUserOnGoingConferenceRequest = new QueryUserOnGoingConferenceRequest([
            "unionId" => "2iPOLbpUNMLzB5LuwggiiqiPwiEiE"
        ]);
        try {
            $client->queryUserOnGoingConferenceWithOptions($queryUserOnGoingConferenceRequest, $queryUserOnGoingConferenceHeaders, new RuntimeOptions([]));
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

  queryUserOnGoingConferenceHeaders := &dingtalkconference_1_0.QueryUserOnGoingConferenceHeaders{}
  queryUserOnGoingConferenceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryUserOnGoingConferenceRequest := &dingtalkconference_1_0.QueryUserOnGoingConferenceRequest{
    UnionId: tea.String("2iPOLbpUNMLzB5LuwggiiqiPwiEiE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryUserOnGoingConferenceWithOptions(queryUserOnGoingConferenceRequest, queryUserOnGoingConferenceHeaders, &util.RuntimeOptions{})
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
    let queryUserOnGoingConferenceHeaders = new $dingtalkconference_1_0.QueryUserOnGoingConferenceHeaders({ });
    queryUserOnGoingConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryUserOnGoingConferenceRequest = new $dingtalkconference_1_0.QueryUserOnGoingConferenceRequest({
      unionId: "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
    });
    try {
      await client.queryUserOnGoingConferenceWithOptions(queryUserOnGoingConferenceRequest, queryUserOnGoingConferenceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryUserOnGoingConferenceHeaders queryUserOnGoingConferenceHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryUserOnGoingConferenceHeaders();
            queryUserOnGoingConferenceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryUserOnGoingConferenceRequest queryUserOnGoingConferenceRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryUserOnGoingConferenceRequest
            {
                UnionId = "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
            };
            try
            {
                client.QueryUserOnGoingConferenceWithOptions(queryUserOnGoingConferenceRequest, queryUserOnGoingConferenceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| onGoingConfIdList | Array of String | 会议id。 |
| memberModelMap | Map<String, Object> | 查询用户在会中的成员信息映射。 |
|  | Object | 成员信息。 |
| unionId | String | 成员的unionId。 |
| conferenceId | String | 视频会议ID。 |
| userNick | String | 成员的昵称。 |
| joinTime | Long | 成员入会时间戳，单位毫秒。 |
| leaveTime | Long | 成员离会时间戳，单位毫秒。 |
| duration | Long | 在会时长，单位毫秒。 |
| attendStatus | Integer | 成员状态：   - 1：初始化 - 2：呼叫中 - 3：活跃（在会） - 4：入会失败（拒接等） - 5：被踢 - 6：离会 |
| host | Boolean | 是否是主持人：   - true：是 - false：否 |
| coHost | Boolean | 是否为联席主持人：   - true：是 - false：否 |
| outerOrgMember | Boolean | 是否非会议所属企业内成员：   - true：是 - false：否 |
| pstnJoin | Boolean | 是否为电话号码入会：   - true：是 - false：否 |
| deviceType | String | 入会的设备类型：   - Win - Mac - iOS - Android |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "onGoingConfIdList" : [ "654058f2411fe90147e68780" ],
  "memberModelMap" : {
    "key" : {
      "unionId" : "2iPOLbpUNMLzB5LuwggiiqiPwiEiE",
      "conferenceId" : "654058f2411fe90147e68780",
      "userNick" : "测试昵称",
      "joinTime" : 1699347295876,
      "leaveTime" : 1699347395876,
      "duration" : 100000,
      "host" : false,
      "coHost" : false,
      "outerOrgMember" : false,
      "pstnJoin" : false,
      "deviceType" : "Win"
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | param.error | 查询人unionId错误 |
| 400 | param.error | missing.user.info | 查询人缺失 |
| 500 | system.error | system.error | 系统错误 |
