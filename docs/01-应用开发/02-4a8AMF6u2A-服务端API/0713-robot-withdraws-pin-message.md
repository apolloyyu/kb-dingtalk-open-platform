---
title: "撤回已经发送的DING消息"
source_url: "https://open.dingtalk.com/document/development/robot-withdraws-pin-message"
namespace: "development"
slug: "robot-withdraws-pin-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 发送DING消息 > 撤回已经发送的DING消息"
doc_id: "stHyRQTKI2"
updated_at: "2026-06-05 13:37:02"
---

> Source: https://open.dingtalk.com/document/development/robot-withdraws-pin-message
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 发送DING消息 > 撤回已经发送的DING消息
> Updated: 2026-06-05 13:37:02

# 撤回已经发送的DING消息

调用本接口，可撤回使用企业机器人发送的DING消息。

## **接口调用说明**

当前接口为[钉钉专业版](dingtalk://dingtalkclient/page/link?spm=ding_open_doc.document.0.0.18684a70jkC6tM&url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fweb-dd-pro%2Fmobile_microApp%2Findex.html%3FcorpId%3D%26channel%3Dopenpf_web_devdoc_apiDING_trial&web_wnd=general&width=480&height=800)和[钉钉专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_apiDING_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)专享接口，仅限钉钉专业版和钉钉专属版客户使用，并可按需[增购OpenAPI发DING额度](https://oa.dingtalk.com/index.htm?#/dataCenter/dingOrder?_dlp_=channel%3Dopenpf_web_devdoc_apiDING)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/ding/recall |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Ding.Write-企业机器人发送撤回DING消息 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| robotCode | String | 是 | 发送DING消息的机器人ID。      需要撤销的DING消息，发送和撤回操作必须是同一个机器人。 |
| openDingId | String | 是 | 需要被撤回的DING消息ID，可调用[发送DING消息](0712-robot-sends-nail-message.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/robot/ding/recall HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "robotCode" : "dingxxxxxxxxx",
  "openDingId" : "54165xxx"
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
        com.aliyun.dingtalkrobot_1_0.models.RobotRecallDingHeaders robotRecallDingHeaders = new com.aliyun.dingtalkrobot_1_0.models.RobotRecallDingHeaders();
        robotRecallDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.RobotRecallDingRequest robotRecallDingRequest = new com.aliyun.dingtalkrobot_1_0.models.RobotRecallDingRequest()
                .setRobotCode("dingxxxxxxxxx")
                .setOpenDingId("54165xxx");
        try {
            client.robotRecallDingWithOptions(robotRecallDingRequest, robotRecallDingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        robot_recall_ding_headers = dingtalkrobot__1__0_models.RobotRecallDingHeaders()
        robot_recall_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        robot_recall_ding_request = dingtalkrobot__1__0_models.RobotRecallDingRequest(
            robot_code='dingxxxxxxxxx',
            open_ding_id='54165xxx'
        )
        try:
            client.robot_recall_ding_with_options(robot_recall_ding_request, robot_recall_ding_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        robot_recall_ding_headers = dingtalkrobot__1__0_models.RobotRecallDingHeaders()
        robot_recall_ding_headers.x_acs_dingtalk_access_token = '<your access token>'
        robot_recall_ding_request = dingtalkrobot__1__0_models.RobotRecallDingRequest(
            robot_code='dingxxxxxxxxx',
            open_ding_id='54165xxx'
        )
        try:
            await client.robot_recall_ding_with_options_async(robot_recall_ding_request, robot_recall_ding_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\RobotRecallDingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\RobotRecallDingRequest;
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
        $robotRecallDingHeaders = new RobotRecallDingHeaders([]);
        $robotRecallDingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $robotRecallDingRequest = new RobotRecallDingRequest([
            "robotCode" => "dingxxxxxxxxx",
            "openDingId" => "54165xxx"
        ]);
        try {
            $client->robotRecallDingWithOptions($robotRecallDingRequest, $robotRecallDingHeaders, new RuntimeOptions([]));
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

  robotRecallDingHeaders := &dingtalkrobot_1_0.RobotRecallDingHeaders{}
  robotRecallDingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  robotRecallDingRequest := &dingtalkrobot_1_0.RobotRecallDingRequest{
    RobotCode: tea.String("dingxxxxxxxxx"),
    OpenDingId: tea.String("54165xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RobotRecallDingWithOptions(robotRecallDingRequest, robotRecallDingHeaders, &util.RuntimeOptions{})
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
    let robotRecallDingHeaders = new $dingtalkrobot_1_0.RobotRecallDingHeaders({ });
    robotRecallDingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let robotRecallDingRequest = new $dingtalkrobot_1_0.RobotRecallDingRequest({
      robotCode: "dingxxxxxxxxx",
      openDingId: "54165xxx",
    });
    try {
      await client.robotRecallDingWithOptions(robotRecallDingRequest, robotRecallDingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotRecallDingHeaders robotRecallDingHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotRecallDingHeaders();
            robotRecallDingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotRecallDingRequest robotRecallDingRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotRecallDingRequest
            {
                RobotCode = "dingxxxxxxxxx",
                OpenDingId = "54165xxx",
            };
            try
            {
                client.RobotRecallDingWithOptions(robotRecallDingRequest, robotRecallDingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| openDingId | String | 撤回成功的DING消息ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openDingId" : "54165xxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | recall.ding.exception | recall.ding.exception %s | 撤回DING消息异常 |
| 400 | invalidParameter.param.invalid | 参数不合法%s | 参数不合法 |
| 500 | system.error | system.error | 系统异常 |
