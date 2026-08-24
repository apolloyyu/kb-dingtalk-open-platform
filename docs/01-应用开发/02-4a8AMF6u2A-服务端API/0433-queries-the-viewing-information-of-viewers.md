---
title: "查询直播观看人员信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-viewing-information-of-viewers"
namespace: "development"
slug: "queries-the-viewing-information-of-viewers"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 直播 > 查询直播观看人员信息"
doc_id: "oO5JlT5NGJ"
updated_at: "2026-06-02 12:14:34"
---

> Source: https://open.dingtalk.com/document/development/queries-the-viewing-information-of-viewers
> Path: 应用开发 / 服务端API / 音视频 > 直播 > 查询直播观看人员信息
> Updated: 2026-06-02 12:14:34

# 查询直播观看人员信息

调用本接口，查询直播观看人员的具体观看信息。

## 接口调用说明

调用本接口，根据直播ID，查询直播观看人员的信息，可获取的信息如下：

- 企业内部应用调用本接口，可获取以下信息：

  - 当前组织内的员工观看直播信息，包括员工userId、姓名、观看时长等。
  - 非当前组织内的成员观看直播信息，包括成员昵称、观看时长等。
- 第三方企业应用调用本接口，可获取以下信息：

  - 当前组织内的员工观看直播信息，包括员工userId、姓名、观看时长等。
  - 非当前组织内的成员观看直播信息，只能获取到观看时长。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/live/lives/watchUsers |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Live.Common.Read-钉钉直播获取数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| liveId | String | 是 | 直播ID，可调用[创建直播](0429-create-live-streaming.md)接口获取。 |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| pageNumber | Integer | 否 | 分页起始位置，从0开始。 |
| pageSize | Integer | 是 | 分页大小，每页大小不超过200。 |

### 请求示例

HTTP

