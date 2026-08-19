---
title: "同步钉工牌码验证结果"
source_url: "https://open.dingtalk.com/document/development/notification-dingtalk-badge-verification-result"
namespace: "development"
slug: "notification-dingtalk-badge-verification-result"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 同步钉工牌码验证结果"
doc_id: "Rl4dT6YmvH"
updated_at: "2025-09-11 21:03:37"
---

> Source: https://open.dingtalk.com/document/development/notification-dingtalk-badge-verification-result
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 同步钉工牌码验证结果
> Updated: 2025-09-11 21:03:37

# 同步钉工牌码验证结果

调用本接口，同步钉工牌码验证结果。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/badge/codes/verifyResults |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Badge.Common.Write-钉工牌基础数据写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| payCode | String | 是 | 码值，接入方硬件设备扫描钉工牌二维码获取的码值。 |
| corpId | String | 是 | 企业corpId。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/)首页查看。 |
| userCorpRelationType | String | 是 | 用户和企业的关系类型，用于区分内部员工，外部联系人，无关系普通用户。   - **INTERNAL\_STAFF**：企业内部员工 - **EXTERNAL\_CONTACT**：外部联系人 - **NO\_RELATION**：普通用户与组织无关 |
| userIdentity | String | 是 | 用户身份标识。取值和userCorpRelationType参数值有关。   - 如果是企业内部用户，通过[获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md)接口传用户的userId。 - 如果是外部联系人通过[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口传外部联系人的userid。 - 如果是无关系用户需传入用户手机号，手机号需带有国家码，例如86-xxxxxxxxxxx。 |
| verifyTime | String | 是 | 验证时间。 |
| verifyResult | Boolean | 是 | 验证结果。 |
| verifyLocation | String | 否 | 验证地点。 |
| verifyNo | String | 否 | 验证流水号，可随机生成，确保用户下唯一 |
| verifyEvent | String | 否 | 验证事件。8个汉字以内，如门禁验证、班车登记、餐盘绑定等。 |
| remark | String | 否 | 备注信息。 |

### 请求示例

HTTP

```
POST /v1.0/badge/codes/verifyResults HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:your-token
Content-Type:application/json

{
  "payCode" : "261234567890",
  "corpId" : "corpxxxx",
  "userCorpRelationType" : "INTERNAL_STAFF",
  "userIdentity" : "180xxxx",
  "verifyTime" : "2021-01-01 12:12:12",
  "verifyResult" : false,
  "verifyLocation" : "钉工牌大道9号",
  "verifyNo" : "202212311212",
  "verifyEvent" : "门禁验证",
  "remark" : "备注"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkbadge_1_0.*;
import com.aliyun.dingtalkbadge_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkbadge_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkbadge_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkbadge_1_0.Client client = Sample.createClient();
        NotifyBadgeCodeVerifyResultHeaders notifyBadgeCodeVerifyResultHeaders = new NotifyBadgeCodeVerifyResultHeaders();
        notifyBadgeCodeVerifyResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
        NotifyBadgeCodeVerifyResultRequest notifyBadgeCodeVerifyResultRequest = new NotifyBadgeCodeVerifyResultRequest()
                .setPayCode("261234567890")
                .setCorpId("corpxxxx")
                .setUserCorpRelationType("INTERNAL_STAFF")
                .setUserIdentity("180xxxx")
                .setVerifyTime("2021-01-01 12:12:12")
                .setVerifyResult(false)
                .setVerifyLocation("钉工牌大道9号");
        try {
            client.notifyBadgeCodeVerifyResultWithOptions(notifyBadgeCodeVerifyResultRequest, notifyBadgeCodeVerifyResultHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.badge_1_0.client import Client as dingtalkbadge_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.badge_1_0 import models as dingtalkbadge__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkbadge_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkbadge_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_badge_code_verify_result_headers = dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultHeaders()
        notify_badge_code_verify_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        notify_badge_code_verify_result_request = dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultRequest(
            pay_code='261234567890',
            corp_id='corpxxxx',
            user_corp_relation_type='INTERNAL_STAFF',
            user_identity='180xxxx',
            verify_time='2021-01-01 12:12:12',
            verify_result=False,
            verify_location='钉工牌大道9号'
        )
        try:
            client.notify_badge_code_verify_result_with_options(notify_badge_code_verify_result_request, notify_badge_code_verify_result_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        notify_badge_code_verify_result_headers = dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultHeaders()
        notify_badge_code_verify_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        notify_badge_code_verify_result_request = dingtalkbadge__1__0_models.NotifyBadgeCodeVerifyResultRequest(
            pay_code='261234567890',
            corp_id='corpxxxx',
            user_corp_relation_type='INTERNAL_STAFF',
            user_identity='180xxxx',
            verify_time='2021-01-01 12:12:12',
            verify_result=False,
            verify_location='钉工牌大道9号'
        )
        try:
            await client.notify_badge_code_verify_result_with_options_async(notify_badge_code_verify_result_request, notify_badge_code_verify_result_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\NotifyBadgeCodeVerifyResultHeaders;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\NotifyBadgeCodeVerifyResultRequest;
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
        $notifyBadgeCodeVerifyResultHeaders = new NotifyBadgeCodeVerifyResultHeaders([]);
        $notifyBadgeCodeVerifyResultHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $notifyBadgeCodeVerifyResultRequest = new NotifyBadgeCodeVerifyResultRequest([
            "payCode" => "261234567890",
            "corpId" => "corpxxxx",
            "userCorpRelationType" => "INTERNAL_STAFF",
            "userIdentity" => "180xxxx",
            "verifyTime" => "2021-01-01 12:12:12",
            "verifyResult" => false,
            "verifyLocation" => "钉工牌大道9号"
        ]);
        try {
            $client->notifyBadgeCodeVerifyResultWithOptions($notifyBadgeCodeVerifyResultRequest, $notifyBadgeCodeVerifyResultHeaders, new RuntimeOptions([]));
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
  dingtalkbadge_1_0  "github.com/alibabacloud-go/dingtalk/badge_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkbadge_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkbadge_1_0.Client{}
  _result, _err = dingtalkbadge_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  notifyBadgeCodeVerifyResultHeaders := &dingtalkbadge_1_0.NotifyBadgeCodeVerifyResultHeaders{}
  notifyBadgeCodeVerifyResultHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  notifyBadgeCodeVerifyResultRequest := &dingtalkbadge_1_0.NotifyBadgeCodeVerifyResultRequest{
    PayCode: tea.String("261234567890"),
    CorpId: tea.String("corpxxxx"),
    UserCorpRelationType: tea.String("INTERNAL_STAFF"),
    UserIdentity: tea.String("180xxxx"),
    VerifyTime: tea.String("2021-01-01 12:12:12"),
    VerifyResult: tea.Bool(false),
    VerifyLocation: tea.String("钉工牌大道9号"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.NotifyBadgeCodeVerifyResultWithOptions(notifyBadgeCodeVerifyResultRequest, notifyBadgeCodeVerifyResultHeaders, &util.RuntimeOptions{})
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
import dingtalkbadge_1_0, * as $dingtalkbadge_1_0 from '@alicloud/dingtalk/badge_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkbadge_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkbadge_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let notifyBadgeCodeVerifyResultHeaders = new $dingtalkbadge_1_0.NotifyBadgeCodeVerifyResultHeaders({ });
    notifyBadgeCodeVerifyResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let notifyBadgeCodeVerifyResultRequest = new $dingtalkbadge_1_0.NotifyBadgeCodeVerifyResultRequest({
      payCode: "261234567890",
      corpId: "corpxxxx",
      userCorpRelationType: "INTERNAL_STAFF",
      userIdentity: "180xxxx",
      verifyTime: "2021-01-01 12:12:12",
      verifyResult: false,
      verifyLocation: "钉工牌大道9号",
    });
    try {
      await client.notifyBadgeCodeVerifyResultWithOptions(notifyBadgeCodeVerifyResultRequest, notifyBadgeCodeVerifyResultHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkbadge_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkbadge_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeVerifyResultHeaders notifyBadgeCodeVerifyResultHeaders = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeVerifyResultHeaders();
            notifyBadgeCodeVerifyResultHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeVerifyResultRequest notifyBadgeCodeVerifyResultRequest = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.NotifyBadgeCodeVerifyResultRequest
            {
                PayCode = "261234567890",
                CorpId = "corpxxxx",
                UserCorpRelationType = "INTERNAL_STAFF",
                UserIdentity = "180xxxx",
                VerifyTime = "2021-01-01 12:12:12",
                VerifyResult = false,
                VerifyLocation = "钉工牌大道9号",
            };
            try
            {
                client.NotifyBadgeCodeVerifyResultWithOptions(notifyBadgeCodeVerifyResultRequest, notifyBadgeCodeVerifyResultHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkbadge__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkbadge_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkbadge_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::Client> client = make_shared<Alibabacloud_Dingtalkbadge_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeVerifyResultHeaders> notifyBadgeCodeVerifyResultHeaders = make_shared<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeVerifyResultHeaders>();
  notifyBadgeCodeVerifyResultHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeVerifyResultRequest> notifyBadgeCodeVerifyResultRequest = make_shared<Alibabacloud_Dingtalkbadge_1_0::NotifyBadgeCodeVerifyResultRequest>(map<string, boost::any>({
    {"payCode", boost::any(string("261234567890"))},
    {"corpId", boost::any(string("corpxxxx"))},
    {"userCorpRelationType", boost::any(string("INTERNAL_STAFF"))},
    {"userIdentity", boost::any(string("180xxxx"))},
    {"verifyTime", boost::any(string("2021-01-01 12:12:12"))},
    {"verifyResult", boost::any(false)},
    {"verifyLocation", boost::any(string("钉工牌大道9号"))}
  }));
  try {
    client->notifyBadgeCodeVerifyResultWithOptions(notifyBadgeCodeVerifyResultRequest, notifyBadgeCodeVerifyResultHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | String | 请求是否成功。   - **SUCCESS**：成功 - **FAIL**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : "SUCCESS"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 无效请求参数 | 无效请求参数 |
| 400 | dataNotConsist | 数据不一致 | 数据不一致 |
| 400 | invalidPayCode | 非法的码值 | 非法的码值 |
| 500 | unknownError | 未知错误 | 未知错误 |
