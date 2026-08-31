---
title: "提交文件"
source_url: "https://open.dingtalk.com/document/development/submit-documents"
namespace: "development"
slug: "submit-documents"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 存储管理 > 文件传输 > 提交文件"
doc_id: "zuIUrvCZcM"
updated_at: "2026-08-25 09:39:00"
---

> Source: https://open.dingtalk.com/document/development/submit-documents
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 存储管理 > 文件传输 > 提交文件
> Updated: 2026-08-25 09:39:00

# 提交文件

调用本接口，提交文件完成文件上传。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[提交文件](0675-submittal-file.md)接口，已接入用户不受影响。

### 接口调用步骤

步骤一：调用[获取文件上传信息](1602-obtain-storage-upload-information.md)接口，获取上传文件需要的信息。

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
> - 存储空间类型为USER时，只有空间拥有者和管理者有操作权限，其他员工均需要授权。
> - 存储空间类型为APP时，任何人操作都需要先进行授权。.
>
> 可调用[添加权限](1598-add-storage-permissions.md)接口进行授权。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/storage/spaces/{spaceId}/files/commit?unionId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "uploadKey" : "String",
  "name" : "String",
  "parentId" : "String",
  "option" : {
    "size" : Long,
    "conflictStrategy" : "String",
    "appProperties" : [ {
      "name" : "String",
      "value" : "String",
      "visibility" : "String"
    } ]
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
| uploadKey | String | 是 | 添加文件唯一标识，调用[获取文件上传信息](1602-obtain-storage-upload-information.md)接口获取uploadKey参数值。 |
| name | String | 是 | 文件的名称，带后缀。命名有以下要求：   - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、| - 不能以"."结尾 |
| parentId | String | 是 | 父目录Id。根目录时，该参数是0，可调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取parentId参数值。 |
| option | Object | 否 | 可选参数。 |
| size | Long | 否 | 文件大小，单位Byte。 |
| conflictStrategy | String | 否 | 文件名称冲突策略。   - **AUTO\_RENAME**：自动重命名，默认值 - **OVERWRITE**：覆盖 - **RETURN\_DENTRY\_IF\_EXISTS**：返回已存在文件 - **RETURN\_ERROR\_IF\_EXISTS**：文件已存在时报错 |
| appProperties | Array | 否 | 当前文件的应用属性列表，最大值3。 |
| name | String | 是 | 属性名。 |
| value | String | 是 | 属性值。 |
| visibility | String | 是 | 属性可见性。   - PUBLIC：所有应用都可见 - PRIVATE：仅限当前应用可见 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| dentry | Object | 文件信息。 |
| id | String | 文件Id。 |
| spaceId | String | 所在空间Id。 |
| parentId | String | 父目录Id。根目录时，该参数是0。 |
| type | String | 类型，本接口返回类型只有FILE。   - **FILE**：文件 |
| name | String | 文件名称。 |
| size | Long | 文件大小，单位Byte。 |
| path | String | 文件在空间内的路径。 |
| version | Long | 版本。 |
| status | String | 状态。   - **NORMAL**：正常 - **DELETED**：已删除 - **EXPIRED**：已过期 |
| extension | String | 文件后缀。 |
| creatorId | String | 创建者unionId。 |
| modifierId | String | 修改者unionId。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| properties | Object | 文件属性。 |
| readOnly | Boolean | 文件是否只读。   - **true**：是 - **false**：否 |
| appProperties | Map<String, Array> | 在特定应用上的属性。key是所属空间的ownerId，value是属性列表。 |
|  | Array | 属性列表。 |
| name | String | 属性名。 |
| value | String | 属性值。 |
| visibility | String | 属性可见性。   - PUBLIC：所有应用都可见 - PRIVATE：仅限当前应用可见 |
| uuid | String | 唯一标识。 |
| partitionType | String | 存储分区。   - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属MiniOSS存储分区 |
| storageDriver | String | 驱动类型。   - **DINGTALK**：钉钉统一存储驱动 - **ALIDOC**：钉钉文档存储驱动 - **UNKNOWN**：未知驱动 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/storage/spaces/space_id/files/commit?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "uploadKey" : "upload_key",
  "name" : "测试文件.xls",
  "parentId" : "0",
  "option" : {
    "size" : 1024,
    "conflictStrategy" : "AUTO_RENAME",
    "appProperties" : [ {
      "name" : "属性1",
      "value" : "属性值1",
      "visibility" : "PUBLIC"
    } ]
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
        com.aliyun.dingtalkstorage_1_0.models.CommitFileHeaders commitFileHeaders = new com.aliyun.dingtalkstorage_1_0.models.CommitFileHeaders();
        commitFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.CommitFileRequest.CommitFileRequestOptionAppProperties optionAppProperties0 = new com.aliyun.dingtalkstorage_1_0.models.CommitFileRequest.CommitFileRequestOptionAppProperties()
                .setName("属性1")
                .setValue("属性值1")
                .setVisibility("PUBLIC");
        com.aliyun.dingtalkstorage_1_0.models.CommitFileRequest.CommitFileRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.CommitFileRequest.CommitFileRequestOption()
                .setSize(1024L)
                .setConflictStrategy("AUTO_RENAME")
                .setAppProperties(java.util.Arrays.asList(
                    optionAppProperties0
                ));
        com.aliyun.dingtalkstorage_1_0.models.CommitFileRequest commitFileRequest = new com.aliyun.dingtalkstorage_1_0.models.CommitFileRequest()
                .setUnionId("chyxxxxx")
                .setUploadKey("upload_key")
                .setName("测试文件.xls")
                .setParentId("0")
                .setOption(option);
        try {
            client.commitFileWithOptions("space_id", commitFileRequest, commitFileHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        commit_file_headers = dingtalkstorage__1__0_models.CommitFileHeaders()
        commit_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_app_properties_0 = dingtalkstorage__1__0_models.CommitFileRequestOptionAppProperties(
            name='属性1',
            value='属性值1',
            visibility='PUBLIC'
        )
        option = dingtalkstorage__1__0_models.CommitFileRequestOption(
            size=1024,
            conflict_strategy='AUTO_RENAME',
            app_properties=[
                option_app_properties_0
            ]
        )
        commit_file_request = dingtalkstorage__1__0_models.CommitFileRequest(
            union_id='chyxxxxx',
            upload_key='upload_key',
            name='测试文件.xls',
            parent_id='0',
            option=option
        )
        try:
            client.commit_file_with_options('space_id', commit_file_request, commit_file_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        commit_file_headers = dingtalkstorage__1__0_models.CommitFileHeaders()
        commit_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_app_properties_0 = dingtalkstorage__1__0_models.CommitFileRequestOptionAppProperties(
            name='属性1',
            value='属性值1',
            visibility='PUBLIC'
        )
        option = dingtalkstorage__1__0_models.CommitFileRequestOption(
            size=1024,
            conflict_strategy='AUTO_RENAME',
            app_properties=[
                option_app_properties_0
            ]
        )
        commit_file_request = dingtalkstorage__1__0_models.CommitFileRequest(
            union_id='chyxxxxx',
            upload_key='upload_key',
            name='测试文件.xls',
            parent_id='0',
            option=option
        )
        try:
            await client.commit_file_with_options_async('space_id', commit_file_request, commit_file_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CommitFileHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CommitFileRequest\option\appProperties;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CommitFileRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\CommitFileRequest;
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
            "name" => "属性1",
            "value" => "属性值1",
            "visibility" => "PUBLIC"
        ]);
        $option = new option([
            "size" => 1024,
            "conflictStrategy" => "AUTO_RENAME",
            "appProperties" => [
                $optionAppProperties0
            ]
        ]);
        $commitFileRequest = new CommitFileRequest([
            "unionId" => "chyxxxxx",
            "uploadKey" => "upload_key",
            "name" => "测试文件.xls",
            "parentId" => "0",
            "option" => $option
        ]);
        try {
            $client->commitFileWithOptions("space_id", $commitFileRequest, $commitFileHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  commitFileHeaders := &dingtalkstorage_1_0.CommitFileHeaders{}
  commitFileHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionAppProperties0 := &dingtalkstorage_1_0.CommitFileRequestOptionAppProperties{
    Name: tea.String("属性1"),
    Value: tea.String("属性值1"),
    Visibility: tea.String("PUBLIC"),
  }
  option := &dingtalkstorage_1_0.CommitFileRequestOption{
    Size: tea.Int64(1024),
    ConflictStrategy: tea.String("AUTO_RENAME"),
    AppProperties: []*dingtalkstorage_1_0.CommitFileRequestOptionAppProperties{optionAppProperties0},
  }
  commitFileRequest := &dingtalkstorage_1_0.CommitFileRequest{
    UnionId: tea.String("chyxxxxx"),
    UploadKey: tea.String("upload_key"),
    Name: tea.String("测试文件.xls"),
    ParentId: tea.String("0"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CommitFileWithOptions(tea.String("space_id"), commitFileRequest, commitFileHeaders, &util.RuntimeOptions{})
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
    let commitFileHeaders = new $dingtalkstorage_1_0.CommitFileHeaders({ });
    commitFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let optionAppProperties0 = new $dingtalkstorage_1_0.CommitFileRequestOptionAppProperties({
      name: "属性1",
      value: "属性值1",
      visibility: "PUBLIC",
    });
    let option = new $dingtalkstorage_1_0.CommitFileRequestOption({
      size: 1024,
      conflictStrategy: "AUTO_RENAME",
      appProperties: [
        optionAppProperties0
      ],
    });
    let commitFileRequest = new $dingtalkstorage_1_0.CommitFileRequest({
      unionId: "chyxxxxx",
      uploadKey: "upload_key",
      name: "测试文件.xls",
      parentId: "0",
      option: option,
    });
    try {
      await client.commitFileWithOptions("space_id", commitFileRequest, commitFileHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileHeaders commitFileHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileHeaders();
            commitFileHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest.CommitFileRequestOption.CommitFileRequestOptionAppProperties optionAppProperties0 = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest.CommitFileRequestOption.CommitFileRequestOptionAppProperties
            {
                Name = "属性1",
                Value = "属性值1",
                Visibility = "PUBLIC",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest.CommitFileRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest.CommitFileRequestOption
            {
                Size = 1024,
                ConflictStrategy = "AUTO_RENAME",
                AppProperties = new List<AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest.CommitFileRequestOption.CommitFileRequestOptionAppProperties>
                {
                    optionAppProperties0
                },
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest commitFileRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.CommitFileRequest
            {
                UnionId = "chyxxxxx",
                UploadKey = "upload_key",
                Name = "测试文件.xls",
                ParentId = "0",
                Option = option,
            };
            try
            {
                client.CommitFileWithOptions("space_id", commitFileRequest, commitFileHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "dentry" : {
    "id" : "123",
    "spaceId" : "854xxxxx",
    "parentId" : "0",
    "type" : "FILE",
    "name" : "测试文件",
    "size" : 512,
    "path" : "/测试文件夹/测试文件",
    "version" : 1,
    "status" : "NORMAL",
    "extension" : "xsl",
    "creatorId" : "cHtUxxxxx",
    "modifierId" : "cHtUxxxxx",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "properties" : {
      "readOnly" : true
    },
    "appProperties" : [ {
      "name" : "属性1",
      "value" : "属性值1",
      "visibility" : "PRIVATE"
    } ],
    "uuid" : "uuid",
    "partitionType" : "PUBLIC_OSS_PARTITION",
    "storageDriver" : "DINGTALK"
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.conflictStrategy | %s | 参数错误-conflictStrategy |
| 400 | spaceQuotaInsufficient | %s | 空间容量不足 |
| 400 | sceneQuotaInsufficient | %s | 场景容量不足 |
| 400 | appQuotaInsufficient | %s | 应用容量不足 |
| 400 | orgQuotaInsufficient | %s | 企业容量不足 |
| 400 | dentryNameIllegal | %s | 文件名非法 |
| 400 | dentryStoreError | %s | 文件存储异常 |
| 403 | permissionDenied | %s | 用户缺少上传文件的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
