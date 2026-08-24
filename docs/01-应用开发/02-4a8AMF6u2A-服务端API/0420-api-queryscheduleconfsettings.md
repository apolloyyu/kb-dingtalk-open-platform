---
title: "查询预约会议设置"
source_url: "https://open.dingtalk.com/document/development/api-queryscheduleconfsettings"
namespace: "development"
slug: "api-queryscheduleconfsettings"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 会议 > 查询预约会议设置"
doc_id: "rpa11SQ6W2"
updated_at: "2026-06-02 09:18:00"
---

> Source: https://open.dingtalk.com/document/development/api-queryscheduleconfsettings
> Path: 应用开发 / 服务端API / 音视频 > 会议 > 查询预约会议设置
> Updated: 2026-06-02 09:18:00

# 查询预约会议设置

根据预约会议id，查询预约会议设置信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/scheduleConferences/settings |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Read-视频会议信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| scheduleConferenceId | String | 是 | 预约会议 id，可通过[创建预约会议](0416-create-appointment-meeting.md)接口获取返回参数`scheduleConferenceId`字段。 |

### 请求示例

HTTP

```
GET /v1.0/conference/scheduleConferences/settings?scheduleConferenceId=dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1ce64c62b52f370c9421422d1bb87dc1
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
        com.aliyun.dingtalkconference_1_0.models.QueryScheduleConfSettingsHeaders queryScheduleConfSettingsHeaders = new com.aliyun.dingtalkconference_1_0.models.QueryScheduleConfSettingsHeaders();
        queryScheduleConfSettingsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.QueryScheduleConfSettingsRequest queryScheduleConfSettingsRequest = new com.aliyun.dingtalkconference_1_0.models.QueryScheduleConfSettingsRequest()
                .setScheduleConferenceId("dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26");
        try {
            client.queryScheduleConfSettingsWithOptions(queryScheduleConfSettingsRequest, queryScheduleConfSettingsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_schedule_conf_settings_headers = dingtalkconference__1__0_models.QueryScheduleConfSettingsHeaders()
        query_schedule_conf_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_schedule_conf_settings_request = dingtalkconference__1__0_models.QueryScheduleConfSettingsRequest(
            schedule_conference_id='dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26'
        )
        try:
            client.query_schedule_conf_settings_with_options(query_schedule_conf_settings_request, query_schedule_conf_settings_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_schedule_conf_settings_headers = dingtalkconference__1__0_models.QueryScheduleConfSettingsHeaders()
        query_schedule_conf_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_schedule_conf_settings_request = dingtalkconference__1__0_models.QueryScheduleConfSettingsRequest(
            schedule_conference_id='dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26'
        )
        try:
            await client.query_schedule_conf_settings_with_options_async(query_schedule_conf_settings_request, query_schedule_conf_settings_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryScheduleConfSettingsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\QueryScheduleConfSettingsRequest;
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
        $queryScheduleConfSettingsHeaders = new QueryScheduleConfSettingsHeaders([]);
        $queryScheduleConfSettingsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryScheduleConfSettingsRequest = new QueryScheduleConfSettingsRequest([
            "scheduleConferenceId" => "dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26"
        ]);
        try {
            $client->queryScheduleConfSettingsWithOptions($queryScheduleConfSettingsRequest, $queryScheduleConfSettingsHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
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

  queryScheduleConfSettingsHeaders := &dingtalkconference_1_0.QueryScheduleConfSettingsHeaders{}
  queryScheduleConfSettingsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryScheduleConfSettingsRequest := &dingtalkconference_1_0.QueryScheduleConfSettingsRequest{
    ScheduleConferenceId: tea.String("dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryScheduleConfSettingsWithOptions(queryScheduleConfSettingsRequest, queryScheduleConfSettingsHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkconference_1_0 = require('@alicloud/dingtalk/conference_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkconference_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryScheduleConfSettingsHeaders = new dingtalkconference_1_0.QueryScheduleConfSettingsHeaders({ });
    queryScheduleConfSettingsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryScheduleConfSettingsRequest = new dingtalkconference_1_0.QueryScheduleConfSettingsRequest({
      scheduleConferenceId: 'dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26',
    });
    try {
      await client.queryScheduleConfSettingsWithOptions(queryScheduleConfSettingsRequest, queryScheduleConfSettingsHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConfSettingsHeaders queryScheduleConfSettingsHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConfSettingsHeaders();
            queryScheduleConfSettingsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConfSettingsRequest queryScheduleConfSettingsRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.QueryScheduleConfSettingsRequest
            {
                ScheduleConferenceId = "dxxx0ad6-b769-418e-8a7e-7b5ef4fafa26",
            };
            try
            {
                client.QueryScheduleConfSettingsWithOptions(queryScheduleConfSettingsRequest, queryScheduleConfSettingsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| scheduleConfSettingModel | Object | 预约会议配置。 |
| hostUnionId | String | 主持人 unionId。 |
| cohostUnionIds | Array of String | 联席主持人 unionId。 |
| confAllowedCorpId | String | 组织内部会议 corpId。 |
| lockRoom | Integer | 锁定会议：   - 0：取消锁定 - 1：锁定 |
| screenShareForbidden | Integer | 发起共享：   - 0：允许共享 - 1：禁止共享 |
| muteOnJoin | Integer | 成员入会时静音：   - -1：开启 - 0：不开启 - 6：超过6人自动开启静音 |
| moziConfVirtualExtraSetting | Object | 预约会议设置。 |
| waitingRoom | Integer | 等候室：   - 0： 不开启 - 1：开启 |
| joinBeforeHost | Integer | 在主持人进会前加入会议：   - 0：不开启 - 1：开启 |
| enableChat | Integer | 聊天和互动：   - 0：不开启 - 1：开启 |
| lockNick | Integer | 自己改名：   - 0：允许自己改名 - 1：禁止自己改名 |
| lockMediaStatusMicMute | Integer | 自己解除静音：   - 0：允许自己解除静音 - 1：禁止自己解除静音 |
| moziConfExtensionAppSettings | Array | 会议扩展应用设置列表。 |
| clientId | String | 钉钉开放应用 clientId。 |
| coolAppCode | String | 酷应用 Code。可通过开发者后台，微应用中查看酷应用Code。 |
| autoOpenMode | String | 自动打开模式：   - 0：不自动打开 - 1：仅主持人/联席主持人自动打开 - 2：全员自动打开 |
| extensionAppBizData | String | 会议维度扩展应用自定义信息。 |
| enableWebAnonymousJoin | Boolean | 是否支持web端免登入会：   - true：支持 - false：不支持 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "scheduleConfSettingModel" : {
    "hostUnionId" : "mE4lK7nFiPFhudV2Ch17AMwiEi",
    "cohostUnionIds" : [ "2iPOLbpUNMLzB5LuwggiiqiPwiEiE" ],
    "confAllowedCorpId" : "dingc02f685fa06381c44ac5d6980864d335",
    "lockRoom" : 1,
    "screenShareForbidden" : 1,
    "muteOnJoin" : 6,
    "moziConfVirtualExtraSetting" : {
      "waitingRoom" : 1,
      "joinBeforeHost" : 1,
      "enableChat" : 1,
      "lockNick" : 1,
      "lockMediaStatusMicMute" : 1,
      "moziConfExtensionAppSettings" : [ {
        "clientId" : "dingwklgz6xxx5yltcyr",
        "coolAppCode" : "COOLAPP-0-1026633886192127xxxB000W",
        "autoOpenMode" : "1",
        "extensionAppBizData" : "bizData"
      } ],
      "enableWebAnonymousJoin" : true
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | paramError | 参数错误，请检查入参 |
| 400 | scheduleConferenceIdError | scheduleConferenceIdError | 预约会议id错误 |
| 400 | userNotInOrg | userNotInOrg | 用户不在组织内 |
| 403 | noPermission | noPermission | 无操作权限 |
| 500 | systemError | systemError | 系统错误 |
