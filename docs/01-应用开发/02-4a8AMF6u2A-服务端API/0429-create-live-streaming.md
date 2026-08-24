---
title: "创建直播"
source_url: "https://open.dingtalk.com/document/development/create-live-streaming"
namespace: "development"
slug: "create-live-streaming"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 直播 > 创建直播"
doc_id: "UkIjWpkYOL"
updated_at: "2026-06-01 14:35:23"
---

> Source: https://open.dingtalk.com/document/development/create-live-streaming
> Path: 应用开发 / 服务端API / 音视频 > 直播 > 创建直播
> Updated: 2026-06-01 14:35:23

# 创建直播

调用本接口，创建直播。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/live/lives |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Live.Common.Write-钉钉直播获取数据写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 发起直播的主播unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
| title | String | 是 | 直播标题。 |
| introduction | String | 否 | 直播简介。 |
| preStartTime | Long | 是 | 预计开播时间戳，单位毫秒。  **[!NOTE]**    该字段值需要大于当前的时间戳。 |
| coverUrl | String | 否 | 直播的封面地址。 |
| preEndTime | Long | 是 | 预计结束时间戳，单位毫秒。  **[!NOTE]**    该字段值需要大于预计开播时间。 |
| publicType | Long | 否 | 直播分享范围：   - **0**:不公开 - **1**:全面公开 - **2**:组织内公开 |
| enableLinkMic | Boolean | 否 | 是否开启连麦功能 |
| isLandscape | Boolean | 否 | 是否横屏直播 |

### 请求示例

HTTP

```
POST /v1.0/live/lives HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "unionId" : "DC7wxxxxx",
  "title" : "测试直播",
  "introduction" : "测试直播简介",
  "coverUrl" : "https://xxx.com/xxxxx.png",
  "preStartTime" : 1659613648000,
  "preEndTime" : 1659653648000,
  "publicType" : 2,
  "enableLinkMic" : true,
  "isLandscape" : true
}
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
        CreateLiveHeaders createLiveHeaders = new CreateLiveHeaders();
        createLiveHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateLiveRequest createLiveRequest = new CreateLiveRequest()
                .setUnionId("DC7wxxxxx")
                .setTitle("测试直播")
                .setIntroduction("测试直播简介")
                .setCoverUrl("https://xxx.com/xxxxx.png")
                .setPreStartTime(1659613648000L)
                .setPreEndTime(1659653648000L);
        try {
            client.createLiveWithOptions(createLiveRequest, createLiveHeaders, new RuntimeOptions());
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
        create_live_headers = dingtalklive__1__0_models.CreateLiveHeaders()
        create_live_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_live_request = dingtalklive__1__0_models.CreateLiveRequest(
            union_id='DC7wxxxxx',
            title='测试直播',
            introduction='测试直播简介',
            cover_url='https://xxx.com/xxxxx.png',
            pre_start_time=1659613648000,
            pre_end_time=1659653648000
        )
        try:
            client.create_live_with_options(create_live_request, create_live_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_live_headers = dingtalklive__1__0_models.CreateLiveHeaders()
        create_live_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_live_request = dingtalklive__1__0_models.CreateLiveRequest(
            union_id='DC7wxxxxx',
            title='测试直播',
            introduction='测试直播简介',
            cover_url='https://xxx.com/xxxxx.png',
            pre_start_time=1659613648000,
            pre_end_time=1659653648000
        )
        try:
            await client.create_live_with_options_async(create_live_request, create_live_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\CreateLiveHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\CreateLiveRequest;
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
        $createLiveHeaders = new CreateLiveHeaders([]);
        $createLiveHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createLiveRequest = new CreateLiveRequest([
            "unionId" => "DC7wxxxxx",
            "title" => "测试直播",
            "introduction" => "测试直播简介",
            "coverUrl" => "https://xxx.com/xxxxx.png",
            "preStartTime" => 1659613648000,
            "preEndTime" => 1659653648000
        ]);
        try {
            $client->createLiveWithOptions($createLiveRequest, $createLiveHeaders, new RuntimeOptions([]));
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

  createLiveHeaders := &dingtalklive_1_0.CreateLiveHeaders{}
  createLiveHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createLiveRequest := &dingtalklive_1_0.CreateLiveRequest{
    UnionId: tea.String("DC7wxxxxx"),
    Title: tea.String("测试直播"),
    Introduction: tea.String("测试直播简介"),
    CoverUrl: tea.String("https://xxx.com/xxxxx.png"),
    PreStartTime: tea.Int64(1659613648000),
    PreEndTime: tea.Int64(1659653648000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateLiveWithOptions(createLiveRequest, createLiveHeaders, &util.RuntimeOptions{})
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
    let createLiveHeaders = new $dingtalklive_1_0.CreateLiveHeaders({ });
    createLiveHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createLiveRequest = new $dingtalklive_1_0.CreateLiveRequest({
      unionId: "DC7wxxxxx",
      title: "测试直播",
      introduction: "测试直播简介",
      coverUrl: "https://xxx.com/xxxxx.png",
      preStartTime: 1659613648000,
      preEndTime: 1659653648000,
    });
    try {
      await client.createLiveWithOptions(createLiveRequest, createLiveHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.CreateLiveHeaders createLiveHeaders = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.CreateLiveHeaders();
            createLiveHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.CreateLiveRequest createLiveRequest = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.CreateLiveRequest
            {
                UnionId = "DC7wxxxxx",
                Title = "测试直播",
                Introduction = "测试直播简介",
                CoverUrl = "https://xxx.com/xxxxx.png",
                PreStartTime = 1659613648000,
                PreEndTime = 1659653648000,
            };
            try
            {
                client.CreateLiveWithOptions(createLiveRequest, createLiveHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| liveId | String | 直播ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "liveId" : "1a3535xxxxx"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | lippi\_live.stream.paramError | 参数错误，预计开播时间必须是未来时间并且小于预计结束时间。 |
| 400 | contentNotCompliant | lippi\_live.validate.contentNotCompliant | 内容不合规 |
| 400 | noPermission | lippi\_live.stream.noPermission | 鉴权失败，请检查publicType字段是否为全域公开,若全域公开需要升级直播权益； |
| 400 | invalidParam | lippi\_live.room.preStartTimeCanNotEarlierThanNow | 预计开始时间不能早于当前时间 |
| 400 | userNoLivePermission | lippi\_live.exception.userNoLivePermission | 用户在当前组织没有直播权限 |
| 500 | serviceError | systemError | 系统服务错误 |
