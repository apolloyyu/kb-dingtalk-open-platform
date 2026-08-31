---
title: "删除订阅日历"
source_url: "https://open.dingtalk.com/document/development/delete-subscription-calendar"
namespace: "development"
slug: "delete-subscription-calendar"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 日历 > 删除订阅日历"
doc_id: "3d4BGD1PNJ"
updated_at: "2026-06-02 09:25:10"
---

> Source: https://open.dingtalk.com/document/development/delete-subscription-calendar
> Path: 应用开发 / 服务端 API / 日程 > 日历 > 删除订阅日历
> Updated: 2026-06-02 09:25:10

# 删除订阅日历

调用本接口，删除订阅日历。

## 接口调用说明

- 目前仅允许日历创建者删除日历，因此Path参数中的userId字段必须是日历创建者的unionId。
- 订阅日历被删除后，已订阅该日历的用户会自动解除订阅。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/subscribedCalendars/{calendarId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Calendar.Write-日历应用中日历写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 日历创建者的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 订阅日历id，可调用[创建订阅日历](0264-create-subscription-calendar.md)接口获取calendarId参数值。 |

### 请求示例

HTTP

```
DELETE /v1.0/calendar/users/iiiP35sJadba8aBSgjrwPRKgiEiF/subscribedCalendars/M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT01
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcalendar_1_0.*;
import com.aliyun.dingtalkcalendar_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcalendar_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcalendar_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcalendar_1_0.Client client = Sample.createClient();
        DeleteSubscribedCalendarHeaders deleteSubscribedCalendarHeaders = new DeleteSubscribedCalendarHeaders();
        deleteSubscribedCalendarHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.deleteSubscribedCalendarWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", deleteSubscribedCalendarHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.calendar_1_0.client import Client as dingtalkcalendar_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.calendar_1_0 import models as dingtalkcalendar__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcalendar_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcalendar_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_subscribed_calendar_headers = dingtalkcalendar__1__0_models.DeleteSubscribedCalendarHeaders()
        delete_subscribed_calendar_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.delete_subscribed_calendar_with_options('iiiP35sJadba8aBSgjrwPRKgiEiF', 'M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv', delete_subscribed_calendar_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_subscribed_calendar_headers = dingtalkcalendar__1__0_models.DeleteSubscribedCalendarHeaders()
        delete_subscribed_calendar_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.delete_subscribed_calendar_with_options_async('iiiP35sJadba8aBSgjrwPRKgiEiF', 'M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv', delete_subscribed_calendar_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\DeleteSubscribedCalendarHeaders;
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
        $deleteSubscribedCalendarHeaders = new DeleteSubscribedCalendarHeaders([]);
        $deleteSubscribedCalendarHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->deleteSubscribedCalendarWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", $deleteSubscribedCalendarHeaders, new RuntimeOptions([]));
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
  dingtalkcalendar_1_0  "github.com/alibabacloud-go/dingtalk/calendar_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcalendar_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcalendar_1_0.Client{}
  _result, _err = dingtalkcalendar_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteSubscribedCalendarHeaders := &dingtalkcalendar_1_0.DeleteSubscribedCalendarHeaders{}
  deleteSubscribedCalendarHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteSubscribedCalendarWithOptions(tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF"), tea.String("M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv"), deleteSubscribedCalendarHeaders, &util.RuntimeOptions{})
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
import dingtalkcalendar_1_0, * as $dingtalkcalendar_1_0 from '@alicloud/dingtalk/calendar_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcalendar_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcalendar_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let deleteSubscribedCalendarHeaders = new $dingtalkcalendar_1_0.DeleteSubscribedCalendarHeaders({ });
    deleteSubscribedCalendarHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.deleteSubscribedCalendarWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", deleteSubscribedCalendarHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.DeleteSubscribedCalendarHeaders deleteSubscribedCalendarHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.DeleteSubscribedCalendarHeaders();
            deleteSubscribedCalendarHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.DeleteSubscribedCalendarWithOptions("iiiP35sJadba8aBSgjrwPRKgiEiF", "M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", deleteSubscribedCalendarHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 接口是否调用成功。true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | calendarId cannot be blank | 日历id不能为空 |
| 403 | permissionDenied | permission denied | 鉴权失败 |
