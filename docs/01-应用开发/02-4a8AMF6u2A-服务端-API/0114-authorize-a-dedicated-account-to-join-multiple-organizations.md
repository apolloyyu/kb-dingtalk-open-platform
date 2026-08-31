---
title: "授权企业账号可加入多组织"
source_url: "https://open.dingtalk.com/document/development/authorize-a-dedicated-account-to-join-multiple-organizations"
namespace: "development"
slug: "authorize-a-dedicated-account-to-join-multiple-organizations"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 授权企业账号可加入多组织"
doc_id: "yfaOZEtbK7"
updated_at: "2026-06-08 11:20:17"
---

> Source: https://open.dingtalk.com/document/development/authorize-a-dedicated-account-to-join-multiple-organizations
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 授权企业账号可加入多组织
> Updated: 2026-06-08 11:20:17

# 授权企业账号可加入多组织

调用本接口，授权企业账号可以加入多个组织，只有被授权后企业账号才能加入外部组织。

## 接口调用说明

授权成功后，只支持接口操作添加进入企业。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccounts/multiOrgPermissions/auth |
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
| joinCorpId | String | 是 | 被授权的组织CorpId。 |
| grantDeptIdList | Array of Long | 否 | 授权的部门列表。   - 如果该参数不传，授权整个企业。 - 如果该参数传值，授权参数值对应的部门。 |

### 请求示例

HTTP

```
POST /v1.0/contact/orgAccounts/multiOrgPermissions/auth HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:0d702e22d08d39bbb0d3e2d9c9aa1220
Content-Type:application/json

{
  "joinCorpId" : "dingxxxxx",
  "grantDeptIdList" : [ 123 ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcontact_1_0.*;
import com.aliyun.dingtalkcontact_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        MultiOrgPermissionGrantHeaders multiOrgPermissionGrantHeaders = new MultiOrgPermissionGrantHeaders();
        multiOrgPermissionGrantHeaders.xAcsDingtalkAccessToken = "<your access token>";
        MultiOrgPermissionGrantRequest multiOrgPermissionGrantRequest = new MultiOrgPermissionGrantRequest()
                .setJoinCorpId("dingxxxxx")
                .setGrantDeptIdList(java.util.Arrays.asList(
                    123L
                ));
        try {
            client.multiOrgPermissionGrantWithOptions(multiOrgPermissionGrantRequest, multiOrgPermissionGrantHeaders, new RuntimeOptions());
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
        multi_org_permission_grant_headers = dingtalkcontact__1__0_models.MultiOrgPermissionGrantHeaders()
        multi_org_permission_grant_headers.x_acs_dingtalk_access_token = '<your access token>'
        multi_org_permission_grant_request = dingtalkcontact__1__0_models.MultiOrgPermissionGrantRequest(
            join_corp_id='dingxxxxx',
            grant_dept_id_list=[
                123
            ]
        )
        try:
            client.multi_org_permission_grant_with_options(multi_org_permission_grant_request, multi_org_permission_grant_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        multi_org_permission_grant_headers = dingtalkcontact__1__0_models.MultiOrgPermissionGrantHeaders()
        multi_org_permission_grant_headers.x_acs_dingtalk_access_token = '<your access token>'
        multi_org_permission_grant_request = dingtalkcontact__1__0_models.MultiOrgPermissionGrantRequest(
            join_corp_id='dingxxxxx',
            grant_dept_id_list=[
                123
            ]
        )
        try:
            await client.multi_org_permission_grant_with_options_async(multi_org_permission_grant_request, multi_org_permission_grant_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\MultiOrgPermissionGrantHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\MultiOrgPermissionGrantRequest;
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
        $multiOrgPermissionGrantHeaders = new MultiOrgPermissionGrantHeaders([]);
        $multiOrgPermissionGrantHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $multiOrgPermissionGrantRequest = new MultiOrgPermissionGrantRequest([
            "joinCorpId" => "dingxxxxx",
            "grantDeptIdList" => [
                123
            ]
        ]);
        try {
            $client->multiOrgPermissionGrantWithOptions($multiOrgPermissionGrantRequest, $multiOrgPermissionGrantHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  multiOrgPermissionGrantHeaders := &dingtalkcontact_1_0.MultiOrgPermissionGrantHeaders{}
  multiOrgPermissionGrantHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  multiOrgPermissionGrantRequest := &dingtalkcontact_1_0.MultiOrgPermissionGrantRequest{
    JoinCorpId: tea.String("dingxxxxx"),
    GrantDeptIdList: []*int64{tea.Int(123)},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.MultiOrgPermissionGrantWithOptions(multiOrgPermissionGrantRequest, multiOrgPermissionGrantHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let multiOrgPermissionGrantHeaders = new $dingtalkcontact_1_0.MultiOrgPermissionGrantHeaders({ });
    multiOrgPermissionGrantHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let multiOrgPermissionGrantRequest = new $dingtalkcontact_1_0.MultiOrgPermissionGrantRequest({
      joinCorpId: "dingxxxxx",
      grantDeptIdList: [
        123
      ],
    });
    try {
      await client.multiOrgPermissionGrantWithOptions(multiOrgPermissionGrantRequest, multiOrgPermissionGrantHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.MultiOrgPermissionGrantHeaders multiOrgPermissionGrantHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.MultiOrgPermissionGrantHeaders();
            multiOrgPermissionGrantHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.MultiOrgPermissionGrantRequest multiOrgPermissionGrantRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.MultiOrgPermissionGrantRequest
            {
                JoinCorpId = "dingxxxxx",
                GrantDeptIdList = new List<long?>
                {
                    123
                },
            };
            try
            {
                client.MultiOrgPermissionGrantWithOptions(multiOrgPermissionGrantRequest, multiOrgPermissionGrantHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcontact__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcontact_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcontact_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcontact_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::MultiOrgPermissionGrantHeaders> multiOrgPermissionGrantHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::MultiOrgPermissionGrantHeaders>();
  multiOrgPermissionGrantHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::MultiOrgPermissionGrantRequest> multiOrgPermissionGrantRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::MultiOrgPermissionGrantRequest>(map<string, boost::any>({
    {"joinCorpId", boost::any(string("dingxxxxx"))},
    {"grantDeptIdList", boost::any(vector<long>({
      123
    }))}
  }));
  try {
    client->multiOrgPermissionGrantWithOptions(multiOrgPermissionGrantRequest, multiOrgPermissionGrantHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.param | 无效参数 | 无效参数 |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
