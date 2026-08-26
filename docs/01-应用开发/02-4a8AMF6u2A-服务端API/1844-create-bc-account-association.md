---
title: "创建钉钉客联钉外账号"
source_url: "https://open.dingtalk.com/document/development/create-bc-account-association"
namespace: "development"
slug: "create-bc-account-association"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 创建钉钉客联钉外账号"
doc_id: "wyAs6hk8Le"
updated_at: "2026-07-22 16:35:14"
---

> Source: https://open.dingtalk.com/document/development/create-bc-account-association
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 创建钉钉客联钉外账号
> Updated: 2026-07-22 16:35:14

# 创建钉钉客联钉外账号

在互通场景中，需要有钉外账号，通过该接口创建钉外用户账号，并且可以建立与钉内用户帐号的关联关系，方便后续建群等操作。

### 接口使用说明

- 该接口**已经暂停新客户支持**，进入EOL（end of life）阶段，敬请期待新的开放能力支持。
- 调用本接口之前，需要开通钉钉互联应用。

调用本接口成功创建账号并建立关联关系后，效果如下图所示。
![](https://img.alicdn.com/imgextra/i4/O1CN01WZyuyQ1ZYOYoE1bdb_!!6000000003206-2-tps-2266-842.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23CreateInterconnection) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23CreateInterconnection) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interconnections HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "interconnections" : [ {
    "appUserId" : "String",
    "appUserName" : "String",
    "appUserAvatarMediaType" : Integer,
    "appUserAvatar" : "String",
    "appUserDynamics" : "String",
    "appUserMobile" : "String",
    "userId" : "String",
    "channelCode" : "String"
  } ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| interconnections | Array | 是 | 最大限制为200个。 |
