---
title: "注册单个设备"
source_url: "https://open.dingtalk.com/document/development/industry-connection-single-device-registration"
namespace: "development"
slug: "industry-connection-single-device-registration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 行业连接 > 注册单个设备"
doc_id: "sejTVJMQ6C"
updated_at: "2025-09-08 19:05:11"
---

> Source: https://open.dingtalk.com/document/development/industry-connection-single-device-registration
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 行业连接 > 注册单个设备
> Updated: 2025-09-08 19:05:11

# 注册单个设备

调用本接口注册单个行业设备到钉钉开放平台。

> **[!NOTE]**
>
> 为提升接口的使用体验，行业链接相关接口正在升级，接口文档已**于2021年11月08日移动至历史文档（不推荐）目录**，后续重新上线时间请关注文档更新日志。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 制造业设备信息写权限 | 暂不支持 |
| 第三方企业应用 | 支持 | 制造业设备信息写权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 制造业设备信息写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/devicemng/devices HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "deviceKey" : "String",
  "deviceName" : "String",
  "departmentId" : Long,
  "managers" : "String",
  "collaborators" : "String",
  "description" : "String",
  "userId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| deviceKey | String | 是 | 设备标识。 |
| deviceName | String | 是 | 设备名称。 |
| departmentId | Long | 是 | 部门ID。 |
| managers | String | 否 | 管理员userid列表，多个userid之间使用英文逗号分隔。 |
| collaborators | String | 否 | 协助者userid列表，多个userid之间使用英文逗号分隔。 |
| description | String | 否 | 设备描述。 |
| userId | String | 是 | 创建者的userid。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | String | 注册是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/devicemng/devices HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxxxx
Content-Type:application/json

