---
title: "匹配文本中的词条"
source_url: "https://open.dingtalk.com/document/development/enterprise-encyclopedia-match-entries-in-a-text"
namespace: "development"
slug: "enterprise-encyclopedia-match-entries-in-a-text"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 企业百科 > 匹配文本中的词条"
doc_id: "B8gsHoBhzB"
updated_at: "2026-06-04 19:10:45"
---

> Source: https://open.dingtalk.com/document/development/enterprise-encyclopedia-match-entries-in-a-text
> Path: 应用开发 / 服务端API / 企业文化 > 企业百科 > 匹配文本中的词条
> Updated: 2026-06-04 19:10:45

# 匹配文本中的词条

企业有多个词条，每个词条有词条全称和别名。用于将文本与企业词条进行匹配，获取与词条全称或别名相同的文本内容。

## **接口调用说明**

- 如果未设置可见范围，调用本接口，词条不会被匹配，至少勾选以下任一群类型。
- 匹配到词条后的文本展示效果，开发者可以自定义，例如高亮、下划线等效果。
- 结合查询词条详情接口，可以实现点击文本展示词条内容。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/wiki/words/parse |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Wiki.Words.Read-企业百科词条读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| content | String | 是 | 待匹配词条的文本，最大长度4096个字符。 |

### 请求示例

HTTP

```
POST /v1.0/wiki/words/parse HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "content" : "钉钉，让工作学习更简单。"
}
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
        WikiWordsParseHeaders wikiWordsParseHeaders = new WikiWordsParseHeaders();
        wikiWordsParseHeaders.xAcsDingtalkAccessToken = "<your access token>";
        WikiWordsParseRequest wikiWordsParseRequest = new WikiWordsParseRequest()
                .setContent("钉钉，让工作学习更简单。");
        try {
            client.wikiWordsParseWithOptions(wikiWordsParseRequest, wikiWordsParseHeaders, new RuntimeOptions());
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
        wiki_words_parse_headers = dingtalkwiki__1__0_models.WikiWordsParseHeaders()
        wiki_words_parse_headers.x_acs_dingtalk_access_token = '<your access token>'
        wiki_words_parse_request = dingtalkwiki__1__0_models.WikiWordsParseRequest(
            content='钉钉，让工作学习更简单。'
        )
        try:
            client.wiki_words_parse_with_options(wiki_words_parse_request, wiki_words_parse_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        wiki_words_parse_headers = dingtalkwiki__1__0_models.WikiWordsParseHeaders()
        wiki_words_parse_headers.x_acs_dingtalk_access_token = '<your access token>'
        wiki_words_parse_request = dingtalkwiki__1__0_models.WikiWordsParseRequest(
            content='钉钉，让工作学习更简单。'
        )
        try:
            await client.wiki_words_parse_with_options_async(wiki_words_parse_request, wiki_words_parse_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vwiki_1_0\Models\WikiWordsParseHeaders;
use AlibabaCloud\SDK\Dingtalk\Vwiki_1_0\Models\WikiWordsParseRequest;
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
        $wikiWordsParseHeaders = new WikiWordsParseHeaders([]);
        $wikiWordsParseHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $wikiWordsParseRequest = new WikiWordsParseRequest([
            "content" => "钉钉，让工作学习更简单。"
        ]);
        try {
            $client->wikiWordsParseWithOptions($wikiWordsParseRequest, $wikiWordsParseHeaders, new RuntimeOptions([]));
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

  wikiWordsParseHeaders := &dingtalkwiki_1_0.WikiWordsParseHeaders{}
  wikiWordsParseHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  wikiWordsParseRequest := &dingtalkwiki_1_0.WikiWordsParseRequest{
    Content: tea.String("钉钉，让工作学习更简单。"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.WikiWordsParseWithOptions(wikiWordsParseRequest, wikiWordsParseHeaders, &util.RuntimeOptions{})
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
    let wikiWordsParseHeaders = new $dingtalkwiki_1_0.WikiWordsParseHeaders({ });
    wikiWordsParseHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let wikiWordsParseRequest = new $dingtalkwiki_1_0.WikiWordsParseRequest({
      content: "钉钉，让工作学习更简单。",
    });
    try {
      await client.wikiWordsParseWithOptions(wikiWordsParseRequest, wikiWordsParseHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsParseHeaders wikiWordsParseHeaders = new AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsParseHeaders();
            wikiWordsParseHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsParseRequest wikiWordsParseRequest = new AlibabaCloud.SDK.Dingtalkwiki_1_0.Models.WikiWordsParseRequest
            {
                Content = "钉钉，让工作学习更简单。",
            };
            try
            {
                client.WikiWordsParseWithOptions(wikiWordsParseRequest, wikiWordsParseHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkwiki__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkwiki_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkwiki_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkwiki_1_0::Client> client = make_shared<Alibabacloud_Dingtalkwiki_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkwiki_1_0::WikiWordsParseHeaders> wikiWordsParseHeaders = make_shared<Alibabacloud_Dingtalkwiki_1_0::WikiWordsParseHeaders>();
  wikiWordsParseHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkwiki_1_0::WikiWordsParseRequest> wikiWordsParseRequest = make_shared<Alibabacloud_Dingtalkwiki_1_0::WikiWordsParseRequest>(map<string, boost::any>({
    {"content", boost::any(string("钉钉，让工作学习更简单。"))}
  }));
  try {
    client->wikiWordsParseWithOptions(wikiWordsParseRequest, wikiWordsParseHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 请求是否成功。   - true：成功。 - false：失败。 |
| errMsg | String | 错误信息。 |
| data | Array | 请求返回的数据对象。 |
| startIndex | Long | 匹配到的字符串在文本内的起始索引（包括），索引从0开始。 |
| endIndex | Long | 匹配到的字符串在文本内的结束索引（不包括）。 |
| wordName | String | 匹配到的字符串信息，有以下两种情况。   - 匹配词条的全名。 - 匹配词条的别名。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "data" : [ {
    "startIndex" : 0,
    "endIndex" : 2,
    "wordName" : "钉钉"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | systemError | 系统错误 | 系统错误 |
| 400 | requestError | 待处理的信息不能为空 | 待处理的信息不能为空 |
