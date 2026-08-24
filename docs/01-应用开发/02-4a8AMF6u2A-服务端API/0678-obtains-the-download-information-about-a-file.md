---
title: "获取文件下载信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-download-information-about-a-file"
namespace: "development"
slug: "obtains-the-download-information-about-a-file"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 文件传输 > 获取文件下载信息"
doc_id: "gzy5lYxgyM"
updated_at: "2026-06-08 12:02:08"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-download-information-about-a-file
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 文件传输 > 获取文件下载信息
> Updated: 2026-06-08 12:02:08

# 获取文件下载信息

调用本接口，获取存储空间内文件的下载信息。

## **接口调用说明**

步骤1：调用本接口，获取文件下载的信息，得到文件下载URL和headers。

步骤2：执行下载，参考示例：

```
public static void main(String[] args) {
        String url = ""; // 调用获取下载信息接口获取的internalResourceUrls。
        String path = "/Users/xxxxx/Downloads/test.txt"; // 文件要下载的目标路径。
        // 调用获取下载信息接口得到的headers信息。
        Map<String, String> headers = "" //调用下载信息接口获取的headers。
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url(url)
                .headers(Headers.of(headers))
                .build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                Sink sink = null;
                BufferedSink bufferedSink = null;
                try {
                    File dest = new File(path);
                    sink = Okio.sink(dest);
                    bufferedSink = Okio.buffer(sink);
                    bufferedSink.writeAll(response.body().source());
                } catch (Exception e) {
                    e.printStackTrace();
                } finally {
                    if (bufferedSink != null) {
                        bufferedSink.close();
                    }
                    if (sink != null) {
                        sink.close();
                    }
                }
            }
        });
    }
```

