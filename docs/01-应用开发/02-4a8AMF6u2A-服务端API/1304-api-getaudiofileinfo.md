---
title: "获取音频文件信息"
source_url: "https://open.dingtalk.com/document/development/api-getaudiofileinfo"
namespace: "development"
slug: "api-getaudiofileinfo"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 视听智能服务 > 获取音频文件信息"
doc_id: "3MWwnMfOYJ"
updated_at: "2026-08-06 15:50:51"
---

> Source: https://open.dingtalk.com/document/development/api-getaudiofileinfo
> Path: 应用开发 / 服务端API / 更多开放 > 视听智能服务 > 获取音频文件信息
> Updated: 2026-08-06 15:50:51

# 获取音频文件信息

通过本接口，获取智能音频设备（A1或B1）产生的音频文件信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/device/audio/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Device.Audio.Read-智能设备音频读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| deviceType | String | 是 | 设备类型：   - 针对A1类型时，需要传递A1。 - 针对B1电子工牌类型时，需要传递B1。 |
| fileId | String | 是 | 文件ID，通过[分页查询指定设备的音频文件列表](1312-api-queryaudiofile.md)接口返回的文件ID。 |

### **请求示例**

HTTP

```
POST /v1.0/dvi/device/audio/get HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:286xxxxjdd6898a
Content-Type:application/json

{
  "deviceType" : "A1",
  "fileId" : "fedf6xxxxdee"
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
        com.aliyun.dingtalkdvi_1_0.models.GetAudioFileInfoHeaders getAudioFileInfoHeaders = new com.aliyun.dingtalkdvi_1_0.models.GetAudioFileInfoHeaders();
        getAudioFileInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.GetAudioFileInfoRequest getAudioFileInfoRequest = new com.aliyun.dingtalkdvi_1_0.models.GetAudioFileInfoRequest()
                .setDeviceType("A1")
                .setFileId("fedf6xxxxdee");
        try {
            client.getAudioFileInfoWithOptions(getAudioFileInfoRequest, getAudioFileInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_audio_file_info_headers = dingtalkdvi__1__0_models.GetAudioFileInfoHeaders()
        get_audio_file_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_audio_file_info_request = dingtalkdvi__1__0_models.GetAudioFileInfoRequest(
            device_type='A1',
            file_id='fedf6xxxxdee'
        )
        try:
            client.get_audio_file_info_with_options(get_audio_file_info_request, get_audio_file_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_audio_file_info_headers = dingtalkdvi__1__0_models.GetAudioFileInfoHeaders()
        get_audio_file_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_audio_file_info_request = dingtalkdvi__1__0_models.GetAudioFileInfoRequest(
            device_type='A1',
            file_id='fedf6xxxxdee'
        )
        try:
            await client.get_audio_file_info_with_options_async(get_audio_file_info_request, get_audio_file_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetAudioFileInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\GetAudioFileInfoRequest;
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
        $getAudioFileInfoHeaders = new GetAudioFileInfoHeaders([]);
        $getAudioFileInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getAudioFileInfoRequest = new GetAudioFileInfoRequest([
            "deviceType" => "A1",
            "fileId" => "fedf6xxxxdee"
        ]);
        try {
            $client->getAudioFileInfoWithOptions($getAudioFileInfoRequest, $getAudioFileInfoHeaders, new RuntimeOptions([]));
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

  getAudioFileInfoHeaders := &dingtalkdvi_1_0.GetAudioFileInfoHeaders{}
  getAudioFileInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getAudioFileInfoRequest := &dingtalkdvi_1_0.GetAudioFileInfoRequest{
    DeviceType: tea.String("A1"),
    FileId: tea.String("fedf6xxxxdee"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetAudioFileInfoWithOptions(getAudioFileInfoRequest, getAudioFileInfoHeaders, &util.RuntimeOptions{})
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
    let getAudioFileInfoHeaders = new dingtalkdvi_1_0.GetAudioFileInfoHeaders({ });
    getAudioFileInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getAudioFileInfoRequest = new dingtalkdvi_1_0.GetAudioFileInfoRequest({
      deviceType: 'A1',
      fileId: 'fedf6xxxxdee',
    });
    try {
      await client.getAudioFileInfoWithOptions(getAudioFileInfoRequest, getAudioFileInfoHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAudioFileInfoHeaders getAudioFileInfoHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAudioFileInfoHeaders();
            getAudioFileInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAudioFileInfoRequest getAudioFileInfoRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.GetAudioFileInfoRequest
            {
                DeviceType = "A1",
                FileId = "fedf6xxxxdee",
            };
            try
            {
                client.GetAudioFileInfoWithOptions(getAudioFileInfoRequest, getAudioFileInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 文件对象。 |
| fileId | String | 文件ID。 |
| fileName | String | 文件名。 |
| creatorUserId | String | 文件所属人。 |
| createTime | Long | 文件生成时间。 |
| duration | Long | 音频文件时长。 |
| fileSize | Long | 文件大小。 |
| attributes | Map | 文件扩展属性,针对不同类型设备产生的文件不同返回的数据不同。对于A1文件，会有以下可选Key返回：   - **minutesId**：听记ID 仅针对A1文件已生成听记时返回对应的听记ID。 - **businessOrder**：通过JSAPI开启A1录音，且在开启录音时设置过此参数时返回。 - **location.latitude**：地理纬度位置信息。 - **location.longitude**：地理经度位置信息。 - **location.title**：地址。 - **location.desc**：详细地址。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "fileId" : "fedf6edxxxx862a1dee",
    "fileName" : "2025-09-15 14:22:53 录音",
    "creatorUserId" : "10011315261777276077",
    "createTime" : 1757917373000,
    "duration" : 60000,
    "fileSize" : 129863
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.fast | request too fast. | 请求过快被限流。 |
| 400 | illegalRequest | Illegal request. | 请求异常。 |
| 400 | request.permission.denied | api permission denied. | 暂无调用权限 |
| 500 | systemError | system error. | 系统异常。 |
