---
title: "BV 设备开始录制"
source_url: "https://open.dingtalk.com/document/development/api-startkanjianrecording"
namespace: "development"
slug: "api-startkanjianrecording"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > DingTalk BV > 看鉴设备 > BV 设备开始录制"
doc_id: "doc_06c34c008c9143d9"
updated_at: "2026-11-17 17:35:20"
---

> Source: https://open.dingtalk.com/document/development/api-startkanjianrecording
> Path: 应用开发 / 服务端 API / 视听智能服务 > DingTalk BV > 看鉴设备 > BV 设备开始录制
> Updated: 2026-11-17 17:35:20

# BV 设备开始录制

调用本接口，让企业看鉴 BV 设备开始录制，返回会话 ID 和记录 ID。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/recordings/start |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Device.Write-钉钉AI看鉴设备数据写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUserId | String | 是 | 操作人 userId，作为记录创建人。 |
| mainTaskId | String | 否 | 要关联的主任务 ID，可通过[分页查询看鉴记录列表](1293-api-listkanjianrecords.md)接口获取。 |
| title | String | 否 | 记录标题，首尾空白会去掉，全空白按未传处理。 |
| deviceSn | String | 是 | 设备序列号，须为本企业生效绑定且在线的设备，可通过[分页查询看鉴记录列表](1293-api-listkanjianrecords.md)接口获取。 |

### **请求示例**

HTTP

```
POST /v1.0/dvi/bv/kanjian/recordings/start HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0917xxxx901d52
Content-Type:application/json

{
  "operatorUserId" : "manager1234",
  "mainTaskId" : "task0001",
  "title" : "morning-check",
  "deviceSn" : "BV0000000001"
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
    public static com.aliyun.dingtalkdvi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdvi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdvi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdvi_1_0.models.StartKanjianRecordingHeaders startKanjianRecordingHeaders = new com.aliyun.dingtalkdvi_1_0.models.StartKanjianRecordingHeaders();
        startKanjianRecordingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.StartKanjianRecordingRequest startKanjianRecordingRequest = new com.aliyun.dingtalkdvi_1_0.models.StartKanjianRecordingRequest()
                .setOperatorUserId("manager1234")
                .setMainTaskId("task0001")
                .setTitle("morning-check")
                .setDeviceSn("BV0000000001");
        try {
            client.startKanjianRecordingWithOptions(startKanjianRecordingRequest, startKanjianRecordingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.dvi_1_0.client import Client as dingtalkdvi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dvi_1_0 import models as dingtalkdvi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdvi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdvi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        start_kanjian_recording_headers = dingtalkdvi__1__0_models.StartKanjianRecordingHeaders()
        start_kanjian_recording_headers.x_acs_dingtalk_access_token = '<your access token>'
        start_kanjian_recording_request = dingtalkdvi__1__0_models.StartKanjianRecordingRequest(
            operator_user_id='manager1234',
            main_task_id='task0001',
            title='morning-check',
            device_sn='BV0000000001'
        )
        try:
            client.start_kanjian_recording_with_options(start_kanjian_recording_request, start_kanjian_recording_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        start_kanjian_recording_headers = dingtalkdvi__1__0_models.StartKanjianRecordingHeaders()
        start_kanjian_recording_headers.x_acs_dingtalk_access_token = '<your access token>'
        start_kanjian_recording_request = dingtalkdvi__1__0_models.StartKanjianRecordingRequest(
            operator_user_id='manager1234',
            main_task_id='task0001',
            title='morning-check',
            device_sn='BV0000000001'
        )
        try:
            await client.start_kanjian_recording_with_options_async(start_kanjian_recording_request, start_kanjian_recording_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\StartKanjianRecordingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\StartKanjianRecordingRequest;
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
        $startKanjianRecordingHeaders = new StartKanjianRecordingHeaders([]);
        $startKanjianRecordingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $startKanjianRecordingRequest = new StartKanjianRecordingRequest([
            "operatorUserId" => "manager1234",
            "mainTaskId" => "task0001",
            "title" => "morning-check",
            "deviceSn" => "BV0000000001"
        ]);
        try {
            $client->startKanjianRecordingWithOptions($startKanjianRecordingRequest, $startKanjianRecordingHeaders, new RuntimeOptions([]));
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
  dingtalkdvi_1_0  "github.com/alibabacloud-go/dingtalk/dvi_1_0"
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
func CreateClient () (_result *dingtalkdvi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdvi_1_0.Client{}
  _result, _err = dingtalkdvi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  startKanjianRecordingHeaders := &dingtalkdvi_1_0.StartKanjianRecordingHeaders{}
  startKanjianRecordingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  startKanjianRecordingRequest := &dingtalkdvi_1_0.StartKanjianRecordingRequest{
    OperatorUserId: tea.String("manager1234"),
    MainTaskId: tea.String("task0001"),
    Title: tea.String("morning-check"),
    DeviceSn: tea.String("BV0000000001"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.StartKanjianRecordingWithOptions(startKanjianRecordingRequest, startKanjianRecordingHeaders, &util.RuntimeOptions{})
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
const dingtalkdvi_1_0 = require('@alicloud/dingtalk/dvi_1_0');
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
    return new dingtalkdvi_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let startKanjianRecordingHeaders = new dingtalkdvi_1_0.StartKanjianRecordingHeaders({ });
    startKanjianRecordingHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let startKanjianRecordingRequest = new dingtalkdvi_1_0.StartKanjianRecordingRequest({
      operatorUserId: 'manager1234',
      mainTaskId: 'task0001',
      title: 'morning-check',
      deviceSn: 'BV0000000001',
    });
    try {
      await client.startKanjianRecordingWithOptions(startKanjianRecordingRequest, startKanjianRecordingHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdvi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdvi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.StartKanjianRecordingHeaders startKanjianRecordingHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.StartKanjianRecordingHeaders();
            startKanjianRecordingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.StartKanjianRecordingRequest startKanjianRecordingRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.StartKanjianRecordingRequest
            {
                OperatorUserId = "manager1234",
                MainTaskId = "task0001",
                Title = "morning-check",
                DeviceSn = "BV0000000001",
            };
            try
            {
                client.StartKanjianRecordingWithOptions(startKanjianRecordingRequest, startKanjianRecordingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 业务结果。 |
| recordId | String | 看鉴记录 ID，用于记录域接口。 |
| sessionId | String | 录制会话 ID，停止录制时传给 `recording.stop`。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "recordId" : "record0001",
    "sessionId" : "session0001"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 参数为空。deviceSn、operatorUserId 必填 | 参数为空。deviceSn、operatorUserId 必填 |
| 400 | emp.notExist | 操作人不是本企业员工，请检查 operatorUserId | 操作人不是本企业员工，请检查 operatorUserId |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
| 400 | device.offline | 设备不在线 | 设备不在线 |
