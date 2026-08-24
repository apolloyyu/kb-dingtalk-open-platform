---
title: "批量更新个人或企业客户数据"
source_url: "https://open.dingtalk.com/document/development/update-multiple-relational-data-tables-at-a-time"
namespace: "development"
slug: "update-multiple-relational-data-tables-at-a-time"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 批量更新个人或企业客户数据"
doc_id: "ToGj8sC5Uo"
updated_at: "2026-07-21 09:26:18"
---

> Source: https://open.dingtalk.com/document/development/update-multiple-relational-data-tables-at-a-time
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户 > 批量更新个人或企业客户数据
> Updated: 2026-07-21 09:26:18

# 批量更新个人或企业客户数据

调用本接口，批量修改个人客户、企业客户数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/relationDatas/batch |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_write-维护CRM主数据的接口写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| relationType | String | 是 | 客户类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| operatorUserId | String | 是 | 操作人userId。 |
| skipDuplicateCheck | Boolean | 否 | 是否跳过查重，默认不跳过。   - **true**：是 - **false**：否   企业可在查重设置中设置查重字段，如下图所示。 |
| relationList | Array | 是 | 更新的客户数据列表，最大值10。 |
| bizDataList | Array | 否 | 更新的客户模型数据列表，最大值256。 |
| key | String | 是 | 模型字段key，该参数传客户对象元数据信息中获取字段的name值，调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口获取name参数值。  该参数是否必填，取决于调用获取客户对象的元数据信息接口，返回的nillable字段值：   - nillable是**true**：本接口参数key和value为非必填。 - nillable是**false**：本接口参数key和value为必填。 |
| value | String | 是 | 模型字段value，不同类型的组件value值格式不同，请参考[新增和更新客户字段格式说明V2](1390-the-model-fields-supported-by-the-interface-and-their-value.md)。  该参数是否必填，取决于调用获取客户对象的元数据信息接口，返回的nillable字段值：   - nillable是**true**：本接口参数key和value为非必填。 - nillable是**false**：本接口参数key和value为必填。 |
| extendValue | String | 否 | 模型字段extendValue。 |
| bizExtMap | Map<String, String> | 否 | 扩展业务字段。      该参数暂不支持使用。 |
| relationId | String | 是 | 客户数据ID，调用[根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口获取instanceId参数值。 |

### 请求示例

HTTP

```
PUT /v1.0/crm/relationDatas/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fghsdffgnfghjghcvbgfghertyghjghj
Content-Type:application/json

{
  "relationType" : "crm_customer",
  "operatorUserId" : "manager021a",
  "skipDuplicateCheck" : false,
  "relationList" : [ {
    "bizDataList" : [ {
      "key" : "TextField_71U51A",
      "value" : "XX有限公司",
      "extendValue" : "{}"
    } ],
    "bizExtMap" : {
      "key" : "1"
    },
    "relationId" : "fasdg8i814-0afsd"
  } ]
}
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
        BatchUpdateRelationDatasHeaders batchUpdateRelationDatasHeaders = new BatchUpdateRelationDatasHeaders();
        batchUpdateRelationDatasHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
            new TeaPair("key", "1")
        );
        BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationListBizDataList relationList0BizDataList0 = new BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationListBizDataList()
                .setKey("TextField_71U51A")
                .setValue("XX有限公司")
                .setExtendValue("{}");
        BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList relationList0 = new BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList()
                .setBizDataList(java.util.Arrays.asList(
                    relationList0BizDataList0
                ))
                .setBizExtMap(relationList0BizExtMap)
                .setRelationId("fasdg8i814-0afsd");
        BatchUpdateRelationDatasRequest batchUpdateRelationDatasRequest = new BatchUpdateRelationDatasRequest()
                .setRelationType("crm_customer")
                .setOperatorUserId("manager021a")
                .setSkipDuplicateCheck(false)
                .setRelationList(java.util.Arrays.asList(
                    relationList0
                ));
        try {
            client.batchUpdateRelationDatasWithOptions(batchUpdateRelationDatasRequest, batchUpdateRelationDatasHeaders, new RuntimeOptions());
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
        batch_update_relation_datas_headers = dingtalkcrm__1__0_models.BatchUpdateRelationDatasHeaders()
        batch_update_relation_datas_headers.x_acs_dingtalk_access_token = '<your access token>'
        relation_list_0biz_ext_map = {
            'key': '1'
        }
        relation_list_0biz_data_list_0 = dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequestRelationListBizDataList(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{}'
        )
        relation_list_0 = dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequestRelationList(
            biz_data_list=[
                relation_list_0biz_data_list_0
            ],
            biz_ext_map=relation_list_0biz_ext_map,
            relation_id='fasdg8i814-0afsd'
        )
        batch_update_relation_datas_request = dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequest(
            relation_type='crm_customer',
            operator_user_id='manager021a',
            skip_duplicate_check=False,
            relation_list=[
                relation_list_0
            ]
        )
        try:
            client.batch_update_relation_datas_with_options(batch_update_relation_datas_request, batch_update_relation_datas_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_update_relation_datas_headers = dingtalkcrm__1__0_models.BatchUpdateRelationDatasHeaders()
        batch_update_relation_datas_headers.x_acs_dingtalk_access_token = '<your access token>'
        relation_list_0biz_ext_map = {
            'key': '1'
        }
        relation_list_0biz_data_list_0 = dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequestRelationListBizDataList(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{}'
        )
        relation_list_0 = dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequestRelationList(
            biz_data_list=[
                relation_list_0biz_data_list_0
            ],
            biz_ext_map=relation_list_0biz_ext_map,
            relation_id='fasdg8i814-0afsd'
        )
        batch_update_relation_datas_request = dingtalkcrm__1__0_models.BatchUpdateRelationDatasRequest(
            relation_type='crm_customer',
            operator_user_id='manager021a',
            skip_duplicate_check=False,
            relation_list=[
                relation_list_0
            ]
        )
        try:
            await client.batch_update_relation_datas_with_options_async(batch_update_relation_datas_request, batch_update_relation_datas_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateRelationDatasHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateRelationDatasRequest\relationList\bizDataList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateRelationDatasRequest\relationList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateRelationDatasRequest;
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
        $batchUpdateRelationDatasHeaders = new BatchUpdateRelationDatasHeaders([]);
        $batchUpdateRelationDatasHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $relationList0BizExtMap = [
            "key" => "1"
        ];
        $relationList0BizDataList0 = new bizDataList([
            "key" => "TextField_71U51A",
            "value" => "XX有限公司",
            "extendValue" => "{}"
        ]);
        $relationList0 = new relationList([
            "bizDataList" => [
                $relationList0BizDataList0
            ],
            "bizExtMap" => $relationList0BizExtMap,
            "relationId" => "fasdg8i814-0afsd"
        ]);
        $batchUpdateRelationDatasRequest = new BatchUpdateRelationDatasRequest([
            "relationType" => "crm_customer",
            "operatorUserId" => "manager021a",
            "skipDuplicateCheck" => false,
            "relationList" => [
                $relationList0
            ]
        ]);
        try {
            $client->batchUpdateRelationDatasWithOptions($batchUpdateRelationDatasRequest, $batchUpdateRelationDatasHeaders, new RuntimeOptions([]));
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

  batchUpdateRelationDatasHeaders := &dingtalkcrm_1_0.BatchUpdateRelationDatasHeaders{}
  batchUpdateRelationDatasHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  relationList0BizExtMap := map[string]*string{
    "key": tea.String("1"),
  }
  relationList0BizDataList0 := &dingtalkcrm_1_0.BatchUpdateRelationDatasRequestRelationListBizDataList{
    Key: tea.String("TextField_71U51A"),
    Value: tea.String("XX有限公司"),
    ExtendValue: tea.String("{}"),
  }
  relationList0 := &dingtalkcrm_1_0.BatchUpdateRelationDatasRequestRelationList{
    BizDataList: []*dingtalkcrm_1_0.BatchUpdateRelationDatasRequestRelationListBizDataList{relationList0BizDataList0},
    BizExtMap: relationList0BizExtMap,
    RelationId: tea.String("fasdg8i814-0afsd"),
  }
  batchUpdateRelationDatasRequest := &dingtalkcrm_1_0.BatchUpdateRelationDatasRequest{
    RelationType: tea.String("crm_customer"),
    OperatorUserId: tea.String("manager021a"),
    SkipDuplicateCheck: tea.Bool(false),
    RelationList: []*dingtalkcrm_1_0.BatchUpdateRelationDatasRequestRelationList{relationList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchUpdateRelationDatasWithOptions(batchUpdateRelationDatasRequest, batchUpdateRelationDatasHeaders, &util.RuntimeOptions{})
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
    let batchUpdateRelationDatasHeaders = new $dingtalkcrm_1_0.BatchUpdateRelationDatasHeaders({ });
    batchUpdateRelationDatasHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let relationList0BizExtMap = {
      key: "1",
    };
    let relationList0BizDataList0 = new $dingtalkcrm_1_0.BatchUpdateRelationDatasRequestRelationListBizDataList({
      key: "TextField_71U51A",
      value: "XX有限公司",
      extendValue: "{}",
    });
    let relationList0 = new $dingtalkcrm_1_0.BatchUpdateRelationDatasRequestRelationList({
      bizDataList: [
        relationList0BizDataList0
      ],
      bizExtMap: relationList0BizExtMap,
      relationId: "fasdg8i814-0afsd",
    });
    let batchUpdateRelationDatasRequest = new $dingtalkcrm_1_0.BatchUpdateRelationDatasRequest({
      relationType: "crm_customer",
      operatorUserId: "manager021a",
      skipDuplicateCheck: false,
      relationList: [
        relationList0
      ],
    });
    try {
      await client.batchUpdateRelationDatasWithOptions(batchUpdateRelationDatasRequest, batchUpdateRelationDatasHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasHeaders batchUpdateRelationDatasHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasHeaders();
            batchUpdateRelationDatasHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> relationList0BizExtMap = new Dictionary<string, string>
            {
                {"key", "1"},
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList.BatchUpdateRelationDatasRequestRelationListBizDataList relationList0BizDataList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList.BatchUpdateRelationDatasRequestRelationListBizDataList
            {
                Key = "TextField_71U51A",
                Value = "XX有限公司",
                ExtendValue = "{}",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList relationList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList
            {
                BizDataList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList.BatchUpdateRelationDatasRequestRelationListBizDataList>
                {
                    relationList0BizDataList0
                },
                BizExtMap = relationList0BizExtMap,
                RelationId = "fasdg8i814-0afsd",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest batchUpdateRelationDatasRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest
            {
                RelationType = "crm_customer",
                OperatorUserId = "manager021a",
                SkipDuplicateCheck = false,
                RelationList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList>
                {
                    relationList0
                },
            };
            try
            {
                client.BatchUpdateRelationDatasWithOptions(batchUpdateRelationDatasRequest, batchUpdateRelationDatasHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| results | Array | 批量更新结果列表，results返回结果和新增数据顺序是一致的，可以查看每条客户数据分别对应的结果是否成功。      例如，调用本接口批量更新了两个客户，第一个客户字段被查重规则拦截导致写入失败；第二个客户写入正常。返回的信息格式为 |
| success | Boolean | 调用是否成功，true表示成功。 |
| errorCode | String | 错误码。   - 如果更新失败，表示失败的错误码。 - 如果更新成功，该字段不返回。 |
| errorMsg | String | 错误信息。   - 如果更新失败，表示失败的错误原因。 - 如果更新成功，该字段不返回。 |
| relationId | String | 更新成功的客户Id。 |
| duplicatedRelationIds | Array of String | 更新客户反馈信息。   - 如果更新客户成功，该字段返回空。 - 如果因为查重导致失败，表示重复的客户Id列表。 - 如果是其他原因导致的失败，该字段返回空，可以查看errorMsg返回的错误详情。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "results" : [ {
    "success" : true,
    "errorCode" : "1002",
    "errorMsg" : "查重失败",
    "relationId" : "gads1ag-sfgasdfxcvxb",
    "duplicatedRelationIds" : [ "gads1ag-sfgasdfxcvx11" ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | fieldId.not.exists | %s | 关系表结构字段缺失 |
| 400 | invalid.relationId | invalid parameter: relationId | relationId不存在 |
| 400 | invalid.relationType | invalid parameter: relationType | relationType不存在 |
| 400 | invalid.content | %s | 内容存在违禁词 |
| 400 | no.permission | %s | 无权限 |
| 400 | operatorUserId.not.exist | operatorUserId not exist | 操作者不存在 |
| 400 | crmApp.not.installed | crm app is not installed | CRM应用未安装 |
| 400 | system.busy | system busy | 请求过于频繁 |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 500 | unknown.error | unknownError | 未知错误 |
