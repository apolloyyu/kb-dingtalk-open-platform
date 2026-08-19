---
title: "创建园区项目"
source_url: "https://open.dingtalk.com/document/development/create-a-campus-project"
namespace: "development"
slug: "create-a-campus-project"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 地产行业 > 创建园区项目"
doc_id: "mIYAyYpqnw"
updated_at: "2025-09-23 19:22:15"
---

> Source: https://open.dingtalk.com/document/development/create-a-campus-project
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 地产行业 > 创建园区项目
> Updated: 2025-09-23 19:22:15

# 创建园区项目

调用本接口，创建一个园区项目。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/industry/campuses/projects |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Industry.Campus.Write-行业化园区管理写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| campusName | String | 是 | 园区项目的名称。 |
| belongProjectGroupId | Long | 否 | 归属的项目组ID，可调用[创建项目组](1099-create-a-project-group.md)接口获取groupId参数值。 |
| telephone | String | 否 | 联系电话。 |
| description | String | 否 | 园区项目的描述。 |
| area | double | 否 | 园区项目面积。  **[!NOTE]**    该参数指定的单位是平方千米。 |
| country | String | 否 | 园区所在国家。  **[!NOTE]**    国家名称，例如：中国。 |
| provId | Integer | 否 | 园区所在省行政编码。  **[!NOTE]**    例如山东省的行政编码为370000。 |
| cityId | Integer | 否 | 园区所在市行政编码。  **[!NOTE]**    例如山东省济南市的行政编码为370100。 |
| countyId | Integer | 否 | 园区所在区/县行政编码。  **[!NOTE]**    例如山东省济南市厉下区的行政编码为370102。 |
| address | String | 否 | 园区所在详细地址信息。 |
| capacity | Integer | 否 | 园区容量。 |
| orderStartTime | Long | 否 | 项目订购开始时间戳，单位毫秒。 |
| orderEndTime | Long | 否 | 项目订购结束时间戳，单位毫秒。 |
| orderInfo | String | 否 | 订单信息。  **[!NOTE]**    该参数值，开发者自定义。 |
| extend | String | 否 | 扩展字段。  **[!NOTE]**    该参数值，开发者自定义。例如：`{\"creator\":\"001\"}` |
| creatorUnionId | String | 是 | 创建人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| location | String | 否 | 经纬度，格式为：经度,维度。 |

### 请求示例

HTTP

