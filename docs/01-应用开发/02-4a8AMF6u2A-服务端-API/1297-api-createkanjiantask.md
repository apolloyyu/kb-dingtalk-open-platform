---
title: "创建看鉴任务"
source_url: "https://open.dingtalk.com/document/development/api-createkanjiantask"
namespace: "development"
slug: "api-createkanjiantask"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > BV 看鉴 > 看鉴任务 > 创建看鉴任务"
doc_id: "doc_427cd99caccb4836"
updated_at: "2026-11-17 17:35:15"
---

> Source: https://open.dingtalk.com/document/development/api-createkanjiantask
> Path: 应用开发 / 服务端 API / 视听智能服务 > BV 看鉴 > 看鉴任务 > 创建看鉴任务
> Updated: 2026-11-17 17:35:15

# 创建看鉴任务

调用本接口，创建看鉴主任务及子任务，返回任务 ID。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/tasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Task.Write-钉钉AI看鉴任务数据写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| description | String | 是 | 任务描述，作为任务指令。 |
| executorUserIds | Array of String | 是 | 执行者。 |
| subTasks | Array | 否 | 子任务列表。 |
| instruction | String | 否 | 子任务说明。 |
| name | String | 否 | 子任务名称。 |
| taskId | String | 否 | 子任务 ID。  **[!NOTE]**  不传由服务端生成，更新时传原 ID 可保留该子任务。 |
| name | String | 是 | 任务名称。 |
| operatorUserId | String | 是 | 操作人 userId，作为任务创建人。 |
| reportContent | String | 否 | 报告要求文本。 |
| adminUserIds | Array of String | 是 | 管理员userId。 |

### **请求示例**

HTTP

