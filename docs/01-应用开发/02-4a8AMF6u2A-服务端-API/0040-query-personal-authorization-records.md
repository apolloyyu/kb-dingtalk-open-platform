---
title: "查询个人授权记录"
source_url: "https://open.dingtalk.com/document/development/query-personal-authorization-records"
namespace: "development"
slug: "query-personal-authorization-records"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 授权套件 > 查询个人授权记录"
doc_id: "loBxU9dL4a"
updated_at: "2026-08-28 10:26:07"
---

> Source: https://open.dingtalk.com/document/development/query-personal-authorization-records
> Path: 应用开发 / 服务端 API / 认证与授权 > 授权套件 > 查询个人授权记录
> Updated: 2026-08-28 10:26:07

# 查询个人授权记录

当需要查询用户的授权记录信息时，可以调用本接口获取用户的个人授权详情。该接口适用于用户隐私权限审计、第三方应用授权状态同步等场景，帮助开发者在用户登录后检查其已授予的敏感权限列表，用于前端界面展示或安全合规审查。

## 接口调用说明

例如下图所示，用户已授权手机号和个人基本信息两项权限，调用本接口可获取当前用户已授权的具体权限点，返回结果如下：

`{ "result": [ { "resource": "rpc_auth", "authItems": [ "Contact.User.Read" ] }, { "resource": "Contact.User", "authItems": [ "mobile" ] } ] }`

![](https://img.alicdn.com/imgextra/i3/O1CN01XZ9URj1NU1M6t6sx8_!!6000000001572-2-tps-352-596.png)

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/authRules/user |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-snsapi\_base-调用SNS API时需要具备的基本权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 获取用户个人身份访问凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/oauth2/authRules/user HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1457a6xxx
Content-Type:application/json
```

Java

```
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
    public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoauth2_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkoauth2_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkoauth2_1_0.models.GetPersonalAuthRuleHeaders getPersonalAuthRuleHeaders = new com.aliyun.dingtalkoauth2_1_0.models.GetPersonalAuthRuleHeaders();
        getPersonalAuthRuleHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getPersonalAuthRuleWithOptions(getPersonalAuthRuleHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkoauth2_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkoauth2_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_personal_auth_rule_headers = dingtalkoauth_2__1__0_models.GetPersonalAuthRuleHeaders()
        get_personal_auth_rule_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_personal_auth_rule_with_options(get_personal_auth_rule_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_personal_auth_rule_headers = dingtalkoauth_2__1__0_models.GetPersonalAuthRuleHeaders()
        get_personal_auth_rule_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_personal_auth_rule_with_options_async(get_personal_auth_rule_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetPersonalAuthRuleHeaders;
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
        $getPersonalAuthRuleHeaders = new GetPersonalAuthRuleHeaders([]);
        $getPersonalAuthRuleHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getPersonalAuthRuleWithOptions($getPersonalAuthRuleHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkoauth2_1_0  "github.com/alibabacloud-go/dingtalk/oauth2_1_0"
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
func CreateClient () (_result *dingtalkoauth2_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkoauth2_1_0.Client{}
  _result, _err = dingtalkoauth2_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getPersonalAuthRuleHeaders := &dingtalkoauth2_1_0.GetPersonalAuthRuleHeaders{}
  getPersonalAuthRuleHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetPersonalAuthRuleWithOptions(getPersonalAuthRuleHeaders, &util.RuntimeOptions{})
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
const dingtalkoauth2_1_0 = require('@alicloud/dingtalk/oauth2_1_0');
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
    return new dingtalkoauth2_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getPersonalAuthRuleHeaders = new dingtalkoauth2_1_0.GetPersonalAuthRuleHeaders({ });
    getPersonalAuthRuleHeaders.xAcsDingtalkAccessToken = '<your access token>';
    try {
      await client.getPersonalAuthRuleWithOptions(getPersonalAuthRuleHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalkoauth2_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetPersonalAuthRuleHeaders getPersonalAuthRuleHeaders = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetPersonalAuthRuleHeaders();
            getPersonalAuthRuleHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetPersonalAuthRuleWithOptions(getPersonalAuthRuleHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 授权记录列表。 |
| resource | String | 授权实体。 |
| authItems | Array of String | 授权项。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "resource" : "Contact.User",
    "authItems" : [ "mobile" ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
