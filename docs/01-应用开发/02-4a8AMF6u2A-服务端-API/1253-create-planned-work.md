---
title: "创建计划工时"
source_url: "https://open.dingtalk.com/document/development/create-planned-work"
namespace: "development"
slug: "create-planned-work"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Teambition 项目管理 > 工时 > 创建计划工时"
doc_id: "eXvOPA0xrF"
updated_at: "2026-06-03 09:29:38"
---

> Source: https://open.dingtalk.com/document/development/create-planned-work
> Path: 应用开发 / 服务端 API / Teambition 项目管理 > 工时 > 创建计划工时
> Updated: 2026-06-03 09:29:38

# 创建计划工时

调用本接口，新增项目任务中对应的计划工时。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/planTimes |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Task.Write.All-项目应用任务写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| tenantType | String | 是 | 接口校验类型，目前为固定值：organization。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| executorId | String | 是 | 目标任务执行者的userId。 |
| objectId | String | 是 | 对象ID，传项目任务ID，调用[创建项目任务](1222-create-a-project-task.md)接口获取的taskId。 |
| objectType | String | 是 | 对象类型，固定值为task，表示项目任务。 |
| isDuration | Boolean | 是 | 当startDate和endDate指定的时间跨天时，添加的工时时长是否平均分配。   - **true**：表示将planTime时长的计划工时平均分配给对应的日期。 - **false**：表示每个日期都添加planTime时长的计划工时。 |
| includesHolidays | Boolean | 是 | 添加计划工时的日期是否包含假期。   - **true**：表示日期范围内如果有假期，则假期也添加工时。 - **false**：表示日期范围内如果有假期，则假期不添加工时。 |
| submitterId | String | 是 | 工时提交人员的userId。 |
| startDate | String | 是 | 开始日期，格式：yyyy-MM-dd。 |
| endDate | String | 是 | 结束时间，格式：yyyy-MM-dd。 |
| planTime | Long | 是 | 计划工时时长，单位毫秒，1小时即为3600000。  **[!NOTE]**    不超过24小时。 |

### 请求示例

HTTP

