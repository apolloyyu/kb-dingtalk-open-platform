---
title: "提交文件"
source_url: "https://open.dingtalk.com/document/development/submittal-file"
namespace: "development"
slug: "submittal-file"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件传输 > 提交文件"
doc_id: "XazD1mswsn"
updated_at: "2026-08-19 17:20:26"
---

> Source: https://open.dingtalk.com/document/development/submittal-file
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件传输 > 提交文件
> Updated: 2026-08-19 17:20:26

# 提交文件

调用本接口，提交文件。

## **接口调用说明**

接口调用步骤如下：

步骤一：调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，获取上传文件需要的信息。

步骤二：使用OSS的header加签方式上传文件，参考示例：

Java

```
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
public void test(){
               // 从接口返回信息中拿到url
                String resourceUrl = "第一步接口获取的resourceUrls";
              // 从接口返回信息中拿到headers
                Map<String, String> headers = 第一步接口获取的headers；
                URL url = new URL(resourceUrl);
                HttpURLConnection connection = (HttpURLConnection)url.openConnection();
               if (headers != null) {
                for (Map.Entry<String, String> entry : headers.entrySet()) {
                    connection.setRequestProperty(entry.getKey(), entry.getValue());
                }
            }
                connection.setDoOutput(true);
                connection.setRequestMethod("PUT");
                connection.setUseCaches(false);
                connection.setReadTimeout(10000);
                connection.setConnectTimeout(10000);
                connection.connect();
                OutputStream out = connection.getOutputStream();
                InputStream is = new FileInputStream(new File("/Users/xxxxx/Desktop/测试文件.xls"));
                byte[] b =new byte[1024];
                int temp;
                while ((temp=is.read(b))!=-1){
                       out.write(b,0,temp);
                }
                out.flush();
                out.close();
                int responseCode = connection.getResponseCode();
                connection.disconnect();
                if (responseCode == 200) {
                    System.out.println("上传成功");
                 } else {
                    System.out.println("上传失败");
                 }
}
```

Python

```
#!/usr/bin/env python

import requests

url = '<第一步接口获取的resourceUrl>'
headers = <第一步接口返回的headers>
result = requests.put(url, data=open('<path_to_file>', 'rb'), headers=headers)
print(result)
```

C#

```
public static string HttpRequest(string url, string filePath, Dictionary<string, string> headers) {

    FileStream fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
    BinaryReader reader = new BinaryReader(fileStream);
    reader.BaseStream.Seek(0, SeekOrigin.Begin);
    byte[] datas = reader.ReadBytes((int)reader.BaseStream.Length);
    HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
    request.Method = "PUT";
    request.Timeout = 150000;
    foreach (var header in headers) {
        request.Headers.Add($"{header.Key}", $"{header.Value}");
    }
    Stream requestStream = null;
    string responseStr = null;
    try {
        if (datas != null) {
            request.ContentLength = datas.Length;
            requestStream = request.GetRequestStream();
            requestStream.Write(datas, 0, datas.Length);
            requestStream.Close();
        } else {
            request.ContentLength = 0;
        }
        HttpWebResponse response = request.GetResponse() as HttpWebResponse;
        responseStr = response.Headers.GetValues("x-oss-request-id")[0];
    } catch (Exception ex) {
        Console.WriteLine("error");
    } finally {
        request = null;
        requestStream = null;
    }
    return responseStr;
}
```

PHP

```
$url = $result->body->headerSignatureInfo->resourceUrls[0];
$headersSource = $result->body->headerSignatureInfo->headers;
foreach ($headersSource as $key => $value) {
$headers[] = $key . ': ' . $value;
}
// 需要主动指定content-type为空
$headers['Content-Type'] = '';

$file = '/Users/dengxian.ldx/Desktop/test.txt';

$ch = curl_init();
curl_setopt_array($ch, array(
CURLOPT_URL => $url,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_HEADER => true,
CURLOPT_TIMEOUT => 100,
CURLOPT_CONNECTTIMEOUT => 100,
CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
CURLOPT_PUT => true,
CURLOPT_HTTPHEADER => $headers,
CURLOPT_SSL_VERIFYPEER => false,
CURLOPT_SSL_VERIFYHOST => false,
));
curl_setopt($ch, CURLOPT_INFILE, fopen($file , 'rb'));
curl_setopt($ch, CURLOPT_INFILESIZE, filesize($file) );
curl_setopt($ch, CURLOPT_UPLOAD, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response .PHP_EOL;
```

