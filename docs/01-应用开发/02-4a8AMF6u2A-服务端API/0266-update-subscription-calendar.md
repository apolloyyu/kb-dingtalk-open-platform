---
title: "更新订阅日历"
source_url: "https://open.dingtalk.com/document/development/update-subscription-calendar"
namespace: "development"
slug: "update-subscription-calendar"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 日历 > 更新订阅日历"
doc_id: "NfOmcJmgkd"
updated_at: "2026-06-02 09:25:10"
---

> Source: https://open.dingtalk.com/document/development/update-subscription-calendar
> Path: 应用开发 / 服务端API / 日程 > 日历 > 更新订阅日历
> Updated: 2026-06-02 09:25:10

# 更新订阅日历

调用本接口，更新单个订阅日历信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/subscribedCalendars/{calendarId} |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Calendar.Write-日历应用中日历写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| calendarId | String | 是 | 订阅日历id，可调用[创建订阅日历](0264-create-subscription-calendar.md)接口获取calendarId参数值。 |
| userId | String | 是 | 日历作者或共同编辑人的unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 否 | 订阅日历的标题。 |
| description | String | 否 | 订阅日历的描述。 |
| managers | Array of String | 否 | 日历共同编辑人的unionId列表。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| subscribeScope | Object | 否 | 日历的可订阅范围。 |
| unionIds | Array of String | 否 | 可订阅该日历的人员unionId。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| openConversationIds | Array of String | 否 | 可订阅该日历的群OpenConversationId列表。   - 企业内部应用，调用[获取群会话的OpenConversationId](0745-obtain-group-openconversationid.md)接口获取openConversationId参数值。 - 第三方企业应用，调用[创建群](1484-create-a-scene-group-v2.md)接口获取open\_conversation\_id参数值。        - 需要传该订阅日程创建者所在的群OpenConversationId。 - 第三方个人应用无需传此参数。 |
| corpIds | Array of String | 否 | 可订阅该日历的组织corpId列表。 登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/)，在首页下查看企业的corpId。      需要传该订阅日程创建者所在的组织corpId。 |

### 请求示例

HTTP

