---
title: "查询单聊机器人的快捷入口"
source_url: "https://open.dingtalk.com/document/development/quick-entrance-of-inquiry-single-chat-robot"
namespace: "development"
slug: "quick-entrance-of-inquiry-single-chat-robot"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 快捷入口管理 > 查询单聊机器人的快捷入口"
doc_id: "UCIEZHdilh"
updated_at: "2026-06-05 13:49:09"
---

> Source: https://open.dingtalk.com/document/development/quick-entrance-of-inquiry-single-chat-robot
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 快捷入口管理 > 查询单聊机器人的快捷入口
> Updated: 2026-06-05 13:49:09

# 查询单聊机器人的快捷入口

调用本接口查询单聊机器人的快捷入口，包含快捷入口名称、快捷入口图标、PC端快捷入口跳转链接和移动端快捷入口链接，适用于企业管理员在配置机器人功能时快速获取快捷入口配置信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/plugins/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Robot.SingleChat.ReadWrite-单聊机器人使用管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| robotCode | String | 是 | 机器人的编码，参见[机器人名词表-robotCode](https://open.dingtalk.com/document/development/robot-overview)内容，获取`robotCode`。 |

### 请求示例

HTTP

```
POST /v1.0/robot/plugins/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:asxsbjekdndkajXXXXX
Content-Type:application/json

{
  "robotCode" : "dingykcdkXXXXXX"
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
    public static com.aliyun.dingtalkrobot_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrobot_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrobot_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrobot_1_0.models.QueryRobotPluginHeaders queryRobotPluginHeaders = new com.aliyun.dingtalkrobot_1_0.models.QueryRobotPluginHeaders();
        queryRobotPluginHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.QueryRobotPluginRequest queryRobotPluginRequest = new com.aliyun.dingtalkrobot_1_0.models.QueryRobotPluginRequest()
                .setRobotCode("dingykcdkXXXXXX");
        try {
            client.queryRobotPluginWithOptions(queryRobotPluginRequest, queryRobotPluginHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrobot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrobot_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_robot_plugin_headers = dingtalkrobot__1__0_models.QueryRobotPluginHeaders()
        query_robot_plugin_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_robot_plugin_request = dingtalkrobot__1__0_models.QueryRobotPluginRequest(
            robot_code='dingykcdkXXXXXX'
        )
        try:
            client.query_robot_plugin_with_options(query_robot_plugin_request, query_robot_plugin_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_robot_plugin_headers = dingtalkrobot__1__0_models.QueryRobotPluginHeaders()
        query_robot_plugin_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_robot_plugin_request = dingtalkrobot__1__0_models.QueryRobotPluginRequest(
            robot_code='dingykcdkXXXXXX'
        )
        try:
            await client.query_robot_plugin_with_options_async(query_robot_plugin_request, query_robot_plugin_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\QueryRobotPluginHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\QueryRobotPluginRequest;
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
        $queryRobotPluginHeaders = new QueryRobotPluginHeaders([]);
        $queryRobotPluginHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryRobotPluginRequest = new QueryRobotPluginRequest([
            "robotCode" => "dingykcdkXXXXXX"
        ]);
        try {
            $client->queryRobotPluginWithOptions($queryRobotPluginRequest, $queryRobotPluginHeaders, new RuntimeOptions([]));
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
  dingtalkrobot_1_0  "github.com/alibabacloud-go/dingtalk/robot_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrobot_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrobot_1_0.Client{}
  _result, _err = dingtalkrobot_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryRobotPluginHeaders := &dingtalkrobot_1_0.QueryRobotPluginHeaders{}
  queryRobotPluginHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryRobotPluginRequest := &dingtalkrobot_1_0.QueryRobotPluginRequest{
    RobotCode: tea.String("dingykcdkXXXXXX"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryRobotPluginWithOptions(queryRobotPluginRequest, queryRobotPluginHeaders, &util.RuntimeOptions{})
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
import dingtalkrobot_1_0, * as $dingtalkrobot_1_0 from '@alicloud/dingtalk/robot_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrobot_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrobot_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryRobotPluginHeaders = new $dingtalkrobot_1_0.QueryRobotPluginHeaders({ });
    queryRobotPluginHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryRobotPluginRequest = new $dingtalkrobot_1_0.QueryRobotPluginRequest({
      robotCode: "dingykcdkXXXXXX",
    });
    try {
      await client.queryRobotPluginWithOptions(queryRobotPluginRequest, queryRobotPluginHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrobot_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrobot_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.QueryRobotPluginHeaders queryRobotPluginHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.QueryRobotPluginHeaders();
            queryRobotPluginHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.QueryRobotPluginRequest queryRobotPluginRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.QueryRobotPluginRequest
            {
                RobotCode = "dingykcdkXXXXXX",
            };
            try
            {
                client.QueryRobotPluginWithOptions(queryRobotPluginRequest, queryRobotPluginHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| pluginInfoList | Array | 快捷入口列表。 |
| name | String | 快捷入口的名称，支持国际化设置，如`{"en_US":"test123","zh_CN":"测试123"}`。 |
| icon | String | 快捷入口的图标id。 |
| pcUrl | String | pc端会话快捷入口跳转链接。 |
| mobileUrl | String | 手机端快捷入口跳转链接。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "pluginInfoList" : [ {
    "name" : "{\"zh_CN\":\"测试123\"}",
    "icon" : "@lALPDtXaDkO3j7hgYA",
    "pcUrl" : "https://www.dingtalk.com",
    "mobileUrl" : "https://www.dingtalk.com"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | 参数错误 | 参数错误 |
| 400 | invalidRequest.robotCodeNotMatch | 应用与绑定的机器人robotCode不相符 | 应用与绑定的机器人robotCode不相符 |
| 400 | invalidRequest.robotNotExist | 机器人不存在，请核实后添加 | 机器人不存在，请核实后添加 |
| 400 | invalidRequest.robotIsStop | 机器人已经被组织停用 | 机器人已经被组织停用 |
| 400 | invalidRequest.exceededMaximumLimit | 超过插件最大个数限制 | 超过插件最大个数限制 |
| 400 | invalidRequest.jsonFormatErroj | json格式错误 | json格式错误 |
| 500 | system.error | 系统错误 | 系统错误 |
| 500 | invalidRequest.pluginInstallFail | 插件安装失败 | 插件安装失败 |
