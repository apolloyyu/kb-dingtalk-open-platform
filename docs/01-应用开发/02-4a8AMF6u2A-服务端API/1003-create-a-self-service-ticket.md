---
title: "创建自助单"
source_url: "https://open.dingtalk.com/document/development/create-a-self-service-ticket"
namespace: "development"
slug: "create-a-self-service-ticket"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 智能客服 > 创建自助单"
doc_id: "B06Gkn9CAy"
updated_at: "2025-09-23 19:20:14"
---

> Source: https://open.dingtalk.com/document/development/create-a-self-service-ticket
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 智能客服 > 创建自助单
> Updated: 2025-09-23 19:20:14

# 创建自助单

调用本接口创建用户自定义的自助单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/customerService/tickets |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_customer\_service\_ticket\_write-客服行业的工单写接口权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| sourceId | String | 是 | 会员来源，取diamond配置的值。 |
| foreignId | String | 是 | 第三方会员ID。 |
| foreignName | String | 是 | 第三方会员名称。 |
| openInstanceId | String | 否 | 实例ID。      单实例企业必须传**default**，多实例企业必须传实例ID。 |
| productionType | Integer | 否 | 智能客服产品类型：   - **1**：智能客服 - **2**：服务群 - **1003**：服务台 - **1004**：小蜜客服 |
| templateId | String | 是 | 自助单ID，钉钉智能客服自助单配置里的值。 |
| title | String | 是 | 工单标题。 |
| properties | Array | 否 | 工单表单。 |
| name | String | 否 | 字段的key。 |
| value | String | 否 | 字段的值。 |

### 请求示例

HTTP

