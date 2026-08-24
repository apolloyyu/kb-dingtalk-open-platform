---
title: "获取文件上传地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-file-upload-address-1"
namespace: "development"
slug: "obtain-the-file-upload-address-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 文件 > 获取文件上传地址"
doc_id: "mbjaqGtHPp"
updated_at: "2026-06-23 18:10:40"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-file-upload-address-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > e签宝 1.0 > 文件 > 获取文件上传地址
> Updated: 2026-06-23 18:10:40

# 获取文件上传地址

调用本接口获取文件上传地址。

## **接口调用说明**

当前接口已完成升级迭代且不再支持新应用申请，存量应用调用不受影响，建议未接入的开发者使用[获取文件上传地址](1085-obtain-the-upload-url-of-a-file-1.md)接口，已接入的开发者结合实际尽快完成迁移。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/esign/files/getUploadUrl |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 不支持新增申请 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| contentType | String | 是 | 目标文件的MIME类型。支持如下格式：   - application/octet-stream - application/pdf       文件流上传的Content-Type参数要和这里一致，否则会出现错误码为403的错误。 |
| contentMd5 | String | 是 | 先计算文件md5值，在对该md5值进行base64编码。   - 可使用[E签宝官网工具](https://smlopen.esign.cn/tools)进行计算。   MD5计算 |
| convert2Pdf | Boolean | 是 | 是否转换成pdf文档，取值：   - true：转换 - false：不转换（默认值）   如果需要转换为pdf文档，那么需要先调用查询文件详情接口查询文件状态，待转换完成后才可使用。 如果本身就是pdf文件，该参数必须传false。 |
| fileName | String | 是 | 文件名称。      此文件名必须包含文件扩展名，且必须与真实的文件扩展名保持一致。例如：需要上传的文件为xxx.docx，那么此参数必须为xxx.docx，而不能是xxx.pdf。 |
| fileSize | Long | 是 | 文件大小，单位byte。      上传的文件大小不能超过50M。 |

### 请求示例

HTTP

```
POST /v1.0/esign/files/getUploadUrl HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:be3xxxx
Content-Type:application/json

{
  "contentType" : "application/octet-stream",
  "contentMd5" : "eGMHwA4TWnbg6PYKMxreUQ==",
  "convert2Pdf" : false,
  "fileName" : "附件.zip",
  "fileSize" : 2542635
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_1_0.*;
import com.aliyun.dingtalkesign_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_1_0.Client client = Sample.createClient();
        GetUploadUrlHeaders getUploadUrlHeaders = new GetUploadUrlHeaders();
        getUploadUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetUploadUrlRequest getUploadUrlRequest = new GetUploadUrlRequest()
                .setContentType("application/octet-stream")
                .setContentMd5("eGMHwA4TWnbg6PYKMxreUQ==")
                .setConvert2Pdf(false)
                .setFileName("附件.zip")
                .setFileSize(2542635L);
        try {
            client.getUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_1_0.client import Client as dingtalkesign_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_upload_url_headers = dingtalkesign__1__0_models.GetUploadUrlHeaders()
        get_upload_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_upload_url_request = dingtalkesign__1__0_models.GetUploadUrlRequest(
            content_type='application/octet-stream',
            content_md_5='eGMHwA4TWnbg6PYKMxreUQ==',
            convert_2pdf=False,
            file_name='附件.zip',
            file_size=2542635
        )
        try:
            client.get_upload_url_with_options(get_upload_url_request, get_upload_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_upload_url_headers = dingtalkesign__1__0_models.GetUploadUrlHeaders()
        get_upload_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_upload_url_request = dingtalkesign__1__0_models.GetUploadUrlRequest(
            content_type='application/octet-stream',
            content_md_5='eGMHwA4TWnbg6PYKMxreUQ==',
            convert_2pdf=False,
            file_name='附件.zip',
            file_size=2542635
        )
        try:
            await client.get_upload_url_with_options_async(get_upload_url_request, get_upload_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetUploadUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetUploadUrlRequest;
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
        $getUploadUrlHeaders = new GetUploadUrlHeaders([]);
        $getUploadUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUploadUrlRequest = new GetUploadUrlRequest([
            "contentType" => "application/octet-stream",
            "contentMd5" => "eGMHwA4TWnbg6PYKMxreUQ==",
            "convert2Pdf" => false,
            "fileName" => "附件.zip",
            "fileSize" => 2542635
        ]);
        try {
            $client->getUploadUrlWithOptions($getUploadUrlRequest, $getUploadUrlHeaders, new RuntimeOptions([]));
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
  dingtalkesign_1_0  ""github.com/alibabacloud-go/dingtalk/esign_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_1_0.Client{}
  _result, _err = dingtalkesign_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUploadUrlHeaders := &dingtalkesign_1_0.GetUploadUrlHeaders{}
  getUploadUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUploadUrlRequest := &dingtalkesign_1_0.GetUploadUrlRequest{
    ContentType: tea.String("application/octet-stream"),
    ContentMd5: tea.String("eGMHwA4TWnbg6PYKMxreUQ=="),
    Convert2Pdf: tea.Bool(false),
    FileName: tea.String("附件.zip"),
    FileSize: tea.Int64(2542635),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_1_0, * as $dingtalkesign_1_0 from '"@alicloud/dingtalk/esign_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUploadUrlHeaders = new $dingtalkesign_1_0.GetUploadUrlHeaders({ });
    getUploadUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUploadUrlRequest = new $dingtalkesign_1_0.GetUploadUrlRequest({
      contentType: "application/octet-stream",
      contentMd5: "eGMHwA4TWnbg6PYKMxreUQ==",
      convert2Pdf: false,
      fileName: "附件.zip",
      fileSize: 2542635,
    });
    try {
      await client.getUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetUploadUrlHeaders getUploadUrlHeaders = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetUploadUrlHeaders();
            getUploadUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetUploadUrlRequest getUploadUrlRequest = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetUploadUrlRequest
            {
                ContentType = "application/octet-stream",
                ContentMd5 = "eGMHwA4TWnbg6PYKMxreUQ==",
                Convert2Pdf = false,
                FileName = "附件.zip",
                FileSize = 2542635,
            };
            try
            {
                client.GetUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetUploadUrlHeaders> getUploadUrlHeaders = make_shared<Alibabacloud_Dingtalkesign_1_0::GetUploadUrlHeaders>();
  getUploadUrlHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetUploadUrlRequest> getUploadUrlRequest = make_shared<Alibabacloud_Dingtalkesign_1_0::GetUploadUrlRequest>(map<string, boost::any>({
    {"contentType", boost::any(string("application/octet-stream"))},
    {"contentMd5", boost::any(string("eGMHwA4TWnbg6PYKMxreUQ=="))},
    {"convert2Pdf", boost::any(false)},
    {"fileName", boost::any(string("附件.zip"))},
    {"fileSize", boost::any(2542635)}
  }));
  try {
    client->getUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| code | Integer | 返回码，0代表成功。 |
| message | String | 返回码描述。 |
| data | Object | 返回结果。 |
| fileId | String | 文件Id。 |
| uploadUrl | String | 文件直传地址。在获取到文件上传地址后，可以直接使用此地址进行文件上传，详情请参考[上传文件](1083-upload-objects-1.md)。      可以重复使用，但是只能传一样的文件，有效期一小时。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : 0,
  "message" : "成功",
  "data" : {
    "fileId" : "049d33e46b7xxx",
    "uploadUrl" : "https://esignoss.oss-cn-hangzhou.aliyuncs.com/116/d8d35867-7e3650efd99e1/%B6.zip?Expires=1&OSSAccessKeyId=&Signature=&callback-var=&callback=&security-token="
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.invalidAguemnts | invalid arguments | 参数错误 |
| 500 | fail.failToCreateCorpAccount | 创建企业账号异常 | 创建企业账号异常 |