Node.js

```
const fs = require('fs');
const request = require('request-promise');

url = <url>;
header = <headers>;

// 注意: 需要主动指定content-type为空
headers['content-type']='';

var options = {
  method: 'PUT',
  url: url,
  headers: headers
};

fs.createReadStream('/Users/dengxian.ldx/temp/test/a.txt').pipe(request(options)).then(body =>{
  console.log(body);
}).catch(err => {
  console.log(err);
});
```

步骤三：调用本接口提交文件，完成文件上传。

> **[!NOTE]**
>
> - 存储空间类型为USER时，空间拥有权限的用户都有操作权限，其他员工调用[添加权限](0681-add-permissions-file.md)接口进行授权。
> - 存储空间类型为APP时，任何人操作都需要调用[添加权限](0681-add-permissions-file.md)接口进行授权。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/storage/spaces/files/{parentDentryUuid}/commit |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Write-企业存储文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| parentDentryUuid | String | 是 | 父节点dentryUuid，可调用[搜索文件](0638-search-for-files.md)或[获取 dentryUuid 信息](0672-api-getuuidbydentryid.md)接口，获取返回参数`dentryUuid`字段。    如果是空间根目录，填空间根目录的dentryUuid。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| uploadKey | String | 是 | 添加文件唯一标识，调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口获取uploadKey参数值。 |
| name | String | 是 | 文件的名称，带后缀。命名有以下要求：   - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、| - 不能以"."结尾 |
| option | Object | 否 | 可选参数。 |
| size | Long | 否 | 默认文件大小，单位:Byte。  **[!NOTE]**  如果此字段不为空，企业存储系统会校验文件实际大小是否和此字段是否一致，不一致会报错 |
| conflictStrategy | String | 否 | 文件名称冲突策略：   - **AUTO\_RENAME（默认）**：自动重命名。 - **OVERWRITE**：覆盖 - **RETURN\_DENTRY\_IF\_EXISTS**：返回已存在文件 - **RETURN\_ERROR\_IF\_EXISTS**：文件已存在时报错 |
| appProperties | Array | 否 | 当前文件的应用属性列表，最大值3。 |
| name | String | 是 | 属性名称。  **[!NOTE]**  该属性名称在当前app下需要保证唯一，不同app间同名属性互不影响。 |
| value | String | 是 | 属性值。 |
| visibility | String | 是 | 属性可见性：   - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见 |
| convertToOnlineDoc | Boolean | 否 | 是否转换成在线文档：   - **false**（默认值）：否 - **true**：是 |
| convertToOnlineDocTargetDocumentType | String | 否 | 转换成在线文档目标格式，未指定时按源文件后缀得到目标格式：   - **DOC**：钉钉文档 - **WORKBOOK**：钉钉表格 - **SMART\_TABLE**：钉钉多维表 |
| classificationLabelId | String | 否 | 文件密级的UUID。 |

### 请求示例

HTTP

