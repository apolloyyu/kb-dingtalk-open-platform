---
title: "查询伙伴角色列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-partners"
namespace: "development"
slug: "query-the-list-of-partners"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 产业互联 > 查询伙伴角色列表"
doc_id: "21bJniprhm"
updated_at: "2026-06-02 19:14:52"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-partners
> Path: 应用开发 / 服务端 API / 专属钉钉 > 产业互联 > 查询伙伴角色列表
> Updated: 2026-06-02 19:14:52

# 查询伙伴角色列表

调用本接口根据父标签ID获取角色列表。

## 接口调用说明

例如，有个伙伴类型名为开放测试，存在角色1，角色1中可见设置为员工小钉（userId为001）、测试部门1（部门ID为1）。角色1的预警设置为员工小钉、测试部门2(部门ID为2)，角色为必邀。

调用本接口后相关信息如图所示，可获取以下信息。

- 对谁可见中可获取：可见员工列表中的员工小钉的userId为001，可见部门列表中的测试部门1的部门ID为1。
- 是否必邀角色：角色1是必邀角色。
- 对谁预警中可获取：预警成员列表中的员工小钉的userId为001，预警部门列表中的测试部门2的部门ID为2。 ![](https://img.alicdn.com/imgextra/i1/O1CN01kth1t81jydOBgTzPE_!!6000000004617-2-tps-2828-1320.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/partners/roles/{parentId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Partner.Department.Read-伙伴钉部门信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| parentId | Long | 是 | 父标签ID，可调用[获取子标签列表](0833-obtain-child-tags-from-a-parent-tag.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/partners/roles/123 HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        ListPartnerRolesHeaders listPartnerRolesHeaders = new ListPartnerRolesHeaders();
        listPartnerRolesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.listPartnerRolesWithOptions("123", listPartnerRolesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_partner_roles_headers = dingtalkexclusive__1__0_models.ListPartnerRolesHeaders()
        list_partner_roles_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.list_partner_roles_with_options('123', list_partner_roles_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_partner_roles_headers = dingtalkexclusive__1__0_models.ListPartnerRolesHeaders()
        list_partner_roles_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.list_partner_roles_with_options_async('123', list_partner_roles_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\ListPartnerRolesHeaders;
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
        $listPartnerRolesHeaders = new ListPartnerRolesHeaders([]);
        $listPartnerRolesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->listPartnerRolesWithOptions("123", $listPartnerRolesHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listPartnerRolesHeaders := &dingtalkexclusive_1_0.ListPartnerRolesHeaders{}
  listPartnerRolesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListPartnerRolesWithOptions(tea.String("123"), listPartnerRolesHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listPartnerRolesHeaders = new $dingtalkexclusive_1_0.ListPartnerRolesHeaders({ });
    listPartnerRolesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.listPartnerRolesWithOptions("123", listPartnerRolesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.ListPartnerRolesHeaders listPartnerRolesHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.ListPartnerRolesHeaders();
            listPartnerRolesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.ListPartnerRolesWithOptions("123", listPartnerRolesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| list | Array | 角色列表。 |
| id | Long | 角色ID。 |
| name | String | 角色名称。 |
| isNecessary | Integer | 是否必邀角色。   - 0: 否 - 1: 是 |
| visibleUsers | Array | 可见员工列表。 |
| userId | String | 可见员工userId。 |
| name | String | 可见员工姓名。 |
| visibleDepts | Array | 可见部门列表。 |
| deptId | Long | 可见部门ID。 |
| name | String | 可见部门名称。 |
| warningUsers | Array | 预警成员列表。 |
| userId | String | 预警成员userId。 |
| name | String | 预警成员姓名。 |
| warningDepts | Array | 预警部门列表。 |
| deptId | Long | 预警部门ID。 |
| name | String | 预警部门名称。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "list" : [ {
    "id" : 123,
    "name" : "供应商",
    "isNecessary" : 1,
    "visibleUsers" : [ {
      "userId" : "123",
      "name" : "张三"
    } ],
    "visibleDepts" : [ {
      "deptId" : 123,
      "name" : "测试部门"
    } ],
    "warningUsers" : [ {
      "userId" : "123",
      "name" : "张三"
    } ],
    "warningDepts" : [ {
      "deptId" : 123,
      "name" : "测试部门"
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | 参数不合法，请确认parentId是否正确 | 参数不合法，请确认parentId是否正确 |
