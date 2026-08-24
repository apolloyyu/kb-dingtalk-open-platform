---
title: "批量新增跟进记录数据"
source_url: "https://open.dingtalk.com/document/development/batch-add-follow-up-record-data"
namespace: "development"
slug: "batch-add-follow-up-record-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 跟进记录 > 批量新增跟进记录数据"
doc_id: "x4fqZZNXso"
updated_at: "2026-06-04 19:12:13"
---

> Source: https://open.dingtalk.com/document/development/batch-add-follow-up-record-data
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 跟进记录 > 批量新增跟进记录数据
> Updated: 2026-06-04 19:12:13

# 批量新增跟进记录数据

调用本接口，批量新增跟进记录数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/followRecords/batch |
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
| operatorUserId | String | 是 | 操作人userId，可调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取userId。 |
| instanceList | Array | 是 | 跟进记录数据字段列表，最大值40。 |
| dataArray | Array | 是 | 新增跟进记录的模型数据列表，最大值256。 |
| key | String | 是 | 模型字段key，该参数传跟进记录对象元数据信息中获取字段的name值，调用[获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md)接口获取name参数值。  该参数是否必填，取决于调用获取跟进记录对象的元数据信息接口，返回的nillable字段值：   - 若nillable是**true**：本接口参数key和value为非必填。 - 若nillable是**false**：本接口参数key和value为必填。 |
| value | String | 是 | 模型字段value，不同类型的组件value值格式不同，请参考[自定义控件字段格式说明V2](1388-custom-control-field-format-description-v2.md)。 |
| extendValue | String | 否 | 特殊模型字段，请参考[自定义控件字段格式说明V2](1388-custom-control-field-format-description-v2.md)。 |

### 请求示例

HTTP

