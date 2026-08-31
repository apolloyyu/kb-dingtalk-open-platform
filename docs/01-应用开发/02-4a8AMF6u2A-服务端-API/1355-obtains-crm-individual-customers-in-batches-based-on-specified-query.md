---
title: "根据指定条件查询个人或企业客户数据"
source_url: "https://open.dingtalk.com/document/development/obtains-crm-individual-customers-in-batches-based-on-specified-query"
namespace: "development"
slug: "obtains-crm-individual-customers-in-batches-based-on-specified-query"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 根据指定条件查询个人或企业客户数据"
doc_id: "jrpbAhrWLe"
updated_at: "2026-06-04 19:12:10"
---

> Source: https://open.dingtalk.com/document/development/obtains-crm-individual-customers-in-batches-based-on-specified-query
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 客户 > 根据指定条件查询个人或企业客户数据
> Updated: 2026-06-04 19:12:10

# 根据指定条件查询个人或企业客户数据

调用本接口，根据指定条件查询CRM个人客户或企业客户数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/personalCustomers |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-获取CRM主数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| currentOperatorUserId | String | 否 | 用户userId。 |
| relationType | String | 否 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| nextToken | String | 否 | 分页游标，获取下一页时传入上一页返回的nextToken。 |
| maxResults | Integer | 是 | 每页条数，最大值100。 |
| queryDsl | String | 否 | 查询条件，参考[查询DSL说明](1393-inner-query-dsl-description.md)。 |

### 请求示例

HTTP

