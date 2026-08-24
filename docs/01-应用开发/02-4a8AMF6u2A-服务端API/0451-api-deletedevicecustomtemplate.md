---
title: "删除自定义屏幕模板"
source_url: "https://open.dingtalk.com/document/development/api-deletedevicecustomtemplate"
namespace: "development"
slug: "api-deletedevicecustomtemplate"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 自定义屏幕模板 > 删除自定义屏幕模板"
doc_id: "NA871TjlC6"
updated_at: "2026-06-02 13:18:21"
---

> Source: https://open.dingtalk.com/document/development/api-deletedevicecustomtemplate
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 自定义屏幕模板 > 删除自定义屏幕模板
> Updated: 2026-06-02 13:18:21

# 删除自定义屏幕模板

调用本接口，根据模板ID，删除自定义屏幕模板。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/devices/screens/templates/remove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Rooms.DeviceTemplate.Write-钉钉会议Rooms系统自定义屏幕写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。  **[!NOTE]**    获取用户token的请求中，使用的入参`code`参数，在通过构造链接获取的过程中，scope范围必须为用户id和组织id，即`scope=openid corpid`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| templateId | Long | 是 | 模板id，可调用[查询自定义屏幕模板列表](https://open.dingtalk.com/document/development/api-querydevicecustomtemplatelist)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/rooms/devices/screens/templates/remove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxx
Content-Type:application/json

{
  "templateId" : 89
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
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.DeleteDeviceCustomTemplateHeaders deleteDeviceCustomTemplateHeaders = new com.aliyun.dingtalkrooms_1_0.models.DeleteDeviceCustomTemplateHeaders();
        deleteDeviceCustomTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.DeleteDeviceCustomTemplateRequest deleteDeviceCustomTemplateRequest = new com.aliyun.dingtalkrooms_1_0.models.DeleteDeviceCustomTemplateRequest()
                .setTemplateId(89L);
        try {
            client.deleteDeviceCustomTemplateWithOptions(deleteDeviceCustomTemplateRequest, deleteDeviceCustomTemplateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys

from typing import List

from alibabacloud_dingtalk.rooms_1_0.client import Client as dingtalkrooms_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.rooms_1_0 import models as dingtalkrooms__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrooms_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrooms_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_device_custom_template_headers = dingtalkrooms__1__0_models.DeleteDeviceCustomTemplateHeaders()
        delete_device_custom_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_device_custom_template_request = dingtalkrooms__1__0_models.DeleteDeviceCustomTemplateRequest(
            template_id=89
        )
        try:
            client.delete_device_custom_template_with_options(delete_device_custom_template_request, delete_device_custom_template_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_device_custom_template_headers = dingtalkrooms__1__0_models.DeleteDeviceCustomTemplateHeaders()
        delete_device_custom_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_device_custom_template_request = dingtalkrooms__1__0_models.DeleteDeviceCustomTemplateRequest(
            template_id=89
        )
        try:
            await client.delete_device_custom_template_with_options_async(delete_device_custom_template_request, delete_device_custom_template_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\DeleteDeviceCustomTemplateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\DeleteDeviceCustomTemplateRequest;
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
        $deleteDeviceCustomTemplateHeaders = new DeleteDeviceCustomTemplateHeaders([]);
        $deleteDeviceCustomTemplateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteDeviceCustomTemplateRequest = new DeleteDeviceCustomTemplateRequest([
            "templateId" => 89
        ]);
        try {
            $client->deleteDeviceCustomTemplateWithOptions($deleteDeviceCustomTemplateRequest, $deleteDeviceCustomTemplateHeaders, new RuntimeOptions([]));
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
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrooms_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrooms_1_0.Client{}
  _result, _err = dingtalkrooms_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteDeviceCustomTemplateHeaders := &dingtalkrooms_1_0.DeleteDeviceCustomTemplateHeaders{}
  deleteDeviceCustomTemplateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteDeviceCustomTemplateRequest := &dingtalkrooms_1_0.DeleteDeviceCustomTemplateRequest{
    TemplateId: tea.Int64(89),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteDeviceCustomTemplateWithOptions(deleteDeviceCustomTemplateRequest, deleteDeviceCustomTemplateHeaders, &util.RuntimeOptions{})
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
import dingtalkrooms_1_0, * as $dingtalkrooms_1_0 from '@alicloud/dingtalk/rooms_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrooms_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrooms_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let deleteDeviceCustomTemplateHeaders = new $dingtalkrooms_1_0.DeleteDeviceCustomTemplateHeaders({ });
    deleteDeviceCustomTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deleteDeviceCustomTemplateRequest = new $dingtalkrooms_1_0.DeleteDeviceCustomTemplateRequest({
      templateId: 89,
    });
    try {
      await client.deleteDeviceCustomTemplateWithOptions(deleteDeviceCustomTemplateRequest, deleteDeviceCustomTemplateHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrooms_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrooms_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteDeviceCustomTemplateHeaders deleteDeviceCustomTemplateHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteDeviceCustomTemplateHeaders();
            deleteDeviceCustomTemplateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteDeviceCustomTemplateRequest deleteDeviceCustomTemplateRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.DeleteDeviceCustomTemplateRequest
            {
                TemplateId = 89,
            };
            try
            {
                client.DeleteDeviceCustomTemplateWithOptions(deleteDeviceCustomTemplateRequest, deleteDeviceCustomTemplateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 删除是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数错误 |
| 400 | no.permission | No Permission | 无权限 |
| 400 | template.not.found | Template Not Found | 模板找不到 |
| 500 | system.error | System Error | 系统错误 |
