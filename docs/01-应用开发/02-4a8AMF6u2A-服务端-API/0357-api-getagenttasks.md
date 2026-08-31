---
title: "获取代理列表"
source_url: "https://open.dingtalk.com/document/development/api-getagenttasks"
namespace: "development"
slug: "api-getagenttasks"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 平台管理 > 获取代理列表"
doc_id: "dA3ePqHdVO"
updated_at: "2026-08-07 10:21:09"
---

> Source: https://open.dingtalk.com/document/development/api-getagenttasks
> Path: 应用开发 / 服务端 API / 宜搭 > 平台管理 > 获取代理列表
> Updated: 2026-08-07 10:21:09

# 获取代理列表

调用本接口，批量查询代理关系列表，可指定代理人和被代理人的userId查询，也可指定代理关系的状态查询。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/yida/forms/resources/agents |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Yida.PlatformResource.Read-宜搭平台资源读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageSize | Integer | 否 | 分页大小，默认每页10条。 |
| pageNumber | Integer | 否 | 当前查询页码，默认第1页。 |
| corpId | String | 是 | 组织的corpId。 |
| userId | String | 是 | 用户的userid。 |
| token | String | 是 | 验权token。校验方式如下：`md5(corpId + userId + corpToken)`。md5取32位大写值。  **[!NOTE]**  每个企业有自己的唯一corpToken。 |
| keywords | String | 否 | 指定userId查询代理关系列表，按代理人或被代理人的userId搜索。 |
| status | String | 否 | 按代理关系的状态筛选：   - **ALL**：全部 - **DIS**：待生效 - **EFF**：代理中 - **OUT**：已过期 - **CANCEL**：已撤销 |
| agentUuid | String | 否 | 代理的唯一标识。 |

### **请求示例**

HTTP

