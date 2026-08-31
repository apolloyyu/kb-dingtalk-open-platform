---
title: "获取智能招聘文件上传信息"
source_url: "https://open.dingtalk.com/document/development/obtain-information-about-the-dingtalk-disk-upload-file"
namespace: "development"
slug: "obtain-information-about-the-dingtalk-disk-upload-file"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 获取智能招聘文件上传信息"
doc_id: "vUbq1ngLWv"
updated_at: "2026-06-04 19:10:36"
---

> Source: https://open.dingtalk.com/document/development/obtain-information-about-the-dingtalk-disk-upload-file
> Path: 应用开发 / 服务端 API / 智能招聘 > 获取智能招聘文件上传信息
> Updated: 2026-06-04 19:10:36

# 获取智能招聘文件上传信息

调用本接口获取智能招聘文件上传到钉盘所需的信息，如accessKeyId信息和accessKeySecret信息等。

## **接口调用说明**

接口使用步骤，如下：

步骤一：调用本接口，获取文件上传OSS的临时凭证。

步骤二：根据返回的上传OSS的临时凭证，参考以下步骤将文件上传到OSS空间。

1. 安装SSO上传文件的SDK，参考[安装OSS上传SDK](https://help.aliyun.com/document_detail/32009.html?spm=ding_open_doc.document.0.0.7dbe722fCqAQdx)。
2. 使用以下示例执行上传操作。

   ```
   public static void main(String[] args) {
    // 以下参数为步骤1返回的上传凭证
    // 阿里云账号的临时accessKeyId。
    String accessKeyId = "<accessKeyId>";
    // 阿里云账号的临时accessKeySecret。
    String accessKeySecret = "<accessKeySecret>";
    // 临时访问密钥。
    String securityToken = "<accessToken>";
    // OSS访问域名。
    String endpoint = "<endpoint>";
    // OSS存储空间。
    String bucket = "<bucket>";
    // 对应OSS Object Key，可用于刷新token以及调用添加文件（夹）接口添加文件记录。
    String ossKey = "<mediaId>";
    DefaultCredentialProvider defaultCredentialProvider = new 
    DefaultCredentialProvider(accessKeyId, accessKeySecret, securityToken);
    ClientConfiguration clientConfiguration = new ClientConfiguration();
    clientConfiguration.setProtocol(Protocol.HTTPS); // 注意, 需要是HTTPS
    OSSClient ossClient = new OSSClient(endpoint, credentialsProvider, clientConfiguration);
    PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, ossKey, new File("文件绝对路径"));
    ossClient.putObject(putObjectRequest);
    // 关闭OSSClient。
    ossClient.shutdown();
    }
   ```

步骤三：调用[添加智能招聘文件到钉盘](0967-add-nail-disk-file.md)接口，将文件保存到钉盘空间。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/files/uploadInfos |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_recruitment\_plugin-智能招聘插件管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizCode | String | 否 | 业务标识，默认值为`ddats`。    如果传该参数，只支持`ddats`。 |
| fileName | String | 是 | 文件名称。 |
| fileSize | Long | 是 | 文件大小，单位字节。    主要用于预检查钉盘剩余空间。 |
| md5 | String | 是 | 文件MD5摘要，示例：`DigestUtils.md5Hex(new FileInputStream("/Users/xxxx/Desktop/111.doc")` |
| opUserId | String | 否 | 当前操作者的userId。    如果该参数为空，默认以企业创建者身份进行操作。 |

### 请求示例

HTTP

```
GET /v1.0/ats/files/uploadInfos?bizCode=ddats&fileName=张三的简历&fileSize=1024&md5=xxx&opUserId=manager5875 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkats_1_0.*;
import com.aliyun.dingtalkats_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkats_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkats_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkats_1_0.Client client = Sample.createClient();
        GetFileUploadInfoHeaders getFileUploadInfoHeaders = new GetFileUploadInfoHeaders();
        getFileUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetFileUploadInfoRequest getFileUploadInfoRequest = new GetFileUploadInfoRequest()
                .setBizCode("ddats")
                .setFileName("张三的简历")
                .setFileSize(1024L)
                .setMd5("xxx")
                .setOpUserId("manager5875");
        try {
            client.getFileUploadInfoWithOptions(getFileUploadInfoRequest, getFileUploadInfoHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.ats_1_0.client import Client as dingtalkats_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.ats_1_0 import models as dingtalkats__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkats_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkats_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_upload_info_headers = dingtalkats__1__0_models.GetFileUploadInfoHeaders()
        get_file_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_file_upload_info_request = dingtalkats__1__0_models.GetFileUploadInfoRequest(
            biz_code='ddats',
            file_name='张三的简历',
            file_size=1024,
            md_5='xxx',
            op_user_id='manager5875'
        )
        try:
            client.get_file_upload_info_with_options(get_file_upload_info_request, get_file_upload_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_upload_info_headers = dingtalkats__1__0_models.GetFileUploadInfoHeaders()
        get_file_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_file_upload_info_request = dingtalkats__1__0_models.GetFileUploadInfoRequest(
            biz_code='ddats',
            file_name='张三的简历',
            file_size=1024,
            md_5='xxx',
            op_user_id='manager5875'
        )
        try:
            await client.get_file_upload_info_with_options_async(get_file_upload_info_request, get_file_upload_info_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\GetFileUploadInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\GetFileUploadInfoRequest;
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
        $getFileUploadInfoHeaders = new GetFileUploadInfoHeaders([]);
        $getFileUploadInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFileUploadInfoRequest = new GetFileUploadInfoRequest([
            "bizCode" => "ddats",
            "fileName" => "张三的简历",
            "fileSize" => 1024,
            "md5" => "xxx",
            "opUserId" => "manager5875"
        ]);
        try {
            $client->getFileUploadInfoWithOptions($getFileUploadInfoRequest, $getFileUploadInfoHeaders, new RuntimeOptions([]));
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
  dingtalkats_1_0  "github.com/alibabacloud-go/dingtalk/ats_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkats_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkats_1_0.Client{}
  _result, _err = dingtalkats_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getFileUploadInfoHeaders := &dingtalkats_1_0.GetFileUploadInfoHeaders{}
  getFileUploadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFileUploadInfoRequest := &dingtalkats_1_0.GetFileUploadInfoRequest{
    BizCode: tea.String("ddats"),
    FileName: tea.String("张三的简历"),
    FileSize: tea.Int64(1024),
    Md5: tea.String("xxx"),
    OpUserId: tea.String("manager5875"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFileUploadInfoWithOptions(getFileUploadInfoRequest, getFileUploadInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkats_1_0, * as $dingtalkats_1_0 from '@alicloud/dingtalk/ats_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkats_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkats_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFileUploadInfoHeaders = new $dingtalkats_1_0.GetFileUploadInfoHeaders({ });
    getFileUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getFileUploadInfoRequest = new $dingtalkats_1_0.GetFileUploadInfoRequest({
      bizCode: "ddats",
      fileName: "张三的简历",
      fileSize: 1024,
      md5: "xxx",
      opUserId: "manager5875",
    });
    try {
      await client.getFileUploadInfoWithOptions(getFileUploadInfoRequest, getFileUploadInfoHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkats_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkats_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkats_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFileUploadInfoHeaders getFileUploadInfoHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFileUploadInfoHeaders();
            getFileUploadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFileUploadInfoRequest getFileUploadInfoRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFileUploadInfoRequest
            {
                BizCode = "ddats",
                FileName = "张三的简历",
                FileSize = 1024,
                Md5 = "xxx",
                OpUserId = "manager5875",
            };
            try
            {
                client.GetFileUploadInfoWithOptions(getFileUploadInfoRequest, getFileUploadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| bucket | String | OSS上传所需bucket信息。 |
| endPoint | String | OSS上传所需endPoint信息。 |
| accessKeyId | String | OSS上传所需accessKeyId信息。 |
| accessKeySecret | String | OSS上传所需accessKeySecret信息。 |
| accessToken | String | OSS上传所需accessToken信息。 |
| accessTokenExpirationMillis | Long | accessToken有效期截止时间戳，单位毫秒。    需要在此时间之前使用OSS功能完成文件上传。 |
| mediaId | String | 文件mediaId。    对应OSS的objectKey，调用OSS接口上传文件时需指定该值为OSS的objectKey。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "bucket" : "lippi-space-zjk",
  "endPoint" : "oss-cn-zhangjiakou.aliyuncs.com",
  "accessKeyId" : "xxx",
  "accessKeySecret" : "xxx",
  "accessToken" : "xxx",
  "accessTokenExpirationMillis" : 1626923829000,
  "mediaId" : "xxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | %s | 无效参数 |
| 500 | systemError | 系统错误 | 系统错误 |
| 503 | systemError.dingSpaceError | 钉盘服务不可用 | 钉盘服务不可用，可以稍后重试 |
