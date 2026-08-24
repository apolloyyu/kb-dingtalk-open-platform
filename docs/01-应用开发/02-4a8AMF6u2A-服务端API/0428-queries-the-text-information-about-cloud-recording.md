---
title: "查询会议录制中的文本信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-text-information-about-cloud-recording"
namespace: "development"
slug: "queries-the-text-information-about-cloud-recording"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 查询会议录制中的文本信息"
doc_id: "tAN0YVScb6"
updated_at: "2026-06-02 12:08:32"
---

> Source: https://open.dingtalk.com/document/development/queries-the-text-information-about-cloud-recording
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 查询会议录制中的文本信息
> Updated: 2026-06-02 12:08:32

# 查询会议录制中的文本信息

调用本接口，查询视频会议录制的语音转文字信息，包括文本内容、文本记录开始时间、文本记录结束时间等。

## 接口调用说明

钉钉视频会议如果开启了云录制（闪记），在开启云录制期间，参会人员发表讲话的内容会自动被转换为文本生成记录。

例如，会议主持人开启了**会议录制-云录制**功能，会议结束后，主持人收到会议录制的推送消息。记录的语音转文字记录中的内容如下图所示。

调用本接口，可获取云录制过程中记录的文本信息，包括文本内容、文本记录开始时间、文本记录结束时间等。 ![](https://img.alicdn.com/imgextra/i2/O1CN019tvQQy1pM3jNl0JLt_!!6000000005345-2-tps-2662-1298.png)

> **[!NOTE]**
>
> 主持人开启会议录制时，需要先选择**云录制（闪记）**，并且在录制期间，参会人员有发言的行为，才可调用本接口查询会议录制中的文本信息。 ![](https://img.alicdn.com/imgextra/i1/O1CN01i4Lml31i0o2RDtPBE_!!6000000004351-2-tps-2202-1568.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/cloudRecords/getTexts |
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
| conferenceId | String | 否 | 会议ID，可调用[创建视频会议](0399-create-a-video-conference.md)接口获取conferenceId参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 否 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
| startTime | Long | 否 | 开始时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值传2000，表示从录制开始的第2秒开始查询。 |
| direction | String | 否 | 查询方式：   - **0**：表示此次查询按照时间由小到大的顺序进行，默认方式。 - **1**：表示此次查询按照时间由大到小的顺序进行。 |
| maxResults | Long | 否 | 单词查询条数，最大2000。 |
| nextToken | Long | 否 | 分页游标。   - 如果是首次查询，该参数可不传。 - 如果是非首次查询，该参数传上次调用本接口时返回的nextToken。 |

### 请求示例

HTTP

```
GET /v1.0/conference/videoConferences/6139b4xxx/cloudRecords/getTexts?unionId=WFBkgJxxx&startTime=6080&direction=1&maxResults=200&nextToken=0 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:ecd72axxx
Content-Type:application/json
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
        QueryCloudRecordTextHeaders queryCloudRecordTextHeaders = new QueryCloudRecordTextHeaders();
        queryCloudRecordTextHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryCloudRecordTextRequest queryCloudRecordTextRequest = new QueryCloudRecordTextRequest()
                .setUnionId("WFBkgJxxx")
                .setStartTime(6080L)
                .setDirection("1")
                .setMaxResults(200L)
                .setNextToken(0L);
        try {
            client.queryCloudRecordTextWithOptions("6139b4xxx", queryCloudRecordTextRequest, queryCloudRecordTextHeaders, new RuntimeOptions());
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
        query_cloud_record_text_headers = dingtalkconference__1__0_models.QueryCloudRecordTextHeaders()
        query_cloud_record_text_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_cloud_record_text_request = dingtalkconference__1__0_models.QueryCloudRecordTextRequest(
            union_id='WFBkgJxxx',
            start_time=6080,
            direction='1',
            max_results=200,
            next_token=0
        )
        try:
            client.query_cloud_record_text_with_options('6139b4xxx', query_cloud_record_text_request, query_cloud_record_text_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_cloud_record_text_headers = dingtalkconference__1__0_models.QueryCloudRecordTextHeaders()
        query_cloud_record_text_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_cloud_record_text_request = dingtalkconference__1__0_models.QueryCloudRecordTextRequest(
            union_id='WFBkgJxxx',
            start_time=6080,
            direction='1',
            max_results=200,
            next_token=0
        )
        try:
            await client.query_cloud_record_text_with_options_async('6139b4xxx', query_cloud_record_text_request, query_cloud_record_text_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryCloudRecordTextHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryCloudRecordTextRequest;
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
        $queryCloudRecordTextHeaders = new QueryCloudRecordTextHeaders([]);
        $queryCloudRecordTextHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryCloudRecordTextRequest = new QueryCloudRecordTextRequest([
            "unionId" => "WFBkgJxxx",
            "startTime" => 6080,
            "direction" => "1",
            "maxResults" => 200,
            "nextToken" => 0
        ]);
        try {
            $client->queryCloudRecordTextWithOptions("6139b4xxx", $queryCloudRecordTextRequest, $queryCloudRecordTextHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
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

  queryCloudRecordTextHeaders := &dingtalkconference_1_0.QueryCloudRecordTextHeaders{}
  queryCloudRecordTextHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryCloudRecordTextRequest := &dingtalkconference_1_0.QueryCloudRecordTextRequest{
    UnionId: tea.String("WFBkgJxxx"),
    StartTime: tea.Int64(6080),
    Direction: tea.String("1"),
    MaxResults: tea.Int64(200),
    NextToken: tea.Int64(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryCloudRecordTextWithOptions(tea.String("6139b4xxx"), queryCloudRecordTextRequest, queryCloudRecordTextHeaders, &util.RuntimeOptions{})
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
    let queryCloudRecordTextHeaders = new $dingtalkconference_1_0.QueryCloudRecordTextHeaders({ });
    queryCloudRecordTextHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryCloudRecordTextRequest = new $dingtalkconference_1_0.QueryCloudRecordTextRequest({
      unionId: "WFBkgJxxx",
      startTime: 6080,
      direction: "1",
      maxResults: 200,
      nextToken: 0,
    });
    try {
      await client.queryCloudRecordTextWithOptions("6139b4xxx", queryCloudRecordTextRequest, queryCloudRecordTextHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryCloudRecordTextHeaders queryCloudRecordTextHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryCloudRecordTextHeaders();
            queryCloudRecordTextHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryCloudRecordTextRequest queryCloudRecordTextRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryCloudRecordTextRequest
            {
                UnionId = "WFBkgJxxx",
                StartTime = 6080,
                Direction = "1",
                MaxResults = 200,
                NextToken = 0,
            };
            try
            {
                client.QueryCloudRecordTextWithOptions("6139b4xxx", queryCloudRecordTextRequest, queryCloudRecordTextHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::QueryCloudRecordTextHeaders> queryCloudRecordTextHeaders = make_shared<Alibabacloud_Dingtalkconference_1_0::QueryCloudRecordTextHeaders>();
  queryCloudRecordTextHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::QueryCloudRecordTextRequest> queryCloudRecordTextRequest = make_shared<Alibabacloud_Dingtalkconference_1_0::QueryCloudRecordTextRequest>(map<string, boost::any>({
    {"unionId", boost::any(string("WFBkgJxxx"))},
    {"startTime", boost::any(6080)},
    {"direction", boost::any(string("1"))},
    {"maxResults", boost::any(200)},
    {"nextToken", boost::any(0)}
  }));
  try {
    client->queryCloudRecordTextWithOptions(make_shared<string>("6139b4xxx"), queryCloudRecordTextRequest, queryCloudRecordTextHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| hasMore | Boolean | 是否有更多数据。   - true：是 - false：否 |
| paragraphList | Array | 段落列表。 |
| nextTtoken | Long | 下一次请求的分页游标。 |
| status | Long | 状态。  **[!NOTE]**    该字段暂无使用场景。 |
| unionId | String | 发言人的unionId。 |
| nickName | String | 发言人昵称。 |
| recordId | Long | 录制ID。 |
| startTime | Long | 段落记录产生时，在会议录制期间内相对时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值是2000，表示在会议录制开始的第2秒，开始了本次语音转文字的记录。 |
| endTime | Long | 段落记录结束时，在会议录制期间内相对时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值是8000，表示在会议录制开始的第8秒，结束了本次语音转文字的记录。 |
| paragraph | String | 段落内容。 |
| sentenceList | Array | 句子列表。 |
| unionId | String | 用户的unionId。 |
| sentence | String | 句子。 |
| startTime | Long | 句子记录产生时，在会议录制期间内相对时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值是2000，表示在会议录制开始的第2秒，开始了本次语音转文字的记录。 |
| endTime | Long | 句子记录结束时，在会议录制期间内相对时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值是2000，表示在会议录制开始的第2秒，结束了本次语音转文字的记录。 |
| wordList | Array | 单词列表。 |
| word | String | 单词。 |
| startTime | Long | 单词记录产生时，在会议录制期间内相对时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值是2000，表示在会议录制开始的第2秒，开始了本次语音转文字的记录。 |
| endTime | Long | 单词记录结束时，在会议录制期间内相对时间的千分之一秒，单位毫秒。  **[!NOTE]**    例如，该参数值是2000，表示在会议录制开始的第2秒，结束了本次语音转文字的记录。 |
| wordId | String | 单词ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "hasMore" : true,
  "paragraphList" : [ {
    "nextTtoken" : 1631172045153000,
    "status" : 1,
    "unionId" : "WFBkgJvxxx",
    "nickName" : "小钉",
    "recordId" : 44444,
    "startTime" : 7940,
    "endTime" : 7940,
    "paragraph" : "嘿！你好，这里是小钉",
    "sentenceList" : [ {
      "unionId" : "WFBkgJvtxxx",
      "sentence" : "这里是小钉",
      "startTime" : 7940,
      "endTime" : 7940,
      "wordList" : [ {
        "word" : "这里",
        "startTime" : 7940,
        "endTime" : 7940,
        "wordId" : "1631172050535000#0"
      } ]
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
| 400 | paramsError | error:%s | 参数错误 |
| 400 | resourceClose | The meeting has ended | 该会议已被关闭 |
| 400 | cloudRecordNotFound | cloudRecordNotFound | 云录制记录未找到/未开启云录制 |
| 404 | permissionError | permissionError:%s | 群权限限制 |
| 500 | systemError | systemError:%s | 系统错误 |
