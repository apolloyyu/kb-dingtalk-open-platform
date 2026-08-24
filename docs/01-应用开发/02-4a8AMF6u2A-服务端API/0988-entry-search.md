---
title: "分页获取企业词条信息"
source_url: "https://open.dingtalk.com/document/development/entry-search"
namespace: "development"
slug: "entry-search"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 企业百科 > 分页获取企业词条信息"
doc_id: "BNlhFh2wJg"
updated_at: "2026-06-04 19:10:44"
---

> Source: https://open.dingtalk.com/document/development/entry-search
> Path: 应用开发 / 服务端API / 企业文化 > 企业百科 > 分页获取企业词条信息
> Updated: 2026-06-04 19:10:44

# 分页获取企业词条信息

调用本接口，根据词条名称搜索符合条件的词条列表，如果名称为空的情况则分页返回所有符合条件的词条列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/pedia/words/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Pedia.Words.Read-企业百科词条读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| wordName | String | 否 | 搜索关键词。    当关键词为空时，分页获取所有词条。 |
| userId | String | 是 | 操作人的userId。 |
| pageSize | Integer | 是 | 当前每页需要展示的数量，最大20。 |
| pageNumber | Integer | 是 | 当前查询的页数，从1开始。 |
| status | String | 是 | 当前搜索列表的状态：   - 0：审核通过 - 1：创建待审核 - 2：更新待审核     默认是0，代表获取所有审核完成的词条。 |

### 请求示例

HTTP

