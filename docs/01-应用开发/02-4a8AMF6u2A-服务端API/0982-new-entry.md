---
title: "新增词条"
source_url: "https://open.dingtalk.com/document/development/new-entry"
namespace: "development"
slug: "new-entry"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 企业百科 > 新增词条"
doc_id: "3SSVuPz0MG"
updated_at: "2026-06-04 19:10:41"
---

> Source: https://open.dingtalk.com/document/development/new-entry
> Path: 应用开发 / 服务端API / 企业文化 > 企业百科 > 新增词条
> Updated: 2026-06-04 19:10:41

# 新增词条

调用本接口，新增词条相关信息到企业百科系统，主要包括词条名称、释义、别名、相关文档、链接、联系人等基本词条信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/pedia/words |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Pedia.Words.Write-企业百科写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| wordName | String | 是 | 新增词条的名称。 |
| wordAlias | Array of String | 否 | 词条的别名列表，多个名字的时候可以添加，每次调用最多传10个。 |
| highLightWordAlias | Array of String | 否 | 词条高亮别名列表，每次调用最多传10个。    从别名中选取，不在别名列表中不展示 |
| relatedDoc | Array | 否 | 词条相关的文档列表，每次调用最多传10个。    支持钉钉在线文档。 |
| name | String | 否 | 文档名称。 |
| type | String | 否 | 文档类型：   - **adoc**：纯文本 - **asheet**：表格 |
| link | String | 否 | 文档地址。 |
| relatedLink | Array | 否 | 词条相关的链接列表，每次调用最多传10个。 |
| name | String | 否 | 链接名称。 |
| link | String | 否 | 链接地址。 |
| wordParaphrase | String | 是 | 词条释义，针对词条的描述内容。 |
| picList | Array | 否 | 词条相关的图片列表，每次调用最多传10个。 |
| mediaIdUrl | String | 否 | 图片的HTTP地址。 |
| userId | String | 是 | 组织对应的员工userId。 |
| contactList | Array | 否 | 词条相关的联系人列表，每次调用最多传10个。 |
| userId | String | 否 | 联系人的userId。 |
| nickName | String | 否 | 联系人的昵称。 |
| avatarMediaId | String | 否 | 联系人的头像地址，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/pedia/words HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "wordName" : "词条名称",
  "wordAlias" : [ "词条别名" ],
  "highLightWordAlias" : [ "别名" ],
  "relatedDoc" : [ {
    "name" : "相关文档",
    "type" : "adoc",
    "link" : "http://example.com"
  } ],
  "relatedLink" : [ {
    "name" : "相关链接",
    "link" : "http://example.com"
  } ],
  "wordParaphrase" : "释义",
  "picList" : [ {
    "mediaIdUrl" : "http://example.com"
  } ],
  "userId" : "manager7675",
  "contactList" : [ {
    "userId" : "manager7675",
    "nickName" : "名称",
    "avatarMediaId" : "@123243"
  } ]
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
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddHeaders pediaWordsAddHeaders = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddHeaders();
        pediaWordsAddHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestContactList contactList0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestContactList()
                .setUserId("manager7675")
                .setNickName("名称")
                .setAvatarMediaId("@123243");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestPicList picList0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestPicList()
                .setMediaIdUrl("http://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestRelatedLink relatedLink0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestRelatedLink()
                .setName("相关链接")
                .setLink("http://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestRelatedDoc relatedDoc0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest.PediaWordsAddRequestRelatedDoc()
                .setName("相关文档")
                .setType("adoc")
                .setLink("http://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest pediaWordsAddRequest = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsAddRequest()
                .setWordName("词条名称")
                .setWordAlias(java.util.Arrays.asList(
                    "词条别名"
                ))
                .setHighLightWordAlias(java.util.Arrays.asList(
                    "别名"
                ))
                .setRelatedDoc(java.util.Arrays.asList(
                    relatedDoc0
                ))
                .setRelatedLink(java.util.Arrays.asList(
                    relatedLink0
                ))
                .setWordParaphrase("释义")
                .setPicList(java.util.Arrays.asList(
                    picList0
                ))
                .setUserId("manager7675")
                .setContactList(java.util.Arrays.asList(
                    contactList0
                ));
        try {
            client.pediaWordsAddWithOptions(pediaWordsAddRequest, pediaWordsAddHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        pedia_words_add_headers = dingtalkpedia__1__0_models.PediaWordsAddHeaders()
        pedia_words_add_headers.x_acs_dingtalk_access_token = '<your access token>'
        contact_list_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestContactList(
            user_id='manager7675',
            nick_name='名称',
            avatar_media_id='@123243'
        )
        pic_list_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestPicList(
            media_id_url='http://example.com'
        )
        related_link_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestRelatedLink(
            name='相关链接',
            link='http://example.com'
        )
        related_doc_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestRelatedDoc(
            name='相关文档',
            type='adoc',
            link='http://example.com'
        )
        pedia_words_add_request = dingtalkpedia__1__0_models.PediaWordsAddRequest(
            word_name='词条名称',
            word_alias=[
                '词条别名'
            ],
            high_light_word_alias=[
                '别名'
            ],
            related_doc=[
                related_doc_0
            ],
            related_link=[
                related_link_0
            ],
            word_paraphrase='释义',
            pic_list=[
                pic_list_0
            ],
            user_id='manager7675',
            contact_list=[
                contact_list_0
            ]
        )
        try:
            client.pedia_words_add_with_options(pedia_words_add_request, pedia_words_add_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_add_headers = dingtalkpedia__1__0_models.PediaWordsAddHeaders()
        pedia_words_add_headers.x_acs_dingtalk_access_token = '<your access token>'
        contact_list_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestContactList(
            user_id='manager7675',
            nick_name='名称',
            avatar_media_id='@123243'
        )
        pic_list_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestPicList(
            media_id_url='http://example.com'
        )
        related_link_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestRelatedLink(
            name='相关链接',
            link='http://example.com'
        )
        related_doc_0 = dingtalkpedia__1__0_models.PediaWordsAddRequestRelatedDoc(
            name='相关文档',
            type='adoc',
            link='http://example.com'
        )
        pedia_words_add_request = dingtalkpedia__1__0_models.PediaWordsAddRequest(
            word_name='词条名称',
            word_alias=[
                '词条别名'
            ],
            high_light_word_alias=[
                '别名'
            ],
            related_doc=[
                related_doc_0
            ],
            related_link=[
                related_link_0
            ],
            word_paraphrase='释义',
            pic_list=[
                pic_list_0
            ],
            user_id='manager7675',
            contact_list=[
                contact_list_0
            ]
        )
        try:
            await client.pedia_words_add_with_options_async(pedia_words_add_request, pedia_words_add_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsAddHeaders;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsAddRequest\contactList;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsAddRequest\picList;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsAddRequest\relatedLink;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsAddRequest\relatedDoc;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsAddRequest;
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
        $pediaWordsAddHeaders = new PediaWordsAddHeaders([]);
        $pediaWordsAddHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $contactList0 = new contactList([
            "userId" => "manager7675",
            "nickName" => "名称",
            "avatarMediaId" => "@123243"
        ]);
        $picList0 = new picList([
            "mediaIdUrl" => "http://example.com"
        ]);
        $relatedLink0 = new relatedLink([
            "name" => "相关链接",
            "link" => "http://example.com"
        ]);
        $relatedDoc0 = new relatedDoc([
            "name" => "相关文档",
            "type" => "adoc",
            "link" => "http://example.com"
        ]);
        $pediaWordsAddRequest = new PediaWordsAddRequest([
            "wordName" => "词条名称",
            "wordAlias" => [
                "词条别名"
            ],
            "highLightWordAlias" => [
                "别名"
            ],
            "relatedDoc" => [
                $relatedDoc0
            ],
            "relatedLink" => [
                $relatedLink0
            ],
            "wordParaphrase" => "释义",
            "picList" => [
                $picList0
            ],
            "userId" => "manager7675",
            "contactList" => [
                $contactList0
            ]
        ]);
        try {
            $client->pediaWordsAddWithOptions($pediaWordsAddRequest, $pediaWordsAddHeaders, new RuntimeOptions([]));
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

  pediaWordsAddHeaders := &dingtalkpedia_1_0.PediaWordsAddHeaders{}
  pediaWordsAddHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  contactList0 := &dingtalkpedia_1_0.PediaWordsAddRequestContactList{
    UserId: tea.String("manager7675"),
    NickName: tea.String("名称"),
    AvatarMediaId: tea.String("@123243"),
  }
  picList0 := &dingtalkpedia_1_0.PediaWordsAddRequestPicList{
    MediaIdUrl: tea.String("http://example.com"),
  }
  relatedLink0 := &dingtalkpedia_1_0.PediaWordsAddRequestRelatedLink{
    Name: tea.String("相关链接"),
    Link: tea.String("http://example.com"),
  }
  relatedDoc0 := &dingtalkpedia_1_0.PediaWordsAddRequestRelatedDoc{
    Name: tea.String("相关文档"),
    Type: tea.String("adoc"),
    Link: tea.String("http://example.com"),
  }
  pediaWordsAddRequest := &dingtalkpedia_1_0.PediaWordsAddRequest{
    WordName: tea.String("词条名称"),
    WordAlias: []*string{tea.String("词条别名")},
    HighLightWordAlias: []*string{tea.String("别名")},
    RelatedDoc: []*dingtalkpedia_1_0.PediaWordsAddRequestRelatedDoc{relatedDoc0},
    RelatedLink: []*dingtalkpedia_1_0.PediaWordsAddRequestRelatedLink{relatedLink0},
    WordParaphrase: tea.String("释义"),
    PicList: []*dingtalkpedia_1_0.PediaWordsAddRequestPicList{picList0},
    UserId: tea.String("manager7675"),
    ContactList: []*dingtalkpedia_1_0.PediaWordsAddRequestContactList{contactList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PediaWordsAddWithOptions(pediaWordsAddRequest, pediaWordsAddHeaders, &util.RuntimeOptions{})
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
    let pediaWordsAddHeaders = new $dingtalkpedia_1_0.PediaWordsAddHeaders({ });
    pediaWordsAddHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let contactList0 = new $dingtalkpedia_1_0.PediaWordsAddRequestContactList({
      userId: "manager7675",
      nickName: "名称",
      avatarMediaId: "@123243",
    });
    let picList0 = new $dingtalkpedia_1_0.PediaWordsAddRequestPicList({
      mediaIdUrl: "http://example.com",
    });
    let relatedLink0 = new $dingtalkpedia_1_0.PediaWordsAddRequestRelatedLink({
      name: "相关链接",
      link: "http://example.com",
    });
    let relatedDoc0 = new $dingtalkpedia_1_0.PediaWordsAddRequestRelatedDoc({
      name: "相关文档",
      type: "adoc",
      link: "http://example.com",
    });
    let pediaWordsAddRequest = new $dingtalkpedia_1_0.PediaWordsAddRequest({
      wordName: "词条名称",
      wordAlias: [
        "词条别名"
      ],
      highLightWordAlias: [
        "别名"
      ],
      relatedDoc: [
        relatedDoc0
      ],
      relatedLink: [
        relatedLink0
      ],
      wordParaphrase: "释义",
      picList: [
        picList0
      ],
      userId: "manager7675",
      contactList: [
        contactList0
      ],
    });
    try {
      await client.pediaWordsAddWithOptions(pediaWordsAddRequest, pediaWordsAddHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddHeaders pediaWordsAddHeaders = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddHeaders();
            pediaWordsAddHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestContactList contactList0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestContactList
            {
                UserId = "manager7675",
                NickName = "名称",
                AvatarMediaId = "@123243",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestPicList picList0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestPicList
            {
                MediaIdUrl = "http://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestRelatedLink relatedLink0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestRelatedLink
            {
                Name = "相关链接",
                Link = "http://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestRelatedDoc relatedDoc0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestRelatedDoc
            {
                Name = "相关文档",
                Type = "adoc",
                Link = "http://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest pediaWordsAddRequest = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest
            {
                WordName = "词条名称",
                WordAlias = new List<string>
                {
                    "词条别名"
                },
                HighLightWordAlias = new List<string>
                {
                    "别名"
                },
                RelatedDoc = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestRelatedDoc>
                {
                    relatedDoc0
                },
                RelatedLink = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestRelatedLink>
                {
                    relatedLink0
                },
                WordParaphrase = "释义",
                PicList = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestPicList>
                {
                    picList0
                },
                UserId = "manager7675",
                ContactList = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsAddRequest.PediaWordsAddRequestContactList>
                {
                    contactList0
                },
            };
            try
            {
                client.PediaWordsAddWithOptions(pediaWordsAddRequest, pediaWordsAddHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| uuid | Long | 插入成功后的编号主键ID。  **[!NOTE]**  词条创建后，当前企业管理员需要在企业百科--管理后台审核通过后，该词条才会生效。 |
| success | Boolean | 请求是否成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "uuid" : 232432,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestError.wordName | 当前传递过来的词条名称信息不能为空 | 当前传递过来的词条名称信息不能为空 |
| 400 | paramError.request | 请求的入参信息不能为空 | 请求的入参信息不能为空 |
| 400 | paramError.wordParaphrase | 释义信息不能为空 | 释义信息不能为空 |
| 400 | paramError.corpId | 获取到的企业编号不能为空 | 获取到的企业编号不能为空 |
| 400 | paramError.userId | 操作员工编号useruserIdid不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.userId | 操作员工编号userId填写错误未找到对应员工信息 | 操作员工编号userId填写错误未找到对应员工信息 |
| 400 | paramError.risk | 当前编辑内容安全审核未通过,存在风险词语 | 当前编辑内容安全审核未通过,存在风险词语 |
| 400 | paramError.contactId | 联系人员工编号填写错误 | 联系人员工编号填写错误 |
