---
title: "查询视频会议信息"
source_url: "https://open.dingtalk.com/document/development/querying-video-conference-information"
namespace: "development"
slug: "querying-video-conference-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 查询视频会议信息"
doc_id: "nQjypaN34Q"
updated_at: "2026-06-03 10:12:04"
---

> Source: https://open.dingtalk.com/document/development/querying-video-conference-information
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 查询视频会议信息
> Updated: 2026-06-03 10:12:04

# 查询视频会议信息

调用本接口，获取会议的基本信息，包括会议名称、会议时长、会议开始时间、会议结束时间、累计参会人数等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId} |
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
| conferenceId | String | 是 | 会议conferenceId，可调用[创建视频会议](0399-create-a-video-conference.md)接口获取conferenceId。 |

### 请求示例

HTTP

```
GET /v1.0/conference/videoConferences/6323d7xxxxx HTTP/1.1
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
        com.aliyun.dingtalkconference_1_0.models.QueryConferenceInfoHeaders queryConferenceInfoHeaders = new com.aliyun.dingtalkconference_1_0.models.QueryConferenceInfoHeaders();
        queryConferenceInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.queryConferenceInfoWithOptions("6323d7xxxxx", queryConferenceInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_conference_info_headers = dingtalkconference__1__0_models.QueryConferenceInfoHeaders()
        query_conference_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.query_conference_info_with_options('6323d7xxxxx', query_conference_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_conference_info_headers = dingtalkconference__1__0_models.QueryConferenceInfoHeaders()
        query_conference_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.query_conference_info_with_options_async('6323d7xxxxx', query_conference_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceInfoHeaders;
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
        $queryConferenceInfoHeaders = new QueryConferenceInfoHeaders([]);
        $queryConferenceInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->queryConferenceInfoWithOptions("6323d7xxxxx", $queryConferenceInfoHeaders, new RuntimeOptions([]));
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

  queryConferenceInfoHeaders := &dingtalkconference_1_0.QueryConferenceInfoHeaders{}
  queryConferenceInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryConferenceInfoWithOptions(tea.String("6323d7xxxxx"), queryConferenceInfoHeaders, &util.RuntimeOptions{})
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
    let queryConferenceInfoHeaders = new $dingtalkconference_1_0.QueryConferenceInfoHeaders({ });
    queryConferenceInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.queryConferenceInfoWithOptions("6323d7xxxxx", queryConferenceInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoHeaders queryConferenceInfoHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoHeaders();
            queryConferenceInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.QueryConferenceInfoWithOptions("6323d7xxxxx", queryConferenceInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| confInfo | Object | 会议信息。 |
| activeNum | Integer | 当前在会人数。 |
| attendNum | Integer | 累积入会人数。 |
| confDuration | Long | 会议时长，单位毫秒。      会议结束后，返回该字段。 |
| conferenceId | String | 会议ID。 |
| creatorId | String | 会议创建人的unionId。 |
| creatorNick | String | 会议创建人的昵称。 |
| externalLinkUrl | String | 会议的入会链接。 |
| invitedNum | Integer | 邀请人数。 |
| startTime | Long | 会议开始时间戳，单位毫秒。 |
| status | Integer | 会议状态。   - 0：初始化 - 1：会议结束 - 2：会议开始 |
| title | String | 会议标题。 |
| roomCode | String | 会议码。 |
| endTime | Long | 会议结束时间戳，单位毫秒。      会议结束后，返回该字段。 |
| scheduleConferenceId | String | 预约会议id。 |
| bizType | String | 会议业务类型：   - **0**：即时视频会议 - **3**：预约会议 - **audio\_conf**：语音会议 |
| cloudRecordStatus | Integer | 会议云录制状态：   - **0**：未录制 - **1**：录制中 - **2**：录制暂停 - **3**：录制已结束 |
| cloudRecordOwnerUnionId | String | 云录制归属者unionId。 |
| minutesStatus | Integer | 会议闪记状态：   - **0**：未开启 - **1**：录制中 - **2**：暂停 - **3**：已结束       会中闪记能力迁移，该字段不再返回 |
| minutesOwnerUnionId | String | 闪记归属者unionId。      会中闪记能力迁移，该字段不再返回 |
| extensionAppSettings | Array | 会议维度扩展应用自定义信息列表。 |
| appId | String | 会议酷应用所属微应用AgentId。 |
| appCode | String | 酷应用 appCode。 |
| autoOpenMode | Integer | 自动打开模式：   - **0**：不自动打开 - **1**：仅主持人/联席主持人自动打开 - **2**：全员自动打开 |
| extensionAppBizData | String | 会议维度扩展应用自定义信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "confInfo" : {
    "activeNum" : 10,
    "attendNum" : 15,
    "confDuration" : 1000000,
    "conferenceId" : "6323dxxxxx",
    "creatorId" : "2iPOLxxxxx",
    "creatorNick" : "小钉",
    "externalLinkUrl" : "https://meeting.dingtalk.com/app?roomCode=42726xxx&token=1_7ac9xxx",
    "invitedNum" : 20,
    "startTime" : 1664175001000,
    "status" : 1,
    "title" : "标题",
    "roomCode" : "4272xxxxx",
    "endTime" : 1663294270000,
    "scheduleConferenceId" : "4331d******",
    "bizType" : "0",
    "cloudRecordStatus" : 0,
    "cloudRecordOwnerUnionId" : "A***EiE",
    "minutesStatus" : 0,
    "minutesOwnerUnionId" : "A***EiE",
    "extensionAppSettings" : [ {
      "appId" : "29****",
      "appCode" : "Coo*****",
      "autoOpenMode" : 0,
      "extensionAppBizData" : "****"
    } ]
  }
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