```
POST /v1.0/industry/campuses/projects HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:111
Content-Type:application/json

{
  "campusName" : "绿城未来park",
  "belongProjectGroupId" : 123,
  "telephone" : "156xxxx4338",
  "description" : "绿城未来park项目",
  "area" : 1000.0,
  "country" : "中国",
  "provId" : 370000,
  "cityId" : 370100,
  "countyId" : 371502,
  "address" : "锦城街道和谐社区101号",
  "capacity" : 1000,
  "orderStartTime" : 1655704317794,
  "orderEndTime" : 1655704317794,
  "orderInfo" : "1655704317794",
  "extend" : "{\"creator\":\"dsy\"}",
  "creatorUnionId" : "1111",
  "location" : "116.397128,39.916527"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkindustry_1_0.*;
import com.aliyun.dingtalkindustry_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkindustry_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkindustry_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkindustry_1_0.Client client = Sample.createClient();
        CampusCreateCampusHeaders campusCreateCampusHeaders = new CampusCreateCampusHeaders();
        campusCreateCampusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CampusCreateCampusRequest campusCreateCampusRequest = new CampusCreateCampusRequest()
                .setCampusName("绿城未来park")
                .setBelongProjectGroupId(123L)
                .setTelephone("156xxxx4338")
                .setDescription("绿城未来park项目")
                .setArea(1000D)
                .setCountry("中国")
                .setProvId(370000)
                .setCityId(370100)
                .setCountyId(371502)
                .setAddress("锦城街道和谐社区101号")
                .setCapacity(1000)
                .setOrderStartTime(1655704317794L)
                .setOrderEndTime(1655704317794L)
                .setOrderInfo("1655704317794")
                .setExtend("{\"creator\":\"dsy\"}")
                .setCreatorUnionId("1111")
                .setLocation("116.397128,39.916527");
        try {
            client.campusCreateCampusWithOptions(campusCreateCampusRequest, campusCreateCampusHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.industry_1_0.client import Client as dingtalkindustry_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.industry_1_0 import models as dingtalkindustry__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkindustry_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkindustry_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        campus_create_campus_headers = dingtalkindustry__1__0_models.CampusCreateCampusHeaders()
        campus_create_campus_headers.x_acs_dingtalk_access_token = '<your access token>'
        campus_create_campus_request = dingtalkindustry__1__0_models.CampusCreateCampusRequest(
            campus_name='绿城未来park',
            belong_project_group_id=123,
            telephone='156xxxx4338',
            description='绿城未来park项目',
            area=1000,
            country='中国',
            prov_id=370000,
            city_id=370100,
            county_id=371502,
            address='锦城街道和谐社区101号',
            capacity=1000,
            order_start_time=1655704317794,
            order_end_time=1655704317794,
            order_info='1655704317794',
            extend='{"creator":"dsy"}',
            creator_union_id='1111',
            location='116.397128,39.916527'
        )
        try:
            client.campus_create_campus_with_options(campus_create_campus_request, campus_create_campus_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        campus_create_campus_headers = dingtalkindustry__1__0_models.CampusCreateCampusHeaders()
        campus_create_campus_headers.x_acs_dingtalk_access_token = '<your access token>'
        campus_create_campus_request = dingtalkindustry__1__0_models.CampusCreateCampusRequest(
            campus_name='绿城未来park',
            belong_project_group_id=123,
            telephone='156xxxx4338',
            description='绿城未来park项目',
            area=1000,
            country='中国',
            prov_id=370000,
            city_id=370100,
            county_id=371502,
            address='锦城街道和谐社区101号',
            capacity=1000,
            order_start_time=1655704317794,
            order_end_time=1655704317794,
            order_info='1655704317794',
            extend='{"creator":"dsy"}',
            creator_union_id='1111',
            location='116.397128,39.916527'
        )
        try:
            await client.campus_create_campus_with_options_async(campus_create_campus_request, campus_create_campus_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Models\CampusCreateCampusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Models\CampusCreateCampusRequest;
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
        $campusCreateCampusHeaders = new CampusCreateCampusHeaders([]);
        $campusCreateCampusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $campusCreateCampusRequest = new CampusCreateCampusRequest([
            "campusName" => "绿城未来park",
            "belongProjectGroupId" => 123,
            "telephone" => "156xxxx4338",
            "description" => "绿城未来park项目",
            "area" => 1000,
            "country" => "中国",
            "provId" => 370000,
            "cityId" => 370100,
            "countyId" => 371502,
            "address" => "锦城街道和谐社区101号",
            "capacity" => 1000,
            "orderStartTime" => 1655704317794,
            "orderEndTime" => 1655704317794,
            "orderInfo" => "1655704317794",
            "extend" => "{\"creator\":\"dsy\"}",
            "creatorUnionId" => "1111",
            "location" => "116.397128,39.916527"
        ]);
        try {
            $client->campusCreateCampusWithOptions($campusCreateCampusRequest, $campusCreateCampusHeaders, new RuntimeOptions([]));
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
  dingtalkindustry_1_0  "github.com/alibabacloud-go/dingtalk/industry_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkindustry_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkindustry_1_0.Client{}
  _result, _err = dingtalkindustry_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  campusCreateCampusHeaders := &dingtalkindustry_1_0.CampusCreateCampusHeaders{}
  campusCreateCampusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  campusCreateCampusRequest := &dingtalkindustry_1_0.CampusCreateCampusRequest{
    CampusName: tea.String("绿城未来park"),
    BelongProjectGroupId: tea.Int64(123),
    Telephone: tea.String("156xxxx4338"),
    Description: tea.String("绿城未来park项目"),
    Area: tea.Float64(1000),
    Country: tea.String("中国"),
    ProvId: tea.Int32(370000),
    CityId: tea.Int32(370100),
    CountyId: tea.Int32(371502),
    Address: tea.String("锦城街道和谐社区101号"),
    Capacity: tea.Int32(1000),
    OrderStartTime: tea.Int64(1655704317794),
    OrderEndTime: tea.Int64(1655704317794),
    OrderInfo: tea.String("1655704317794"),
    Extend: tea.String("{\"creator\":\"dsy\"}"),
    CreatorUnionId: tea.String("1111"),
    Location: tea.String("116.397128,39.916527"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CampusCreateCampusWithOptions(campusCreateCampusRequest, campusCreateCampusHeaders, &util.RuntimeOptions{})
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
import dingtalkindustry_1_0, * as $dingtalkindustry_1_0 from '@alicloud/dingtalk/industry_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkindustry_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkindustry_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let campusCreateCampusHeaders = new $dingtalkindustry_1_0.CampusCreateCampusHeaders({ });
    campusCreateCampusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let campusCreateCampusRequest = new $dingtalkindustry_1_0.CampusCreateCampusRequest({
      campusName: "绿城未来park",
      belongProjectGroupId: 123,
      telephone: "156xxxx4338",
      description: "绿城未来park项目",
      area: 1000,
      country: "中国",
      provId: 370000,
      cityId: 370100,
      countyId: 371502,
      address: "锦城街道和谐社区101号",
      capacity: 1000,
      orderStartTime: 1655704317794,
      orderEndTime: 1655704317794,
      orderInfo: "1655704317794",
      extend: "{\"creator\":\"dsy\"}",
      creatorUnionId: "1111",
      location: "116.397128,39.916527",
    });
    try {
      await client.campusCreateCampusWithOptions(campusCreateCampusRequest, campusCreateCampusHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkindustry_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkindustry_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusHeaders campusCreateCampusHeaders = new AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusHeaders();
            campusCreateCampusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusRequest campusCreateCampusRequest = new AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusRequest
            {
                CampusName = "绿城未来park",
                BelongProjectGroupId = 123,
                Telephone = "156xxxx4338",
                Description = "绿城未来park项目",
                Area = 1000,
                Country = "中国",
                ProvId = 370000,
                CityId = 370100,
                CountyId = 371502,
                Address = "锦城街道和谐社区101号",
                Capacity = 1000,
                OrderStartTime = 1655704317794,
                OrderEndTime = 1655704317794,
                OrderInfo = "1655704317794",
                Extend = "{\"creator\":\"dsy\"}",
                CreatorUnionId = "1111",
                Location = "116.397128,39.916527",
            };
            try
            {
                client.CampusCreateCampusWithOptions(campusCreateCampusRequest, campusCreateCampusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| campusCorpId | String | 园区组织CorpId。 |
| campusDeptId | String | 园区组织在上下游组织内的部门ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "campusCorpId" : "园区组织ID",
  "campusDeptId" : "园区部门ID"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | system.error.contact | %s | 创建项目失败 |
| 500 | sytem.error | system error %s | 系统错误 |
| 500 | checkParam.invalid.notCampusTenantOrg | %s | 当前组织非园区租户组织 |
| 500 | system.error.campusProjectContactNotInit | %s | 项目通讯录未初始化 |
