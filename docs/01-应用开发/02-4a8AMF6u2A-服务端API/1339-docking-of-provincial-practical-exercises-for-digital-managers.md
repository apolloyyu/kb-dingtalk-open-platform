---
title: "检查用户是否完成所有任务"
source_url: "https://open.dingtalk.com/document/development/docking-of-provincial-practical-exercises-for-digital-managers"
namespace: "development"
slug: "docking-of-provincial-practical-exercises-for-digital-managers"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 数字化管理师 > 检查用户是否完成所有任务"
doc_id: "UKjYqq1Hv2"
updated_at: "2025-09-23 19:19:17"
---

> Source: https://open.dingtalk.com/document/development/docking-of-provincial-practical-exercises-for-digital-managers
> Path: 应用开发 / 服务端API / 更多开放 > 数字化管理师 > 检查用户是否完成所有任务
> Updated: 2025-09-23 19:19:17

# 检查用户是否完成所有任务

调用本接口检查用户是否完成所有数字化管理师的实操任务。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/occupationauth/userTasks/check |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方个人应用 |
| 权限要求 | permission-DigitalManager.TaskStatus.Read-数字化管理师任务状态读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| provinceCode | String | 是 | 省级任务对接入。 |

### 请求示例

HTTP

```
POST /v1.0/occupationauth/userTasks/check?provinceCode=18baojo123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:adjb123
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkoccupationauth_1_0.*;
import com.aliyun.dingtalkoccupationauth_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkoccupationauth_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkoccupationauth_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkoccupationauth_1_0.Client client = Sample.createClient();
        CheckUserTasksStatusHeaders checkUserTasksStatusHeaders = new CheckUserTasksStatusHeaders();
        checkUserTasksStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CheckUserTasksStatusRequest checkUserTasksStatusRequest = new CheckUserTasksStatusRequest()
                .setProvinceCode("18baojo123");
        try {
            client.checkUserTasksStatusWithOptions(checkUserTasksStatusRequest, checkUserTasksStatusHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.occupationauth_1_0.client import Client as dingtalkoccupationauth_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.occupationauth_1_0 import models as dingtalkoccupationauth__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkoccupationauth_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkoccupationauth_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_user_tasks_status_headers = dingtalkoccupationauth__1__0_models.CheckUserTasksStatusHeaders()
        check_user_tasks_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        check_user_tasks_status_request = dingtalkoccupationauth__1__0_models.CheckUserTasksStatusRequest(
            province_code='18baojo123'
        )
        try:
            client.check_user_tasks_status_with_options(check_user_tasks_status_request, check_user_tasks_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_user_tasks_status_headers = dingtalkoccupationauth__1__0_models.CheckUserTasksStatusHeaders()
        check_user_tasks_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        check_user_tasks_status_request = dingtalkoccupationauth__1__0_models.CheckUserTasksStatusRequest(
            province_code='18baojo123'
        )
        try:
            await client.check_user_tasks_status_with_options_async(check_user_tasks_status_request, check_user_tasks_status_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Voccupationauth_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Voccupationauth_1_0\Models\CheckUserTasksStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Voccupationauth_1_0\Models\CheckUserTasksStatusRequest;
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
        $checkUserTasksStatusHeaders = new CheckUserTasksStatusHeaders([]);
        $checkUserTasksStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $checkUserTasksStatusRequest = new CheckUserTasksStatusRequest([
            "provinceCode" => "18baojo123"
        ]);
        try {
            $client->checkUserTasksStatusWithOptions($checkUserTasksStatusRequest, $checkUserTasksStatusHeaders, new RuntimeOptions([]));
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
  dingtalkoccupationauth_1_0  "github.com/alibabacloud-go/dingtalk/occupationauth_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkoccupationauth_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkoccupationauth_1_0.Client{}
  _result, _err = dingtalkoccupationauth_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  checkUserTasksStatusHeaders := &dingtalkoccupationauth_1_0.CheckUserTasksStatusHeaders{}
  checkUserTasksStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  checkUserTasksStatusRequest := &dingtalkoccupationauth_1_0.CheckUserTasksStatusRequest{
    ProvinceCode: tea.String("18baojo123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CheckUserTasksStatusWithOptions(checkUserTasksStatusRequest, checkUserTasksStatusHeaders, &util.RuntimeOptions{})
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
import dingtalkoccupationauth_1_0, * as $dingtalkoccupationauth_1_0 from '@alicloud/dingtalk/occupationauth_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkoccupationauth_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkoccupationauth_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let checkUserTasksStatusHeaders = new $dingtalkoccupationauth_1_0.CheckUserTasksStatusHeaders({ });
    checkUserTasksStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let checkUserTasksStatusRequest = new $dingtalkoccupationauth_1_0.CheckUserTasksStatusRequest({
      provinceCode: "18baojo123",
    });
    try {
      await client.checkUserTasksStatusWithOptions(checkUserTasksStatusRequest, checkUserTasksStatusHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Models.CheckUserTasksStatusHeaders checkUserTasksStatusHeaders = new AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Models.CheckUserTasksStatusHeaders();
            checkUserTasksStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Models.CheckUserTasksStatusRequest checkUserTasksStatusRequest = new AlibabaCloud.SDK.Dingtalkoccupationauth_1_0.Models.CheckUserTasksStatusRequest
            {
                ProvinceCode = "18baojo123",
            };
            try
            {
                client.CheckUserTasksStatusWithOptions(checkUserTasksStatusRequest, checkUserTasksStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkoccupationauth__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkoccupationauth_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkoccupationauth_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkoccupationauth_1_0::Client> client = make_shared<Alibabacloud_Dingtalkoccupationauth_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkoccupationauth_1_0::CheckUserTasksStatusHeaders> checkUserTasksStatusHeaders = make_shared<Alibabacloud_Dingtalkoccupationauth_1_0::CheckUserTasksStatusHeaders>();
  checkUserTasksStatusHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkoccupationauth_1_0::CheckUserTasksStatusRequest> checkUserTasksStatusRequest = make_shared<Alibabacloud_Dingtalkoccupationauth_1_0::CheckUserTasksStatusRequest>(map<string, boost::any>({
    {"provinceCode", boost::any(string("18baojo123"))}
  }));
  try {
    client->checkUserTasksStatusWithOptions(checkUserTasksStatusRequest, checkUserTasksStatusHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| status | Boolean | 是否完成所有实操题任务。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "status" : false
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invaild.parameter | invaildParameter | 参数非法 |
| 500 | system.error | system error %s | 系统错误 |
