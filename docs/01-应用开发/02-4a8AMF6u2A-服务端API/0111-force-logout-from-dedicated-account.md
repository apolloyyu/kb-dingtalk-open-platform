---
title: "强制登出企业账号"
source_url: "https://open.dingtalk.com/document/development/force-logout-from-dedicated-account"
namespace: "development"
slug: "force-logout-from-dedicated-account"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 企业账号 > 强制登出企业账号"
doc_id: "KHdTU3eTH3"
updated_at: "2026-06-01 15:50:16"
---

> Source: https://open.dingtalk.com/document/development/force-logout-from-dedicated-account
> Path: 应用开发 / 服务端API / 通讯录管理 > 企业账号 > 强制登出企业账号
> Updated: 2026-06-01 15:50:16

# 强制登出企业账号

调用本接口，强制登出指定的企业账号。

## 接口调用说明

在某些特定场景中，如果需要紧急强制登出某企业账号时，可以调用本接口执行强制登出。

登出后，用户侧钉钉显示如下图：

![](https://img.alicdn.com/imgextra/i4/O1CN01y1CTHh1NqSkACLAap_!!6000000001621-2-tps-300-649.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccounts/signOut |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.OrgAccountSecurity.ReadWrite-通讯录企业账号安全数据读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 企业账号的userid，可通过以下四种方式获得：   - [根据手机号查询企业账号用户](0117-obtain-the-userid-of-your-mobile-phone-number.md) - [创建SSO企业账号](0104-create-an-sso-account.md) - [创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md) - [邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md) |
| reason | String | 否 | 企业账号强制登出的原因(显示在钉钉管理后台审计日志) |
| reasonI18nForEmployee | Map<String, String> | 否 | - 企业账号强制登出的原因(显示给员工查看) - 例子：{"zh\_CN":"登出原因","en\_US":"Reason for logging out"} - 支持的语言参考钉钉客户端当前的语言。例如："zh\_CN", "zh\_HK", "zh\_TW", "en\_US", "ja\_JP","vi\_VN", "fr\_FR", "ru\_RU", "ko\_KR", "es\_LA","tr\_TR", "pt\_BR", "ms\_MY", "id\_ID", "th\_TH" |

### 请求示例

HTTP

```
POST /v1.0/contact/orgAccounts/signOut HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "userId" : "user123",
  "reason" : "账号停用",
  "reasonI18nForEmployee" : {
    {"zh_CN":"管理员已经将你的账号退出登录，如有疑问请联系管理员"}
  }
}
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
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.SignOutHeaders signOutHeaders = new com.aliyun.dingtalkcontact_1_0.models.SignOutHeaders();
        signOutHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> reasonI18nForEmployee = TeaConverter.buildMap(
            new TeaPair("key", "-")
        );
        com.aliyun.dingtalkcontact_1_0.models.SignOutRequest signOutRequest = new com.aliyun.dingtalkcontact_1_0.models.SignOutRequest()
                .setUserId("user123")
                .setReason("账号停用")
                .setReasonI18nForEmployee(reasonI18nForEmployee)
                .setOpenDeviceId("-");
        try {
            client.signOutWithOptions(signOutRequest, signOutHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sign_out_headers = dingtalkcontact__1__0_models.SignOutHeaders()
        sign_out_headers.x_acs_dingtalk_access_token = '<your access token>'
        reason_i18n_for_employee = {
            'key': '-'
        }
        sign_out_request = dingtalkcontact__1__0_models.SignOutRequest(
            user_id='user123',
            reason='账号停用',
            reason_i18n_for_employee=reason_i18n_for_employee,
            open_device_id='-'
        )
        try:
            client.sign_out_with_options(sign_out_request, sign_out_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sign_out_headers = dingtalkcontact__1__0_models.SignOutHeaders()
        sign_out_headers.x_acs_dingtalk_access_token = '<your access token>'
        reason_i18n_for_employee = {
            'key': '-'
        }
        sign_out_request = dingtalkcontact__1__0_models.SignOutRequest(
            user_id='user123',
            reason='账号停用',
            reason_i18n_for_employee=reason_i18n_for_employee,
            open_device_id='-'
        )
        try:
            await client.sign_out_with_options_async(sign_out_request, sign_out_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\SignOutHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\SignOutRequest;
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
        $signOutHeaders = new SignOutHeaders([]);
        $signOutHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $reasonI18nForEmployee = [
            "key" => "-"
        ];
        $signOutRequest = new SignOutRequest([
            "userId" => "user123",
            "reason" => "账号停用",
            "reasonI18nForEmployee" => $reasonI18nForEmployee,
            "openDeviceId" => "-"
        ]);
        try {
            $client->signOutWithOptions($signOutRequest, $signOutHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
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
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  signOutHeaders := &dingtalkcontact_1_0.SignOutHeaders{}
  signOutHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  reasonI18nForEmployee := map[string]*string{
    "key": tea.String("-"),
  }
  signOutRequest := &dingtalkcontact_1_0.SignOutRequest{
    UserId: tea.String("user123"),
    Reason: tea.String("账号停用"),
    ReasonI18nForEmployee: reasonI18nForEmployee,
    OpenDeviceId: tea.String("-"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SignOutWithOptions(signOutRequest, signOutHeaders, &util.RuntimeOptions{})
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
const dingtalkcontact_1_0 = require('@alicloud/dingtalk/contact_1_0');
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
    return new dingtalkcontact_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let signOutHeaders = new dingtalkcontact_1_0.SignOutHeaders({ });
    signOutHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let reasonI18nForEmployee = {
      key: '-',
    };
    let signOutRequest = new dingtalkcontact_1_0.SignOutRequest({
      userId: 'user123',
      reason: '账号停用',
      reasonI18nForEmployee: reasonI18nForEmployee,
      openDeviceId: '-',
    });
    try {
      await client.signOutWithOptions(signOutRequest, signOutHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SignOutHeaders signOutHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SignOutHeaders();
            signOutHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> reasonI18nForEmployee = new Dictionary<string, string>
            {
                {"key", "-"},
            };
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SignOutRequest signOutRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SignOutRequest
            {
                UserId = "user123",
                Reason = "账号停用",
                ReasonI18nForEmployee = reasonI18nForEmployee,
                OpenDeviceId = "-",
            };
            try
            {
                client.SignOutWithOptions(signOutRequest, signOutHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 退出是否成功，true表示成功。 |

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
| 400 | invalid.param | 无效参数 | 无效参数 |
| 400 | user.not.exist | 用户不存在 | 用户不存在 |
| 400 | exclusive.account.only | 只能操作归属该组织的专属账号 | 只能操作归属该组织的专属账号 |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
