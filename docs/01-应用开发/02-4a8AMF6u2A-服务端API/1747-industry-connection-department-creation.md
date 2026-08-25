---
title: "创建部门"
source_url: "https://open.dingtalk.com/document/development/industry-connection-department-creation"
namespace: "development"
slug: "industry-connection-department-creation"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 行业连接 > 创建部门"
doc_id: "ljDR2uunI8"
updated_at: "2025-09-08 19:05:11"
---

> Source: https://open.dingtalk.com/document/development/industry-connection-department-creation
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 行业连接 > 创建部门
> Updated: 2025-09-08 19:05:11

# 创建部门

调用本接口为组织创建部门，部门会关联多个设备，实现对设备的管理。

> **[!NOTE]**
>
> 为提升接口的使用体验，行业链接相关接口正在升级，接口文档已**于2021年11月08日移动至历史文档（不推荐）目录**，后续重新上线时间请关注文档更新日志。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 暂不支持 | 制造业设备信息写权限 | 暂不支持 |
| 第三方企业应用 | 暂不支持 | 制造业设备信息写权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 制造业设备信息写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/devicemng/departments HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "departmentName" : "String",
  "departmentType" : "String",
  "systemUrl" : "String",
  "authType" : "String",
  "authInfo" : "String",
  "description" : "String",
  "bizExt" : "String",
  "userId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| departmentName | String | 是 | 部门名称。 |
