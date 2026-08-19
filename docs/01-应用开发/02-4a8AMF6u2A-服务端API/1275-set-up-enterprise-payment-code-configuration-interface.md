---
title: "配置企业钉工牌"
source_url: "https://open.dingtalk.com/document/development/set-up-enterprise-payment-code-configuration-interface"
namespace: "development"
slug: "set-up-enterprise-payment-code-configuration-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 配置企业钉工牌"
doc_id: "EMtHzchK3C"
updated_at: "2025-09-11 21:03:43"
---

> Source: https://open.dingtalk.com/document/development/set-up-enterprise-payment-code-configuration-interface
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 使用SuiteAccessToken调用 > 配置企业钉工牌
> Updated: 2025-09-11 21:03:43

# 配置企业钉工牌

调用本接口，可用于开通或关闭企业钉工牌，并设置相关关联配置信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/finance/payCodes/corpSettings |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Finance.PayCode.Write-钉钉付款码信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| codeIdentity | String | 是 | 码标识，取值：   - **DT\_VISITOR**：访客码 - **DT\_CONFERENCE**：会展码 - **DT\_IDENTITY**：身份码 |
| corpId | String | 是 | 开通的企业corpId。 |
| status | String | 是 | 状态，取值。   - **OPEN**：开启 - **CLOSED**：关闭 |
| extInfo | Map<String, String> | 否 | 扩展参数，是否关联支付宝。   - **true**: 关联支付宝：可以应用到当面付等支付场景，支付时可以使用用户支付宝的钱。 - **false**: 不关联支付宝：用户生成的码只能用作身份码，不能应用到支付场景。   参数示例：   ``` "extInfo": {     "supportRelateAlipay": "false" } ``` |

### 请求示例

HTTP

```
POST /v1.0/finance/payCodes/corpSettings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:00adbxxx
Content-Type:application/json

{
  "codeIdentity" : "TEST",
  "corpId" : "ding1234",
  "status" : "OPEN"
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
        SaveCorpPayCodeHeaders saveCorpPayCodeHeaders = new SaveCorpPayCodeHeaders();
        saveCorpPayCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SaveCorpPayCodeRequest saveCorpPayCodeRequest = new SaveCorpPayCodeRequest()
                .setCodeIdentity("TEST")
                .setCorpId("ding1234")
                .setStatus("OPEN");
        try {
            client.saveCorpPayCodeWithOptions(saveCorpPayCodeRequest, saveCorpPayCodeHeaders, new RuntimeOptions());
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
        save_corp_pay_code_headers = dingtalkfinance__1__0_models.SaveCorpPayCodeHeaders()
        save_corp_pay_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        save_corp_pay_code_request = dingtalkfinance__1__0_models.SaveCorpPayCodeRequest(
            code_identity='TEST',
            corp_id='ding1234',
            status='OPEN'
        )
        try:
            client.save_corp_pay_code_with_options(save_corp_pay_code_request, save_corp_pay_code_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        save_corp_pay_code_headers = dingtalkfinance__1__0_models.SaveCorpPayCodeHeaders()
        save_corp_pay_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        save_corp_pay_code_request = dingtalkfinance__1__0_models.SaveCorpPayCodeRequest(
            code_identity='TEST',
            corp_id='ding1234',
            status='OPEN'
        )
        try:
            await client.save_corp_pay_code_with_options_async(save_corp_pay_code_request, save_corp_pay_code_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\SaveCorpPayCodeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vfinance_1_0\Models\SaveCorpPayCodeRequest;
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
        $saveCorpPayCodeHeaders = new SaveCorpPayCodeHeaders([]);
        $saveCorpPayCodeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $saveCorpPayCodeRequest = new SaveCorpPayCodeRequest([
            "codeIdentity" => "TEST",
            "corpId" => "ding1234",
            "status" => "OPEN"
        ]);
        try {
            $client->saveCorpPayCodeWithOptions($saveCorpPayCodeRequest, $saveCorpPayCodeHeaders, new RuntimeOptions([]));
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

  saveCorpPayCodeHeaders := &dingtalkfinance_1_0.SaveCorpPayCodeHeaders{}
  saveCorpPayCodeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  saveCorpPayCodeRequest := &dingtalkfinance_1_0.SaveCorpPayCodeRequest{
    CodeIdentity: tea.String("TEST"),
    CorpId: tea.String("ding1234"),
    Status: tea.String("OPEN"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SaveCorpPayCodeWithOptions(saveCorpPayCodeRequest, saveCorpPayCodeHeaders, &util.RuntimeOptions{})
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
import dingtalkfinance_1_0, * as $dingtalkfinance_1_0 from '@alicloud/dingtalk/finance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkfinance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkfinance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let saveCorpPayCodeHeaders = new $dingtalkfinance_1_0.SaveCorpPayCodeHeaders({ });
    saveCorpPayCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let saveCorpPayCodeRequest = new $dingtalkfinance_1_0.SaveCorpPayCodeRequest({
      codeIdentity: "TEST",
      corpId: "ding1234",
      status: "OPEN",
    });
    try {
      await client.saveCorpPayCodeWithOptions(saveCorpPayCodeRequest, saveCorpPayCodeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.SaveCorpPayCodeHeaders saveCorpPayCodeHeaders = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.SaveCorpPayCodeHeaders();
            saveCorpPayCodeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.SaveCorpPayCodeRequest saveCorpPayCodeRequest = new AlibabaCloud.SDK.Dingtalkfinance_1_0.Models.SaveCorpPayCodeRequest
            {
                CodeIdentity = "TEST",
                CorpId = "ding1234",
                Status = "OPEN",
            };
            try
            {
                client.SaveCorpPayCodeWithOptions(saveCorpPayCodeRequest, saveCorpPayCodeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::SaveCorpPayCodeHeaders> saveCorpPayCodeHeaders = make_shared<Alibabacloud_Dingtalkfinance_1_0::SaveCorpPayCodeHeaders>();
  saveCorpPayCodeHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkfinance_1_0::SaveCorpPayCodeRequest> saveCorpPayCodeRequest = make_shared<Alibabacloud_Dingtalkfinance_1_0::SaveCorpPayCodeRequest>(map<string, boost::any>({
    {"codeIdentity", boost::any(string("TEST"))},
    {"corpId", boost::any(string("ding1234"))},
    {"status", boost::any(string("OPEN"))}
  }));
  try {
    client->saveCorpPayCodeWithOptions(saveCorpPayCodeRequest, saveCorpPayCodeHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| codeIdentity | String | 码标识，取值：   - **DT\_VISITOR**：访客码 - **DT\_CONFERENCE**：会展码 |
| corpId | String | 开通企业的corpId。 |
| status | String | 状态，取值。   - **OPEN**：开启 - **CLOSED**：关闭 |
| extInfo | Map<String, String> | 扩展参数。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "codeIdentity" : "TEST",
  "corpId" : "ding1234",
  "status" : "OPEN",
  "extInfo" : {
    "key" : "\\\"extInfo\\\": {    \\\"supportRelateAlipay\\\": \\\"false\\\"}"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | missingParameter | 缺少必须参数 | 缺少必须参数 |
| 400 | invalidParameter | 非法的参数 | 非法的参数 |
| 400 | remoteServiceError | 远程服务错误 | 远程服务错误 |
| 500 | unknownError | 未知错误 | 未知错误 |
