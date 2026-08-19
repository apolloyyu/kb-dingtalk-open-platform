---
title: "查询客户数据"
source_url: "https://open.dingtalk.com/document/development/querying-customer-data"
namespace: "development"
slug: "querying-customer-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 查询客户数据"
doc_id: "iv3KX5yNOP"
updated_at: "2025-10-09 18:06:11"
---

> Source: https://open.dingtalk.com/document/development/querying-customer-data
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户 > 查询客户数据
> Updated: 2025-10-09 18:06:11

# 查询客户数据

调用本接口，根据客户的unionId查询客户详情信息，包括客户姓名和客户标签等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/relations/datas/targets/{targetId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-获取CRM主数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| targetId | String | 是 | 客户的unionId，只能通过以下方式获取：   - 企业内部应用，调用[查询用户详情](0056-query-user-details.md)接口获取。 - 第三方企业应用，通过[钉钉统一授权套件](0007-function-description.md)获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| relationType | String | 是 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |

### 请求示例

HTTP

```
GET /v1.0/crm/relations/datas/targets/abc123?relationType=crm_customer HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
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
        QueryRelationDatasByTargetIdHeaders queryRelationDatasByTargetIdHeaders = new QueryRelationDatasByTargetIdHeaders();
        queryRelationDatasByTargetIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryRelationDatasByTargetIdRequest queryRelationDatasByTargetIdRequest = new QueryRelationDatasByTargetIdRequest()
                .setRelationType("crm_customer");
        try {
            client.queryRelationDatasByTargetIdWithOptions("abc123", queryRelationDatasByTargetIdRequest, queryRelationDatasByTargetIdHeaders, new RuntimeOptions());
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
        query_relation_datas_by_target_id_headers = dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdHeaders()
        query_relation_datas_by_target_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_relation_datas_by_target_id_request = dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdRequest(
            relation_type='crm_customer'
        )
        try:
            client.query_relation_datas_by_target_id_with_options('abc123', query_relation_datas_by_target_id_request, query_relation_datas_by_target_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_relation_datas_by_target_id_headers = dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdHeaders()
        query_relation_datas_by_target_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_relation_datas_by_target_id_request = dingtalkcrm__1__0_models.QueryRelationDatasByTargetIdRequest(
            relation_type='crm_customer'
        )
        try:
            await client.query_relation_datas_by_target_id_with_options_async('abc123', query_relation_datas_by_target_id_request, query_relation_datas_by_target_id_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryRelationDatasByTargetIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryRelationDatasByTargetIdRequest;
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
        $queryRelationDatasByTargetIdHeaders = new QueryRelationDatasByTargetIdHeaders([]);
        $queryRelationDatasByTargetIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryRelationDatasByTargetIdRequest = new QueryRelationDatasByTargetIdRequest([
            "relationType" => "crm_customer"
        ]);
        try {
            $client->queryRelationDatasByTargetIdWithOptions("abc123", $queryRelationDatasByTargetIdRequest, $queryRelationDatasByTargetIdHeaders, new RuntimeOptions([]));
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

  queryRelationDatasByTargetIdHeaders := &dingtalkcrm_1_0.QueryRelationDatasByTargetIdHeaders{}
  queryRelationDatasByTargetIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryRelationDatasByTargetIdRequest := &dingtalkcrm_1_0.QueryRelationDatasByTargetIdRequest{
    RelationType: tea.String("crm_customer"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryRelationDatasByTargetIdWithOptions(tea.String("abc123"), queryRelationDatasByTargetIdRequest, queryRelationDatasByTargetIdHeaders, &util.RuntimeOptions{})
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
    let queryRelationDatasByTargetIdHeaders = new $dingtalkcrm_1_0.QueryRelationDatasByTargetIdHeaders({ });
    queryRelationDatasByTargetIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryRelationDatasByTargetIdRequest = new $dingtalkcrm_1_0.QueryRelationDatasByTargetIdRequest({
      relationType: "crm_customer",
    });
    try {
      await client.queryRelationDatasByTargetIdWithOptions("abc123", queryRelationDatasByTargetIdRequest, queryRelationDatasByTargetIdHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryRelationDatasByTargetIdHeaders queryRelationDatasByTargetIdHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryRelationDatasByTargetIdHeaders();
            queryRelationDatasByTargetIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryRelationDatasByTargetIdRequest queryRelationDatasByTargetIdRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryRelationDatasByTargetIdRequest
            {
                RelationType = "crm_customer",
            };
            try
            {
                client.QueryRelationDatasByTargetIdWithOptions("abc123", queryRelationDatasByTargetIdRequest, queryRelationDatasByTargetIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| relations | Array | 客户数据列表。 |
| relationId | String | 客户实例ID。 |
| relationType | String | 客户类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| bizDataList | Array | 客户字段列表。 |
| key | String | 客户字段名。 |
| value | String | 客户字段值。 |
| extendValue | String | 客户字段扩展值。 |
| openConversationIds | Array of String | 客户所在的客户群openConversationId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "relations" : [ {
    "relationId" : "abc123",
    "relationType" : "abc123",
    "bizDataList" : [ {
      "key" : "customer_name",
      "value" : "abc123",
      "extendValue" : "{}"
    } ],
    "openConversationIds" : [ "Aa1F" ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.unionId | invalid unionId | unionId非法 |
| 400 | illegalParameter.relationType | 参数错误：relationType非法 | 参数错误：relationType非法 |
| 500 | systemError.busy | 请求太频繁 | 请求被限流 |
| 500 | systemError | system error %s | 未知错误 |
