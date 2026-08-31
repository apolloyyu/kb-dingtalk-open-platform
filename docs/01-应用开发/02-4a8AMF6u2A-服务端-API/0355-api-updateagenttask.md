---
title: "修改代理信息"
source_url: "https://open.dingtalk.com/document/development/api-updateagenttask"
namespace: "development"
slug: "api-updateagenttask"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 平台管理 > 修改代理信息"
doc_id: "7ViuGS1iE2"
updated_at: "2026-08-07 14:50:57"
---

> Source: https://open.dingtalk.com/document/development/api-updateagenttask
> Path: 应用开发 / 服务端 API / 宜搭 > 平台管理 > 修改代理信息
> Updated: 2026-08-07 14:50:57

# 修改代理信息

调用本接口，根据代理关系唯一标识（agentUuid）修改指定代理的配置信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/yida/forms/resources/agents/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Yida.PlatformResource.Write-宜搭平台资源写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织的corpId。 |
| userId | String | 是 | 用户的userid。 |
| token | String | 是 | 验权token。校验方式如下：`md5(corpId + userId + corpToken)`。md5取32位大写值。  **[!NOTE]**  每个企业有自己的唯一corpToken。 |
| agentUuid | String | 是 | 代理关系唯一标识，可通过[获取代理列表](0357-api-getagenttasks.md)接口获取。 |
| agentUserId | String | 是 | 代理人的userid。 |
| startTimestamp | String | 否 | 代理生效时间。  **[!NOTE]**  时间戳格式，单位为毫秒。 |
| endTimestamp | String | 否 | 代理过期时间。  **[!NOTE]**  时间戳格式，单位为毫秒。 |
| agentRangeType | String | 否 | 代理范围的类型。   - **ALL**：全部流程 - **PART**：部分流程 |
| agentRangeValue | String | 否 | 代理范围的详细内容。  **[!NOTE]**  如指定代理某应用下的表单：  `[{"appType":"APP_XXX","formUuid":"FORM-XXX"}]` |
| needNoticePrincipal | String | 否 | 代理生效期间，被代理任务的审批通知是否需要发给被代理人（原审批人是否需要收到通知）。   - **y**：是，代理人和被代理人均会收到通知和待办。 - **n**：否，代理人会收到通知和待办，不再通知被代理人。 |

### **请求示例**

HTTP

