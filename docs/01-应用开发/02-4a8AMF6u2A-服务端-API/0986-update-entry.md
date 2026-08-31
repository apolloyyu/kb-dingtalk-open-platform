---
title: "更新词条"
source_url: "https://open.dingtalk.com/document/development/update-entry"
namespace: "development"
slug: "update-entry"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "企业文化 > 企业百科 > 更新词条"
doc_id: "OFpPFNUuk1"
updated_at: "2026-06-04 19:10:43"
---

> Source: https://open.dingtalk.com/document/development/update-entry
> Path: 应用开发 / 服务端 API / 企业文化 > 企业百科 > 更新词条
> Updated: 2026-06-04 19:10:43

# 更新词条

调用本接口，对已经通过审核并且生效的词条进行更新操作。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/pedia/words |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Pedia.Words.Write-企业百科写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| uuid | Long | 是 | 需要更新的词条编号，可调用[分页获取企业词条信息](0988-entry-search.md)接口获取。 |
| wordName | String | 是 | 词条名称。 |
| wordAlias | Array of String | 否 | 词条别名列表，最大值10。 |
| highLightWordAlias | Array of String | 否 | 可高亮的别名列表，最大值10。      高亮别名必须来自别名，否则不生效。 |
| relatedDoc | Array | 否 | 词条相关文档列表，最大值10。      支持钉钉在线文档。 |
| name | String | 否 | 文档名称。 |
| type | String | 否 | 文档类型：   - adoc：纯文本 - asheet：表格 |
| link | String | 否 | 在线文档链接。 |
| relatedLink | Array | 否 | 词条相关链接列表，最大值10。 |
| name | String | 否 | 链接名称。 |
| link | String | 否 | 链接地址。 |
| wordParaphrase | String | 是 | 词条释义。 |
| appLink | Array | 否 | 词条相关应用，最大值10。 |
| appName | String | 否 | 应用名称。 |
| pcLink | String | 否 | 电脑端地址。 |
| phoneLink | String | 否 | 手机端地址。 |
| iconLink | String | 否 | icon地址。 |
| userId | String | 否 | 操作人的userId。 |
| picList | Array | 否 | 词条的相关图片列表，最大值10。 |
| mediaIdUrl | String | 否 | 图片地址。 |
| contactList | Array | 否 | 词条的相关联系人列表，最大值10。 |
| userId | String | 否 | 联系人的userId。 |
| nickName | String | 否 | 联系人的昵称。 |
| avatarMediaId | String | 否 | 联系人的头像地址。 |

### 请求示例

HTTP

