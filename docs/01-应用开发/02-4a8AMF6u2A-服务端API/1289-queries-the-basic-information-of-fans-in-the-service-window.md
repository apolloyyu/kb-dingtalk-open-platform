---
title: "查询服务窗粉丝用户基础信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-basic-information-of-fans-in-the-service-window"
namespace: "development"
slug: "queries-the-basic-information-of-fans-in-the-service-window"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 服务窗 > 查询服务窗粉丝用户基础信息"
doc_id: "3koV3uugwR"
updated_at: "2025-09-11 21:03:52"
---

> Source: https://open.dingtalk.com/document/development/queries-the-basic-information-of-fans-in-the-service-window
> Path: 应用开发 / 服务端API / 更多开放 > 服务窗 > 查询服务窗粉丝用户基础信息
> Updated: 2025-09-11 21:03:52

# 查询服务窗粉丝用户基础信息

调用本接口实现查询指定unionId的服务窗粉丝用户基础信息，如该用户是否关注服务窗。

## 请求

### **基本信息**

| HTTP URL | https://api.dingtalk.com/v1.0/crm/officialAccounts/basics/users |
| --- | --- |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方个人应用 |
| 权限要求 | permission-OfficialAccount.User.Read.OpenApp-服务窗用户信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 需要查询关注状态信息的用户unionId，调用[获取用户基本信息](0052-queries-basic-user-information.md)接口，获取用户unionId信息。 |
| bindingToken | String | 是 | 服务窗与第三方个人应用绑定时生成的授权码，可通过服务窗微应用-开放互联功能进行账号与第三方个人应用的绑定后获取。 |

### 请求示例

HTTP

```
GET /v1.0/crm/officialAccounts/basics/users?unionId=钉钉用户unionId&bindingToken=服务窗与第三方应用绑定时产生的bindingToken HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2955287872ed38ad9ed7e7c7b234ddks
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
        QueryOfficialAccountUserBasicInfoHeaders queryOfficialAccountUserBasicInfoHeaders = new QueryOfficialAccountUserBasicInfoHeaders();
        queryOfficialAccountUserBasicInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryOfficialAccountUserBasicInfoRequest queryOfficialAccountUserBasicInfoRequest = new QueryOfficialAccountUserBasicInfoRequest()
                .setUnionId("钉钉用户unionId")
                .setBindingToken("服务窗与第三方应用绑定时产生的bindingToken");
        try {
            client.queryOfficialAccountUserBasicInfoWithOptions(queryOfficialAccountUserBasicInfoRequest, queryOfficialAccountUserBasicInfoHeaders, new RuntimeOptions());
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
        query_official_account_user_basic_info_headers = dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoHeaders()
        query_official_account_user_basic_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_official_account_user_basic_info_request = dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoRequest(
            union_id='钉钉用户unionId',
            binding_token='服务窗与第三方应用绑定时产生的bindingToken'
        )
        try:
            client.query_official_account_user_basic_info_with_options(query_official_account_user_basic_info_request, query_official_account_user_basic_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_official_account_user_basic_info_headers = dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoHeaders()
        query_official_account_user_basic_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_official_account_user_basic_info_request = dingtalkcrm__1__0_models.QueryOfficialAccountUserBasicInfoRequest(
            union_id='钉钉用户unionId',
            binding_token='服务窗与第三方应用绑定时产生的bindingToken'
        )
        try:
            await client.query_official_account_user_basic_info_with_options_async(query_official_account_user_basic_info_request, query_official_account_user_basic_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryOfficialAccountUserBasicInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryOfficialAccountUserBasicInfoRequest;
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
        $queryOfficialAccountUserBasicInfoHeaders = new QueryOfficialAccountUserBasicInfoHeaders([]);
        $queryOfficialAccountUserBasicInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryOfficialAccountUserBasicInfoRequest = new QueryOfficialAccountUserBasicInfoRequest([
            "unionId" => "钉钉用户unionId",
            "bindingToken" => "服务窗与第三方应用绑定时产生的bindingToken"
        ]);
        try {
            $client->queryOfficialAccountUserBasicInfoWithOptions($queryOfficialAccountUserBasicInfoRequest, $queryOfficialAccountUserBasicInfoHeaders, new RuntimeOptions([]));
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

  queryOfficialAccountUserBasicInfoHeaders := &dingtalkcrm_1_0.QueryOfficialAccountUserBasicInfoHeaders{}
  queryOfficialAccountUserBasicInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryOfficialAccountUserBasicInfoRequest := &dingtalkcrm_1_0.QueryOfficialAccountUserBasicInfoRequest{
    UnionId: tea.String("钉钉用户unionId"),
    BindingToken: tea.String("服务窗与第三方应用绑定时产生的bindingToken"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryOfficialAccountUserBasicInfoWithOptions(queryOfficialAccountUserBasicInfoRequest, queryOfficialAccountUserBasicInfoHeaders, &util.RuntimeOptions{})
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
    let queryOfficialAccountUserBasicInfoHeaders = new $dingtalkcrm_1_0.QueryOfficialAccountUserBasicInfoHeaders({ });
    queryOfficialAccountUserBasicInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryOfficialAccountUserBasicInfoRequest = new $dingtalkcrm_1_0.QueryOfficialAccountUserBasicInfoRequest({
      unionId: "钉钉用户unionId",
      bindingToken: "服务窗与第三方应用绑定时产生的bindingToken",
    });
    try {
      await client.queryOfficialAccountUserBasicInfoWithOptions(queryOfficialAccountUserBasicInfoRequest, queryOfficialAccountUserBasicInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryOfficialAccountUserBasicInfoHeaders queryOfficialAccountUserBasicInfoHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryOfficialAccountUserBasicInfoHeaders();
            queryOfficialAccountUserBasicInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryOfficialAccountUserBasicInfoRequest queryOfficialAccountUserBasicInfoRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryOfficialAccountUserBasicInfoRequest
            {
                UnionId = "钉钉用户unionId",
                BindingToken = "服务窗与第三方应用绑定时产生的bindingToken",
            };
            try
            {
                client.QueryOfficialAccountUserBasicInfoWithOptions(queryOfficialAccountUserBasicInfoRequest, queryOfficialAccountUserBasicInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求ID标识。 |
| result | Object | 查询结果。 |
| status | String | 用户关注服务窗的状态。   - FOLLOWED：已关注。 - UNFOLLOW：未关注。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "abdd-fd-ew-sfe",
  "result" : {
    "status" : "FOLLOWED"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.tast | request too fast. | 请求过快被限流。 |
| 400 | illegalParameter.bindingClient | illegal binding client | 第三方应用与服务窗绑定关系不正确 |
| 400 | illegalParameter.bindingToken | illegal binding token | bindingToken参数不正确。 |
| 400 | illegalParameter | illegal parameter | 请求参数不正确 |
| 500 | systemError | system error. | 系统处理出错。 |