```
POST /v1.0/crm/followRecords/batch HTTP/1.1
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
    } ]
  } ]
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
        com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsHeaders batchAddFollowRecordsHeaders = new com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsHeaders();
        batchAddFollowRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceListDataArray instanceList0DataArray0 = new com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceListDataArray()
                .setKey("TextField_71U51A")
                .setValue("XX有限公司")
                .setExtendValue("{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }");
        com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList instanceList0 = new com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList()
                .setDataArray(java.util.Arrays.asList(
                    instanceList0DataArray0
                ));
        com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsRequest batchAddFollowRecordsRequest = new com.aliyun.dingtalkcrm_1_0.models.BatchAddFollowRecordsRequest()
                .setOperatorUserId("manager021")
                .setInstanceList(java.util.Arrays.asList(
                    instanceList0
                ));
        try {
            client.batchAddFollowRecordsWithOptions(batchAddFollowRecordsRequest, batchAddFollowRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        batch_add_follow_records_headers = dingtalkcrm__1__0_models.BatchAddFollowRecordsHeaders()
        batch_add_follow_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        instance_list_0data_array_0 = dingtalkcrm__1__0_models.BatchAddFollowRecordsRequestInstanceListDataArray(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{     "key":"PhoneField-xxxxxx",     "value":"185xxxxxxxx" }'
        )
        instance_list_0 = dingtalkcrm__1__0_models.BatchAddFollowRecordsRequestInstanceList(
            data_array=[
                instance_list_0data_array_0
            ]
        )
        batch_add_follow_records_request = dingtalkcrm__1__0_models.BatchAddFollowRecordsRequest(
            operator_user_id='manager021',
            instance_list=[
                instance_list_0
            ]
        )
        try:
            client.batch_add_follow_records_with_options(batch_add_follow_records_request, batch_add_follow_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_add_follow_records_headers = dingtalkcrm__1__0_models.BatchAddFollowRecordsHeaders()
        batch_add_follow_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        instance_list_0data_array_0 = dingtalkcrm__1__0_models.BatchAddFollowRecordsRequestInstanceListDataArray(
            key='TextField_71U51A',
            value='XX有限公司',
            extend_value='{     "key":"PhoneField-xxxxxx",     "value":"185xxxxxxxx" }'
        )
        instance_list_0 = dingtalkcrm__1__0_models.BatchAddFollowRecordsRequestInstanceList(
            data_array=[
                instance_list_0data_array_0
            ]
        )
        batch_add_follow_records_request = dingtalkcrm__1__0_models.BatchAddFollowRecordsRequest(
            operator_user_id='manager021',
            instance_list=[
                instance_list_0
            ]
        )
        try:
            await client.batch_add_follow_records_with_options_async(batch_add_follow_records_request, batch_add_follow_records_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddFollowRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddFollowRecordsRequest\instanceList\dataArray;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddFollowRecordsRequest\instanceList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchAddFollowRecordsRequest;
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
        $batchAddFollowRecordsHeaders = new BatchAddFollowRecordsHeaders([]);
        $batchAddFollowRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $instanceList0DataArray0 = new dataArray([
            "key" => "TextField_71U51A",
            "value" => "XX有限公司",
            "extendValue" => "{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }"
        ]);
        $instanceList0 = new instanceList([
            "dataArray" => [
                $instanceList0DataArray0
            ]
        ]);
        $batchAddFollowRecordsRequest = new BatchAddFollowRecordsRequest([
            "operatorUserId" => "manager021",
            "instanceList" => [
                $instanceList0
            ]
        ]);
        try {
            $client->batchAddFollowRecordsWithOptions($batchAddFollowRecordsRequest, $batchAddFollowRecordsHeaders, new RuntimeOptions([]));
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

  batchAddFollowRecordsHeaders := &dingtalkcrm_1_0.BatchAddFollowRecordsHeaders{}
  batchAddFollowRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  instanceList0DataArray0 := &dingtalkcrm_1_0.BatchAddFollowRecordsRequestInstanceListDataArray{
    Key: tea.String("TextField_71U51A"),
    Value: tea.String("XX有限公司"),
    ExtendValue: tea.String("{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }"),
  }
  instanceList0 := &dingtalkcrm_1_0.BatchAddFollowRecordsRequestInstanceList{
    DataArray: []*dingtalkcrm_1_0.BatchAddFollowRecordsRequestInstanceListDataArray{instanceList0DataArray0},
  }
  batchAddFollowRecordsRequest := &dingtalkcrm_1_0.BatchAddFollowRecordsRequest{
    OperatorUserId: tea.String("manager021"),
    InstanceList: []*dingtalkcrm_1_0.BatchAddFollowRecordsRequestInstanceList{instanceList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchAddFollowRecordsWithOptions(batchAddFollowRecordsRequest, batchAddFollowRecordsHeaders, &util.RuntimeOptions{})
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
    let batchAddFollowRecordsHeaders = new $dingtalkcrm_1_0.BatchAddFollowRecordsHeaders({ });
    batchAddFollowRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let instanceList0DataArray0 = new $dingtalkcrm_1_0.BatchAddFollowRecordsRequestInstanceListDataArray({
      key: "TextField_71U51A",
      value: "XX有限公司",
      extendValue: "{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }",
    });
    let instanceList0 = new $dingtalkcrm_1_0.BatchAddFollowRecordsRequestInstanceList({
      dataArray: [
        instanceList0DataArray0
      ],
    });
    let batchAddFollowRecordsRequest = new $dingtalkcrm_1_0.BatchAddFollowRecordsRequest({
      operatorUserId: "manager021",
      instanceList: [
        instanceList0
      ],
    });
    try {
      await client.batchAddFollowRecordsWithOptions(batchAddFollowRecordsRequest, batchAddFollowRecordsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsHeaders batchAddFollowRecordsHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsHeaders();
            batchAddFollowRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList.BatchAddFollowRecordsRequestInstanceListDataArray instanceList0DataArray0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList.BatchAddFollowRecordsRequestInstanceListDataArray
            {
                Key = "TextField_71U51A",
                Value = "XX有限公司",
                ExtendValue = "{     \"key\":\"PhoneField-xxxxxx\",     \"value\":\"185xxxxxxxx\" }",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList instanceList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList
            {
                DataArray = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList.BatchAddFollowRecordsRequestInstanceListDataArray>
                {
                    instanceList0DataArray0
                },
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest batchAddFollowRecordsRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest
            {
                OperatorUserId = "manager021",
                InstanceList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchAddFollowRecordsRequest.BatchAddFollowRecordsRequestInstanceList>
                {
                    instanceList0
                },
            };
            try
            {
                client.BatchAddFollowRecordsWithOptions(batchAddFollowRecordsRequest, batchAddFollowRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| results | Array | 批量新增结果列表，results返回结果和新增数据顺序是一致的，可以查看每条数据分别对应的结果是否成功。    例如，调用本接口批量新增了两个跟进记录，第一个跟进记录写入失败；第二个跟进记录写入正常。返回的信息格式为 |
| success | Boolean | 数据是否保存成功。   - **true**：成功 - **false**：失败 |
| errorCode | String | 错误码。   - 如果保存失败，表示失败的错误码。 - 如果保存成功，该字段不返回。 |
| errorMsg | String | 错误信息。   - 如果保存失败，表示失败的错误原因。 - 如果保存成功，该字段不返回。 |
| instanceId | String | 保存成功的跟进记录instanceId。 |

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
| 400 | duplicated.field | duplicated field | 存在重复模型字段key |
| 400 | related.customer.required | related customer required | 关联客户字段必填 |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 500 | unknown.error | unknownError | 未知错误 |
