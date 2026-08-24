---
title: "查询场景群成员"
source_url: "https://open.dingtalk.com/document/development/query-group-members"
namespace: "development"
slug: "query-group-members"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群成员"
doc_id: "PqCzlH6p65"
updated_at: "2026-08-14 09:41:53"
---

> Source: https://open.dingtalk.com/document/development/query-group-members
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群成员
> Updated: 2026-08-14 09:41:53

# 查询场景群成员

调用本接口，查询群成员信息，适用于需要获取群成员信息的场景，如在群管理界面展示群成员列表、统计群成员数量等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/members/batchQuery |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群ID：   - 基于群模板创建的群，可调用[创建群](1484-create-a-scene-group-v2.md)接口获取`open_conversation_id`参数值。 - 安装群聊酷应用的群，通过[安装酷应用入群](../03-Ogu5SlPY4t-客户端JSAPI/0273-install-coothe-group.md)获取返回参数`openConversationId`参数值。 |
| coolAppCode | String | 否 | 群聊酷应用编码：   - 基于群模板创建的群，不需要传入此参数。 - 安装群聊酷应用的群，**必须**传入此参数。 |
| maxResults | Long | 是 | 分页大小。      接口返回结果可能会大于或小于maxResults，以实际返回结果为准。如果群成员数量不超过1000，而直接一次性返回全部群成员；如果群成员数量大于1000，则按照分页大小分批次返回。 |
| nextToken | String | 否 | 分页游标，置空表示从首页开始查询。 |

### 请求示例

HTTP

```
POST /v1.0/im/sceneGroups/members/batchQuery HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:beE4*****75d
Content-Type:application/json

{
  "openConversationId" : "cidxxxc354",
  "coolAppCode" : "COOLAPP_XXXXX",
  "maxResults" : 200,
  "nextToken" : "10"
}
```

Java