{
  "deviceKey" : "key_xxxxxxx",
  "deviceName" : "生产1组1号机",
  "departmentId" : 1,
  "managers" : "manager1,manager2",
  "collaborators" : "manager1,1000,10001",
  "description" : "生产组1号设备负责生产第一批产品",
  "userId" : "manager10"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdevicemng_1_0.*;
import com.aliyun.dingtalkdevicemng_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdevicemng_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdevicemng_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdevicemng_1_0.Client client = Sample.createClient();
        RegisterDeviceHeaders registerDeviceHeaders = new RegisterDeviceHeaders();
        registerDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        RegisterDeviceRequest registerDeviceRequest = new RegisterDeviceRequest()
                .setDeviceKey("key_xxxxxxx")
                .setDeviceName("生产1组1号机")
                .setDepartmentId(1L)
                .setManagers("manager1,manager2")
                .setCollaborators("manager1,1000,10001")
                .setDescription("生产组1号设备负责生产第一批产品")
                .setUserId("manager10");
        try {
            client.registerDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可��助开发定位问题
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

from alibabacloud_dingtalk.devicemng_1_0.client import Client as dingtalkdevicemng_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.devicemng_1_0 import models as dingtalkdevicemng__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdevicemng_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdevicemng_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_device_headers = dingtalkdevicemng__1__0_models.RegisterDeviceHeaders()
        register_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_device_request = dingtalkdevicemng__1__0_models.RegisterDeviceRequest(
            device_key='key_xxxxxxx',
            device_name='生产1组1号机',
            department_id=1,
            managers='manager1,manager2',
            collaborators='manager1,1000,10001',
            description='生产组1号设备负责生产第一批产品',
            user_id='manager10'
        )
        try:
            client.register_device_with_options(register_device_request, register_device_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        register_device_headers = dingtalkdevicemng__1__0_models.RegisterDeviceHeaders()
        register_device_headers.x_acs_dingtalk_access_token = '<your access token>'
        register_device_request = dingtalkdevicemng__1__0_models.RegisterDeviceRequest(
            device_key='key_xxxxxxx',
            device_name='生产1组1号机',
            department_id=1,
            managers='manager1,manager2',
            collaborators='manager1,1000,10001',
            description='生产组1号设备负责生产第一批产品',
            user_id='manager10'
        )
        try:
            await client.register_device_with_options_async(register_device_request, register_device_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterDeviceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\RegisterDeviceRequest;
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
        $registerDeviceHeaders = new RegisterDeviceHeaders([]);
        $registerDeviceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $registerDeviceRequest = new RegisterDeviceRequest([
            "deviceKey" => "key_xxxxxxx",
            "deviceName" => "生产1组1号机",
            "departmentId" => 1,
            "managers" => "manager1,manager2",
            "collaborators" => "manager1,1000,10001",
            "description" => "生产组1号设备负责生产第一批产品",
            "userId" => "manager10"
        ]);
        try {
            $client->registerDeviceWithOptions($registerDeviceRequest, $registerDeviceHeaders, new RuntimeOptions([]));
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
  dingtalkdevicemng_1_0  "github.com/alibabacloud-go/dingtalk/devicemng_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdevicemng_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdevicemng_1_0.Client{}
  _result, _err = dingtalkdevicemng_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  registerDeviceHeaders := &dingtalkdevicemng_1_0.RegisterDeviceHeaders{}
  registerDeviceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  registerDeviceRequest := &dingtalkdevicemng_1_0.RegisterDeviceRequest{
    DeviceKey: tea.String("key_xxxxxxx"),
    DeviceName: tea.String("生产1组1号机"),
    DepartmentId: tea.Int64(1),
    Managers: tea.String("manager1,manager2"),
    Collaborators: tea.String("manager1,1000,10001"),
    Description: tea.String("生产组1号设备负责生产第一批产品"),
    UserId: tea.String("manager10"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RegisterDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, &util.RuntimeOptions{})
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
import dingtalkdevicemng_1_0, * as $dingtalkdevicemng_1_0 from '@alicloud/dingtalk/devicemng_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdevicemng_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdevicemng_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let registerDeviceHeaders = new $dingtalkdevicemng_1_0.RegisterDeviceHeaders({ });
    registerDeviceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let registerDeviceRequest = new $dingtalkdevicemng_1_0.RegisterDeviceRequest({
      deviceKey: "key_xxxxxxx",
      deviceName: "生产1组1号机",
      departmentId: 1,
      managers: "manager1,manager2",
      collaborators: "manager1,1000,10001",
      description: "生产组1号设备负责生产第一批产品",
      userId: "manager10",
    });
    try {
      await client.registerDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterDeviceHeaders registerDeviceHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterDeviceHeaders();
            registerDeviceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterDeviceRequest registerDeviceRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.RegisterDeviceRequest
            {
                DeviceKey = "key_xxxxxxx",
                DeviceName = "生产1组1号机",
                DepartmentId = 1,
                Managers = "manager1,manager2",
                Collaborators = "manager1,1000,10001",
                Description = "生产组1号设备负责生产第一批产品",
                UserId = "manager10",
            };
            try
            {
                client.RegisterDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdevicemng__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdevicemng_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdevicemng_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::RegisterDeviceHeaders> registerDeviceHeaders = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::RegisterDeviceHeaders>();
  registerDeviceHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::RegisterDeviceRequest> registerDeviceRequest = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::RegisterDeviceRequest>(map<string, boost::any>({
    {"deviceKey", boost::any(string("key_xxxxxxx"))},
    {"deviceName", boost::any(string("生产1组1号机"))},
    {"departmentId", boost::any(1)},
    {"managers", boost::any(string("manager1,manager2"))},
    {"collaborators", boost::any(string("manager1,1000,10001"))},
    {"description", boost::any(string("生产组1号设备负责生产第一批产品"))},
    {"userId", boost::any(string("manager10"))}
  }));
  try {
    client->registerDeviceWithOptions(registerDeviceRequest, registerDeviceHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "result" : "success"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | deviceNumLimit | 设备数量达到上限 | 设备数量达到上限 |
| 400 | departmentNotExist | 部门不存在 | 部门不存在 |
| 400 | devicenameAlreadyExist | 设备名称已存在 | 设备名称已存在 |
| 400 | devicekeyAlreadyExist | 设备key已存在 | 设备key已存在 |
| 400 | deviceNotExist | 找不到设备 | 找不到设备 |
| 500 | systemError | 系统错误 | 系统错误 |
| 500 | installRobotFail | 机器人安装异常 | 机器人安装异常 |
| 500 | createRobotException | 机器人创建异常 | 机器人创建异常 |
| 500 | createRobotFail | 机器人创建失败 | 机器人创建失败 |
