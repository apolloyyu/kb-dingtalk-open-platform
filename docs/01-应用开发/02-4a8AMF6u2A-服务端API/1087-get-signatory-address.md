---
title: "获取签署人签署地址"
source_url: "https://open.dingtalk.com/document/development/get-signatory-address"
namespace: "development"
slug: "get-signatory-address"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 获取签署人签署地址"
doc_id: "DVpTKRPC4Y"
updated_at: "2025-09-23 19:21:45"
---

> Source: https://open.dingtalk.com/document/development/get-signatory-address
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 获取签署人签署地址
> Updated: 2025-09-23 19:21:45

# 获取签署人签署地址

调用本接口获取到签署地址，isv应用内用户可点击进入签署页面进行签署，区分钉钉容器内的地址和钉钉容器外的地址（浏览器）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/process/executeUrls |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-E签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceGroup | String | 否 | 预留参数，此版本无需此参数。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 是 | 任务ID。 |
| signContainer | Integer | 否 | 签署链接允许在哪个容器打开，取值：   - **1**：钉钉 - **2**：浏览器   默认值：1。 |
| account | String | 否 | 签署人账号ID。      **signContainer**为**2**时，此参数必填，其他情况不用填。 |

### 请求示例

HTTP

```
POST /v2.0/esign/process/executeUrls HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "taskId" : "PRO-289F96A1xxx",
  "signContainer" : 1,
  "account" : "188xxx"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_2_0.*;
import com.aliyun.dingtalkesign_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_2_0.Client client = Sample.createClient();
        GetExecuteUrlHeaders getExecuteUrlHeaders = new GetExecuteUrlHeaders();
        getExecuteUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetExecuteUrlRequest getExecuteUrlRequest = new GetExecuteUrlRequest()
                .setTaskId("PRO-289F96A1xxx")
                .setSignContainer(1)
                .setAccount("188xxx");
        try {
            client.getExecuteUrlWithOptions(getExecuteUrlRequest, getExecuteUrlHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_2_0.client import Client as dingtalkesign_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_execute_url_headers = dingtalkesign__2__0_models.GetExecuteUrlHeaders()
        get_execute_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_execute_url_request = dingtalkesign__2__0_models.GetExecuteUrlRequest(
            task_id='PRO-289F96A1xxx',
            sign_container=1,
            account='188xxx'
        )
        try:
            client.get_execute_url_with_options(get_execute_url_request, get_execute_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_execute_url_headers = dingtalkesign__2__0_models.GetExecuteUrlHeaders()
        get_execute_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_execute_url_request = dingtalkesign__2__0_models.GetExecuteUrlRequest(
            task_id='PRO-289F96A1xxx',
            sign_container=1,
            account='188xxx'
        )
        try:
            await client.get_execute_url_with_options_async(get_execute_url_request, get_execute_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\GetExecuteUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\GetExecuteUrlRequest;
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
        $getExecuteUrlHeaders = new GetExecuteUrlHeaders([]);
        $getExecuteUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getExecuteUrlRequest = new GetExecuteUrlRequest([
            "taskId" => "PRO-289F96A1xxx",
            "signContainer" => 1,
            "account" => "188xxx"
        ]);
        try {
            $client->getExecuteUrlWithOptions($getExecuteUrlRequest, $getExecuteUrlHeaders, new RuntimeOptions([]));
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
  dingtalkesign_2_0  ""github.com/alibabacloud-go/dingtalk/esign_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_2_0.Client{}
  _result, _err = dingtalkesign_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getExecuteUrlHeaders := &dingtalkesign_2_0.GetExecuteUrlHeaders{}
  getExecuteUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getExecuteUrlRequest := &dingtalkesign_2_0.GetExecuteUrlRequest{
    TaskId: tea.String("PRO-289F96A1xxx"),
    SignContainer: tea.Int32(1),
    Account: tea.String("188xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetExecuteUrlWithOptions(getExecuteUrlRequest, getExecuteUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_2_0, * as $dingtalkesign_2_0 from '"@alicloud/dingtalk/esign_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getExecuteUrlHeaders = new $dingtalkesign_2_0.GetExecuteUrlHeaders({ });
    getExecuteUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getExecuteUrlRequest = new $dingtalkesign_2_0.GetExecuteUrlRequest({
      taskId: "PRO-289F96A1xxx",
      signContainer: 1,
      account: "188xxx",
    });
    try {
      await client.getExecuteUrlWithOptions(getExecuteUrlRequest, getExecuteUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetExecuteUrlHeaders getExecuteUrlHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetExecuteUrlHeaders();
            getExecuteUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetExecuteUrlRequest getExecuteUrlRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetExecuteUrlRequest
            {
                TaskId = "PRO-289F96A1xxx",
                SignContainer = 1,
                Account = "188xxx",
            };
            try
            {
                client.GetExecuteUrlWithOptions(getExecuteUrlRequest, getExecuteUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__2__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_2_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_2_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_2_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::GetExecuteUrlHeaders> getExecuteUrlHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::GetExecuteUrlHeaders>();
  getExecuteUrlHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::GetExecuteUrlRequest> getExecuteUrlRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::GetExecuteUrlRequest>(map<string, boost::any>({
    {"taskId", boost::any(string("PRO-289F96A1xxx"))},
    {"signContainer", boost::any(1)},
    {"account", boost::any(string("188xxx"))}
  }));
  try {
    client->getExecuteUrlWithOptions(getExecuteUrlRequest, getExecuteUrlHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| mobileUrl | String | 移动端钉钉容器内流程地址。      **signContainer**为**1**时，返回该地址。 |
| pcUrl | String | PC端钉钉容器内流程的地址。      **signContainer**为**1**时，返回该地址。 |
| longUrl | String | 流程地址，用于在浏览器内打开，长链地址永久有效, 不区分移动端或PC端，UI会自适应。      **signContainer**为**2**时，返回该地址。 |
| shortUrl | String | 流程地址，用于在浏览器内打开，短链地址30天有效, 不区分移动端或PC端，UI会自适应。      **signContainer**为**2**时，返回该地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "mobileUrl" : "http://xxx.com",
  "pcUrl" : "http://xxx.com",
  "longUrl" : "http://www.xxx.com",
  "shortUrl" : "http://www.xxx.com"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | getFlowInfoError | 获取流程信息失败 | 获取流程信息失败 |
| 400 | queryFlowError | 查询流程详情异常 | 查询流程详情异常 |
| 400 | getUserInfoFail | 获取用户信息失败,%s，%s | 获取用户信息失败 |
| 400 | getSignUrlError | 获取签署链接失败: %s | 获取签署链接失败 |
