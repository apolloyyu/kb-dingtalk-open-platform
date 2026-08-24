---
title: "获取审批钉盘空间信息"
source_url: "https://open.dingtalk.com/document/development/api-premiumgetattachmentspace"
namespace: "development"
slug: "api-premiumgetattachmentspace"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批钉盘空间&附件 > 获取审批钉盘空间信息"
doc_id: "zmtwIMbtVf"
updated_at: "2026-06-03 10:12:50"
---

> Source: https://open.dingtalk.com/document/development/api-premiumgetattachmentspace
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批钉盘空间&附件 > 获取审批钉盘空间信息
> Updated: 2026-06-03 10:12:50

# 获取审批钉盘空间信息

调用本接口，获取审批钉盘空间的ID并授予当前用户上传附件的权限。该接口支持支持离职人员获取，以满足企业离职审计等场景需求。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

建议开发者通过以下方式实现带附件的审批流程：

1. 调用本接口，获取钉盘空间的上传权限，并获取space\_id。
2. 根据审批钉盘空间spaceId，网页应用（H5微应用）/小程序，通过[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)获取钉盘附件file的信息。

   > **[!NOTE]**
   >
   > space\_id
   >
   > - 一个企业内审批附件钉盘space\_id是唯一的。
   > - 本接口有授权上传权限的作用。每次调用上传附件API接口前，建议使用上传操作人userId再调用一次本接口。
   > - 审批附件钉盘，属于企业钉盘的一部分，占用的是企业钉盘空间，但是审批附件钉盘空间和其中的文件在客户端内是不可见的。
3. 传递附件信息，调用[发起审批实例](0497-create-an-approval-instance.md)接口传递附件信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processInstances/spaces/infos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户的userId，支持离职人员。 |
| agentId | Long | 否 | 应用的agentId：   - 企业内部应用，可查看[基础信息-AgentId](https://open.dingtalk.com/document/development/basic-concepts-beta#884d363067bnq)信息。 - 第三方企业应用，可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取`agentid`参数值。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processInstances/spaces/infos/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "userId" : "user123",
  "agentId" : 8345000
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
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetAttachmentSpaceHeaders premiumGetAttachmentSpaceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetAttachmentSpaceHeaders();
        premiumGetAttachmentSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumGetAttachmentSpaceRequest premiumGetAttachmentSpaceRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumGetAttachmentSpaceRequest()
                .setUserId("user123")
                .setAgentId(8345000L);
        try {
            client.premiumGetAttachmentSpaceWithOptions(premiumGetAttachmentSpaceRequest, premiumGetAttachmentSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_get_attachment_space_headers = dingtalkworkflow__1__0_models.PremiumGetAttachmentSpaceHeaders()
        premium_get_attachment_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_attachment_space_request = dingtalkworkflow__1__0_models.PremiumGetAttachmentSpaceRequest(
            user_id='user123',
            agent_id=8345000
        )
        try:
            client.premium_get_attachment_space_with_options(premium_get_attachment_space_request, premium_get_attachment_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_get_attachment_space_headers = dingtalkworkflow__1__0_models.PremiumGetAttachmentSpaceHeaders()
        premium_get_attachment_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_get_attachment_space_request = dingtalkworkflow__1__0_models.PremiumGetAttachmentSpaceRequest(
            user_id='user123',
            agent_id=8345000
        )
        try:
            await client.premium_get_attachment_space_with_options_async(premium_get_attachment_space_request, premium_get_attachment_space_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetAttachmentSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumGetAttachmentSpaceRequest;
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
        $premiumGetAttachmentSpaceHeaders = new PremiumGetAttachmentSpaceHeaders([]);
        $premiumGetAttachmentSpaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumGetAttachmentSpaceRequest = new PremiumGetAttachmentSpaceRequest([
            "userId" => "user123",
            "agentId" => 8345000
        ]);
        try {
            $client->premiumGetAttachmentSpaceWithOptions($premiumGetAttachmentSpaceRequest, $premiumGetAttachmentSpaceHeaders, new RuntimeOptions([]));
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

  premiumGetAttachmentSpaceHeaders := &dingtalkworkflow_1_0.PremiumGetAttachmentSpaceHeaders{}
  premiumGetAttachmentSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumGetAttachmentSpaceRequest := &dingtalkworkflow_1_0.PremiumGetAttachmentSpaceRequest{
    UserId: tea.String("user123"),
    AgentId: tea.Int64(8345000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumGetAttachmentSpaceWithOptions(premiumGetAttachmentSpaceRequest, premiumGetAttachmentSpaceHeaders, &util.RuntimeOptions{})
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
    let premiumGetAttachmentSpaceHeaders = new dingtalkworkflow_1_0.PremiumGetAttachmentSpaceHeaders({ });
    premiumGetAttachmentSpaceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumGetAttachmentSpaceRequest = new dingtalkworkflow_1_0.PremiumGetAttachmentSpaceRequest({
      userId: 'user123',
      agentId: 8345000,
    });
    try {
      await client.premiumGetAttachmentSpaceWithOptions(premiumGetAttachmentSpaceRequest, premiumGetAttachmentSpaceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetAttachmentSpaceHeaders premiumGetAttachmentSpaceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetAttachmentSpaceHeaders();
            premiumGetAttachmentSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetAttachmentSpaceRequest premiumGetAttachmentSpaceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumGetAttachmentSpaceRequest
            {
                UserId = "user123",
                AgentId = 8345000,
            };
            try
            {
                client.PremiumGetAttachmentSpaceWithOptions(premiumGetAttachmentSpaceRequest, premiumGetAttachmentSpaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| spaceId | Long | 钉盘空间ID。 |
| success | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "spaceId" : 3996960664
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 获取审批钉盘空间信息参数错误 | 获取审批钉盘空间信息参数错误 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | noPermission | 无权访问，企业没有开通相应的微应用 | 无权访问，企业没有开通相应的微应用 |
| 400 | invalidUserId | 获取审批钉盘空间信息，用户userId不能为空 | 获取审批钉盘空间信息，用户userId不能为空 |
| 400 | invalidAgentId | 获取审批钉盘空间信息，应用agentId不能为空 | 获取审批钉盘空间信息，应用agentId不能为空 |
| 400 | invalidParameterCspace | 使用授权码方式认证时，isvOrgId不能为空 | 使用授权码方式认证时，isvOrgId不能为空 |
| 400 | hsfIntegrationErrorCspaceGetCustomSpace | 获取钉盘space的信息失败 | 获取钉盘space的信息失败 |
| 400 | hsfIntegrationErrorCspaceGetSimpleMicroAppByRelatedAppId | 根据relatedAppId查询获取微应用信息失败 | 根据relatedAppId查询获取微应用信息失败 |
| 400 | hsfIntegrationErrorCspaceDentryServiceGrant | 授权访问钉盘失败 | 授权访问钉盘失败 |
| 400 | hsfIntegrationErrorCspace | 钉盘附件依赖三方错误 | 钉盘附件依赖三方错误 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 接口访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期，请开通/续费OA高级版 | 权益校验失败 |
| 400 | benefit.query.error | 权益查询失败，请稍后重试 | 权益查询失败 |
| 500 | systemError | 系统异常 | 系统异常 |
