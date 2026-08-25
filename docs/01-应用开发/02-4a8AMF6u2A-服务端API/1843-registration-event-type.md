---
title: "批量注册事件类型"
source_url: "https://open.dingtalk.com/document/development/registration-event-type"
namespace: "development"
slug: "registration-event-type"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉物联 > 批量注册事件类型"
doc_id: "xJOBw2bxDm"
updated_at: "2025-09-08 19:06:09"
---

> Source: https://open.dingtalk.com/document/development/registration-event-type
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉物联 > 批量注册事件类型
> Updated: 2025-09-08 19:06:09

# 批量注册事件类型

调用本接口将所有事件类型注册到钉钉物联应用。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，钉钉物联接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 钉钉物联接口相关文档，已于2023年01月02日迁移至历史文档（不推荐）目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

每个组织最多添加500个事件类型。

![](https://img.alicdn.com/imgextra/i2/O1CN01CHNSWP1hzQrGqShUr_!!6000000004348-2-tps-1090-681.png)

> **[!NOTE]**
>
> 调用本接口，需要开通钉钉物联应用，请参考[如何接入钉钉物联接口能力](https://open.dingtalk.com/document/orgapp/ding-iot-overview)。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 暂不支持 | — | — |

## 请求方法

```
POST /v1.0/diot/eventTypes/registrations/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "corpId" : "String",
  "eventTypes" : [ {
    "eventType" : "String",
    "eventTypeName" : "String"
  } ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 否 | 钉钉物联组织ID， 服务商必填。 |
| eventTypes | Array | 是 | 事件类型列表。 |
| eventType | String | 是 | 事件类型，自定义，最长20个字符。 |
| eventTypeName | String | 是 | 事件类型名称，自定义，长度4-20个字符。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| eventTypes | Array of String | 注册成功的事件类型。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/diot/eventTypes/registrations/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:98b4f244xxx
Content-Type:application/json

{
  "corpId" : "ding12345",
  "eventTypes" : [ {
    "eventType" : "fireDetect",
    "eventTypeName" : "火焰告警"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdiot_1_0.*;
import com.aliyun.dingtalkdiot_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdiot_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdiot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdiot_1_0.Client client = Sample.createClient();
        BatchRegisterEventTypeHeaders batchRegisterEventTypeHeaders = new BatchRegisterEventTypeHeaders();
        batchRegisterEventTypeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchRegisterEventTypeRequest.BatchRegisterEventTypeRequestEventTypes eventTypes0 = new BatchRegisterEventTypeRequest.BatchRegisterEventTypeRequestEventTypes()
                .setEventType("fireDetect")
                .setEventTypeName("火焰告警");
        BatchRegisterEventTypeRequest batchRegisterEventTypeRequest = new BatchRegisterEventTypeRequest()
                .setCorpId("ding12345")
                .setEventTypes(java.util.Arrays.asList(
                    eventTypes0
                ));
        try {
            client.batchRegisterEventTypeWithOptions(batchRegisterEventTypeRequest, batchRegisterEventTypeHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.diot_1_0.client import Client as dingtalkdiot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.diot_1_0 import models as dingtalkdiot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdiot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdiot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_register_event_type_headers = dingtalkdiot__1__0_models.BatchRegisterEventTypeHeaders()
        batch_register_event_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        event_types_0 = dingtalkdiot__1__0_models.BatchRegisterEventTypeRequestEventTypes(
            event_type='fireDetect',
            event_type_name='火焰告警'
        )
        batch_register_event_type_request = dingtalkdiot__1__0_models.BatchRegisterEventTypeRequest(
            corp_id='ding12345',
            event_types=[
                event_types_0
            ]
        )
        try:
            client.batch_register_event_type_with_options(batch_register_event_type_request, batch_register_event_type_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_register_event_type_headers = dingtalkdiot__1__0_models.BatchRegisterEventTypeHeaders()
        batch_register_event_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        event_types_0 = dingtalkdiot__1__0_models.BatchRegisterEventTypeRequestEventTypes(
            event_type='fireDetect',
            event_type_name='火焰告警'
        )
        batch_register_event_type_request = dingtalkdiot__1__0_models.BatchRegisterEventTypeRequest(
            corp_id='ding12345',
            event_types=[
                event_types_0
            ]
        )
        try:
            await client.batch_register_event_type_with_options_async(batch_register_event_type_request, batch_register_event_type_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterEventTypeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterEventTypeRequest\eventTypes;
use AlibabaCloud\SDK\Dingtalk\Vdiot_1_0\Models\BatchRegisterEventTypeRequest;
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
        $batchRegisterEventTypeHeaders = new BatchRegisterEventTypeHeaders([]);
        $batchRegisterEventTypeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $eventTypes0 = new eventTypes([
            "eventType" => "fireDetect",
            "eventTypeName" => "火焰告警"
        ]);
        $batchRegisterEventTypeRequest = new BatchRegisterEventTypeRequest([
            "corpId" => "ding12345",
            "eventTypes" => [
                $eventTypes0
            ]
        ]);
        try {
            $client->batchRegisterEventTypeWithOptions($batchRegisterEventTypeRequest, $batchRegisterEventTypeHeaders, new RuntimeOptions([]));
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
  dingtalkdiot_1_0  "github.com/alibabacloud-go/dingtalk/diot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdiot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdiot_1_0.Client{}
  _result, _err = dingtalkdiot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchRegisterEventTypeHeaders := &dingtalkdiot_1_0.BatchRegisterEventTypeHeaders{}
  batchRegisterEventTypeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  eventTypes0 := &dingtalkdiot_1_0.BatchRegisterEventTypeRequestEventTypes{
    EventType: tea.String("fireDetect"),
    EventTypeName: tea.String("火焰告警"),
  }
  batchRegisterEventTypeRequest := &dingtalkdiot_1_0.BatchRegisterEventTypeRequest{
    CorpId: tea.String("ding12345"),
    EventTypes: []*dingtalkdiot_1_0.BatchRegisterEventTypeRequestEventTypes{eventTypes0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchRegisterEventTypeWithOptions(batchRegisterEventTypeRequest, batchRegisterEventTypeHeaders, &util.RuntimeOptions{})
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
        public static AlibabaCloud.SDK.Dingtalkdiot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdiot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeHeaders batchRegisterEventTypeHeaders = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeHeaders();
            batchRegisterEventTypeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeRequest.BatchRegisterEventTypeRequestEventTypes eventTypes0 = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeRequest.BatchRegisterEventTypeRequestEventTypes
            {
                EventType = "fireDetect",
                EventTypeName = "火焰告警",
            };
            AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeRequest batchRegisterEventTypeRequest = new AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeRequest
            {
                CorpId = "ding12345",
                EventTypes = new List<AlibabaCloud.SDK.Dingtalkdiot_1_0.Models.BatchRegisterEventTypeRequest.BatchRegisterEventTypeRequestEventTypes>
                {
                    eventTypes0
                },
            };
            try
            {
                client.BatchRegisterEventTypeWithOptions(batchRegisterEventTypeRequest, batchRegisterEventTypeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdiot__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdiot_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdiot_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdiot_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeHeaders> batchRegisterEventTypeHeaders = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeHeaders>();
  batchRegisterEventTypeHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeRequestEventTypes> eventTypes0 = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeRequestEventTypes>(map<string, boost::any>({
    {"eventType", boost::any(string("fireDetect"))},
    {"eventTypeName", boost::any(string("火焰告警"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeRequest> batchRegisterEventTypeRequest = make_shared<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding12345"))},
    {"eventTypes", boost::any(vector<Alibabacloud_Dingtalkdiot_1_0::BatchRegisterEventTypeRequestEventTypes>({
      eventTypes0
    }))}
  }));
  try {
    client->batchRegisterEventTypeWithOptions(batchRegisterEventTypeRequest, batchRegisterEventTypeHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "eventTypes" : [ "fireDetect" ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 401 | system.not.exist | 系统未注册 | 系统未在钉钉物联平台注册 |
| 401 | corp.not.bind | 组织未绑定 | 钉钉组织未绑定该系统 |
| 500 | system.error | 系统异常 | 系统异常 |
| 500 | crop.not.install | 企业未安装钉钉物联应用，请联系我们(https://open.dingtalk.com/document/orgapp-server/dingtalk-iot-overview) | 企业未安装钉钉物联应用 |
