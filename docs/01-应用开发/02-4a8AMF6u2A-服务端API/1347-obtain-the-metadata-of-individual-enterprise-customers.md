---
title: "获取个人或企业客户的元数据"
source_url: "https://open.dingtalk.com/document/development/obtain-the-metadata-of-individual-enterprise-customers"
namespace: "development"
slug: "obtain-the-metadata-of-individual-enterprise-customers"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 获取个人或企业客户的元数据"
doc_id: "5MHKbt0NUG"
updated_at: "2025-12-08 14:14:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-metadata-of-individual-enterprise-customers
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户 > 获取个人或企业客户的元数据
> Updated: 2025-12-08 14:14:33

# 获取个人或企业客户的元数据

调用本接口，获取CRM个人客户或企业客户的元数据描述，包括字段名、字段Id、字段类型等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/personalCustomers/objectMeta |
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
| relationType | String | 否 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |

### 请求示例

HTTP

```
GET /v1.0/crm/personalCustomers/objectMeta?relationType=crm_customer_personal HTTP/1.1
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
        DescribeCrmPersonalCustomerObjectMetaHeaders describeCrmPersonalCustomerObjectMetaHeaders = new DescribeCrmPersonalCustomerObjectMetaHeaders();
        describeCrmPersonalCustomerObjectMetaHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DescribeCrmPersonalCustomerObjectMetaRequest describeCrmPersonalCustomerObjectMetaRequest = new DescribeCrmPersonalCustomerObjectMetaRequest()
                .setRelationType("crm_customer_personal");
        try {
            client.describeCrmPersonalCustomerObjectMetaWithOptions(describeCrmPersonalCustomerObjectMetaRequest, describeCrmPersonalCustomerObjectMetaHeaders, new RuntimeOptions());
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
        describe_crm_personal_customer_object_meta_headers = dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaHeaders()
        describe_crm_personal_customer_object_meta_headers.x_acs_dingtalk_access_token = '<your access token>'
        describe_crm_personal_customer_object_meta_request = dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaRequest(
            relation_type='crm_customer_personal'
        )
        try:
            client.describe_crm_personal_customer_object_meta_with_options(describe_crm_personal_customer_object_meta_request, describe_crm_personal_customer_object_meta_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_crm_personal_customer_object_meta_headers = dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaHeaders()
        describe_crm_personal_customer_object_meta_headers.x_acs_dingtalk_access_token = '<your access token>'
        describe_crm_personal_customer_object_meta_request = dingtalkcrm__1__0_models.DescribeCrmPersonalCustomerObjectMetaRequest(
            relation_type='crm_customer_personal'
        )
        try:
            await client.describe_crm_personal_customer_object_meta_with_options_async(describe_crm_personal_customer_object_meta_request, describe_crm_personal_customer_object_meta_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\DescribeCrmPersonalCustomerObjectMetaHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\DescribeCrmPersonalCustomerObjectMetaRequest;
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
        $describeCrmPersonalCustomerObjectMetaHeaders = new DescribeCrmPersonalCustomerObjectMetaHeaders([]);
        $describeCrmPersonalCustomerObjectMetaHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $describeCrmPersonalCustomerObjectMetaRequest = new DescribeCrmPersonalCustomerObjectMetaRequest([
            "relationType" => "crm_customer_personal"
        ]);
        try {
            $client->describeCrmPersonalCustomerObjectMetaWithOptions($describeCrmPersonalCustomerObjectMetaRequest, $describeCrmPersonalCustomerObjectMetaHeaders, new RuntimeOptions([]));
        }
        catch (Exception $err) {
            if (!($err instanceof TeaError)) {
                $err = new TeaError([], $err->getMessage(), $err->getCode(), $err);
            }
            if (!Utils::empty_($err->code) && !Utils::empty_($err->message)) {
                // err 中含有 code 和 message 属性，可���助开发定位问题
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

  describeCrmPersonalCustomerObjectMetaHeaders := &dingtalkcrm_1_0.DescribeCrmPersonalCustomerObjectMetaHeaders{}
  describeCrmPersonalCustomerObjectMetaHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  describeCrmPersonalCustomerObjectMetaRequest := &dingtalkcrm_1_0.DescribeCrmPersonalCustomerObjectMetaRequest{
    RelationType: tea.String("crm_customer_personal"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DescribeCrmPersonalCustomerObjectMetaWithOptions(describeCrmPersonalCustomerObjectMetaRequest, describeCrmPersonalCustomerObjectMetaHeaders, &util.RuntimeOptions{})
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
    let describeCrmPersonalCustomerObjectMetaHeaders = new $dingtalkcrm_1_0.DescribeCrmPersonalCustomerObjectMetaHeaders({ });
    describeCrmPersonalCustomerObjectMetaHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let describeCrmPersonalCustomerObjectMetaRequest = new $dingtalkcrm_1_0.DescribeCrmPersonalCustomerObjectMetaRequest({
      relationType: "crm_customer_personal",
    });
    try {
      await client.describeCrmPersonalCustomerObjectMetaWithOptions(describeCrmPersonalCustomerObjectMetaRequest, describeCrmPersonalCustomerObjectMetaHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DescribeCrmPersonalCustomerObjectMetaHeaders describeCrmPersonalCustomerObjectMetaHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DescribeCrmPersonalCustomerObjectMetaHeaders();
            describeCrmPersonalCustomerObjectMetaHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DescribeCrmPersonalCustomerObjectMetaRequest describeCrmPersonalCustomerObjectMetaRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DescribeCrmPersonalCustomerObjectMetaRequest
            {
                RelationType = "crm_customer_personal",
            };
            try
            {
                client.DescribeCrmPersonalCustomerObjectMetaWithOptions(describeCrmPersonalCustomerObjectMetaRequest, describeCrmPersonalCustomerObjectMetaHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| name | String | 对象名称。 |
| customized | Boolean | 是否自定义对象。   - **true**：是 - **false**：不是 |
| fields | Array | 字段列表。 |
| name | String | 字段名称。 |
| customized | Boolean | 是否自定义字段。   - **true**：是 - **false**：不是 |
| label | String | 字段展示名。 |
| type | String | 字段类型。 |
| nillable | Boolean | 是否可空。   - **true**：可以为空。 - **false**：不能为空。 |
| format | String | 日期格式。 |
| unit | String | 日期单位或金额单位。 |
| selectOptions | Array | 选项列表。 |
| key | String | 选项key。 |
| value | String | 选项值。 |
| quote | Boolean | 是否引用关联。   - **true**：引用 - **false**：不引用 |
| referenceTo | String | 关联对象名称。 |
| referenceFields | Array | 引用的关联对象的字段列表。 |
| label | String | 引用的关联对象字段显示名。 |
| type | String | 引用的关联对象字段类型。 |
| nillable | Boolean | 引用的关联对象字段是否可空。   - **true**：可以为空 - **false**：不能为空 |
| unit | String | 引用的关联对象字段单位。 |
| format | String | 引用的关联对象字段格式。 |
| selectOptions | Array | 引用的关联对象的字段选项列表。 |
| key | String | 引用的关联对象的字段选项key。 |
| value | String | 引用的关联对象的字段选项值。 |
| name | String | 引用的关联对象的字段名称。 |
| rollUpSummaryFields | Array | 对MasterDetail类型有效。 |
| name | String | 需要汇总的明细内字段名。 |
| aggregator | String | 汇总方法。 |
| status | String | 表单状态。   - **PUBLISHED**：已发布 - **INVALID**：已停用 |
| code | String | 表单code。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "name" : "对象名称",
  "customized" : false,
  "fields" : [ {
    "name" : "customer_name",
    "customized" : false,
    "label" : "抱壹",
    "type" : "Text",
    "nillable" : false,
    "format" : "yyyy-MM-dd",
    "unit" : "天",
    "selectOptions" : [ {
      "key" : "option_1",
      "value" : "选项1"
    } ],
    "quote" : true,
    "referenceTo" : "crm_contact",
    "referenceFields" : [ {
      "label" : "联系人名称",
      "type" : "Text",
      "nillable" : false,
      "unit" : "天",
      "format" : "yyyy-MM-dd",
      "selectOptions" : [ {
        "key" : "option_2",
        "value" : "选项2"
      } ],
      "name" : "crm_customer"
    } ],
    "rollUpSummaryFields" : [ {
      "name" : "Money-XDADDF",
      "aggregator" : "SUM"
    } ]
  } ],
  "status" : "PUBLISHED",
  "code" : "PROC-XXXX"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | invalid param, %s | 应用id不能为空 |
| 400 | systemError.notPermittedAccess | system error, %s | 无权限操作 |
| 400 | systemError | system error, %s | 获取模板归属应用失败 |
| 400 | businessError | businessError, %s | 业务错误 |
