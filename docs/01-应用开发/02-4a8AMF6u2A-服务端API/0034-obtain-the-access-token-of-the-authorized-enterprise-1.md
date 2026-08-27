---
title: "获取第三方应用授权企业的accessToken"
source_url: "https://open.dingtalk.com/document/development/obtain-the-access-token-of-the-authorized-enterprise-1"
namespace: "development"
slug: "obtain-the-access-token-of-the-authorized-enterprise-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "认证与授权 > 访问凭证 > 应用身份凭证 > 获取第三方应用授权企业的accessToken"
doc_id: "QXkyTi5zqS"
updated_at: "2026-06-08 12:02:03"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-access-token-of-the-authorized-enterprise-1
> Path: 应用开发 / 服务端API / 认证与授权 > 访问凭证 > 应用身份凭证 > 获取第三方应用授权企业的accessToken
> Updated: 2026-06-08 12:02:03

# 获取第三方应用授权企业的accessToken

产品服务商可通过此接口获取授权企业的accessToken。当第三方企业应用调用服务端API获取应用资源时，使用获取的accessToken进行身份验证。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/oauth2/corpAccessToken |
| HTTP Method | POST |
| 支持的应用类型 | `appType-企业内部应用（委托产品服务商）``appType-第三方企业应用` |
| 权限要求 | `permission-isvapi_base-三方应用开通使用基础权限` |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| suiteKey | String | 是 | 已创建的第三方企业应用的 Cilent ID（原第三方企业应用SuiteKey）。 |
| suiteSecret | String | 是 | 已创建的第三方企业应用的 Cilent Secret（原第三方企业应用SuiteSecret）。 |
| authCorpId | String | 是 | 授权企业的CorpId。   - 网页应用（H5）：  你可以在应用首页地址/PC端首页地址添加参数`corpid=$CORPID$`，例如：https://example.com?corpid=$CORPID$，当从工作台访问该应用时，会将 $CORPID$ 自动解析为当前访问用户所在的组织 ID。   image.png - 小程序：  使用客户端[corpId](../03-Ogu5SlPY4t-客户端JSAPI/0025-jsapi-corp-id.md)接口获取。 |
| suiteTicket | String | 是 | 钉钉推送的suiteTicket，获取步骤：   1. 接入第三方企业应用的事件订阅，请参考[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)。 2. 事件订阅配置成功时，钉钉会定期推送授权事件[套件票据](../04-LFcRvVD08N-事件订阅/0006-event-suite-ticket.md)内的 suiteTicket 值。  **[!NOTE]**  suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。 |

### **请求示例**

HTTP

```
POST /v1.0/oauth2/corpAccessToken HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1cc1bb3xxxx
Content-Type:application/json

{
  "suiteKey" : "suitep1f5lzyglm7fryxxxx",
  "suiteSecret" : "_FP5PpZF3irDKjxxx",
  "authCorpId" : "ding123456",
  "suiteTicket" : "1f5lzyglm7fryxxxx"
}
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
    public static com.aliyun.dingtalkoauth2_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoauth2_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkoauth2_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkoauth2_1_0.models.GetCorpAccessTokenRequest getCorpAccessTokenRequest = new com.aliyun.dingtalkoauth2_1_0.models.GetCorpAccessTokenRequest()
                .setSuiteKey("suitep1f5lzyglm7fryxxxx")
                .setSuiteSecret("_FP5PpZF3irDKjxxx")
                .setAuthCorpId("ding123456")
                .setSuiteTicket("1f5lzyglm7fryxxxx");
        try {
            client.getCorpAccessToken(getCorpAccessTokenRequest);
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
        get_corp_access_token_request = dingtalkoauth_2__1__0_models.GetCorpAccessTokenRequest(
            suite_key='suitep1f5lzyglm7fryxxxx',
            suite_secret='_FP5PpZF3irDKjxxx',
            auth_corp_id='ding123456',
            suite_ticket='1f5lzyglm7fryxxxx'
        )
        try:
            client.get_corp_access_token(get_corp_access_token_request)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_corp_access_token_request = dingtalkoauth_2__1__0_models.GetCorpAccessTokenRequest(
            suite_key='suitep1f5lzyglm7fryxxxx',
            suite_secret='_FP5PpZF3irDKjxxx',
            auth_corp_id='ding123456',
            suite_ticket='1f5lzyglm7fryxxxx'
        )
        try:
            await client.get_corp_access_token_async(get_corp_access_token_request)
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
use AlibabaCloud\SDK\Dingtalk\Voauth2_1_0\Models\GetCorpAccessTokenRequest;

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
        $getCorpAccessTokenRequest = new GetCorpAccessTokenRequest([
            "suiteKey" => "suitep1f5lzyglm7fryxxxx",
            "suiteSecret" => "_FP5PpZF3irDKjxxx",
            "authCorpId" => "ding123456",
            "suiteTicket" => "1f5lzyglm7fryxxxx"
        ]);
        try {
            $client->getCorpAccessToken($getCorpAccessTokenRequest);
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

  getCorpAccessTokenRequest := &dingtalkoauth2_1_0.GetCorpAccessTokenRequest{
    SuiteKey: tea.String("suitep1f5lzyglm7fryxxxx"),
    SuiteSecret: tea.String("_FP5PpZF3irDKjxxx"),
    AuthCorpId: tea.String("ding123456"),
    SuiteTicket: tea.String("1f5lzyglm7fryxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetCorpAccessToken(getCorpAccessTokenRequest)
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
import Util from '@alicloud/tea-util';
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
    let getCorpAccessTokenRequest = new $dingtalkoauth2_1_0.GetCorpAccessTokenRequest({
      suiteKey: "suitep1f5lzyglm7fryxxxx",
      suiteSecret: "_FP5PpZF3irDKjxxx",
      authCorpId: "ding123456",
      suiteTicket: "1f5lzyglm7fryxxxx",
    });
    try {
      await client.getCorpAccessToken(getCorpAccessTokenRequest);
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
            AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetCorpAccessTokenRequest getCorpAccessTokenRequest = new AlibabaCloud.SDK.Dingtalkoauth2_1_0.Models.GetCorpAccessTokenRequest
            {
                SuiteKey = "suitep1f5lzyglm7fryxxxx",
                SuiteSecret = "_FP5PpZF3irDKjxxx",
                AuthCorpId = "ding123456",
                SuiteTicket = "1f5lzyglm7fryxxxx",
            };
            try
            {
                client.GetCorpAccessToken(getCorpAccessTokenRequest);
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
| accessToken | String | 定制应用的的accessToken。  **[!NOTE]**  在使用accessToken时，请注意：   - 开发者需要缓存accessToken，用于后续接口的调用。因为每个应用的accessToken是彼此独立的，所以进行缓存时需要区分应用来进行存储。 - 不能频繁调用gettoken接口，否则会受到频率拦截。 |
| expireIn | Long | 定制应用的accessToken超时时间，单位秒。  **[!NOTE]**  accessToken的有效期为7200秒（2小时），有效期内重复获取会返回新的accessToken。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "accessToken" : "1cc1bb3xxxx",
  "expireIn" : 7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidSuiteKey | suitekey不合法 | suitekey不合法 |
| 400 | invalidSuiteTicket | suiteTicket无效 | suiteTicket无效 |
| 400 | invalidAuthInfo | 授权关系不存在 | 企业未开通对应的三方应用，无法获取该企业token |
