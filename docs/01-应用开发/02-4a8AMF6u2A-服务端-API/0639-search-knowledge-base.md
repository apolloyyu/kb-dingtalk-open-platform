---
title: "搜索知识库"
source_url: "https://open.dingtalk.com/document/development/search-knowledge-base"
namespace: "development"
slug: "search-knowledge-base"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 搜索 > 搜索知识库"
doc_id: "yjjlgU4F9Q"
updated_at: "2026-06-04 19:09:28"
---

> Source: https://open.dingtalk.com/document/development/search-knowledge-base
> Path: 应用开发 / 服务端 API / 文档/文件 > 搜索 > 搜索知识库
> Updated: 2026-06-04 19:09:28

# 搜索知识库

调用本接口，根据操作人unionId和关键词信息，搜索知识库信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/storage/workspaces/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Wiki.Workspace.Search-知识库搜索权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人unionId。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| keyword | String | 是 | 搜索关键词。 |
| option | Object | 否 | 可选参数。 |
| nextToken | String | 否 | 分页游标。      首次拉取不用传。 |
| maxResults | Integer | 否 | 分页大小，默认值20。      最大值20。 |

### 请求示例

HTTP

```
POST /v2.0/storage/workspaces/search?operatorId=tXguN309iPhE4roSKPlLURAiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "keyword" : "keyword",
  "option" : {
    "nextToken" : "next_token",
    "maxResults" : 20
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
    public static com.aliyun.dingtalkstorage_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_2_0.models.SearchWorkspacesHeaders searchWorkspacesHeaders = new com.aliyun.dingtalkstorage_2_0.models.SearchWorkspacesHeaders();
        searchWorkspacesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_2_0.models.SearchWorkspacesRequest.SearchWorkspacesRequestOption option = new com.aliyun.dingtalkstorage_2_0.models.SearchWorkspacesRequest.SearchWorkspacesRequestOption()
                .setNextToken("next_token")
                .setMaxResults(20);
        com.aliyun.dingtalkstorage_2_0.models.SearchWorkspacesRequest searchWorkspacesRequest = new com.aliyun.dingtalkstorage_2_0.models.SearchWorkspacesRequest()
                .setOperatorId("tXguN309iPhE4roSKPlLURAiEiE")
                .setKeyword("keyword")
                .setOption(option);
        try {
            client.searchWorkspacesWithOptions(searchWorkspacesRequest, searchWorkspacesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        search_workspaces_headers = dingtalkstorage__2__0_models.SearchWorkspacesHeaders()
        search_workspaces_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__2__0_models.SearchWorkspacesRequestOption(
            next_token='next_token',
            max_results=20
        )
        search_workspaces_request = dingtalkstorage__2__0_models.SearchWorkspacesRequest(
            operator_id='tXguN309iPhE4roSKPlLURAiEiE',
            keyword='keyword',
            option=option
        )
        try:
            client.search_workspaces_with_options(search_workspaces_request, search_workspaces_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_workspaces_headers = dingtalkstorage__2__0_models.SearchWorkspacesHeaders()
        search_workspaces_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__2__0_models.SearchWorkspacesRequestOption(
            next_token='next_token',
            max_results=20
        )
        search_workspaces_request = dingtalkstorage__2__0_models.SearchWorkspacesRequest(
            operator_id='tXguN309iPhE4roSKPlLURAiEiE',
            keyword='keyword',
            option=option
        )
        try:
            await client.search_workspaces_with_options_async(search_workspaces_request, search_workspaces_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchWorkspacesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchWorkspacesRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchWorkspacesRequest;
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
        $searchWorkspacesHeaders = new SearchWorkspacesHeaders([]);
        $searchWorkspacesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "nextToken" => "next_token",
            "maxResults" => 20
        ]);
        $searchWorkspacesRequest = new SearchWorkspacesRequest([
            "operatorId" => "tXguN309iPhE4roSKPlLURAiEiE",
            "keyword" => "keyword",
            "option" => $option
        ]);
        try {
            $client->searchWorkspacesWithOptions($searchWorkspacesRequest, $searchWorkspacesHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_2_0  "github.com/alibabacloud-go/dingtalk/storage_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  searchWorkspacesHeaders := &dingtalkstorage_2_0.SearchWorkspacesHeaders{}
  searchWorkspacesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_2_0.SearchWorkspacesRequestOption{
    NextToken: tea.String("next_token"),
    MaxResults: tea.Int32(20),
  }
  searchWorkspacesRequest := &dingtalkstorage_2_0.SearchWorkspacesRequest{
    OperatorId: tea.String("tXguN309iPhE4roSKPlLURAiEiE"),
    Keyword: tea.String("keyword"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SearchWorkspacesWithOptions(searchWorkspacesRequest, searchWorkspacesHeaders, &util.RuntimeOptions{})
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
import dingtalkstorage_2_0, * as $dingtalkstorage_2_0 from '@alicloud/dingtalk/storage_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkstorage_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkstorage_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let searchWorkspacesHeaders = new $dingtalkstorage_2_0.SearchWorkspacesHeaders({ });
    searchWorkspacesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let option = new $dingtalkstorage_2_0.SearchWorkspacesRequestOption({
      nextToken: "next_token",
      maxResults: 20,
    });
    let searchWorkspacesRequest = new $dingtalkstorage_2_0.SearchWorkspacesRequest({
      operatorId: "tXguN309iPhE4roSKPlLURAiEiE",
      keyword: "keyword",
      option: option,
    });
    try {
      await client.searchWorkspacesWithOptions(searchWorkspacesRequest, searchWorkspacesHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchWorkspacesHeaders searchWorkspacesHeaders = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchWorkspacesHeaders();
            searchWorkspacesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchWorkspacesRequest.SearchWorkspacesRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchWorkspacesRequest.SearchWorkspacesRequestOption
            {
                NextToken = "next_token",
                MaxResults = 20,
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchWorkspacesRequest searchWorkspacesRequest = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchWorkspacesRequest
            {
                OperatorId = "tXguN309iPhE4roSKPlLURAiEiE",
                Keyword = "keyword",
                Option = option,
            };
            try
            {
                client.SearchWorkspacesWithOptions(searchWorkspacesRequest, searchWorkspacesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| items | Array | 搜索结果列表，最大size20。 |
| workspaceId | String | 知识库id(spaceUuid)。 |
| name | String | 知识库名称。 |
| url | String | 知识库访问url。 |
| nextToken | String | 分页游标。      不为空表示有更多数据。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "items" : [ {
    "workspaceId" : "By8jQS1ZYjGn5b0M",
    "name" : "workspace_name",
    "url" : "workspace_url"
  } ],
  "nextToken" : "next_token"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError-keyword | %s | 参数错误-keyword |
| 400 | paramError.maxResults | %s | 参数错误-maxResults |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
