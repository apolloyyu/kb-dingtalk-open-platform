---
title: "查询词条详情"
source_url: "https://open.dingtalk.com/document/development/enterprise-encyclopedia-query-entry-details-by-entry-name"
namespace: "development"
slug: "enterprise-encyclopedia-query-entry-details-by-entry-name"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "企业文化 > 企业百科 > 查询词条详情"
doc_id: "fcgi7gsVm9"
updated_at: "2026-06-04 19:10:42"
---

> Source: https://open.dingtalk.com/document/development/enterprise-encyclopedia-query-entry-details-by-entry-name
> Path: 应用开发 / 服务端 API / 企业文化 > 企业百科 > 查询词条详情
> Updated: 2026-06-04 19:10:42

# 查询词条详情

用于根据词条名称查询该词条相关详情信息，包括词条编号、创建时间和修改时间等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/wiki/words/details |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Wiki.Words.Read-企业百科词条读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| wordName | String | 是 | 词条名称，最大长度50个字符。 |

### 请求示例

HTTP

```
GET /v1.0/wiki/words/details?wordName=测试词条 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7d413aebb4a63e2a8240649bba06aa9a
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkwiki_1_0.*;
import com.aliyun.dingtalkwiki_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkwiki_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkwiki_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkwiki_1_0.Client client = Sample.createClient();
        WikiWordsDetailHeaders wikiWordsDetailHeaders = new WikiWordsDetailHeaders();
        wikiWordsDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        WikiWordsDetailRequest wikiWordsDetailRequest = new WikiWordsDetailRequest()
                .setWordName("测试词条");
        try {
            client.wikiWordsDetailWithOptions(wikiWordsDetailRequest, wikiWordsDetailHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.wiki_1_0.client import Client as dingtalkwiki_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.wiki_1_0 import models as dingtalkwiki__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkwiki_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkwiki_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        wiki_words_detail_headers = dingtalkwiki__1__0_models.WikiWordsDetailHeaders()
        wiki_words_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        wiki_words_detail_request = dingtalkwiki__1__0_models.WikiWordsDetailRequest(
            word_name='测试词条'
        )
        try:
            client.wiki_words_detail_with_options(wiki_words_detail_request, wiki_words_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        wiki_words_detail_headers = dingtalkwiki__1__0_models.WikiWordsDetailHeaders()
        wiki_words_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        wiki_words_detail_request = dingtalkwiki__1__0_models.WikiWordsDetailRequest(
            word_name='测试词条'
        )
        try:
            await client.wiki_words_detail_with_options_async(wiki_words_detail_request, wiki_words_detail_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vwiki_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vwiki_1_0\Models\WikiWordsDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vwiki_1_0\Models\WikiWordsDetailRequest;
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
        $wikiWordsDetailHeaders = new WikiWordsDetailHeaders([]);
        $wikiWordsDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $wikiWordsDetailRequest = new WikiWordsDetailRequest([
            "wordName" => "测试词条"
        ]);
        try {
            $client->wikiWordsDetailWithOptions($wikiWordsDetailRequest, $wikiWordsDetailHeaders, new RuntimeOptions([]));
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
  dingtalkwiki_1_0  "github.com/alibabacloud-go/dingtalk/wiki_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkwiki_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkwiki_1_0.Client{}
  _result, _err = dingtalkwiki_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  wikiWordsDetailHeaders := &dingtalkwiki_1_0.WikiWordsDetailHeaders{}
  wikiWordsDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  wikiWordsDetailRequest := &dingtalkwiki_1_0.WikiWordsDetailRequest{
    WordName: tea.String("测试词条"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.WikiWordsDetailWithOptions(wikiWordsDetailRequest, wikiWordsDetailHeaders, &util.RuntimeOptions{})
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
import dingtalkwiki_1_0, * as $dingtalkwiki_1_0 from '@alicloud/dingtalk/wiki_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkwiki_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkwiki_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let wikiWordsDetailHeaders = new $dingtalkwiki_1_0.WikiWordsDetailHeaders({ });
    wikiWordsDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let wikiWordsDetailRequest = new $dingtalkwiki_1_0.WikiWordsDetailRequest({
      wordName: "测试词条",
    });
    try {
      await client.wikiWordsDetailWithOptions(wikiWordsDetailRequest, wikiWordsDetailHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkwiki_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkwiki_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkwiki_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsDetailHeaders wikiWordsDetailHeaders = new AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsDetailHeaders();
            wikiWordsDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsDetailRequest wikiWordsDetailRequest = new AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsDetailRequest
            {
                WordName = "测试词条",
            };
            try
            {
                client.WikiWordsDetailWithOptions(wikiWordsDetailRequest, wikiWordsDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Array | 返回的词条信息列表。 |
| wordName | String | 词条的名称。 |
| uuid | Long | 词条的唯一编号。 |
| gmtCreate | Long | 词条创建的时间，单位毫秒。 |
| gmtModify | Long | 词条修改的时间戳，单位毫秒。 |
| orgName | String | 词条所属的组织名称。 |
| wordAlias | Array of String | 词条别名列表。      创建或修改词条时，可添加词条别名。 |
| highLightWordAlias | Array of String | 设置了群内可见的别名。      词条设置了别名，提交词条审核时，可以设置哪些别名可以在群内显示高亮。 |
| wordFullName | String | 词条全名。 |
| relatedDoc | Array | 词条相关文档列表。 |
| name | String | 文档名称。 |
| type | String | 文档类型。   - axls：表格。 - adoc：文档。 - amind：脑图。 - awbd：白板。 - appt：演示ppt。 |
| link | String | 文档的链接。 |
| relatedLink | Array | 词条相关链接列表。 |
| name | String | 链接名称。 |
| type | String | 链接类型，暂时无返回。 |
| link | String | 链接地址。 |
| creatorName | String | 词条创建人的名字。 |
| updaterName | String | 词条更新人的名字。 |
| approveName | String | 词条的审批人名字。 |
| wordParaphrase | String | 词条的释义信息。 |
| simpleWordParaphrase | String | 抹除文本格式后的释义。 |
| contacts | Array of String | 词条相关联系人名字。 |
| tagsList | Array of String | 分类名称。 |
| appLink | Array | 词条相关的应用列表。 |
| appName | String | 应用名称。 |
| appId | Long | 应用编号。 |
| pcLink | String | 应用PC端链接。 |
| phoneLink | String | 应用手机端链接。 |
| iconLink | String | 应用图标的链接。 |
| imHighLight | Boolean | 内部群是否高亮。   - true：高亮。 - false：不高亮。 |
| simHighLight | Boolean | 服务群是否高亮。   - true：高亮。 - false：不高亮。 |
| errMsg | String | 返回的错误信息。 |
| success | Boolean | 请求是否成功。   - true：成功。 - false：失败。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "wordName" : "测试",
    "uuid" : 2343544554,
    "gmtCreate" : 1232432234,
    "gmtModify" : 2423423234,
    "orgName" : "测试组织",
    "wordAlias" : [ "测试2" ],
    "highLightWordAlias" : [ "测试2" ],
    "wordFullName" : "测试的词条",
    "relatedDoc" : [ {
      "name" : "测试文档",
      "type" : "doc",
      "link" : "https://124343.com"
    } ],
    "relatedLink" : [ {
      "name" : "测试链接",
      "type" : "空",
      "link" : "https://12434.com"
    } ],
    "creatorName" : "人名1",
    "updaterName" : "人名2",
    "approveName" : "人名3",
    "wordParaphrase" : "词条的说明问题",
    "simpleWordParaphrase" : "词条的说明问题1111",
    "contacts" : [ "联系人1" ],
    "tagsList" : [ "分类1" ],
    "appLink" : [ {
      "appName" : "企业百科",
      "appId" : 4343,
      "pcLink" : "https://123434.com",
      "phoneLink" : "https://123434.com",
      "iconLink" : "https://123434.com"
    } ],
    "imHighLight" : true,
    "simHighLight" : true
  } ],
  "errMsg" : "40000",
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestError | 当前传递过来的词条信息不能为空 | 当前传递过来的词条信息不能为空 |
| 400 | systemError | 系统错误 | 系统错误 |
