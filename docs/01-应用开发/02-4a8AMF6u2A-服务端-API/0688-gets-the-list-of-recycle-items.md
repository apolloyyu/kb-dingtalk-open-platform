---
title: "获取回收项列表"
source_url: "https://open.dingtalk.com/document/development/gets-the-list-of-recycle-items"
namespace: "development"
slug: "gets-the-list-of-recycle-items"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 回收站管理 > 获取回收项列表"
doc_id: "aElUOWshat"
updated_at: "2026-06-04 19:09:43"
---

> Source: https://open.dingtalk.com/document/development/gets-the-list-of-recycle-items
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 回收站管理 > 获取回收项列表
> Updated: 2026-06-04 19:09:43

# 获取回收项列表

调用本接口，分页获取回收站所有回收项的详情信息，包括原来所在空间Id、原路径、大小、名称等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/recycleBins/{recycleBinId}/recycleItems |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.RecycleBin.Read-企业存储回收站读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recycleBinId | String | 是 | 回收站Id，可调用[获取回收站信息](0687-obtain-information-about-the-recycle-bin.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 每页最大条目数，默认值50，最大值50。 |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/storage/recycleBins/recyclebin_id/recycleItems?nextToken=next_token&maxResults=30&unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json
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
        com.aliyun.dingtalkstorage_1_0.models.ListRecycleItemsHeaders listRecycleItemsHeaders = new com.aliyun.dingtalkstorage_1_0.models.ListRecycleItemsHeaders();
        listRecycleItemsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.ListRecycleItemsRequest listRecycleItemsRequest = new com.aliyun.dingtalkstorage_1_0.models.ListRecycleItemsRequest()
                .setNextToken("next_token")
                .setMaxResults(30)
                .setUnionId("chyxxxxx");
        try {
            client.listRecycleItemsWithOptions("recyclebin_id", listRecycleItemsRequest, listRecycleItemsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_recycle_items_headers = dingtalkstorage__1__0_models.ListRecycleItemsHeaders()
        list_recycle_items_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_recycle_items_request = dingtalkstorage__1__0_models.ListRecycleItemsRequest(
            next_token='next_token',
            max_results=30,
            union_id='chyxxxxx'
        )
        try:
            client.list_recycle_items_with_options('recyclebin_id', list_recycle_items_request, list_recycle_items_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_recycle_items_headers = dingtalkstorage__1__0_models.ListRecycleItemsHeaders()
        list_recycle_items_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_recycle_items_request = dingtalkstorage__1__0_models.ListRecycleItemsRequest(
            next_token='next_token',
            max_results=30,
            union_id='chyxxxxx'
        )
        try:
            await client.list_recycle_items_with_options_async('recyclebin_id', list_recycle_items_request, list_recycle_items_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListRecycleItemsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListRecycleItemsRequest;
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
        $listRecycleItemsHeaders = new ListRecycleItemsHeaders([]);
        $listRecycleItemsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listRecycleItemsRequest = new ListRecycleItemsRequest([
            "nextToken" => "next_token",
            "maxResults" => 30,
            "unionId" => "chyxxxxx"
        ]);
        try {
            $client->listRecycleItemsWithOptions("recyclebin_id", $listRecycleItemsRequest, $listRecycleItemsHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  listRecycleItemsHeaders := &dingtalkstorage_1_0.ListRecycleItemsHeaders{}
  listRecycleItemsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listRecycleItemsRequest := &dingtalkstorage_1_0.ListRecycleItemsRequest{
    NextToken: tea.String("next_token"),
    MaxResults: tea.Int32(30),
    UnionId: tea.String("chyxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListRecycleItemsWithOptions(tea.String("recyclebin_id"), listRecycleItemsRequest, listRecycleItemsHeaders, &util.RuntimeOptions{})
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
    let listRecycleItemsHeaders = new $dingtalkstorage_1_0.ListRecycleItemsHeaders({ });
    listRecycleItemsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listRecycleItemsRequest = new $dingtalkstorage_1_0.ListRecycleItemsRequest({
      nextToken: "next_token",
      maxResults: 30,
      unionId: "chyxxxxx",
    });
    try {
      await client.listRecycleItemsWithOptions("recyclebin_id", listRecycleItemsRequest, listRecycleItemsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListRecycleItemsHeaders listRecycleItemsHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListRecycleItemsHeaders();
            listRecycleItemsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListRecycleItemsRequest listRecycleItemsRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListRecycleItemsRequest
            {
                NextToken = "next_token",
                MaxResults = 30,
                UnionId = "chyxxxxx",
            };
            try
            {
                client.ListRecycleItemsWithOptions("recyclebin_id", listRecycleItemsRequest, listRecycleItemsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| recycleItems | Array | 回收项列表。 |
| id | String | 回收项id。 |
| spaceId | String | 原文件或文件夹所在的空间Id。 |
| dentryId | String | 原文件或文件夹Id。 |
| size | Long | 原文件或文件夹大小，单位Byte。 |
| type | String | 类型。   - **FILE**：文件 - **FOLDER**：文件夹 |
| originalName | String | 原文件或文件夹名称。 |
| originalPath | String | 原文件或文件夹路径。 |
| operatorId | String | 删除操作人unionId。 |
| operatorTime | String | 删除时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| nextToken | String | 分页游标。      不为空表示有更多数据。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "recycleItems" : [ {
    "id" : "2528xxxxx",
    "spaceId" : "8415xxxxx",
    "dentryId" : "6585xxxxx",
    "size" : 512,
    "type" : "FILE",
    "originalName" : "测试文件夹",
    "originalPath" : "./测试文件夹",
    "operatorId" : "chyxxxxx",
    "operatorTime" : "2022-01-01T10:00:00Z"
  } ],
  "nextToken" : "1660268242000:2528089682"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.recycleBinId | %s | 参数错误-recycleBinId |
| 400 | paramError.maxResults | %s | 参数错误-maxResults |
| 404 | recycleBinNotExist | %s | 回收站不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
