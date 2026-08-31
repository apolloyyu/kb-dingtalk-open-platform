---
title: "查询考勤写操作权限"
source_url: "https://open.dingtalk.com/document/development/attendance-writing-operation-is-brand-new-query"
namespace: "development"
slug: "attendance-writing-operation-is-brand-new-query"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 查询考勤写操作权限"
doc_id: "AA3xzxgBGF"
updated_at: "2026-06-01 16:41:46"
---

> Source: https://open.dingtalk.com/document/development/attendance-writing-operation-is-brand-new-query
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 查询考勤写操作权限
> Updated: 2026-06-01 16:41:46

# 查询考勤写操作权限

调用本接口，查询企业员工在考勤组内的操作权限。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/writePermissions/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Attendance.Permission.Read-考勤授权信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUserId | String | 是 | 员工userId。 |
| category | String | 是 | 资源类型：   - **GROUP**：考勤组，目前仅支持该值。 |
| resourceKey | String | 是 | 权限点：   - **GROUP\_MEMBER**：设置参与考勤人员 - **GROUP\_NAME**：修改考勤组名称 - **GROUP\_TYPE**：设置考勤组类型 - **CHECK\_TIME**：设置考勤时间 - **SCHEDULE**：员工排班 - **CHECK\_POSITION\_TYPE**：设置打卡方式 - **OVER\_TIME\_RULE**：设置加班规则 - **CAMERA\_CHECK**：拍照验证规则 - **OUT\_SIDE\_CHECK**：设置外勤打卡 - **MANAGE**：考勤组子负责人 - **OWNER**：考勤组主负责人 - **DELETE\_GROUP**：删除考勤组 |
| entityIds | Array of Long | 是 | 资源ID，如果category参数值为GROUP，该参数值传考勤组ID，可通过[获取用户考勤组](0180-queries-a-user-attendance-group.md)接口获取group\_id参数值。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/writePermissions/query?corpId=ding09ccd4b45301e86xxxx3d9884 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json

{
  "opUserId" : "050728xxx921",
  "category" : "GROUP",
  "resourceKey" : "SCHEDULE",
  "entityIds" : [ 1 ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkattendance_1_0.*;
import com.aliyun.dingtalkattendance_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        CheckWritePermissionHeaders checkWritePermissionHeaders = new CheckWritePermissionHeaders();
        checkWritePermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CheckWritePermissionRequest checkWritePermissionRequest = new CheckWritePermissionRequest()
                .setOpUserId("050728xxx921")
                .setCategory("GROUP")
                .setResourceKey("SCHEDULE")
                .setEntityIds(java.util.Arrays.asList(
                    1L
                ));
        try {
            client.checkWritePermissionWithOptions(checkWritePermissionRequest, checkWritePermissionHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.attendance_1_0.client import Client as dingtalkattendance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.attendance_1_0 import models as dingtalkattendance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkattendance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkattendance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_write_permission_headers = dingtalkattendance__1__0_models.CheckWritePermissionHeaders()
        check_write_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        check_write_permission_request = dingtalkattendance__1__0_models.CheckWritePermissionRequest(
            op_user_id='050728xxx921',
            category='GROUP',
            resource_key='SCHEDULE',
            entity_ids=[
                1
            ]
        )
        try:
            client.check_write_permission_with_options(check_write_permission_request, check_write_permission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        check_write_permission_headers = dingtalkattendance__1__0_models.CheckWritePermissionHeaders()
        check_write_permission_headers.x_acs_dingtalk_access_token = '<your access token>'
        check_write_permission_request = dingtalkattendance__1__0_models.CheckWritePermissionRequest(
            op_user_id='050728xxx921',
            category='GROUP',
            resource_key='SCHEDULE',
            entity_ids=[
                1
            ]
        )
        try:
            await client.check_write_permission_with_options_async(check_write_permission_request, check_write_permission_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CheckWritePermissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\CheckWritePermissionRequest;
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
        $checkWritePermissionHeaders = new CheckWritePermissionHeaders([]);
        $checkWritePermissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $checkWritePermissionRequest = new CheckWritePermissionRequest([
            "opUserId" => "050728xxx921",
            "category" => "GROUP",
            "resourceKey" => "SCHEDULE",
            "entityIds" => [
                1
            ]
        ]);
        try {
            $client->checkWritePermissionWithOptions($checkWritePermissionRequest, $checkWritePermissionHeaders, new RuntimeOptions([]));
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
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkattendance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkattendance_1_0.Client{}
  _result, _err = dingtalkattendance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  checkWritePermissionHeaders := &dingtalkattendance_1_0.CheckWritePermissionHeaders{}
  checkWritePermissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  checkWritePermissionRequest := &dingtalkattendance_1_0.CheckWritePermissionRequest{
    OpUserId: tea.String("050728xxx921"),
    Category: tea.String("GROUP"),
    ResourceKey: tea.String("SCHEDULE"),
    EntityIds: []*int64{tea.Int(1)},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CheckWritePermissionWithOptions(checkWritePermissionRequest, checkWritePermissionHeaders, &util.RuntimeOptions{})
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
import dingtalkattendance_1_0, * as $dingtalkattendance_1_0 from '@alicloud/dingtalk/attendance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkattendance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkattendance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let checkWritePermissionHeaders = new $dingtalkattendance_1_0.CheckWritePermissionHeaders({ });
    checkWritePermissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let checkWritePermissionRequest = new $dingtalkattendance_1_0.CheckWritePermissionRequest({
      opUserId: "050728xxx921",
      category: "GROUP",
      resourceKey: "SCHEDULE",
      entityIds: [
        1
      ],
    });
    try {
      await client.checkWritePermissionWithOptions(checkWritePermissionRequest, checkWritePermissionHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkattendance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkattendance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckWritePermissionHeaders checkWritePermissionHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckWritePermissionHeaders();
            checkWritePermissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckWritePermissionRequest checkWritePermissionRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.CheckWritePermissionRequest
            {
                OpUserId = "050728xxx921",
                Category = "GROUP",
                ResourceKey = "SCHEDULE",
                EntityIds = new List<long?>
                {
                    1
                },
            };
            try
            {
                client.CheckWritePermissionWithOptions(checkWritePermissionRequest, checkWritePermissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkattendance__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkattendance_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkattendance_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::Client> client = make_shared<Alibabacloud_Dingtalkattendance_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::CheckWritePermissionHeaders> checkWritePermissionHeaders = make_shared<Alibabacloud_Dingtalkattendance_1_0::CheckWritePermissionHeaders>();
  checkWritePermissionHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkattendance_1_0::CheckWritePermissionRequest> checkWritePermissionRequest = make_shared<Alibabacloud_Dingtalkattendance_1_0::CheckWritePermissionRequest>(map<string, boost::any>({
    {"opUserId", boost::any(string("050728xxx921"))},
    {"category", boost::any(string("GROUP"))},
    {"resourceKey", boost::any(string("SCHEDULE"))},
    {"entityIds", boost::any(vector<long>({
      1
    }))}
  }));
  try {
    client->checkWritePermissionWithOptions(checkWritePermissionRequest, checkWritePermissionHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| entityPermissionMap | Map<String, Boolean> | 权限结果。  返回示例：{"entityPermissionMap":{"key":value}}。   - key，指资源ID，即请求参数entityIds的值。 - value，指是否有权限。    - true：有权限。   - false：无权限。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "entityPermissionMap" : {
    "key" : true
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.invalid | PARAMETER\_INVALID | 参数异常 |
| 500 | system.error | SYSTEM\_ERROR | 系统异常 |