```
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
        com.aliyun.dingtalkim_1_0.models.BatchQueryGroupMemberHeaders batchQueryGroupMemberHeaders = new com.aliyun.dingtalkim_1_0.models.BatchQueryGroupMemberHeaders();
        batchQueryGroupMemberHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.BatchQueryGroupMemberRequest batchQueryGroupMemberRequest = new com.aliyun.dingtalkim_1_0.models.BatchQueryGroupMemberRequest()
                .setOpenConversationId("cidxxxc354")
                .setCoolAppCode("COOLAPP_XXXXX")
                .setMaxResults(200L)
                .setNextToken("10");
        try {
            client.batchQueryGroupMemberWithOptions(batchQueryGroupMemberRequest, batchQueryGroupMemberHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

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
        batch_query_group_member_headers = dingtalkim__1__0_models.BatchQueryGroupMemberHeaders()
        batch_query_group_member_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_query_group_member_request = dingtalkim__1__0_models.BatchQueryGroupMemberRequest(
            open_conversation_id='cidxxxc354',
            cool_app_code='COOLAPP_XXXXX',
            max_results=200,
            next_token='10'
        )
        try:
            client.batch_query_group_member_with_options(batch_query_group_member_request, batch_query_group_member_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_query_group_member_headers = dingtalkim__1__0_models.BatchQueryGroupMemberHeaders()
        batch_query_group_member_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_query_group_member_request = dingtalkim__1__0_models.BatchQueryGroupMemberRequest(
            open_conversation_id='cidxxxc354',
            cool_app_code='COOLAPP_XXXXX',
            max_results=200,
            next_token='10'
        )
        try:
            await client.batch_query_group_member_with_options_async(batch_query_group_member_request, batch_query_group_member_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\BatchQueryGroupMemberHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\BatchQueryGroupMemberRequest;
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
        $batchQueryGroupMemberHeaders = new BatchQueryGroupMemberHeaders([]);
        $batchQueryGroupMemberHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchQueryGroupMemberRequest = new BatchQueryGroupMemberRequest([
            "openConversationId" => "cidxxxc354",
            "coolAppCode" => "COOLAPP_XXXXX",
            "maxResults" => 200,
            "nextToken" => "10"
        ]);
        try {
            $client->batchQueryGroupMemberWithOptions($batchQueryGroupMemberRequest, $batchQueryGroupMemberHeaders, new RuntimeOptions([]));
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

  batchQueryGroupMemberHeaders := &dingtalkim_1_0.BatchQueryGroupMemberHeaders{}
  batchQueryGroupMemberHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchQueryGroupMemberRequest := &dingtalkim_1_0.BatchQueryGroupMemberRequest{
    OpenConversationId: tea.String("cidxxxc354"),
    CoolAppCode: tea.String("COOLAPP_XXXXX"),
    MaxResults: tea.Int64(200),
    NextToken: tea.String("10"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchQueryGroupMemberWithOptions(batchQueryGroupMemberRequest, batchQueryGroupMemberHeaders, &util.RuntimeOptions{})
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
    let batchQueryGroupMemberHeaders = new dingtalkim_1_0.BatchQueryGroupMemberHeaders({ });
    batchQueryGroupMemberHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let batchQueryGroupMemberRequest = new dingtalkim_1_0.BatchQueryGroupMemberRequest({
      openConversationId: 'cidxxxc354',
      coolAppCode: 'COOLAPP_XXXXX',
      maxResults: 200,
      nextToken: '10',
    });
    try {
      await client.batchQueryGroupMemberWithOptions(batchQueryGroupMemberRequest, batchQueryGroupMemberHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.BatchQueryGroupMemberHeaders batchQueryGroupMemberHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.BatchQueryGroupMemberHeaders();
            batchQueryGroupMemberHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.BatchQueryGroupMemberRequest batchQueryGroupMemberRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.BatchQueryGroupMemberRequest
            {
                OpenConversationId = "cidxxxc354",
                CoolAppCode = "COOLAPP_XXXXX",
                MaxResults = 200,
                NextToken = "10",
            };
            try
            {
                client.BatchQueryGroupMemberWithOptions(batchQueryGroupMemberRequest, batchQueryGroupMemberHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 请求是否成功：   - **true**：执行成功 - **false**：执行失败 |
| memberUserIds | Array of String | 群成员id。 |
| hasMore | Boolean | 是否还有更多数据。 |
| nextToken | String | 下一次请求的游标，若没有更多数据，则此参数为空。 |
| unionIdList | Array of String | 企业外成员的unionId。 |
| staffIdNickMap | Map<String, String> | 企业内员工的名称。 |
| unionIdNickMap | Map<String, String> | 企业成员的名称。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "memberUserIds" : [ "manager7675" ],
  "hasMore" : false,
  "nextToken" : "92233720368",
  "unionIdList" : [ "un123456" ],
  "staffIdNickMap" : {
    "key" : "nick1"
  },
  "unionIdNickMap" : {
    "key" : "nick2"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | groupPermissionDenied | 无权限，该群没有安装群模板 | 无权限，该群没有安装群模板 |
| 400 | paramIllegal | 请求参数非法 | 请求参数非法 |
| 400 | paramBlank | 请求参数为空 | 请求参数为空 |
| 400 | cidEncryptError | 群ID解析错误 | 群ID解析错误 |
| 400 | groupTemplatePermissionDenied | 无权限，该群安装的群模板不属于当前token对应的应用名下 | 无权限，该群安装的群模板不属于当前token对应的应用名下 |
| 400 | coolAppUninstalled | 无权限，该群没有安装群聊酷应用 | 无权限，该群没有安装群聊酷应用 |
| 400 | coolAppUnexist | 群聊酷应用不存在 | 群聊酷应用不存在，请检查酷应用编码是否正确 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 400 | coolAppPermissionDenied | 无权限，指定的群聊酷应用不属于当前token对应的应用名下 | 无权限，指定的群聊酷应用不属于当前token对应的应用名下 |
| 400 | systemError | 系统异常 | 系统内部异常 |
| 400 | auth.error | %s | 权限校验不通过 |
