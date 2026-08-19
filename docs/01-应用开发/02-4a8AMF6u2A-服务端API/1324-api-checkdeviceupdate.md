---
title: "检查指定设备的固件升级"
source_url: "https://open.dingtalk.com/document/development/api-checkdeviceupdate"
namespace: "development"
slug: "api-checkdeviceupdate"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 智能硬件 > AIoT 平台 > 检查指定设备的固件升级"
doc_id: "Bj2x7hWgdi"
updated_at: "2026-07-15 17:05:04"
---

> Source: https://open.dingtalk.com/document/development/api-checkdeviceupdate
> Path: 应用开发 / 服务端API / 更多开放 > 智能硬件 > AIoT 平台 > 检查指定设备的固件升级
> Updated: 2026-07-15 17:05:04

# 检查指定设备的固件升级

调用本接口，检查指定设备的固件升级。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/aiot/products/{productKey}/devices/{deviceName}/firmware/checkUpdate |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Device.AIoT.Read-AIoT平台读取设备信息权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| productKey | String | 是 | 产品Key。 |
| deviceName | String | 是 | 设备名字。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 是 | 设备当前安装的固件模块和版本列表。 |
| moduleName | String | 是 | 模块的名字。 |
| currentVersion | String | 否 | 当前版本。 |

### **请求示例**

HTTP

```
POST /v1.0/aiot/products/OjpTuxxxxCkveZjo/devices/dn_0xxxx200/firmware/checkUpdate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e41e9xxxxcbbc
Content-Type:application/json

[ {
  "moduleName" : "main",
  "currentVersion" : "1.2.0"
} ]
```

Java

```
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkaiot_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkaiot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkaiot_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkaiot_1_0.models.CheckDeviceUpdateHeaders checkDeviceUpdateHeaders = new com.aliyun.dingtalkaiot_1_0.models.CheckDeviceUpdateHeaders();
        checkDeviceUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkaiot_1_0.models.CheckDeviceUpdateRequest.CheckDeviceUpdateRequestBody body0 = new com.aliyun.dingtalkaiot_1_0.models.CheckDeviceUpdateRequest.CheckDeviceUpdateRequestBody()
                .setModuleName("main")
                .setCurrentVersion("1.2.0");
        com.aliyun.dingtalkaiot_1_0.models.CheckDeviceUpdateRequest checkDeviceUpdateRequest = new com.aliyun.dingtalkaiot_1_0.models.CheckDeviceUpdateRequest()
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.checkDeviceUpdateWithOptions("OjpTuxxxxCkveZjo", "dn_0xxxx200", checkDeviceUpdateRequest, checkDeviceUpdateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.aiot_1_0.client import Client as dingtalkaiot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.aiot_1_0 import models as dingtalkaiot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkaiot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkaiot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_device_update_headers = dingtalkaiot__1__0_models.CheckDeviceUpdateHeaders()
        check_device_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkaiot__1__0_models.CheckDeviceUpdateRequestBody(
            module_name='main',
            current_version='1.2.0'
        )
        check_device_update_request = dingtalkaiot__1__0_models.CheckDeviceUpdateRequest(
            body=[
                body_0
            ]
        )
        try:
            client.check_device_update_with_options('OjpTuxxxxCkveZjo', 'dn_0xxxx200', check_device_update_request, check_device_update_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_device_update_headers = dingtalkaiot__1__0_models.CheckDeviceUpdateHeaders()
        check_device_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkaiot__1__0_models.CheckDeviceUpdateRequestBody(
            module_name='main',
            current_version='1.2.0'
        )
        check_device_update_request = dingtalkaiot__1__0_models.CheckDeviceUpdateRequest(
            body=[
                body_0
            ]
        )
        try:
            await client.check_device_update_with_options_async('OjpTuxxxxCkveZjo', 'dn_0xxxx200', check_device_update_request, check_device_update_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vaiot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vaiot_1_0\Models\CheckDeviceUpdateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vaiot_1_0\Models\CheckDeviceUpdateRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vaiot_1_0\Models\CheckDeviceUpdateRequest;
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
        $checkDeviceUpdateHeaders = new CheckDeviceUpdateHeaders([]);
        $checkDeviceUpdateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "moduleName" => "main",
            "currentVersion" => "1.2.0"
        ]);
        $checkDeviceUpdateRequest = new CheckDeviceUpdateRequest([
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->checkDeviceUpdateWithOptions("OjpTuxxxxCkveZjo", "dn_0xxxx200", $checkDeviceUpdateRequest, $checkDeviceUpdateHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkaiot_1_0  "github.com/alibabacloud-go/dingtalk/aiot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalkaiot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkaiot_1_0.Client{}
  _result, _err = dingtalkaiot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  checkDeviceUpdateHeaders := &dingtalkaiot_1_0.CheckDeviceUpdateHeaders{}
  checkDeviceUpdateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkaiot_1_0.CheckDeviceUpdateRequestBody{
    ModuleName: tea.String("main"),
    CurrentVersion: tea.String("1.2.0"),
  }
  checkDeviceUpdateRequest := &dingtalkaiot_1_0.CheckDeviceUpdateRequest{
    Body: []*dingtalkaiot_1_0.CheckDeviceUpdateRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CheckDeviceUpdateWithOptions(tea.String("OjpTuxxxxCkveZjo"), tea.String("dn_0xxxx200"), checkDeviceUpdateRequest, checkDeviceUpdateHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkaiot_1_0 = require('@alicloud/dingtalk/aiot_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkaiot_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let checkDeviceUpdateHeaders = new dingtalkaiot_1_0.CheckDeviceUpdateHeaders({ });
    checkDeviceUpdateHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let body0 = new dingtalkaiot_1_0.CheckDeviceUpdateRequestBody({
      moduleName: 'main',
      currentVersion: '1.2.0',
    });
    let checkDeviceUpdateRequest = new dingtalkaiot_1_0.CheckDeviceUpdateRequest({
      body: [
        body0
      ],
    });
    try {
      await client.checkDeviceUpdateWithOptions('OjpTuxxxxCkveZjo', 'dn_0xxxx200', checkDeviceUpdateRequest, checkDeviceUpdateHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
Client.main(process.argv.slice(2));
```

