---
title: "查询钉钉客联互通群成员列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-group-member-list"
namespace: "development"
slug: "queries-the-group-member-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 查询钉钉客联互通群成员列表"
doc_id: "6kjA8cbsjB"
updated_at: "2026-07-22 16:48:02"
---

> Source: https://open.dingtalk.com/document/development/queries-the-group-member-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 查询钉钉客联互通群成员列表
> Updated: 2026-07-22 16:48:02

# 查询钉钉客联互通群成员列表

调用本接口，查询互通群成员列表，用户类型包括钉内成员、钉外成员、群机器人；内容包括成员名称、头像地址、用户类型等。

### 接口使用说明

> **[!NOTE]**
>
> - 该接口**已经暂停新客户支持**，进入EOL（end of life）阶段，敬请期待新的开放能力支持。
> - 调用本接口之前，需要开通钉钉互联应用。

例如，名为**普通群**的互通群，成员信息如下图所示。
![](https://img.alicdn.com/imgextra/i4/O1CN01xlL05c1hHSqNYZdBe_!!6000000004252-2-tps-2270-1162.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23QueryGroupMember) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23QueryGroupMember) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
GET /v1.0/im/interconnections/conversations/members?openConversationId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群会话openConversationId，可调用[创建钉钉客联普通互通群](1848-create-common-group-new-version.md) / [创建钉钉客联两人互通群](1849-creating-two-groups-of-people.md)接口获取，长度限制为1～32个字符，例如：14da\*\*\*\*2760。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversationId | String | 群会话openConversationId。  **[!NOTE]**    客联的群会话id与钉钉IM的群会话ID不同，客联的群会话ID是随机生成的，在使用时不可混用。 |
| groupMembers | Array | 群成员列表。 |
| groupMemberId | String | 群成员Id。   - 如果是钉内用户，该字段值为userId。 - 如果是钉外用户，该字段值为业务标识。 |
| groupMemberName | String | 群成员名称。 |
| groupMemberType | Integer | 群成员类型，取值：   - **1**：群主(属于钉内成员) - **2**：钉内成员 - **3**：钉外成员 - **4**：群机器人 |
| groupMemberAvatar | String | 群成员头像地址。 |
| groupMemberAvatarMediaId | String | 群成员头像mediaId，可通过调用[查询钉钉客联互通群成员列表](1858-queries-the-group-member-list.md)接口获取返回的groupMemberAvatarMediaId值。 |
| groupMemberDynamics | String | 群成员头像mediaId，可通过调用[查询钉钉客联互通群成员列表](1858-queries-the-group-member-list.md)接口获取返回的groupMemberDynamics值。 |
| groupMemberTypeV2 | Integer | 群成员类型V2 当groupMemberType类型为群主时，通过这个字段判断成员的实际类型如钉内群成员。 2 钉内群成员 3 钉外群成员 |
| appUid | Long | 客联租户内IM唯一id |

## 示例

**请求示例**

HTTP

```
GET /v1.0/im/interconnections/conversations/members?openConversationId=14da****2760 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
        com.aliyun.dingtalkim_1_0.models.QueryGroupMemberHeaders queryGroupMemberHeaders = new com.aliyun.dingtalkim_1_0.models.QueryGroupMemberHeaders();
        queryGroupMemberHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.QueryGroupMemberRequest queryGroupMemberRequest = new com.aliyun.dingtalkim_1_0.models.QueryGroupMemberRequest()
                .setOpenConversationId("14da****2760");
        try {
            client.queryGroupMemberWithOptions(queryGroupMemberRequest, queryGroupMemberHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_group_member_headers = dingtalkim__1__0_models.QueryGroupMemberHeaders()
        query_group_member_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_group_member_request = dingtalkim__1__0_models.QueryGroupMemberRequest(
            open_conversation_id='14da****2760'
        )
        try:
            client.query_group_member_with_options(query_group_member_request, query_group_member_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_group_member_headers = dingtalkim__1__0_models.QueryGroupMemberHeaders()
        query_group_member_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_group_member_request = dingtalkim__1__0_models.QueryGroupMemberRequest(
            open_conversation_id='14da****2760'
        )
        try:
            await client.query_group_member_with_options_async(query_group_member_request, query_group_member_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QueryGroupMemberHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QueryGroupMemberRequest;
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
        $queryGroupMemberHeaders = new QueryGroupMemberHeaders([]);
        $queryGroupMemberHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryGroupMemberRequest = new QueryGroupMemberRequest([
            "openConversationId" => "14da****2760"
        ]);
        try {
            $client->queryGroupMemberWithOptions($queryGroupMemberRequest, $queryGroupMemberHeaders, new RuntimeOptions([]));
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

  queryGroupMemberHeaders := &dingtalkim_1_0.QueryGroupMemberHeaders{}
  queryGroupMemberHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryGroupMemberRequest := &dingtalkim_1_0.QueryGroupMemberRequest{
    OpenConversationId: tea.String("14da****2760"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryGroupMemberWithOptions(queryGroupMemberRequest, queryGroupMemberHeaders, &util.RuntimeOptions{})
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
    let queryGroupMemberHeaders = new dingtalkim_1_0.QueryGroupMemberHeaders({ });
    queryGroupMemberHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryGroupMemberRequest = new dingtalkim_1_0.QueryGroupMemberRequest({
      openConversationId: '14da****2760',
    });
    try {
      await client.queryGroupMemberWithOptions(queryGroupMemberRequest, queryGroupMemberHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMemberHeaders queryGroupMemberHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMemberHeaders();
            queryGroupMemberHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMemberRequest queryGroupMemberRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QueryGroupMemberRequest
            {
                OpenConversationId = "14da****2760",
            };
            try
            {
                client.QueryGroupMemberWithOptions(queryGroupMemberRequest, queryGroupMemberHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "groupMembers" : [ {
    "groupMemberId" : "1107****2120",
    "groupMemberName" : "Foo",
    "groupMemberType" : 1,
    "groupMemberAvatar" : "http://****.png",
    "groupMemberAvatarMediaId" : "abc",
    "groupMemberDynamics" : "认真工作,快乐生活",
    "groupMemberTypeV2" : 2,
    "appUid" : 1000000
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | group.nonexist | 群不存在，请检查 | 群不存在，请检查 |
| 400 | template.nonexist | 群模板不存在，请检查 | 群模板不存在，请检查 |
| 500 | system.error | 系统异常 | 系统异常 |
