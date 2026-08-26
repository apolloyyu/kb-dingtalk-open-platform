---
title: "解散钉钉客联互通群"
source_url: "https://open.dingtalk.com/document/development/disband-bc-interconnection-group"
namespace: "development"
slug: "disband-bc-interconnection-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 解散钉钉客联互通群"
doc_id: "1h0v9LiboZ"
updated_at: "2026-07-21 10:10:09"
---

> Source: https://open.dingtalk.com/document/development/disband-bc-interconnection-group
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 解散钉钉客联互通群
> Updated: 2026-07-21 10:10:09

# 解散钉钉客联互通群

调用本接口，解散互通群。

### 接口使用说明

> **[!NOTE]**
>
> - 该接口**已经暂停新客户支持**，进入EOL（end of life）阶段，敬请期待新的开放能力支持。
> - 调用本接口之前，需要开通钉钉互联应用。

例如，有一个互通群名为**测试群**，调用本接口可解散该群会话。接口调用成功后，效果如下图所示。
![](https://img.alicdn.com/imgextra/i1/O1CN01P3LPvE1w0GCjCdVJY_!!6000000006245-2-tps-2266-1058.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23DismissGroupConversation) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23DismissGroupConversation) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interconnections/groups/dismiss HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "openConversationId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群会话openConversationId，可调用[创建钉钉客联普通互通群](1845-create-common-group-new-version.md) / [创建钉钉客联两人互通群](1846-creating-two-groups-of-people.md)接口获取，长度限制为1～32个字符，例如：14da\*\*\*\*2760。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversationId | String | 被解散的群会话openConversationId。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/groups/dismiss HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "openConversationId" : "14da****2760"
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
        com.aliyun.dingtalkim_1_0.models.DismissGroupConversationHeaders dismissGroupConversationHeaders = new com.aliyun.dingtalkim_1_0.models.DismissGroupConversationHeaders();
        dismissGroupConversationHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.DismissGroupConversationRequest dismissGroupConversationRequest = new com.aliyun.dingtalkim_1_0.models.DismissGroupConversationRequest()
                .setOpenConversationId("14da****2760");
        try {
            client.dismissGroupConversationWithOptions(dismissGroupConversationRequest, dismissGroupConversationHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        dismiss_group_conversation_headers = dingtalkim__1__0_models.DismissGroupConversationHeaders()
        dismiss_group_conversation_headers.x_acs_dingtalk_access_token = '<your access token>'
        dismiss_group_conversation_request = dingtalkim__1__0_models.DismissGroupConversationRequest(
            open_conversation_id='14da****2760'
        )
        try:
            client.dismiss_group_conversation_with_options(dismiss_group_conversation_request, dismiss_group_conversation_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        dismiss_group_conversation_headers = dingtalkim__1__0_models.DismissGroupConversationHeaders()
        dismiss_group_conversation_headers.x_acs_dingtalk_access_token = '<your access token>'
        dismiss_group_conversation_request = dingtalkim__1__0_models.DismissGroupConversationRequest(
            open_conversation_id='14da****2760'
        )
        try:
            await client.dismiss_group_conversation_with_options_async(dismiss_group_conversation_request, dismiss_group_conversation_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\DismissGroupConversationHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\DismissGroupConversationRequest;
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
        $dismissGroupConversationHeaders = new DismissGroupConversationHeaders([]);
        $dismissGroupConversationHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $dismissGroupConversationRequest = new DismissGroupConversationRequest([
            "openConversationId" => "14da****2760"
        ]);
        try {
            $client->dismissGroupConversationWithOptions($dismissGroupConversationRequest, $dismissGroupConversationHeaders, new RuntimeOptions([]));
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

  dismissGroupConversationHeaders := &dingtalkim_1_0.DismissGroupConversationHeaders{}
  dismissGroupConversationHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  dismissGroupConversationRequest := &dingtalkim_1_0.DismissGroupConversationRequest{
    OpenConversationId: tea.String("14da****2760"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DismissGroupConversationWithOptions(dismissGroupConversationRequest, dismissGroupConversationHeaders, &util.RuntimeOptions{})
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
    let dismissGroupConversationHeaders = new dingtalkim_1_0.DismissGroupConversationHeaders({ });
    dismissGroupConversationHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let dismissGroupConversationRequest = new dingtalkim_1_0.DismissGroupConversationRequest({
      openConversationId: '14da****2760',
    });
    try {
      await client.dismissGroupConversationWithOptions(dismissGroupConversationRequest, dismissGroupConversationHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.DismissGroupConversationHeaders dismissGroupConversationHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.DismissGroupConversationHeaders();
            dismissGroupConversationHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.DismissGroupConversationRequest dismissGroupConversationRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.DismissGroupConversationRequest
            {
                OpenConversationId = "14da****2760",
            };
            try
            {
                client.DismissGroupConversationWithOptions(dismissGroupConversationRequest, dismissGroupConversationHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "openConversationId" : "14da****2760"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | group.nonexist | 群不存在，请检查 | 群不存在，请检查 |
| 400 | group.creating | 群会话仍在创建中，请稍后重试 | 群会话仍在创建中，请稍后重试 |
| 500 | group.dismissError | 解散群失败 | 解散群失败 |
| 500 | system.error | 系统异常 | 系统异常 |
