---
title: "分页查询工单"
source_url: "https://open.dingtalk.com/document/development/intelligent-customer-service-paging-query-work-order"
namespace: "development"
slug: "intelligent-customer-service-paging-query-work-order"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 智能客服 > 分页查询工单"
doc_id: "7i9CDUjr9d"
updated_at: "2026-01-29 14:03:51"
---

> Source: https://open.dingtalk.com/document/development/intelligent-customer-service-paging-query-work-order
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 智能客服 > 分页查询工单
> Updated: 2026-01-29 14:03:51

# 分页查询工单

通过此接口可分页查询工单记录，支持按模板、状态、时间范围等条件筛选，适用于客服系统中查看用户提交的工单数据，便于实现工单列表展示、历史记录追溯和分页浏览等功能。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/customerService/tickets |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_customer\_service\_ticket\_read-客服行业的工单读接口权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openInstanceId | String | 否 | 实例ID。 |
| productionType | Integer | 否 | 智能客服产品类型：   - **1**：智能客服 - **2**：服务群 - **1003**：服务台 - **1004**：小蜜客服 |
| templateId | String | 是 | 工单模板ID。 |
| ticketId | String | 否 | 工单ID。 |
| sourceId | String | 否 | 会员来源，取`diamond`配置的值。  **[!NOTE]**     - 必须与`foreignId`参数配合使用。 - 两者需同时为空或同时非空。 |
| foreignId | String | 否 | 第三方用户userid。  **[!NOTE]**     - 必须与 sourceId 参数配合使用。 - 两者需同时为空或同时非空。 |
| ticketStatus | String | 否 | 工单状态。  **[!NOTE]**    在钉钉工单类型配置里的工单状态机里自主配置。 |
| startTime | Long | 否 | 开始时间，时间戳，单位毫秒。 |
| endTime | Long | 否 | 结束时间，时间戳，单位毫秒。 |
| nextToken | String | 是 | 查询数据的起始位置，0表示从头开始。 |
| maxResults | Integer | 是 | 查询单页查询的最大条目数，最大值为100。 |

### 请求示例

HTTP

