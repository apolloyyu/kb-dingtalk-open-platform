---
title: "计件报工"
source_url: "https://open.dingtalk.com/document/development/riqing-monthly-settlement-piece-rate-reporting-interface"
namespace: "development"
slug: "riqing-monthly-settlement-piece-rate-reporting-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 制造业 > 计件报工"
doc_id: "KHKkxuXOo3"
updated_at: "2025-09-23 19:22:22"
---

> Source: https://open.dingtalk.com/document/development/riqing-monthly-settlement-piece-rate-reporting-interface
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 制造业 > 计件报工
> Updated: 2025-09-23 19:22:22

# 计件报工

本接口用于MES系统上报计件数据到平台。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/manufacturing/users/{userId}/jobs |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Manufacture.JobBook.Write-制造业计件报工数据写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 员工钉钉userid。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| scrappedQuantity | String | 否 | 报废数量。 |
| productSpecification | String | 否 | 产品规格。 |
| qualifiedQuantity | String | 是 | 合格数量。 |
| reworkableQuantity | String | 否 | 可重工数量。 |
| userName | String | 否 | 员工姓名。 |
| uuid | String | 是 | 随机字符串，唯一标识，用于幂等及更新。 |
| productName | String | 否 | 产品名称，例如：双头螺柱001。 |
| productEnName | String | 否 | 产品英文名称。 |
| extend | String | 否 | 扩展字段，用于增加自定义字段。   ``` [     {         "code": "equipmentName",         "name": "设备名称",         "value": "8000",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段1",         "value": "值",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段2",         "value": "值",         "valueType": "number"     } ] ``` |
| productCode | String | 否 | 产品唯一标识。 |
| processName | String | 否 | 制程名称。 |
| processEnName | String | 否 | 制程英文名称。 |
| mesAppKey | String | 是 | **mes**系统唯一标识。 |
| instNo | String | 是 | 工单编号。 |
| manufactureDate | String | 是 | 生产日期时间，格式：`yyyy-MM-dd HH:mm:ss`。 |
| dingCorpId | String | 否 | 工厂所在钉钉组织的企业corpId。 |
| isBatchJob | String | 否 | 是否是批量报工，即一次计件报工由多个工人一起分担。   - y：是 - n：否 |
| userNameList | String | 否 | 批量报工时，多个工人的用户名列表，以英文逗号分隔。 |
| userIdList | String | 否 | 批量报工时，多个工人的钉钉工号列表，以英文逗号分隔。 |
| unitPrice | String | 否 | 计件单价，单位：分。 |

### 请求示例

HTTP

