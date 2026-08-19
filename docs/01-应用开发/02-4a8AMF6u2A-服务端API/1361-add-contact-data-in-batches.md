---
title: "批量新增联系人数据"
source_url: "https://open.dingtalk.com/document/development/add-contact-data-in-batches"
namespace: "development"
slug: "add-contact-data-in-batches"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 联系人管理 > 批量新增联系人数据"
doc_id: "yPIo68XCUs"
updated_at: "2025-10-09 18:06:14"
---

> Source: https://open.dingtalk.com/document/development/add-contact-data-in-batches
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 联系人管理 > 批量新增联系人数据
> Updated: 2025-10-09 18:06:14

# 批量新增联系人数据

调用本接口，批量新增联系人数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/contacts/batch |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_write-维护CRM主数据的接口写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUserId | String | 是 | 操作人userId。 |
| relationList | Array | 是 | 联系人数据列表，最大值10。 |
| bizDataList | Array | 是 | 新增联系人的模型数据列表，最大值256。 |
| key | String | 是 | 模型字段key，该参数传[获取联系人的元数据](1364-gets-the-metadata-description-of-a-crm-contact-object.md)接口中获取的name字段值。      该参数是否必填，取决于**获取联系人的元数据**接口，返回的nillable字段值。   - nillable是**true**：本接口参数key和value为非必填。 - nillable是**false**：本接口参数key和value为必填。 |
| value | String | 是 | 模型字段value，不同类型的组件value值格式不同，请参考[新增和更新联系人字段格式说明V2](1392-add-and-update-contact-field-format-description-v2.md)。 |
| extendValue | String | 否 | 模型字段extendValue。 |
| bizExtMap | Map<String, String> | 否 | 扩展业务字段。      该参数暂不支持使用。 |

### 请求示例

HTTP