| appUserId | String | 是 | 钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。 例如：1107\*\*\*\*2120 |
| appUserName | String | 是 | 钉外账号名称，长度限制为1~64个字符。 例如：Foo |
| appUserAvatarMediaType | Integer | 否 | 钉外账号头像类型，取值：   - **1**：http类型 |
| appUserAvatar | String | 否 | 钉外账号头像链接，长度限制为1～1024个字符。 例如：http://\*\*\*\*.png |
| appUserDynamics | String | 否 | 钉外账号动态信息，长度限制为1～64个字符。 例如：认真工作,快乐生活 |
| appUserMobile | String | 是 | 钉外账号手机号，长度限制为11位号码。例如：188\*\*\*\*8655 |
| userId | String | 否 | 钉内账号userId，长度限制为1～64个字符。 例如：1745\*\*\*\*8777 |
| channelCode | String | 是 | 渠道code。例如：M0U+\*\*\*\*8Ep=  **[!NOTE]**    该参数在创建渠道后获取，如何创建可参考[渠道配置](1839-interconnections-channel.md)文档。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| results | Array | 创建失败的钉内与钉外用户关系列表。 |
| appUserId | String | 钉外账号在业务系统内的唯一标识。 |
| userId | String | 钉内账号userId。 |
| message | String | 失败原因。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "interconnections" : [ {
    "appUserId" : "1107****2120",
    "appUserName" : "Foo",
    "appUserAvatarMediaType" : 1,
    "appUserAvatar" : "http://****.png",
    "appUserDynamics" : "认真工作,快乐生活",
    "appUserMobile" : "188****8655",
    "userId" : "1745****8777",
    "channelCode" : "M0U+****8Ep="
  } ]
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
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_1_0.models.CreateInterconnectionHeaders createInterconnectionHeaders = new com.aliyun.dingtalkim_1_0.models.CreateInterconnectionHeaders();
        createInterconnectionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.CreateInterconnectionRequest.CreateInterconnectionRequestInterconnections interconnections0 = new com.aliyun.dingtalkim_1_0.models.CreateInterconnectionRequest.CreateInterconnectionRequestInterconnections()
                .setAppUserId("1107****2120")
                .setAppUserName("Foo")
                .setAppUserAvatarMediaType(1)
                .setAppUserAvatar("http://****.png")
                .setAppUserDynamics("认真工作,快乐生活")
                .setAppUserMobile("188****8655")
                .setUserId("1745****8777")
                .setChannelCode("M0U+****8Ep=");
        com.aliyun.dingtalkim_1_0.models.CreateInterconnectionRequest createInterconnectionRequest = new com.aliyun.dingtalkim_1_0.models.CreateInterconnectionRequest()
                .setInterconnections(java.util.Arrays.asList(
                    interconnections0
                ));
        try {
            client.createInterconnectionWithOptions(createInterconnectionRequest, createInterconnectionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.im_1_0.client import Client as dingtalkim_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.im_1_0 import models as dingtalkim__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkim_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_interconnection_headers = dingtalkim__1__0_models.CreateInterconnectionHeaders()
        create_interconnection_headers.x_acs_dingtalk_access_token = '<your access token>'
        interconnections_0 = dingtalkim__1__0_models.CreateInterconnectionRequestInterconnections(
            app_user_id='1107****2120',
            app_user_name='Foo',
            app_user_avatar_media_type=1,
            app_user_avatar='http://****.png',
            app_user_dynamics='认真工作,快乐生活',
            app_user_mobile='188****8655',
            user_id='1745****8777',
            channel_code='M0U+****8Ep='
        )
        create_interconnection_request = dingtalkim__1__0_models.CreateInterconnectionRequest(
            interconnections=[
                interconnections_0
            ]
        )
        try:
            client.create_interconnection_with_options(create_interconnection_request, create_interconnection_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_interconnection_headers = dingtalkim__1__0_models.CreateInterconnectionHeaders()
        create_interconnection_headers.x_acs_dingtalk_access_token = '<your access token>'
        interconnections_0 = dingtalkim__1__0_models.CreateInterconnectionRequestInterconnections(
            app_user_id='1107****2120',
            app_user_name='Foo',
            app_user_avatar_media_type=1,
            app_user_avatar='http://****.png',
            app_user_dynamics='认真工作,快乐生活',
            app_user_mobile='188****8655',
            user_id='1745****8777',
            channel_code='M0U+****8Ep='
        )
        create_interconnection_request = dingtalkim__1__0_models.CreateInterconnectionRequest(
            interconnections=[
                interconnections_0
            ]
        )
        try:
            await client.create_interconnection_with_options_async(create_interconnection_request, create_interconnection_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateInterconnectionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateInterconnectionRequest\interconnections;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateInterconnectionRequest;
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
        $createInterconnectionHeaders = new CreateInterconnectionHeaders([]);
        $createInterconnectionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $interconnections0 = new interconnections([
            "appUserId" => "1107****2120",
            "appUserName" => "Foo",
            "appUserAvatarMediaType" => 1,
            "appUserAvatar" => "http://****.png",
            "appUserDynamics" => "认真工作,快乐生活",
            "appUserMobile" => "188****8655",
            "userId" => "1745****8777",
            "channelCode" => "M0U+****8Ep="
        ]);
        $createInterconnectionRequest = new CreateInterconnectionRequest([
            "interconnections" => [
                $interconnections0
            ]
        ]);
        try {
            $client->createInterconnectionWithOptions($createInterconnectionRequest, $createInterconnectionHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
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
func CreateClient () (_result *dingtalkim_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkim_1_0.Client{}
  _result, _err = dingtalkim_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createInterconnectionHeaders := &dingtalkim_1_0.CreateInterconnectionHeaders{}
  createInterconnectionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  interconnections0 := &dingtalkim_1_0.CreateInterconnectionRequestInterconnections{
    AppUserId: tea.String("1107****2120"),
    AppUserName: tea.String("Foo"),
    AppUserAvatarMediaType: tea.Int32(1),
    AppUserAvatar: tea.String("http://****.png"),
    AppUserDynamics: tea.String("认真工作,快乐生活"),
    AppUserMobile: tea.String("188****8655"),
    UserId: tea.String("1745****8777"),
    ChannelCode: tea.String("M0U+****8Ep="),
  }
  createInterconnectionRequest := &dingtalkim_1_0.CreateInterconnectionRequest{
    Interconnections: []*dingtalkim_1_0.CreateInterconnectionRequestInterconnections{interconnections0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateInterconnectionWithOptions(createInterconnectionRequest, createInterconnectionHeaders, &util.RuntimeOptions{})
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
const dingtalkim_1_0 = require('@alicloud/dingtalk/im_1_0');
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
    return new dingtalkim_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createInterconnectionHeaders = new dingtalkim_1_0.CreateInterconnectionHeaders({ });
    createInterconnectionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let interconnections0 = new dingtalkim_1_0.CreateInterconnectionRequestInterconnections({
      appUserId: '1107****2120',
      appUserName: 'Foo',
      appUserAvatarMediaType: 1,
      appUserAvatar: 'http://****.png',
      appUserDynamics: '认真工作,快乐生活',
      appUserMobile: '188****8655',
      userId: '1745****8777',
      channelCode: 'M0U+****8Ep=',
    });
    let createInterconnectionRequest = new dingtalkim_1_0.CreateInterconnectionRequest({
      interconnections: [
        interconnections0
      ],
    });
    try {
      await client.createInterconnectionWithOptions(createInterconnectionRequest, createInterconnectionHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkim_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkim_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkim_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionHeaders createInterconnectionHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionHeaders();
            createInterconnectionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionRequest.CreateInterconnectionRequestInterconnections interconnections0 = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionRequest.CreateInterconnectionRequestInterconnections
            {
                AppUserId = "1107****2120",
                AppUserName = "Foo",
                AppUserAvatarMediaType = 1,
                AppUserAvatar = "http://****.png",
                AppUserDynamics = "认真工作,快乐生活",
                AppUserMobile = "188****8655",
                UserId = "1745****8777",
                ChannelCode = "M0U+****8Ep=",
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionRequest createInterconnectionRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionRequest
            {
                Interconnections = new List<AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateInterconnectionRequest.CreateInterconnectionRequestInterconnections>
                {
                    interconnections0
                },
            };
            try
            {
                client.CreateInterconnectionWithOptions(createInterconnectionRequest, createInterconnectionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "results" : [ {
    "appUserId" : "1107****2120",
    "userId" : "1745****8777",
    "message" : "****"
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否缺少必要参数或内容不正确 | 输入参数有误，请检查是否缺少必要参数或内容不正确 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | client.add.error | 创建钉外账号及关联关系失败 | 创建钉外账号及关联关系失败 |
| 400 | general.signatureError | 参数签名失败，请检查 | 参数签名失败，请检查 |
| 400 | client.nameIllegal | 用户名称中包含不合规内容，请检查 | 用户名称中包含不合规内容，请检查 |
| 500 | system.error | 系统异常 | 系统异常 |
