---
title: "根据听记ID获取A1音频文件信息"
source_url: "https://open.dingtalk.com/document/development/api-queryfileinfobyminutesid"
namespace: "development"
slug: "api-queryfileinfobyminutesid"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 视听智能服务 > 根据听记ID获取A1音频文件信息"
doc_id: "9L6rHiVdWY"
updated_at: "2026-08-06 15:50:53"
---

> Source: https://open.dingtalk.com/document/development/api-queryfileinfobyminutesid
> Path: 应用开发 / 服务端 API / 更多开放 > 视听智能服务 > 根据听记ID获取A1音频文件信息
> Updated: 2026-08-06 15:50:53

# 根据听记ID获取A1音频文件信息

通过本接口可以使用A1文件产生的听记ID反查A1文件信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/audios/minutes |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Device.Audio.Read-智能设备音频读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| minutesId | String | 是 | 听记ID，可通过[获取音频文件信息](1304-api-getaudiofileinfo.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/audios/minutes?minutesId=76327*****385f39 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d0c74******89ce760
Content-Type:application/json
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
        com.aliyun.dingtalkdvi_1_0.models.QueryFileInfoByMinutesIdHeaders queryFileInfoByMinutesIdHeaders = new com.aliyun.dingtalkdvi_1_0.models.QueryFileInfoByMinutesIdHeaders();
        queryFileInfoByMinutesIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.QueryFileInfoByMinutesIdRequest queryFileInfoByMinutesIdRequest = new com.aliyun.dingtalkdvi_1_0.models.QueryFileInfoByMinutesIdRequest()
                .setMinutesId("76327*****385f39");
        try {
            client.queryFileInfoByMinutesIdWithOptions(queryFileInfoByMinutesIdRequest, queryFileInfoByMinutesIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_file_info_by_minutes_id_headers = dingtalkdvi__1__0_models.QueryFileInfoByMinutesIdHeaders()
        query_file_info_by_minutes_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_file_info_by_minutes_id_request = dingtalkdvi__1__0_models.QueryFileInfoByMinutesIdRequest(
            minutes_id='76327*****385f39'
        )
        try:
            client.query_file_info_by_minutes_id_with_options(query_file_info_by_minutes_id_request, query_file_info_by_minutes_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_file_info_by_minutes_id_headers = dingtalkdvi__1__0_models.QueryFileInfoByMinutesIdHeaders()
        query_file_info_by_minutes_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_file_info_by_minutes_id_request = dingtalkdvi__1__0_models.QueryFileInfoByMinutesIdRequest(
            minutes_id='76327*****385f39'
        )
        try:
            await client.query_file_info_by_minutes_id_with_options_async(query_file_info_by_minutes_id_request, query_file_info_by_minutes_id_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\QueryFileInfoByMinutesIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\QueryFileInfoByMinutesIdRequest;
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
        $queryFileInfoByMinutesIdHeaders = new QueryFileInfoByMinutesIdHeaders([]);
        $queryFileInfoByMinutesIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryFileInfoByMinutesIdRequest = new QueryFileInfoByMinutesIdRequest([
            "minutesId" => "76327*****385f39"
        ]);
        try {
            $client->queryFileInfoByMinutesIdWithOptions($queryFileInfoByMinutesIdRequest, $queryFileInfoByMinutesIdHeaders, new RuntimeOptions([]));
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

  queryFileInfoByMinutesIdHeaders := &dingtalkdvi_1_0.QueryFileInfoByMinutesIdHeaders{}
  queryFileInfoByMinutesIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryFileInfoByMinutesIdRequest := &dingtalkdvi_1_0.QueryFileInfoByMinutesIdRequest{
    MinutesId: tea.String("76327*****385f39"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryFileInfoByMinutesIdWithOptions(queryFileInfoByMinutesIdRequest, queryFileInfoByMinutesIdHeaders, &util.RuntimeOptions{})
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
    let queryFileInfoByMinutesIdHeaders = new dingtalkdvi_1_0.QueryFileInfoByMinutesIdHeaders({ });
    queryFileInfoByMinutesIdHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryFileInfoByMinutesIdRequest = new dingtalkdvi_1_0.QueryFileInfoByMinutesIdRequest({
      minutesId: '76327*****385f39',
    });
    try {
      await client.queryFileInfoByMinutesIdWithOptions(queryFileInfoByMinutesIdRequest, queryFileInfoByMinutesIdHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.QueryFileInfoByMinutesIdHeaders queryFileInfoByMinutesIdHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.QueryFileInfoByMinutesIdHeaders();
            queryFileInfoByMinutesIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.QueryFileInfoByMinutesIdRequest queryFileInfoByMinutesIdRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.QueryFileInfoByMinutesIdRequest
            {
                MinutesId = "76327*****385f39",
            };
            try
            {
                client.QueryFileInfoByMinutesIdWithOptions(queryFileInfoByMinutesIdRequest, queryFileInfoByMinutesIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| attributes | Map | 文件扩展信息。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "fileId" : "1jfFd0*****kKGt-0",
    "fileName" : "2026-04-02 13:28:38 文件",
    "creatorUserId" : "500****7",
    "createTime" : 1773229966000,
    "duration" : 6000,
    "fileSize" : 35185
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
