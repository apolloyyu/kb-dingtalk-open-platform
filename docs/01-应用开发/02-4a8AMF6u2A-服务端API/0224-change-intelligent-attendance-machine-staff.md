---
title: "变更智能考勤机员工"
source_url: "https://open.dingtalk.com/document/development/change-intelligent-attendance-machine-staff"
namespace: "development"
slug: "change-intelligent-attendance-machine-staff"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤机管理 > 变更智能考勤机员工"
doc_id: "lgUVvNL13m"
updated_at: "2026-06-01 16:50:45"
---

> Source: https://open.dingtalk.com/document/development/change-intelligent-attendance-machine-staff
> Path: 应用开发 / 服务端API / 考勤 > 考勤机管理 > 变更智能考勤机员工
> Updated: 2026-06-01 16:50:45

# 变更智能考勤机员工

调用本接口，可变更智能考勤机员工，包括新增或删除部门、新增或删除员工。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/smartDevice/atmachines/users |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_dingtalk\_attendance\_manage-钉钉考勤机人员管理 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| delUserIds | Array of String | 否 | 移除的员工userId列表，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| deviceIds | Array of String | 否 | 加密后的考勤机设备ID列表，字符串数组，可调用[查询考勤机信息](0223-query-attendance-machine-information.md)接口获取deviceId参数值。 |
| addUserIds | Array of String | 否 | 新增的员工userId列表，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| devIds | Array of Long | 否 | 考勤机设备ID列表，Long数组，可调用[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取device\_id参数值。 |
| delDeptIds | Array of Long | 否 | 删除的部门id列表，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |
| addDeptIds | Array of Long | 否 | 新增的部门id列表，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |

### 请求示例

HTTP

```
PUT /v1.0/smartDevice/atmachines/users HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token
Content-Type:application/json

{
  "delUserIds" : [ "user01" ],
  "deviceIds" : [ "GWIl/hopqUhkNQuL6e+Lpuxxx" ],
  "addUserIds" : [ "user02" ],
  "devIds" : [ 10011111 ],
  "delDeptIds" : [ 111 ],
  "addDeptIds" : [ 222 ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalksmart_device_1_0.*;
import com.aliyun.dingtalksmart_device_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalksmart_device_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalksmart_device_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalksmart_device_1_0.Client client = Sample.createClient();
        MachineUsersUpdateHeaders machineUsersUpdateHeaders = new MachineUsersUpdateHeaders();
        machineUsersUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        MachineUsersUpdateRequest machineUsersUpdateRequest = new MachineUsersUpdateRequest()
                .setDelUserIds(java.util.Arrays.asList(
                    "user01"
                ))
                .setDeviceIds(java.util.Arrays.asList(
                    "GWIl/hopqUhkNQuL6e+Lpuxxx"
                ))
                .setAddUserIds(java.util.Arrays.asList(
                    "user02"
                ))
                .setDevIds(java.util.Arrays.asList(
                    10011111L
                ))
                .setDelDeptIds(java.util.Arrays.asList(
                    111L
                ))
                .setAddDeptIds(java.util.Arrays.asList(
                    222L
                ));
        try {
            client.machineUsersUpdateWithOptions(machineUsersUpdateRequest, machineUsersUpdateHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.smartDevice_1_0.client import Client as dingtalksmartDevice_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.smartDevice_1_0 import models as dingtalksmart_device__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalksmartDevice_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalksmartDevice_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        machine_users_update_headers = dingtalksmart_device__1__0_models.MachineUsersUpdateHeaders()
        machine_users_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        machine_users_update_request = dingtalksmart_device__1__0_models.MachineUsersUpdateRequest(
            del_user_ids=[
                'user01'
            ],
            device_ids=[
                'GWIl/hopqUhkNQuL6e+Lpuxxx'
            ],
            add_user_ids=[
                'user02'
            ],
            dev_ids=[
                10011111
            ],
            del_dept_ids=[
                111
            ],
            add_dept_ids=[
                222
            ]
        )
        try:
            client.machine_users_update_with_options(machine_users_update_request, machine_users_update_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        machine_users_update_headers = dingtalksmart_device__1__0_models.MachineUsersUpdateHeaders()
        machine_users_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        machine_users_update_request = dingtalksmart_device__1__0_models.MachineUsersUpdateRequest(
            del_user_ids=[
                'user01'
            ],
            device_ids=[
                'GWIl/hopqUhkNQuL6e+Lpuxxx'
            ],
            add_user_ids=[
                'user02'
            ],
            dev_ids=[
                10011111
            ],
            del_dept_ids=[
                111
            ],
            add_dept_ids=[
                222
            ]
        )
        try:
            await client.machine_users_update_with_options_async(machine_users_update_request, machine_users_update_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vsmart_device_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vsmart_device_1_0\Models\MachineUsersUpdateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vsmart_device_1_0\Models\MachineUsersUpdateRequest;
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
        $machineUsersUpdateHeaders = new MachineUsersUpdateHeaders([]);
        $machineUsersUpdateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $machineUsersUpdateRequest = new MachineUsersUpdateRequest([
            "delUserIds" => [
                "user01"
            ],
            "deviceIds" => [
                "GWIl/hopqUhkNQuL6e+Lpuxxx"
            ],
            "addUserIds" => [
                "user02"
            ],
            "devIds" => [
                10011111
            ],
            "delDeptIds" => [
                111
            ],
            "addDeptIds" => [
                222
            ]
        ]);
        try {
            $client->machineUsersUpdateWithOptions($machineUsersUpdateRequest, $machineUsersUpdateHeaders, new RuntimeOptions([]));
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
  dingtalksmartdevice_1_0  "github.com/alibabacloud-go/dingtalk/smartDevice_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalksmartdevice_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalksmartdevice_1_0.Client{}
  _result, _err = dingtalksmartdevice_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  machineUsersUpdateHeaders := &dingtalksmartdevice_1_0.MachineUsersUpdateHeaders{}
  machineUsersUpdateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  machineUsersUpdateRequest := &dingtalksmartdevice_1_0.MachineUsersUpdateRequest{
    DelUserIds: []*string{tea.String("user01")},
    DeviceIds: []*string{tea.String("GWIl/hopqUhkNQuL6e+Lpuxxx")},
    AddUserIds: []*string{tea.String("user02")},
    DevIds: []*int64{tea.Int(10011111)},
    DelDeptIds: []*int64{tea.Int(111)},
    AddDeptIds: []*int64{tea.Int(222)},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.MachineUsersUpdateWithOptions(machineUsersUpdateRequest, machineUsersUpdateHeaders, &util.RuntimeOptions{})
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
import dingtalksmartDevice_1_0, * as $dingtalksmartDevice_1_0 from '@alicloud/dingtalk/smartDevice_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalksmartDevice_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalksmartDevice_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let machineUsersUpdateHeaders = new $dingtalksmartDevice_1_0.MachineUsersUpdateHeaders({ });
    machineUsersUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let machineUsersUpdateRequest = new $dingtalksmartDevice_1_0.MachineUsersUpdateRequest({
      delUserIds: [
        "user01"
      ],
      deviceIds: [
        "GWIl/hopqUhkNQuL6e+Lpuxxx"
      ],
      addUserIds: [
        "user02"
      ],
      devIds: [
        10011111
      ],
      delDeptIds: [
        111
      ],
      addDeptIds: [
        222
      ],
    });
    try {
      await client.machineUsersUpdateWithOptions(machineUsersUpdateRequest, machineUsersUpdateHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalksmart_device_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalksmart_device_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalksmart_device_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalksmart_device_1_0.Models.MachineUsersUpdateHeaders machineUsersUpdateHeaders = new AlibabaCloud.SDK.Dingtalksmart_device_1_0.Models.MachineUsersUpdateHeaders();
            machineUsersUpdateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalksmart_device_1_0.Models.MachineUsersUpdateRequest machineUsersUpdateRequest = new AlibabaCloud.SDK.Dingtalksmart_device_1_0.Models.MachineUsersUpdateRequest
            {
                DelUserIds = new List<string>
                {
                    "user01"
                },
                DeviceIds = new List<string>
                {
                    "GWIl/hopqUhkNQuL6e+Lpuxxx"
                },
                AddUserIds = new List<string>
                {
                    "user02"
                },
                DevIds = new List<long?>
                {
                    10011111
                },
                DelDeptIds = new List<long?>
                {
                    111
                },
                AddDeptIds = new List<long?>
                {
                    222
                },
            };
            try
            {
                client.MachineUsersUpdateWithOptions(machineUsersUpdateRequest, machineUsersUpdateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalksmart_device__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalksmart_device_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalksmart_device_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalksmart_device_1_0::Client> client = make_shared<Alibabacloud_Dingtalksmart_device_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalksmart_device_1_0::MachineUsersUpdateHeaders> machineUsersUpdateHeaders = make_shared<Alibabacloud_Dingtalksmart_device_1_0::MachineUsersUpdateHeaders>();
  machineUsersUpdateHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalksmart_device_1_0::MachineUsersUpdateRequest> machineUsersUpdateRequest = make_shared<Alibabacloud_Dingtalksmart_device_1_0::MachineUsersUpdateRequest>(map<string, boost::any>({
    {"delUserIds", boost::any(vector<string>({
      "user01"
    }))},
    {"deviceIds", boost::any(vector<string>({
      "GWIl/hopqUhkNQuL6e+Lpuxxx"
    }))},
    {"addUserIds", boost::any(vector<string>({
      "user02"
    }))},
    {"devIds", boost::any(vector<long>({
      10011111
    }))},
    {"delDeptIds", boost::any(vector<long>({
      111
    }))},
    {"addDeptIds", boost::any(vector<long>({
      222
    }))}
  }));
  try {
    client->machineUsersUpdateWithOptions(machineUsersUpdateRequest, machineUsersUpdateHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | systemError | 系统错误，请稍后重试 | 系统错误，请稍后重试 |
| 400 | paramIllegal | 参数错误 | 参数错误 |
| 400 | noAuthority | 未授权 | 未授权 |
| 400 | userNotInOrg | 用户不在此组织中 | 用户不在此组织中 |
| 400 | deviceNotExist | 设备不存在 | 设备不存在 |
| 500 | unknownError | 未知错误 | 未知错误 |
