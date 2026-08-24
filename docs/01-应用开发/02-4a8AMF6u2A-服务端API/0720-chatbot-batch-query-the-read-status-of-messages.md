---
title: "批量查询人与机器人会话机器人消息是否已读"
source_url: "https://open.dingtalk.com/document/development/chatbot-batch-query-the-read-status-of-messages"
namespace: "development"
slug: "chatbot-batch-query-the-read-status-of-messages"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 消息查询 > 批量查询人与机器人会话机器人消息是否已读"
doc_id: "krEOXw2dkH"
updated_at: "2026-06-05 13:41:56"
---

> Source: https://open.dingtalk.com/document/development/chatbot-batch-query-the-read-status-of-messages
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 消息查询 > 批量查询人与机器人会话机器人消息是否已读
> Updated: 2026-06-05 13:41:56

# 批量查询人与机器人会话机器人消息是否已读

调用本接口，批量查询人与机器人会话时，机器人消息是否已读，适用于企业内部沟通中24小时内需要确认消息是否被阅读的场景。

## **接口调用说明**

- 一次最多可以查询一条单聊信息20名接收者的消息是否已读数据。
- 若直接发起http请求，需要先对processQueryKey参数进行URLEncoding转义，然后再将转义后的processQueryKey拼入URL中。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/oToMessages/readStatus |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_robot\_sendmsg-企业内机器人发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| robotCode | String | 是 | 机器人的编码，详情参考[机器人 ID](0698-development-robot-overview.md#447ec33014hrl)。 |
| processQueryKey | String | 是 | 消息唯一标识，可通过[批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口返回参数中`processQueryKey`字段获取。    在发送消息24小时内可以通过processQueryKey查询消息已读状态，超过24小时则无法查询。 |

### 请求示例

HTTP

```
GET /v1.0/robot/oToMessages/readStatus?robotCode=dingzxcifuvdfbvegdf&processQueryKey=xxxxxxxxxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkrobot_1_0.*;
import com.aliyun.dingtalkrobot_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkrobot_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrobot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrobot_1_0.Client client = Sample.createClient();
        BatchOTOQueryHeaders batchOTOQueryHeaders = new BatchOTOQueryHeaders();
        batchOTOQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchOTOQueryRequest batchOTOQueryRequest = new BatchOTOQueryRequest()
                .setRobotCode("dingzxcifuvdfbvegdf")
                .setProcessQueryKey("xxxxxxxxxxxxx");
        try {
            client.batchOTOQueryWithOptions(batchOTOQueryRequest, batchOTOQueryHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrobot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrobot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_otoquery_headers = dingtalkrobot__1__0_models.BatchOTOQueryHeaders()
        batch_otoquery_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_otoquery_request = dingtalkrobot__1__0_models.BatchOTOQueryRequest(
            robot_code='dingzxcifuvdfbvegdf',
            process_query_key='xxxxxxxxxxxxx'
        )
        try:
            client.batch_otoquery_with_options(batch_otoquery_request, batch_otoquery_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_otoquery_headers = dingtalkrobot__1__0_models.BatchOTOQueryHeaders()
        batch_otoquery_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_otoquery_request = dingtalkrobot__1__0_models.BatchOTOQueryRequest(
            robot_code='dingzxcifuvdfbvegdf',
            process_query_key='xxxxxxxxxxxxx'
        )
        try:
            await client.batch_otoquery_with_options_async(batch_otoquery_request, batch_otoquery_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchOTOQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchOTOQueryRequest;
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
        $batchOTOQueryHeaders = new BatchOTOQueryHeaders([]);
        $batchOTOQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchOTOQueryRequest = new BatchOTOQueryRequest([
            "robotCode" => "dingzxcifuvdfbvegdf",
            "processQueryKey" => "xxxxxxxxxxxxx"
        ]);
        try {
            $client->batchOTOQueryWithOptions($batchOTOQueryRequest, $batchOTOQueryHeaders, new RuntimeOptions([]));
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
  dingtalkrobot_1_0  "github.com/alibabacloud-go/dingtalk/robot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrobot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrobot_1_0.Client{}
  _result, _err = dingtalkrobot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchOTOQueryHeaders := &dingtalkrobot_1_0.BatchOTOQueryHeaders{}
  batchOTOQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchOTOQueryRequest := &dingtalkrobot_1_0.BatchOTOQueryRequest{
    RobotCode: tea.String("dingzxcifuvdfbvegdf"),
    ProcessQueryKey: tea.String("xxxxxxxxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchOTOQueryWithOptions(batchOTOQueryRequest, batchOTOQueryHeaders, &util.RuntimeOptions{})
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
import dingtalkrobot_1_0, * as $dingtalkrobot_1_0 from '@alicloud/dingtalk/robot_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrobot_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrobot_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let batchOTOQueryHeaders = new $dingtalkrobot_1_0.BatchOTOQueryHeaders({ });
    batchOTOQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let batchOTOQueryRequest = new $dingtalkrobot_1_0.BatchOTOQueryRequest({
      robotCode: "dingzxcifuvdfbvegdf",
      processQueryKey: "xxxxxxxxxxxxx",
    });
    try {
      await client.batchOTOQueryWithOptions(batchOTOQueryRequest, batchOTOQueryHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrobot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrobot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchOTOQueryHeaders batchOTOQueryHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchOTOQueryHeaders();
            batchOTOQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchOTOQueryRequest batchOTOQueryRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchOTOQueryRequest
            {
                RobotCode = "dingzxcifuvdfbvegdf",
                ProcessQueryKey = "xxxxxxxxxxxxx",
            };
            try
            {
                client.BatchOTOQueryWithOptions(batchOTOQueryRequest, batchOTOQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkrobot__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkrobot_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkrobot_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::Client> client = make_shared<Alibabacloud_Dingtalkrobot_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::BatchOTOQueryHeaders> batchOTOQueryHeaders = make_shared<Alibabacloud_Dingtalkrobot_1_0::BatchOTOQueryHeaders>();
  batchOTOQueryHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::BatchOTOQueryRequest> batchOTOQueryRequest = make_shared<Alibabacloud_Dingtalkrobot_1_0::BatchOTOQueryRequest>(map<string, boost::any>({
    {"robotCode", boost::any(string("dingzxcifuvdfbvegdf"))},
    {"processQueryKey", boost::any(string("xxxxxxxxxxxxx"))}
  }));
  try {
    client->batchOTOQueryWithOptions(batchOTOQueryRequest, batchOTOQueryHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| sendStatus | String | 消息发送状态：   - **SUCCESS**：成功 - **RECALLED**：已撤回 - **PROCESSING**： 处理中 |
| messageReadInfoList | Array | 消息已读情况。 |
| name | String | 消息接收者名称。 |
| userId | String | 消息接收者的userId。 |
| readStatus | String | 已读状态：   - **READ**：已读 - **UNREAD**：未读 |
| readTimestamp | Long | 暂不支持。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "sendStatus" : "SUCESS",
  "messageReadInfoList" : [ {
    "name" : "曲大岳",
    "userId" : "201382020",
    "readStatus" : "READ"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.robotCode.empty | %s | 机器人robotCode无效 |
| 400 | invalidParameter.param.invalid | %s | 参数不合法，请检查参数是否为空 |
| 400 | invalidParameter.robotCode.notExsit | %s | 机器人不存在 |
| 400 | unknown.send.result | %s | 未知的发送结果 |
| 400 | invalidParameter.robotCode.missing | %s | 缺少robotCode |
| 400 | invalidParameter.processQueryKey.missing | %s | 缺少processQueryKey |
| 400 | invalidParameter.robotCode.invalid | %s | 机器人不存在，请检查企业内是否安装了robotCode对应的机器人 |
| 400 | invalid.processQueryKey | %s | 无效的processQueryKey，请检查processQueryKey是否正确 |
| 400 | template.not.existed | %s | 机器人模板不存在 |
| 400 | template.stopped | %s | 机器人模板已经停用 |
| 400 | processQueryKey.expireTime | %s | processQueryKey还未生成消息查询数据或已过期，无法查询消息 |
| 500 | system.error | %s | 系统繁忙，请稍后再试 |