```
POST /v1.0/customerService/tickets HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:111111111
Content-Type:application/json

{
  "sourceId" : "AliTest",
  "foreignId" : "20210001",
  "foreignName" : "自助单测试用户",
  "openInstanceId" : "default",
  "productionType" : 1,
  "templateId" : "31904",
  "title" : "测试自助单",
  "properties" : [ {
    "name" : "question_type",
    "value" : "requirement"
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
import com.aliyun.dingtalkcustomer_service_1_0.*;
import com.aliyun.dingtalkcustomer_service_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcustomer_service_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcustomer_service_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcustomer_service_1_0.Client client = Sample.createClient();
        CreateTicketHeaders createTicketHeaders = new CreateTicketHeaders();
        createTicketHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateTicketRequest.CreateTicketRequestProperties properties0 = new CreateTicketRequest.CreateTicketRequestProperties()
                .setName("question_type")
                .setValue("requirement");
        CreateTicketRequest createTicketRequest = new CreateTicketRequest()
                .setSourceId("AliTest")
                .setForeignId("20210001")
                .setForeignName("自助单测试用户")
                .setOpenInstanceId("default")
                .setProductionType(1)
                .setTemplateId("31904")
                .setTitle("测试自助单")
                .setProperties(java.util.Arrays.asList(
                    properties0
                ));
        try {
            client.createTicketWithOptions(createTicketRequest, createTicketHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.customerService_1_0.client import Client as dingtalkcustomerService_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.customerService_1_0 import models as dingtalkcustomer_service__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcustomerService_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcustomerService_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_ticket_headers = dingtalkcustomer_service__1__0_models.CreateTicketHeaders()
        create_ticket_headers.x_acs_dingtalk_access_token = '<your access token>'
        properties_0 = dingtalkcustomer_service__1__0_models.CreateTicketRequestProperties(
            name='question_type',
            value='requirement'
        )
        create_ticket_request = dingtalkcustomer_service__1__0_models.CreateTicketRequest(
            source_id='AliTest',
            foreign_id='20210001',
            foreign_name='自助单测试用户',
            open_instance_id='default',
            production_type=1,
            template_id='31904',
            title='测试自助单',
            properties=[
                properties_0
            ]
        )
        try:
            client.create_ticket_with_options(create_ticket_request, create_ticket_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_ticket_headers = dingtalkcustomer_service__1__0_models.CreateTicketHeaders()
        create_ticket_headers.x_acs_dingtalk_access_token = '<your access token>'
        properties_0 = dingtalkcustomer_service__1__0_models.CreateTicketRequestProperties(
            name='question_type',
            value='requirement'
        )
        create_ticket_request = dingtalkcustomer_service__1__0_models.CreateTicketRequest(
            source_id='AliTest',
            foreign_id='20210001',
            foreign_name='自助单测试用户',
            open_instance_id='default',
            production_type=1,
            template_id='31904',
            title='测试自助单',
            properties=[
                properties_0
            ]
        )
        try:
            await client.create_ticket_with_options_async(create_ticket_request, create_ticket_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcustomer_service_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcustomer_service_1_0\Models\CreateTicketHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcustomer_service_1_0\Models\CreateTicketRequest\properties;
use AlibabaCloud\SDK\Dingtalk\Vcustomer_service_1_0\Models\CreateTicketRequest;
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
        $createTicketHeaders = new CreateTicketHeaders([]);
        $createTicketHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $properties0 = new properties([
            "name" => "question_type",
            "value" => "requirement"
        ]);
        $createTicketRequest = new CreateTicketRequest([
            "sourceId" => "AliTest",
            "foreignId" => "20210001",
            "foreignName" => "自助单测试用户",
            "openInstanceId" => "default",
            "productionType" => 1,
            "templateId" => "31904",
            "title" => "测试自助单",
            "properties" => [
                $properties0
            ]
        ]);
        try {
            $client->createTicketWithOptions($createTicketRequest, $createTicketHeaders, new RuntimeOptions([]));
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
  dingtalkcustomerservice_1_0  "github.com/alibabacloud-go/dingtalk/customerService_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcustomerservice_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcustomerservice_1_0.Client{}
  _result, _err = dingtalkcustomerservice_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createTicketHeaders := &dingtalkcustomerservice_1_0.CreateTicketHeaders{}
  createTicketHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  properties0 := &dingtalkcustomerservice_1_0.CreateTicketRequestProperties{
    Name: tea.String("question_type"),
    Value: tea.String("requirement"),
  }
  createTicketRequest := &dingtalkcustomerservice_1_0.CreateTicketRequest{
    SourceId: tea.String("AliTest"),
    ForeignId: tea.String("20210001"),
    ForeignName: tea.String("自助单测试用户"),
    OpenInstanceId: tea.String("default"),
    ProductionType: tea.Int32(1),
    TemplateId: tea.String("31904"),
    Title: tea.String("测试自助单"),
    Properties: []*dingtalkcustomerservice_1_0.CreateTicketRequestProperties{properties0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTicketWithOptions(createTicketRequest, createTicketHeaders, &util.RuntimeOptions{})
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
import dingtalkcustomerService_1_0, * as $dingtalkcustomerService_1_0 from '@alicloud/dingtalk/customerService_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcustomerService_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcustomerService_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createTicketHeaders = new $dingtalkcustomerService_1_0.CreateTicketHeaders({ });
    createTicketHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let properties0 = new $dingtalkcustomerService_1_0.CreateTicketRequestProperties({
      name: "question_type",
      value: "requirement",
    });
    let createTicketRequest = new $dingtalkcustomerService_1_0.CreateTicketRequest({
      sourceId: "AliTest",
      foreignId: "20210001",
      foreignName: "自助单测试用户",
      openInstanceId: "default",
      productionType: 1,
      templateId: "31904",
      title: "测试自助单",
      properties: [
        properties0
      ],
    });
    try {
      await client.createTicketWithOptions(createTicketRequest, createTicketHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketHeaders createTicketHeaders = new AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketHeaders();
            createTicketHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketRequest.CreateTicketRequestProperties properties0 = new AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketRequest.CreateTicketRequestProperties
            {
                Name = "question_type",
                Value = "requirement",
            };
            AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketRequest createTicketRequest = new AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketRequest
            {
                SourceId = "AliTest",
                ForeignId = "20210001",
                ForeignName = "自助单测试用户",
                OpenInstanceId = "default",
                ProductionType = 1,
                TemplateId = "31904",
                Title = "测试自助单",
                Properties = new List<AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.CreateTicketRequest.CreateTicketRequestProperties>
                {
                    properties0
                },
            };
            try
            {
                client.CreateTicketWithOptions(createTicketRequest, createTicketHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcustomer_service__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcustomer_service_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcustomer_service_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcustomer_service_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcustomer_service_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketHeaders> createTicketHeaders = make_shared<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketHeaders>();
  createTicketHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketRequestProperties> properties0 = make_shared<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketRequestProperties>(map<string, boost::any>({
    {"name", boost::any(string("question_type"))},
    {"value", boost::any(string("requirement"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketRequest> createTicketRequest = make_shared<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketRequest>(map<string, boost::any>({
    {"sourceId", boost::any(string("AliTest"))},
    {"foreignId", boost::any(string("20210001"))},
    {"foreignName", boost::any(string("自助单测试用户"))},
    {"openInstanceId", boost::any(string("default"))},
    {"productionType", boost::any(1)},
    {"templateId", boost::any(string("31904"))},
    {"title", boost::any(string("测试自助单"))},
    {"properties", boost::any(vector<Alibabacloud_Dingtalkcustomer_service_1_0::CreateTicketRequestProperties>({
      properties0
    }))}
  }));
  try {
    client->createTicketWithOptions(createTicketRequest, createTicketHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| ticketId | String | 新创建的工单ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "ticketId" : "202100001"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | system.error | 系统错误 | 系统错误 |
| 400 | illegal.parameter | 参数错误 | 参数错误 |