```
POST /v2.0/yida/forms/resources/agents/update?corpId=dingxxxx&userId=manager123&token=IASUDYxxx&agentUuid=Agent--xxxxx&agentUserId=10001&startTimestamp=1761204600404&endTimestamp=1761204600404&agentRangeType=ALL&agentRangeValue=[{"appType":"APP_XXX","formUuid":"FORM-XXX"}]&needNoticePrincipal=y HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:tokenskjhkjkxx
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
    public static com.aliyun.dingtalkyida_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkyida_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkyida_2_0.models.UpdateAgentTaskHeaders updateAgentTaskHeaders = new com.aliyun.dingtalkyida_2_0.models.UpdateAgentTaskHeaders();
        updateAgentTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkyida_2_0.models.UpdateAgentTaskRequest updateAgentTaskRequest = new com.aliyun.dingtalkyida_2_0.models.UpdateAgentTaskRequest()
                .setCorpId("dingxxxx")
                .setUserId("manager123")
                .setToken("IASUDYxxx")
                .setAgentUuid("Agent--xxxxx")
                .setAgentUserId("10001")
                .setStartTimestamp("1761204600404")
                .setEndTimestamp("1761204600404")
                .setAgentRangeType("ALL")
                .setAgentRangeValue("[{\"appType\":\"APP_XXX\",\"formUuid\":\"FORM-XXX\"}]")
                .setNeedNoticePrincipal("y");
        try {
            client.updateAgentTaskWithOptions(updateAgentTaskRequest, updateAgentTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.yida_2_0.client import Client as dingtalkyida_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_2_0 import models as dingtalkyida__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_agent_task_headers = dingtalkyida__2__0_models.UpdateAgentTaskHeaders()
        update_agent_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_agent_task_request = dingtalkyida__2__0_models.UpdateAgentTaskRequest(
            corp_id='dingxxxx',
            user_id='manager123',
            token='IASUDYxxx',
            agent_uuid='Agent--xxxxx',
            agent_user_id='10001',
            start_timestamp='1761204600404',
            end_timestamp='1761204600404',
            agent_range_type='ALL',
            agent_range_value='[{"appType":"APP_XXX","formUuid":"FORM-XXX"}]',
            need_notice_principal='y'
        )
        try:
            client.update_agent_task_with_options(update_agent_task_request, update_agent_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_agent_task_headers = dingtalkyida__2__0_models.UpdateAgentTaskHeaders()
        update_agent_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_agent_task_request = dingtalkyida__2__0_models.UpdateAgentTaskRequest(
            corp_id='dingxxxx',
            user_id='manager123',
            token='IASUDYxxx',
            agent_uuid='Agent--xxxxx',
            agent_user_id='10001',
            start_timestamp='1761204600404',
            end_timestamp='1761204600404',
            agent_range_type='ALL',
            agent_range_value='[{"appType":"APP_XXX","formUuid":"FORM-XXX"}]',
            need_notice_principal='y'
        )
        try:
            await client.update_agent_task_with_options_async(update_agent_task_request, update_agent_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\UpdateAgentTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\UpdateAgentTaskRequest;
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
        $updateAgentTaskHeaders = new UpdateAgentTaskHeaders([]);
        $updateAgentTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateAgentTaskRequest = new UpdateAgentTaskRequest([
            "corpId" => "dingxxxx",
            "userId" => "manager123",
            "token" => "IASUDYxxx",
            "agentUuid" => "Agent--xxxxx",
            "agentUserId" => "10001",
            "startTimestamp" => "1761204600404",
            "endTimestamp" => "1761204600404",
            "agentRangeType" => "ALL",
            "agentRangeValue" => "[{\"appType\":\"APP_XXX\",\"formUuid\":\"FORM-XXX\"}]",
            "needNoticePrincipal" => "y"
        ]);
        try {
            $client->updateAgentTaskWithOptions($updateAgentTaskRequest, $updateAgentTaskHeaders, new RuntimeOptions([]));
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
  dingtalkyida_2_0  "github.com/alibabacloud-go/dingtalk/yida_2_0"
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
func CreateClient () (_result *dingtalkyida_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_2_0.Client{}
  _result, _err = dingtalkyida_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateAgentTaskHeaders := &dingtalkyida_2_0.UpdateAgentTaskHeaders{}
  updateAgentTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateAgentTaskRequest := &dingtalkyida_2_0.UpdateAgentTaskRequest{
    CorpId: tea.String("dingxxxx"),
    UserId: tea.String("manager123"),
    Token: tea.String("IASUDYxxx"),
    AgentUuid: tea.String("Agent--xxxxx"),
    AgentUserId: tea.String("10001"),
    StartTimestamp: tea.String("1761204600404"),
    EndTimestamp: tea.String("1761204600404"),
    AgentRangeType: tea.String("ALL"),
    AgentRangeValue: tea.String("[{\"appType\":\"APP_XXX\",\"formUuid\":\"FORM-XXX\"}]"),
    NeedNoticePrincipal: tea.String("y"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateAgentTaskWithOptions(updateAgentTaskRequest, updateAgentTaskHeaders, &util.RuntimeOptions{})
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
const dingtalkyida_2_0 = require('@alicloud/dingtalk/yida_2_0');
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
    return new dingtalkyida_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateAgentTaskHeaders = new dingtalkyida_2_0.UpdateAgentTaskHeaders({ });
    updateAgentTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateAgentTaskRequest = new dingtalkyida_2_0.UpdateAgentTaskRequest({
      corpId: 'dingxxxx',
      userId: 'manager123',
      token: 'IASUDYxxx',
      agentUuid: 'Agent--xxxxx',
      agentUserId: '10001',
      startTimestamp: '1761204600404',
      endTimestamp: '1761204600404',
      agentRangeType: 'ALL',
      agentRangeValue: '[{"appType":"APP_XXX","formUuid":"FORM-XXX"}]',
      needNoticePrincipal: 'y',
    });
    try {
      await client.updateAgentTaskWithOptions(updateAgentTaskRequest, updateAgentTaskHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateAgentTaskHeaders updateAgentTaskHeaders = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateAgentTaskHeaders();
            updateAgentTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateAgentTaskRequest updateAgentTaskRequest = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateAgentTaskRequest
            {
                CorpId = "dingxxxx",
                UserId = "manager123",
                Token = "IASUDYxxx",
                AgentUuid = "Agent--xxxxx",
                AgentUserId = "10001",
                StartTimestamp = "1761204600404",
                EndTimestamp = "1761204600404",
                AgentRangeType = "ALL",
                AgentRangeValue = "[{\"appType\":\"APP_XXX\",\"formUuid\":\"FORM-XXX\"}]",
                NeedNoticePrincipal = "y",
            };
            try
            {
                client.UpdateAgentTaskWithOptions(updateAgentTaskRequest, updateAgentTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口请求是否成功，true/false。 |
| errorMsg | String | 接口失败信息。 |
| errorCode | String | 接口失败错误码。 |
| result | Boolean | 是否成功更新了代理关系。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "errorMsg" : "接口失败信息",
  "errorCode" : "000000",
  "result" : true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | unclassifiedError | 宜搭未分类的异常信息:%s | 宜搭未分类的异常信息 |
| 500 | failure.user.userNotExist | 用户不存在:%s | 用户不存在 |
| 500 | invalidParameter.corp.corpNotExist | 企业不存在:%s | 企业不存在 |
| 500 | invalidState.authorization.invalidAuthorizationInformation | 无效的认证信息:%s | 无效的认证信息 |
| 500 | failure.operation.tooManyVisitors | 平台当前访问人数过多，请稍后重试:%s | 平台当前访问人数过多，请稍后重试 |
| 500 | invalidParameter.validation.parameterValidationFailed | 参数校验失败:%s | 参数校验失败 |
| 500 | noPermission.permission.deny | 没有权限:%s | 没有权限 |
