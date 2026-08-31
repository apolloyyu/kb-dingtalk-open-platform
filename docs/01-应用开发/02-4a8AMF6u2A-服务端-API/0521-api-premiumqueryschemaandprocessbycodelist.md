---
title: "批量获取表单模板schema（包含表单和流程配置信息）"
source_url: "https://open.dingtalk.com/document/development/api-premiumqueryschemaandprocessbycodelist"
namespace: "development"
slug: "api-premiumqueryschemaandprocessbycodelist"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批表单 > 批量获取表单模板schema（包含表单和流程配置信息）"
doc_id: "lBZGzTMZie"
updated_at: "2026-06-03 10:12:42"
---

> Source: https://open.dingtalk.com/document/development/api-premiumqueryschemaandprocessbycodelist
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批表单 > 批量获取表单模板schema（包含表单和流程配置信息）
> Updated: 2026-06-03 10:12:42

# 批量获取表单模板schema（包含表单和流程配置信息）

调用本接口，根据processCode列表批量获取表单模板schema相关信息（包含表单和流程配置信息）。

## **接口调用说明**

当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processes/schemas/batchQuery |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCodes | Array of String | 是 | 模板code。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processes/schemas/batchQuery HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f31f78b59d9438b9859e40xxxx9882f0
Content-Type:application/json

