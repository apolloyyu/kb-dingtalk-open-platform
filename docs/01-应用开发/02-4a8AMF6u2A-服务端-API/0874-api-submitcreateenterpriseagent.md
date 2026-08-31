---
title: "提交创建企业自建Agent"
source_url: "https://open.dingtalk.com/document/development/api-submitcreateenterpriseagent"
namespace: "development"
slug: "api-submitcreateenterpriseagent"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 智能体 > 提交创建企业自建Agent"
doc_id: "I4s1nG4CKS"
updated_at: "2026-07-24 09:14:12"
---

> Source: https://open.dingtalk.com/document/development/api-submitcreateenterpriseagent
> Path: 应用开发 / 服务端 API / 钉钉应用 > 智能体 > 提交创建企业自建Agent
> Updated: 2026-07-24 09:14:12

# 提交创建企业自建Agent

调用本接口，提交创建企业自建 Agent 任务。接口异步执行企业自建应用创建、机器人创建、默认权限授权、应用版本提交与发布，并返回 taskId。

## **接口调用说明**

- 任务状态通过 [查询创建企业自建Agent任务进度](0875-api-querycreateenterpriseagent.md)接口 查询，状态包括：

  - **WAITING**：任务处理中
  - **SUCCESS**：创建成功
  - **FAIL**：创建失败
  - **EXPIRED**：任务不存在或已过期
- 企业创建链路不返回 `APPROVAL_REQUIRED`。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/enterpriseAgent/submit |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-微应用管理权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求示例**

HTTP

```
POST /v1.0/microApp/enterpriseAgent/submit HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token15xxxxz1
Content-Type:application/json

userid=user1&appName=测试一下&robotName=测试机器人&desc=这是一个测试应用&taskId=task12&robotMediaId=@lADxxxxrMyMzI&previewMediaId=@lADxxxxrMyMzI
```

Java

