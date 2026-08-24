---
title: "设置权限继承模式"
source_url: "https://open.dingtalk.com/document/development/set-permission-inheritance-mode"
namespace: "development"
slug: "set-permission-inheritance-mode"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 权限管理 > 设置权限继承模式"
doc_id: "4SBiv7k5J6"
updated_at: "2026-06-08 11:40:28"
---

> Source: https://open.dingtalk.com/document/development/set-permission-inheritance-mode
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 权限管理 > 设置权限继承模式
> Updated: 2026-06-08 11:40:28

# 设置权限继承模式

调用本接口，根据文件uuid、操作者unionId和权限继承模式inheritance，设置权限的继承模式。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/storage/spaces/dentries/{dentryUuid}/permissions/inheritances |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.Permission.Write-企业存储授权信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dentryUuid | String | 是 | 文件uuid，可调用[搜索文件](0638-search-for-files.md)或[获取 dentryUuid 信息](0672-api-getuuidbydentryid.md)接口，获取返回参数`dentryUuid`字段。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| inheritance | String | 是 | 权限继承模式，枚举值：   - **PASS\_ON**：传递，当前文件(夹)会继承所有父节点的权限，然后结合当前文件(夹)上的权限，相同成员权限取最大。 - **BREAK**: 打断，权限的传递在当前节点做一个打断。        - 不支持OWNER和MANAGER的打断 - 默认权限继承模式 |

### 请求示例

HTTP

```
PUT /v2.0/storage/spaces/dentries/EpGBaxxxxxR35y/permissions/inheritances?unionId=tXguxxxxlLURAiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "inheritance" : "PASS_ON"
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
    public static com.aliyun.dingtalkstorage_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkstorage_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_2_0.models.SetPermissionInheritanceHeaders setPermissionInheritanceHeaders = new com.aliyun.dingtalkstorage_2_0.models.SetPermissionInheritanceHeaders();
        setPermissionInheritanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_2_0.models.SetPermissionInheritanceRequest setPermissionInheritanceRequest = new com.aliyun.dingtalkstorage_2_0.models.SetPermissionInheritanceRequest()
                .setUnionId("tXguxxxxlLURAiEiE")
                .setInheritance("PASS_ON");
        try {
            client.setPermissionInheritanceWithOptions("EpGBaxxxxxR35y", setPermissionInheritanceRequest, setPermissionInheritanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.storage_2_0.client import Client as dingtalkstorage_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_2_0 import models as dingtalkstorage__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        set_permission_inheritance_headers = dingtalkstorage__2__0_models.SetPermissionInheritanceHeaders()
        set_permission_inheritance_headers.x_acs_dingtalk_access_token = '<your access token>'
        set_permission_inheritance_request = dingtalkstorage__2__0_models.SetPermissionInheritanceRequest(
            union_id='tXguxxxxlLURAiEiE',
            inheritance='PASS_ON'
        )
        try:
            client.set_permission_inheritance_with_options('EpGBaxxxxxR35y', set_permission_inheritance_request, set_permission_inheritance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        set_permission_inheritance_headers = dingtalkstorage__2__0_models.SetPermissionInheritanceHeaders()
        set_permission_inheritance_headers.x_acs_dingtalk_access_token = '<your access token>'
        set_permission_inheritance_request = dingtalkstorage__2__0_models.SetPermissionInheritanceRequest(
            union_id='tXguxxxxlLURAiEiE',
            inheritance='PASS_ON'
        )
        try:
            await client.set_permission_inheritance_with_options_async('EpGBaxxxxxR35y', set_permission_inheritance_request, set_permission_inheritance_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SetPermissionInheritanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SetPermissionInheritanceRequest;
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
        $setPermissionInheritanceHeaders = new SetPermissionInheritanceHeaders([]);
        $setPermissionInheritanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $setPermissionInheritanceRequest = new SetPermissionInheritanceRequest([
            "unionId" => "tXguxxxxlLURAiEiE",
            "inheritance" => "PASS_ON"
        ]);
        try {
            $client->setPermissionInheritanceWithOptions("EpGBaxxxxxR35y", $setPermissionInheritanceRequest, $setPermissionInheritanceHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_2_0  "github.com/alibabacloud-go/dingtalk/storage_2_0"
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
func CreateClient () (_result *dingtalkstorage_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_2_0.Client{}
  _result, _err = dingtalkstorage_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  setPermissionInheritanceHeaders := &dingtalkstorage_2_0.SetPermissionInheritanceHeaders{}
  setPermissionInheritanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  setPermissionInheritanceRequest := &dingtalkstorage_2_0.SetPermissionInheritanceRequest{
    UnionId: tea.String("tXguxxxxlLURAiEiE"),
    Inheritance: tea.String("PASS_ON"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SetPermissionInheritanceWithOptions(tea.String("EpGBaxxxxxR35y"), setPermissionInheritanceRequest, setPermissionInheritanceHeaders, &util.RuntimeOptions{})
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
const dingtalkstorage_2_0 = require('@alicloud/dingtalk/storage_2_0');
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
    return new dingtalkstorage_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let setPermissionInheritanceHeaders = new dingtalkstorage_2_0.SetPermissionInheritanceHeaders({ });
    setPermissionInheritanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let setPermissionInheritanceRequest = new dingtalkstorage_2_0.SetPermissionInheritanceRequest({
      unionId: 'tXguxxxxlLURAiEiE',
      inheritance: 'PASS_ON',
    });
    try {
      await client.setPermissionInheritanceWithOptions('EpGBaxxxxxR35y', setPermissionInheritanceRequest, setPermissionInheritanceHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SetPermissionInheritanceHeaders setPermissionInheritanceHeaders = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SetPermissionInheritanceHeaders();
            setPermissionInheritanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SetPermissionInheritanceRequest setPermissionInheritanceRequest = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SetPermissionInheritanceRequest
            {
                UnionId = "tXguxxxxlLURAiEiE",
                Inheritance = "PASS_ON",
            };
            try
            {
                client.SetPermissionInheritanceWithOptions("EpGBaxxxxxR35y", setPermissionInheritanceRequest, setPermissionInheritanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 本次操作是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.dentryUuid | %s | 参数错误-dentryUuid |
| 400 | paramError.permissionInheritance | %s | 参数错误-permissionInheritance |
| 400 | permissionInheritanceUnsupportedForRootDentry | %s | 根目录不支持权限继承 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
