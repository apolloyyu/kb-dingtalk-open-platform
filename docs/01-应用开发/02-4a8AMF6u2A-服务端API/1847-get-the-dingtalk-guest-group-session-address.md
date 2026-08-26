---
title: "获取钉钉客联H5页面地址"
source_url: "https://open.dingtalk.com/document/development/get-the-dingtalk-guest-group-session-address"
namespace: "development"
slug: "get-the-dingtalk-guest-group-session-address"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 获取钉钉客联H5页面地址"
doc_id: "SLWFoAuUux"
updated_at: "2026-07-21 10:00:21"
---

> Source: https://open.dingtalk.com/document/development/get-the-dingtalk-guest-group-session-address
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 获取钉钉客联H5页面地址
> Updated: 2026-07-21 10:00:21

# 获取钉钉客联H5页面地址

创建钉钉客联互通群后，可以调用本接口获取钉钉客联H5会话地址，钉外账号通过H5页面地址打开对应的群会话。

### 接口使用说明

- 该接口**已经暂停新客户支持**，进入EOL（end of life）阶段，敬请期待新的开放能力支持。
- 调用本接口之前，需要开通钉钉互联应用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23GetConversationUrl) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23GetConversationUrl) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/conversations/urls HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "appUserId" : "String",
  "userId" : "String",
  "openConversationId" : "String",
  "channelCode" : "String",
  "deviceId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appUserId | String | 是 | 钉外账号在业务系统内的标识，通过调用[创建钉钉客联钉外账号](1844-create-bc-account-association.md)接口获取，长度限制为1~64个字符。例如：1107\*\*\*\*2120。 |
| userId | String | 否 | 钉内账号userId，长度限制为1～64个字符。 例如：1745\*\*\*\*8777  **[!NOTE]**     - 如果传该参数，返回的地址是与当前钉内userId用户的会话地址。 - 如果不传该参数，返回的地址是与当前钉外用户所有相关的会话列表页面地址。 |
| openConversationId | String | 否 | 群会话openConversationId，可调用[创建钉钉客联普通互通群](1845-create-common-group-new-version.md) / [创建钉钉客联两人互通群](1846-creating-two-groups-of-people.md)接口获取，长度限制为1～32个字符，例如：14da\*\*\*\*2760。 |
| channelCode | String | 是 | 渠道code，获取方式可查看[渠道配置](1839-interconnections-channel.md)文档，示例如：M0U+\*\*\*\*8Ep=。  **[!NOTE]**     - 如果当前code是移动端的渠道code，则返回值结果为移动端H5页面地址；若果是PC端的渠道code，则返回PC端H5页面。 - 不同渠道的code只会影响渲染效果，不会影响群列表的返回结果。 |
| deviceId | String | 否 | 设备id，用于支持多端登录。长度限制为1~20个字符   - 若不传该参数，多次生成同一个钉外账号的url，访问url会互踢会话。 - 若传了该参数，多次生成同一个钉外账号的url，访问url会同时在线。 - 最多支持5个设备同时在线，超过5个会互踢。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| url | String | H5页面URL。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/conversations/urls HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "appUserId" : "1107****2120",
  "userId" : "1745****8777",
  "openConversationId" : "14da****2760",
  "channelCode" : "M0U+****8Ep="
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
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_1_0.models.GetConversationUrlHeaders getConversationUrlHeaders = new com.aliyun.dingtalkim_1_0.models.GetConversationUrlHeaders();
        getConversationUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.GetConversationUrlRequest getConversationUrlRequest = new com.aliyun.dingtalkim_1_0.models.GetConversationUrlRequest()
                .setAppUserId("1107****2120")
                .setUserId("1745****8777")
                .setOpenConversationId("14da****2760")
                .setChannelCode("M0U+****8Ep=");
        try {
            client.getConversationUrlWithOptions(getConversationUrlRequest, getConversationUrlHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_conversation_url_headers = dingtalkim__1__0_models.GetConversationUrlHeaders()
        get_conversation_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_conversation_url_request = dingtalkim__1__0_models.GetConversationUrlRequest(
            app_user_id='1107****2120',
            user_id='1745****8777',
            open_conversation_id='14da****2760',
            channel_code='M0U+****8Ep='
        )
        try:
            client.get_conversation_url_with_options(get_conversation_url_request, get_conversation_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_conversation_url_headers = dingtalkim__1__0_models.GetConversationUrlHeaders()
        get_conversation_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_conversation_url_request = dingtalkim__1__0_models.GetConversationUrlRequest(
            app_user_id='1107****2120',
            user_id='1745****8777',
            open_conversation_id='14da****2760',
            channel_code='M0U+****8Ep='
        )
        try:
            await client.get_conversation_url_with_options_async(get_conversation_url_request, get_conversation_url_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\GetConversationUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\GetConversationUrlRequest;
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
        $getConversationUrlHeaders = new GetConversationUrlHeaders([]);
        $getConversationUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getConversationUrlRequest = new GetConversationUrlRequest([
            "appUserId" => "1107****2120",
            "userId" => "1745****8777",
            "openConversationId" => "14da****2760",
            "channelCode" => "M0U+****8Ep="
        ]);
        try {
            $client->getConversationUrlWithOptions($getConversationUrlRequest, $getConversationUrlHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  getConversationUrlHeaders := &dingtalkim_1_0.GetConversationUrlHeaders{}
  getConversationUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getConversationUrlRequest := &dingtalkim_1_0.GetConversationUrlRequest{
    AppUserId: tea.String("1107****2120"),
    UserId: tea.String("1745****8777"),
    OpenConversationId: tea.String("14da****2760"),
    ChannelCode: tea.String("M0U+****8Ep="),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetConversationUrlWithOptions(getConversationUrlRequest, getConversationUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkim_1_0, * as $dingtalkim_1_0 from '@alicloud/dingtalk/im_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkim_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkim_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getConversationUrlHeaders = new $dingtalkim_1_0.GetConversationUrlHeaders({ });
    getConversationUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getConversationUrlRequest = new $dingtalkim_1_0.GetConversationUrlRequest({
      appUserId: "1107****2120",
      userId: "1745****8777",
      openConversationId: "14da****2760",
      channelCode: "M0U+****8Ep=",
    });
    try {
      await client.getConversationUrlWithOptions(getConversationUrlRequest, getConversationUrlHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetConversationUrlHeaders getConversationUrlHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetConversationUrlHeaders();
            getConversationUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetConversationUrlRequest getConversationUrlRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetConversationUrlRequest
            {
                AppUserId = "1107****2120",
                UserId = "1745****8777",
                OpenConversationId = "14da****2760",
                ChannelCode = "M0U+****8Ep=",
            };
            try
            {
                client.GetConversationUrlWithOptions(getConversationUrlRequest, getConversationUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "url" : "https://****"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | service.nonexist | 钉内账号不存在，请检查 | 钉内账号不存在，请检查 |
| 400 | channel.nonexist | 渠道不存在，请检查 | 渠道不存在，请检查 |
| 400 | group.qrcode.nonexist | 群会话不存在，请检查 | 群会话不存在，请检查 |
| 500 | system.error | 系统异常 | 系统异常 |
