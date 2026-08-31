---
title: "查询创建企业自建Agent任务进度"
source_url: "https://open.dingtalk.com/document/development/api-querycreateenterpriseagent"
namespace: "development"
slug: "api-querycreateenterpriseagent"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 智能体 > 查询创建企业自建Agent任务进度"
doc_id: "6srvznQX4r"
updated_at: "2026-07-22 17:11:42"
---

> Source: https://open.dingtalk.com/document/development/api-querycreateenterpriseagent
> Path: 应用开发 / 服务端 API / 钉钉应用 > 智能体 > 查询创建企业自建Agent任务进度
> Updated: 2026-07-22 17:11:42

# 查询创建企业自建Agent任务进度

调用本接口，根据任务ID获取任务进度信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/agent/create/query |
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
POST /v1.0/microApp/agent/create/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:cnNxxxxxT01
Content-Type:application/json

userid=user1&taskId=create-axxxx60612-001
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
        com.aliyun.dingtalkmicro_app_1_0.models.QueryCreateEnterpriseAgentHeaders queryCreateEnterpriseAgentHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.QueryCreateEnterpriseAgentHeaders();
        queryCreateEnterpriseAgentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.QueryCreateEnterpriseAgentRequest queryCreateEnterpriseAgentRequest = new com.aliyun.dingtalkmicro_app_1_0.models.QueryCreateEnterpriseAgentRequest()
                .setUserid("user1")
                .setTaskId("create-axxxx60612-001");
        try {
            client.queryCreateEnterpriseAgentWithOptions(queryCreateEnterpriseAgentRequest, queryCreateEnterpriseAgentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_create_enterprise_agent_headers = dingtalkmicro_app__1__0_models.QueryCreateEnterpriseAgentHeaders()
        query_create_enterprise_agent_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_create_enterprise_agent_request = dingtalkmicro_app__1__0_models.QueryCreateEnterpriseAgentRequest(
            userid='user1',
            task_id='create-axxxx60612-001'
        )
        try:
            client.query_create_enterprise_agent_with_options(query_create_enterprise_agent_request, query_create_enterprise_agent_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_create_enterprise_agent_headers = dingtalkmicro_app__1__0_models.QueryCreateEnterpriseAgentHeaders()
        query_create_enterprise_agent_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_create_enterprise_agent_request = dingtalkmicro_app__1__0_models.QueryCreateEnterpriseAgentRequest(
            userid='user1',
            task_id='create-axxxx60612-001'
        )
        try:
            await client.query_create_enterprise_agent_with_options_async(query_create_enterprise_agent_request, query_create_enterprise_agent_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\QueryCreateEnterpriseAgentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\QueryCreateEnterpriseAgentRequest;
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
        $queryCreateEnterpriseAgentHeaders = new QueryCreateEnterpriseAgentHeaders([]);
        $queryCreateEnterpriseAgentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryCreateEnterpriseAgentRequest = new QueryCreateEnterpriseAgentRequest([
            "userid" => "user1",
            "taskId" => "create-axxxx60612-001"
        ]);
        try {
            $client->queryCreateEnterpriseAgentWithOptions($queryCreateEnterpriseAgentRequest, $queryCreateEnterpriseAgentHeaders, new RuntimeOptions([]));
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

  queryCreateEnterpriseAgentHeaders := &dingtalkmicroapp_1_0.QueryCreateEnterpriseAgentHeaders{}
  queryCreateEnterpriseAgentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryCreateEnterpriseAgentRequest := &dingtalkmicroapp_1_0.QueryCreateEnterpriseAgentRequest{
    Userid: tea.String("user1"),
    TaskId: tea.String("create-axxxx60612-001"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryCreateEnterpriseAgentWithOptions(queryCreateEnterpriseAgentRequest, queryCreateEnterpriseAgentHeaders, &util.RuntimeOptions{})
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
    let queryCreateEnterpriseAgentHeaders = new dingtalkmicroApp_1_0.QueryCreateEnterpriseAgentHeaders({ });
    queryCreateEnterpriseAgentHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryCreateEnterpriseAgentRequest = new dingtalkmicroApp_1_0.QueryCreateEnterpriseAgentRequest({
      userid: 'user1',
      taskId: 'create-axxxx60612-001',
    });
    try {
      await client.queryCreateEnterpriseAgentWithOptions(queryCreateEnterpriseAgentRequest, queryCreateEnterpriseAgentHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.QueryCreateEnterpriseAgentHeaders queryCreateEnterpriseAgentHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.QueryCreateEnterpriseAgentHeaders();
            queryCreateEnterpriseAgentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.QueryCreateEnterpriseAgentRequest queryCreateEnterpriseAgentRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.QueryCreateEnterpriseAgentRequest
            {
                Userid = "user1",
                TaskId = "create-axxxx60612-001",
            };
            try
            {
                client.QueryCreateEnterpriseAgentWithOptions(queryCreateEnterpriseAgentRequest, queryCreateEnterpriseAgentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| taskId | String | 任务ID。 |
| status | String | 任务状态：   - **WAITING**：等待中 - **SUCCESS**：成功 - **FAIL**：失败 - **EXPIRED**：过期 |
| agentId | String | 创建成功后的企业内部应用 AgentId，仅`SUCCESS`时返回。 |
| robotCode | String | 创建成功后的机器人编码，仅`SUCCESS`时返回。 |
| clientId | String | 应用 Client ID / AppKey，仅`SUCCESS`时返回。 |
| clientSecret | String | 应用 Client Secret / AppSecret，仅`SUCCESS`时返回，敏感字段。 |
| errorCode | String | 失败错误码，仅失败时返回。 |
| errorMsg | String | 失败原因或过期说明。 |
| expiresIn | Long | 任务有效期，单位秒。 |
| interval | Long | 建议轮询间隔，单位秒。 |
| retryCount | Long | 当前任务已重试次数。 |
| gmtCreate | Long | 创建时间。 |
| gmtModified | Long | 最后更新时间。 |
| unifiedAppId | String | 统一应用 ID即App ID，用于唯一标识钉钉开放平台中的应用。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "taskId" : "task1",
  "status" : "SUCCESS",
  "agentId" : "39xxxx5125",
  "robotCode" : "robotxxxxx30687",
  "clientId" : "dingxxxxxqkqc",
  "clientSecret" : "PSTmmCxxxxxkR7u",
  "errorCode" : "200",
  "errorMsg" : "成功",
  "expiresIn" : 86400,
  "interval" : 5,
  "retryCount" : 0,
  "gmtCreate" : 1781244390000,
  "gmtModified" : 1781244400000,
  "unifiedAppId" : "3de5d8xxxx38a88297"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.parameter | The request parameter is invalid. | 请求参数无效，taskId/userid 缺失。 |
| 400 | invalid.parameter.orgId | The orgId resolved from accessToken is invalid. | 企业accessToken解析出的orgId无效。 |
| 403 | forbidden.task.owner | Forbidden.TaskOwner You are not authorized to access this task. | 当前调用方无权操作该创建任务（orgId/userid与任务归属不匹配）。 |
| 500 | service.unavailable | An internal error occurred, please retry later. | 系统繁忙，请稍后重试。 |