```
POST /v1.0/pedia/words/search HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "wordName" : "企业百科",
  "userId" : "121213213",
  "pageSize" : 1,
  "pageNumber" : 1,
  "status" : "1"
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
    public static com.aliyun.dingtalkpedia_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkpedia_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkpedia_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsSearchHeaders pediaWordsSearchHeaders = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsSearchHeaders();
        pediaWordsSearchHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsSearchRequest pediaWordsSearchRequest = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsSearchRequest()
                .setWordName("企业百科")
                .setUserId("121213213")
                .setPageSize(1)
                .setPageNumber(1)
                .setStatus("1");
        try {
            client.pediaWordsSearchWithOptions(pediaWordsSearchRequest, pediaWordsSearchHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.pedia_1_0.client import Client as dingtalkpedia_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.pedia_1_0 import models as dingtalkpedia__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkpedia_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkpedia_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_search_headers = dingtalkpedia__1__0_models.PediaWordsSearchHeaders()
        pedia_words_search_headers.x_acs_dingtalk_access_token = '<your access token>'
        pedia_words_search_request = dingtalkpedia__1__0_models.PediaWordsSearchRequest(
            word_name='企业百科',
            user_id='121213213',
            page_size=1,
            page_number=1,
            status='1'
        )
        try:
            client.pedia_words_search_with_options(pedia_words_search_request, pedia_words_search_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_search_headers = dingtalkpedia__1__0_models.PediaWordsSearchHeaders()
        pedia_words_search_headers.x_acs_dingtalk_access_token = '<your access token>'
        pedia_words_search_request = dingtalkpedia__1__0_models.PediaWordsSearchRequest(
            word_name='企业百科',
            user_id='121213213',
            page_size=1,
            page_number=1,
            status='1'
        )
        try:
            await client.pedia_words_search_with_options_async(pedia_words_search_request, pedia_words_search_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsSearchHeaders;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsSearchRequest;
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
        $pediaWordsSearchHeaders = new PediaWordsSearchHeaders([]);
        $pediaWordsSearchHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pediaWordsSearchRequest = new PediaWordsSearchRequest([
            "wordName" => "企业百科",
            "userId" => "121213213",
            "pageSize" => 1,
            "pageNumber" => 1,
            "status" => "1"
        ]);
        try {
            $client->pediaWordsSearchWithOptions($pediaWordsSearchRequest, $pediaWordsSearchHeaders, new RuntimeOptions([]));
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
  dingtalkpedia_1_0  "github.com/alibabacloud-go/dingtalk/pedia_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkpedia_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkpedia_1_0.Client{}
  _result, _err = dingtalkpedia_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  pediaWordsSearchHeaders := &dingtalkpedia_1_0.PediaWordsSearchHeaders{}
  pediaWordsSearchHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pediaWordsSearchRequest := &dingtalkpedia_1_0.PediaWordsSearchRequest{
    WordName: tea.String("企业百科"),
    UserId: tea.String("121213213"),
    PageSize: tea.Int32(1),
    PageNumber: tea.Int32(1),
    Status: tea.String("1"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PediaWordsSearchWithOptions(pediaWordsSearchRequest, pediaWordsSearchHeaders, &util.RuntimeOptions{})
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
import dingtalkpedia_1_0, * as $dingtalkpedia_1_0 from '@alicloud/dingtalk/pedia_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkpedia_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkpedia_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let pediaWordsSearchHeaders = new $dingtalkpedia_1_0.PediaWordsSearchHeaders({ });
    pediaWordsSearchHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let pediaWordsSearchRequest = new $dingtalkpedia_1_0.PediaWordsSearchRequest({
      wordName: "企业百科",
      userId: "121213213",
      pageSize: 1,
      pageNumber: 1,
      status: "1",
    });
    try {
      await client.pediaWordsSearchWithOptions(pediaWordsSearchRequest, pediaWordsSearchHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkpedia_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkpedia_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsSearchHeaders pediaWordsSearchHeaders = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsSearchHeaders();
            pediaWordsSearchHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsSearchRequest pediaWordsSearchRequest = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsSearchRequest
            {
                WordName = "企业百科",
                UserId = "121213213",
                PageSize = 1,
                PageNumber = 1,
                Status = "1",
            };
            try
            {
                client.PediaWordsSearchWithOptions(pediaWordsSearchRequest, pediaWordsSearchHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Array | 词条详情列表。 |
| wordName | String | 词条名称。 |
| uuid | Long | 当前词条对应的主键ID。 |
| gmtCreate | Long | 词条创建时间戳，单位毫秒。 |
| gmtModify | Long | 词条修改时间戳，单位毫秒。 |
| wordAlias | Array of String | 词条别名列表。 |
| highLightWordAlias | Array of String | 词条中可高亮的别名列表。 |
| relatedLink | Array | 相关链接列表。 |
| name | String | 链接名称。 |
| type | String | 链接类型。 |
| link | String | 链接地址。 |
| relatedDoc | Array | 相关文档链接列表。 |
| name | String | 在线文档的名称。 |
| type | String | 在线文档的类型：   - adoc：纯文本 - asheet：表格 |
| link | String | 当前在线文档链接地址。 |
| creatorName | String | 创建者的名称。 |
| updaterName | String | 更新者名称。 |
| approveName | String | 审核者名称。 |
| wordParaphrase | String | 词条富文本释义。 |
| simpleWordParaphrase | String | 词条非富文本释义。 |
| contacts | Array of String | 相关联系人列表。 |
| tagsList | Array of String | 分类列表。 |
| appLink | Array | 相关应用列表。 |
| appName | String | 应用名称。 |
| pcLink | String | PC端链接地址。 |
| phoneLink | String | 手机端地址。 |
| iconLink | String | 应用图标地址。 |
| imHighLight | Boolean | 该词条内部群是否高亮：   - true：高亮 - false：不高亮 |
| simHighLight | Boolean | 该词条服务群是否分词：   - true：高亮 - false：不高亮 |
| picList | Array | 相关图片列表。 |
| mediaIdUrl | String | 相关图片地址。 |
| contactList | Array | 相关联系人列表。 |
| userId | String | 员工的userId。 |
| nickName | String | 员工的名字。 |
| avatarMediaId | String | 员工头像。 |
| userId | String | 员工的userId。 |
| parentUuid | Long | 当前词条的父类ID，审核通过的该字段为空。 |
| success | Boolean | 请求是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "wordName" : "词条名称",
    "uuid" : 12312321312,
    "gmtCreate" : 312312312,
    "gmtModify" : 3123123123,
    "wordAlias" : [ "词条别名" ],
    "highLightWordAlias" : [ "词条别名" ],
    "relatedLink" : [ {
      "name" : "相关链接",
      "type" : "xxxxx",
      "link" : "https://example.com"
    } ],
    "relatedDoc" : [ {
      "name" : "相关文档",
      "type" : "adoc",
      "link" : "https://example.com"
    } ],
    "creatorName" : "创建人",
    "updaterName" : "更新人",
    "approveName" : "审核人",
    "wordParaphrase" : "释义",
    "simpleWordParaphrase" : "非富文本释义",
    "contacts" : [ "联系人" ],
    "tagsList" : [ "分类" ],
    "appLink" : [ {
      "appName" : "相关应用",
      "pcLink" : "https://example.com",
      "phoneLink" : "https://example.com",
      "iconLink" : "https://example.com"
    } ],
    "imHighLight" : true,
    "simHighLight" : true,
    "picList" : [ {
      "mediaIdUrl" : "https://example.com"
    } ],
    "contactList" : [ {
      "userId" : "1232343",
      "nickName" : "小钉",
      "avatarMediaId" : "@12313"
    } ],
    "userId" : "312312312",
    "parentUuid" : 1231312312
  } ],
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError.corpId | 获取到的企业编号不能为空 | 获取到的企业编号不能为空 |
| 400 | paramError.request | 请求的参数信息不能为空 | 请求的参数信息不能为空 |
| 400 | paramError.pageSize | 搜索接口的分页数pageSize必须传递 | 搜索接口的分页数pageSize必须传递 |
| 400 | paramError.userId | 操作员工编号userId不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.userId | 操作员工编号userId填写错误未找到对应员工信息 | 操作员工编号userId填写错误未找到对应员工信息 |
| 400 | paramError.pageSize | 当前搜索pageSize数据大于默认值20 | 当前搜索pageSize数据大于默认值20 |
