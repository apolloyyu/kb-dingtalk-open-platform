---
title: "停止视频会议云录制"
source_url: "https://open.dingtalk.com/document/development/video-conferencing-stops-cloud-recording"
namespace: "development"
slug: "video-conferencing-stops-cloud-recording"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 停止视频会议云录制"
doc_id: "8zJaLtj0Ih"
updated_at: "2026-06-02 09:10:48"
---

> Source: https://open.dingtalk.com/document/development/video-conferencing-stops-cloud-recording
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 停止视频会议云录制
> Updated: 2026-06-02 09:10:48

# 停止视频会议云录制

调用本接口停止视频会议云录制，视频会议正常进行，不会被结束。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/cloudRecords/stop |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conferenceId | String | 是 | 会议ID，可调用[创建视频会议](0399-create-a-video-conference.md)接口获取conferenceId参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。    只有当用户是会议主持人时，才有权限关闭云录制。 |

### 请求示例

HTTP

```
POST /v1.0/conference/videoConferences/61289fxxx/cloudRecords/stop HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d27c05xxx
Content-Type:application/json

{
  "unionId" : "WFBkgxxx"
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
        StopCloudRecordHeaders stopCloudRecordHeaders = new StopCloudRecordHeaders();
        stopCloudRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
        StopCloudRecordRequest stopCloudRecordRequest = new StopCloudRecordRequest()
                .setUnionId("WFBkgxxx");
        try {
            client.stopCloudRecordWithOptions("61289fxxx", stopCloudRecordRequest, stopCloudRecordHeaders, new RuntimeOptions());
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
        stop_cloud_record_headers = dingtalkconference__1__0_models.StopCloudRecordHeaders()
        stop_cloud_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        stop_cloud_record_request = dingtalkconference__1__0_models.StopCloudRecordRequest(
            union_id='WFBkgxxx'
        )
        try:
            client.stop_cloud_record_with_options('61289fxxx', stop_cloud_record_request, stop_cloud_record_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        stop_cloud_record_headers = dingtalkconference__1__0_models.StopCloudRecordHeaders()
        stop_cloud_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        stop_cloud_record_request = dingtalkconference__1__0_models.StopCloudRecordRequest(
            union_id='WFBkgxxx'
        )
        try:
            await client.stop_cloud_record_with_options_async('61289fxxx', stop_cloud_record_request, stop_cloud_record_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\StopCloudRecordHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\StopCloudRecordRequest;
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
        $stopCloudRecordHeaders = new StopCloudRecordHeaders([]);
        $stopCloudRecordHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $stopCloudRecordRequest = new StopCloudRecordRequest([
            "unionId" => "WFBkgxxx"
        ]);
        try {
            $client->stopCloudRecordWithOptions("61289fxxx", $stopCloudRecordRequest, $stopCloudRecordHeaders, new RuntimeOptions([]));
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

  stopCloudRecordHeaders := &dingtalkconference_1_0.StopCloudRecordHeaders{}
  stopCloudRecordHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  stopCloudRecordRequest := &dingtalkconference_1_0.StopCloudRecordRequest{
    UnionId: tea.String("WFBkgxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.StopCloudRecordWithOptions(tea.String("61289fxxx"), stopCloudRecordRequest, stopCloudRecordHeaders, &util.RuntimeOptions{})
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
    let stopCloudRecordHeaders = new $dingtalkconference_1_0.StopCloudRecordHeaders({ });
    stopCloudRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let stopCloudRecordRequest = new $dingtalkconference_1_0.StopCloudRecordRequest({
      unionId: "WFBkgxxx",
    });
    try {
      await client.stopCloudRecordWithOptions("61289fxxx", stopCloudRecordRequest, stopCloudRecordHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StopCloudRecordHeaders stopCloudRecordHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StopCloudRecordHeaders();
            stopCloudRecordHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StopCloudRecordRequest stopCloudRecordRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.StopCloudRecordRequest
            {
                UnionId = "WFBkgxxx",
            };
            try
            {
                client.StopCloudRecordWithOptions("61289fxxx", stopCloudRecordRequest, stopCloudRecordHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::StopCloudRecordHeaders> stopCloudRecordHeaders = make_shared<Alibabacloud_Dingtalkconference_1_0::StopCloudRecordHeaders>();
  stopCloudRecordHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkconference_1_0::StopCloudRecordRequest> stopCloudRecordRequest = make_shared<Alibabacloud_Dingtalkconference_1_0::StopCloudRecordRequest>(map<string, boost::any>({
    {"unionId", boost::any(string("WFBkgxxx"))}
  }));
  try {
    client->stopCloudRecordWithOptions(make_shared<string>("61289fxxx"), stopCloudRecordRequest, stopCloudRecordHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| code | String | 返回码。    如果视频会议云录制关闭成功，且接口调用成功，该字段值为200。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : "200"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | recordStopPermissionError | you can't operator, please contact meeting manager | 录制因权限问题停止失败 |
| 400 | roomClosed | the meeting has ended | 房间已关闭 |
| 400 | recordStopError | record stop error, please try again | 录制停止失败 |
| 500 | systemError | system error | 系统错误 |
| 500 | innerSystemError | The system is busy, please try again later | 服务端内部错误 |