```
GET /v1.0/customerService/tickets?openInstanceId=default&productionType=1&templateId=42&ticketId=2050000012047051&sourceId=4d75dd75-f2bd-4621-b93f-4c317f137cf2&foreignId=202101&ticketStatus=1&startTime=1619507898000&endTime=1622188240376&nextToken=0&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:11111111
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
    public static com.aliyun.dingtalkcustomer_service_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcustomer_service_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcustomer_service_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcustomer_service_1_0.models.PageListTicketHeaders pageListTicketHeaders = new com.aliyun.dingtalkcustomer_service_1_0.models.PageListTicketHeaders();
        pageListTicketHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcustomer_service_1_0.models.PageListTicketRequest pageListTicketRequest = new com.aliyun.dingtalkcustomer_service_1_0.models.PageListTicketRequest()
                .setOpenInstanceId("default")
                .setProductionType(1)
                .setTemplateId("42")
                .setTicketId("2050000012047051")
                .setSourceId("4d75dd75-f2bd-4621-b93f-4c317f137cf2")
                .setForeignId("202101")
                .setTicketStatus("1")
                .setStartTime(1619507898000L)
                .setEndTime(1622188240376L)
                .setNextToken("0")
                .setMaxResults(10);
        try {
            client.pageListTicketWithOptions(pageListTicketRequest, pageListTicketHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        page_list_ticket_headers = dingtalkcustomer_service__1__0_models.PageListTicketHeaders()
        page_list_ticket_headers.x_acs_dingtalk_access_token = '<your access token>'
        page_list_ticket_request = dingtalkcustomer_service__1__0_models.PageListTicketRequest(
            open_instance_id='default',
            production_type=1,
            template_id='42',
            ticket_id='2050000012047051',
            source_id='4d75dd75-f2bd-4621-b93f-4c317f137cf2',
            foreign_id='202101',
            ticket_status='1',
            start_time=1619507898000,
            end_time=1622188240376,
            next_token='0',
            max_results=10
        )
        try:
            client.page_list_ticket_with_options(page_list_ticket_request, page_list_ticket_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        page_list_ticket_headers = dingtalkcustomer_service__1__0_models.PageListTicketHeaders()
        page_list_ticket_headers.x_acs_dingtalk_access_token = '<your access token>'
        page_list_ticket_request = dingtalkcustomer_service__1__0_models.PageListTicketRequest(
            open_instance_id='default',
            production_type=1,
            template_id='42',
            ticket_id='2050000012047051',
            source_id='4d75dd75-f2bd-4621-b93f-4c317f137cf2',
            foreign_id='202101',
            ticket_status='1',
            start_time=1619507898000,
            end_time=1622188240376,
            next_token='0',
            max_results=10
        )
        try:
            await client.page_list_ticket_with_options_async(page_list_ticket_request, page_list_ticket_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcustomer_service_1_0\Models\PageListTicketHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcustomer_service_1_0\Models\PageListTicketRequest;
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
        $pageListTicketHeaders = new PageListTicketHeaders([]);
        $pageListTicketHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pageListTicketRequest = new PageListTicketRequest([
            "openInstanceId" => "default",
            "productionType" => 1,
            "templateId" => "42",
            "ticketId" => "2050000012047051",
            "sourceId" => "4d75dd75-f2bd-4621-b93f-4c317f137cf2",
            "foreignId" => "202101",
            "ticketStatus" => "1",
            "startTime" => 1619507898000,
            "endTime" => 1622188240376,
            "nextToken" => "0",
            "maxResults" => 10
        ]);
        try {
            $client->pageListTicketWithOptions($pageListTicketRequest, $pageListTicketHeaders, new RuntimeOptions([]));
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
  dingtalkcustomerservice_1_0  "github.com/alibabacloud-go/dingtalk/customerService_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  pageListTicketHeaders := &dingtalkcustomerservice_1_0.PageListTicketHeaders{}
  pageListTicketHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pageListTicketRequest := &dingtalkcustomerservice_1_0.PageListTicketRequest{
    OpenInstanceId: tea.String("default"),
    ProductionType: tea.Int32(1),
    TemplateId: tea.String("42"),
    TicketId: tea.String("2050000012047051"),
    SourceId: tea.String("4d75dd75-f2bd-4621-b93f-4c317f137cf2"),
    ForeignId: tea.String("202101"),
    TicketStatus: tea.String("1"),
    StartTime: tea.Int64(1619507898000),
    EndTime: tea.Int64(1622188240376),
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PageListTicketWithOptions(pageListTicketRequest, pageListTicketHeaders, &util.RuntimeOptions{})
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
    let pageListTicketHeaders = new $dingtalkcustomerService_1_0.PageListTicketHeaders({ });
    pageListTicketHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let pageListTicketRequest = new $dingtalkcustomerService_1_0.PageListTicketRequest({
      openInstanceId: "default",
      productionType: 1,
      templateId: "42",
      ticketId: "2050000012047051",
      sourceId: "4d75dd75-f2bd-4621-b93f-4c317f137cf2",
      foreignId: "202101",
      ticketStatus: "1",
      startTime: 1619507898000,
      endTime: 1622188240376,
      nextToken: "0",
      maxResults: 10,
    });
    try {
      await client.pageListTicketWithOptions(pageListTicketRequest, pageListTicketHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.PageListTicketHeaders pageListTicketHeaders = new AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.PageListTicketHeaders();
            pageListTicketHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.PageListTicketRequest pageListTicketRequest = new AlibabaCloud.SDK.Dingtalkcustomer_service_1_0.Models.PageListTicketRequest
            {
                OpenInstanceId = "default",
                ProductionType = 1,
                TemplateId = "42",
                TicketId = "2050000012047051",
                SourceId = "4d75dd75-f2bd-4621-b93f-4c317f137cf2",
                ForeignId = "202101",
                TicketStatus = "1",
                StartTime = 1619507898000,
                EndTime = 1622188240376,
                NextToken = "0",
                MaxResults = 10,
            };
            try
            {
                client.PageListTicketWithOptions(pageListTicketRequest, pageListTicketHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextCursor | Long | 是否还有下一页数据。 |
| total | Long | 总记录数。 |
| list | Array | 查询结果。 |
| foreignId | String | 第三方会员。  **[!NOTE]**    如果系统中不存在需要在CRM中新建。 |
| sourceId | String | 第三方来源。 |
| foreignName | String | 第三方会员名。 |
| templateId | String | 工单模板ID。 |
| title | String | 工单标题。 |
| ticketId | String | 工单ID。 |
| ticketStatus | String | 工单状态。  **[!NOTE]**    在钉钉工单类型配置里的工单状态机里自主配置。 |
| openInstanceId | String | 实例ID。 |
| productionType | Integer | 智能客服产品类型：   - **1**：智能客服 - **2**：服务群 - **1003**：服务台 - **1004**：小蜜客服 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 最新修改时间。 |
| bizDataMap | Map | 工单自定义业务字段信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextCursor" : 10,
  "total" : 20,
  "list" : [ {
    "foreignId" : "2021001",
    "sourceId" : "4d754621-b93f-4c317f137cf2",
    "foreignName" : "测试",
    "templateId" : "42",
    "title" : "测试自助单",
    "ticketId" : "20523423447180",
    "ticketStatus" : "受理中",
    "openInstanceId" : "default",
    "productionType" : 1,
    "gmtCreate" : "2021-05-21T14:57Z",
    "gmtModified" : "2021-05-21T14:57Z"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | system.error | 系统错误 | 系统错误 |
| 400 | illegal.parameter | 参数错误 | 参数错误 |
