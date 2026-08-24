---
title: "批量撤回人与机器人会话中机器人消息"
source_url: "https://open.dingtalk.com/document/development/batch-message-recall-chat"
namespace: "development"
slug: "batch-message-recall-chat"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 消息撤回 > 批量撤回人与机器人会话中机器人消息"
doc_id: "zoPZB7T5hD"
updated_at: "2026-06-05 13:49:03"
---

> Source: https://open.dingtalk.com/document/development/batch-message-recall-chat
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 消息撤回 > 批量撤回人与机器人会话中机器人消息
> Updated: 2026-06-05 13:49:03

# 批量撤回人与机器人会话中机器人消息

用于批量撤回人与机器人会话中机器人消息。调用时通过 POST 请求提交 robotCode、processQueryKeys 等业务字段。本接口适用于企业24小时内撤回错误发送的通知消息等场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/otoMessages/batchRecall |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_robot\_sendmsg-企业内机器人发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| robotCode | String | 是 | 机器人的编码，详情参考[机器人 ID](0698-development-robot-overview.md#447ec33014hrl)。  需要与[机器人发送群聊消息](0716-the-robot-sends-a-group-message.md)接口时使用的robotCode一致。 |
| processQueryKeys | Array of String | 是 | 消息唯一标识列表，可通过[批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口获取。    - 每次最多传20个。 - 在发送消息24小时内可以通过processQueryKey撤回消息，超过24小时则无法撤回消息。 |

### 请求示例

HTTP

```
POST /v1.0/robot/otoMessages/batchRecall HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:8ca04016xxx
Content-Type:application/json

{
  "robotCode" : "dingXXXXXX",
  "processQueryKeys" : [ "b5fe1xxx" ]
}
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
        BatchRecallOTOHeaders batchRecallOTOHeaders = new BatchRecallOTOHeaders();
        batchRecallOTOHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchRecallOTORequest batchRecallOTORequest = new BatchRecallOTORequest()
                .setRobotCode("dingXXXXXX")
                .setProcessQueryKeys(java.util.Arrays.asList(
                    "b5fe1xxx"
                ));
        try {
            client.batchRecallOTOWithOptions(batchRecallOTORequest, batchRecallOTOHeaders, new RuntimeOptions());
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
        batch_recall_otoheaders = dingtalkrobot__1__0_models.BatchRecallOTOHeaders()
        batch_recall_otoheaders.x_acs_dingtalk_access_token = '<your access token>'
        batch_recall_otorequest = dingtalkrobot__1__0_models.BatchRecallOTORequest(
            robot_code='dingXXXXXX',
            process_query_keys=[
                'b5fe1xxx'
            ]
        )
        try:
            client.batch_recall_otowith_options(batch_recall_otorequest, batch_recall_otoheaders, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_recall_otoheaders = dingtalkrobot__1__0_models.BatchRecallOTOHeaders()
        batch_recall_otoheaders.x_acs_dingtalk_access_token = '<your access token>'
        batch_recall_otorequest = dingtalkrobot__1__0_models.BatchRecallOTORequest(
            robot_code='dingXXXXXX',
            process_query_keys=[
                'b5fe1xxx'
            ]
        )
        try:
            await client.batch_recall_otowith_options_async(batch_recall_otorequest, batch_recall_otoheaders, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchRecallOTOHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\BatchRecallOTORequest;
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
        $batchRecallOTOHeaders = new BatchRecallOTOHeaders([]);
        $batchRecallOTOHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchRecallOTORequest = new BatchRecallOTORequest([
            "robotCode" => "dingXXXXXX",
            "processQueryKeys" => [
                "b5fe1xxx"
            ]
        ]);
        try {
            $client->batchRecallOTOWithOptions($batchRecallOTORequest, $batchRecallOTOHeaders, new RuntimeOptions([]));
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

  batchRecallOTOHeaders := &dingtalkrobot_1_0.BatchRecallOTOHeaders{}
  batchRecallOTOHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchRecallOTORequest := &dingtalkrobot_1_0.BatchRecallOTORequest{
    RobotCode: tea.String("dingXXXXXX"),
    ProcessQueryKeys: []*string{tea.String("b5fe1xxx")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchRecallOTOWithOptions(batchRecallOTORequest, batchRecallOTOHeaders, &util.RuntimeOptions{})
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
    let batchRecallOTOHeaders = new $dingtalkrobot_1_0.BatchRecallOTOHeaders({ });
    batchRecallOTOHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let batchRecallOTORequest = new $dingtalkrobot_1_0.BatchRecallOTORequest({
      robotCode: "dingXXXXXX",
      processQueryKeys: [
        "b5fe1xxx"
      ],
    });
    try {
      await client.batchRecallOTOWithOptions(batchRecallOTORequest, batchRecallOTOHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallOTOHeaders batchRecallOTOHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallOTOHeaders();
            batchRecallOTOHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallOTORequest batchRecallOTORequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.BatchRecallOTORequest
            {
                RobotCode = "dingXXXXXX",
                ProcessQueryKeys = new List<string>
                {
                    "b5fe1xxx"
                },
            };
            try
            {
                client.BatchRecallOTOWithOptions(batchRecallOTORequest, batchRecallOTOHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::BatchRecallOTOHeaders> batchRecallOTOHeaders = make_shared<Alibabacloud_Dingtalkrobot_1_0::BatchRecallOTOHeaders>();
  batchRecallOTOHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkrobot_1_0::BatchRecallOTORequest> batchRecallOTORequest = make_shared<Alibabacloud_Dingtalkrobot_1_0::BatchRecallOTORequest>(map<string, boost::any>({
    {"robotCode", boost::any(string("dingXXXXXX"))},
    {"processQueryKeys", boost::any(vector<string>({
      "b5fe1xxx"
    }))}
  }));
  try {
    client->batchRecallOTOWithOptions(batchRecallOTORequest, batchRecallOTOHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| successResult | Array of String | 撤回成功的消息发送任务ID列表。  **[!NOTE]**  撤回机器人发送的消息，在聊天框中没有提示。 |
| failedResult | Map<String, String> | 撤回失败的消息发送任务ID列表及对应的失败原因。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "successResult" : [ "b5fe1xxx" ],
  "failedResult" : { }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.robotCode | %s | 机器人不存在，请检查企业内是否安装了robotCode对应的机器人 |
| 400 | invalidParameter.processQueryKeys.overMax | %s | processQueryKeys超过数量上限20，请将processQueryKeys拆分成多个长度不超过20的数组，分批次调用此接口 |
| 400 | not.allowed.robotCode | %s | 待撤回的消息不是robotCode对应的机器人发出的，无权限撤回消息，请传入正确的robotCode |
| 400 | invalidParameter.param.invalid | %s | 参数不合法，请检查参数是否为空 |
| 400 | invalidParameter.processQueryKey.missing | %s | 缺少processQueryKey |
| 400 | invalid.processQueryKey | %s | 无效的processQueryKey，请检查processQueryKey是否正确 |
| 400 | robot.processQueryKey.expired | %s | processQueryKey已过期，无法撤回消息 |
| 400 | notRevoke.all.messages | %s | 消息未能全部撤回 |
| 500 | system.error | %s | 未知的系统错误 |
