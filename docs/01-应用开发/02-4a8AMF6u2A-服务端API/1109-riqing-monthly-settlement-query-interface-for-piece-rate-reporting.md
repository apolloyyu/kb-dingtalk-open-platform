---
title: "查询计件报工数据"
source_url: "https://open.dingtalk.com/document/development/riqing-monthly-settlement-query-interface-for-piece-rate-reporting"
namespace: "development"
slug: "riqing-monthly-settlement-query-interface-for-piece-rate-reporting"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 制造业 > 查询计件报工数据"
doc_id: "AbzyyyJBWS"
updated_at: "2025-09-23 19:22:22"
---

> Source: https://open.dingtalk.com/document/development/riqing-monthly-settlement-query-interface-for-piece-rate-reporting
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 制造业 > 查询计件报工数据
> Updated: 2025-09-23 19:22:22

# 查询计件报工数据

调用本接口查询计件报工的数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/manufacturing/users/jobs/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Manufacture.JobBook.Read-制造业计件报工数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| productName | String | 否 | 产品中文名称。 |
| pageSize | Integer | 否 | 分页参数每页显示条数。 |
| qualifiedQuantity | String | 否 | 报工合格数量。 |
| manufactureDay | String | 否 | 生产日期。 |
| instNo | String | 否 | 工单编号。 |
| userName | String | 否 | 员工姓名。 |
| productCode | String | 否 | 产品唯一标识。 |
| productSpecification | String | 否 | 产品规格。 |
| unitPrice | String | 否 | 计件单价，单位：分。 |
| uuid | String | 否 | 报工记录的唯一标识。 |
| currentPage | Integer | 否 | 分页参数，页码，从1开始。 |
| userId | String | 否 | 员工的userid。 |
| mesAppKey | String | 否 | MES系统唯一标识。 |

### 请求示例

HTTP

