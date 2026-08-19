---
title: "获取跳转到企业实名的地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-address-that-is-redirected-to-the-enterprise-s-real"
namespace: "development"
slug: "obtain-the-address-that-is-redirected-to-the-enterprise-s-real"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 用户 > 获取跳转到企业实名的地址"
doc_id: "rwk2w54Puq"
updated_at: "2025-09-23 19:21:40"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-address-that-is-redirected-to-the-enterprise-s-real
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 用户 > 获取跳转到企业实名的地址
> Updated: 2025-09-23 19:21:40

# 获取跳转到企业实名的地址

通过企业信息接口查询到企业未实名时，可调用本接口获取实名地址，在应用内展示给企业。

## 接口调用说明

企业在e签宝进行实名认证时，只能由企业的管理员或子管理员操作，因此实名入口的展示建议做权限判断，只展示给企业管理员。因e签宝应用首页也有实名入口，此企业实名入口展示非必须，ISV可实际需求处理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/corps/realnames |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-E签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceGroup | String | 否 | 预留参数，此版本无需此参数。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 当前用户userid。      必须是管理员。 |
| redirectUrl | String | 否 | 企业实名操作成功后的重定向地址。  **[!NOTE]**  地址有效期为2小时。 |

### 请求示例

HTTP

```
POST /v2.0/esign/corps/realnames HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "userId" : "manager1122",
  "redirectUrl" : "http://xxx.com"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_2_0.*;
import com.aliyun.dingtalkesign_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_2_0.Client client = Sample.createClient();
        CorpRealnameHeaders corpRealnameHeaders = new CorpRealnameHeaders();
        corpRealnameHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CorpRealnameRequest corpRealnameRequest = new CorpRealnameRequest()
                .setUserId("manager1122")
                .setRedirectUrl("http://xxx.com");
        try {
            client.corpRealnameWithOptions(corpRealnameRequest, corpRealnameHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_2_0.client import Client as dingtalkesign_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        corp_realname_headers = dingtalkesign__2__0_models.CorpRealnameHeaders()
        corp_realname_headers.x_acs_dingtalk_access_token = '<your access token>'
        corp_realname_request = dingtalkesign__2__0_models.CorpRealnameRequest(
            user_id='manager1122',
            redirect_url='http://xxx.com'
        )
        try:
            client.corp_realname_with_options(corp_realname_request, corp_realname_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        corp_realname_headers = dingtalkesign__2__0_models.CorpRealnameHeaders()
        corp_realname_headers.x_acs_dingtalk_access_token = '<your access token>'
        corp_realname_request = dingtalkesign__2__0_models.CorpRealnameRequest(
            user_id='manager1122',
            redirect_url='http://xxx.com'
        )
        try:
            await client.corp_realname_with_options_async(corp_realname_request, corp_realname_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CorpRealnameHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CorpRealnameRequest;
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
        $corpRealnameHeaders = new CorpRealnameHeaders([]);
        $corpRealnameHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $corpRealnameRequest = new CorpRealnameRequest([
            "userId" => "manager1122",
            "redirectUrl" => "http://xxx.com"
        ]);
        try {
            $client->corpRealnameWithOptions($corpRealnameRequest, $corpRealnameHeaders, new RuntimeOptions([]));
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
  dingtalkesign_2_0  ""github.com/alibabacloud-go/dingtalk/esign_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_2_0.Client{}
  _result, _err = dingtalkesign_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  corpRealnameHeaders := &dingtalkesign_2_0.CorpRealnameHeaders{}
  corpRealnameHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  corpRealnameRequest := &dingtalkesign_2_0.CorpRealnameRequest{
    UserId: tea.String("manager1122"),
    RedirectUrl: tea.String("http://xxx.com"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CorpRealnameWithOptions(corpRealnameRequest, corpRealnameHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_2_0, * as $dingtalkesign_2_0 from '"@alicloud/dingtalk/esign_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let corpRealnameHeaders = new $dingtalkesign_2_0.CorpRealnameHeaders({ });
    corpRealnameHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let corpRealnameRequest = new $dingtalkesign_2_0.CorpRealnameRequest({
      userId: "manager1122",
      redirectUrl: "http://xxx.com",
    });
    try {
      await client.corpRealnameWithOptions(corpRealnameRequest, corpRealnameHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CorpRealnameHeaders corpRealnameHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CorpRealnameHeaders();
            corpRealnameHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CorpRealnameRequest corpRealnameRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CorpRealnameRequest
            {
                UserId = "manager1122",
                RedirectUrl = "http://xxx.com",
            };
            try
            {
                client.CorpRealnameWithOptions(corpRealnameRequest, corpRealnameHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__2__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_2_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_2_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_2_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CorpRealnameHeaders> corpRealnameHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::CorpRealnameHeaders>();
  corpRealnameHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CorpRealnameRequest> corpRealnameRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::CorpRealnameRequest>(map<string, boost::any>({
    {"userId", boost::any(string("manager1122"))},
    {"redirectUrl", boost::any(string("http://xxx.com"))}
  }));
  try {
    client->corpRealnameWithOptions(corpRealnameRequest, corpRealnameHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| taskId | String | 任务ID。 |
| pcUrl | String | PC端实名认证地址。 |
| mobileUrl | String | 移动端实名认证地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "taskId" : "PRO-E990xxx",
  "pcUrl" : "http://xxx.com",
  "mobileUrl" : "http://xxx.com"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | getOpenIsvInfoError | 获取对接服务商信息异常 | 获取对接服务商信息异常 |
| 400 | createUserError | 创建用户账号异常 | 创建用户账号异常 |
| 400 | isDingAdminError | 判断钉钉管理员异常 | 判断钉钉管理员异常 |
| 400 | dingAdminAuthError | 非钉钉管理员无法操作 | 非钉钉管理员无法操作 |
| 400 | saveTaskError | 保存任务信息异常 | 保存任务信息异常 |
