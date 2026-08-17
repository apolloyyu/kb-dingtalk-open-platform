---
title: "更新发送文件的检测状态"
source_url: "https://open.dingtalk.com/document/development/update-the-detection-status-of-a-sent-file"
namespace: "development"
slug: "update-the-detection-status-of-a-sent-file"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 更新发送文件的检测状态"
doc_id: "Y9favm5vNR"
updated_at: "2025-09-23 19:20:10"
---

> Source: https://open.dingtalk.com/document/development/update-the-detection-status-of-a-sent-file
> Path: 应用开发 / 服务端API / 专属钉钉 > 更新发送文件的检测状态
> Updated: 2025-09-23 19:20:10

# 更新发送文件的检测状态

调用本接口更改发送文件的检测状态。

## 接口调用说明

专属钉钉组织管理员登录[企业管理后台](https://oa.dingtalk.com)，在**钉钉专属版 > 专属安全 > 安全引擎中心 > 三色管控**中设置了DLP策略后，员工发送的文件将进入检测状态。调用本接口可更改发送文件的检测状态，修改文件检测状态为检测通过、检测不通过或额外审批。 ![](https://img.alicdn.com/imgextra/i3/O1CN01TaYLbT1tRnFIp7kbI_!!6000000005899-0-tps-1108-880.jpg)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/sending/files/status |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.FileCheck.ReadWrite-专属钉钉文件内容检测结果读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| requestIds | Array of String | 是 | 文件发送的请求requestId，从订阅的[企业员工发送文件的检测事件](../04-LFcRvVD08N-事件订阅/0206-detection-event-of-enterprise-employee-sending-file.md)中获取。 |
| status | Integer | 是 | 更新状态，取值：   - 1：检测通过。 - 2：检测不通过。 - 3：需要额外审批（需要先勾选“启用DLP后审批”）       如果检测不通过或额外审批未通过，文件接收方无法预览或者下载该文件。 |

### 请求示例

HTTP

```
PUT /v1.0/exclusive/sending/files/status HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "requestIds" : [ "dlpId13xx23232" ],
  "status" : 1
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        UpdateFileStatusHeaders updateFileStatusHeaders = new UpdateFileStatusHeaders();
        updateFileStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateFileStatusRequest updateFileStatusRequest = new UpdateFileStatusRequest()
                .setRequestIds(java.util.Arrays.asList(
                    "dlpId13xx23232"
                ))
                .setStatus(1);
        try {
            client.updateFileStatusWithOptions(updateFileStatusRequest, updateFileStatusHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_file_status_headers = dingtalkexclusive__1__0_models.UpdateFileStatusHeaders()
        update_file_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_file_status_request = dingtalkexclusive__1__0_models.UpdateFileStatusRequest(
            request_ids=[
                'dlpId13xx23232'
            ],
            status=1
        )
        try:
            client.update_file_status_with_options(update_file_status_request, update_file_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_file_status_headers = dingtalkexclusive__1__0_models.UpdateFileStatusHeaders()
        update_file_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_file_status_request = dingtalkexclusive__1__0_models.UpdateFileStatusRequest(
            request_ids=[
                'dlpId13xx23232'
            ],
            status=1
        )
        try:
            await client.update_file_status_with_options_async(update_file_status_request, update_file_status_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\UpdateFileStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\UpdateFileStatusRequest;
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
        $updateFileStatusHeaders = new UpdateFileStatusHeaders([]);
        $updateFileStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateFileStatusRequest = new UpdateFileStatusRequest([
            "requestIds" => [
                "dlpId13xx23232"
            ],
            "status" => 1
        ]);
        try {
            $client->updateFileStatusWithOptions($updateFileStatusRequest, $updateFileStatusHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateFileStatusHeaders := &dingtalkexclusive_1_0.UpdateFileStatusHeaders{}
  updateFileStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateFileStatusRequest := &dingtalkexclusive_1_0.UpdateFileStatusRequest{
    RequestIds: []*string{tea.String("dlpId13xx23232")},
    Status: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateFileStatusWithOptions(updateFileStatusRequest, updateFileStatusHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let updateFileStatusHeaders = new $dingtalkexclusive_1_0.UpdateFileStatusHeaders({ });
    updateFileStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateFileStatusRequest = new $dingtalkexclusive_1_0.UpdateFileStatusRequest({
      requestIds: [
        "dlpId13xx23232"
      ],
      status: 1,
    });
    try {
      await client.updateFileStatusWithOptions(updateFileStatusRequest, updateFileStatusHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.UpdateFileStatusHeaders updateFileStatusHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.UpdateFileStatusHeaders();
            updateFileStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.UpdateFileStatusRequest updateFileStatusRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.UpdateFileStatusRequest
            {
                RequestIds = new List<string>
                {
                    "dlpId13xx23232"
                },
                Status = 1,
            };
            try
            {
                client.UpdateFileStatusWithOptions(updateFileStatusRequest, updateFileStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkexclusive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkexclusive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkexclusive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkexclusive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::UpdateFileStatusHeaders> updateFileStatusHeaders = make_shared<Alibabacloud_Dingtalkexclusive_1_0::UpdateFileStatusHeaders>();
  updateFileStatusHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::UpdateFileStatusRequest> updateFileStatusRequest = make_shared<Alibabacloud_Dingtalkexclusive_1_0::UpdateFileStatusRequest>(map<string, boost::any>({
    {"requestIds", boost::any(vector<string>({
      "dlpId13xx23232"
    }))},
    {"status", boost::any(1)}
  }));
  try {
    client->updateFileStatusWithOptions(updateFileStatusRequest, updateFileStatusHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| success | Boolean | 是否成功，取值：   - true：成功 - false：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | %s | 参数不合法，如requestIds不合法、status不合法 |
| 400 | param.length.exceed | %s | 参数requestIds长度超出限制 |
