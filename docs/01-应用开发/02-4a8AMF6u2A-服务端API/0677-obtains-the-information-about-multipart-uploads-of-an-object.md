---
title: "获取文件分片上传信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-information-about-multipart-uploads-of-an-object"
namespace: "development"
slug: "obtains-the-information-about-multipart-uploads-of-an-object"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 文件传输 > 分片上传 > 获取文件分片上传信息"
doc_id: "lNVR98XyS3"
updated_at: "2026-06-04 19:09:38"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-information-about-multipart-uploads-of-an-object
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 文件传输 > 分片上传 > 获取文件分片上传信息
> Updated: 2026-06-04 19:09:38

# 获取文件分片上传信息

调用本接口，获取文件分片后每片文件的上传信息。

## **接口调用说明**

接口调用步骤如下：

步骤一：调用[初始化文件分片上传](0676-initialize-a-multipart-upload-object.md)接口，获取上传标识uploadKey。

步骤二：调用本接口获取每片文件的上传信息。

步骤三：循环对每片文件执行上传。

步骤四：使用步骤一接口获取的上传标识uploadKey，调用[提交文件](0675-submittal-file.md)接口，完成上传。

完整示例请参考：

```
import com.aliyun.dingtalkstorage_1_0.models.*;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.teautil.models.RuntimeOptions;
import com.util.AccessTokenUtil;
import org.junit.Test;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.Map;

public class MultipartUpload {
  public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
    Config config = new Config();
    config.protocol = "https";
    config.regionId = "central";
    return new com.aliyun.dingtalkstorage_1_0.Client(config);
  }
  @Test
  public void test() throws Exception {
    com.aliyun.dingtalkstorage_1_0.Client client = MultipartUpload.createClient();

    String spaceId = "存储空间ID";
    String filePath = "/Users/xxxxx/Desktop/音乐.mp3";
    // 每片文件大小
    long partSize = 1 * 1024 * 1024L;  // 1MB
    // 初始化分片上传接口
    InitMultipartFileUploadHeaders initMultipartFileUploadHeaders = new InitMultipartFileUploadHeaders();
    initMultipartFileUploadHeaders.xAcsDingtalkAccessToken = "accessToken";
    InitMultipartFileUploadRequest initMultipartFileUploadRequest = new InitMultipartFileUploadRequest();
    initMultipartFileUploadRequest.setUnionId(unionId);
    InitMultipartFileUploadRequest.InitMultipartFileUploadRequestOption initMultipartFileUploadRequestOption = new InitMultipartFileUploadRequest.InitMultipartFileUploadRequestOption();
    initMultipartFileUploadRequestOption.setStorageDriver("DINGTALK");
    initMultipartFileUploadRequest.setOption(initMultipartFileUploadRequestOption);
    String uploadKey = client.initMultipartFileUploadWithOptions(spaceId, initMultipartFileUploadRequest, initMultipartFileUploadHeaders, new RuntimeOptions()).getBody().getUploadKey();

    File file = new File(filePath);
    long fileLength = file.length();
    int partCount = (int) (fileLength / partSize) + ((fileLength % partSize != 0) ? 1 : 0);

    for (int i = 0; i < partCount; i++) {
      long startPos = i * partSize;
      long curPartSize = (i + 1 == partCount) ? (fileLength - startPos) : partSize;
      // 获取分片上传信息
      GetMultipartFileUploadInfosHeaders getMultipartFileUploadInfosHeaders = new GetMultipartFileUploadInfosHeaders();
      getMultipartFileUploadInfosHeaders.xAcsDingtalkAccessToken = "accessToken";
      GetMultipartFileUploadInfosRequest getMultipartFileUploadInfosRequest = new GetMultipartFileUploadInfosRequest();
      getMultipartFileUploadInfosRequest.setUnionId(unionId);
      getMultipartFileUploadInfosRequest.setUploadKey("第一步初始化分片上传接口获取的uploadKey");
      getMultipartFileUploadInfosRequest.setPartNumbers(Arrays.asList(i + 1));
      GetMultipartFileUploadInfosResponseBody.GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfosHeaderSignatureInfo headerSignatureInfo = client.getMultipartFileUploadInfosWithOptions(getMultipartFileUploadInfosRequest, getMultipartFileUploadInfosHeaders, new RuntimeOptions()).body.multipartHeaderSignatureInfos.get(0).headerSignatureInfo;
            uploadPartFile(startPos, curPartSize, headerSignatureInfo, file);
        }
            // 提交文件，完成上传
            CommitFileHeaders commitFileHeaders = new CommitFileHeaders();
            commitFileHeaders.xAcsDingtalkAccessToken = "accessToken";
            CommitFileRequest.CommitFileRequestOption commitFileRequestOption
                = new CommitFileRequest.CommitFileRequestOption()
                .setSize(1024L)
                .setConflictStrategy("OVERWRITE");
            CommitFileRequest commitFileRequest = new CommitFileRequest()
                .setUnionId(unionId)
                .setUploadKey(“第一步初始化分片上传接口获取的uploadKey”)
                .setName("音乐.mp3")
                .setParentId("0")
                .setOption(commitFileRequestOption);
            CommitFileResponseBody.CommitFileResponseBodyDentry dentry = client.commitFileWithOptions("存储空间ID", commitFileRequest, commitFileHeaders, new RuntimeOptions()).body.dentry;
            System.out.println(dentry);
    }

    private void uploadPartFile(long start, long size, GetMultipartFileUploadInfosResponseBody.GetMultipartFileUploadInfosResponseBodyMultipartHeaderSignatureInfosHeaderSignatureInfo headerSignatureInfo, File file) throws Exception {
        InputStream inputStream = new FileInputStream(file);
        if (start > 0) {
            inputStream.skip(start);
        }

        URL url = new URL(headerSignatureInfo.getResourceUrls().get(0));
        HttpURLConnection connection = (HttpURLConnection)url.openConnection();
        connection.setDoOutput(true);
        connection.setRequestMethod("PUT");
        connection.setUseCaches(false);
        if (headerSignatureInfo.getHeaders() != null) {
            for (Map.Entry<String, String> entry : headerSignatureInfo.getHeaders().entrySet()) {
                connection.setRequestProperty(entry.getKey(), entry.getValue());
            }
        }
        connection.setReadTimeout(10000);
        connection.setConnectTimeout(10000);
        connection.connect();
        OutputStream out = connection.getOutputStream();
        byte[] buffer = new byte[1024];
        long remain = size;
        for (;remain > 0;) {
            int sizeToRead = remain < buffer.length ? (int)remain : buffer.length;
            int rsz = inputStream.read(buffer, 0, sizeToRead);
            if (rsz < 0) {
                break;
            }
            out.write(buffer, 0, rsz);
            remain -= rsz;
        }
        out.flush();
        out.close();
        int responseCode = connection.getResponseCode();
        if (responseCode == 200) {
            System.out.println("上传成功");
        } else {
            System.out.println("上传失败");
        }
        connection.disconnect();
    }
}
```

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/files/multiPartUploadInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.UploadInfo.Read-企业存储文件上传信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| uploadKey | String | 是 | 上传唯一标识，调用[初始化文件分片上传](0676-initialize-a-multipart-upload-object.md)接口，获取上传标识uploadKey。 |
| partNumbers | Array of Integer | 是 | 每片文件的Id，文件的分片数量最大值10000，每片文件大小限制范围是100KB~5GB，最多传30。    每片文件的Id，由开发者指定，本接口会返回每片文件的上传地址和headers等信息。  示例：[1,2,3,4,5] |
| option | Object | 否 | 可选参数。 |
| preferIntranet | Boolean | 否 | 是否优先使用内网传输，使用该参数前提是配置了专属存储内网传输。   - true：是，默认值 - false：否 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/files/multiPartUploadInfos/query?unionId=chyxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "uploadKey" : "hwHPAAAAAipHxxxxx",
  "partNumbers" : [ 1 ],
  "option" : {
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
        com.aliyun.dingtalkstorage_1_0.models.GetMultipartFileUploadInfosHeaders getMultipartFileUploadInfosHeaders = new com.aliyun.dingtalkstorage_1_0.models.GetMultipartFileUploadInfosHeaders();
        getMultipartFileUploadInfosHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.GetMultipartFileUploadInfosRequest.GetMultipartFileUploadInfosRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.GetMultipartFileUploadInfosRequest.GetMultipartFileUploadInfosRequestOption()
                .setPreferIntranet(true);
        com.aliyun.dingtalkstorage_1_0.models.GetMultipartFileUploadInfosRequest getMultipartFileUploadInfosRequest = new com.aliyun.dingtalkstorage_1_0.models.GetMultipartFileUploadInfosRequest()
                .setUnionId("chyxxxxx")
                .setUploadKey("hwHPAAAAAipHxxxxx")
                .setPartNumbers(java.util.Arrays.asList(
                    1
                ))
                .setOption(option);
        try {
            client.getMultipartFileUploadInfosWithOptions(getMultipartFileUploadInfosRequest, getMultipartFileUploadInfosHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_multipart_file_upload_infos_headers = dingtalkstorage__1__0_models.GetMultipartFileUploadInfosHeaders()
        get_multipart_file_upload_infos_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.GetMultipartFileUploadInfosRequestOption(
            prefer_intranet=True
        )
        get_multipart_file_upload_infos_request = dingtalkstorage__1__0_models.GetMultipartFileUploadInfosRequest(
            union_id='chyxxxxx',
            upload_key='hwHPAAAAAipHxxxxx',
            part_numbers=[
                1
            ],
            option=option
        )
        try:
            client.get_multipart_file_upload_infos_with_options(get_multipart_file_upload_infos_request, get_multipart_file_upload_infos_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_multipart_file_upload_infos_headers = dingtalkstorage__1__0_models.GetMultipartFileUploadInfosHeaders()
        get_multipart_file_upload_infos_headers.x_acs_dingtalk_access_token = '<your access token>'
        option = dingtalkstorage__1__0_models.GetMultipartFileUploadInfosRequestOption(
            prefer_intranet=True
        )
        get_multipart_file_upload_infos_request = dingtalkstorage__1__0_models.GetMultipartFileUploadInfosRequest(
            union_id='chyxxxxx',
            upload_key='hwHPAAAAAipHxxxxx',
            part_numbers=[
                1
            ],
            option=option
        )
        try:
            await client.get_multipart_file_upload_infos_with_options_async(get_multipart_file_upload_infos_request, get_multipart_file_upload_infos_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetMultipartFileUploadInfosHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetMultipartFileUploadInfosRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetMultipartFileUploadInfosRequest;
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
        $getMultipartFileUploadInfosHeaders = new GetMultipartFileUploadInfosHeaders([]);
        $getMultipartFileUploadInfosHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $option = new option([
            "preferIntranet" => true
        ]);
        $getMultipartFileUploadInfosRequest = new GetMultipartFileUploadInfosRequest([
            "unionId" => "chyxxxxx",
            "uploadKey" => "hwHPAAAAAipHxxxxx",
            "partNumbers" => [
                1
            ],
            "option" => $option
        ]);
        try {
            $client->getMultipartFileUploadInfosWithOptions($getMultipartFileUploadInfosRequest, $getMultipartFileUploadInfosHeaders, new RuntimeOptions([]));
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

  getMultipartFileUploadInfosHeaders := &dingtalkstorage_1_0.GetMultipartFileUploadInfosHeaders{}
  getMultipartFileUploadInfosHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  option := &dingtalkstorage_1_0.GetMultipartFileUploadInfosRequestOption{
    PreferIntranet: tea.Bool(true),
  }
  getMultipartFileUploadInfosRequest := &dingtalkstorage_1_0.GetMultipartFileUploadInfosRequest{
    UnionId: tea.String("chyxxxxx"),
    UploadKey: tea.String("hwHPAAAAAipHxxxxx"),
    PartNumbers: []*int32{tea.Int(1)},
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetMultipartFileUploadInfosWithOptions(getMultipartFileUploadInfosRequest, getMultipartFileUploadInfosHeaders, &util.RuntimeOptions{})
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
    let getMultipartFileUploadInfosHeaders = new $dingtalkstorage_1_0.GetMultipartFileUploadInfosHeaders({ });
    getMultipartFileUploadInfosHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let option = new $dingtalkstorage_1_0.GetMultipartFileUploadInfosRequestOption({
      preferIntranet: true,
    });
    let getMultipartFileUploadInfosRequest = new $dingtalkstorage_1_0.GetMultipartFileUploadInfosRequest({
      unionId: "chyxxxxx",
      uploadKey: "hwHPAAAAAipHxxxxx",
      partNumbers: [
        1
      ],
      option: option,
    });
    try {
      await client.getMultipartFileUploadInfosWithOptions(getMultipartFileUploadInfosRequest, getMultipartFileUploadInfosHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetMultipartFileUploadInfosHeaders getMultipartFileUploadInfosHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetMultipartFileUploadInfosHeaders();
            getMultipartFileUploadInfosHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetMultipartFileUploadInfosRequest.GetMultipartFileUploadInfosRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetMultipartFileUploadInfosRequest.GetMultipartFileUploadInfosRequestOption
            {
                PreferIntranet = true,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetMultipartFileUploadInfosRequest getMultipartFileUploadInfosRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetMultipartFileUploadInfosRequest
            {
                UnionId = "chyxxxxx",
                UploadKey = "hwHPAAAAAipHxxxxx",
                PartNumbers = new List<int?>
                {
                    1
                },
                Option = option,
            };
            try
            {
                client.GetMultipartFileUploadInfosWithOptions(getMultipartFileUploadInfosRequest, getMultipartFileUploadInfosHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| multipartHeaderSignatureInfos | Array | 分片Header加签上传信息列表。 |
| partNumber | Integer | 分片Id。 |
| headerSignatureInfo | Object | header信息。 |
| resourceUrls | Array of String | 多个上传URL，最大值10，前面的url优先。 |
| headers | Map<String, String> | 请求头。 |
| expirationSeconds | Integer | 过期时间，单位秒。 |
| region | String | 地域。   - **ZHANGJIAKOU**：张家口 - **SHENZHEN**：深圳 - **SHANGHAI**：上海 - **SINGAPORE**：新加坡 - **UNKNOWN**：未知 |
| internalResourceUrls | Array of String | 内网URL列表。    该字段目前无使用场景，请忽略。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "multipartHeaderSignatureInfos" : [ {
    "partNumber" : 1,
    "headerSignatureInfo" : {
      "resourceUrls" : [ "https://zjk.trans.dingtalkxxxxx" ],
      "headers" : {
        "key" : "header_value"
      },
      "expirationSeconds" : 900,
      "region" : "ZHANGJIAKOU",
      "internalResourceUrls" : [ "lippi-space-zjk.oss-cnxxxxx" ]
    }
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.uploadKey | %s | 参数错误-uploadKey |
| 400 | paramError.partNumbers | %s | 参数错误-partNumbers |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
