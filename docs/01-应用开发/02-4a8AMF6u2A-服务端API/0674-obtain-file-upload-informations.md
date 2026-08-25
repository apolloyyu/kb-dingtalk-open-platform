---
title: "获取文件上传信息"
source_url: "https://open.dingtalk.com/document/development/obtain-file-upload-informations"
namespace: "development"
slug: "obtain-file-upload-informations"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 文件传输 > 获取文件上传信息"
doc_id: "oIb09idwKx"
updated_at: "2026-06-04 19:09:36"
---

> Source: https://open.dingtalk.com/document/development/obtain-file-upload-informations
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 文件传输 > 获取文件上传信息
> Updated: 2026-06-04 19:09:36

# 获取文件上传信息

调用本接口，获取文件上传信息。

## 接口调用说明

> **[!NOTE]**
>
> - 如果上传文件时提供的入参为spaceId字段，使用[获取文件上传信息](1600-obtain-storage-upload-information.md)接口。
> - 如果上传文件时提供的入参为dentryUuid或者uuid字段，推荐使用该文档。

接口的调用流程如下：

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

步骤三：调用[提交文件](0675-submittal-file.md)接口，完成文件上传。

> **[!NOTE]**
>
> - 存储空间类型为USER时，空间拥有权限的用户都有操作权限，其他员工调用[添加权限](0681-add-permissions-file.md)接口进行授权。
> - 存储空间类型为APP时，任何人操作都需要调用[添加权限](0681-add-permissions-file.md)接口进行授权。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/storage/spaces/files/{parentDentryUuid}/uploadInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.UploadInfo.Read-企业存储文件上传信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| parentDentryUuid | String | 是 | 父节点dentryUuid，可调用[搜索文件](0638-search-for-files.md)或[获取 dentryUuid 信息](0672-api-getuuidbydentryid.md)接口，获取返回参数`dentryUuid`字段。    如果是空间根目录, 填空间根目录的dentryUuid。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| protocol | String | 是 | 通过指定上传协议返回不同协议上传所需要的信息。   - **HEADER\_SIGNATURE**：Header加签 |
| option | Object | 否 | 可选参数 |
| storageDriver | String | 否 | 文件存储驱动类型。    当前只支持DINGTALK。 |
| preCheckParam | Object | 否 | 预检查的字段。可实现对文件名称，文件完整性，容量的校验 |
| size | Long | 否 | 文件大小, 做容量相关校验。不传则不做校验。 |
| name | String | 否 | 文件名称, 文件名称合法性和文件名称冲突校验。    规则：   - 头尾不能包含空格，否则会自动去除。 - 不能包含特殊字符，包括：制表符、\*、"、<、>、|。 - 不能以"."结尾。 |
| preferRegion | String | 否 | 优先地域：   - **ZHANGJIAKOU**：张家口 - **SHENZHEN**：深圳 - **SHANGHAI**：上海 - **SINGAPORE**：新加坡 - **UNKNOWN**：未知     倾向于将资源存到哪个地域，可实现就近上传等功能。 |
| preferIntranet | Boolean | 否 | 是否优先使用内网传输，使用该参数前提是配置了专属存储内网传输。   - **true**：是，默认值 - **false**：否 |

### 请求示例

HTTP

