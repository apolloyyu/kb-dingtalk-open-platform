---
title: "获取数据资产平台数据服务"
source_url: "https://open.dingtalk.com/document/dataopen/api-querygeneraldataservicebatch"
namespace: "dataopen"
slug: "api-querygeneraldataservicebatch"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "API 参考 > 获取数据资产平台数据服务"
doc_id: "5nDqpfORIh"
updated_at: "2026-06-15 10:33:47"
---

> Source: https://open.dingtalk.com/document/dataopen/api-querygeneraldataservicebatch
> Path: 数据资产 / 平台介绍 / API 参考 > 获取数据资产平台数据服务
> Updated: 2026-06-15 10:33:47

# 获取数据资产平台数据服务

数据资产平台数据服务接口，部门维度接口支持多个部门ID传参（最大10个），员工维度接口支持多个员工ID入参（最大10个）。

## **接口调用说明**

该接口支持部门、员工维度批量拉取。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/datacenter/dataServices/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-DataCenter.GeneralDataSet.Read-数据服务目录资产服务读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceId | String | 是 | 服务编码，在创建数据服务后获取。 |
| startDate | String | 是 | 开始日期，例如：20220901。 |
| endDate | String | 是 | 结束日期，例如：20220901。 |
| userId | String | 否 | 员工userId。 |
| deptIds | Array of String | 否 | 部门ID，非部门维度接口不需要传。 |
| userIds | Array of String | 否 | 员工ID，非员工维度接口不需要传。 |
| pageSize | Long | 是 | 每页大小，不填默认为10，最大为500。 |
| pageNumber | Long | 是 | 分页页码，从1开始，不填默认为1。 |

### 请求示例

HTTP

