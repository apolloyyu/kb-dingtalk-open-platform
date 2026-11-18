---
title: "更新看鉴主任务"
source_url: "https://open.dingtalk.com/document/development/api-updatekanjiantask"
namespace: "development"
slug: "api-updatekanjiantask"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > DingTalk BV > 看鉴任务 > 更新看鉴主任务"
doc_id: "doc_45d7e999598c4ab7"
updated_at: "2026-11-17 17:35:17"
---

> Source: https://open.dingtalk.com/document/development/api-updatekanjiantask
> Path: 应用开发 / 服务端 API / 视听智能服务 > DingTalk BV > 看鉴任务 > 更新看鉴主任务
> Updated: 2026-11-17 17:35:17

# 更新看鉴主任务

调用本接口，更新看鉴主任务，只修改传入的非空字段。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/tasks |
| HTTP Method | PATCH |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Task.Write-钉钉AI看鉴任务数据写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| description | String | 否 | 任务描述。 |
| subTasks | Array | 否 | 子任务列表。  **[!NOTE]**  传入子任务、管理员或执行人时，对应列表按本次传入全量覆盖。 |
| instruction | String | 否 | 子任务说明。 |
| name | String | 否 | 子任务名称。 |
| taskId | String | 否 | 子任务 ID，可通过[分页查询看鉴任务列表](1300-api-listkanjiantasks.md)接口获取。 |
| name | String | 否 | 任务名称。 |
| operatorUserId | String | 否 | 操作人 userId。 |
| reportContent | String | 否 | 报告要求文本。 |
| taskId | String | 否 | 主任务 ID，可通过[分页查询看鉴任务列表](1300-api-listkanjiantasks.md)接口获取。 |
| adminUserIds | Array of String | 否 | 任务管理员。  **[!NOTE]**  传入子任务、管理员或执行人时，对应列表按本次传入全量覆盖。 |
| executorUserIds | Array of String | 否 | 任务执行者。  **[!NOTE]**  传入子任务、管理员或执行人时，对应列表按本次传入全量覆盖。 |

### **请求示例**

HTTP

