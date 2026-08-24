---
title: "查询场景群内群模板机器人"
source_url: "https://open.dingtalk.com/document/development/search-group-scene-template-robot"
namespace: "development"
slug: "search-group-scene-template-robot"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群内群模板机器人"
doc_id: "AC6kVRH98Y"
updated_at: "2026-08-14 09:42:01"
---

> Source: https://open.dingtalk.com/document/development/search-group-scene-template-robot
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群管理 > 查询场景群内群模板机器人
> Updated: 2026-08-14 09:42:01

# 查询场景群内群模板机器人

调用本接口，查询群内群模板机器人信息，适用于需要获取群内群模板机器人信息的场景，如在群管理界面展示机器人信息，或者在业务处理中需要使用机器人的 userId 和 unionId 等情况。

## **接口调用说明**

支持以下场景使用：基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/templates/robots |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| robotCode | String | 否 | 机器人的编码。 登录[开发者后台 > 开放能力 > 场景群 > 机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)查看id。 |
| openConversationId | String | 否 | 群ID，可调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。 |

### 请求示例

HTTP

```
GET /v1.0/im/sceneGroups/templates/robots?robotCode=jLyahpLSgXXXXXXXXXXX79521009&openConversationId=cidCtneF+XyQjcyF2ROdgSeIg== HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:basgdasxxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkim_1_0.*;
import com.aliyun.dingtalkim_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        QuerySceneGroupTemplateRobotHeaders querySceneGroupTemplateRobotHeaders = new QuerySceneGroupTemplateRobotHeaders();
        querySceneGroupTemplateRobotHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QuerySceneGroupTemplateRobotRequest querySceneGroupTemplateRobotRequest = new QuerySceneGroupTemplateRobotRequest()
                .setRobotCode("jLyahpLSgXXXXXXXXXXX79521009")
                .setOpenConversationId("cidCtneF+XyQjcyF2ROdgSeIg==");
        try {
            client.querySceneGroupTemplateRobotWithOptions(querySceneGroupTemplateRobotRequest, querySceneGroupTemplateRobotHeaders, new RuntimeOptions());
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
        query_scene_group_template_robot_headers = dingtalkim__1__0_models.QuerySceneGroupTemplateRobotHeaders()
        query_scene_group_template_robot_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_scene_group_template_robot_request = dingtalkim__1__0_models.QuerySceneGroupTemplateRobotRequest(
            robot_code='jLyahpLSgXXXXXXXXXXX79521009',
            open_conversation_id='cidCtneF+XyQjcyF2ROdgSeIg=='
        )
        try:
            client.query_scene_group_template_robot_with_options(query_scene_group_template_robot_request, query_scene_group_template_robot_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_scene_group_template_robot_headers = dingtalkim__1__0_models.QuerySceneGroupTemplateRobotHeaders()
        query_scene_group_template_robot_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_scene_group_template_robot_request = dingtalkim__1__0_models.QuerySceneGroupTemplateRobotRequest(
            robot_code='jLyahpLSgXXXXXXXXXXX79521009',
            open_conversation_id='cidCtneF+XyQjcyF2ROdgSeIg=='
        )
        try:
            await client.query_scene_group_template_robot_with_options_async(query_scene_group_template_robot_request, query_scene_group_template_robot_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QuerySceneGroupTemplateRobotHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\QuerySceneGroupTemplateRobotRequest;
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
        $querySceneGroupTemplateRobotHeaders = new QuerySceneGroupTemplateRobotHeaders([]);
        $querySceneGroupTemplateRobotHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $querySceneGroupTemplateRobotRequest = new QuerySceneGroupTemplateRobotRequest([
            "robotCode" => "jLyahpLSgXXXXXXXXXXX79521009",
            "openConversationId" => "cidCtneF+XyQjcyF2ROdgSeIg=="
        ]);
        try {
            $client->querySceneGroupTemplateRobotWithOptions($querySceneGroupTemplateRobotRequest, $querySceneGroupTemplateRobotHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  querySceneGroupTemplateRobotHeaders := &dingtalkim_1_0.QuerySceneGroupTemplateRobotHeaders{}
  querySceneGroupTemplateRobotHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  querySceneGroupTemplateRobotRequest := &dingtalkim_1_0.QuerySceneGroupTemplateRobotRequest{
    RobotCode: tea.String("jLyahpLSgXXXXXXXXXXX79521009"),
    OpenConversationId: tea.String("cidCtneF+XyQjcyF2ROdgSeIg=="),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QuerySceneGroupTemplateRobotWithOptions(querySceneGroupTemplateRobotRequest, querySceneGroupTemplateRobotHeaders, &util.RuntimeOptions{})
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
    let querySceneGroupTemplateRobotHeaders = new $dingtalkim_1_0.QuerySceneGroupTemplateRobotHeaders({ });
    querySceneGroupTemplateRobotHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let querySceneGroupTemplateRobotRequest = new $dingtalkim_1_0.QuerySceneGroupTemplateRobotRequest({
      robotCode: "jLyahpLSgXXXXXXXXXXX79521009",
      openConversationId: "cidCtneF+XyQjcyF2ROdgSeIg==",
    });
    try {
      await client.querySceneGroupTemplateRobotWithOptions(querySceneGroupTemplateRobotRequest, querySceneGroupTemplateRobotHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySceneGroupTemplateRobotHeaders querySceneGroupTemplateRobotHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySceneGroupTemplateRobotHeaders();
            querySceneGroupTemplateRobotHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySceneGroupTemplateRobotRequest querySceneGroupTemplateRobotRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.QuerySceneGroupTemplateRobotRequest
            {
                RobotCode = "jLyahpLSgXXXXXXXXXXX79521009",
                OpenConversationId = "cidCtneF+XyQjcyF2ROdgSeIg==",
            };
            try
            {
                client.QuerySceneGroupTemplateRobotWithOptions(querySceneGroupTemplateRobotRequest, querySceneGroupTemplateRobotHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| userId | String | 机器人的userId。 |
| unionId | String | 机器人的unionId。      仅当userId无值时才返回unionId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "userId" : "0321326XXXXXXX",
    "unionId" : "EGKJhXXXXXXXFAiE"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam.openConversationIdEmpry | 会话ID为空 | 会话ID为空 |
| 400 | invalidParam.robotCodeEmpry | 机器人编码为空 | 机器人编码为空 |
| 400 | invalidParam.sceneGroupPermissionDenied | 无权限访问此群数据 | 无权限，该群未安装群模板，或者安装的群模板不属于当前token对应的应用名下 |
| 400 | robotDisabled | 机器人已停用 | 机器人已停用 |
| 400 | robotNotFound | 机器人不存在 | 机器人不存在 |
| 400 | invalidParam | %s | 参数为空或参数不合法 |
| 400 | not.found | %s | 群聊不存在，请检查openConversationId是否正确 |
| 400 | unauthorized | %s | 权限不足，群聊所属企业不匹配 |
| 400 | unavailable | %s | 群内未安装群模板 |
| 400 | auth.failed | %s | 无权限，群内安装的群模板不属于当前token对应的应用名下 |
| 500 | systemInnerError | 系统繁忙 | 系统繁忙，请稍后再试 |