> **[!NOTE]**
>
> 如果文件过大，需要分段获取资源，可在上述示例中添加headers字段：`headers.put("Range","bytes=0-499");`，具体请参考[通过指定Range下载部分内容](0679-use-range-download-a-part-of-content.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{dentryId}/downloadInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Storage.DownloadInfo.Read-企业存储文件下载信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| dentryId | String | 是 | 文件Id，调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)或[根据 dentryUuid 获取 spaceId](0673-api-getdentryidbyuuid.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| option | Object | 否 | 可选参数。 |
| version | Long | 否 | 文件的版本号，可调用[获取文件版本列表](0663-obtains-a-list-of-file-versions.md)接口获取version。 |
| preferIntranet | Boolean | 否 | 是否优先使用内网传输，使用该参数前提是配置了专属存储内网传输。   - true：是，默认值 - false：否 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/854xxxx/dentries/798xxxxx/downloadInfos/query?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "option" : {
    "version" : 1,
    "preferIntranet" : false
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
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.GetFileDownloadInfoHeaders getFileDownloadInfoHeaders = new com.aliyun.dingtalkstorage_1_0.models.GetFileDownloadInfoHeaders();
        getFileDownloadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.GetFileDownloadInfoRequest.GetFileDownloadInfoRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.GetFileDownloadInfoRequest.GetFileDownloadInfoRequestOption()
                .setVersion(1L)
                .setPreferIntranet(false);
        com.aliyun.dingtalkstorage_1_0.models.GetFileDownloadInfoRequest getFileDownloadInfoRequest = new com.aliyun.dingtalkstorage_1_0.models.GetFileDownloadInfoRequest()
                .setUnionId("chyxxxxx")
                .setOption(option);
        try {
            client.getFileDownloadInfoWithOptions("854xxxx", "798xxxxx", getFileDownloadInfoRequest, getFileDownloadInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_file_download_info_headers = dingtalkstorage__1__0_models.GetFileDownloadInfoHeaders()
        get_file_download_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.GetFileDownloadInfoRequestOption(
            version=1,
            prefer_intranet=False
        )
        get_file_download_info_request = dingtalkstorage__1__0_models.GetFileDownloadInfoRequest(
            union_id='chyxxxxx',
            option=option
        )
        try:
            client.get_file_download_info_with_options('854xxxx', '798xxxxx', get_file_download_info_request, get_file_download_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_download_info_headers = dingtalkstorage__1__0_models.GetFileDownloadInfoHeaders()
        get_file_download_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.GetFileDownloadInfoRequestOption(
            version=1,
            prefer_intranet=False
        )
        get_file_download_info_request = dingtalkstorage__1__0_models.GetFileDownloadInfoRequest(
            union_id='chyxxxxx',
            option=option
        )
        try:
            await client.get_file_download_info_with_options_async('854xxxx', '798xxxxx', get_file_download_info_request, get_file_download_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileDownloadInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileDownloadInfoRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileDownloadInfoRequest;
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
        $getFileDownloadInfoHeaders = new GetFileDownloadInfoHeaders([]);
        $getFileDownloadInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "version" => 1,
            "preferIntranet" => false
        ]);
        $getFileDownloadInfoRequest = new GetFileDownloadInfoRequest([
            "unionId" => "chyxxxxx",
            "option" => $option
        ]);
        try {
            $client->getFileDownloadInfoWithOptions("854xxxx", "798xxxxx", $getFileDownloadInfoRequest, $getFileDownloadInfoHeaders, new RuntimeOptions([]));
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

  getFileDownloadInfoHeaders := &dingtalkstorage_1_0.GetFileDownloadInfoHeaders{}
  getFileDownloadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.GetFileDownloadInfoRequestOption{
    Version: tea.Int64(1),
    PreferIntranet: tea.Bool(false),
  }
  getFileDownloadInfoRequest := &dingtalkstorage_1_0.GetFileDownloadInfoRequest{
    UnionId: tea.String("chyxxxxx"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFileDownloadInfoWithOptions(tea.String("854xxxx"), tea.String("798xxxxx"), getFileDownloadInfoRequest, getFileDownloadInfoHeaders, &util.RuntimeOptions{})
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
    let getFileDownloadInfoHeaders = new $dingtalkstorage_1_0.GetFileDownloadInfoHeaders({ });
    getFileDownloadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let option = new $dingtalkstorage_1_0.GetFileDownloadInfoRequestOption({
      version: 1,
      preferIntranet: false,
    });
    let getFileDownloadInfoRequest = new $dingtalkstorage_1_0.GetFileDownloadInfoRequest({
      unionId: "chyxxxxx",
      option: option,
    });
    try {
      await client.getFileDownloadInfoWithOptions("854xxxx", "798xxxxx", getFileDownloadInfoRequest, getFileDownloadInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileDownloadInfoHeaders getFileDownloadInfoHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileDownloadInfoHeaders();
            getFileDownloadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileDownloadInfoRequest.GetFileDownloadInfoRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileDownloadInfoRequest.GetFileDownloadInfoRequestOption
            {
                Version = 1,
                PreferIntranet = false,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileDownloadInfoRequest getFileDownloadInfoRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileDownloadInfoRequest
            {
                UnionId = "chyxxxxx",
                Option = option,
            };
            try
            {
                client.GetFileDownloadInfoWithOptions("854xxxx", "798xxxxx", getFileDownloadInfoRequest, getFileDownloadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| protocol | String | 文件下载协议。   - **HEADER\_SIGNATURE**：Header加签 |
| headerSignatureInfo | Object | Header加签信息。      当protocol字段值为HEADER\_SIGNATURE时，此字段生效。 |
| resourceUrls | Array of String | 多个下载URL，越靠前的URL越优先。 |
| headers | Map<String, String> | 请求头信息。 |
| expirationSeconds | Integer | 过期时间，单位秒。 |
| region | String | 地域。   - **ZHANGJIAKOU**：张家口 - **SHENZHEN**：深圳 - **SHANGHAI**：上海 - **SINGAPORE**：新加坡 - **UNKNOWN**：未知 |
| internalResourceUrls | Array of String | 内网URL。      该字段目前无使用场景，请忽略。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "protocol" : "HEADER_SIGNATURE",
  "headerSignatureInfo" : {
    "resourceUrls" : [ "resource_url" ],
    "headers" : {
      "key" : "header_value"
    },
    "expirationSeconds" : 900,
    "region" : "ZHANGJIAKOU",
    "internalResourceUrls" : [ "internal_resource_url" ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 403 | orgAuthLevelNotEnough | auth level of org is not enough | 企业认证等级过低 |
| 403 | permissionDenied | %s | 用户缺少下载文件的权限 |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | operationNotSupported | %s | 文件不支持下载 |
| 400 | dentryDownloadProtocolNotSupport | %s | 下载协议不支持 |
| 400 | fileArchived | %s | 文件处于归档状态, 会自动触发解归档, 请稍后重试 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
