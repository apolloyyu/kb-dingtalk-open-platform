---
title: "获取文件预览或编辑信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-object-preview-or-editing-information"
namespace: "development"
slug: "obtains-the-object-preview-or-editing-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 获取文件预览或编辑信息"
doc_id: "wMBLkN5SHV"
updated_at: "2026-06-02 18:49:01"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-object-preview-or-editing-information
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 获取文件预览或编辑信息
> Updated: 2026-06-02 18:49:01

# 获取文件预览或编辑信息

调用本接口，可获取存储空间内文件的预览或编辑链接，拥有权限的用户可通过链接对文件进行预览或编辑操作。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/openInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Read-企业存储文件读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| dentryId | String | 是 | 文件Id，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)或[根据dentryUuid获取spaceId和dentryId](0673-api-getdentryidbyuuid.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| option | Object | 否 | 可选参数。 |
| version | Long | 否 | 指定文件的版本号，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取id参数值。 |
| type | String | 否 | 文件的打开方式：   - **PREVIEW**：预览，默认值 - **EDIT**：编辑 |
| waterMark | Boolean | 否 | 是否需要水印：   - **true**：需要 - **false**：不需要，默认值   **[!NOTE]**    目前仅WPS格式文件(Word、Excel、PPT、Pdf)支持水印。 |
| checkLogin | Boolean | 否 | 是否检查钉钉登录态，目前仅对type参数值为PREVIEW时生效。   - **true**：检查，进入页面会校验钉钉登录态。如果没有登录态，会跳转到登录页面，登录成功后继续跳转到当前页面。 - **false**（默认值）：不检查，进入页面不校验钉钉登录态，但有以下限制：    - 支持基础文档格式文件（Word、Excel、PPT、Pdf)、部分图片格式(jpg、jpeg、jpe、png、gif、bmp、pcx、jiff、tiff、tif、ico、fax、wbmp、webp）和所有类型音视频文件。预览窗口右上角不支持转发副本、在线编辑、下载等功能操作。   - 链接获取后，只能被访问一次（针对浏览器session）。   - 链接获取后，5分钟不使用会自动失效。 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/854xxxxx/dentries/989xxxxx/openInfos/query?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "option" : {
    "version" : 1,
    "type" : "PREVIEW",
    "waterMark" : true,
    "checkLogin" : true
  }
}
```

Java

```
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.GetDentryOpenInfoHeaders getDentryOpenInfoHeaders = new com.aliyun.dingtalkstorage_1_0.models.GetDentryOpenInfoHeaders();
        getDentryOpenInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.GetDentryOpenInfoRequest.GetDentryOpenInfoRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.GetDentryOpenInfoRequest.GetDentryOpenInfoRequestOption()
                .setVersion(1L)
                .setType("PREVIEW")
                .setWaterMark(true)
                .setCheckLogin(true);
        com.aliyun.dingtalkstorage_1_0.models.GetDentryOpenInfoRequest getDentryOpenInfoRequest = new com.aliyun.dingtalkstorage_1_0.models.GetDentryOpenInfoRequest()
                .setUnionId("chyxxxxx")
                .setOption(option);
        try {
            client.getDentryOpenInfoWithOptions("854xxxxx", "989xxxxx", getDentryOpenInfoRequest, getDentryOpenInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys
import json

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
        get_dentry_open_info_headers = dingtalkstorage__1__0_models.GetDentryOpenInfoHeaders()
        get_dentry_open_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.GetDentryOpenInfoRequestOption(
            version=1,
            type='PREVIEW',
            water_mark=True,
            check_login=True
        )
        get_dentry_open_info_request = dingtalkstorage__1__0_models.GetDentryOpenInfoRequest(
            union_id='chyxxxxx',
            option=option
        )
        try:
            client.get_dentry_open_info_with_options('854xxxxx', '989xxxxx', get_dentry_open_info_request, get_dentry_open_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_dentry_open_info_headers = dingtalkstorage__1__0_models.GetDentryOpenInfoHeaders()
        get_dentry_open_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.GetDentryOpenInfoRequestOption(
            version=1,
            type='PREVIEW',
            water_mark=True,
            check_login=True
        )
        get_dentry_open_info_request = dingtalkstorage__1__0_models.GetDentryOpenInfoRequest(
            union_id='chyxxxxx',
            option=option
        )
        try:
            await client.get_dentry_open_info_with_options_async('854xxxxx', '989xxxxx', get_dentry_open_info_request, get_dentry_open_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetDentryOpenInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetDentryOpenInfoRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetDentryOpenInfoRequest;
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
        $getDentryOpenInfoHeaders = new GetDentryOpenInfoHeaders([]);
        $getDentryOpenInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "version" => 1,
            "type" => "PREVIEW",
            "waterMark" => true,
            "checkLogin" => true
        ]);
        $getDentryOpenInfoRequest = new GetDentryOpenInfoRequest([
            "unionId" => "chyxxxxx",
            "option" => $option
        ]);
        try {
            $client->getDentryOpenInfoWithOptions("854xxxxx", "989xxxxx", $getDentryOpenInfoRequest, $getDentryOpenInfoHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
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

  getDentryOpenInfoHeaders := &dingtalkstorage_1_0.GetDentryOpenInfoHeaders{}
  getDentryOpenInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.GetDentryOpenInfoRequestOption{
    Version: tea.Int64(1),
    Type: tea.String("PREVIEW"),
    WaterMark: tea.Bool(true),
    CheckLogin: tea.Bool(true),
  }
  getDentryOpenInfoRequest := &dingtalkstorage_1_0.GetDentryOpenInfoRequest{
    UnionId: tea.String("chyxxxxx"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetDentryOpenInfoWithOptions(tea.String("854xxxxx"), tea.String("989xxxxx"), getDentryOpenInfoRequest, getDentryOpenInfoHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkstorage_1_0 = require('@alicloud/dingtalk/storage_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkstorage_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getDentryOpenInfoHeaders = new dingtalkstorage_1_0.GetDentryOpenInfoHeaders({ });
    getDentryOpenInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let option = new dingtalkstorage_1_0.GetDentryOpenInfoRequestOption({
      version: 1,
      type: 'PREVIEW',
      waterMark: true,
      checkLogin: true,
    });
    let getDentryOpenInfoRequest = new dingtalkstorage_1_0.GetDentryOpenInfoRequest({
      unionId: 'chyxxxxx',
      option: option,
    });
    try {
      await client.getDentryOpenInfoWithOptions('854xxxxx', '989xxxxx', getDentryOpenInfoRequest, getDentryOpenInfoHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
Client.main(process.argv.slice(2));
```

C#

```
using Newtonsoft.Json;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryOpenInfoHeaders getDentryOpenInfoHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryOpenInfoHeaders();
            getDentryOpenInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryOpenInfoRequest.GetDentryOpenInfoRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryOpenInfoRequest.GetDentryOpenInfoRequestOption
            {
                Version = 1,
                Type = "PREVIEW",
                WaterMark = true,
                CheckLogin = true,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryOpenInfoRequest getDentryOpenInfoRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetDentryOpenInfoRequest
            {
                UnionId = "chyxxxxx",
                Option = option,
            };
            try
            {
                client.GetDentryOpenInfoWithOptions("854xxxxx", "989xxxxx", getDentryOpenInfoRequest, getDentryOpenInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| url | String | 文件链接。 |
| hasWaterMark | Boolean | 是否支持水印：   - **true**：支持 - **false**：不支持 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "url" : "url",
  "hasWaterMark" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | paramError.openType | %s | 参数错误-openType |
| 400 | dentryEditNotSupport | %s | 文件不支持编辑 |
| 400 | dentryPreviewNotSupport | %s | 文件不支持预览 |
| 400 | dentryExtensionNotSupport | %s | 文件后缀不支持 |
| 400 | fileViral | %s | 病毒文件 |
| 400 | fileMalicious | %s | 恶意文件 |
| 403 | permissionDenied | %s | 用户缺少读取文件的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