```
POST /v1.0/manufacturing/users/jobs/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d41d8cd98f00b204e9800998ecf8427e
Content-Type:application/json

{
  "productName" : "双头螺柱001",
  "pageSize" : 10,
  "qualifiedQuantity" : "100",
  "manufactureDay" : "2021-07-05",
  "instNo" : "d41d8cd98f00b204e9800998ecf8427e",
  "userName" : "张三",
  "productCode" : "A001",
  "productSpecification" : "M56*3*10501",
  "unitPrice" : "1.2",
  "uuid" : "d41d8cd98f00b204e9800998ecf8427e",
  "currentPage" : 1,
  "userId" : "1919442747879773",
  "mesAppKey" : "mes41d8cd98f0b204e9800998ecf8427e"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkmanufacturing_1_0.*;
import com.aliyun.dingtalkmanufacturing_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkmanufacturing_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmanufacturing_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkmanufacturing_1_0.Client client = Sample.createClient();
        IndustrializeManufactureQueryJobsHeaders industrializeManufactureQueryJobsHeaders = new IndustrializeManufactureQueryJobsHeaders();
        industrializeManufactureQueryJobsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        IndustrializeManufactureQueryJobsRequest industrializeManufactureQueryJobsRequest = new IndustrializeManufactureQueryJobsRequest()
                .setProductName("双头螺柱001")
                .setPageSize(10)
                .setQualifiedQuantity("100")
                .setManufactureDay("2021-07-05")
                .setInstNo("d41d8cd98f0xxxx")
                .setUserName("小明")
                .setProductCode("A001")
                .setProductSpecification("M56*3*10501")
                .setUnitPrice("1.2")
                .setUuid("d41d8cd98f0xxxx")
                .setCurrentPage(1)
                .setUserId("19194427xxx")
                .setMesAppKey("mes41d8cdxxxx");
        try {
            client.industrializeManufactureQueryJobsWithOptions(industrializeManufactureQueryJobsRequest, industrializeManufactureQueryJobsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.manufacturing_1_0.client import Client as dingtalkmanufacturing_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.manufacturing_1_0 import models as dingtalkmanufacturing__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmanufacturing_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmanufacturing_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        industrialize_manufacture_query_jobs_headers = dingtalkmanufacturing__1__0_models.IndustrializeManufactureQueryJobsHeaders()
        industrialize_manufacture_query_jobs_headers.x_acs_dingtalk_access_token = '<your access token>'
        industrialize_manufacture_query_jobs_request = dingtalkmanufacturing__1__0_models.IndustrializeManufactureQueryJobsRequest(
            product_name='双头螺柱001',
            page_size=10,
            qualified_quantity='100',
            manufacture_day='2021-07-05',
            inst_no='d41d8cd98f0xxxx',
            user_name='小明',
            product_code='A001',
            product_specification='M56*3*10501',
            unit_price='1.2',
            uuid='d41d8cd98f0xxxx',
            current_page=1,
            user_id='19194427xxx',
            mes_app_key='mes41d8cdxxxx'
        )
        try:
            client.industrialize_manufacture_query_jobs_with_options(industrialize_manufacture_query_jobs_request, industrialize_manufacture_query_jobs_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        industrialize_manufacture_query_jobs_headers = dingtalkmanufacturing__1__0_models.IndustrializeManufactureQueryJobsHeaders()
        industrialize_manufacture_query_jobs_headers.x_acs_dingtalk_access_token = '<your access token>'
        industrialize_manufacture_query_jobs_request = dingtalkmanufacturing__1__0_models.IndustrializeManufactureQueryJobsRequest(
            product_name='双头螺柱001',
            page_size=10,
            qualified_quantity='100',
            manufacture_day='2021-07-05',
            inst_no='d41d8cd98f0xxxx',
            user_name='小明',
            product_code='A001',
            product_specification='M56*3*10501',
            unit_price='1.2',
            uuid='d41d8cd98f0xxxx',
            current_page=1,
            user_id='19194427xxx',
            mes_app_key='mes41d8cdxxxx'
        )
        try:
            await client.industrialize_manufacture_query_jobs_with_options_async(industrialize_manufacture_query_jobs_request, industrialize_manufacture_query_jobs_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmanufacturing_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmanufacturing_1_0\Models\IndustrializeManufactureQueryJobsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmanufacturing_1_0\Models\IndustrializeManufactureQueryJobsRequest;
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
        $industrializeManufactureQueryJobsHeaders = new IndustrializeManufactureQueryJobsHeaders([]);
        $industrializeManufactureQueryJobsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $industrializeManufactureQueryJobsRequest = new IndustrializeManufactureQueryJobsRequest([
            "productName" => "双头螺柱001",
            "pageSize" => 10,
            "qualifiedQuantity" => "100",
            "manufactureDay" => "2021-07-05",
            "instNo" => "d41d8cd98f0xxxx",
            "userName" => "小明",
            "productCode" => "A001",
            "productSpecification" => "M56*3*10501",
            "unitPrice" => "1.2",
            "uuid" => "d41d8cd98f0xxxx",
            "currentPage" => 1,
            "userId" => "19194427xxx",
            "mesAppKey" => "mes41d8cdxxxx"
        ]);
        try {
            $client->industrializeManufactureQueryJobsWithOptions($industrializeManufactureQueryJobsRequest, $industrializeManufactureQueryJobsHeaders, new RuntimeOptions([]));
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
  dingtalkmanufacturing_1_0  "github.com/alibabacloud-go/dingtalk/manufacturing_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkmanufacturing_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmanufacturing_1_0.Client{}
  _result, _err = dingtalkmanufacturing_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  industrializeManufactureQueryJobsHeaders := &dingtalkmanufacturing_1_0.IndustrializeManufactureQueryJobsHeaders{}
  industrializeManufactureQueryJobsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  industrializeManufactureQueryJobsRequest := &dingtalkmanufacturing_1_0.IndustrializeManufactureQueryJobsRequest{
    ProductName: tea.String("双头螺柱001"),
    PageSize: tea.Int32(10),
    QualifiedQuantity: tea.String("100"),
    ManufactureDay: tea.String("2021-07-05"),
    InstNo: tea.String("d41d8cd98f0xxxx"),
    UserName: tea.String("小明"),
    ProductCode: tea.String("A001"),
    ProductSpecification: tea.String("M56*3*10501"),
    UnitPrice: tea.String("1.2"),
    Uuid: tea.String("d41d8cd98f0xxxx"),
    CurrentPage: tea.Int32(1),
    UserId: tea.String("19194427xxx"),
    MesAppKey: tea.String("mes41d8cdxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.IndustrializeManufactureQueryJobsWithOptions(industrializeManufactureQueryJobsRequest, industrializeManufactureQueryJobsHeaders, &util.RuntimeOptions{})
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
import dingtalkmanufacturing_1_0, * as $dingtalkmanufacturing_1_0 from '@alicloud/dingtalk/manufacturing_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkmanufacturing_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkmanufacturing_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let industrializeManufactureQueryJobsHeaders = new $dingtalkmanufacturing_1_0.IndustrializeManufactureQueryJobsHeaders({ });
    industrializeManufactureQueryJobsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let industrializeManufactureQueryJobsRequest = new $dingtalkmanufacturing_1_0.IndustrializeManufactureQueryJobsRequest({
      productName: "双头螺柱001",
      pageSize: 10,
      qualifiedQuantity: "100",
      manufactureDay: "2021-07-05",
      instNo: "d41d8cd98f0xxxx",
      userName: "小明",
      productCode: "A001",
      productSpecification: "M56*3*10501",
      unitPrice: "1.2",
      uuid: "d41d8cd98f0xxxx",
      currentPage: 1,
      userId: "19194427xxx",
      mesAppKey: "mes41d8cdxxxx",
    });
    try {
      await client.industrializeManufactureQueryJobsWithOptions(industrializeManufactureQueryJobsRequest, industrializeManufactureQueryJobsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Models.IndustrializeManufactureQueryJobsHeaders industrializeManufactureQueryJobsHeaders = new AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Models.IndustrializeManufactureQueryJobsHeaders();
            industrializeManufactureQueryJobsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Models.IndustrializeManufactureQueryJobsRequest industrializeManufactureQueryJobsRequest = new AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Models.IndustrializeManufactureQueryJobsRequest
            {
                ProductName = "双头螺柱001",
                PageSize = 10,
                QualifiedQuantity = "100",
                ManufactureDay = "2021-07-05",
                InstNo = "d41d8cd98f0xxxx",
                UserName = "小明",
                ProductCode = "A001",
                ProductSpecification = "M56*3*10501",
                UnitPrice = "1.2",
                Uuid = "d41d8cd98f0xxxx",
                CurrentPage = 1,
                UserId = "19194427xxx",
                MesAppKey = "mes41d8cdxxxx",
            };
            try
            {
                client.IndustrializeManufactureQueryJobsWithOptions(industrializeManufactureQueryJobsRequest, industrializeManufactureQueryJobsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkmanufacturing__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkmanufacturing_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkmanufacturing_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkmanufacturing_1_0::Client> client = make_shared<Alibabacloud_Dingtalkmanufacturing_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkmanufacturing_1_0::IndustrializeManufactureQueryJobsHeaders> industrializeManufactureQueryJobsHeaders = make_shared<Alibabacloud_Dingtalkmanufacturing_1_0::IndustrializeManufactureQueryJobsHeaders>();
  industrializeManufactureQueryJobsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkmanufacturing_1_0::IndustrializeManufactureQueryJobsRequest> industrializeManufactureQueryJobsRequest = make_shared<Alibabacloud_Dingtalkmanufacturing_1_0::IndustrializeManufactureQueryJobsRequest>(map<string, boost::any>({
    {"productName", boost::any(string("双头螺柱001"))},
    {"pageSize", boost::any(10)},
    {"qualifiedQuantity", boost::any(string("100"))},
    {"manufactureDay", boost::any(string("2021-07-05"))},
    {"instNo", boost::any(string("d41d8cd98f0xxxx"))},
    {"userName", boost::any(string("小明"))},
    {"productCode", boost::any(string("A001"))},
    {"productSpecification", boost::any(string("M56*3*10501"))},
    {"unitPrice", boost::any(string("1.2"))},
    {"uuid", boost::any(string("d41d8cd98f0xxxx"))},
    {"currentPage", boost::any(1)},
    {"userId", boost::any(string("19194427xxx"))},
    {"mesAppKey", boost::any(string("mes41d8cdxxxx"))}
  }));
  try {
    client->industrializeManufactureQueryJobsWithOptions(industrializeManufactureQueryJobsRequest, industrializeManufactureQueryJobsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| httpCode | String | 返回的HTTP状态码。 |
| content | String | 查询的数据结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "httpCode" : "200",
  "content" : "{     \"data\": [         {             \"productSpecification\": \"M56*3*xxx\",             \"qualifiedQuantity\": 100,             \"userName\": \"小明\",             \"gmtCreate\": \"2021-08-08 14:34:28\",             \"uuid\": \"a902f747-cxxxx\",             \"userId\": \"1924xxxx\",             \"productName\": \"双头螺柱001\",             \"productCode\": \"A001\",             \"processName\": \"制程名称\",             \"mesAppKey\": \"mERP\",             \"instNo\": \"123\",             \"manufactureDay\": \"2021-07-05\",             \"manufactureDate\": \"2021-07-05 08:10:21\"         }     ],     \"pageSize\": 10,     \"currentPage\": 1,     \"totalCount\": 1 }"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 401 | illegal.argument | 参数有误 %s | 参数有误 %s |
| 403 | permission.wrong | 无权限 %s | 无权限 %s |
| 404 | error.notFound | 接口路径错误 %s | 接口路径错误 %s |
| 500 | error.unknownerror | 服务器内部错误 %s | 服务器内部错误 %s |
