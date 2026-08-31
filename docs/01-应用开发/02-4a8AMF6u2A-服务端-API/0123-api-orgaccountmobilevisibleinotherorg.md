---
title: "授权其他组织查看本组织的企业账号信息"
source_url: "https://open.dingtalk.com/document/development/api-orgaccountmobilevisibleinotherorg"
namespace: "development"
slug: "api-orgaccountmobilevisibleinotherorg"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 授权其他组织查看本组织的企业账号信息"
doc_id: "Yj2lhCCjlN"
updated_at: "2026-06-01 16:06:13"
---

> Source: https://open.dingtalk.com/document/development/api-orgaccountmobilevisibleinotherorg
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 授权其他组织查看本组织的企业账号信息
> Updated: 2026-06-01 16:06:13

# 授权其他组织查看本组织的企业账号信息

授权当前组织的企业账号在加入其他组织之后，在其他组织查看组织的企业账号信息的具体字段

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccounts/mobiles/visibleInOtherOrg |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.OrgAccount.VisiblityInOtherOrg-企业账号加入其他组织后数据可见性权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| toCorpIds | Array of String | 是 | 被授权组织对应corpId列表。  **[!NOTE]**    被授权组织的corpId列表和调用接口的调用者对应 userId，都不能为空且参数出错会导致调用报错。 |
| optUserId | String | 是 | 当前调用接口的调用者对应userId。  **[!NOTE]**    用于数据审计，需填写当前组织下真实的员工userId，否则接口调用会失败。 |
| fields | Array of String | 否 | 授权字段:  **[!NOTE]**  如果fields为空或者空集合表示仅授权mobile（历史版本兼容）   - **mobile**：企业账号手机号。 - **status**： 企业账号停用状态。 |

### 请求示例

HTTP

```
PUT /v1.0/contact/orgAccounts/mobiles/visibleInOtherOrg HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:101w3c04ffa2386da6530e5123bdf260
Content-Type:application/json

{
  "toCorpIds" : [ "ding12345678" ],
  "optUserId" : "102530009661373952",
  "fields" : [ "mobile" ]
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
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.OrgAccountMobileVisibleInOtherOrgHeaders orgAccountMobileVisibleInOtherOrgHeaders = new com.aliyun.dingtalkcontact_1_0.models.OrgAccountMobileVisibleInOtherOrgHeaders();
        orgAccountMobileVisibleInOtherOrgHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.OrgAccountMobileVisibleInOtherOrgRequest orgAccountMobileVisibleInOtherOrgRequest = new com.aliyun.dingtalkcontact_1_0.models.OrgAccountMobileVisibleInOtherOrgRequest()
                .setToCorpIds(java.util.Arrays.asList(
                    "ding12345678"
                ))
                .setOptUserId("102530009661373952")
                .setFields(java.util.Arrays.asList(
                    "mobile"
                ));
        try {
            client.orgAccountMobileVisibleInOtherOrgWithOptions(orgAccountMobileVisibleInOtherOrgRequest, orgAccountMobileVisibleInOtherOrgHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        org_account_mobile_visible_in_other_org_headers = dingtalkcontact__1__0_models.OrgAccountMobileVisibleInOtherOrgHeaders()
        org_account_mobile_visible_in_other_org_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_account_mobile_visible_in_other_org_request = dingtalkcontact__1__0_models.OrgAccountMobileVisibleInOtherOrgRequest(
            to_corp_ids=[
                'ding12345678'
            ],
            opt_user_id='102530009661373952',
            fields=[
                'mobile'
            ]
        )
        try:
            client.org_account_mobile_visible_in_other_org_with_options(org_account_mobile_visible_in_other_org_request, org_account_mobile_visible_in_other_org_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        org_account_mobile_visible_in_other_org_headers = dingtalkcontact__1__0_models.OrgAccountMobileVisibleInOtherOrgHeaders()
        org_account_mobile_visible_in_other_org_headers.x_acs_dingtalk_access_token = '<your access token>'
        org_account_mobile_visible_in_other_org_request = dingtalkcontact__1__0_models.OrgAccountMobileVisibleInOtherOrgRequest(
            to_corp_ids=[
                'ding12345678'
            ],
            opt_user_id='102530009661373952',
            fields=[
                'mobile'
            ]
        )
        try:
            await client.org_account_mobile_visible_in_other_org_with_options_async(org_account_mobile_visible_in_other_org_request, org_account_mobile_visible_in_other_org_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\OrgAccountMobileVisibleInOtherOrgHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\OrgAccountMobileVisibleInOtherOrgRequest;
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
        $orgAccountMobileVisibleInOtherOrgHeaders = new OrgAccountMobileVisibleInOtherOrgHeaders([]);
        $orgAccountMobileVisibleInOtherOrgHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $orgAccountMobileVisibleInOtherOrgRequest = new OrgAccountMobileVisibleInOtherOrgRequest([
            "toCorpIds" => [
                "ding12345678"
            ],
            "optUserId" => "102530009661373952",
            "fields" => [
                "mobile"
            ]
        ]);
        try {
            $client->orgAccountMobileVisibleInOtherOrgWithOptions($orgAccountMobileVisibleInOtherOrgRequest, $orgAccountMobileVisibleInOtherOrgHeaders, new RuntimeOptions([]));
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

  orgAccountMobileVisibleInOtherOrgHeaders := &dingtalkcontact_1_0.OrgAccountMobileVisibleInOtherOrgHeaders{}
  orgAccountMobileVisibleInOtherOrgHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  orgAccountMobileVisibleInOtherOrgRequest := &dingtalkcontact_1_0.OrgAccountMobileVisibleInOtherOrgRequest{
    ToCorpIds: []*string{tea.String("ding12345678")},
    OptUserId: tea.String("102530009661373952"),
    Fields: []*string{tea.String("mobile")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.OrgAccountMobileVisibleInOtherOrgWithOptions(orgAccountMobileVisibleInOtherOrgRequest, orgAccountMobileVisibleInOtherOrgHeaders, &util.RuntimeOptions{})
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
    let orgAccountMobileVisibleInOtherOrgHeaders = new dingtalkcontact_1_0.OrgAccountMobileVisibleInOtherOrgHeaders({ });
    orgAccountMobileVisibleInOtherOrgHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let orgAccountMobileVisibleInOtherOrgRequest = new dingtalkcontact_1_0.OrgAccountMobileVisibleInOtherOrgRequest({
      toCorpIds: [
        'ding12345678'
      ],
      optUserId: '102530009661373952',
      fields: [
        'mobile'
      ],
    });
    try {
      await client.orgAccountMobileVisibleInOtherOrgWithOptions(orgAccountMobileVisibleInOtherOrgRequest, orgAccountMobileVisibleInOtherOrgHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.OrgAccountMobileVisibleInOtherOrgHeaders orgAccountMobileVisibleInOtherOrgHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.OrgAccountMobileVisibleInOtherOrgHeaders();
            orgAccountMobileVisibleInOtherOrgHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.OrgAccountMobileVisibleInOtherOrgRequest orgAccountMobileVisibleInOtherOrgRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.OrgAccountMobileVisibleInOtherOrgRequest
            {
                ToCorpIds = new List<string>
                {
                    "ding12345678"
                },
                OptUserId = "102530009661373952",
                Fields = new List<string>
                {
                    "mobile"
                },
            };
            try
            {
                client.OrgAccountMobileVisibleInOtherOrgWithOptions(orgAccountMobileVisibleInOtherOrgRequest, orgAccountMobileVisibleInOtherOrgHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 接口调用结果 |

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
| 400 | invalid.param | 参数无效 | 无效参数 |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
