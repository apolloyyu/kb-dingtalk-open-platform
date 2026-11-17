---
title: "看鉴记录首次绑定主任务"
source_url: "https://open.dingtalk.com/document/development/api-bindkanjianrecordtask"
namespace: "development"
slug: "api-bindkanjianrecordtask"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > BV 看鉴 > 看鉴记录 > 看鉴记录首次绑定主任务"
doc_id: "doc_b5d89782ea6b4293"
updated_at: "2026-11-17 17:35:11"
---

> Source: https://open.dingtalk.com/document/development/api-bindkanjianrecordtask
> Path: 应用开发 / 服务端 API / 视听智能服务 > BV 看鉴 > 看鉴记录 > 看鉴记录首次绑定主任务
> Updated: 2026-11-17 17:35:11

# 看鉴记录首次绑定主任务

调用本接口，给看鉴 BV 记录首次绑定主任务。记录已完成转写时，绑定后会按该任务触发分析。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/records/task |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Record.Write-钉钉AI看鉴记录数据写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| mainTaskId | String | 是 | 要绑定的主任务 ID，可通过[分页查询看鉴记录列表](1293-api-listkanjianrecords.md)接口获取。 |
| operatorUserId | String | 是 | 操作人 userId。  **[!NOTE]**  须为企业管理员或有记录绑定任务权限。 |
| recordId | String | 是 | 记录 ID，可通过[分页查询看鉴记录列表](1293-api-listkanjianrecords.md)接口获取。 |

### **请求示例**

HTTP

```
POST /v1.0/dvi/bv/kanjian/records/task HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0215xxxxx91d52
Content-Type:application/json

{
  "mainTaskId" : "task0001",
  "operatorUserId" : "manager1234",
  "recordId" : "record0001"
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
        com.aliyun.dingtalkdvi_1_0.models.BindKanjianRecordTaskHeaders bindKanjianRecordTaskHeaders = new com.aliyun.dingtalkdvi_1_0.models.BindKanjianRecordTaskHeaders();
        bindKanjianRecordTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.BindKanjianRecordTaskRequest bindKanjianRecordTaskRequest = new com.aliyun.dingtalkdvi_1_0.models.BindKanjianRecordTaskRequest()
                .setMainTaskId("task0001")
                .setOperatorUserId("manager1234")
                .setRecordId("record0001");
        try {
            client.bindKanjianRecordTaskWithOptions(bindKanjianRecordTaskRequest, bindKanjianRecordTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        bind_kanjian_record_task_headers = dingtalkdvi__1__0_models.BindKanjianRecordTaskHeaders()
        bind_kanjian_record_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        bind_kanjian_record_task_request = dingtalkdvi__1__0_models.BindKanjianRecordTaskRequest(
            main_task_id='task0001',
            operator_user_id='manager1234',
            record_id='record0001'
        )
        try:
            client.bind_kanjian_record_task_with_options(bind_kanjian_record_task_request, bind_kanjian_record_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        bind_kanjian_record_task_headers = dingtalkdvi__1__0_models.BindKanjianRecordTaskHeaders()
        bind_kanjian_record_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        bind_kanjian_record_task_request = dingtalkdvi__1__0_models.BindKanjianRecordTaskRequest(
            main_task_id='task0001',
            operator_user_id='manager1234',
            record_id='record0001'
        )
        try:
            await client.bind_kanjian_record_task_with_options_async(bind_kanjian_record_task_request, bind_kanjian_record_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\BindKanjianRecordTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\BindKanjianRecordTaskRequest;
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
        $bindKanjianRecordTaskHeaders = new BindKanjianRecordTaskHeaders([]);
        $bindKanjianRecordTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $bindKanjianRecordTaskRequest = new BindKanjianRecordTaskRequest([
            "mainTaskId" => "task0001",
            "operatorUserId" => "manager1234",
            "recordId" => "record0001"
        ]);
        try {
            $client->bindKanjianRecordTaskWithOptions($bindKanjianRecordTaskRequest, $bindKanjianRecordTaskHeaders, new RuntimeOptions([]));
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

  bindKanjianRecordTaskHeaders := &dingtalkdvi_1_0.BindKanjianRecordTaskHeaders{}
  bindKanjianRecordTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  bindKanjianRecordTaskRequest := &dingtalkdvi_1_0.BindKanjianRecordTaskRequest{
    MainTaskId: tea.String("task0001"),
    OperatorUserId: tea.String("manager1234"),
    RecordId: tea.String("record0001"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BindKanjianRecordTaskWithOptions(bindKanjianRecordTaskRequest, bindKanjianRecordTaskHeaders, &util.RuntimeOptions{})
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
    let bindKanjianRecordTaskHeaders = new dingtalkdvi_1_0.BindKanjianRecordTaskHeaders({ });
    bindKanjianRecordTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let bindKanjianRecordTaskRequest = new dingtalkdvi_1_0.BindKanjianRecordTaskRequest({
      mainTaskId: 'task0001',
      operatorUserId: 'manager1234',
      recordId: 'record0001',
    });
    try {
      await client.bindKanjianRecordTaskWithOptions(bindKanjianRecordTaskRequest, bindKanjianRecordTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.BindKanjianRecordTaskHeaders bindKanjianRecordTaskHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.BindKanjianRecordTaskHeaders();
            bindKanjianRecordTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.BindKanjianRecordTaskRequest bindKanjianRecordTaskRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.BindKanjianRecordTaskRequest
            {
                MainTaskId = "task0001",
                OperatorUserId = "manager1234",
                RecordId = "record0001",
            };
            try
            {
                client.BindKanjianRecordTaskWithOptions(bindKanjianRecordTaskRequest, bindKanjianRecordTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 固定为 true。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "success" : true
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 参数为空。recordId、mainTaskId、operatorUserId 必填 | 参数为空。recordId、mainTaskId、operatorUserId 必填 |
| 400 | emp.notExist | 操作人不是本企业员工，请检查 operatorUserId | 操作人不是本企业员工，请检查 operatorUserId |
| 400 | task.notFound | 主任务不存在，请检查 mainTaskId | 主任务不存在，请检查 mainTaskId |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | record.notFound | 看鉴记录不存在或已删除 | 看鉴记录不存在或已删除 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
| 400 | task.alreadyBound | 记录已绑定任务，不能重复绑定 | 记录已绑定任务，不能重复绑定 |
| 400 | record.invalidStatus | 记录状态不支持绑定任务，仅待分析的记录可绑定 | 记录状态不支持绑定任务，仅待分析的记录可绑定 |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