```
PATCH /v1.0/dvi/bv/kanjian/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0917fxxxx8901d52
Content-Type:application/json

{
  "description" : "check shelf and price tags",
  "subTasks" : [ {
    "instruction" : "is the shelf tidy",
    "name" : "shelf-check",
    "taskId" : "item0001"
  } ],
  "name" : "daily-check-v2",
  "operatorUserId" : "manager1234",
  "reportContent" : "summarize issues",
  "taskId" : "task0001",
  "adminUserIds" : [ "admin0001" ],
  "executorUserIds" : [ "staff0001" ]
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
        com.aliyun.dingtalkdvi_1_0.models.UpdateKanjianTaskHeaders updateKanjianTaskHeaders = new com.aliyun.dingtalkdvi_1_0.models.UpdateKanjianTaskHeaders();
        updateKanjianTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.UpdateKanjianTaskRequest.UpdateKanjianTaskRequestSubTasks subTasks0 = new com.aliyun.dingtalkdvi_1_0.models.UpdateKanjianTaskRequest.UpdateKanjianTaskRequestSubTasks()
                .setInstruction("is the shelf tidy")
                .setName("shelf-check")
                .setTaskId("item0001");
        com.aliyun.dingtalkdvi_1_0.models.UpdateKanjianTaskRequest updateKanjianTaskRequest = new com.aliyun.dingtalkdvi_1_0.models.UpdateKanjianTaskRequest()
                .setDescription("check shelf and price tags")
                .setSubTasks(java.util.Arrays.asList(
                    subTasks0
                ))
                .setName("daily-check-v2")
                .setOperatorUserId("manager1234")
                .setReportContent("summarize issues")
                .setTaskId("task0001")
                .setAdminUserIds(java.util.Arrays.asList(
                    "admin0001"
                ))
                .setExecutorUserIds(java.util.Arrays.asList(
                    "staff0001"
                ));
        try {
            client.updateKanjianTaskWithOptions(updateKanjianTaskRequest, updateKanjianTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_kanjian_task_headers = dingtalkdvi__1__0_models.UpdateKanjianTaskHeaders()
        update_kanjian_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        sub_tasks_0 = dingtalkdvi__1__0_models.UpdateKanjianTaskRequestSubTasks(
            instruction='is the shelf tidy',
            name='shelf-check',
            task_id='item0001'
        )
        update_kanjian_task_request = dingtalkdvi__1__0_models.UpdateKanjianTaskRequest(
            description='check shelf and price tags',
            sub_tasks=[
                sub_tasks_0
            ],
            name='daily-check-v2',
            operator_user_id='manager1234',
            report_content='summarize issues',
            task_id='task0001',
            admin_user_ids=[
                'admin0001'
            ],
            executor_user_ids=[
                'staff0001'
            ]
        )
        try:
            client.update_kanjian_task_with_options(update_kanjian_task_request, update_kanjian_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_kanjian_task_headers = dingtalkdvi__1__0_models.UpdateKanjianTaskHeaders()
        update_kanjian_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        sub_tasks_0 = dingtalkdvi__1__0_models.UpdateKanjianTaskRequestSubTasks(
            instruction='is the shelf tidy',
            name='shelf-check',
            task_id='item0001'
        )
        update_kanjian_task_request = dingtalkdvi__1__0_models.UpdateKanjianTaskRequest(
            description='check shelf and price tags',
            sub_tasks=[
                sub_tasks_0
            ],
            name='daily-check-v2',
            operator_user_id='manager1234',
            report_content='summarize issues',
            task_id='task0001',
            admin_user_ids=[
                'admin0001'
            ],
            executor_user_ids=[
                'staff0001'
            ]
        )
        try:
            await client.update_kanjian_task_with_options_async(update_kanjian_task_request, update_kanjian_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\UpdateKanjianTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\UpdateKanjianTaskRequest\subTasks;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\UpdateKanjianTaskRequest;
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
        $updateKanjianTaskHeaders = new UpdateKanjianTaskHeaders([]);
        $updateKanjianTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $subTasks0 = new subTasks([
            "instruction" => "is the shelf tidy",
            "name" => "shelf-check",
            "taskId" => "item0001"
        ]);
        $updateKanjianTaskRequest = new UpdateKanjianTaskRequest([
            "description" => "check shelf and price tags",
            "subTasks" => [
                $subTasks0
            ],
            "name" => "daily-check-v2",
            "operatorUserId" => "manager1234",
            "reportContent" => "summarize issues",
            "taskId" => "task0001",
            "adminUserIds" => [
                "admin0001"
            ],
            "executorUserIds" => [
                "staff0001"
            ]
        ]);
        try {
            $client->updateKanjianTaskWithOptions($updateKanjianTaskRequest, $updateKanjianTaskHeaders, new RuntimeOptions([]));
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

  updateKanjianTaskHeaders := &dingtalkdvi_1_0.UpdateKanjianTaskHeaders{}
  updateKanjianTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  subTasks0 := &dingtalkdvi_1_0.UpdateKanjianTaskRequestSubTasks{
    Instruction: tea.String("is the shelf tidy"),
    Name: tea.String("shelf-check"),
    TaskId: tea.String("item0001"),
  }
  updateKanjianTaskRequest := &dingtalkdvi_1_0.UpdateKanjianTaskRequest{
    Description: tea.String("check shelf and price tags"),
    SubTasks: []*dingtalkdvi_1_0.UpdateKanjianTaskRequestSubTasks{subTasks0},
    Name: tea.String("daily-check-v2"),
    OperatorUserId: tea.String("manager1234"),
    ReportContent: tea.String("summarize issues"),
    TaskId: tea.String("task0001"),
    AdminUserIds: []*string{tea.String("admin0001")},
    ExecutorUserIds: []*string{tea.String("staff0001")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateKanjianTaskWithOptions(updateKanjianTaskRequest, updateKanjianTaskHeaders, &util.RuntimeOptions{})
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
    let updateKanjianTaskHeaders = new dingtalkdvi_1_0.UpdateKanjianTaskHeaders({ });
    updateKanjianTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let subTasks0 = new dingtalkdvi_1_0.UpdateKanjianTaskRequestSubTasks({
      instruction: 'is the shelf tidy',
      name: 'shelf-check',
      taskId: 'item0001',
    });
    let updateKanjianTaskRequest = new dingtalkdvi_1_0.UpdateKanjianTaskRequest({
      description: 'check shelf and price tags',
      subTasks: [
        subTasks0
      ],
      name: 'daily-check-v2',
      operatorUserId: 'manager1234',
      reportContent: 'summarize issues',
      taskId: 'task0001',
      adminUserIds: [
        'admin0001'
      ],
      executorUserIds: [
        'staff0001'
      ],
    });
    try {
      await client.updateKanjianTaskWithOptions(updateKanjianTaskRequest, updateKanjianTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskHeaders updateKanjianTaskHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskHeaders();
            updateKanjianTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskRequest.UpdateKanjianTaskRequestSubTasks subTasks0 = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskRequest.UpdateKanjianTaskRequestSubTasks
            {
                Instruction = "is the shelf tidy",
                Name = "shelf-check",
                TaskId = "item0001",
            };
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskRequest updateKanjianTaskRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskRequest
            {
                Description = "check shelf and price tags",
                SubTasks = new List<AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.UpdateKanjianTaskRequest.UpdateKanjianTaskRequestSubTasks>
                {
                    subTasks0
                },
                Name = "daily-check-v2",
                OperatorUserId = "manager1234",
                ReportContent = "summarize issues",
                TaskId = "task0001",
                AdminUserIds = new List<string>
                {
                    "admin0001"
                },
                ExecutorUserIds = new List<string>
                {
                    "staff0001"
                },
            };
            try
            {
                client.UpdateKanjianTaskWithOptions(updateKanjianTaskRequest, updateKanjianTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| 400 | param.empty | 参数为空。taskId、operatorUserId 必填 | 参数为空。taskId、operatorUserId 必填 |
| 400 | emp.notExist | 操作人不是本企业员工，请检查 operatorUserId | 操作人不是本企业员工，请检查 operatorUserId |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
| 400 | task.notFound | 任务不存在 | 任务不存在 |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | task.itemLimitExceeded | 子任务数量超过上限，默认最多 50 个 | 子任务数量超过上限，默认最多 50 个 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
| 400 | task.noPermission | 无任务操作权限，仅任务管理员可操作 | 无任务操作权限，仅任务管理员可操作 |
| 400 | subTask.notSupported | 仅支持主任务，不支持子任务 | 仅支持主任务，不支持子任务 |
| 400 | task.fieldTooLong | 任务内容超出字数限制。默认 name 最多 50 字，description 最多 500 字，items 的名称、说明和选项合计最多 5000 字，reportContent 最多 10000 字 | 任务内容超出字数限制。默认 name 最多 50 字，description 最多 500 字，items 的名称、说明和选项合计最多 5000 字，reportContent 最多 10000 字 |