```
PUT /v1.0/pedia/words HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "uuid" : 2131321,
  "wordName" : "词条名称",
  "wordAlias" : [ "别名" ],
  "highLightWordAlias" : [ "词条别名" ],
  "relatedDoc" : [ {
    "name" : "相关文档",
    "type" : "adoc",
    "link" : "https://example.com"
  } ],
  "relatedLink" : [ {
    "name" : "相关链接",
    "link" : "https://example.com"
  } ],
  "wordParaphrase" : "释义",
  "appLink" : [ {
    "appName" : "应用名称",
    "pcLink" : "https://example.com",
    "phoneLink" : "https://example.com",
    "iconLink" : "https://example.com"
  } ],
  "userId" : "312123213",
  "picList" : [ {
    "mediaIdUrl" : "https://example.com"
  } ],
  "contactList" : [ {
    "userId" : "12131312",
    "nickName" : "名称",
    "avatarMediaId" : "@12312312"
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
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateHeaders pediaWordsUpdateHeaders = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateHeaders();
        pediaWordsUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestContactList contactList0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestContactList()
                .setUserId("12131312")
                .setNickName("名称")
                .setAvatarMediaId("@12312312");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestPicList picList0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestPicList()
                .setMediaIdUrl("https://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestAppLink appLink0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestAppLink()
                .setAppName("应用名称")
                .setPcLink("https://example.com")
                .setPhoneLink("https://example.com")
                .setIconLink("https://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedLink relatedLink0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedLink()
                .setName("相关链接")
                .setLink("https://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedDoc relatedDoc0 = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedDoc()
                .setName("相关文档")
                .setType("adoc")
                .setLink("https://example.com");
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest pediaWordsUpdateRequest = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsUpdateRequest()
                .setUuid(2131321L)
                .setWordName("词条名称")
                .setWordAlias(java.util.Arrays.asList(
                    "别名"
                ))
                .setHighLightWordAlias(java.util.Arrays.asList(
                    "词条别名"
                ))
                .setRelatedDoc(java.util.Arrays.asList(
                    relatedDoc0
                ))
                .setRelatedLink(java.util.Arrays.asList(
                    relatedLink0
                ))
                .setWordParaphrase("释义")
                .setAppLink(java.util.Arrays.asList(
                    appLink0
                ))
                .setUserId("312123213")
                .setPicList(java.util.Arrays.asList(
                    picList0
                ))
                .setContactList(java.util.Arrays.asList(
                    contactList0
                ));
        try {
            client.pediaWordsUpdateWithOptions(pediaWordsUpdateRequest, pediaWordsUpdateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        pedia_words_update_headers = dingtalkpedia__1__0_models.PediaWordsUpdateHeaders()
        pedia_words_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        contact_list_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestContactList(
            user_id='12131312',
            nick_name='名称',
            avatar_media_id='@12312312'
        )
        pic_list_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestPicList(
            media_id_url='https://example.com'
        )
        app_link_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestAppLink(
            app_name='应用名称',
            pc_link='https://example.com',
            phone_link='https://example.com',
            icon_link='https://example.com'
        )
        related_link_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestRelatedLink(
            name='相关链接',
            link='https://example.com'
        )
        related_doc_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestRelatedDoc(
            name='相关文档',
            type='adoc',
            link='https://example.com'
        )
        pedia_words_update_request = dingtalkpedia__1__0_models.PediaWordsUpdateRequest(
            uuid=2131321,
            word_name='词条名称',
            word_alias=[
                '别名'
            ],
            high_light_word_alias=[
                '词条别名'
            ],
            related_doc=[
                related_doc_0
            ],
            related_link=[
                related_link_0
            ],
            word_paraphrase='释义',
            app_link=[
                app_link_0
            ],
            user_id='312123213',
            pic_list=[
                pic_list_0
            ],
            contact_list=[
                contact_list_0
            ]
        )
        try:
            client.pedia_words_update_with_options(pedia_words_update_request, pedia_words_update_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_update_headers = dingtalkpedia__1__0_models.PediaWordsUpdateHeaders()
        pedia_words_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        contact_list_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestContactList(
            user_id='12131312',
            nick_name='名称',
            avatar_media_id='@12312312'
        )
        pic_list_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestPicList(
            media_id_url='https://example.com'
        )
        app_link_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestAppLink(
            app_name='应用名称',
            pc_link='https://example.com',
            phone_link='https://example.com',
            icon_link='https://example.com'
        )
        related_link_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestRelatedLink(
            name='相关链接',
            link='https://example.com'
        )
        related_doc_0 = dingtalkpedia__1__0_models.PediaWordsUpdateRequestRelatedDoc(
            name='相关文档',
            type='adoc',
            link='https://example.com'
        )
        pedia_words_update_request = dingtalkpedia__1__0_models.PediaWordsUpdateRequest(
            uuid=2131321,
            word_name='词条名称',
            word_alias=[
                '别名'
            ],
            high_light_word_alias=[
                '词条别名'
            ],
            related_doc=[
                related_doc_0
            ],
            related_link=[
                related_link_0
            ],
            word_paraphrase='释义',
            app_link=[
                app_link_0
            ],
            user_id='312123213',
            pic_list=[
                pic_list_0
            ],
            contact_list=[
                contact_list_0
            ]
        )
        try:
            await client.pedia_words_update_with_options_async(pedia_words_update_request, pedia_words_update_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateRequest\contactList;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateRequest\picList;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateRequest\appLink;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateRequest\relatedLink;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateRequest\relatedDoc;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsUpdateRequest;
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
        $pediaWordsUpdateHeaders = new PediaWordsUpdateHeaders([]);
        $pediaWordsUpdateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $contactList0 = new contactList([
            "userId" => "12131312",
            "nickName" => "名称",
            "avatarMediaId" => "@12312312"
        ]);
        $picList0 = new picList([
            "mediaIdUrl" => "https://example.com"
        ]);
        $appLink0 = new appLink([
            "appName" => "应用名称",
            "pcLink" => "https://example.com",
            "phoneLink" => "https://example.com",
            "iconLink" => "https://example.com"
        ]);
        $relatedLink0 = new relatedLink([
            "name" => "相关链接",
            "link" => "https://example.com"
        ]);
        $relatedDoc0 = new relatedDoc([
            "name" => "相关文档",
            "type" => "adoc",
            "link" => "https://example.com"
        ]);
        $pediaWordsUpdateRequest = new PediaWordsUpdateRequest([
            "uuid" => 2131321,
            "wordName" => "词条名称",
            "wordAlias" => [
                "别名"
            ],
            "highLightWordAlias" => [
                "词条别名"
            ],
            "relatedDoc" => [
                $relatedDoc0
            ],
            "relatedLink" => [
                $relatedLink0
            ],
            "wordParaphrase" => "释义",
            "appLink" => [
                $appLink0
            ],
            "userId" => "312123213",
            "picList" => [
                $picList0
            ],
            "contactList" => [
                $contactList0
            ]
        ]);
        try {
            $client->pediaWordsUpdateWithOptions($pediaWordsUpdateRequest, $pediaWordsUpdateHeaders, new RuntimeOptions([]));
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

  pediaWordsUpdateHeaders := &dingtalkpedia_1_0.PediaWordsUpdateHeaders{}
  pediaWordsUpdateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  contactList0 := &dingtalkpedia_1_0.PediaWordsUpdateRequestContactList{
    UserId: tea.String("12131312"),
    NickName: tea.String("名称"),
    AvatarMediaId: tea.String("@12312312"),
  }
  picList0 := &dingtalkpedia_1_0.PediaWordsUpdateRequestPicList{
    MediaIdUrl: tea.String("https://example.com"),
  }
  appLink0 := &dingtalkpedia_1_0.PediaWordsUpdateRequestAppLink{
    AppName: tea.String("应用名称"),
    PcLink: tea.String("https://example.com"),
    PhoneLink: tea.String("https://example.com"),
    IconLink: tea.String("https://example.com"),
  }
  relatedLink0 := &dingtalkpedia_1_0.PediaWordsUpdateRequestRelatedLink{
    Name: tea.String("相关链接"),
    Link: tea.String("https://example.com"),
  }
  relatedDoc0 := &dingtalkpedia_1_0.PediaWordsUpdateRequestRelatedDoc{
    Name: tea.String("相关文档"),
    Type: tea.String("adoc"),
    Link: tea.String("https://example.com"),
  }
  pediaWordsUpdateRequest := &dingtalkpedia_1_0.PediaWordsUpdateRequest{
    Uuid: tea.Int64(2131321),
    WordName: tea.String("词条名称"),
    WordAlias: []*string{tea.String("别名")},
    HighLightWordAlias: []*string{tea.String("词条别名")},
    RelatedDoc: []*dingtalkpedia_1_0.PediaWordsUpdateRequestRelatedDoc{relatedDoc0},
    RelatedLink: []*dingtalkpedia_1_0.PediaWordsUpdateRequestRelatedLink{relatedLink0},
    WordParaphrase: tea.String("释义"),
    AppLink: []*dingtalkpedia_1_0.PediaWordsUpdateRequestAppLink{appLink0},
    UserId: tea.String("312123213"),
    PicList: []*dingtalkpedia_1_0.PediaWordsUpdateRequestPicList{picList0},
    ContactList: []*dingtalkpedia_1_0.PediaWordsUpdateRequestContactList{contactList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PediaWordsUpdateWithOptions(pediaWordsUpdateRequest, pediaWordsUpdateHeaders, &util.RuntimeOptions{})
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
    let pediaWordsUpdateHeaders = new $dingtalkpedia_1_0.PediaWordsUpdateHeaders({ });
    pediaWordsUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let contactList0 = new $dingtalkpedia_1_0.PediaWordsUpdateRequestContactList({
      userId: "12131312",
      nickName: "名称",
      avatarMediaId: "@12312312",
    });
    let picList0 = new $dingtalkpedia_1_0.PediaWordsUpdateRequestPicList({
      mediaIdUrl: "https://example.com",
    });
    let appLink0 = new $dingtalkpedia_1_0.PediaWordsUpdateRequestAppLink({
      appName: "应用名称",
      pcLink: "https://example.com",
      phoneLink: "https://example.com",
      iconLink: "https://example.com",
    });
    let relatedLink0 = new $dingtalkpedia_1_0.PediaWordsUpdateRequestRelatedLink({
      name: "相关链接",
      link: "https://example.com",
    });
    let relatedDoc0 = new $dingtalkpedia_1_0.PediaWordsUpdateRequestRelatedDoc({
      name: "相关文档",
      type: "adoc",
      link: "https://example.com",
    });
    let pediaWordsUpdateRequest = new $dingtalkpedia_1_0.PediaWordsUpdateRequest({
      uuid: 2131321,
      wordName: "词条名称",
      wordAlias: [
        "别名"
      ],
      highLightWordAlias: [
        "词条别名"
      ],
      relatedDoc: [
        relatedDoc0
      ],
      relatedLink: [
        relatedLink0
      ],
      wordParaphrase: "释义",
      appLink: [
        appLink0
      ],
      userId: "312123213",
      picList: [
        picList0
      ],
      contactList: [
        contactList0
      ],
    });
    try {
      await client.pediaWordsUpdateWithOptions(pediaWordsUpdateRequest, pediaWordsUpdateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateHeaders pediaWordsUpdateHeaders = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateHeaders();
            pediaWordsUpdateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestContactList contactList0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestContactList
            {
                UserId = "12131312",
                NickName = "名称",
                AvatarMediaId = "@12312312",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestPicList picList0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestPicList
            {
                MediaIdUrl = "https://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestAppLink appLink0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestAppLink
            {
                AppName = "应用名称",
                PcLink = "https://example.com",
                PhoneLink = "https://example.com",
                IconLink = "https://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedLink relatedLink0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedLink
            {
                Name = "相关链接",
                Link = "https://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedDoc relatedDoc0 = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedDoc
            {
                Name = "相关文档",
                Type = "adoc",
                Link = "https://example.com",
            };
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest pediaWordsUpdateRequest = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest
            {
                Uuid = 2131321,
                WordName = "词条名称",
                WordAlias = new List<string>
                {
                    "别名"
                },
                HighLightWordAlias = new List<string>
                {
                    "词条别名"
                },
                RelatedDoc = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedDoc>
                {
                    relatedDoc0
                },
                RelatedLink = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestRelatedLink>
                {
                    relatedLink0
                },
                WordParaphrase = "释义",
                AppLink = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestAppLink>
                {
                    appLink0
                },
                UserId = "312123213",
                PicList = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestPicList>
                {
                    picList0
                },
                ContactList = new List<AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsUpdateRequest.PediaWordsUpdateRequestContactList>
                {
                    contactList0
                },
            };
            try
            {
                client.PediaWordsUpdateWithOptions(pediaWordsUpdateRequest, pediaWordsUpdateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| uuid | Long | 更新后待审核词条编号。  **[!NOTE]**  更新词条后，需要管理员同意审核后，才能生效。 |
| success | Boolean | 请求是否成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "uuid" : 3213213213,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestError.wordName | 当前传递过来的词条名称信息不能为空 | 当前传递过来的词条名称信息不能为空 |
| 400 | paramError.request | 请求的参数信息不能为空 | 请求的参数信息不能为空 |
| 400 | paramError.wordParaphrase | 释义信息不能为空 | 释义信息不能为空 |
| 400 | paramError.corpId | 获取到的企业编号不能为空 | 获取到的企业编号不能为空 |
| 400 | paramError.uuid | 词条操作主键uuid不能为空 | 词条操作主键uuid不能为空 |
| 400 | paramError.userId | 操作员工编号userId不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.userId | 操作员工编号userId填写错误未找到对应员工信息 | 操作员工编号userId填写错误未找到对应员工信息 |
| 400 | paramError.risk | 当前编辑内容安全审核未通过,存在风险词语 | 当前编辑内容安全审核未通过,存在风险词语 |
| 400 | paramError.contactsId | 当前联系人信息输入错误，请确认后再操作 | 当前联系人信息输入错误，请确认后再操作 |
