---
title: "查询已设置为条件的表单组件"
source_url: "https://open.dingtalk.com/document/development/query-form-components-that-have-been-set-as-criteria-1"
namespace: "development"
slug: "query-form-components-that-have-been-set-as-criteria-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批表单 > 查询已设置为条件的表单组件"
doc_id: "uB6xY2eYXw"
updated_at: "2026-06-03 10:12:24"
---

> Source: https://open.dingtalk.com/document/development/query-form-components-that-have-been-set-as-criteria-1
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批表单 > 查询已设置为条件的表单组件
> Updated: 2026-06-03 10:12:24

# 查询已设置为条件的表单组件

用于查询已设置为条件的表单组件。

## **接口调用说明**

产品方案商通过创建审批模板接口，帮企业生成审批模板后，企业可以在审批管理后台设置审批流程。设置过程中，可以把表单组件设为流程条件。此时，这些被设为流程条件的表单组件，ISV是不能再次更新的。通过此接口，可以查询有哪些表单组件被设置为流程条件了。

![](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20220919/ftrz/OA条件组件.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/conditions/components |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Form.Read-工作流模板读权限。 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 是 | 审批流的唯一码，调用[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口或[OA审批概述-名词解释](0473-workflow-overview.md)获取。 |
| agentId | Long | 否 | 应用的agentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/#/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/processes/conditions/components?processCode=PROC-xxx&agentId=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.GetConditionFormComponentHeaders getConditionFormComponentHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetConditionFormComponentHeaders();
        getConditionFormComponentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.GetConditionFormComponentRequest getConditionFormComponentRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetConditionFormComponentRequest()
                .setProcessCode("PROC-xxx")
                .setAgentId(10L);
        try {
            client.getConditionFormComponentWithOptions(getConditionFormComponentRequest, getConditionFormComponentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_condition_form_component_headers = dingtalkworkflow__1__0_models.GetConditionFormComponentHeaders()
        get_condition_form_component_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_condition_form_component_request = dingtalkworkflow__1__0_models.GetConditionFormComponentRequest(
            process_code='PROC-xxx',
            agent_id=10
        )
        try:
            client.get_condition_form_component_with_options(get_condition_form_component_request, get_condition_form_component_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_condition_form_component_headers = dingtalkworkflow__1__0_models.GetConditionFormComponentHeaders()
        get_condition_form_component_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_condition_form_component_request = dingtalkworkflow__1__0_models.GetConditionFormComponentRequest(
            process_code='PROC-xxx',
            agent_id=10
        )
        try:
            await client.get_condition_form_component_with_options_async(get_condition_form_component_request, get_condition_form_component_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetConditionFormComponentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetConditionFormComponentRequest;
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
        $getConditionFormComponentHeaders = new GetConditionFormComponentHeaders([]);
        $getConditionFormComponentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getConditionFormComponentRequest = new GetConditionFormComponentRequest([
            "processCode" => "PROC-xxx",
            "agentId" => 10
        ]);
        try {
            $client->getConditionFormComponentWithOptions($getConditionFormComponentRequest, $getConditionFormComponentHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  getConditionFormComponentHeaders := &dingtalkworkflow_1_0.GetConditionFormComponentHeaders{}
  getConditionFormComponentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getConditionFormComponentRequest := &dingtalkworkflow_1_0.GetConditionFormComponentRequest{
    ProcessCode: tea.String("PROC-xxx"),
    AgentId: tea.Int64(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetConditionFormComponentWithOptions(getConditionFormComponentRequest, getConditionFormComponentHeaders, &util.RuntimeOptions{})
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
import dingtalkworkflow_1_0, * as $dingtalkworkflow_1_0 from '@alicloud/dingtalk/workflow_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkflow_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkflow_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getConditionFormComponentHeaders = new $dingtalkworkflow_1_0.GetConditionFormComponentHeaders({ });
    getConditionFormComponentHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getConditionFormComponentRequest = new $dingtalkworkflow_1_0.GetConditionFormComponentRequest({
      processCode: "PROC-xxx",
      agentId: 10,
    });
    try {
      await client.getConditionFormComponentWithOptions(getConditionFormComponentRequest, getConditionFormComponentHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetConditionFormComponentHeaders getConditionFormComponentHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetConditionFormComponentHeaders();
            getConditionFormComponentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetConditionFormComponentRequest getConditionFormComponentRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetConditionFormComponentRequest
            {
                ProcessCode = "PROC-xxx",
                AgentId = 10,
            };
            try
            {
                client.GetConditionFormComponentWithOptions(getConditionFormComponentRequest, getConditionFormComponentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 表单ID。 |
| label | String | 表单名称。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "id" : "TextField",
    "label" : "输入框"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidProcessCode | 审批模板processCode不能为空 | 审批模板processCode不能为空 |
| 400 | processNotExist | 审批流不存在 | 审批流不存在 |
| 400 | needAuth | 需要授权 | 需要授权 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 500 | systemError | 系统异常 | 系统异常 |
