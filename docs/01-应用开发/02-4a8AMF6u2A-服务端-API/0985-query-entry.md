---
title: "根据词条ID查询详情"
source_url: "https://open.dingtalk.com/document/development/query-entry"
namespace: "development"
slug: "query-entry"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "企业文化 > 企业百科 > 根据词条ID查询详情"
doc_id: "WADSAC7AsB"
updated_at: "2026-06-04 19:10:43"
---

> Source: https://open.dingtalk.com/document/development/query-entry
> Path: 应用开发 / 服务端 API / 企业文化 > 企业百科 > 根据词条ID查询详情
> Updated: 2026-06-04 19:10:43

# 根据词条ID查询详情

调用本接口，根据词条ID查询某个词条的详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/pedia/words/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Pedia.Words.Read-企业百科词条读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| uuid | Long | 是 | 查询主键编号，可调用[分页获取企业词条信息](0988-entry-search.md)接口获取。 |
| userId | String | 是 | 当前操作用户的userId。 |

### 请求示例

HTTP

```
POST /v1.0/pedia/words/query?uuid=211121&userId=212121 HTTP/1.1
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
    public static com.aliyun.dingtalkpedia_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkpedia_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkpedia_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsQueryHeaders pediaWordsQueryHeaders = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsQueryHeaders();
        pediaWordsQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsQueryRequest pediaWordsQueryRequest = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsQueryRequest()
                .setUuid(211121L)
                .setUserId("212121");
        try {
            client.pediaWordsQueryWithOptions(pediaWordsQueryRequest, pediaWordsQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        pedia_words_query_headers = dingtalkpedia__1__0_models.PediaWordsQueryHeaders()
        pedia_words_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        pedia_words_query_request = dingtalkpedia__1__0_models.PediaWordsQueryRequest(
            uuid=211121,
            user_id='212121'
        )
        try:
            client.pedia_words_query_with_options(pedia_words_query_request, pedia_words_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_query_headers = dingtalkpedia__1__0_models.PediaWordsQueryHeaders()
        pedia_words_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        pedia_words_query_request = dingtalkpedia__1__0_models.PediaWordsQueryRequest(
            uuid=211121,
            user_id='212121'
        )
        try:
            await client.pedia_words_query_with_options_async(pedia_words_query_request, pedia_words_query_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsQueryRequest;
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
        $pediaWordsQueryHeaders = new PediaWordsQueryHeaders([]);
        $pediaWordsQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pediaWordsQueryRequest = new PediaWordsQueryRequest([
            "uuid" => 211121,
            "userId" => "212121"
        ]);
        try {
            $client->pediaWordsQueryWithOptions($pediaWordsQueryRequest, $pediaWordsQueryHeaders, new RuntimeOptions([]));
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

  pediaWordsQueryHeaders := &dingtalkpedia_1_0.PediaWordsQueryHeaders{}
  pediaWordsQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pediaWordsQueryRequest := &dingtalkpedia_1_0.PediaWordsQueryRequest{
    Uuid: tea.Int64(211121),
    UserId: tea.String("212121"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PediaWordsQueryWithOptions(pediaWordsQueryRequest, pediaWordsQueryHeaders, &util.RuntimeOptions{})
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
    let pediaWordsQueryHeaders = new $dingtalkpedia_1_0.PediaWordsQueryHeaders({ });
    pediaWordsQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let pediaWordsQueryRequest = new $dingtalkpedia_1_0.PediaWordsQueryRequest({
      uuid: 211121,
      userId: "212121",
    });
    try {
      await client.pediaWordsQueryWithOptions(pediaWordsQueryRequest, pediaWordsQueryHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsQueryHeaders pediaWordsQueryHeaders = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsQueryHeaders();
            pediaWordsQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsQueryRequest pediaWordsQueryRequest = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsQueryRequest
            {
                Uuid = 211121,
                UserId = "212121",
            };
            try
            {
                client.PediaWordsQueryWithOptions(pediaWordsQueryRequest, pediaWordsQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Object | 返回词条具体对象。 |
| wordName | String | 词条名称。 |
| uuid | Long | 词条主键ID。 |
| gmtCreate | Long | 创建时间戳，单位毫秒。 |
| gmtModify | Long | 修改时间戳，单位毫秒。 |
| wordAlias | Array of String | 词条别名列表。 |
| highLightWordAlias | Array of String | 高亮的别名列表。 |
| relatedDoc | Array | 相关文档列表。 |
| name | String | 文档名称。 |
| type | String | 文档类型：   - adoc：纯文本 - asheet：表格 |
| link | String | 相关链接。 |
| relatedLink | Array | 相关链接列表。 |
| name | String | 链接名称。 |
| link | String | 链接地址。 |
| creatorName | String | 创建者。 |
| updaterName | String | 更新人。 |
| approveName | String | 审核人。 |
| wordParaphrase | String | 词条释义，富文本。 |
| simpleWordParaphrase | String | 词条释义，非富文本。 |
| contacts | Array of String | 相关联系人列表。 |
| tagsList | Array of String | 分类列表。 |
| appLink | Array | 相关应用列表。 |
| appName | String | 应用名称。 |
| pcLink | String | 桌面端链接。 |
| phoneLink | String | 手机端链接。 |
| iconLink | String | 应用icon地址。 |
| imHighLight | Boolean | 内部群是否高亮。   - true：是 - false：否 |
| simHighLight | Boolean | 服务群是否高亮。   - true：是 - false：否 |
| picList | Array | 相关图片列表。 |
| mediaIdUrl | String | 图片HTTP地址。 |
| contactList | Array | 联系人列表。 |
| userId | String | 联系人员工userId。 |
| nickName | String | 联系人名称。 |
| avatarMediaId | String | 联系人图片。 |
| userId | String | 操作员工userId。 |
| parentUuid | Long | 当为待审核词条的时候的父编号。 |
| success | Boolean | 请求是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : {
    "wordName" : "词条名称",
    "uuid" : 2131321432,
    "gmtCreate" : 1683280595465,
    "gmtModify" : 1683280595465,
    "wordAlias" : [ "词条别名" ],
    "highLightWordAlias" : [ "词条别名" ],
    "relatedDoc" : [ {
      "name" : "测试文档",
      "type" : "adoc",
      "link" : "https://example.com"
    } ],
    "relatedLink" : [ {
      "name" : "测试链接",
      "link" : "https://example.com"
    } ],
    "creatorName" : "小钉",
    "updaterName" : "小月",
    "approveName" : "小七",
    "wordParaphrase" : "测试释义",
    "simpleWordParaphrase" : "测试简单释义",
    "contacts" : [ "测试" ],
    "tagsList" : [ "分类" ],
    "appLink" : [ {
      "appName" : "应用1",
      "pcLink" : "https://example.com",
      "phoneLink" : "https://example.com",
      "iconLink" : "https://example.com"
    } ],
    "imHighLight" : true,
    "simHighLight" : false,
    "picList" : [ {
      "mediaIdUrl" : "https://example.com"
    } ],
    "contactList" : [ {
      "userId" : "12321231",
      "nickName" : "测试",
      "avatarMediaId" : "1231312@ad"
    } ],
    "userId" : "213123123",
    "parentUuid" : 11123232
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestError.wordName | 当前传递过来的词条名称信息不能为空 | 当前传递过来的词条名称信息不能为空 |
| 400 | paramError.uuid | 查询操作主键uuid不能为空 | 查询操作主键uuid不能为空 |
| 400 | paramError.corpId | 获取到的企业编号不能为空 | 获取到的企业编号不能为空 |
| 400 | paramError.userId | 操作员工编号userId不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.userId | 操作员工编号userId填写错误未找到对应员工信息 | 操作员工编号userId填写错误未找到对应员工信息 |
