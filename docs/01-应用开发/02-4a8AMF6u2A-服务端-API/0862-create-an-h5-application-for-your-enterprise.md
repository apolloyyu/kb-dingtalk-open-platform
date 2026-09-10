---
title: "创建企业内部应用"
source_url: "https://open.dingtalk.com/document/development/create-an-h5-application-for-your-enterprise"
namespace: "development"
slug: "create-an-h5-application-for-your-enterprise"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 应用管理 > 创建企业内部应用"
doc_id: "OPYhzodKBE"
updated_at: "2026-06-03 11:44:57"
---

> Source: https://open.dingtalk.com/document/development/create-an-h5-application-for-your-enterprise
> Path: 应用开发 / 服务端 API / 钉钉应用 > 应用管理 > 创建企业内部应用
> Updated: 2026-06-03 11:44:57

# 创建企业内部应用

调用本接口，创建企业内部应用，创建成功后，获取应用的AgentId、AppKey和AppSecret信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/apps |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-管理微应用的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUnionId | String | 是 | 操作人的unionId，该用户必须是拥有**应用管理权限**的管理员，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| name | String | 是 | 应用名称。 |
| desc | String | 是 | 应用描述。 |
| icon | String | 否 | 应用图标media，调用[上传媒体文件](0646-upload-media-files.md)接口获取media\_id参数值。 |
| homepageLink | String | 否 | 应用首页地址。  **[!NOTE]**     - 当`developType`=0，即创建企业内部H5微应用，该参数必传。 - 当`developType`=1，即创建企业内部小程序，该参数无需透传。 |
| pcHomepageLink | String | 否 | 应用PC端地址。 |
| ompLink | String | 否 | 应用管理后台地址。 |
| ipWhiteList | Array of String | 否 | 服务器出口IP白名单列表，最大值50。 |
| scopeType | String | 否 | 权限类型，目前只支持BASE。   - **BASE**：表示创建的应用，具有免登的接口权限。 |
| developType | Integer | 否 | 创建的内部应用类型：【默认为0】   - **0**：创建企业内部H5微应用 - **1**：创建企业内部小程序 |

### 请求示例

HTTP

