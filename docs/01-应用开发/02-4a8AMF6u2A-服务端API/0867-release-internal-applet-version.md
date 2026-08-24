---
title: "发布企业内部小程序版本"
source_url: "https://open.dingtalk.com/document/development/release-internal-applet-version"
namespace: "development"
slug: "release-internal-applet-version"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉应用 > 版本管理 > 发布企业内部小程序版本"
doc_id: "6fsp57hl7j"
updated_at: "2026-06-04 19:10:07"
---

> Source: https://open.dingtalk.com/document/development/release-internal-applet-version
> Path: 应用开发 / 服务端API / 钉钉应用 > 版本管理 > 发布企业内部小程序版本
> Updated: 2026-06-04 19:10:07

# 发布企业内部小程序版本

通过本接口，管理员可灵活发布小程序的不同版本类型，支持线上版本和体验版本的发布，并可选择是否支持PC端访问，实现小程序版本的全生命周期管理。

## **接口调用说明**

只有企业内部小程序才能调用该接口获取数据，且当前小程序存在对应的版本信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/versions/publish |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-管理微应用的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | Long | 是 | 应用的AgentId，请参考[基础概念-AgentId](https://open.dingtalk.com/document/development/basic-concepts-beta#884d363067bnq)。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appVersionId | Long | 是 | 小程序版本id，用于唯一标识小程序版本信息，可调用[获取企业内部小程序的版本列表](0869-get-the-version-list-of-the-enterprise-internal-applet.md)接口，获取返回参数中 `appVersionId` 字段值。 |
| opUnionId | String | 是 | 操作人的unionId，该用户必须是拥有**应用管理权限**的管理员，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| publishType | String | 否 | 小程序发布类型，取值：   - **online**：发布线上版本 - **experience**：发布体验版本 |
| miniAppOnPc | Boolean | 否 | 是否支持PC端打开小程序，取值：   - **false**：只发布移动端 - **true**：既发布移动端又发布PC端       体验版本发布目前默认只支持移动端发布 |

### 请求示例

HTTP

```
POST /v1.0/microApp/innerMiniApps/1/versions/publish HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f2a6d208b64432df8eea4a9a937
Content-Type:application/json

{
  "appVersionId" : 1,
  "opUnionId" : "ez275xxx",
  "publishType" : "online",
  "miniAppOnPc" : false
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.PublishInnerAppVersionHeaders publishInnerAppVersionHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.PublishInnerAppVersionHeaders();
        publishInnerAppVersionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.PublishInnerAppVersionRequest publishInnerAppVersionRequest = new com.aliyun.dingtalkmicro_app_1_0.models.PublishInnerAppVersionRequest()
                .setAppVersionId(1L)
                .setOpUnionId("ez275xxx")
                .setPublishType("online")
                .setMiniAppOnPc(false);
        try {
            client.publishInnerAppVersionWithOptions("1", publishInnerAppVersionRequest, publishInnerAppVersionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        publish_inner_app_version_headers = dingtalkmicro_app__1__0_models.PublishInnerAppVersionHeaders()
        publish_inner_app_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        publish_inner_app_version_request = dingtalkmicro_app__1__0_models.PublishInnerAppVersionRequest(
            app_version_id=1,
            op_union_id='ez275xxx',
            publish_type='online',
            mini_app_on_pc=False
        )
        try:
            client.publish_inner_app_version_with_options('1', publish_inner_app_version_request, publish_inner_app_version_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        publish_inner_app_version_headers = dingtalkmicro_app__1__0_models.PublishInnerAppVersionHeaders()
        publish_inner_app_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        publish_inner_app_version_request = dingtalkmicro_app__1__0_models.PublishInnerAppVersionRequest(
            app_version_id=1,
            op_union_id='ez275xxx',
            publish_type='online',
            mini_app_on_pc=False
        )
        try:
            await client.publish_inner_app_version_with_options_async('1', publish_inner_app_version_request, publish_inner_app_version_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\PublishInnerAppVersionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\PublishInnerAppVersionRequest;
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
        $publishInnerAppVersionHeaders = new PublishInnerAppVersionHeaders([]);
        $publishInnerAppVersionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $publishInnerAppVersionRequest = new PublishInnerAppVersionRequest([
            "appVersionId" => 1,
            "opUnionId" => "ez275xxx",
            "publishType" => "online",
            "miniAppOnPc" => false
        ]);
        try {
            $client->publishInnerAppVersionWithOptions("1", $publishInnerAppVersionRequest, $publishInnerAppVersionHeaders, new RuntimeOptions([]));
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

  publishInnerAppVersionHeaders := &dingtalkmicroapp_1_0.PublishInnerAppVersionHeaders{}
  publishInnerAppVersionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  publishInnerAppVersionRequest := &dingtalkmicroapp_1_0.PublishInnerAppVersionRequest{
    AppVersionId: tea.Int64(1),
    OpUnionId: tea.String("ez275xxx"),
    PublishType: tea.String("online"),
    MiniAppOnPc: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PublishInnerAppVersionWithOptions(tea.String("1"), publishInnerAppVersionRequest, publishInnerAppVersionHeaders, &util.RuntimeOptions{})
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
    let publishInnerAppVersionHeaders = new dingtalkmicroApp_1_0.PublishInnerAppVersionHeaders({ });
    publishInnerAppVersionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let publishInnerAppVersionRequest = new dingtalkmicroApp_1_0.PublishInnerAppVersionRequest({
      appVersionId: 1,
      opUnionId: 'ez275xxx',
      publishType: 'online',
      miniAppOnPc: false,
    });
    try {
      await client.publishInnerAppVersionWithOptions('1', publishInnerAppVersionRequest, publishInnerAppVersionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PublishInnerAppVersionHeaders publishInnerAppVersionHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PublishInnerAppVersionHeaders();
            publishInnerAppVersionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PublishInnerAppVersionRequest publishInnerAppVersionRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PublishInnerAppVersionRequest
            {
                AppVersionId = 1,
                OpUnionId = "ez275xxx",
                PublishType = "online",
                MiniAppOnPc = false,
            };
            try
            {
                client.PublishInnerAppVersionWithOptions("1", publishInnerAppVersionRequest, publishInnerAppVersionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 小程序发布结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 400 | appTypeNotSupport | 只支持企业自建小程序调用 | 只支持企业自建小程序调用 |
| 400 | noAppManagePermission | 当前企业没有操作应用的权限 | 当前企业没有操作应用的权限 |
| 400 | invalidMiniVersion | 不合法的versionId | 不合法的versionId |
| 400 | preCheckError | 前置校验失败: %s | 前置校验失败 |
| 400 | invalidUser | 当前用户不在该组织下 | 当前用户不在该组织下 |
| 400 | noUserAuth | 当前用户无操作应用的权限 | 当前用户无操作应用的权限 |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
