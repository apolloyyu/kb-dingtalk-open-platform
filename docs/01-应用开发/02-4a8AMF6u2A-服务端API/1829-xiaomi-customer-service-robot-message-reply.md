---
title: "小蜜客服机器人消息回复"
source_url: "https://open.dingtalk.com/document/development/xiaomi-customer-service-robot-message-reply"
namespace: "development"
slug: "xiaomi-customer-service-robot-message-reply"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 小蜜客服 > 小蜜客服机器人消息回复"
doc_id: "pOWdESgquY"
updated_at: "2025-09-08 19:06:31"
---

> Source: https://open.dingtalk.com/document/development/xiaomi-customer-service-robot-message-reply
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 小蜜客服 > 小蜜客服机器人消息回复
> Updated: 2025-09-08 19:06:31

# 小蜜客服机器人消息回复

调用本接口根据小蜜客服机器人sessionId进行异步消息回复。

> **[!NOTE]**
>
> - 调用本接口前需要先开通小蜜客服的消息开放能力，详情可参考[消息开放能力](https://www.yuque.com/dingdingxiaomikefu/cdvg5o/rnoftn)。
> - 本接口调用详细说明，可参考[小蜜客服机器人异步消息回复](https://www.yuque.com/dingdingxiaomikefu/cdvg5o/vk2cqe#gYOnp)。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 小蜜客服商业化数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingmi_1.0%23ReplyRobot) |
| 第三方企业应用 | 暂不支持 | 小蜜客服商业化数据管理权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 小蜜客服商业化数据管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/dingmi/robots/reply HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "proxyMessageStr" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| proxyMessageStr | String | 是 | 回复消息内容的内容。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Boolean | 回复是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/dingmi/robots/reply HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json

{
  "proxyMessageStr" : "{\"bizParamMap\":{\"proxySessionId\":\"DINGTALK_RYnVfayNAe_4000006001201145\"},\"msgType\":\"text\",\"text\":\"测试回复机器人消息\"}"
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
    public static com.aliyun.dingtalkdingmi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdingmi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdingmi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdingmi_1_0.models.ReplyRobotHeaders replyRobotHeaders = new com.aliyun.dingtalkdingmi_1_0.models.ReplyRobotHeaders();
        replyRobotHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdingmi_1_0.models.ReplyRobotRequest replyRobotRequest = new com.aliyun.dingtalkdingmi_1_0.models.ReplyRobotRequest()
                .setProxyMessageStr("{\"bizParamMap\":{\"proxySessionId\":\"DINGTALK_RYnVfayNAe_4000006001201145\"},\"msgType\":\"text\",\"text\":\"测试回复机器人消息\"}");
        try {
            client.replyRobotWithOptions(replyRobotRequest, replyRobotHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.dingmi_1_0.client import Client as dingtalkdingmi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dingmi_1_0 import models as dingtalkdingmi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdingmi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdingmi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        reply_robot_headers = dingtalkdingmi__1__0_models.ReplyRobotHeaders()
        reply_robot_headers.x_acs_dingtalk_access_token = '<your access token>'
        reply_robot_request = dingtalkdingmi__1__0_models.ReplyRobotRequest(
            proxy_message_str='{"bizParamMap":{"proxySessionId":"DINGTALK_RYnVfayNAe_4000006001201145"},"msgType":"text","text":"测试回复机器人消息"}'
        )
        try:
            client.reply_robot_with_options(reply_robot_request, reply_robot_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        reply_robot_headers = dingtalkdingmi__1__0_models.ReplyRobotHeaders()
        reply_robot_headers.x_acs_dingtalk_access_token = '<your access token>'
        reply_robot_request = dingtalkdingmi__1__0_models.ReplyRobotRequest(
            proxy_message_str='{"bizParamMap":{"proxySessionId":"DINGTALK_RYnVfayNAe_4000006001201145"},"msgType":"text","text":"测试回复机器人消息"}'
        )
        try:
            await client.reply_robot_with_options_async(reply_robot_request, reply_robot_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\ReplyRobotHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\ReplyRobotRequest;
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
        $replyRobotHeaders = new ReplyRobotHeaders([]);
        $replyRobotHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $replyRobotRequest = new ReplyRobotRequest([
            "proxyMessageStr" => "{\"bizParamMap\":{\"proxySessionId\":\"DINGTALK_RYnVfayNAe_4000006001201145\"},\"msgType\":\"text\",\"text\":\"测试回复机器人消息\"}"
        ]);
        try {
            $client->replyRobotWithOptions($replyRobotRequest, $replyRobotHeaders, new RuntimeOptions([]));
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
  dingtalkdingmi_1_0  "github.com/alibabacloud-go/dingtalk/dingmi_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdingmi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdingmi_1_0.Client{}
  _result, _err = dingtalkdingmi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  replyRobotHeaders := &dingtalkdingmi_1_0.ReplyRobotHeaders{}
  replyRobotHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  replyRobotRequest := &dingtalkdingmi_1_0.ReplyRobotRequest{
    ProxyMessageStr: tea.String("{\"bizParamMap\":{\"proxySessionId\":\"DINGTALK_RYnVfayNAe_4000006001201145\"},\"msgType\":\"text\",\"text\":\"测试回复机器人消息\"}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ReplyRobotWithOptions(replyRobotRequest, replyRobotHeaders, &util.RuntimeOptions{})
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
import dingtalkdingmi_1_0, * as $dingtalkdingmi_1_0 from '@alicloud/dingtalk/dingmi_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdingmi_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdingmi_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let replyRobotHeaders = new $dingtalkdingmi_1_0.ReplyRobotHeaders({ });
    replyRobotHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let replyRobotRequest = new $dingtalkdingmi_1_0.ReplyRobotRequest({
      proxyMessageStr: "{\"bizParamMap\":{\"proxySessionId\":\"DINGTALK_RYnVfayNAe_4000006001201145\"},\"msgType\":\"text\",\"text\":\"测试回复机器人消息\"}",
    });
    try {
      await client.replyRobotWithOptions(replyRobotRequest, replyRobotHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.ReplyRobotHeaders replyRobotHeaders = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.ReplyRobotHeaders();
            replyRobotHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.ReplyRobotRequest replyRobotRequest = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.ReplyRobotRequest
            {
                ProxyMessageStr = "{\"bizParamMap\":{\"proxySessionId\":\"DINGTALK_RYnVfayNAe_4000006001201145\"},\"msgType\":\"text\",\"text\":\"测试回复机器人消息\"}",
            };
            try
            {
                client.ReplyRobotWithOptions(replyRobotRequest, replyRobotHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | 参数错误 | 接口参数错误 |
| 500 | system.error | 推送失败：%s | 系统错误导致推送失败 |
