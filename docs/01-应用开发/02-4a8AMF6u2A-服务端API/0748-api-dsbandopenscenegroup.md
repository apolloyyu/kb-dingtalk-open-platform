---
title: "解散场景群"
source_url: "https://open.dingtalk.com/document/development/api-dsbandopenscenegroup"
namespace: "development"
slug: "api-dsbandopenscenegroup"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 解散场景群"
doc_id: "MfTls3182y"
updated_at: "2026-05-10 01:10:50"
---

> Source: https://open.dingtalk.com/document/development/api-dsbandopenscenegroup
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 解散场景群
> Updated: 2026-05-10 01:10:50

# 解散场景群

调用本接口，根据群ID解散指定群。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/chat/scenegroup/disband |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群ID，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |

### 请求示例

HTTP

```
POST /v1.0/im/chat/scenegroup/disband HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1b*****
Content-Type:application/json

{
  "openConversationId" : "cidxxxx"
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
        com.aliyun.dingtalkim_1_0.models.DsbandOpenSceneGroupHeaders dsbandOpenSceneGroupHeaders = new com.aliyun.dingtalkim_1_0.models.DsbandOpenSceneGroupHeaders();
        dsbandOpenSceneGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_1_0.models.DsbandOpenSceneGroupRequest dsbandOpenSceneGroupRequest = new com.aliyun.dingtalkim_1_0.models.DsbandOpenSceneGroupRequest()
                .setOpenConversationId("cidxxxx");
        try {
            client.dsbandOpenSceneGroupWithOptions(dsbandOpenSceneGroupRequest, dsbandOpenSceneGroupHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        dsband_open_scene_group_headers = dingtalkim__1__0_models.DsbandOpenSceneGroupHeaders()
        dsband_open_scene_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        dsband_open_scene_group_request = dingtalkim__1__0_models.DsbandOpenSceneGroupRequest(
            open_conversation_id='cidxxxx'
        )
        try:
            client.dsband_open_scene_group_with_options(dsband_open_scene_group_request, dsband_open_scene_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        dsband_open_scene_group_headers = dingtalkim__1__0_models.DsbandOpenSceneGroupHeaders()
        dsband_open_scene_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        dsband_open_scene_group_request = dingtalkim__1__0_models.DsbandOpenSceneGroupRequest(
            open_conversation_id='cidxxxx'
        )
        try:
            await client.dsband_open_scene_group_with_options_async(dsband_open_scene_group_request, dsband_open_scene_group_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\DsbandOpenSceneGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\DsbandOpenSceneGroupRequest;
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
        $dsbandOpenSceneGroupHeaders = new DsbandOpenSceneGroupHeaders([]);
        $dsbandOpenSceneGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $dsbandOpenSceneGroupRequest = new DsbandOpenSceneGroupRequest([
            "openConversationId" => "cidxxxx"
        ]);
        try {
            $client->dsbandOpenSceneGroupWithOptions($dsbandOpenSceneGroupRequest, $dsbandOpenSceneGroupHeaders, new RuntimeOptions([]));
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

  dsbandOpenSceneGroupHeaders := &dingtalkim_1_0.DsbandOpenSceneGroupHeaders{}
  dsbandOpenSceneGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  dsbandOpenSceneGroupRequest := &dingtalkim_1_0.DsbandOpenSceneGroupRequest{
    OpenConversationId: tea.String("cidxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DsbandOpenSceneGroupWithOptions(dsbandOpenSceneGroupRequest, dsbandOpenSceneGroupHeaders, &util.RuntimeOptions{})
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
    let dsbandOpenSceneGroupHeaders = new dingtalkim_1_0.DsbandOpenSceneGroupHeaders({ });
    dsbandOpenSceneGroupHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let dsbandOpenSceneGroupRequest = new dingtalkim_1_0.DsbandOpenSceneGroupRequest({
      openConversationId: 'cidxxxx',
    });
    try {
      await client.dsbandOpenSceneGroupWithOptions(dsbandOpenSceneGroupRequest, dsbandOpenSceneGroupHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.DsbandOpenSceneGroupHeaders dsbandOpenSceneGroupHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.DsbandOpenSceneGroupHeaders();
            dsbandOpenSceneGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.DsbandOpenSceneGroupRequest dsbandOpenSceneGroupRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.DsbandOpenSceneGroupRequest
            {
                OpenConversationId = "cidxxxx",
            };
            try
            {
                client.DsbandOpenSceneGroupWithOptions(dsbandOpenSceneGroupRequest, dsbandOpenSceneGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 删除结果：   - **true**：执行成功 - **false**：执行失败 |

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
| 400 | paramIllegal | paramIllegal | 参数错误，请检查 |
| 400 | permession.checkFailed | 群主不在应用可见性内 | 群主不在应用可见性内 |
| 500 | system.error | system.error | 系统错误 |
