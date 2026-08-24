---
title: "查看单个日程的签退详情"
source_url: "https://open.dingtalk.com/document/development/view-the-billing-details-of-a-single-schedule"
namespace: "development"
slug: "view-the-billing-details-of-a-single-schedule"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日程 > 签到 > 查看单个日程的签退详情"
doc_id: "qiC4k0QsjB"
updated_at: "2026-06-02 09:25:12"
---

> Source: https://open.dingtalk.com/document/development/view-the-billing-details-of-a-single-schedule
> Path: 应用开发 / 服务端API / 日程 > 签到 > 查看单个日程的签退详情
> Updated: 2026-06-02 09:25:12

# 查看单个日程的签退详情

调用本接口，可获取单个日程的签退人员列表和未签退人员列表，列表信息包含人员unionid、用户名等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/signOut |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Calendar.Event.Read-日历应用中日程读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 本次请求的资源所归属的用户unionId，该用户需要为请求日程的组织者和日程的参与者。   - 企业内部应用和第三方企业应用，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 - 第三方个人应用，调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口获取unionId参数值。 |
| calendarId | String | 是 | 日程所属的日历ID，参数填写为primary，表示用户的主日历。 |
| eventId | String | 是 | 日程ID，可调用[查询日程列表](0254-query-an-event-list.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| maxResults | Integer | 是 | 查询返回结果数，最大值500。 |
| nextToken | String | 否 | 分页游标。      如果一个查询条件一次无法全部返回结果，会返回分页token，下次查询带上该token后会返回后续数据，直到分页token为null表示数据已经全部查询完毕。 |
| type | String | 是 | 签退信息类型。   - **sign\_out**：已签退 - **not\_yet\_sign\_out**：未签退 |

### 请求示例

HTTP

```
GET /v1.0/calendar/users/iiiP35sxxx/calendars/primary/events/cnNTbWxxx/signOut?maxResults=25&nextToken=cnNTbxxx&type=sign_out HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dd438xxx
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
        GetSignOutListHeaders getSignOutListHeaders = new GetSignOutListHeaders();
        getSignOutListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetSignOutListRequest getSignOutListRequest = new GetSignOutListRequest()
                .setMaxResults(25)
                .setNextToken("cnNTbxxx")
                .setType("sign_out");
        try {
            client.getSignOutListWithOptions("iiiP35sxxx", "primary", "cnNTbWxxx", getSignOutListRequest, getSignOutListHeaders, new RuntimeOptions());
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
        get_sign_out_list_headers = dingtalkcalendar__1__0_models.GetSignOutListHeaders()
        get_sign_out_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_sign_out_list_request = dingtalkcalendar__1__0_models.GetSignOutListRequest(
            max_results=25,
            next_token='cnNTbxxx',
            type='sign_out'
        )
        try:
            client.get_sign_out_list_with_options('iiiP35sxxx', 'primary', 'cnNTbWxxx', get_sign_out_list_request, get_sign_out_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_sign_out_list_headers = dingtalkcalendar__1__0_models.GetSignOutListHeaders()
        get_sign_out_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_sign_out_list_request = dingtalkcalendar__1__0_models.GetSignOutListRequest(
            max_results=25,
            next_token='cnNTbxxx',
            type='sign_out'
        )
        try:
            await client.get_sign_out_list_with_options_async('iiiP35sxxx', 'primary', 'cnNTbWxxx', get_sign_out_list_request, get_sign_out_list_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetSignOutListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcalendar_1_0\Models\GetSignOutListRequest;
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
        $getSignOutListHeaders = new GetSignOutListHeaders([]);
        $getSignOutListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSignOutListRequest = new GetSignOutListRequest([
            "maxResults" => 25,
            "nextToken" => "cnNTbxxx",
            "type" => "sign_out"
        ]);
        try {
            $client->getSignOutListWithOptions("iiiP35sxxx", "primary", "cnNTbWxxx", $getSignOutListRequest, $getSignOutListHeaders, new RuntimeOptions([]));
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

  getSignOutListHeaders := &dingtalkcalendar_1_0.GetSignOutListHeaders{}
  getSignOutListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSignOutListRequest := &dingtalkcalendar_1_0.GetSignOutListRequest{
    MaxResults: tea.Int32(25),
    NextToken: tea.String("cnNTbxxx"),
    Type: tea.String("sign_out"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSignOutListWithOptions(tea.String("iiiP35sxxx"), tea.String("primary"), tea.String("cnNTbWxxx"), getSignOutListRequest, getSignOutListHeaders, &util.RuntimeOptions{})
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
    let getSignOutListHeaders = new $dingtalkcalendar_1_0.GetSignOutListHeaders({ });
    getSignOutListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getSignOutListRequest = new $dingtalkcalendar_1_0.GetSignOutListRequest({
      maxResults: 25,
      nextToken: "cnNTbxxx",
      type: "sign_out",
    });
    try {
      await client.getSignOutListWithOptions("iiiP35sxxx", "primary", "cnNTbWxxx", getSignOutListRequest, getSignOutListHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetSignOutListHeaders getSignOutListHeaders = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetSignOutListHeaders();
            getSignOutListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetSignOutListRequest getSignOutListRequest = new AlibabaCloud.SDK.Dingtalkcalendar_1_0.Models.GetSignOutListRequest
            {
                MaxResults = 25,
                NextToken = "cnNTbxxx",
                Type = "sign_out",
            };
            try
            {
                client.GetSignOutListWithOptions("iiiP35sxxx", "primary", "cnNTbWxxx", getSignOutListRequest, getSignOutListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcalendar__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcalendar_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcalendar_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcalendar_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcalendar_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcalendar_1_0::GetSignOutListHeaders> getSignOutListHeaders = make_shared<Alibabacloud_Dingtalkcalendar_1_0::GetSignOutListHeaders>();
  getSignOutListHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcalendar_1_0::GetSignOutListRequest> getSignOutListRequest = make_shared<Alibabacloud_Dingtalkcalendar_1_0::GetSignOutListRequest>(map<string, boost::any>({
    {"maxResults", boost::any(25)},
    {"nextToken", boost::any(string("cnNTbxxx"))},
    {"type", boost::any(string("sign_out"))}
  }));
  try {
    client->getSignOutListWithOptions(make_shared<string>("iiiP35sxxx"), make_shared<string>("primary"), make_shared<string>("cnNTbWxxx"), getSignOutListRequest, getSignOutListHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| nextToken | String | 分页游标。      如果一个查询条件一次无法全部返回结果，会返回分页token，下次查询带上该token后会返回后续数据，直到分页token为null表示数据已经全部查询完毕。 |
| users | Array | 签退信息。 |
| userId | String | 日程所属用户的unionId。 |
| displayName | String | 用户名。 |
| checkOutTime | Long | 签退时间，单位毫秒。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "cnNTbW1YbxxxxdlQrQT09",
  "users" : [ {
    "userId" : "iiiP35sJaxxx",
    "displayName" : "张三",
    "checkOutTime" : 1632304130862
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | CalendarId cannot be blank | 日历id不能为空 |
| 400 | invalidParameter | eventId cannot be blank | 日程id不能为空 |
| 400 | invalidParameter | Subscribed calendar not support this method | 订阅日历不支持此方法 |