```
POST /v2.0/storage/spaces/files/uuid/commit?unionId=union_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "uploadKey" : "upload_key",
  "name" : "dentry_name",
  "option" : {
    "size" : 512,
    "conflictStrategy" : "AUTO_RENAME",
    "appProperties" : [ {
      "name" : "property_name",
      "value" : "property_value",
      "visibility" : "PRIVATE"
    } ],
    "convertToOnlineDoc" : false,
    "convertToOnlineDocTargetDocumentType" : "DOC",
    "classificationLabelId" : "880787xxxxaf08b6"
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
    public static com.aliyun.dingtalkstorage_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkstorage_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_2_0.models.CommitFileHeaders commitFileHeaders = new com.aliyun.dingtalkstorage_2_0.models.CommitFileHeaders();
        commitFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_2_0.models.CommitFileRequest.CommitFileRequestOptionAppProperties optionAppProperties0 = new com.aliyun.dingtalkstorage_2_0.models.CommitFileRequest.CommitFileRequestOptionAppProperties()
                .setName("property_name")
                .setValue("property_value")
                .setVisibility("PRIVATE");
        com.aliyun.dingtalkstorage_2_0.models.CommitFileRequest.CommitFileRequestOption option = new com.aliyun.dingtalkstorage_2_0.models.CommitFileRequest.CommitFileRequestOption()
                .setSize(512L)
                .setConflictStrategy("AUTO_RENAME")
                .setAppProperties(java.util.Arrays.asList(
                    optionAppProperties0
                ))
                .setConvertToOnlineDoc(false)
                .setConvertToOnlineDocTargetDocumentType("DOC")
                .setClassificationLabelId("88078761-1821-47c3-9825-24db78af08b6");
        com.aliyun.dingtalkstorage_2_0.models.CommitFileRequest commitFileRequest = new com.aliyun.dingtalkstorage_2_0.models.CommitFileRequest()
                .setUnionId("union_id")
                .setUploadKey("upload_key")
                .setName("dentry_name")
                .setOption(option);
        try {
            client.commitFileWithOptions("uuid", commitFileRequest, commitFileHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.storage_2_0.client import Client as dingtalkstorage_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_2_0 import models as dingtalkstorage__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        commit_file_headers = dingtalkstorage__2__0_models.CommitFileHeaders()
        commit_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_app_properties_0 = dingtalkstorage__2__0_models.CommitFileRequestOptionAppProperties(
            name='property_name',
            value='property_value',
            visibility='PRIVATE'
        )
        option = dingtalkstorage__2__0_models.CommitFileRequestOption(
            size=512,
            conflict_strategy='AUTO_RENAME',
            app_properties=[
                option_app_properties_0
            ],
            convert_to_online_doc=False,
            convert_to_online_doc_target_document_type='DOC',
            classification_label_id='88078761-1821-47c3-9825-24db78af08b6'
        )
        commit_file_request = dingtalkstorage__2__0_models.CommitFileRequest(
            union_id='union_id',
            upload_key='upload_key',
            name='dentry_name',
            option=option
        )
        try:
            client.commit_file_with_options('uuid', commit_file_request, commit_file_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        commit_file_headers = dingtalkstorage__2__0_models.CommitFileHeaders()
        commit_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_app_properties_0 = dingtalkstorage__2__0_models.CommitFileRequestOptionAppProperties(
            name='property_name',
            value='property_value',
            visibility='PRIVATE'
        )
        option = dingtalkstorage__2__0_models.CommitFileRequestOption(
            size=512,
            conflict_strategy='AUTO_RENAME',
            app_properties=[
                option_app_properties_0
            ],
            convert_to_online_doc=False,
            convert_to_online_doc_target_document_type='DOC',
            classification_label_id='88078761-1821-47c3-9825-24db78af08b6'
        )
        commit_file_request = dingtalkstorage__2__0_models.CommitFileRequest(
            union_id='union_id',
            upload_key='upload_key',
            name='dentry_name',
            option=option
        )
        try:
            await client.commit_file_with_options_async('uuid', commit_file_request, commit_file_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\CommitFileHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\CommitFileRequest\option\appProperties;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\CommitFileRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\CommitFileRequest;
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
        $commitFileHeaders = new CommitFileHeaders([]);
        $commitFileHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $optionAppProperties0 = new appProperties([
            "name" => "property_name",
            "value" => "property_value",
            "visibility" => "PRIVATE"
        ]);
        $option = new option([
            "size" => 512,
            "conflictStrategy" => "AUTO_RENAME",
            "appProperties" => [
                $optionAppProperties0
            ],
            "convertToOnlineDoc" => false,
            "convertToOnlineDocTargetDocumentType" => "DOC",
            "classificationLabelId" => "88078761-1821-47c3-9825-24db78af08b6"
        ]);
        $commitFileRequest = new CommitFileRequest([
            "unionId" => "union_id",
            "uploadKey" => "upload_key",
            "name" => "dentry_name",
            "option" => $option
        ]);
        try {
            $client->commitFileWithOptions("uuid", $commitFileRequest, $commitFileHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_2_0  "github.com/alibabacloud-go/dingtalk/storage_2_0"
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
func CreateClient () (_result *dingtalkstorage_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_2_0.Client{}
  _result, _err = dingtalkstorage_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  commitFileHeaders := &dingtalkstorage_2_0.CommitFileHeaders{}
  commitFileHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionAppProperties0 := &dingtalkstorage_2_0.CommitFileRequestOptionAppProperties{
    Name: tea.String("property_name"),
    Value: tea.String("property_value"),
    Visibility: tea.String("PRIVATE"),
  }
  option := &dingtalkstorage_2_0.CommitFileRequestOption{
    Size: tea.Int64(512),
    ConflictStrategy: tea.String("AUTO_RENAME"),
    AppProperties: []*dingtalkstorage_2_0.CommitFileRequestOptionAppProperties{optionAppProperties0},
    ConvertToOnlineDoc: tea.Bool(false),
    ConvertToOnlineDocTargetDocumentType: tea.String("DOC"),
    ClassificationLabelId: tea.String("88078761-1821-47c3-9825-24db78af08b6"),
  }
  commitFileRequest := &dingtalkstorage_2_0.CommitFileRequest{
    UnionId: tea.String("union_id"),
    UploadKey: tea.String("upload_key"),
    Name: tea.String("dentry_name"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CommitFileWithOptions(tea.String("uuid"), commitFileRequest, commitFileHeaders, &util.RuntimeOptions{})
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
const dingtalkstorage_2_0 = require('@alicloud/dingtalk/storage_2_0');
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
    return new dingtalkstorage_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let commitFileHeaders = new dingtalkstorage_2_0.CommitFileHeaders({ });
    commitFileHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let optionAppProperties0 = new dingtalkstorage_2_0.CommitFileRequestOptionAppProperties({
      name: 'property_name',
      value: 'property_value',
      visibility: 'PRIVATE',
    });
    let option = new dingtalkstorage_2_0.CommitFileRequestOption({
      size: 512,
      conflictStrategy: 'AUTO_RENAME',
      appProperties: [
        optionAppProperties0
      ],
      convertToOnlineDoc: false,
      convertToOnlineDocTargetDocumentType: 'DOC',
      classificationLabelId: '88078761-1821-47c3-9825-24db78af08b6',
    });
    let commitFileRequest = new dingtalkstorage_2_0.CommitFileRequest({
      unionId: 'union_id',
      uploadKey: 'upload_key',
      name: 'dentry_name',
      option: option,
    });
    try {
      await client.commitFileWithOptions('uuid', commitFileRequest, commitFileHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileHeaders commitFileHeaders = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileHeaders();
            commitFileHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest.CommitFileRequestOption.CommitFileRequestOptionAppProperties optionAppProperties0 = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest.CommitFileRequestOption.CommitFileRequestOptionAppProperties
            {
                Name = "property_name",
                Value = "property_value",
                Visibility = "PRIVATE",
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest.CommitFileRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest.CommitFileRequestOption
            {
                Size = 512,
                ConflictStrategy = "AUTO_RENAME",
                AppProperties = new List<AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest.CommitFileRequestOption.CommitFileRequestOptionAppProperties>
                {
                    optionAppProperties0
                },
                ConvertToOnlineDoc = false,
                ConvertToOnlineDocTargetDocumentType = "DOC",
                ClassificationLabelId = "88078761-1821-47c3-9825-24db78af08b6",
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest commitFileRequest = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.CommitFileRequest
            {
                UnionId = "union_id",
                UploadKey = "upload_key",
                Name = "dentry_name",
                Option = option,
            };
            try
            {
                client.CommitFileWithOptions("uuid", commitFileRequest, commitFileHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dentry | Object | 文件信息。 |
| id | String | 文件id。 |
| spaceId | String | 所在空间id。 |
| parentId | String | 父目录Id。根目录时，该参数是0。    空值代表根目录的parentId不存在。 |
| type | String | 类型，目录或文件，枚举值:   - **FILE**：文件 - **FOLDER**：文件夹 |
| name | String | 文件名称。 |
| size | Long | 文件大小, 单位:Byte。 |
| path | String | 文件在空间内的路径。 |
| version | Long | 版本。 |
| status | String | 状态：   - **NORMAL**：正常 - **DELETED**：已删除 - **EXPIRED**：已过期 |
| extension | String | 文件后缀。 |
| creatorId | String | 创建者unionId。 |
| modifierId | String | 修改者unionId。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| properties | Object | 文件属性。 |
| readOnly | Boolean | 文件是否只读。   - **true**：是 - **false**：否 |
| appProperties | Map<String, Array> | 在特定应用上的属性。key是所属空间的ownerId，value是属性列表。 |
|  | Array | 属性列表。 |
| name | String | 属性名称。 |
| value | String | 属性值。 |
| visibility | String | 属性可见性。   - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见 |
| uuid | String | 唯一标识uuid，如移动文件，此字段不变。 |
| partitionType | String | 存储分区：   - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属MiniOSS存储分区 |
| storageDriver | String | 驱动类型，枚举值:   - **DINGTALK**：钉钉统一存储驱动 - **ALIDOC**：钉钉文档存储驱动 - **SHANJI**：闪记存储驱动 - **UNKNOWN**：未知驱动 |
| thumbnail | Object | 缩略图信息。 |
| width | Integer | 缩略图宽度。 |
| height | Integer | 缩略图高度。 |
| url | String | 缩略图url。 |
| category | String | 类别，枚举值:   - **IMAGE**：图片 - **VIDEO**：视频 - **AUDIO**：音频 - **ARCHIVE**：压缩包 - **SHORTCUT**：快捷方式 - **DOCUMENT**：文档 - **ALI\_DOC**：钉钉文档 - **OTHER**：其它 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "dentry" : {
    "id" : "dentry_id",
    "spaceId" : "space_id",
    "parentId" : "parent_id",
    "type" : "FILE",
    "name" : "dentry_name",
    "size" : 512,
    "path" : "dentry_path",
    "version" : 1,
    "status" : "NORMAL",
    "extension" : "txt",
    "creatorId" : "creator_id",
    "modifierId" : "modifier_id",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "properties" : {
      "readOnly" : true
    },
    "appProperties" : [ {
      "name" : "property_name",
      "value" : "property_value",
      "visibility" : "PRIVATE"
    } ],
    "uuid" : "uuid",
    "partitionType" : "PUBLIC_OSS_PARTITION",
    "storageDriver" : "DINGTALK",
    "thumbnail" : {
      "width" : 64,
      "height" : 64,
      "url" : "url"
    },
    "category" : "DOCUMENT"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | operationConcurrentControl | %s | 并发控制 |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.parentDentryUuid | %s | 参数错误-parentDentryUuid |
| 400 | paramError.uploadKey | %s | 参数错误-uploadKey |
| 400 | paramError.name | %s | 参数错误-name |
| 400 | paramError.conflictStrategy | %s | 参数错误-conflictStrategy |
| 400 | spaceQuotaInsufficient | %s | 空间容量不足 |
| 400 | sceneQuotaInsufficient | %s | 场景容量不足 |
| 400 | appQuotaInsufficient | %s | 应用容量不足 |
| 400 | orgQuotaInsufficient | %s | 企业容量不足 |
| 400 | dentryNameIllegal | %s | 文件名非法 |
| 400 | dentryStoreError | %s | 文件存储异常 |
| 400 | dentryNameConflict | %s | 文件名冲突 |
| 400 | dentryFormatNotSupport | %s | 不支持的文件格式 |
| 403 | permissionDenied | %s | 用户缺少上传文件的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
