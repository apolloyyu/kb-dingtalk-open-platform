---
title: "文件下载流程"
source_url: "https://open.dingtalk.com/document/development/file-download-process"
namespace: "development"
slug: "file-download-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件传输 > 文件下载流程"
doc_id: "BXtJNXN0sX"
updated_at: "2026-08-25 13:50:02"
---

> Source: https://open.dingtalk.com/document/development/file-download-process
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件传输 > 文件下载流程
> Updated: 2026-08-25 13:50:02

# 文件下载流程

本文介绍如何下载钉盘文件。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件下载信息](0678-obtains-the-download-information-about-a-file.md)接口，已接入用户不受影响。

## 操作步骤

1. 调用[获取文件下载信息](1569-obtain-download-file-info.md)接口，获取文件下载所需的加签URL信息。

   示例代码如下：

   > **[!NOTE]**
   >
   > 以下示例代码仅供参考。

   Java

   ```
   // This file is auto-generated, don't edit it. Thanks.
   package com.aliyun.sample;

   import com.aliyun.tea.*;
   import com.aliyun.teautil.*;
   import com.aliyun.teautil.models.*;
   import com.aliyun.dingtalkdrive_1_0.*;
   import com.aliyun.dingtalkdrive_1_0.models.*;
   import com.aliyun.teaopenapi.*;
   import com.aliyun.teaopenapi.models.*;

   public class Sample {

     /**
        * 使用 Token 初始化账号Client
        * @return Client
        * @throws Exception
        */
     public static com.aliyun.dingtalkdrive_1_0.Client createClient() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";
       return new com.aliyun.dingtalkdrive_1_0.Client(config);
     }

     public static void main(String[] args_) throws Exception {
       java.util.List<String> args = java.util.Arrays.asList(args_);
       com.aliyun.dingtalkdrive_1_0.Client client = Sample.createClient();
       GetDownloadInfoHeaders getDownloadInfoHeaders = new GetDownloadInfoHeaders();
       getDownloadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
       GetDownloadInfoRequest getDownloadInfoRequest = new GetDownloadInfoRequest()
         .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx");
       try {
         client.getDownloadInfoWithOptions("<spaceId>", "<fileId>", getDownloadInfoRequest, getDownloadInfoHeaders, new RuntimeOptions());
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

   from alibabacloud_dingtalk.drive_1_0.client import Client as dingtalkdrive_1_0Client
   from alibabacloud_tea_openapi import models as open_api_models
   from alibabacloud_dingtalk.drive_1_0 import models as dingtalkdrive__1__0_models
   from alibabacloud_tea_util import models as util_models
   from alibabacloud_tea_util.client import Client as UtilClient

   class Sample:
       def __init__(self):
           pass

       @staticmethod
       def create_client() -> dingtalkdrive_1_0Client:
           """
           使用 Token 初始化账号Client
           @return: Client
           @throws Exception
           """
           config = open_api_models.Config()
           config.protocol = 'https'
           config.region_id = 'central'
           return dingtalkdrive_1_0Client(config)

       @staticmethod
       def main(
           args: List[str],
       ) -> None:
           client = Sample.create_client()
           get_download_info_headers = dingtalkdrive__1__0_models.GetDownloadInfoHeaders()
           get_download_info_headers.x_acs_dingtalk_access_token = '<your access token>'
           get_download_info_request = dingtalkdrive__1__0_models.GetDownloadInfoRequest(
               union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
           )
           try:
               client.get_download_info_with_options('<spaceId>', '<fileId>', get_download_info_request, get_download_info_headers, util_models.RuntimeOptions())
           except Exception as err:
               if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                   # err 中含有 code 和 message 属性，可帮助开发定位问题
                   pass

       @staticmethod
       async def main_async(
           args: List[str],
       ) -> None:
           client = Sample.create_client()
           get_download_info_headers = dingtalkdrive__1__0_models.GetDownloadInfoHeaders()
           get_download_info_headers.x_acs_dingtalk_access_token = '<your access token>'
           get_download_info_request = dingtalkdrive__1__0_models.GetDownloadInfoRequest(
               union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
           )
           try:
               await client.get_download_info_with_options_async('<spaceId>', '<fileId>', get_download_info_request, get_download_info_headers, util_models.RuntimeOptions())
           except Exception as err:
               if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                   # err 中含有 code 和 message 属性，可帮助开发定位问题
                   pass

   if __name__ == '__main__':
       Sample.main(sys.argv[1:])
   ```

   Go

   ```
   // This file is auto-generated, don't edit it. Thanks.
   package main

   import (
     "os"
     util  "github.com/alibabacloud-go/tea-utils/service"
     dingtalkdrive_1_0  "github.com/alibabacloud-go/dingtalk/drive_1_0/client"
     openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
     "github.com/alibabacloud-go/tea/tea"
   )

   /**
    * 使用 Token 初始化账号Client
    * @return Client
    * @throws Exception
    */
   func CreateClient () (_result *dingtalkdrive_1_0.Client, _err error) {
     config := &openapi.Config{}
     config.Protocol = tea.String("https")
     config.RegionId = tea.String("central")
     _result = &dingtalkdrive_1_0.Client{}
     _result, _err = dingtalkdrive_1_0.NewClient(config)
     return _result, _err
   }

   func _main (args []*string) (_err error) {
     client, _err := CreateClient()
     if _err != nil {
       return _err
     }

     getDownloadInfoHeaders := &dingtalkdrive_1_0.GetDownloadInfoHeaders{}
     getDownloadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
     getDownloadInfoRequest := &dingtalkdrive_1_0.GetDownloadInfoRequest{
       UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
     }
     tryErr := func()(_e error) {
       defer func() {
         if r := tea.Recover(recover()); r != nil {
           _e = r
         }
       }()
       _, _err = client.GetDownloadInfoWithOptions(tea.String("<spaceId>"), tea.String("<fileId>"), getDownloadInfoRequest, getDownloadInfoHeaders, &util.RuntimeOptions{})
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

   PHP

   ```
   <?php

   // This file is auto-generated, don't edit it. Thanks.
   namespace AlibabaCloud\SDK\Sample;

   use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Dingtalk;
   use \Exception;
   use AlibabaCloud\Tea\Exception\TeaError;
   use AlibabaCloud\Tea\Utils\Utils;

   use Darabonba\OpenApi\Models\Config;
   use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\GetDownloadInfoHeaders;
   use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\GetDownloadInfoRequest;
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
           $getDownloadInfoHeaders = new GetDownloadInfoHeaders([]);
           $getDownloadInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
           $getDownloadInfoRequest = new GetDownloadInfoRequest([
               "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
           ]);
           try {
               $client->getDownloadInfoWithOptions("<spaceId>", "<fileId>", $getDownloadInfoRequest, $getDownloadInfoHeaders, new RuntimeOptions([]));
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
           public static AlibabaCloud.SDK.Dingtalkdrive_1_0.Client CreateClient()
           {
               AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
               config.Protocol = "https";
               config.RegionId = "central";
               return new AlibabaCloud.SDK.Dingtalkdrive_1_0.Client(config);
           }

           public static void Main(string[] args)
           {
               AlibabaCloud.SDK.Dingtalkdrive_1_0.Client client = CreateClient();
               AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetDownloadInfoHeaders getDownloadInfoHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetDownloadInfoHeaders();
               getDownloadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
               AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetDownloadInfoRequest getDownloadInfoRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetDownloadInfoRequest
               {
                   UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
               };
               try
               {
                   client.GetDownloadInfoWithOptions("<spaceId>", "<fileId>", getDownloadInfoRequest, getDownloadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

   JavaScript

   ```
   // This file is auto-generated, don't edit it
   import Util, * as $Util from '@alicloud/tea-util';
   import dingtalkdrive_1_0, * as $dingtalkdrive_1_0 from '@alicloud/dingtalk/drive_1_0';
   import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
   import * as $tea from '@alicloud/tea-typescript';

   export default class Client {

     /**
      * 使用 Token 初始化账号Client
      * @return Client
      * @throws Exception
      */
     static createClient(): dingtalkdrive_1_0 {
       let config = new $OpenApi.Config({ });
       config.protocol = "https";
       config.regionId = "central";
       return new dingtalkdrive_1_0(config);
     }

     static async main(args: string[]): Promise<void> {
       let client = Client.createClient();
       let getDownloadInfoHeaders = new $dingtalkdrive_1_0.GetDownloadInfoHeaders({ });
       getDownloadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
       let getDownloadInfoRequest = new $dingtalkdrive_1_0.GetDownloadInfoRequest({
         unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
       });
       try {
         await client.getDownloadInfoWithOptions("<spaceId>", "<fileId>", getDownloadInfoRequest, getDownloadInfoHeaders, new $Util.RuntimeOptions({ }));
       } catch (err) {
         if (!Util.empty(err.code) && !Util.empty(err.message)) {
           // err 中含有 code 和 message 属性，可帮助开发定位问题
         }

       }    
     }

   }

   Client.main(process.argv.slice(2));
   ```
2. 根据获取到的加签URL信息，下载文件。

   示例代码如下：

   > **[!NOTE]**
   >
   > 必须使用[获取文件下载信息](1569-obtain-download-file-info.md)接口返回的加签URL信息和Header信息才能下载。

   Java

   ```
   public static void main(String[] args) {
     String url = "<url>";
     String path = "<path_to_file>";
     Map<String, String> headers = new HashMap<>();
     headers.put("<headerKey1>", "<headerValue1>");
     headers.put("<headerKey2>", "<headerValue2>");
       
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

   Python

   ```
   #!/usr/bin/env python
   import urllib.request

   url = '<url>'
   opener = urllib.request.build_opener()
   opener.addheaders = [('<headerKey1>', '<headerValue1>'), ('<headerKey2>', '<headerValue2>')]
   urllib.request.install_opener(opener)
   urllib.request.urlretrieve(url, '<path_to_file>')
   ```

   Go

   ```
   package main

   import (
       "io"
       "net/http"
       "os"
   )

   func main() {
       client := &http.Client{}
       url := "<url>"
       request, err := http.NewRequest("GET", url, nil)
       request.Header.Add("<headerKey1>", "<headerValue1>")
       request.Header.Add("<headerKey2>", "<headerValue2>")
       if err != nil {
           panic(err)
       }
       file, err := os.Create("<path_to_file>")
       if err != nil {
           panic(err)
       }
       response, _ := client.Do(request)
       io.Copy(file, response.Body)
   }
   ```

   C#

   ```
   WebRequest webRequest =  WebRequest.Create(<url>);
   MethodInfo addHeaderMethod = webRequest.Headers.GetType().GetMethod("AddWithoutValidate", BindingFlags.Instance | BindingFlags.NonPublic);
   addHeaderMethod.Invoke(webRequest.Headers, new[] { "Date", <headers.date> });
   webRequest.Headers.Add("Authorization", <headers.authorization>);

   HttpWebResponse response = null;
   Stream getResponseStream = null;
   Stream fileStream = null;

   try {
       response = (System.Net.HttpWebResponse)webRequest.GetResponse();
       getResponseStream = response.GetResponseStream();
       fileStream = new System.IO.FileStream("<path_to_file>", System.IO.FileMode.Create);
       byte[] buffer = new byte[1024];
       while ((osize = getResponseStream.Read(buffer, 0, (int)buffer.Length)) > 0)
       {
           fileStream.Write(buffer, 0, osize);
       }
   } catch {
       // do nothing
   } finally {
       if (response != null) {
           response.Close();
       }
       if (getResponseStream != null) {
           getResponseStream.Close();
       }
       if (fileStream != null) {
           fileStream.Close();
       }
   }
   ```

   JavaScript

   ```
   const fs = require('fs');
   const Axios = require('axios');
   const url = "<url>";
   const path = "<path_to_file>";
   const writer = fs.createWriteStream(path);
   Axios({
       url,
       method: "GET",
       responseType: "stream",
       headers: {
           '<headerKey1>': '<headerValue1>',
           '<headerKey2>': '<headerValue2>'
       }
   }).then(function(response) {
       response.data.pipe(writer);
   });
   ```

   HTTP

   ```
   curl -X GET -H "<headerKey1>:<headerValue1>" -H "<headerKey2>:<headerValue2>" --url "<url>"
   ```
