---
title: "查询市内用车申请单"
source_url: "https://open.dingtalk.com/document/development/query-the-application-form-for-third-party-vehicles-in-the-city"
namespace: "development"
slug: "query-the-application-form-for-third-party-vehicles-in-the-city"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 市内用车申请 > 查询市内用车申请单"
doc_id: "PLQcEvXTMi"
updated_at: "2026-01-29 14:31:11"
---

> Source: https://open.dingtalk.com/document/development/query-the-application-form-for-third-party-vehicles-in-the-city
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 市内用车申请 > 查询市内用车申请单
> Updated: 2026-01-29 14:31:11

# 查询市内用车申请单

通过此接口查询企业员工提交的市内用车审批申请单，支持按创建时间、员工ID、第三方审批单ID等条件进行筛选。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/cityCarApprovals |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限点 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业的CorpId。 |
| createdEndAt | String | 否 | 审批单创建时间小于值，例如2021-03-18 20:26:50。 |
| createdStartAt | String | 否 | 审批单创建时间大于或等于的时间，例如2021-03-18 20:26:56。 |
| pageNumber | Long | 否 | 页码，要求大于等于1，默认1。 |
| pageSize | Long | 否 | 每页数据量，要求大于等于1，默认20。 |
| thirdPartApplyId | String | 否 | 三方审批单ID。 |
| userId | String | 否 | 第三方员工ID。 |

### 请求示例

HTTP

