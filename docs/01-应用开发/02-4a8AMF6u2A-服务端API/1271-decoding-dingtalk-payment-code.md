---
title: "解码钉工牌电子码"
source_url: "https://open.dingtalk.com/document/development/decoding-dingtalk-payment-code"
namespace: "development"
slug: "decoding-dingtalk-payment-code"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 解码钉工牌电子码"
doc_id: "mOjXv1UkX8"
updated_at: "2025-09-11 21:03:40"
---

> Source: https://open.dingtalk.com/document/development/decoding-dingtalk-payment-code
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 解码钉工牌电子码
> Updated: 2025-09-11 21:03:40

# 解码钉工牌电子码

调用本接口，解析钉工牌电子码，本接口可获取关联的企业、用户userId等信息，获取用户信息后即可进行身份验证。

## 接口调用说明

目前解码接口仅支持钉钉侧的码值，不支持标准码（支付宝）解析。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/finance/payCodes/decode |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Finance.PayCode.Read-钉钉付款码信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| payCode | String | 否 | 付款码，硬件设置扫面获取码值。      解码接口仅支持钉钉侧生成的码值。目前不支持标准码解析，标准码是由支付宝生成的。 |
| requestId | String | 否 | 请求ID，由调用方随机生成幂等字符串。  例如：   - UUID随机字符串 - 时间戳+用户ID等        - 两次调用解码同一个码，传的requestId必须要一致，才能解码成功。 - 调用支付宝解码后，10分钟后码就会过期，再次调用，即使使用相同的**requestId**，支付宝也会返回失败。 |

### 请求示例

HTTP

