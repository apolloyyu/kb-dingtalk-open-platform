---
title: "确认完成权益的更新"
source_url: "https://open.dingtalk.com/document/development/confirm-benefits"
namespace: "development"
slug: "confirm-benefits"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能招聘 > 确认完成权益的更新"
doc_id: "1hlR7qkqSL"
updated_at: "2026-06-04 19:10:35"
---

> Source: https://open.dingtalk.com/document/development/confirm-benefits
> Path: 应用开发 / 服务端API / 智能招聘 > 确认完成权益的更新
> Updated: 2026-06-04 19:10:35

# 确认完成权益的更新

企业用户在智能招聘的权益发生变更后，第三方企业应用需要调用此接口确认权益。

## **接口调用说明**

调用本接口前，需先申请注册为智能招聘插件应用。申请流程：通过[技术支持-在线答疑](https://open.dingtalk.com/document/contactus/ngliko)申请，同时请提供插件名称、第三方企业应用的AppId和SuiteKey。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/rights/{rightsCode}/confirm |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_recruitment\_plugin-智能招聘插件管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| rightsCode | String | 是 | 权益码，常见权益码如下：   - RIGHTS\_ATS\_ADVANCED：智能招聘高级版       其他权益场景需线下提供，请通过[技术支持-在线答疑自助工具](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)咨询。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizCode | String | 否 | 业务标识，默认值为`ddats`。    如果传该参数，只支持`ddats`。 |

### 请求示例

HTTP

```
POST /v1.0/ats/rights/RIGHTS_ATS_ADVANCED/confirm?bizCode=ddats HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c652e6841b5339b6ba2fa835785b32e8
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkats_1_0.*;
import com.aliyun.dingtalkats_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkats_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkats_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkats_1_0.Client client = Sample.createClient();
        ConfirmRightsHeaders confirmRightsHeaders = new ConfirmRightsHeaders();
        confirmRightsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ConfirmRightsRequest confirmRightsRequest = new ConfirmRightsRequest()
                .setBizCode("ddats");
        try {
            client.confirmRightsWithOptions("RIGHTS_ATS_ADVANCED", confirmRightsRequest, confirmRightsHeaders, new RuntimeOptions());
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
        confirm_rights_headers = dingtalkats__1__0_models.ConfirmRightsHeaders()
        confirm_rights_headers.x_acs_dingtalk_access_token = '<your access token>'
        confirm_rights_request = dingtalkats__1__0_models.ConfirmRightsRequest(
            biz_code='ddats'
        )
        try:
            client.confirm_rights_with_options('RIGHTS_ATS_ADVANCED', confirm_rights_request, confirm_rights_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        confirm_rights_headers = dingtalkats__1__0_models.ConfirmRightsHeaders()
        confirm_rights_headers.x_acs_dingtalk_access_token = '<your access token>'
        confirm_rights_request = dingtalkats__1__0_models.ConfirmRightsRequest(
            biz_code='ddats'
        )
        try:
            await client.confirm_rights_with_options_async('RIGHTS_ATS_ADVANCED', confirm_rights_request, confirm_rights_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\ConfirmRightsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\ConfirmRightsRequest;
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
        $confirmRightsHeaders = new ConfirmRightsHeaders([]);
        $confirmRightsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $confirmRightsRequest = new ConfirmRightsRequest([
            "bizCode" => "ddats"
        ]);
        try {
            $client->confirmRightsWithOptions("RIGHTS_ATS_ADVANCED", $confirmRightsRequest, $confirmRightsHeaders, new RuntimeOptions([]));
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
  dingtalkats_1_0  "github.com/alibabacloud-go/dingtalk/ats_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  confirmRightsHeaders := &dingtalkats_1_0.ConfirmRightsHeaders{}
  confirmRightsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  confirmRightsRequest := &dingtalkats_1_0.ConfirmRightsRequest{
    BizCode: tea.String("ddats"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ConfirmRightsWithOptions(tea.String("RIGHTS_ATS_ADVANCED"), confirmRightsRequest, confirmRightsHeaders, &util.RuntimeOptions{})
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
    let confirmRightsHeaders = new $dingtalkats_1_0.ConfirmRightsHeaders({ });
    confirmRightsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let confirmRightsRequest = new $dingtalkats_1_0.ConfirmRightsRequest({
      bizCode: "ddats",
    });
    try {
      await client.confirmRightsWithOptions("RIGHTS_ATS_ADVANCED", confirmRightsRequest, confirmRightsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.ConfirmRightsHeaders confirmRightsHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.ConfirmRightsHeaders();
            confirmRightsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.ConfirmRightsRequest confirmRightsRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.ConfirmRightsRequest
            {
                BizCode = "ddats",
            };
            try
            {
                client.ConfirmRightsWithOptions("RIGHTS_ATS_ADVANCED", confirmRightsRequest, confirmRightsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkats__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkats_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkats_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkats_1_0::Client> client = make_shared<Alibabacloud_Dingtalkats_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkats_1_0::ConfirmRightsHeaders> confirmRightsHeaders = make_shared<Alibabacloud_Dingtalkats_1_0::ConfirmRightsHeaders>();
  confirmRightsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkats_1_0::ConfirmRightsRequest> confirmRightsRequest = make_shared<Alibabacloud_Dingtalkats_1_0::ConfirmRightsRequest>(map<string, boost::any>({
    {"bizCode", boost::any(string("ddats"))}
  }));
  try {
    client->confirmRightsWithOptions(make_shared<string>("RIGHTS_ATS_ADVANCED"), confirmRightsRequest, confirmRightsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Boolean | 调用结果。   - true：成功 - false：失败 |

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
| 400 | invalidParam | %s | 无效参数 |
| 404 | rights.notExists | 权益不存在 | 权益不存在（可能已被删除） |
| 500 | systemError | 系统错误 | 系统错误 |
