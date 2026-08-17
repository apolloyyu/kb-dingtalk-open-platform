---
title: "更新场景群管理员"
source_url: "https://open.dingtalk.com/document/development/update-group-administrators"
namespace: "development"
slug: "update-group-administrators"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 更新场景群管理员"
doc_id: "a9nGMwKy69"
updated_at: "2026-05-10 01:06:15"
---

> Source: https://open.dingtalk.com/document/development/update-group-administrators
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 更新场景群管理员
> Updated: 2026-05-10 01:06:15

# 更新场景群管理员

调用本接口，更新群的群管理员，适用于群创建者或已有管理员需要调整群管理员设置，如添加新管理员、移除现有管理员等场景。

## 接口调用说明

支持基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/subAdmins |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群ID，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |
| userIds | Array of String | 否 | 用户userid列表。      最多传12个。 |
| role | Long | 是 | 群成员类型：   - **2**：群管理员 - **3**：普通群成员 |
| unionIds | Array of String | 否 | 外部联系人unionId列表。 |

### 请求示例

HTTP

```
PUT /v1.0/im/sceneGroups/subAdmins HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "openConversationId" : "cidXxxx",
  "userIds" : [ "user123" ],
  "role" : 2,
  "unionIds" : [ "unionId" ]
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
        com.aliyun.dingtalkim_1_0.models.UpdateGroupSubAdminHeaders updateGroupSubAdminHeaders = new com.aliyun.dingtalkim_1_0.models.UpdateGroupSubAdminHeaders();
        updateGroupSubAdminHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.UpdateGroupSubAdminRequest updateGroupSubAdminRequest = new com.aliyun.dingtalkim_1_0.models.UpdateGroupSubAdminRequest()
                .setOpenConversationId("cidXxxx")
                .setUserIds(java.util.Arrays.asList(
                    "user123"
                ))
                .setRole(2L)
                .setUnionIds(java.util.Arrays.asList(
                    "unionId"
                ));
        try {
            client.updateGroupSubAdminWithOptions(updateGroupSubAdminRequest, updateGroupSubAdminHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_group_sub_admin_headers = dingtalkim__1__0_models.UpdateGroupSubAdminHeaders()
        update_group_sub_admin_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_group_sub_admin_request = dingtalkim__1__0_models.UpdateGroupSubAdminRequest(
            open_conversation_id='cidXxxx',
            user_ids=[
                'user123'
            ],
            role=2,
            union_ids=[
                'unionId'
            ]
        )
        try:
            client.update_group_sub_admin_with_options(update_group_sub_admin_request, update_group_sub_admin_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_group_sub_admin_headers = dingtalkim__1__0_models.UpdateGroupSubAdminHeaders()
        update_group_sub_admin_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_group_sub_admin_request = dingtalkim__1__0_models.UpdateGroupSubAdminRequest(
            open_conversation_id='cidXxxx',
            user_ids=[
                'user123'
            ],
            role=2,
            union_ids=[
                'unionId'
            ]
        )
        try:
            await client.update_group_sub_admin_with_options_async(update_group_sub_admin_request, update_group_sub_admin_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateGroupSubAdminHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateGroupSubAdminRequest;
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
        $updateGroupSubAdminHeaders = new UpdateGroupSubAdminHeaders([]);
        $updateGroupSubAdminHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateGroupSubAdminRequest = new UpdateGroupSubAdminRequest([
            "openConversationId" => "cidXxxx",
            "userIds" => [
                "user123"
            ],
            "role" => 2,
            "unionIds" => [
                "unionId"
            ]
        ]);
        try {
            $client->updateGroupSubAdminWithOptions($updateGroupSubAdminRequest, $updateGroupSubAdminHeaders, new RuntimeOptions([]));
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

  updateGroupSubAdminHeaders := &dingtalkim_1_0.UpdateGroupSubAdminHeaders{}
  updateGroupSubAdminHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateGroupSubAdminRequest := &dingtalkim_1_0.UpdateGroupSubAdminRequest{
    OpenConversationId: tea.String("cidXxxx"),
    UserIds: []*string{tea.String("user123")},
    Role: tea.Int64(2),
    UnionIds: []*string{tea.String("unionId")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateGroupSubAdminWithOptions(updateGroupSubAdminRequest, updateGroupSubAdminHeaders, &util.RuntimeOptions{})
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
    let updateGroupSubAdminHeaders = new dingtalkim_1_0.UpdateGroupSubAdminHeaders({ });
    updateGroupSubAdminHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateGroupSubAdminRequest = new dingtalkim_1_0.UpdateGroupSubAdminRequest({
      openConversationId: 'cidXxxx',
      userIds: [
        'user123'
      ],
      role: 2,
      unionIds: [
        'unionId'
      ],
    });
    try {
      await client.updateGroupSubAdminWithOptions(updateGroupSubAdminRequest, updateGroupSubAdminHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupSubAdminHeaders updateGroupSubAdminHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupSubAdminHeaders();
            updateGroupSubAdminHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupSubAdminRequest updateGroupSubAdminRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateGroupSubAdminRequest
            {
                OpenConversationId = "cidXxxx",
                UserIds = new List<string>
                {
                    "user123"
                },
                Role = 2,
                UnionIds = new List<string>
                {
                    "unionId"
                },
            };
            try
            {
                client.UpdateGroupSubAdminWithOptions(updateGroupSubAdminRequest, updateGroupSubAdminHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 更新是否成功。 |

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
| 400 | openConversationIdDecriptFailed | 群 ID 解码失败 | 群 ID 解码失败 |
| 400 | groupPermissionDenied | 无权限访问此群数据 | 无权限访问此群数据 |
| 400 | grayControlDenied | 接口灰度中暂时无法使用 | 接口灰度中暂时无法使用 |
| 400 | apiPermissionDenied | 无权限访问此接口 | 无权限访问此接口 |
| 400 | commonParamIllegal | 网关入参非法 | 网关入参非法 |
| 400 | invalidUserId | 无效的用户ID清单 | 无效的用户ID清单 |
| 400 | subAdminNumberExcessive | 管理员数量超过最大限制 | 管理员数量超过最大限制 |
| 400 | invalidUserIds | 无效的用户ID清单 | 无效的用户ID清单 |
| 400 | invalidOpenConversationId | 无效的群ID | 无效的群ID |
| 400 | systemError | 系统异常 | 系统异常 |
| 400 | userNotInGroup | 用户不在群中 | 用户不在群中 |
| 400 | userNotExists | 用户不存在 | 用户不存在 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 400 | groupDisbang | 群已经解散 | 群已经解散 |
| 400 | invalidParams | 不合法的参数 | 不合法的参数 |
