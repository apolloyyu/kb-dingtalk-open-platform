---
title: "根据手机号获取候选人信息"
source_url: "https://open.dingtalk.com/document/development/obtain-candidate-information-based-on-mobile-phone-number"
namespace: "development"
slug: "obtain-candidate-information-based-on-mobile-phone-number"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 根据手机号获取候选人信息"
doc_id: "vJ2QsVvhhG"
updated_at: "2026-06-04 19:10:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-candidate-information-based-on-mobile-phone-number
> Path: 应用开发 / 服务端 API / 智能招聘 > 根据手机号获取候选人信息
> Updated: 2026-06-04 19:10:33

# 根据手机号获取候选人信息

根据手机号获取候选人信息，包括候选人标识和候选人名字。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/candidates |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_recruitment\_plugin-智能招聘插件管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizCode | String | 否 | 业务标识，默认值为`ddats`。    如果传该参数，只支持`ddats`。 |
| phoneNumber | String | 是 | 候选人手机号。    可以在智能招聘应用的候选人信息中获取。 |

### 请求示例

HTTP

```
GET /v1.0/ats/candidates?bizCode=ddats&phoneNumber=136xxxx8888 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
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
    public static com.aliyun.dingtalkats_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkats_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkats_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkats_1_0.models.GetCandidateByPhoneNumberHeaders getCandidateByPhoneNumberHeaders = new com.aliyun.dingtalkats_1_0.models.GetCandidateByPhoneNumberHeaders();
        getCandidateByPhoneNumberHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkats_1_0.models.GetCandidateByPhoneNumberRequest getCandidateByPhoneNumberRequest = new com.aliyun.dingtalkats_1_0.models.GetCandidateByPhoneNumberRequest()
                .setBizCode("ddats")
                .setPhoneNumber("136xxxx8888");
        try {
            client.getCandidateByPhoneNumberWithOptions(getCandidateByPhoneNumberRequest, getCandidateByPhoneNumberHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.ats_1_0.client import Client as dingtalkats_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.ats_1_0 import models as dingtalkats__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkats_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkats_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_candidate_by_phone_number_headers = dingtalkats__1__0_models.GetCandidateByPhoneNumberHeaders()
        get_candidate_by_phone_number_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_candidate_by_phone_number_request = dingtalkats__1__0_models.GetCandidateByPhoneNumberRequest(
            biz_code='ddats',
            phone_number='136xxxx8888'
        )
        try:
            client.get_candidate_by_phone_number_with_options(get_candidate_by_phone_number_request, get_candidate_by_phone_number_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_candidate_by_phone_number_headers = dingtalkats__1__0_models.GetCandidateByPhoneNumberHeaders()
        get_candidate_by_phone_number_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_candidate_by_phone_number_request = dingtalkats__1__0_models.GetCandidateByPhoneNumberRequest(
            biz_code='ddats',
            phone_number='136xxxx8888'
        )
        try:
            await client.get_candidate_by_phone_number_with_options_async(get_candidate_by_phone_number_request, get_candidate_by_phone_number_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\GetCandidateByPhoneNumberHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\GetCandidateByPhoneNumberRequest;
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
        $getCandidateByPhoneNumberHeaders = new GetCandidateByPhoneNumberHeaders([]);
        $getCandidateByPhoneNumberHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getCandidateByPhoneNumberRequest = new GetCandidateByPhoneNumberRequest([
            "bizCode" => "ddats",
            "phoneNumber" => "136xxxx8888"
        ]);
        try {
            $client->getCandidateByPhoneNumberWithOptions($getCandidateByPhoneNumberRequest, $getCandidateByPhoneNumberHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkats_1_0  "github.com/alibabacloud-go/dingtalk/ats_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkats_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkats_1_0.Client{}
  _result, _err = dingtalkats_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getCandidateByPhoneNumberHeaders := &dingtalkats_1_0.GetCandidateByPhoneNumberHeaders{}
  getCandidateByPhoneNumberHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getCandidateByPhoneNumberRequest := &dingtalkats_1_0.GetCandidateByPhoneNumberRequest{
    BizCode: tea.String("ddats"),
    PhoneNumber: tea.String("136xxxx8888"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetCandidateByPhoneNumberWithOptions(getCandidateByPhoneNumberRequest, getCandidateByPhoneNumberHeaders, &util.RuntimeOptions{})
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
import dingtalkats_1_0, * as $dingtalkats_1_0 from '@alicloud/dingtalk/ats_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkats_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkats_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getCandidateByPhoneNumberHeaders = new $dingtalkats_1_0.GetCandidateByPhoneNumberHeaders({ });
    getCandidateByPhoneNumberHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getCandidateByPhoneNumberRequest = new $dingtalkats_1_0.GetCandidateByPhoneNumberRequest({
      bizCode: "ddats",
      phoneNumber: "136xxxx8888",
    });
    try {
      await client.getCandidateByPhoneNumberWithOptions(getCandidateByPhoneNumberRequest, getCandidateByPhoneNumberHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkats_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkats_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkats_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetCandidateByPhoneNumberHeaders getCandidateByPhoneNumberHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetCandidateByPhoneNumberHeaders();
            getCandidateByPhoneNumberHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetCandidateByPhoneNumberRequest getCandidateByPhoneNumberRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetCandidateByPhoneNumberRequest
            {
                BizCode = "ddats",
                PhoneNumber = "136xxxx8888",
            };
            try
            {
                client.GetCandidateByPhoneNumberWithOptions(getCandidateByPhoneNumberRequest, getCandidateByPhoneNumberHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| candidateId | String | 候选人标识。 |
| name | String | 候选人姓名。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "candidateId" : "xxx",
  "name" : "张三"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | %s | 无效参数 |
| 404 | candidate.notExists | 候选人不存在 | 候选人不存在 |
| 500 | systemError | 系统错误 | 系统错误 |
