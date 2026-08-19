---
title: "更新设备绑定关系"
source_url: "https://open.dingtalk.com/document/development/api-updatedevicebinding"
namespace: "development"
slug: "api-updatedevicebinding"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 视听智能服务 > 更新设备绑定关系"
doc_id: "eKUSFjGFoY"
updated_at: "2026-06-24 13:44:36"
---

> Source: https://open.dingtalk.com/document/development/api-updatedevicebinding
> Path: 应用开发 / 服务端API / 更多开放 > 视听智能服务 > 更新设备绑定关系
> Updated: 2026-06-24 13:44:36

# 更新设备绑定关系

通过本接口，更新AI销售管理中硬件设备与使用人之间的绑定关系。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/devices/binding/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Sale.Device.Write-钉钉AI销售管理智能硬件操作权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户userId。 |
| sn | String | 是 | 设备SN编号。 |
| action | String | 是 | 操作类型：   - **bind**：绑定设备到指定的员工 - **unbind**：解绑设备 |
| teamCode | String | 是 | 团队编码。  **[!NOTE]**   - 绑定场景下，必填参数 - 解绑场景下，可选 （如果一个员工身上绑定了多块设备时必选参数） |

### **请求示例**

HTTP

```
POST /v1.0/dvi/devices/binding/update HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a4d6xxxx5fdb71f0
Content-Type:application/json

{
  "userId" : "01123448786924",
  "sn" : "T-69Axxxx1F",
  "action" : "bind",
  "teamCode" : "7e68xxxx98f731"
}
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
    public static com.aliyun.dingtalkdvi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdvi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdvi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdvi_1_0.models.UpdateDeviceBindingHeaders updateDeviceBindingHeaders = new com.aliyun.dingtalkdvi_1_0.models.UpdateDeviceBindingHeaders();
        updateDeviceBindingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.UpdateDeviceBindingRequest updateDeviceBindingRequest = new com.aliyun.dingtalkdvi_1_0.models.UpdateDeviceBindingRequest()
                .setUserId("01123448786924")
                .setSn("T-69Axxxx1F")
                .setAction("bind")
                .setTeamCode("7e68xxxx98f731");
        try {
            client.updateDeviceBindingWithOptions(updateDeviceBindingRequest, updateDeviceBindingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.dvi_1_0.client import Client as dingtalkdvi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dvi_1_0 import models as dingtalkdvi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdvi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdvi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_device_binding_headers = dingtalkdvi__1__0_models.UpdateDeviceBindingHeaders()
        update_device_binding_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_device_binding_request = dingtalkdvi__1__0_models.UpdateDeviceBindingRequest(
            user_id='01123448786924',
            sn='T-69Axxxx1F',
            action='bind',
            team_code='7e68xxxx98f731'
        )
        try:
            client.update_device_binding_with_options(update_device_binding_request, update_device_binding_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_device_binding_headers = dingtalkdvi__1__0_models.UpdateDeviceBindingHeaders()
        update_device_binding_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_device_binding_request = dingtalkdvi__1__0_models.UpdateDeviceBindingRequest(
            user_id='01123448786924',
            sn='T-69Axxxx1F',
            action='bind',
            team_code='7e68xxxx98f731'
        )
        try:
            await client.update_device_binding_with_options_async(update_device_binding_request, update_device_binding_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\UpdateDeviceBindingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\UpdateDeviceBindingRequest;
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
        $updateDeviceBindingHeaders = new UpdateDeviceBindingHeaders([]);
        $updateDeviceBindingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateDeviceBindingRequest = new UpdateDeviceBindingRequest([
            "userId" => "01123448786924",
            "sn" => "T-69Axxxx1F",
            "action" => "bind",
            "teamCode" => "7e68xxxx98f731"
        ]);
        try {
            $client->updateDeviceBindingWithOptions($updateDeviceBindingRequest, $updateDeviceBindingHeaders, new RuntimeOptions([]));
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
  dingtalkdvi_1_0  "github.com/alibabacloud-go/dingtalk/dvi_1_0"
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
func CreateClient () (_result *dingtalkdvi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdvi_1_0.Client{}
  _result, _err = dingtalkdvi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateDeviceBindingHeaders := &dingtalkdvi_1_0.UpdateDeviceBindingHeaders{}
  updateDeviceBindingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateDeviceBindingRequest := &dingtalkdvi_1_0.UpdateDeviceBindingRequest{
    UserId: tea.String("01123448786924"),
    Sn: tea.String("T-69Axxxx1F"),
    Action: tea.String("bind"),
    TeamCode: tea.String("7e68xxxx98f731"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateDeviceBindingWithOptions(updateDeviceBindingRequest, updateDeviceBindingHeaders, &util.RuntimeOptions{})
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
const dingtalkdvi_1_0 = require('@alicloud/dingtalk/dvi_1_0');
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
    return new dingtalkdvi_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateDeviceBindingHeaders = new dingtalkdvi_1_0.UpdateDeviceBindingHeaders({ });
    updateDeviceBindingHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateDeviceBindingRequest = new dingtalkdvi_1_0.UpdateDeviceBindingRequest({
      userId: '01123448786924',
      sn: 'T-69Axxxx1F',
      action: 'bind',
      teamCode: '7e68xxxx98f731',
    });
    try {
      await client.updateDeviceBindingWithOptions(updateDeviceBindingRequest, updateDeviceBindingHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdvi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdvi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateDeviceBindingHeaders updateDeviceBindingHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateDeviceBindingHeaders();
            updateDeviceBindingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateDeviceBindingRequest updateDeviceBindingRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateDeviceBindingRequest
            {
                UserId = "01123448786924",
                Sn = "T-69Axxxx1F",
                Action = "bind",
                TeamCode = "7e68xxxx98f731",
            };
            try
            {
                client.UpdateDeviceBindingWithOptions(updateDeviceBindingRequest, updateDeviceBindingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 绑定、解绑结果：   - **true**：成功 - **false**：失败 |

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
| 400 | request.too.fast | request too fast. | 请求过快被限流。 |
| 400 | illegalRequest | Illegal request. | 请求异常。 |
| 400 | request.permission.denied | api permission denied. | 暂无调用权限 |
| 500 | systemError | system error. | 系统异常。 |