```
GET /v2.0/yida/forms/resources/agents?pageSize=10&pageNumber=1&corpId=dingxxxx&userId=manager123&token=IASUDYxxx&keywords=10001&status=ALL HTTP/1.1
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
        com.aliyun.dingtalkyida_2_0.models.GetAgentTasksHeaders getAgentTasksHeaders = new com.aliyun.dingtalkyida_2_0.models.GetAgentTasksHeaders();
        getAgentTasksHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkyida_2_0.models.GetAgentTasksRequest getAgentTasksRequest = new com.aliyun.dingtalkyida_2_0.models.GetAgentTasksRequest()
                .setPageSize(10)
                .setPageNumber(1)
                .setCorpId("dingxxxx")
                .setUserId("manager123")
                .setToken("IASUDYxxx")
                .setKeywords("10001")
                .setStatus("ALL");
        try {
            client.getAgentTasksWithOptions(getAgentTasksRequest, getAgentTasksHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_agent_tasks_headers = dingtalkyida__2__0_models.GetAgentTasksHeaders()
        get_agent_tasks_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_agent_tasks_request = dingtalkyida__2__0_models.GetAgentTasksRequest(
            page_size=10,
            page_number=1,
            corp_id='dingxxxx',
            user_id='manager123',
            token='IASUDYxxx',
            keywords='10001',
            status='ALL'
        )
        try:
            client.get_agent_tasks_with_options(get_agent_tasks_request, get_agent_tasks_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_agent_tasks_headers = dingtalkyida__2__0_models.GetAgentTasksHeaders()
        get_agent_tasks_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_agent_tasks_request = dingtalkyida__2__0_models.GetAgentTasksRequest(
            page_size=10,
            page_number=1,
            corp_id='dingxxxx',
            user_id='manager123',
            token='IASUDYxxx',
            keywords='10001',
            status='ALL'
        )
        try:
            await client.get_agent_tasks_with_options_async(get_agent_tasks_request, get_agent_tasks_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\GetAgentTasksHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\GetAgentTasksRequest;
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
        $getAgentTasksHeaders = new GetAgentTasksHeaders([]);
        $getAgentTasksHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getAgentTasksRequest = new GetAgentTasksRequest([
            "pageSize" => 10,
            "pageNumber" => 1,
            "corpId" => "dingxxxx",
            "userId" => "manager123",
            "token" => "IASUDYxxx",
            "keywords" => "10001",
            "status" => "ALL"
        ]);
        try {
            $client->getAgentTasksWithOptions($getAgentTasksRequest, $getAgentTasksHeaders, new RuntimeOptions([]));
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

  getAgentTasksHeaders := &dingtalkyida_2_0.GetAgentTasksHeaders{}
  getAgentTasksHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getAgentTasksRequest := &dingtalkyida_2_0.GetAgentTasksRequest{
    PageSize: tea.Int32(10),
    PageNumber: tea.Int32(1),
    CorpId: tea.String("dingxxxx"),
    UserId: tea.String("manager123"),
    Token: tea.String("IASUDYxxx"),
    Keywords: tea.String("10001"),
    Status: tea.String("ALL"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAgentTasksWithOptions(getAgentTasksRequest, getAgentTasksHeaders, &util.RuntimeOptions{})
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
    let getAgentTasksHeaders = new dingtalkyida_2_0.GetAgentTasksHeaders({ });
    getAgentTasksHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getAgentTasksRequest = new dingtalkyida_2_0.GetAgentTasksRequest({
      pageSize: 10,
      pageNumber: 1,
      corpId: 'dingxxxx',
      userId: 'manager123',
      token: 'IASUDYxxx',
      keywords: '10001',
      status: 'ALL',
    });
    try {
      await client.getAgentTasksWithOptions(getAgentTasksRequest, getAgentTasksHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetAgentTasksHeaders getAgentTasksHeaders = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetAgentTasksHeaders();
            getAgentTasksHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetAgentTasksRequest getAgentTasksRequest = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.GetAgentTasksRequest
            {
                PageSize = 10,
                PageNumber = 1,
                CorpId = "dingxxxx",
                UserId = "manager123",
                Token = "IASUDYxxx",
                Keywords = "10001",
                Status = "ALL",
            };
            try
            {
                client.GetAgentTasksWithOptions(getAgentTasksRequest, getAgentTasksHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| values | Array | 返回的代理关系列表。 |
| creator | String | 代理创建人的userId。 |
| creatorName | String | 代理创建人的名称。 |
| agentCreateGMT | String | 代理创建时间，遵循ISO 8601格式，如：2025-10-22T11:06Z。 |
| agentUserId | String | 代理人的userId。 |
| agentName | String | 代理人的名称。 |
| principalUserId | String | 被代理人的userId。 |
| principalName | String | 被代理人的名称。 |
| agentStartGMT | String | 代理生效时间，遵循ISO 8601格式，如：2025-10-22T11:06Z。 |
| agentEndGMT | String | 代理过期时间，遵循ISO 8601格式，如：2025-10-22T11:06Z。 |
| agentType | String | 代理类型。   - **NORMAL**：普通代理 - **DEPARTURE** ：离职代理 |
| status | String | 代理状态：   - **DIS**：待生效 - **EFF**：代理中 - **OUT**：已过期 - **CANCEL**：已撤销 |
| agentUuid | String | 代理唯一标识。 |
| agentCategory | String | 代理类别。   - **STAR**：待提交流程 - **EXECUTE**：待处理流程 |
| agentRangeType | String | 代理范围的类型。   - **ALL**：全部流程 - **PART**：部分流程 |
| agentRangeValue | String | 代理范围的详细内容，代理全部流程时无值，仅指定代理部分流程时有值。如指定代理某应用下的表单：[{"appType":"APP\_XXX","formUuid":"FORM-XXX"}] |
| modifier | String | 代理修改人userId。 |
| needNoticePrincipal | String | 代理生效期间，被代理任务的审批通知是否需要发给被代理人（原审批人是否需要收到通知）。   - **y**：是，代理人和被代理人均会收到通知和待办。 - **n**：否，代理人会收到通知和待办，不再通知被代理人。 |
| start | Integer | 当前查询起始位置。 |
| limit | Integer | 每页查询条数。 |
| totalCount | Integer | 查询记录的总数。 |
| currentPage | Integer | 当前页码。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "values" : [ {
    "creator" : "10001",
    "creatorName" : "张三",
    "agentCreateGMT" : "2025-10-22T11:06Z",
    "agentUserId" : "10001",
    "agentName" : "李四",
    "principalUserId" : "10001",
    "principalName" : "王五",
    "agentStartGMT" : "2025-10-22T11:06Z",
    "agentEndGMT" : "2025-10-22T11:06Z",
    "agentType" : "ALL",
    "status" : "EFF",
    "agentUuid" : "Agent--XXXXX",
    "agentCategory" : "EXECUTE",
    "agentRangeType" : "ALL",
    "agentRangeValue" : "[{\"appType\":\"APP_XXX\",\"formUuid\":\"FORM-XXX\"}]",
    "modifier" : "10001",
    "needNoticePrincipal" : "y"
  } ],
  "start" : 0,
  "limit" : 10,
  "totalCount" : 1024,
  "currentPage" : 1
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
