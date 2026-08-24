---
title: "创建自定义部门下的班级"
source_url: "https://open.dingtalk.com/document/development/create-classes-in-a-custom-department"
namespace: "development"
slug: "create-classes-in-a-custom-department"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建自定义部门下的班级"
doc_id: "jvdqtkm8pq"
updated_at: "2026-06-04 19:11:29"
---

> Source: https://open.dingtalk.com/document/development/create-classes-in-a-custom-department
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建自定义部门下的班级
> Updated: 2026-06-04 19:11:29

# 创建自定义部门下的班级

调用本接口，创建自定义部门下的班级。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/customClasses |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-教育行业扩展通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| customClass | Object | 是 | 班级信息。 |
| name | String | 是 | 班级名称。 |
| superId | Long | 是 | 上级部门ID，可通过调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_id参数值。 |
| operator | String | 是 | 操作人userId。 |

### 请求示例

HTTP

```
POST /v1.0/edu/customClasses HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:638bab94c8xxxx
Content-Type:application/json

{
  "customClass" : {
    "name" : "2021级培训班"
  },
  "superId" : 12345,
  "operator" : "manager"
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
    public static com.aliyun.dingtalkedu_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkedu_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkedu_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkedu_1_0.models.CreateCustomClassHeaders createCustomClassHeaders = new com.aliyun.dingtalkedu_1_0.models.CreateCustomClassHeaders();
        createCustomClassHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.CreateCustomClassRequest.CreateCustomClassRequestCustomClass customClass = new com.aliyun.dingtalkedu_1_0.models.CreateCustomClassRequest.CreateCustomClassRequestCustomClass()
                .setName("2021级培训班");
        com.aliyun.dingtalkedu_1_0.models.CreateCustomClassRequest createCustomClassRequest = new com.aliyun.dingtalkedu_1_0.models.CreateCustomClassRequest()
                .setCustomClass(customClass)
                .setSuperId(12345L)
                .setOperator("manager");
        try {
            client.createCustomClassWithOptions(createCustomClassRequest, createCustomClassHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.edu_1_0.client import Client as dingtalkedu_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.edu_1_0 import models as dingtalkedu__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkedu_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkedu_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_custom_class_headers = dingtalkedu__1__0_models.CreateCustomClassHeaders()
        create_custom_class_headers.x_acs_dingtalk_access_token = '<your access token>'
        custom_class = dingtalkedu__1__0_models.CreateCustomClassRequestCustomClass(
            name='2021级培训班'
        )
        create_custom_class_request = dingtalkedu__1__0_models.CreateCustomClassRequest(
            custom_class=custom_class,
            super_id=12345,
            operator='manager'
        )
        try:
            client.create_custom_class_with_options(create_custom_class_request, create_custom_class_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_custom_class_headers = dingtalkedu__1__0_models.CreateCustomClassHeaders()
        create_custom_class_headers.x_acs_dingtalk_access_token = '<your access token>'
        custom_class = dingtalkedu__1__0_models.CreateCustomClassRequestCustomClass(
            name='2021级培训班'
        )
        create_custom_class_request = dingtalkedu__1__0_models.CreateCustomClassRequest(
            custom_class=custom_class,
            super_id=12345,
            operator='manager'
        )
        try:
            await client.create_custom_class_with_options_async(create_custom_class_request, create_custom_class_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCustomClassHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCustomClassRequest\customClass;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCustomClassRequest;
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
        $createCustomClassHeaders = new CreateCustomClassHeaders([]);
        $createCustomClassHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $customClass = new customClass([
            "name" => "2021级培训班"
        ]);
        $createCustomClassRequest = new CreateCustomClassRequest([
            "customClass" => $customClass,
            "superId" => 12345,
            "operator" => "manager"
        ]);
        try {
            $client->createCustomClassWithOptions($createCustomClassRequest, $createCustomClassHeaders, new RuntimeOptions([]));
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
  dingtalkedu_1_0  "github.com/alibabacloud-go/dingtalk/edu_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkedu_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkedu_1_0.Client{}
  _result, _err = dingtalkedu_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createCustomClassHeaders := &dingtalkedu_1_0.CreateCustomClassHeaders{}
  createCustomClassHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  customClass := &dingtalkedu_1_0.CreateCustomClassRequestCustomClass{
    Name: tea.String("2021级培训班"),
  }
  createCustomClassRequest := &dingtalkedu_1_0.CreateCustomClassRequest{
    CustomClass: customClass,
    SuperId: tea.Int64(12345),
    Operator: tea.String("manager"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateCustomClassWithOptions(createCustomClassRequest, createCustomClassHeaders, &util.RuntimeOptions{})
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
import dingtalkedu_1_0, * as $dingtalkedu_1_0 from '@alicloud/dingtalk/edu_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkedu_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkedu_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createCustomClassHeaders = new $dingtalkedu_1_0.CreateCustomClassHeaders({ });
    createCustomClassHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let customClass = new $dingtalkedu_1_0.CreateCustomClassRequestCustomClass({
      name: "2021级培训班",
    });
    let createCustomClassRequest = new $dingtalkedu_1_0.CreateCustomClassRequest({
      customClass: customClass,
      superId: 12345,
      operator: "manager",
    });
    try {
      await client.createCustomClassWithOptions(createCustomClassRequest, createCustomClassHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkedu_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkedu_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkedu_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCustomClassHeaders createCustomClassHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCustomClassHeaders();
            createCustomClassHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCustomClassRequest.CreateCustomClassRequestCustomClass customClass = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCustomClassRequest.CreateCustomClassRequestCustomClass
            {
                Name = "2021级培训班",
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCustomClassRequest createCustomClassRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCustomClassRequest
            {
                CustomClass = customClass,
                SuperId = 12345,
                Operator = "manager",
            };
            try
            {
                client.CreateCustomClassWithOptions(createCustomClassRequest, createCustomClassHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| deptId | Long | 班级ID。 |
| success | Boolean | 是否调用成功，true表示调用成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "deptId" : 12233
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | PARAMETER INVALID | 参数非法 |
| 400 | illegalOrg | ILLEGAL ORG | 未被组织授权 |
| 400 | noRight | NO RIGHT | 当前用户没有操作权限 |
| 400 | invalidSubDeptType | INVALID SUB\_DEPT TYPE | 部门下不能同时挂自定义部门和班级 |
| 500 | systemBusy | SYSTEM BUSY | 系统繁忙 |
| 500 | createClassFail | CREATE CLASS FAIL | 创建自定义班级失败 |
