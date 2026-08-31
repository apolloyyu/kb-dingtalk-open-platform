---
title: "批量更新跟进记录数据"
source_url: "https://open.dingtalk.com/document/development/batch-update-follow-up-record-data"
namespace: "development"
slug: "batch-update-follow-up-record-data"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 跟进记录 > 批量更新跟进记录数据"
doc_id: "DfXBnZOvf0"
updated_at: "2026-06-04 19:12:14"
---

> Source: https://open.dingtalk.com/document/development/batch-update-follow-up-record-data
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 跟进记录 > 批量更新跟进记录数据
> Updated: 2026-06-04 19:12:14

# 批量更新跟进记录数据

调用本接口，批量修改跟进记录数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/followRecords/batch |
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
| operatorUserId | String | 是 | 操作人userId，可调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取userId。 |
| instanceList | Array | 是 | 更新的跟进记录数据列表，最大值40。 |
| dataArray | Array | 是 | 更新的跟进记录模型数据列表，最大值256。 |
| key | String | 是 | 模型字段key，填写[获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md)接口返回的name值。该参数是否必填，取决于获取跟进记录对象的元数据接口中返回的nillable值：   - 若nillable是true：则key和value非必填。 - 若nillable是false：则key和value必填。 |
| value | String | 是 | 模型字段value，不同类型的组件value值格式不同，请参考[自定义控件字段格式说明V2](1388-custom-control-field-format-description-v2.md)。 |
| extendValue | String | 否 | 特殊模型字段，请参考[自定义控件字段格式说明V2](1388-custom-control-field-format-description-v2.md)。 |
| instanceId | String | 是 | 跟进记录ID，调用[根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md)接口获取。 |

### 请求示例

HTTP

```
PUT /v1.0/crm/followRecords/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "operatorUserId" : "manager021",
  "instanceList" : [ {
    "dataArray" : [ {
      "key" : "TextField_71U51A",
      "value" : "XX有限公司",
      "extendValue" : "{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }"
    } ],
    "instanceId" : "yU9TbExxxxx"
  } ]
}
```

Java

```
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsHeaders batchUpdateFollowRecordsHeaders = new com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsHeaders();
        batchUpdateFollowRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceListDataArray instanceList0DataArray0 = new com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceListDataArray()
                .setKey("TextField_71U51A")
                .setValue("XX有限公司")
                .setExtendValue("{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }");
        com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList instanceList0 = new com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList()
                .setDataArray(java.util.Arrays.asList(
                    instanceList0DataArray0
                ))
                .setInstanceId("yU9TbExxxxx");
        com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsRequest batchUpdateFollowRecordsRequest = new com.aliyun.dingtalkcrm_1_0.models.BatchUpdateFollowRecordsRequest()
                .setOperatorUserId("manager021")
                .setInstanceList(java.util.Arrays.asList(
                    instanceList0
                ));
        try {
            client.batchUpdateFollowRecordsWithOptions(batchUpdateFollowRecordsRequest, batchUpdateFollowRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys
import json

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
        batch_update_follow_records_headers = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsHeaders()
        batch_update_follow_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        instance_list_0data_array_0 = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsRequestInstanceListDataArray(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{     "key":"PhoneField-xxxxxx",     "value":"185xxxxxxxx" }'
        )
        instance_list_0 = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsRequestInstanceList(
            data_array=[
                instance_list_0data_array_0
            ],
            instance_id='yU9TbExxxxx'
        )
        batch_update_follow_records_request = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsRequest(
            operator_user_id='manager021',
            instance_list=[
                instance_list_0
            ]
        )
        try:
            client.batch_update_follow_records_with_options(batch_update_follow_records_request, batch_update_follow_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_update_follow_records_headers = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsHeaders()
        batch_update_follow_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        instance_list_0data_array_0 = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsRequestInstanceListDataArray(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{     "key":"PhoneField-xxxxxx",     "value":"185xxxxxxxx" }'
        )
        instance_list_0 = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsRequestInstanceList(
            data_array=[
                instance_list_0data_array_0
            ],
            instance_id='yU9TbExxxxx'
        )
        batch_update_follow_records_request = dingtalkcrm__1__0_models.BatchUpdateFollowRecordsRequest(
            operator_user_id='manager021',
            instance_list=[
                instance_list_0
            ]
        )
        try:
            await client.batch_update_follow_records_with_options_async(batch_update_follow_records_request, batch_update_follow_records_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateFollowRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateFollowRecordsRequest\instanceList\dataArray;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateFollowRecordsRequest\instanceList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchUpdateFollowRecordsRequest;
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
        $batchUpdateFollowRecordsHeaders = new BatchUpdateFollowRecordsHeaders([]);
        $batchUpdateFollowRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $instanceList0DataArray0 = new dataArray([
            "key" => "TextField_71U51A",
            "value" => "XX有限公司",
            "extendValue" => "{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }"
        ]);
        $instanceList0 = new instanceList([
            "dataArray" => [
                $instanceList0DataArray0
            ],
            "instanceId" => "yU9TbExxxxx"
        ]);
        $batchUpdateFollowRecordsRequest = new BatchUpdateFollowRecordsRequest([
            "operatorUserId" => "manager021",
            "instanceList" => [
                $instanceList0
            ]
        ]);
        try {
            $client->batchUpdateFollowRecordsWithOptions($batchUpdateFollowRecordsRequest, $batchUpdateFollowRecordsHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
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

  batchUpdateFollowRecordsHeaders := &dingtalkcrm_1_0.BatchUpdateFollowRecordsHeaders{}
  batchUpdateFollowRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  instanceList0DataArray0 := &dingtalkcrm_1_0.BatchUpdateFollowRecordsRequestInstanceListDataArray{
    Key: tea.String("TextField_71U51A"),
    Value: tea.String("XX有限公司"),
    ExtendValue: tea.String("{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }"),
  }
  instanceList0 := &dingtalkcrm_1_0.BatchUpdateFollowRecordsRequestInstanceList{
    DataArray: []*dingtalkcrm_1_0.BatchUpdateFollowRecordsRequestInstanceListDataArray{instanceList0DataArray0},
    InstanceId: tea.String("yU9TbExxxxx"),
  }
  batchUpdateFollowRecordsRequest := &dingtalkcrm_1_0.BatchUpdateFollowRecordsRequest{
    OperatorUserId: tea.String("manager021"),
    InstanceList: []*dingtalkcrm_1_0.BatchUpdateFollowRecordsRequestInstanceList{instanceList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchUpdateFollowRecordsWithOptions(batchUpdateFollowRecordsRequest, batchUpdateFollowRecordsHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkcrm_1_0 = require('@alicloud/dingtalk/crm_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkcrm_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let batchUpdateFollowRecordsHeaders = new dingtalkcrm_1_0.BatchUpdateFollowRecordsHeaders({ });
    batchUpdateFollowRecordsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let instanceList0DataArray0 = new dingtalkcrm_1_0.BatchUpdateFollowRecordsRequestInstanceListDataArray({
      key: 'TextField_71U51A',
      value: 'XX有限公司',
      extendValue: '{     "key":"PhoneField-xxxxxx",     "value":"185xxxxxxxx" }',
    });
    let instanceList0 = new dingtalkcrm_1_0.BatchUpdateFollowRecordsRequestInstanceList({
      dataArray: [
        instanceList0DataArray0
      ],
      instanceId: 'yU9TbExxxxx',
    });
    let batchUpdateFollowRecordsRequest = new dingtalkcrm_1_0.BatchUpdateFollowRecordsRequest({
      operatorUserId: 'manager021',
      instanceList: [
        instanceList0
      ],
    });
    try {
      await client.batchUpdateFollowRecordsWithOptions(batchUpdateFollowRecordsRequest, batchUpdateFollowRecordsHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
Client.main(process.argv.slice(2));
```