```
POST /v1.0/finance/payCodes/decode HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:315ddxxx
Content-Type:application/json

{
  "payCode" : "28698xxx",
  "requestId" : "requestId"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkfinance_1_0.*;
import com.aliyun.dingtalkfinance_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkfinance_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkfinance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkfinance_1_0.Client client = Sample.createClient();
        DecodePayCodeHeaders decodePayCodeHeaders = new DecodePayCodeHeaders();
        decodePayCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DecodePayCodeRequest decodePayCodeRequest = new DecodePayCodeRequest()
                .setPayCode("28698xxx")
                .setRequestId("requestId");
        try {
            client.decodePayCodeWithOptions(decodePayCodeRequest, decodePayCodeHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.finance_1_0.client import Client as dingtalkfinance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.finance_1_0 import models as dingtalkfinance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkfinance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkfinance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        decode_pay_code_headers = dingtalkfinance__1__0_models.DecodePayCodeHeaders()
        decode_pay_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        decode_pay_code_request = dingtalkfinance__1__0_models.DecodePayCodeRequest(
            pay_code='28698xxx',
            request_id='requestId'
        )
        try:
            client.decode_pay_code_with_options(decode_pay_code_request, decode_pay_code_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        decode_pay_code_headers = dingtalkfinance__1__0_models.DecodePayCodeHeaders()
        decode_pay_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        decode_pay_code_request = dingtalkfinance__1__0_models.DecodePayCodeRequest(
            pay_code='28698xxx',
            request_id='requestId'
        )
        try:
            await client.decode_pay_code_with_options_async(decode_pay_code_request, decode_pay_code_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\DecodePayCodeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\DecodePayCodeRequest;
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
        $decodePayCodeHeaders = new DecodePayCodeHeaders([]);
        $decodePayCodeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $decodePayCodeRequest = new DecodePayCodeRequest([
            "payCode" => "28698xxx",
            "requestId" => "requestId"
        ]);
        try {
            $client->decodePayCodeWithOptions($decodePayCodeRequest, $decodePayCodeHeaders, new RuntimeOptions([]));
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
  dingtalkfinance_1_0  "github.com/alibabacloud-go/dingtalk/finance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkfinance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkfinance_1_0.Client{}
  _result, _err = dingtalkfinance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  decodePayCodeHeaders := &dingtalkfinance_1_0.DecodePayCodeHeaders{}
  decodePayCodeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  decodePayCodeRequest := &dingtalkfinance_1_0.DecodePayCodeRequest{
    PayCode: tea.String("28698xxx"),
    RequestId: tea.String("requestId"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DecodePayCodeWithOptions(decodePayCodeRequest, decodePayCodeHeaders, &util.RuntimeOptions{})
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
        public static AlibabaCloud.SDK.Dingtalkfinance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkfinance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.DecodePayCodeHeaders decodePayCodeHeaders = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.DecodePayCodeHeaders();
            decodePayCodeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.DecodePayCodeRequest decodePayCodeRequest = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.DecodePayCodeRequest
            {
                PayCode = "28698xxx",
                RequestId = "requestId",
            };
            try
            {
                client.DecodePayCodeWithOptions(decodePayCodeRequest, decodePayCodeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkfinance__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkfinance_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkfinance_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::Client> client = make_shared<Alibabacloud_Dingtalkfinance_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::DecodePayCodeHeaders> decodePayCodeHeaders = make_shared<Alibabacloud_Dingtalkfinance_1_0::DecodePayCodeHeaders>();
  decodePayCodeHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::DecodePayCodeRequest> decodePayCodeRequest = make_shared<Alibabacloud_Dingtalkfinance_1_0::DecodePayCodeRequest>(map<string, boost::any>({
    {"payCode", boost::any(string("28698xxx"))},
    {"requestId", boost::any(string("requestId"))}
  }));
  try {
    client->decodePayCodeWithOptions(decodePayCodeRequest, decodePayCodeHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| corpId | String | 企业的corpId。 |
| userId | String | 员工的userId。 |
| userInCorp | Boolean | 用户是否还在组织内。   - **true**：在组织内 - **false**：不在组织内 |
| codeType | String | 付款码类型，取值。   - **PURE\_IDENTITY\_CODE**：纯身份码 - **PAY\_IDENTITY\_CODE**：可支付的身份码 |
| alipayCode | String | 支付宝付款码。 |
| userCorpRelationType | String | 用户和企业关系，取值：   - **INTERNAL\_STAFF**：企业内部员工 - **EXTERNAL\_CONTACT**：外部联系人 - **NO\_RELATION**：普通用户与组织无关 |
| codeIdentity | String | 码标识，取值：   - **DT\_IDENTITY**：工牌码 - **DT\_VISITOR**：访客码 - **DT\_CONFERENCE**：会展码 |
| codeId | String | 码ID，例如访客码ID或会展码等。 |
| outBizId | String | 外部业务ID。   - 第三方企业应用，值为[创建钉工牌电子码](https://open.dingtalk.com/document/isvapp/create-a-user-code-instance)接口传入的参数requestId。 |
| extInfo | String | 扩展信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "corpId" : "ding1234",
  "userId" : "user456",
  "userInCorp" : true,
  "codeType" : "PURE_IDENTIFY_CODE",
  "alipayCode" : "2512345678",
  "userCorpRelationType" : "INTERNAL_STAFF",
  "codeIdentity" : "DT_VISITOR",
  "codeId" : "codeIdxxxxx",
  "outBizId" : "xxxxx",
  "extInfo" : "{\"authRules\":{}}"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | remoteServiceError | 远程服务错误 | 远程服务错误 |
| 400 | illegalAlipayCode | 非法的支付宝码值 | 非法的支付宝码值 |
| 400 | requestIdNotConsist | RequestId不一致 | 两次解码传入的requestId不一致 |
| 400 | expiredPayCode | 码已过期 | 码已过期 |
| 400 | invalidParameter | 请求对象为空 | 请求对象为空 |
| 400 | invalidParameter | 无效请求参数 | 无效请求参数 |
| 400 | invalidParameter | 存在空参数 | 存在空参数 |
| 400 | missingParameter | 缺少必填参数 | 缺少必填参数 |
| 400 | invalidPayCode | 无效的付款码 | 无效的付款码 |
| 400 | dataNotConsist | 数据不一致 | 数据不一致 |
| 400 | moneyNotConsist | 金额不一致 | 金额不一致 |
| 400 | callAlipayFail | 调用支付宝异常 | 调用支付宝异常 |
| 400 | callOrgFail | 调用内部通讯录异常 | 调用内部通讯录异常 |
| 400 | accessStorageFail | 调用存储异常 | 调用存储异常 |
| 500 | unknownError | 未知错误 | 未知错误 |
