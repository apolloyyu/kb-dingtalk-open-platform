---
title: "更新文件或文件夹的应用属性"
source_url: "https://open.dingtalk.com/document/development/update-file-application-properties"
namespace: "development"
slug: "update-file-application-properties"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 更新文件或文件夹的应用属性"
doc_id: "iHx8zmQiCu"
updated_at: "2026-06-04 19:09:35"
---

> Source: https://open.dingtalk.com/document/development/update-file-application-properties
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 更新文件或文件夹的应用属性
> Updated: 2026-06-04 19:09:35

# 更新文件或文件夹的应用属性

调用本接口，更新文件或文件夹的应用属性。

## **接口调用说明**

接口传入的应用属性信息，会根据属性名称校验。

- 如果文件或文件夹原有属性名与接口参数传入的属性名相同，接口执行更新属性。
- 如果文件或文件夹原有属性名与接口参数传入的属性名不相同，接口执行添加属性。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/appProperties |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Write-企业存储文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | Long | 是 | 空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| dentryId | Long | 是 | 文件或文件夹的id，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)或[根据dentryUuid获取spaceId和dentryId](0673-api-getdentryidbyuuid.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appProperties | Array | 是 | 应用属性列表，最大值3。 |
| name | String | 是 | 属性名称。       - 如果属性名称已存在，会更新原有的属性信息。 - 如果属性名称不存在，会添加该属性信息。 |
| value | String | 是 | 属性值。 |
| visibility | String | 是 | 属性可见范围。   - **PUBLIC**：该属性所有App可见 - **PRIVATE**：该属性仅其归属App可见，默认值 |

### 请求示例

HTTP

```
PUT /v1.0/storage/spaces/854xxxxx/dentries/634xxxxx/appProperties?unionId=cHtUxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "appProperties" : [ {
    "name" : "属性1",
    "value" : "属性值1",
    "visibility" : "PRIVATE"
  } ]
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
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.UpdateDentryAppPropertiesHeaders updateDentryAppPropertiesHeaders = new com.aliyun.dingtalkstorage_1_0.models.UpdateDentryAppPropertiesHeaders();
        updateDentryAppPropertiesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.UpdateDentryAppPropertiesRequest.UpdateDentryAppPropertiesRequestAppProperties appProperties0 = new com.aliyun.dingtalkstorage_1_0.models.UpdateDentryAppPropertiesRequest.UpdateDentryAppPropertiesRequestAppProperties()
                .setName("属性1")
                .setValue("属性值1")
                .setVisibility("PRIVATE");
        com.aliyun.dingtalkstorage_1_0.models.UpdateDentryAppPropertiesRequest updateDentryAppPropertiesRequest = new com.aliyun.dingtalkstorage_1_0.models.UpdateDentryAppPropertiesRequest()
                .setUnionId("cHtUxxxxx")
                .setAppProperties(java.util.Arrays.asList(
                    appProperties0
                ));
        try {
            client.updateDentryAppPropertiesWithOptions("", "", updateDentryAppPropertiesRequest, updateDentryAppPropertiesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.storage_1_0.client import Client as dingtalkstorage_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_1_0 import models as dingtalkstorage__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_dentry_app_properties_headers = dingtalkstorage__1__0_models.UpdateDentryAppPropertiesHeaders()
        update_dentry_app_properties_headers.x_acs_dingtalk_access_token = '<your access token>'
        app_properties_0 = dingtalkstorage__1__0_models.UpdateDentryAppPropertiesRequestAppProperties(
            name='属性1',
            value='属性值1',
            visibility='PRIVATE'
        )
        update_dentry_app_properties_request = dingtalkstorage__1__0_models.UpdateDentryAppPropertiesRequest(
            union_id='cHtUxxxxx',
            app_properties=[
                app_properties_0
            ]
        )
        try:
            client.update_dentry_app_properties_with_options('', '', update_dentry_app_properties_request, update_dentry_app_properties_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_dentry_app_properties_headers = dingtalkstorage__1__0_models.UpdateDentryAppPropertiesHeaders()
        update_dentry_app_properties_headers.x_acs_dingtalk_access_token = '<your access token>'
        app_properties_0 = dingtalkstorage__1__0_models.UpdateDentryAppPropertiesRequestAppProperties(
            name='属性1',
            value='属性值1',
            visibility='PRIVATE'
        )
        update_dentry_app_properties_request = dingtalkstorage__1__0_models.UpdateDentryAppPropertiesRequest(
            union_id='cHtUxxxxx',
            app_properties=[
                app_properties_0
            ]
        )
        try:
            await client.update_dentry_app_properties_with_options_async('', '', update_dentry_app_properties_request, update_dentry_app_properties_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdateDentryAppPropertiesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdateDentryAppPropertiesRequest\appProperties;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\UpdateDentryAppPropertiesRequest;
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
        $updateDentryAppPropertiesHeaders = new UpdateDentryAppPropertiesHeaders([]);
        $updateDentryAppPropertiesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $appProperties0 = new appProperties([
            "name" => "属性1",
            "value" => "属性值1",
            "visibility" => "PRIVATE"
        ]);
        $updateDentryAppPropertiesRequest = new UpdateDentryAppPropertiesRequest([
            "unionId" => "cHtUxxxxx",
            "appProperties" => [
                $appProperties0
            ]
        ]);
        try {
            $client->updateDentryAppPropertiesWithOptions("", "", $updateDentryAppPropertiesRequest, $updateDentryAppPropertiesHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
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
func CreateClient () (_result *dingtalkstorage_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_1_0.Client{}
  _result, _err = dingtalkstorage_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateDentryAppPropertiesHeaders := &dingtalkstorage_1_0.UpdateDentryAppPropertiesHeaders{}
  updateDentryAppPropertiesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  appProperties0 := &dingtalkstorage_1_0.UpdateDentryAppPropertiesRequestAppProperties{
    Name: tea.String("属性1"),
    Value: tea.String("属性值1"),
    Visibility: tea.String("PRIVATE"),
  }
  updateDentryAppPropertiesRequest := &dingtalkstorage_1_0.UpdateDentryAppPropertiesRequest{
    UnionId: tea.String("cHtUxxxxx"),
    AppProperties: []*dingtalkstorage_1_0.UpdateDentryAppPropertiesRequestAppProperties{appProperties0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateDentryAppPropertiesWithOptions(tea.String(""), tea.String(""), updateDentryAppPropertiesRequest, updateDentryAppPropertiesHeaders, &util.RuntimeOptions{})
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
const dingtalkstorage_1_0 = require('@alicloud/dingtalk/storage_1_0');
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
    return new dingtalkstorage_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateDentryAppPropertiesHeaders = new dingtalkstorage_1_0.UpdateDentryAppPropertiesHeaders({ });
    updateDentryAppPropertiesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let appProperties0 = new dingtalkstorage_1_0.UpdateDentryAppPropertiesRequestAppProperties({
      name: '属性1',
      value: '属性值1',
      visibility: 'PRIVATE',
    });
    let updateDentryAppPropertiesRequest = new dingtalkstorage_1_0.UpdateDentryAppPropertiesRequest({
      unionId: 'cHtUxxxxx',
      appProperties: [
        appProperties0
      ],
    });
    try {
      await client.updateDentryAppPropertiesWithOptions('', '', updateDentryAppPropertiesRequest, updateDentryAppPropertiesHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesHeaders updateDentryAppPropertiesHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesHeaders();
            updateDentryAppPropertiesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesRequest.UpdateDentryAppPropertiesRequestAppProperties appProperties0 = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesRequest.UpdateDentryAppPropertiesRequestAppProperties
            {
                Name = "属性1",
                Value = "属性值1",
                Visibility = "PRIVATE",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesRequest updateDentryAppPropertiesRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesRequest
            {
                UnionId = "cHtUxxxxx",
                AppProperties = new List<AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.UpdateDentryAppPropertiesRequest.UpdateDentryAppPropertiesRequestAppProperties>
                {
                    appProperties0
                },
            };
            try
            {
                client.UpdateDentryAppPropertiesWithOptions("", "", updateDentryAppPropertiesRequest, updateDentryAppPropertiesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 本次更新是否成功。   - **true**：成功 - **false**：失败 |

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
| 400 | operationConcurrentControl | %s | 并发控制 |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | dentryAppPropertiesNumberExceedsLimit | %s | dentry上单App设置属性的数量超出限制, 最大数量 3 |
| 403 | permissionDenied | %s | 用户缺少修改文件(夹)属性的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