```
GET /v1.0/alitrip/cityCarApprovals?corpId=corpx&createdEndAt=2021-03-18 20:26:59&createdStartAt=2021-03-18 20:20:56&pageNumber=1&pageSize=20&thirdPartApplyId=apply1&userId=user1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkalitrip_1_0.*;
import com.aliyun.dingtalkalitrip_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkalitrip_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkalitrip_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkalitrip_1_0.Client client = Sample.createClient();
        QueryCityCarApplyHeaders queryCityCarApplyHeaders = new QueryCityCarApplyHeaders();
        queryCityCarApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryCityCarApplyRequest queryCityCarApplyRequest = new QueryCityCarApplyRequest()
                .setCorpId("corpx")
                .setCreatedEndAt("2021-03-18 20:26:59")
                .setCreatedStartAt("2021-03-18 20:20:56")
                .setPageNumber(1L)
                .setPageSize(20L)
                .setThirdPartApplyId("apply1")
                .setUserId("user1");
        try {
            client.queryCityCarApplyWithOptions(queryCityCarApplyRequest, queryCityCarApplyHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.alitrip_1_0.client import Client as dingtalkalitrip_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.alitrip_1_0 import models as dingtalkalitrip__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkalitrip_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkalitrip_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_city_car_apply_headers = dingtalkalitrip__1__0_models.QueryCityCarApplyHeaders()
        query_city_car_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_city_car_apply_request = dingtalkalitrip__1__0_models.QueryCityCarApplyRequest(
            corp_id='corpx',
            created_end_at='2021-03-18 20:26:59',
            created_start_at='2021-03-18 20:20:56',
            page_number=1,
            page_size=20,
            third_part_apply_id='apply1',
            user_id='user1'
        )
        try:
            client.query_city_car_apply_with_options(query_city_car_apply_request, query_city_car_apply_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_city_car_apply_headers = dingtalkalitrip__1__0_models.QueryCityCarApplyHeaders()
        query_city_car_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_city_car_apply_request = dingtalkalitrip__1__0_models.QueryCityCarApplyRequest(
            corp_id='corpx',
            created_end_at='2021-03-18 20:26:59',
            created_start_at='2021-03-18 20:20:56',
            page_number=1,
            page_size=20,
            third_part_apply_id='apply1',
            user_id='user1'
        )
        try:
            await client.query_city_car_apply_with_options_async(query_city_car_apply_request, query_city_car_apply_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\QueryCityCarApplyHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\QueryCityCarApplyRequest;
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
        $queryCityCarApplyHeaders = new QueryCityCarApplyHeaders([]);
        $queryCityCarApplyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryCityCarApplyRequest = new QueryCityCarApplyRequest([
            "corpId" => "corpx",
            "createdEndAt" => "2021-03-18 20:26:59",
            "createdStartAt" => "2021-03-18 20:20:56",
            "pageNumber" => 1,
            "pageSize" => 20,
            "thirdPartApplyId" => "apply1",
            "userId" => "user1"
        ]);
        try {
            $client->queryCityCarApplyWithOptions($queryCityCarApplyRequest, $queryCityCarApplyHeaders, new RuntimeOptions([]));
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
  dingtalkalitrip_1_0  "github.com/alibabacloud-go/dingtalk/alitrip_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkalitrip_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkalitrip_1_0.Client{}
  _result, _err = dingtalkalitrip_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryCityCarApplyHeaders := &dingtalkalitrip_1_0.QueryCityCarApplyHeaders{}
  queryCityCarApplyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryCityCarApplyRequest := &dingtalkalitrip_1_0.QueryCityCarApplyRequest{
    CorpId: tea.String("corpx"),
    CreatedEndAt: tea.String("2021-03-18 20:26:59"),
    CreatedStartAt: tea.String("2021-03-18 20:20:56"),
    PageNumber: tea.Int64(1),
    PageSize: tea.Int64(20),
    ThirdPartApplyId: tea.String("apply1"),
    UserId: tea.String("user1"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryCityCarApplyWithOptions(queryCityCarApplyRequest, queryCityCarApplyHeaders, &util.RuntimeOptions{})
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
import dingtalkalitrip_1_0, * as $dingtalkalitrip_1_0 from '@alicloud/dingtalk/alitrip_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkalitrip_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkalitrip_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryCityCarApplyHeaders = new $dingtalkalitrip_1_0.QueryCityCarApplyHeaders({ });
    queryCityCarApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryCityCarApplyRequest = new $dingtalkalitrip_1_0.QueryCityCarApplyRequest({
      corpId: "corpx",
      createdEndAt: "2021-03-18 20:26:59",
      createdStartAt: "2021-03-18 20:20:56",
      pageNumber: 1,
      pageSize: 20,
      thirdPartApplyId: "apply1",
      userId: "user1",
    });
    try {
      await client.queryCityCarApplyWithOptions(queryCityCarApplyRequest, queryCityCarApplyHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryCityCarApplyHeaders queryCityCarApplyHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryCityCarApplyHeaders();
            queryCityCarApplyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryCityCarApplyRequest queryCityCarApplyRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.QueryCityCarApplyRequest
            {
                CorpId = "corpx",
                CreatedEndAt = "2021-03-18 20:26:59",
                CreatedStartAt = "2021-03-18 20:20:56",
                PageNumber = 1,
                PageSize = 20,
                ThirdPartApplyId = "apply1",
                UserId = "user1",
            };
            try
            {
                client.QueryCityCarApplyWithOptions(queryCityCarApplyRequest, queryCityCarApplyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkalitrip__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkalitrip_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkalitrip_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::Client> client = make_shared<Alibabacloud_Dingtalkalitrip_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::QueryCityCarApplyHeaders> queryCityCarApplyHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::QueryCityCarApplyHeaders>();
  queryCityCarApplyHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::QueryCityCarApplyRequest> queryCityCarApplyRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::QueryCityCarApplyRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("corpx"))},
    {"createdEndAt", boost::any(string("2021-03-18 20:26:59"))},
    {"createdStartAt", boost::any(string("2021-03-18 20:20:56"))},
    {"pageNumber", boost::any(1)},
    {"pageSize", boost::any(20)},
    {"thirdPartApplyId", boost::any(string("apply1"))},
    {"userId", boost::any(string("user1"))}
  }));
  try {
    client->queryCityCarApplyWithOptions(queryCityCarApplyRequest, queryCityCarApplyHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| applyList | Array | 审批单列表。 |
| approverList | Array | 审批单列表。 |
| note | String | 审批备注。 |
| operateTime | String | 审批时间。 |
| order | Long | 审批人排序值。 |
| status | Long | 审批状态：   - **0**：审批中 - **1**：已同意 - **2**：已拒绝 |
| statusDesc | String | 审批状态描述。 |
| userId | String | 审批员工ID。 |
| userName | String | 审批员工姓名。 |
| departId | String | 员工所在部门ID。 |
| departName | String | 员工所在部门。 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 最近修改时间。 |
| itineraryList | Array | 审批单关联的行程。 |
| arrCity | String | 目的地城市。 |
| arrCityCode | String | 目的地城市三字码。 |
| arrDate | String | 到达目的地城市时间。 |
| costCenterId | Long | 商旅内部成本中心ID。 |
| costCenterName | String | 成本中心名称。 |
| depCity | String | 出发城市。 |
| depCityCode | String | 出发城市三字码。 |
| depDate | String | 出发时间。 |
| invoiceId | Long | 商旅内部发票抬头ID。 |
| invoiceName | String | 发票抬头名称。 |
| itineraryId | String | 商旅内部行程单ID。 |
| projectCode | String | 项目code。 |
| projectTitle | String | 项目名称。 |
| trafficType | Long | 交通方式：   - **4**：市内交通 |
| status | Long | 审批单状态：   - **0**：申请 - **1**：同意 - **2**：拒绝 |
| statusDesc | String | 审批单状态：   - **0**：申请 - **1**：同意 - **2**：拒绝 |
| thirdPartApplyId | String | 三方审批单ID。 |
| tripCause | String | 申请事由。 |
| tripTitle | String | 审批单标题。 |
| userId | String | 发起审批员工userid。 |
| userName | String | 发起审批员工名。 |
| total | Long | 总数。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "applyList" : [ {
    "approverList" : [ {
      "note" : "同意",
      "operateTime" : "2021-03-18 20:26:56",
      "order" : 1,
      "status" : 1,
      "statusDesc" : "同意",
      "userId" : "user1",
      "userName" : "员工1"
    } ],
    "departId" : "1",
    "departName" : "部门1",
    "gmtCreate" : "2021-03-18 20:26:56",
    "gmtModified" : "2021-03-18 20:26:56",
    "itineraryList" : [ {
      "arrCity" : "杭州",
      "arrCityCode" : "HGH",
      "arrDate" : "2021-03-18 20:26:56",
      "costCenterId" : 1,
      "costCenterName" : "成本中心1",
      "depCity" : "杭州",
      "depCityCode" : "HGH",
      "depDate" : "2021-03-18 20:26:56",
      "invoiceId" : 1,
      "invoiceName" : "发票抬头1",
      "itineraryId" : "1",
      "projectCode" : "projectx",
      "projectTitle" : "项目x",
      "trafficType" : 4
    } ],
    "statusDesc" : "0",
    "thirdPartApplyId" : "apply1",
    "tripCause" : "杭州出差",
    "tripTitle" : "杭州出差",
    "userId" : "user1",
    "userName" : "员工1"
  } ],
  "total" : 10
}
```