```
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.SubmitCreateEnterpriseAgentHeaders submitCreateEnterpriseAgentHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.SubmitCreateEnterpriseAgentHeaders();
        submitCreateEnterpriseAgentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.SubmitCreateEnterpriseAgentRequest submitCreateEnterpriseAgentRequest = new com.aliyun.dingtalkmicro_app_1_0.models.SubmitCreateEnterpriseAgentRequest()
                .setUserid("user1")
                .setAppName("测试一下")
                .setRobotName("测试机器人")
                .setDesc("这是一个测试应用")
                .setTaskId("task12")
                .setRobotMediaId("@lADxxxxrMyMzI")
                .setPreviewMediaId("@lADxxxxrMyMzI");
        try {
            client.submitCreateEnterpriseAgentWithOptions(submitCreateEnterpriseAgentRequest, submitCreateEnterpriseAgentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.micro_app_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmicroApp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmicroApp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        submit_create_enterprise_agent_headers = dingtalkmicro_app__1__0_models.SubmitCreateEnterpriseAgentHeaders()
        submit_create_enterprise_agent_headers.x_acs_dingtalk_access_token = '<your access token>'
        submit_create_enterprise_agent_request = dingtalkmicro_app__1__0_models.SubmitCreateEnterpriseAgentRequest(
            userid='user1',
            app_name='测试一下',
            robot_name='测试机器人',
            desc='这是一个测试应用',
            task_id='task12',
            robot_media_id='@lADxxxxrMyMzI',
            preview_media_id='@lADxxxxrMyMzI'
        )
        try:
            client.submit_create_enterprise_agent_with_options(submit_create_enterprise_agent_request, submit_create_enterprise_agent_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        submit_create_enterprise_agent_headers = dingtalkmicro_app__1__0_models.SubmitCreateEnterpriseAgentHeaders()
        submit_create_enterprise_agent_headers.x_acs_dingtalk_access_token = '<your access token>'
        submit_create_enterprise_agent_request = dingtalkmicro_app__1__0_models.SubmitCreateEnterpriseAgentRequest(
            userid='user1',
            app_name='测试一下',
            robot_name='测试机器人',
            desc='这是一个测试应用',
            task_id='task12',
            robot_media_id='@lADxxxxrMyMzI',
            preview_media_id='@lADxxxxrMyMzI'
        )
        try:
            await client.submit_create_enterprise_agent_with_options_async(submit_create_enterprise_agent_request, submit_create_enterprise_agent_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\SubmitCreateEnterpriseAgentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\SubmitCreateEnterpriseAgentRequest;
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
        $submitCreateEnterpriseAgentHeaders = new SubmitCreateEnterpriseAgentHeaders([]);
        $submitCreateEnterpriseAgentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $submitCreateEnterpriseAgentRequest = new SubmitCreateEnterpriseAgentRequest([
            "userid" => "user1",
            "appName" => "测试一下",
            "robotName" => "测试机器人",
            "desc" => "这是一个测试应用",
            "taskId" => "task12",
            "robotMediaId" => "@lADxxxxrMyMzI",
            "previewMediaId" => "@lADxxxxrMyMzI"
        ]);
        try {
            $client->submitCreateEnterpriseAgentWithOptions($submitCreateEnterpriseAgentRequest, $submitCreateEnterpriseAgentHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
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
func CreateClient () (_result *dingtalkmicroapp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmicroapp_1_0.Client{}
  _result, _err = dingtalkmicroapp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  submitCreateEnterpriseAgentHeaders := &dingtalkmicroapp_1_0.SubmitCreateEnterpriseAgentHeaders{}
  submitCreateEnterpriseAgentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  submitCreateEnterpriseAgentRequest := &dingtalkmicroapp_1_0.SubmitCreateEnterpriseAgentRequest{
    Userid: tea.String("user1"),
    AppName: tea.String("测试一下"),
    RobotName: tea.String("测试机器人"),
    Desc: tea.String("这是一个测试应用"),
    TaskId: tea.String("task12"),
    RobotMediaId: tea.String("@lADxxxxrMyMzI"),
    PreviewMediaId: tea.String("@lADxxxxrMyMzI"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SubmitCreateEnterpriseAgentWithOptions(submitCreateEnterpriseAgentRequest, submitCreateEnterpriseAgentHeaders, &util.RuntimeOptions{})
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
const dingtalkmicroApp_1_0 = require('@alicloud/dingtalk/microApp_1_0');
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
    return new dingtalkmicroApp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let submitCreateEnterpriseAgentHeaders = new dingtalkmicroApp_1_0.SubmitCreateEnterpriseAgentHeaders({ });
    submitCreateEnterpriseAgentHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let submitCreateEnterpriseAgentRequest = new dingtalkmicroApp_1_0.SubmitCreateEnterpriseAgentRequest({
      userid: 'user1',
      appName: '测试一下',
      robotName: '测试机器人',
      desc: '这是一个测试应用',
      taskId: 'task12',
      robotMediaId: '@lADxxxxrMyMzI',
      previewMediaId: '@lADxxxxrMyMzI',
    });
    try {
      await client.submitCreateEnterpriseAgentWithOptions(submitCreateEnterpriseAgentRequest, submitCreateEnterpriseAgentHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SubmitCreateEnterpriseAgentHeaders submitCreateEnterpriseAgentHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SubmitCreateEnterpriseAgentHeaders();
            submitCreateEnterpriseAgentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SubmitCreateEnterpriseAgentRequest submitCreateEnterpriseAgentRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.SubmitCreateEnterpriseAgentRequest
            {
                Userid = "user1",
                AppName = "测试一下",
                RobotName = "测试机器人",
                Desc = "这是一个测试应用",
                TaskId = "task12",
                RobotMediaId = "@lADxxxxrMyMzI",
                PreviewMediaId = "@lADxxxxrMyMzI",
            };
            try
            {
                client.SubmitCreateEnterpriseAgentWithOptions(submitCreateEnterpriseAgentRequest, submitCreateEnterpriseAgentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| taskId | String | 创建任务 ID。 |
| status | String | 任务状态：提交成功为 `WAITING`。  **[!NOTE]**  成功返回表示创建任务已提交，不代表应用和机器人已完成创建。   - **WAITING** - **SUCCESS** - **FAIL** - **EXPIRED** |
| expiresIn | String | 任务结果缓存有效期，单位秒。 |
| interval | String | 建议轮询间隔，单位秒。 |
| retryCount | String | 任务重试次数。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "taskId" : "task12",
  "status" : "SUCCESS",
  "expiresIn" : "86400",
  "interval" : "5",
  "retryCount" : "0"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.parameter | 参数无效 | userid/appName/robotName/desc 缺失 |
| 409 | task.conflict | 创建任务正在提交 | 分布式锁冲突 |
| 500 | system.busy | 系统繁忙 | 后端未知异常 |