```
POST /v2.0/storage/spaces/files/uuid/uploadInfos/query?unionId=union_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "protocol" : "HEADER_SIGNATURE",
  "option" : {
    "storageDriver" : "DINGTALK",
    "preCheckParam" : {
      "size" : 512,
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
    public static com.aliyun.dingtalkstorage_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoHeaders getFileUploadInfoHeaders = new com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoHeaders();
        getFileUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOptionPreCheckParam optionPreCheckParam = new com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOptionPreCheckParam()
                .setSize(512L)
                .setName("dentry_name");
        com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption option = new com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption()
                .setStorageDriver("DINGTALK")
                .setPreCheckParam(optionPreCheckParam)
                .setPreferRegion("ZHANGJIAKOU")
                .setPreferIntranet(true);
        com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoRequest getFileUploadInfoRequest = new com.aliyun.dingtalkstorage_2_0.models.GetFileUploadInfoRequest()
                .setUnionId("union_id")
                .setProtocol("HEADER_SIGNATURE")
                .setOption(option);
        try {
            client.getFileUploadInfoWithOptions("uuid", getFileUploadInfoRequest, getFileUploadInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_file_upload_info_headers = dingtalkstorage__2__0_models.GetFileUploadInfoHeaders()
        get_file_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_pre_check_param = dingtalkstorage__2__0_models.GetFileUploadInfoRequestOptionPreCheckParam(
            size=512,
            name='dentry_name'
        )
        option = dingtalkstorage__2__0_models.GetFileUploadInfoRequestOption(
            storage_driver='DINGTALK',
            pre_check_param=option_pre_check_param,
            prefer_region='ZHANGJIAKOU',
            prefer_intranet=True
        )
        get_file_upload_info_request = dingtalkstorage__2__0_models.GetFileUploadInfoRequest(
            union_id='union_id',
            protocol='HEADER_SIGNATURE',
            option=option
        )
        try:
            client.get_file_upload_info_with_options('uuid', get_file_upload_info_request, get_file_upload_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_file_upload_info_headers = dingtalkstorage__2__0_models.GetFileUploadInfoHeaders()
        get_file_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_pre_check_param = dingtalkstorage__2__0_models.GetFileUploadInfoRequestOptionPreCheckParam(
            size=512,
            name='dentry_name'
        )
        option = dingtalkstorage__2__0_models.GetFileUploadInfoRequestOption(
            storage_driver='DINGTALK',
            pre_check_param=option_pre_check_param,
            prefer_region='ZHANGJIAKOU',
            prefer_intranet=True
        )
        get_file_upload_info_request = dingtalkstorage__2__0_models.GetFileUploadInfoRequest(
            union_id='union_id',
            protocol='HEADER_SIGNATURE',
            option=option
        )
        try:
            await client.get_file_upload_info_with_options_async('uuid', get_file_upload_info_request, get_file_upload_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\GetFileUploadInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\GetFileUploadInfoRequest\option\preCheckParam;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\GetFileUploadInfoRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_2_0\Models\GetFileUploadInfoRequest;
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
            "size" => 512,
            "name" => "dentry_name"
        ]);
        $option = new option([
            "storageDriver" => "DINGTALK",
            "preCheckParam" => $optionPreCheckParam,
            "preferRegion" => "ZHANGJIAKOU",
            "preferIntranet" => true
        ]);
        $getFileUploadInfoRequest = new GetFileUploadInfoRequest([
            "unionId" => "union_id",
            "protocol" => "HEADER_SIGNATURE",
            "option" => $option
        ]);
        try {
            $client->getFileUploadInfoWithOptions("uuid", $getFileUploadInfoRequest, $getFileUploadInfoHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_2_0  "github.com/alibabacloud-go/dingtalk/storage_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  getFileUploadInfoHeaders := &dingtalkstorage_2_0.GetFileUploadInfoHeaders{}
  getFileUploadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionPreCheckParam := &dingtalkstorage_2_0.GetFileUploadInfoRequestOptionPreCheckParam{
    Size: tea.Int64(512),
    Name: tea.String("dentry_name"),
  }
  option := &dingtalkstorage_2_0.GetFileUploadInfoRequestOption{
    StorageDriver: tea.String("DINGTALK"),
    PreCheckParam: optionPreCheckParam,
    PreferRegion: tea.String("ZHANGJIAKOU"),
    PreferIntranet: tea.Bool(true),
  }
  getFileUploadInfoRequest := &dingtalkstorage_2_0.GetFileUploadInfoRequest{
    UnionId: tea.String("union_id"),
    Protocol: tea.String("HEADER_SIGNATURE"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFileUploadInfoWithOptions(tea.String("uuid"), getFileUploadInfoRequest, getFileUploadInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkstorage_2_0, * as $dingtalkstorage_2_0 from '@alicloud/dingtalk/storage_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkstorage_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkstorage_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFileUploadInfoHeaders = new $dingtalkstorage_2_0.GetFileUploadInfoHeaders({ });
    getFileUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let optionPreCheckParam = new $dingtalkstorage_2_0.GetFileUploadInfoRequestOptionPreCheckParam({
      size: 512,
      name: "dentry_name",
    });
    let option = new $dingtalkstorage_2_0.GetFileUploadInfoRequestOption({
      storageDriver: "DINGTALK",
      preCheckParam: optionPreCheckParam,
      preferRegion: "ZHANGJIAKOU",
      preferIntranet: true,
    });
    let getFileUploadInfoRequest = new $dingtalkstorage_2_0.GetFileUploadInfoRequest({
      unionId: "union_id",
      protocol: "HEADER_SIGNATURE",
      option: option,
    });
    try {
      await client.getFileUploadInfoWithOptions("uuid", getFileUploadInfoRequest, getFileUploadInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoHeaders getFileUploadInfoHeaders = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoHeaders();
            getFileUploadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption.GetFileUploadInfoRequestOptionPreCheckParam optionPreCheckParam = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption.GetFileUploadInfoRequestOptionPreCheckParam
            {
                Size = 512,
                Name = "dentry_name",
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoRequest.GetFileUploadInfoRequestOption
            {
                StorageDriver = "DINGTALK",
                PreCheckParam = optionPreCheckParam,
                PreferRegion = "ZHANGJIAKOU",
                PreferIntranet = true,
            };
            AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoRequest getFileUploadInfoRequest = new AlibabaCloud.SDK.Dingtalkstorage_2_0.Models.GetFileUploadInfoRequest
            {
                UnionId = "union_id",
                Protocol = "HEADER_SIGNATURE",
                Option = option,
            };
            try
            {
                client.GetFileUploadInfoWithOptions("uuid", getFileUploadInfoRequest, getFileUploadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| uploadKey | String | 上传唯一标识 |
| storageDriver | String | 文件存储类型。 |
| protocol | String | 上传协议：   - **HEADER\_SIGNATURE**：Header加签 |
| headerSignatureInfo | Object | Header加签上传信息。    当protocol参数传HEADER\_SIGNATURE时，返回该字段。 |
| resourceUrls | Array of String | 传输地址。 |
| headers | Map<String, String> | 请求头，最大size：20。 |
| expirationSeconds | Integer | 过期时间，单位秒 |
| region | String | 地域，枚举值：   - **ZHANGJIAKOU**：张家口 - **SHENZHEN**：深圳 - **SHANGHAI**：上海 - **SINGAPORE**：新加坡 - **UNKNOWN**：未知 |
| internalResourceUrls | Array of String | 内网地址。    该字段目前无使用场景，请忽略。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "uploadKey" : "upload_key",
  "storageDriver" : "DINGTALK",
  "protocol" : "HEADER_SIGNATURE",
  "headerSignatureInfo" : {
    "resourceUrls" : [ "resourceUrl" ],
    "headers" : {
      "key" : "header_value"
    },
    "expirationSeconds" : 900,
    "region" : "ZHANGJIAKOU",
    "internalResourceUrls" : [ "internalResourceUrl" ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.protocol | %s | 参数错误-protocol |
| 400 | paramError.parentDentryUuid | %s | 参数错误-parentDentryUuid |
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
