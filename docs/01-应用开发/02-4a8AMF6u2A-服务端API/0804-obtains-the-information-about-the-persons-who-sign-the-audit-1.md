---
title: "获取审计协议签署人员信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-information-about-the-persons-who-sign-the-audit-1"
namespace: "development"
slug: "obtains-the-information-about-the-persons-who-sign-the-audit-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 审计 > 获取审计协议签署人员信息"
doc_id: "RzM5mV9uY8"
updated_at: "2026-06-04 19:09:53"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-information-about-the-persons-who-sign-the-audit-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 审计 > 获取审计协议签署人员信息
> Updated: 2026-06-04 19:09:53

# 获取审计协议签署人员信息

本接口用于获取审计应用内已签署和未签署人员的信息，包括人员的姓名，userId，手机号，部门等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/audits/users |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Audit.Read-专属钉钉审计读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageNumber | Long | 是 | 页码，首次传1。 |
| signStatus | Long | 是 | 签署状态。   - 0：未签署 - 1：已签署 |
| pageSize | Long | 是 | 每页数量，最大值2000。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/audits/users?pageNumber=1&signStatus=1&pageSize=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:tokenxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        GetSignedDetailByPageHeaders getSignedDetailByPageHeaders = new GetSignedDetailByPageHeaders();
        getSignedDetailByPageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetSignedDetailByPageRequest getSignedDetailByPageRequest = new GetSignedDetailByPageRequest()
                .setPageNumber(1L)
                .setSignStatus(1L)
                .setPageSize(1L);
        try {
            client.getSignedDetailByPageWithOptions(getSignedDetailByPageRequest, getSignedDetailByPageHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_signed_detail_by_page_headers = dingtalkexclusive__1__0_models.GetSignedDetailByPageHeaders()
        get_signed_detail_by_page_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_signed_detail_by_page_request = dingtalkexclusive__1__0_models.GetSignedDetailByPageRequest(
            page_number=1,
            sign_status=1,
            page_size=1
        )
        try:
            client.get_signed_detail_by_page_with_options(get_signed_detail_by_page_request, get_signed_detail_by_page_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_signed_detail_by_page_headers = dingtalkexclusive__1__0_models.GetSignedDetailByPageHeaders()
        get_signed_detail_by_page_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_signed_detail_by_page_request = dingtalkexclusive__1__0_models.GetSignedDetailByPageRequest(
            page_number=1,
            sign_status=1,
            page_size=1
        )
        try:
            await client.get_signed_detail_by_page_with_options_async(get_signed_detail_by_page_request, get_signed_detail_by_page_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetSignedDetailByPageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetSignedDetailByPageRequest;
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
        $getSignedDetailByPageHeaders = new GetSignedDetailByPageHeaders([]);
        $getSignedDetailByPageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSignedDetailByPageRequest = new GetSignedDetailByPageRequest([
            "pageNumber" => 1,
            "signStatus" => 1,
            "pageSize" => 1
        ]);
        try {
            $client->getSignedDetailByPageWithOptions($getSignedDetailByPageRequest, $getSignedDetailByPageHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getSignedDetailByPageHeaders := &dingtalkexclusive_1_0.GetSignedDetailByPageHeaders{}
  getSignedDetailByPageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSignedDetailByPageRequest := &dingtalkexclusive_1_0.GetSignedDetailByPageRequest{
    PageNumber: tea.Int64(1),
    SignStatus: tea.Int64(1),
    PageSize: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSignedDetailByPageWithOptions(getSignedDetailByPageRequest, getSignedDetailByPageHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getSignedDetailByPageHeaders = new $dingtalkexclusive_1_0.GetSignedDetailByPageHeaders({ });
    getSignedDetailByPageHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getSignedDetailByPageRequest = new $dingtalkexclusive_1_0.GetSignedDetailByPageRequest({
      pageNumber: 1,
      signStatus: 1,
      pageSize: 1,
    });
    try {
      await client.getSignedDetailByPageWithOptions(getSignedDetailByPageRequest, getSignedDetailByPageHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetSignedDetailByPageHeaders getSignedDetailByPageHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetSignedDetailByPageHeaders();
            getSignedDetailByPageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetSignedDetailByPageRequest getSignedDetailByPageRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetSignedDetailByPageRequest
            {
                PageNumber = 1,
                SignStatus = 1,
                PageSize = 1,
            };
            try
            {
                client.GetSignedDetailByPageWithOptions(getSignedDetailByPageRequest, getSignedDetailByPageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkexclusive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkexclusive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkexclusive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkexclusive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::GetSignedDetailByPageHeaders> getSignedDetailByPageHeaders = make_shared<Alibabacloud_Dingtalkexclusive_1_0::GetSignedDetailByPageHeaders>();
  getSignedDetailByPageHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::GetSignedDetailByPageRequest> getSignedDetailByPageRequest = make_shared<Alibabacloud_Dingtalkexclusive_1_0::GetSignedDetailByPageRequest>(map<string, boost::any>({
    {"pageNumber", boost::any(1)},
    {"signStatus", boost::any(1)},
    {"pageSize", boost::any(1)}
  }));
  try {
    client->getSignedDetailByPageWithOptions(getSignedDetailByPageRequest, getSignedDetailByPageHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| auditSignedDetailDTOList | Array | 员工信息 |
| name | String | 员工名称。 |
| staffId | String | 员工userId。 |
| title | String | 职位。 |
| phone | String | 员工手机号。 |
| email | String | 邮件。 |
| deptName | String | 部门名称。 |
| roles | String | 角色名称。 |
| currentPage | Long | 当前页码。 |
| pageSize | Long | 当前页数据量。 |
| total | Long | 总数据量。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "auditSignedDetailDTOList" : [ {
    "name" : "小张",
    "staffId" : "123***",
    "title" : "经理",
    "phone" : "***",
    "email" : "**@**.com",
    "deptName" : "部门1",
    "roles" : "主管理员"
  } ],
  "currentPage" : 1,
  "pageSize" : 50,
  "total" : 1000
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.missing | 参数不能为空 | 参数不能为空 |
| 500 | system.busy | 系统繁忙，请稍后再试 | 系统繁忙 |