C#

```
using Newtonsoft.Json;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsHeaders batchUpdateFollowRecordsHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsHeaders();
            batchUpdateFollowRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList.BatchUpdateFollowRecordsRequestInstanceListDataArray instanceList0DataArray0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList.BatchUpdateFollowRecordsRequestInstanceListDataArray
            {
                Key = "TextField_71U51A",
                Value = "XX有限公司",
                ExtendValue = "{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList instanceList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList
            {
                DataArray = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList.BatchUpdateFollowRecordsRequestInstanceListDataArray>
                {
                    instanceList0DataArray0
                },
                InstanceId = "yU9TbExxxxx",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest batchUpdateFollowRecordsRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest
            {
                OperatorUserId = "manager021",
                InstanceList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchUpdateFollowRecordsRequest.BatchUpdateFollowRecordsRequestInstanceList>
                {
                    instanceList0
                },
            };
            try
            {
                client.BatchUpdateFollowRecordsWithOptions(batchUpdateFollowRecordsRequest, batchUpdateFollowRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| results | Array | 批量更新结果列表，results返回结果和新增数据顺序是一致的，可以查看每条数据分别对应的结果是否成功。      例如，调用本接口批量更新了两个跟进记录，第一个跟进记录更新失败；第二个更新正常。返回的信息格式为 |
| success | Boolean | 数据更新是否成功，true表示成功。 |
| errorCode | String | 错误码。   - 如果更新失败，表示失败的错误码。 - 如果更新成功，该字段不返回。 |
| errorMsg | String | 错误信息。   - 如果更新失败，表示失败的错误原因。 - 如果更新成功，该字段不返回。 |
| instanceId | String | 更新成功的跟进记录Id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "results" : [ {
    "success" : true,
    "instanceId" : "yU9TbER1TDazjPq1rRCzwg04841675924041"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.content | %s | 内容存在违禁词 |
| 400 | no.permission | %s | 无权限 |
| 400 | operatorUserId.not.exist | operatorUserId not exist | 操作者不存在 |
| 400 | crmApp.not.installed | crm app is not installed | CRM应用未安装 |
| 400 | system.busy | system busy | 请求过于频繁 |
| 400 | no.field.permission | %s | 没有指定字段的编辑权限 |
| 400 | duplicated.field | duplicated field | 存在重复模型字段key |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 500 | unknown.error | unknownError | 未知错误 |
