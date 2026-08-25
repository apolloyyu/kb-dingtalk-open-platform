---
title: "获取文件上传地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-upload-url-of-a-file-2"
namespace: "development"
slug: "obtain-the-upload-url-of-a-file-2"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 氚云 > 文件管理 > 获取文件上传地址"
doc_id: "BMrfxhE3nR"
updated_at: "2025-09-08 19:06:28"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-upload-url-of-a-file-2
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 氚云 > 文件管理 > 获取文件上传地址
> Updated: 2025-09-08 19:06:28

# 获取文件上传地址

调用此接口返回表单中指定图片、附件等控件的文件上传地址。

> **[!IMPORTANT]**
>
> 为了更进一步提升接口质量以及用户体验，我们对本接口文档做出如下调整：
>
> - 自 2024 年 8 月 1 日起，本接口文档将会被迁移至历史文档目录。
> - 氚云接口不再支持新应用接入，已接入应用可继续使用，后续若需要接入氚云接口，请使用[氚云开发者手册](https://help.h3yun.com/channels/899.html)。

![](https://img.alicdn.com/imgextra/i3/O1CN017iq4c11TKl1sWh64L_!!6000000002364-2-tps-1080-671.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=h3yun_1.0%23GetUploadUrl) |
| 第三方企业应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=h3yun_1.0%23GetUploadUrl) |
| 第三方个人应用 | 暂不支持 | 氚云数据管理权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/h3yun/attachments/uploadUrls?schemaCode=String&bizObjectId=String&fieldName=String&isOverwrite=Boolean HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| schemaCode | String | 是 | 表单编码。 |
| bizObjectId | String | 是 | 业务数据实例ID。 |
| fieldName | String | 是 | 文件上传至目标控件的字段名。 |
| isOverwrite | Boolean | 是 | 是否覆盖，取值：   - **false**：添加 - **true**：覆盖 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 状态码。 |
| message | String | 状态码描述。 |
| data | Object | 返回结果。 |
| uploadUrl | String | 附件上传地址，有效期：30分钟。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/h3yun/attachments/uploadUrls?schemaCode=D00018xxx&bizObjectId=006f870b-4xxx&fieldName=Image&isOverwrite=true HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:0a642axxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkh3yun_1_0.*;
import com.aliyun.dingtalkh3yun_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkh3yun_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkh3yun_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkh3yun_1_0.Client client = Sample.createClient();
        GetUploadUrlHeaders getUploadUrlHeaders = new GetUploadUrlHeaders();
        getUploadUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetUploadUrlRequest getUploadUrlRequest = new GetUploadUrlRequest()
                .setSchemaCode("D00018xxx")
                .setBizObjectId("006f870b-4xxx")
                .setFieldName("Image")
                .setIsOverwrite(true);
        try {
            client.getUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.h3yun_1_0.client import Client as dingtalkh3yun_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.h3yun_1_0 import models as dingtalkh_3yun__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkh3yun_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkh3yun_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_upload_url_headers = dingtalkh_3yun__1__0_models.GetUploadUrlHeaders()
        get_upload_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_upload_url_request = dingtalkh_3yun__1__0_models.GetUploadUrlRequest(
            schema_code='D00018xxx',
            biz_object_id='006f870b-4xxx',
            field_name='Image',
            is_overwrite=True
        )
        try:
            client.get_upload_url_with_options(get_upload_url_request, get_upload_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_upload_url_headers = dingtalkh_3yun__1__0_models.GetUploadUrlHeaders()
        get_upload_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_upload_url_request = dingtalkh_3yun__1__0_models.GetUploadUrlRequest(
            schema_code='D00018xxx',
            biz_object_id='006f870b-4xxx',
            field_name='Image',
            is_overwrite=True
        )
        try:
            await client.get_upload_url_with_options_async(get_upload_url_request, get_upload_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\GetUploadUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\GetUploadUrlRequest;
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
        $getUploadUrlHeaders = new GetUploadUrlHeaders([]);
        $getUploadUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUploadUrlRequest = new GetUploadUrlRequest([
            "schemaCode" => "D00018xxx",
            "bizObjectId" => "006f870b-4xxx",
            "fieldName" => "Image",
            "isOverwrite" => true
        ]);
        try {
            $client->getUploadUrlWithOptions($getUploadUrlRequest, $getUploadUrlHeaders, new RuntimeOptions([]));
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
  dingtalkh3yun_1_0  "github.com/alibabacloud-go/dingtalk/h3yun_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkh3yun_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkh3yun_1_0.Client{}
  _result, _err = dingtalkh3yun_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUploadUrlHeaders := &dingtalkh3yun_1_0.GetUploadUrlHeaders{}
  getUploadUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUploadUrlRequest := &dingtalkh3yun_1_0.GetUploadUrlRequest{
    SchemaCode: tea.String("D00018xxx"),
    BizObjectId: tea.String("006f870b-4xxx"),
    FieldName: tea.String("Image"),
    IsOverwrite: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkh3yun_1_0, * as $dingtalkh3yun_1_0 from '@alicloud/dingtalk/h3yun_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkh3yun_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkh3yun_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUploadUrlHeaders = new $dingtalkh3yun_1_0.GetUploadUrlHeaders({ });
    getUploadUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUploadUrlRequest = new $dingtalkh3yun_1_0.GetUploadUrlRequest({
      schemaCode: "D00018xxx",
      bizObjectId: "006f870b-4xxx",
      fieldName: "Image",
      isOverwrite: true,
    });
    try {
      await client.getUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetUploadUrlHeaders getUploadUrlHeaders = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetUploadUrlHeaders();
            getUploadUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetUploadUrlRequest getUploadUrlRequest = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.GetUploadUrlRequest
            {
                SchemaCode = "D00018xxx",
                BizObjectId = "006f870b-4xxx",
                FieldName = "Image",
                IsOverwrite = true,
            };
            try
            {
                client.GetUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkh_3yun__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkh3yun_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkh3yun_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::Client> client = make_shared<Alibabacloud_Dingtalkh3yun_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::GetUploadUrlHeaders> getUploadUrlHeaders = make_shared<Alibabacloud_Dingtalkh3yun_1_0::GetUploadUrlHeaders>();
  getUploadUrlHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::GetUploadUrlRequest> getUploadUrlRequest = make_shared<Alibabacloud_Dingtalkh3yun_1_0::GetUploadUrlRequest>(map<string, boost::any>({
    {"schemaCode", boost::any(string("D00018xxx"))},
    {"bizObjectId", boost::any(string("006f870b-4xxx"))},
    {"fieldName", boost::any(string("Image"))},
    {"isOverwrite", boost::any(true)}
  }));
  try {
    client->getUploadUrlWithOptions(getUploadUrlRequest, getUploadUrlHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : "success",
  "message" : "OK",
  "data" : {
    "uploadUrl" : "https://xxx?uploadSecret=xxx"
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | dataNotExist.form.schemaNotExist | 表单结构不存在 | 无效的schemaCode参数 |
| 400 | invalidRequest.bizObjectNotExist | 业务对象不存在 | 无效的bizObjectId参数 |
| 400 | invalidRequest.file.getUploadUrlFile | 获取文件上传地址失败 | 获取文件上传地址失败 |
| 500 | systemError | 系统异常 | 系统异常 |
