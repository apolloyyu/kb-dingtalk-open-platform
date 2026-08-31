---
title: "获取服务待办信息"
source_url: "https://open.dingtalk.com/document/development/api-listservicetodo"
namespace: "development"
slug: "api-listservicetodo"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 视听智能服务 > 获取服务待办信息"
doc_id: "tJX9PamRcN"
updated_at: "2026-06-24 13:44:31"
---

> Source: https://open.dingtalk.com/document/development/api-listservicetodo
> Path: 应用开发 / 服务端 API / 更多开放 > 视听智能服务 > 获取服务待办信息
> Updated: 2026-06-24 13:44:31

# 获取服务待办信息

调用本接口，通过服务记录ID，获取AI销售管理中的服务记录待列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/service-todos |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Sale.Service.Read-钉钉AI销售管理服务数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recordId | String | 是 | 服务记录ID，可通过[分页获取企业下的服务记录信息](1311-api-listservicerecord.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/service-todos?recordId=2cf7eaxxxx02c32 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:ac21axxxx81ee
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
        com.aliyun.dingtalkdvi_1_0.models.ListServiceTodoHeaders listServiceTodoHeaders = new com.aliyun.dingtalkdvi_1_0.models.ListServiceTodoHeaders();
        listServiceTodoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.ListServiceTodoRequest listServiceTodoRequest = new com.aliyun.dingtalkdvi_1_0.models.ListServiceTodoRequest()
                .setRecordId("2cf7eaxxxx02c32");
        try {
            client.listServiceTodoWithOptions(listServiceTodoRequest, listServiceTodoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_service_todo_headers = dingtalkdvi__1__0_models.ListServiceTodoHeaders()
        list_service_todo_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_service_todo_request = dingtalkdvi__1__0_models.ListServiceTodoRequest(
            record_id='2cf7eaxxxx02c32'
        )
        try:
            client.list_service_todo_with_options(list_service_todo_request, list_service_todo_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_service_todo_headers = dingtalkdvi__1__0_models.ListServiceTodoHeaders()
        list_service_todo_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_service_todo_request = dingtalkdvi__1__0_models.ListServiceTodoRequest(
            record_id='2cf7eaxxxx02c32'
        )
        try:
            await client.list_service_todo_with_options_async(list_service_todo_request, list_service_todo_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListServiceTodoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListServiceTodoRequest;
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
        $listServiceTodoHeaders = new ListServiceTodoHeaders([]);
        $listServiceTodoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listServiceTodoRequest = new ListServiceTodoRequest([
            "recordId" => "2cf7eaxxxx02c32"
        ]);
        try {
            $client->listServiceTodoWithOptions($listServiceTodoRequest, $listServiceTodoHeaders, new RuntimeOptions([]));
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

  listServiceTodoHeaders := &dingtalkdvi_1_0.ListServiceTodoHeaders{}
  listServiceTodoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listServiceTodoRequest := &dingtalkdvi_1_0.ListServiceTodoRequest{
    RecordId: tea.String("2cf7eaxxxx02c32"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListServiceTodoWithOptions(listServiceTodoRequest, listServiceTodoHeaders, &util.RuntimeOptions{})
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
    let listServiceTodoHeaders = new dingtalkdvi_1_0.ListServiceTodoHeaders({ });
    listServiceTodoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listServiceTodoRequest = new dingtalkdvi_1_0.ListServiceTodoRequest({
      recordId: '2cf7eaxxxx02c32',
    });
    try {
      await client.listServiceTodoWithOptions(listServiceTodoRequest, listServiceTodoHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceTodoHeaders listServiceTodoHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceTodoHeaders();
            listServiceTodoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceTodoRequest listServiceTodoRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceTodoRequest
            {
                RecordId = "2cf7eaxxxx02c32",
            };
            try
            {
                client.ListServiceTodoWithOptions(listServiceTodoRequest, listServiceTodoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 服务记录列表。 |
| uuid | String | 服务待办ID标识。 |
| dingTodoId | String | 钉钉待办ID，针对产生了钉钉待办的场景时返回此数据。 |
| creator | String | 待办创建人userId。 |
| todoContent | String | 待办详情内容。 |
| planFinishDate | Long | 截止时间戳，单位毫秒。 |
| finished | Boolean | 是否完成：   - **true**：完成 - **false**：未完成 |
| executors | Array | 执行人列表。 |
| userId | String | 执行人userId。 |
| name | String | 执行人名称。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "uuid" : "2cf7xxxxc32",
    "dingTodoId" : "1234",
    "creator" : "98347djds",
    "todoContent" : "拜访李总",
    "planFinishDate" : 123456,
    "finished" : true,
    "executors" : [ {
      "userId" : "userId",
      "name" : "王五"
    } ]
  } ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
