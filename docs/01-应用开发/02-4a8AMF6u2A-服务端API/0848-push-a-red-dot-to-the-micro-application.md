---
title: "专属小红点推送"
source_url: "https://open.dingtalk.com/document/development/push-a-red-dot-to-the-micro-application"
namespace: "development"
slug: "push-a-red-dot-to-the-micro-application"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 专属小红点推送"
doc_id: "Cqas9klo5d"
updated_at: "2026-06-04 19:10:01"
---

> Source: https://open.dingtalk.com/document/development/push-a-red-dot-to-the-micro-application
> Path: 应用开发 / 服务端API / 专属钉钉 > 专属小红点推送
> Updated: 2026-06-04 19:10:01

# 专属小红点推送

调用本接口，给企业自建或第三方企业应用推送在快捷栏上显示的小红点信息。

## 接口调用说明

仅限购买了**开放&集成包**的专属钉钉企业进行使用，如需购买，请联系钉钉小二咨询，使用前你可以登录[**钉钉管理后台**](https://oa.dingtalk.com/#/welcome) > **钉钉专属版** > **开放&运维** > **能力开放** > **推送小红点**进行配置。 ![](https://down-cdn.dingtalk.com/ddmedia/iwElAqNwbmcDBgTRB2oF0QLGBrAKg0X-H_CgFQWiegjMpQoAB9MAAAAA-hsdTwgACapvcGVuLnRvb2xzCgAL0gAKTA8.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/exclusiveDesigns/redPoints/push |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Design.ReadWrite-专属钉钉专属设计读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证：   - 企业内部应用可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| badgeItems | Array | 否 | 推送列表，建议不超过100。 |
| userId | String | 否 | 员工userId。 |
| pushValue | String | 否 | 推送的内容（目前仅限数字）。   - 当该参数值为"0"时，表示移除对应的小红点推送。 |
| agentId | String | 是 | 微应用agentId，请参考[基础概念-AgentId](https://open.dingtalk.com/document/orgapp/basic-concepts-beta#813cbd7067yn0)。 |
| pushType | String | 是 | 推送类型取值：   - Number：pushValue值为数字 |
| version | Long | 否 | 推送版本字段，必须为调用时生成的毫秒时间戳（如 1737299280123）。 1. 传非时间戳值（短数字、长数字）将引发故障。一旦发生，概不负责。 2. 不传则服务端用接收时刻时间戳补全，低并发下不会有影响。 3. 为什么需要这个字段？因网络不可靠，“先发”未必“先到”，只有发出时刻的时间戳能真实反映业务意图顺序。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/exclusiveDesigns/redPoints/push HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "badgeItems" : [ {
    "userId" : "12345",
    "pushValue" : "1"
  } ],
  "agentId" : "110000000",
  "pushType" : "Number"
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.PushBadgeHeaders pushBadgeHeaders = new com.aliyun.dingtalkexclusive_1_0.models.PushBadgeHeaders();
        pushBadgeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.PushBadgeRequest.PushBadgeRequestBadgeItems badgeItems0 = new com.aliyun.dingtalkexclusive_1_0.models.PushBadgeRequest.PushBadgeRequestBadgeItems()
                .setUserId("12345")
                .setPushValue("1");
        com.aliyun.dingtalkexclusive_1_0.models.PushBadgeRequest pushBadgeRequest = new com.aliyun.dingtalkexclusive_1_0.models.PushBadgeRequest()
                .setBadgeItems(java.util.Arrays.asList(
                    badgeItems0
                ))
                .setAgentId("110000000")
                .setPushType("Number");
        try {
            client.pushBadgeWithOptions(pushBadgeRequest, pushBadgeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        push_badge_headers = dingtalkexclusive__1__0_models.PushBadgeHeaders()
        push_badge_headers.x_acs_dingtalk_access_token = '<your access token>'
        badge_items_0 = dingtalkexclusive__1__0_models.PushBadgeRequestBadgeItems(
            user_id='12345',
            push_value='1'
        )
        push_badge_request = dingtalkexclusive__1__0_models.PushBadgeRequest(
            badge_items=[
                badge_items_0
            ],
            agent_id='110000000',
            push_type='Number'
        )
        try:
            client.push_badge_with_options(push_badge_request, push_badge_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        push_badge_headers = dingtalkexclusive__1__0_models.PushBadgeHeaders()
        push_badge_headers.x_acs_dingtalk_access_token = '<your access token>'
        badge_items_0 = dingtalkexclusive__1__0_models.PushBadgeRequestBadgeItems(
            user_id='12345',
            push_value='1'
        )
        push_badge_request = dingtalkexclusive__1__0_models.PushBadgeRequest(
            badge_items=[
                badge_items_0
            ],
            agent_id='110000000',
            push_type='Number'
        )
        try:
            await client.push_badge_with_options_async(push_badge_request, push_badge_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\PushBadgeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\PushBadgeRequest\badgeItems;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\PushBadgeRequest;
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
        $pushBadgeHeaders = new PushBadgeHeaders([]);
        $pushBadgeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $badgeItems0 = new badgeItems([
            "userId" => "12345",
            "pushValue" => "1"
        ]);
        $pushBadgeRequest = new PushBadgeRequest([
            "badgeItems" => [
                $badgeItems0
            ],
            "agentId" => "110000000",
            "pushType" => "Number"
        ]);
        try {
            $client->pushBadgeWithOptions($pushBadgeRequest, $pushBadgeHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  pushBadgeHeaders := &dingtalkexclusive_1_0.PushBadgeHeaders{}
  pushBadgeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  badgeItems0 := &dingtalkexclusive_1_0.PushBadgeRequestBadgeItems{
    UserId: tea.String("12345"),
    PushValue: tea.String("1"),
  }
  pushBadgeRequest := &dingtalkexclusive_1_0.PushBadgeRequest{
    BadgeItems: []*dingtalkexclusive_1_0.PushBadgeRequestBadgeItems{badgeItems0},
    AgentId: tea.String("110000000"),
    PushType: tea.String("Number"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PushBadgeWithOptions(pushBadgeRequest, pushBadgeHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let pushBadgeHeaders = new $dingtalkexclusive_1_0.PushBadgeHeaders({ });
    pushBadgeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let badgeItems0 = new $dingtalkexclusive_1_0.PushBadgeRequestBadgeItems({
      userId: "12345",
      pushValue: "1",
    });
    let pushBadgeRequest = new $dingtalkexclusive_1_0.PushBadgeRequest({
      badgeItems: [
        badgeItems0
      ],
      agentId: "110000000",
      pushType: "Number",
    });
    try {
      await client.pushBadgeWithOptions(pushBadgeRequest, pushBadgeHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeHeaders pushBadgeHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeHeaders();
            pushBadgeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeRequest.PushBadgeRequestBadgeItems badgeItems0 = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeRequest.PushBadgeRequestBadgeItems
            {
                UserId = "12345",
                PushValue = "1",
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeRequest pushBadgeRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeRequest
            {
                BadgeItems = new List<AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.PushBadgeRequest.PushBadgeRequestBadgeItems>
                {
                    badgeItems0
                },
                AgentId = "110000000",
                PushType = "Number",
            };
            try
            {
                client.PushBadgeWithOptions(pushBadgeRequest, pushBadgeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 推送是否成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | param.illegal | 参数错误:%s | 参数错误，包含agentId、pushType、userIdList、pushValue |
| 500 | not.have.permission | 当前组织没有红点推送权限 | 当前组织没有红点推送权限 |
| 500 | system.error | 系统错误 | 内部服务发生的异常情况 |
| 500 | agent.not.allow | 未授权该微应用红点推送权限 | 未授权该微应用红点推送权限 |
