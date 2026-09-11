---
title: "下载机器人接收消息的文件内容"
source_url: "https://open.dingtalk.com/document/development/download-the-file-content-of-the-robot-receiving-message"
namespace: "development"
slug: "download-the-file-content-of-the-robot-receiving-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 消息接收 > 下载机器人接收消息的文件内容"
doc_id: "RFt9sbk5s9"
updated_at: "2026-06-05 13:41:57"
---

> Source: https://open.dingtalk.com/document/development/download-the-file-content-of-the-robot-receiving-message
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 消息接收 > 下载机器人接收消息的文件内容
> Updated: 2026-06-05 13:41:57

# 下载机器人接收消息的文件内容

获取机器人消息中文件下载链接

## **接口调用说明**

1. 当用户向机器人发送图片消息、语音消息、视频消息、文件消息、富文本消息时，通过机器人回调给开发者的信息中获取临时下载码`downloadCode`。
2. 通过临时下载码`downloadCode`，调用本接口获取消息中的图片、语音、文件、视频等文件的临时下载链接。
3. 访问临时下载链接，获取文件内容。

> **[!NOTE]**
>
> - 群聊会话中：群成员@机器人，机器人不支持接收语音、文件、视频类型。
> - 人与人的会话中：机器人不支持接收语音、文件、视频类型。
> - 人与机器人的会话中：机器人支持接收语音、文件、视频类型。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/robot/messageFiles/download |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_robot\_sendmsg-企业内机器人发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| downloadCode | String | 是 | 用户向机器人发送文件消息后，机器人回调给开发者消息中的下载码。详情参考[机器人接收消息](https://open.dingtalk.com/document/dingstart/receive-message)。 |
| robotCode | String | 是 | 机器人的编码，详情参考[机器人 ID](https://open.dingtalk.com/document/development/robot-overview)。 |

### 请求示例

HTTP

```
POST /v1.0/robot/messageFiles/download HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:qkops*****cviojsdjn
Content-Type:application/json

{
  "downloadCode" : "mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==",
  "robotCode" : "ding******yn0pjqd"
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
        com.aliyun.dingtalkrobot_1_0.models.RobotMessageFileDownloadHeaders robotMessageFileDownloadHeaders = new com.aliyun.dingtalkrobot_1_0.models.RobotMessageFileDownloadHeaders();
        robotMessageFileDownloadHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrobot_1_0.models.RobotMessageFileDownloadRequest robotMessageFileDownloadRequest = new com.aliyun.dingtalkrobot_1_0.models.RobotMessageFileDownloadRequest()
                .setDownloadCode("mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==")
                .setRobotCode("ding******yn0pjqd");
        try {
            client.robotMessageFileDownloadWithOptions(robotMessageFileDownloadRequest, robotMessageFileDownloadHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        robot_message_file_download_headers = dingtalkrobot__1__0_models.RobotMessageFileDownloadHeaders()
        robot_message_file_download_headers.x_acs_dingtalk_access_token = '<your access token>'
        robot_message_file_download_request = dingtalkrobot__1__0_models.RobotMessageFileDownloadRequest(
            download_code='mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==',
            robot_code='ding******yn0pjqd'
        )
        try:
            client.robot_message_file_download_with_options(robot_message_file_download_request, robot_message_file_download_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        robot_message_file_download_headers = dingtalkrobot__1__0_models.RobotMessageFileDownloadHeaders()
        robot_message_file_download_headers.x_acs_dingtalk_access_token = '<your access token>'
        robot_message_file_download_request = dingtalkrobot__1__0_models.RobotMessageFileDownloadRequest(
            download_code='mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==',
            robot_code='ding******yn0pjqd'
        )
        try:
            await client.robot_message_file_download_with_options_async(robot_message_file_download_request, robot_message_file_download_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\RobotMessageFileDownloadHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrobot_1_0\Models\RobotMessageFileDownloadRequest;
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
        $robotMessageFileDownloadHeaders = new RobotMessageFileDownloadHeaders([]);
        $robotMessageFileDownloadHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $robotMessageFileDownloadRequest = new RobotMessageFileDownloadRequest([
            "downloadCode" => "mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==",
            "robotCode" => "ding******yn0pjqd"
        ]);
        try {
            $client->robotMessageFileDownloadWithOptions($robotMessageFileDownloadRequest, $robotMessageFileDownloadHeaders, new RuntimeOptions([]));
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

  robotMessageFileDownloadHeaders := &dingtalkrobot_1_0.RobotMessageFileDownloadHeaders{}
  robotMessageFileDownloadHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  robotMessageFileDownloadRequest := &dingtalkrobot_1_0.RobotMessageFileDownloadRequest{
    DownloadCode: tea.String("mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q=="),
    RobotCode: tea.String("ding******yn0pjqd"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RobotMessageFileDownloadWithOptions(robotMessageFileDownloadRequest, robotMessageFileDownloadHeaders, &util.RuntimeOptions{})
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
    let robotMessageFileDownloadHeaders = new $dingtalkrobot_1_0.RobotMessageFileDownloadHeaders({ });
    robotMessageFileDownloadHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let robotMessageFileDownloadRequest = new $dingtalkrobot_1_0.RobotMessageFileDownloadRequest({
      downloadCode: "mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==",
      robotCode: "ding******yn0pjqd",
    });
    try {
      await client.robotMessageFileDownloadWithOptions(robotMessageFileDownloadRequest, robotMessageFileDownloadHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotMessageFileDownloadHeaders robotMessageFileDownloadHeaders = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotMessageFileDownloadHeaders();
            robotMessageFileDownloadHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotMessageFileDownloadRequest robotMessageFileDownloadRequest = new AlibabaCloud.SDK.Dingtalkrobot_1_0.Models.RobotMessageFileDownloadRequest
            {
                DownloadCode = "mIofN*********gn38tqVwL+zoRgzXipAMzmV5uhVKUlBdjKugAIvsm+TrvaPI0JYCMjvFMAlXvMWnMJsi2nZ9a0+N2c9CoV90hiB/B+fEThASPz+jmIa4J6x4WTsmmU3E/AopGsSGugE+hkHBcu52o76Yd2SCpPNUqenvdySSqjowEt1+Ddz55/9Qj8Y8ZhTryqsb7tYwzLFB+F3lsWCotXBOQvEgy3e/bEQtOyV6YrP3KG6YNSb3Q==",
                RobotCode = "ding******yn0pjqd",
            };
            try
            {
                client.RobotMessageFileDownloadWithOptions(robotMessageFileDownloadRequest, robotMessageFileDownloadHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| downloadUrl | String | 文件的临时下载链接。    访问临时下载链接，获取下载文件，在文件被下载到本地后，需开发者替换本地下载的文件扩展名。例如替换视频文件：   - 替换前：`iAEI******IVAiYgXNCKMGzSsRB85j_Z7zCM0CYA.file`。 - 替换后：`iAEI******IVAiYgXNCKMGzSsRB85j_Z7zCM0CYA.mp4`。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "downloadUrl" : "http://wukong-**********gEv&Signature=5BNf2tBJcpKpkQw4wakBBM6ZJ0E%3D&Expires=1671377946"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.robotCode.empty | 机器人robotCode为空 | 机器人robotCode无效，请检查机器人是否在群内 |
| 400 | invalidParameter.robotCode.auth | 此downloadCode和机器人robotCode不匹配，请使用接收此条消息机器人robotCode和对应的downloadCode | 此downloadCode和机器人robotCode不匹配，请使用接收此条消息机器人robotCode和对应的downloadCode |
| 400 | invalidParameter.robotCode.empty | 机器人downloadCode为空 | 机器人downloadCode为空 |
| 400 | invalidParameter.robotCode.auth | 该接口仅支持企业自建应用或三方应用授权调用 | 该接口仅支持企业自建应用或三方应用授权调用 |
| 400 | invalidParameter.robotCode.downloadCode | 下载码有误或者已经过期 | 下载码有误或者已经过期 |
| 400 | invalidParameter.robotCode.auth | 调用该接口的企业和此downloadCode对应机器人企业所属不同 | 调用该接口的企业和此downloadCode对应机器人企业所属不同 |
