---
title: "获取单个数据表单实例详情"
source_url: "https://open.dingtalk.com/document/development/obtain-details-of-a-single-data-form-instance"
namespace: "development"
slug: "obtain-details-of-a-single-data-form-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 获取单个数据表单实例详情"
doc_id: "F6TbhSuFme"
updated_at: "2026-06-03 10:13:06"
---

> Source: https://open.dingtalk.com/document/development/obtain-details-of-a-single-data-form-instance
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 获取单个数据表单实例详情
> Updated: 2026-06-03 10:13:06

# 获取单个数据表单实例详情

调用本接口，根据实例ID获取单个数据表单实例详情，包括表单提交时间、表单实例ID、提交人姓名、表单实例详情数据等信息。

## **接口调用说明**

当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances |
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
| formInstanceId | String | 是 | 数据表单实例ID。 |
| formCode | String | 是 | 数据表单模板ID，通过[OA审批概述-名词解释](0473-workflow-overview.md)获取。 |
| appUuid | String | 否 | 应用搭建ID，默认为企业corpId。在**钉钉管理后台**—**应用管理**—应用编辑页的URL中查看。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/premium/dataForms/formInstances?formInstanceId=951a8-8828-430c-b3e-example&formCode=PROC-abcdef-example&appUuid=SWAPP-dfeacds-example HTTP/1.1
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
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstanceHeaders premiumGetFormInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstanceHeaders();
        premiumGetFormInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstanceRequest premiumGetFormInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetFormInstanceRequest()
                .setFormInstanceId("951a8-8828-430c-b3e-example")
                .setFormCode("PROC-abcdef-example")
                .setAppUuid("SWAPP-dfeacds-example");
        try {
            client.premiumGetFormInstanceWithOptions(premiumGetFormInstanceRequest, premiumGetFormInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_get_form_instance_headers = dingtalkworkflow__1__0_models.PremiumGetFormInstanceHeaders()
        premium_get_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_form_instance_request = dingtalkworkflow__1__0_models.PremiumGetFormInstanceRequest(
            form_instance_id='951a8-8828-430c-b3e-example',
            form_code='PROC-abcdef-example',
            app_uuid='SWAPP-dfeacds-example'
        )
        try:
            client.premium_get_form_instance_with_options(premium_get_form_instance_request, premium_get_form_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_get_form_instance_headers = dingtalkworkflow__1__0_models.PremiumGetFormInstanceHeaders()
        premium_get_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_form_instance_request = dingtalkworkflow__1__0_models.PremiumGetFormInstanceRequest(
            form_instance_id='951a8-8828-430c-b3e-example',
            form_code='PROC-abcdef-example',
            app_uuid='SWAPP-dfeacds-example'
        )
        try:
            await client.premium_get_form_instance_with_options_async(premium_get_form_instance_request, premium_get_form_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetFormInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetFormInstanceRequest;
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
        $premiumGetFormInstanceHeaders = new PremiumGetFormInstanceHeaders([]);
        $premiumGetFormInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumGetFormInstanceRequest = new PremiumGetFormInstanceRequest([
            "formInstanceId" => "951a8-8828-430c-b3e-example",
            "formCode" => "PROC-abcdef-example",
            "appUuid" => "SWAPP-dfeacds-example"
        ]);
        try {
            $client->premiumGetFormInstanceWithOptions($premiumGetFormInstanceRequest, $premiumGetFormInstanceHeaders, new RuntimeOptions([]));
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

  premiumGetFormInstanceHeaders := &dingtalkworkflow_1_0.PremiumGetFormInstanceHeaders{}
  premiumGetFormInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumGetFormInstanceRequest := &dingtalkworkflow_1_0.PremiumGetFormInstanceRequest{
    FormInstanceId: tea.String("951a8-8828-430c-b3e-example"),
    FormCode: tea.String("PROC-abcdef-example"),
    AppUuid: tea.String("SWAPP-dfeacds-example"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumGetFormInstanceWithOptions(premiumGetFormInstanceRequest, premiumGetFormInstanceHeaders, &util.RuntimeOptions{})
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
    let premiumGetFormInstanceHeaders = new dingtalkworkflow_1_0.PremiumGetFormInstanceHeaders({ });
    premiumGetFormInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumGetFormInstanceRequest = new dingtalkworkflow_1_0.PremiumGetFormInstanceRequest({
      formInstanceId: '951a8-8828-430c-b3e-example',
      formCode: 'PROC-abcdef-example',
      appUuid: 'SWAPP-dfeacds-example',
    });
    try {
      await client.premiumGetFormInstanceWithOptions(premiumGetFormInstanceRequest, premiumGetFormInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstanceHeaders premiumGetFormInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstanceHeaders();
            premiumGetFormInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstanceRequest premiumGetFormInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetFormInstanceRequest
            {
                FormInstanceId = "951a8-8828-430c-b3e-example",
                FormCode = "PROC-abcdef-example",
                AppUuid = "SWAPP-dfeacds-example",
            };
            try
            {
                client.PremiumGetFormInstanceWithOptions(premiumGetFormInstanceRequest, premiumGetFormInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| formInstanceId | String | 实例ID。 |
| formInstDataList | Array | 表单控件数据列表。 |
| componentType | String | 控件类型。 |
| bizAlias | String | 控件别名。 |
| extendValue | String | 表单控件扩展数据。 |
| label | String | 控件名称。 |
| value | String | 控件填写的数据。 |
| key | String | 控件唯一ID。 |
| appUuid | String | 应用搭建ID。 |
| formCode | String | 表单模板ID。 |
| title | String | 表单标题。 |
| creator | String | 创建人。 |
| modifier | String | 修改人。 |
| createTimestamp | Long | 实例创建时间戳。 |
| modifyTimestamp | Long | 实例最近修改时间戳。 |
| outInstanceId | String | 外联业务实例ID。 |
| outBizCode | String | 外联业务code。 |
| attributes | Map | 扩展信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "formInstanceId" : "951a8-8828-430c-b3e-example",
  "formInstDataList" : [ {
    "componentType" : "TextField",
    "bizAlias" : "staff_name",
    "extendValue" : "{\"key\":\"value}",
    "label" : "员工姓名",
    "value" : "张三",
    "key" : "TextField-abcdefg"
  } ],
  "appUuid" : "SWAPP-dfeacds-example",
  "formCode" : "PROC-abcdef-example",
  "title" : "xxx提交的表单数据",
  "creator" : "00003",
  "modifier" : "000025",
  "createTimestamp" : 1631870043000,
  "modifyTimestamp" : 1631870043000,
  "outInstanceId" : "951a8-8828-430c-b3e-example",
  "outBizCode" : "PROC-abcdef-example"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | permission.error | %s | 没有访问权限 |
| 400 | system.error | %s | 系统错误 |
| 400 | instance.query.error | %s | 表单实例查询失败 |
| 400 | param.code.error | %s | 表单模板查询错误 |
| 400 | param.error | %s | 参数错误 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验失败，未开通或过期 |
| 500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 请求过于频繁，稍后重试 |
