---
title: "删除文件或文件夹"
source_url: "https://open.dingtalk.com/document/development/delete-a-file-or-folder"
namespace: "development"
slug: "delete-a-file-or-folder"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 删除文件或文件夹"
doc_id: "7L5XgsBmT6"
updated_at: "2026-06-02 18:48:58"
---

> Source: https://open.dingtalk.com/document/development/delete-a-file-or-folder
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 删除文件或文件夹
> Updated: 2026-06-02 18:48:58

# 删除文件或文件夹

调用本接口，可以实现删除文件或文件夹。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId} |
| HTTP Method | DELETE |
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
| dentryId | String | 是 | 需要被删除的文件或文件夹Id，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)或[根据dentryUuid获取spaceId和dentryId](0673-api-getdentryidbyuuid.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| toRecycleBin | Boolean | 否 | 删除后，是否备份到回收站：   - **true**：是 - **false**：否，默认值   **[!NOTE]**    目前仅支持[新建空间](0634-new-space.md)接口创建的云盘空间内的文件和文件夹支持备份到回收站。 |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求示例

HTTP

```
DELETE /v1.0/storage/spaces/85xxxxx/dentries/456xxxxx?toRecycleBin=true&unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
        com.aliyun.dingtalkstorage_1_0.models.DeleteDentryHeaders deleteDentryHeaders = new com.aliyun.dingtalkstorage_1_0.models.DeleteDentryHeaders();
        deleteDentryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.DeleteDentryRequest deleteDentryRequest = new com.aliyun.dingtalkstorage_1_0.models.DeleteDentryRequest()
                .setToRecycleBin(true)
                .setUnionId("chyxxxxx");
        try {
            client.deleteDentryWithOptions("85xxxxx", "456xxxxx", deleteDentryRequest, deleteDentryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        delete_dentry_headers = dingtalkstorage__1__0_models.DeleteDentryHeaders()
        delete_dentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_dentry_request = dingtalkstorage__1__0_models.DeleteDentryRequest(
            to_recycle_bin=True,
            union_id='chyxxxxx'
        )
        try:
            client.delete_dentry_with_options('85xxxxx', '456xxxxx', delete_dentry_request, delete_dentry_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_dentry_headers = dingtalkstorage__1__0_models.DeleteDentryHeaders()
        delete_dentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_dentry_request = dingtalkstorage__1__0_models.DeleteDentryRequest(
            to_recycle_bin=True,
            union_id='chyxxxxx'
        )
        try:
            await client.delete_dentry_with_options_async('85xxxxx', '456xxxxx', delete_dentry_request, delete_dentry_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteDentryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteDentryRequest;
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
        $deleteDentryHeaders = new DeleteDentryHeaders([]);
        $deleteDentryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteDentryRequest = new DeleteDentryRequest([
            "toRecycleBin" => true,
            "unionId" => "chyxxxxx"
        ]);
        try {
            $client->deleteDentryWithOptions("85xxxxx", "456xxxxx", $deleteDentryRequest, $deleteDentryHeaders, new RuntimeOptions([]));
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

  deleteDentryHeaders := &dingtalkstorage_1_0.DeleteDentryHeaders{}
  deleteDentryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteDentryRequest := &dingtalkstorage_1_0.DeleteDentryRequest{
    ToRecycleBin: tea.Bool(true),
    UnionId: tea.String("chyxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteDentryWithOptions(tea.String("85xxxxx"), tea.String("456xxxxx"), deleteDentryRequest, deleteDentryHeaders, &util.RuntimeOptions{})
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
    let deleteDentryHeaders = new dingtalkstorage_1_0.DeleteDentryHeaders({ });
    deleteDentryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let deleteDentryRequest = new dingtalkstorage_1_0.DeleteDentryRequest({
      toRecycleBin: true,
      unionId: 'chyxxxxx',
    });
    try {
      await client.deleteDentryWithOptions('85xxxxx', '456xxxxx', deleteDentryRequest, deleteDentryHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentryHeaders deleteDentryHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentryHeaders();
            deleteDentryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentryRequest deleteDentryRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteDentryRequest
            {
                ToRecycleBin = true,
                UnionId = "chyxxxxx",
            };
            try
            {
                client.DeleteDentryWithOptions("85xxxxx", "456xxxxx", deleteDentryRequest, deleteDentryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| async | Boolean | 是否是异步任务。   - **true**：是 - **false**：否 |
| taskId | String | 任务Id，用于查询任务执行状态。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "async" : true,
  "taskId" : "task_id"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | operationConcurrentControl | %s | 并发控制 |
| 400 | paramError | %s | 参数错误 |
| 400 | recycleBinNotSupportForSpace | %s | 空间不支持回收站 |
| 403 | permissionDenied | %s | 用户缺少删除文件(夹)的权限 |
| 403 | operationNotSupported | %s | 不支持删除到回收站 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