C#

```
using Newtonsoft.Json;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkaiot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkaiot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkaiot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateHeaders checkDeviceUpdateHeaders = new AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateHeaders();
            checkDeviceUpdateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateRequest.CheckDeviceUpdateRequestBody body0 = new AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateRequest.CheckDeviceUpdateRequestBody
            {
                ModuleName = "main",
                CurrentVersion = "1.2.0",
            };
            AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateRequest checkDeviceUpdateRequest = new AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateRequest
            {
                Body = new List<AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.CheckDeviceUpdateRequest.CheckDeviceUpdateRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.CheckDeviceUpdateWithOptions("OjpTuxxxxCkveZjo", "dn_0xxxx200", checkDeviceUpdateRequest, checkDeviceUpdateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| modules | Array | 模块信息。 |
| moduleName | String | 固件模块名。 |
| currentVersion | String | 识别到的设备当前版本，若没有版本则为空。 |
| criticalNext | String | 若存在必须逐级升级的关键版本链，表示下一跳版本，若没有则为空。 |
| latest | String | 当前设备可升级到的最新版本；无可用升级时为空。 |
| upgradeMode | String | 升级模式：   - **NOTIFY**：通知并等待确认 - **FORCE**：强制升级但仍需确认 - **SILENT**：静默升级、无需客户端确认 |
| noticeZh | String | 中文升级提示文案。 |
| noticeEn | String | 英文升级提示文案。 |
| fileUrl | String | 固件包下载地址。 |
| checksum | String | 固件包校验值。 |
| checksumAlgorithm | String | 校验算法，如 SHA256。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "modules" : [ {
    "moduleName" : "main",
    "currentVersion" : "1.2.0",
    "criticalNext" : "1.2.5",
    "latest" : "1.3.0",
    "upgradeMode" : "NOTIFY",
    "noticeZh" : "修复稳定性问题，建议升级。",
    "noticeEn" : "Stability fixes. Upgrade recommended.",
    "fileUrl" : "https://example.invalid/firmware/main-1.2.5.bin",
    "checksum" : "8f6cxxxd12a",
    "checksumAlgorithm" : "SHA256"
  } ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | The request parameter is invalid. | 参数错误 |
| 404 | firmware.notFound | The specified firmware does not exist. | 指定的固件不存在 |
| 500 | internalError | Internal server error. | 服务端内部错误 |
