---
title: "更换钉钉客联互通群群主"
source_url: "https://open.dingtalk.com/document/development/change-group-owner"
namespace: "development"
slug: "change-group-owner"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 更换钉钉客联互通群群主"
doc_id: "ZlbJ1b6Frq"
updated_at: "2026-08-28 10:26:36"
---

> Source: https://open.dingtalk.com/document/development/change-group-owner
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 钉钉客联 > 更换钉钉客联互通群群主
> Updated: 2026-08-28 10:26:36

# 更换钉钉客联互通群群主

调用本接口，将指定钉内账号或钉外账号更换为群主，更换群主后，只支持钉外用户查看群主的变更结果，钉钉客户端内的群主信息暂不同步更新。

> **[!IMPORTANT]**
>
> 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
PUT /v1.0/im/interconnections/groups/owners HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "openConversationId" : "String",
  "groupOwnerId" : "String",
  "groupOwnerType" : Integer
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群会话openConversationId，可调用[创建钉钉客联钉外账号](1847-create-bc-account-association.md)接口获取，长度限制为1～32个字符。 |
| groupOwnerId | String | 是 | 群主在业务系统内的唯一标识，可调用[创建钉钉客联钉外账号](1847-create-bc-account-association.md)接口获取。  **[!NOTE]**  支持指定钉内账号或钉外账号为群主：   - 若是钉内账号userId，长度限制为1～64个字符。 - 若是钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。 |
| groupOwnerType | Integer | 是 | 群主类型，取值：   - **2**：钉内用户。 - **3**：钉外用户。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| newGroupOwnerId | String | 新群主Id。 |
| newGroupOwnerType | Integer | 新群主类型，取值：   - **2**：钉内用户 - **3**：钉外用户 |

## 示例

**请求示例**

HTTP

```
PUT /v1.0/im/interconnections/groups/owners HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "openConversationId" : "14da****2760",
  "groupOwnerId" : "1745****8778",
  "groupOwnerType" : 2
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
        com.aliyun.dingtalkim_1_0.models.ChangeGroupOwnerHeaders changeGroupOwnerHeaders = new com.aliyun.dingtalkim_1_0.models.ChangeGroupOwnerHeaders();
        changeGroupOwnerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.ChangeGroupOwnerRequest changeGroupOwnerRequest = new com.aliyun.dingtalkim_1_0.models.ChangeGroupOwnerRequest()
                .setOpenConversationId("14da****2760")
                .setGroupOwnerId("1745****8778")
                .setGroupOwnerType(2);
        try {
            client.changeGroupOwnerWithOptions(changeGroupOwnerRequest, changeGroupOwnerHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        change_group_owner_headers = dingtalkim__1__0_models.ChangeGroupOwnerHeaders()
        change_group_owner_headers.x_acs_dingtalk_access_token = '<your access token>'
        change_group_owner_request = dingtalkim__1__0_models.ChangeGroupOwnerRequest(
            open_conversation_id='14da****2760',
            group_owner_id='1745****8778',
            group_owner_type=2
        )
        try:
            client.change_group_owner_with_options(change_group_owner_request, change_group_owner_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        change_group_owner_headers = dingtalkim__1__0_models.ChangeGroupOwnerHeaders()
        change_group_owner_headers.x_acs_dingtalk_access_token = '<your access token>'
        change_group_owner_request = dingtalkim__1__0_models.ChangeGroupOwnerRequest(
            open_conversation_id='14da****2760',
            group_owner_id='1745****8778',
            group_owner_type=2
        )
        try:
            await client.change_group_owner_with_options_async(change_group_owner_request, change_group_owner_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\ChangeGroupOwnerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\ChangeGroupOwnerRequest;
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
        $changeGroupOwnerHeaders = new ChangeGroupOwnerHeaders([]);
        $changeGroupOwnerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $changeGroupOwnerRequest = new ChangeGroupOwnerRequest([
            "openConversationId" => "14da****2760",
            "groupOwnerId" => "1745****8778",
            "groupOwnerType" => 2
        ]);
        try {
            $client->changeGroupOwnerWithOptions($changeGroupOwnerRequest, $changeGroupOwnerHeaders, new RuntimeOptions([]));
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

  changeGroupOwnerHeaders := &dingtalkim_1_0.ChangeGroupOwnerHeaders{}
  changeGroupOwnerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  changeGroupOwnerRequest := &dingtalkim_1_0.ChangeGroupOwnerRequest{
    OpenConversationId: tea.String("14da****2760"),
    GroupOwnerId: tea.String("1745****8778"),
    GroupOwnerType: tea.Int32(2),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChangeGroupOwnerWithOptions(changeGroupOwnerRequest, changeGroupOwnerHeaders, &util.RuntimeOptions{})
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
    let changeGroupOwnerHeaders = new dingtalkim_1_0.ChangeGroupOwnerHeaders({ });
    changeGroupOwnerHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let changeGroupOwnerRequest = new dingtalkim_1_0.ChangeGroupOwnerRequest({
      openConversationId: '14da****2760',
      groupOwnerId: '1745****8778',
      groupOwnerType: 2,
    });
    try {
      await client.changeGroupOwnerWithOptions(changeGroupOwnerRequest, changeGroupOwnerHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChangeGroupOwnerHeaders changeGroupOwnerHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChangeGroupOwnerHeaders();
            changeGroupOwnerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChangeGroupOwnerRequest changeGroupOwnerRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.ChangeGroupOwnerRequest
            {
                OpenConversationId = "14da****2760",
                GroupOwnerId = "1745****8778",
                GroupOwnerType = 2,
            };
            try
            {
                client.ChangeGroupOwnerWithOptions(changeGroupOwnerRequest, changeGroupOwnerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "newGroupOwnerId" : "1745****8778",
  "newGroupOwnerType" : 2
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | group.nonexist | 群不存在，请检查 | 群不存在，请检查 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | service.nonexist | 钉内账号不存在，请检查 | 钉内账号不存在，请检查 |
| 400 | general.enumError | 入参枚举有误，请检查 | 入参枚举有误，请检查 |
| 400 | member.nonexist | 找不到群成员，请检查 | 找不到群成员，请检查 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 500 | system.error | 系统异常 | 系统异常 |
