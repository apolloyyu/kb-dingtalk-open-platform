---
title: "批量查询跨钉两人互通群列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-session-information-of-two-population-groups"
namespace: "development"
slug: "queries-the-session-information-of-two-population-groups"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 批量查询跨钉两人互通群列表"
doc_id: "x1Vvskg84R"
updated_at: "2026-07-21 10:01:40"
---

> Source: https://open.dingtalk.com/document/development/queries-the-session-information-of-two-population-groups
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 批量查询跨钉两人互通群列表
> Updated: 2026-07-21 10:01:40

# 批量查询跨钉两人互通群列表

调用本接口，可根据钉内成员userId和钉外成员标识，查询两者共同存在的互通群列表。

### 接口使用说明

- 该接口**已经暂停新客户支持**，进入EOL（end of life）阶段，敬请期待新的开放能力支持。
- 调用本接口之前，需要开通钉钉互联应用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=im_1.0%23QuerySingleGroup) |
| 第三方企业应用 | 支持 | 钉钉客联基础数据读写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=im_1.0%23QuerySingleGroup) |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/im/interconnections/doubleGroups/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "groupTemplateId" : "String",
  "groupMembers" : [ {
    "appUserId" : "String",
    "userId" : "String"
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
| groupTemplateId | String | 是 | 群模板Id，获取方式请参考[群模板配置](1838-interconnections-model.md)文档， 长度限制为1～32个字符，例如：8d42\*\*\*\*nkld。  **[!NOTE]**    本接口查询的是跨钉两人群，模板ID需要传群类型为**跨钉两人群**的模板。 |
| groupMembers | Array | 是 | 群成员列表，最大值20。 |
| appUserId | String | 是 | 钉外账号在业务系统内的唯一标志，调用[创建钉钉客联钉外账号](1844-create-bc-account-association.md)接口获取，长度限制为1～64个字符，例如：1107\*\*\*\*2120。 |
| userId | String | 是 | 钉内账号userId，长度限制为1～64个字符，例如：1745\*\*\*\*8777。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| openConversations | Array | 群列表。 |
| openConversationId | String | 钉钉客联群会话openConversationId。  **[!NOTE]**    客联的群会话id与钉钉IM的群会话ID不同，客联的群会话ID是随机生成的，在使用时不可混用。 |
| appUserId | String | 钉外账号在业务系统内的唯一标志，长度限制为1～64个字符。 |
| userId | String | 钉内账号userId，长度限制为1～64个字符。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/im/interconnections/doubleGroups/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "groupTemplateId" : "14da****2760",
  "groupMembers" : [ {
    "appUserId" : "1107****2120",
    "userId" : "1745****8778"
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
        com.aliyun.dingtalkim_1_0.models.QuerySingleGroupHeaders querySingleGroupHeaders = new com.aliyun.dingtalkim_1_0.models.QuerySingleGroupHeaders();
        querySingleGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.QuerySingleGroupRequest.QuerySingleGroupRequestGroupMembers groupMembers0 = new com.aliyun.dingtalkim_1_0.models.QuerySingleGroupRequest.QuerySingleGroupRequestGroupMembers()
                .setAppUserId("1107****2120")
                .setUserId("1745****8778");
        com.aliyun.dingtalkim_1_0.models.QuerySingleGroupRequest querySingleGroupRequest = new com.aliyun.dingtalkim_1_0.models.QuerySingleGroupRequest()
                .setGroupTemplateId("14da****2760")
                .setGroupMembers(java.util.Arrays.asList(
                    groupMembers0
                ));
        try {
            client.querySingleGroupWithOptions(querySingleGroupRequest, querySingleGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_single_group_headers = dingtalkim__1__0_models.QuerySingleGroupHeaders()
        query_single_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        group_members_0 = dingtalkim__1__0_models.QuerySingleGroupRequestGroupMembers(
            app_user_id='1107****2120',
            user_id='1745****8778'
        )
        query_single_group_request = dingtalkim__1__0_models.QuerySingleGroupRequest(
            group_template_id='14da****2760',
            group_members=[
                group_members_0
            ]
        )
        try:
            client.query_single_group_with_options(query_single_group_request, query_single_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_single_group_headers = dingtalkim__1__0_models.QuerySingleGroupHeaders()
        query_single_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        group_members_0 = dingtalkim__1__0_models.QuerySingleGroupRequestGroupMembers(
            app_user_id='1107****2120',
            user_id='1745****8778'
        )
        query_single_group_request = dingtalkim__1__0_models.QuerySingleGroupRequest(
            group_template_id='14da****2760',
            group_members=[
                group_members_0
            ]
        )
        try:
            await client.query_single_group_with_options_async(query_single_group_request, query_single_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QuerySingleGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QuerySingleGroupRequest\groupMembers;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QuerySingleGroupRequest;
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
        $querySingleGroupHeaders = new QuerySingleGroupHeaders([]);
        $querySingleGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $groupMembers0 = new groupMembers([
            "appUserId" => "1107****2120",
            "userId" => "1745****8778"
        ]);
        $querySingleGroupRequest = new QuerySingleGroupRequest([
            "groupTemplateId" => "14da****2760",
            "groupMembers" => [
                $groupMembers0
            ]
        ]);
        try {
            $client->querySingleGroupWithOptions($querySingleGroupRequest, $querySingleGroupHeaders, new RuntimeOptions([]));
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

  querySingleGroupHeaders := &dingtalkim_1_0.QuerySingleGroupHeaders{}
  querySingleGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  groupMembers0 := &dingtalkim_1_0.QuerySingleGroupRequestGroupMembers{
    AppUserId: tea.String("1107****2120"),
    UserId: tea.String("1745****8778"),
  }
  querySingleGroupRequest := &dingtalkim_1_0.QuerySingleGroupRequest{
    GroupTemplateId: tea.String("14da****2760"),
    GroupMembers: []*dingtalkim_1_0.QuerySingleGroupRequestGroupMembers{groupMembers0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QuerySingleGroupWithOptions(querySingleGroupRequest, querySingleGroupHeaders, &util.RuntimeOptions{})
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
    let querySingleGroupHeaders = new $dingtalkim_1_0.QuerySingleGroupHeaders({ });
    querySingleGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let groupMembers0 = new $dingtalkim_1_0.QuerySingleGroupRequestGroupMembers({
      appUserId: "1107****2120",
      userId: "1745****8778",
    });
    let querySingleGroupRequest = new $dingtalkim_1_0.QuerySingleGroupRequest({
      groupTemplateId: "14da****2760",
      groupMembers: [
        groupMembers0
      ],
    });
    try {
      await client.querySingleGroupWithOptions(querySingleGroupRequest, querySingleGroupHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupHeaders querySingleGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupHeaders();
            querySingleGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupRequest.QuerySingleGroupRequestGroupMembers groupMembers0 = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupRequest.QuerySingleGroupRequestGroupMembers
            {
                AppUserId = "1107****2120",
                UserId = "1745****8778",
            };
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupRequest querySingleGroupRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupRequest
            {
                GroupTemplateId = "14da****2760",
                GroupMembers = new List<AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySingleGroupRequest.QuerySingleGroupRequestGroupMembers>
                {
                    groupMembers0
                },
            };
            try
            {
                client.QuerySingleGroupWithOptions(querySingleGroupRequest, querySingleGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "openConversations" : [ {
    "openConversationId" : "14da****2760",
    "appUserId" : "1107****2120",
    "userId" : "1745****8778"
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | group.num.overlimit | 查询群个群超出阈值，请检查 | 查询群个群超出阈值，请检查 |
| 400 | aim.nonexist | 租户不存在，请检查 | 租户不存在，请检查 |
| 400 | template.nonexist | 群模板不存在，请检查 | 群模板不存在，请检查 |
| 400 | template.mismatch | 群模板类型不匹配 | 群模板类型不匹配 |
| 500 | system.error | 系统异常 | 系统异常 |
