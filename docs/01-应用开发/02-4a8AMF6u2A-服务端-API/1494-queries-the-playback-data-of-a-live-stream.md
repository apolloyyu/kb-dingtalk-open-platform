---
title: "查询直播的观看数据"
source_url: "https://open.dingtalk.com/document/development/queries-the-playback-data-of-a-live-stream"
namespace: "development"
slug: "queries-the-playback-data-of-a-live-stream"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 音视频 > 查询直播的观看数据"
doc_id: "T4AAS8PCuq"
updated_at: "2026-08-25 09:37:23"
---

> Source: https://open.dingtalk.com/document/development/queries-the-playback-data-of-a-live-stream
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 音视频 > 查询直播的观看数据
> Updated: 2026-08-25 09:37:23

# 查询直播的观看数据

调用本接口，查询直播的观看数据。

> **[!IMPORTANT]**
>
> 为统一数据资产管理体验，钉钉数据资产平台已整合原分散的数据服务。本接口及另外 60 个[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description) 已停止新权限申请，本文档同步迁入「历史文档」目录。
>
> 本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
> - **未接入用户**：请直接使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取数据服务。
> - **已接入用户**：请评估业务情况，逐步切换至钉钉数据资产平台。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v1.0/live/lives/watchDetails?liveId=String&unionId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| liveId | String | 是 | 直播ID，可调用[创建直播](0429-create-live-streaming.md)接口获取liveId参数值。 |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 返回结果。 |
| pv | Integer | 观看次数。 |
| uv | Integer | 观看总人数。 |
| liveUv | Integer | 观看直播人数。 |
| playbackUv | Integer | 观看回放人数。 |
| totalWatchTime | Long | 观看总时长，单位毫秒。 |
| avgWatchTime | Long | 平均观看时长，单位毫秒。 |
| praiseCount | Integer | 点赞数。 |
| msgCount | Integer | 消息数。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/live/lives/watchDetails?liveId=1a353xxxxx&unionId=DC7wxxxxx HTTP/1.1
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
        QueryLiveWatchDetailHeaders queryLiveWatchDetailHeaders = new QueryLiveWatchDetailHeaders();
        queryLiveWatchDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryLiveWatchDetailRequest queryLiveWatchDetailRequest = new QueryLiveWatchDetailRequest()
                .setLiveId("1a353xxxxx")
                .setUnionId("DC7wxxxxx");
        try {
            client.queryLiveWatchDetailWithOptions(queryLiveWatchDetailRequest, queryLiveWatchDetailHeaders, new RuntimeOptions());
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
        query_live_watch_detail_headers = dingtalklive__1__0_models.QueryLiveWatchDetailHeaders()
        query_live_watch_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_live_watch_detail_request = dingtalklive__1__0_models.QueryLiveWatchDetailRequest(
            live_id='1a353xxxxx',
            union_id='DC7wxxxxx'
        )
        try:
            client.query_live_watch_detail_with_options(query_live_watch_detail_request, query_live_watch_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_live_watch_detail_headers = dingtalklive__1__0_models.QueryLiveWatchDetailHeaders()
        query_live_watch_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_live_watch_detail_request = dingtalklive__1__0_models.QueryLiveWatchDetailRequest(
            live_id='1a353xxxxx',
            union_id='DC7wxxxxx'
        )
        try:
            await client.query_live_watch_detail_with_options_async(query_live_watch_detail_request, query_live_watch_detail_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\QueryLiveWatchDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\QueryLiveWatchDetailRequest;
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
        $queryLiveWatchDetailHeaders = new QueryLiveWatchDetailHeaders([]);
        $queryLiveWatchDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryLiveWatchDetailRequest = new QueryLiveWatchDetailRequest([
            "liveId" => "1a353xxxxx",
            "unionId" => "DC7wxxxxx"
        ]);
        try {
            $client->queryLiveWatchDetailWithOptions($queryLiveWatchDetailRequest, $queryLiveWatchDetailHeaders, new RuntimeOptions([]));
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

  queryLiveWatchDetailHeaders := &dingtalklive_1_0.QueryLiveWatchDetailHeaders{}
  queryLiveWatchDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryLiveWatchDetailRequest := &dingtalklive_1_0.QueryLiveWatchDetailRequest{
    LiveId: tea.String("1a353xxxxx"),
    UnionId: tea.String("DC7wxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryLiveWatchDetailWithOptions(queryLiveWatchDetailRequest, queryLiveWatchDetailHeaders, &util.RuntimeOptions{})
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
    let queryLiveWatchDetailHeaders = new $dingtalklive_1_0.QueryLiveWatchDetailHeaders({ });
    queryLiveWatchDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryLiveWatchDetailRequest = new $dingtalklive_1_0.QueryLiveWatchDetailRequest({
      liveId: "1a353xxxxx",
      unionId: "DC7wxxxxx",
    });
    try {
      await client.queryLiveWatchDetailWithOptions(queryLiveWatchDetailRequest, queryLiveWatchDetailHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchDetailHeaders queryLiveWatchDetailHeaders = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchDetailHeaders();
            queryLiveWatchDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchDetailRequest queryLiveWatchDetailRequest = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryLiveWatchDetailRequest
            {
                LiveId = "1a353xxxxx",
                UnionId = "DC7wxxxxx",
            };
            try
            {
                client.QueryLiveWatchDetailWithOptions(queryLiveWatchDetailRequest, queryLiveWatchDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "pv" : 120,
    "uv" : 90,
    "liveUv" : 55,
    "playbackUv" : 72,
    "totalWatchTime" : 1903640,
    "avgWatchTime" : 3560,
    "praiseCount" : 500,
    "msgCount" : 252
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | lippi\_live.stream.paramError | 参数错误，该直播不存在 |
| 500 | serviceError | error:%s | 系统服务错误 |
