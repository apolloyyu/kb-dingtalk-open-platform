---
title: "查询宜搭表单服务调用执行记录"
source_url: "https://open.dingtalk.com/document/development/the-query-should-be-based-on-the-execution-records-of"
namespace: "development"
slug: "the-query-should-be-based-on-the-execution-records-of"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 服务调用 > 查询宜搭表单服务调用执行记录"
doc_id: "obfOhWqjqO"
updated_at: "2026-06-03 10:11:59"
---

> Source: https://open.dingtalk.com/document/development/the-query-should-be-based-on-the-execution-records-of
> Path: 应用开发 / 服务端 API / 宜搭 > 服务调用 > 查询宜搭表单服务调用执行记录
> Updated: 2026-06-03 10:11:59

# 查询宜搭表单服务调用执行记录

根据宜搭表单Id查询对应的服务调用执行记录信息，包括服务调用状态、服务调用地址和服务调用结果等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/yida/services/invocationRecords |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Yida.Form.Read-宜搭表单数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作人的userId。 |
| hookType | String | 否 | 服务类型，目前只有HTTP服务调用。 |
| systemToken | String | 是 | 宜搭应用密钥。      该参数从宜搭应用中查看。 |
| hookUuid | String | 否 | 本次服务调用的唯一ID，自定义参数。 |
| sourceUuid | String | 否 | 被重试的服务调用唯一ID。      该参数值传某个执行失败的调用服务的唯一ID。 |
| requestUrl | String | 否 | 服务调用地址中包含的部分字符串，用于模糊查询。 |
| success | Boolean | 否 | 服务调用是否成功。   - true：成功 - false：不成功       不传该参数则查询全部。 |
| pageNumber | Integer | 否 | 当前页码，从1开始。 |
| instanceId | String | 是 | 宜搭表单实例Id，调用[获取实例ID列表](0310-api-getinstanceidlist-v2.md)接口或者[获取多个表单实例ID](0324-api-searchformdataidlist-v2.md)接口获取。 |
| invokeAfterDateGMT | String | 否 | 查询调用服务的开始时间。 |
| pageSize | Integer | 否 | 每页最大条目数，最大值100。 |
| invokeStatus | String | 否 | 服务调用状态，可选值：   - SUCCESS：调用成功 - FAIL：调用失败 - FINAL\_SUCCESS：重试后调用成功 - ERROR：调用异常 |
| appType | String | 是 | 宜搭应用编码。      该参数从宜搭应用中查看。 |
| invokeBeforeDateGMT | String | 否 | 查询调用服务的结束时间。 |
| formUuid | String | 是 | 宜搭表单编码。      该参数从宜搭应用中查看。 |

### 请求示例

HTTP

