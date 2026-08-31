---
title: "获取企业开通应用后的授权信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-authorization-information-after-the-enterprise-activates-the-application-1"
namespace: "development"
slug: "obtains-the-authorization-information-after-the-enterprise-activates-the-application-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "应用授权 > 获取企业开通应用后的授权信息"
doc_id: "K9lVtuKSBB"
updated_at: "2026-08-28 10:26:10"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-authorization-information-after-the-enterprise-activates-the-application-1
> Path: 应用开发 / 服务端 API / 应用授权 > 获取企业开通应用后的授权信息
> Updated: 2026-08-28 10:26:10

# 获取企业开通应用后的授权信息

第三方企业可调用本接口获取企业开通应用后的授权信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/oauth2/apps/authInfo |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_base-三方应用开通使用基础权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | BExxx | 调用该接口的访问凭证，可通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| authCorpId | String | 是 | dingxxx | 授权企业的corpId。 |

### **请求体示例**

HTTP

```
GET /v1.0/oauth2/apps/authInfo?authCorpId=dingxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkoauth2_1_0.*;
import com.aliyun.dingtalkoauth2_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoauth2_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkoauth2_1_0.Client client = Sample.createClient();
        GetAuthInfoHeaders getAuthInfoHeaders = new GetAuthInfoHeaders();
        getAuthInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetAuthInfoRequest getAuthInfoRequest = new GetAuthInfoRequest()
                .setAuthCorpId("dingxxx");
        try {
            client.getAuthInfoWithOptions(getAuthInfoRequest, getAuthInfoHeaders, new RuntimeOptions());
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
        get_auth_info_headers = dingtalkoauth_2__1__0_models.GetAuthInfoHeaders()
        get_auth_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_auth_info_request = dingtalkoauth_2__1__0_models.GetAuthInfoRequest(
            auth_corp_id='dingxxx'
        )
        try:
            client.get_auth_info_with_options(get_auth_info_request, get_auth_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_auth_info_headers = dingtalkoauth_2__1__0_models.GetAuthInfoHeaders()
        get_auth_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_auth_info_request = dingtalkoauth_2__1__0_models.GetAuthInfoRequest(
            auth_corp_id='dingxxx'
        )
        try:
            await client.get_auth_info_with_options_async(get_auth_info_request, get_auth_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetAuthInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetAuthInfoRequest;
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
        $getAuthInfoHeaders = new GetAuthInfoHeaders([]);
        $getAuthInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getAuthInfoRequest = new GetAuthInfoRequest([
            "authCorpId" => "dingxxx"
        ]);
        try {
            $client->getAuthInfoWithOptions($getAuthInfoRequest, $getAuthInfoHeaders, new RuntimeOptions([]));
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
  dingtalkoauth2_1_0  "github.com/alibabacloud-go/dingtalk/oauth2_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  getAuthInfoHeaders := &dingtalkoauth2_1_0.GetAuthInfoHeaders{}
  getAuthInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getAuthInfoRequest := &dingtalkoauth2_1_0.GetAuthInfoRequest{
    AuthCorpId: tea.String("dingxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAuthInfoWithOptions(getAuthInfoRequest, getAuthInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkoauth2_1_0, * as $dingtalkoauth2_1_0 from '@alicloud/dingtalk/oauth2_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkoauth2_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkoauth2_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getAuthInfoHeaders = new $dingtalkoauth2_1_0.GetAuthInfoHeaders({ });
    getAuthInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getAuthInfoRequest = new $dingtalkoauth2_1_0.GetAuthInfoRequest({
      authCorpId: "dingxxx",
    });
    try {
      await client.getAuthInfoWithOptions(getAuthInfoRequest, getAuthInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetAuthInfoHeaders getAuthInfoHeaders = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetAuthInfoHeaders();
            getAuthInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetAuthInfoRequest getAuthInfoRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetAuthInfoRequest
            {
                AuthCorpId = "dingxxx",
            };
            try
            {
                client.GetAuthInfoWithOptions(getAuthInfoRequest, getAuthInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| authAppInfo | Object |  | 授权应用信息。 |
| agentList | Array |  | 应用列表。 |
| agentId | Long | 888 | 应用ID。 |
| agentName | String | 小程序DEMO | 应用名称。 |
| appId | Long | 111 | 第三方应用ID。 |
| adminList | Array of String | [ "manager975" ] | 对此微应用有管理权限的管理员userid列表。 |
| authCorpInfo | Object |  | 应用企业信息。 |
| inviteCode | String | 111 | 邀请码。    只有自己邀请的企业才会返回邀请码，可用该邀请码统计不同渠道的拉新，否则值为空字符串。 |
| industry | String | 201 | 企业所属行业。 |
| corpName | String | 小程序体验HTTP | 授权方企业名称。 |
| licenseCode | String | 111 | 序列号。 |
| authChannel | String | 123 | 渠道码。 |
| authChannelType | String | 1 | 渠道类型。  返回值可能为空，非空时当前只有**满天星类型**，值为**STAR\_ACTIVITY**。    为了避免渠道码重复，可与渠道码共同确认渠道。 |
| authLevel | Long | 1 | 企业认证等级，取值：   - **0**：未认证 - **1**：高级认证 - **2**：中级认证 - **3**：初级认证 |
| inviteUrl | String | https://wx.dingtalk.com/invite-page/xxx | 企业邀请链接。 |
| corpLogoUrl | String | https://static-legacy.dingtalk.com/xxx | 企业logo。 |
| authUserInfo | Object |  | 授权用户信息。 |
| userId | String | manager975 | 授权管理员userid。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "authAppInfo" : {
    "agentList" : [ {
      "agentId" : 888,
      "agentName" : "小程序DEMO",
      "appId" : 111,
      "adminList" : [ "manager975" ]
    } ]
  },
  "authCorpInfo" : {
    "inviteCode" : "111",
    "industry" : "201",
    "corpName" : "小程序体验HTTP",
    "licenseCode" : "111",
    "authChannel" : "123",
    "authChannelType" : "1",
    "authLevel" : 1,
    "inviteUrl" : "https://wx.dingtalk.com/invite-page/xxx",
    "corpLogoUrl" : "https://static-legacy.dingtalk.com/xxx"
  },
  "authUserInfo" : {
    "userId" : "manager975"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgNotExist | 企业已解散 | 企业已解散 |
| 400 | orgNotAuthApp | 企业未授权开通应用 | 企业未授权开通应用 |
| 400 | invalidCorpId | 参数错误 | 参数错误 |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
