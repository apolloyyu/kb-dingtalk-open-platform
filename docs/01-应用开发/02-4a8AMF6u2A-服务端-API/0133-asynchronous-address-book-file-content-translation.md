---
title: "异步转译通讯录ID"
source_url: "https://open.dingtalk.com/document/development/asynchronous-address-book-file-content-translation"
namespace: "development"
slug: "asynchronous-address-book-file-content-translation"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 通讯录ID转译 > 异步转译通讯录ID"
doc_id: "Tb2VE3RKXf"
updated_at: "2026-07-02 10:35:53"
---

> Source: https://open.dingtalk.com/document/development/asynchronous-address-book-file-content-translation
> Path: 应用开发 / 服务端 API / 通讯录管理 > 通讯录ID转译 > 异步转译通讯录ID
> Updated: 2026-07-02 10:35:53

# 异步转译通讯录ID

调用本接口，发起异步通讯录ID内容转译，替换产品方案商通讯录权限范围内的用户ID和部门ID。

## **接口调用说明**

如果第三方企业应用选择了[通讯录加密](0135-address-book-encryption.md)部署方式，该应用调用通讯录等相关接口，无法获取授权企业员工姓名、职位和所在部门名称等信息。可以通过以下方法获取：

例如，某企业授权开通一个第三方企业应用，使用应用导出本企业可以使用该第三方应用的员工列表及信息，包含员工userID、员工姓名、员工所在部门ID和员工所在部门名称。可按照以下步骤实现。

1. 构造需要转译的文档，示例如下图所示。

   > **[!NOTE]**
   >
   > 只支持xlsx，xls，csv，txt格式文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8903630871/p1075878.png)
2. 调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，获取media\_id。
3. 调用本接口，获取转译任务ID。

   > **[!NOTE]**
   >
   > 调用本接口后，如果文件转译成功，会触发异步任务回调通知。
4. 调用[获取异步转译任务结果](https://open.dingtalk.com/document/isvapp/obtains-the-results-of-an-asynchronous-translation-task)接口，获取转译后的文件下载链接。

   > **[!NOTE]**
   >
   > 返回的文件下载链接建议使用`<a>标签`引用，`download`属性不可指定（浏览器兼容性问题）。
5. 用户下载得到的文件内容，如下图所示。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8903630871/p1075879.png)

在调用本接口的过程中，你可能会遇到以下问题：

- **问题**：使用`NodeJs`第三方库`exceljs`生成的`excel`文件，文件内容看上去正常，但是转译不成功。
- **问题原因**：`exceljs`在不开启`sharedString`的情况下，会默认使用`formula string`进行文件内容写入，这种行为不合规范，导致转译失败。
- **解决方法**：查看`exceljs`文档，强制开启`useSharedStrings`选项。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/files/translate |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| medias | Map<String, String> | 是 | 需要转译的文件信息。   - Map类型，key为钉盘文件media\_id，调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口获取。 - value为文件名，需要包含文件扩展名，与调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口时传入的文件名称保持一致。        - 只支持xlsx，xls，csv，txt类型文件。 - 最大数量20个文件。 |
| outputFileName | String | 否 | 转译完打包的文件名，不需带后缀。      若medias中文件个数大于1，则该参数必填。 |
| unionId | String | 是 | 当前操作导出文档的用户的unionId，可以调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/contact/files/translate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BWe2xxxx
Content-Type:application/json

{
  "medias" : {
    "key" : "xxxx"
  },
  "outputFileName" : "学习手册",
  "unionId" : "fXRUNxxx"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcontact_1_0.*;
import com.aliyun.dingtalkcontact_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        TranslateFileHeaders translateFileHeaders = new TranslateFileHeaders();
        translateFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> medias = TeaConverter.buildMap(
            new TeaPair("key", "xxxx")
        );
        TranslateFileRequest translateFileRequest = new TranslateFileRequest()
                .setMedias(medias)
                .setOutputFileName("学习手册")
                .setUnionId("fXRUNxxx");
        try {
            client.translateFileWithOptions(translateFileRequest, translateFileHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        translate_file_headers = dingtalkcontact__1__0_models.TranslateFileHeaders()
        translate_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        medias = {
            'key': 'xxxx'
        }
        translate_file_request = dingtalkcontact__1__0_models.TranslateFileRequest(
            medias=medias,
            output_file_name='学习手册',
            union_id='fXRUNxxx'
        )
        try:
            client.translate_file_with_options(translate_file_request, translate_file_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        translate_file_headers = dingtalkcontact__1__0_models.TranslateFileHeaders()
        translate_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        medias = {
            'key': 'xxxx'
        }
        translate_file_request = dingtalkcontact__1__0_models.TranslateFileRequest(
            medias=medias,
            output_file_name='学习手册',
            union_id='fXRUNxxx'
        )
        try:
            await client.translate_file_with_options_async(translate_file_request, translate_file_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\TranslateFileHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\TranslateFileRequest;
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
        $translateFileHeaders = new TranslateFileHeaders([]);
        $translateFileHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $medias = [
            "key" => "xxxx"
        ];
        $translateFileRequest = new TranslateFileRequest([
            "medias" => $medias,
            "outputFileName" => "学习手册",
            "unionId" => "fXRUNxxx"
        ]);
        try {
            $client->translateFileWithOptions($translateFileRequest, $translateFileHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  translateFileHeaders := &dingtalkcontact_1_0.TranslateFileHeaders{}
  translateFileHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  medias := map[string]*string{
    "key": tea.String("xxxx"),
  }
  translateFileRequest := &dingtalkcontact_1_0.TranslateFileRequest{
    Medias: medias,
    OutputFileName: tea.String("学习手册"),
    UnionId: tea.String("fXRUNxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.TranslateFileWithOptions(translateFileRequest, translateFileHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let translateFileHeaders = new $dingtalkcontact_1_0.TranslateFileHeaders({ });
    translateFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let medias = {
      key: "xxxx",
    };
    let translateFileRequest = new $dingtalkcontact_1_0.TranslateFileRequest({
      medias: medias,
      outputFileName: "学习手册",
      unionId: "fXRUNxxx",
    });
    try {
      await client.translateFileWithOptions(translateFileRequest, translateFileHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.TranslateFileHeaders translateFileHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.TranslateFileHeaders();
            translateFileHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> medias = new Dictionary<string, string>
            {
                {"key", "xxxx"},
            };
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.TranslateFileRequest translateFileRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.TranslateFileRequest
            {
                Medias = medias,
                OutputFileName = "学习手册",
                UnionId = "fXRUNxxx",
            };
            try
            {
                client.TranslateFileWithOptions(translateFileRequest, translateFileHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| jobId | String | 异步转译任务ID，最大长度为64字符。    **jobId**用于接口[获取异步转译任务结果](0134-obtains-the-results-of-an-asynchronous-translation-task.md)传递。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "jobId" : "fXrgPrvsNxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.invalid | %s | 参数不合法 |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
