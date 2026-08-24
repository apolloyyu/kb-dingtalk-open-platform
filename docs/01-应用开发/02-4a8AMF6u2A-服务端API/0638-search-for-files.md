---
title: "搜索文件"
source_url: "https://open.dingtalk.com/document/development/search-for-files"
namespace: "development"
slug: "search-for-files"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 搜索 > 搜索文件"
doc_id: "3dpgjZBxT0"
updated_at: "2026-06-04 19:09:27"
---

> Source: https://open.dingtalk.com/document/development/search-for-files
> Path: 应用开发 / 服务端API / 文档/文件 > 搜索 > 搜索文件
> Updated: 2026-06-04 19:09:27

# 搜索文件

调用本接口，根据操作者unionId和关键词信息，获取文件信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/storage/dentries/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.Dentry.Search-文件搜索权限 |

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
| maxResults | Integer | 否 | 分页大小，默认值50。      最大值50。 |
| dentryCategories | Array of String | 否 | 限定文件类别。 |
| creatorIds | Array of String | 否 | 限定创建者。 |
| modifierIds | Array of String | 否 | 限定修改者。 |
| createTimeRange | Object | 否 | 限定创建时间范围。      不指定时, 默认所有创建时间。 |
| startTime | Long | 否 | 开始时间戳。 |
| endTime | Long | 否 | 结束时间戳。 |
| visitTimeRange | Object | 否 | 限定访问时间范围。    不指定时, 默认所有访问时间。 |
| startTime | Long | 否 | 开始时间戳。 |
| endTime | Long | 否 | 结束时间戳。 |

### 请求示例

HTTP

