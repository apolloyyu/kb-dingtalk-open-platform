---
title: "判断用户是否是认证组织的语文老师接口"
source_url: "https://open.dingtalk.com/document/development/api-isyuwencertifiedteacher"
namespace: "development"
slug: "api-isyuwencertifiedteacher"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 判断用户是否是认证组织的语文老师接口"
doc_id: "QfOKo9P0VK"
updated_at: "2026-06-08 09:48:21"
---

> Source: https://open.dingtalk.com/document/development/api-isyuwencertifiedteacher
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 判断用户是否是认证组织的语文老师接口
> Updated: 2026-06-08 09:48:21

# 判断用户是否是认证组织的语文老师接口

调用本接口，根据userId和业务code，判断用户是否是认证组织的语文老师接口。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/paas/certifiedTeachers/chineseTeachers/check |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该API的应用凭证，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 可通过根据手机号获取userid接口获取userid；长度限制1～50个字符。 |
| bizCode | String | 是 | 三方ISV接入的业务编码，长度限制1～50个字符。 |

### **请求示例**

HTTP

```
POST /v1.0/edu/paas/certifiedTeachers/chineseTeachers/check HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b9517332f5753ada8c5b35ee1752fe74
Content-Type:application/json

{
  "userId" : "1737009576001",
  "bizCode" : "EDU_HW_TEST"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkedu_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkedu_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkedu_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkedu_1_0.models.IsYuwenCertifiedTeacherHeaders isYuwenCertifiedTeacherHeaders = new com.aliyun.dingtalkedu_1_0.models.IsYuwenCertifiedTeacherHeaders();
        isYuwenCertifiedTeacherHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.IsYuwenCertifiedTeacherRequest isYuwenCertifiedTeacherRequest = new com.aliyun.dingtalkedu_1_0.models.IsYuwenCertifiedTeacherRequest()
                .setUserId("1737009576001")
                .setBizCode("EDU_HW_TEST");
        try {
            client.isYuwenCertifiedTeacherWithOptions(isYuwenCertifiedTeacherRequest, isYuwenCertifiedTeacherHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.edu_1_0.client import Client as dingtalkedu_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.edu_1_0 import models as dingtalkedu__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkedu_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkedu_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        is_yuwen_certified_teacher_headers = dingtalkedu__1__0_models.IsYuwenCertifiedTeacherHeaders()
        is_yuwen_certified_teacher_headers.x_acs_dingtalk_access_token = '<your access token>'
        is_yuwen_certified_teacher_request = dingtalkedu__1__0_models.IsYuwenCertifiedTeacherRequest(
            user_id='1737009576001',
            biz_code='EDU_HW_TEST'
        )
        try:
            client.is_yuwen_certified_teacher_with_options(is_yuwen_certified_teacher_request, is_yuwen_certified_teacher_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        is_yuwen_certified_teacher_headers = dingtalkedu__1__0_models.IsYuwenCertifiedTeacherHeaders()
        is_yuwen_certified_teacher_headers.x_acs_dingtalk_access_token = '<your access token>'
        is_yuwen_certified_teacher_request = dingtalkedu__1__0_models.IsYuwenCertifiedTeacherRequest(
            user_id='1737009576001',
            biz_code='EDU_HW_TEST'
        )
        try:
            await client.is_yuwen_certified_teacher_with_options_async(is_yuwen_certified_teacher_request, is_yuwen_certified_teacher_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\IsYuwenCertifiedTeacherHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\IsYuwenCertifiedTeacherRequest;
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
        $isYuwenCertifiedTeacherHeaders = new IsYuwenCertifiedTeacherHeaders([]);
        $isYuwenCertifiedTeacherHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $isYuwenCertifiedTeacherRequest = new IsYuwenCertifiedTeacherRequest([
            "userId" => "1737009576001",
            "bizCode" => "EDU_HW_TEST"
        ]);
        try {
            $client->isYuwenCertifiedTeacherWithOptions($isYuwenCertifiedTeacherRequest, $isYuwenCertifiedTeacherHeaders, new RuntimeOptions([]));
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
  dingtalkedu_1_0  "github.com/alibabacloud-go/dingtalk/edu_1_0"
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
func CreateClient () (_result *dingtalkedu_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkedu_1_0.Client{}
  _result, _err = dingtalkedu_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  isYuwenCertifiedTeacherHeaders := &dingtalkedu_1_0.IsYuwenCertifiedTeacherHeaders{}
  isYuwenCertifiedTeacherHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  isYuwenCertifiedTeacherRequest := &dingtalkedu_1_0.IsYuwenCertifiedTeacherRequest{
    UserId: tea.String("1737009576001"),
    BizCode: tea.String("EDU_HW_TEST"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.IsYuwenCertifiedTeacherWithOptions(isYuwenCertifiedTeacherRequest, isYuwenCertifiedTeacherHeaders, &util.RuntimeOptions{})
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
const dingtalkedu_1_0 = require('@alicloud/dingtalk/edu_1_0');
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
    return new dingtalkedu_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let isYuwenCertifiedTeacherHeaders = new dingtalkedu_1_0.IsYuwenCertifiedTeacherHeaders({ });
    isYuwenCertifiedTeacherHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let isYuwenCertifiedTeacherRequest = new dingtalkedu_1_0.IsYuwenCertifiedTeacherRequest({
      userId: '1737009576001',
      bizCode: 'EDU_HW_TEST',
    });
    try {
      await client.isYuwenCertifiedTeacherWithOptions(isYuwenCertifiedTeacherRequest, isYuwenCertifiedTeacherHeaders, new Util.RuntimeOptions({ }));
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkedu_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkedu_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkedu_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.IsYuwenCertifiedTeacherHeaders isYuwenCertifiedTeacherHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.IsYuwenCertifiedTeacherHeaders();
            isYuwenCertifiedTeacherHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.IsYuwenCertifiedTeacherRequest isYuwenCertifiedTeacherRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.IsYuwenCertifiedTeacherRequest
            {
                UserId = "1737009576001",
                BizCode = "EDU_HW_TEST",
            };
            try
            {
                client.IsYuwenCertifiedTeacherWithOptions(isYuwenCertifiedTeacherRequest, isYuwenCertifiedTeacherHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 判断接口调用是否正常返回。 |
| result | Boolean | 是否为认证组织的语文老师。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 200 | parameterInvalid | PARAMETER\_INVALID | 非法的业务编码 |
