---
title: "解码钉工牌电子码"
source_url: "https://open.dingtalk.com/document/development/stack-dingtalk-badge"
namespace: "development"
slug: "stack-dingtalk-badge"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 解码钉工牌电子码"
doc_id: "rGYuVi6A3C"
updated_at: "2026-07-20 09:21:57"
---

> Source: https://open.dingtalk.com/document/development/stack-dingtalk-badge
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 解码钉工牌电子码
> Updated: 2026-07-20 09:21:57

# 解码钉工牌电子码

调用本接口，解码钉工牌码，目前的解码仅支持钉钉侧的码值，不支持标准码解析。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/badge/codes/decode |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Badge.Common.Read-钉工牌基础数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| payCode | String | 是 | 码值，解码接口仅支持钉钉侧生成的码值。      目前不支持标准码解析，标准码是由支付宝侧生成的。 |
| requestId | String | 是 | 请求ID，由调用方随机生成幂等字符串。  例如：   - UUID随机字符串 - 时间戳+用户ID等        - 两次调用解码同一个码，传的requestId必须要一致，才能解码成功。 - 调用支付宝解码后，10分钟后码就会过期，再次调用，即使使用相同的**requestId**，支付宝也会返回失败。 |

### 请求示例

HTTP

```
POST /v1.0/badge/codes/decode HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "payCode" : "dingbadgexxxx",
  "requestId" : "202103232"
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
        DecodeBadgeCodeHeaders decodeBadgeCodeHeaders = new DecodeBadgeCodeHeaders();
        decodeBadgeCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DecodeBadgeCodeRequest decodeBadgeCodeRequest = new DecodeBadgeCodeRequest()
                .setPayCode("dingbadgexxxx")
                .setRequestId("202103232");
        try {
            client.decodeBadgeCodeWithOptions(decodeBadgeCodeRequest, decodeBadgeCodeHeaders, new RuntimeOptions());
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
        decode_badge_code_headers = dingtalkbadge__1__0_models.DecodeBadgeCodeHeaders()
        decode_badge_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        decode_badge_code_request = dingtalkbadge__1__0_models.DecodeBadgeCodeRequest(
            pay_code='dingbadgexxxx',
            request_id='202103232'
        )
        try:
            client.decode_badge_code_with_options(decode_badge_code_request, decode_badge_code_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        decode_badge_code_headers = dingtalkbadge__1__0_models.DecodeBadgeCodeHeaders()
        decode_badge_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        decode_badge_code_request = dingtalkbadge__1__0_models.DecodeBadgeCodeRequest(
            pay_code='dingbadgexxxx',
            request_id='202103232'
        )
        try:
            await client.decode_badge_code_with_options_async(decode_badge_code_request, decode_badge_code_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\DecodeBadgeCodeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\DecodeBadgeCodeRequest;
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
        $decodeBadgeCodeHeaders = new DecodeBadgeCodeHeaders([]);
        $decodeBadgeCodeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $decodeBadgeCodeRequest = new DecodeBadgeCodeRequest([
            "payCode" => "dingbadgexxxx",
            "requestId" => "202103232"
        ]);
        try {
            $client->decodeBadgeCodeWithOptions($decodeBadgeCodeRequest, $decodeBadgeCodeHeaders, new RuntimeOptions([]));
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

  decodeBadgeCodeHeaders := &dingtalkbadge_1_0.DecodeBadgeCodeHeaders{}
  decodeBadgeCodeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  decodeBadgeCodeRequest := &dingtalkbadge_1_0.DecodeBadgeCodeRequest{
    PayCode: tea.String("dingbadgexxxx"),
    RequestId: tea.String("202103232"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DecodeBadgeCodeWithOptions(decodeBadgeCodeRequest, decodeBadgeCodeHeaders, &util.RuntimeOptions{})
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
    let decodeBadgeCodeHeaders = new $dingtalkbadge_1_0.DecodeBadgeCodeHeaders({ });
    decodeBadgeCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let decodeBadgeCodeRequest = new $dingtalkbadge_1_0.DecodeBadgeCodeRequest({
      payCode: "dingbadgexxxx",
      requestId: "202103232",
    });
    try {
      await client.decodeBadgeCodeWithOptions(decodeBadgeCodeRequest, decodeBadgeCodeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.DecodeBadgeCodeHeaders decodeBadgeCodeHeaders = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.DecodeBadgeCodeHeaders();
            decodeBadgeCodeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.DecodeBadgeCodeRequest decodeBadgeCodeRequest = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.DecodeBadgeCodeRequest
            {
                PayCode = "dingbadgexxxx",
                RequestId = "202103232",
            };
            try
            {
                client.DecodeBadgeCodeWithOptions(decodeBadgeCodeRequest, decodeBadgeCodeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::DecodeBadgeCodeHeaders> decodeBadgeCodeHeaders = make_shared<Alibabacloud_Dingtalkbadge_1_0::DecodeBadgeCodeHeaders>();
  decodeBadgeCodeHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::DecodeBadgeCodeRequest> decodeBadgeCodeRequest = make_shared<Alibabacloud_Dingtalkbadge_1_0::DecodeBadgeCodeRequest>(map<string, boost::any>({
    {"payCode", boost::any(string("dingbadgexxxx"))},
    {"requestId", boost::any(string("202103232"))}
  }));
  try {
    client->decodeBadgeCodeWithOptions(decodeBadgeCodeRequest, decodeBadgeCodeHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| corpId | String | 企业corpId。 |
| userId | String | 员工的userId。 |
| codeType | String | 付款码类型，取值：   - **PURE\_IDENTITY\_CODE**：纯身份码 - **PAY\_IDENTITY\_CODE**：可支付的身份码 |
| alipayCode | String | 支付宝付款码。 |
| userCorpRelationType | String | 用户和企业关系，取值：   - **INTERNAL\_STAFF**：企业内部员工 - **EXTERNAL\_CONTACT**：外部联系人 - **NO\_RELATION**：普通用户与组织无关 |
| codeIdentity | String | 码标识。取值：   - **DT\_IDENTITY**：工牌码 - **DT\_VISITOR**：访客码 - **DT\_CONFERENCE**：会展码 |
| codeId | String | 码ID，例如访客码ID或会展码ID等。 |
| outBizId | String | 外部业务ID，值为[创建钉工牌电子码](1262-create-a-badge-user-instance.md)接口传入的参数requestId。 |
| extInfo | String | 扩展信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "corpId" : "ding1234",
  "userId" : "staffId",
  "codeType" : "PURE_IDENTIFY_CODE",
  "alipayCode" : "2512345678",
  "userCorpRelationType" : "INTERNAL_STAFF",
  "codeIdentity" : "DT_VISITOR",
  "codeId" : "codeIdxxxxx",
  "outBizId" : "xxxx",
  "extInfo" : "{\"authRules\":{}}"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | expiredPayCode | 码已过期 | 码已过期 |
| 400 | requestIdNotConsist | RequestId不一致 | 两次解码传入的requestId不一致 |
| 400 | invalidParameter | 请求对象为空 | 请求对象为空 |
| 400 | invalidParameter | 无效请求参数 | 无效请求参数 |
| 400 | invalidParameter | 存在空参数 | 存在空参数 |
| 400 | missingParameter | 缺少必填参数 | 缺少必填参数 |
| 400 | invalidPayCode | 无效的付款码 | 无效的付款码 |
| 400 | dataNotConsist | 数据不一致 | 数据不一致 |
| 400 | moneyNotConsist | 金额不一致 | 金额不一致 |
| 500 | unknownError | 未知错误 | 未知错误 |
| 500 | callAlipayFail | 调用支付宝异常 | 调用支付宝异常 |
| 500 | callOrgFail | 调用内部通讯录异常 | 调用内部通讯录异常 |
| 500 | accessStorageFail | 调用存储异常 | 调用存储异常 |
