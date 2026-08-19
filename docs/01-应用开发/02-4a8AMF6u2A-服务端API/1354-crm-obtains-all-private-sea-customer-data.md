---
title: "获取全量个人或企业客户数据"
source_url: "https://open.dingtalk.com/document/development/crm-obtains-all-private-sea-customer-data"
namespace: "development"
slug: "crm-obtains-all-private-sea-customer-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 获取全量个人或企业客户数据"
doc_id: "eGYQ4bT4dh"
updated_at: "2025-10-09 18:06:08"
---

> Source: https://open.dingtalk.com/document/development/crm-obtains-all-private-sea-customer-data
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户 > 获取全量个人或企业客户数据
> Updated: 2025-10-09 18:06:08

# 获取全量个人或企业客户数据

调用本接口，获取CRM个人或企业客户数据，包括私海个人客户、私海企业客户、公海个人客户、公海企业客户。单个ISV单企业限流1QPS。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/customerInstances |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-获取CRM主数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUserId | String | 否 | 操作人员的userId。 |
| maxResults | Long | 否 | 每页条目数，取值范围1~100。 |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数传空或者null。 - 如果不是首次调用，该参数传上次调用时返回的nextToken。 |
| objectType | String | 否 | 数据类型，不传或者传null时，默认值为**crm\_customer**，具体参数如下。   - **crm\_customer\_personal**：私海个人客户 - **crm\_customer**：私海企业客户 - **open\_customer\_personal**：公海个人客户 - **open\_customer\_org**：公海企业客户 |

### 请求示例

HTTP

```
POST /v1.0/crm/customerInstances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1289367jkasdhjkashd78912yej
Content-Type:application/json

{
  "operatorUserId" : "ding_userid",
  "maxResults" : 100,
  "nextToken" : "100010",
  "objectType" : "crm_customer"
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
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcrm_1_0.models.QueryAllCustomerHeaders queryAllCustomerHeaders = new com.aliyun.dingtalkcrm_1_0.models.QueryAllCustomerHeaders();
        queryAllCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.QueryAllCustomerRequest queryAllCustomerRequest = new com.aliyun.dingtalkcrm_1_0.models.QueryAllCustomerRequest()
                .setOperatorUserId("ding_userid")
                .setMaxResults(100L)
                .setNextToken("100010")
                .setObjectType("crm_customer");
        try {
            client.queryAllCustomerWithOptions(queryAllCustomerRequest, queryAllCustomerHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_all_customer_headers = dingtalkcrm__1__0_models.QueryAllCustomerHeaders()
        query_all_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_all_customer_request = dingtalkcrm__1__0_models.QueryAllCustomerRequest(
            operator_user_id='ding_userid',
            max_results=100,
            next_token='100010',
            object_type='crm_customer'
        )
        try:
            client.query_all_customer_with_options(query_all_customer_request, query_all_customer_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_all_customer_headers = dingtalkcrm__1__0_models.QueryAllCustomerHeaders()
        query_all_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_all_customer_request = dingtalkcrm__1__0_models.QueryAllCustomerRequest(
            operator_user_id='ding_userid',
            max_results=100,
            next_token='100010',
            object_type='crm_customer'
        )
        try:
            await client.query_all_customer_with_options_async(query_all_customer_request, query_all_customer_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryAllCustomerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryAllCustomerRequest;
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
        $queryAllCustomerHeaders = new QueryAllCustomerHeaders([]);
        $queryAllCustomerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryAllCustomerRequest = new QueryAllCustomerRequest([
            "operatorUserId" => "ding_userid",
            "maxResults" => 100,
            "nextToken" => "100010",
            "objectType" => "crm_customer"
        ]);
        try {
            $client->queryAllCustomerWithOptions($queryAllCustomerRequest, $queryAllCustomerHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  queryAllCustomerHeaders := &dingtalkcrm_1_0.QueryAllCustomerHeaders{}
  queryAllCustomerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryAllCustomerRequest := &dingtalkcrm_1_0.QueryAllCustomerRequest{
    OperatorUserId: tea.String("ding_userid"),
    MaxResults: tea.Int64(100),
    NextToken: tea.String("100010"),
    ObjectType: tea.String("crm_customer"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryAllCustomerWithOptions(queryAllCustomerRequest, queryAllCustomerHeaders, &util.RuntimeOptions{})
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
    let queryAllCustomerHeaders = new $dingtalkcrm_1_0.QueryAllCustomerHeaders({ });
    queryAllCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryAllCustomerRequest = new $dingtalkcrm_1_0.QueryAllCustomerRequest({
      operatorUserId: "ding_userid",
      maxResults: 100,
      nextToken: "100010",
      objectType: "crm_customer",
    });
    try {
      await client.queryAllCustomerWithOptions(queryAllCustomerRequest, queryAllCustomerHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryAllCustomerHeaders queryAllCustomerHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryAllCustomerHeaders();
            queryAllCustomerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryAllCustomerRequest queryAllCustomerRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryAllCustomerRequest
            {
                OperatorUserId = "ding_userid",
                MaxResults = 100,
                NextToken = "100010",
                ObjectType = "crm_customer",
            };
            try
            {
                client.QueryAllCustomerWithOptions(queryAllCustomerRequest, queryAllCustomerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 分页结果。 |
| nextToken | String | 下一页的游标，为null则表示无更多数据。 |
| values | Array | 客户数据列表。 |
| creatorNick | String | 创建记录的用户昵称。 |
| modifyTime | String | 记录修改时间。 |
| creatorUserId | String | 创建记录的用户的userId。 |
| instanceId | String | 客户数据ID。 |
| data | Map | 数据内容。 |
| extendData | Map | 扩展数据内容。 |
| createTime | String | 记录创建时间。 |
| objectType | String | 数据类型：   - **crm\_customer\_personal**：私海个人客户 - **crm\_customer**：私海企业客户 - **open\_customer\_personal**：公海个人客户 - **open\_customer\_org**：公海企业客户 |
| permission | Object | 数据权限信息。 |
| participantStaffIds | Array of String | 协同人用户userId。 |
| ownerStaffIds | Array of String | 负责人用户userId。 |
| processOutResult | String | 审批结果。   - **terminate**：撤销 - **agree**：同意 - **refuse**：拒绝       本接口返回都是agree。 |
| processInstanceStatus | String | 审批状态。   - **NEW**：新创建 - **RUNNING**：审批中 - **TERMINATED**：撤销 - **COMPLETED**：完成       本接口返回都是COMPLETED。 |
| maxResults | Long | 每页条目数量。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "nextToken" : "100",
    "values" : [ {
      "creatorNick" : "张三",
      "modifyTime" : "2019-12-25 15:33:12",
      "creatorUserId" : "ding_userid",
      "instanceId" : "instance_id",
      "createTime" : "2019-12-25 15:33:12",
      "objectType" : "crm_customer",
      "permission" : {
        "participantStaffIds" : [ "staff_id" ],
        "ownerStaffIds" : [ "staff_id" ]
      },
      "processOutResult" : "agree",
      "processInstanceStatus" : "COMPLETE"
    } ],
    "maxResults" : 100
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | crm.not.installed | crm.not.installed | 客户管理应用未安装。 |
| 400 | request.too.frequent | 请求太频繁 | 请求过于频繁。 |
| 400 | invalid.objectType | invalid objectType | 不存在的objectType |
| 400 | param.error | 参数非法 | 参数非法 |
| 400 | org.not.exists | org not exists | 组织不存在或已解散 |
| 500 | system.error | 系统错误 | 系统错误 |