```
GET /v1.0/yida/services/invocationRecords?userId=user001&hookType=HTTP&systemToken=0986xxx&hookUuid=INVOKE-E77xxx&sourceUuid=INVOKE-E7xxx&requestUrl=www.dingtalk.com/query/&success=true&pageNumber=1&instanceId=FINST-Nxxx&invokeAfterDateGMT=2022-03-28 10:10:10&pageSize=100&invokeStatus=SUCCESS&appType=APP_XCxxx&invokeBeforeDateGMT=2022-03-29 10:10:10&formUuid=FORM-GX8xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:063xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkyida_1_0.*;
import com.aliyun.dingtalkyida_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkyida_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkyida_1_0.Client client = Sample.createClient();
        QueryServiceRecordHeaders queryServiceRecordHeaders = new QueryServiceRecordHeaders();
        queryServiceRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryServiceRecordRequest queryServiceRecordRequest = new QueryServiceRecordRequest()
                .setUserId("user001")
                .setHookType("HTTP")
                .setSystemToken("0986xxx")
                .setHookUuid("INVOKE-E77xxx")
                .setSourceUuid("INVOKE-E7xxx")
                .setRequestUrl("www.dingtalk.com/query/")
                .setSuccess(true)
                .setPageNumber(1)
                .setInstanceId("FINST-Nxxx")
                .setInvokeAfterDateGMT("2022-03-28 10:10:10")
                .setPageSize(100)
                .setInvokeStatus("SUCCESS")
                .setAppType("APP_XCxxx")
                .setInvokeBeforeDateGMT("2022-03-29 10:10:10")
                .setFormUuid("FORM-GX8xxx");
        try {
            client.queryServiceRecordWithOptions(queryServiceRecordRequest, queryServiceRecordHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_service_record_headers = dingtalkyida__1__0_models.QueryServiceRecordHeaders()
        query_service_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_service_record_request = dingtalkyida__1__0_models.QueryServiceRecordRequest(
            user_id='user001',
            hook_type='HTTP',
            system_token='0986xxx',
            hook_uuid='INVOKE-E77xxx',
            source_uuid='INVOKE-E7xxx',
            request_url='www.dingtalk.com/query/',
            success=True,
            page_number=1,
            instance_id='FINST-Nxxx',
            invoke_after_date_gmt='2022-03-28 10:10:10',
            page_size=100,
            invoke_status='SUCCESS',
            app_type='APP_XCxxx',
            invoke_before_date_gmt='2022-03-29 10:10:10',
            form_uuid='FORM-GX8xxx'
        )
        try:
            client.query_service_record_with_options(query_service_record_request, query_service_record_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_service_record_headers = dingtalkyida__1__0_models.QueryServiceRecordHeaders()
        query_service_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_service_record_request = dingtalkyida__1__0_models.QueryServiceRecordRequest(
            user_id='user001',
            hook_type='HTTP',
            system_token='0986xxx',
            hook_uuid='INVOKE-E77xxx',
            source_uuid='INVOKE-E7xxx',
            request_url='www.dingtalk.com/query/',
            success=True,
            page_number=1,
            instance_id='FINST-Nxxx',
            invoke_after_date_gmt='2022-03-28 10:10:10',
            page_size=100,
            invoke_status='SUCCESS',
            app_type='APP_XCxxx',
            invoke_before_date_gmt='2022-03-29 10:10:10',
            form_uuid='FORM-GX8xxx'
        )
        try:
            await client.query_service_record_with_options_async(query_service_record_request, query_service_record_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\QueryServiceRecordHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\QueryServiceRecordRequest;
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
        $queryServiceRecordHeaders = new QueryServiceRecordHeaders([]);
        $queryServiceRecordHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryServiceRecordRequest = new QueryServiceRecordRequest([
            "userId" => "user001",
            "hookType" => "HTTP",
            "systemToken" => "0986xxx",
            "hookUuid" => "INVOKE-E77xxx",
            "sourceUuid" => "INVOKE-E7xxx",
            "requestUrl" => "www.dingtalk.com/query/",
            "success" => true,
            "pageNumber" => 1,
            "instanceId" => "FINST-Nxxx",
            "invokeAfterDateGMT" => "2022-03-28 10:10:10",
            "pageSize" => 100,
            "invokeStatus" => "SUCCESS",
            "appType" => "APP_XCxxx",
            "invokeBeforeDateGMT" => "2022-03-29 10:10:10",
            "formUuid" => "FORM-GX8xxx"
        ]);
        try {
            $client->queryServiceRecordWithOptions($queryServiceRecordRequest, $queryServiceRecordHeaders, new RuntimeOptions([]));
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
  dingtalkyida_1_0  "github.com/alibabacloud-go/dingtalk/yida_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkyida_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_1_0.Client{}
  _result, _err = dingtalkyida_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryServiceRecordHeaders := &dingtalkyida_1_0.QueryServiceRecordHeaders{}
  queryServiceRecordHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryServiceRecordRequest := &dingtalkyida_1_0.QueryServiceRecordRequest{
    UserId: tea.String("user001"),
    HookType: tea.String("HTTP"),
    SystemToken: tea.String("0986xxx"),
    HookUuid: tea.String("INVOKE-E77xxx"),
    SourceUuid: tea.String("INVOKE-E7xxx"),
    RequestUrl: tea.String("www.dingtalk.com/query/"),
    Success: tea.Bool(true),
    PageNumber: tea.Int32(1),
    InstanceId: tea.String("FINST-Nxxx"),
    InvokeAfterDateGMT: tea.String("2022-03-28 10:10:10"),
    PageSize: tea.Int32(100),
    InvokeStatus: tea.String("SUCCESS"),
    AppType: tea.String("APP_XCxxx"),
    InvokeBeforeDateGMT: tea.String("2022-03-29 10:10:10"),
    FormUuid: tea.String("FORM-GX8xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryServiceRecordWithOptions(queryServiceRecordRequest, queryServiceRecordHeaders, &util.RuntimeOptions{})
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
import dingtalkyida_1_0, * as $dingtalkyida_1_0 from '@alicloud/dingtalk/yida_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkyida_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkyida_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryServiceRecordHeaders = new $dingtalkyida_1_0.QueryServiceRecordHeaders({ });
    queryServiceRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryServiceRecordRequest = new $dingtalkyida_1_0.QueryServiceRecordRequest({
      userId: "user001",
      hookType: "HTTP",
      systemToken: "0986xxx",
      hookUuid: "INVOKE-E77xxx",
      sourceUuid: "INVOKE-E7xxx",
      requestUrl: "www.dingtalk.com/query/",
      success: true,
      pageNumber: 1,
      instanceId: "FINST-Nxxx",
      invokeAfterDateGMT: "2022-03-28 10:10:10",
      pageSize: 100,
      invokeStatus: "SUCCESS",
      appType: "APP_XCxxx",
      invokeBeforeDateGMT: "2022-03-29 10:10:10",
      formUuid: "FORM-GX8xxx",
    });
    try {
      await client.queryServiceRecordWithOptions(queryServiceRecordRequest, queryServiceRecordHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.QueryServiceRecordHeaders queryServiceRecordHeaders = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.QueryServiceRecordHeaders();
            queryServiceRecordHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.QueryServiceRecordRequest queryServiceRecordRequest = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.QueryServiceRecordRequest
            {
                UserId = "user001",
                HookType = "HTTP",
                SystemToken = "0986xxx",
                HookUuid = "INVOKE-E77xxx",
                SourceUuid = "INVOKE-E7xxx",
                RequestUrl = "www.dingtalk.com/query/",
                Success = true,
                PageNumber = 1,
                InstanceId = "FINST-Nxxx",
                InvokeAfterDateGMT = "2022-03-28 10:10:10",
                PageSize = 100,
                InvokeStatus = "SUCCESS",
                AppType = "APP_XCxxx",
                InvokeBeforeDateGMT = "2022-03-29 10:10:10",
                FormUuid = "FORM-GX8xxx",
            };
            try
            {
                client.QueryServiceRecordWithOptions(queryServiceRecordRequest, queryServiceRecordHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCount | Integer | 总数量。 |
| values | Array | 服务调用记录列表。 |
| serviceContent | String | 宜搭调用目标服务时传的实际参数。 |
| formUuid | String | 表单编码。 |
| sourceUuid | String | 重试的服务调用唯一ID。 |
| invokeStatus | String | 服务调用状态，可选值：   - SUCCESS：调用成功 - FAIL：调用失败 - FINAL\_SUCCESS：重试后调用成功 - ERROR：调用异常 |
| invokeUrl | String | 服务调用地址。 |
| invokeResult | String | 服务调用的返回结果值。 |
| invokeParameter | String | 服务调用的实际入参。 |
| hookUuid | String | 本次服务调用的唯一ID。 |
| formInstanceId | String | 表单实例Id。 |
| serviceParameter | String | 服务调用的实际入参。 |
| serviceName | String | 服务名称。 |
| hookType | String | 服务类型，目前只有HTTP服务调用。 |
| invokeSuccess | String | 服务调用是否成功。   - y：成功 - n：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 100,
  "values" : [ {
    "serviceContent" : "{\"url\":\"https://www.aliwork.com/query/loginFreeFormData/listFormDataByType.json?type=templateCenter&searchFieldJson=%7B%22isShow%22%3A%22y%22%2C%22suggest%22%3A%22%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%22%2C%22industry%22%3A%22%22%2C%22role%22%3A%22%22%2C%22tags%22%3A%22%22%2C%22templateTitle%22%3A%22%22%7D&dynamicOrder=%7B%22orderNum%22%3A%22%2B%22%7D&pageSize=48&currentPage=1\",\"isMd5\":null,\"signature\":\"\",\"isSHA\":null,\"hmacSecret\":\"\",\"type\":\"HttpExt\",\"params\":[{\"field\":\"name\",\"value\":\"name\",\"label\":{\"zh_CN\":\"name\",\"en_US\":\"name\",\"type\":\"i18n\"},\"type\":\"java.lang.String\"}]}",
    "formUuid" : "FORM-GX8xxx",
    "sourceUuid" : "INVOKE-E7xxx",
    "invokeStatus" : "SUCCESS",
    "invokeUrl" : "https://www.aliwork.com/query/loginFreeFormData/listFormDataByType.json?type=templateCenter&searchFieldJson=%7B%22isShow%22%3A%22y%22%2C%22suggest%22%3A%22%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%22%2C%22industry%22%3A%22%22%2C%22role%22%3A%22%22%2C%22tags%22%3A%22%22%2C%22templateTitle%22%3A%22%22%7D&dynamicOrder=%7B%22orderNum%22%3A%22%2B%22%7D&pageSize=48&currentPage=1",
    "invokeResult" : "{\"content\":{\"currentPage\":1,\"data\":[{\"industry_id\":\"互联网\",\"role\":\"人事\",\"textField_kzi3b7ql\":\"场景\",\"textField_kzi3b7qk\":\"角色\",\"description\":\"用于企业员工假期请假、值班、就近办公等信息统计，便于假期工作事项安排。\",\"orderNum\":5,\"industry\":\"互联网\",\"textField_kzi3b7qj\":\"推荐\",\"usageNum_value\":\"3365\",\"textField_kzi3b7qm\":\"能力\",\"scene\":\"企业应用\",\"usageNum\":3365,\"role_id\":\"人事\",\"suggest_id\":\"快速入门\",\"imageUrl\":\"https://tianshu-vpc.oss-cn-shanghai.aliyuncs.com/49315603-3a20-4bd8-aeb0-a1430be3177a.jpg\",\"templateTitle\":\"员工排班表\",\"guide\":\"\",\"orderNum_value\":\"5\",\"author\":\"宜搭官方\",\"appTplUuid\":\"TPL_RAOW06MPQBKKNENFMD5U\",\"textField_kzp6ix74\":\"行业\",\"scene_id\":\"企业应用\",\"suggest\":\"快速入门\",\"tags\":[\"表单\"],\"isShow\":\"显示\",\"isShow_id\":\"y\",\"tags_id\":[\"表单\"]}],\"entities\":null,\"hasMore\":false,\"idCursor\":0,\"totalCount\":7},\"errorCode\":\"\",\"errorExtInfo\":null,\"errorLevel\":\"\",\"errorMsg\":\"\",\"success\":true,\"throwable\":\"\"}",
    "invokeParameter" : "{\"parameter1\":\"测试服务执行\"}",
    "hookUuid" : "INVOKE-E7xxx",
    "formInstanceId" : "FINST-J8xxx",
    "serviceParameter" : "{\"parameter1\":\"测试服务执行\"}",
    "serviceName" : "查询宜搭模板",
    "hookType" : "HTTP",
    "invokeSuccess" : "y"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidState.batchOperation.onlyTheFrontPortionCanBeUpdated | 最多可按当前筛选条件更新前若干条数据，如有超过，请调整筛选条件:%s | 最多可按当前筛选条件更新前若干条数据，如有超过，请调整筛选条件 |
| 400 | invalidState.batchOperation.excelRowCountExceed | excel中行数超过限制:%s | excel中行数超过限制 |
| 400 | invalidState.batchOperation.noDataInExcel | excel中没有数据:%s | excel中没有数据 |
| 400 | invalidState.batchOperation.illegalUpdateValue | 更新值不合法:%s | 更新值不合法 |
| 400 | failure.message.dingTalkMessageError | 钉消息参数或返回结果处理异常:%s | 钉消息参数或返回结果处理异常 |
| 400 | invalidState.batchOperation.duplicateConditionExist | 存在多行相同的过滤条件:%s | 存在多行相同的过滤条件 |
| 400 | failure.batchOperation.sameComponentInConditionAndUpdateTarget | 同一个组件不能同时作为条件和更新值:%s | 同一个组件不能同时作为条件和更新值 |
| 400 | failure.spi.spiLoadError | 系统SPI加载异常:%s | 系统SPI加载异常 |
| 400 | noPermission.submit.deny | 您现在正在预览应用，无法操作提交动作。:%s | 您现在正在预览应用，无法操作提交动作。 |
| 400 | applicationNotExist.application.notExits | 应用不存在:%s | 应用不存在 |
| 400 | failure.masterData.invokeMasterDataFailed | 主数据调用异常:%s | 主数据调用异常 |
| 400 | systemRuntimeException.exception.systemException | 系统运行异常:%s | 系统运行异常 |
| 400 | applicationNotExist.application.applicationNotExits | 应用不存在:%s | 应用不存在 |
| 400 | cacheNotExists.cache.notExists | 缓存类型不存在:%s | 缓存类型不存在 |
| 400 | invalidParameter.applicationName.applicationNameDuplicate | 应用名称已被占用:%s | 应用名称已被占用 |
| 400 | failure.operation.exceptionOccurredInSearch | 搜索异常，请检查查询参数，有问题请通过宜搭官网首页右下角帮助链接联系我们:%s | 搜索异常，请检查查询参数，有问题请通过宜搭官网首页右下角帮助链接联系我们 |
| 400 | failure.operation.processIsBeingRepaired | 正在修复流程，无需重复操作:%s | 正在修复流程，无需重复操作 |
| 400 | invalidState.batchOperation.previousBatchUpdatingIsRunning | 存在正在运行的批量修改，请稍后再试:%s | 存在正在运行的批量修改，请稍后再试 |
| 400 | invalidState.batchOperation.ruleIsInvalid | 批量更新规则中有不存在的组件:%s | 批量更新规则中有不存在的组件 |
| 400 | failure.operation.applicationContainsCrossApplicationDataSource | 操作异常，应用下包含跨应用数据源:%s | 操作异常，应用下包含跨应用数据源 |
| 400 | invalidState.batchOperation.batchUpdateRecordDoesNotExist | 批量更新记录查询不到:%s | 批量更新记录查询不到 |
| 400 | failure.batchOperation.noUpdatingComponentInBatchUpdatingRule | 批量更新规则中未指定更新组件:%s | 批量更新规则中未指定更新组件 |
| 400 | failure.batchOperation.batchUpdatingRuleNeedConditionComponent | 批量更新规则中未指定条件组件:%s | 批量更新规则中未指定条件组件 |
| 400 | invalidParameter.appKey.targetAppKeyInvalid | 目标应用编码非法:%s | 目标应用编码非法 |
| 400 | failure.operation.onlyTemplateAppCanBeCopied | 只能复制模板应用:%s | 只能复制模板应用 |
| 400 | failure.batchOperation.dataAmountToStartProcessExceed | 批量发起流程的数据过多:%s | 批量发起流程的数据过多 |
| 400 | failure.operation.appCopyFail | 应用复制失败:%s | 应用复制失败 |
| 400 | failure.batchOperation.excelDataIsEmpty | 批量发起的excel数据为空:%s | 批量发起的excel数据为空 |
| 400 | invalidState.template.appTemplateNotExist | 应用模板不存在:%s | 应用模板不存在 |
| 400 | failure.batchOperation.canNotFindImportSequence | 找不到导入序列记录:%s | 找不到导入序列记录 |
| 400 | invalidParameter.applicationName.applicationNameTooLong | 名称不能超过150个字符(75个汉字):%s | 名称不能超过150个字符(75个汉字) |
| 400 | failure.operation.failedToRegister | 注册失败:%s | 注册失败 |
| 400 | invalidParameter.name.invalid | 只允许数字，字母，下划线:%s | 只允许数字，字母，下划线 |
| 400 | failure.process.oneTaskPermitOneBackAppend | 相同任务只能进行一次后加签:%s | 相同任务只能进行一次后加签 |
| 400 | noPermission.permission.deny | 没有权限:%s | 没有权限 |
| 400 | failure.task.failedToPerformApproval | 任务审批失败:%s | 任务审批失败 |
| 400 | invalidParameter.parameter.error | 参数错误:%s | 参数错误 |
| 400 | failure.process.failedToCreateProcess | 创建流程失败:%s | 创建流程失败 |
| 400 | fieldTooMuch.field.exceed | 字段超过最大允许数量:%s | 字段超过最大允许数量 |
| 400 | invalidState.process.targetActivityIsIllegal | 非法的跳转节点:%s | 非法的跳转节点 |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | noPermission.process.onlyRunningTasksCanBeAppended | 非运行状态的流程无法加签:%s | 非运行状态的流程无法加签 |
| 400 | invalidParameter.parameter.parameterIsEmpty | 不能为空:%s | 不能为空 |
| 400 | noPermission.process.onlyRunningTasksCanBeRedirected | 非运行状态的流程无法转交:%s | 非运行状态的流程无法转交 |
| 400 | invalidParameter.parameter.accessKeyNotMatch | 接入密钥不匹配:%s | 接入密钥不匹配 |
| 400 | noPermission.process.onlyCurrentApproverCanReturnProcessInstance | 不是流程当前审批人，不能执行退回:%s | 不是流程当前审批人，不能执行退回 |
| 400 | failure.process.failureOfProcessRetry | 流程重试失败:%s | 流程重试失败 |
| 400 | failure.process.canOnlyRetryTheAbnormalProcess | 您只能对异常的流程进行重试:%s | 您只能对异常的流程进行重试 |
| 400 | invalidState.permission.incorrectPermissionType | 权限类型不正确:%s | 权限类型不正确 |
| 400 | failure.operation.fatalSystemError | 系统异常，请联系企业管理员:%s | 系统异常，请联系企业管理员 |
| 400 | failure.operation.lightSystemError | 系统异常，请通过宜搭官网首页右下角帮助链接联系我们:%s | 系统异常，请通过宜搭官网首页右下角帮助链接联系我们 |
| 400 | failure.operation.warn | 提醒:%s | 提醒 |
| 400 | failure.connector.operateFailed | 操作失败:%s | 操作失败 |
| 400 | invalidState.openSearch.failToSaveData | 数据保存失败，组件映射关系找不到:%s | 数据保存失败，组件映射关系找不到 |
| 400 | invalidState.openSearch.invalidFormDataExist | 表单数据有误，请联系应用管理员:%s | 表单数据有误，请联系应用管理员 |
| 400 | invalidState.openSearch.currentFormIsRebuilding | 当前表单重构中，请稍后再试:%s | 当前表单重构中，请稍后再试 |
| 400 | invalidState.openSearch.searchFieldExceed | 该类型支持搜索的字段超过限制:%s | 该类型支持搜索的字段超过限制 |
| 400 | invalidState.openSearch.deficiencyOfMappingForFormField | 表单组件和索引的映射关系不存在:%s | 表单组件和索引的映射关系不存在 |
| 400 | invalidState.openSearch.dataToUpdateNotFound | 更新的高性能检索服务 data数据不存在:%s | 更新的高性能检索服务 data数据不存在 |
| 400 | invalidParameter.process.emptyProcessInstanceIds | processInstanceIds不能为空:%s | processInstanceIds不能为空 |
| 400 | systemRuntimeException.exception.platformKnownException | 宜搭平台发生了异常:%s | 宜搭平台发生了异常 |
| 400 | invalidParameter.parameter.blankDataTitle | 数据标题不能为空，请检查数据标题设置:%s | 数据标题不能为空，请检查数据标题设置 |
| 400 | invalidParameter.number.exceedMax | 超过限制:%s | 超过限制 |
| 400 | invalidParameter.parameter.optionValueOfRadioSelectFieldExceed | 单选和下拉单选组件选项值不能超过255:%s | 单选和下拉单选组件选项值不能超过255 |
| 400 | failure.operation.failedToChangeEncryptionConfiguration | 表单下已存在数据，不允许变更加密配置:%s | 表单下已存在数据，不允许变更加密配置 |
| 400 | failure.operation.formDesignHistoryCanNotBeFound | 表单历史查询不到:%s | 表单历史查询不到 |
| 400 | invalidState.form.incorrectPageSetting | 前页面存在系统配置问题，请联系应用管理员:%s | 前页面存在系统配置问题，请联系应用管理员 |
| 400 | invalidParameter.serviceCallBack.unsupportedServiceInvokeType | 不支持的服务注册类型:%s | 不支持的服务注册类型 |
| 400 | failure.operation.logicServiceFail | 调用逻辑编排服务处理失败:%s | 调用逻辑编排服务处理失败 |
| 400 | failure.serviceCallBack.failedToExecuteService | 执行回调服务失败:%s | 执行回调服务失败 |
| 400 | invalidState.serviceCallBack.serviceDataNotExist | 回调服务不存在:%s | 回调服务不存在 |
| 400 | failure.operation.logicServiceInvokeFail | 调用逻辑编排服务失败:%s | 调用逻辑编排服务失败 |
| 400 | failure.serviceCallBack.failedToInvokeService | 执行回调服务失败:%s | 执行回调服务失败 |
| 400 | invalidParameter.parameter.illegalParameterLength | 长度参数非法:%s | 长度参数非法 |
| 400 | invalidParameter.parameter.exceedLengthLimit | 参数超过了长度限制:%s | 参数超过了长度限制 |
| 400 | failure.data.failedToConstructData | 数据构建失败:%s | 数据构建失败 |
| 400 | invalidState.key.keyCorrespondingToDataAlreadyExists | 数据对应的KEY已存在:%s | 数据对应的KEY已存在 |
| 400 | failure.operation.forbidToReinitializeMappingRelationships | 固定的映射关系不允许重新初始化:%s | 固定的映射关系不允许重新初始化 |
| 400 | failure.resource.dataTypeAccessAmountReachLimit | 数据类型接入数量已满:%s | 数据类型接入数量已满 |
| 400 | invalidState.form.instanceAssociationComponentDoesNotExist | 实例关联组件不存在:%s | 实例关联组件不存在 |
| 400 | failure.form.instanceAssociationComponentNotSupportReceiptData | 单据数据不支持实例关联:%s | 单据数据不支持实例关联 |
| 400 | invalidState.plugin.pluginOutputFieldShouldNotUseExpression | 表单中的某个插件输出字段不允许使用公式:%s | 表单中的某个插件输出字段不允许使用公式 |
| 400 | invalidState.permissionPackage.permissionPackageNotExist | 权限组不存在:%s | 权限组不存在 |
| 400 | invalidState.plugin.invalidFormat | 插件格式有误，请修正:%s | 插件格式有误，请修正 |
| 400 | invalidState.plugin.failedToExecute | 插件执行失败，请检查插件定义或联系管理员:%s | 插件执行失败，请检查插件定义或联系管理员 |
| 400 | invalidState.plugin.mutualDependencyInOutputField | 插件输出字段之间不能互相依赖:%s | 插件输出字段之间不能互相依赖 |
| 400 | invalidParameter.parameter.illegalSerialNumberFieldType | 流水号组件类型非法:%s | 流水号组件类型非法 |
| 400 | invalidParameter.parameter.illegalSerialNumberPrefix | 流水号前缀格式错误:%s | 流水号前缀格式错误 |
| 400 | failure.operation.processingImportSequenceCanNotBeDeleted | 处理中的批次不允许删除:%s | 处理中的批次不允许删除 |
| 400 | failure.operation.processFormCanNotSaveReceiptFormData | 流程表单不能保存单据数据:%s | 流程表单不能保存单据数据 |
| 400 | noPermission.access.accessDeny | 暂无访问权限，应用管理员关闭了「家校通讯录」成员访问，如需访问请联系管理员开启。:%s | 暂无访问权限，应用管理员关闭了「家校通讯录」成员访问，如需访问请联系管理员开启。 |
| 400 | failure.operation.receiptFormCanNotStartInstance | 单据表单不能发起流程:%s | 单据表单不能发起流程 |
| 400 | invalidParameter.parameter.incorrectFormUuid | 指定的表单id有误:%s | 指定的表单id有误 |
| 400 | invalidParameter.parameter.attachmentsAmountExceedTwo | 不可以超过两个附件:%s | 不可以超过两个附件 |
| 400 | invalidState.batchOperation.importSequenceDoesNotExist | 导入批次不存在或已删除:%s | 导入批次不存在或已删除 |
| 400 | failure.operation.uploadFileFail | 文件上传失败:%s | 文件上传失败 |
| 400 | invalidParameter.parameter.invalidFileUrl | 文件地址参数非法:%s | 文件地址参数非法 |
| 400 | invalidState.service.improperServiceResultFormat | 服务返回结果格式不正确:%s | 服务返回结果格式不正确 |
| 400 | failure.encrypt.encryptError | 加密失败:%s | 加密失败 |
| 400 | systemRuntimeException.exception.platformUnknownException | 宜搭平台发生了未知的异常:%s | 宜搭平台发生了未知的异常 |
| 400 | failure.operation.failToSearchApp | 应用查询失败，请联系管理员:%s | 应用查询失败，请联系管理员 |
| 400 | invalidState.authorization.invalidAuthorizationInformation | 无效的认证信息:%s | 无效的认证信息 |
| 400 | failure.operation.tooManyVisitors | 平台当前访问人数过多，请稍后重试:%s | 平台当前访问人数过多，请稍后重试 |
| 400 | invalidState.form.formDataIsBlank | 表单数据不能为空:%s | 表单数据不能为空 |
| 400 | failure.operation.dataAmountToBeClearExceedThreeHundred | 表单数据最多清空300条:%s | 表单数据最多清空300条 |
| 400 | invalidState.form.formWasModified | 表单已变更，请刷新当前页面重新提交:%s | 表单已变更，请刷新当前页面重新提交 |
| 400 | invalidParameter.parameter.tableFieldInTableField | 明细组件下不能含有明细组件:%s | 明细组件下不能含有明细组件 |
| 400 | invalidState.process.nameLengthExceed | 名称过长:%s | 名称过长 |
| 400 | failure.process.redirectProcessFailure | 流程实例跳转失败:%s | 流程实例跳转失败 |
| 400 | invalidState.process.circularProcessInvocationExist | 存在环路调用流程:%s | 存在环路调用流程 |
| 400 | invalidState.form.variablesExceedFive | 表单内置变量不能超过5个:%s | 表单内置变量不能超过5个 |
| 400 | failure.operation.forbidToDeleteEnabledProcess | 已启用的流程不允许删除:%s | 已启用的流程不允许删除 |
| 400 | invalidState.process.invalidFormEvent | 异常的流程事件绑定关系，请为流程正确配置触发事件:%s | 异常的流程事件绑定关系，请为流程正确配置触发事件 |
| 400 | invalidState.process.noAppropriateFormIsBoundToOriginalProcess | 原流程不存在表单绑定关系:%s | 原流程不存在表单绑定关系 |
| 400 | invalidState.process.processHasBeenEnabledOrDisabled | 流程已启用或者已禁用:%s | 流程已启用或者已禁用 |
| 400 | invalidState.process.processDefinitionNotExist | 原流程定义不存在:%s | 原流程定义不存在 |
| 400 | invalidState.form.correspondingFormIsDeleted | 对应表单已删除，请联系应用管理员:%s | 对应表单已删除，请联系应用管理员 |
| 400 | invalidState.process.processRequireAppropriateEvent | 流程未正确绑定触发事件:%s | 流程未正确绑定触发事件 |
| 400 | invalidState.form.targetFormIsDeleted | 跳转的目标表单已删除:%s | 跳转的目标表单已删除 |
| 400 | invalidState.form.componentIsDeleted | 组件已被删除:%s | 组件已被删除 |
| 400 | invalidParameter.validation.parameterValidationFailed | 参数校验失败:%s | 参数校验失败 |
| 400 | invalidState.mapping.mappingTypeNotMatchFieldType | 字段类型与映射类型不匹配:%s | 字段类型与映射类型不匹配 |
| 400 | invalidState.dataLinkage.dataSourceFieldNotSupportSearch | 数据联动配置错误，数据来源字段未支持搜索，请在“数据管理”进行配置:%s | 数据联动配置错误，数据来源字段未支持搜索，请在“数据管理”进行配置 |
| 400 | invalidState.mapping.noMappingRelationship | 不存在映射关系:%s | 不存在映射关系 |
| 400 | failure.operation.onlyReceiptDataCanBeCleared | 只有单据表单才允许清空数据:%s | 只有单据表单才允许清空数据 |
| 400 | invalidState.dataLinkage.filterFieldNotSupportSearch | 数据联动配置错误，过滤字段未支持搜索，请在“数据管理”进行配置:%s | 数据联动配置错误，过滤字段未支持搜索，请在“数据管理”进行配置 |
| 400 | failure.operation.onlyReceiptDataCanBeDeletedInBatches | 只能批量删除单据数据:%s | 只能批量删除单据数据 |
| 400 | invalidState.associationForm.incorrectAssociationDataSetting | 关联其他表单数据配置错误，数据来源字段未支持搜索，请在“数据管理”进行配置:%s | 关联其他表单数据配置错误，数据来源字段未支持搜索，请在“数据管理”进行配置 |
| 400 | invalidState.instance.instanceDataHasBeenModified | 实例数据已修改，请刷新当前页面:%s | 实例数据已修改，请刷新当前页面 |
| 400 | invalidState.instance.instanceStatusHasChanged | 实例状态已变更，请刷新当前页面:%s | 实例状态已变更，请刷新当前页面 |
| 400 | invalidParameter.parameter.expectDoubleButNonNumeric | DOUBLE类型非数字:%s | DOUBLE类型非数字 |
| 400 | invalidParameter.corporation.invalidAuthorizationCorporationId | 不是合法的授权组织:%s | 不是合法的授权组织 |
| 400 | invalidParameter.parameter.typeOfArrayItemCanNotBeString | ARRAY类型不允许为String:%s | ARRAY类型不允许为String |
| 400 | invalidParameter.metaKey.invalidMetaKey | 非法的元数据关键词:%s | 非法的元数据关键词 |
| 400 | invalidParameter.parameter.arrayLengthExceed | ARRAY类型超长:%s | ARRAY类型超长 |
| 400 | failure.operation.currentEditionCanOnlyCreateApp | 当前版本能创建的应用个数已达您企业内应用数量上限:%s | 当前版本能创建的应用个数已达您企业内应用数量上限 |
| 400 | invalidParameter.parameter.doubleTypeLengthExceed | DOUBLE类型超长:%s | DOUBLE类型超长 |
| 400 | failure.operation.requestTooFast | 请求过于频繁，请稍后重试:%s | 请求过于频繁，请稍后重试 |
| 400 | invalidState.form.dataDoesNotExistOrIsDeleted | 数据不存在或已删除:%s | 数据不存在或已删除 |
| 400 | failure.operation.environmentDoesNotSupport | 所在环境不支持当前操作:%s | 所在环境不支持当前操作 |
| 400 | failure.form.canNotPaasSubmissionRulesCheck | 不满足提交规则:%s | 不满足提交规则 |
| 400 | failure.form.dataAmountExceedFiveThousand | 数据量过大，不能超过5000条:%s | 数据量过大，不能超过5000条 |
| 400 | noPermission.access.illegalIp | 非法的IP地址访问:%s | 非法的IP地址访问 |
| 400 | resourceCapacity.resource.resourceReachedLimit | 宜搭资源校验失败:%s | 宜搭资源校验失败 |
| 400 | invalidState.instance.formStatusChanged | 实例状态已变更，请刷新后再试:%s | 实例状态已变更，请刷新后再试 |
| 400 | failure.operation.applicationKeyIsSensitiveInformation | 应用密钥为敏感信息， 请联系应用主管理员获取:%s | 应用密钥为敏感信息， 请联系应用主管理员获取 |
| 400 | invalidState.file.failedToUploadSchema | 上传到内容分发服务器失败:%s | 上传到内容分发服务器失败 |
| 400 | invalidState.form.formNotExist | 表单不存在:%s | 表单不存在 |
| 400 | invalidState.form.invalidFormData | 表单校验失败:%s | 表单校验失败 |
| 400 | invalidState.form.invalidPageStatus | 表单状态错误:%s | 表单状态错误 |
| 400 | noPermission.form.systemNavigationCanNotDelete | 系统导航不允许删除:%s | 系统导航不允许删除 |
| 400 | invalidState.form.pageNotFound | 页面不存在:%s | 页面不存在 |
| 400 | failure.operation.saasApplicationNotFound | 无法找到应用，请核对应用信息:%s | 无法找到应用，请核对应用信息 |
| 400 | failure.service.failedToInvokeFileService | 调用文件服务失败:%s | 调用文件服务失败 |
| 400 | failure.operation.incorrectMessageState | 消息状态异常下执行操作:%s | 消息状态异常下执行操作 |
| 400 | failure.service.failedToInvokeHsf | 调用宜搭HSF接口失败:%s | 调用宜搭HSF接口失败 |
| 400 | invalidState.service.argumentsTypeNotFount | 找不到调用宜搭HSF接口的参数类型:%s | 找不到调用宜搭HSF接口的参数类型 |
| 400 | failure.message.failedToSendMessage | 消息发送失败:%s | 消息发送失败 |
| 400 | invalidState.message.orderedMessageQueueWithoutShardingKey | 顺序消息未指定shardingKey:%s | 顺序消息未指定shardingKey |
| 400 | invalidState.account.accountNotAuthorized | 您所使用的账号未被授权，请联系您所在企业的宜搭平台管理员进行账号授权后继续使用:%s | 您所使用的账号未被授权，请联系您所在企业的宜搭平台管理员进行账号授权后继续使用 |
| 400 | invalidState.account.trialAccountAttachmentCapacityExceed | 试用版宜搭账号上传附件容量已超额， 请在钉钉购买宜搭正式版本后继续使用:%s | 试用版宜搭账号上传附件容量已超额， 请在钉钉购买宜搭正式版本后继续使用 |
| 400 | invalidState.account.trialAccountSubmissionRecordExceed | 试用版宜搭账号提交记录已超额， 请在钉钉购买宜搭正式版本后继续使用:%s | 试用版宜搭账号提交记录已超额， 请在钉钉购买宜搭正式版本后继续使用 |
| 400 | invalidState.processConfig.processConfigIsWrong | 流程配置错误，请联系流程管理员:%s | 流程配置错误，请联系流程管理员 |
| 400 | invalidParameter.publicAccount.publicAccountNotSupport | 暂不支持公共账号登录:%s | 暂不支持公共账号登录 |
| 400 | invalidState.mobileVerificationCode.codeIsAbnormal | 发送验证码异常， 请检查手机号码是否正确:%s | 发送验证码异常， 请检查手机号码是否正确 |
| 400 | invalidParameter.phoneNumber.numberIsBlank | 手机号码不能为空:%s | 手机号码不能为空 |
| 400 | invalidState.mobileVerificationCode.codeIncorrect | 手机验证码有误， 请重新输入:%s | 手机验证码有误， 请重新输入 |
| 400 | invalidState.mobileVerificationCode.codeExpired | 手机验证码已经失效， 请重新发送:%s | 手机验证码已经失效， 请重新发送 |
| 400 | failure.operation.registrationPasswordDoesNotMatchRules | 注册密码不符合规则:%s | 注册密码不符合规则 |
| 400 | invalidState.template.templateNameAlreadyExists | 模板名称已存在:%s | 模板名称已存在 |
| 400 | invalidState.form.failedToDeleteNavigationWithPage | 不允许删除包含有页面的导航:%s | 不允许删除包含有页面的导航 |
| 400 | invalidState.template.templateIsEmpty | 模板内容不能为空:%s | 模板内容不能为空 |
| 400 | failure.operation.operationDeniedDuringThePublishPeriod | 表单发布中，不能进行其他操作:%s | 表单发布中，不能进行其他操作 |
| 400 | failure.form.pageChanged | 页面已变更，请更新后再修改并重新保存:%s | 页面已变更，请更新后再修改并重新保存 |
| 400 | failure.operation.snapshotForAppPublishIsNotAllowedToDelete | 发布版本快照不允许删除:%s | 发布版本快照不允许删除 |
| 400 | invalidState.form.processContainsRunningInstances | 流程存在运行中的实例不能删除:%s | 流程存在运行中的实例不能删除 |
| 400 | failure.operation.operationDeniedDuringTheRollbackPeriod | 数据回滚进行中，不能进行其他操作:%s | 数据回滚进行中，不能进行其他操作 |
| 400 | invalidState.form.emptyPage | 页面内容不能为空:%s | 页面内容不能为空 |
| 400 | invalidState.template.templateDoesNotExist | 模板不存在:%s | 模板不存在 |
| 400 | invalidState.form.duplicateComponentID | 组件ID不允许重复:%s | 组件ID不允许重复 |
| 400 | invalidState.process.expectOnlyOneTask | 该实例下必须有且只有一个宜搭平台任务:%s | 该实例下必须有且只有一个宜搭平台任务 |
| 400 | invalidParameter.task.onlyPlatformTaskCanBeExecuted | 只能执行宜搭平台任务:%s | 只能执行宜搭平台任务 |
| 400 | invalidParameter.task.unsupportedOutResultType | 不支持的任务执行动作:%s | 不支持的任务执行动作 |
| 400 | invalidParameter.form.invalidArgumentsForSearchingEmployeeField | 搜人员组件值参数有误:%s | 搜人员组件值参数有误 |
| 400 | failure.operation.uploadAttachmentCapacityExceed | 上传附件容量超额， 请在钉钉购买后继续上传:%s | 上传附件容量超额， 请在钉钉购买后继续上传 |
| 400 | failure.operation.theSubmissionRecordExceed | 提交记录已超额， 请在钉钉购买后继续提交:%s | 提交记录已超额， 请在钉钉购买后继续提交 |
| 400 | failure.operation.registerError | 注册失败:%s | 注册失败 |
| 400 | failure.operation.operatingFrequencyTooFast | 操作频率过快，请稍后重试:%s | 操作频率过快，请稍后重试 |
| 400 | invalidState.application.invalidApplicationSetting | 应用配置错误，请联系管理员:%s | 应用配置错误，请联系管理员 |
| 400 | failure.operation.failedToSearchEmployeeFieldValues | 查不到人:%s | 查不到人 |
| 400 | failure.operation.fileSizeTooBig | 附件预览暂不支持大小超过20M的文件，请下载后查看:%s | 附件预览暂不支持大小超过20M的文件，请下载后查看 |
| 400 | invalidParameter.parameter.invalidUrl | 请求地址非法:%s | 请求地址非法 |
| 400 | invalidData.data.dataIsInvalid | 数据非法:%s | 数据非法 |
| 400 | invalidState.form.invalidComponentID | 组件ID不合法:%s | 组件ID不合法 |
| 400 | invalidState.form.bindingOfFormAndOtherProcessesAlreadyExist | 页面与其他流程已有绑定关系:%s | 页面与其他流程已有绑定关系 |
| 400 | failure.operation.canNotModify | 封网期间，不允许执行该操作:%s | 封网期间，不允许执行该操作 |
| 400 | invalidState.form.componentActingAsApprovalConditionNotFilled | 已作为条件审批的组件必须必填(包含已失效条件):%s | 已作为条件审批的组件必须必填(包含已失效条件) |
| 400 | noPermission.form.deleteApprovalConditionComponentsWasNotAllowed | 不允许删除作为条件审批的组件(包含已失效条件):%s | 不允许删除作为条件审批的组件(包含已失效条件) |
| 400 | invalidState.form.relationBetweenFormAndTheProcessDoesNotExist | 页面与流程的关联关系不存在:%s | 页面与流程的关联关系不存在 |
| 400 | invalidState.form.pageInstanceNotFound | 未找到页面实例:%s | 未找到页面实例 |
| 400 | invalidState.form.publishedPageNotFound | 未找到已上线的页面:%s | 未找到已上线的页面 |
| 400 | invalidState.openSearch.cursorExceedFiveThousand | 搜索接口翻页不能超过5000，请细化过滤条件缩小查询范围:%s | 搜索接口翻页不能超过5000，请细化过滤条件缩小查询范围 |
| 400 | failure.openSearch.preciseSearchNonsupportMultipleDistinctKey | 精确搜索不支持多个distinct字段:%s | 精确搜索不支持多个distinct字段 |
| 400 | invalidState.openSearch.numberComponentCanNotSupportNullQuery | 数字组件不支持null查询:%s | 数字组件不支持null查询 |
| 400 | invalidState.openSearch.openSearchQueryFail | 高性能检索服务查询失败:%s | 高性能检索服务查询失败 |
| 400 | invalidState.openSearch.simultaneousFuzzySearchAndPreciseSearch | 精确搜索和模糊搜索无法同时支持:%s | 精确搜索和模糊搜索无法同时支持 |
| 400 | invalidState.openSearch.componentCanNotSupportThisOperatorType | 组件不支持该逻辑操作:%s | 组件不支持该逻辑操作 |
| 400 | failure.operation.numberOfQueryDataExceed | 单次查询超过条数限制:%s | 单次查询超过条数限制 |
| 400 | invalidState.openSearch.canNotFindKeyAccordingToComponentFieldId | 找不到高性能检索服务上对应的key:%s | 找不到高性能检索服务上对应的key |
| 400 | failure.message.sendYidaInnerMessageError | 宜搭内部消息发送失败:%s | 宜搭内部消息发送失败 |
| 400 | invalidState.openSearch.notSupportDataLinkageAndAssociationForm | 数据联动和关联其他表单数据 不支持用高性能检索服务替换mysql:%s | 数据联动和关联其他表单数据 不支持用高性能检索服务替换mysql |
| 400 | invalidParameter.json.componentValuesEmptyInSearchFieldJson | searchFieldJson所有组件值都为空:%s | searchFieldJson所有组件值都为空 |
| 400 | failure.expression.expressionEvaluateFail | 公式执行失败:%s | 公式执行失败 |
| 400 | failure.user.userNotExist | 用户不存在:%s | 用户不存在 |
| 400 | failure.address.addressDoesNotExist | 请求地址不存在:%s | 请求地址不存在 |
| 400 | invalidState.administrator.tooManyAdministrators | 管理员过多:%s | 管理员过多 |
| 400 | invalidParameter.corp.corpNotExist | 企业不存在:%s | 企业不存在 |
| 400 | failure.operation.applicationNameNotCorrect | 应用名称不匹配，无法删除:%s | 应用名称不匹配，无法删除 |
| 400 | failure.batchOperation.batchDeletingSequenceIsPerforming | 当前表单有正在删除的批次，请等待完成后再重试:%s | 当前表单有正在删除的批次，请等待完成后再重试 |
| 400 | failure.batchOperation.currentFormIsExecutingBatchDeleting | 当前表单正在执行批量删除操作，请稍后再试:%s | 当前表单正在执行批量删除操作，请稍后再试 |
| 400 | invalidState.batchOperation.runningImportTaskExceedLimit | 存在的运行中的导入任务超过上限:%s | 存在的运行中的导入任务超过上限 |
| 400 | invalidState.batchOperation.dataNeedNotToBeUpdate | 没有符合条件的数据需要更新:%s | 没有符合条件的数据需要更新 |
| 500 | unclassifiedError | 宜搭未分类的异常信息:%s | 宜搭未分类的异常信息 |
| 500 | failure.businessError.unclassifiedError | 宜搭未分类的错误信息:%s | 宜搭未分类的错误信息 |
| 500 | failure.businessError.unclassifiedException | 宜搭未分类的错误信息:%s | 宜搭未分类的错误信息 |
| 500 | failure.businessError.businessException | 宜搭未分类的业务异常信息:%s | 宜搭未分类的业务异常信息 |
| 500 | innerError | 宜搭服务内部异常信息:%s | 宜搭服务内部异常信息 |