```
GET /v1.0/live/lives/watchUsers?liveId=1a353547-040d-4095-bb93-404bc5d47920&unionId=DC7wZGOSueEEIGOf3WKwWgiEiE&pageNumber=0&pageSize=20 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalklive_1_0.*;
import com.aliyun.dingtalklive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalklive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalklive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalklive_1_0.Client client = Sample.createClient();
        QueryLiveWatchUserListHeaders queryLiveWatchUserListHeaders = new QueryLiveWatchUserListHeaders();
        queryLiveWatchUserListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryLiveWatchUserListRequest queryLiveWatchUserListRequest = new QueryLiveWatchUserListRequest()
                .setLiveId("1a353547-040d-4095-bb93-404bc5d47920")
                .setUnionId("DC7wZGOSueEEIGOf3WKwWgiEiE")
                .setPageNumber(0)
                .setPageSize(20);
        try {
            client.queryLiveWatchUserListWithOptions(queryLiveWatchUserListRequest, queryLiveWatchUserListHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.live_1_0.client import Client as dingtalklive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.live_1_0 import models as dingtalklive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalklive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalklive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_live_watch_user_list_headers = dingtalklive__1__0_models.QueryLiveWatchUserListHeaders()
        query_live_watch_user_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_live_watch_user_list_request = dingtalklive__1__0_models.QueryLiveWatchUserListRequest(
            live_id='1a353547-040d-4095-bb93-404bc5d47920',
            union_id='DC7wZGOSueEEIGOf3WKwWgiEiE',
            page_number=0,
            page_size=20
        )
        try:
            client.query_live_watch_user_list_with_options(query_live_watch_user_list_request, query_live_watch_user_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_live_watch_user_list_headers = dingtalklive__1__0_models.QueryLiveWatchUserListHeaders()
        query_live_watch_user_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_live_watch_user_list_request = dingtalklive__1__0_models.QueryLiveWatchUserListRequest(
            live_id='1a353547-040d-4095-bb93-404bc5d47920',
            union_id='DC7wZGOSueEEIGOf3WKwWgiEiE',
            page_number=0,
            page_size=20
        )
        try:
            await client.query_live_watch_user_list_with_options_async(query_live_watch_user_list_request, query_live_watch_user_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\QueryLiveWatchUserListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\QueryLiveWatchUserListRequest;
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
        $queryLiveWatchUserListHeaders = new QueryLiveWatchUserListHeaders([]);
        $queryLiveWatchUserListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryLiveWatchUserListRequest = new QueryLiveWatchUserListRequest([
            "liveId" => "1a353547-040d-4095-bb93-404bc5d47920",
            "unionId" => "DC7wZGOSueEEIGOf3WKwWgiEiE",
            "pageNumber" => 0,
            "pageSize" => 20
        ]);
        try {
            $client->queryLiveWatchUserListWithOptions($queryLiveWatchUserListRequest, $queryLiveWatchUserListHeaders, new RuntimeOptions([]));
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
  dingtalklive_1_0  "github.com/alibabacloud-go/dingtalk/live_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalklive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalklive_1_0.Client{}
  _result, _err = dingtalklive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryLiveWatchUserListHeaders := &dingtalklive_1_0.QueryLiveWatchUserListHeaders{}
  queryLiveWatchUserListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryLiveWatchUserListRequest := &dingtalklive_1_0.QueryLiveWatchUserListRequest{
    LiveId: tea.String("1a353547-040d-4095-bb93-404bc5d47920"),
    UnionId: tea.String("DC7wZGOSueEEIGOf3WKwWgiEiE"),
    PageNumber: tea.Int32(0),
    PageSize: tea.Int32(20),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryLiveWatchUserListWithOptions(queryLiveWatchUserListRequest, queryLiveWatchUserListHeaders, &util.RuntimeOptions{})
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
import dingtalklive_1_0, * as $dingtalklive_1_0 from '@alicloud/dingtalk/live_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalklive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalklive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryLiveWatchUserListHeaders = new $dingtalklive_1_0.QueryLiveWatchUserListHeaders({ });
    queryLiveWatchUserListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryLiveWatchUserListRequest = new $dingtalklive_1_0.QueryLiveWatchUserListRequest({
      liveId: "1a353547-040d-4095-bb93-404bc5d47920",
      unionId: "DC7wZGOSueEEIGOf3WKwWgiEiE",
      pageNumber: 0,
      pageSize: 20,
    });
    try {
      await client.queryLiveWatchUserListWithOptions(queryLiveWatchUserListRequest, queryLiveWatchUserListHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalklive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalklive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalklive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchUserListHeaders queryLiveWatchUserListHeaders = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchUserListHeaders();
            queryLiveWatchUserListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchUserListRequest queryLiveWatchUserListRequest = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchUserListRequest
            {
                LiveId = "1a353547-040d-4095-bb93-404bc5d47920",
                UnionId = "DC7wZGOSueEEIGOf3WKwWgiEiE",
                PageNumber = 0,
                PageSize = 20,
            };
            try
            {
                client.QueryLiveWatchUserListWithOptions(queryLiveWatchUserListRequest, queryLiveWatchUserListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| orgUsesList | Array | 组织内的观看用户列表。 |
| unionId | String | 用户unionId。 |
| userId | String | 员工userId。 |
| name | String | 员工姓名。 |
| deptName | String | 员工所在部门名称。 |
| watchLiveTime | Long | 观看直播时长，单位毫秒。 |
| watchPlaybackTime | Long | 观看回放时长，单位毫秒。 |
| watchProgressMs | Long | 回放观看进度，单位毫秒。  **[!NOTE]**    指的是观看回放时当前进度条显示的时长。 |
| firstWatchTime | Long | 首次观看直播/回放时间戳 |
| outOrgUserList | Array | 组织外的观看用户列表。 |
| name | String | 用户昵称。   - 如果是企业内部应用，可获取组织外用户的钉钉昵称。 - 如果是第三方企业应用，获取不到组织外用户的钉钉昵称，统一字段值为**组织外观众**。 |
| watchLiveTime | Long | 观看直播时长，单位毫秒。 |
| watchPlaybackTime | Long | 观看回放时长，单位毫秒。 |
| watchProgressMs | Long | 回放观看进度，单位毫秒。  **[!NOTE]**    指的是观看回放时当前进度条显示的时长。 |
| firstWatchTime | Long | 首次观看直播/回放时间戳 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "orgUsesList" : [ {
      "unionId" : "DC7wxxxxx",
      "userId" : "214675",
      "name" : "李四",
      "deptName" : "xxx.设计部",
      "watchLiveTime" : 189930,
      "watchPlaybackTime" : 23667,
      "watchProgressMs" : 2330,
      "firstWatchTime" : 1751003911636
    } ],
    "outOrgUserList" : [ {
      "name" : "张三/组织外观众",
      "watchLiveTime" : 23440,
      "watchPlaybackTime" : 2330,
      "watchProgressMs" : 150,
      "firstWatchTime" : 1751003911636
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | lippi\_live.stream.paramError | 参数错误，该直播不存在 |
| 500 | serviceError | error:%s | 系统服务错误 |
