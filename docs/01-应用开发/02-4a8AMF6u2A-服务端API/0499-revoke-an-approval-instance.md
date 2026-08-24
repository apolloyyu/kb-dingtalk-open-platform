---
title: "撤销审批实例"
source_url: "https://open.dingtalk.com/document/development/revoke-an-approval-instance"
namespace: "development"
slug: "revoke-an-approval-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批实例 > 撤销审批实例"
doc_id: "cRPDAjuKFG"
updated_at: "2026-06-03 10:12:27"
---

> Source: https://open.dingtalk.com/document/development/revoke-an-approval-instance
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批实例 > 撤销审批实例
> Updated: 2026-06-03 10:12:27

# 撤销审批实例

调用本接口，撤销发起的处于流程中的审批实例。

## **接口调用说明**

- 审批发起15秒内不能撤销审批流程。
- 当入参isSystem选择为false时（由指定的操作者终止），需要传发起人才能撤销。
- 本接口只能撤销流程中的审批实例，不能撤销已审批完成的审批实例。
- 调用本接口前，需要在[钉钉管理后台](https://oa.dingtalk.com/)> **工作台 > 应用管理 > OA审批应用**，进入**OA审批管理后台**，找到**模板 > 高级设置 > 撤销/修改审批单** >勾选**允许提交人撤销审批中的审批单**，才能撤销审批实例，否则会报错`errcode:820008, success:false, errmsg:审批系统错误`，原因为【您没有任务处理的权限】。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7472540871/p1076089.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances/terminate |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workflow.Instance.Write-工作流实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 审批实例ID。   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| isSystem | Boolean | 否 | 是否通过系统操作。   - **true**：由系统直接终止 - **false**：由指定的操作者终止（需要传发起人才能撤销） |
| remark | String | 否 | 终止说明，最大长度1024字符。 |
| operatingUserId | String | 否 | 操作人的userId。      当isSystem为false时，该参数必传（需要传发起人才能撤销）。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processInstances/terminate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:be311xxxx
Content-Type:application/json

{
  "processInstanceId" : "a171de6c-8bxxxx",
  "isSystem" : true,
  "remark" : "终止说明。",
  "operatingUserId" : "133743186427339452"
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
        
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceHeaders terminateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceHeaders();
        terminateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceRequest terminateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.TerminateProcessInstanceRequest()
                .setProcessInstanceId("a171de6c-8bxxxx")
                .setIsSystem(true)
                .setRemark("终止说明。")
                .setOperatingUserId("133743186427339452");
        try {
            client.terminateProcessInstanceWithOptions(terminateProcessInstanceRequest, terminateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        terminate_process_instance_headers = dingtalkworkflow__1__0_models.TerminateProcessInstanceHeaders()
        terminate_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        terminate_process_instance_request = dingtalkworkflow__1__0_models.TerminateProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx',
            is_system=True,
            remark='终止说明。',
            operating_user_id='133743186427339452'
        )
        try:
            client.terminate_process_instance_with_options(terminate_process_instance_request, terminate_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        terminate_process_instance_headers = dingtalkworkflow__1__0_models.TerminateProcessInstanceHeaders()
        terminate_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        terminate_process_instance_request = dingtalkworkflow__1__0_models.TerminateProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx',
            is_system=True,
            remark='终止说明。',
            operating_user_id='133743186427339452'
        )
        try:
            await client.terminate_process_instance_with_options_async(terminate_process_instance_request, terminate_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\TerminateProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\TerminateProcessInstanceRequest;
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
        $terminateProcessInstanceHeaders = new TerminateProcessInstanceHeaders([]);
        $terminateProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $terminateProcessInstanceRequest = new TerminateProcessInstanceRequest([
            "processInstanceId" => "a171de6c-8bxxxx",
            "isSystem" => true,
            "remark" => "终止说明。",
            "operatingUserId" => "133743186427339452"
        ]);
        try {
            $client->terminateProcessInstanceWithOptions($terminateProcessInstanceRequest, $terminateProcessInstanceHeaders, new RuntimeOptions([]));
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

  terminateProcessInstanceHeaders := &dingtalkworkflow_1_0.TerminateProcessInstanceHeaders{}
  terminateProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  terminateProcessInstanceRequest := &dingtalkworkflow_1_0.TerminateProcessInstanceRequest{
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
    IsSystem: tea.Bool(true),
    Remark: tea.String("终止说明。"),
    OperatingUserId: tea.String("133743186427339452"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.TerminateProcessInstanceWithOptions(terminateProcessInstanceRequest, terminateProcessInstanceHeaders, &util.RuntimeOptions{})
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
    let terminateProcessInstanceHeaders = new dingtalkworkflow_1_0.TerminateProcessInstanceHeaders({ });
    terminateProcessInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let terminateProcessInstanceRequest = new dingtalkworkflow_1_0.TerminateProcessInstanceRequest({
      processInstanceId: 'a171de6c-8bxxxx',
      isSystem: true,
      remark: '终止说明。',
      operatingUserId: '133743186427339452',
    });
    try {
      await client.terminateProcessInstanceWithOptions(terminateProcessInstanceRequest, terminateProcessInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.TerminateProcessInstanceHeaders terminateProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.TerminateProcessInstanceHeaders();
            terminateProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.TerminateProcessInstanceRequest terminateProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.TerminateProcessInstanceRequest
            {
                ProcessInstanceId = "a171de6c-8bxxxx",
                IsSystem = true,
                Remark = "终止说明。",
                OperatingUserId = "133743186427339452",
            };
            try
            {
                client.TerminateProcessInstanceWithOptions(terminateProcessInstanceRequest, terminateProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否撤销成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 撤销审批实例参数错误 | 撤销审批实例参数错误 |
| 400 | userNotExist | 用户不存在 | 请检查operatingUserId参数是否正确 |
| 400 | aflowProcessInstNotExist | 审批实例不存在 | 请检查processInstanceId参数是否正确 |
| 400 | aflowProcessInstStatusException | %s | 审批单状态异常，具体可能为：提交审批单后15秒内不能进行撤回、审批单已结束等 |
| 400 | invalidInstanceId | 审批实例ID不能为空 | 请检查processInstanceId参数是否正确 |
| 400 | invalidInstanceTerminateIsSystem | 撤销审批实例，是否通过系统操作参数不能为空 | 撤销审批实例，是否通过系统操作参数不能为空 |
| 400 | invalidInstanceTerminateOperatingUserId | 撤销审批实例，当isSystem为false时，操作人的userId不能为空 | 撤销审批实例，当isSystem为false时，操作人的userId不能为空 |
| 400 | internalError | %s | 系统内部异常，具体可能为：管理后台未设置允许提交人撤销审批中的审批单，导致您没有任务处理的权限 |
| 500 | systemError | 系统异常 | 系统异常 |
