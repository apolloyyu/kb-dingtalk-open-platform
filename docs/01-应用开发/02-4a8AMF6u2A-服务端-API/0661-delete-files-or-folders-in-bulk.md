---
title: "批量删除文件或文件夹"
source_url: "https://open.dingtalk.com/document/development/delete-files-or-folders-in-bulk"
namespace: "development"
slug: "delete-files-or-folders-in-bulk"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 批量删除文件或文件夹"
doc_id: "iE870qKMmN"
updated_at: "2026-06-02 18:48:59"
---

> Source: https://open.dingtalk.com/document/development/delete-files-or-folders-in-bulk
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 批量删除文件或文件夹
> Updated: 2026-06-02 18:48:59

# 批量删除文件或文件夹

调用本接口，可实现批量删除文件或文件夹。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/batchRemove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Write-企业存储文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dentryIds | Array of String | 是 | 文件或文件夹ID列表，最多50个，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)或[根据dentryUuid获取spaceId和dentryId](0673-api-getdentryidbyuuid.md)接口获取id参数值。 |
| option | Object | 否 | 可选参数。 |
| toRecycleBin | Boolean | 否 | 是否删除到回收站。   - **true**：回收 - **false**（默认）：不回收，直接删除 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/457xxxxx/dentries/batchRemove?unionId=CHYxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "dentryIds" : [ "658xxxxx" ],
  "option" : {
    "toRecycleBin" : true
  }
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
        com.aliyun.dingtalkstorage_1_0.models.DeleteDentriesHeaders deleteDentriesHeaders = new com.aliyun.dingtalkstorage_1_0.models.DeleteDentriesHeaders();
        deleteDentriesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.DeleteDentriesRequest.DeleteDentriesRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.DeleteDentriesRequest.DeleteDentriesRequestOption()
                .setToRecycleBin(true);
        com.aliyun.dingtalkstorage_1_0.models.DeleteDentriesRequest deleteDentriesRequest = new com.aliyun.dingtalkstorage_1_0.models.DeleteDentriesRequest()
                .setUnionId("CHYxxxxx")
                .setDentryIds(java.util.Arrays.asList(
                    "658xxxxx"
                ))
                .setOption(option);
        try {
            client.deleteDentriesWithOptions("457xxxxx", deleteDentriesRequest, deleteDentriesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        delete_dentries_headers = dingtalkstorage__1__0_models.DeleteDentriesHeaders()
        delete_dentries_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.DeleteDentriesRequestOption(
            to_recycle_bin=True
        )
        delete_dentries_request = dingtalkstorage__1__0_models.DeleteDentriesRequest(
            union_id='CHYxxxxx',
            dentry_ids=[
                '658xxxxx'
            ],
            option=option
        )
        try:
            client.delete_dentries_with_options('457xxxxx', delete_dentries_request, delete_dentries_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_dentries_headers = dingtalkstorage__1__0_models.DeleteDentriesHeaders()
        delete_dentries_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.DeleteDentriesRequestOption(
            to_recycle_bin=True
        )
        delete_dentries_request = dingtalkstorage__1__0_models.DeleteDentriesRequest(
            union_id='CHYxxxxx',
            dentry_ids=[
                '658xxxxx'
            ],
            option=option
        )
        try:
            await client.delete_dentries_with_options_async('457xxxxx', delete_dentries_request, delete_dentries_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteDentriesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteDentriesRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteDentriesRequest;
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
        $deleteDentriesHeaders = new DeleteDentriesHeaders([]);
        $deleteDentriesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "toRecycleBin" => true
        ]);
        $deleteDentriesRequest = new DeleteDentriesRequest([
            "unionId" => "CHYxxxxx",
            "dentryIds" => [
                "658xxxxx"
            ],
            "option" => $option
        ]);
        try {
            $client->deleteDentriesWithOptions("457xxxxx", $deleteDentriesRequest, $deleteDentriesHeaders, new RuntimeOptions([]));
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

  deleteDentriesHeaders := &dingtalkstorage_1_0.DeleteDentriesHeaders{}
  deleteDentriesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.DeleteDentriesRequestOption{
    ToRecycleBin: tea.Bool(true),
  }
  deleteDentriesRequest := &dingtalkstorage_1_0.DeleteDentriesRequest{
    UnionId: tea.String("CHYxxxxx"),
    DentryIds: []*string{tea.String("658xxxxx")},
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteDentriesWithOptions(tea.String("457xxxxx"), deleteDentriesRequest, deleteDentriesHeaders, &util.RuntimeOptions{})
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
    let deleteDentriesHeaders = new dingtalkstorage_1_0.DeleteDentriesHeaders({ });
    deleteDentriesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let option = new dingtalkstorage_1_0.DeleteDentriesRequestOption({
      toRecycleBin: true,
    });
    let deleteDentriesRequest = new dingtalkstorage_1_0.DeleteDentriesRequest({
      unionId: 'CHYxxxxx',
      dentryIds: [
        '658xxxxx'
      ],
      option: option,
    });
    try {
      await client.deleteDentriesWithOptions('457xxxxx', deleteDentriesRequest, deleteDentriesHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentriesHeaders deleteDentriesHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentriesHeaders();
            deleteDentriesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentriesRequest.DeleteDentriesRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentriesRequest.DeleteDentriesRequestOption
            {
                ToRecycleBin = true,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentriesRequest deleteDentriesRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentriesRequest
            {
                UnionId = "CHYxxxxx",
                DentryIds = new List<string>
                {
                    "658xxxxx"
                },
                Option = option,
            };
            try
            {
                client.DeleteDentriesWithOptions("457xxxxx", deleteDentriesRequest, deleteDentriesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| resultItems | Array | 批量删除文件结果列表。 |
| spaceId | String | 源文件或文件夹的空间ID。 |
| dentryId | String | 源文件或文件夹的ID。 |
| async | Boolean | 是否是异步任务。   - **true**：是 - **false**：否   **[!NOTE]**    如果操作对象有子节点，则会异步处理。 |
| success | Boolean | 是否成功。   - **true**：成功 - **false**：失败   **[!NOTE]**    如果为异步任务，该字段为空。 |
| errorCode | String | 错误原因。  **[!NOTE]**    如果为异步任务，该字段为空。 |
| taskId | String | 异步任务ID，可用于查询任务执行状态。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "resultItems" : [ {
    "spaceId" : "654xxxxx",
    "dentryId" : "655xxxxx",
    "async" : true,
    "success" : true,
    "errorCode" : "permissionDenied",
    "taskId" : "123xxxx"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | operationConcurrentControl | %s | 并发控制 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryIds | %s | 参数错误-dentryIds |
| 400 | recycleBinNotSupportForSpace | %s | 空间不支持回收站 |
| 403 | permissionDenied | %s | 用户缺少删除文件(夹)的权限 |
| 403 | operationNotSupported | %s | 不支持删除到回收站 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
