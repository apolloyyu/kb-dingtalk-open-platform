---
title: "回滚企业内部小程序版本"
source_url: "https://open.dingtalk.com/document/development/rollback-of-enterprise-internal-applet-version"
namespace: "development"
slug: "rollback-of-enterprise-internal-applet-version"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉应用 > 版本管理 > 回滚企业内部小程序版本"
doc_id: "O5PR7dz4rL"
updated_at: "2026-06-03 11:47:36"
---

> Source: https://open.dingtalk.com/document/development/rollback-of-enterprise-internal-applet-version
> Path: 应用开发 / 服务端API / 钉钉应用 > 版本管理 > 回滚企业内部小程序版本
> Updated: 2026-06-03 11:47:36

# 回滚企业内部小程序版本

通过本接口，可将企业内部小程序回滚至指定的历史版本，实现版本的快速恢复与管理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/versions/rollback |
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
| agentId | Long | 是 | 应用AgentId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appVersionId | Long | 是 | 小程序版本ID，用于唯一标识一个历史版本。可通过调用[获取企业内部小程序历史版本列表](0870-obtain-the-list-of-historical-versions-of-enterprise-internal-applets.md)接口，在返回结果中获取`appVersionId`字段值。 |
| opUnionId | String | 是 | 操作人的unionId，必须为当前企业内拥有应用管理权限的有效管理员，可通过[查询用户详情](0056-query-user-details.md)接口获取`unionId`参数值。 |

### 请求示例

HTTP

```
POST /v1.0/microApp/innerMiniApps/1/versions/rollback HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:*****7e3a37b1ab3e69faed071024
Content-Type:application/json

{
  "appVersionId" : 2791149,
  "opUnionId" : "xxx"
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
        com.aliyun.dingtalkmicro_app_1_0.models.RollbackInnerAppVersionHeaders rollbackInnerAppVersionHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.RollbackInnerAppVersionHeaders();
        rollbackInnerAppVersionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.RollbackInnerAppVersionRequest rollbackInnerAppVersionRequest = new com.aliyun.dingtalkmicro_app_1_0.models.RollbackInnerAppVersionRequest()
                .setAppVersionId(2791149L)
                .setOpUnionId("xxx");
        try {
            client.rollbackInnerAppVersionWithOptions("1", rollbackInnerAppVersionRequest, rollbackInnerAppVersionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        rollback_inner_app_version_headers = dingtalkmicro_app__1__0_models.RollbackInnerAppVersionHeaders()
        rollback_inner_app_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        rollback_inner_app_version_request = dingtalkmicro_app__1__0_models.RollbackInnerAppVersionRequest(
            app_version_id=2791149,
            op_union_id='xxx'
        )
        try:
            client.rollback_inner_app_version_with_options('1', rollback_inner_app_version_request, rollback_inner_app_version_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        rollback_inner_app_version_headers = dingtalkmicro_app__1__0_models.RollbackInnerAppVersionHeaders()
        rollback_inner_app_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        rollback_inner_app_version_request = dingtalkmicro_app__1__0_models.RollbackInnerAppVersionRequest(
            app_version_id=2791149,
            op_union_id='xxx'
        )
        try:
            await client.rollback_inner_app_version_with_options_async('1', rollback_inner_app_version_request, rollback_inner_app_version_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\RollbackInnerAppVersionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\RollbackInnerAppVersionRequest;
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
        $rollbackInnerAppVersionHeaders = new RollbackInnerAppVersionHeaders([]);
        $rollbackInnerAppVersionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $rollbackInnerAppVersionRequest = new RollbackInnerAppVersionRequest([
            "appVersionId" => 2791149,
            "opUnionId" => "xxx"
        ]);
        try {
            $client->rollbackInnerAppVersionWithOptions("1", $rollbackInnerAppVersionRequest, $rollbackInnerAppVersionHeaders, new RuntimeOptions([]));
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

  rollbackInnerAppVersionHeaders := &dingtalkmicroapp_1_0.RollbackInnerAppVersionHeaders{}
  rollbackInnerAppVersionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  rollbackInnerAppVersionRequest := &dingtalkmicroapp_1_0.RollbackInnerAppVersionRequest{
    AppVersionId: tea.Int64(2791149),
    OpUnionId: tea.String("xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RollbackInnerAppVersionWithOptions(tea.String("1"), rollbackInnerAppVersionRequest, rollbackInnerAppVersionHeaders, &util.RuntimeOptions{})
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
    let rollbackInnerAppVersionHeaders = new dingtalkmicroApp_1_0.RollbackInnerAppVersionHeaders({ });
    rollbackInnerAppVersionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let rollbackInnerAppVersionRequest = new dingtalkmicroApp_1_0.RollbackInnerAppVersionRequest({
      appVersionId: 2791149,
      opUnionId: 'xxx',
    });
    try {
      await client.rollbackInnerAppVersionWithOptions('1', rollbackInnerAppVersionRequest, rollbackInnerAppVersionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.RollbackInnerAppVersionHeaders rollbackInnerAppVersionHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.RollbackInnerAppVersionHeaders();
            rollbackInnerAppVersionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.RollbackInnerAppVersionRequest rollbackInnerAppVersionRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.RollbackInnerAppVersionRequest
            {
                AppVersionId = 2791149,
                OpUnionId = "xxx",
            };
            try
            {
                client.RollbackInnerAppVersionWithOptions("1", rollbackInnerAppVersionRequest, rollbackInnerAppVersionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 小程序回滚结果。 |

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
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | invalidMiniVersion | 不合法的versionId | 不合法的versionId |
| 400 | preCheckError | 前置校验失败: %s | 前置校验失败 |
| 400 | invalidUser | 当前用户不在该组织下 | 当前用户不在该组织下 |
| 400 | noUserAuth | 当前用户无操作应用的权限 | 当前用户无操作应用的权限 |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
