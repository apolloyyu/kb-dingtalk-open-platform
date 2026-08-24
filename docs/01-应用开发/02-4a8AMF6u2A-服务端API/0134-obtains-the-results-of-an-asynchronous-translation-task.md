---
title: "获取异步转译任务结果"
source_url: "https://open.dingtalk.com/document/development/obtains-the-results-of-an-asynchronous-translation-task"
namespace: "development"
slug: "obtains-the-results-of-an-asynchronous-translation-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 通讯录ID转译 > 获取异步转译任务结果"
doc_id: "Qd412Y1qzD"
updated_at: "2026-07-02 10:35:54"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-results-of-an-asynchronous-translation-task
> Path: 应用开发 / 服务端API / 通讯录管理 > 通讯录ID转译 > 获取异步转译任务结果
> Updated: 2026-07-02 10:35:54

# 获取异步转译任务结果

调用本接口，获取查询已经提交过的转译任务结果。

## **接口调用说明**

### 接口功能介绍

如果第三方企业应用选择了[通讯录加密](0135-address-book-encryption.md)部署方式，该应用调用通讯录等相关接口，无法获取授权企业员工姓名、职位和所在部门名称等信息。可以通过以下方法获取：

例如，某企业授权开通一个第三方企业应用，使用应用导出本企业可以使用该第三方应用的员工列表及信息，包含员工userID、员工姓名、员工所在部门ID和员工所在部门名称。可按照以下步骤实现。

1. 构造需要转译的文档，示例如下图所示。

   > **[!NOTE]**
   >
   > 只支持xlsx，xls，csv，txt格式文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9903630871/p1075881.png)
2. 调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，获取media\_id。
3. 调用[异步转译通讯录ID](0133-asynchronous-address-book-file-content-translation.md)接口，获取转译任务ID。

   > **[!NOTE]**
   >
   > 调用异步转译通讯录ID接口后，如果文件转译成功，会触发异步任务回调通知。
4. 调用本接口，获取转译后的文件下载链接。

   > **[!NOTE]**
   >
   > 返回的文件下载链接建议使用`<a>标签`引用，`download`属性不可指定（浏览器兼容性问题）。
5. 用户下载得到的文件内容，如下图所示。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9903630871/p1075882.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/files/translateResults |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| jobId | String | 是 | 异步转译任务ID，调用[异步转译通讯录ID](0133-asynchronous-address-book-file-content-translation.md)接口获取jobId参数值。 |

### 请求示例

HTTP

```
GET /v1.0/contact/files/translateResults?jobId=fXrgPrvsNiZNa8RWis9Nk1SY HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE6hsxxxx
Content-Type:application/json
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
        GetTranslateFileJobResultHeaders getTranslateFileJobResultHeaders = new GetTranslateFileJobResultHeaders();
        getTranslateFileJobResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetTranslateFileJobResultRequest getTranslateFileJobResultRequest = new GetTranslateFileJobResultRequest()
                .setJobId("fXrgPrvsNiZNa8RWis9Nk1SY");
        try {
            client.getTranslateFileJobResultWithOptions(getTranslateFileJobResultRequest, getTranslateFileJobResultHeaders, new RuntimeOptions());
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
        get_translate_file_job_result_headers = dingtalkcontact__1__0_models.GetTranslateFileJobResultHeaders()
        get_translate_file_job_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_translate_file_job_result_request = dingtalkcontact__1__0_models.GetTranslateFileJobResultRequest(
            job_id='fXrgPrvsNiZNa8RWis9Nk1SY'
        )
        try:
            client.get_translate_file_job_result_with_options(get_translate_file_job_result_request, get_translate_file_job_result_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_translate_file_job_result_headers = dingtalkcontact__1__0_models.GetTranslateFileJobResultHeaders()
        get_translate_file_job_result_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_translate_file_job_result_request = dingtalkcontact__1__0_models.GetTranslateFileJobResultRequest(
            job_id='fXrgPrvsNiZNa8RWis9Nk1SY'
        )
        try:
            await client.get_translate_file_job_result_with_options_async(get_translate_file_job_result_request, get_translate_file_job_result_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetTranslateFileJobResultHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetTranslateFileJobResultRequest;
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
        $getTranslateFileJobResultHeaders = new GetTranslateFileJobResultHeaders([]);
        $getTranslateFileJobResultHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getTranslateFileJobResultRequest = new GetTranslateFileJobResultRequest([
            "jobId" => "fXrgPrvsNiZNa8RWis9Nk1SY"
        ]);
        try {
            $client->getTranslateFileJobResultWithOptions($getTranslateFileJobResultRequest, $getTranslateFileJobResultHeaders, new RuntimeOptions([]));
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

  getTranslateFileJobResultHeaders := &dingtalkcontact_1_0.GetTranslateFileJobResultHeaders{}
  getTranslateFileJobResultHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getTranslateFileJobResultRequest := &dingtalkcontact_1_0.GetTranslateFileJobResultRequest{
    JobId: tea.String("fXrgPrvsNiZNa8RWis9Nk1SY"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetTranslateFileJobResultWithOptions(getTranslateFileJobResultRequest, getTranslateFileJobResultHeaders, &util.RuntimeOptions{})
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
    let getTranslateFileJobResultHeaders = new $dingtalkcontact_1_0.GetTranslateFileJobResultHeaders({ });
    getTranslateFileJobResultHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getTranslateFileJobResultRequest = new $dingtalkcontact_1_0.GetTranslateFileJobResultRequest({
      jobId: "fXrgPrvsNiZNa8RWis9Nk1SY",
    });
    try {
      await client.getTranslateFileJobResultWithOptions(getTranslateFileJobResultRequest, getTranslateFileJobResultHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetTranslateFileJobResultHeaders getTranslateFileJobResultHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetTranslateFileJobResultHeaders();
            getTranslateFileJobResultHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetTranslateFileJobResultRequest getTranslateFileJobResultRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetTranslateFileJobResultRequest
            {
                JobId = "fXrgPrvsNiZNa8RWis9Nk1SY",
            };
            try
            {
                client.GetTranslateFileJobResultWithOptions(getTranslateFileJobResultRequest, getTranslateFileJobResultHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcontact__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcontact_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcontact_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcontact_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetTranslateFileJobResultHeaders> getTranslateFileJobResultHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetTranslateFileJobResultHeaders>();
  getTranslateFileJobResultHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetTranslateFileJobResultRequest> getTranslateFileJobResultRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetTranslateFileJobResultRequest>(map<string, boost::any>({
    {"jobId", boost::any(string("fXrgPrvsNiZNa8RWis9Nk1SY"))}
  }));
  try {
    client->getTranslateFileJobResultWithOptions(getTranslateFileJobResultRequest, getTranslateFileJobResultHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| status | String | 转译任务结果，取值：   - **0**：任务进行中 - **1**：任务处理成功 - **2**：任务处理失败 |
| url | String | 文件内容转译成功后的URL。    需要通过oauth2授权登录在用户侧打开。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "status" : "1",
  "url" : "xxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.invalid | %s | 参数不合法 |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
