---
title: "添加智能招聘文件到钉盘"
source_url: "https://open.dingtalk.com/document/development/add-nail-disk-file"
namespace: "development"
slug: "add-nail-disk-file"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 添加智能招聘文件到钉盘"
doc_id: "lFe1W2Hkbc"
updated_at: "2026-07-14 09:22:33"
---

> Source: https://open.dingtalk.com/document/development/add-nail-disk-file
> Path: 应用开发 / 服务端 API / 智能招聘 > 添加智能招聘文件到钉盘
> Updated: 2026-07-14 09:22:33

# 添加智能招聘文件到钉盘

调用本接口，将文件保存到智能招聘的钉盘空间。

## **接口调用说明**

本接口需要和其他接口结合使用。例如，获取到文件ID和空间ID，调用其他和文件相关的业务类接口，添加简历、添加面试评价表等。添加简历、添加面试评价表等能力后续开放，请关注文档更新。

> **[!NOTE]**
>
> 企业授权开通智能招聘产品时，会在钉盘下自动生成一个智能招聘专用的钉盘空间。
>
> - 调用本接口，可以将文件上传到智能招聘专用的钉盘空间。
> - 智能招聘相关文件的操作，都需要在智能招聘钉盘空间下操作才会生效，调用[钉盘-上传文件到钉盘](1564-add-file-and-folder.md)无法实现。

本接口使用步骤如下：

步骤一：调用[获取智能招聘文件上传信息](0966-obtain-information-about-the-dingtalk-disk-upload-file.md)口，获取文件上传OSS的临时凭证。

步骤二：根据获取的上传OSS的临时凭证，通过以下步骤将文件上传到OSS空间。

1. 安装OSS上传文件的SDK，参考[如何在OSS上安装SDK](https://help.aliyun.com/document_detail/32009.html?spm=ding_open_doc.document.0.0.7dbe722fCqAQdx)。
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

步骤三：调用本接口，将智能招聘文件保存到钉盘空间。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/files |
| HTTP Method | POST |
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
| opUserId | String | 否 | 操作人的userId。    如果该参数为空，默认以企业创建者身份进行操作。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| mediaId | String | 是 | 文件mediaId，调用[获取智能招聘文件上传信息](0966-obtain-information-about-the-dingtalk-disk-upload-file.md)接口获取。    调用[获取智能招聘文件上传信息](0966-obtain-information-about-the-dingtalk-disk-upload-file.md)接口获取的mediaId，必须使用OSS上传后才能使用，上传流程请参考本文档介绍的接口调用流程示例。否则本接口会出现报错**钉盘空间不可用**。 |
| fileName | String | 是 | 文件名称。    需要包含扩展名。 |

### 请求示例

HTTP

```
POST /v1.0/ats/files?bizCode=ddats&opUserId=manager5875 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c652e6841b5339b6ba2fa835785b32e8
Content-Type:application/json

{
  "mediaId" : "xxx",
  "fileName" : "张三的简历.pdf"
}
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
        AddFileHeaders addFileHeaders = new AddFileHeaders();
        addFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddFileRequest addFileRequest = new AddFileRequest()
                .setBizCode("ddats")
                .setOpUserId("manager5875")
                .setMediaId("xxx")
                .setFileName("张三的简历.pdf");
        try {
            client.addFileWithOptions(addFileRequest, addFileHeaders, new RuntimeOptions());
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
        add_file_headers = dingtalkats__1__0_models.AddFileHeaders()
        add_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_file_request = dingtalkats__1__0_models.AddFileRequest(
            biz_code='ddats',
            op_user_id='manager5875',
            media_id='xxx',
            file_name='张三的简历.pdf'
        )
        try:
            client.add_file_with_options(add_file_request, add_file_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_file_headers = dingtalkats__1__0_models.AddFileHeaders()
        add_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_file_request = dingtalkats__1__0_models.AddFileRequest(
            biz_code='ddats',
            op_user_id='manager5875',
            media_id='xxx',
            file_name='张三的简历.pdf'
        )
        try:
            await client.add_file_with_options_async(add_file_request, add_file_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\AddFileHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\AddFileRequest;
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
        $addFileHeaders = new AddFileHeaders([]);
        $addFileHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addFileRequest = new AddFileRequest([
            "bizCode" => "ddats",
            "opUserId" => "manager5875",
            "mediaId" => "xxx",
            "fileName" => "张三的简历.pdf"
        ]);
        try {
            $client->addFileWithOptions($addFileRequest, $addFileHeaders, new RuntimeOptions([]));
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

  addFileHeaders := &dingtalkats_1_0.AddFileHeaders{}
  addFileHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addFileRequest := &dingtalkats_1_0.AddFileRequest{
    BizCode: tea.String("ddats"),
    OpUserId: tea.String("manager5875"),
    MediaId: tea.String("xxx"),
    FileName: tea.String("张三的简历.pdf"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddFileWithOptions(addFileRequest, addFileHeaders, &util.RuntimeOptions{})
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
    let addFileHeaders = new $dingtalkats_1_0.AddFileHeaders({ });
    addFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let addFileRequest = new $dingtalkats_1_0.AddFileRequest({
      bizCode: "ddats",
      opUserId: "manager5875",
      mediaId: "xxx",
      fileName: "张三的简历.pdf",
    });
    try {
      await client.addFileWithOptions(addFileRequest, addFileHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.AddFileHeaders addFileHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.AddFileHeaders();
            addFileHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.AddFileRequest addFileRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.AddFileRequest
            {
                BizCode = "ddats",
                OpUserId = "manager5875",
                MediaId = "xxx",
                FileName = "张三的简历.pdf",
            };
            try
            {
                client.AddFileWithOptions(addFileRequest, addFileHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| spaceId | Long | 空间标识。 |
| fileId | String | 文件标识。 |
| fileName | String | 文件名。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "spaceId" : 123456,
  "fileId" : "111111",
  "fileName" : "张三的简历"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | %s | 无效参数 |
| 500 | systemError | 系统错误 | 系统错误 |
| 503 | systemError.dingSpaceError | 钉盘服务不可用 | 钉盘服务不可用，可以稍后重试 |
