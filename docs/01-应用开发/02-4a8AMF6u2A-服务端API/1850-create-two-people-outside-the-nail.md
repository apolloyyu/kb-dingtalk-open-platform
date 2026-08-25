---
title: "创建钉外两人群"
source_url: "https://open.dingtalk.com/document/development/create-two-people-outside-the-nail"
namespace: "development"
slug: "create-two-people-outside-the-nail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 创建钉外两人群"
doc_id: "Hncnf5uQth"
updated_at: "2025-09-08 19:06:12"
---

> Source: https://open.dingtalk.com/document/development/create-two-people-outside-the-nail
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 创建钉外两人群
> Updated: 2025-09-08 19:06:12

# 创建钉外两人群

调用本接口创建钉外两人群。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对钉钉客联接口进行了升级。本接口文档已于2023年8月6日迁移至历史文档（不推荐）目录下，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[创建两人群](https://open.dingtalk.com/document/orgapp/creating-two-groups-of-people)接口。
> - 如果已使用本接口，建议您根据自身实际情况切换至推荐接口。

### 接口使用说明

由于钉外两人群的成员都是钉外账号，因此调用本接口创建的钉外两人群，在钉钉客户端内不会显示。

钉外账号可根据H5会话地址打开会话列表或钉外两人群：

- 企业内部应用，可调用[获取钉钉客联群会话地址](https://open.dingtalk.com/document/orgapp/get-the-dingtalk-guest-group-session-address)接口获取url。
- 第三方企业应用，可调用[获取钉钉客联群会话地址](https://open.dingtalk.com/document/isvapp/obtain-the-session-address)接口获取url。

> **[!NOTE]**
>
> 调用本接口之前，需要开通钉钉互联应用：
>
> - 企业内部应用，请参考[如何开通钉钉客联](https://open.dingtalk.com/document/orgapp/dingtalk-customer-contact-product-overview-document)。
> - 第三方企业应用，请参考[如何开通钉钉客联](https://open.dingtalk.com/document/isvapp/dingtalk-customer-contact-product-overview-document)。

### 钉外两人群特性

> **[!NOTE]**
>
> 前置条件：需要传群模板类型为“钉外两人群”的群模板，否则创建为普通群。

- **钉外账号1唯一标识**+**钉外账号2唯一标识**组成该群的唯一标识，再次创建会返回同一个群会话。
- 当群里只有**钉外账号1**和**钉外账号2**时，**钉外账号1**看到的群名称和群头像是**钉外账号2**的群名称和群头像，**钉外账号2**看到的群名称和群头像是**钉外账号1**的群名称和群头像。若是其他情况，则看到的是正常的群名称和群头像。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23CreateCoupleGroupConversation) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23CreateCoupleGroupConversation) |
| 第三方个人应用 | 暂不支持 | 钉钉客联基础数据读写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interconnections/coupleGroups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "groupName" : "String",
  "groupAvatar" : "String",
  "groupTemplateId" : "String",
  "groupOwnerId" : "String",
  "appUserId" : "String",
  "operatorId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| groupName | String | 是 | 群名称，长度限制为1～64个字符。例如：钉外两人群。 |
| groupAvatar | String | 否 | 群头像地址，长度限制为1～1024个字符。例如：http://\*\*\*.png。 |
| groupTemplateId | String | 是 | 群模板Id，长度限制为1～32个字符。例如：8d42\*\*\*\*nkld。  **[!NOTE]**  本接口创建的互通群，支持的群类型为钉外两人群，关联的群模板中的群类型要求是**钉外两人群**。 |
| groupOwnerId | String | 是 | 群主在业务系统内的唯一标识。  **[!NOTE]**  群主为钉外账号：   - 钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。例如：1107\*\*\*\*2120。 |
| appUserId | String | 是 | 钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。例如：1107\*\*\*\*2120。   - 企业内部应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/orgapp/create-bc-account-association)接口获取appUserId参数值。 - 第三方企业应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/isvapp/create-bc-account-association)接口获取appUserId参数值。 |
| operatorId | String | 是 | 操作者在业务系统内的唯一标识。  **[!NOTE]**  支持指定钉内账号或钉外账号为操作者：   - 若是钉内账号userId，长度限制为1～64个字符。例如：1745\*\*\*\*8777。 - 若是钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。例如：1107\*\*\*\*2120。   - 企业内部应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/orgapp/create-bc-account-association)接口获取appUserId参数值。 - 第三方企业应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/isvapp/create-bc-account-association)接口获取appUserId参数值。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversationId | String | 群会话Id。 |
| conversationId | String | 钉钉群会话Id。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/coupleGroups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "groupName" : "钉外两人群",
  "groupAvatar" : "http://***.png",
  "groupTemplateId" : "8d42****nkld",
  "groupOwnerId" : "1107****2120",
  "appUserId" : "1107****2121",
  "operatorId" : "1107****2120"
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
        com.aliyun.dingtalkim_1_0.models.CreateCoupleGroupConversationHeaders createCoupleGroupConversationHeaders = new com.aliyun.dingtalkim_1_0.models.CreateCoupleGroupConversationHeaders();
        createCoupleGroupConversationHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.CreateCoupleGroupConversationRequest createCoupleGroupConversationRequest = new com.aliyun.dingtalkim_1_0.models.CreateCoupleGroupConversationRequest()
                .setGroupName("钉外两人群")
                .setGroupAvatar("http://***.png")
                .setGroupTemplateId("8d42****nkld")
                .setGroupOwnerId("1107****2120")
                .setAppUserId("1107****2121")
                .setOperatorId("1107****2120");
        try {
            client.createCoupleGroupConversationWithOptions(createCoupleGroupConversationRequest, createCoupleGroupConversationHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_couple_group_conversation_headers = dingtalkim__1__0_models.CreateCoupleGroupConversationHeaders()
        create_couple_group_conversation_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_couple_group_conversation_request = dingtalkim__1__0_models.CreateCoupleGroupConversationRequest(
            group_name='钉外两人群',
            group_avatar='http://***.png',
            group_template_id='8d42****nkld',
            group_owner_id='1107****2120',
            app_user_id='1107****2121',
            operator_id='1107****2120'
        )
        try:
            client.create_couple_group_conversation_with_options(create_couple_group_conversation_request, create_couple_group_conversation_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_couple_group_conversation_headers = dingtalkim__1__0_models.CreateCoupleGroupConversationHeaders()
        create_couple_group_conversation_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_couple_group_conversation_request = dingtalkim__1__0_models.CreateCoupleGroupConversationRequest(
            group_name='钉外两人群',
            group_avatar='http://***.png',
            group_template_id='8d42****nkld',
            group_owner_id='1107****2120',
            app_user_id='1107****2121',
            operator_id='1107****2120'
        )
        try:
            await client.create_couple_group_conversation_with_options_async(create_couple_group_conversation_request, create_couple_group_conversation_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateCoupleGroupConversationHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateCoupleGroupConversationRequest;
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
        $createCoupleGroupConversationHeaders = new CreateCoupleGroupConversationHeaders([]);
        $createCoupleGroupConversationHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createCoupleGroupConversationRequest = new CreateCoupleGroupConversationRequest([
            "groupName" => "钉外两人群",
            "groupAvatar" => "http://***.png",
            "groupTemplateId" => "8d42****nkld",
            "groupOwnerId" => "1107****2120",
            "appUserId" => "1107****2121",
            "operatorId" => "1107****2120"
        ]);
        try {
            $client->createCoupleGroupConversationWithOptions($createCoupleGroupConversationRequest, $createCoupleGroupConversationHeaders, new RuntimeOptions([]));
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

  createCoupleGroupConversationHeaders := &dingtalkim_1_0.CreateCoupleGroupConversationHeaders{}
  createCoupleGroupConversationHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createCoupleGroupConversationRequest := &dingtalkim_1_0.CreateCoupleGroupConversationRequest{
    GroupName: tea.String("钉外两人群"),
    GroupAvatar: tea.String("http://***.png"),
    GroupTemplateId: tea.String("8d42****nkld"),
    GroupOwnerId: tea.String("1107****2120"),
    AppUserId: tea.String("1107****2121"),
    OperatorId: tea.String("1107****2120"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateCoupleGroupConversationWithOptions(createCoupleGroupConversationRequest, createCoupleGroupConversationHeaders, &util.RuntimeOptions{})
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
    let createCoupleGroupConversationHeaders = new $dingtalkim_1_0.CreateCoupleGroupConversationHeaders({ });
    createCoupleGroupConversationHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createCoupleGroupConversationRequest = new $dingtalkim_1_0.CreateCoupleGroupConversationRequest({
      groupName: "钉外两人群",
      groupAvatar: "http://***.png",
      groupTemplateId: "8d42****nkld",
      groupOwnerId: "1107****2120",
      appUserId: "1107****2121",
      operatorId: "1107****2120",
    });
    try {
      await client.createCoupleGroupConversationWithOptions(createCoupleGroupConversationRequest, createCoupleGroupConversationHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateCoupleGroupConversationHeaders createCoupleGroupConversationHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateCoupleGroupConversationHeaders();
            createCoupleGroupConversationHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateCoupleGroupConversationRequest createCoupleGroupConversationRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateCoupleGroupConversationRequest
            {
                GroupName = "钉外两人群",
                GroupAvatar = "http://***.png",
                GroupTemplateId = "8d42****nkld",
                GroupOwnerId = "1107****2120",
                AppUserId = "1107****2121",
                OperatorId = "1107****2120",
            };
            try
            {
                client.CreateCoupleGroupConversationWithOptions(createCoupleGroupConversationRequest, createCoupleGroupConversationHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "openConversationId" : "14da****2760",
  "conversationId" : "cid****8Q=="
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否超出最大值或传参规则不正确 | 输入参数有误，请检查是否超出最大值或传参规则不正确 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | template.nonexist | 群模板不存在，请检查 | 群模板不存在，请检查 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | coupleGroup.memberError | 两人群需要指定两个钉外账号，请检查 | 两人群需要指定两个钉外账号，请检查 |
| 400 | request.duplicate | 重复请求，请稍后重试 | 重复请求，请稍后重试 |
| 400 | clientOwner.nonexist | 群主不存在，群主为钉外账号 | 群主不存在，群主为钉外账号 |
| 400 | client.nameIllegal | 用户名称中包含不合规内容，请检查 | 用户名称中包含不合规内容，请检查 |
| 400 | group.nameIllegal | 群名称中包含不合规内容，请检查 | 群名称中包含不合规内容，请检查 |
| 500 | group.create.error | 创建群失败 | 创建群失败 |
| 500 | system.error | 系统异常 | 系统异常 |
