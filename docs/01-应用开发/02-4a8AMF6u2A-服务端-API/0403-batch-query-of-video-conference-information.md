---
title: "批量查询视频会议信息"
source_url: "https://open.dingtalk.com/document/development/batch-query-of-video-conference-information"
namespace: "development"
slug: "batch-query-of-video-conference-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 批量查询视频会议信息"
doc_id: "YgiByk4X13"
updated_at: "2026-06-02 09:18:02"
---

> Source: https://open.dingtalk.com/document/development/batch-query-of-video-conference-information
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 批量查询视频会议信息
> Updated: 2026-06-02 09:18:02

# 批量查询视频会议信息

调用本接口查询会议信息以及参会人员。

## 接口调用说明

目前只支持查询正在进行的会议。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conferenceIdList | Array of String | 是 | 会议ID列表。 |

### 请求示例

HTTP

```
POST /v1.0/conference/videoConferences/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e1377bxxx
Content-Type:application/json

{
  "conferenceIdList" : [ "607452e0xxxxxxxxe39609e1" ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkconference_1_0.*;
import com.aliyun.dingtalkconference_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        QueryConferenceInfoBatchHeaders queryConferenceInfoBatchHeaders = new QueryConferenceInfoBatchHeaders();
        queryConferenceInfoBatchHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryConferenceInfoBatchRequest queryConferenceInfoBatchRequest = new QueryConferenceInfoBatchRequest()
                .setConferenceIdList(java.util.Arrays.asList(
                    "607452e0xxxxxxxxe39609e1"
                ));
        try {
            client.queryConferenceInfoBatchWithOptions(queryConferenceInfoBatchRequest, queryConferenceInfoBatchHeaders, new RuntimeOptions());
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
        query_conference_info_batch_headers = dingtalkconference__1__0_models.QueryConferenceInfoBatchHeaders()
        query_conference_info_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_conference_info_batch_request = dingtalkconference__1__0_models.QueryConferenceInfoBatchRequest(
            conference_id_list=[
                '607452e0xxxxxxxxe39609e1'
            ]
        )
        try:
            client.query_conference_info_batch_with_options(query_conference_info_batch_request, query_conference_info_batch_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_conference_info_batch_headers = dingtalkconference__1__0_models.QueryConferenceInfoBatchHeaders()
        query_conference_info_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_conference_info_batch_request = dingtalkconference__1__0_models.QueryConferenceInfoBatchRequest(
            conference_id_list=[
                '607452e0xxxxxxxxe39609e1'
            ]
        )
        try:
            await client.query_conference_info_batch_with_options_async(query_conference_info_batch_request, query_conference_info_batch_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceInfoBatchHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryConferenceInfoBatchRequest;
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
        $queryConferenceInfoBatchHeaders = new QueryConferenceInfoBatchHeaders([]);
        $queryConferenceInfoBatchHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryConferenceInfoBatchRequest = new QueryConferenceInfoBatchRequest([
            "conferenceIdList" => [
                "607452e0xxxxxxxxe39609e1"
            ]
        ]);
        try {
            $client->queryConferenceInfoBatchWithOptions($queryConferenceInfoBatchRequest, $queryConferenceInfoBatchHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  ""github.com/alibabacloud-go/dingtalk/conference_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  queryConferenceInfoBatchHeaders := &dingtalkconference_1_0.QueryConferenceInfoBatchHeaders{}
  queryConferenceInfoBatchHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryConferenceInfoBatchRequest := &dingtalkconference_1_0.QueryConferenceInfoBatchRequest{
    ConferenceIdList: []*string{tea.String("607452e0xxxxxxxxe39609e1")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryConferenceInfoBatchWithOptions(queryConferenceInfoBatchRequest, queryConferenceInfoBatchHeaders, &util.RuntimeOptions{})
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
import dingtalkconference_1_0, * as $dingtalkconference_1_0 from '"@alicloud/dingtalk/conference_1_0';
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
    let queryConferenceInfoBatchHeaders = new $dingtalkconference_1_0.QueryConferenceInfoBatchHeaders({ });
    queryConferenceInfoBatchHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryConferenceInfoBatchRequest = new $dingtalkconference_1_0.QueryConferenceInfoBatchRequest({
      conferenceIdList: [
        "607452e0xxxxxxxxe39609e1"
      ],
    });
    try {
      await client.queryConferenceInfoBatchWithOptions(queryConferenceInfoBatchRequest, queryConferenceInfoBatchHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoBatchHeaders queryConferenceInfoBatchHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoBatchHeaders();
            queryConferenceInfoBatchHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoBatchRequest queryConferenceInfoBatchRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryConferenceInfoBatchRequest
            {
                ConferenceIdList = new List<string>
                {
                    "607452e0xxxxxxxxe39609e1"
                },
            };
            try
            {
                client.QueryConferenceInfoBatchWithOptions(queryConferenceInfoBatchRequest, queryConferenceInfoBatchHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkconference__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

Alibabacloud_Dingtalkconference_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkconference_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::Client> client = make_shared<Alibabacloud_Dingtalkconference_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::QueryConferenceInfoBatchHeaders> queryConferenceInfoBatchHeaders = make_shared<Alibabacloud_Dingtalkconference_1_0::QueryConferenceInfoBatchHeaders>();
  queryConferenceInfoBatchHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::QueryConferenceInfoBatchRequest> queryConferenceInfoBatchRequest = make_shared<Alibabacloud_Dingtalkconference_1_0::QueryConferenceInfoBatchRequest>(map<string, boost::any>({
    {"conferenceIdList", boost::any(vector<string>({
      "607452e0xxxxxxxxe39609e1"
    }))}
  }));
  try {
    client->queryConferenceInfoBatchWithOptions(queryConferenceInfoBatchRequest, queryConferenceInfoBatchHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| infos | Array | 会议详情列表。 |
| conferenceId | String | 实时会议ID。 |
| title | String | 会议名称。 |
| startTime | Long | 会议开始时间。 |
| status | Long | 会议状态。   - **0**：初始化 - **1**：会议结束 - **2**：会议开始 |
| mediaStatus | Long | 媒体状态。   - **0**：正常 - **1**：麦克风静音 - **2**：摄像头关闭 - **4**：强制全员静音 |
| userList | Array | 参会用户列表。 |
| userId | String | 用户userid。 |
| nick | String | 用户昵称。 |
| attendStatus | Long | 在会状态。   - **0**：未定义 - **1**：初始化 - **2**：加入中 - **3**：在会 - **4**：加入失败 - **5**：被踢出 - **6**：离开 |
| cameraStatus | Long | 摄像头状态。   - **0**：初始化 - **1**：关闭 - **2**：打开 |
| micStatus | Long | 麦克风状态。   - **0**：初始化 - **1**：关闭 - **2**：打开 |
| rejectDescription | String | 拒绝原因。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "infos" : [ {
    "conferenceId" : "607452e0xxx",
    "title" : "示例会议",
    "status" : 2,
    "mediaStatus" : 0,
    "userList" : [ {
      "userId" : "27SaQ3iiHLN0uwqcPisedfreNwiEiE",
      "nick" : "钉三多",
      "attendStatus" : 3,
      "cameraStatus" : 2,
      "micStatus" : 2,
      "rejectDescription" : "抱歉，正在开会"
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgAccessForbidden | orgAccessForbidden | 组织访问受限 |
| 400 | unknownUserError | unknownUserError | 无法识别的用户 |
| 400 | paramsTitleError | error:%s | 会议标题非法 |
| 400 | paramsError | error:%s | 参数错误 |
| 400 | resourceClose | The meeting has ended | 该会议已被关闭 |
| 404 | waterLimitError | waterLimitError:%s | 人数水位限流 |
| 404 | permissionError | permissionError:%s | 群权限限制 |
| 500 | systemError | systemError:%s | 系统错误 |