```
POST /v1.0/dvi/bv/kanjian/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0215fxxxx1d52
Content-Type:application/json

{
  "description" : "check shelf and price tags",
  "executorUserIds" : [ "user0001" ],
  "subTasks" : [ {
    "instruction" : "is the shelf tidy",
    "name" : "shelf-check",
    "taskId" : "subTask0001"
  } ],
  "name" : "daily-check",
  "operatorUserId" : "user0001",
  "reportContent" : "summarize issues",
  "adminUserIds" : [ "user0001" ]
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
        com.aliyun.dingtalkdvi_1_0.models.CreateKanjianTaskHeaders createKanjianTaskHeaders = new com.aliyun.dingtalkdvi_1_0.models.CreateKanjianTaskHeaders();
        createKanjianTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.CreateKanjianTaskRequest.CreateKanjianTaskRequestSubTasks subTasks0 = new com.aliyun.dingtalkdvi_1_0.models.CreateKanjianTaskRequest.CreateKanjianTaskRequestSubTasks()
                .setInstruction("is the shelf tidy")
                .setName("shelf-check")
                .setTaskId("subTask0001");
        com.aliyun.dingtalkdvi_1_0.models.CreateKanjianTaskRequest createKanjianTaskRequest = new com.aliyun.dingtalkdvi_1_0.models.CreateKanjianTaskRequest()
                .setDescription("check shelf and price tags")
                .setExecutorUserIds(java.util.Arrays.asList(
                    "user0001"
                ))
                .setSubTasks(java.util.Arrays.asList(
                    subTasks0
                ))
                .setName("daily-check")
                .setOperatorUserId("user0001")
                .setReportContent("summarize issues")
                .setAdminUserIds(java.util.Arrays.asList(
                    "user0001"
                ));
        try {
            client.createKanjianTaskWithOptions(createKanjianTaskRequest, createKanjianTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_kanjian_task_headers = dingtalkdvi__1__0_models.CreateKanjianTaskHeaders()
        create_kanjian_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        sub_tasks_0 = dingtalkdvi__1__0_models.CreateKanjianTaskRequestSubTasks(
            instruction='is the shelf tidy',
            name='shelf-check',
            task_id='subTask0001'
        )
        create_kanjian_task_request = dingtalkdvi__1__0_models.CreateKanjianTaskRequest(
            description='check shelf and price tags',
            executor_user_ids=[
                'user0001'
            ],
            sub_tasks=[
                sub_tasks_0
            ],
            name='daily-check',
            operator_user_id='user0001',
            report_content='summarize issues',
            admin_user_ids=[
                'user0001'
            ]
        )
        try:
            client.create_kanjian_task_with_options(create_kanjian_task_request, create_kanjian_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_kanjian_task_headers = dingtalkdvi__1__0_models.CreateKanjianTaskHeaders()
        create_kanjian_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        sub_tasks_0 = dingtalkdvi__1__0_models.CreateKanjianTaskRequestSubTasks(
            instruction='is the shelf tidy',
            name='shelf-check',
            task_id='subTask0001'
        )
        create_kanjian_task_request = dingtalkdvi__1__0_models.CreateKanjianTaskRequest(
            description='check shelf and price tags',
            executor_user_ids=[
                'user0001'
            ],
            sub_tasks=[
                sub_tasks_0
            ],
            name='daily-check',
            operator_user_id='user0001',
            report_content='summarize issues',
            admin_user_ids=[
                'user0001'
            ]
        )
        try:
            await client.create_kanjian_task_with_options_async(create_kanjian_task_request, create_kanjian_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\CreateKanjianTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\CreateKanjianTaskRequest\subTasks;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\CreateKanjianTaskRequest;
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
        $createKanjianTaskHeaders = new CreateKanjianTaskHeaders([]);
        $createKanjianTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $subTasks0 = new subTasks([
            "instruction" => "is the shelf tidy",
            "name" => "shelf-check",
            "taskId" => "subTask0001"
        ]);
        $createKanjianTaskRequest = new CreateKanjianTaskRequest([
            "description" => "check shelf and price tags",
            "executorUserIds" => [
                "user0001"
            ],
            "subTasks" => [
                $subTasks0
            ],
            "name" => "daily-check",
            "operatorUserId" => "user0001",
            "reportContent" => "summarize issues",
            "adminUserIds" => [
                "user0001"
            ]
        ]);
        try {
            $client->createKanjianTaskWithOptions($createKanjianTaskRequest, $createKanjianTaskHeaders, new RuntimeOptions([]));
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

  createKanjianTaskHeaders := &dingtalkdvi_1_0.CreateKanjianTaskHeaders{}
  createKanjianTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  subTasks0 := &dingtalkdvi_1_0.CreateKanjianTaskRequestSubTasks{
    Instruction: tea.String("is the shelf tidy"),
    Name: tea.String("shelf-check"),
    TaskId: tea.String("subTask0001"),
  }
  createKanjianTaskRequest := &dingtalkdvi_1_0.CreateKanjianTaskRequest{
    Description: tea.String("check shelf and price tags"),
    ExecutorUserIds: []*string{tea.String("user0001")},
    SubTasks: []*dingtalkdvi_1_0.CreateKanjianTaskRequestSubTasks{subTasks0},
    Name: tea.String("daily-check"),
    OperatorUserId: tea.String("user0001"),
    ReportContent: tea.String("summarize issues"),
    AdminUserIds: []*string{tea.String("user0001")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateKanjianTaskWithOptions(createKanjianTaskRequest, createKanjianTaskHeaders, &util.RuntimeOptions{})
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
    let createKanjianTaskHeaders = new dingtalkdvi_1_0.CreateKanjianTaskHeaders({ });
    createKanjianTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let subTasks0 = new dingtalkdvi_1_0.CreateKanjianTaskRequestSubTasks({
      instruction: 'is the shelf tidy',
      name: 'shelf-check',
      taskId: 'subTask0001',
    });
    let createKanjianTaskRequest = new dingtalkdvi_1_0.CreateKanjianTaskRequest({
      description: 'check shelf and price tags',
      executorUserIds: [
        'user0001'
      ],
      subTasks: [
        subTasks0
      ],
      name: 'daily-check',
      operatorUserId: 'user0001',
      reportContent: 'summarize issues',
      adminUserIds: [
        'user0001'
      ],
    });
    try {
      await client.createKanjianTaskWithOptions(createKanjianTaskRequest, createKanjianTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskHeaders createKanjianTaskHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskHeaders();
            createKanjianTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskRequest.CreateKanjianTaskRequestSubTasks subTasks0 = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskRequest.CreateKanjianTaskRequestSubTasks
            {
                Instruction = "is the shelf tidy",
                Name = "shelf-check",
                TaskId = "subTask0001",
            };
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskRequest createKanjianTaskRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskRequest
            {
                Description = "check shelf and price tags",
                ExecutorUserIds = new List<string>
                {
                    "user0001"
                },
                SubTasks = new List<AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.CreateKanjianTaskRequest.CreateKanjianTaskRequestSubTasks>
                {
                    subTasks0
                },
                Name = "daily-check",
                OperatorUserId = "user0001",
                ReportContent = "summarize issues",
                AdminUserIds = new List<string>
                {
                    "user0001"
                },
            };
            try
            {
                client.CreateKanjianTaskWithOptions(createKanjianTaskRequest, createKanjianTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| taskId | String | 任务id。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "taskId" : "task0001"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数非法。executorUserIds、adminUserIds 至少包含 1 个本企业员工，且都须能解析 | 参数非法。executorUserIds、adminUserIds 至少包含 1 个本企业员工，且都须能解析 |
| 400 | param.empty | 参数为空。operatorUserId、name、description、executorUserIds 必填 | 参数为空。operatorUserId、name、description、executorUserIds 必填 |
| 400 | emp.notExist | 操作人不是本企业员工，请检查 operatorUserId | 操作人不是本企业员工，请检查 operatorUserId |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | task.itemLimitExceeded | 子任务数量超过上限，默认最多 50 个 | 子任务数量超过上限，默认最多 50 个 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
| 400 | task.fieldTooLong | 任务内容超出字数限制。默认 name 最多 50 字，description 最多 500 字，items 的名称、说明和选项合计最多 5000 字，reportContent 最多 10000 字 | 任务内容超出字数限制。默认 name 最多 50 字，description 最多 500 字，items 的名称、说明和选项合计最多 5000 字，reportContent 最多 10000 字 |
| 400 | task.orgLimitExceeded | 企业任务数量已达上限 | 企业任务数量已达上限 |
| 400 | task.userLimitExceeded | 操作人管理的任务数量已达上限 | 操作人管理的任务数量已达上限 |
| 429 | system.busy | 系统繁忙，请稍后重试 | 系统繁忙，请稍后重试 |
