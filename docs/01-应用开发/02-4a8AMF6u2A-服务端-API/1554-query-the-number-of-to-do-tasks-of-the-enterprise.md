---
title: "查询企业个人待办数量"
source_url: "https://open.dingtalk.com/document/development/query-the-number-of-to-do-tasks-of-the-enterprise"
namespace: "development"
slug: "query-the-number-of-to-do-tasks-of-the-enterprise"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 待办任务 > 查询企业个人待办数量"
doc_id: "ennnUHKfaN"
updated_at: "2026-08-25 09:38:12"
---

> Source: https://open.dingtalk.com/document/development/query-the-number-of-to-do-tasks-of-the-enterprise
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 待办任务 > 查询企业个人待办数量
> Updated: 2026-08-25 09:38:12

# 查询企业个人待办数量

调用本接口查询企业个人待办数量。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[查询企业下用户待办列表](0798-query-the-to-do-list-of-enterprise-users.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 请求方法

```
GET /v1.0/workrecord/counts?userId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 要查询的用户的userid。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| undoCount | Long | 指定用户的审批待办任务数量。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/workrecord/counts?userId=a123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkworkrecord_1_0.*;
import com.aliyun.dingtalkworkrecord_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkworkrecord_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkrecord_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkrecord_1_0.Client client = Sample.createClient();
        CountWorkRecordHeaders countWorkRecordHeaders = new CountWorkRecordHeaders();
        countWorkRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CountWorkRecordRequest countWorkRecordRequest = new CountWorkRecordRequest()
                .setUserId("a123");
        try {
            client.countWorkRecordWithOptions(countWorkRecordRequest, countWorkRecordHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.workrecord_1_0.client import Client as dingtalkworkrecord_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workrecord_1_0 import models as dingtalkworkrecord__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkrecord_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkrecord_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        count_work_record_headers = dingtalkworkrecord__1__0_models.CountWorkRecordHeaders()
        count_work_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        count_work_record_request = dingtalkworkrecord__1__0_models.CountWorkRecordRequest(
            user_id='a123'
        )
        try:
            client.count_work_record_with_options(count_work_record_request, count_work_record_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        count_work_record_headers = dingtalkworkrecord__1__0_models.CountWorkRecordHeaders()
        count_work_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        count_work_record_request = dingtalkworkrecord__1__0_models.CountWorkRecordRequest(
            user_id='a123'
        )
        try:
            await client.count_work_record_with_options_async(count_work_record_request, count_work_record_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkrecord_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkrecord_1_0\Models\CountWorkRecordHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkrecord_1_0\Models\CountWorkRecordRequest;
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
        $countWorkRecordHeaders = new CountWorkRecordHeaders([]);
        $countWorkRecordHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $countWorkRecordRequest = new CountWorkRecordRequest([
            "userId" => "a123"
        ]);
        try {
            $client->countWorkRecordWithOptions($countWorkRecordRequest, $countWorkRecordHeaders, new RuntimeOptions([]));
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
  dingtalkworkrecord_1_0  "github.com/alibabacloud-go/dingtalk/workrecord_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkworkrecord_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkrecord_1_0.Client{}
  _result, _err = dingtalkworkrecord_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  countWorkRecordHeaders := &dingtalkworkrecord_1_0.CountWorkRecordHeaders{}
  countWorkRecordHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  countWorkRecordRequest := &dingtalkworkrecord_1_0.CountWorkRecordRequest{
    UserId: tea.String("a123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CountWorkRecordWithOptions(countWorkRecordRequest, countWorkRecordHeaders, &util.RuntimeOptions{})
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
import dingtalkworkrecord_1_0, * as $dingtalkworkrecord_1_0 from '@alicloud/dingtalk/workrecord_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkrecord_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkrecord_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let countWorkRecordHeaders = new $dingtalkworkrecord_1_0.CountWorkRecordHeaders({ });
    countWorkRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let countWorkRecordRequest = new $dingtalkworkrecord_1_0.CountWorkRecordRequest({
      userId: "a123",
    });
    try {
      await client.countWorkRecordWithOptions(countWorkRecordRequest, countWorkRecordHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

Client.main(process.argv.slice(2));
```

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkworkrecord__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkworkrecord_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkworkrecord_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkworkrecord_1_0::Client> client = make_shared<Alibabacloud_Dingtalkworkrecord_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkworkrecord_1_0::CountWorkRecordHeaders> countWorkRecordHeaders = make_shared<Alibabacloud_Dingtalkworkrecord_1_0::CountWorkRecordHeaders>();
  countWorkRecordHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkworkrecord_1_0::CountWorkRecordRequest> countWorkRecordRequest = make_shared<Alibabacloud_Dingtalkworkrecord_1_0::CountWorkRecordRequest>(map<string, boost::any>({
    {"userId", boost::any(string("a123"))}
  }));
  try {
    client->countWorkRecordWithOptions(countWorkRecordRequest, countWorkRecordHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "undoCount" : 10
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 503 | unknownError | 未知错误 | 未知错误 |