| departmentType | String | 是 | 部门类型，取值：   - **Primary**：基础部门，可挂载设备上限为**100** - Middle：中等部门，可挂载设备上限为**300** - Advance：高级部门，可挂载设备上限为**1000** |
| systemUrl | String | 是 | 业务系统地址。 |
| authType | String | 是 | 认证方式，取值：   - **None**：免认证 - **Account**：账密方式 - **Code**：登录code方式 |
| authInfo | String | 是 | 认证信息。 |
| description | String | 是 | 部门描述。 |
| bizExt | String | 是 | 业务扩展。 |
| userId | String | 是 | 创建人userid。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | String | 创建是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/devicemng/departments HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "departmentName" : "生产1组",
  "departmentType" : "Primary",
  "systemUrl" : "https://xxx.xxx.com/manage",
  "authType" : "Acount",
  "authInfo" : "zhangsan/password",
  "description" : "生产1组负责中控机的组装",
  "bizExt" : "{\"workdate\":\"workday\"}",
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
        CreateDepartmentHeaders createDepartmentHeaders = new CreateDepartmentHeaders();
        createDepartmentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateDepartmentRequest createDepartmentRequest = new CreateDepartmentRequest()
                .setDepartmentName("生产1组")
                .setDepartmentType("Primary")
                .setSystemUrl("https://xxx.xxx.com/manage")
                .setAuthType("Acount")
                .setAuthInfo("zhangsan/password")
                .setDescription("生产1组负责中控机的组装")
                .setBizExt("{\"workdate\":\"workday\"}")
                .setUserId("manager10");
        try {
            client.createDepartmentWithOptions(createDepartmentRequest, createDepartmentHeaders, new RuntimeOptions());
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
        create_department_headers = dingtalkdevicemng__1__0_models.CreateDepartmentHeaders()
        create_department_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_department_request = dingtalkdevicemng__1__0_models.CreateDepartmentRequest(
            department_name='生产1组',
            department_type='Primary',
            system_url='https://xxx.xxx.com/manage',
            auth_type='Acount',
            auth_info='zhangsan/password',
            description='生产1组负责中控机的组装',
            biz_ext='{"workdate":"workday"}',
            user_id='manager10'
        )
        try:
            client.create_department_with_options(create_department_request, create_department_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_department_headers = dingtalkdevicemng__1__0_models.CreateDepartmentHeaders()
        create_department_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_department_request = dingtalkdevicemng__1__0_models.CreateDepartmentRequest(
            department_name='生产1组',
            department_type='Primary',
            system_url='https://xxx.xxx.com/manage',
            auth_type='Acount',
            auth_info='zhangsan/password',
            description='生产1组负责中控机的组装',
            biz_ext='{"workdate":"workday"}',
            user_id='manager10'
        )
        try:
            await client.create_department_with_options_async(create_department_request, create_department_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\CreateDepartmentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\CreateDepartmentRequest;
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
        $createDepartmentHeaders = new CreateDepartmentHeaders([]);
        $createDepartmentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createDepartmentRequest = new CreateDepartmentRequest([
            "departmentName" => "生产1组",
            "departmentType" => "Primary",
            "systemUrl" => "https://xxx.xxx.com/manage",
            "authType" => "Acount",
            "authInfo" => "zhangsan/password",
            "description" => "生产1组负责中控机的组装",
            "bizExt" => "{\"workdate\":\"workday\"}",
            "userId" => "manager10"
        ]);
        try {
            $client->createDepartmentWithOptions($createDepartmentRequest, $createDepartmentHeaders, new RuntimeOptions([]));
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

  createDepartmentHeaders := &dingtalkdevicemng_1_0.CreateDepartmentHeaders{}
  createDepartmentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createDepartmentRequest := &dingtalkdevicemng_1_0.CreateDepartmentRequest{
    DepartmentName: tea.String("生产1组"),
    DepartmentType: tea.String("Primary"),
    SystemUrl: tea.String("https://xxx.xxx.com/manage"),
    AuthType: tea.String("Acount"),
    AuthInfo: tea.String("zhangsan/password"),
    Description: tea.String("生产1组负责中控机的组装"),
    BizExt: tea.String("{\"workdate\":\"workday\"}"),
    UserId: tea.String("manager10"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateDepartmentWithOptions(createDepartmentRequest, createDepartmentHeaders, &util.RuntimeOptions{})
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
    let createDepartmentHeaders = new $dingtalkdevicemng_1_0.CreateDepartmentHeaders({ });
    createDepartmentHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createDepartmentRequest = new $dingtalkdevicemng_1_0.CreateDepartmentRequest({
      departmentName: "生产1组",
      departmentType: "Primary",
      systemUrl: "https://xxx.xxx.com/manage",
      authType: "Acount",
      authInfo: "zhangsan/password",
      description: "生产1组负责中控机的组装",
      bizExt: "{\"workdate\":\"workday\"}",
      userId: "manager10",
    });
    try {
      await client.createDepartmentWithOptions(createDepartmentRequest, createDepartmentHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.CreateDepartmentHeaders createDepartmentHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.CreateDepartmentHeaders();
            createDepartmentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.CreateDepartmentRequest createDepartmentRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.CreateDepartmentRequest
            {
                DepartmentName = "生产1组",
                DepartmentType = "Primary",
                SystemUrl = "https://xxx.xxx.com/manage",
                AuthType = "Acount",
                AuthInfo = "zhangsan/password",
                Description = "生产1组负责中控机的组装",
                BizExt = "{\"workdate\":\"workday\"}",
                UserId = "manager10",
            };
            try
            {
                client.CreateDepartmentWithOptions(createDepartmentRequest, createDepartmentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::CreateDepartmentHeaders> createDepartmentHeaders = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::CreateDepartmentHeaders>();
  createDepartmentHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdevicemng_1_0::CreateDepartmentRequest> createDepartmentRequest = make_shared<Alibabacloud_Dingtalkdevicemng_1_0::CreateDepartmentRequest>(map<string, boost::any>({
    {"departmentName", boost::any(string("生产1组"))},
    {"departmentType", boost::any(string("Primary"))},
    {"systemUrl", boost::any(string("https://xxx.xxx.com/manage"))},
    {"authType", boost::any(string("Acount"))},
    {"authInfo", boost::any(string("zhangsan/password"))},
    {"description", boost::any(string("生产1组负责中控机的组装"))},
    {"bizExt", boost::any(string("{"workdate":"workday"}"))},
    {"userId", boost::any(string("manager10"))}
  }));
  try {
    client->createDepartmentWithOptions(createDepartmentRequest, createDepartmentHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| 400 | departmentTypeError | 部门类型不对 | 部门类型不对 |
| 400 | departmentAlreadyExist | 部门已存在 | 部门已存在 |
| 500 | systemError | 系统异常 | 系统异常 |
