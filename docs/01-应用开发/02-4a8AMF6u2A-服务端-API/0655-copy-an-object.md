---
title: "复制文件或文件夹"
source_url: "https://open.dingtalk.com/document/development/copy-an-object"
namespace: "development"
slug: "copy-an-object"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 复制文件或文件夹"
doc_id: "lzISo9eG1L"
updated_at: "2026-06-02 18:46:46"
---

> Source: https://open.dingtalk.com/document/development/copy-an-object
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 复制文件或文件夹
> Updated: 2026-06-02 18:46:46

# 复制文件或文件夹

调用本接口，可实现复制文件或文件夹到其他空间或目录。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/copy |
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
| spaceId | String | 是 | 文件或文件夹所在的源空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| dentryId | String | 是 | 需要被复制的文件或文件夹Id，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)或[根据dentryUuid获取spaceId和dentryId](0673-api-getdentryidbyuuid.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| targetSpaceId | String | 是 | 需要存放的目标空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| targetFolderId | String | 是 | 需要存放的位置父目录Id，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取id参数值。 |
| option | Object | 否 | 可选参数。 |
| conflictStrategy | String | 否 | 文件和文件夹的名称冲突策略：   - **AUTO\_RENAME**（默认值）：自动重命名 - **OVERWRITE**：覆盖 - **RETURN\_DENTRY\_IF\_EXISTS**：返回已存在文件 - **RETURN\_ERROR\_IF\_EXISTS**：文件已存在时报错 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/space_id/dentries/dentry_id/copy?unionId=cHtUYxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "targetSpaceId" : "622xxxxx",
  "targetFolderId" : "532xxxxx",
  "option" : {
    "conflictStrategy" : "AUTO_RENAME"
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
        com.aliyun.dingtalkstorage_1_0.models.CopyDentryHeaders copyDentryHeaders = new com.aliyun.dingtalkstorage_1_0.models.CopyDentryHeaders();
        copyDentryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.CopyDentryRequest.CopyDentryRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.CopyDentryRequest.CopyDentryRequestOption()
                .setConflictStrategy("AUTO_RENAME");
        com.aliyun.dingtalkstorage_1_0.models.CopyDentryRequest copyDentryRequest = new com.aliyun.dingtalkstorage_1_0.models.CopyDentryRequest()
                .setUnionId("cHtUYxxxxx")
                .setTargetSpaceId("622xxxxx")
                .setTargetFolderId("532xxxxx")
                .setOption(option);
        try {
            client.copyDentryWithOptions("space_id", "dentry_id", copyDentryRequest, copyDentryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        copy_dentry_headers = dingtalkstorage__1__0_models.CopyDentryHeaders()
        copy_dentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.CopyDentryRequestOption(
            conflict_strategy='AUTO_RENAME'
        )
        copy_dentry_request = dingtalkstorage__1__0_models.CopyDentryRequest(
            union_id='cHtUYxxxxx',
            target_space_id='622xxxxx',
            target_folder_id='532xxxxx',
            option=option
        )
        try:
            client.copy_dentry_with_options('space_id', 'dentry_id', copy_dentry_request, copy_dentry_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        copy_dentry_headers = dingtalkstorage__1__0_models.CopyDentryHeaders()
        copy_dentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.CopyDentryRequestOption(
            conflict_strategy='AUTO_RENAME'
        )
        copy_dentry_request = dingtalkstorage__1__0_models.CopyDentryRequest(
            union_id='cHtUYxxxxx',
            target_space_id='622xxxxx',
            target_folder_id='532xxxxx',
            option=option
        )
        try:
            await client.copy_dentry_with_options_async('space_id', 'dentry_id', copy_dentry_request, copy_dentry_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CopyDentryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CopyDentryRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CopyDentryRequest;
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
        $copyDentryHeaders = new CopyDentryHeaders([]);
        $copyDentryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "conflictStrategy" => "AUTO_RENAME"
        ]);
        $copyDentryRequest = new CopyDentryRequest([
            "unionId" => "cHtUYxxxxx",
            "targetSpaceId" => "622xxxxx",
            "targetFolderId" => "532xxxxx",
            "option" => $option
        ]);
        try {
            $client->copyDentryWithOptions("space_id", "dentry_id", $copyDentryRequest, $copyDentryHeaders, new RuntimeOptions([]));
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

  copyDentryHeaders := &dingtalkstorage_1_0.CopyDentryHeaders{}
  copyDentryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.CopyDentryRequestOption{
    ConflictStrategy: tea.String("AUTO_RENAME"),
  }
  copyDentryRequest := &dingtalkstorage_1_0.CopyDentryRequest{
    UnionId: tea.String("cHtUYxxxxx"),
    TargetSpaceId: tea.String("622xxxxx"),
    TargetFolderId: tea.String("532xxxxx"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CopyDentryWithOptions(tea.String("space_id"), tea.String("dentry_id"), copyDentryRequest, copyDentryHeaders, &util.RuntimeOptions{})
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
    let copyDentryHeaders = new dingtalkstorage_1_0.CopyDentryHeaders({ });
    copyDentryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let option = new dingtalkstorage_1_0.CopyDentryRequestOption({
      conflictStrategy: 'AUTO_RENAME',
    });
    let copyDentryRequest = new dingtalkstorage_1_0.CopyDentryRequest({
      unionId: 'cHtUYxxxxx',
      targetSpaceId: '622xxxxx',
      targetFolderId: '532xxxxx',
      option: option,
    });
    try {
      await client.copyDentryWithOptions('space_id', 'dentry_id', copyDentryRequest, copyDentryHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CopyDentryHeaders copyDentryHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CopyDentryHeaders();
            copyDentryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CopyDentryRequest.CopyDentryRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CopyDentryRequest.CopyDentryRequestOption
            {
                ConflictStrategy = "AUTO_RENAME",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CopyDentryRequest copyDentryRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CopyDentryRequest
            {
                UnionId = "cHtUYxxxxx",
                TargetSpaceId = "622xxxxx",
                TargetFolderId = "532xxxxx",
                Option = option,
            };
            try
            {
                client.CopyDentryWithOptions("space_id", "dentry_id", copyDentryRequest, copyDentryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dentry | Object | 文件或文件夹信息列表。 |
| id | String | 文件或文件夹id。 |
| spaceId | String | 所在空间Id。 |
| parentId | String | 父目录Id。 |
| type | String | 类型：   - **FILE**：文件 - **FOLDER**：文件夹 |
| name | String | 文件或文件夹名称。 |
| size | Long | 文件大小，单位Byte。  **[!NOTE]**    文件夹不返回该字段。 |
| path | String | 路径。 |
| version | Long | 版本。 |
| status | String | 状态：   - **NORMAL**：正常 - **DELETED**：已删除 - **EXPIRED**：已过期 |
| extension | String | 文件后缀。  **[!NOTE]**    文件夹不返回该字段。 |
| creatorId | String | 创建者unionId。 |
| modifierId | String | 修改者unionId。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| properties | Object | 属性。 |
| readOnly | Boolean | 文件或文件夹是否只读：   - **true**：是 - **false**：否 |
| appProperties | Map<String, Array> | 在特定应用上的属性。 |
|  | Array | 属性列表。 |
| name | String | 属性名称。 |
| value | String | 属性值。 |
| visibility | String | 属性可见性：   - **PUBLIC**：公开可见 - **PRIVATE**：仅当前空间可见 |
| uuid | String | 标识字段。 |
| partitionType | String | 存储分区：   - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属MiniOSS存储分区 |
| storageDriver | String | 驱动类型：   - **DINGTALK**：钉钉统一存储驱动 - **ALIDOC**：钉钉文档存储驱动 - **UNKNOWN**：未知驱动 |
| async | Boolean | 是否是异步任务：   - **true**：是 - **false**：否 |
| taskId | String | 任务Id，用于查询任务执行状态。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "dentry" : {
    "id" : "675xxxxx",
    "spaceId" : "883xxxxx",
    "parentId" : "654xxxxx",
    "type" : "FILE",
    "name" : "测试",
    "size" : 512,
    "path" : "/测试文件夹",
    "version" : 1,
    "status" : "NORMAL",
    "extension" : "txt",
    "creatorId" : "cHtUYxxxxx",
    "modifierId" : "cHtUYxxxxx",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "properties" : {
      "readOnly" : true
    },
    "appProperties" : [ {
      "name" : "属性名1",
      "value" : "属性值1",
      "visibility" : "PRIVATE"
    } ],
    "uuid" : "uuid",
    "partitionType" : "PUBLIC_OSS_PARTITION",
    "storageDriver" : "DINGTALK"
  },
  "async" : true,
  "taskId" : "1234xxxxx"
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
| 400 | paramError.targetSpaceId | %s | 参数错误-targetSpaceId |
| 400 | paramError.targetFolderId | %s | 参数错误-targetFolderId |
| 400 | paramError.conflictStrategy | %s | 参数错误-conflictStrategy |
| 400 | spaceQuotaInsufficient | %s | 空间容量不足 |
| 400 | sceneQuotaInsufficient | %s | 场景容量不足 |
| 400 | appQuotaInsufficient | %s | 应用容量不足 |
| 400 | orgQuotaInsufficient | %s | 企业容量不足 |
| 400 | dentryAlreadyExist | %s | 同名文件已存在 |
| 403 | permissionDenied | %s | 用户缺少拷贝文件(夹)的权限 |
| 404 | spaceNotExist | %s | 源文件(夹)或目标目录所在空间不存在 |
| 404 | dentryNotExist | %s | 源文件(夹)或目标目录不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