```
PUT /v1.0/calendar/users/iiiP35sJadba8aBSgjrwPRKgiEiF/subscribedCalendars/M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:cnNTbW1YbU9sL2p6aFJZdEgvdlQrQT01
Content-Type:application/json

{
  "name" : "中国传统日历",
  "description" : "中国传统日历",
  "managers" : [ "iiiP35sJadba8aBSgjrwPRKgiEiF" ],
  "subscribeScope" : {
    "unionIds" : [ "iiiP35sJadba8aBSgjrwPRKgiEiF" ],
    "openConversationIds" : [ "cidvrURjEqVe8xxxxxxx" ],
    "corpIds" : [ "dingz0xc7v89789asasdf" ]
  }
}
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
        UpdateSubscribedCalendarsHeaders updateSubscribedCalendarsHeaders = new UpdateSubscribedCalendarsHeaders();
        updateSubscribedCalendarsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateSubscribedCalendarsRequest.UpdateSubscribedCalendarsRequestSubscribeScope subscribeScope = new UpdateSubscribedCalendarsRequest.UpdateSubscribedCalendarsRequestSubscribeScope()
                .setUnionIds(java.util.Arrays.asList(
                    "iiiP35sJadba8aBSgjrwPRKgiEiF"
                ))
                .setOpenConversationIds(java.util.Arrays.asList(
                    "cidvrURjEqVe8xxxxxxx"
                ))
                .setCorpIds(java.util.Arrays.asList(
                    "dingz0xc7v89789asasdf"
                ));
        UpdateSubscribedCalendarsRequest updateSubscribedCalendarsRequest = new UpdateSubscribedCalendarsRequest()
                .setName("中国传统日历")
                .setDescription("中国传统日历")
                .setManagers(java.util.Arrays.asList(
                    "iiiP35sJadba8aBSgjrwPRKgiEiF"
                ))
                .setSubscribeScope(subscribeScope);
        try {
            client.updateSubscribedCalendarsWithOptions("M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", "iiiP35sJadba8aBSgjrwPRKgiEiF", updateSubscribedCalendarsRequest, updateSubscribedCalendarsHeaders, new RuntimeOptions());
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
        update_subscribed_calendars_headers = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsHeaders()
        update_subscribed_calendars_headers.x_acs_dingtalk_access_token = '<your access token>'
        subscribe_scope = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequestSubscribeScope(
            union_ids=[
                'iiiP35sJadba8aBSgjrwPRKgiEiF'
            ],
            open_conversation_ids=[
                'cidvrURjEqVe8xxxxxxx'
            ],
            corp_ids=[
                'dingz0xc7v89789asasdf'
            ]
        )
        update_subscribed_calendars_request = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequest(
            name='中国传统日历',
            description='中国传统日历',
            managers=[
                'iiiP35sJadba8aBSgjrwPRKgiEiF'
            ],
            subscribe_scope=subscribe_scope
        )
        try:
            client.update_subscribed_calendars_with_options('M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv', 'iiiP35sJadba8aBSgjrwPRKgiEiF', update_subscribed_calendars_request, update_subscribed_calendars_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_subscribed_calendars_headers = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsHeaders()
        update_subscribed_calendars_headers.x_acs_dingtalk_access_token = '<your access token>'
        subscribe_scope = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequestSubscribeScope(
            union_ids=[
                'iiiP35sJadba8aBSgjrwPRKgiEiF'
            ],
            open_conversation_ids=[
                'cidvrURjEqVe8xxxxxxx'
            ],
            corp_ids=[
                'dingz0xc7v89789asasdf'
            ]
        )
        update_subscribed_calendars_request = dingtalkcalendar__1__0_models.UpdateSubscribedCalendarsRequest(
            name='中国传统日历',
            description='中国传统日历',
            managers=[
                'iiiP35sJadba8aBSgjrwPRKgiEiF'
            ],
            subscribe_scope=subscribe_scope
        )
        try:
            await client.update_subscribed_calendars_with_options_async('M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv', 'iiiP35sJadba8aBSgjrwPRKgiEiF', update_subscribed_calendars_request, update_subscribed_calendars_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\UpdateSubscribedCalendarsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\UpdateSubscribedCalendarsRequest\subscribeScope;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\UpdateSubscribedCalendarsRequest;
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
        $updateSubscribedCalendarsHeaders = new UpdateSubscribedCalendarsHeaders([]);
        $updateSubscribedCalendarsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $subscribeScope = new subscribeScope([
            "unionIds" => [
                "iiiP35sJadba8aBSgjrwPRKgiEiF"
            ],
            "openConversationIds" => [
                "cidvrURjEqVe8xxxxxxx"
            ],
            "corpIds" => [
                "dingz0xc7v89789asasdf"
            ]
        ]);
        $updateSubscribedCalendarsRequest = new UpdateSubscribedCalendarsRequest([
            "name" => "中国传统日历",
            "description" => "中国传统日历",
            "managers" => [
                "iiiP35sJadba8aBSgjrwPRKgiEiF"
            ],
            "subscribeScope" => $subscribeScope
        ]);
        try {
            $client->updateSubscribedCalendarsWithOptions("M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", "iiiP35sJadba8aBSgjrwPRKgiEiF", $updateSubscribedCalendarsRequest, $updateSubscribedCalendarsHeaders, new RuntimeOptions([]));
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

  updateSubscribedCalendarsHeaders := &dingtalkcalendar_1_0.UpdateSubscribedCalendarsHeaders{}
  updateSubscribedCalendarsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  subscribeScope := &dingtalkcalendar_1_0.UpdateSubscribedCalendarsRequestSubscribeScope{
    UnionIds: []*string{tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF")},
    OpenConversationIds: []*string{tea.String("cidvrURjEqVe8xxxxxxx")},
    CorpIds: []*string{tea.String("dingz0xc7v89789asasdf")},
  }
  updateSubscribedCalendarsRequest := &dingtalkcalendar_1_0.UpdateSubscribedCalendarsRequest{
    Name: tea.String("中国传统日历"),
    Description: tea.String("中国传统日历"),
    Managers: []*string{tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF")},
    SubscribeScope: subscribeScope,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateSubscribedCalendarsWithOptions(tea.String("M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv"), tea.String("iiiP35sJadba8aBSgjrwPRKgiEiF"), updateSubscribedCalendarsRequest, updateSubscribedCalendarsHeaders, &util.RuntimeOptions{})
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
    let updateSubscribedCalendarsHeaders = new $dingtalkcalendar_1_0.UpdateSubscribedCalendarsHeaders({ });
    updateSubscribedCalendarsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let subscribeScope = new $dingtalkcalendar_1_0.UpdateSubscribedCalendarsRequestSubscribeScope({
      unionIds: [
        "iiiP35sJadba8aBSgjrwPRKgiEiF"
      ],
      openConversationIds: [
        "cidvrURjEqVe8xxxxxxx"
      ],
      corpIds: [
        "dingz0xc7v89789asasdf"
      ],
    });
    let updateSubscribedCalendarsRequest = new $dingtalkcalendar_1_0.UpdateSubscribedCalendarsRequest({
      name: "中国传统日历",
      description: "中国传统日历",
      managers: [
        "iiiP35sJadba8aBSgjrwPRKgiEiF"
      ],
      subscribeScope: subscribeScope,
    });
    try {
      await client.updateSubscribedCalendarsWithOptions("M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", "iiiP35sJadba8aBSgjrwPRKgiEiF", updateSubscribedCalendarsRequest, updateSubscribedCalendarsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.UpdateSubscribedCalendarsHeaders updateSubscribedCalendarsHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.UpdateSubscribedCalendarsHeaders();
            updateSubscribedCalendarsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.UpdateSubscribedCalendarsRequest.UpdateSubscribedCalendarsRequestSubscribeScope subscribeScope = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.UpdateSubscribedCalendarsRequest.UpdateSubscribedCalendarsRequestSubscribeScope
            {
                UnionIds = new List<string>
                {
                    "iiiP35sJadba8aBSgjrwPRKgiEiF"
                },
                OpenConversationIds = new List<string>
                {
                    "cidvrURjEqVe8xxxxxxx"
                },
                CorpIds = new List<string>
                {
                    "dingz0xc7v89789asasdf"
                },
            };
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.UpdateSubscribedCalendarsRequest updateSubscribedCalendarsRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.UpdateSubscribedCalendarsRequest
            {
                Name = "中国传统日历",
                Description = "中国传统日历",
                Managers = new List<string>
                {
                    "iiiP35sJadba8aBSgjrwPRKgiEiF"
                },
                SubscribeScope = subscribeScope,
            };
            try
            {
                client.UpdateSubscribedCalendarsWithOptions("M5MjkxNDUxQHVzZXJzLmRpbmd0YWxrLmNv", "iiiP35sJadba8aBSgjrwPRKgiEiF", updateSubscribedCalendarsRequest, updateSubscribedCalendarsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | invalidParameter | calendar id cannot be blank | 日历id不能为空 |
| 400 | invalidParameter | calendar name length must less than 128 | 日历名长度不能超过128个字 |
| 400 | invalidParameter | subscribe range cannot be null | 订阅范围不能为空 |
| 400 | invalidParameter | calendar name cannot be blank | 日历名不能为空 |
| 400 | invalidParameter | current user must in range | 当前用户必须在相应的群和企业内 |
| 403 | permissionDenied | permission denied | 鉴权失败 |
