---
title: "获取文件上传地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-upload-url-of-a-file-1"
namespace: "development"
slug: "obtain-the-upload-url-of-a-file-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 文件 > 获取文件上传地址"
doc_id: "pvqsk68lJO"
updated_at: "2025-09-23 19:21:41"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-upload-url-of-a-file-1
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 文件 > 获取文件上传地址
> Updated: 2025-09-23 19:21:41

# 获取文件上传地址

调用本接口获取到文件上传地址。

## **接口调用说明**

获取文件上传地址后，可以直接使用此地址[上传文件](1083-upload-objects-1.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/files/uploadUrls |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-E签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceGroup | String | 否 | 预留参数，此版本无需此参数。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| contentMd5 | String | 否 | ContentMD5值计算方法如下：   1. 先计算出文件MD5的二进制数组（128位）。 2. 再对MD5的二进制数组进行Base64编码（而不是对32位字符串编码）。 |
| contentType | String | 否 | 目标文件的MIME类型，支持：   - application/octet-stream - application/pdf       后面文件流上传的Content-Type参数要和这里一致，不然就会有403的报错。 |
| fileName | String | 否 | 文件名称，必须带上文件扩展名，不然会导致后续发起流程校验过不去。例如：合同.pdf 。      该字段的文件后缀名称和真实的文件后缀需要一致。例如上传的文件类型是word文件，那该参数需要传`xxx.docx`，不能是`xxx.pdf`。 |
| fileSize | Long | 否 | 文件大小，单位byte。 |
| convert2Pdf | Boolean | 否 | 是否转换成pdf文档，默认false，代表不做转换。转换是异步行为，如果指定要转换，需要调用查询文件信息接口查询状态，转换完成后才可使用。      如果本身就是PDF文件，该参数必须传false，否则在【通过模板创建文件】的时候不能填充内容。 |

### 请求示例

HTTP

```
POST /v2.0/esign/files/uploadUrls HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "contentMd5" : "nOA3Ixxx",
  "contentType" : "application/octet-stream",
  "fileName" : "合同.pdf",
  "fileSize" : 88888,
  "convert2Pdf" : false
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_2_0.*;
import com.aliyun.dingtalkesign_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_2_0.Client client = Sample.createClient();
        GetFileUploadUrlHeaders getFileUploadUrlHeaders = new GetFileUploadUrlHeaders();
        getFileUploadUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetFileUploadUrlRequest getFileUploadUrlRequest = new GetFileUploadUrlRequest()
                .setContentMd5("nOA3Ixxx")
                .setContentType("application/octet-stream")
                .setFileName("合同.pdf")
                .setFileSize(88888L)
                .setConvert2Pdf(false);
        try {
            client.getFileUploadUrlWithOptions(getFileUploadUrlRequest, getFileUploadUrlHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_2_0.client import Client as dingtalkesign_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_upload_url_headers = dingtalkesign__2__0_models.GetFileUploadUrlHeaders()
        get_file_upload_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_file_upload_url_request = dingtalkesign__2__0_models.GetFileUploadUrlRequest(
            content_md_5='nOA3Ixxx',
            content_type='application/octet-stream',
            file_name='合同.pdf',
            file_size=88888,
            convert_2pdf=False
        )
        try:
            client.get_file_upload_url_with_options(get_file_upload_url_request, get_file_upload_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_upload_url_headers = dingtalkesign__2__0_models.GetFileUploadUrlHeaders()
        get_file_upload_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_file_upload_url_request = dingtalkesign__2__0_models.GetFileUploadUrlRequest(
            content_md_5='nOA3Ixxx',
            content_type='application/octet-stream',
            file_name='合同.pdf',
            file_size=88888,
            convert_2pdf=False
        )
        try:
            await client.get_file_upload_url_with_options_async(get_file_upload_url_request, get_file_upload_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\GetFileUploadUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\GetFileUploadUrlRequest;
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
        $getFileUploadUrlHeaders = new GetFileUploadUrlHeaders([]);
        $getFileUploadUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFileUploadUrlRequest = new GetFileUploadUrlRequest([
            "contentMd5" => "nOA3Ixxx",
            "contentType" => "application/octet-stream",
            "fileName" => "合同.pdf",
            "fileSize" => 88888,
            "convert2Pdf" => false
        ]);
        try {
            $client->getFileUploadUrlWithOptions($getFileUploadUrlRequest, $getFileUploadUrlHeaders, new RuntimeOptions([]));
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
  dingtalkesign_2_0  ""github.com/alibabacloud-go/dingtalk/esign_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_2_0.Client{}
  _result, _err = dingtalkesign_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getFileUploadUrlHeaders := &dingtalkesign_2_0.GetFileUploadUrlHeaders{}
  getFileUploadUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFileUploadUrlRequest := &dingtalkesign_2_0.GetFileUploadUrlRequest{
    ContentMd5: tea.String("nOA3Ixxx"),
    ContentType: tea.String("application/octet-stream"),
    FileName: tea.String("合同.pdf"),
    FileSize: tea.Int64(88888),
    Convert2Pdf: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFileUploadUrlWithOptions(getFileUploadUrlRequest, getFileUploadUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_2_0, * as $dingtalkesign_2_0 from '"@alicloud/dingtalk/esign_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFileUploadUrlHeaders = new $dingtalkesign_2_0.GetFileUploadUrlHeaders({ });
    getFileUploadUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getFileUploadUrlRequest = new $dingtalkesign_2_0.GetFileUploadUrlRequest({
      contentMd5: "nOA3Ixxx",
      contentType: "application/octet-stream",
      fileName: "合同.pdf",
      fileSize: 88888,
      convert2Pdf: false,
    });
    try {
      await client.getFileUploadUrlWithOptions(getFileUploadUrlRequest, getFileUploadUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetFileUploadUrlHeaders getFileUploadUrlHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetFileUploadUrlHeaders();
            getFileUploadUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetFileUploadUrlRequest getFileUploadUrlRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetFileUploadUrlRequest
            {
                ContentMd5 = "nOA3Ixxx",
                ContentType = "application/octet-stream",
                FileName = "合同.pdf",
                FileSize = 88888,
                Convert2Pdf = false,
            };
            try
            {
                client.GetFileUploadUrlWithOptions(getFileUploadUrlRequest, getFileUploadUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__2__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_2_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_2_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_2_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::GetFileUploadUrlHeaders> getFileUploadUrlHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::GetFileUploadUrlHeaders>();
  getFileUploadUrlHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::GetFileUploadUrlRequest> getFileUploadUrlRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::GetFileUploadUrlRequest>(map<string, boost::any>({
    {"contentMd5", boost::any(string("nOA3Ixxx"))},
    {"contentType", boost::any(string("application/octet-stream"))},
    {"fileName", boost::any(string("合同.pdf"))},
    {"fileSize", boost::any(88888)},
    {"convert2Pdf", boost::any(false)}
  }));
  try {
    client->getFileUploadUrlWithOptions(getFileUploadUrlRequest, getFileUploadUrlHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| fileId | String | 文件ID。 |
| uploadUrl | String | 文件直传地址, 可以重复使用，但是只能传相同的文件，有效期一小时。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "fileId" : "748435c2xxxxx",
  "uploadUrl" : "https://xxx.com/xxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | createOrgAccountError | 创建企业账号异常 | 创建企业账号异常 |
| 400 | getUserInfoError | 获取用户信息异常 | 获取用户信息异常 |
| 400 | getFileUploadUrlError | 获取文件上传地址异常 | 获取文件上传地址异常 |
