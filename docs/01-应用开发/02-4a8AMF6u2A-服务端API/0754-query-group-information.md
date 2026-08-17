---
title: "查询场景群简要信息"
source_url: "https://open.dingtalk.com/document/development/query-group-information"
namespace: "development"
slug: "query-group-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群简要信息"
doc_id: "oMZn2ooR6S"
updated_at: "2026-05-10 01:09:42"
---

> Source: https://open.dingtalk.com/document/development/query-group-information
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群简要信息
> Updated: 2026-05-10 01:09:42

# 查询场景群简要信息

调用本接口，根据群ID查询群名称、群图标、群主id等基本信息，适用于需要快速获取群基本信息的场景，如在群列表展示群名称、头像等信息，或者在业务处理中需要判断群状态等情况。

## 接口调用说明

支持以下场景使用：

- 基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。
- 安装群聊酷应用的群，详情参见[群聊酷应用](../01-XOnnmGCTbn-开发指南/0042-coolapp-overview.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/query |
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
| openConversationId | String | 是 | 群ID：   - 基于群模板创建的群：调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 - 安装群聊酷应用的群：通过[群内安装酷应用事件](../01-XOnnmGCTbn-开发指南/0058-group-chat-coolapp-event.md)获取回调参数`OpenConversationId`参数值。 |
| coolAppCode | String | 否 | 群聊酷应用编码：   - 基于群模板创建的群：不需要传入此参数。 - 安装群聊酷应用的群，**必须**传入此参数。 |

### 请求示例

HTTP

```
POST /v1.0/im/sceneGroups/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c0fa518xxx
Content-Type:application/json

{
  "openConversationId" : "cid/i4vQnDxxx",
  "coolAppCode" : "XXXXXXX"
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
        com.aliyun.dingtalkim_1_0.models.GetSceneGroupInfoHeaders getSceneGroupInfoHeaders = new com.aliyun.dingtalkim_1_0.models.GetSceneGroupInfoHeaders();
        getSceneGroupInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.GetSceneGroupInfoRequest getSceneGroupInfoRequest = new com.aliyun.dingtalkim_1_0.models.GetSceneGroupInfoRequest()
                .setOpenConversationId("cid/i4vQnDxxx")
                .setCoolAppCode("XXXXXXX");
        try {
            client.getSceneGroupInfoWithOptions(getSceneGroupInfoRequest, getSceneGroupInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_scene_group_info_headers = dingtalkim__1__0_models.GetSceneGroupInfoHeaders()
        get_scene_group_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_scene_group_info_request = dingtalkim__1__0_models.GetSceneGroupInfoRequest(
            open_conversation_id='cid/i4vQnDxxx',
            cool_app_code='XXXXXXX'
        )
        try:
            client.get_scene_group_info_with_options(get_scene_group_info_request, get_scene_group_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_scene_group_info_headers = dingtalkim__1__0_models.GetSceneGroupInfoHeaders()
        get_scene_group_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_scene_group_info_request = dingtalkim__1__0_models.GetSceneGroupInfoRequest(
            open_conversation_id='cid/i4vQnDxxx',
            cool_app_code='XXXXXXX'
        )
        try:
            await client.get_scene_group_info_with_options_async(get_scene_group_info_request, get_scene_group_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\GetSceneGroupInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\GetSceneGroupInfoRequest;
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
        $getSceneGroupInfoHeaders = new GetSceneGroupInfoHeaders([]);
        $getSceneGroupInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSceneGroupInfoRequest = new GetSceneGroupInfoRequest([
            "openConversationId" => "cid/i4vQnDxxx",
            "coolAppCode" => "XXXXXXX"
        ]);
        try {
            $client->getSceneGroupInfoWithOptions($getSceneGroupInfoRequest, $getSceneGroupInfoHeaders, new RuntimeOptions([]));
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

  getSceneGroupInfoHeaders := &dingtalkim_1_0.GetSceneGroupInfoHeaders{}
  getSceneGroupInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSceneGroupInfoRequest := &dingtalkim_1_0.GetSceneGroupInfoRequest{
    OpenConversationId: tea.String("cid/i4vQnDxxx"),
    CoolAppCode: tea.String("XXXXXXX"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSceneGroupInfoWithOptions(getSceneGroupInfoRequest, getSceneGroupInfoHeaders, &util.RuntimeOptions{})
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
    let getSceneGroupInfoHeaders = new dingtalkim_1_0.GetSceneGroupInfoHeaders({ });
    getSceneGroupInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getSceneGroupInfoRequest = new dingtalkim_1_0.GetSceneGroupInfoRequest({
      openConversationId: 'cid/i4vQnDxxx',
      coolAppCode: 'XXXXXXX',
    });
    try {
      await client.getSceneGroupInfoWithOptions(getSceneGroupInfoRequest, getSceneGroupInfoHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetSceneGroupInfoHeaders getSceneGroupInfoHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetSceneGroupInfoHeaders();
            getSceneGroupInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetSceneGroupInfoRequest getSceneGroupInfoRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.GetSceneGroupInfoRequest
            {
                OpenConversationId = "cid/i4vQnDxxx",
                CoolAppCode = "XXXXXXX",
            };
            try
            {
                client.GetSceneGroupInfoWithOptions(getSceneGroupInfoRequest, getSceneGroupInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 调用是否成功。 |
| openConversationId | String | 开放群ID。 |
| templateId | String | 场景群模板ID。 |
| title | String | 群名称。 |
| ownerUserId | String | 群主的userId。 |
| icon | String | 群头像mediaId。 |
| groupUrl | String | 群URL。 |
| status | Integer | 群状态：   - **1**：正常 - **2**：已解散 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "openConversationId" : "cidXXXXXXXXX==",
  "templateId" : "13d42075-b3e2-xxx",
  "title" : "奥运项目组",
  "ownerUserId" : "wb292913",
  "icon" : "@sdkhaiuhxxx",
  "groupUrl" : "https://xxx.com",
  "status" : 1
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | groupPermissionDenied | 无权限 | 无权限,该群不是内部群，或者未安装群模板，或者未安装入参指定的群聊酷应用，或者入参指定的群聊酷应用不属于当前token所属应用名下 |
| 400 | paramIllegal | 请求参数非法 | 请求参数非法 |
| 400 | paramBlank | 请求参数为空 | 请求参数为空 |
| 400 | cidEncryptError | 群ID解析错误 | 群ID解析错误 |
| 400 | groupTemplatePermissionDenied | 无权限，该群安装的群模板不属于当前token对应的应用名下 | 无权限，该群安装的群模板不属于当前token对应的应用名下 |
| 400 | coolAppUninstalled | 无权限，该群没有安装群聊酷应用 | 无权限，该群没有安装群聊酷应用 |
| 400 | coolAppUnexist | 群聊酷应用不存在 | 群聊酷应用不存在 |
| 400 | coolAppPermissionDenied | 无权限，指定的群扩展不属于当前token对应的应用名下 | 无权限，指定的群扩展不属于当前token对应的应用名下 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 400 | systemError | 系统异常 | 系统内部异常，请稍后再试 |
| 400 | auth.error | %s | 权限校验不通过 |
