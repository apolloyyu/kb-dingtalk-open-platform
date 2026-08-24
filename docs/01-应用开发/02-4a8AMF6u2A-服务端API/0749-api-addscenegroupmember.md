---
title: "添加场景群成员"
source_url: "https://open.dingtalk.com/document/development/api-addscenegroupmember"
namespace: "development"
slug: "api-addscenegroupmember"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 添加场景群成员"
doc_id: "mEyjOlnkTo"
updated_at: "2026-08-14 09:41:51"
---

> Source: https://open.dingtalk.com/document/development/api-addscenegroupmember
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 添加场景群成员
> Updated: 2026-08-14 09:41:51

# 添加场景群成员

调用本接口用于向群内新增群成员（群成员人数上限1000），适用于企业需要批量添加成员到群聊的场景，如项目组扩充人员、活动组织新增参与者等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroup/member/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 群会话Id，可通过[创建场景群](0746-create-a-scene-group.md)接口获取。 |
| user\_ids | Array of String | 否 | userid列表。 |
| union\_ids | Array of String | 否 | unionId列表。 |

### 请求示例

HTTP

```
POST /v1.0/im/sceneGroup/member/add HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1b*****
Content-Type:application/json

{
  "open_conversation_id" : "cidxxxxxx==",
  "user_ids" : [ "1107****2120" ],
  "union_ids" : [ "1107****2120" ]
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
        com.aliyun.dingtalkim_1_0.models.AddSceneGroupMemberHeaders addSceneGroupMemberHeaders = new com.aliyun.dingtalkim_1_0.models.AddSceneGroupMemberHeaders();
        addSceneGroupMemberHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.AddSceneGroupMemberRequest addSceneGroupMemberRequest = new com.aliyun.dingtalkim_1_0.models.AddSceneGroupMemberRequest()
                .setOpenConversationId("cidxxxxxx==")
                .setUserIds(java.util.Arrays.asList(
                    "1107****2120"
                ))
                .setUnionIds(java.util.Arrays.asList(
                    "1107****2120"
                ));
        try {
            client.addSceneGroupMemberWithOptions(addSceneGroupMemberRequest, addSceneGroupMemberHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_scene_group_member_headers = dingtalkim__1__0_models.AddSceneGroupMemberHeaders()
        add_scene_group_member_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_scene_group_member_request = dingtalkim__1__0_models.AddSceneGroupMemberRequest(
            open_conversation_id='cidxxxxxx==',
            user_ids=[
                '1107****2120'
            ],
            union_ids=[
                '1107****2120'
            ]
        )
        try:
            client.add_scene_group_member_with_options(add_scene_group_member_request, add_scene_group_member_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_scene_group_member_headers = dingtalkim__1__0_models.AddSceneGroupMemberHeaders()
        add_scene_group_member_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_scene_group_member_request = dingtalkim__1__0_models.AddSceneGroupMemberRequest(
            open_conversation_id='cidxxxxxx==',
            user_ids=[
                '1107****2120'
            ],
            union_ids=[
                '1107****2120'
            ]
        )
        try:
            await client.add_scene_group_member_with_options_async(add_scene_group_member_request, add_scene_group_member_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\AddSceneGroupMemberHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\AddSceneGroupMemberRequest;
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
        $addSceneGroupMemberHeaders = new AddSceneGroupMemberHeaders([]);
        $addSceneGroupMemberHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addSceneGroupMemberRequest = new AddSceneGroupMemberRequest([
            "openConversationId" => "cidxxxxxx==",
            "userIds" => [
                "1107****2120"
            ],
            "unionIds" => [
                "1107****2120"
            ]
        ]);
        try {
            $client->addSceneGroupMemberWithOptions($addSceneGroupMemberRequest, $addSceneGroupMemberHeaders, new RuntimeOptions([]));
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

  addSceneGroupMemberHeaders := &dingtalkim_1_0.AddSceneGroupMemberHeaders{}
  addSceneGroupMemberHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addSceneGroupMemberRequest := &dingtalkim_1_0.AddSceneGroupMemberRequest{
    OpenConversationId: tea.String("cidxxxxxx=="),
    UserIds: []*string{tea.String("1107****2120")},
    UnionIds: []*string{tea.String("1107****2120")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddSceneGroupMemberWithOptions(addSceneGroupMemberRequest, addSceneGroupMemberHeaders, &util.RuntimeOptions{})
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
    let addSceneGroupMemberHeaders = new dingtalkim_1_0.AddSceneGroupMemberHeaders({ });
    addSceneGroupMemberHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let addSceneGroupMemberRequest = new dingtalkim_1_0.AddSceneGroupMemberRequest({
      openConversationId: 'cidxxxxxx==',
      userIds: [
        '1107****2120'
      ],
      unionIds: [
        '1107****2120'
      ],
    });
    try {
      await client.addSceneGroupMemberWithOptions(addSceneGroupMemberRequest, addSceneGroupMemberHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.AddSceneGroupMemberHeaders addSceneGroupMemberHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.AddSceneGroupMemberHeaders();
            addSceneGroupMemberHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.AddSceneGroupMemberRequest addSceneGroupMemberRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.AddSceneGroupMemberRequest
            {
                OpenConversationId = "cidxxxxxx==",
                UserIds = new List<string>
                {
                    "1107****2120"
                },
                UnionIds = new List<string>
                {
                    "1107****2120"
                },
            };
            try
            {
                client.AddSceneGroupMemberWithOptions(addSceneGroupMemberRequest, addSceneGroupMemberHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 调用是否成功：   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.invalid | 输入参数错误 | 根据接口要求，传入必要参数。 |
| 400 | permession.checkFailed | 权限校验失败 | 权限校验失败 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 500 | system.error | 请重试，若始终失败请提交工单 | 请重试，若始终失败请提交工单 |
