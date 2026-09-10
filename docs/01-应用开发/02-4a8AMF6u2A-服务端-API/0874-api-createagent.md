---
title: "创建企业智能体应用"
source_url: "https://open.dingtalk.com/document/development/api-createagent"
namespace: "development"
slug: "api-createagent"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 智能体 > 创建企业智能体应用"
doc_id: "yciY13Hpzk"
updated_at: "2026-07-24 09:14:11"
---

> Source: https://open.dingtalk.com/document/development/api-createagent
> Path: 应用开发 / 服务端 API / 钉钉应用 > 智能体 > 创建企业智能体应用
> Updated: 2026-07-24 09:14:11

# 创建企业智能体应用

调用本接口，创建企业智能体应用。

## **接口调用说明**

一次性完成「建应用 + 建机器人 + 下发凭证」的聚合接口，把开发者从 3 步以上的手工配置降为 1 次 API 调用，默认开启范围仅自己可见。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/agent/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-微应用管理权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userid | String | 否 | 企业内员工 userId/staffId。  服务端通过 orgId + userid 查询员工并转换为内部 uid，后续作为应用归属人、机器人创建者和权限授权操作者。 |
| appName | String | 否 | 智能体应用名称，长度 2~20，企业内唯一。 |
| robotName | String | 否 | 承载机器人名称，长度 2~20 |
| desc | String | 否 | 机器人功能描述，长度 ≤ 200 |
| robotMediaId | String | 否 | 机器人图标 mediaId。  为空时使用服务端默认图标 |
| previewMediaId | String | 否 | 机器人预览图 mediaId。   - 为空时复用 robotMediaId。 - 如果 robotMediaId 也为空，则使用默认图标。 |

### **请求示例**

HTTP

```
POST /v1.0/microApp/agent/create HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:17231273616
Content-Type:application/json

{
  "userid" : "13213",
  "appName" : "李四应用",
  "robotName" : "李四应用",
  "desc" : "李四应用描述",
  "robotMediaId" : "1231312314",
  "previewMediaId" : "1231312314"
}
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
        com.aliyun.dingtalkmicro_app_1_0.models.CreateAgentHeaders createAgentHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.CreateAgentHeaders();
        createAgentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.CreateAgentRequest createAgentRequest = new com.aliyun.dingtalkmicro_app_1_0.models.CreateAgentRequest()
                .setUserid("13213")
                .setAppName("李四应用")
                .setRobotName("李四应用")
                .setDesc("李四应用描述")
                .setRobotMediaId("1231312314")
                .setPreviewMediaId("1231312314");
        try {
            client.createAgentWithOptions(createAgentRequest, createAgentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_agent_headers = dingtalkmicro_app__1__0_models.CreateAgentHeaders()
        create_agent_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_agent_request = dingtalkmicro_app__1__0_models.CreateAgentRequest(
            userid='13213',
            app_name='李四应用',
            robot_name='李四应用',
            desc='李四应用描述',
            robot_media_id='1231312314',
            preview_media_id='1231312314'
        )
        try:
            client.create_agent_with_options(create_agent_request, create_agent_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_agent_headers = dingtalkmicro_app__1__0_models.CreateAgentHeaders()
        create_agent_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_agent_request = dingtalkmicro_app__1__0_models.CreateAgentRequest(
            userid='13213',
            app_name='李四应用',
            robot_name='李四应用',
            desc='李四应用描述',
            robot_media_id='1231312314',
            preview_media_id='1231312314'
        )
        try:
            await client.create_agent_with_options_async(create_agent_request, create_agent_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\CreateAgentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\CreateAgentRequest;
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
        $createAgentHeaders = new CreateAgentHeaders([]);
        $createAgentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createAgentRequest = new CreateAgentRequest([
            "userid" => "13213",
            "appName" => "李四应用",
            "robotName" => "李四应用",
            "desc" => "李四应用描述",
            "robotMediaId" => "1231312314",
            "previewMediaId" => "1231312314"
        ]);
        try {
            $client->createAgentWithOptions($createAgentRequest, $createAgentHeaders, new RuntimeOptions([]));
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

  createAgentHeaders := &dingtalkmicroapp_1_0.CreateAgentHeaders{}
  createAgentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createAgentRequest := &dingtalkmicroapp_1_0.CreateAgentRequest{
    Userid: tea.String("13213"),
    AppName: tea.String("李四应用"),
    RobotName: tea.String("李四应用"),
    Desc: tea.String("李四应用描述"),
    RobotMediaId: tea.String("1231312314"),
    PreviewMediaId: tea.String("1231312314"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateAgentWithOptions(createAgentRequest, createAgentHeaders, &util.RuntimeOptions{})
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
    let createAgentHeaders = new dingtalkmicroApp_1_0.CreateAgentHeaders({ });
    createAgentHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createAgentRequest = new dingtalkmicroApp_1_0.CreateAgentRequest({
      userid: '13213',
      appName: '李四应用',
      robotName: '李四应用',
      desc: '李四应用描述',
      robotMediaId: '1231312314',
      previewMediaId: '1231312314',
    });
    try {
      await client.createAgentWithOptions(createAgentRequest, createAgentHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateAgentHeaders createAgentHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateAgentHeaders();
            createAgentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateAgentRequest createAgentRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateAgentRequest
            {
                Userid = "13213",
                AppName = "李四应用",
                RobotName = "李四应用",
                Desc = "李四应用描述",
                RobotMediaId = "1231312314",
                PreviewMediaId = "1231312314",
            };
            try
            {
                client.CreateAgentWithOptions(createAgentRequest, createAgentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| agentId | String | 返回结果。 |
| robotCode | String | 机器人编码，用于服务端消息推送、消息回调路由 |
| clientId | String | 客户端身份标识（等同 AppKey）。 |
| clientSecret | String | 客户端凭证，仅创建时返回一次，请妥善保存。 |
| unifiedAppId | String | 统一应用 ID即App ID，用于唯一标识钉钉开放平台中的应用。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "agentId" : "21313",
  "robotCode" : "ding123132",
  "clientId" : "ding123132",
  "clientSecret" : "ada*****des",
  "unifiedAppId" : "3gsdxxxxxd56h"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | userid / orgId / appName / robotName / desc 任一为空 | 参数错误 |
