---
title: "删除数据表单实例"
source_url: "https://open.dingtalk.com/document/development/api-premiumdeleteforminstance"
namespace: "development"
slug: "api-premiumdeleteforminstance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 删除数据表单实例"
doc_id: "7hDYZO7W3z"
updated_at: "2026-06-03 10:13:05"
---

> Source: https://open.dingtalk.com/document/development/api-premiumdeleteforminstance
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 删除数据表单实例
> Updated: 2026-06-03 10:13:05

# 删除数据表单实例

调用本接口，删除数据表单实例。

## **接口调用说明**

- 本接口仅限以管理员身份调用。
- 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances/remove |
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
| processCode | String | 是 | 数据表单模板code。可在数据表单模板编辑页-基础设置-页面底部查看。 |
| formInstanceIds | Array of String | 否 | 待删除的数据表单实例ID。 |
| userId | String | 否 | 用户userId，仅限以管理员身份调用。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/dataForms/formInstances/remove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6dexxx
Content-Type:application/json

{
  "processCode" : "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
  "formInstanceIds" : [ "abc" ],
  "userId" : "managerUserId1"
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
        com.aliyun.dingtalkworkflow_1_0.models.PremiumDeleteFormInstanceHeaders premiumDeleteFormInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumDeleteFormInstanceHeaders();
        premiumDeleteFormInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumDeleteFormInstanceRequest premiumDeleteFormInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumDeleteFormInstanceRequest()
                .setProcessCode("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1")
                .setFormInstanceIds(java.util.Arrays.asList(
                    "abc"
                ))
                .setUserId("managerUserId1");
        try {
            client.premiumDeleteFormInstanceWithOptions(premiumDeleteFormInstanceRequest, premiumDeleteFormInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_delete_form_instance_headers = dingtalkworkflow__1__0_models.PremiumDeleteFormInstanceHeaders()
        premium_delete_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_delete_form_instance_request = dingtalkworkflow__1__0_models.PremiumDeleteFormInstanceRequest(
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            form_instance_ids=[
                'abc'
            ],
            user_id='managerUserId1'
        )
        try:
            client.premium_delete_form_instance_with_options(premium_delete_form_instance_request, premium_delete_form_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_delete_form_instance_headers = dingtalkworkflow__1__0_models.PremiumDeleteFormInstanceHeaders()
        premium_delete_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_delete_form_instance_request = dingtalkworkflow__1__0_models.PremiumDeleteFormInstanceRequest(
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            form_instance_ids=[
                'abc'
            ],
            user_id='managerUserId1'
        )
        try:
            await client.premium_delete_form_instance_with_options_async(premium_delete_form_instance_request, premium_delete_form_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumDeleteFormInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumDeleteFormInstanceRequest;
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
        $premiumDeleteFormInstanceHeaders = new PremiumDeleteFormInstanceHeaders([]);
        $premiumDeleteFormInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumDeleteFormInstanceRequest = new PremiumDeleteFormInstanceRequest([
            "processCode" => "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
            "formInstanceIds" => [
                "abc"
            ],
            "userId" => "managerUserId1"
        ]);
        try {
            $client->premiumDeleteFormInstanceWithOptions($premiumDeleteFormInstanceRequest, $premiumDeleteFormInstanceHeaders, new RuntimeOptions([]));
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

  premiumDeleteFormInstanceHeaders := &dingtalkworkflow_1_0.PremiumDeleteFormInstanceHeaders{}
  premiumDeleteFormInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumDeleteFormInstanceRequest := &dingtalkworkflow_1_0.PremiumDeleteFormInstanceRequest{
    ProcessCode: tea.String("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1"),
    FormInstanceIds: []*string{tea.String("abc")},
    UserId: tea.String("managerUserId1"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumDeleteFormInstanceWithOptions(premiumDeleteFormInstanceRequest, premiumDeleteFormInstanceHeaders, &util.RuntimeOptions{})
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
    let premiumDeleteFormInstanceHeaders = new dingtalkworkflow_1_0.PremiumDeleteFormInstanceHeaders({ });
    premiumDeleteFormInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumDeleteFormInstanceRequest = new dingtalkworkflow_1_0.PremiumDeleteFormInstanceRequest({
      processCode: 'PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
      formInstanceIds: [
        'abc'
      ],
      userId: 'managerUserId1',
    });
    try {
      await client.premiumDeleteFormInstanceWithOptions(premiumDeleteFormInstanceRequest, premiumDeleteFormInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumDeleteFormInstanceHeaders premiumDeleteFormInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumDeleteFormInstanceHeaders();
            premiumDeleteFormInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumDeleteFormInstanceRequest premiumDeleteFormInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumDeleteFormInstanceRequest
            {
                ProcessCode = "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
                FormInstanceIds = new List<string>
                {
                    "abc"
                },
                UserId = "managerUserId1",
            };
            try
            {
                client.PremiumDeleteFormInstanceWithOptions(premiumDeleteFormInstanceRequest, premiumDeleteFormInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | String | 是否删除成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : "true"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | processcode.error | processCode对应的表单不存在 | processCode对应的表单不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | processes.error | 获取模板列表失败 | 获取模板列表失败 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | system.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | user.not.exist | 用户不存在 | 用户不存在 |
| 500 | system.error | 系统错误 | 系统错误 |
| 500 | param.error | %s | 参数错误 |
| 500 | form.error | 参数错误，不是存表单 | 参数错误 |
| 500 | form.code.error | 表单详情查询失败 | 参数错误 |
| 500 | size.error | 删除实例个数超出限制 | 参数错误 |
| 500 | auth.error | 没有权限操作 | 权限错误 |
| 500 | delete.error | 删除实例失败 | 删除实例失败 |
| 500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验失败，未开通或过期 |
| 500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 请求过于频繁，稍后重试 |
