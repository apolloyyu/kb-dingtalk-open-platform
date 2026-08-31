---
title: "批量获取个人或企业客户数据"
source_url: "https://open.dingtalk.com/document/development/acquire-crm-individual-customers-in-batches"
namespace: "development"
slug: "acquire-crm-individual-customers-in-batches"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 批量获取个人或企业客户数据"
doc_id: "BcJ5GXur9r"
updated_at: "2026-06-04 19:12:08"
---

> Source: https://open.dingtalk.com/document/development/acquire-crm-individual-customers-in-batches
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 客户 > 批量获取个人或企业客户数据
> Updated: 2026-06-04 19:12:08

# 批量获取个人或企业客户数据

调用本接口，批量获取CRM个人客户或企业客户数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/personalCustomers/batchQuery |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-获取CRM主数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| currentOperatorUserId | String | 否 | 操作人的用户userId。 |
| relationType | String | 否 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array of String | 是 | 客户数据ID，调用[根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口获取instanceId参数值。 |

### 请求示例

HTTP

```
POST /v1.0/crm/personalCustomers/batchQuery?currentOperatorUserId=2665246100805992 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c364097xxx
Content-Type:application/json

[ "ec6ed86e-af53-4c9f-afd3-206c3fc68c64" ]
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
        ListCrmPersonalCustomersHeaders listCrmPersonalCustomersHeaders = new ListCrmPersonalCustomersHeaders();
        listCrmPersonalCustomersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListCrmPersonalCustomersRequest listCrmPersonalCustomersRequest = new ListCrmPersonalCustomersRequest()
                .setCurrentOperatorUserId("2665246100805992")
                .setBody(java.util.Arrays.asList(
                    "ec6ed86e-af53-4c9f-afd3-206c3fc68c64"
                ));
        try {
            client.listCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, new RuntimeOptions());
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
        list_crm_personal_customers_headers = dingtalkcrm__1__0_models.ListCrmPersonalCustomersHeaders()
        list_crm_personal_customers_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_crm_personal_customers_request = dingtalkcrm__1__0_models.ListCrmPersonalCustomersRequest(
            current_operator_user_id='2665246100805992',
            body=[
                'ec6ed86e-af53-4c9f-afd3-206c3fc68c64'
            ]
        )
        try:
            client.list_crm_personal_customers_with_options(list_crm_personal_customers_request, list_crm_personal_customers_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_crm_personal_customers_headers = dingtalkcrm__1__0_models.ListCrmPersonalCustomersHeaders()
        list_crm_personal_customers_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_crm_personal_customers_request = dingtalkcrm__1__0_models.ListCrmPersonalCustomersRequest(
            current_operator_user_id='2665246100805992',
            body=[
                'ec6ed86e-af53-4c9f-afd3-206c3fc68c64'
            ]
        )
        try:
            await client.list_crm_personal_customers_with_options_async(list_crm_personal_customers_request, list_crm_personal_customers_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\ListCrmPersonalCustomersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\ListCrmPersonalCustomersRequest;
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
        $listCrmPersonalCustomersHeaders = new ListCrmPersonalCustomersHeaders([]);
        $listCrmPersonalCustomersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listCrmPersonalCustomersRequest = new ListCrmPersonalCustomersRequest([
            "currentOperatorUserId" => "2665246100805992",
            "body" => [
                "ec6ed86e-af53-4c9f-afd3-206c3fc68c64"
            ]
        ]);
        try {
            $client->listCrmPersonalCustomersWithOptions($listCrmPersonalCustomersRequest, $listCrmPersonalCustomersHeaders, new RuntimeOptions([]));
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

  listCrmPersonalCustomersHeaders := &dingtalkcrm_1_0.ListCrmPersonalCustomersHeaders{}
  listCrmPersonalCustomersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listCrmPersonalCustomersRequest := &dingtalkcrm_1_0.ListCrmPersonalCustomersRequest{
    CurrentOperatorUserId: tea.String("2665246100805992"),
    Body: []*string{tea.String("ec6ed86e-af53-4c9f-afd3-206c3fc68c64")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, &util.RuntimeOptions{})
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
    let listCrmPersonalCustomersHeaders = new $dingtalkcrm_1_0.ListCrmPersonalCustomersHeaders({ });
    listCrmPersonalCustomersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listCrmPersonalCustomersRequest = new $dingtalkcrm_1_0.ListCrmPersonalCustomersRequest({
      currentOperatorUserId: "2665246100805992",
      body: [
        "ec6ed86e-af53-4c9f-afd3-206c3fc68c64"
      ],
    });
    try {
      await client.listCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListCrmPersonalCustomersHeaders listCrmPersonalCustomersHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListCrmPersonalCustomersHeaders();
            listCrmPersonalCustomersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListCrmPersonalCustomersRequest listCrmPersonalCustomersRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListCrmPersonalCustomersRequest
            {
                CurrentOperatorUserId = "2665246100805992",
                Body = new List<string>
                {
                    "ec6ed86e-af53-4c9f-afd3-206c3fc68c64"
                },
            };
            try
            {
                client.ListCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

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
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::ListCrmPersonalCustomersHeaders> listCrmPersonalCustomersHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::ListCrmPersonalCustomersHeaders>();
  listCrmPersonalCustomersHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::ListCrmPersonalCustomersRequest> listCrmPersonalCustomersRequest = make_shared<Alibabacloud_Dingtalkcrm_1_0::ListCrmPersonalCustomersRequest>(map<string, boost::any>({
    {"currentOperatorUserId", boost::any(string("2665246100805992"))},
    {"body", boost::any(vector<string>({
      "ec6ed86e-af53-4c9f-afd3-206c3fc68c64"
    }))}
  }));
  try {
    client->listCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Array | 返回结果。 |
| instanceId | String | 客户数据实例instanceId。 |
| objectType | String | 数据类型。 |
| creatorUserId | String | 创建人的用户userId。 |
| creatorNick | String | 创建人的昵称。 |
| data | Map | 数据内容。 |
| extendData | Map | 扩展数据内容。 |
| permission | Object | 数据权限信息。 |
| ownerStaffIds | Array of String | 负责人用户userId。 |
| participantStaffIds | Array of String | 协同人用户userId。 |
| appUuid | String | 应用appUuid。 |
| formCode | String | 表单formCode。 |
| procOutResult | String | 审批结果。 |
| procInstStatus | String | 审批状态。 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 修改时间。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "instanceId" : "ec6ed86e-af53-4c9f-afd3-206c3fc68c64",
    "objectType" : "crm_customer_personal",
    "creatorUserId" : "2665246100805992",
    "creatorNick" : "小钉",
    "permission" : {
      "ownerStaffIds" : [ "2665246100805992" ],
      "participantStaffIds" : [ "2665246100805992" ]
    },
    "appUuid" : "xxxx-xxxx",
    "formCode" : "xxxx-xxxx",
    "procOutResult" : "agree",
    "procInstStatus" : "COMPLATE",
    "gmtCreate" : "2019-12-25 15:33:12",
    "gmtModified" : "2019-12-25 15:33:12"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.frequent | request too frequent | 请求过于频繁 |
| 400 | relationType.not.exists | relationType not exists | relationType不存在 |
| 400 | systemError.appNotExists | system error app not exists, %s | 应用不存在 |
| 400 | systemError.notPermittedAccess | system error not permitted access, %s | 无操作权限 |
| 500 | systemError | system error %s | 系统错误 |
