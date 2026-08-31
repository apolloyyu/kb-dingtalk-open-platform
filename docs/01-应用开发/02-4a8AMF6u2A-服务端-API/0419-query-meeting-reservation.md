---
title: "查询预约会议"
source_url: "https://open.dingtalk.com/document/development/query-meeting-reservation"
namespace: "development"
slug: "query-meeting-reservation"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 查询预约会议"
doc_id: "eK8zwHThXa"
updated_at: "2026-06-02 12:08:30"
---

> Source: https://open.dingtalk.com/document/development/query-meeting-reservation
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 查询预约会议
> Updated: 2026-06-02 12:08:30

# 查询预约会议

根据预约会议id查询预约会议标题等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/scheduleConferences/{scheduleConferenceId}/infos |
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
| scheduleConferenceId | String | 是 | 预约会议id，可通过[创建预约会议](0416-create-appointment-meeting.md)接口获取返回参数`scheduleConferenceId`字段。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| requestUnionId | String | 是 | 请求者unionId。 |

### 请求示例

HTTP

```
GET /v1.0/conference/scheduleConferences/2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx/infos?requestUnionId=qzR1iSMDvzR9iP7Pxxxxxxxxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2d7fb90563253ae1a64c16a5f2aaeb3d
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
        com.aliyun.dingtalkconference_1_0.models.QueryScheduleConferenceHeaders queryScheduleConferenceHeaders = new com.aliyun.dingtalkconference_1_0.models.QueryScheduleConferenceHeaders();
        queryScheduleConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.QueryScheduleConferenceRequest queryScheduleConferenceRequest = new com.aliyun.dingtalkconference_1_0.models.QueryScheduleConferenceRequest()
                .setRequestUnionId("qzR1iSMDvzR9iP7Pxxxxxxxxxxxx");
        try {
            client.queryScheduleConferenceWithOptions("2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx", queryScheduleConferenceRequest, queryScheduleConferenceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_schedule_conference_headers = dingtalkconference__1__0_models.QueryScheduleConferenceHeaders()
        query_schedule_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_schedule_conference_request = dingtalkconference__1__0_models.QueryScheduleConferenceRequest(
            request_union_id='qzR1iSMDvzR9iP7Pxxxxxxxxxxxx'
        )
        try:
            client.query_schedule_conference_with_options('2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx', query_schedule_conference_request, query_schedule_conference_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_schedule_conference_headers = dingtalkconference__1__0_models.QueryScheduleConferenceHeaders()
        query_schedule_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_schedule_conference_request = dingtalkconference__1__0_models.QueryScheduleConferenceRequest(
            request_union_id='qzR1iSMDvzR9iP7Pxxxxxxxxxxxx'
        )
        try:
            await client.query_schedule_conference_with_options_async('2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx', query_schedule_conference_request, query_schedule_conference_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryScheduleConferenceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryScheduleConferenceRequest;
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
        $queryScheduleConferenceHeaders = new QueryScheduleConferenceHeaders([]);
        $queryScheduleConferenceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryScheduleConferenceRequest = new QueryScheduleConferenceRequest([
            "requestUnionId" => "qzR1iSMDvzR9iP7Pxxxxxxxxxxxx"
        ]);
        try {
            $client->queryScheduleConferenceWithOptions("2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx", $queryScheduleConferenceRequest, $queryScheduleConferenceHeaders, new RuntimeOptions([]));
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

  queryScheduleConferenceHeaders := &dingtalkconference_1_0.QueryScheduleConferenceHeaders{}
  queryScheduleConferenceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryScheduleConferenceRequest := &dingtalkconference_1_0.QueryScheduleConferenceRequest{
    RequestUnionId: tea.String("qzR1iSMDvzR9iP7Pxxxxxxxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryScheduleConferenceWithOptions(tea.String("2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx"), queryScheduleConferenceRequest, queryScheduleConferenceHeaders, &util.RuntimeOptions{})
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
    let queryScheduleConferenceHeaders = new $dingtalkconference_1_0.QueryScheduleConferenceHeaders({ });
    queryScheduleConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryScheduleConferenceRequest = new $dingtalkconference_1_0.QueryScheduleConferenceRequest({
      requestUnionId: "qzR1iSMDvzR9iP7Pxxxxxxxxxxxx",
    });
    try {
      await client.queryScheduleConferenceWithOptions("2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx", queryScheduleConferenceRequest, queryScheduleConferenceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConferenceHeaders queryScheduleConferenceHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConferenceHeaders();
            queryScheduleConferenceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConferenceRequest queryScheduleConferenceRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConferenceRequest
            {
                RequestUnionId = "qzR1iSMDvzR9iP7Pxxxxxxxxxxxx",
            };
            try
            {
                client.QueryScheduleConferenceWithOptions("2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx", queryScheduleConferenceRequest, queryScheduleConferenceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求id。 |
| scheduleConferenceId | String | 预约会议id。 |
| title | String | 预约会议标题。 |
| startTime | Long | 预约会议开始时间，毫秒级UTC时间戳。 |
| endTime | Long | 预约会议结束时间，毫秒级UTC时间戳。 |
| roomCode | String | 会议号。 |
| url | String | 预约会议分享链接。 |
| phones | Array of String | 呼入电话号码。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "xxxxx",
  "scheduleConferenceId" : "2a489c68-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "title" : "预约会议标题",
  "startTime" : 1687924800000,
  "endTime" : 1687928400000,
  "roomCode" : "838 722 xxxxx",
  "url" : "https://meeting.dingtalk.com/j/Bsbp3ixxxxxUyJJ9",
  "phones" : [ "+86123xxxx" ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramsError | error:%s | 参数错误 |
| 400 | permissionError | permissionError:%s | 无权操作该会议 |
| 400 | resourceCancel | Schedule conference has canceled | 预约会议已被取消 |
| 500 | systemError | systemError:%s | 系统错误 |