```
POST /v1.0/microApp/apps HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:kfwINxxx
Content-Type:application/json

{
  "opUnionId" : "ez275xxx",
  "name" : "应用名称",
  "desc" : "应用描述",
  "icon" : "mediaxxx",
  "homepageLink" : "https://www.dingtalk.com",
  "pcHomepageLink" : "https://www.dingtalk.com",
  "ompLink" : "https://www.dingtalk.com",
  "ipWhiteList" : [ "1.1.1.1" ],
  "scopeType" : "BASE",
  "developType" : 0
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.CreateInnerAppHeaders createInnerAppHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.CreateInnerAppHeaders();
        createInnerAppHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.CreateInnerAppRequest createInnerAppRequest = new com.aliyun.dingtalkmicro_app_1_0.models.CreateInnerAppRequest()
                .setOpUnionId("ez275xxx")
                .setName("应用名称")
                .setDesc("应用描述")
                .setIcon("mediaxxx")
                .setHomepageLink("https://www.dingtalk.com")
                .setPcHomepageLink("https://www.dingtalk.com")
                .setOmpLink("https://www.dingtalk.com")
                .setIpWhiteList(java.util.Arrays.asList(
                    "1.1.1.1"
                ))
                .setScopeType("BASE")
                .setDevelopType(0);
        try {
            client.createInnerAppWithOptions(createInnerAppRequest, createInnerAppHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from typing import List

from alibabacloud_dingtalk.micro_app_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmicroApp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmicroApp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_inner_app_headers = dingtalkmicro_app__1__0_models.CreateInnerAppHeaders()
        create_inner_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_inner_app_request = dingtalkmicro_app__1__0_models.CreateInnerAppRequest(
            op_union_id='ez275xxx',
            name='应用名称',
            desc='应用描述',
            icon='mediaxxx',
            homepage_link='https://www.dingtalk.com',
            pc_homepage_link='https://www.dingtalk.com',
            omp_link='https://www.dingtalk.com',
            ip_white_list=[
                '1.1.1.1'
            ],
            scope_type='BASE',
            develop_type=0
        )
        try:
            client.create_inner_app_with_options(create_inner_app_request, create_inner_app_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_inner_app_headers = dingtalkmicro_app__1__0_models.CreateInnerAppHeaders()
        create_inner_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_inner_app_request = dingtalkmicro_app__1__0_models.CreateInnerAppRequest(
            op_union_id='ez275xxx',
            name='应用名称',
            desc='应用描述',
            icon='mediaxxx',
            homepage_link='https://www.dingtalk.com',
            pc_homepage_link='https://www.dingtalk.com',
            omp_link='https://www.dingtalk.com',
            ip_white_list=[
                '1.1.1.1'
            ],
            scope_type='BASE',
            develop_type=0
        )
        try:
            await client.create_inner_app_with_options_async(create_inner_app_request, create_inner_app_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\CreateInnerAppHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\CreateInnerAppRequest;
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
        $createInnerAppHeaders = new CreateInnerAppHeaders([]);
        $createInnerAppHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createInnerAppRequest = new CreateInnerAppRequest([
            "opUnionId" => "ez275xxx",
            "name" => "应用名称",
            "desc" => "应用描述",
            "icon" => "mediaxxx",
            "homepageLink" => "https://www.dingtalk.com",
            "pcHomepageLink" => "https://www.dingtalk.com",
            "ompLink" => "https://www.dingtalk.com",
            "ipWhiteList" => [
                "1.1.1.1"
            ],
            "scopeType" => "BASE",
            "developType" => 0
        ]);
        try {
            $client->createInnerAppWithOptions($createInnerAppRequest, $createInnerAppHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
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
func CreateClient () (_result *dingtalkmicroapp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmicroapp_1_0.Client{}
  _result, _err = dingtalkmicroapp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createInnerAppHeaders := &dingtalkmicroapp_1_0.CreateInnerAppHeaders{}
  createInnerAppHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createInnerAppRequest := &dingtalkmicroapp_1_0.CreateInnerAppRequest{
    OpUnionId: tea.String("ez275xxx"),
    Name: tea.String("应用名称"),
    Desc: tea.String("应用描述"),
    Icon: tea.String("mediaxxx"),
    HomepageLink: tea.String("https://www.dingtalk.com"),
    PcHomepageLink: tea.String("https://www.dingtalk.com"),
    OmpLink: tea.String("https://www.dingtalk.com"),
    IpWhiteList: []*string{tea.String("1.1.1.1")},
    ScopeType: tea.String("BASE"),
    DevelopType: tea.Int32(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateInnerAppWithOptions(createInnerAppRequest, createInnerAppHeaders, &util.RuntimeOptions{})
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
const dingtalkmicroApp_1_0 = require('@alicloud/dingtalk/microApp_1_0');
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
    return new dingtalkmicroApp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createInnerAppHeaders = new dingtalkmicroApp_1_0.CreateInnerAppHeaders({ });
    createInnerAppHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let createInnerAppRequest = new dingtalkmicroApp_1_0.CreateInnerAppRequest({
      opUnionId: 'ez275xxx',
      name: '应用名称',
      desc: '应用描述',
      icon: 'mediaxxx',
      homepageLink: 'https://www.dingtalk.com',
      pcHomepageLink: 'https://www.dingtalk.com',
      ompLink: 'https://www.dingtalk.com',
      ipWhiteList: [
        '1.1.1.1'
      ],
      scopeType: 'BASE',
      developType: 0,
    });
    try {
      await client.createInnerAppWithOptions(createInnerAppRequest, createInnerAppHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateInnerAppHeaders createInnerAppHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateInnerAppHeaders();
            createInnerAppHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateInnerAppRequest createInnerAppRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.CreateInnerAppRequest
            {
                OpUnionId = "ez275xxx",
                Name = "应用名称",
                Desc = "应用描述",
                Icon = "mediaxxx",
                HomepageLink = "https://www.dingtalk.com",
                PcHomepageLink = "https://www.dingtalk.com",
                OmpLink = "https://www.dingtalk.com",
                IpWhiteList = new List<string>
                {
                    "1.1.1.1"
                },
                ScopeType = "BASE",
                DevelopType = 0,
            };
            try
            {
                client.CreateInnerAppWithOptions(createInnerAppRequest, createInnerAppHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| agentId | Long | 应用的AgentId。 |
| appKey | String | 应用的AppKey。 |
| appSecret | String | 应用的AppSecret。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "agentId" : 111,
  "appKey" : "dingryhxxx",
  "appSecret" : "iXMVbjRxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | invalidUser | 用户id不合法，不在对应企业中 | 用户id不合法，不在对应企业中 |
| 400 | invalidEcologicalCorpId | 不合法的合作空间corpId | 不合法的合作空间corpId |
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | illegalIp | ip不合法 | ip不合法，可能是单个ip不合法，也可能是ip总长度超过了50 |
| 400 | illegalAppName | 应用名称含有不规范词语 | 应用名称含有不规范词语 |
| 400 | illegalAppDesc | 应用描述含有不规范词语 | 应用描述含有不规范词语 |
| 400 | illegalAppIcon | 应用图标含有不规范词语 | 应用图标含有不规范词语 |
| 400 | overMaxCount | 超过最大可创建应用数 | 超过最大可创建应用数 |
| 500 | systemError | 系统繁忙 | 系统繁忙 |