```
GET /v1.0/crm/personalCustomers?currentOperatorUserId=2665246xxx&relationType=crm_customer_personal&nextToken=0&maxResults=10&queryDsl={"queryGroupList":[{"logicType":"AND","queryObjectList":[{"fieldId":"customer_name","filterType":"EQ","value":"xx有限公司"}]}]} HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c36409xxxx
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
        QueryCrmPersonalCustomerHeaders queryCrmPersonalCustomerHeaders = new QueryCrmPersonalCustomerHeaders();
        queryCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryCrmPersonalCustomerRequest queryCrmPersonalCustomerRequest = new QueryCrmPersonalCustomerRequest()
                .setCurrentOperatorUserId("2665246xxx")
                .setRelationType("crm_customer_personal")
                .setNextToken("0")
                .setMaxResults(10)
                .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}");
        try {
            client.queryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, new RuntimeOptions());
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
        query_crm_personal_customer_headers = dingtalkcrm__1__0_models.QueryCrmPersonalCustomerHeaders()
        query_crm_personal_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_crm_personal_customer_request = dingtalkcrm__1__0_models.QueryCrmPersonalCustomerRequest(
            current_operator_user_id='2665246xxx',
            relation_type='crm_customer_personal',
            next_token='0',
            max_results=10,
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"fieldId":"customer_name","filterType":"EQ","value":"xx有限公司"}]}]}'
        )
        try:
            client.query_crm_personal_customer_with_options(query_crm_personal_customer_request, query_crm_personal_customer_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_crm_personal_customer_headers = dingtalkcrm__1__0_models.QueryCrmPersonalCustomerHeaders()
        query_crm_personal_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_crm_personal_customer_request = dingtalkcrm__1__0_models.QueryCrmPersonalCustomerRequest(
            current_operator_user_id='2665246xxx',
            relation_type='crm_customer_personal',
            next_token='0',
            max_results=10,
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"fieldId":"customer_name","filterType":"EQ","value":"xx有限公司"}]}]}'
        )
        try:
            await client.query_crm_personal_customer_with_options_async(query_crm_personal_customer_request, query_crm_personal_customer_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryCrmPersonalCustomerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryCrmPersonalCustomerRequest;
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
        $queryCrmPersonalCustomerHeaders = new QueryCrmPersonalCustomerHeaders([]);
        $queryCrmPersonalCustomerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryCrmPersonalCustomerRequest = new QueryCrmPersonalCustomerRequest([
            "currentOperatorUserId" => "2665246xxx",
            "relationType" => "crm_customer_personal",
            "nextToken" => "0",
            "maxResults" => 10,
            "queryDsl" => "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}"
        ]);
        try {
            $client->queryCrmPersonalCustomerWithOptions($queryCrmPersonalCustomerRequest, $queryCrmPersonalCustomerHeaders, new RuntimeOptions([]));
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

  queryCrmPersonalCustomerHeaders := &dingtalkcrm_1_0.QueryCrmPersonalCustomerHeaders{}
  queryCrmPersonalCustomerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryCrmPersonalCustomerRequest := &dingtalkcrm_1_0.QueryCrmPersonalCustomerRequest{
    CurrentOperatorUserId: tea.String("2665246xxx"),
    RelationType: tea.String("crm_customer_personal"),
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(10),
    QueryDsl: tea.String("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, &util.RuntimeOptions{})
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
    let queryCrmPersonalCustomerHeaders = new $dingtalkcrm_1_0.QueryCrmPersonalCustomerHeaders({ });
    queryCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryCrmPersonalCustomerRequest = new $dingtalkcrm_1_0.QueryCrmPersonalCustomerRequest({
      currentOperatorUserId: "2665246xxx",
      relationType: "crm_customer_personal",
      nextToken: "0",
      maxResults: 10,
      queryDsl: "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}",
    });
    try {
      await client.queryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmPersonalCustomerHeaders queryCrmPersonalCustomerHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmPersonalCustomerHeaders();
            queryCrmPersonalCustomerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmPersonalCustomerRequest queryCrmPersonalCustomerRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmPersonalCustomerRequest
            {
                CurrentOperatorUserId = "2665246xxx",
                RelationType = "crm_customer_personal",
                NextToken = "0",
                MaxResults = 10,
                QueryDsl = "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}",
            };
            try
            {
                client.QueryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::QueryCrmPersonalCustomerHeaders> queryCrmPersonalCustomerHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::QueryCrmPersonalCustomerHeaders>();
  queryCrmPersonalCustomerHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::QueryCrmPersonalCustomerRequest> queryCrmPersonalCustomerRequest = make_shared<Alibabacloud_Dingtalkcrm_1_0::QueryCrmPersonalCustomerRequest>(map<string, boost::any>({
    {"currentOperatorUserId", boost::any(string("2665246xxx"))},
    {"relationType", boost::any(string("crm_customer_personal"))},
    {"nextToken", boost::any(string("0"))},
    {"maxResults", boost::any(10)},
    {"queryDsl", boost::any(string("{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"fieldId":"customer_name","filterType":"EQ","value":"xx有限公司"}]}]}"))}
  }));
  try {
    client->queryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| values | Array | 返回结果。 |
| instanceId | String | 数据ID。 |
| objectType | String | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| creatorUserId | String | 创建记录的用户userId。 |
| creatorNick | String | 创建记录的用户昵称。 |
| data | Map | 数据内容。 |
| extendData | Map | 扩展数据内容。 |
| permission | Object | 数据权限信息。 |
| ownerStaffIds | Array of String | 负责人用户userId列表。 |
| participantStaffIds | Array of String | 协同人用户userId列表。 |
| procOutResult | String | 审批结果。 |
| procInstStatus | String | 审批状态。 |
| gmtCreate | String | 记录创建时间。 |
| gmtModified | String | 记录修改时间。 |
| hasMore | Boolean | 是否有下一页。   - **true**：有 - **false**：没有 |
| nextToken | String | 分页游标。 |
| maxResults | Integer | 分页大小。 |
| totalCount | Integer | 总条数。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "values" : [ {
    "instanceId" : "8a0d5031-xxx",
    "objectType" : "crm_customer_personal",
    "creatorUserId" : "266524610xxxx",
    "creatorNick" : "小钉",
    "permission" : {
      "ownerStaffIds" : [ "2665246xxxx" ],
      "participantStaffIds" : [ "266524610xxx" ]
    },
    "procOutResult" : "agree",
    "procInstStatus" : "COMPLATE",
    "gmtCreate" : "2019-12-25 15:33:12",
    "gmtModified" : "2019-12-25 15:33:12"
  } ],
  "hasMore" : true,
  "nextToken" : "10",
  "maxResults" : 10,
  "totalCount" : 1000
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | queryDsl.invalid.json | queryDsl is not json format | queryDsl不是有效的JSON字符串 |
| 400 | request.too.frequent | request too frequent | 请求过于频繁 |
| 400 | relationType.not.exists | relationType not exists | relationType不存在 |
| 400 | systemError.appNotExists | system error, app not exists, %s | 应用不存在 |
| 400 | systemError.notPermittedAccess | system error, not permitted access, %s | 无权限操作 |
| 400 | crmAppNotExisted | crmAppNotExisted | 客户管理应用不存在 |
| 500 | systemError | system error %s | 系统错误 |
