---
title: "获取文件或文件夹列表"
source_url: "https://open.dingtalk.com/document/development/get-a-list-of-files-or-folders"
namespace: "development"
slug: "get-a-list-of-files-or-folders"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 获取文件或文件夹列表"
doc_id: "SDdLWa7D1P"
updated_at: "2026-06-02 18:49:01"
---

> Source: https://open.dingtalk.com/document/development/get-a-list-of-files-or-folders
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 文件管理 > 获取文件或文件夹列表
> Updated: 2026-06-02 18:49:01

# 获取文件或文件夹列表

调用本接口，获取空间内的文件或文件夹列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Read-企业存储文件读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，调用[添加空间](0652-add-space.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| parentId | String | 是 | 父目录Id。根目录时，该参数是0，调用[获取文件或文件夹列表](#)接口获取parentId参数值。 |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数值不传。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 每页条目数，最大值50。 |
| orderBy | String | 否 | 排序字段。   - **MODIFIED\_TIME**：最后修改时间，默认值 - **CREATE\_TIME**：创建时间 - **NAME**：名称 - **SIZE**：大小 |
| order | String | 否 | 排序规则。   - **ASC**：升序 - **DESC**：降序，默认值 |
| withThumbnail | Boolean | 否 | 是否获取文件缩略图临时链接。按需获取，会影响接口耗时。   - true：获取 - false：不获取，默认值 |
| unionId | String | 是 | 操作者的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/storage/spaces/854xxxxx/dentries?parentId=0&nextToken=next_token&maxResults=30&orderBy=MODIFIED_TIME&order=DESC&withThumbnail=false&unionId=cHtUxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
        com.aliyun.dingtalkstorage_1_0.models.ListDentriesHeaders listDentriesHeaders = new com.aliyun.dingtalkstorage_1_0.models.ListDentriesHeaders();
        listDentriesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.ListDentriesRequest listDentriesRequest = new com.aliyun.dingtalkstorage_1_0.models.ListDentriesRequest()
                .setParentId("0")
                .setNextToken("next_token")
                .setMaxResults(30)
                .setOrderBy("MODIFIED_TIME")
                .setOrder("DESC")
                .setWithThumbnail(false)
                .setUnionId("cHtUxxxxx");
        try {
            client.listDentriesWithOptions("854xxxxx", listDentriesRequest, listDentriesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_dentries_headers = dingtalkstorage__1__0_models.ListDentriesHeaders()
        list_dentries_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_dentries_request = dingtalkstorage__1__0_models.ListDentriesRequest(
            parent_id='0',
            next_token='next_token',
            max_results=30,
            order_by='MODIFIED_TIME',
            order='DESC',
            with_thumbnail=False,
            union_id='cHtUxxxxx'
        )
        try:
            client.list_dentries_with_options('854xxxxx', list_dentries_request, list_dentries_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_dentries_headers = dingtalkstorage__1__0_models.ListDentriesHeaders()
        list_dentries_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_dentries_request = dingtalkstorage__1__0_models.ListDentriesRequest(
            parent_id='0',
            next_token='next_token',
            max_results=30,
            order_by='MODIFIED_TIME',
            order='DESC',
            with_thumbnail=False,
            union_id='cHtUxxxxx'
        )
        try:
            await client.list_dentries_with_options_async('854xxxxx', list_dentries_request, list_dentries_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListDentriesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\ListDentriesRequest;
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
        $listDentriesHeaders = new ListDentriesHeaders([]);
        $listDentriesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listDentriesRequest = new ListDentriesRequest([
            "parentId" => "0",
            "nextToken" => "next_token",
            "maxResults" => 30,
            "orderBy" => "MODIFIED_TIME",
            "order" => "DESC",
            "withThumbnail" => false,
            "unionId" => "cHtUxxxxx"
        ]);
        try {
            $client->listDentriesWithOptions("854xxxxx", $listDentriesRequest, $listDentriesHeaders, new RuntimeOptions([]));
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

  listDentriesHeaders := &dingtalkstorage_1_0.ListDentriesHeaders{}
  listDentriesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listDentriesRequest := &dingtalkstorage_1_0.ListDentriesRequest{
    ParentId: tea.String("0"),
    NextToken: tea.String("next_token"),
    MaxResults: tea.Int32(30),
    OrderBy: tea.String("MODIFIED_TIME"),
    Order: tea.String("DESC"),
    WithThumbnail: tea.Bool(false),
    UnionId: tea.String("cHtUxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListDentriesWithOptions(tea.String("854xxxxx"), listDentriesRequest, listDentriesHeaders, &util.RuntimeOptions{})
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
    let listDentriesHeaders = new $dingtalkstorage_1_0.ListDentriesHeaders({ });
    listDentriesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listDentriesRequest = new $dingtalkstorage_1_0.ListDentriesRequest({
      parentId: "0",
      nextToken: "next_token",
      maxResults: 30,
      orderBy: "MODIFIED_TIME",
      order: "DESC",
      withThumbnail: false,
      unionId: "cHtUxxxxx",
    });
    try {
      await client.listDentriesWithOptions("854xxxxx", listDentriesRequest, listDentriesHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListDentriesHeaders listDentriesHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListDentriesHeaders();
            listDentriesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListDentriesRequest listDentriesRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.ListDentriesRequest
            {
                ParentId = "0",
                NextToken = "next_token",
                MaxResults = 30,
                OrderBy = "MODIFIED_TIME",
                Order = "DESC",
                WithThumbnail = false,
                UnionId = "cHtUxxxxx",
            };
            try
            {
                client.ListDentriesWithOptions("854xxxxx", listDentriesRequest, listDentriesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dentries | Array | 文件或文件夹列表。 |
| id | String | 文件或文件夹的id。 |
| spaceId | String | 所在空间Id。 |
| parentId | String | 父目录Id。根目录时，该参数是0。 |
| type | String | 类型。   - **FIL**E：文件 - **FOLDER**：文件夹 |
| name | String | 文件或文件夹的名称。 |
| size | Long | 文件大小，单位Byte。 |
| path | String | 文件或文件夹的路径。 |
| version | Long | 版本。 |
| status | String | 状态。   - **NORMAL**：正常 - **DELETED**：已删除 - **EXPIRED**：已过期 |
| extension | String | 文件后缀。 |
| creatorId | String | 创建者unionId。 |
| modifierId | String | 修改者unionId。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| properties | Object | 属性信息。 |
| readOnly | Boolean | 文件或文件夹是否只读。   - **true**：是 - **false**：否 |
| appProperties | Map<String, Array> | 在特定应用上的属性。 |
|  | Array | 空间属性列表。 |
| name | String | 属性名称。 |
| value | String | 属性值。 |
| visibility | String | 可见性。   - **PUBLIC**：公开 - **PRIVATE**：仅当前空间可见 |
| uuid | String | 标识字段。 |
| partitionType | String | 存储分区。   - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属MiniOSS存储分区 |
| storageDriver | String | 驱动类型。   - **DINGTALK**：钉钉统一存储驱动 - **ALIDOC**：钉钉文档存储驱动 - **UNKNOWN**：未知驱动 |
| thumbnail | Object | 缩略图信息。 |
| width | Integer | 缩略图宽度，单位px。 |
| height | Integer | 缩略图高度，单位px。 |
| url | String | 缩略图url。 |
| nextToken | String | 分页游标。  **[!NOTE]**    该字段不为空，表示有更多数据。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "dentries" : [ {
    "id" : "657xxxxx",
    "spaceId" : "854xxxxx",
    "parentId" : "0",
    "type" : "FILE",
    "name" : "测试文件夹",
    "size" : 512,
    "path" : "./test.txt",
    "version" : 1,
    "status" : "NORMAL",
    "extension" : "txt",
    "creatorId" : "cHtUxxxxx",
    "modifierId" : "cHtUxxxxx",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "properties" : {
      "readOnly" : true
    },
    "appProperties" : [ {
      "name" : "属性1",
      "value" : "属性值1",
      "visibility" : "PRIVATE"
    } ],
    "uuid" : "123xxxxx",
    "partitionType" : "PUBLIC_OSS_PARTITION",
    "storageDriver" : "DINGTALK",
    "thumbnail" : {
      "width" : 64,
      "height" : 64,
      "url" : "url"
    }
  } ],
  "nextToken" : "next_token"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 403 | permissionDenied | %s | 用户缺少获取文件列表的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