{
  "processCodes" : [ "Proc-123" ]
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumQuerySchemaAndProcessByCodeListHeaders premiumQuerySchemaAndProcessByCodeListHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumQuerySchemaAndProcessByCodeListHeaders();
        premiumQuerySchemaAndProcessByCodeListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumQuerySchemaAndProcessByCodeListRequest premiumQuerySchemaAndProcessByCodeListRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumQuerySchemaAndProcessByCodeListRequest()
                .setProcessCodes(java.util.Arrays.asList(
                    "Proc-123"
                ));
        try {
            client.premiumQuerySchemaAndProcessByCodeListWithOptions(premiumQuerySchemaAndProcessByCodeListRequest, premiumQuerySchemaAndProcessByCodeListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_query_schema_and_process_by_code_list_headers = dingtalkworkflow__1__0_models.PremiumQuerySchemaAndProcessByCodeListHeaders()
        premium_query_schema_and_process_by_code_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_query_schema_and_process_by_code_list_request = dingtalkworkflow__1__0_models.PremiumQuerySchemaAndProcessByCodeListRequest(
            process_codes=[
                'Proc-123'
            ]
        )
        try:
            client.premium_query_schema_and_process_by_code_list_with_options(premium_query_schema_and_process_by_code_list_request, premium_query_schema_and_process_by_code_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_query_schema_and_process_by_code_list_headers = dingtalkworkflow__1__0_models.PremiumQuerySchemaAndProcessByCodeListHeaders()
        premium_query_schema_and_process_by_code_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_query_schema_and_process_by_code_list_request = dingtalkworkflow__1__0_models.PremiumQuerySchemaAndProcessByCodeListRequest(
            process_codes=[
                'Proc-123'
            ]
        )
        try:
            await client.premium_query_schema_and_process_by_code_list_with_options_async(premium_query_schema_and_process_by_code_list_request, premium_query_schema_and_process_by_code_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumQuerySchemaAndProcessByCodeListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumQuerySchemaAndProcessByCodeListRequest;
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
        $premiumQuerySchemaAndProcessByCodeListHeaders = new PremiumQuerySchemaAndProcessByCodeListHeaders([]);
        $premiumQuerySchemaAndProcessByCodeListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumQuerySchemaAndProcessByCodeListRequest = new PremiumQuerySchemaAndProcessByCodeListRequest([
            "processCodes" => [
                "Proc-123"
            ]
        ]);
        try {
            $client->premiumQuerySchemaAndProcessByCodeListWithOptions($premiumQuerySchemaAndProcessByCodeListRequest, $premiumQuerySchemaAndProcessByCodeListHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
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
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  premiumQuerySchemaAndProcessByCodeListHeaders := &dingtalkworkflow_1_0.PremiumQuerySchemaAndProcessByCodeListHeaders{}
  premiumQuerySchemaAndProcessByCodeListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumQuerySchemaAndProcessByCodeListRequest := &dingtalkworkflow_1_0.PremiumQuerySchemaAndProcessByCodeListRequest{
    ProcessCodes: []*string{tea.String("Proc-123")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumQuerySchemaAndProcessByCodeListWithOptions(premiumQuerySchemaAndProcessByCodeListRequest, premiumQuerySchemaAndProcessByCodeListHeaders, &util.RuntimeOptions{})
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
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
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
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let premiumQuerySchemaAndProcessByCodeListHeaders = new dingtalkworkflow_1_0.PremiumQuerySchemaAndProcessByCodeListHeaders({ });
    premiumQuerySchemaAndProcessByCodeListHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumQuerySchemaAndProcessByCodeListRequest = new dingtalkworkflow_1_0.PremiumQuerySchemaAndProcessByCodeListRequest({
      processCodes: [
        'Proc-123'
      ],
    });
    try {
      await client.premiumQuerySchemaAndProcessByCodeListWithOptions(premiumQuerySchemaAndProcessByCodeListRequest, premiumQuerySchemaAndProcessByCodeListHeaders, new Util.RuntimeOptions({ }));
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQuerySchemaAndProcessByCodeListHeaders premiumQuerySchemaAndProcessByCodeListHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQuerySchemaAndProcessByCodeListHeaders();
            premiumQuerySchemaAndProcessByCodeListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQuerySchemaAndProcessByCodeListRequest premiumQuerySchemaAndProcessByCodeListRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumQuerySchemaAndProcessByCodeListRequest
            {
                ProcessCodes = new List<string>
                {
                    "Proc-123"
                },
            };
            try
            {
                client.PremiumQuerySchemaAndProcessByCodeListWithOptions(premiumQuerySchemaAndProcessByCodeListRequest, premiumQuerySchemaAndProcessByCodeListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 返回结果。 |
| processCode | String | 模板code。 |
| formUuid | String | 表单formUuid。 |
| bizCategoryId | String | 模板业务类型标识。 |
| processId | Long | 流程processId。 |
| appUuid | String | 表单应用 uuid 或者 企业corpId。 |
| name | String | 模板名称。 |
| memo | String | 模板描述。 |
| icon | String | 图标icon地址。 |
| status | String | 模板状态：   - PUBLISHED：启用 - INVALID：停用 - SAVED：草稿 |
| creatorUserId | String | 模板创建人的userId。 |
| modifierUserId | String | 模板修改人的userId。 |
| createTime | Long | 模板创建时间。 |
| modifyTime | Long | 模板创建时间。 |
| schemaContent | String | 表单schema内容，json字符串。 |
| processConfig | String | 流程配置schema内容，json字符串。 |
| success | Boolean | 接口请求是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "processCode" : "PROC-17428B8C-6C60-470E-xxxx-64F1037AE067",
    "formUuid" : "FORM-28215C3E-00E3-4118-xxxx-4091F828AF2F",
    "bizCategoryId" : "hrm.xxx",
    "processId" : 123,
    "appUuid" : "ding123",
    "name" : "示例模板",
    "memo" : "模板描述1",
    "icon" : "https//:xxx",
    "status" : "PUBLISHED",
    "creatorUserId" : "userId123",
    "modifierUserId" : "userId123",
    "createTime" : 1638326995000,
    "modifyTime" : 1638326995000,
    "schemaContent" : "{\\\"commentHiddenForProposer\\\":\\\"\\\",\\\"commentRequired\\\":\\\"\\\",\\\"icon\\\":\\\"timefades#red\\\",\\\"commentDescription\\\":\\\"\\\",\\\"description\\\":\\\"支持地址控件\\\",\\\"title\\\":\\\"官方OA审批-POP-2025-0109\\\",\\\"items\\\":[{\\\"componentName\\\":\\\"TimeAndLocationField\\\",\\\"props\\\":{\\\"label\\\":[\\\"当前时间\\\",\\\"当前地点\\\"],\\\"id\\\":\\\"TimeAndLocationField_1CVHM5TIIWR9C\\\",\\\"required\\\":false}},{\\\"componentName\\\":\\\"TextField\\\",\\\"props\\\":{\\\"placeholder\\\":\\\"请输入\\\",\\\"label\\\":\\\"单行输入框\\\",\\\"id\\\":\\\"TextField_17EZKEGSOCTC0\\\",\\\"required\\\":false}}]}",
    "processConfig" : "{\\\"name\\\":\\\"发起人\\\",\\\"type\\\":\\\"start\\\",\\\"nodeId\\\":\\\"sid-startevent\\\",\\\"childNode\\\":{\\\"name\\\":\\\"审批人\\\",\\\"prevId\\\":\\\"sid-startevent\\\",\\\"type\\\":\\\"approver\\\",\\\"nodeId\\\":\\\"sid-1234_5678\\\",\\\"properties\\\":{\\\"activateType\\\":\\\"ONE_BY_ONE\\\",\\\"approvalType\\\":\\\"MANUAL\\\"}}}"
  } ],
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidProcessCode | 审批模板processCode不能为空或超过最大数量限制 | 请检查processCode参数传值是否正确 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 400 | userNotExist | 用户不存在 | 请检查当前用户是否归属于当前组织 |
| 400 | processNotExist | 审批模板不存在 | 请检查processCode参数传值是否正确 |
| 500 | systemError | 系统异常 | 系统异常 |
