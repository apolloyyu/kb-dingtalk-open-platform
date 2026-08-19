---
title: "创建项目组"
source_url: "https://open.dingtalk.com/document/development/create-a-project-group"
namespace: "development"
slug: "create-a-project-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 地产行业 > 创建项目组"
doc_id: "aSHxP5HFwp"
updated_at: "2025-09-23 19:22:14"
---

> Source: https://open.dingtalk.com/document/development/create-a-project-group
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 地产行业 > 创建项目组
> Updated: 2025-09-23 19:22:14

# 创建项目组

调用本接口，创建一个项目组。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/industry/campuses/projects/groups |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Industry.Campus.Write-行业化园区管理写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 项目组名称。 |
| extend | String | 否 | 扩展信息。      该参数值自定义传入，例如:`{\"level\":3}`。 |

### 请求示例

HTTP

```
POST /v1.0/industry/campuses/projects/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "name" : "测试项目组",
  "extend" : "扩展信息"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkindustry_1_0.*;
import com.aliyun.dingtalkindustry_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkindustry_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkindustry_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkindustry_1_0.Client client = Sample.createClient();
        CampusCreateCampusGroupHeaders campusCreateCampusGroupHeaders = new CampusCreateCampusGroupHeaders();
        campusCreateCampusGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CampusCreateCampusGroupRequest campusCreateCampusGroupRequest = new CampusCreateCampusGroupRequest()
                .setName("测试项目组")
                .setExtend("扩展信息");
        try {
            client.campusCreateCampusGroupWithOptions(campusCreateCampusGroupRequest, campusCreateCampusGroupHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.industry_1_0.client import Client as dingtalkindustry_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.industry_1_0 import models as dingtalkindustry__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkindustry_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkindustry_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        campus_create_campus_group_headers = dingtalkindustry__1__0_models.CampusCreateCampusGroupHeaders()
        campus_create_campus_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        campus_create_campus_group_request = dingtalkindustry__1__0_models.CampusCreateCampusGroupRequest(
            name='测试项目组',
            extend='扩展信息'
        )
        try:
            client.campus_create_campus_group_with_options(campus_create_campus_group_request, campus_create_campus_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        campus_create_campus_group_headers = dingtalkindustry__1__0_models.CampusCreateCampusGroupHeaders()
        campus_create_campus_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        campus_create_campus_group_request = dingtalkindustry__1__0_models.CampusCreateCampusGroupRequest(
            name='测试项目组',
            extend='扩展信息'
        )
        try:
            await client.campus_create_campus_group_with_options_async(campus_create_campus_group_request, campus_create_campus_group_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Models\CampusCreateCampusGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Models\CampusCreateCampusGroupRequest;
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
        $campusCreateCampusGroupHeaders = new CampusCreateCampusGroupHeaders([]);
        $campusCreateCampusGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $campusCreateCampusGroupRequest = new CampusCreateCampusGroupRequest([
            "name" => "测试项目组",
            "extend" => "扩展信息"
        ]);
        try {
            $client->campusCreateCampusGroupWithOptions($campusCreateCampusGroupRequest, $campusCreateCampusGroupHeaders, new RuntimeOptions([]));
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
  dingtalkindustry_1_0  "github.com/alibabacloud-go/dingtalk/industry_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkindustry_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkindustry_1_0.Client{}
  _result, _err = dingtalkindustry_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  campusCreateCampusGroupHeaders := &dingtalkindustry_1_0.CampusCreateCampusGroupHeaders{}
  campusCreateCampusGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  campusCreateCampusGroupRequest := &dingtalkindustry_1_0.CampusCreateCampusGroupRequest{
    Name: tea.String("测试项目组"),
    Extend: tea.String("扩展信息"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CampusCreateCampusGroupWithOptions(campusCreateCampusGroupRequest, campusCreateCampusGroupHeaders, &util.RuntimeOptions{})
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
import dingtalkindustry_1_0, * as $dingtalkindustry_1_0 from '@alicloud/dingtalk/industry_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkindustry_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkindustry_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let campusCreateCampusGroupHeaders = new $dingtalkindustry_1_0.CampusCreateCampusGroupHeaders({ });
    campusCreateCampusGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let campusCreateCampusGroupRequest = new $dingtalkindustry_1_0.CampusCreateCampusGroupRequest({
      name: "测试项目组",
      extend: "扩展信息",
    });
    try {
      await client.campusCreateCampusGroupWithOptions(campusCreateCampusGroupRequest, campusCreateCampusGroupHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkindustry_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkindustry_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusGroupHeaders campusCreateCampusGroupHeaders = new AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusGroupHeaders();
            campusCreateCampusGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusGroupRequest campusCreateCampusGroupRequest = new AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.CampusCreateCampusGroupRequest
            {
                Name = "测试项目组",
                Extend = "扩展信息",
            };
            try
            {
                client.CampusCreateCampusGroupWithOptions(campusCreateCampusGroupRequest, campusCreateCampusGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| groupId | Long | 项目组ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "groupId" : 12345
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | sytem.error | system error %s | 创建失败 |
| 501 | campus.noRoot | 项目通讯录未初始化 | 项目通讯录未初始化 |
| 502 | campus.notFit | 非园区租户组织 | 非园区租户组织 |
