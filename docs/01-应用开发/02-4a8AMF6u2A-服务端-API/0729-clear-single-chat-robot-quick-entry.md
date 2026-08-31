---
title: "清空单聊机器人快捷入口"
source_url: "https://open.dingtalk.com/document/development/clear-single-chat-robot-quick-entry"
namespace: "development"
slug: "clear-single-chat-robot-quick-entry"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 快捷入口管理 > 清空单聊机器人快捷入口"
doc_id: "7k9sc5c3fa"
updated_at: "2026-06-04 10:57:43"
---

> Source: https://open.dingtalk.com/document/development/clear-single-chat-robot-quick-entry
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 快捷入口管理 > 清空单聊机器人快捷入口
> Updated: 2026-06-04 10:57:43

# 清空单聊机器人快捷入口

调用本接口清空单聊机器人快捷入口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/plugins/clear |
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
POST /v1.0/robot/plugins/clear HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:asxsbjekdndkajXXXXX
Content-Type:application/json

{
  "robotCode" : "dingkxnemxbqkXXXX"
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
        com.aliyun.dingtalkrobot_1_0.models.ClearRobotPluginHeaders clearRobotPluginHeaders = new com.aliyun.dingtalkrobot_1_0.models.ClearRobotPluginHeaders();
        clearRobotPluginHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.ClearRobotPluginRequest clearRobotPluginRequest = new com.aliyun.dingtalkrobot_1_0.models.ClearRobotPluginRequest()
                .setRobotCode("dingkxnemxbqkXXXX");
        try {
            client.clearRobotPluginWithOptions(clearRobotPluginRequest, clearRobotPluginHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        clear_robot_plugin_headers = dingtalkrobot__1__0_models.ClearRobotPluginHeaders()
        clear_robot_plugin_headers.x_acs_dingtalk_access_token = '<your access token>'
        clear_robot_plugin_request = dingtalkrobot__1__0_models.ClearRobotPluginRequest(
            robot_code='dingkxnemxbqkXXXX'
        )
        try:
            client.clear_robot_plugin_with_options(clear_robot_plugin_request, clear_robot_plugin_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        clear_robot_plugin_headers = dingtalkrobot__1__0_models.ClearRobotPluginHeaders()
        clear_robot_plugin_headers.x_acs_dingtalk_access_token = '<your access token>'
        clear_robot_plugin_request = dingtalkrobot__1__0_models.ClearRobotPluginRequest(
            robot_code='dingkxnemxbqkXXXX'
        )
        try:
            await client.clear_robot_plugin_with_options_async(clear_robot_plugin_request, clear_robot_plugin_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\ClearRobotPluginHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\ClearRobotPluginRequest;
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
        $clearRobotPluginHeaders = new ClearRobotPluginHeaders([]);
        $clearRobotPluginHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $clearRobotPluginRequest = new ClearRobotPluginRequest([
            "robotCode" => "dingkxnemxbqkXXXX"
        ]);
        try {
            $client->clearRobotPluginWithOptions($clearRobotPluginRequest, $clearRobotPluginHeaders, new RuntimeOptions([]));
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

  clearRobotPluginHeaders := &dingtalkrobot_1_0.ClearRobotPluginHeaders{}
  clearRobotPluginHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  clearRobotPluginRequest := &dingtalkrobot_1_0.ClearRobotPluginRequest{
    RobotCode: tea.String("dingkxnemxbqkXXXX"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ClearRobotPluginWithOptions(clearRobotPluginRequest, clearRobotPluginHeaders, &util.RuntimeOptions{})
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
    let clearRobotPluginHeaders = new $dingtalkrobot_1_0.ClearRobotPluginHeaders({ });
    clearRobotPluginHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let clearRobotPluginRequest = new $dingtalkrobot_1_0.ClearRobotPluginRequest({
      robotCode: "dingkxnemxbqkXXXX",
    });
    try {
      await client.clearRobotPluginWithOptions(clearRobotPluginRequest, clearRobotPluginHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.ClearRobotPluginHeaders clearRobotPluginHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.ClearRobotPluginHeaders();
            clearRobotPluginHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.ClearRobotPluginRequest clearRobotPluginRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.ClearRobotPluginRequest
            {
                RobotCode = "dingkxnemxbqkXXXX",
            };
            try
            {
                client.ClearRobotPluginWithOptions(clearRobotPluginRequest, clearRobotPluginHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否成功清空机器人快捷入口。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
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
| 500 | system.error | 系统错误 | 系统错误 |
