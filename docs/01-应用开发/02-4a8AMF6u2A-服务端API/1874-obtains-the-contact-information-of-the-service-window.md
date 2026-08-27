---
title: "获取服务窗联系人信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-contact-information-of-the-service-window"
namespace: "development"
slug: "obtains-the-contact-information-of-the-service-window"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 获取服务窗联系人信息"
doc_id: "1cO6kq66o8"
updated_at: "2025-09-08 19:07:58"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-contact-information-of-the-service-window
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 获取服务窗联系人信息
> Updated: 2025-09-08 19:07:58

# 获取服务窗联系人信息

获取服务窗联系人信息，例如手机号、主企业信息等。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，客户管理的**服务窗**接口已升级。**客户管理-服务窗API**文档已于2022年11月30日移动至历史文档（不推荐）目录，接口不再支持新应用接入，已接入的应用可继续调用。新产品开放上线时间请关注文档更新日志。

![](https://img.alicdn.com/imgextra/i3/O1CN01mAUNEt1xuslUszEuz_!!6000000006504-2-tps-2784-1198.png)

> **[!NOTE]**
>
> 各敏感字段需要提前调用授权接口进行授权，授权后接口会自动返回。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | — | — |
| 第三方企业应用 | 暂不支持 | — | — |
| 第三方个人应用 | 暂不支持 | — | — |

## 请求方法

```
GET /v1.0/crm/officialAccounts/contacts/{userId} HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 服务窗联系人的userId。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corpName | String | 联系人主企业名称。 |
| mobile | String | 联系人的手机号。 |
| stateCode | String | 手机号国家码。 |
| unionId | String | 联系人的unionId，可通过[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details)接口获取。 |
| authItems | Array of String | 已经授权的字段，包括手机号，主企业信息等。 |
| userInfos | Array of String | 用户实例ID。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/crm/officialAccounts/contacts/user_id1234 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:asjkdhjk12387
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcrm_1_0.*;
import com.aliyun.dingtalkcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        GetOfficialAccountContactInfoHeaders getOfficialAccountContactInfoHeaders = new GetOfficialAccountContactInfoHeaders();
        getOfficialAccountContactInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getOfficialAccountContactInfoWithOptions("user_id1234", getOfficialAccountContactInfoHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_official_account_contact_info_headers = dingtalkcrm__1__0_models.GetOfficialAccountContactInfoHeaders()
        get_official_account_contact_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_official_account_contact_info_with_options('user_id1234', get_official_account_contact_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_official_account_contact_info_headers = dingtalkcrm__1__0_models.GetOfficialAccountContactInfoHeaders()
        get_official_account_contact_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_official_account_contact_info_with_options_async('user_id1234', get_official_account_contact_info_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetOfficialAccountContactInfoHeaders;
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
        $getOfficialAccountContactInfoHeaders = new GetOfficialAccountContactInfoHeaders([]);
        $getOfficialAccountContactInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getOfficialAccountContactInfoWithOptions("user_id1234", $getOfficialAccountContactInfoHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getOfficialAccountContactInfoHeaders := &dingtalkcrm_1_0.GetOfficialAccountContactInfoHeaders{}
  getOfficialAccountContactInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetOfficialAccountContactInfoWithOptions(tea.String("user_id1234"), getOfficialAccountContactInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getOfficialAccountContactInfoHeaders = new $dingtalkcrm_1_0.GetOfficialAccountContactInfoHeaders({ });
    getOfficialAccountContactInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.getOfficialAccountContactInfoWithOptions("user_id1234", getOfficialAccountContactInfoHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetOfficialAccountContactInfoHeaders getOfficialAccountContactInfoHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetOfficialAccountContactInfoHeaders();
            getOfficialAccountContactInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetOfficialAccountContactInfoWithOptions("user_id1234", getOfficialAccountContactInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

using namespace std;

Alibabacloud_Dingtalkcrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::GetOfficialAccountContactInfoHeaders> getOfficialAccountContactInfoHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::GetOfficialAccountContactInfoHeaders>();
  getOfficialAccountContactInfoHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->getOfficialAccountContactInfoWithOptions(make_shared<string>("user_id1234"), getOfficialAccountContactInfoHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "corpName" : "阿里巴巴钉钉",
  "mobile" : "18812341234",
  "stateCode" : "+86",
  "unionId" : "unionId1234",
  "authItems" : [ "mainOrgName" ],
  "userInfos" : [ "{\"instanceId \":\"ec6ed86e-af53-4c9f-afd3-206c3fc68c64\" }" ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | userId.not.exists | userId not exists | 用户不存在或该用户未关注服务窗 |
| 400 | invalidParameter.invalidOrgId | crm has not been installed for this org | 服务窗的组织id非法 |
| 403 | permission.deny | need user auth | 用户未授权 |
| 429 | system.busy | system busy, request too frequest | 请求太频繁，系统限流 |
| 503 | system.error | system error | 系统错误 |
