---
title: "确认执行设备固件升级"
source_url: "https://open.dingtalk.com/document/development/api-confirmfirmwareupgrade"
namespace: "development"
slug: "api-confirmfirmwareupgrade"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 智能硬件 > AIoT 平台 > 确认执行设备固件升级"
doc_id: "3M33DU5iZE"
updated_at: "2026-07-15 17:05:03"
---

> Source: https://open.dingtalk.com/document/development/api-confirmfirmwareupgrade
> Path: 应用开发 / 服务端API / 更多开放 > 智能硬件 > AIoT 平台 > 确认执行设备固件升级
> Updated: 2026-07-15 17:05:03

# 确认执行设备固件升级

调用本接口，确认执行设备固件升级。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/aiot/products/{productKey}/devices/{deviceName}/firmware/confirmUpgrade |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Device.AIoT.Write-AIoT平台操作设备权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| productKey | String | 是 | 产品Key。 |
| deviceName | String | 是 | 设备名称。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| moduleName | String | 否 | 模块名字。 |

### **请求示例**

HTTP

```
POST /v1.0/aiot/products/OjpTxxxxveZjo/devices/dn_xxxx0200/firmware/confirmUpgrade?moduleName=main HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e41e9xxxxcbbc
Content-Type:application/json
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
        com.aliyun.dingtalkaiot_1_0.models.ConfirmFirmwareUpgradeHeaders confirmFirmwareUpgradeHeaders = new com.aliyun.dingtalkaiot_1_0.models.ConfirmFirmwareUpgradeHeaders();
        confirmFirmwareUpgradeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkaiot_1_0.models.ConfirmFirmwareUpgradeRequest confirmFirmwareUpgradeRequest = new com.aliyun.dingtalkaiot_1_0.models.ConfirmFirmwareUpgradeRequest()
                .setModuleName("main");
        try {
            client.confirmFirmwareUpgradeWithOptions("OjpTxxxxveZjo", "dn_xxxx0200", confirmFirmwareUpgradeRequest, confirmFirmwareUpgradeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        confirm_firmware_upgrade_headers = dingtalkaiot__1__0_models.ConfirmFirmwareUpgradeHeaders()
        confirm_firmware_upgrade_headers.x_acs_dingtalk_access_token = '<your access token>'
        confirm_firmware_upgrade_request = dingtalkaiot__1__0_models.ConfirmFirmwareUpgradeRequest(
            module_name='main'
        )
        try:
            client.confirm_firmware_upgrade_with_options('OjpTxxxxveZjo', 'dn_xxxx0200', confirm_firmware_upgrade_request, confirm_firmware_upgrade_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        confirm_firmware_upgrade_headers = dingtalkaiot__1__0_models.ConfirmFirmwareUpgradeHeaders()
        confirm_firmware_upgrade_headers.x_acs_dingtalk_access_token = '<your access token>'
        confirm_firmware_upgrade_request = dingtalkaiot__1__0_models.ConfirmFirmwareUpgradeRequest(
            module_name='main'
        )
        try:
            await client.confirm_firmware_upgrade_with_options_async('OjpTxxxxveZjo', 'dn_xxxx0200', confirm_firmware_upgrade_request, confirm_firmware_upgrade_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vaiot_1_0\Models\ConfirmFirmwareUpgradeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vaiot_1_0\Models\ConfirmFirmwareUpgradeRequest;
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
        $confirmFirmwareUpgradeHeaders = new ConfirmFirmwareUpgradeHeaders([]);
        $confirmFirmwareUpgradeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $confirmFirmwareUpgradeRequest = new ConfirmFirmwareUpgradeRequest([
            "moduleName" => "main"
        ]);
        try {
            $client->confirmFirmwareUpgradeWithOptions("OjpTxxxxveZjo", "dn_xxxx0200", $confirmFirmwareUpgradeRequest, $confirmFirmwareUpgradeHeaders, new RuntimeOptions([]));
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

  confirmFirmwareUpgradeHeaders := &dingtalkaiot_1_0.ConfirmFirmwareUpgradeHeaders{}
  confirmFirmwareUpgradeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  confirmFirmwareUpgradeRequest := &dingtalkaiot_1_0.ConfirmFirmwareUpgradeRequest{
    ModuleName: tea.String("main"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ConfirmFirmwareUpgradeWithOptions(tea.String("OjpTxxxxveZjo"), tea.String("dn_xxxx0200"), confirmFirmwareUpgradeRequest, confirmFirmwareUpgradeHeaders, &util.RuntimeOptions{})
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
    let confirmFirmwareUpgradeHeaders = new dingtalkaiot_1_0.ConfirmFirmwareUpgradeHeaders({ });
    confirmFirmwareUpgradeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let confirmFirmwareUpgradeRequest = new dingtalkaiot_1_0.ConfirmFirmwareUpgradeRequest({
      moduleName: 'main',
    });
    try {
      await client.confirmFirmwareUpgradeWithOptions('OjpTxxxxveZjo', 'dn_xxxx0200', confirmFirmwareUpgradeRequest, confirmFirmwareUpgradeHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.ConfirmFirmwareUpgradeHeaders confirmFirmwareUpgradeHeaders = new AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.ConfirmFirmwareUpgradeHeaders();
            confirmFirmwareUpgradeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.ConfirmFirmwareUpgradeRequest confirmFirmwareUpgradeRequest = new AlibabaCloud.SDK.Dingtalkaiot_1_0.Models.ConfirmFirmwareUpgradeRequest
            {
                ModuleName = "main",
            };
            try
            {
                client.ConfirmFirmwareUpgradeWithOptions("OjpTxxxxveZjo", "dn_xxxx0200", confirmFirmwareUpgradeRequest, confirmFirmwareUpgradeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 执行结果。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | The request parameter is invalid. | 参数错误 |
| 400 | upgrade.confirmNotSupported | The underlying platform does not support upgrade confirmation. | 不支持的升级确认 |
| 404 | device.notFound | The specified device does not exist. | 指定的设备不存在 |
| 404 | firmware.notFound | The specified firmware does not exist. | 指定的固件不存在 |
| 409 | upgrade.notAwaitingConfirm | The device is not awaiting upgrade confirmation. | 设备没有待确认的升级 |
| 409 | upgrade.confirmRejected | The upgrade confirmation was rejected by the underlying platform. | 升级拒绝 |
| 500 | internalError | Internal server error. | 服务端内部错误 |