```
POST /v2.0/storage/dentries/search?operatorId=tXguN309iPhE4roSKPlLURAiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "keyword" : "keyword",
  "option" : {
    "nextToken" : "next_token",
    "maxResults" : 20,
    "dentryCategories" : [ "category" ],
    "creatorIds" : [ "creator_id" ],
    "modifierIds" : [ "modifier_id" ],
    "createTimeRange" : { },
    "visitTimeRange" : { }
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
        com.aliyun.dingtalkstorage_2_0.models.SearchDentriesHeaders searchDentriesHeaders = new com.aliyun.dingtalkstorage_2_0.models.SearchDentriesHeaders();
        searchDentriesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest.SearchDentriesRequestOptionVisitTimeRange optionVisitTimeRange = new com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest.SearchDentriesRequestOptionVisitTimeRange();
        com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest.SearchDentriesRequestOptionCreateTimeRange optionCreateTimeRange = new com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest.SearchDentriesRequestOptionCreateTimeRange();
        com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest.SearchDentriesRequestOption option = new com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest.SearchDentriesRequestOption()
                .setNextToken("next_token")
                .setMaxResults(20)
                .setDentryCategories(java.util.Arrays.asList(
                    "category"
                ))
                .setCreatorIds(java.util.Arrays.asList(
                    "creator_id"
                ))
                .setModifierIds(java.util.Arrays.asList(
                    "modifier_id"
                ))
                .setCreateTimeRange(optionCreateTimeRange)
                .setVisitTimeRange(optionVisitTimeRange);
        com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest searchDentriesRequest = new com.aliyun.dingtalkstorage_2_0.models.SearchDentriesRequest()
                .setOperatorId("tXguN309iPhE4roSKPlLURAiEiE")
                .setKeyword("keyword")
                .setOption(option);
        try {
            client.searchDentriesWithOptions(searchDentriesRequest, searchDentriesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        search_dentries_headers = dingtalkstorage__2__0_models.SearchDentriesHeaders()
        search_dentries_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_visit_time_range = dingtalkstorage__2__0_models.SearchDentriesRequestOptionVisitTimeRange()
        option_create_time_range = dingtalkstorage__2__0_models.SearchDentriesRequestOptionCreateTimeRange()
        option = dingtalkstorage__2__0_models.SearchDentriesRequestOption(
            next_token='next_token',
            max_results=20,
            dentry_categories=[
                'category'
            ],
            creator_ids=[
                'creator_id'
            ],
            modifier_ids=[
                'modifier_id'
            ],
            create_time_range=option_create_time_range,
            visit_time_range=option_visit_time_range
        )
        search_dentries_request = dingtalkstorage__2__0_models.SearchDentriesRequest(
            operator_id='tXguN309iPhE4roSKPlLURAiEiE',
            keyword='keyword',
            option=option
        )
        try:
            client.search_dentries_with_options(search_dentries_request, search_dentries_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_dentries_headers = dingtalkstorage__2__0_models.SearchDentriesHeaders()
        search_dentries_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_visit_time_range = dingtalkstorage__2__0_models.SearchDentriesRequestOptionVisitTimeRange()
        option_create_time_range = dingtalkstorage__2__0_models.SearchDentriesRequestOptionCreateTimeRange()
        option = dingtalkstorage__2__0_models.SearchDentriesRequestOption(
            next_token='next_token',
            max_results=20,
            dentry_categories=[
                'category'
            ],
            creator_ids=[
                'creator_id'
            ],
            modifier_ids=[
                'modifier_id'
            ],
            create_time_range=option_create_time_range,
            visit_time_range=option_visit_time_range
        )
        search_dentries_request = dingtalkstorage__2__0_models.SearchDentriesRequest(
            operator_id='tXguN309iPhE4roSKPlLURAiEiE',
            keyword='keyword',
            option=option
        )
        try:
            await client.search_dentries_with_options_async(search_dentries_request, search_dentries_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchDentriesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchDentriesRequest\option\visitTimeRange;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchDentriesRequest\option\createTimeRange;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchDentriesRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\SearchDentriesRequest;
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
        $searchDentriesHeaders = new SearchDentriesHeaders([]);
        $searchDentriesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $optionVisitTimeRange = new visitTimeRange([]);
        $optionCreateTimeRange = new createTimeRange([]);
        $option = new option([
            "nextToken" => "next_token",
            "maxResults" => 20,
            "dentryCategories" => [
                "category"
            ],
            "creatorIds" => [
                "creator_id"
            ],
            "modifierIds" => [
                "modifier_id"
            ],
            "createTimeRange" => $optionCreateTimeRange,
            "visitTimeRange" => $optionVisitTimeRange
        ]);
        $searchDentriesRequest = new SearchDentriesRequest([
            "operatorId" => "tXguN309iPhE4roSKPlLURAiEiE",
            "keyword" => "keyword",
            "option" => $option
        ]);
        try {
            $client->searchDentriesWithOptions($searchDentriesRequest, $searchDentriesHeaders, new RuntimeOptions([]));
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

  searchDentriesHeaders := &dingtalkstorage_2_0.SearchDentriesHeaders{}
  searchDentriesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionVisitTimeRange := &dingtalkstorage_2_0.SearchDentriesRequestOptionVisitTimeRange{}
  optionCreateTimeRange := &dingtalkstorage_2_0.SearchDentriesRequestOptionCreateTimeRange{}
  option := &dingtalkstorage_2_0.SearchDentriesRequestOption{
    NextToken: tea.String("next_token"),
    MaxResults: tea.Int32(20),
    DentryCategories: []*string{tea.String("category")},
    CreatorIds: []*string{tea.String("creator_id")},
    ModifierIds: []*string{tea.String("modifier_id")},
    CreateTimeRange: optionCreateTimeRange,
    VisitTimeRange: optionVisitTimeRange,
  }
  searchDentriesRequest := &dingtalkstorage_2_0.SearchDentriesRequest{
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
    _, _err = client.SearchDentriesWithOptions(searchDentriesRequest, searchDentriesHeaders, &util.RuntimeOptions{})
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
    let searchDentriesHeaders = new $dingtalkstorage_2_0.SearchDentriesHeaders({ });
    searchDentriesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let optionVisitTimeRange = new $dingtalkstorage_2_0.SearchDentriesRequestOptionVisitTimeRange({ });
    let optionCreateTimeRange = new $dingtalkstorage_2_0.SearchDentriesRequestOptionCreateTimeRange({ });
    let option = new $dingtalkstorage_2_0.SearchDentriesRequestOption({
      nextToken: "next_token",
      maxResults: 20,
      dentryCategories: [
        "category"
      ],
      creatorIds: [
        "creator_id"
      ],
      modifierIds: [
        "modifier_id"
      ],
      createTimeRange: optionCreateTimeRange,
      visitTimeRange: optionVisitTimeRange,
    });
    let searchDentriesRequest = new $dingtalkstorage_2_0.SearchDentriesRequest({
      operatorId: "tXguN309iPhE4roSKPlLURAiEiE",
      keyword: "keyword",
      option: option,
    });
    try {
      await client.searchDentriesWithOptions(searchDentriesRequest, searchDentriesHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesHeaders searchDentriesHeaders = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesHeaders();
            searchDentriesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest.SearchDentriesRequestOption.SearchDentriesRequestOptionVisitTimeRange optionVisitTimeRange = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest.SearchDentriesRequestOption.SearchDentriesRequestOptionVisitTimeRange();
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest.SearchDentriesRequestOption.SearchDentriesRequestOptionCreateTimeRange optionCreateTimeRange = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest.SearchDentriesRequestOption.SearchDentriesRequestOptionCreateTimeRange();
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest.SearchDentriesRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest.SearchDentriesRequestOption
            {
                NextToken = "next_token",
                MaxResults = 20,
                DentryCategories = new List<string>
                {
                    "category"
                },
                CreatorIds = new List<string>
                {
                    "creator_id"
                },
                ModifierIds = new List<string>
                {
                    "modifier_id"
                },
                CreateTimeRange = optionCreateTimeRange,
                VisitTimeRange = optionVisitTimeRange,
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest searchDentriesRequest = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.SearchDentriesRequest
            {
                OperatorId = "tXguN309iPhE4roSKPlLURAiEiE",
                Keyword = "keyword",
                Option = option,
            };
            try
            {
                client.SearchDentriesWithOptions(searchDentriesRequest, searchDentriesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| items | Array | 搜索结果列表，最大size50。 |
| dentryUuid | String | 文件uuid。 |
| name | String | 文件名称。 |
| creator | Object | 创建者。 |
| userId | String | 用户id。 |
| name | String | 名称。 |
| modifier | Object | 修改者。 |
| userId | String | 用户id。 |
| name | String | 名称。 |
| nextToken | String | 分页游标，不为空表示有更多数据。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "items" : [ {
    "dentryUuid" : "EpGBa2Lm8aRmzkkNhplMx1prWgN7R35y",
    "name" : "name",
    "creator" : {
      "userId" : "01472825524039877041",
      "name" : "user_name"
    },
    "modifier" : {
      "userId" : "01472825524039877041",
      "name" : "user_name"
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
| 400 | paramError-keyword | %s | 参数错误-keyword |
| 400 | paramError.maxResults | %s | 参数错误-maxResults |
| 400 | paramError.searchScopes | %s | 参数错误-searchScopes |
| 400 | paramError.searchTargets | %s | 参数错误-searchTargets |
| 400 | paramError.dentryTypes | %s | 参数错误-dentryTypes |
| 400 | paramError.dentryCategories | %s | 参数错误-dentryCategories |
| 400 | paramError.createTimeRange | %s | 参数错误-createTimeRange |
| 400 | paramError.modifiedTimeRange | %s | 参数错误-modifiedTimeRange |
| 400 | paramError.visitTimeRange | %s | 参数错误-visitTimeRange |
| 403 | spaceNotAccessible | %s | 空间不可访问 |
| 403 | workspaceNotAccessible | %s | 知识库不可访问 |
| 403 | workspaceTeamNotAccessible | %s | 知识小组不可访问 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