```
POST /v1.0/project/users/user001/planTimes?tenantType=organization HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxxxxxx
Content-Type:application/json

{
  "executorId" : "user002",
  "objectId" : "63186xxxxx",
  "objectType" : "task",
  "isDuration" : true,
  "includesHolidays" : true,
  "submitterId" : "123456",
  "startDate" : "2022-09-05",
  "endDate" : "2022-09-05",
  "planTime" : 3600000
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
    public static com.aliyun.dingtalkproject_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkproject_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkproject_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeHeaders createPlanTimeHeaders = new com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeHeaders();
        createPlanTimeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeRequest createPlanTimeRequest = new com.aliyun.dingtalkproject_1_0.models.CreatePlanTimeRequest()
                .setTenantType("organization")
                .setExecutorId("user002")
                .setObjectId("63186xxxxx")
                .setObjectType("task")
                .setIsDuration(true)
                .setIncludesHolidays(true)
                .setSubmitterId("123456")
                .setStartDate("2022-09-05")
                .setEndDate("2022-09-05")
                .setPlanTime(3600000L);
        try {
            client.createPlanTimeWithOptions("user001", createPlanTimeRequest, createPlanTimeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.project_1_0.client import Client as dingtalkproject_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.project_1_0 import models as dingtalkproject__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkproject_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkproject_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_plan_time_headers = dingtalkproject__1__0_models.CreatePlanTimeHeaders()
        create_plan_time_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_plan_time_request = dingtalkproject__1__0_models.CreatePlanTimeRequest(
            tenant_type='organization',
            executor_id='user002',
            object_id='63186xxxxx',
            object_type='task',
            is_duration=True,
            includes_holidays=True,
            submitter_id='123456',
            start_date='2022-09-05',
            end_date='2022-09-05',
            plan_time=3600000
        )
        try:
            client.create_plan_time_with_options('user001', create_plan_time_request, create_plan_time_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_plan_time_headers = dingtalkproject__1__0_models.CreatePlanTimeHeaders()
        create_plan_time_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_plan_time_request = dingtalkproject__1__0_models.CreatePlanTimeRequest(
            tenant_type='organization',
            executor_id='user002',
            object_id='63186xxxxx',
            object_type='task',
            is_duration=True,
            includes_holidays=True,
            submitter_id='123456',
            start_date='2022-09-05',
            end_date='2022-09-05',
            plan_time=3600000
        )
        try:
            await client.create_plan_time_with_options_async('user001', create_plan_time_request, create_plan_time_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreatePlanTimeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreatePlanTimeRequest;
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
        $createPlanTimeHeaders = new CreatePlanTimeHeaders([]);
        $createPlanTimeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createPlanTimeRequest = new CreatePlanTimeRequest([
            "tenantType" => "organization",
            "executorId" => "user002",
            "objectId" => "63186xxxxx",
            "objectType" => "task",
            "isDuration" => true,
            "includesHolidays" => true,
            "submitterId" => "123456",
            "startDate" => "2022-09-05",
            "endDate" => "2022-09-05",
            "planTime" => 3600000
        ]);
        try {
            $client->createPlanTimeWithOptions("user001", $createPlanTimeRequest, $createPlanTimeHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkproject_1_0  "github.com/alibabacloud-go/dingtalk/project_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkproject_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkproject_1_0.Client{}
  _result, _err = dingtalkproject_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createPlanTimeHeaders := &dingtalkproject_1_0.CreatePlanTimeHeaders{}
  createPlanTimeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createPlanTimeRequest := &dingtalkproject_1_0.CreatePlanTimeRequest{
    TenantType: tea.String("organization"),
    ExecutorId: tea.String("user002"),
    ObjectId: tea.String("63186xxxxx"),
    ObjectType: tea.String("task"),
    IsDuration: tea.Bool(true),
    IncludesHolidays: tea.Bool(true),
    SubmitterId: tea.String("123456"),
    StartDate: tea.String("2022-09-05"),
    EndDate: tea.String("2022-09-05"),
    PlanTime: tea.Int64(3600000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreatePlanTimeWithOptions(tea.String("user001"), createPlanTimeRequest, createPlanTimeHeaders, &util.RuntimeOptions{})
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
import dingtalkproject_1_0, * as $dingtalkproject_1_0 from '@alicloud/dingtalk/project_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkproject_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkproject_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createPlanTimeHeaders = new $dingtalkproject_1_0.CreatePlanTimeHeaders({ });
    createPlanTimeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createPlanTimeRequest = new $dingtalkproject_1_0.CreatePlanTimeRequest({
      tenantType: "organization",
      executorId: "user002",
      objectId: "63186xxxxx",
      objectType: "task",
      isDuration: true,
      includesHolidays: true,
      submitterId: "123456",
      startDate: "2022-09-05",
      endDate: "2022-09-05",
      planTime: 3600000,
    });
    try {
      await client.createPlanTimeWithOptions("user001", createPlanTimeRequest, createPlanTimeHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkproject_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkproject_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkproject_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreatePlanTimeHeaders createPlanTimeHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreatePlanTimeHeaders();
            createPlanTimeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreatePlanTimeRequest createPlanTimeRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreatePlanTimeRequest
            {
                TenantType = "organization",
                ExecutorId = "user002",
                ObjectId = "63186xxxxx",
                ObjectType = "task",
                IsDuration = true,
                IncludesHolidays = true,
                SubmitterId = "123456",
                StartDate = "2022-09-05",
                EndDate = "2022-09-05",
                PlanTime = 3600000,
            };
            try
            {
                client.CreatePlanTimeWithOptions("user001", createPlanTimeRequest, createPlanTimeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| ok | Boolean | 是否成功。 |
| message | String | 执行结果描述。 |
| body | Array | 返回体。 |
| objectId | String | 工时关联的任务ID。 |
| date | String | 新增的计划工时所属日期，iso8601格式，例如：2022-07-29T14:55Z。 |
| planTime | Long | 对应日期内已累计的计划工时时长，单位毫秒。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "ok" : true,
    "message" : "创建工时成功",
    "body" : [ {
      "objectId" : "63186e54e07f18003fea6b90",
      "date" : "2022-09-05T00:00:00.000Z",
      "planTime" : 360000
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user.not.exist | 用户在当前企业中不存在 |
| 400 | org.not.exist | org.not.exist | 当前企业在Teambition中不存在 |
| 500 | server.error | server.error | 系统内部服务错误 |
