---
title: "开启视频会议直播推流"
source_url: "https://open.dingtalk.com/document/development/video-conference-enables-live-stream-ingest"
namespace: "development"
slug: "video-conference-enables-live-stream-ingest"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 开启视频会议直播推流"
doc_id: "ylXJdST5qr"
updated_at: "2026-06-03 10:12:05"
---

> Source: https://open.dingtalk.com/document/development/video-conference-enables-live-stream-ingest
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 开启视频会议直播推流
> Updated: 2026-06-03 10:12:05

# 开启视频会议直播推流

调用本接口开启视频会议直播推流。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/streamOuts/start |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取第三方个人应用的access\_token](0035-obtain-personal-application.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conferenceId | String | 是 | 会议id，可调用[创建视频会议](0399-create-a-video-conference.md)接口获取返回参数`conferenceId`字段。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId。 |
| needHostJoin | Boolean | 是 | 是否需要主持人加入后才允许推流：   - true：允许 - false：不允许 |
| streamUrlList | Array of String | 是 | 推流地址列表，最多10个，需要以rtmp开头。 |
| streamName | String | 是 | 推流名称。 |
| mode | String | 是 | 布局，取值：   - **grid**：宫格模式 - **speech**：演讲者模式 - **full\_screen**：全屏模式 |
| smallWindowPosition | String | 是 | 小窗位置，取值：   - **relative\_right**：分离右侧 - **float\_right**：悬浮右侧 - **float\_bottom**：悬浮底部 |

### 请求示例

HTTP

```
POST /v1.0/conference/videoConferences/61289fxxx/streamOuts/start HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d27c054b72bd3f4398c9fxxxxx71e866
Content-Type:application/json

{
  "unionId" : "wfh98hxxx",
  "needHostJoin" : false,
  "streamUrlList" : [ "rtmp://ns8.indexforce.com/home/mystream" ],
  "streamName" : "推流名称",
  "mode" : "grip",
  "smallWindowPosition" : "relative_right"
}
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
        com.aliyun.dingtalkconference_1_0.models.StartStreamOutHeaders startStreamOutHeaders = new com.aliyun.dingtalkconference_1_0.models.StartStreamOutHeaders();
        startStreamOutHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.StartStreamOutRequest startStreamOutRequest = new com.aliyun.dingtalkconference_1_0.models.StartStreamOutRequest()
                .setUnionId("wfh98hxxx")
                .setNeedHostJoin(false)
                .setStreamUrlList(java.util.Arrays.asList(
                    "rtmp://ns8.indexforce.com/home/mystream"
                ))
                .setStreamName("推流名称")
                .setMode("grip")
                .setSmallWindowPosition("relative_right");
        try {
            client.startStreamOutWithOptions("61289fxxx", startStreamOutRequest, startStreamOutHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        start_stream_out_headers = dingtalkconference__1__0_models.StartStreamOutHeaders()
        start_stream_out_headers.x_acs_dingtalk_access_token = '<your access token>'
        start_stream_out_request = dingtalkconference__1__0_models.StartStreamOutRequest(
            union_id='wfh98hxxx',
            need_host_join=False,
            stream_url_list=[
                'rtmp://ns8.indexforce.com/home/mystream'
            ],
            stream_name='推流名称',
            mode='grip',
            small_window_position='relative_right'
        )
        try:
            client.start_stream_out_with_options('61289fxxx', start_stream_out_request, start_stream_out_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        start_stream_out_headers = dingtalkconference__1__0_models.StartStreamOutHeaders()
        start_stream_out_headers.x_acs_dingtalk_access_token = '<your access token>'
        start_stream_out_request = dingtalkconference__1__0_models.StartStreamOutRequest(
            union_id='wfh98hxxx',
            need_host_join=False,
            stream_url_list=[
                'rtmp://ns8.indexforce.com/home/mystream'
            ],
            stream_name='推流名称',
            mode='grip',
            small_window_position='relative_right'
        )
        try:
            await client.start_stream_out_with_options_async('61289fxxx', start_stream_out_request, start_stream_out_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\StartStreamOutHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\StartStreamOutRequest;
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
        $startStreamOutHeaders = new StartStreamOutHeaders([]);
        $startStreamOutHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $startStreamOutRequest = new StartStreamOutRequest([
            "unionId" => "wfh98hxxx",
            "needHostJoin" => false,
            "streamUrlList" => [
                "rtmp://ns8.indexforce.com/home/mystream"
            ],
            "streamName" => "推流名称",
            "mode" => "grip",
            "smallWindowPosition" => "relative_right"
        ]);
        try {
            $client->startStreamOutWithOptions("61289fxxx", $startStreamOutRequest, $startStreamOutHeaders, new RuntimeOptions([]));
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

  startStreamOutHeaders := &dingtalkconference_1_0.StartStreamOutHeaders{}
  startStreamOutHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  startStreamOutRequest := &dingtalkconference_1_0.StartStreamOutRequest{
    UnionId: tea.String("wfh98hxxx"),
    NeedHostJoin: tea.Bool(false),
    StreamUrlList: []*string{tea.String("rtmp://ns8.indexforce.com/home/mystream")},
    StreamName: tea.String("推流名称"),
    Mode: tea.String("grip"),
    SmallWindowPosition: tea.String("relative_right"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.StartStreamOutWithOptions(tea.String("61289fxxx"), startStreamOutRequest, startStreamOutHeaders, &util.RuntimeOptions{})
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
    let startStreamOutHeaders = new $dingtalkconference_1_0.StartStreamOutHeaders({ });
    startStreamOutHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let startStreamOutRequest = new $dingtalkconference_1_0.StartStreamOutRequest({
      unionId: "wfh98hxxx",
      needHostJoin: false,
      streamUrlList: [
        "rtmp://ns8.indexforce.com/home/mystream"
      ],
      streamName: "推流名称",
      mode: "grip",
      smallWindowPosition: "relative_right",
    });
    try {
      await client.startStreamOutWithOptions("61289fxxx", startStreamOutRequest, startStreamOutHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StartStreamOutHeaders startStreamOutHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StartStreamOutHeaders();
            startStreamOutHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StartStreamOutRequest startStreamOutRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StartStreamOutRequest
            {
                UnionId = "wfh98hxxx",
                NeedHostJoin = false,
                StreamUrlList = new List<string>
                {
                    "rtmp://ns8.indexforce.com/home/mystream"
                },
                StreamName = "推流名称",
                Mode = "grip",
                SmallWindowPosition = "relative_right",
            };
            try
            {
                client.StartStreamOutWithOptions("61289fxxx", startStreamOutRequest, startStreamOutHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| successStreamMap | Map | 成功推流地址与liveId映射。 |
| failStreamMap | Map | 失败的地址与失败原因映射。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "successStreamMap" : {
    "rtmp://ns8.indexforce.com/home/mystream" : "61289f3xxx"
  },
  "failStreamMap" : {
    "rtmp://ns8.indexforce.com/home/mystream" : "inner error"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgAccessForbidden | orgAccessForbidden | 组织访问受限 |
| 400 | unknownUserError | unknownUserError | 无法识别的用户 |
| 400 | paramsError | error:%s | 参数错误 |
| 500 | systemError | systemError:%s | 系统错误 |
