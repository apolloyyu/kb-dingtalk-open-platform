---
title: "获取用户高管模式设置"
source_url: "https://open.dingtalk.com/document/development/get-user-executive-mode-settings"
namespace: "development"
slug: "get-user-executive-mode-settings"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 获取用户高管模式设置"
doc_id: "zjUVKU7Lly"
updated_at: "2026-06-01 15:25:05"
---

> Source: https://open.dingtalk.com/document/development/get-user-executive-mode-settings
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 获取用户高管模式设置
> Updated: 2026-06-01 15:25:05

# 获取用户高管模式设置

调用本接口获取用户高管模式设置。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/seniorSettings |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| seniorStaffId | String | 是 | 用户userId，可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获得userId。 |

### 请求示例

HTTP

```
GET /v1.0/contact/seniorSettings?seniorStaffId=1234567 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:afe8143b8xxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.ListSeniorSettingsHeaders listSeniorSettingsHeaders = new com.aliyun.dingtalkcontact_1_0.models.ListSeniorSettingsHeaders();
        listSeniorSettingsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.ListSeniorSettingsRequest listSeniorSettingsRequest = new com.aliyun.dingtalkcontact_1_0.models.ListSeniorSettingsRequest()
                .setSeniorStaffId("1234567");
        try {
            client.listSeniorSettingsWithOptions(listSeniorSettingsRequest, listSeniorSettingsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_senior_settings_headers = dingtalkcontact__1__0_models.ListSeniorSettingsHeaders()
        list_senior_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_senior_settings_request = dingtalkcontact__1__0_models.ListSeniorSettingsRequest(
            senior_staff_id='1234567'
        )
        try:
            client.list_senior_settings_with_options(list_senior_settings_request, list_senior_settings_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_senior_settings_headers = dingtalkcontact__1__0_models.ListSeniorSettingsHeaders()
        list_senior_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_senior_settings_request = dingtalkcontact__1__0_models.ListSeniorSettingsRequest(
            senior_staff_id='1234567'
        )
        try:
            await client.list_senior_settings_with_options_async(list_senior_settings_request, list_senior_settings_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListSeniorSettingsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListSeniorSettingsRequest;
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
        $listSeniorSettingsHeaders = new ListSeniorSettingsHeaders([]);
        $listSeniorSettingsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listSeniorSettingsRequest = new ListSeniorSettingsRequest([
            "seniorStaffId" => "1234567"
        ]);
        try {
            $client->listSeniorSettingsWithOptions($listSeniorSettingsRequest, $listSeniorSettingsHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listSeniorSettingsHeaders := &dingtalkcontact_1_0.ListSeniorSettingsHeaders{}
  listSeniorSettingsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listSeniorSettingsRequest := &dingtalkcontact_1_0.ListSeniorSettingsRequest{
    SeniorStaffId: tea.String("1234567"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListSeniorSettingsWithOptions(listSeniorSettingsRequest, listSeniorSettingsHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listSeniorSettingsHeaders = new $dingtalkcontact_1_0.ListSeniorSettingsHeaders({ });
    listSeniorSettingsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listSeniorSettingsRequest = new $dingtalkcontact_1_0.ListSeniorSettingsRequest({
      seniorStaffId: "1234567",
    });
    try {
      await client.listSeniorSettingsWithOptions(listSeniorSettingsRequest, listSeniorSettingsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListSeniorSettingsHeaders listSeniorSettingsHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListSeniorSettingsHeaders();
            listSeniorSettingsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListSeniorSettingsRequest listSeniorSettingsRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListSeniorSettingsRequest
            {
                SeniorStaffId = "1234567",
            };
            try
            {
                client.ListSeniorSettingsWithOptions(listSeniorSettingsRequest, listSeniorSettingsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| seniorStaffId | String | 用户userId。 |
| protectScenes | Array of String | 拦截场景列表。 |
| seniorWhiteList | Array | 高管白名单列表。 |
| id | String | 高管白名单对象ID，取值为：   - type=1：表示userId。 - type=2：表示部门deptId。 - type=3：表示角色roleId。 |
| type | Integer | 高管白名单类型，取值：   - **1**：表示为用户 - **2**：表示为部门 - **3**：表示为角色 |
| name | String | 高管白名单对象名称，取值为：   - type=1：表示员工名称。 - type=2：表示部门名称。 - type=3：表示角色名称。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "seniorStaffId" : "高管userId",
  "protectScenes" : [ "CHAT" ],
  "seniorWhiteList" : [ {
    "id" : "1234",
    "type" : 1,
    "name" : "测试角色"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 500 | parameter.userNotExists | 用户不存在 | 用户不存在 |
| 500 | parameter.orgNotExists | 组织不存在 | 组织不存在 |
| 500 | system.error | 获取设置出错 | 获取配置出错 |