```
POST /v1.0/manufacturing/users/员工钉钉userId/jobs HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d8cdxxx
Content-Type:application/json

{
  "scrappedQuantity" : "0",
  "productSpecification" : "M56*3*10501",
  "qualifiedQuantity" : "100",
  "reworkableQuantity" : "1",
  "userName" : "张xx",
  "uuid" : "9b29c34f95736d",
  "productName" : "双头螺柱001",
  "productEnName" : "Stud 001",
  "extend" : "[     {         \"code\": \"equipmentName\",         \"name\": \"设备名称\",         \"value\": \"8000\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段1\",         \"value\": \"值\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段2\",         \"value\": \"值\",         \"valueType\": \"number\"     } ]",
  "productCode" : "A001",
  "processName" : "制程名称",
  "processEnName" : "制程英文名称",
  "mesAppKey" : "lingfei",
  "instNo" : "123",
  "manufactureDate" : "2021-07-05 08:10:21"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
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
        IndustrializeManufactureJobBookRequest industrializeManufactureJobBookRequest = new IndustrializeManufactureJobBookRequest()
                .setScrappedQuantity("0")
                .setProductSpecification("M56*3*10501")
                .setQualifiedQuantity("100")
                .setReworkableQuantity("1")
                .setUserName("张xx")
                .setUuid("9b29c34f95736d")
                .setProductName("双头螺柱001")
                .setProductEnName("Stud 001")
                .setExtend("[     {         \"code\": \"equipmentName\",         \"name\": \"设备名称\",         \"value\": \"8000\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段1\",         \"value\": \"值\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段2\",         \"value\": \"值\",         \"valueType\": \"number\"     } ]")
                .setProductCode("A001")
                .setProcessName("制程名称")
                .setProcessEnName("制程英文名称")
                .setMesAppKey("lingfei")
                .setInstNo("123")
                .setManufactureDate("2021-07-05 08:10:21")
                .setDingCorpId("ding128727edd28e83a35c2f4657eb378")
                .setIsBatchJob("y")
                .setUserNameList("小明,小红")
                .setUserIdList("1919442747879777,1919442747879775")
                .setUnitPrice("0.02");
        try {
            client.industrializeManufactureJobBook("员工钉钉userId", industrializeManufactureJobBookRequest);
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
        industrialize_manufacture_job_book_request = dingtalkmanufacturing__1__0_models.IndustrializeManufactureJobBookRequest(
            scrapped_quantity='0',
            product_specification='M56*3*10501',
            qualified_quantity='100',
            reworkable_quantity='1',
            user_name='张xx',
            uuid='9b29c34f95736d',
            product_name='双头螺柱001',
            product_en_name='Stud 001',
            extend='[     {         "code": "equipmentName",         "name": "设备名称",         "value": "8000",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段1",         "value": "值",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段2",         "value": "值",         "valueType": "number"     } ]',
            product_code='A001',
            process_name='制程名称',
            process_en_name='制程英文名称',
            mes_app_key='lingfei',
            inst_no='123',
            manufacture_date='2021-07-05 08:10:21',
            ding_corp_id='ding128727edd28e83a35c2f4657eb378',
            is_batch_job='y',
            user_name_list='小明,小红',
            user_id_list='1919442747879777,1919442747879775',
            unit_price='0.02'
        )
        try:
            client.industrialize_manufacture_job_book('员工钉钉userId', industrialize_manufacture_job_book_request)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        industrialize_manufacture_job_book_request = dingtalkmanufacturing__1__0_models.IndustrializeManufactureJobBookRequest(
            scrapped_quantity='0',
            product_specification='M56*3*10501',
            qualified_quantity='100',
            reworkable_quantity='1',
            user_name='张xx',
            uuid='9b29c34f95736d',
            product_name='双头螺柱001',
            product_en_name='Stud 001',
            extend='[     {         "code": "equipmentName",         "name": "设备名称",         "value": "8000",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段1",         "value": "值",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段2",         "value": "值",         "valueType": "number"     } ]',
            product_code='A001',
            process_name='制程名称',
            process_en_name='制程英文名称',
            mes_app_key='lingfei',
            inst_no='123',
            manufacture_date='2021-07-05 08:10:21',
            ding_corp_id='ding128727edd28e83a35c2f4657eb378',
            is_batch_job='y',
            user_name_list='小明,小红',
            user_id_list='1919442747879777,1919442747879775',
            unit_price='0.02'
        )
        try:
            await client.industrialize_manufacture_job_book_async('员工钉钉userId', industrialize_manufacture_job_book_request)
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
use AlibabaCloud\SDK\Dingtalk\Vmanufacturing_1_0\Models\IndustrializeManufactureJobBookRequest;

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
        $industrializeManufactureJobBookRequest = new IndustrializeManufactureJobBookRequest([
            "scrappedQuantity" => "0",
            "productSpecification" => "M56*3*10501",
            "qualifiedQuantity" => "100",
            "reworkableQuantity" => "1",
            "userName" => "张xx",
            "uuid" => "9b29c34f95736d",
            "productName" => "双头螺柱001",
            "productEnName" => "Stud 001",
            "extend" => "[     {         \"code\": \"equipmentName\",         \"name\": \"设备名称\",         \"value\": \"8000\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段1\",         \"value\": \"值\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段2\",         \"value\": \"值\",         \"valueType\": \"number\"     } ]",
            "productCode" => "A001",
            "processName" => "制程名称",
            "processEnName" => "制程英文名称",
            "mesAppKey" => "lingfei",
            "instNo" => "123",
            "manufactureDate" => "2021-07-05 08:10:21",
            "dingCorpId" => "ding128727edd28e83a35c2f4657eb378",
            "isBatchJob" => "y",
            "userNameList" => "小明,小红",
            "userIdList" => "1919442747879777,1919442747879775",
            "unitPrice" => "0.02"
        ]);
        try {
            $client->industrializeManufactureJobBook("员工钉钉userId", $industrializeManufactureJobBookRequest);
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

  industrializeManufactureJobBookRequest := &dingtalkmanufacturing_1_0.IndustrializeManufactureJobBookRequest{
    ScrappedQuantity: tea.String("0"),
    ProductSpecification: tea.String("M56*3*10501"),
    QualifiedQuantity: tea.String("100"),
    ReworkableQuantity: tea.String("1"),
    UserName: tea.String("张xx"),
    Uuid: tea.String("9b29c34f95736d"),
    ProductName: tea.String("双头螺柱001"),
    ProductEnName: tea.String("Stud 001"),
    Extend: tea.String("[     {         \"code\": \"equipmentName\",         \"name\": \"设备名称\",         \"value\": \"8000\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段1\",         \"value\": \"值\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段2\",         \"value\": \"值\",         \"valueType\": \"number\"     } ]"),
    ProductCode: tea.String("A001"),
    ProcessName: tea.String("制程名称"),
    ProcessEnName: tea.String("制程英文名称"),
    MesAppKey: tea.String("lingfei"),
    InstNo: tea.String("123"),
    ManufactureDate: tea.String("2021-07-05 08:10:21"),
    DingCorpId: tea.String("ding128727edd28e83a35c2f4657eb378"),
    IsBatchJob: tea.String("y"),
    UserNameList: tea.String("小明,小红"),
    UserIdList: tea.String("1919442747879777,1919442747879775"),
    UnitPrice: tea.String("0.02"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.IndustrializeManufactureJobBook(tea.String("员工钉钉userId"), industrializeManufactureJobBookRequest)
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
import Util from '@alicloud/tea-util';
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
    let industrializeManufactureJobBookRequest = new $dingtalkmanufacturing_1_0.IndustrializeManufactureJobBookRequest({
      scrappedQuantity: "0",
      productSpecification: "M56*3*10501",
      qualifiedQuantity: "100",
      reworkableQuantity: "1",
      userName: "张xx",
      uuid: "9b29c34f95736d",
      productName: "双头螺柱001",
      productEnName: "Stud 001",
      extend: "[     {         \"code\": \"equipmentName\",         \"name\": \"设备名称\",         \"value\": \"8000\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段1\",         \"value\": \"值\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段2\",         \"value\": \"值\",         \"valueType\": \"number\"     } ]",
      productCode: "A001",
      processName: "制程名称",
      processEnName: "制程英文名称",
      mesAppKey: "lingfei",
      instNo: "123",
      manufactureDate: "2021-07-05 08:10:21",
      dingCorpId: "ding128727edd28e83a35c2f4657eb378",
      isBatchJob: "y",
      userNameList: "小明,小红",
      userIdList: "1919442747879777,1919442747879775",
      unitPrice: "0.02",
    });
    try {
      await client.industrializeManufactureJobBook("员工钉钉userId", industrializeManufactureJobBookRequest);
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
            AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Models.IndustrializeManufactureJobBookRequest industrializeManufactureJobBookRequest = new AlibabaCloud.SDK.Dingtalkmanufacturing_1_0.Models.IndustrializeManufactureJobBookRequest
            {
                ScrappedQuantity = "0",
                ProductSpecification = "M56*3*10501",
                QualifiedQuantity = "100",
                ReworkableQuantity = "1",
                UserName = "张xx",
                Uuid = "9b29c34f95736d",
                ProductName = "双头螺柱001",
                ProductEnName = "Stud 001",
                Extend = "[     {         \"code\": \"equipmentName\",         \"name\": \"设备名称\",         \"value\": \"8000\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段1\",         \"value\": \"值\",         \"valueType\": \"string\"     },     {         \"code\": \"唯一标识\",         \"name\": \"自定义字段2\",         \"value\": \"值\",         \"valueType\": \"number\"     } ]",
                ProductCode = "A001",
                ProcessName = "制程名称",
                ProcessEnName = "制程英文名称",
                MesAppKey = "lingfei",
                InstNo = "123",
                ManufactureDate = "2021-07-05 08:10:21",
                DingCorpId = "ding128727edd28e83a35c2f4657eb378",
                IsBatchJob = "y",
                UserNameList = "小明,小红",
                UserIdList = "1919442747879777,1919442747879775",
                UnitPrice = "0.02",
            };
            try
            {
                client.IndustrializeManufactureJobBook("员工钉钉userId", industrializeManufactureJobBookRequest);
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
  shared_ptr<Alibabacloud_Dingtalkmanufacturing_1_0::IndustrializeManufactureJobBookRequest> industrializeManufactureJobBookRequest = make_shared<Alibabacloud_Dingtalkmanufacturing_1_0::IndustrializeManufactureJobBookRequest>(map<string, boost::any>({
    {"scrappedQuantity", boost::any(string("0"))},
    {"productSpecification", boost::any(string("M56*3*10501"))},
    {"qualifiedQuantity", boost::any(string("100"))},
    {"reworkableQuantity", boost::any(string("1"))},
    {"userName", boost::any(string("张xx"))},
    {"uuid", boost::any(string("9b29c34f95736d"))},
    {"productName", boost::any(string("双头螺柱001"))},
    {"productEnName", boost::any(string("Stud 001"))},
    {"extend", boost::any(string("[     {         "code": "equipmentName",         "name": "设备名称",         "value": "8000",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段1",         "value": "值",         "valueType": "string"     },     {         "code": "唯一标识",         "name": "自定义字段2",         "value": "值",         "valueType": "number"     } ]"))},
    {"productCode", boost::any(string("A001"))},
    {"processName", boost::any(string("制程名称"))},
    {"processEnName", boost::any(string("制程英文名称"))},
    {"mesAppKey", boost::any(string("lingfei"))},
    {"instNo", boost::any(string("123"))},
    {"manufactureDate", boost::any(string("2021-07-05 08:10:21"))},
    {"dingCorpId", boost::any(string("ding128727edd28e83a35c2f4657eb378"))},
    {"isBatchJob", boost::any(string("y"))},
    {"userNameList", boost::any(string("小明,小红"))},
    {"userIdList", boost::any(string("1919442747879777,1919442747879775"))},
    {"unitPrice", boost::any(string("0.02"))}
  }));
  try {
    client->industrializeManufactureJobBook(make_shared<string>("员工钉钉userId"), industrializeManufactureJobBookRequest);
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
| httpCode | String | HTTP响应码。 |
| uuid | String | 此次上报的计件数据的唯一标识。 |
| content | String | 返回结果。 |
| errorMsg | String | 错误码描述。 |
| errorLevel | Integer | 错误级别，取值：   - 200：警告 - 100：业务错误 - 0：系统错误 |
| errorCode | String | 调用失败时返回的错误码。 |
| success | Boolean | 调用是否成功，取值:   - true：成功 - false：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "content" : {
    "id" : 21,
    "count" : 1
  },
  "uuid" : "d41d8cd98f00xxx"
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
| 501 | illegal.field.notnull | 当前字段不能为空 %s | 当前字段不能为空 %s |
| 999 | error.unknownerror | %s | %s |
