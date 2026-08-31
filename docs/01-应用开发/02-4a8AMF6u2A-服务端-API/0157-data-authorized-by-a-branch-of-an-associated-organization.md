---
title: "获取上下级组织分支授权的数据"
source_url: "https://open.dingtalk.com/document/development/data-authorized-by-a-branch-of-an-associated-organization"
namespace: "development"
slug: "data-authorized-by-a-branch-of-an-associated-organization"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 上下级组织（原关联组织） > 获取上下级组织分支授权的数据"
doc_id: "Erp8rtF4zE"
updated_at: "2026-06-02 09:24:48"
---

> Source: https://open.dingtalk.com/document/development/data-authorized-by-a-branch-of-an-associated-organization
> Path: 应用开发 / 服务端 API / 通讯录管理 > 上下级组织（原关联组织） > 获取上下级组织分支授权的数据
> Updated: 2026-06-02 09:24:48

# 获取上下级组织分支授权的数据

获取关联组织分支授权的数据

## 接口调用说明

更多数据开放及消费能力请移至[数据资产平台](https://open.dingtalk.com/document/dataopen/overview)。数据资产平台（dPaaS）是为企业提供的统一数据管理平台，基于钉钉构建安全、可扩展、易维护和管理的数据服务，助力业务决策。

分支组织关联到主干时，可选择授权给主干的数据范围，主干组织上的企业内部应用可以使用该接口获取分支组织的授权数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/branchAuthDatas/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.UnionBranchData.Read-通讯录分支组织授权数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| branchCorpId | String | 是 | 分支组织的corpId，可通过[获取分支组织列表](0155-obtains-the-branch-organization-list.md)接口获取union\_corpid参数值。 |
| code | String | 是 | 子类数据编码，详情可参考[授权数据编码及入参条件概览](https://open.dingtalk.com/document/development/data-authorized-by-a-branch-of-an-associated-organization-instructions)。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Map<String, String> | 否 | 数据查询条件，可参考[授权数据编码及入参条件概览](https://open.dingtalk.com/document/development/data-authorized-by-a-branch-of-an-associated-organization-instructions)。 |

### 请求示例

HTTP

```
POST /v1.0/contact/branchAuthDatas/search?branchCorpId=ding1b1ed7160e8e47353d8fd98s67sa786fg&code=GROUP_GRO_ORG_OPEN_ORG HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:74fadfda243fsd23253d309d8744bcrdafa
Content-Type:application/json

{
  "key" : "20210507"
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
        GetBranchAuthDataHeaders getBranchAuthDataHeaders = new GetBranchAuthDataHeaders();
        getBranchAuthDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> body = TeaConverter.buildMap(
            new TeaPair("key", "20210507")
        );
        GetBranchAuthDataRequest getBranchAuthDataRequest = new GetBranchAuthDataRequest()
                .setBranchCorpId("ding1b1ed7160e8e47353d8fd98s67sa786fg")
                .setCode("GROUP_GRO_ORG_OPEN_ORG")
                .setBody(body);
        try {
            client.getBranchAuthDataWithOptions(getBranchAuthDataRequest, getBranchAuthDataHeaders, new RuntimeOptions());
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
        get_branch_auth_data_headers = dingtalkcontact__1__0_models.GetBranchAuthDataHeaders()
        get_branch_auth_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        body = {
            'key': '20210507'
        }
        get_branch_auth_data_request = dingtalkcontact__1__0_models.GetBranchAuthDataRequest(
            branch_corp_id='ding1b1ed7160e8e47353d8fd98s67sa786fg',
            code='GROUP_GRO_ORG_OPEN_ORG',
            body=body
        )
        try:
            client.get_branch_auth_data_with_options(get_branch_auth_data_request, get_branch_auth_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_branch_auth_data_headers = dingtalkcontact__1__0_models.GetBranchAuthDataHeaders()
        get_branch_auth_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        body = {
            'key': '20210507'
        }
        get_branch_auth_data_request = dingtalkcontact__1__0_models.GetBranchAuthDataRequest(
            branch_corp_id='ding1b1ed7160e8e47353d8fd98s67sa786fg',
            code='GROUP_GRO_ORG_OPEN_ORG',
            body=body
        )
        try:
            await client.get_branch_auth_data_with_options_async(get_branch_auth_data_request, get_branch_auth_data_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetBranchAuthDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetBranchAuthDataRequest;
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
        $getBranchAuthDataHeaders = new GetBranchAuthDataHeaders([]);
        $getBranchAuthDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body = [
            "key" => "20210507"
        ];
        $getBranchAuthDataRequest = new GetBranchAuthDataRequest([
            "branchCorpId" => "ding1b1ed7160e8e47353d8fd98s67sa786fg",
            "code" => "GROUP_GRO_ORG_OPEN_ORG",
            "body" => $body
        ]);
        try {
            $client->getBranchAuthDataWithOptions($getBranchAuthDataRequest, $getBranchAuthDataHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  ""github.com/alibabacloud-go/dingtalk/contact_1_0"
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

  getBranchAuthDataHeaders := &dingtalkcontact_1_0.GetBranchAuthDataHeaders{}
  getBranchAuthDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body := map[string]*string{
    "key": tea.String("20210507"),
  }
  getBranchAuthDataRequest := &dingtalkcontact_1_0.GetBranchAuthDataRequest{
    BranchCorpId: tea.String("ding1b1ed7160e8e47353d8fd98s67sa786fg"),
    Code: tea.String("GROUP_GRO_ORG_OPEN_ORG"),
    Body: body,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetBranchAuthDataWithOptions(getBranchAuthDataRequest, getBranchAuthDataHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '"@alicloud/dingtalk/contact_1_0';
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
    let getBranchAuthDataHeaders = new $dingtalkcontact_1_0.GetBranchAuthDataHeaders({ });
    getBranchAuthDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let body = {
      key: "20210507",
    };
    let getBranchAuthDataRequest = new $dingtalkcontact_1_0.GetBranchAuthDataRequest({
      branchCorpId: "ding1b1ed7160e8e47353d8fd98s67sa786fg",
      code: "GROUP_GRO_ORG_OPEN_ORG",
      body: body,
    });
    try {
      await client.getBranchAuthDataWithOptions(getBranchAuthDataRequest, getBranchAuthDataHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetBranchAuthDataHeaders getBranchAuthDataHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetBranchAuthDataHeaders();
            getBranchAuthDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> body = new Dictionary<string, string>
            {
                {"key", "20210507"},
            };
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetBranchAuthDataRequest getBranchAuthDataRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetBranchAuthDataRequest
            {
                BranchCorpId = "ding1b1ed7160e8e47353d8fd98s67sa786fg",
                Code = "GROUP_GRO_ORG_OPEN_ORG",
                Body = body,
            };
            try
            {
                client.GetBranchAuthDataWithOptions(getBranchAuthDataRequest, getBranchAuthDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetBranchAuthDataHeaders> getBranchAuthDataHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetBranchAuthDataHeaders>();
  getBranchAuthDataHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<map<string, string>> body = make_shared<map<string, string>>(map<string, string>({
    {"key", "20210507"}
  })
);
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetBranchAuthDataRequest> getBranchAuthDataRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetBranchAuthDataRequest>(map<string, boost::any>({
    {"branchCorpId", boost::any(string("ding1b1ed7160e8e47353d8fd98s67sa786fg"))},
    {"code", boost::any(string("GROUP_GRO_ORG_OPEN_ORG"))},
    {"body", !body ? boost::any() : boost::any(*body)}
  }));
  try {
    client->getBranchAuthDataWithOptions(getBranchAuthDataRequest, getBranchAuthDataHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Array | 查询结果集。 |
| fieldCode | String | 指标编码。 |
| fieldName | String | 指标名称。 |
| fieldValue | String | 指标值。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "fieldCode" : "CRO_ORG_OPEN_EDU_001",
    "fieldName" : "注册班级数",
    "fieldValue" : "100"
  } ]
}
```
