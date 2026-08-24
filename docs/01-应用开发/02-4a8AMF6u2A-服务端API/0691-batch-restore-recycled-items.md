---
title: "批量还原回收项"
source_url: "https://open.dingtalk.com/document/development/batch-restore-recycled-items"
namespace: "development"
slug: "batch-restore-recycled-items"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 回收站管理 > 批量还原回收项"
doc_id: "cWs4Htpc7j"
updated_at: "2026-06-03 17:22:00"
---

> Source: https://open.dingtalk.com/document/development/batch-restore-recycled-items
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 回收站管理 > 批量还原回收项
> Updated: 2026-06-03 17:22:00

# 批量还原回收项

调用本接口，批量还原回收项。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/recycleBins/{recycleBinId}/recycleItems/batchRestore |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.RecycleBin.Write-钉盘应用回收站文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recycleBinId | String | 是 | 回收站ID，可调用[获取回收站信息](0687-obtain-information-about-the-recycle-bin.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recycleItemIds | Array of String | 是 | 回收项ID列表，调用[获取回收项列表](0688-gets-the-list-of-recycle-items.md)接口获取，最大值30。 |
| option | Object | 否 | 可选参数。 |
| conflictStrategy | String | 否 | 文件名称冲突策略，还原时原路径可能已经存在同名的文件。   - **AUTO\_RENAME**：自动重命名，默认值 - **OVERWRITE**：覆盖 - **RETURN\_DENTRY\_IF\_EXISTS**：返回已存在文件 - **RETURN\_ERROR\_IF\_EXISTS**：文件已存在时报错 |

### 请求示例

HTTP

```
POST /v1.0/storage/recycleBins/recyclebin_id/recycleItems/batchRestore?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "recycleItemIds" : [ "123xxxxx" ],
  "option" : {
    "conflictStrategy" : "AUTO_RENAME"
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.RestoreRecycleItemsHeaders restoreRecycleItemsHeaders = new com.aliyun.dingtalkstorage_1_0.models.RestoreRecycleItemsHeaders();
        restoreRecycleItemsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.RestoreRecycleItemsRequest.RestoreRecycleItemsRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.RestoreRecycleItemsRequest.RestoreRecycleItemsRequestOption()
                .setConflictStrategy("AUTO_RENAME");
        com.aliyun.dingtalkstorage_1_0.models.RestoreRecycleItemsRequest restoreRecycleItemsRequest = new com.aliyun.dingtalkstorage_1_0.models.RestoreRecycleItemsRequest()
                .setUnionId("chyxxxxx")
                .setRecycleItemIds(java.util.Arrays.asList(
                    "123xxxxx"
                ))
                .setOption(option);
        try {
            client.restoreRecycleItemsWithOptions("recyclebin_id", restoreRecycleItemsRequest, restoreRecycleItemsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import sys

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
        restore_recycle_items_headers = dingtalkstorage__1__0_models.RestoreRecycleItemsHeaders()
        restore_recycle_items_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.RestoreRecycleItemsRequestOption(
            conflict_strategy='AUTO_RENAME'
        )
        restore_recycle_items_request = dingtalkstorage__1__0_models.RestoreRecycleItemsRequest(
            union_id='chyxxxxx',
            recycle_item_ids=[
                '123xxxxx'
            ],
            option=option
        )
        try:
            client.restore_recycle_items_with_options('recyclebin_id', restore_recycle_items_request, restore_recycle_items_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        restore_recycle_items_headers = dingtalkstorage__1__0_models.RestoreRecycleItemsHeaders()
        restore_recycle_items_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.RestoreRecycleItemsRequestOption(
            conflict_strategy='AUTO_RENAME'
        )
        restore_recycle_items_request = dingtalkstorage__1__0_models.RestoreRecycleItemsRequest(
            union_id='chyxxxxx',
            recycle_item_ids=[
                '123xxxxx'
            ],
            option=option
        )
        try:
            await client.restore_recycle_items_with_options_async('recyclebin_id', restore_recycle_items_request, restore_recycle_items_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\RestoreRecycleItemsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\RestoreRecycleItemsRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\RestoreRecycleItemsRequest;
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
        $restoreRecycleItemsHeaders = new RestoreRecycleItemsHeaders([]);
        $restoreRecycleItemsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "conflictStrategy" => "AUTO_RENAME"
        ]);
        $restoreRecycleItemsRequest = new RestoreRecycleItemsRequest([
            "unionId" => "chyxxxxx",
            "recycleItemIds" => [
                "123xxxxx"
            ],
            "option" => $option
        ]);
        try {
            $client->restoreRecycleItemsWithOptions("recyclebin_id", $restoreRecycleItemsRequest, $restoreRecycleItemsHeaders, new RuntimeOptions([]));
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
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  restoreRecycleItemsHeaders := &dingtalkstorage_1_0.RestoreRecycleItemsHeaders{}
  restoreRecycleItemsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.RestoreRecycleItemsRequestOption{
    ConflictStrategy: tea.String("AUTO_RENAME"),
  }
  restoreRecycleItemsRequest := &dingtalkstorage_1_0.RestoreRecycleItemsRequest{
    UnionId: tea.String("chyxxxxx"),
    RecycleItemIds: []*string{tea.String("123xxxxx")},
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RestoreRecycleItemsWithOptions(tea.String("recyclebin_id"), restoreRecycleItemsRequest, restoreRecycleItemsHeaders, &util.RuntimeOptions{})
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
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkstorage_1_0, * as $dingtalkstorage_1_0 from '@alicloud/dingtalk/storage_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkstorage_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkstorage_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let restoreRecycleItemsHeaders = new $dingtalkstorage_1_0.RestoreRecycleItemsHeaders({ });
    restoreRecycleItemsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let option = new $dingtalkstorage_1_0.RestoreRecycleItemsRequestOption({
      conflictStrategy: "AUTO_RENAME",
    });
    let restoreRecycleItemsRequest = new $dingtalkstorage_1_0.RestoreRecycleItemsRequest({
      unionId: "chyxxxxx",
      recycleItemIds: [
        "123xxxxx"
      ],
      option: option,
    });
    try {
      await client.restoreRecycleItemsWithOptions("recyclebin_id", restoreRecycleItemsRequest, restoreRecycleItemsHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.RestoreRecycleItemsHeaders restoreRecycleItemsHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.RestoreRecycleItemsHeaders();
            restoreRecycleItemsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.RestoreRecycleItemsRequest.RestoreRecycleItemsRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.RestoreRecycleItemsRequest.RestoreRecycleItemsRequestOption
            {
                ConflictStrategy = "AUTO_RENAME",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.RestoreRecycleItemsRequest restoreRecycleItemsRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.RestoreRecycleItemsRequest
            {
                UnionId = "chyxxxxx",
                RecycleItemIds = new List<string>
                {
                    "123xxxxx"
                },
                Option = option,
            };
            try
            {
                client.RestoreRecycleItemsWithOptions("recyclebin_id", restoreRecycleItemsRequest, restoreRecycleItemsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| resultItems | Array | 批量还原文件或文件夹的结果列表。 |
| recycleBinId | String | 回收站ID。 |
| recycleItemId | String | 回收项ID。 |
| async | Boolean | 是否是异步任务。   - **true**：是 - **false**：否   **[!NOTE]**    如果操作对象有子节点，则会异步处理。 |
| success | Boolean | 是否成功。   - **true**：成功 - **false**：失败   **[!NOTE]**    异步任务该字段不返回。 |
| errorCode | String | 错误原因。  **[!NOTE]**    异步任务该字段不返回。 |
| taskId | String | 异步任务ID，可用于查询任务执行状态。   - 企业内部应用，可调用[获取存储中异步任务信息](https://open.dingtalk.com/document/orgapp-server/get-the-asynchronous-task-information-in-storage)接口查询任务执行状态。 - 第三方企业应用，可调用[获取存储中异步任务信息](https://open.dingtalk.com/document/isvapp-server/get-the-asynchronous-task-information-in-storage)接口查询任务执行状态。 |
| spaceId | String | 还原后的文件或文件夹所在的空间ID。  **[!NOTE]**    非失败情况下，同步或异步都会返回。 |
| dentryId | String | 还原后的文件或文件夹ID。  **[!NOTE]**    非失败情况下，同步或异步都会返回。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "resultItems" : [ {
    "recycleBinId" : "778xxxxx",
    "recycleItemId" : "768xxxxx",
    "async" : true,
    "success" : true,
    "errorCode" : "permissionDenied",
    "taskId" : "123xxxxx",
    "spaceId" : "789xxxxx",
    "dentryId" : "776xxxxx"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.recycleBinId | %s | 参数错误-recycleBinId |
| 400 | paramError.recycleItemIds | %s | 参数错误-recycleItemIds |
| 400 | paramError.conflictStrategy | %s | 参数错误-conflictStrategy |
| 403 | permissionDenied | %s | 用户缺少对回收项原文件(夹)的管理权限 |
| 404 | recycleBinNotExist | %s | 回收站不存在 |
| 404 | recycleItemNotExist | %s | 回收项不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
