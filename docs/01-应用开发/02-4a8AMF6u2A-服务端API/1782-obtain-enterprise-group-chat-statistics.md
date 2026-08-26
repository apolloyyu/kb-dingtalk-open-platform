---
title: "获取企业群聊统计数据"
source_url: "https://open.dingtalk.com/document/development/obtain-enterprise-group-chat-statistics"
namespace: "development"
slug: "obtain-enterprise-group-chat-statistics"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 获取企业群聊统计数据"
doc_id: "I3pfHnxmRm"
updated_at: "2025-09-08 19:05:53"
---

> Source: https://open.dingtalk.com/document/development/obtain-enterprise-group-chat-statistics
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 获取企业群聊统计数据
> Updated: 2025-09-08 19:05:53

# 获取企业群聊统计数据

调用本接口获取企业即时沟通中群聊的统计数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

| 统计日期 | 组织ID | 群聊用户数 | 群聊消息数 | 活跃群数 | 新增群数 | 内部群数量 | 部门群数量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20210101 | 12345 | 289 | 1175 | 198 | 15 | 218 | 341 |

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 数据服务目录即时沟通统计读权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 暂不支持 | 数据服务目录即时沟通统计读权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 数据服务目录即时沟通统计读权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/datacenter/groupMessageData?statDate=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证：   - 企业内部应用调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| statDate | String | 是 | 查询时间，日期格式为yyyyMMdd。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| dataList | Array of Object | 指标数据列表。  **[!NOTE]**  指标数据为Map类型，指标值的取值key为**指标ID\_指标周期**，例如：4001\_DAY。 |
| metaList | Array | 指标元数据列表，包括指标ID、指标名称、指标周期、指标口径等信息。 |
| kpiId | String | 字段ID。 |
| kpiName | String | 字段名称。 |
| unit | String | 字段单位。 |
| kpiCaliber | String | 字段描述。 |
| period | String | 字段统计周期。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/datacenter/groupMessageData?statDate=20210620 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:85dd6a3xxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkdatacenter_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdatacenter_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdatacenter_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdatacenter_1_0.models.QueryGroupMessageStatisticalDataHeaders queryGroupMessageStatisticalDataHeaders = new com.aliyun.dingtalkdatacenter_1_0.models.QueryGroupMessageStatisticalDataHeaders();
        queryGroupMessageStatisticalDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdatacenter_1_0.models.QueryGroupMessageStatisticalDataRequest queryGroupMessageStatisticalDataRequest = new com.aliyun.dingtalkdatacenter_1_0.models.QueryGroupMessageStatisticalDataRequest()
                .setStatDate("20210620");
        try {
            client.queryGroupMessageStatisticalDataWithOptions(queryGroupMessageStatisticalDataRequest, queryGroupMessageStatisticalDataHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_group_message_statistical_data_headers = dingtalkdatacenter__1__0_models.QueryGroupMessageStatisticalDataHeaders()
        query_group_message_statistical_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_group_message_statistical_data_request = dingtalkdatacenter__1__0_models.QueryGroupMessageStatisticalDataRequest(
            stat_date='20210620'
        )
        try:
            client.query_group_message_statistical_data_with_options(query_group_message_statistical_data_request, query_group_message_statistical_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_group_message_statistical_data_headers = dingtalkdatacenter__1__0_models.QueryGroupMessageStatisticalDataHeaders()
        query_group_message_statistical_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_group_message_statistical_data_request = dingtalkdatacenter__1__0_models.QueryGroupMessageStatisticalDataRequest(
            stat_date='20210620'
        )
        try:
            await client.query_group_message_statistical_data_with_options_async(query_group_message_statistical_data_request, query_group_message_statistical_data_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\QueryGroupMessageStatisticalDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdatacenter_1_0\Models\QueryGroupMessageStatisticalDataRequest;
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
        $queryGroupMessageStatisticalDataHeaders = new QueryGroupMessageStatisticalDataHeaders([]);
        $queryGroupMessageStatisticalDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryGroupMessageStatisticalDataRequest = new QueryGroupMessageStatisticalDataRequest([
            "statDate" => "20210620"
        ]);
        try {
            $client->queryGroupMessageStatisticalDataWithOptions($queryGroupMessageStatisticalDataRequest, $queryGroupMessageStatisticalDataHeaders, new RuntimeOptions([]));
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
  dingtalkdatacenter_1_0  "github.com/alibabacloud-go/dingtalk/datacenter_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  queryGroupMessageStatisticalDataHeaders := &dingtalkdatacenter_1_0.QueryGroupMessageStatisticalDataHeaders{}
  queryGroupMessageStatisticalDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryGroupMessageStatisticalDataRequest := &dingtalkdatacenter_1_0.QueryGroupMessageStatisticalDataRequest{
    StatDate: tea.String("20210620"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryGroupMessageStatisticalDataWithOptions(queryGroupMessageStatisticalDataRequest, queryGroupMessageStatisticalDataHeaders, &util.RuntimeOptions{})
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
import dingtalkdatacenter_1_0, * as $dingtalkdatacenter_1_0 from '@alicloud/dingtalk/datacenter_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdatacenter_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdatacenter_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryGroupMessageStatisticalDataHeaders = new $dingtalkdatacenter_1_0.QueryGroupMessageStatisticalDataHeaders({ });
    queryGroupMessageStatisticalDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryGroupMessageStatisticalDataRequest = new $dingtalkdatacenter_1_0.QueryGroupMessageStatisticalDataRequest({
      statDate: "20210620",
    });
    try {
      await client.queryGroupMessageStatisticalDataWithOptions(queryGroupMessageStatisticalDataRequest, queryGroupMessageStatisticalDataHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGroupMessageStatisticalDataHeaders queryGroupMessageStatisticalDataHeaders = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGroupMessageStatisticalDataHeaders();
            queryGroupMessageStatisticalDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGroupMessageStatisticalDataRequest queryGroupMessageStatisticalDataRequest = new AlibabaCloud.SDK.Dingtalkdatacenter_1_0.Models.QueryGroupMessageStatisticalDataRequest
            {
                StatDate = "20210620",
            };
            try
            {
                client.QueryGroupMessageStatisticalDataWithOptions(queryGroupMessageStatisticalDataRequest, queryGroupMessageStatisticalDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "metaList" : [ {
    "unit" : "人",
    "period" : "DAY",
    "kpiId" : "4030",
    "kpiCaliber" : "企业内发送群聊消息用户数",
    "kpiName" : "群聊用户数"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "4031",
    "kpiCaliber" : "企业内部群新增数量",
    "kpiName" : "新增群数"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "4032",
    "kpiCaliber" : "有群聊消息发生的企业内部群数量",
    "kpiName" : "活跃群数"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "4033",
    "kpiCaliber" : "企业内部群消息数",
    "kpiName" : "群聊消息数"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "4034",
    "kpiCaliber" : "当前存在的企业内部群数量",
    "kpiName" : "内部群数量"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "4035",
    "kpiCaliber" : "当前存在的部门群数量",
    "kpiName" : "部门群数量"
  } ],
  "dataList" : [ {
    "4034_DAY" : 19,
    "4033_DAY" : 403,
    "4032_DAY" : 0,
    "4030_DAY" : 61,
    "stat_date" : "20210620",
    "4031_DAY" : 0,
    "4035_DAY" : 15,
    "corp_id" : "ding32fxxx"
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | IdempotentParameterMismatch | The request uses the same client token as a previous, but non-identical request. Do not reuse a client token with different requests, unless the requests are identical. | client token不合法。 |
| 500 | statDate.is.null | statDate请求参数为空 | statDate请求参数为空 |
| 500 | service.meta.isNull | service meta信息为空 | service meta信息为空 |
| 500 | serviceId.is.null | serviceId为空 | serviceId为空 |
| 500 | systemError | 系统异常 | 系统异常，请稍后重试 |
| 500 | orgId.is.null | orgId请求参数为空 | orgId请求参数为空 |
| 500 | statDate.format.iserror | statDate请求参数格式不正确，正确格式：yyyyMMdd | statDate请求参数格式不正确，正确格式：yyyyMMdd |
| 500 | unknownError | 未知错误 | 未知错误 |
