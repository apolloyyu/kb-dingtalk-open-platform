---
title: "创建互通群"
source_url: "https://open.dingtalk.com/document/development/create-an-intercommunication-group"
namespace: "development"
slug: "create-an-intercommunication-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 创建互通群"
doc_id: "Wqnbrpr7YQ"
updated_at: "2025-12-08 10:03:53"
---

> Source: https://open.dingtalk.com/document/development/create-an-intercommunication-group
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 创建互通群
> Updated: 2025-12-08 10:03:53

# 创建互通群

调用本接口创建钉钉客联互通群，支持群类型为普通群、跨钉两人群。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对钉钉客联接口进行了升级。本接口文档已于2023年8月6日迁移至历史文档（不推荐）目录下，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[创建普通群](https://open.dingtalk.com/document/orgapp/create-common-group-new-version)接口。
> - 如果已使用本接口，建议您根据自身实际情况切换至推荐接口。

### 接口使用说明

在将钉外员工与钉内员工建立关联关系后，调用本接口可实现将钉外员工与钉内员工作为群成员，创建一个互通群。

调用本接口成功创建互通群后，效果如下图所示。
![](https://img.alicdn.com/imgextra/i2/O1CN01HmVTY81Oy4zsuT2MZ_!!6000000001773-2-tps-2262-1102.png)

> **[!NOTE]**
>
> 调用本接口之前，需要开通钉钉互联应用：
>
> - 企业内部应用，请参考[如何开通钉钉客联](https://open.dingtalk.com/document/orgapp/dingtalk-customer-contact-product-overview-document)。
> - 第三方企业应用，请参考[如何开通钉钉客联](https://open.dingtalk.com/document/isvapp/dingtalk-customer-contact-product-overview-document)。

### 跨钉两人群特性

> **[!NOTE]**
>
> 前置条件：需要传群模板类型为“跨钉两人群”的群模板，否则创建为普通群。

- **钉外账号1唯一标识**+**钉内账号1唯一标识**组成该群的唯一标识，再次创建会返回同一个群会话。
- 当群里只有**钉外账号1**和**钉内账号1**时，**钉外账号1**看到的群名称和群头像是**钉内账号1**的群名称和群头像，**钉内账号1**看到的群名称和群头像是**钉外账号1**的群名称和群头像。若是其他情况，则看到的是正常的群名称和群头像。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23CreateGroupConversation) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23CreateGroupConversation) |
| 第三方个人应用 | 暂不支持 | 钉钉客联基础数据读写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interconnections/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "groupName" : "String",
  "groupAvatar" : "String",
  "groupTemplateId" : "String",
  "groupOwnerId" : "String",
  "groupOwnerType" : Integer,
  "appUserIds" : [ "String" ],
  "userIds" : [ "String" ],
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
| groupName | String | 是 | 群名称，长度限制为1～64个字符。例如：客户群。 |
| groupAvatar | String | 否 | 群头像地址，长度限制为1～1024个字符。例如：http://\*\*\*.png。 |
| groupTemplateId | String | 是 | 群模板Id，长度限制为1～32个字符。例如：8d42\*\*\*\*nkld。  **[!NOTE]**  本接口创建的互通群，支持的群类型为普通互通群、跨钉两人群和钉外两人群，关联的群模板中的群类型要求是**普通群**、**跨钉两人群**、**钉外两人群**。 |
| groupOwnerId | String | 是 | 群主在业务系统内的唯一标识。  **[!NOTE]**  支持指定钉内账号或钉外账号为群主 ：   - 若是钉内账号userId，长度限制为1～64个字符。例如：1745\*\*\*\*8777。 - 若是钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。例如：1107\*\*\*\*2120。   - 企业内部应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/orgapp/create-bc-account-association)接口获取appUserId参数值。 - 第三方企业应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/isvapp/create-bc-account-association)接口获取appUserId参数值。 |
| groupOwnerType | Integer | 否 | 群主类型，取值：   - **2**：钉内用户 - **3**：钉外用户   **[!NOTE]**  该值不传的情况下，默认是钉内用户。 |
| appUserIds | Array of String | 否 | 钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。例如：1107\*\*\*\*2120。   - 企业内部应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/orgapp/create-bc-account-association)接口获取appUserId参数值。 - 第三方企业应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/isvapp/create-bc-account-association)接口获取appUserId参数值。 |
| userIds | Array of String | 否 | 钉内账号userId，长度限制为1～64个字符。例如：1745\*\*\*\*8777。 |
| operatorId | String | 是 | 操作者在业务系统内的唯一标识。  **[!NOTE]**  支持指定钉内账号或钉外账号为操作者：   - 若是钉内账号userId，长度限制为1～64个字符。例如：1745\*\*\*\*8777。 - 若是钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。例如：1107\*\*\*\*2120。   - 企业内部应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/orgapp/create-bc-account-association)接口获取appUserId参数值。 - 第三方企业应用，调用[创建钉钉客联帐号关联关系](https://open.dingtalk.com/document/isvapp/create-bc-account-association)接口获取appUserId参数值。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversationId | String | 群会话openConversationId。 |
| conversationId | String | 钉钉群会话Id。 |
| appUserIds | Array of String | 添加成功的钉外用户Id列表。 |
| userIds | Array of String | 添加成功的钉内用户userId列表。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/groups HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "groupName" : "客户群",
  "groupAvatar" : "http://***.png",
  "groupTemplateId" : "8d42****nkld",
  "groupOwnerId" : "1745****8777",
  "groupOwnerType" : 2,
  "appUserIds" : [ "1107****2120" ],
  "userIds" : [ "1745****8778" ],
  "operatorId" : "1745****8777"
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
        com.aliyun.dingtalkim_1_0.models.CreateGroupConversationHeaders createGroupConversationHeaders = new com.aliyun.dingtalkim_1_0.models.CreateGroupConversationHeaders();
        createGroupConversationHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.CreateGroupConversationRequest createGroupConversationRequest = new com.aliyun.dingtalkim_1_0.models.CreateGroupConversationRequest()
                .setGroupName("客户群")
                .setGroupAvatar("http://***.png")
                .setGroupTemplateId("8d42****nkld")
                .setGroupOwnerId("1745****8777")
                .setGroupOwnerType(2)
                .setAppUserIds(java.util.Arrays.asList(
                    "1107****2120"
                ))
                .setUserIds(java.util.Arrays.asList(
                    "1745****8778"
                ))
                .setOperatorId("1745****8777");
        try {
            client.createGroupConversationWithOptions(createGroupConversationRequest, createGroupConversationHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_group_conversation_headers = dingtalkim__1__0_models.CreateGroupConversationHeaders()
        create_group_conversation_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_conversation_request = dingtalkim__1__0_models.CreateGroupConversationRequest(
            group_name='客户群',
            group_avatar='http://***.png',
            group_template_id='8d42****nkld',
            group_owner_id='1745****8777',
            group_owner_type=2,
            app_user_ids=[
                '1107****2120'
            ],
            user_ids=[
                '1745****8778'
            ],
            operator_id='1745****8777'
        )
        try:
            client.create_group_conversation_with_options(create_group_conversation_request, create_group_conversation_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_group_conversation_headers = dingtalkim__1__0_models.CreateGroupConversationHeaders()
        create_group_conversation_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_conversation_request = dingtalkim__1__0_models.CreateGroupConversationRequest(
            group_name='客户群',
            group_avatar='http://***.png',
            group_template_id='8d42****nkld',
            group_owner_id='1745****8777',
            group_owner_type=2,
            app_user_ids=[
                '1107****2120'
            ],
            user_ids=[
                '1745****8778'
            ],
            operator_id='1745****8777'
        )
        try:
            await client.create_group_conversation_with_options_async(create_group_conversation_request, create_group_conversation_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateGroupConversationHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\CreateGroupConversationRequest;
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
        $createGroupConversationHeaders = new CreateGroupConversationHeaders([]);
        $createGroupConversationHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createGroupConversationRequest = new CreateGroupConversationRequest([
            "groupName" => "客户群",
            "groupAvatar" => "http://***.png",
            "groupTemplateId" => "8d42****nkld",
            "groupOwnerId" => "1745****8777",
            "groupOwnerType" => 2,
            "appUserIds" => [
                "1107****2120"
            ],
            "userIds" => [
                "1745****8778"
            ],
            "operatorId" => "1745****8777"
        ]);
        try {
            $client->createGroupConversationWithOptions($createGroupConversationRequest, $createGroupConversationHeaders, new RuntimeOptions([]));
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

  createGroupConversationHeaders := &dingtalkim_1_0.CreateGroupConversationHeaders{}
  createGroupConversationHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createGroupConversationRequest := &dingtalkim_1_0.CreateGroupConversationRequest{
    GroupName: tea.String("客户群"),
    GroupAvatar: tea.String("http://***.png"),
    GroupTemplateId: tea.String("8d42****nkld"),
    GroupOwnerId: tea.String("1745****8777"),
    GroupOwnerType: tea.Int32(2),
    AppUserIds: []*string{tea.String("1107****2120")},
    UserIds: []*string{tea.String("1745****8778")},
    OperatorId: tea.String("1745****8777"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateGroupConversationWithOptions(createGroupConversationRequest, createGroupConversationHeaders, &util.RuntimeOptions{})
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
    let createGroupConversationHeaders = new $dingtalkim_1_0.CreateGroupConversationHeaders({ });
    createGroupConversationHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createGroupConversationRequest = new $dingtalkim_1_0.CreateGroupConversationRequest({
      groupName: "客户群",
      groupAvatar: "http://***.png",
      groupTemplateId: "8d42****nkld",
      groupOwnerId: "1745****8777",
      groupOwnerType: 2,
      appUserIds: [
        "1107****2120"
      ],
      userIds: [
        "1745****8778"
      ],
      operatorId: "1745****8777",
    });
    try {
      await client.createGroupConversationWithOptions(createGroupConversationRequest, createGroupConversationHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupConversationHeaders createGroupConversationHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupConversationHeaders();
            createGroupConversationHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupConversationRequest createGroupConversationRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.CreateGroupConversationRequest
            {
                GroupName = "客户群",
                GroupAvatar = "http://***.png",
                GroupTemplateId = "8d42****nkld",
                GroupOwnerId = "1745****8777",
                GroupOwnerType = 2,
                AppUserIds = new List<string>
                {
                    "1107****2120"
                },
                UserIds = new List<string>
                {
                    "1745****8778"
                },
                OperatorId = "1745****8777",
            };
            try
            {
                client.CreateGroupConversationWithOptions(createGroupConversationRequest, createGroupConversationHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "conversationId" : "cidpZ****Vcp4g==",
  "appUserIds" : [ "1107****2120" ],
  "userIds" : [ "1745****8778" ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | general.parameterError | 输入参数有误，请检查是否超出最大值或传参规则不正确 | 输入参数有误，请检查是否超出最大值或传参规则不正确 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | service.nonexist | 钉内账号不存在，请检查 | 钉内账号不存在，请检查 |
| 400 | template.nonexist | 群模板不存在，请检查 | 群模板不存在，请检查 |
| 400 | general.enumError | 入参枚举有误，请检查 | 入参枚举有误，请检查 |
| 400 | image.urlError | 上传群头像失败，请检查图片url是否可用或者图片大小超过1M | 上传群头像失败，请检查图片url是否可用或者图片大小超过1M |
| 400 | request.duplicate | 重复请求，请稍后重试 | 重复请求，请稍后重试 |
| 400 | serviceOwner.nonexist | 群主不存在，群主为钉内账号 | 群主不存在，群主为钉内账号 |
| 400 | clientOwner.nonexist | 群主不存在，群主为钉外账号 | 群主不存在，群主为钉外账号 |
| 400 | client.nameIllegal | 用户名称中包含不合规内容，请检查 | 用户名称中包含不合规内容，请检查 |
| 400 | group.nameIllegal | 群名称中包含不合规内容，请检查 | 群名称中包含不合规内容，请检查 |
| 500 | group.create.error | 创建群失败 | 创建群失败 |
| 500 | system.error | 系统异常 | 系统异常 |
