---
title: "获取审批表单控件字段操作权限"
source_url: "https://open.dingtalk.com/document/development/api-premiumgetinstfieldsetting"
namespace: "development"
slug: "api-premiumgetinstfieldsetting"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 获取审批表单控件字段操作权限"
doc_id: "qufUg8TaPd"
updated_at: "2026-06-03 10:12:46"
---

> Source: https://open.dingtalk.com/document/development/api-premiumgetinstfieldsetting
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 获取审批表单控件字段操作权限
> Updated: 2026-06-03 10:12:46

# 获取审批表单控件字段操作权限

调用本接口，支持获取当前审批人对流程表单控件的操作权限（可编辑、只读、隐藏等）。可用于在三方业务自建系统中做权限控制，与【更新流程表单审批实例】接口配套使用，根据业务场景需要在指定场景下对流程中和已完成的实例数据进行更新。

## **接口调用说明**

当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processes/fields/settings/query |
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
| processInstanceId | String | 是 | 审批实例ID：   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| userId | String | 是 | 当前审批人userId。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processes/fields/settings/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processInstanceId" : "proc-FF6Y2xxxx",
  "userId" : "userId123"
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
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetInstFieldSettingHeaders premiumGetInstFieldSettingHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetInstFieldSettingHeaders();
        premiumGetInstFieldSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetInstFieldSettingRequest premiumGetInstFieldSettingRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetInstFieldSettingRequest()
                .setProcessInstanceId("proc-FF6Y2xxxx")
                .setUserId("userId123");
        try {
            client.premiumGetInstFieldSettingWithOptions(premiumGetInstFieldSettingRequest, premiumGetInstFieldSettingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_get_inst_field_setting_headers = dingtalkworkflow__1__0_models.PremiumGetInstFieldSettingHeaders()
        premium_get_inst_field_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_inst_field_setting_request = dingtalkworkflow__1__0_models.PremiumGetInstFieldSettingRequest(
            process_instance_id='proc-FF6Y2xxxx',
            user_id='userId123'
        )
        try:
            client.premium_get_inst_field_setting_with_options(premium_get_inst_field_setting_request, premium_get_inst_field_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_get_inst_field_setting_headers = dingtalkworkflow__1__0_models.PremiumGetInstFieldSettingHeaders()
        premium_get_inst_field_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_inst_field_setting_request = dingtalkworkflow__1__0_models.PremiumGetInstFieldSettingRequest(
            process_instance_id='proc-FF6Y2xxxx',
            user_id='userId123'
        )
        try:
            await client.premium_get_inst_field_setting_with_options_async(premium_get_inst_field_setting_request, premium_get_inst_field_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetInstFieldSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetInstFieldSettingRequest;
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
        $premiumGetInstFieldSettingHeaders = new PremiumGetInstFieldSettingHeaders([]);
        $premiumGetInstFieldSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumGetInstFieldSettingRequest = new PremiumGetInstFieldSettingRequest([
            "processInstanceId" => "proc-FF6Y2xxxx",
            "userId" => "userId123"
        ]);
        try {
            $client->premiumGetInstFieldSettingWithOptions($premiumGetInstFieldSettingRequest, $premiumGetInstFieldSettingHeaders, new RuntimeOptions([]));
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

  premiumGetInstFieldSettingHeaders := &dingtalkworkflow_1_0.PremiumGetInstFieldSettingHeaders{}
  premiumGetInstFieldSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumGetInstFieldSettingRequest := &dingtalkworkflow_1_0.PremiumGetInstFieldSettingRequest{
    ProcessInstanceId: tea.String("proc-FF6Y2xxxx"),
    UserId: tea.String("userId123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumGetInstFieldSettingWithOptions(premiumGetInstFieldSettingRequest, premiumGetInstFieldSettingHeaders, &util.RuntimeOptions{})
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
    let premiumGetInstFieldSettingHeaders = new dingtalkworkflow_1_0.PremiumGetInstFieldSettingHeaders({ });
    premiumGetInstFieldSettingHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumGetInstFieldSettingRequest = new dingtalkworkflow_1_0.PremiumGetInstFieldSettingRequest({
      processInstanceId: 'proc-FF6Y2xxxx',
      userId: 'userId123',
    });
    try {
      await client.premiumGetInstFieldSettingWithOptions(premiumGetInstFieldSettingRequest, premiumGetInstFieldSettingHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetInstFieldSettingHeaders premiumGetInstFieldSettingHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetInstFieldSettingHeaders();
            premiumGetInstFieldSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetInstFieldSettingRequest premiumGetInstFieldSettingRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetInstFieldSettingRequest
            {
                ProcessInstanceId = "proc-FF6Y2xxxx",
                UserId = "userId123",
            };
            try
            {
                client.PremiumGetInstFieldSettingWithOptions(premiumGetInstFieldSettingRequest, premiumGetInstFieldSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| fieldId | String | 字段id。 |
| fieldBehavior | String | 组件操作权限：   - NORMAL:可编辑 - READONLY:只读 - HIDDEN:隐藏 |
| componentType | String | 组件类型。 |
| success | Boolean | 接口请求是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "fieldId" : "TextField-abcd",
    "fieldBehavior" : "READONLY",
    "componentType" : "TextField"
  } ],
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidInstanceIdOrFieldId | 审批实例id或当前审核人id不能为空 | 请检查processInstanceId、userId参数传值是否正确 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 400 | userNotExist | 用户不存在 | 请检查当前用户是否归属于当前组织 |
| 400 | processInstanceNotExist | 审批实例不存在 | 请检查processInstanceId参数传值是否正确 |
| 400 | getInstFieldSettingError | 获取流程表单控件可见性失败 | 请记录异常日志，稍后再试 |
| 500 | systemError | 系统异常 | 系统异常 |
