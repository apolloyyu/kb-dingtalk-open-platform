---
title: "获取数据表单实例列表"
source_url: "https://open.dingtalk.com/document/development/api-premiumgetforminstances"
namespace: "development"
slug: "api-premiumgetforminstances"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 获取数据表单实例列表"
doc_id: "7Gf9LrGBOz"
updated_at: "2026-06-03 10:13:06"
---

> Source: https://open.dingtalk.com/document/development/api-premiumgetforminstances
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 获取数据表单实例列表
> Updated: 2026-06-03 10:13:06

# 获取数据表单实例列表

调用本接口，根据表单模板code分页获取数据表单实例列表，包括表单提交时间、表单实例ID、提交人姓名、表单实例详情数据等信息。

## **接口调用说明**

当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances/pages |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标，第一次调用传空或者null。 |
| maxResults | Integer | 是 | 分页大小，最大值100。 |
| appUuid | String | 否 | 应用搭建ID，默认为企业corpId。   - 在**钉钉管理后台**—**应用管理**—应用编辑页的URL中查看。 |
| formCode | String | 是 | 数据表单模板ID。   - 通过[OA审批概述-名词解释](0473-workflow-overview.md)获取。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/premium/dataForms/formInstances/pages?nextToken=100010&maxResults=100&appUuid=SWAPP-dacdsa-example&formCode=PROC-daccea-example HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6dexxx
Content-Type:application/json
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
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstancesHeaders premiumGetFormInstancesHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstancesHeaders();
        premiumGetFormInstancesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstancesRequest premiumGetFormInstancesRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstancesRequest()
                .setNextToken("100010")
                .setMaxResults(100)
                .setAppUuid("SWAPP-dacdsa-example")
                .setFormCode("PROC-daccea-example");
        try {
            client.premiumGetFormInstancesWithOptions(premiumGetFormInstancesRequest, premiumGetFormInstancesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_get_form_instances_headers = dingtalkworkflow__1__0_models.PremiumGetFormInstancesHeaders()
        premium_get_form_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_form_instances_request = dingtalkworkflow__1__0_models.PremiumGetFormInstancesRequest(
            next_token='100010',
            max_results=100,
            app_uuid='SWAPP-dacdsa-example',
            form_code='PROC-daccea-example'
        )
        try:
            client.premium_get_form_instances_with_options(premium_get_form_instances_request, premium_get_form_instances_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_get_form_instances_headers = dingtalkworkflow__1__0_models.PremiumGetFormInstancesHeaders()
        premium_get_form_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_form_instances_request = dingtalkworkflow__1__0_models.PremiumGetFormInstancesRequest(
            next_token='100010',
            max_results=100,
            app_uuid='SWAPP-dacdsa-example',
            form_code='PROC-daccea-example'
        )
        try:
            await client.premium_get_form_instances_with_options_async(premium_get_form_instances_request, premium_get_form_instances_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetFormInstancesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetFormInstancesRequest;
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
        $premiumGetFormInstancesHeaders = new PremiumGetFormInstancesHeaders([]);
        $premiumGetFormInstancesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumGetFormInstancesRequest = new PremiumGetFormInstancesRequest([
            "nextToken" => "100010",
            "maxResults" => 100,
            "appUuid" => "SWAPP-dacdsa-example",
            "formCode" => "PROC-daccea-example"
        ]);
        try {
            $client->premiumGetFormInstancesWithOptions($premiumGetFormInstancesRequest, $premiumGetFormInstancesHeaders, new RuntimeOptions([]));
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

  premiumGetFormInstancesHeaders := &dingtalkworkflow_1_0.PremiumGetFormInstancesHeaders{}
  premiumGetFormInstancesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumGetFormInstancesRequest := &dingtalkworkflow_1_0.PremiumGetFormInstancesRequest{
    NextToken: tea.String("100010"),
    MaxResults: tea.Int32(100),
    AppUuid: tea.String("SWAPP-dacdsa-example"),
    FormCode: tea.String("PROC-daccea-example"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumGetFormInstancesWithOptions(premiumGetFormInstancesRequest, premiumGetFormInstancesHeaders, &util.RuntimeOptions{})
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
    let premiumGetFormInstancesHeaders = new dingtalkworkflow_1_0.PremiumGetFormInstancesHeaders({ });
    premiumGetFormInstancesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumGetFormInstancesRequest = new dingtalkworkflow_1_0.PremiumGetFormInstancesRequest({
      nextToken: '100010',
      maxResults: 100,
      appUuid: 'SWAPP-dacdsa-example',
      formCode: 'PROC-daccea-example',
    });
    try {
      await client.premiumGetFormInstancesWithOptions(premiumGetFormInstancesRequest, premiumGetFormInstancesHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstancesHeaders premiumGetFormInstancesHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstancesHeaders();
            premiumGetFormInstancesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstancesRequest premiumGetFormInstancesRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstancesRequest
            {
                NextToken = "100010",
                MaxResults = 100,
                AppUuid = "SWAPP-dacdsa-example",
                FormCode = "PROC-daccea-example",
            };
            try
            {
                client.PremiumGetFormInstancesWithOptions(premiumGetFormInstancesRequest, premiumGetFormInstancesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 分页结果。 |
| nextToken | String | 下一页的游标。 |
| hasMore | Boolean | 是否有更多数据。 |
| maxResults | Long | 分页大小。 |
| values | Array | 实例数据列表。 |
| formInstanceId | String | 表单实例ID。 |
| appUuid | String | 应用搭建ID。 |
| formCode | String | 表单模板code。 |
| title | String | 标题。 |
| creator | String | 创建人。 |
| modifier | String | 修改人。 |
| createTimestamp | Long | 创建时间。 |
| modifyTimestamp | Long | 修改时间。 |
| outInstanceId | String | 外部实例编码。 |
| outBizCode | String | 外部业务编码。 |
| attributes | Map | 扩展信息。 |
| formInstDataList | Array | 表单实例控件数据列表。 |
| componentType | String | 控件类型。 |
| bizAlias | String | 控件别名。 |
| extendValue | String | 表单控件扩展数据。 |
| label | String | 控件名称。 |
| value | String | 控件填写的数据。 |
| key | String | 控件唯一ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "nextToken" : "10",
    "hasMore" : true,
    "maxResults" : 20,
    "values" : [ {
      "formInstanceId" : "abcd-eaf-acde12f",
      "appUuid" : "SWAPP-abcd-example",
      "formCode" : "PROC-abcd-example",
      "title" : "xxx提交的数据",
      "creator" : "30314512",
      "modifier" : "032142312",
      "createTimestamp" : 1635151039000,
      "modifyTimestamp" : 1635151039000,
      "outInstanceId" : "323",
      "outBizCode" : "abcd",
      "formInstDataList" : [ {
        "componentType" : "TextField",
        "bizAlias" : "staff_name",
        "extendValue" : "{\"key\":\"value}",
        "label" : "员工姓名",
        "value" : "张三",
        "key" : "TextField-abcdefg"
      } ]
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | pageSize.invalid | illegal pageSize | 分页大小错误 |
| 400 | pageIndex.invalid | illegal nextToken | 游标错误 |
| 400 | permission.error | no permission | 没有访问权限 |
| 400 | formCode.error | formCode query error | 模板编码查询错误 |
| 400 | system.error | system error | 系统错误 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | instance.query.error | instance query error | 表单实例查询失败 |
| 500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验失败，未开通或过期 |
| 500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 请求过于频繁，稍后重试 |
