---
title: "获取文件上传信息"
source_url: "https://open.dingtalk.com/document/development/obtain-storage-upload-information"
namespace: "development"
slug: "obtain-storage-upload-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 存储管理 > 文件传输 > 获取文件上传信息"
doc_id: "0dzPk97EC5"
updated_at: "2026-08-25 09:38:59"
---

> Source: https://open.dingtalk.com/document/development/obtain-storage-upload-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 存储管理 > 文件传输 > 获取文件上传信息
> Updated: 2026-08-25 09:38:59

# 获取文件上传信息

调用本接口，获取文件上传信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 如果使用入参为spaceId字段，推荐使用本接口。
> - 如果使用入参为dentryUuid或者Uuid字段，建议使用新版[获取文件上传信息](0674-obtain-file-upload-informations.md)接口。

### 接口调用流程

步骤一：调用本接口，获取上传文件需要的`resourceUrls`和`headers`参数值。

步骤二：使用OSS的header加签方式上传文件，参考示例：

Java

```
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
public void test(){
  // 从接口返回信息中拿到resourceUrls
  String resourceUrl = "第一步接口返回的resourceUrls";
  // 从接口返回信息中拿到headers
  Map<String, String> headers = 第一步接口返回的headers;
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

步骤三：调用[提交文件](1601-submit-documents.md)接口，完成文件上传。

> **[!NOTE]**
>
> - 存储空间类型为USER时，只有空间拥有者和管理者有操作权限，其他员工均需要授权。
> - 存储空间类型为APP时，任何人操作都需要先进行授权。
>
> 可调用[添加权限](1596-add-storage-permissions.md)接口进行授权。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 企业存储文件上传信息读权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=storage_1.0%23GetFileUploadInfo) |
| 第三方企业应用 | 支持 | 企业存储文件上传信息读权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=storage_1.0%23GetFileUploadInfo) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/storage/spaces/{spaceId}/files/uploadInfos/query?unionId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "protocol" : "String",
  "multipart" : Boolean,
  "option" : {
    "storageDriver" : "String",
    "preCheckParam" : {
      "md5" : "String",
      "size" : Long,
      "parentId" : "String",
      "name" : "String"
    },
    "preferRegion" : "String",
    "preferIntranet" : Boolean
  }
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，调用[添加空间](0652-add-space.md)接口获取id参数值。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，调用[查询用户详情](0056-query-user-details.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| protocol | String | 是 | 通过指定上传协议返回不同协议上传所需要的信息。   - **HEADER\_SIGNATURE**：Header加签 |
| multipart | Boolean | 是 | 是否需要分片上传。   - **true**：需要 - **false**：不需要   **[!NOTE]**  - 5G以下文件，设为false，简化上传步骤。 - 5G以上文件，必须设为true，否则会上传失败。 |
| option | Object | 否 | 可选参数。 |
| storageDriver | String | 否 | 文件存储驱动类型。   - **DINGTALK**：钉钉统一存储驱动，默认值 - **ALIDOC**：钉钉文档存储驱动 - **UNKNOWN**：未知驱动 |
| preCheckParam | Object | 否 | 预检查的字段。  **[!NOTE]**  可实现对文件名称，文件完整性，容量的校验。 |
| md5 | String | 否 | 文件md5值，`DigestUtils.md5Hex()`。  **[!NOTE]**  文件完整性校验，不传则不做校验。 |
| size | Long | 否 | 文件大小，单位Byte。  **[!NOTE]**  容量相关校验，不传则不做校验。 |
| parentId | String | 否 | 父目录Id。根目录时，该参数是0。  **[!NOTE]**  用于同目录文件名冲突校验。 |
| name | String | 否 | 文件名称，命名有以下要求：   - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、| - 不能以"."结尾   > 文件名称合法性和文件名称冲突校验。 |
| preferRegion | String | 否 | 优先地域。   - **ZHANGJIAKOU**：张家口 - **SHENZHEN**：深圳 - **SHANGHAI**：上海 - **SINGAPORE**：新加坡 - **UNKNOWN**：未知   **[!NOTE]**  倾向于将资源存到哪个地域，可实现就近上传等功能。 |
| preferIntranet | Boolean | 否 | 是否优先使用内网传输，使用该参数前提是配置了专属存储内网传输。   - true：是，默认值 - false：否 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| uploadKey | String | 上传唯一标识。 |
| storageDriver | String | 文件存储类型。   - **DINGTALK**：钉钉统一存储驱动 - **ALIDOC**：钉钉文档存储驱动 - **UNKNOWN**：未知驱动 |
| protocol | String | 上传协议。   - **HEADER\_SIGNATURE**：Header加签 |
| headerSignatureInfo | Object | Header加签上传信息。  **[!NOTE]**  当protocol参数传HEADER\_SIGNATURE时，返回该字段。 |
| resourceUrls | Array of String | 多个上传下载URL列表。 |
| headers | Map<String, String> | 请求头信息。 |
| expirationSeconds | Integer | 过期时间，单位秒。 |
| region | String | 地域。   - **ZHANGJIAKOU**：张家口 - **SHENZHEN**：深圳 - **SHANGHAI**：上海 - **SINGAPORE**：新加坡 - **UNKNOWN**：未知 |
| internalResourceUrls | Array of String | 内网访问地址。  **[!NOTE]**  该字段目前无使用场景，请忽略。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/storage/spaces/854xxxxx/files/uploadInfos/query?unionId=cHtUxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "protocol" : "HEADER_SIGNATURE",
  "multipart" : false,
  "option" : {
    "storageDriver" : "DINGTALK",
    "preCheckParam" : {
      "md5" : "md5",
      "size" : 512,
      "parentId" : "parent_id",
      "name" : "dentry_name"
    },
    "preferRegion" : "ZHANGJIAKOU",
    "preferIntranet" : true
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
        com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoHeaders getFileUploadInfoHeaders = new com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoHeaders();
        getFileUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOptionPreCheckParam optionPreCheckParam = new com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOptionPreCheckParam()
                .setMd5("md5")
                .setSize(512L)
                .setParentId("parent_id")
                .setName("dentry_name");
        com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption()
                .setStorageDriver("DINGTALK")
                .setPreCheckParam(optionPreCheckParam)
                .setPreferRegion("ZHANGJIAKOU")
                .setPreferIntranet(true);
        com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoRequest getFileUploadInfoRequest = new com.aliyun.dingtalkstorage_1_0.models.GetFileUploadInfoRequest()
                .setUnionId("cHtUxxxxx")
                .setProtocol("HEADER_SIGNATURE")
                .setMultipart(false)
                .setOption(option);
        try {
            client.getFileUploadInfoWithOptions("854xxxxx", getFileUploadInfoRequest, getFileUploadInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_file_upload_info_headers = dingtalkstorage__1__0_models.GetFileUploadInfoHeaders()
        get_file_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_pre_check_param = dingtalkstorage__1__0_models.GetFileUploadInfoRequestOptionPreCheckParam(
            md_5='md5',
            size=512,
            parent_id='parent_id',
            name='dentry_name'
        )
        option = dingtalkstorage__1__0_models.GetFileUploadInfoRequestOption(
            storage_driver='DINGTALK',
            pre_check_param=option_pre_check_param,
            prefer_region='ZHANGJIAKOU',
            prefer_intranet=True
        )
        get_file_upload_info_request = dingtalkstorage__1__0_models.GetFileUploadInfoRequest(
            union_id='cHtUxxxxx',
            protocol='HEADER_SIGNATURE',
            multipart=False,
            option=option
        )
        try:
            client.get_file_upload_info_with_options('854xxxxx', get_file_upload_info_request, get_file_upload_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_upload_info_headers = dingtalkstorage__1__0_models.GetFileUploadInfoHeaders()
        get_file_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_pre_check_param = dingtalkstorage__1__0_models.GetFileUploadInfoRequestOptionPreCheckParam(
            md_5='md5',
            size=512,
            parent_id='parent_id',
            name='dentry_name'
        )
        option = dingtalkstorage__1__0_models.GetFileUploadInfoRequestOption(
            storage_driver='DINGTALK',
            pre_check_param=option_pre_check_param,
            prefer_region='ZHANGJIAKOU',
            prefer_intranet=True
        )
        get_file_upload_info_request = dingtalkstorage__1__0_models.GetFileUploadInfoRequest(
            union_id='cHtUxxxxx',
            protocol='HEADER_SIGNATURE',
            multipart=False,
            option=option
        )
        try:
            await client.get_file_upload_info_with_options_async('854xxxxx', get_file_upload_info_request, get_file_upload_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileUploadInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileUploadInfoRequest\option\preCheckParam;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileUploadInfoRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetFileUploadInfoRequest;
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
        $optionPreCheckParam = new preCheckParam([
            "md5" => "md5",
            "size" => 512,
            "parentId" => "parent_id",
            "name" => "dentry_name"
        ]);
        $option = new option([
            "storageDriver" => "DINGTALK",
            "preCheckParam" => $optionPreCheckParam,
            "preferRegion" => "ZHANGJIAKOU",
            "preferIntranet" => true
        ]);
        $getFileUploadInfoRequest = new GetFileUploadInfoRequest([
            "unionId" => "cHtUxxxxx",
            "protocol" => "HEADER_SIGNATURE",
            "multipart" => false,
            "option" => $option
        ]);
        try {
            $client->getFileUploadInfoWithOptions("854xxxxx", $getFileUploadInfoRequest, $getFileUploadInfoHeaders, new RuntimeOptions([]));
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

  getFileUploadInfoHeaders := &dingtalkstorage_1_0.GetFileUploadInfoHeaders{}
  getFileUploadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionPreCheckParam := &dingtalkstorage_1_0.GetFileUploadInfoRequestOptionPreCheckParam{
    Md5: tea.String("md5"),
    Size: tea.Int64(512),
    ParentId: tea.String("parent_id"),
    Name: tea.String("dentry_name"),
  }
  option := &dingtalkstorage_1_0.GetFileUploadInfoRequestOption{
    StorageDriver: tea.String("DINGTALK"),
    PreCheckParam: optionPreCheckParam,
    PreferRegion: tea.String("ZHANGJIAKOU"),
    PreferIntranet: tea.Bool(true),
  }
  getFileUploadInfoRequest := &dingtalkstorage_1_0.GetFileUploadInfoRequest{
    UnionId: tea.String("cHtUxxxxx"),
    Protocol: tea.String("HEADER_SIGNATURE"),
    Multipart: tea.Bool(false),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFileUploadInfoWithOptions(tea.String("854xxxxx"), getFileUploadInfoRequest, getFileUploadInfoHeaders, &util.RuntimeOptions{})
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
    let getFileUploadInfoHeaders = new $dingtalkstorage_1_0.GetFileUploadInfoHeaders({ });
    getFileUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let optionPreCheckParam = new $dingtalkstorage_1_0.GetFileUploadInfoRequestOptionPreCheckParam({
      md5: "md5",
      size: 512,
      parentId: "parent_id",
      name: "dentry_name",
    });
    let option = new $dingtalkstorage_1_0.GetFileUploadInfoRequestOption({
      storageDriver: "DINGTALK",
      preCheckParam: optionPreCheckParam,
      preferRegion: "ZHANGJIAKOU",
      preferIntranet: true,
    });
    let getFileUploadInfoRequest = new $dingtalkstorage_1_0.GetFileUploadInfoRequest({
      unionId: "cHtUxxxxx",
      protocol: "HEADER_SIGNATURE",
      multipart: false,
      option: option,
    });
    try {
      await client.getFileUploadInfoWithOptions("854xxxxx", getFileUploadInfoRequest, getFileUploadInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoHeaders getFileUploadInfoHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoHeaders();
            getFileUploadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption.GetFileUploadInfoRequestOptionPreCheckParam optionPreCheckParam = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption.GetFileUploadInfoRequestOptionPreCheckParam
            {
                Md5 = "md5",
                Size = 512,
                ParentId = "parent_id",
                Name = "dentry_name",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption
            {
                StorageDriver = "DINGTALK",
                PreCheckParam = optionPreCheckParam,
                PreferRegion = "ZHANGJIAKOU",
                PreferIntranet = true,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoRequest getFileUploadInfoRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetFileUploadInfoRequest
            {
                UnionId = "cHtUxxxxx",
                Protocol = "HEADER_SIGNATURE",
                Multipart = false,
                Option = option,
            };
            try
            {
                client.GetFileUploadInfoWithOptions("854xxxxx", getFileUploadInfoRequest, getFileUploadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "uploadKey" : "upload_key",
  "storageDriver" : "DINGTALK",
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

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.protocol | %s | 参数错误-protocol |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.storageDriver | %s | 参数错误-storageDriver |
| 400 | dentryUploadError | %s | 文件上传错误 |
| 400 | spaceQuotaInsufficient | %s | 空间容量不足 |
| 400 | sceneQuotaInsufficient | %s | 场景容量不足 |
| 400 | appQuotaInsufficient | %s | 应用容量不足 |
| 400 | orgQuotaInsufficient | %s | 企业容量不足 |
| 400 | dentryUploadForbidden | %s | 禁止上传 |
| 400 | dentryUploadProtocolNotSupport | %s | 不支持的上传协议 |
| 403 | permissionDenied | %s | 用户缺少上传文件的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