```
POST /v1.0/datacenter/dataServices/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:4f29c24cf71d3423b57d0e8678c25fff
Content-Type:application/json

{
  "serviceId" : "API-xxx",
  "startDate" : "20240611",
  "endDate" : "20240619",
  "userId" : "344221",
  "deptIds" : [ "11" ],
  "userIds" : [ "222" ],
  "pageSize" : 10,
  "pageNumber" : 1
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkdatacenter_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdatacenter_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdatacenter_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataServiceBatchHeaders queryGeneralDataServiceBatchHeaders = new com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataServiceBatchHeaders();
        queryGeneralDataServiceBatchHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataServiceBatchRequest queryGeneralDataServiceBatchRequest = new com.aliyun.dingtalkdatacenter_1_0.models.QueryGeneralDataServiceBatchRequest()
                .setServiceId("API-xxx")
                .setStartDate("20240611")
                .setEndDate("20240619")
                .setUserId("344221")
                .setDeptIds(java.util.Arrays.asList(
                    "11"
                ))
                .setUserIds(java.util.Arrays.asList(
                    "222"
                ))
                .setPageSize(10L)
                .setPageNumber(1L);
        try {
            client.queryGeneralDataServiceBatchWithOptions(queryGeneralDataServiceBatchRequest, queryGeneralDataServiceBatchHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from typing import List

from alibabacloud_dingtalk.datacenter_1_0.client import Client as dingtalkdatacenter_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.datacenter_1_0 import models as dingtalkdatacenter__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdatacenter_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdatacenter_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_general_data_service_batch_headers = dingtalkdatacenter__1__0_models.QueryGeneralDataServiceBatchHeaders()
        query_general_data_service_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_general_data_service_batch_request = dingtalkdatacenter__1__0_models.QueryGeneralDataServiceBatchRequest(
            service_id='API-xxx',
            start_date='20240611',
            end_date='20240619',
            user_id='344221',
            dept_ids=[
                '11'
            ],
            user_ids=[
                '222'
            ],
            page_size=10,
            page_number=1
        )
        try:
            client.query_general_data_service_batch_with_options(query_general_data_service_batch_request, query_general_data_service_batch_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_general_data_service_batch_headers = dingtalkdatacenter__1__0_models.QueryGeneralDataServiceBatchHeaders()
        query_general_data_service_batch_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_general_data_service_batch_request = dingtalkdatacenter__1__0_models.QueryGeneralDataServiceBatchRequest(
            service_id='API-xxx',
            start_date='20240611',
            end_date='20240619',
            user_id='344221',
            dept_ids=[
                '11'
            ],
            user_ids=[
                '222'
            ],
            page_size=10,
            page_number=1
        )
        try:
            await client.query_general_data_service_batch_with_options_async(query_general_data_service_batch_request, query_general_data_service_batch_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\QueryGeneralDataServiceBatchHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\QueryGeneralDataServiceBatchRequest;
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
        $queryGeneralDataServiceBatchHeaders = new QueryGeneralDataServiceBatchHeaders([]);
        $queryGeneralDataServiceBatchHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryGeneralDataServiceBatchRequest = new QueryGeneralDataServiceBatchRequest([
            "serviceId" => "API-xxx",
            "startDate" => "20240611",
            "endDate" => "20240619",
            "userId" => "344221",
            "deptIds" => [
                "11"
            ],
            "userIds" => [
                "222"
            ],
            "pageSize" => 10,
            "pageNumber" => 1
        ]);
        try {
            $client->queryGeneralDataServiceBatchWithOptions($queryGeneralDataServiceBatchRequest, $queryGeneralDataServiceBatchHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkdatacenter_1_0  "github.com/alibabacloud-go/dingtalk/datacenter_1_0"
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
func CreateClient () (_result *dingtalkdatacenter_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdatacenter_1_0.Client{}
  _result, _err = dingtalkdatacenter_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryGeneralDataServiceBatchHeaders := &dingtalkdatacenter_1_0.QueryGeneralDataServiceBatchHeaders{}
  queryGeneralDataServiceBatchHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryGeneralDataServiceBatchRequest := &dingtalkdatacenter_1_0.QueryGeneralDataServiceBatchRequest{
    ServiceId: tea.String("API-xxx"),
    StartDate: tea.String("20240611"),
    EndDate: tea.String("20240619"),
    UserId: tea.String("344221"),
    DeptIds: []*string{tea.String("11")},
    UserIds: []*string{tea.String("222")},
    PageSize: tea.Int64(10),
    PageNumber: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryGeneralDataServiceBatchWithOptions(queryGeneralDataServiceBatchRequest, queryGeneralDataServiceBatchHeaders, &util.RuntimeOptions{})
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
const dingtalkdatacenter_1_0 = require('@alicloud/dingtalk/datacenter_1_0');
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
    return new dingtalkdatacenter_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryGeneralDataServiceBatchHeaders = new dingtalkdatacenter_1_0.QueryGeneralDataServiceBatchHeaders({ });
    queryGeneralDataServiceBatchHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryGeneralDataServiceBatchRequest = new dingtalkdatacenter_1_0.QueryGeneralDataServiceBatchRequest({
      serviceId: 'API-xxx',
      startDate: '20240611',
      endDate: '20240619',
      userId: '344221',
      deptIds: [
        '11'
      ],
      userIds: [
        '222'
      ],
      pageSize: 10,
      pageNumber: 1,
    });
    try {
      await client.queryGeneralDataServiceBatchWithOptions(queryGeneralDataServiceBatchRequest, queryGeneralDataServiceBatchHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataServiceBatchHeaders queryGeneralDataServiceBatchHeaders = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataServiceBatchHeaders();
            queryGeneralDataServiceBatchHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataServiceBatchRequest queryGeneralDataServiceBatchRequest = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGeneralDataServiceBatchRequest
            {
                ServiceId = "API-xxx",
                StartDate = "20240611",
                EndDate = "20240619",
                UserId = "344221",
                DeptIds = new List<string>
                {
                    "11"
                },
                UserIds = new List<string>
                {
                    "222"
                },
                PageSize = 10,
                PageNumber = 1,
            };
            try
            {
                client.QueryGeneralDataServiceBatchWithOptions(queryGeneralDataServiceBatchRequest, queryGeneralDataServiceBatchHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dataList | Array of Object | 指标数据。 |
| metaList | Array | 指标元数据。 |
| fieldName | String | 指标ID。 |
| fieldDesc | String | 指标名称。 |
| fieldType | String | 指标单位。 |
| fieldId | String | 指标口径。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "dataList" : [ null ],
  "metaList" : [ {
    "fieldName" : "字段名称",
    "fieldDesc" : "字段描述",
    "fieldType" : "字段类型",
    "fieldId" : "字段ID"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](../../01-应用开发/02-4a8AMF6u2A-服务端API/0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | inputParams.startOrEndDate.empty | startDate和endDate不能为空 | startDate和endDate不能为空 |
| 400 | inputParams.date.invalid | startDate或endDate日期格式不正确,正确日期格式:20220801 | startDate或endDate日期格式不正确,正确日期格式:20220801 |
| 400 | inputParams.startGraterEnd.date | 开始日期不能大于结束日期 | 开始日期不能大于结束日期 |
| 400 | inputParams.deptId.empty | 入参：deptId不能为空 | 入参：deptId不能为空 |
| 400 | inputParams.staffId.empty | userId不能为空 | userId不能为空 |
| 400 | inputParamsDate.over.timeScope | 查询时间超过最大时间范围 | 查询时间超过最大时间范围 |
| 500 | apiDataConnect.datasource.overLimit | 暂不支持跨数据源查询 | 暂不支持跨数据源查询 |
| 500 | apiDataConnect.dataset.overLimit | 查询超过跨数据集个数限制 | 查询超过跨数据集个数限制 |
| 500 | apiDataConnect.detailDataset.overLimit | 明细类型数据服务暂不支持跨数据集查询 | 明细类型数据服务暂不支持跨数据集查询 |
| 500 | service.code.invalid | 数据服务编码无效 | 数据服务编码无效 |
| 500 | apiDataConnect.dataFields.overMaxLimit | 数据项字段超过限制 | 数据项字段超过限制 |
| 500 | service.not.found | 数据服务未找到 | 数据服务未找到 |
| 500 | apiDataConnect.dataset.notFound | 数据集未找到 | 数据集未找到 |
| 500 | apiDataConnect.datasource.notFound | 数据源未找到 | 数据源未找到 |
| 500 | approval.not.completed | 该数据服务审批未完成 | 该数据服务审批未完成 |
| 500 | approval.result.refused | 该数据服务审批被拒绝 | 该数据服务审批被拒绝 |
| 500 | service.not.online | 该服务未上架 | 该服务未上架 |
| 500 | return.field.empty | 配置返回字段为空 | 配置返回字段为空 |
| 500 | api.fields.notAllAuth | 服务配置字段未被全部授权 | 服务配置字段未被全部授权 |
| 500 | service.code.invalid | 数据服务编码无效:serviceId不属于本组织 | 数据服务编码无效:serviceId不属于本组织 |
| 500 | unauthorized | %s | 服务未授权,前往授权链接 |
| 500 | invoker.notIn.corp | 调用者不是本组织成员，请检查userId入参是否正确 | 调用者不是本组织成员，请检查userId入参是否正确 |
| 500 | fields.not.mappingConfig | 自定义模型中，有字段未配置映射关系 | 自定义模型中，有字段未配置映射关系 |
| 500 | dataItem.quota.notEnough | 调用数据项次数额度不足 | 调用数据项次数额度不足 |
| 500 | dashboard.quota.notEnough | 自定义仪表盘额度不足 | 自定义仪表盘额度不足 |