```
POST /v1.0/crm/contacts/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fghsdffgnfghjghcvbgfghertyghjghj
Content-Type:application/json

{
  "operatorUserId" : "manager021a",
  "relationList" : [ {
    "bizDataList" : [ {
      "key" : "TextField_71U51A",
      "value" : "XX有限公司",
      "extendValue" : "{}"
    } ],
    "bizExtMap" : {
      "key" : "{}"
    }
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
        BatchAddContactsHeaders batchAddContactsHeaders = new BatchAddContactsHeaders();
        batchAddContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
            new TeaPair("key", "{}")
        );
        BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList0 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                .setKey("TextField_71U51A")
                .setValue("XX有限公司")
                .setExtendValue("{}");
        BatchAddContactsRequest.BatchAddContactsRequestRelationList relationList0 = new BatchAddContactsRequest.BatchAddContactsRequestRelationList()
                .setBizDataList(java.util.Arrays.asList(
                    relationList0BizDataList0
                ))
                .setBizExtMap(relationList0BizExtMap);
        BatchAddContactsRequest batchAddContactsRequest = new BatchAddContactsRequest()
                .setOperatorUserId("manager021a")
                .setRelationList(java.util.Arrays.asList(
                    relationList0
                ));
        try {
            client.batchAddContactsWithOptions(batchAddContactsRequest, batchAddContactsHeaders, new RuntimeOptions());
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
        batch_add_contacts_headers = dingtalkcrm__1__0_models.BatchAddContactsHeaders()
        batch_add_contacts_headers.x_acs_dingtalk_access_token = '<your access token>'
        relation_list_0biz_ext_map = {
            'key': '{}'
        }
        relation_list_0biz_data_list_0 = dingtalkcrm__1__0_models.BatchAddContactsRequestRelationListBizDataList(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{}'
        )
        relation_list_0 = dingtalkcrm__1__0_models.BatchAddContactsRequestRelationList(
            biz_data_list=[
                relation_list_0biz_data_list_0
            ],
            biz_ext_map=relation_list_0biz_ext_map
        )
        batch_add_contacts_request = dingtalkcrm__1__0_models.BatchAddContactsRequest(
            operator_user_id='manager021a',
            relation_list=[
                relation_list_0
            ]
        )
        try:
            client.batch_add_contacts_with_options(batch_add_contacts_request, batch_add_contacts_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_add_contacts_headers = dingtalkcrm__1__0_models.BatchAddContactsHeaders()
        batch_add_contacts_headers.x_acs_dingtalk_access_token = '<your access token>'
        relation_list_0biz_ext_map = {
            'key': '{}'
        }
        relation_list_0biz_data_list_0 = dingtalkcrm__1__0_models.BatchAddContactsRequestRelationListBizDataList(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{}'
        )
        relation_list_0 = dingtalkcrm__1__0_models.BatchAddContactsRequestRelationList(
            biz_data_list=[
                relation_list_0biz_data_list_0
            ],
            biz_ext_map=relation_list_0biz_ext_map
        )
        batch_add_contacts_request = dingtalkcrm__1__0_models.BatchAddContactsRequest(
            operator_user_id='manager021a',
            relation_list=[
                relation_list_0
            ]
        )
        try:
            await client.batch_add_contacts_with_options_async(batch_add_contacts_request, batch_add_contacts_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddContactsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddContactsRequest\relationList\bizDataList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddContactsRequest\relationList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddContactsRequest;
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
        $batchAddContactsHeaders = new BatchAddContactsHeaders([]);
        $batchAddContactsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $relationList0BizExtMap = [
            "key" => "{}"
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
            "bizExtMap" => $relationList0BizExtMap
        ]);
        $batchAddContactsRequest = new BatchAddContactsRequest([
            "operatorUserId" => "manager021a",
            "relationList" => [
                $relationList0
            ]
        ]);
        try {
            $client->batchAddContactsWithOptions($batchAddContactsRequest, $batchAddContactsHeaders, new RuntimeOptions([]));
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

  batchAddContactsHeaders := &dingtalkcrm_1_0.BatchAddContactsHeaders{}
  batchAddContactsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  relationList0BizExtMap := map[string]*string{
    "key": tea.String("{}"),
  }
  relationList0BizDataList0 := &dingtalkcrm_1_0.BatchAddContactsRequestRelationListBizDataList{
    Key: tea.String("TextField_71U51A"),
    Value: tea.String("XX有限公司"),
    ExtendValue: tea.String("{}"),
  }
  relationList0 := &dingtalkcrm_1_0.BatchAddContactsRequestRelationList{
    BizDataList: []*dingtalkcrm_1_0.BatchAddContactsRequestRelationListBizDataList{relationList0BizDataList0},
    BizExtMap: relationList0BizExtMap,
  }
  batchAddContactsRequest := &dingtalkcrm_1_0.BatchAddContactsRequest{
    OperatorUserId: tea.String("manager021a"),
    RelationList: []*dingtalkcrm_1_0.BatchAddContactsRequestRelationList{relationList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchAddContactsWithOptions(batchAddContactsRequest, batchAddContactsHeaders, &util.RuntimeOptions{})
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
    let batchAddContactsHeaders = new $dingtalkcrm_1_0.BatchAddContactsHeaders({ });
    batchAddContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let relationList0BizExtMap = {
      key: "{}",
    };
    let relationList0BizDataList0 = new $dingtalkcrm_1_0.BatchAddContactsRequestRelationListBizDataList({
      key: "TextField_71U51A",
      value: "XX有限公司",
      extendValue: "{}",
    });
    let relationList0 = new $dingtalkcrm_1_0.BatchAddContactsRequestRelationList({
      bizDataList: [
        relationList0BizDataList0
      ],
      bizExtMap: relationList0BizExtMap,
    });
    let batchAddContactsRequest = new $dingtalkcrm_1_0.BatchAddContactsRequest({
      operatorUserId: "manager021a",
      relationList: [
        relationList0
      ],
    });
    try {
      await client.batchAddContactsWithOptions(batchAddContactsRequest, batchAddContactsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsHeaders batchAddContactsHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsHeaders();
            batchAddContactsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> relationList0BizExtMap = new Dictionary<string, string>
            {
                {"key", "{}"},
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest.BatchAddContactsRequestRelationList.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest.BatchAddContactsRequestRelationList.BatchAddContactsRequestRelationListBizDataList
            {
                Key = "TextField_71U51A",
                Value = "XX有限公司",
                ExtendValue = "{}",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest.BatchAddContactsRequestRelationList relationList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest.BatchAddContactsRequestRelationList
            {
                BizDataList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest.BatchAddContactsRequestRelationList.BatchAddContactsRequestRelationListBizDataList>
                {
                    relationList0BizDataList0
                },
                BizExtMap = relationList0BizExtMap,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest batchAddContactsRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest
            {
                OperatorUserId = "manager021a",
                RelationList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddContactsRequest.BatchAddContactsRequestRelationList>
                {
                    relationList0
                },
            };
            try
            {
                client.BatchAddContactsWithOptions(batchAddContactsRequest, batchAddContactsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| results | Array | 批量新增结果列表，results返回结果和新增数据顺序是一致的，可以查看每条联系人数据分别对应的结果是否成功。    例如，调用本接口批量新增了两个联系人，第一个联系人写入失败；第二个联系人写入正常。返回的信息格式如图所示。 |
| success | Boolean | 数据是否保存成功。   - **true**：成功 - **false**：失败 |
| errorCode | String | 错误码。   - 如果保存成功，该字段不返回。 - 如果保存失败，表示失败的错误码。 |
| errorMsg | String | 错误信息。   - 如果保存成功，该字段不返回。 - 如果保存失败，表示失败的错误原因。 |
| relationId | String | 联系人relationId。   - 如果保存成功，表示联系人Id。 - 如果保存失败，该字段不返回。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "results" : [ {
    "success" : true,
    "errorCode" : "1002",
    "errorMsg" : "查重失败",
    "relationId" : "gads1ag-sfgasdfxcvxb"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | fieldId.not.exists | %s | 联系人表结构字段缺失 |
| 400 | invalid.content | %s | 内容存在违禁词 |
| 400 | no.permission | %s | 无权限 |
| 400 | operatorUserId.not.exist | operatorUserId not exist | 操作者不存在 |
| 400 | crmApp.not.installed | crm app is not installed | CRM应用未安装 |
| 400 | system.busy | system busy | 请求过于频繁 |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 500 | unknown.error | unknownError | 未知错误 |
